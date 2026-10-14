// Jälkitarkistus koko Suomen aineistolla: kelisivun liukkaussäännöt ajetaan jälkikäteen Tiesää-arkiston asemille.
// Säännöt haetaan suoraan kelisivun keruusta (Sambbor/Vantaakeli collector/collect.mjs, lohko LIUKKAUSSÄÄNNÖT),
// joten tarkistus käyttää aina samoja sääntöjä kuin sivu.
//
// Jokaiselle asemalle ja tunnille: liukkausindeksi +2/+6/+12 h (aseman mittaus, Fintrafficin tienpintaennuste ja
// Ilmatieteen laitoksen ennuste sillä hetkellä) verrataan aseman myöhempään mittaukseen (liukas havainto, obsSlippery).
// Lisäksi kalibrointitaulukot: kuuran havaitseminen kuurakertymän mukaan ja liukkaus suolatulla / suolaamattomalla
// märällä tiellä tienpinnan mukaan.
//
// Päivä käsitellään, kun seuraava päivä on kokonaan arkistossa (+12 h tarkistus). Tulokset: retro/days/YYYY-MM-DD.json,
// yhteenveto retro/summary.json ja retro/raportti.md. Sääntöversion vaihtuessa viimeiset 60 päivää lasketaan uudelleen.
import fs from 'node:fs';
import zlib from 'node:zlib';

const RULES_URL = 'https://raw.githubusercontent.com/Sambbor/Vantaakeli/main/collector/collect.mjs';
const VERSION = 'rt2';   // 15.10.: tienpinta +0,5 °C mukaan suolataulukon ylimpään luokkaan
const LEADS = [2, 6, 12];
const MATCH_MIN = 40;          // myöhempi mittaus enintään näin kaukana tarkistushetkestä
const RECOMPUTE_DAYS = 60;
const H = 36e5;

async function loadRules(){
  const src = process.env.RULES_FILE ? fs.readFileSync(process.env.RULES_FILE, 'utf8') : await (await fetch(RULES_URL)).text();   // RULES_FILE: paikallinen testaus
  const a = src.indexOf('// ===== LIUKKAUSSÄÄNNÖT'), b = src.indexOf('// ===== /LIUKKAUSSÄÄNNÖT');
  if(a < 0 || b < 0) throw new Error('sääntölohkoa ei löytynyt kelisivun keruusta');
  return new Function(src.slice(a, b) + '\nreturn {RULES_VERSION, slipSeriesCore, obsSlippery, frostAccHist, frostPt, WET_KELI, WARN_RANK, FROST_SLIP, SALT_LIMIT};')();
}

function parseCsv(txt){
  const lines = txt.split('\n').filter(l => l.length);
  if(!lines.length) return [];
  const split = l => { const out = []; let cur = '', q = false;
    for(let i = 0; i < l.length; i++){ const ch = l[i];
      if(q){ if(ch === '"'){ if(l[i+1] === '"'){ cur += '"'; i++; } else q = false; } else cur += ch; }
      else if(ch === '"') q = true; else if(ch === ','){ out.push(cur); cur = ''; } else cur += ch; }
    out.push(cur); return out; };
  const h = split(lines[0]);
  return lines.slice(1).map(l => { const v = split(l), o = {}; h.forEach((k, i) => { o[k] = v[i] ?? ''; }); return o; });
}
function readDay(prefix, day){
  const cur = `data/current/${prefix}-${day}.csv`, arc = `archive/${day.slice(0, 7)}/${prefix}-${day}.csv.gz`;
  try{ if(fs.existsSync(cur)) return parseCsv(fs.readFileSync(cur, 'utf8')); }catch(e){}
  try{ if(fs.existsSync(arc)) return parseCsv(zlib.gunzipSync(fs.readFileSync(arc)).toString('utf8')); }catch(e){}
  return null;
}
const num = v => v === '' || v == null ? null : (isFinite(+v) ? +v : null);
const iso = t => new Date(t).toISOString().replace(/\.\d+Z$/, 'Z');
const dayStr = t => new Date(t).toISOString().slice(0, 10);
const addDay = (d, n) => dayStr(new Date(d + 'T00:00:00Z').getTime() + n * 864e5);
const load = (p, d) => { try{ return JSON.parse(fs.readFileSync(p, 'utf8')); }catch(e){ return d; } };
const save = (p, o, ind) => { fs.mkdirSync(p.split('/').slice(0, -1).join('/') || '.', {recursive: true}); fs.writeFileSync(p, JSON.stringify(o, null, ind)); };

