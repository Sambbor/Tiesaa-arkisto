# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v20) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 42 (2026-10-12 – 2026-11-22), laskentoja 454758. Päivitetty 2026-11-24T06:11:38Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 11805.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 11153 | 414 | 32520 | 229745 | 96 % | 74 % |
| +6 h | 10911 | 1298 | 40334 | 221391 | 89 % | 79 % |
| +12 h | 11362 | 1238 | 44990 | 214862 | 90 % | 80 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 2556 | 340 | 5953 | 88 % | 70 % |
| Lappi | 3034 | 123 | 3808 | 96 % | 56 % |
| Keski-Suomi | 976 | 137 | 3817 | 88 % | 80 % |
| Uusimaa | 131 | 17 | 3983 | 89 % | 97 % |
| Etelä-Pohjanmaa | 838 | 141 | 3024 | 86 % | 78 % |
| Pohjois-Savo | 942 | 172 | 2717 | 85 % | 74 % |
| Pirkanmaa | 339 | 32 | 2364 | 91 % | 87 % |
| Pohjanmaa | 319 | 89 | 2234 | 78 % | 88 % |
| Varsinais-Suomi | 134 | 14 | 2400 | 91 % | 95 % |
| Kymenlaakso | 197 | 29 | 1816 | 87 % | 90 % |
| Pohjois-Karjala | 243 | 66 | 1550 | 79 % | 86 % |
| Keski-Pohjanmaa | 463 | 34 | 1128 | 93 % | 71 % |
| Etelä-Savo | 210 | 39 | 1100 | 84 % | 84 % |
| Satakunta | 134 | 20 | 1158 | 87 % | 90 % |
| Etelä-Karjala | 122 | 25 | 1035 | 83 % | 89 % |
| Päijät-Häme | 68 | 5 | 1013 | 93 % | 94 % |
| Kanta-Häme | 49 | 3 | 732 | 94 % | 94 % |
| Kainuu | 156 | 12 | 502 | 93 % | 76 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 2283 | 19005 | 11 % |
| tiesääennuste (Digitraffic) | 3240 | 13482 | 19 % |
| märkä tie jäätyy | 2510 | 5914 | 30 % |
| lumisade | 2818 | 1801 | 61 % |
| jäätävä sade | 60 | 132 | 31 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 667 |
| tie −1…+1 °C | 466 |
| tie alle −4 °C | 165 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 28505 | 1506 | 58307 | 363221 | 95 % | 67 % |
| +6 h | 26366 | 4648 | 71397 | 349007 | 85 % | 73 % |
| +12 h | 27426 | 4312 | 79441 | 337861 | 86 % | 74 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 9706 | 1044 | 9874 | 90 % |
| Pohjois-Pohjanmaa | 4828 | 977 | 9975 | 83 % |
| Finavia lentokentät | 1357 | 832 | 6015 | 62 % |
| Etelä-Pohjanmaa | 1270 | 185 | 4962 | 87 % |
| Kainuu | 2013 | 286 | 3792 | 88 % |
| Pohjois-Savo | 1607 | 244 | 3894 | 87 % |
| Keski-Suomi | 1193 | 138 | 4129 | 90 % |
| Pohjois-Karjala | 1049 | 202 | 4207 | 84 % |
| Uusimaa | 196 | 46 | 4912 | 81 % |
| Varsinais-Suomi | 308 | 55 | 3865 | 85 % |
| Pirkanmaa | 468 | 70 | 3085 | 87 % |
| Pohjanmaa | 496 | 114 | 2696 | 81 % |
| Keski-Pohjanmaa | 796 | 60 | 1926 | 93 % |
| Etelä-Savo | 306 | 43 | 2113 | 88 % |
| Kymenlaakso | 253 | 47 | 1867 | 84 % |
| Etelä-Karjala | 184 | 251 | 1143 | 42 % |
| Satakunta | 185 | 41 | 1118 | 82 % |
| Päijät-Häme | 86 | 7 | 1108 | 92 % |
| Kanta-Häme | 65 | 6 | 716 | 92 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 8274 | 34769 |
| tiesääennuste (Digitraffic) | 8402 | 22752 |
| märkä tie jäätyy | 3698 | 9840 |
| lumisade | 5808 | 3740 |
| jäätävä sade | 184 | 296 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 2593 |
| varoitus häly | 642 |
| kitka < 0,45 | 608 |
| keli lumi | 442 |
| jäätä tiellä | 287 |
| keli kuura | 76 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 25777 | 4707 (18 %) | 51626 | 0 (0 %) | 4057 (8 %) | 12687 (25 %) |
| 0,5–2 | 6670 | 1052 (16 %) | 12906 | 0 (0 %) | 2904 (23 %) | 2800 (22 %) |
| 2–4 | 4544 | 782 (17 %) | 9728 | 0 (0 %) | 2029 (21 %) | 2390 (25 %) |
| 4–8 | 4796 | 811 (17 %) | 10791 | 2 (0 %) | 2142 (20 %) | 2801 (26 %) |
| yli 8 | 6316 | 1470 (23 %) | 16918 | 569 (3 %) | 2511 (15 %) | 5227 (31 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 12317 | 28 % (26 % / 18713) | 20592 | 30 % (31 % / 32798) |
| −4…−2 | 2499 | 22 % (17 % / 4263) | 5009 | 34 % (35 % / 8102) |
| −6…−4 | 336 | 46 % (29 % / 583) | 1156 | 69 % (58 % / 1941) |
| −8…−6 | 33 | 73 % (60 % / 57) | 468 | 77 % (67 % / 630) |
| alle −8 | 0 | – (66 % / 32) | 726 | 88 % (80 % / 881) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 36 päivältä, 16753 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 4887 | 1595 |
| Vain urakka suolasi | 290 | 6 |
| Vain ennuste hälytti | 5741 | 1673 |
| Kumpikaan ei | 5835 | 24 |

Suolauskertoja 5916: ennuste hälytti 0–12 h ennen 5258 kertaa (89 %), keskimäärin 7,7 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 1764 kertaa (30 %).
Liukkaista asemavuorokausista 3298: suolattu ennen ensimmäistä liukasta mittausta 859, vasta sen jälkeen (6 h sisällä) 482.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 3074 | 666 | 115 | 1049 | 848 | 671 | 161 |
| Oulu | 504 | 255 | 22 | 143 | 256 | 206 | 99 |
| Kuopio | 396 | 172 | 11 | 94 | 251 | 222 | 105 |
| Raahe/Ylivieska | 315 | 146 | 6 | 89 | 192 | 178 | 101 |
| Kajaani | 288 | 170 | 0 | 57 | 224 | 216 | 82 |
| Kemi | 282 | 103 | 1 | 143 | 126 | 121 | 58 |
| Kittilä | 281 | 0 | 0 | 260 | 0 | 0 | 0 |
| Lapua | 324 | 143 | 15 | 87 | 163 | 137 | 69 |
| Salo | 396 | 117 | 0 | 104 | 132 | 114 | 8 |
| Seinäjoki | 272 | 111 | 2 | 82 | 146 | 142 | 66 |
| Tampere | 324 | 79 | 12 | 88 | 125 | 107 | 22 |
| Kotka | 360 | 60 | 5 | 121 | 85 | 77 | 12 |
| Ivalo | 216 | 1 | 0 | 204 | 1 | 1 | 0 |
| Espoo 19-24 | 485 | 99 | 6 | 85 | 108 | 97 | 14 |
| Joensuu | 250 | 79 | 7 | 93 | 99 | 81 | 31 |
| Pudasjärvi-Taivalkoski | 180 | 71 | 1 | 94 | 92 | 88 | 32 |
| Kristiinankaupunki | 252 | 97 | 2 | 69 | 105 | 96 | 28 |
| Nummi | 324 | 96 | 6 | 73 | 99 | 92 | 6 |
| Paimio | 324 | 80 | 2 | 78 | 89 | 81 | 3 |
| Kuusamo | 180 | 38 | 0 | 122 | 43 | 43 | 37 |
| Lappeenranta | 216 | 59 | 4 | 65 | 87 | 81 | 27 |
| Veteli | 180 | 66 | 0 | 69 | 82 | 79 | 47 |
| Kemijärvi-Posio | 158 | 15 | 0 | 131 | 16 | 16 | 7 |
| Pori | 216 | 62 | 1 | 52 | 90 | 74 | 29 |
| Hyvinkää | 252 | 66 | 0 | 68 | 73 | 67 | 4 |
| Orivesi | 207 | 79 | 1 | 38 | 102 | 96 | 26 |
| Nurmes | 180 | 58 | 0 | 88 | 51 | 49 | 23 |
| Sodankylä | 144 | 0 | 0 | 137 | 0 | 0 | 0 |
| Mikkeli | 205 | 63 | 0 | 62 | 71 | 69 | 18 |
| Äänekoski | 180 | 64 | 0 | 56 | 77 | 73 | 43 |
| Vaasa | 144 | 55 | 4 | 43 | 88 | 74 | 22 |
| Lahti | 216 | 74 | 3 | 45 | 81 | 70 | 8 |
| Suonenjoki | 144 | 51 | 1 | 57 | 67 | 63 | 32 |
| Rovaniemi | 108 | 40 | 1 | 55 | 65 | 59 | 20 |
| Kitee | 169 | 63 | 6 | 49 | 69 | 54 | 16 |
| E18 Muurla-Lohja | 216 | 72 | 0 | 45 | 71 | 60 | 0 |
| Pyhäjärvi | 108 | 55 | 0 | 28 | 85 | 81 | 38 |
| Jyväskylä | 252 | 72 | 13 | 31 | 81 | 64 | 1 |
| Viinijärvi | 144 | 43 | 0 | 64 | 47 | 44 | 21 |
| Raisio | 216 | 72 | 6 | 41 | 69 | 55 | 7 |
| Suomussalmi | 114 | 23 | 0 | 81 | 24 | 22 | 11 |
| Porvoo | 214 | 44 | 1 | 58 | 45 | 37 | 3 |
| Juva | 144 | 37 | 1 | 51 | 44 | 40 | 8 |
| Kauhajoki | 108 | 40 | 1 | 36 | 57 | 57 | 25 |
| Pihtipudas | 108 | 43 | 0 | 35 | 54 | 52 | 29 |
| Kokkola | 108 | 47 | 0 | 37 | 52 | 52 | 33 |
| Ii | 108 | 34 | 1 | 55 | 33 | 32 | 19 |
| Lieto | 180 | 58 | 5 | 33 | 54 | 46 | 1 |
| Kouvola | 144 | 39 | 1 | 41 | 44 | 40 | 4 |
| Puolanka | 108 | 15 | 0 | 72 | 13 | 13 | 7 |
| Jämsä | 144 | 29 | 0 | 53 | 30 | 30 | 6 |
| Koskenkylä -Kotka | 144 | 30 | 3 | 31 | 51 | 40 | 6 |
| Alavus | 97 | 55 | 1 | 23 | 57 | 54 | 17 |
| Siikalatva | 77 | 47 | 1 | 15 | 62 | 57 | 36 |
| Raasepori | 180 | 36 | 3 | 40 | 35 | 30 | 0 |
| Virrat | 108 | 40 | 1 | 29 | 45 | 40 | 10 |
| Pieksämäki | 108 | 29 | 0 | 46 | 28 | 28 | 7 |
| Rovaniemi 17-22 | 72 | 25 | 0 | 44 | 29 | 29 | 11 |
| Karstula | 72 | 29 | 0 | 23 | 45 | 43 | 30 |
| Savonlinna | 97 | 33 | 3 | 25 | 42 | 40 | 13 |
| Hamina-Vaalimaa | 108 | 19 | 1 | 36 | 30 | 29 | 7 |
| Imatra | 108 | 29 | 0 | 33 | 32 | 31 | 7 |
| Pello | 65 | 18 | 0 | 44 | 21 | 21 | 14 |
| Kuhmo | 72 | 12 | 0 | 47 | 14 | 14 | 8 |
| Nilsiä | 72 | 30 | 0 | 25 | 33 | 31 | 21 |
| Mäntsälä | 108 | 27 | 0 | 27 | 30 | 26 | 2 |
| Ilomantsi | 72 | 12 | 0 | 45 | 11 | 11 | 1 |
| Keuruu | 71 | 24 | 1 | 26 | 28 | 25 | 15 |
| Iisalmi | 72 | 37 | 0 | 16 | 36 | 35 | 19 |
| Kangasala | 72 | 24 | 4 | 11 | 39 | 33 | 11 |
| Espoo | 108 | 25 | 1 | 20 | 29 | 24 | 3 |
| Parkano | 72 | 24 | 0 | 19 | 27 | 26 | 14 |
| Harjavalta | 72 | 15 | 0 | 27 | 17 | 17 | 1 |
| Merikarvia | 72 | 21 | 0 | 13 | 31 | 28 | 11 |
| Heinola | 72 | 19 | 2 | 22 | 22 | 21 | 3 |
| Hämeenlinna | 72 | 16 | 2 | 19 | 17 | 14 | 1 |
| Huittinen | 72 | 17 | 0 | 19 | 16 | 16 | 2 |
| Pielavesi | 36 | 11 | 0 | 18 | 15 | 15 | 9 |
| Ranua | 36 | 11 | 0 | 21 | 10 | 9 | 4 |
| Kankaanpää | 36 | 10 | 1 | 14 | 14 | 13 | 6 |
| Vantaa | 60 | 13 | 3 | 11 | 15 | 11 | 0 |
| Sastamala | 36 | 9 | 0 | 13 | 12 | 12 | 3 |
| Kiuruvesi | 36 | 11 | 0 | 16 | 9 | 8 | 2 |
| Loimaa | 36 | 8 | 0 | 12 | 8 | 8 | 1 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
