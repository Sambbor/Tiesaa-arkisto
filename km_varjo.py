#!/usr/bin/env python3
# Oma kuurapistemalli – varjoajo (km1, 10.11.2026, Samuli: "Tee molemmat", kierros 2 kohta 3d).
# Kuura ratkeaa erotuksesta tienpinta − kuurapiste (kelikeskuksessa kuurapiste = kastepiste, frostPt), joka on yleensä 0–1 °C.
# Coworkin 7.11. vertailussa ennustetun erotuksen virhe oli noin 1 °C eli yhtä suuri kuin ilmiö. Tämä malli on tienpintamallin (tm_varjo.py,
# tv1) sisarmalli samalla rungolla ja koko Suomen aineistolla:
#   - td:  aseman kastepiste +2/+4/+6/+12 h. Pohja = kelikeskuksen tapa: Ilmatieteen laitoksen kastepiste kiinnitettynä aseman mittaukseen,
#          kiinnitys laimenee 24 h:ssa (laskenta.html TD_DECAY). Malli oppii virheen pohjaan.
#   - ero: suoraan tie − kastepiste samoille pituuksille. Pohja = kelikeskuksen tienpinta (tv1:n "sivu") − pohjan kastepiste. Kahden erikseen
#          ennustetun luvun virheet kertautuvat erotuksessa; suoraan opittu erotus välttää sen.
#
#   python3 km_varjo.py train     opettaa mallit koko arkistolla → .tm_model/km.pkl (tienpintamalli.yml, sama välimuisti kuin tv1).
#                                  Ennen lopullista opetusta testi: opetus ilman viimeistä 7 vrk:ta ja arvio sillä (km/testi.json).
#   python3 km_varjo.py predict   arkistoajon lopussa tm_varjo.py:n jälkeen (käyttää sen historiaa tm/hist-*): ennuste Vantaan asemille ja
#                                  aiempien tarkistus → km/latest.json, km/verif-YYYY-MM.csv, km/verif.json (Päivystyskirjan Seuranta lukee)
#
# Varjo: ei vaikuta kelikeskuksen liukkausindeksiin, varjokomentoon eikä puhelinilmoituksiin.
import sys, os, glob, json, pickle, time
import numpy as np, pandas as pd
import tm_varjo as T

H = T.H
MODEL = '.tm_model/km.pkl'
KM = 'km'
KV = 'km1'
TD_DECAY = 24
KUURA_ERO, KUURA_TR = -0.5, 0.5   # kuuraava: tie vähintään 0,5 °C kastepistettä kylmempi ja tie enintään +0,5 °C (Coworkin määritelmä 7.11.)
P_COLS = ['t0', 'st', 'h', 'tt', 'tr0', 'td0', 'sivu_tr', 'sivu_td', 'malli_td', 'sivu_ero', 'malli_ero']
V_COLS = P_COLS + ['y_tr', 'y_td']


def kfeats(h):
    return T.feats(h) + ['rh', 'ero0', f'fmi_td_d{h}']


def frame(d, h):
    m = T.hframe(d, h)
    m['ero0'] = m.tr1 - m.td
    m[f'fmi_td_d{h}'] = m[f'fmi_td{h}'] - m.fmi_td0
    m['sivu_tr'] = T.sivu(m, h)
    m['sivu_td'] = m[f'fmi_td{h}'] + (m.td - m.fmi_td0) * max(0, 1 - h / TD_DECAY)
    m['sivu_ero'] = m.sivu_tr - m.sivu_td
    for c in kfeats(h):
        if c not in m:
            m[c] = np.nan
    return m.dropna(subset=['sivu_td', 'sivu_tr'])


def targets(d):
    return d[['st', 'mt', 'tr1', 'td']].rename(columns={'mt': 'tt', 'tr1': 'y_tr', 'td': 'y_td'}).dropna().sort_values('tt')


