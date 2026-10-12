#!/usr/bin/env python3
"""Tiesää-arkisto – koko Suomen tiesääasemien mittaukset ja tiesääennusteet talteen liukkausmallin opettamista varten.

Ajetaan GitHub Actionsissa 30 min välein (säilö Sambbor/Tiesaa-arkisto).
- Kaikki keräävät asemat (noin 525): tienpinta, ilma, kastepiste, kuurapiste, keli, varoitus, jäätymispiste, suola,
  vesi/lumi/jää, kitka, sade, näkyvyys, tuuli (stations/data, yksi haku koko maasta).
- Jokaiselle asemalle lähimmän tiesääennusteen tiekohdan ennuste nyt ja +2/4/6/12 h (forecast-sections/forecasts, yksi haku).
- Vain uudet mittaukset tallennetaan (asema, jonka mittausaika ei ole muuttunut, ohitetaan). Yli 2 h vanhat anturilukemat ohitetaan.
- Päivän rivit: data/current/obs-YYYY-MM-DD.csv (UTC-päivä). Edelliset päivät pakataan archive/YYYY-MM/obs-YYYY-MM-DD.csv.gz.
- Asemien tiedot (tie, tieosa, urakka, kunta, maakunta) meta/stations.json, asema → ennusteen tiekohta meta/pairs.json.
Data: Fintraffic / Digitraffic, CC BY 4.0. Vain Pythonin vakiokirjasto.
"""
import gzip, json, math, os, time, urllib.request
from datetime import datetime, timezone

VERSION = 'ta1'
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


def get(path, timeout=90):
    req = urllib.request.Request(DT + path, headers=HDR)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        b = r.read()
        if r.headers.get('Content-Encoding', '').lower() == 'gzip' or b[:2] == b'\x1f\x8b':
            b = gzip.decompress(b)
    return json.loads(b)


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


def compress_old(today):
    """Pakkaa edellisten päivien CSV:t arkistoon (archive/YYYY-MM/obs-YYYY-MM-DD.csv.gz)."""
    n = 0
    d = 'data/current'
    if not os.path.isdir(d):
        return 0
    for fn in sorted(os.listdir(d)):
        if not (fn.startswith('obs-') and fn.endswith('.csv')):
            continue
        day = fn[4:14]
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

    path = 'data/current/obs-%s.csv' % today
    new = not os.path.exists(path)
    with open(path, 'a', encoding='utf-8') as f:
        if new:
            f.write(','.join(COLS) + '\n')
        for r in rows:
            f.write(','.join(cell(r.get(c)) for c in COLS) + '\n')
    packed = compress_old(today)

    idx['rows'] = idx.get('rows', 0) + len(rows)
    if today not in idx.get('days', []):
        idx.setdefault('days', []).append(today)
    idx.update({'updated': iso(now), 'v': VERSION, 'stations': len(coords), 'meta': len(meta), 'paired': len(pairs.get('p', {})),
                'last_rows': len(rows), 'last_dup': dup, 'last_stale': stale_n, 'last_sec': round(time.time() - t0, 1),
                'first': idx.get('first') or iso(now), 'cols': COLS})
    save('meta/state.json', state)
    save('meta/index.json', idx, indent=1)
    print('Tallennettu %d asemariviä (%d ennallaan, %d vanhaa lukemaa), asemia %d, perustiedot %d, ennustekohdat %d, pakattu %d päivää, %.0f s'
          % (len(rows), dup, stale_n, len(coords), len(meta), len(pairs.get('p', {})), packed, time.time() - t0))


if __name__ == '__main__':
    main()