function availableDays(){
  const days = new Set();
  const add = f => { const m = f.match(/^obs-(\d{4}-\d{2}-\d{2})\.csv(\.gz)?$/); if(m) days.add(m[1]); };
  try{ fs.readdirSync('data/current').forEach(add); }catch(e){}
  try{ for(const m of fs.readdirSync('archive')) fs.readdirSync('archive/' + m).forEach(add); }catch(e){}
  return [...days].sort();
}

// asemarivi → säännöille sopiva havainto
function obsOf(r, R){
  const tr = [num(r.tr1), num(r.tr2)].filter(v => v != null);
  const k1 = num(r.keli1), k2 = num(r.keli2);
  const w = [num(r.warn1), num(r.warn2)].filter(v => v != null);
  const fr = [num(r.fric1), num(r.fric2)].filter(v => v != null);
  const td = num(r.td);
  return {t: new Date(r.mt).getTime(), tr: tr.length ? Math.min(...tr) : null, ta: num(r.ta), td, fp: num(r.fp) ?? (td != null ? R.frostPt(td) : null),
    keli: k1 > 0 ? k1 : (k2 > 0 ? k2 : k1), warn: w.length ? w.reduce((a, x) => (R.WARN_RANK[x] ?? 0) > (R.WARN_RANK[a] ?? -1) ? x : a, -1) : null,
    fric: fr.length ? Math.min(...fr) : null, water: num(r.water1), snow: num(r.snow1), ice: num(r.ice1), tf: num(r.tf1), salt: num(r.salt1),
    rain: num(r.rain), raw: r};
}
function fcList(o){
  const r = o.raw, out = [], reason = p => ({roadCondition: r[p + '_rc'] || undefined, frictionCondition: r[p + '_fc'] || undefined,
    freezingRainCondition: r[p + '_fz'] === '1', winterSlipperiness: r[p + '_sl'] === '1'});
  if(num(r.fo_tr) != null) out.push({type: 'OBSERVATION', time: iso(o.t), roadTemperature: num(r.fo_tr), forecastConditionReason: {roadCondition: r.fo_rc || undefined}});
  for(const [n, p, L] of [['2h', 'f2', 2], ['4h', 'f4', 4], ['6h', 'f6', 6], ['12h', 'f12', 12]])
    if(num(r[p + '_tr']) != null) out.push({type: 'FORECAST', forecastName: n, time: iso(o.t + L * H), roadTemperature: num(r[p + '_tr']), forecastConditionReason: reason(p)});
  return out;
}
function fmiRows(issue, T){
  const h0 = Math.floor(T / H) * H, rows = [];
  for(let L = 0; L <= 24; L++){
    const t = issue.h0 + L * H; if(t < h0) continue;
    const g = k => num(issue.r[k + String(L).padStart(2, '0')]);
    if(g('t') == null) continue;
    rows.push({t: iso(t), Temperature: g('t'), DewPoint: g('td'), Precipitation1h: g('p') ?? 0, WeatherSymbol3: g('sym'), TotalCloudCover: g('cc'), WindSpeedMS: g('ws')});
  }
  return rows;
}
const nearest = (arr, t) => { let lo = 0, hi = arr.length - 1, best = null;   // arr aikajärjestyksessä
  while(lo <= hi){ const m = (lo + hi) >> 1; if(arr[m].t < t) lo = m + 1; else hi = m - 1; }
  for(const i of [lo - 1, lo]) if(arr[i] && (!best || Math.abs(arr[i].t - t) < Math.abs(best.t - t))) best = arr[i];
  return best && Math.abs(best.t - t) <= MATCH_MIN * 6e4 ? best : null; };
