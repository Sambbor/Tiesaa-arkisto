#!/usr/bin/env python3
"""Koko Suomen talvihoidon toteumat tiesääasemien ympäriltä (Tiesää-arkisto, osa 2).

Joka ajo hakee Digitrafficin kunnossapitoseurannasta valtion maanteiden suolaus-, auraus- ja hiekoituskirjaukset
edellisen ajon jälkeen päättyneiltä ajoilta (enintään 24 h kerrallaan, rajapinnan enimmäisikkuna) ja tallentaa jokaisesta
kirjauksesta rivin jokaiselle tiesääasemalle, jonka 2 km säteellä kone kulki.

- data/current/toteumat-YYYY-MM-DD.csv  (UTC-päivä; arkisto.py pakkaa edelliset päivät archive/YYYY-MM/:ään)
- meta/toteumat_state.json            (seuraavan haun alku, viimeksi nähdyt kirjaukset, yhteenveto)

Sarakkeet: t keruuaika, st asema, task (salt / plow / sand), start ja end kirjauksen alku ja loppu (UTC),
d lähin etäisyys asemaan (m), rid kirjauksen tunniste, sys lähettävä järjestelmä.
Paikallaan seisovan koneen kirjaukset jätetään pois (liike alle 30 m ja kesto vähintään minuutti), kuten kelisivun keruussa.
Asemien urakka-alue, tie ja kunta ovat tiedostossa meta/stations.json.

Käyttö: koko Suomen urakoiden suolaus- ja auraushetket suhteessa asemien keliin ja liukkauteen
(ennakoiva vai jälkikäteinen toiminta), sekä päivystäjän simulaattorin "mitä oikeasti tehtiin".
"""
import json, math, os, sys, time
from datetime import datetime, timezone

from arkisto import get, load, save, iso, parse_t, write_csv, seg_dist, M_LAT

VERSION = 'tt1'
RADIUS = 2000.0                       # m
MAX_WINDOW = 24 * 3600 - 60           # rajapinnan enimmäisikkuna
FIRST_WINDOW = 2 * 3600               # ensimmäinen ajo: 2 h taaksepäin
OVERLAP = 90 * 60                     # kirjaukset voivat ilmestyä rajapintaan viiveellä: haetaan limittäin
SEEN_KEEP = 4 * 3600                  # nähtyjen tunnisteiden muisti (tuplien esto limityksessä)
FI_BBOX = (19.0, 59.5, 31.7, 70.2)
SALT = ['SALTING']
PLOW = ['PLOUGHING_AND_SLUSH_REMOVAL', 'PLOUGHING_OF_SLUSH_DITCH', 'LOWERING_OF_SNOWBANKS', 'REMOVAL_OF_BULGE_ICE', 'TRANSFER_OF_SNOW']
SAND = ['LINE_SANDING', 'SPOT_SANDING']
GROUPS = (('salt', set(SALT)), ('plow', set(PLOW)), ('sand', set(SAND)))
COLS = ['t', 'st', 'task', 'start', 'end', 'd', 'rid', 'sys']
CELL = 0.1                            # asemaruudukko asteina


def points(g):
    if not g:
        return []
    t, c = g.get('type'), g.get('coordinates') or []
    if t == 'Point':
        return [c]
    if t == 'LineString':
        return c
    if t == 'MultiLineString':
        return [p for l in c for p in l]
    return []


def lines(g):
    if not g:
        return []
    t, c = g.get('type'), g.get('coordinates') or []
    if t == 'Point':
        return [[c]]
    if t == 'LineString':
        return [c]
    if t == 'MultiLineString':
        return c
    return []


