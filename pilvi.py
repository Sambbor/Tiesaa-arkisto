#!/usr/bin/env python3
# pi1 (12.11.2026, Samuli: "Aloita"): satelliitin pilvimaski Etelä-Suomen päältä 15 min välein – VARJOKERUU.
# Tarkoitus: selvittää talven aikana, kertooko pilven rakoilu tai pysyminen tienpinnan jäähtymisestä etukäteen
# (nykyinen tienpintaennuste on ollut liian kylmä pilvisinä öinä). Ei vaikuta kelisivuun eikä ilmoituksiin.
#
# Lähde: EUMETSAT, Meteosat 0° Cloud Mask (msg_fes:clm), EUMETView WMS (view.eumetsat.int), © EUMETSAT.
# Pikselit: valkoinen = pilvi, vihreä = selkeä maa, sininen = selkeä vesi. Tarkkuus Suomessa noin 5 × 9 km.
#
# Tulos: data/current/pilvi-YYYY-MM-DD/ (kuvan aika UTC-päivänä) → arkisto.py:n compress_old pakkaa
# archive/YYYY-MM/pilvi-YYYY-MM-DD.csv.gz. Sarakkeet:
#   t keruuaika, it kuvan aika, van / van60 / salo / salo60 pilvisten ruutujen osuus 0–1 urakan päällä (r ≤ 18 km)
#   ja renkaalla 18–60 km, n kelvollisia ruutuja, g ruudukko (rivit pohjoisesta etelään, 1 = pilvi, 0 = selkeä maa,
#   2 = selkeä vesi, 9 = ei tietoa; lat 61,00…59,70 0,05° välein, lon 22,50…26,50 0,1° välein → 26 × 40), v versio.
# Tila: meta/pilvi_state.json (viimeisin tallennettu kuva-aika).
# Käyttö: python3 pilvi.py            → hakee viimeisimmän tallennetun jälkeiset kuvat (enintään 12 kpl = 3 h)
#         PILVI_ALKU=2026-10-12 python3 pilvi.py → takautuva haku annetusta päivästä (enintään PILVI_MAX kuvaa)
import json, math, os, re, struct, sys, time, urllib.request, zlib
from datetime import datetime, timedelta, timezone

from arkisto import write_csv

VERSION = 'pi1'
WMS = 'https://view.eumetsat.int/geoserver/ows'
LAYER = 'msg_fes:clm'
LAT_N, LAT_S, LON_W, LON_E = 61.00, 59.70, 22.50, 26.50
W, H = 40, 26
STEP = timedelta(minutes=15)
URAKAT = {'van': (60.32, 24.97), 'salo': (60.39, 23.13)}
R_IN, R_OUT = 18.0, 60.0
STATE = 'meta/pilvi_state.json'
COLS = ['t', 'it', 'van', 'van60', 'salo', 'salo60', 'n', 'g', 'v']
HDR = {'User-Agent': 'tiesaa-arkisto/1 (pilvimaski, varjo)'}


def fetch(params, timeout=60):
    q = '&'.join('%s=%s' % (k, v) for k, v in params.items())
    req = urllib.request.Request(WMS + '?' + q, headers=HDR)
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(), r.headers.get('Content-Type', '')
        except Exception as e:
            if i == 2:
                raise
            time.sleep(5 * (i + 1))


def png_pixels(data):
    """Pieni PNG-purkaja (8-bittinen, lomittamaton; värityypit 2, 3, 6). Palauttaa rivit RGB-monikkoina."""
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError('ei PNG: ' + data[:80].decode('latin-1', 'replace'))
    pos, idat, plte = 8, b'', None
    while pos < len(data):
        ln, typ = struct.unpack('>I4s', data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + ln]
        if typ == b'IHDR':
            w, h, bd, ct, _, _, il = struct.unpack('>IIBBBBB', body)
        elif typ == b'PLTE':
            plte = [tuple(body[i:i + 3]) for i in range(0, len(body), 3)]
        elif typ == b'IDAT':
            idat += body
        elif typ == b'IEND':
            break
        pos += 12 + ln
    if bd != 8 or il != 0 or ct not in (2, 3, 6):
        raise ValueError('PNG-muoto ei tuettu (bd %s ct %s il %s)' % (bd, ct, il))
    bpp = {2: 3, 3: 1, 6: 4}[ct]
    raw = zlib.decompress(idat)
    stride = w * bpp
    prev = bytearray(stride)
    rows, p = [], 0
    for _ in range(h):
        f = raw[p]; line = bytearray(raw[p + 1:p + 1 + stride]); p += 1 + stride
        for i in range(stride):
            a = line[i - bpp] if i >= bpp else 0
            b = prev[i]
            c = prev[i - bpp] if i >= bpp else 0
            if f == 1: line[i] = (line[i] + a) & 255
            elif f == 2: line[i] = (line[i] + b) & 255
            elif f == 3: line[i] = (line[i] + ((a + b) >> 1)) & 255
            elif f == 4:
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                pr = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
                line[i] = (line[i] + pr) & 255
        prev = line
        if ct == 3:
            rows.append([plte[v] for v in line])
        else:
            rows.append([tuple(line[i:i + 3]) for i in range(0, stride, bpp)])
    return rows