function obsReason(o){
  if([5, 6, 7, 9].includes(o.keli)) return {5: 'keli kuura', 6: 'keli lumi', 7: 'keli jää', 9: 'keli sohjo'}[o.keli];
  if(o.warn === 2) return 'varoitus häly';
  if(o.fric != null && o.fric < 0.45) return 'kitka < 0,45';
  if((o.ice || 0) >= 0.1) return 'jäätä tiellä';
  if((o.snow || 0) > 0.2) return 'lunta tiellä';
  return 'muu';
}
const FROST_BINS = [[0, 0.5, '0–0,5'], [0.5, 2, '0,5–2'], [2, 4, '2–4'], [4, 8, '4–8'], [8, 1e9, 'yli 8']];
const TR_BINS = [[-2, 0.51, '−2…+0,5'], [-4, -2, '−4…−2'], [-6, -4, '−6…−4'], [-8, -6, '−8…−6'], [-1e9, -8, 'alle −8']];
const binOf = (bins, v) => (bins.find(([a, b]) => v >= a && v < b) || [])[2];
const C0 = () => ({hit: 0, miss: 0, fa: 0, cn: 0});

function processDay(day, R, prov){
  const obsRows = [addDay(day, -1), day, addDay(day, 1)].flatMap(d => readDay('obs', d) || []);
  const fcRows = [addDay(day, -1), day].flatMap(d => readDay('fmi-fc', d) || []);
  const byS = new Map();
  for(const r of obsRows){ if(!r.mt) continue; const o = obsOf(r, R); if(!isFinite(o.t)) continue; (byS.get(r.st) || byS.set(r.st, []).get(r.st)).push(o); }
  for(const a of byS.values()) a.sort((x, y) => x.t - y.t);
  const issues = new Map();
  for(const r of fcRows){ const h0 = new Date(r.h0).getTime(), t = new Date(r.t).getTime(); if(!isFinite(h0)) continue; (issues.get(r.st) || issues.set(r.st, []).get(r.st)).push({t, h0, r}); }
  for(const a of issues.values()) a.sort((x, y) => x.t - y.t);
  const d0 = new Date(day + 'T00:00:00Z').getTime(), d1 = d0 + 864e5;
  const res = {day, rv: R.RULES_VERSION, v: VERSION, samples: 0, stations: 0, lead: {}, byProv: {}, byWhy: {}, missObs: {}, frost: {}, salt: {}};
  for(const L of LEADS) res.lead[L] = C0();
  for(const [st, arr] of byS){
    const iss = issues.get(st) || []; let used = false, lastHour = -1;
    for(const o of arr){
      if(o.t < d0 || o.t >= d1 || o.tr == null) continue;
      const hour = Math.floor(o.t / H); if(hour === lastHour) continue; lastHour = hour;   // yksi laskenta tunnissa
      const is = [...iss].reverse().find(x => x.t <= o.t + 5 * 6e4); if(!is) continue;
      const rows = fmiRows(is, o.t); if(rows.length < 13) continue;
      const hist = arr.filter(x => x.t > o.t - 12 * H && x.t <= o.t && x.tr != null).map(x => [x.t, x.tr, x.fp]);
      const frAcc0 = hist.length >= 2 ? R.frostAccHist(hist) : 0;
      const wetNow = (o.water != null && o.water > 0.03) || (o.snow || 0) > 0 || (o.ice || 0) > 0 || R.WET_KELI.includes(o.keli) ? 1 : 0;
      const slipNow = R.obsSlippery(o);
      let ser;
      try{ ser = R.slipSeriesCore({now: o.t, rows, trNow: o.tr, fc: fcList(o), tf0: Math.min(0, o.tf ?? 0), wetNow, slipNow, dewNow: o.td, bias: null, frAcc0}); }catch(e){ continue; }
      used = true; res.samples++;
      const p = prov[st] || 'tuntematon';
      for(const L of LEADS){
        const c = ser.find(c => Math.abs(c.lead - L) < 0.5); if(!c || c.idx == null) continue;
        const later = nearest(arr, o.t + L * H); if(!later) continue;
        const pr = c.idx >= 50, ob = R.obsSlippery(later), k = pr && ob ? 'hit' : !pr && ob ? 'miss' : pr ? 'fa' : 'cn';
        res.lead[L][k]++;
        if(L === 6){
          (res.byProv[p] = res.byProv[p] || C0())[k]++;
          if(pr){ const w = res.byWhy[c.why || '?'] = res.byWhy[c.why || '?'] || {hit: 0, fa: 0}; w[ob ? 'hit' : 'fa']++; }
          if(!pr && ob){ const why = obsReason(later); res.missObs[why] = (res.missObs[why] || 0) + 1; }
        }
      }
      // kuuran kalibrointi: tie ≤ +0,5 °C, ei suolan suojaa – havaitaanko kuura kertymän mukaan
      if(o.tr <= 0.5 && !(o.tf != null && o.tf <= -1 && o.tr > R.SALT_LIMIT)){
        const b = binOf(FROST_BINS, frAcc0); const f = res.frost[b] = res.frost[b] || {n: 0, frost: 0, warn: 0, slip: 0};
        f.n++; if(o.keli === 5) f.frost++; if(o.warn === 3) f.warn++; if(slipNow) f.slip++;   // keli 5 = kuura tiellä; varoitus 3 = kuuraava tilanne
      }
      // suolan kalibrointi: märkä tie pakkasella – liukasta 0–6 h sisällä suolan kanssa / ilman, tienpinnan mukaan
      if(wetNow && o.tr <= 0.5 && o.tf != null){
        const b = binOf(TR_BINS, o.tr), sKey = o.tf <= -1 ? 'suolaa' : 'ei suolaa';
        const later6 = arr.some(x => x.t > o.t && x.t <= o.t + 6 * H && R.obsSlippery(x));
        const grp = res.salt[sKey] = res.salt[sKey] || {}, s = grp[b] = grp[b] || {n: 0, slip: 0};
        s.n++; if(later6) s.slip++;
      }
    }
    if(used) res.stations++;
  }
  return res;
}

