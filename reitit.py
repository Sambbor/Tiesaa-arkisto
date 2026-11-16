#!/usr/bin/env python3
"""Hoitourakan talvihoitoreittien päättely Harja-toteumista (hr1, 16.11.2026, Samuli: "Voidaanko tämän perusteella saada
Heinolan reitit selville?").

Digitrafficin kunnossapitoseurannasta haetaan urakan alueen suolaus-, auraus- ja hiekoituskirjaukset (oletus 60 vrk).
Koneen tunnistetta ei julkaista, joten kirjaukset ketjutetaan koneajoiksi: previousId tai jatkuvuus (seuraava kirjaus alkaa
alle 6 min ja 400 m päässä edellisen lopusta). Ajot kohdistetaan urakan tieverkon 500 m:n tieosiin (data/tieverkko-<urakka>.json).
Reitti = tieosat, jotka sama kone ajaa samalla kierroksella: tieosien verkko, jossa paino = yhteisten ajojen määrä / harvemmin
ajetun osan ajot, ja yhteisöt Louvainilla. Mukana tieosat, joilla työtä on tehty vähintään 3 eri kerralla.
Puhtaus = kuinka suuri osa ajon tieosista on sen omalla reitillä (mediaani); lähellä 1 = koneet pysyvät reiteillään.

Tulos: data/reitit-<urakka>.json. Ajetaan reitit.yml:ssä kerran viikossa. Lähde: Fintraffic / Digitraffic (CC BY 4.0).
"""
import collections, gzip, itertools, json, math, os, sys, time, urllib.request
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import networkx as nx

VERSION = 'hr1'
URAKAT = {'heinola': 'Heinola'}
DAYS = int(os.environ.get('REITIT_PAIVAT', '60'))
TZ = ZoneInfo('Europe/Helsinki')
LAT0 = 61.3
ML, MO = 111320, 111320 * math.cos(math.radians(LAT0))
TASKS = {'SALTING': 'salt', 'PLOUGHING_AND_SLUSH_REMOVAL': 'plow', 'LINE_SANDING': 'sand', 'SPOT_SANDING': 'sand'}
SEG = 5            # 5 × 100 m = 500 m tieosa
MIN_EVENTS = 3     # tieosa reitille, jos työtä vähintään näin monella kerralla
RES = 1.0          # Louvainin resoluutio (1.0 = vakain jako Heinolan suolauksessa)
MIN_ROUTE_KM = 5


def dist(a, b):
    return math.hypot((a[0] - b[0]) * MO, (a[1] - b[1]) * ML)


def dens(l, step):
    out = [tuple(l[0])]
    for a, b in zip(l, l[1:]):
        n = max(1, math.ceil(dist(a, b) / step))
        for k in range(1, n + 1):
            out.append((a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n))
    return out


def ts(s):
    return datetime.fromisoformat(s.replace('Z', '+00:00')).timestamp()


def fetch(box, frm, to):
    base = ('https://tie.digitraffic.fi/api/maintenance/v1/tracking/routes?domain=state-roads&xMin=%.3f&yMin=%.3f&xMax=%.3f&yMax=%.3f' % box
            + ''.join('&taskId=' + t for t in TASKS))
    out, t = {}, frm
    while t < to:
        z = min(to, t + timedelta(hours=12))
        u = base + '&endFrom=' + t.strftime('%Y-%m-%dT%H:%M:%SZ') + '&endBefore=' + z.strftime('%Y-%m-%dT%H:%M:%SZ')
        for k in range(4):
            try:
                req = urllib.request.Request(u, headers={'Digitraffic-User': 'Tiesaa-arkisto/reitit', 'Accept-Encoding': 'gzip'})
                with urllib.request.urlopen(req, timeout=120) as r:
                    b = r.read()
                    if r.headers.get('Content-Encoding') == 'gzip': b = gzip.decompress(b)
                for f in json.loads(b).get('features', []):
                    out[f['properties']['id']] = f
                break
            except Exception as e:
                if k == 3: raise
                time.sleep(5 * (k + 1))
        t = z
    return list(out.values())


