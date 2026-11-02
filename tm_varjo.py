#!/usr/bin/env python3
# Oma tienpintamalli – varjoajo (tv1, 2.11.2026, Samuli: "Aloitetaan varjoajo").
# Sama korjausmalli kuin viikkoarviossa (claude/tienpintamalli_viikko.py, tm1): HistGradientBoosting ennustaa virheen
# sivun ennusteeseen (Digitrafficin tiekohtaennuste kiinnitettynä aseman mittaukseen, kiinnitys laimenee 12 h:ssa).
#
#   python3 tm_varjo.py train     opettaa mallit koko arkistolla (+2/+4/+6/+12 h) → .tm_model/model.pkl
#                                  (tienpintamalli.yml kerran vuorokaudessa; malli säilytetään Actionsin välimuistissa, ei säilössä)
#   python3 tm_varjo.py predict   arkistoajon lopussa: ennuste Vantaan asemille, aiempien ennusteiden tarkistus mittauksia vasten
#                                  → tm/latest.json, tm/verif-YYYY-MM.csv, tm/verif.json (kelisivun Seuranta-välilehti lukee)
#
# Varjo: ei vaikuta kelisivun liukkausindeksiin, varjokomentoon eikä puhelinilmoituksiin.
import sys, os, glob, json, pickle, time
import numpy as np, pandas as pd, warnings
warnings.simplefilter('ignore', pd.errors.PerformanceWarning)

H = [2, 4, 6, 12]
VANTAA = {1034, 1041, 1004, 1005, 1115, 1011, 1036, 1084, 1085, 1117}
MODEL = '.tm_model/model.pkl'
TM = 'tm'
HIST_H = 8          # tm/hist-*: Vantaan asemien viimeiset 8 h (vuorokauden vaihde: eilisen palat ovat jo arkistossa)
TV = 'tv1'
P_COLS = ['t0', 'st', 'h', 'tt', 'tr0', 'dig', 'sivu', 'malli']
V_COLS = P_COLS + ['y', 'ymt']


def feats(h):
    return ['tr1', 'ta', 'td', 'fp', 'tr_fp', 'tr_ta', 'tg1', 'ws', 'water1', 'ice1', 'snow1', 'rain', 'light', 'keli1', 'dtr1', 'dtr3', 'dta1', 'dta3',
            'fo_tr', 'off', 'fh', 'fh_ta', 'fh_ws', 'fh_drop', 'f2_tr', 'f6_tr', 'f12_tr', 'fmi_t0', 'fmi_td0', f'fmi_t{h}', f'fmi_td{h}', f'fmi_cc{h}', 'fmi_cc0',
            f'fmi_p{h}', f'fmi_ws{h}', 'fmi_dt', 'hour_t', 'hour_n', 'lat', 'lon']


def read_kind(kind, archive=True, today_only=False):
    f = sorted(glob.glob(f'archive/*/{kind}-*.csv.gz')) if archive else []
    cur = sorted(glob.glob(f'data/current/{kind}-*/*.csv')) + sorted(glob.glob(f'data/current/{kind}-*.csv'))
    if today_only:
        day = time.strftime('%Y-%m-%d', time.gmtime())
        cur = [x for x in cur if day in x]
    a = []
    for x in f + cur:
        try:
            a.append(pd.read_csv(x, low_memory=False))
        except Exception as e:
            print('ohitettu', x, e)
    return pd.concat(a, ignore_index=True) if a else pd.DataFrame()


def num(df, cols):
    for c in cols:
        if c in df:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    return df


