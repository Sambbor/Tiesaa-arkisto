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

## Talvihoidon toteumat (toteumat)
`toteumat.py` ajetaan samassa työnkulussa. Se hakee Digitrafficin kunnossapitoseurannasta valtion maanteiden
suolaus-, auraus- ja hiekoituskirjaukset edellisen ajon jälkeen (limittäin 90 min, tuplat karsitaan) ja tallentaa rivin
jokaiselle tiesääasemalle, jonka 2 km säteellä kone kulki: `data/current/toteumat-YYYY-MM-DD.csv`.
Sarakkeet: `t` keruuaika, `st` asema, `task` salt / plow / sand, `start` ja `end` kirjauksen alku ja loppu (UTC),
`d` lähin etäisyys asemaan m, `rid` kirjauksen tunniste, `sys` lähettävä järjestelmä. tt2 (7.11.2026): `prev` edellisen kirjauksen tunniste (Digitrafficin previousId) ja `ku` koneen urakka: haun kirjaukset ketjutetaan koneittain (previousId tai jatkuvuus 3 min / 300 m), ja ketjun urakka on se, jonka teillä (`meta/urakkaverkko.json.gz`, Väyläviraston hoitourakoiden tiet 250 m ruuduin, päivitys 30 vrk välein) ketjun pisteistä on eniten. Yökooste laskee kirjauksen urakalle vain, jos `ku` on sama tai tyhjä. Paikallaan seisovan koneen kirjaukset jätetään pois.
Tila ja yhteenveto: `meta/toteumat_state.json`. Asemien urakka-alue on tiedostossa `meta/stations.json`.
Käyttö: koko maan urakoiden suolaus- ja auraushetket suhteessa asemien keliin (ennakoiva vai jälkikäteinen toiminta)
ja päivystäjän simulaattorin "mitä oikeasti tehtiin".

## Koko Suomen yökooste (suomi)
`suomi.py` (su1) laskee joka aamu jokaiselle maanteiden hoitourakalle edellisen yön (klo 18–08 Suomen aikaa) riskin ja toimenpiteet:
- `meta/urakat.json`: asema → urakkakoodi (Väylävirasto, Maanteiden hoitourakan tiet; tieosoite urakan tieosuudella). Urakat ovat
  julkisissa tiedostoissa urakkakoodeina ja ELY-alueina, ei nimiä eikä urakoitsijoita.
- `suomi/YYYY-MM-DD.json` (illan päivämäärä): urakoittain asemat, alin tienpinta (2. kylmin asema), riskitunnit ja riskin alku
  (tienpinta ≤ 0 °C ja kuura, märkä tie tai sade, tai lumisade, vähintään 20 %:lla urakan asemista ja vähintään 1 h),
  anturien liukashälytykset, suolaus-, auraus- ja hiekoituskerrat (kirjaus enintään 1 km päässä urakan asemasta) ja ajoitusluokka:
  ennakoiva (suolattu 0–6 h ennen riskin alkua, suolaus luetaan klo 15 alkaen), nopea (alle 2 h), myöhäinen, ei, ilman_riskia,
  ei_tarvetta, tuntematon (toteumakeruussa aukko).
- `data/suomi.json`: kausi urakoittain ja viimeisin yö. Yöt, joilta toteumat puuttuvat, eivät ole mukana kausiluvuissa.
Riski on mittauksista laskettu: anturit näyttävät kuuraa myös öinä, jolloin ajoradat pysyvät kuivina. Siksi su2 lisää
havaitun liukkauden: optinen kitka alle 0,6 kylmällä tiellä vähintään 1 h (`havaittu`, `havAlku`, `kitkaMin`, `opt` = optisia asemia,
`tulos` liukasta / ei_liukasta / ei_optista, `suolaVsLiukas` ennen / jalkeen / ei).
Poikkeavat anturit (`vika`) jätetään pois: tienpinta yön mediaanina yli 4 °C urakan muista tai yksittäinen mittaus yli 4 °C
muista, kitka-anturi liukas yli +3 °C:n tiellä. Kausi: `liukasYot`, `ehtiEnnen`, `ehtiPros`, `eiSuolaLiukas`, `riskiEiLiukasta`.
- `data/suomi.json` → `ennuste` (su4): kelikeskuksen indeksi klo 18 ja 22 (`retro/yot/YYYY-MM-DD.json`, retro.mjs rt4: asemittain
  huippu ja ensimmäinen hetki ≥ 50 ennen aamua klo 08) vs. havaittu liukkaus urakoittain: osumat, ohi, turhat, oikein ei riskiä,
  ennakko tunteina, hälytyksen syy, ELY ja urakka, klo 22 tiedossa olleet piirteet (riskin alku, tienpinta, tie − kastepiste, kitka)
  ja sääntöehdokkaiden vaikutus. Jälkitarkistus valmistuu noin vuorokauden viiveellä.