function addInto(a, b){
  for(const [k, v] of Object.entries(b)){
    if(typeof v === 'number') a[k] = (a[k] || 0) + v;
    else if(v && typeof v === 'object') addInto(a[k] = a[k] || {}, v);
  }
  return a;
}
const pct = (a, b) => b ? Math.round(100 * a / b) : null;
const fmt = v => v == null ? '–' : String(v).replace('.', ',');

function report(S){
  const L = [];
  L.push('# Jälkitarkistus koko Suomen aineistolla', '');
  L.push(`Kelisivun liukkaussäännöt (${S.rv}) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä ${S.days.length} (${S.days[0] || '–'} – ${S.days[S.days.length - 1] || '–'}), laskentoja ${S.samples}. Päivitetty ${S.updated}.`, '');
  L.push('Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Ennuste "liukas" = indeksi ≥ 50.', '');
  L.push('## Osumatarkkuus', '', '| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |', '|---|---|---|---|---|---|---|');
  for(const k of LEADS){ const c = S.lead[k] || C0(); L.push(`| +${k} h | ${c.hit} | ${c.miss} | ${c.fa} | ${c.cn} | ${fmt(pct(c.hit, c.hit + c.miss))} % | ${fmt(pct(c.fa, c.hit + c.fa))} % |`); }
  L.push('', '## Maakunnittain (+6 h)', '', '| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |', '|---|---|---|---|---|');
  for(const [p, c] of Object.entries(S.byProv).sort((a, b) => (b[1].hit + b[1].miss + b[1].fa) - (a[1].hit + a[1].miss + a[1].fa)))
    if(c.hit + c.miss + c.fa) L.push(`| ${p} | ${c.hit} | ${c.miss} | ${c.fa} | ${fmt(pct(c.hit, c.hit + c.miss))} % |`);
  L.push('', '## Hälytyksen syy (+6 h, indeksi ≥ 50)', '', '| Syy | Osui | Turha |', '|---|---|---|');
  for(const [w, c] of Object.entries(S.byWhy).sort((a, b) => (b[1].hit + b[1].fa) - (a[1].hit + a[1].fa))) L.push(`| ${w} | ${c.hit} | ${c.fa} |`);
  L.push('', '## Ohi menneet: mitä asema mittasi (+6 h)', '', '| Havainto | Kpl |', '|---|---|');
  for(const [w, n] of Object.entries(S.missObs).sort((a, b) => b[1] - a[1])) L.push(`| ${w} | ${n} |`);
  L.push('', '## Kuura kuurakertymän mukaan', '', 'Tienpinta enintään +0,5 °C eikä suolan suojaa. Kuinka usein asema mittasi kuuraa tiellä (keli kuura), antoi Kuura-varoituksen (kuuraava tilanne: tie kastepisteen alapuolella) tai mittasi liukasta samalla hetkellä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".', '', '| Kertymä °C·h | Tunteja | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta |', '|---|---|---|---|---|');
  for(const [, , b] of FROST_BINS){ const f = S.frost[b]; if(f) L.push(`| ${b} | ${f.n} | ${f.frost} (${fmt(pct(f.frost, f.n))} %) | ${f.warn ?? 0} (${fmt(pct(f.warn ?? 0, f.n))} %) | ${f.slip} (${fmt(pct(f.slip, f.n))} %) |`); }
  L.push('', '## Märkä tie pakkasella: suolan vaikutus', '', 'Liukasta 6 tunnin sisällä. "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.', '', '| Tienpinta °C | Suolaa: tunteja | liukasta | Ei suolaa: tunteja | liukasta |', '|---|---|---|---|---|');
  for(const [, , b] of TR_BINS){ const a = (S.salt['suolaa'] || {})[b], c = (S.salt['ei suolaa'] || {})[b]; if(a || c)
    L.push(`| ${b} | ${a ? a.n : 0} | ${a ? fmt(pct(a.slip, a.n)) + ' %' : '–'} | ${c ? c.n : 0} | ${c ? fmt(pct(c.slip, c.n)) + ' %' : '–'} |`); }
  L.push('', 'Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0). Säännöt: Sambbor/Vantaakeli, collector/collect.mjs.');
  return L.join('\n') + '\n';
}