def fit(x, h):
    from sklearn.ensemble import HistGradientBoostingRegressor as HGB
    mk = lambda: HGB(max_iter=400, learning_rate=0.05, max_leaf_nodes=31, min_samples_leaf=50, l2_regularization=1.0, random_state=0)
    gtd, gero = mk(), mk()
    gtd.fit(x[kfeats(h)], x.y_td - x.sivu_td)
    gero.fit(x[kfeats(h)], (x.y_tr - x.y_td) - x.sivu_ero)
    return {'td': gtd, 'ero': gero}


def evaluate(x, g, h):
    """Arvio: kastepiste, erotus ja kuuraavat hetket (yö klo 18–08, tie ennustehetkellä −4…+4 °C)."""
    x = x.copy()
    x['malli_td'] = x.sivu_td + g['td'].predict(x[kfeats(h)])
    x['malli_ero'] = x.sivu_ero + g['ero'].predict(x[kfeats(h)])
    x['td_ero'] = x.sivu_tr - x.malli_td
    y_ero = x.y_tr - x.y_td
    lh = T.loc(x.tt).dt.hour
    sel = ((lh >= 18) | (lh < 8)) & x.tr1.between(-4, 4)
    x, y_ero = x[sel], y_ero[sel]
    r = {'n': int(len(x))}
    if not len(x):
        return r
    e = lambda p, y: {'mae': round(float((p - y).abs().mean()), 2), 'bias': round(float((p - y).mean()), 2)}
    r['td'] = {'sivu': e(x.sivu_td, x.y_td), 'malli': e(x.malli_td, x.y_td)}
    r['ero'] = {'sivu': e(x.sivu_ero, y_ero), 'malli_td': e(x.td_ero, y_ero), 'malli': e(x.malli_ero, y_ero)}
    obs = (y_ero <= KUURA_ERO) & (x.y_tr <= KUURA_TR)
    r['kuura'] = {'havaittu': int(obs.sum())}
    for k, p, tr in (('sivu', x.sivu_ero, x.sivu_tr), ('malli_td', x.td_ero, x.sivu_tr), ('malli', x.malli_ero, x.sivu_tr)):
        pr = (p <= KUURA_ERO) & (tr <= KUURA_TR)
        r['kuura'][k] = {'osui': int((pr & obs).sum()), 'ohi': int((~pr & obs).sum()), 'turha': int((pr & ~obs).sum())}
    return r


