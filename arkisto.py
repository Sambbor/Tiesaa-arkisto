#!/usr/bin/env python3
"""Tiesää-arkisto – koko Suomen tiesääasemien mittaukset ja tiesääennusteet talteen liukkausmallin opettamista varten.

Ajetaan GitHub Actionsissa 30 min välein (säilö Sambbor/Tiesaa-arkisto).
- Kaikki keräävät asemat (noin 525): tienpinta, ilma, kastepiste, kuurapiste, keli, varoitus, jäätymispiste, suola,
  vesi/lumi/jää, kitka, sade, näkyvyys, tuuli (stations/data, yksi haku koko maasta).
- Jokaiselle asemalle lähimmän tiesääennusteen tiekohdan ennuste nyt ja +2/4/6/12 h (forecast-sections/forecasts, yksi haku).
- Vain uudet mittaukset tallennetaan (asema, jonka mittausaika ei ole muuttunut, ohitetaan). Yli 2 h vanhat anturilukemat ohitetaan.
- Päivän rivit: data/current/obs-YYYY-MM-DD.csv (UTC-päivä). Edelliset päivät pakataan archive/YYYY-MM/obs-YYYY-MM-DD.csv.gz.
- Asemien tiedot (tie, tieosa, urakka, kunta, maakunta) meta/stations.json, asema → ennusteen tiekohta meta/pairs.json.
- Ilmatieteen laitos (ta2): toimitettu ennuste jokaiselle tiesääasemalle 3 h välein, tunneittain 0–24 h
  (data/current/fmi-fc-YYYY-MM-DD.csv) – samat suureet, joita kelisivun liukkausennuste käyttää.
- Ilmatieteen laitoksen säähavainnot kerran tunnissa (data/current/fmi-obs-YYYY-MM-DD.csv): pilvisyys, lumensyvyys,
  sade, näkyvyys, sää ja säteilyasemilta auringon- ja pitkäaaltosäteily. Havaintoasemat meta/fmi_stations.json.
Data: Fintraffic / Digitraffic ja Ilmatieteen laitos, CC BY 4.0. Vain Pythonin vakiokirjasto.
"""
import gzip, json, math, os, re, time, urllib.request
from datetime import datetime, timezone

VERSION = 'ta2'
DT = 'https://tie.digitraffic.fi'
HDR = {'Digitraffic-User': 'Vantaa-urakka-tiesaa-arkisto', 'User-Agent': 'tiesaa-arkisto/1', 'Accept-Encoding': 'gzip'}
STALE_H = 2
PAIR_MAX_M = 1000           # ennustekohta enintään näin kaukana asemasta
PAIR_REFRESH_D = 30
META_REFRESH_D = 60
META_PER_RUN = 150          # asemien perustietoja haetaan erissä

# Anturi → sarake
SENS = [('ILMA', 'ta'), ('KASTEPISTE', 'td'), ('ILMAN_KOSTEUS', 'rh'), ('KUURAPISTE', 'fp'),
        ('TIE_1', 'tr1'), ('TIE_2', 'tr2'), ('MAA_1', 'tg1'), ('TURVALLISUUSLÄMPÖ_1', 'safe1'),
        ('KELI_1', 'keli1'), ('KELI_2', 'keli2'), ('OPTISEN_ANTURIN_KELI1', 'okeli1'), ('TIENPINNAN_TILA_1', 'surf1'),
        ('VAROITUS_1', 'warn1'), ('VAROITUS_2', 'warn2'),
        ('JÄÄTYMISPISTE_1', 'tf1'), ('JÄÄTYMISPISTE_2', 'tf2'), ('SUOLAN_MÄÄRÄ_1', 'salt1'), ('SUOLAN_VÄKEVYYS_1', 'saltc1'),
        ('KOSTEUDEN_MÄÄRÄ_1', 'moist1'), ('VEDEN_MÄÄRÄ1', 'water1'), ('LUMEN_MÄÄRÄ1', 'snow1'), ('JÄÄN_MÄÄRÄ1', 'ice1'),
        ('KITKA1_LUKU', 'fric1'), ('KITKA2_LUKU', 'fric2'),
        ('SADE', 'rain'), ('SADE_INTENSITEETTI', 'rain_i'), ('SATEEN_OLOMUOTO_PWDXX', 'rain_form'),
        ('SADESUMMA_LIUKUVA_24H', 'rain24'), ('VALLITSEVA_SÄÄ', 'wx'), ('NÄKYVYYS_KM', 'vis'),
        ('KESKITUULI', 'ws'), ('MAKSIMITUULI', 'wg'), ('TUULENSUUNTA', 'wd'), ('VALOISAA', 'light')]
