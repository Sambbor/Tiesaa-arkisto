#!/usr/bin/env python3
"""Naapuriurakat samana yönä (nu1, 25.10.2026, Samuli: idea 5).

Kelisivun Viime yö -osio näyttää, mitä viereiset hoitourakat tekivät samana yönä (klo 18–08 Suomen aikaa)
ja mittasivatko niiden tiesääasemat liukasta. Lähteet: tämän arkiston asemarivit (obs) ja talvihoidon toteumat
(toteumat.py: suolaus/auraus/hiekoitus 2 km säteellä asemasta). Urakka = aseman contractAreaCode (meta/stations.json).
Tulos: data/naapurit.json (kuluva tai viimeisin yö) ja valmiista öistä naapurit/YYYY-MM-DD.json.
Varaus: toteuma lasketaan urakalle, jos kone kulki 2 km päässä sen asemasta – urakkarajan lähellä naapurin kone voi osua.
"""
import csv, gzip, io, json, os, urllib.request
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from arkisto import current_parts, read_current

VERSION = 'nu1'
HEL = ZoneInfo('Europe/Helsinki')
RAW = 'https://raw.githubusercontent.com/Sambbor/Tiesaa-arkisto/main/'
# Urakkanimet koodeittain (Digitrafficin contractArea-nimi on osalla asemista väärä, esim. 301 = "Jyväskylä")
NAMES = {301: 'Vantaa', 283: 'Espoo', 288: 'Hyvinkää', 360: 'Porvoo', 342: 'Mäntsälä',
         333: 'Salo', 282: 'E18 Muurla–Lohja', 349: 'Paimio', 344: 'Nummi', 336: 'Lieto', 279: 'Raasepori'}
# Samuli 25.10.: Espoo 19–24 (142) on vanha urakka → pois; Saloon Raasepori (279)
GROUPS = {'vantaa': [301, 283, 288, 342, 360], 'salo': [333, 282, 279, 349, 344, 336]}
SLIP_KELI = {5, 6, 7, 9}
# Samuli 25.10.: vanhan Espoo 19–24 -urakan (142) asemat kuuluvat nykyiseen Espoon urakkaan (283); Digitraffic käyttää yhä vanhaa koodia
ALIAS = {142: 283}


def f(v):
    try:
        x = float(v); return x if x == x else None
    except Exception:
        return None


def read_day(kind, day):
    if current_parts('%s-%s' % (kind, day)):   # ta3: päivän palat
        return read_current('%s-%s' % (kind, day))
    a = 'archive/%s/%s-%s.csv.gz' % (day[:7], kind, day)
    try:
        if os.path.exists(a):
            b = open(a, 'rb').read()
        else:
            req = urllib.request.Request(RAW + a, headers={'User-Agent': 'tiesaa-arkisto/1'})
            with urllib.request.urlopen(req, timeout=60) as r:
                b = r.read()
        return list(csv.DictReader(io.StringIO(gzip.decompress(b).decode('utf-8'))))
    except Exception:
        return []


def ts(s):
    try:
        return datetime.fromisoformat(str(s).replace('Z', '+00:00'))
    except Exception:
        return None


def slippery(r):
    tr, keli, warn = f(r.get('tr1')), f(r.get('keli1')), f(r.get('warn1'))
    fric = [x for x in (f(r.get('fric1')), f(r.get('fric2'))) if x is not None]
    ice, snow = f(r.get('ice1')) or 0, f(r.get('snow1')) or 0
    if keli is not None and int(keli) in SLIP_KELI: return True
    if warn == 2: return True
    return (tr is None or tr <= 1) and ((fric and min(fric) < 0.45) or ice >= 0.1 or snow > 0.2)


def plaus(tr, ta):
    return tr is not None and -45 < tr < 65 and not (ta is not None and tr < ta - 10)


def runs(times):
    """Kirjaukset ajokerroiksi: yli 30 min tauko = uusi kerta (sama kuin kelisivun yöyhteenveto)."""
    if not times: return {'n': 0}
    s = sorted(times); n = 1
    for a, b in zip(s, s[1:]):
        if (b - a).total_seconds() > 1800: n += 1
    z = lambda t: t.strftime('%Y-%m-%dT%H:%M:%SZ')
    return {'n': n, 'first': z(s[0]), 'last': z(s[-1])}