async function main(){
  const R = await loadRules();
  const state = load('retro/state.json', {rv: null, done: []});
  const meta = load('meta/stations.json', {});
  const prov = Object.fromEntries(Object.entries(meta).map(([id, m]) => [id, m.prov || 'tuntematon']));
  const days = availableDays(), today = dayStr(Date.now());
  // käsiteltävissä: päivä ja sitä seuraava päivä kokonaan menneitä (seuraavan päivän tiedosto on arkistossa)
  const ready = days.filter(d => addDay(d, 1) < today && days.includes(addDay(d, 1)));
  let todo;
  if(state.rv !== R.RULES_VERSION){ todo = ready.slice(-RECOMPUTE_DAYS); state.done = []; try{ fs.rmSync('retro/days', {recursive: true, force: true}); }catch(e){} }
  else todo = ready.filter(d => !state.done.includes(d));
  for(const d of todo){
    const t0 = Date.now(), res = processDay(d, R, prov);
    save(`retro/days/${d}.json`, res);
    state.done.push(d);
    console.log(`${d}: ${res.samples} laskentaa, ${res.stations} asemaa, +6 h osumat ${res.lead[6].hit} / ohi ${res.lead[6].miss} / turhat ${res.lead[6].fa} (${((Date.now() - t0) / 1000).toFixed(1)} s)`);
  }
  state.rv = R.RULES_VERSION; state.done = [...new Set(state.done)].sort(); state.updated = iso(Date.now());
  save('retro/state.json', state, 1);
  // yhteenveto kaikista saman sääntöversion päivistä
  const S = {rv: R.RULES_VERSION, v: VERSION, updated: iso(Date.now()), days: [], samples: 0, lead: {}, byProv: {}, byWhy: {}, missObs: {}, frost: {}, salt: {}, weeks: {}};
  for(const d of state.done){ const r = load(`retro/days/${d}.json`, null); if(!r || r.rv !== R.RULES_VERSION) continue;
    S.days.push(d); addInto(S, {samples: r.samples, lead: r.lead, byProv: r.byProv, byWhy: r.byWhy, missObs: r.missObs, frost: r.frost, salt: r.salt});
    const dt = new Date(d + 'T00:00:00Z'), th = new Date(dt.getTime() + (3 - ((dt.getUTCDay() + 6) % 7)) * 864e5), y = th.getUTCFullYear();
    const wk = y + '-W' + String(1 + Math.round(((th - new Date(Date.UTC(y, 0, 4))) / 864e5 - 3 + ((new Date(Date.UTC(y, 0, 4)).getUTCDay() + 6) % 7)) / 7)).padStart(2, '0');
    addInto(S.weeks[wk] = S.weeks[wk] || {}, {lead6: r.lead[6], days: 1}); }
  save('retro/summary.json', S, 1);
  fs.writeFileSync('retro/raportti.md', report(S));
  console.log(`Yhteenveto: ${S.days.length} päivää, sääntöversio ${S.rv}, käsitelty nyt ${todo.length} päivää`);
}
main().catch(e => { console.error(e); process.exit(1); });