SENS_MAP = dict(SENS)
# Ennuste: nykyhetken mallitila (OBSERVATION) ja ennusteet
FC_OBS = ['tr', 'ta', 'ov', 'rc', 'rel']
FC_H = [('2h', 'f2'), ('4h', 'f4'), ('6h', 'f6'), ('12h', 'f12')]
FC_F = ['tr', 'ta', 'ws', 'sym', 'ov', 'rc', 'pc', 'fc', 'fz', 'sl']
COLS = ['t', 'st', 'mt'] + [c for _, c in SENS] + ['sec', 'sec_d'] + ['fo_' + k for k in FC_OBS] \
    + [p + '_' + k for _, p in FC_H for k in FC_F] + ['v']

M_LAT = 111320.0

# Ilmatieteen laitos
FMI = 'https://opendata.fmi.fi/wfs?service=WFS&version=2.0.0&request=getFeature&storedquery_id='
FMI_BBOX = '19,59.5,32,70.2'
FMI_FC_EVERY_MIN = 170          # ennuste noin 3 h välein
FMI_OBS_EVERY_MIN = 50          # havainnot kerran tunnissa
FMI_FC_CHUNK = 90               # rajapinta sallii enintään 99 pistettä kyselyssä
FC_PARAMS = [('Temperature', 't'), ('DewPoint', 'td'), ('Precipitation1h', 'p'), ('WeatherSymbol3', 'sym'),
             ('TotalCloudCover', 'cc'), ('WindSpeedMS', 'ws')]
FC_LEADS = range(0, 25)
FMI_FC_COLS = ['t', 'st', 'h0'] + ['%s%02d' % (c, L) for _, c in FC_PARAMS for L in FC_LEADS] + ['v']
OBS_W = [('t2m', 'ta'), ('td', 'td'), ('rh', 'rh'), ('ws_10min', 'ws'), ('wg_10min', 'wg'), ('wd_10min', 'wd'),
         ('n_man', 'cc'), ('snow_aws', 'snow'), ('r_1h', 'r1h'), ('ri_10min', 'ri'), ('vis', 'vis'), ('wawa', 'wawa')]
OBS_R = [('GLOB_1MIN', 'glob'), ('LWIN_1MIN', 'lwin'), ('LWOUT_1MIN', 'lwout'), ('DIR_1MIN', 'dir'), ('DIFF_1MIN', 'diff')]
# bl1 (21.10.2026): säämallien ennusteet samoille asemille ja samalla rytmillä mallien yhdistelmän opettamiseen.
# ECMWF:n kastepiste lasketaan mallin suhteellisesta kosteudesta (FMI:n palvelu ei anna sitä); ECMWF:n pilvisyys ja tuuli puuttuvat palvelusta.
# bl2 (21.10.2026): MEPSistä lisäksi auringon kokonaissäteily (rg, W/m²), alas tuleva pitkäaaltosäteily (rlw, W/m²) ja maanpinnan
# lämpötila (tg) – selkeän yön jäähtyminen tienpintamallille. ECMWF:ltä niitä ei saa FMI:n palvelusta (tyhjiä).
MODEL_PARAMS = [('Temperature', 't'), ('DewPoint', 'td'), ('Precipitation1h', 'p'), ('TotalCloudCover', 'cc'), ('WindSpeedMS', 'ws'),
                ('RadiationGlobal', 'rg'), ('RadiationLW', 'rlw'), ('GroundTemperature', 'tg')]
