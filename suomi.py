#!/usr/bin/env python3
"""Koko Suomen yökooste: urakoiden riski ja toimenpiteet samana yönä (su1, 6.11.2026, Samuli: "Koko Suomi, julkinen ilman nimiä").

su2: riskin rinnalle havaittu liukkaus optisesta kitkasta (riski liioittelee: 2026 loka–marraskuussa vain noin joka seitsemäs
riskiyö näkyi kitkassa), poikkeavat tienpinta- ja kitka-anturit pois laskuista.

Jokaiselle maanteiden hoitourakalle illan klo 18 – aamun klo 08 (Suomen aikaa) yhteenveto tämän arkiston aineistosta:
- riski urakan tiesääasemilta: alin tienpinta, kuura- ja jäätymisaskeleet (fysikaalinen ehto, ei anturin keli-koodia, koska
  keli-anturit hälyttävät turhaan), anturin liukashälytykset erikseen
- toimenpiteet: suolaus, auraus ja hiekoitus (toteumat.py: kirjaus enintään 1 km päässä urakan asemasta). Suolaus luetaan jo klo 15 alkaen,
  jotta illan ennakkosuolaus näkyy.
- ajoitus: ennakoiva (suolattu ennen riskin alkua), nopea (alle 2 h alusta), myöhäinen, ei suolausta, suolaus ilman riskiä

Urakka tunnistetaan Väyläviraston tiedosta Maanteiden hoitourakan tiet (aseman tieosoite urakan tieosuudella; muuten saman tien
viiva 400 m päässä). Digitrafficin aseman urakkatieto ei kelpaa (osa vanhoista urakoista, osa puuttuu, nimiä väärin).
Julkisessa tiedostossa urakat ovat urakkakoodeina (PR…) ja ELY-alueina, ei nimiä eikä urakoitsijoita.

Tulokset:
- meta/urakat.json      asema → urakkakoodi, urakoiden ELY (haetaan uudelleen 30 vrk välein tai hoitovuoden vaihtuessa)
- suomi/YYYY-MM-DD.json yksi yö (illan päivämäärä)
- data/suomi.json       kausi urakoittain + viimeisin yö
Käyttö: python3 suomi.py (arkiston ajo: valmis yö lasketaan uudelleen 6 h ajan myöhästyvien kirjausten takia)
        python3 suomi.py --yo 2026-11-03 | --alku 2026-10-12 [--loppu 2026-11-05]
Varaukset: toteuma näkyy vain asemien lähellä (1 km), rajan lähellä naapurin kone voi osua. Riski asemamittauksista, ei koko tieverkolta.
"""
import glob, json, os, statistics, sys, urllib.parse, urllib.request
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from naapurit import read_day, f, ts, plaus, slippery

VERSION = 'su3'   # su2 (6.11.2026, Samuli: "Tee 1"): havaittu liukkaus optisesta kitkasta, poikkeavat anturit pois; su3: tuuliehto pois kuurasta
HEL = ZoneInfo('Europe/Helsinki')
WFS = 'https://avoinapi.vaylapilvi.fi/vaylatiedot/ows'
UA = {'User-Agent': 'tiesaa-arkisto/1'}
TOT_M = 1000          # toteuma enintään näin kaukana asemasta
RISK_MIN = 2          # riskiyö: vähintään 2 puolen tunnin askelta (1 h) riskissä
NOPEA_MIN = 120
RECOMPUTE_H = 6
KITKA_LIUKAS = 0.6    # optinen kitka: 0,82 kuiva, 0,6–0,75 märkä tai ohut kuura, alle 0,6 liukas
TR_POIKKEAMA = 4.0    # °C: aseman tienpinta yön mediaanina näin paljon urakan muiden asemien alle (tai 1,5 × yli) → viallinen


def layer(d):
    y = d.year if d.month >= 10 else d.year - 1
    return 'tiestotiedot:maanteiden_hoitourakat_0110%02d' % (y % 100)


def wfs(q, timeout=300):
    q = dict({'service': 'WFS', 'version': '2.0.0', 'request': 'GetFeature', 'outputFormat': 'application/json'}, **q)
    with urllib.request.urlopen(urllib.request.Request(WFS + '?' + urllib.parse.urlencode(q), headers=UA), timeout=timeout) as r:
        return json.loads(r.read())


