#!/usr/bin/env python3
"""Koko maan kuura-aamujen kamerakuvat (ku2, 25.10.2026, Samuli: idea 7).

Kuuraöiden jälkeen tallennetaan niiden kelikameroiden kuvat, joiden vieressä (≤ PAIR_M) on tiesääasema:
  A = viimeinen kuva ennen klo 06 (paikallista aikaa; kuura ei vielä ehtinyt sulaa)
  B = ensimmäinen valoisa kuva (aurinko ≥ SUN_MIN° kameran kohdalla)
Kuuraehto lasketaan aseman yön havainnoista (klo 18–06): tienpinta ≤ +1 °C ja tienpinta alle kastepisteen
(ehto 'kuura') tai enintään 1 °C sen yläpuolella (ehto 'raja', vertailuksi rajatapauksista).
Kuvat: kuura/kuvat/YYYY-MM/DD/<preset>_<A|B>.jpg (≈ 400 px), tiedot: kuura/data/kuura-YYYY-MM.csv.
Merkinnät (kuura_tie / kuura_reuna / ei / epävarma / ei_nay) tehdään erikseen (aamuanalyysi), sarake 'luokka' jää tyhjäksi.
"""
import csv, gzip, io, json, math, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from arkisto import current_parts, read_current

VERSION = 'ku2'
DT = 'https://tie.digitraffic.fi'
RAW = 'https://raw.githubusercontent.com/Sambbor/Tiesaa-arkisto/main/'
HDR = {'Digitraffic-User': 'Vantaa-urakka-tiesaa-arkisto', 'User-Agent': 'tiesaa-arkisto/1', 'Accept-Encoding': 'gzip'}
HEL = ZoneInfo('Europe/Helsinki')
PAIR_M = 300            # kamera ja asema enintään näin kaukana toisistaan
CAMS_REFRESH_D = 7
SUN_MIN = 2.0
A_FROM, A_TO = 4.75, 6.0   # A-kuva otetaan, kun paikallinen kello on välillä 04.45–06.00 (viimeisin ajo voittaa)
B_LAST_H = 12              # valoisaa kuvaa ei enää haeta klo 12 jälkeen
TR_MAX = 1.0
TR_MIN = -6.0             # kovilla pakkasilla tie on yleensä muutenkin luminen/jäinen: ei kuvata (säästää tilaa)
RAJA = 1.0
IMG_W = 400
META = 'kuura/meta'
COLS = ['pvm', 'vaihe', 'kuva_aika', 'st', 'asema', 'cam', 'preset', 'suunta', 'tie', 'maakunta', 'dist_m', 'aurinko',
        'tr', 'td', 'ta', 'tf', 'keli', 'varoitus', 'yo_tr_min', 'yo_ero_min', 'kuura_h', 'ehto', 'tiedosto', 'luokka', 'v']


def get(url, timeout=60, raw=False):
    req = urllib.request.Request(url if url.startswith('http') else DT + url, headers=HDR)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        b = r.read(); h = dict(r.headers)
    if h.get('Content-Encoding', '').lower() == 'gzip' and not raw:
        b = gzip.decompress(b)
    return (b, h) if raw else json.loads(b)


def load(p, d):
    try:
        with open(p, encoding='utf-8') as f: return json.load(f)
    except Exception: return d


def save(p, o):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p + '.tmp', 'w', encoding='utf-8') as f: json.dump(o, f, ensure_ascii=False, indent=1)
    os.replace(p + '.tmp', p)


def dist(a, b):
    k = math.cos(math.radians((a[1] + b[1]) / 2))
    return math.hypot((a[0] - b[0]) * 111320 * k, (a[1] - b[1]) * 111320)


def sun_elev(t, lat, lon):
    n = t / 86400.0 + 2440587.5 - 2451545.0
    L = (280.460 + 0.9856474 * n) % 360
    g = math.radians((357.528 + 0.9856003 * n) % 360)
    lam = math.radians(L + 1.915 * math.sin(g) + 0.020 * math.sin(2 * g))
    eps = math.radians(23.439 - 0.0000004 * n)
    dec = math.asin(math.sin(eps) * math.sin(lam))
    ra = math.degrees(math.atan2(math.cos(eps) * math.sin(lam), math.cos(lam)))
    gmst = (18.697374558 + 24.06570982441908 * n) % 24
    ha = math.radians(gmst * 15 + lon - ra)
    la = math.radians(lat)
    return round(math.degrees(math.asin(math.sin(la) * math.sin(dec) + math.cos(la) * math.cos(dec) * math.cos(ha))), 1)