def prep_obs(d, S):
    """Asemamittaukset: siivous ja 1 h / 3 h muutokset (sama kuin viikkoarviossa)."""
    d = d.copy()
    d['mt'] = pd.to_datetime(d.mt, utc=True, format='ISO8601')
    d['st'] = pd.to_numeric(d.st, errors='coerce')
    d = num(d, [c for c in d.columns if c not in ('t', 'mt')])
    d = d.dropna(subset=['tr1', 'st']).drop_duplicates(['st', 'mt'])
    d['st'] = d.st.astype(int)
    d = d[(d.keli1 != 0) & (d.tr1 < 40) & (d.tr1 > -40)].sort_values('mt').reset_index(drop=True)
    d['lat'] = d.st.astype(str).map(lambda s: (S.get(s) or {}).get('lat'))
    d['lon'] = d.st.astype(str).map(lambda s: (S.get(s) or {}).get('lon'))
    base = d[['st', 'mt', 'tr1', 'ta']].sort_values('mt')
    for k in [1, 3]:
        x = d[['st', 'mt']].copy(); x['tq'] = x.mt - pd.Timedelta(hours=k); x = x.reset_index().sort_values('tq')
        m = pd.merge_asof(x, base.rename(columns={'mt': 'tq', 'tr1': 'trp', 'ta': 'tap'}), on='tq', by='st',
                          tolerance=pd.Timedelta(minutes=20), direction='nearest').set_index('index').sort_index()
        d[f'dtr{k}'] = d.tr1 - m.trp; d[f'dta{k}'] = d.ta - m.tap
    return d


def prep_fc(F):
    F = F.copy()
    F['t'] = pd.to_datetime(F.t, utc=True, format='ISO8601'); F['h0'] = pd.to_datetime(F.h0, utc=True, format='ISO8601')
    F['st'] = pd.to_numeric(F.st, errors='coerce'); F = F.dropna(subset=['st']); F['st'] = F.st.astype(int)
    return F.sort_values('t')


def add_fmi(d, F):
    """Ilmatieteen laitoksen ennuste (viimeisin enintään 4 h vanha anto) +0/2/4/6/12 h aseman mittaushetkestä."""
    if not len(F):   # ennustetta ei (vielä) ole: sarakkeet tyhjinä, malli selviää puuttuvista arvoista
        for hh in [0, 2, 4, 6, 12]:
            for v in ['t', 'td', 'cc', 'p', 'ws']:
                d[f'fmi_{v}{hh}'] = np.nan
        return d
    x = d[['st', 'mt']].reset_index().sort_values('mt')
    M = pd.merge_asof(x, F, left_on='mt', right_on='t', by='st', tolerance=pd.Timedelta(hours=4), direction='backward').set_index('index').sort_index()
    for hh in [0, 2, 4, 6, 12]:
        k = np.round(((d.mt + pd.Timedelta(hours=hh)) - M.h0).dt.total_seconds() / 3600)
        for v in ['t', 'td', 'cc', 'p', 'ws']:
            out = np.full(len(d), np.nan)
            for kk in range(25):
                c = f'{v}{kk:02d}'
                if c in M:
                    sel = (k == kk).values; out[sel] = pd.to_numeric(M[c], errors='coerce').values[sel]
            d[f'fmi_{v}{hh}'] = out
    return d


loc = lambda t: t.dt.tz_convert('Europe/Helsinki')


def hframe(d, h):
    """Ennustepituuden h piirteet; vain rivit, joilla on Digitrafficin ennuste ja mallitila."""
    m = d.copy(); m['tt'] = m.mt + pd.Timedelta(hours=h)
    m = m.dropna(subset=[f'f{h}_tr', 'fo_tr'])
    lt = loc(m.tt); m['hour_t'] = lt.dt.hour + lt.dt.minute / 60; m['hour_n'] = loc(m.mt).dt.hour
    m['off'] = m.tr1 - m.fo_tr; m['fh'] = m[f'f{h}_tr']; m['fh_ta'] = m[f'f{h}_ta']; m['fh_ws'] = m[f'f{h}_ws']
    m['fh_drop'] = m.fh - m.fo_tr; m['fmi_dt'] = m[f'fmi_t{h}'] - m.fmi_t0; m['tr_fp'] = m.tr1 - m.fp; m['tr_ta'] = m.tr1 - m.ta
    for c in feats(h):
        if c not in m:
            m[c] = np.nan
    return m


sivu = lambda q, h: q.fh + q.off * max(0, 1 - h / 12)