- `data/joukko.json` (su5, kollektiivinen päivystäjä): päätöshetkittäin (klo 18 / 22) kelikeskuksen indeksiluokka × urakan alin
  tienpinta → urakkayötä (`n`), suolasi (`suolasiPros`), oli jo suolannut (`joPros`), ensimmäisen suolauksen mediaani tunteina
  päätöksestä (`suolaH`), liukasta kitka-anturillisista (`liukasPros`) sekä suolatuista ja suolaamattomista erikseen. Solut alle
  15 yön: pelkkä indeksiluokka (`|*`). Kelikeskus ja Päivystyskirja hakevat tästä Vantaan illan arvion varjokomennon luvuilla.
- Aukkovahti (su6): jokaisessa yössä `aukot` = toteumapäivät, jotka puuttuvat (`toteumaPaivat`), puolen tunnin askeleet, joilla alle
  puolet asemista mittasi (`mittausVajaat`), ja yli 4 h katkot toteumakeruussa riskiöinä (`toteumaKatkot`); `data/suomi.json` →
  `aukot` = viimeisten 30 yön puutteet. Aukosta tulee Actionsiin varoitus, ja Päivystyskirja näyttää sen.
- rt6/su8 (7.11.2026): päätöshetkiin myös kelikeskuksen varjokomennon toimenpidetaso (`toim`, `toimWhy`: indeksi ≥ 50, ei yli 12 h
  arviota, ennustettu kuura vasta kun kuuraa on alkanut kertyä; mallien yhtäpitävyyttä ei arkistossa ole). `ennuste.slots.*.toimenpide`
  ja syy-, alue-, urakka- ja piirre-erittelyt tällä tasolla (raaka indeksi `jokin` vertailuna).
- `km_varjo.py` (km1, 10.11.2026): kuurapistemalli varjona tienpintamallin rinnalle. Opettaa kastepisteen ja suoraan erotuksen
  tie − kastepiste (+2/+4/+6/+12 h) koko arkistolla (tienpintamalli.yml, malli välimuistissa), testi ilman viimeistä 7 vrk:ta →
  `km/testi.json`. Arkistoajo ennustaa Vantaan asemille ja tarkistaa → `km/verif.json`, `km/verif-YYYY-MM.csv`, `km/latest.json`.
- rt7/su9 (7.11.2026): toimenpidetasoon mallien yhtäpitävyys (MEPS ja EC arkistosta, kuten kelikeskuksessa; MET puuttuu), päätöshetkeen
  tienpinta (`tr`). Illan tila: Arkiston ajastin käynnistää retro.yml:n (`ilta=true`) klo 18.23 ja 22.23 → `retro.mjs --ilta` ja
  `suomi.py --ilta` → `data/joukko-ilta.json` (joukon arvio kaikille urakoille samalla laskennalla kuin `data/joukko.json`).
- Jälkitarkistus (retro.yml) käynnistyy Arkiston ajastimesta klo 08.11 Suomen aikaa. Illan päätöshetket (`retro/yot/`) lasketaan heti
  yön jälkeen (rt5, `ennakko: true`), täysi tarkistus seuraavana päivänä. Lopuksi `suomi.py --kausi` päivittää kauden ja joukon taulukon.

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