def cams():
    """Kamera–asema-parit koko maasta (välimuisti viikko). Yksi esiasento kameraa kohden: ensimmäinen keräyksessä oleva."""
    c = load(META + '/cams.json', None)
    if c and c.get('v') == VERSION and time.time() - c.get('t', 0) < CAMS_REFRESH_D * 86400:
        return c['cams']
    ws = {f['id']: f['geometry']['coordinates'][:2] for f in get('/api/weather/v1/stations')['features']}
    feats = [f for f in get('/api/weathercam/v1/stations')['features'] if f['properties'].get('collectionStatus') == 'GATHERING']

    def one(f):
        try:
            d = get('/api/weathercam/v1/stations/' + f['id'])
        except Exception:
            return None
        p0 = d['properties']; x, y = d['geometry']['coordinates'][:2]
        sid = p0.get('nearestWeatherStationId')
        if sid not in ws:
            return None
        dm = round(dist(ws[sid], (x, y)))
        if dm > PAIR_M:
            return None
        pr = [p for p in p0.get('presets', []) if p.get('inCollection', True)]
        if not pr:
            return None
        p = sorted(pr, key=lambda q: q['id'])[0]
        ra = p0.get('roadAddress') or {}
        return {'cam': d['id'], 'preset': p['id'], 'dir': p.get('presentationName') or '', 'st': sid, 'dist_m': dm,
                'road': ra.get('roadNumber'), 'lon': x, 'lat': y,
                'url': p.get('imageUrl') or ('https://weathercam.digitraffic.fi/' + p['id'] + '.jpg')}
    with ThreadPoolExecutor(6) as ex:
        out = [r for r in ex.map(one, feats) if r]
    print('kameroita keräyksessä', len(feats), '– pareja asemaan ≤', PAIR_M, 'm:', len(out))
    if len(out) < 10 and c:
        return c['cams']   # rajapintahäiriö: pidetään vanha lista
    save(META + '/cams.json', {'t': time.time(), 'v': VERSION, 'cams': out})
    return out


def obs_rows(day):
    """Aseman havaintorivit UTC-päivältä: data/current tai arkisto (paikallinen tai githubista)."""
    if current_parts('obs-%s' % day):   # ta3: päivän palat
        return read_current('obs-%s' % day)
    a = 'archive/%s/obs-%s.csv.gz' % (day[:7], day)
    try:
        b = open(a, 'rb').read() if os.path.exists(a) else get(RAW + a, raw=True)[0]
        return list(csv.DictReader(io.StringIO(gzip.decompress(b).decode('utf-8'))))
    except Exception as e:
        print('ei havaintoja', day, e); return []


def f(v):
    try: return float(v)
    except Exception: return None


def night_stats(now_utc, local_day):
    """Asemittain yön (edellinen ilta 18 – klo 06 paikallista) tienpinta ja ero kastepisteeseen + viimeisin havainto."""
    t0 = datetime(local_day.year, local_day.month, local_day.day, 18, tzinfo=HEL) - timedelta(days=1)
    t1 = datetime(local_day.year, local_day.month, local_day.day, 6, tzinfo=HEL)
    days = sorted({t0.astimezone(timezone.utc).date().isoformat(), now_utc.date().isoformat()})
    S = {}
    for d in days:
        for r in obs_rows(d):
            try:
                t = datetime.fromisoformat(r['t'].replace('Z', '+00:00'))
            except Exception:
                continue
            st = r.get('st'); tr, td = f(r.get('tr1')), f(r.get('td'))
            o = S.setdefault(st, {'trmin': None, 'eromin': None, 'kh': 0.0, 'last': None, 'lt': None})
            if t0 <= t <= t1 and tr is not None:
                o['trmin'] = tr if o['trmin'] is None else min(o['trmin'], tr)
                if td is not None:
                    e = tr - td
                    o['eromin'] = e if o['eromin'] is None else min(o['eromin'], e)
                    if tr <= TR_MAX and e < 0: o['kh'] += 0.5   # arkisto tallentaa 30 min välein
            if t <= now_utc and (o['lt'] is None or t > o['lt']):
                o['lt'] = t; o['last'] = r
    for o in S.values():
        e = o['eromin']
        o['ehto'] = None if o['trmin'] is None or e is None or o['trmin'] > TR_MAX or o['trmin'] < TR_MIN else 'kuura' if e < 0 else 'raja' if e <= RAJA else None
    return S


def shrink(b):
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(b)).convert('RGB')
        if im.width > IMG_W:
            im = im.resize((IMG_W, round(im.height * IMG_W / im.width)), Image.LANCZOS)
        o = io.BytesIO(); im.save(o, 'JPEG', quality=72, optimize=True); return o.getvalue()
    except ImportError:
        return b