def train():
    from sklearn.ensemble import HistGradientBoostingRegressor as HGB
    import sklearn
    S = json.load(open('meta/stations.json'))
    t0 = time.time()
    d = add_fmi(prep_obs(read_kind('obs'), S), prep_fc(read_kind('fmi-fc')))
    tg = d[['st', 'mt', 'tr1']].rename(columns={'mt': 'tt', 'tr1': 'y'}).sort_values('tt')
    models, rows = {}, {}
    for h in H:
        x = hframe(d, h).reset_index(drop=True).sort_values('tt')
        m = pd.merge_asof(x, tg, on='tt', by='st', tolerance=pd.Timedelta(minutes=15), direction='nearest').dropna(subset=['y'])
        g = HGB(max_iter=400, learning_rate=0.05, max_leaf_nodes=31, min_samples_leaf=50, l2_regularization=1.0, random_state=0)
        g.fit(m[feats(h)], m.y - sivu(m, h))
        models[h] = g; rows[h] = int(len(m))
        print(f'+{h} h: {len(m)} opetusriviä')
    info = {'v': TV, 'trained': pd.Timestamp.now(tz='UTC').strftime('%Y-%m-%dT%H:%MZ'), 'from': d.mt.min().strftime('%Y-%m-%dT%H:%MZ'),
            'to': d.mt.max().strftime('%Y-%m-%dT%H:%MZ'), 'stations': int(d.st.nunique()), 'rows': rows, 'sklearn': sklearn.__version__, 'sec': round(time.time() - t0)}
    os.makedirs(os.path.dirname(MODEL), exist_ok=True)
    with open(MODEL, 'wb') as f:
        pickle.dump({'info': info, 'models': models}, f)
    json.dump(info, open(os.path.join(os.path.dirname(MODEL), 'info.json'), 'w'))
    print('Malli tallennettu:', json.dumps(info, ensure_ascii=False))


def read_csv_safe(p, **kw):
    try:
        return pd.read_csv(p, **kw)
    except Exception:
        return pd.DataFrame()