class Net:
    def __init__(self, d):
        self.cells, self.idx, self.G = [], collections.defaultdict(list), 0.004
        for rd in d['roads']:
            for li, l in enumerate(rd['l']):
                for k, c in enumerate(dens(l, 100)):
                    cid = len(self.cells); self.cells.append((c[0], c[1], rd['r'], li, k))
                    self.idx[(int(c[0] // self.G), int(c[1] // self.G))].append(cid)
        self.segpts = collections.defaultdict(list)
        for c in self.cells: self.segpts[self.seg_of(c)].append(c)

    @staticmethod
    def seg_of(c):
        return (c[2], c[3], c[4] // SEG)

    def near(self, c, tol):
        best, bd = None, tol
        cx, cy = int(c[0] // self.G), int(c[1] // self.G)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for q in self.idx.get((cx + dx, cy + dy), ()):
                    # kevyen liikenteen väylät (tie ≥ 70000) kulkevat ajoradan vieressä: ajorata etusijalle
                    dd = dist(self.cells[q], c) + (35 if self.cells[q][2] >= 70000 else 0)
                    if dd < bd: bd, best = dd, q
        return best, bd


def prep(feats, net):
    recs = []
    for f in feats:
        p, g = f['properties'], f['geometry']
        cats = {TASKS[t] for t in p.get('tasks', []) if t in TASKS}
        if not cats or not g: continue
        ls = [g['coordinates']] if g['type'] == 'LineString' else g['coordinates'] if g['type'] == 'MultiLineString' else [[g['coordinates']]]
        pts = [c for l in ls for c in l]
        if not pts: continue
        dp = [c for l in ls for c in (dens(l, 50) if len(l) > 1 else [tuple(l[0])])]
        on, segs = 0, set()
        for c in dp:
            q, dd = net.near(c, 150)
            if q is not None:
                on += 1
                if dd < 60: segs.add(net.seg_of(net.cells[q]))
        recs.append(dict(id=p['id'], prev=p.get('previousId'), cats=cats, s=ts(p['startTime']), e=ts(p['endTime']),
                         first=pts[0], last=pts[-1], onnet=on >= max(1, len(dp) / 3) and max(dist(c, pts[0]) for c in pts) >= 30, segs=segs))
    return sorted(recs, key=lambda r: r['s'])


def chains_of(recs):
    """Kirjaukset koneajoiksi: previousId tai jatkuvuus (alle 6 min, alle 400 m)."""
    open_, chains = [], []
    for r in recs:
        open_ = [c for c in open_ if r['s'] - c['e'] <= 6 * 60]
        best, bd = None, 400
        for c in open_:
            if r['s'] < c['e'] - 90: continue
            dd = 0 if r['prev'] is not None and r['prev'] == c['lastid'] else dist(c['last'], r['first'])
            if dd < bd: bd, best = dd, c
        if best is None:
            best = dict(recs=[], e=0); chains.append(best)
        else:
            open_.remove(best)
        open_.append(best)
        best['recs'].append(r); best['e'] = max(best['e'], r['e']); best['last'] = r['last']; best['lastid'] = r['id']
    return chains


def events_of(chains):
    """Työkerrat: ajot, joiden väli on alle 4 h."""
    ev, cur = [], None
    for c in sorted(chains, key=lambda c: c['recs'][0]['s']):
        s = c['recs'][0]['s']
        if cur and s - cur['e'] < 4 * 3600:
            cur['ch'].append(c); cur['e'] = max(cur['e'], c['e'])
        else:
            cur = dict(s=s, e=c['e'], ch=[c]); ev.append(cur)
    return ev


def polylines(segs, net):
    """Tieosat viivoiksi: peräkkäiset saman tien saman viivan osat yhdeksi."""
    by = collections.defaultdict(list)
    for s in segs: by[(s[0], s[1])].append(s[2])
    out = []
    for (r, li), ks in sorted(by.items()):
        ks.sort(); run = [ks[0]]
        for k in ks[1:] + [None]:
            if k is not None and k == run[-1] + 1: run.append(k); continue
            pts = [p for kk in run for p in net.segpts[(r, li, kk)]]
            pts.sort(key=lambda c: c[4])
            out.append({'r': r, 'l': [[round(p[0], 5), round(p[1], 5)] for p in pts]})
            if k is not None: run = [k]
    return out


def routes_for(cat, recs, net):
    rs = [r for r in recs if cat in r['cats']]
    chains = [c for c in chains_of(rs) if sum(1 for r in c['recs'] if r['onnet']) >= 3]
    ev = events_of(chains)
    segEv, chainSegs = collections.defaultdict(set), []
    for ei, e in enumerate(ev):
        for c in e['ch']:
            ss = set().union(*[r['segs'] for r in c['recs'] if r['onnet']])
            if len(ss) < 4: continue
            chainSegs.append((ei, c, ss))
            for s in ss: segEv[s].add(ei)
    nEv = len({ei for ei, _, _ in chainSegs})
    if nEv < MIN_EVENTS:
        return {'tila': 'liian_vahan', 'kerrat': nEv, 'tarvitaan': MIN_EVENTS, 'reitit': []}
    core = {s for s, v in segEv.items() if len(v) >= MIN_EVENTS}
    occ, co = collections.Counter(), collections.Counter()
    for _, _, ss in chainSegs:
        ss = sorted(s for s in ss if s in core)
        for s in ss: occ[s] += 1
        for a, b in itertools.combinations(ss, 2): co[(a, b)] += 1
    G = nx.Graph(); G.add_nodes_from(core)
    for (a, b), n in co.items():
        w = n / min(occ[a], occ[b])
        if w >= 0.3: G.add_edge(a, b, weight=w)
    com = [c for c in nx.community.louvain_communities(G, weight='weight', resolution=RES, seed=1) if len(c) * SEG / 10 >= MIN_ROUTE_KM]
    # Rinnakkaiset koneet: jos reitin osat ajetaan samaan aikaan (ensimmäisten kirjausten aikavälit menevät päällekkäin
    # vähintään 60 %:lla kerroista), kyse on kahdesta koneesta, jotka lähtevät samasta paikasta → jaetaan.
    def firsts(part):
        out = []
        for e in ev:
            t = [r['s'] for c in e['ch'] for r in c['recs'] if r['onnet'] and r['segs'] & part]
            if len(t) >= 3: t.sort(); out.append((t[0], t[int(len(t) * 0.8)]))
            else: out.append(None)
        return out
    def overlap(a, b):
        both = [(x, y) for x, y in zip(firsts(a), firsts(b)) if x and y]
        if len(both) < MIN_EVENTS: return 0.0
        # päällekkäin = yhteistä aikaa yli 30 % lyhyemmästä ikkunasta (pelkkä vaihtokohta ei riitä)
        return sum(1 for x, y in both if min(x[1], y[1]) - max(x[0], y[0]) > 0.3 * max(600, min(x[1] - x[0], y[1] - y[0]))) / len(both)
    def link(a, b):
        w = sum(G[s][t]['weight'] for s in a for t in G[s] if t in b)
        return w / math.sqrt(len(a) * len(b))
    split = []
    for c in com:
        parts = [set(x) for x in nx.community.louvain_communities(G.subgraph(c), weight='weight', resolution=2.0, seed=1)]
        big = [p for p in parts if len(p) * SEG / 10 >= 10]
        if len(big) < 2: split.append(c); continue
        ov = {(i, j): overlap(big[i], big[j]) for i in range(len(big)) for j in range(i + 1, len(big))}
        groups = [[i] for i in range(len(big))]
        while True:   # yhdistetään eniten yhteisiä ajoja omaavat osat, jos niitä ei ajeta samaan aikaan
            best = None
            for gi, gj in itertools.combinations(range(len(groups)), 2):
                if any(ov[tuple(sorted((a, b)))] >= 0.5 for a in groups[gi] for b in groups[gj]): continue
                w = link(set().union(*[big[a] for a in groups[gi]]), set().union(*[big[b] for b in groups[gj]]))
                if w > 0 and (best is None or w > best[0]): best = (w, gi, gj)
            if not best: break
            _, gi, gj = best; groups[gi] += groups[gj]; del groups[gj]
        if len(groups) == 1: split.append(c); continue
        gs = [set().union(*[big[a] for a in g]) for g in groups]
        for s in c - set().union(*gs):   # pienet palat ryhmälle, jonka kanssa eniten yhteisiä ajoja
            k = max(range(len(gs)), key=lambda q: sum(G[s][t]['weight'] for t in G[s] if t in gs[q])); gs[k].add(s)
        print('  reitti jaettu rinnakkaisiksi koneiksi:', [round(len(g) * SEG / 10) for g in gs], file=sys.stderr)
        split += gs
    com = sorted(split, key=lambda c: -len(c))
    lab = {s: i for i, c in enumerate(com) for s in c}
    pur = []
    for _, _, ss in chainSegs:
        cc = collections.Counter(lab[s] for s in ss if s in lab)
        if sum(cc.values()) >= 10: pur.append(cc.most_common(1)[0][1] / sum(cc.values()))
    out = []
    for i, cm in enumerate(com):
        roadKm = collections.Counter()
        for s in cm: roadKm[s[0]] += SEG / 10
        # kierrokset: kerrat, joilla vähintään puolet reitistä ajettiin; alku = ensimmäinen kirjaus, kesto = 90 % reitistä ajettu
        starts, durs, chainsPer = [], [], []
        for ei, e in enumerate(ev):
            first = {}
            nch = 0
            for c in e['ch']:
                hit = False
                for r in c['recs']:
                    if not r['onnet']: continue
                    for s in r['segs'] & cm:
                        hit = True
                        if s not in first or r['s'] < first[s]: first[s] = r['s']
                nch += hit
            if len(first) < len(cm) / 2: continue
            t = sorted(first.values())
            starts.append(t[0]); durs.append((t[int(len(t) * 0.9) - 1 if len(t) > 1 else 0] - t[0]) / 3600); chainsPer.append(nch)
        med = lambda a: sorted(a)[len(a) // 2] if a else None
        out.append({
            'id': i + 1, 'km': round(len(cm) * SEG / 10, 1),
            'tiet': [{'tie': r, 'km': round(k, 1)} for r, k in roadKm.most_common()],
            'kierrokset': len(starts),
            'alut': [datetime.fromtimestamp(t, TZ).strftime('%Y-%m-%d %H:%M') for t in starts],
            'kestoH': round(med(durs), 1) if durs else None,
            'ajojaKierroksella': med(chainsPer),
            'viivat': polylines(cm, net)})
    # satunnaiset: tieosat, joilla työtä 1–2 kertaa (ei reitille)
    rare = [s for s, v in segEv.items() if s not in core]
    return {'tila': 'ok', 'kerrat': nEv, 'ajoja': len(chainSegs), 'puhtaus': round(sorted(pur)[len(pur) // 2], 2) if pur else None,
            'tyokerrat': [datetime.fromtimestamp(e['s'], TZ).strftime('%Y-%m-%d %H:%M') for e in ev],
            'reitit': out, 'satunnaiset': polylines(rare, net)}


def main():
    force = '--force' in sys.argv
    os.makedirs('data', exist_ok=True)
    for key, name in URAKAT.items():
        p = 'data/reitit-%s.json' % key
        try:
            old = json.load(open(p, encoding='utf-8'))
            if not force and time.time() - old.get('t', 0) < 6.5 * 86400:
                print('Reitit %s: tuore (%s), ohitetaan' % (name, old.get('laskettu'))); continue
        except Exception:
            pass
        d = json.load(open('data/tieverkko-%s.json' % key, encoding='utf-8'))
        net = Net(d)
        pts = [c for rd in d['roads'] for l in rd['l'] for c in l]
        box = (min(c[0] for c in pts) - 0.02, min(c[1] for c in pts) - 0.01, max(c[0] for c in pts) + 0.02, max(c[1] for c in pts) + 0.01)
        now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
        feats = fetch(box, now - timedelta(days=DAYS), now)
        recs = prep(feats, net)
        out = {'v': VERSION, 't': int(time.time()), 'laskettu': datetime.now(TZ).strftime('%Y-%m-%d %H:%M'), 'urakka': d.get('urakka', name),
               'jakso': [(now - timedelta(days=DAYS)).astimezone(TZ).strftime('%Y-%m-%d'), now.astimezone(TZ).strftime('%Y-%m-%d')],
               'kirjauksia': len(feats), 'urakanKirjauksia': sum(r['onnet'] for r in recs),
               'lahde': 'Fintraffic / Digitraffic, kunnossapidon seuranta (CC BY 4.0); Väylävirasto, Maanteiden hoitourakan tiet (CC BY 4.0)',
               'tyolajit': {c: routes_for(c, recs, net) for c in ('salt', 'plow', 'sand')}}
        json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        for c, v in out['tyolajit'].items():
            print('Reitit %s %s: %s, %d kertaa, %d reittiä %s, puhtaus %s' % (name, c, v['tila'], v['kerrat'], len(v['reitit']),
                  [r['km'] for r in v['reitit']], v.get('puhtaus')))


if __name__ == '__main__':
    main()
