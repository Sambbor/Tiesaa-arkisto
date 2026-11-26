# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v23) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 44 (2026-10-12 – 2026-11-24), laskentoja 477516. Päivitetty 2026-11-26T06:12:22Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 12384.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 13422 | 1056 | 27321 | 245865 | 93 % | 67 % |
| +6 h | 12493 | 2237 | 39183 | 233848 | 85 % | 76 % |
| +12 h | 12845 | 2229 | 46274 | 224925 | 85 % | 78 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 2813 | 560 | 5111 | 83 % | 65 % |
| Lappi | 3465 | 156 | 3539 | 96 % | 51 % |
| Keski-Suomi | 1202 | 258 | 3821 | 82 % | 76 % |
| Etelä-Pohjanmaa | 927 | 301 | 3010 | 75 % | 76 % |
| Pohjois-Savo | 1059 | 262 | 2677 | 80 % | 72 % |
| Uusimaa | 146 | 21 | 3706 | 87 % | 96 % |
| Pirkanmaa | 404 | 141 | 2306 | 74 % | 85 % |
| Pohjanmaa | 325 | 96 | 2319 | 77 % | 88 % |
| Varsinais-Suomi | 148 | 45 | 2298 | 77 % | 94 % |
| Kymenlaakso | 232 | 40 | 1928 | 85 % | 89 % |
| Pohjois-Karjala | 357 | 103 | 1518 | 78 % | 81 % |
| Keski-Pohjanmaa | 550 | 81 | 1095 | 87 % | 67 % |
| Etelä-Savo | 263 | 61 | 1265 | 81 % | 83 % |
| Etelä-Karjala | 150 | 40 | 1165 | 79 % | 89 % |
| Satakunta | 142 | 28 | 1149 | 84 % | 89 % |
| Päijät-Häme | 70 | 14 | 1090 | 83 % | 94 % |
| Kanta-Häme | 67 | 13 | 745 | 84 % | 92 % |
| Kainuu | 173 | 17 | 441 | 91 % | 72 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 2702 | 20890 | 11 % |
| tiesääennuste (Digitraffic) | 3974 | 12204 | 25 % |
| märkä tie jäätyy | 2873 | 3976 | 42 % |
| lumisade | 2884 | 1981 | 59 % |
| jäätävä sade | 60 | 132 | 31 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 1294 |
| tie −1…+1 °C | 558 |
| tie alle −4 °C | 385 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 29472 | 6515 | 53205 | 385094 | 82 % | 64 % |
| +6 h | 29606 | 6829 | 71715 | 366001 | 81 % | 71 % |
| +12 h | 30777 | 6264 | 83198 | 351535 | 83 % | 73 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 10867 | 1293 | 9738 | 89 % |
| Pohjois-Pohjanmaa | 5100 | 1439 | 9251 | 78 % |
| Finavia lentokentät | 1832 | 1053 | 6367 | 64 % |
| Etelä-Pohjanmaa | 1388 | 371 | 5039 | 79 % |
| Kainuu | 2159 | 456 | 3805 | 83 % |
| Pohjois-Savo | 1726 | 486 | 3900 | 78 % |
| Pohjois-Karjala | 1328 | 271 | 4316 | 83 % |
| Keski-Suomi | 1420 | 282 | 4141 | 83 % |
| Uusimaa | 219 | 53 | 4589 | 81 % |
| Varsinais-Suomi | 328 | 160 | 3914 | 67 % |
| Pirkanmaa | 543 | 201 | 3080 | 73 % |
| Pohjanmaa | 525 | 120 | 2872 | 81 % |
| Keski-Pohjanmaa | 894 | 115 | 1936 | 89 % |
| Etelä-Savo | 407 | 82 | 2444 | 83 % |
| Kymenlaakso | 288 | 69 | 1996 | 81 % |
| Etelä-Karjala | 219 | 267 | 1286 | 45 % |
| Satakunta | 195 | 70 | 1105 | 74 % |
| Päijät-Häme | 86 | 18 | 1206 | 83 % |
| Kanta-Häme | 82 | 20 | 730 | 80 % |
| Ahvenanmaa | 0 | 3 | 0 | 0 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 9779 | 37615 |
| tiesääennuste (Digitraffic) | 9929 | 22999 |
| märkä tie jäätyy | 3843 | 6819 |
| lumisade | 5865 | 3983 |
| jäätävä sade | 190 | 299 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 3770 |
| kitka < 0,45 | 1076 |
| varoitus häly | 779 |
| keli lumi | 732 |
| jäätä tiellä | 390 |
| keli kuura | 82 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 32822 | 6567 (20 %) | 63171 | 0 (0 %) | 4536 (7 %) | 6741 (11 %) |
| 0,5–2 | 7048 | 1181 (17 %) | 13777 | 0 (0 %) | 3084 (22 %) | 1430 (10 %) |
| 2–4 | 4919 | 959 (19 %) | 10478 | 0 (0 %) | 2159 (21 %) | 1127 (11 %) |
| 4–8 | 5091 | 965 (19 %) | 11503 | 2 (0 %) | 2270 (20 %) | 1065 (9 %) |
| yli 8 | 6655 | 1714 (26 %) | 18382 | 845 (5 %) | 2738 (15 %) | 1592 (9 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 13136 | 28 % (30 % / 14690) | 21355 | 32 % (36 % / 27243) |
| −4…−2 | 2423 | 21 % (21 % / 2724) | 4988 | 38 % (43 % / 6514) |
| −6…−4 | 368 | 36 % (31 % / 398) | 1619 | 61 % (58 % / 2110) |
| −8…−6 | 43 | 58 % (45 % / 58) | 741 | 65 % (58 % / 983) |
| alle −8 | 0 | – (0 % / 25) | 1016 | 89 % (80 % / 1212) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 38 päivältä, 17705 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 5269 | 1919 |
| Vain urakka suolasi | 405 | 14 |
| Vain ennuste hälytti | 5914 | 1880 |
| Kumpikaan ei | 6117 | 81 |

Suolauskertoja 6732: ennuste hälytti 0–12 h ennen 5850 kertaa (87 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 2234 kertaa (33 %).
Liukkaista asemavuorokausista 3894: suolattu ennen ensimmäistä liukasta mittausta 1143, vasta sen jälkeen (6 h sisällä) 567.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 3250 | 717 | 140 | 1092 | 952 | 740 | 205 |
| Oulu | 532 | 249 | 28 | 162 | 256 | 199 | 99 |
| Kuopio | 418 | 192 | 13 | 90 | 291 | 253 | 132 |
| Raahe/Ylivieska | 333 | 148 | 7 | 100 | 197 | 182 | 106 |
| Kajaani | 304 | 172 | 0 | 70 | 226 | 215 | 84 |
| Kemi | 298 | 102 | 2 | 149 | 126 | 121 | 58 |
| Lapua | 342 | 152 | 16 | 94 | 178 | 150 | 82 |
| Kittilä | 296 | 0 | 0 | 268 | 0 | 0 | 0 |
| Salo | 418 | 123 | 1 | 107 | 147 | 130 | 21 |
| Kotka | 380 | 79 | 6 | 119 | 125 | 108 | 26 |
| Seinäjoki | 288 | 117 | 2 | 88 | 155 | 149 | 73 |
| Tampere | 344 | 93 | 15 | 79 | 151 | 125 | 39 |
| Ivalo | 228 | 1 | 0 | 216 | 1 | 1 | 0 |
| Espoo 19-24 | 513 | 107 | 22 | 74 | 142 | 116 | 21 |
| Joensuu | 264 | 92 | 8 | 84 | 121 | 99 | 47 |
| Pudasjärvi-Taivalkoski | 190 | 71 | 1 | 104 | 92 | 88 | 32 |
| Nummi | 342 | 104 | 9 | 69 | 121 | 107 | 14 |
| Kristiinankaupunki | 266 | 104 | 2 | 72 | 116 | 105 | 34 |
| Paimio | 342 | 85 | 4 | 77 | 97 | 83 | 8 |
| Kuusamo | 190 | 37 | 1 | 127 | 43 | 42 | 37 |
| Lappeenranta | 228 | 70 | 5 | 62 | 107 | 99 | 35 |
| Orivesi | 219 | 86 | 1 | 40 | 124 | 112 | 44 |
| Veteli | 190 | 69 | 1 | 74 | 87 | 83 | 52 |
| Kemijärvi-Posio | 168 | 15 | 0 | 141 | 16 | 16 | 7 |
| Pori | 228 | 68 | 3 | 50 | 105 | 84 | 34 |
| Mikkeli | 217 | 75 | 0 | 61 | 94 | 92 | 28 |
| Hyvinkää | 266 | 74 | 6 | 61 | 93 | 81 | 16 |
| Nurmes | 190 | 67 | 0 | 89 | 62 | 59 | 30 |
| Äänekoski | 191 | 75 | 0 | 55 | 93 | 87 | 57 |
| Lahti | 228 | 84 | 5 | 44 | 103 | 89 | 17 |
| Sodankylä | 152 | 0 | 0 | 145 | 0 | 0 | 0 |
| Vaasa | 152 | 58 | 4 | 48 | 91 | 75 | 23 |
| Suonenjoki | 152 | 55 | 1 | 60 | 77 | 73 | 42 |
| E18 Muurla-Lohja | 228 | 77 | 1 | 46 | 84 | 69 | 2 |
| Kitee | 179 | 71 | 8 | 45 | 84 | 67 | 27 |
| Rovaniemi | 114 | 40 | 1 | 61 | 65 | 59 | 20 |
| Jyväskylä | 266 | 74 | 25 | 24 | 97 | 67 | 4 |
| Raisio | 228 | 75 | 9 | 42 | 79 | 59 | 15 |
| Porvoo | 226 | 49 | 3 | 58 | 62 | 51 | 13 |
| Viinijärvi | 152 | 48 | 0 | 62 | 58 | 54 | 31 |
| Pyhäjärvi | 114 | 56 | 1 | 32 | 87 | 80 | 40 |
| Suomussalmi | 122 | 23 | 0 | 88 | 24 | 22 | 11 |
| Juva | 152 | 43 | 1 | 52 | 54 | 50 | 16 |
| Kouvola | 152 | 45 | 3 | 39 | 63 | 50 | 13 |
| Kauhajoki | 114 | 43 | 1 | 39 | 63 | 63 | 30 |
| Koskenkylä -Kotka | 152 | 34 | 6 | 31 | 67 | 49 | 11 |
| Pihtipudas | 114 | 47 | 0 | 35 | 62 | 59 | 34 |
| Kokkola | 114 | 50 | 0 | 39 | 57 | 55 | 38 |
| Lieto | 190 | 62 | 6 | 35 | 60 | 50 | 5 |
| Ii | 114 | 33 | 2 | 60 | 33 | 30 | 19 |
| Jämsä | 152 | 34 | 0 | 56 | 36 | 34 | 11 |
| Alavus | 105 | 59 | 1 | 27 | 63 | 60 | 22 |
| Puolanka | 114 | 16 | 0 | 73 | 14 | 14 | 8 |
| Pieksämäki | 114 | 34 | 0 | 47 | 36 | 36 | 14 |
| Siikalatva | 83 | 49 | 1 | 19 | 64 | 57 | 38 |
| Savonlinna | 103 | 41 | 1 | 25 | 56 | 53 | 27 |
| Virrat | 114 | 43 | 1 | 32 | 49 | 44 | 14 |
| Hamina-Vaalimaa | 114 | 25 | 1 | 35 | 42 | 41 | 15 |
| Raasepori | 190 | 37 | 4 | 39 | 37 | 29 | 1 |
| Imatra | 114 | 35 | 0 | 31 | 43 | 42 | 16 |
| Rovaniemi 17-22 | 76 | 24 | 1 | 45 | 29 | 28 | 11 |
| Karstula | 76 | 32 | 0 | 24 | 49 | 47 | 34 |
| Pello | 69 | 18 | 0 | 48 | 21 | 21 | 14 |
| Kuhmo | 76 | 13 | 0 | 50 | 15 | 15 | 9 |
| Mäntsälä | 114 | 30 | 0 | 26 | 36 | 30 | 5 |
| Nilsiä | 76 | 31 | 0 | 28 | 34 | 32 | 22 |
| Ilomantsi | 76 | 14 | 0 | 47 | 14 | 14 | 1 |
| Kangasala | 76 | 25 | 7 | 11 | 46 | 34 | 14 |
| Iisalmi | 76 | 36 | 1 | 20 | 36 | 35 | 19 |
| Keuruu | 73 | 26 | 1 | 26 | 30 | 26 | 17 |
| Parkano | 76 | 26 | 0 | 20 | 34 | 33 | 21 |
| Espoo | 114 | 29 | 2 | 16 | 37 | 28 | 4 |
| Harjavalta | 76 | 17 | 0 | 29 | 22 | 20 | 6 |
| Heinola | 76 | 23 | 2 | 22 | 29 | 27 | 8 |
| Merikarvia | 76 | 23 | 0 | 15 | 35 | 31 | 12 |
| Hämeenlinna | 76 | 20 | 2 | 16 | 25 | 22 | 5 |
| Huittinen | 76 | 19 | 0 | 19 | 18 | 18 | 3 |
| Pielavesi | 38 | 12 | 0 | 19 | 17 | 17 | 11 |
| Ranua | 38 | 11 | 0 | 23 | 10 | 9 | 4 |
| Vantaa | 66 | 14 | 8 | 11 | 20 | 13 | 2 |
| Kankaanpää | 38 | 11 | 1 | 14 | 15 | 13 | 7 |
| Kiuruvesi | 38 | 11 | 0 | 18 | 9 | 8 | 2 |
| Sastamala | 38 | 11 | 0 | 12 | 13 | 13 | 3 |
| Loimaa | 38 | 9 | 1 | 12 | 10 | 9 | 2 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