def predict_step(M, S, obs_new, fc_new, now, out=TM):
    """Yksi varjoajo: päivittää historian, tekee ennusteet ja tarkistaa vanhat. Palauttaa (uudet ennusteet, tarkistetut)."""
    os.makedirs(out, exist_ok=True)
    now = pd.Timestamp(now).tz_convert('UTC') if pd.Timestamp(now).tzinfo else pd.Timestamp(now, tz='UTC')
    # historia: Vantaan asemat, viimeiset HIST_H tuntia (raakarivit, jotta vuorokauden vaihde ei katkaise 1 h / 3 h muutoksia)
    ho = read_csv_safe(f'{out}/hist-obs.csv.gz', low_memory=False); hf = read_csv_safe(f'{out}/hist-fc.csv.gz', low_memory=False)
    pick = lambda df: df[pd.to_numeric(df.st, errors='coerce').isin(VANTAA)] if len(df) else df
    ho = pd.concat([ho, pick(obs_new)], ignore_index=True); hf = pd.concat([hf, pick(fc_new)], ignore_index=True)
    if len(ho):
        ho['_m'] = pd.to_datetime(ho.mt, utc=True, format='ISO8601')
        ho = ho[(ho._m >= now - pd.Timedelta(hours=HIST_H)) & (ho._m <= now + pd.Timedelta(minutes=5))].drop_duplicates(['st', 'mt']).drop(columns='_m')
    if len(hf):
        hf['_h'] = pd.to_datetime(hf.h0, utc=True, format='ISO8601')
        hf = hf[(hf._h >= now - pd.Timedelta(hours=HIST_H)) & (hf._h <= now + pd.Timedelta(minutes=5))].drop_duplicates(['st', 'h0']).drop(columns='_h')
    ho.to_csv(f'{out}/hist-obs.csv.gz', index=False); hf.to_csv(f'{out}/hist-fc.csv.gz', index=False)
    if not len(ho):
        return pd.DataFrame(columns=P_COLS), pd.DataFrame(columns=V_COLS)
    d = prep_obs(ho, S)
    d = add_fmi(d, prep_fc(hf) if len(hf) else hf)
    # ennusteet: aseman uusin mittaus, enintään 45 min vanha
    last = d[d.mt >= now - pd.Timedelta(minutes=45)].sort_values('mt').groupby('st').tail(1)
    new = []
    if M is not None and len(last):
        for h in H:
            q = hframe(last, h)
            if not len(q):
                continue
            g = M['models'][h]
            s = sivu(q, h)
            new.append(pd.DataFrame({'t0': q.mt.dt.strftime('%Y-%m-%dT%H:%M:%SZ'), 'st': q.st, 'h': h, 'tt': q.tt.dt.strftime('%Y-%m-%dT%H:%M:%SZ'),
                                     'tr0': q.tr1, 'dig': q.fh, 'sivu': s.round(2), 'malli': (s + g.predict(q[feats(h)])).round(2)}))
    new = pd.concat(new, ignore_index=True) if new else pd.DataFrame(columns=P_COLS)
    # odottavat ennusteet ja tarkistus: lähin mittaus ±15 min kohdehetkestä, kun kohdehetkestä on kulunut ≥ 15 min
    pend = read_csv_safe(f'{out}/pending.csv')
    pend = pd.concat([pend, new], ignore_index=True).drop_duplicates(['t0', 'st', 'h']) if len(pend) else new.copy()
    ver = pd.DataFrame(columns=V_COLS)
    if len(pend):
        pt = pd.to_datetime(pend.tt, utc=True, format='ISO8601')
        ripe = pt <= now - pd.Timedelta(minutes=15)
        obs = d[['st', 'mt', 'tr1']].sort_values('mt')
        if ripe.any():
            r = pend[ripe].copy(); r['_t'] = pt[ripe]; r['st'] = r.st.astype(int)
            r = pd.merge_asof(r.reset_index().sort_values('_t'), obs.rename(columns={'mt': '_t', 'tr1': 'y'}).assign(ymt=lambda o: o._t),
                              on='_t', by='st', tolerance=pd.Timedelta(minutes=15), direction='nearest').set_index('index')
            ok = r.y.notna()
            ver = r[ok].copy(); ver['ymt'] = ver.ymt.dt.strftime('%Y-%m-%dT%H:%M:%SZ'); ver = ver[V_COLS]
            gone = r.index[ok].tolist() + r.index[(~ok) & (r._t < now - pd.Timedelta(hours=2))].tolist()   # ei mittausta 2 h kuluessa → pois
            pend = pend.drop(index=gone)
    pend[P_COLS].to_csv(f'{out}/pending.csv', index=False)
    if len(ver):
        for mon, g in ver.groupby(ver.tt.str.slice(0, 7)):
            p = f'{out}/verif-{mon}.csv'
            g.to_csv(p, mode='a', header=not os.path.exists(p), index=False)
    return new, ver


def stats(v):
    out = {}
    for h in H:
        x = v[v.h == h]
        if not len(x):
            continue
        r = {'n': int(len(x))}
        for k in ['dig', 'sivu', 'malli']:
            e = x[k] - x.y
            r[k] = {'mae': round(float(e.abs().mean()), 2), 'bias': round(float(e.mean()), 2)}
        z = x[x.y.between(-2, 2)]   # nollaraja: tie −2…+2 °C kohdehetkellä – osuuko ennuste samalle puolelle nollaa
        if len(z):
            r['zero'] = {'n': int(len(z)), **{k: round(float(((z[k] <= 0) == (z.y <= 0)).mean() * 100)) for k in ['dig', 'sivu', 'malli']}}
        out[str(h)] = r
    return out