def urakat(today, force=False):
    """Asema → urakkakoodi. Ensisijaisesti tieosoite (tie, osa, etäisyys) urakan tieosuudella, muuten saman tien viiva 400 m säteellä."""
    path = 'meta/urakat.json'
    old = None
    try:
        old = json.load(open(path, encoding='utf-8'))
    except Exception:
        pass
    lay = layer(today)
    if old and not force and old.get('layer') == lay and (today - date.fromisoformat(old['haettu'])).days < 30:
        return old
    meta = json.load(open('meta/stations.json', encoding='utf-8'))
    try:
        j = wfs({'typeNames': lay, 'propertyName': 'nimi,urakkakoodi,ely,tie,aosa,aet,losa,let'})
    except Exception as e:
        print('Urakkatieto ei saatavilla (%s)' % e)
        return old
    by, U = {}, {}
    for ft in j.get('features', []):
        p = ft['properties']
        if not p.get('urakkakoodi'): continue
        by.setdefault(p['tie'], []).append(p)
        U.setdefault(p['urakkakoodi'], {'ely': (p.get('ely') or '').replace(' ELY', '').strip()})
    st, src = {}, {}
    for sid, m in meta.items():
        r, s, d = m.get('road'), m.get('sec'), m.get('dist')
        if r is None or s is None or d is None: continue
        hit = [p['urakkakoodi'] for p in by.get(r, []) if (p['aosa'], p['aet']) <= (s, d) <= (p['losa'], p['let'])]
        if hit:
            st[sid], src[sid] = hit[0], 'osoite'
    for sid, m in meta.items():   # tieosoite vanhentunut tai katuosuus: saman tien viiva lähellä
        if sid in st or m.get('lat') is None or not m.get('road'): continue
        lat, lon, dt, dl = m['lat'], m['lon'], 0.0036, 0.0072
        try:
            g = wfs({'typeNames': lay, 'propertyName': 'urakkakoodi,tie', 'count': '50',
                     'BBOX': '%f,%f,%f,%f,urn:ogc:def:crs:EPSG::4326' % (lat - dt, lon - dl, lat + dt, lon + dl)}, 60)
        except Exception:
            continue
        hit = [ft['properties']['urakkakoodi'] for ft in g.get('features', []) if ft['properties'].get('tie') == m['road']]
        if hit:
            st[sid], src[sid] = max(set(hit), key=hit.count), 'sijainti'
    for k in U: U[k]['asemia'] = sum(1 for v in st.values() if v == k)
    out = {'v': VERSION, 'layer': lay, 'haettu': today.isoformat(), 'st': st, 'lahde': src,
           'u': {k: {'ely': v['ely'], 'asemia': v['asemia']} for k, v in sorted(U.items())},
           'ilman_urakkaa': sorted(set(meta) - set(st)),
           'note': 'Lähde: Väylävirasto, Maanteiden hoitourakan tiet (CC BY 4.0). Asemat ilman urakkaa: kadut, Ahvenanmaa, elinkaariurakat.'}
    os.makedirs('meta', exist_ok=True)
    json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('Urakat: %d asemaa %d urakkaan (%d sijainnista), %d ilman urakkaa' % (
        len(st), len(U), sum(1 for v in src.values() if v == 'sijainti'), len(out['ilman_urakkaa'])))
    return out


def window(ev):
    e = date.fromisoformat(ev)
    n = e + timedelta(days=1)
    return (datetime(e.year, e.month, e.day, 18, tzinfo=HEL).astimezone(timezone.utc),
            datetime(n.year, n.month, n.day, 8, tzinfo=HEL).astimezone(timezone.utc),
            datetime(e.year, e.month, e.day, 15, tzinfo=HEL).astimezone(timezone.utc))


def step(t):
    return t.replace(minute=30 if t.minute >= 30 else 0, second=0, microsecond=0)


def z(t):
    return t.strftime('%Y-%m-%dT%H:%MZ') if t else None


def kitka(r):
    v = [x for x in (f(r.get('fric1')), f(r.get('fric2'))) if x is not None and 0 < x <= 1]
    return min(v) if v else None


def risk_kind(r):
    """Fysikaalinen jäätymisriski yhdessä mittauksessa: 'kuura', 'marka' (märkä tai sade pakkasella), 'lumi' tai None.
    Tuulta ei käytetä (Samuli 6.11.: tuuli ei estä kuuraantumista; pohjoinen kuiva tuuli voi vain vähän auttaa)."""
    tr, ta, td = f(r.get('tr1')), f(r.get('ta')), f(r.get('td'))
    if not plaus(tr, ta) or tr > 0.5: return None
    rain, form = f(r.get('rain_i')) or f(r.get('rain')) or 0, f(r.get('rain_form'))
    water = f(r.get('water1')) or 0
    if rain > 0 and form is not None and int(form) in (3, 4, 5, 6) and (ta is None or ta <= 1): return 'lumi'
    if tr <= 0 and (rain > 0 or water >= 0.1): return 'marka'
    if td is not None and tr <= 0 and td >= tr: return 'kuura'
    return None


