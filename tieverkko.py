#!/usr/bin/env python3
"""Hoitourakoiden koko tieverkko kelisivun karttaa varten (tv1, 26.10.2026, Samuli: kartan idea 1).

Väyläviraston avoin rajapinta: Maanteiden hoitourakan tiet (tiestotiedot:maanteiden_hoitourakat_0110VV, hoitovuoden mukaan).
Viivat yksinkertaistetaan (Douglas–Peucker 8 m) ja pyöristetään 5 desimaaliin → data/tieverkko-<urakka>.json (~110 kt).
Haetaan uudelleen, kun tiedosto on yli 30 vrk vanha tai hoitovuosi vaihtuu. Lähde: Väylävirasto, CC BY 4.0.
"""
import json, math, os, sys, time, urllib.parse, urllib.request
from datetime import date

VERSION = 'tv1'
WFS = 'https://avoinapi.vaylapilvi.fi/vaylatiedot/ows'
URAKAT = {'vantaa': 'Vantaa', 'salo': 'Salo'}
TOL_M = 8.0
MAX_AGE_D = 30
KX, KY = 111320 * math.cos(math.radians(60.3)), 111320


def layer(today=None):
    d = today or date.today()
    y = d.year if d.month >= 10 else d.year - 1
    return 'tiestotiedot:maanteiden_hoitourakat_0110%02d' % (y % 100)


def fetch(lay, name):
    q = {'service': 'WFS', 'version': '2.0.0', 'request': 'GetFeature', 'typeNames': lay, 'outputFormat': 'application/json',
         'srsName': 'EPSG:4326', 'propertyName': 'nimi,tie,geom', 'CQL_FILTER': "nimi LIKE '%s%%'" % name}
    req = urllib.request.Request(WFS + '?' + urllib.parse.urlencode(q), headers={'User-Agent': 'Vantaa-urakka-tiesaa-arkisto/1'})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())


def dp(pts, tol):
    if len(pts) < 3: return pts
    keep = [False] * len(pts); keep[0] = keep[-1] = True; st = [(0, len(pts) - 1)]
    while st:
        a, b = st.pop()
        ax, ay, bx, by = pts[a][0] * KX, pts[a][1] * KY, pts[b][0] * KX, pts[b][1] * KY
        dx, dy = bx - ax, by - ay; L = dx * dx + dy * dy; md, mi = 0.0, -1
        for i in range(a + 1, b):
            x, y = pts[i][0] * KX, pts[i][1] * KY
            t = ((x - ax) * dx + (y - ay) * dy) / L if L else 0.0
            t = max(0.0, min(1.0, t)); d = math.hypot(x - ax - t * dx, y - ay - t * dy)
            if d > md: md, mi = d, i
        if md > tol:
            keep[mi] = True; st += [(a, mi), (mi, b)]
    return [p for p, k in zip(pts, keep) if k]


def build(j):
    by = {}
    for f in j.get('features', []):
        g = f.get('geometry')
        if not g: continue
        parts = g['coordinates'] if g['type'] == 'MultiLineString' else [g['coordinates']]
        arr = by.setdefault(int(f['properties']['tie']), [])
        cur = None
        for p in parts:   # peräkkäiset palat yhdeksi viivaksi
            if cur and abs(cur[-1][0] - p[0][0]) < 1e-7 and abs(cur[-1][1] - p[0][1]) < 1e-7: cur += p[1:]
            else:
                if cur: arr.append(cur)
                cur = list(p)
        if cur: arr.append(cur)
    roads = []
    for r in sorted(by):
        ls = [[[round(c[0], 5), round(c[1], 5)] for c in dp(l, TOL_M)] for l in by[r]]
        roads.append({'r': r, 'l': [l for l in ls if len(l) >= 2]})
    return roads


def main():
    lay = layer(); os.makedirs('data', exist_ok=True)
    for key, name in URAKAT.items():
        p = 'data/tieverkko-%s.json' % key
        try:
            old = json.load(open(p, encoding='utf-8'))
            if old.get('layer') == lay and time.time() - old.get('t', 0) < MAX_AGE_D * 86400 and '--force' not in sys.argv:
                continue
        except Exception:
            pass
        try:
            j = fetch(lay, name)
            roads = build(j)
            if len(roads) < 10: raise ValueError('liian vähän teitä: %d' % len(roads))
        except Exception as e:
            print('Tieverkko %s jäi hakematta: %s' % (name, e)); continue
        out = {'v': VERSION, 't': int(time.time()), 'layer': lay, 'urakka': j['features'][0]['properties']['nimi'],
               'lahde': 'Väylävirasto, Maanteiden hoitourakan tiet (CC BY 4.0)', 'tol_m': TOL_M, 'roads': roads}
        json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        print('Tieverkko %s: %d tietä, %d pistettä, %d kt' % (out['urakka'], len(roads), sum(len(l) for r in roads for l in r['l']), os.path.getsize(p) // 1024))


if __name__ == '__main__':
    main()
