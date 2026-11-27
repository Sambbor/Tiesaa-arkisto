#!/usr/bin/env python3
"""Hoitourakoiden koko tieverkko kelisivun karttaa varten (tv1, 26.10.2026, Samuli: kartan idea 1).

Väyläviraston avoin rajapinta: Maanteiden hoitourakan tiet (tiestotiedot:maanteiden_hoitourakat_0110VV, hoitovuoden mukaan).
Viivat yksinkertaistetaan (Douglas–Peucker 8 m) ja pyöristetään 5 desimaaliin → data/tieverkko-<urakka>.json (~110 kt).
Haetaan uudelleen, kun tiedosto on yli 30 vrk vanha tai hoitovuosi vaihtuu. Lähde: Väylävirasto, CC BY 4.0.
"""
import json, math, os, sys, time, urllib.parse, urllib.request
from datetime import date

VERSION = 'tv1'
SUOMI_VERSION = 'tv2'   # tv2 (27.11.2026, Samuli): kaikkien hoitourakoiden tieverkot koko Suomen toimenpidekarttaa varten (--suomi)
WFS = 'https://avoinapi.vaylapilvi.fi/vaylatiedot/ows'
URAKAT = {'vantaa': 'Vantaa', 'salo': 'Salo', 'heinola': 'Heinola'}  # heinola: toimenpidekartta (hk1, 16.11.2026)
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


def suomi():
    """tv2: kaikkien maanteiden hoitourakoiden tieverkot → data/urakat/<urakkakoodi>.json (sama muoto kuin tieverkko-<urakka>.json)
    ja data/urakat/index.json (urakat: ELY, tiekilometrit, rajaus ja yleiskartan karkea viiva). Urakat ovat koodeina ja ELY-alueina,
    ei nimiä eikä urakoitsijoita (su1-linja). Tiedosto kirjoitetaan vain, kun tieverkko muuttuu, joten säilö ei kasva turhaan.
    Haetaan uudelleen, kun edellisestä on yli 30 vrk tai hoitovuosi vaihtuu (tila meta/tieverkko_suomi.json)."""
    lay = layer(); state_p = 'meta/tieverkko_suomi.json'
    try:
        st = json.load(open(state_p, encoding='utf-8'))
        if st.get('layer') == lay and time.time() - st.get('t', 0) < MAX_AGE_D * 86400 and '--force' not in sys.argv:
            print('Koko Suomen tieverkko ajan tasalla (%s)' % st.get('haettu')); return
    except Exception:
        pass
    q = {'service': 'WFS', 'version': '2.0.0', 'request': 'GetFeature', 'typeNames': lay, 'outputFormat': 'application/json',
         'srsName': 'EPSG:4326', 'propertyName': 'urakkakoodi,ely,tie,geom'}
    req = urllib.request.Request(WFS + '?' + urllib.parse.urlencode(q), headers={'User-Agent': 'Vantaa-urakka-tiesaa-arkisto/1'})
    with urllib.request.urlopen(req, timeout=900) as r:
        j = json.loads(r.read())
    by, ely = {}, {}
    for f in j.get('features', []):
        k = (f.get('properties') or {}).get('urakkakoodi')
        if not k or not f.get('geometry'): continue
        by.setdefault(k, []).append(f)
        ely.setdefault(k, ((f['properties'].get('ely') or '').replace(' ELY', '').strip()))
    if len(by) < 50: raise ValueError('liian vähän urakoita: %d' % len(by))
    os.makedirs('data/urakat', exist_ok=True)
    idx, muuttui = [], 0
    for k in sorted(by):
        roads = build({'features': by[k]})
        if not roads: continue
        out = {'v': SUOMI_VERSION, 'layer': lay, 'urakka': k, 'ely': ely[k],
               'lahde': 'Väylävirasto, Maanteiden hoitourakan tiet (CC BY 4.0)', 'tol_m': TOL_M, 'roads': roads}
        p = 'data/urakat/%s.json' % k
        txt = json.dumps(out, ensure_ascii=False, separators=(',', ':'))
        try: old = open(p, encoding='utf-8').read()
        except Exception: old = None
        if old != txt:
            open(p, 'w', encoding='utf-8').write(txt); muuttui += 1
        L = 0.0; w = e = s_ = n = None
        for rd in roads:
            for l in rd['l']:
                for i, c in enumerate(l):
                    w = c[0] if w is None else min(w, c[0]); e = c[0] if e is None else max(e, c[0])
                    s_ = c[1] if s_ is None else min(s_, c[1]); n = c[1] if n is None else max(n, c[1])
                    if i: L += math.hypot((c[0] - l[i - 1][0]) * KX, (c[1] - l[i - 1][1]) * KY)
        # yleiskartta: valta-, kanta- ja seututiet (tie < 1000) karkeana viivana (Douglas–Peucker 400 m, 3 desimaalia)
        yl = []
        for rd in roads:
            if rd['r'] >= 1000: continue
            for l in rd['l']:
                q2 = [[round(c[0], 3), round(c[1], 3)] for c in dp(l, 400.0)]
                if len(q2) >= 2: yl.append(q2)
        idx.append({'k': k, 'ely': ely[k], 'km': round(L / 1000), 'bb': [round(w, 3), round(s_, 3), round(e, 3), round(n, 3)],
                    'kt': len(txt.encode('utf-8')) // 1024, 'yl': yl})
    poistetut = 0
    for fn in os.listdir('data/urakat'):
        if fn.endswith('.json') and fn != 'index.json' and fn[:-5] not in by:
            os.remove(os.path.join('data/urakat', fn)); poistetut += 1
    ix = {'v': SUOMI_VERSION, 'layer': lay, 'lahde': 'Väylävirasto, Maanteiden hoitourakan tiet (CC BY 4.0)',
          'note': 'Urakat urakkakoodeina ja ELY-alueina. yl = yleiskartan karkea viiva (tiet < 1000).', 'u': idx}
    txt = json.dumps(ix, ensure_ascii=False, separators=(',', ':'))
    try: old = open('data/urakat/index.json', encoding='utf-8').read()
    except Exception: old = None
    if old != txt: open('data/urakat/index.json', 'w', encoding='utf-8').write(txt)
    os.makedirs('meta', exist_ok=True)
    json.dump({'v': SUOMI_VERSION, 'layer': lay, 't': int(time.time()), 'haettu': date.today().isoformat(), 'urakoita': len(idx)},
              open(state_p, 'w', encoding='utf-8'))
    print('Koko Suomen tieverkko: %d urakkaa, %d tiedostoa muuttui, %d poistettu, yhteensä %d kt' % (
        len(idx), muuttui, poistetut, sum(x['kt'] for x in idx)))


if __name__ == '__main__':
    if '--suomi' in sys.argv: suomi()
    else: main()