def analyse(a):
    """Aseman rivit → poikkeavat anturit, riski askelittain, havaittu liukkaus optisesta kitkasta."""
    R = a['rows']
    # tienpinta-anturi, joka on koko yön selvästi urakan muiden asemien alla tai yllä (esim. Keimola −9 °C muiden ollessa +1 °C)
    out = set()   # (asema, askel): yksittäinen mittaus selvästi muista poikkeava
    if len(R) >= 4:
        dev = {}
        for s in {k for v in R.values() for k in v}:
            v = [(st, f(rr.get('tr1'))) for st, x in R.items() for rr in [x.get(s)] if rr is not None]
            v = [(st, x) for st, x in v if x is not None and -45 < x < 65]
            if len(v) < 4: continue
            m = statistics.median(x for _, x in v)
            for st, x in v:
                dev.setdefault(st, []).append(x - m)
                if abs(x - m) > TR_POIKKEAMA: out.add((st, s))
        for st, d in dev.items():
            if len(d) >= 6:
                md = statistics.median(d)
                if md < -TR_POIKKEAMA or md > 1.5 * TR_POIKKEAMA: a['vika'][st] = 'tienpinta %+.1f °C' % md; a['trVika'].add(st)
        for st in {st for st, _ in out}:
            n = sum(1 for x, _ in out if x == st)
            if n >= 3 and st not in a['vika']: a['vika'][st] = 'tienpinta poikkeaa %d mittauksessa' % n
    for st, x in R.items():
        # optinen anturi, joka näyttää liukasta lämpimällä tiellä, on viallinen
        lammin = sum(1 for rr in x.values() if (kitka(rr) or 1) < KITKA_LIUKAS and (f(rr.get('tr1')) or -99) > 3)
        if lammin >= 4: a['vika'].setdefault(st, 'kitka-anturi')
    for st, x in R.items():
        for s, r in x.items():
            tr, ta = f(r.get('tr1')), f(r.get('ta'))
            trvika = st in a['trVika'] or (st, s) in out
            if not trvika and plaus(tr, ta) and tr < a['trSt'].get(st, 99): a['trSt'][st] = tr
            k = None if trvika else risk_kind(r)
            if k:
                a['risk'].setdefault(s, set()).add(st); a['kind'][k] = a['kind'].get(k, 0) + 1
            if slippery(r): a['slip'].add(st)
            fr_ = kitka(r)
            if fr_ is None or a['vika'].get(st) == 'kitka-anturi': continue
            a['opt'].add(st)
            if a['kitkaMin'] is None or fr_ < a['kitkaMin']: a['kitkaMin'] = fr_
            kylma = (tr is not None and tr <= 1) if not trvika else (ta is not None and ta <= 2)
            if fr_ < KITKA_LIUKAS and kylma: a['obs'].setdefault(st, []).append(s)


def havaittu(a, salt, riski):
    """Havaittu liukkaus: optinen kitka alle 0,6 kylmällä tiellä vähintään 1 h (2 peräkkäistä mittausta) yhdellä asemalla."""
    if not a['opt']:
        return {'opt': 0, 'havaittu': None, 'tulos': 'ei_optista' if riski else None, 'vika': a['vika'] or None}
    alut = []
    steps = set()
    for st, v in a['obs'].items():
        v = sorted(v)
        for x, y in zip(v, v[1:]):
            if (y - x).total_seconds() <= 1800: alut.append(x); break
        steps |= set(v)
    hav = bool(alut)
    alku = min(alut) if alut else None
    ehti = None
    if hav:
        ehti = 'ennen' if any(x <= alku for x in salt) else 'jalkeen' if any(x > alku for x in salt) else 'ei'
    tulos = ('liukasta' if hav else 'ei_liukasta') if riski else ('liukasta_ilman_riskia' if hav else None)
    return {'opt': len(a['opt']), 'havaittu': hav, 'havAlku': z(alku), 'havH': round(len(steps) / 2, 1) if hav else 0,
            'kitkaMin': None if a['kitkaMin'] is None else round(a['kitkaMin'], 2), 'suolaVsLiukas': ehti, 'tulos': tulos,
            'vika': a['vika'] or None}