def main():
    now = datetime.now(timezone.utc)
    loc = now.astimezone(HEL); lh = loc.hour + loc.minute / 60
    test = '--test' in sys.argv   # testiajo: muutama kuva kuuraehdosta riippumatta /tmp-kansioon, ei tallennusta
    force = test
    if not force and not (A_FROM <= lh < B_LAST_H):
        print('ei kuvausaikaa', loc.isoformat()); return
    day = loc.date(); ds = day.isoformat()
    state = load(META + '/state.json', {})
    if state.get('day') != ds:
        state = {'day': ds, 'A': {}, 'B': []}
    C = cams()
    S = night_stats(now, day)
    meta = load('meta/stations.json', {})
    phaseA = force or A_FROM <= lh < A_TO
    todo = []
    for c in C:
        o = S.get(str(c['st']))
        if not o or (not o['ehto'] and not test):
            continue
        sun = sun_elev(now.timestamp(), c['lat'], c['lon'])
        if test or (phaseA and sun < SUN_MIN):
            todo.append((c, o, 'A', sun))
        elif not phaseA and sun >= SUN_MIN and c['preset'] not in state['B']:
            todo.append((c, o, 'B', sun))
    if test:
        todo = todo[:5]
    print(loc.strftime('%d.%m. %H.%M'), 'pareja', len(C), '– kuura/raja-asemia', sum(1 for o in S.values() if o['ehto']), '– kuvattavia', len(todo))

    def shoot(job):
        c, o, ph, sun = job
        try:
            b, h = get(c['url'], timeout=30, raw=True)
        except Exception as e:
            return None
        lm = h.get('Last-Modified')
        try:
            it = datetime.strptime(lm, '%a, %d %b %Y %H:%M:%S %Z').replace(tzinfo=timezone.utc) if lm else now
        except Exception:
            it = now
        if (now - it).total_seconds() > 3 * 3600:
            return None   # kamera ei päivity
        fn = ('/tmp/kuura-testi/' if test else 'kuura/kuvat/%s/%s/' % (ds[:7], ds[8:])) + '%s_%s.jpg' % (c['preset'], ph)
        os.makedirs(os.path.dirname(fn), exist_ok=True)
        open(fn, 'wb').write(shrink(b))
        r = o['last'] or {}; m = meta.get(str(c['st']), {})
        return {'pvm': ds, 'vaihe': ph, 'kuva_aika': it.astimezone(HEL).strftime('%Y-%m-%dT%H:%M'), 'st': c['st'],
                'asema': m.get('name', ''), 'cam': c['cam'], 'preset': c['preset'], 'suunta': c['dir'], 'tie': c.get('road') or m.get('road', ''),
                'maakunta': m.get('prov', ''), 'dist_m': c['dist_m'], 'aurinko': sun,
                'tr': r.get('tr1', ''), 'td': r.get('td', ''), 'ta': r.get('ta', ''), 'tf': r.get('tf1', ''), 'keli': r.get('keli1', ''),
                'varoitus': r.get('warn1', ''), 'yo_tr_min': None if o['trmin'] is None else round(o['trmin'], 1), 'yo_ero_min': None if o['eromin'] is None else round(o['eromin'], 1), 'kuura_h': o['kh'],
                'ehto': o['ehto'], 'tiedosto': fn, 'luokka': '', 'v': VERSION}
    with ThreadPoolExecutor(6) as ex:
        res = [r for r in ex.map(shoot, todo) if r]
    if test:
        for r in res: print('testi', r['preset'], r['asema'], r['dist_m'], 'm', r['kuva_aika'], os.path.getsize(r['tiedosto']), 't')
        return
    if not res:
        save(META + '/state.json', state); return
    # CSV: A-kuva korvataan myöhemmällä (lähempänä klo 06), B-kuva lisätään kerran
    p = 'kuura/data/kuura-%s.csv' % ds[:7]; os.makedirs('kuura/data', exist_ok=True)
    old = list(csv.DictReader(open(p, encoding='utf-8'))) if os.path.exists(p) else []
    new = {(r['pvm'], r['vaihe'], r['preset']) for r in res}
    keep = [r for r in old if (r['pvm'], r['vaihe'], r['preset']) not in new]
    with open(p, 'w', encoding='utf-8', newline='') as fo:
        w = csv.DictWriter(fo, COLS, extrasaction='ignore'); w.writeheader(); w.writerows(keep + res)
    for r in res:
        if r['vaihe'] == 'A': state['A'][r['preset']] = r['kuva_aika']
        else: state['B'].append(r['preset'])
    save(META + '/state.json', state)
    print('tallennettu', len(res), 'kuvaa:', sum(r['vaihe'] == 'A' for r in res), 'A,', sum(r['vaihe'] == 'B' for r in res), 'B')


if __name__ == '__main__':
    main()
