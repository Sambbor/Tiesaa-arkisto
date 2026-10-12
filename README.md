# Tiesää-arkisto – koko Suomen tiesääasemat ja tiesääennusteet

Kaikkien Suomen tiesääasemien (noin 525) mittaukset ja lähimmän tiekohdan tiesääennusteet 30 minuutin välein,
Ilmatieteen laitoksen ennuste jokaiselle tiesääasemalle 3 tunnin välein sekä Ilmatieteen laitoksen säähavainnot kerran tunnissa.
Aineistolla opetetaan ja testataan Vantaan hoitourakan liukkausennustetta (https://sambbor.github.io/Vantaakeli/):
kuura, märän tien jäätyminen, suolan teho, tienpintaennusteen virheet. Digitraffic säilyttää asemahistoriaa vain
24 tuntia, joten pidempi aineisto syntyy vain keräämällä.

## Tiedostot
- `data/current/obs-YYYY-MM-DD.csv` – kuluvan päivän rivit (UTC-päivä).
- `archive/YYYY-MM/obs-YYYY-MM-DD.csv.gz` – aiemmat päivät pakattuna.
- `meta/stations.json` – asemat: nimi, sijainti, tie, tieosa, ajorata, urakka, kunta, maakunta.
- `meta/pairs.json` – asema → lähin tiesääennusteen tiekohta (enintään 1 km) ja etäisyys.
- `data/current/fmi-fc-YYYY-MM-DD.csv` – Ilmatieteen laitoksen toimitettu ennuste tiesääasemien kohdalle.
- `data/current/fmi-obs-YYYY-MM-DD.csv` – Ilmatieteen laitoksen säähavainnot ja säteily.
- `meta/fmi_stations.json` – Ilmatieteen laitoksen havaintoasemat (fmisid, nimi, sijainti, säteilyasema).
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

## Ilmatieteen laitoksen ennuste (fmi-fc)
3 tunnin välein jokaiselle tiesääasemalle (`st`). `h0` = ennusteen ensimmäinen tunti (UTC), sarakkeet tunneittain 00–24 h:
`tNN` ilma, `tdNN` kastepiste, `pNN` sade mm/h, `symNN` sääsymboli (WeatherSymbol3), `ccNN` pilvisyys %, `wsNN` tuuli m/s.
Samat suureet, joita kelisivun liukkausennuste käyttää, joten malli voidaan opettaa samoilla syötteillä.

## Ilmatieteen laitoksen havainnot (fmi-obs)
Kerran tunnissa kunkin havaintoaseman (`fmisid`) uusin tunti: `ot` havaintoaika, `ta` ilma, `td` kastepiste, `rh` kosteus,
`ws/wg/wd` tuuli, `cc` pilvisyys (oktaa), `snow` lumensyvyys cm, `r1h` sade 1 h, `ri` sateen intensiteetti, `vis` näkyvyys m,
`wawa` sääkoodi. Säteilyasemilta `rt` havaintoaika, `glob` auringon kokonaissäteily, `lwin/lwout` pitkäaaltosäteily alas/ylös,
`dir` suora, `diff` hajasäteily (W/m²).

Lähteet: Fintraffic / digitraffic.fi ja Ilmatieteen laitos (avoin data), lisenssi CC BY 4.0.