MODEL_FC_COLS = ['t', 'st', 'h0'] + ['%s%02d' % (c, L) for _, c in MODEL_PARAMS for L in FC_LEADS] + ['v']
MODELS = [('meps', 'fmi::forecast::meps::surface::point::multipointcoverage', 'Temperature,DewPoint,Precipitation1h,TotalCloudCover,WindSpeedMS,RadiationGlobal,RadiationLW,GroundTemperature'),
          ('ec', 'ecmwf::forecast::surface::point::multipointcoverage', 'Temperature,Humidity,Precipitation1h')]
FMI_OBS_COLS = ['t', 'fmisid', 'ot'] + [c for _, c in OBS_W] + ['rt'] + [c for _, c in OBS_R] + ['v']


def get(path, timeout=90):
    req = urllib.request.Request(DT + path, headers=HDR)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        b = r.read()
        if r.headers.get('Content-Encoding', '').lower() == 'gzip' or b[:2] == b'\x1f\x8b':
            b = gzip.decompress(b)
    return json.loads(b)


def fmi_get(q, timeout=90):
    req = urllib.request.Request(FMI + q, headers={'User-Agent': 'tiesaa-arkisto/1', 'Accept-Encoding': 'gzip'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        b = r.read()
        if b[:2] == b'\x1f\x8b':
            b = gzip.decompress(b)
    return b.decode('utf-8')


def ll_key(lat, lon):
    return '%.4f %.4f' % (float(lat), float(lon))


def parse_mpc(x):
    """FMI multipointcoverage: pisteet {sijainti: (id, nimi)} ja rivit [(sijainti, epoch, {suure: arvo})]."""
    pts = {}
    for m in re.finditer(r'<gml:Point gml:id="point-([^"]+)"[^>]*>\s*<gml:name>([^<]*)</gml:name>\s*<gml:pos>([^<]*)</gml:pos>', x):
        a = m.group(3).split()
        pts[ll_key(a[0], a[1])] = (m.group(1), m.group(2))
    fields = re.findall(r'<swe:field name="([^"]+)"', x)
    pm = re.search(r'<gmlcov:positions>([\s\S]*?)</gmlcov:positions>', x)
    dm = re.search(r'<gml:doubleOrNilReasonTupleList>([\s\S]*?)</gml:doubleOrNilReasonTupleList>', x)
    rows = []
    if pm and dm:
        pos = [l.split() for l in pm.group(1).strip().splitlines() if l.strip()]
        dat = [l.split() for l in dm.group(1).strip().splitlines() if l.strip()]
        for p, d in zip(pos, dat):
            rec = {}
            for f, v in zip(fields, d):
                rec[f] = None if v == 'NaN' else float(v)
            rows.append((ll_key(p[0], p[1]), int(p[2]), rec))
    return pts, rows


def num(v, nd=2):
    if v is None:
        return None
    r = round(v, nd)
    return int(r) if r == int(r) else r


def iso(t):
    return datetime.fromtimestamp(t, timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def parse_t(s):
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00')).timestamp() if s else None
    except Exception:
        return None


def load(path, default):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return default


def save(path, obj, indent=None):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
    os.replace(tmp, path)


def seg_dist(p, a, b, mlon):
    ax, ay = (a[0] - p[0]) * mlon, (a[1] - p[1]) * M_LAT
    bx, by = (b[0] - p[0]) * mlon, (b[1] - p[1]) * M_LAT
    dx, dy = bx - ax, by - ay
    l = dx * dx + dy * dy
    t = max(0.0, min(1.0, -(ax * dx + ay * dy) / l)) if l else 0.0
    return math.hypot(ax + t * dx, ay + t * dy)


def make_pairs(coords):
    """Asema → lähin tiesääennusteen tiekohta (forecast-sections). Raskas haku (~40 Mt), tehdään kerran kuukaudessa."""
    lines = []
    for f in get('/api/weather/v1/forecast-sections', timeout=180).get('features', []):
        g = f.get('geometry') or {}
        cs = g.get('coordinates') or []
        parts = cs if g.get('type') == 'MultiLineString' else [cs]
        for l in parts:
            if len(l) < 2:
                continue
            xs = [c[0] for c in l]; ys = [c[1] for c in l]
            lines.append((f['id'], min(xs), max(xs), min(ys), max(ys), [c[:2] for c in l]))
    out = {}
    for sid, (x, y) in coords.items():
        mlon = M_LAT * math.cos(math.radians(y))
        dx, dy = PAIR_MAX_M / mlon, PAIR_MAX_M / M_LAT
        best = None
        for fid, x0, x1, y0, y1, l in lines:
            if x < x0 - dx or x > x1 + dx or y < y0 - dy or y > y1 + dy:
                continue
            for i in range(len(l) - 1):
                d = seg_dist((x, y), l[i], l[i + 1], mlon)
                if best is None or d < best[1]:
                    best = (fid, d)
        if best and best[1] <= PAIR_MAX_M:
            out[sid] = [best[0], round(best[1])]
    return out


def fc_fields(f, keys):
    r = f.get('forecastConditionReason') or {}
    v = {'tr': f.get('roadTemperature'), 'ta': f.get('temperature'), 'ws': f.get('windSpeed'), 'sym': f.get('weatherSymbol'),
         'ov': f.get('overallRoadCondition'), 'rc': r.get('roadCondition'), 'pc': r.get('precipitationCondition'),
         'fc': r.get('frictionCondition'), 'fz': 1 if r.get('freezingRainCondition') else (0 if r else None),
         'sl': 1 if r.get('winterSlipperiness') else (0 if r else None), 'rel': f.get('reliability')}
    return {k: v[k] for k in keys}


def cell(v):
    if v is None:
        return ''
    if isinstance(v, bool):
        return '1' if v else '0'
    s = str(v)
    return '"' + s.replace('"', '""') + '"' if any(c in s for c in ',"\n') else s


def write_csv(path, cols, rows):
    new = not os.path.exists(path)
    if not new:   # sarakkeet muuttuneet kesken päivän (esim. bl2): kirjoitetaan tiedosto uudella otsikolla, puuttuvat tyhjiksi
        with open(path, encoding='utf-8') as f:
            head = f.readline().rstrip('\n').split(',')
        if head != cols:
            import csv
            with open(path, encoding='utf-8', newline='') as f:
                old = list(csv.DictReader(f))
            with open(path, 'w', encoding='utf-8') as f:
                f.write(','.join(cols) + '\n')
                for r in old:
                    f.write(','.join(cell(r.get(c) or None) for c in cols) + '\n')
    with open(path, 'a', encoding='utf-8') as f:
        if new:
            f.write(','.join(cols) + '\n')
        for r in rows:
            f.write(','.join(cell(r.get(c)) for c in cols) + '\n')


def dew_from_rh(t, rh):
    if t is None or rh is None or rh <= 0:
        return None
    g = math.log(min(rh, 100.0) / 100.0) + 17.62 * t / (243.12 + t)
    return 243.12 * g / (17.62 - g)


def collect_fmi_fc(coords, now, query='fmi::forecast::edited::weather::scandinavia::point::multipointcoverage', params=None):
    """Toimitettu ennuste (edited) tai säämalli (query, params) jokaiselle tiesääasemalle tunneittain 0–24 h. Pisteet 90 kpl erissä."""
    keys = {}
    for sid, (lon, lat) in coords.items():
        if not (59.0 <= lat <= 70.5 and 19.0 <= lon <= 32.0):   # Digitrafficissa on asemia virheellisin koordinaatein
            continue
        keys.setdefault(ll_key(lat, lon), []).append(sid)
    klist = sorted(keys)
    h0 = int(now // 3600 * 3600)
    res, errors, dropped = {}, 0, []

    def fetch(chunk):
        nonlocal errors
        q = query \
            + ''.join('&latlon=%s,%s' % tuple(k.split()) for k in chunk) \
            + '&parameters=' + (params or ','.join(p for p, _ in FC_PARAMS)) + '&timestep=60&starttime=' + iso(h0) + '&endtime=' + iso(h0 + 24 * 3600)
        try:
            _, rows = parse_mpc(fmi_get(q))
        except Exception as e:
            # yksikin piste, jolle ei ole dataa, kaataa koko kyselyn → puolitetaan ja pudotetaan ongelmapiste
            if len(chunk) > 1:
                time.sleep(1)
                h = len(chunk) // 2
                fetch(chunk[:h]); fetch(chunk[h:])
            else:
                dropped.append(chunk[0])
                errors += 1
            return
        for key, ep, rec in rows:
            L = int(round((ep - h0) / 3600))
            if L in FC_LEADS:
                for sid in keys.get(key, []):
                    res.setdefault(sid, {})[L] = rec
        time.sleep(1)

    for i in range(0, len(klist), FMI_FC_CHUNK):
        fetch(klist[i:i + FMI_FC_CHUNK])
    if dropped:
        print('%s: ei dataa pisteille %s' % (query.split('::')[0] + '/' + query.split('::')[2], ', '.join(dropped[:10])))
    out = []
    plist = MODEL_PARAMS if params else FC_PARAMS
    for sid in sorted(res, key=lambda s: int(s) if s.isdigit() else s):
        row = {'t': iso(now), 'st': sid, 'h0': iso(h0), 'v': VERSION}
        for L, rec in res[sid].items():
            if params and 'Humidity' in rec and rec.get('DewPoint') is None:
                rec = dict(rec, DewPoint=dew_from_rh(rec.get('Temperature'), rec.get('Humidity')))
            for p, c in plist:
                row['%s%02d' % (c, L)] = num(rec.get(p), 0 if c in ('rg', 'rlw') else 1 if c in ('t', 'td', 'ws', 'cc', 'tg') else 2)
        out.append(row)
    return out, errors


def collect_fmi_obs(now, last, fmeta):
    """Säähavainnot (koko maa) ja säteily: kunkin aseman uusin tunti viimeisen 3 h ajalta."""
    base = '&bbox=%s&starttime=%s&timestep=60' % (FMI_BBOX, iso(now - 3 * 3600))
    latest = {}
    pts, rows = parse_mpc(fmi_get('fmi::observations::weather::multipointcoverage' + base + '&parameters=' + ','.join(p for p, _ in OBS_W)))
    for key, ep, rec in rows:
        if key not in pts or all(v is None for v in rec.values()):
            continue
        fid, name = pts[key]
        if fid not in latest or ep > latest[fid][0]:
            latest[fid] = (ep, rec)
        if fid not in fmeta:
            lat, lon = key.split()
            fmeta[fid] = {'name': name, 'lat': float(lat), 'lon': float(lon)}
    rad = {}
    try:
        rpts, rrows = parse_mpc(fmi_get('fmi::observations::radiation::multipointcoverage' + base + '&parameters=' + ','.join(p for p, _ in OBS_R)))
        for key, ep, rec in rrows:
            if key not in rpts or all(v is None for v in rec.values()):
                continue
            fid, name = rpts[key]
            if fid not in rad or ep > rad[fid][0]:
                rad[fid] = (ep, rec)
            if fid not in fmeta:
                lat, lon = key.split()
                fmeta[fid] = {'name': name, 'lat': float(lat), 'lon': float(lon), 'rad': True}
            else:
                fmeta[fid]['rad'] = True
    except Exception as e:
        print('FMI-säteily:', e)
    out = []
    for fid in sorted(set(latest) | set(rad), key=lambda s: int(s) if s.isdigit() else s):
        ep = latest[fid][0] if fid in latest else None
        rep = rad[fid][0] if fid in rad else None
        if last.get(fid) == [ep, rep]:
            continue
        last[fid] = [ep, rep]
        row = {'t': iso(now), 'fmisid': fid, 'v': VERSION}
        if fid in latest:
            row['ot'] = iso(ep)
            for p, c in OBS_W:
                row[c] = num(latest[fid][1].get(p), 1)
        if fid in rad:
            row['rt'] = iso(rep)
            for p, c in OBS_R:
                row[c] = num(rad[fid][1].get(p), 1)
        out.append(row)
    return out


def compress_old(today):
    """Pakkaa edellisten päivien CSV:t arkistoon (archive/YYYY-MM/<nimi>-YYYY-MM-DD.csv.gz)."""
    n = 0
    d = 'data/current'
    if not os.path.isdir(d):
        return 0
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.csv') or len(fn) < 15 or fn[-15] != '-':
            continue
        day = fn[-14:-4]
        if day >= today:
            continue
        dst = 'archive/%s/%s.gz' % (day[:7], fn)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(os.path.join(d, fn), 'rb') as src, gzip.open(dst, 'wb', compresslevel=9) as out:
            out.write(src.read())
        os.remove(os.path.join(d, fn))
        n += 1
    return n


def main():
    t0 = time.time()
    now = t0
    today = datetime.fromtimestamp(now, timezone.utc).strftime('%Y-%m-%d')
    os.makedirs('meta', exist_ok=True)
    os.makedirs('data/current', exist_ok=True)
    meta = load('meta/stations.json', {})
    pairs = load('meta/pairs.json', {'t': 0, 'p': {}})
    state = load('meta/state.json', {})
    idx = load('meta/index.json', {'rows': 0, 'days': [], 'first': None})

    lst = get('/api/weather/v1/stations')
    coords = {str(f['id']): f['geometry']['coordinates'][:2] for f in lst.get('features', [])
              if (f.get('properties') or {}).get('collectionStatus') == 'GATHERING' and f.get('geometry')}

    # asemien perustiedot erissä
    todo = [i for i in coords if i not in meta or now - meta[i].get('t', 0) > META_REFRESH_D * 86400][:META_PER_RUN]
    for i in todo:
        try:
            p = get('/api/weather/v1/stations/' + i, timeout=30).get('properties', {})
        except Exception as e:
            print('asema %s: %s' % (i, e))
            continue
        ra = p.get('roadAddress') or {}
        meta[i] = {'name': (p.get('names') or {}).get('fi') or p.get('name'), 'lon': coords[i][0], 'lat': coords[i][1],
                   'road': ra.get('roadNumber'), 'sec': ra.get('roadSection'), 'dist': ra.get('distanceFromRoadSectionStart'),
                   'cw': ra.get('carriageway'), 'area': ra.get('contractArea'), 'area_code': ra.get('contractAreaCode'),
                   'mun': p.get('municipality'), 'prov': p.get('province'), 't': round(now)}
    if todo:
        save('meta/stations.json', meta, indent=0)

    # asema → ennusteen tiekohta
    if now - pairs.get('t', 0) > PAIR_REFRESH_D * 86400 or len(set(coords) - set(pairs.get('p', {})) - set(pairs.get('none', []))) > 20:
        try:
            p = make_pairs(coords)
            pairs = {'t': round(now), 'p': p, 'none': sorted(set(coords) - set(p))}
            save('meta/pairs.json', pairs, indent=0)
            print('Ennustekohdat yhdistetty: %d asemaa, ilman kohtaa %d' % (len(p), len(pairs['none'])))
        except Exception as e:
            print('ennustekohtien yhdistäminen epäonnistui:', e)

    data = get('/api/weather/v1/stations/data', timeout=120)
    fc = {}
    try:
        for s in get('/api/weather/v1/forecast-sections/forecasts', timeout=180).get('forecastSections', []):
            fc[s['id']] = s.get('forecasts', [])
    except Exception as e:
        print('tiesääennuste jäi hakematta:', e)

    rows, dup, stale_n = [], 0, 0
    for s in data.get('stations', []):
        sid = str(s.get('id'))
        if sid not in coords:
            continue
        vals, tmax = {}, None
        for v in s.get('sensorValues', []):
            col = SENS_MAP.get(v.get('name'))
            if not col:
                continue
            mt = parse_t(v.get('measuredTime'))
            if mt is not None and now - mt > STALE_H * 3600:
                stale_n += 1
                continue
            vals[col] = v.get('value')
            if mt is not None and (tmax is None or mt > tmax):
                tmax = mt
        if not vals or tmax is None:
            continue
        if state.get(sid) == round(tmax):
            dup += 1
            continue
        state[sid] = round(tmax)
        row = {'t': iso(now), 'st': sid, 'mt': iso(tmax), 'v': VERSION}
        row.update(vals)
        pr = pairs.get('p', {}).get(sid)
        if pr:
            row['sec'], row['sec_d'] = pr
            F = fc.get(pr[0]) or []
            o = next((f for f in F if f.get('type') == 'OBSERVATION'), None)
            if o:
                row.update({'fo_' + k: v for k, v in fc_fields(o, FC_OBS).items()})
            for name, pre in FC_H:
                f = next((f for f in F if f.get('forecastName') == name), None)
                if f:
                    row.update({pre + '_' + k: v for k, v in fc_fields(f, FC_F).items()})
        rows.append(row)

    write_csv('data/current/obs-%s.csv' % today, COLS, rows)

    # Ilmatieteen laitos: ennuste 3 h välein, havainnot kerran tunnissa
    fst = load('meta/fmi_state.json', {'fc_t': 0, 'obs_t': 0, 'last': {}})
    fmeta = load('meta/fmi_stations.json', {})
    fc_n = obs_n = None
    if now - fst.get('fc_t', 0) >= FMI_FC_EVERY_MIN * 60:
        try:
            fr, ferr = collect_fmi_fc(coords, now)
            write_csv('data/current/fmi-fc-%s.csv' % today, FMI_FC_COLS, fr)
            fc_n = len(fr)
            if len(fr) >= 0.8 * len(coords):
                fst['fc_t'] = round(now)
        except Exception as e:
            print('FMI-ennuste jäi hakematta:', e)
    model_n = {}
    for name, query, params in MODELS:   # bl1: MEPS ja ECMWF samalla rytmillä, omat tilat (virhe ei estä muuta keruuta)
        if now - fst.get(name + '_t', 0) < FMI_FC_EVERY_MIN * 60:
            continue
        try:
            mr, _ = collect_fmi_fc(coords, now, query, params)
            write_csv('data/current/%s-fc-%s.csv' % (name, today), MODEL_FC_COLS, mr)
            model_n[name] = len(mr)
            if len(mr) >= 0.8 * len(coords):
                fst[name + '_t'] = round(now)
        except Exception as e:
            print('%s-ennuste jäi hakematta:' % name.upper(), e)
    if now - fst.get('obs_t', 0) >= FMI_OBS_EVERY_MIN * 60:
        try:
            orows = collect_fmi_obs(now, fst.setdefault('last', {}), fmeta)
            write_csv('data/current/fmi-obs-%s.csv' % today, FMI_OBS_COLS, orows)
            obs_n = len(orows)
            fst['obs_t'] = round(now)
            save('meta/fmi_stations.json', fmeta, indent=0)
        except Exception as e:
            print('FMI-havainnot jäivät hakematta:', e)
    save('meta/fmi_state.json', fst)
    packed = compress_old(today)

    idx['rows'] = idx.get('rows', 0) + len(rows)
    if today not in idx.get('days', []):
        idx.setdefault('days', []).append(today)
    idx.update({'updated': iso(now), 'v': VERSION, 'stations': len(coords), 'meta': len(meta), 'paired': len(pairs.get('p', {})),
                'last_rows': len(rows), 'last_dup': dup, 'last_stale': stale_n, 'last_sec': round(time.time() - t0, 1),
                'first': idx.get('first') or iso(now), 'cols': COLS, 'fmi_fc_cols': FMI_FC_COLS, 'fmi_obs_cols': FMI_OBS_COLS,
                'fmi_stations': len(fmeta)})
    if fc_n is not None:
        idx['fmi_fc_last'] = {'t': iso(now), 'rows': fc_n}
    for name, n in model_n.items():
        idx[name + '_fc_last'] = {'t': iso(now), 'rows': n}
    idx['model_fc_cols'] = MODEL_FC_COLS
    if obs_n is not None:
        idx['fmi_obs_last'] = {'t': iso(now), 'rows': obs_n}
    save('meta/state.json', state)
    save('meta/index.json', idx, indent=1)
    print('Tallennettu %d asemariviä (%d ennallaan, %d vanhaa lukemaa), asemia %d, perustiedot %d, ennustekohdat %d, '
          'FMI-ennuste %s, mallit %s, FMI-havainnot %s, pakattu %d tiedostoa, %.0f s'
          % (len(rows), dup, stale_n, len(coords), len(meta), len(pairs.get('p', {})),
             '-' if fc_n is None else fc_n, ' '.join('%s %d' % kv for kv in model_n.items()) or '-', '-' if obs_n is None else obs_n, packed, time.time() - t0))


if __name__ == '__main__':
    main()