def station_grid(meta):
    grid = {}
    for sid, m in meta.items():
        try:
            x, y = float(m['lon']), float(m['lat'])
        except (KeyError, TypeError, ValueError):
            continue
        grid.setdefault((int(x // CELL), int(y // CELL)), []).append((sid, x, y))
    return grid


def near_stations(geom, grid):
    """Asemat, joiden 2 km säteellä kirjaus kulki: {asema: lähin etäisyys m}."""
    pts = points(geom)
    if not pts:
        return {}
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    ymid = (min(ys) + max(ys)) / 2
    mlon = M_LAT * math.cos(math.radians(ymid))
    dx, dy = RADIUS / mlon, RADIUS / M_LAT
    x0, x1, y0, y1 = min(xs) - dx, max(xs) + dx, min(ys) - dy, max(ys) + dy
    cand = []
    for gx in range(int(x0 // CELL), int(x1 // CELL) + 1):
        for gy in range(int(y0 // CELL), int(y1 // CELL) + 1):
            for s in grid.get((gx, gy), ()):
                if x0 <= s[1] <= x1 and y0 <= s[2] <= y1:
                    cand.append(s)
    out = {}
    for sid, x, y in cand:
        best = math.inf
        for l in lines(geom):
            if len(l) == 1:
                best = min(best, math.hypot((l[0][0] - x) * mlon, (l[0][1] - y) * M_LAT))
                continue
            for i in range(len(l) - 1):
                # karsitaan kaukaiset osat ennen tarkkaa laskentaa
                if min(abs(l[i][0] - x), abs(l[i + 1][0] - x)) * mlon > RADIUS + 5000:
                    continue
                d = seg_dist((x, y), l[i], l[i + 1], mlon)
                if d < best:
                    best = d
        if best <= RADIUS:
            out[sid] = round(best)
    return out


def is_still(geom, start, end):
    pts = points(geom)
    if not pts:
        return True
    c0 = pts[0]
    mlon = M_LAT * math.cos(math.radians(c0[1]))
    ext = max(math.hypot((c[0] - c0[0]) * mlon, (c[1] - c0[1]) * M_LAT) for c in pts)
    dur = (end - start) if (start and end) else 0
    return ext < 30 and (dur >= 60 or len(pts) == 1)


def fetch(t_from, t_to):
    q = ('/api/maintenance/v1/tracking/routes?domain=state-roads'
         + '&xMin=%s&yMin=%s&xMax=%s&yMax=%s' % FI_BBOX
         + '&endFrom=' + iso(t_from) + '&endBefore=' + iso(t_to)
         + ''.join('&taskId=' + t for t in SALT + PLOW + SAND))
    return get(q, timeout=180)


def build_rows(features, grid, now, seen):
    rows, n_routes, n_still, n_dup = [], 0, 0, 0
    for f in features:
        p = f.get('properties') or {}
        rid = str(f.get('id') if f.get('id') is not None else p.get('id', ''))
        if rid and rid in seen:
            n_dup += 1
            continue
        n_routes += 1
        start, end = parse_t(p.get('startTime')), parse_t(p.get('endTime') or p.get('startTime'))
        if rid:
            seen[rid] = int(end or now)
        tasks = set(p.get('tasks') or [])
        groups = [g for g, s in GROUPS if tasks & s]
        if not groups:
            continue
        geom = f.get('geometry')
        if is_still(geom, start, end):
            n_still += 1
            continue
        near = near_stations(geom, grid)
        for sid, d in sorted(near.items()):
            for g in groups:
                rows.append({'t': iso(now), 'st': sid, 'task': g, 'start': iso(start) if start else '',
                             'end': iso(end) if end else '', 'd': d, 'rid': rid, 'sys': p.get('sendingSystem') or ''})
    return rows, n_routes, n_still, n_dup


def main():
    t0 = time.time()
    now = int(t0)
    today = datetime.fromtimestamp(now, timezone.utc).strftime('%Y-%m-%d')
    meta = load('meta/stations.json', {})
    if not meta:
        print('Toteumat: asemien perustiedot puuttuvat (meta/stations.json), ohitetaan')
        return 0
    st = load('meta/toteumat_state.json', {})
    last = st.get('next_from') or (now - FIRST_WINDOW + OVERLAP)
    t_from = max(last - OVERLAP, now - MAX_WINDOW)
    seen = st.get('seen') if isinstance(st.get('seen'), dict) else {}
    try:
        data = fetch(t_from, now)
    except Exception as e:
        st.update({'v': VERSION, 'last_err': '%s %s' % (iso(now), str(e)[:300])})
        save('meta/toteumat_state.json', st)
        print('Toteumat: haku epäonnistui (%s), yritetään seuraavalla ajolla samasta kohdasta' % e)
        return 0
    feats = (data or {}).get('features') or []
    rows, n_routes, n_still, n_dup = build_rows(feats, station_grid(meta), now, seen)
    os.makedirs('data/current', exist_ok=True)
    if rows:
        write_csv('data/current/toteumat-%s.csv' % today, COLS, rows)
    # Seuraava haku alkaa 90 min ennen tämän ajon loppua; nähdyt tunnisteet estävät tuplat limityksessä.
    seen = {k: v for k, v in seen.items() if v >= now - SEEN_KEEP}
    st.update({'v': VERSION, 'next_from': now, 'seen': seen,
               'last': {'t': iso(now), 'from': iso(t_from), 'features': len(feats), 'routes': n_routes,
                        'still': n_still, 'dup': n_dup, 'rows': len(rows), 'sec': round(time.time() - t0, 1)},
               'rows_total': st.get('rows_total', 0) + len(rows), 'first': st.get('first') or iso(now),
               'cols': COLS, 'last_err': st.get('last_err')})
    save('meta/toteumat_state.json', st)
    print('Toteumat: %d kirjausta (%d uutta, %d paikallaan, %d jo nähty), %d asemariviä, %.0f s'
          % (len(feats), n_routes, n_still, n_dup, len(rows), time.time() - t0))
    return 0


if __name__ == '__main__':
    sys.exit(main())