def night(ev, U):
    fr, to, fr_tot = window(ev)
    days = sorted({fr_tot.date().isoformat(), fr.date().isoformat(), to.date().isoformat()})
    code = U['st']
    A, puuttuu = {}, []
    def a_of(c):
        if c not in A:
            A[c] = {'st': set(), 'rows': {}, 'trSt': {}, 'risk': {}, 'kind': {}, 'slip': set(), 'obs': {}, 'opt': set(),
                    'kitkaMin': None, 'vika': {}, 'trVika': set(), 'w': {'salt': {}, 'plow': {}, 'sand': {}}}
        return A[c]
    for d in days:
        for r in read_day('obs', d):
            c = code.get(r.get('st'))
            if not c: continue
            t = ts(r.get('t'))
            if not t or t < fr or t > to: continue
            a = a_of(c); a['st'].add(r['st'])
            a['rows'].setdefault(r['st'], {})[step(t)] = r
        T = read_day('toteumat', d)
        if not T: puuttuu.append(d)
        for r in T:
            c = code.get(r.get('st'))
            if not c or r.get('task') not in ('salt', 'plow', 'sand'): continue
            e, dd = ts(r.get('end')), f(r.get('d'))
            if not e or e > to or (dd is not None and dd > TOT_M): continue
            if e < (fr_tot if r['task'] == 'salt' else fr): continue
            a_of(c)['w'][r['task']][r.get('rid') or (r.get('start'), r.get('end'))] = e
    for a in A.values():
        analyse(a)
    rows = []
    for c, a in sorted(A.items()):
        n = len(a['st'])
        if not n: continue
        need = max(1, round(0.2 * n))
        mins = sorted(a['trSt'].values())
        trMin = (mins[1] if len(mins) >= 3 else mins[0]) if mins else None   # 2. kylmin asema: yksi viallinen anturi ei ratkaise
        rs = sorted(s for s, v in a['risk'].items() if len(v) >= need)
        riski = len(rs) >= RISK_MIN
        alku = rs[0] if riski else None
        w = {k: sorted(set(v.values())) for k, v in a['w'].items()}
        def kerrat(ts_):
            if not ts_: return 0
            return 1 + sum(1 for x, y in zip(ts_, ts_[1:]) if (y - x).total_seconds() > 1800)
        salt = w['salt']
        ens = salt[0] if salt else None
        if puuttuu:
            luokka, viive = ('tuntematon' if riski else 'ei_tarvetta'), None
        elif riski:
            pre = [x for x in salt if alku - timedelta(hours=6) <= x <= alku]
            post = [x for x in salt if x > alku]
            if pre: luokka, viive = 'ennakoiva', 0
            elif post:
                viive = round((post[0] - alku).total_seconds() / 60)
                luokka = 'nopea' if viive <= NOPEA_MIN else 'myohainen'
            else: luokka, viive = 'ei', None
        else:
            luokka, viive = ('ilman_riskia' if [x for x in salt if x >= fr] else 'ei_tarvetta'), None
        rows.append({'u': c, 'ely': U['u'].get(c, {}).get('ely'), 'as': n, 'trMin': None if trMin is None else round(trMin, 1),
                     'riskiH': round(len(rs) / 2, 1), 'riski': riski, 'alku': z(alku),
                     'laji': max(a['kind'], key=a['kind'].get) if a['kind'] else None, 'anturiLiukas': len(a['slip']),
                     'suola': kerrat(salt), 'suolaEka': z(ens), 'aura': kerrat(w['plow']), 'hiekka': kerrat(w['sand']),
                     'luokka': luokka, 'viive': viive, **havaittu(a, salt, riski)})
    return {'v': VERSION, 'yo': ev, 'from': z(fr), 'to': z(to), 'laskettu': z(datetime.now(timezone.utc)),
            'toteumat': not puuttuu, 'urakat': rows}