def night_window(now):
    loc = now.astimezone(HEL)
    ev = (loc - timedelta(days=1)).date() if loc.hour < 18 else loc.date()
    fr = datetime(ev.year, ev.month, ev.day, 18, tzinfo=HEL)
    nx = ev + timedelta(days=1)
    to = datetime(nx.year, nx.month, nx.day, 8, tzinfo=HEL)
    return ev.isoformat(), fr.astimezone(timezone.utc), to.astimezone(timezone.utc)


def summarize(now):
    night, fr, to = night_window(now)
    days = sorted({fr.date().isoformat(), min(to, now).date().isoformat()})
    meta = json.load(open('meta/stations.json', encoding='utf-8'))
    code = {str(k): ALIAS.get(v.get('area_code'), v.get('area_code')) for k, v in meta.items()}
    want = {c for g in GROUPS.values() for c in g}
    A = {c: {'code': c, 'name': NAMES.get(c, str(c)), 'st': set(), 'slipSt': set(), 'slipFirst': None, 'frostSt': set(), 'trMin': None,
             'trMinSt': None, 'w': {'salt': {}, 'plow': {}, 'sand': {}}} for c in want}
    for d in days:
        for r in read_day('obs', d):
            c = code.get(r.get('st'))
            if c not in want: continue
            t = ts(r.get('t'))
            if not t or t < fr or t > to: continue
            a = A[c]; a['st'].add(r['st'])
            tr, ta, td = f(r.get('tr1')), f(r.get('ta')), f(r.get('td'))
            if plaus(tr, ta):
                if a['trMin'] is None or tr < a['trMin']: a['trMin'], a['trMinSt'] = tr, r['st']
                if td is not None and tr <= 1 and tr < td: a['frostSt'].add(r['st'])
            if slippery(r):
                a['slipSt'].add(r['st'])
                if a['slipFirst'] is None or t < a['slipFirst']: a['slipFirst'] = t
        for r in read_day('toteumat', d):
            c = code.get(r.get('st'))
            if c not in want or r.get('task') not in ('salt', 'plow', 'sand'): continue
            e = ts(r.get('end'))
            if not e or e < fr or e > to: continue
            A[c]['w'][r['task']][r.get('rid') or (r.get('start'), r.get('end'))] = e   # sama kirjaus monen aseman lähellä kerran
    out = {}
    for g, codes in GROUPS.items():
        L = []
        for c in codes:
            a = A[c]
            if not a['st']: continue
            L.append({'code': c, 'name': a['name'], 'home': c == codes[0], 'stations': len(a['st']), 'slip': len(a['slipSt']),
                      'slipFirst': a['slipFirst'].strftime('%Y-%m-%dT%H:%M:%SZ') if a['slipFirst'] else None,
                      'frost': len(a['frostSt']), 'trMin': None if a['trMin'] is None else round(a['trMin'], 1),
                      'trMinName': (meta.get(a['trMinSt']) or {}).get('name') if a['trMinSt'] else None,
                      'salt': runs(list(a['w']['salt'].values())), 'plow': runs(list(a['w']['plow'].values())), 'sand': runs(list(a['w']['sand'].values()))})
        out[g] = L
    z = lambda t: t.strftime('%Y-%m-%dT%H:%M:%SZ')
    return {'v': VERSION, 'night': night, 'from': z(fr), 'to': z(to), 'complete': now >= to, 'updated': z(now), 'groups': out,
            'note': 'Toteumat: suolaus/auraus/hiekoitus 2 km päässä urakan tiesääasemasta (rajan lähellä naapurin kone voi osua). Liukas = keli kuura/lumi/jää/sohjo, hälytys tai tie ≤ +1 °C ja kitka < 0,45, jäätä tai lunta.'}


def main():
    now = datetime.now(timezone.utc)
    N = summarize(now)
    os.makedirs('data', exist_ok=True)
    json.dump(N, open('data/naapurit.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    if N['complete']:
        os.makedirs('naapurit', exist_ok=True)
        json.dump(N, open('naapurit/%s.json' % N['night'], 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('Naapuriurakat yö %s: %s' % (N['night'], ', '.join('%s %d as./%d liukas/suolaus %d' % (x['name'], x['stations'], x['slip'], x['salt']['n']) for x in N['groups']['vantaa'])))


if __name__ == '__main__':
    main()
