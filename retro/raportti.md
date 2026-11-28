# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v24) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 46 (2026-10-12 – 2026-11-26), laskentoja 500457. Päivitetty 2026-11-28T06:11:41Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 12960.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 16209 | 1327 | 28080 | 255863 | 92 % | 63 % |
| +6 h | 15177 | 2645 | 42118 | 241636 | 85 % | 74 % |
| +12 h | 15636 | 2545 | 51652 | 230255 | 86 % | 77 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 3619 | 653 | 5279 | 85 % | 59 % |
| Lappi | 3974 | 179 | 3541 | 96 % | 47 % |
| Keski-Suomi | 1552 | 311 | 4064 | 83 % | 72 % |
| Etelä-Pohjanmaa | 1179 | 345 | 3197 | 77 % | 73 % |
| Pohjois-Savo | 1162 | 324 | 2827 | 78 % | 71 % |
| Uusimaa | 163 | 30 | 4044 | 84 % | 96 % |
| Pirkanmaa | 512 | 168 | 2716 | 75 % | 84 % |
| Pohjanmaa | 517 | 114 | 2552 | 82 % | 83 % |
| Varsinais-Suomi | 187 | 46 | 2812 | 80 % | 94 % |
| Kymenlaakso | 288 | 64 | 2046 | 82 % | 88 % |
| Pohjois-Karjala | 361 | 105 | 1494 | 77 % | 81 % |
| Keski-Pohjanmaa | 689 | 98 | 1126 | 88 % | 62 % |
| Etelä-Savo | 293 | 70 | 1330 | 81 % | 82 % |
| Satakunta | 173 | 34 | 1386 | 84 % | 89 % |
| Etelä-Karjala | 157 | 53 | 1213 | 75 % | 89 % |
| Päijät-Häme | 73 | 19 | 1164 | 79 % | 94 % |
| Kanta-Häme | 80 | 14 | 835 | 85 % | 91 % |
| Kainuu | 198 | 18 | 492 | 92 % | 71 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 3663 | 22663 | 14 % |
| tiesääennuste (Digitraffic) | 4973 | 13298 | 27 % |
| märkä tie jäätyy | 3620 | 4103 | 47 % |
| lumisade | 2861 | 1926 | 60 % |
| jäätävä sade | 60 | 128 | 32 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 1483 |
| tie −1…+1 °C | 615 |
| tie alle −4 °C | 547 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 33552 | 7409 | 56690 | 399564 | 82 % | 63 % |
| +6 h | 34046 | 7539 | 78018 | 377475 | 82 % | 70 % |
| +12 h | 35403 | 6880 | 92760 | 359652 | 84 % | 72 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 11995 | 1339 | 10211 | 90 % |
| Pohjois-Pohjanmaa | 6008 | 1634 | 9902 | 79 % |
| Finavia lentokentät | 2260 | 1064 | 7110 | 68 % |
| Etelä-Pohjanmaa | 1709 | 398 | 5506 | 81 % |
| Kainuu | 2350 | 506 | 4211 | 82 % |
| Pohjois-Savo | 1872 | 585 | 4155 | 76 % |
| Keski-Suomi | 1695 | 324 | 4515 | 84 % |
| Pohjois-Karjala | 1411 | 360 | 4469 | 80 % |
| Varsinais-Suomi | 614 | 238 | 4517 | 72 % |
| Uusimaa | 276 | 123 | 4937 | 69 % |
| Pirkanmaa | 719 | 225 | 3577 | 76 % |
| Pohjanmaa | 639 | 128 | 3338 | 83 % |
| Keski-Pohjanmaa | 1030 | 99 | 2092 | 91 % |
| Etelä-Savo | 449 | 112 | 2594 | 80 % |
| Kymenlaakso | 384 | 105 | 2085 | 79 % |
| Etelä-Karjala | 225 | 164 | 1344 | 58 % |
| Satakunta | 226 | 87 | 1342 | 72 % |
| Päijät-Häme | 93 | 19 | 1289 | 83 % |
| Kanta-Häme | 91 | 20 | 824 | 82 % |
| Ahvenanmaa | 0 | 9 | 0 | 0 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 11733 | 40520 |
| tiesääennuste (Digitraffic) | 11781 | 26028 |
| märkä tie jäätyy | 4550 | 7175 |
| lumisade | 5789 | 4007 |
| jäätävä sade | 193 | 288 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 4683 |
| kitka < 0,45 | 1510 |
| keli lumi | 837 |
| jäätä tiellä | 416 |
| keli kuura | 93 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 41700 | 8173 (20 %) | 76907 | 0 (0 %) | 0 (0 %) | 8245 (11 %) |
| 0,5–2 | 7828 | 1563 (20 %) | 14945 | 0 (0 %) | 0 (0 %) | 1805 (12 %) |
| 2–4 | 5240 | 1130 (22 %) | 11066 | 0 (0 %) | 0 (0 %) | 1320 (12 %) |
| 4–8 | 5148 | 1171 (23 %) | 11938 | 4 (0 %) | 0 (0 %) | 1187 (10 %) |
| yli 8 | 6643 | 2224 (33 %) | 19523 | 1338 (7 %) | 0 (0 %) | 2191 (11 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 13914 | 27 % (30 % / 15475) | 22402 | 32 % (36 % / 28329) |
| −4…−2 | 2778 | 21 % (19 % / 3207) | 6772 | 36 % (38 % / 8523) |
| −6…−4 | 568 | 27 % (21 % / 655) | 3159 | 49 % (50 % / 3915) |
| −8…−6 | 118 | 52 % (32 % / 156) | 1908 | 54 % (54 % / 2346) |
| alle −8 | 33 | 52 % (29 % / 58) | 1790 | 80 % (76 % / 2182) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 40 päivältä, 18662 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 5441 | 1943 |
| Vain urakka suolasi | 425 | 17 |
| Vain ennuste hälytti | 6591 | 2198 |
| Kumpikaan ei | 6205 | 74 |

Suolauskertoja 6878: ennuste hälytti 0–12 h ennen 5948 kertaa (86 %), keskimäärin 7,5 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 2269 kertaa (33 %).
Liukkaista asemavuorokausista 4232: suolattu ennen ensimmäistä liukasta mittausta 1153, vasta sen jälkeen (6 h sisällä) 584.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 3426 | 749 | 146 | 1203 | 977 | 760 | 216 |
| Oulu | 560 | 248 | 29 | 187 | 256 | 198 | 98 |
| Kuopio | 440 | 199 | 13 | 105 | 300 | 257 | 133 |
| Raahe/Ylivieska | 351 | 155 | 7 | 111 | 204 | 189 | 111 |
| Kajaani | 320 | 171 | 1 | 86 | 226 | 215 | 83 |
| Lapua | 360 | 153 | 16 | 111 | 179 | 151 | 82 |
| Kemi | 314 | 102 | 2 | 162 | 126 | 121 | 57 |
| Kittilä | 312 | 0 | 0 | 283 | 0 | 0 | 0 |
| Salo | 440 | 123 | 1 | 129 | 147 | 129 | 21 |
| Kotka | 400 | 80 | 6 | 137 | 126 | 108 | 24 |
| Seinäjoki | 304 | 118 | 2 | 100 | 156 | 150 | 73 |
| Tampere | 364 | 99 | 15 | 93 | 158 | 128 | 44 |
| Ivalo | 240 | 1 | 0 | 228 | 1 | 1 | 0 |
| Espoo 19-24 | 541 | 121 | 23 | 85 | 143 | 117 | 21 |
| Joensuu | 278 | 92 | 9 | 94 | 122 | 97 | 47 |
| Pudasjärvi-Taivalkoski | 200 | 71 | 1 | 114 | 92 | 88 | 32 |
| Nummi | 360 | 107 | 9 | 83 | 122 | 106 | 14 |
| Kristiinankaupunki | 280 | 107 | 2 | 81 | 120 | 106 | 35 |
| Paimio | 360 | 93 | 4 | 84 | 102 | 87 | 11 |
| Lappeenranta | 240 | 75 | 5 | 66 | 114 | 105 | 37 |
| Kuusamo | 200 | 37 | 1 | 137 | 43 | 42 | 37 |
| Orivesi | 231 | 91 | 1 | 46 | 129 | 117 | 47 |
| Veteli | 200 | 70 | 1 | 83 | 88 | 84 | 47 |
| Pori | 240 | 74 | 4 | 52 | 115 | 93 | 37 |
| Mikkeli | 229 | 77 | 0 | 71 | 96 | 94 | 28 |
| Kemijärvi-Posio | 178 | 15 | 0 | 151 | 16 | 16 | 7 |
| Hyvinkää | 280 | 84 | 7 | 64 | 98 | 85 | 17 |
| Äänekoski | 203 | 79 | 1 | 62 | 100 | 93 | 62 |
| Nurmes | 200 | 67 | 0 | 99 | 62 | 59 | 30 |
| Lahti | 240 | 87 | 5 | 52 | 107 | 91 | 19 |
| Sodankylä | 160 | 0 | 0 | 153 | 0 | 0 | 0 |
| Vaasa | 161 | 58 | 4 | 57 | 91 | 75 | 23 |
| Suonenjoki | 160 | 56 | 1 | 67 | 79 | 74 | 41 |
| E18 Muurla-Lohja | 240 | 76 | 2 | 54 | 84 | 67 | 2 |
| Kitee | 189 | 71 | 8 | 53 | 84 | 67 | 27 |
| Rovaniemi | 120 | 41 | 1 | 66 | 66 | 60 | 20 |
| Porvoo | 238 | 49 | 3 | 68 | 62 | 51 | 13 |
| Raisio | 240 | 85 | 9 | 43 | 84 | 64 | 18 |
| Viinijärvi | 160 | 48 | 0 | 69 | 58 | 52 | 31 |
| Jyväskylä | 280 | 79 | 27 | 29 | 97 | 66 | 4 |
| Pyhäjärvi | 120 | 56 | 1 | 38 | 87 | 79 | 40 |
| Suomussalmi | 130 | 23 | 0 | 96 | 24 | 22 | 11 |
| Juva | 160 | 45 | 1 | 58 | 57 | 53 | 18 |
| Kouvola | 160 | 45 | 3 | 46 | 63 | 50 | 13 |
| Kauhajoki | 120 | 43 | 1 | 44 | 63 | 63 | 30 |
| Koskenkylä -Kotka | 160 | 34 | 6 | 37 | 67 | 49 | 11 |
| Pihtipudas | 120 | 50 | 0 | 38 | 65 | 62 | 35 |
| Lieto | 200 | 69 | 7 | 37 | 65 | 54 | 6 |
| Kokkola | 120 | 51 | 0 | 44 | 58 | 56 | 37 |
| Jämsä | 160 | 38 | 0 | 60 | 40 | 38 | 12 |
| Ii | 120 | 33 | 2 | 66 | 33 | 30 | 18 |
| Alavus | 113 | 59 | 1 | 34 | 63 | 60 | 21 |
| Puolanka | 120 | 16 | 0 | 78 | 14 | 14 | 6 |
| Siikalatva | 89 | 49 | 1 | 25 | 64 | 57 | 38 |
| Virrat | 120 | 43 | 1 | 38 | 49 | 44 | 14 |
| Pieksämäki | 120 | 35 | 0 | 50 | 37 | 37 | 13 |
| Savonlinna | 109 | 42 | 2 | 28 | 58 | 54 | 28 |
| Raasepori | 200 | 43 | 4 | 43 | 40 | 31 | 2 |
| Hamina-Vaalimaa | 120 | 26 | 1 | 40 | 43 | 42 | 14 |
| Imatra | 120 | 37 | 0 | 34 | 46 | 44 | 18 |
| Rovaniemi 17-22 | 80 | 24 | 1 | 49 | 29 | 28 | 11 |
| Karstula | 80 | 34 | 0 | 26 | 51 | 49 | 36 |
| Pello | 73 | 18 | 0 | 52 | 21 | 21 | 14 |
| Kuhmo | 80 | 13 | 0 | 54 | 15 | 15 | 9 |
| Mäntsälä | 120 | 30 | 0 | 32 | 36 | 27 | 5 |
| Nilsiä | 80 | 31 | 0 | 32 | 34 | 32 | 22 |
| Ilomantsi | 80 | 14 | 0 | 51 | 14 | 14 | 1 |
| Iisalmi | 80 | 36 | 1 | 24 | 36 | 35 | 19 |
| Kangasala | 80 | 26 | 7 | 12 | 47 | 35 | 15 |
| Keuruu | 77 | 26 | 1 | 29 | 30 | 26 | 15 |
| Parkano | 80 | 28 | 0 | 22 | 36 | 35 | 22 |
| Espoo | 120 | 32 | 2 | 18 | 37 | 28 | 3 |
| Harjavalta | 80 | 17 | 0 | 32 | 22 | 20 | 6 |
| Merikarvia | 80 | 24 | 0 | 18 | 36 | 32 | 12 |
| Heinola | 80 | 23 | 2 | 25 | 29 | 27 | 8 |
| Hämeenlinna | 80 | 21 | 2 | 17 | 26 | 22 | 5 |
| Huittinen | 80 | 19 | 0 | 23 | 18 | 18 | 3 |
| Pielavesi | 40 | 12 | 0 | 21 | 17 | 17 | 11 |
| Ranua | 40 | 11 | 0 | 25 | 10 | 9 | 3 |
| Vantaa | 72 | 14 | 10 | 14 | 20 | 12 | 2 |
| Kankaanpää | 40 | 11 | 1 | 16 | 15 | 13 | 5 |
| Kiuruvesi | 40 | 11 | 0 | 20 | 9 | 8 | 2 |
| Sastamala | 40 | 12 | 0 | 13 | 14 | 14 | 4 |
| Loimaa | 40 | 9 | 1 | 14 | 10 | 9 | 2 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