def kausi():
    K = {}
    nights = []
    for p in sorted(glob.glob('suomi/????-??-??.json')):
        try:
            N = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        nights.append(N['yo'])
        if not N.get('toteumat', True): continue   # toteumakeruussa aukko: yö ei mukana kausiluvuissa
        for r in N['urakat']:
            k = K.setdefault(r['u'], {'u': r['u'], 'ely': r['ely'], 'yot': 0, 'riskiyot': 0, 'ennakoiva': 0, 'nopea': 0, 'myohainen': 0,
                                      'ei': 0, 'ilman_riskia': 0, 'suolauskerrat': 0, 'viiveet': [], 'trMin': None,
                                      'optYot': 0, 'liukasYot': 0, 'riskiEiLiukasta': 0, 'ehtiEnnen': 0, 'suolaJalkeen': 0, 'eiSuolaLiukas': 0})
            k['yot'] += 1; k['riskiyot'] += r['riski']; k['suolauskerrat'] += r['suola']
            if r['luokka'] in k: k[r['luokka']] += 1
            if r['viive']: k['viiveet'].append(r['viive'])
            if r.get('havaittu') is not None:
                k['optYot'] += 1; k['liukasYot'] += r['havaittu']; k['riskiEiLiukasta'] += r.get('tulos') == 'ei_liukasta'
                sv = r.get('suolaVsLiukas')
                k['ehtiEnnen'] += sv == 'ennen'; k['suolaJalkeen'] += sv == 'jalkeen'; k['eiSuolaLiukas'] += sv == 'ei'
            if r['trMin'] is not None and (k['trMin'] is None or r['trMin'] < k['trMin']): k['trMin'] = r['trMin']
    rows = []
    for k in K.values():
        v = k.pop('viiveet')
        k['viiveMed'] = round(statistics.median(v)) if v else None
        k['ennakoivaPros'] = round(100 * k['ennakoiva'] / k['riskiyot']) if k['riskiyot'] else None
        k['ehtiPros'] = round(100 * k['ehtiEnnen'] / k['liukasYot']) if k['liukasYot'] else None
        k['oikeaanAikaanPros'] = round(100 * (k['ennakoiva'] + k['nopea']) / k['riskiyot']) if k['riskiyot'] else None
        rows.append(k)
    rk = [r['ennakoivaPros'] for r in rows if r['riskiyot'] >= 3]
    rh = [r['ehtiPros'] for r in rows if r['liukasYot'] >= 2]
    return {'v': VERSION, 'yot': nights, 'mukana': sum(1 for p in nights if json.load(open('suomi/%s.json' % p)).get('toteumat', True)), 'urakat': sorted(rows, key=lambda r: r['u']),
            'maa': {'urakoita': len(rows), 'ennakoivaMed': round(statistics.median(rk)) if rk else None,
                    'ehtiMed': round(statistics.median(rh)) if rh else None}}


def write(ev, U):
    N = night(ev, U)
    os.makedirs('suomi', exist_ok=True)
    json.dump(N, open('suomi/%s.json' % ev, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    r = N['urakat']
    print('Suomi yö %s: %d urakkaa, riskiyö %d, suolasi %d, ennakoiva %d, nopea %d, myöhäinen %d, ei %d' % (
        ev, len(r), sum(x['riski'] for x in r), sum(1 for x in r if x['suola']),
        *[sum(1 for x in r if x['luokka'] == l) for l in ('ennakoiva', 'nopea', 'myohainen', 'ei')]))
    return N


def main(argv):
    now = datetime.now(timezone.utc)
    U = urakat(now.astimezone(HEL).date(), force='--urakat' in argv)
    if not U: return
    evs = []
    if '--yo' in argv:
        evs = [argv[argv.index('--yo') + 1]]
    elif '--alku' in argv:
        a = date.fromisoformat(argv[argv.index('--alku') + 1])
        b = date.fromisoformat(argv[argv.index('--loppu') + 1]) if '--loppu' in argv else now.astimezone(HEL).date() - timedelta(days=1)
        while a <= b: evs.append(a.isoformat()); a += timedelta(days=1)
    else:
        ev = (now.astimezone(HEL) - timedelta(days=1)).date().isoformat()
        fr, to, _ = window(ev)
        if to <= now <= to + timedelta(hours=RECOMPUTE_H) or not os.path.exists('suomi/%s.json' % ev):
            if now >= to: evs = [ev]
    last = None
    for ev in evs:
        last = write(ev, U)
    if not evs: return
    K = kausi()
    if last is None and K['yot']:
        last = json.load(open('suomi/%s.json' % K['yot'][-1], encoding='utf-8'))
    K['viimeisin'] = last
    K['note'] = ('Urakat urakkakoodeina (Väylävirasto). Riski: tienpinta ≤ 0 °C ja kuura (kastepiste ≥ tienpinta), märkä tie tai sade, '
                 'tai lumisade, vähintään 1 h ja vähintään 20 %:lla urakan asemista. Toimenpiteet: kirjaukset 1 km päässä urakan asemista. '
                 'Ennakoiva = suolattu 0–6 h ennen riskin alkua (suolaus luetaan klo 15 alkaen), nopea = alle 2 h alusta. '
                 'Havaittu liukkaus = optinen kitka alle 0,6 kylmällä tiellä vähintään '
                 '1 h yhdellä asemalla (noin puolella asemista on optinen anturi). Poikkeavat anturit (tienpinta yli 4 °C muista, '
                 'kitka-anturi liukas lämpimällä tiellä) jätetään pois.')
    os.makedirs('data', exist_ok=True)
    json.dump(K, open('data/suomi.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))


if __name__ == '__main__':
    main(sys.argv[1:])