def summary(M, now, out=TM):
    fs = sorted(glob.glob(f'{out}/verif-*.csv'))[-3:]
    v = pd.concat([read_csv_safe(f) for f in fs], ignore_index=True) if fs else pd.DataFrame(columns=V_COLS)
    res = {'v': TV, 'updated': pd.Timestamp(now).strftime('%Y-%m-%dT%H:%MZ'), 'model': M['info'] if M else None, 'stations': sorted(VANTAA),
           'note': 'Varjoajo: ei vaikuta kelisivun liukkausindeksiin. sivu = Digitrafficin tiekohtaennuste kiinnitettynä aseman mittaukseen (kiinnitys laimenee 12 h:ssa), '
                   'malli = sivu + opittu korjaus. Virhe = ennuste − mitattu (°C), + = liian lämmin. zero = osuuko ennuste samalle puolelle nollaa, kun tie on mitattuna −2…+2 °C (%).'}
    if len(v):
        v = v.dropna(subset=['y']).drop_duplicates(['t0', 'st', 'h'])
        tt = pd.to_datetime(v.tt, utc=True, format='ISO8601'); lh = loc(tt).dt.hour
        night = (lh >= 18) | (lh < 8); cold = v.tr0.between(-4, 4)
        res['since'] = tt.min().strftime('%Y-%m-%dT%H:%MZ')
        win = {'7': tt >= pd.Timestamp(now) - pd.Timedelta(days=7), 'all': tt == tt}
        res['groups'] = {w: {'kaikki': stats(v[m]), 'yo': stats(v[m & night]), 'yo_kylma': stats(v[m & night & cold])} for w, m in win.items()}
        # öittäin (klo 18–08, Suomen aika): 6 h ennusteen keskivirhe
        nv = v[night & (v.h == 6)].copy(); nv['night'] = (loc(tt[night & (v.h == 6)]) - pd.Timedelta(hours=8)).dt.strftime('%Y-%m-%d')
        res['nights'] = [{'night': k, 'n': int(len(g)), 'trMin': round(float(g.y.min()), 1), **{x: round(float((g[x] - g.y).abs().mean()), 2) for x in ['dig', 'sivu', 'malli']}}
                         for k, g in nv.groupby('night')][-14:]
        sv = v[win['7'] & night & (v.h == 6)]
        res['perSt'] = [{'st': int(s), **{x: round(float((g[x] - g.y).abs().mean()), 2) for x in ['sivu', 'malli']}, 'n': int(len(g))} for s, g in sv.groupby('st')]
    json.dump(res, open(f'{out}/verif.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    return res


def latest(M, S, new, now, out=TM):
    L = {'v': TV, 'updated': pd.Timestamp(now).strftime('%Y-%m-%dT%H:%MZ'), 'trained': M['info']['trained'] if M else None, 'st': {}}
    for st, g in new.groupby('st'):
        L['st'][str(int(st))] = {'name': (S.get(str(int(st))) or {}).get('name'), 't0': g.t0.iloc[0], 'tr0': float(g.tr0.iloc[0]),
                                 'f': {str(int(r.h)): {'malli': float(r.malli), 'sivu': float(r.sivu), 'dig': float(r.dig)} for r in g.itertuples()}}
    json.dump(L, open(f'{out}/latest.json', 'w'), ensure_ascii=False, separators=(',', ':'))


def predict():
    S = json.load(open('meta/stations.json'))
    M = None
    if os.path.exists(MODEL):
        with open(MODEL, 'rb') as f:
            M = pickle.load(f)
    else:
        print('Mallia ei ole (välimuisti tyhjä) – vain historia ja tarkistus päivittyvät')
    now = pd.Timestamp.now(tz='UTC')
    new, ver = predict_step(M, S, read_kind('obs', archive=False, today_only=True), read_kind('fmi-fc', archive=False, today_only=True), now)
    latest(M, S, new, now); res = summary(M, now)
    print(f'Varjoennuste: {len(new)} riviä {new.st.nunique() if len(new) else 0} asemalle, tarkistettu {len(ver)}; '
          f'malli opetettu {M["info"]["trained"] if M else "–"}')


if __name__ == '__main__':
    {'train': train, 'predict': predict}[sys.argv[1] if len(sys.argv) > 1 else 'predict']()