def train():
    import sklearn
    S = json.load(open('meta/stations.json'))
    t0 = time.time()
    d = T.add_fmi(T.prep_obs(T.read_kind('obs'), S), T.prep_fc(T.read_kind('fmi-fc')))
    tg = targets(d)
    cut = d.mt.max() - pd.Timedelta(days=7)
    models, rows, test = {}, {}, {'v': KV, 'tehty': pd.Timestamp.now(tz='UTC').strftime('%Y-%m-%dT%H:%MZ'),
                                   'testijakso': [cut.strftime('%Y-%m-%dT%H:%MZ'), d.mt.max().strftime('%Y-%m-%dT%H:%MZ')], 'pituudet': {}}
    for h in H:
        x = frame(d, h).reset_index(drop=True).sort_values('tt')
        x = pd.merge_asof(x, tg, on='tt', by='st', tolerance=pd.Timedelta(minutes=15), direction='nearest').dropna(subset=['y_tr', 'y_td'])
        a, b = x[x.tt < cut], x[x.mt >= cut]
        if len(a) > 1000 and len(b):   # testi: opetus ennen testijaksoa, arvio testijaksolla (koko maa ja Vantaa)
            g = fit(a, h)
            test['pituudet'][str(h)] = {'koko_maa': evaluate(b, g, h), 'vantaa': evaluate(b[b.st.isin(T.VANTAA)], g, h)}
        models[h] = fit(x, h); rows[h] = int(len(x))
        print(f'+{h} h: {len(x)} opetusriviä')
    info = {'v': KV, 'trained': pd.Timestamp.now(tz='UTC').strftime('%Y-%m-%dT%H:%MZ'), 'from': d.mt.min().strftime('%Y-%m-%dT%H:%MZ'),
            'to': d.mt.max().strftime('%Y-%m-%dT%H:%MZ'), 'stations': int(d.st.nunique()), 'rows': rows, 'sklearn': sklearn.__version__, 'sec': round(time.time() - t0)}
    os.makedirs(os.path.dirname(MODEL), exist_ok=True)
    with open(MODEL, 'wb') as f:
        pickle.dump({'info': info, 'models': models}, f)
    os.makedirs(KM, exist_ok=True)
    test['malli'] = info
    json.dump(test, open(f'{KM}/testi.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    print('Kuurapistemalli tallennettu:', json.dumps(info, ensure_ascii=False))
    print('Testi:', json.dumps(test['pituudet'].get('6', {}), ensure_ascii=False))


def predict():
    S = json.load(open('meta/stations.json'))
    M = None
    if os.path.exists(MODEL):
        with open(MODEL, 'rb') as f:
            M = pickle.load(f)
    now = pd.Timestamp.now(tz='UTC')
    os.makedirs(KM, exist_ok=True)
    ho = T.read_csv_safe(f'{T.TM}/hist-obs.csv.gz', low_memory=False); hf = T.read_csv_safe(f'{T.TM}/hist-fc.csv.gz', low_memory=False)
    new = pd.DataFrame(columns=P_COLS)
    d = None
    if len(ho):
        d = T.add_fmi(T.prep_obs(ho, S), T.prep_fc(hf) if len(hf) else hf)
        last = d[d.mt >= now - pd.Timedelta(minutes=45)].sort_values('mt').groupby('st').tail(1)
        out = []
        if M is not None and len(last):
            for h in H:
                q = frame(last, h)
                if not len(q):
                    continue
                g = M['models'][h]
                out.append(pd.DataFrame({'t0': q.mt.dt.strftime('%Y-%m-%dT%H:%M:%SZ'), 'st': q.st, 'h': h, 'tt': q.tt.dt.strftime('%Y-%m-%dT%H:%M:%SZ'),
                                         'tr0': q.tr1, 'td0': q.td, 'sivu_tr': q.sivu_tr.round(2), 'sivu_td': q.sivu_td.round(2),
                                         'malli_td': (q.sivu_td + g['td'].predict(q[kfeats(h)])).round(2), 'sivu_ero': q.sivu_ero.round(2),
                                         'malli_ero': (q.sivu_ero + g['ero'].predict(q[kfeats(h)])).round(2)}))
        if out: new = pd.concat(out, ignore_index=True)
    pend = T.read_csv_safe(f'{KM}/pending.csv')
    pend = pd.concat([pend, new], ignore_index=True).drop_duplicates(['t0', 'st', 'h']) if len(pend) else new.copy()
    ver = pd.DataFrame(columns=V_COLS)
    if len(pend) and d is not None:
        pt = pd.to_datetime(pend.tt, utc=True, format='ISO8601'); ripe = pt <= now - pd.Timedelta(minutes=15)
        if ripe.any():
            r = pend[ripe].copy(); r['_t'] = pt[ripe]; r['st'] = r.st.astype(int)
            o = d[['st', 'mt', 'tr1', 'td']].dropna().sort_values('mt').rename(columns={'mt': '_t', 'tr1': 'y_tr', 'td': 'y_td'})
            r = pd.merge_asof(r.reset_index().sort_values('_t'), o, on='_t', by='st', tolerance=pd.Timedelta(minutes=15), direction='nearest').set_index('index')
            ok = r.y_tr.notna() & r.y_td.notna()
            ver = r[ok][V_COLS].copy()
            pend = pend.drop(index=r.index[ok].tolist() + r.index[(~ok) & (r._t < now - pd.Timedelta(hours=2))].tolist())
    pend[P_COLS].to_csv(f'{KM}/pending.csv', index=False)
    if len(ver):
        for mon, g in ver.groupby(ver.tt.str.slice(0, 7)):
            p = f'{KM}/verif-{mon}.csv'
            g.to_csv(p, mode='a', header=not os.path.exists(p), index=False)
    summary(M, now)
    L = {'v': KV, 'updated': now.strftime('%Y-%m-%dT%H:%MZ'), 'trained': M['info']['trained'] if M else None, 'st': {}}
    for st, g in new.groupby('st'):
        L['st'][str(int(st))] = {'name': (S.get(str(int(st))) or {}).get('name'), 't0': g.t0.iloc[0], 'tr0': float(g.tr0.iloc[0]), 'td0': float(g.td0.iloc[0]),
                                 'f': {str(int(r.h)): {'sivu_ero': float(r.sivu_ero), 'malli_ero': float(r.malli_ero), 'malli_td': float(r.malli_td)} for r in g.itertuples()}}
    json.dump(L, open(f'{KM}/latest.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    print(f'Kuurapistevarjo: {len(new)} ennustetta, tarkistettu {len(ver)}; malli opetettu {M["info"]["trained"] if M else "–"}')


def summary(M, now):
    fs = sorted(glob.glob(f'{KM}/verif-*.csv'))[-3:]
    v = pd.concat([T.read_csv_safe(f) for f in fs], ignore_index=True) if fs else pd.DataFrame(columns=V_COLS)
    try:
        test = json.load(open(f'{KM}/testi.json', encoding='utf-8'))
    except Exception:
        test = None
    res = {'v': KV, 'updated': now.strftime('%Y-%m-%dT%H:%MZ'), 'model': M['info'] if M else None, 'testi': test,
           'note': 'Varjoajo: ei vaikuta kelikeskukseen. Erotus = tie − kastepiste (kuurapiste). sivu = kelikeskuksen tapa (Digitrafficin tienpinta '
                   'kiinnitettynä aseman mittaukseen − Ilmatieteen laitoksen kastepiste kiinnitettynä mittaukseen), malli_td = sivun tienpinta − opittu '
                   'kastepiste, malli = suoraan opittu erotus. Kuuraava = tie vähintään 0,5 °C kastepistettä kylmempi ja tie enintään +0,5 °C. '
                   'Yö klo 18–08, tie ennustehetkellä −4…+4 °C.'}
    if len(v):
        v = v.dropna(subset=['y_tr', 'y_td']).drop_duplicates(['t0', 'st', 'h'])
        v['tt'] = pd.to_datetime(v.tt, utc=True, format='ISO8601'); v['mt'] = pd.to_datetime(v.t0, utc=True, format='ISO8601')
        v['tr1'] = v.tr0; v['td_ero'] = v.sivu_tr - v.malli_td
        res['since'] = v.tt.min().strftime('%Y-%m-%dT%H:%MZ')
        out = {}
        for h in H:
            x = v[v.h == h]
            lh = T.loc(x.tt).dt.hour; x = x[((lh >= 18) | (lh < 8)) & x.tr1.between(-4, 4)]
            if not len(x): continue
            y = x.y_tr - x.y_td
            e = lambda p, yy: {'mae': round(float((p - yy).abs().mean()), 2), 'bias': round(float((p - yy).mean()), 2)}
            obs = (y <= KUURA_ERO) & (x.y_tr <= KUURA_TR)
            r = {'n': int(len(x)), 'td': {'sivu': e(x.sivu_td, x.y_td), 'malli': e(x.malli_td, x.y_td)},
                 'ero': {'sivu': e(x.sivu_ero, y), 'malli_td': e(x.td_ero, y), 'malli': e(x.malli_ero, y)}, 'kuura': {'havaittu': int(obs.sum())}}
            for k, p in (('sivu', x.sivu_ero), ('malli_td', x.td_ero), ('malli', x.malli_ero)):
                pr = (p <= KUURA_ERO) & (x.sivu_tr <= KUURA_TR)
                r['kuura'][k] = {'osui': int((pr & obs).sum()), 'ohi': int((~pr & obs).sum()), 'turha': int((pr & ~obs).sum())}
            out[str(h)] = r
        res['vantaa'] = out
    json.dump(res, open(f'{KM}/verif.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    return res


if __name__ == '__main__':
    {'train': train, 'predict': predict}[sys.argv[1] if len(sys.argv) > 1 else 'predict']()