def classify(rgb):
    r, g, b = rgb
    if r > 200 and g > 200 and b > 200: return '1'   # pilvi
    if g > 120 and r < 80 and b < 80: return '0'      # selkeä maa
    if b > 150 and r < 80 and g < 80: return '2'      # selkeä vesi
    return '9'


def cell_centers():
    dlat, dlon = (LAT_N - LAT_S) / H, (LON_E - LON_W) / W
    return [[(LAT_N - (j + 0.5) * dlat, LON_W + (i + 0.5) * dlon) for i in range(W)] for j in range(H)]


CENTERS = cell_centers()


def km(a, b):
    return math.hypot((a[0] - b[0]) * 111.2, (a[1] - b[1]) * 111.2 * math.cos(math.radians((a[0] + b[0]) / 2)))


def shares(grid):
    out = {}
    for k, c in URAKAT.items():
        inn, ring = [], []
        for j in range(H):
            for i in range(W):
                v = grid[j][i]
                if v == '9':
                    continue
                d = km(CENTERS[j][i], c)
                if d <= R_IN: inn.append(v == '1')
                elif d <= R_OUT: ring.append(v == '1')
        out[k] = round(sum(inn) / len(inn), 2) if inn else None
        out[k + '60'] = round(sum(ring) / len(ring), 2) if ring else None
    return out


def latest_time():
    """Viimeisin kuva-aika kerroksen GetCapabilities-tiedosta (nearestValue palauttaisi muuten vanhan kuvan uudelleen)."""
    body, _ = fetch({'service': 'WMS', 'request': 'GetCapabilities', 'version': '1.3.0'}, timeout=90)
    t = body.decode('utf-8', 'replace')
    i = t.find('<Name>%s</Name>' % LAYER)
    m = re.search(r'<Dimension name="time"[^>]*default="([^"]+)"', t[i:i + 6000]) if i >= 0 else None
    if not m:
        raise RuntimeError('kerroksen %s aikaa ei löytynyt' % LAYER)
    return datetime.strptime(m.group(1)[:16], '%Y-%m-%dT%H:%M').replace(tzinfo=timezone.utc)


def grab(it):
    body, ctype = fetch({'service': 'WMS', 'version': '1.3.0', 'request': 'GetMap', 'layers': LAYER, 'styles': '',
                         'crs': 'EPSG:4326', 'bbox': '%.2f,%.2f,%.2f,%.2f' % (LAT_S, LON_W, LAT_N, LON_E),
                         'width': W, 'height': H, 'format': 'image/png', 'time': it.strftime('%Y-%m-%dT%H:%M:00Z')})
    px = png_pixels(body)
    return [''.join(classify(p) for p in row) for row in px]


def main():
    now = datetime.now(timezone.utc)
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    alku = os.environ.get('PILVI_ALKU')
    latest = latest_time()
    if alku:
        t0 = datetime.strptime(alku, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        maxn = int(os.environ.get('PILVI_MAX', '3500'))
    else:
        last = st.get('last')
        t0 = (datetime.strptime(last, '%Y-%m-%dT%H:%MZ').replace(tzinfo=timezone.utc) + STEP) if last else latest - 4 * STEP
        t0 = max(t0, latest - 11 * STEP)   # enintään 3 h taaksepäin tavallisessa ajossa
        maxn = 12
    times, t = [], t0
    while t <= latest and len(times) < maxn:
        times.append(t); t += STEP
    by_day, ok, fail = {}, 0, 0
    for it in times:
        try:
            g = grab(it)
        except Exception as e:
            fail += 1
            print('kuva %s epäonnistui: %s' % (it.isoformat(), e))
            if fail >= 5 and ok == 0:
                break
            continue
        flat = ''.join(g)
        n = sum(ch != '9' for ch in flat)
        if n < W * H // 2:   # kuva puuttuu tai ei käsitelty
            fail += 1
            continue
        row = {'t': now.strftime('%Y-%m-%dT%H:%M:%SZ'), 'it': it.strftime('%Y-%m-%dT%H:%MZ'), 'n': n, 'g': flat, 'v': VERSION}
        row.update(shares(g))
        by_day.setdefault(it.strftime('%Y-%m-%d'), []).append(row)
        ok += 1
        if alku:
            time.sleep(0.2)
    for day, rows in sorted(by_day.items()):
        write_csv('data/current/pilvi-%s.csv' % day, COLS, rows)
    if ok:
        last_it = max(r['it'] for rows in by_day.values() for r in rows)
        if not alku or last_it > st.get('last', ''):
            st['last'] = last_it
        st.update({'updated': now.strftime('%Y-%m-%dT%H:%MZ'), 'v': VERSION, 'layer': LAYER,
                   'grid': {'lat': [LAT_N, LAT_S], 'lon': [LON_W, LON_E], 'w': W, 'h': H}})
        os.makedirs('meta', exist_ok=True)
        json.dump(st, open(STATE, 'w'), indent=1)
    print('pilvimaski: %d kuvaa tallennettu, %d epäonnistui (%s … %s)' % (
        ok, fail, times[0].isoformat() if times else '-', times[-1].isoformat() if times else '-'))
    if times and ok == 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
