# Tiesää-arkisto – koko Suomen tiesääasemat ja tiesääennusteet

Kaikkien Suomen tiesääasemien (noin 525) mittaukset ja lähimmän tiekohdan tiesääennusteet 30 minuutin välein.
Aineistolla opetetaan ja testataan Vantaan hoitourakan liukkausennustetta (https://sambbor.github.io/Vantaakeli/):
kuura, märän tien jäätyminen, suolan teho, tienpintaennusteen virheet. Digitraffic säilyttää asemahistoriaa vain
24 tuntia, joten pidempi aineisto syntyy vain keräämällä.

## Tiedostot
- `data/current/obs-YYYY-MM-DD.csv` – kuluvan päivän rivit (UTC-päivä).
- `archive/YYYY-MM/obs-YYYY-MM-DD.csv.gz` – aiemmat päivät pakattuna.
- `meta/stations.json` – asemat: nimi, sijainti, tie, tieosa, ajorata, urakka, kunta, maakunta.
- `meta/pairs.json` – asema → lähin tiesääennusteen tiekohta (enintään 1 km) ja etäisyys.
- `meta/index.json` – yhteenveto ja sarakkeiden luettelo.

## Sarakkeet
- `t` tallennusaika, `st` asema, `mt` aseman uusin mittausaika (UTC). Rivi tallennetaan vain, kun asemalla on uusi mittaus.
- Mittaukset: `ta` ilma, `td` kastepiste, `rh` kosteus, `fp` kuurapiste, `tr1/tr2` tienpinta, `tg1` maa, `safe1` turvallisuuslämpö,
  `keli1/keli2` keli (0 vika, 1 kuiva, 2 kostea, 3 märkä, 4 märkä ja suolattu, 5 kuura, 6 lumi, 7 jää, 8 tod. kostea ja suolainen, 9 sohjoinen),
  `okeli1` optisen anturin keli, `surf1` tienpinnan tila, `warn1/warn2` varoitus (0 OK, 1 Varo, 2 Häly, 3 Kuura, 4 Sade),
  `tf1/tf2` jäätymispiste, `salt1` suolan määrä, `saltc1` suolan väkevyys, `moist1` kosteuden määrä, `water1/snow1/ice1` vesi/lumi/jää (mm),
  `fric1/fric2` kitka, `rain` sade (0 pouta, 1–3 vesi, 4–6 lumi/räntä), `rain_i` intensiteetti, `rain_form` olomuoto (PWD),
  `rain24` 24 h sadesumma, `wx` vallitseva sää, `vis` näkyvyys km, `ws/wg/wd` tuuli, `light` valoisaa.
  Yli 2 h vanhat anturilukemat jätetään tyhjiksi.
- Ennuste (`sec` tiekohta, `sec_d` etäisyys m): `fo_*` mallin nykytila, `f2_* f4_* f6_* f12_*` ennusteet:
  `tr` tienpinta, `ta` ilma, `ws` tuuli, `sym` sääsymboli, `ov` yleiskeli, `rc` tienpinnan ennustettu tila, `pc` sade,
  `fc` kitka, `fz` jäätävä sade, `sl` talviliukkaus, `rel` luotettavuus.

Lähde: Fintraffic / digitraffic.fi, lisenssi CC BY 4.0.
