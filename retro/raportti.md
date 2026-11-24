# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v22) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 42 (2026-10-12 – 2026-11-22), laskentoja 454758. Päivitetty 2026-11-24T15:21:23Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 11805.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 11109 | 458 | 25718 | 236547 | 96 % | 70 % |
| +6 h | 10853 | 1356 | 36219 | 225506 | 89 % | 77 % |
| +12 h | 11332 | 1268 | 42578 | 217274 | 90 % | 79 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 2535 | 361 | 4972 | 88 % | 66 % |
| Lappi | 3024 | 133 | 3433 | 96 % | 53 % |
| Keski-Suomi | 976 | 137 | 3597 | 88 % | 79 % |
| Etelä-Pohjanmaa | 832 | 147 | 2933 | 85 % | 78 % |
| Pohjois-Savo | 939 | 175 | 2473 | 84 % | 72 % |
| Uusimaa | 130 | 18 | 3375 | 88 % | 96 % |
| Pirkanmaa | 338 | 33 | 2192 | 91 % | 87 % |
| Pohjanmaa | 317 | 91 | 2069 | 78 % | 87 % |
| Varsinais-Suomi | 133 | 15 | 2176 | 90 % | 94 % |
| Kymenlaakso | 191 | 35 | 1622 | 85 % | 89 % |
| Pohjois-Karjala | 243 | 66 | 1338 | 79 % | 85 % |
| Keski-Pohjanmaa | 460 | 37 | 1052 | 93 % | 70 % |
| Etelä-Savo | 210 | 39 | 1051 | 84 % | 83 % |
| Satakunta | 134 | 20 | 1082 | 87 % | 89 % |
| Etelä-Karjala | 120 | 27 | 918 | 82 % | 88 % |
| Päijät-Häme | 68 | 5 | 900 | 93 % | 93 % |
| Kanta-Häme | 49 | 3 | 616 | 94 % | 93 % |
| Kainuu | 154 | 14 | 420 | 92 % | 73 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 2310 | 20190 | 10 % |
| tiesääennuste (Digitraffic) | 3271 | 10093 | 24 % |
| märkä tie jäätyy | 2381 | 3965 | 38 % |
| lumisade | 2831 | 1839 | 61 % |
| jäätävä sade | 60 | 132 | 31 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 705 |
| tie −1…+1 °C | 470 |
| tie alle −4 °C | 181 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 28309 | 1702 | 51351 | 370177 | 94 % | 64 % |
| +6 h | 26116 | 4898 | 67069 | 353335 | 84 % | 72 % |
| +12 h | 27301 | 4437 | 76842 | 340460 | 86 % | 74 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 9617 | 1133 | 9569 | 89 % |
| Pohjois-Pohjanmaa | 4762 | 1043 | 8969 | 82 % |
| Finavia lentokentät | 1345 | 844 | 5920 | 61 % |
| Etelä-Pohjanmaa | 1266 | 189 | 4869 | 87 % |
| Kainuu | 2011 | 288 | 3710 | 87 % |
| Pohjois-Savo | 1566 | 285 | 3681 | 85 % |
| Pohjois-Karjala | 1049 | 202 | 3995 | 84 % |
| Keski-Suomi | 1192 | 139 | 3900 | 90 % |
| Uusimaa | 195 | 47 | 4167 | 81 % |
| Varsinais-Suomi | 291 | 72 | 3605 | 80 % |
| Pirkanmaa | 468 | 70 | 2909 | 87 % |
| Pohjanmaa | 495 | 115 | 2525 | 81 % |
| Keski-Pohjanmaa | 795 | 61 | 1848 | 93 % |
| Etelä-Savo | 304 | 45 | 2064 | 87 % |
| Kymenlaakso | 244 | 56 | 1676 | 81 % |
| Etelä-Karjala | 182 | 253 | 1025 | 42 % |
| Satakunta | 185 | 41 | 1040 | 82 % |
| Päijät-Häme | 84 | 9 | 997 | 90 % |
| Kanta-Häme | 65 | 6 | 600 | 92 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 8369 | 35977 |
| tiesääennuste (Digitraffic) | 8296 | 19010 |
| märkä tie jäätyy | 3447 | 8007 |
| lumisade | 5820 | 3779 |
| jäätävä sade | 184 | 296 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 2791 |
| varoitus häly | 657 |
| kitka < 0,45 | 617 |
| keli lumi | 464 |
| jäätä tiellä | 290 |
| keli kuura | 79 |

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
| Ennuste hälytti ja urakka suolasi | 4827 | 1594 |
| Vain urakka suolasi | 350 | 7 |
| Vain ennuste hälytti | 5585 | 1673 |
| Kumpikaan ei | 5991 | 24 |

Suolauskertoja 5916: ennuste hälytti 0–12 h ennen 5171 kertaa (87 %), keskimäärin 7,8 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 1764 kertaa (30 %).
Liukkaista asemavuorokausista 3298: suolattu ennen ensimmäistä liukasta mittausta 859, vasta sen jälkeen (6 h sisällä) 482.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 3074 | 661 | 120 | 1034 | 848 | 658 | 161 |
| Oulu | 504 | 249 | 28 | 136 | 256 | 200 | 99 |
| Kuopio | 396 | 172 | 11 | 92 | 251 | 222 | 105 |
| Kajaani | 288 | 170 | 0 | 57 | 224 | 216 | 82 |
| Raahe/Ylivieska | 315 | 145 | 7 | 86 | 192 | 177 | 101 |
| Kemi | 282 | 102 | 2 | 135 | 126 | 121 | 58 |
| Kittilä | 281 | 0 | 0 | 259 | 0 | 0 | 0 |
| Lapua | 324 | 142 | 16 | 85 | 163 | 137 | 69 |
| Salo | 396 | 116 | 1 | 102 | 132 | 113 | 8 |
| Seinäjoki | 272 | 111 | 2 | 79 | 146 | 142 | 66 |
| Tampere | 324 | 79 | 12 | 82 | 125 | 106 | 22 |
| Ivalo | 216 | 1 | 0 | 204 | 1 | 1 | 0 |
| Kotka | 360 | 59 | 6 | 119 | 85 | 74 | 12 |
| Pudasjärvi-Taivalkoski | 180 | 71 | 1 | 94 | 92 | 88 | 32 |
| Joensuu | 250 | 78 | 8 | 84 | 99 | 79 | 31 |
| Espoo 19-24 | 485 | 91 | 14 | 72 | 108 | 92 | 14 |
| Kristiinankaupunki | 252 | 97 | 2 | 65 | 105 | 96 | 28 |
| Nummi | 324 | 94 | 8 | 66 | 99 | 90 | 6 |
| Kuusamo | 180 | 38 | 0 | 122 | 43 | 43 | 37 |
| Paimio | 324 | 78 | 4 | 74 | 89 | 77 | 3 |
| Veteli | 180 | 65 | 1 | 68 | 82 | 78 | 47 |
| Lappeenranta | 216 | 58 | 5 | 62 | 87 | 79 | 27 |
| Kemijärvi-Posio | 158 | 15 | 0 | 131 | 16 | 16 | 7 |
| Nurmes | 180 | 58 | 0 | 88 | 51 | 49 | 23 |
| Orivesi | 207 | 79 | 1 | 36 | 102 | 93 | 26 |
| Sodankylä | 144 | 0 | 0 | 137 | 0 | 0 | 0 |
| Pori | 216 | 61 | 2 | 46 | 90 | 74 | 29 |
| Hyvinkää | 252 | 62 | 4 | 61 | 73 | 63 | 4 |
| Mikkeli | 205 | 63 | 0 | 61 | 71 | 69 | 18 |
| Äänekoski | 180 | 64 | 0 | 55 | 77 | 72 | 43 |
| Vaasa | 144 | 55 | 4 | 43 | 88 | 72 | 22 |
| Lahti | 216 | 72 | 5 | 44 | 81 | 68 | 8 |
| Suonenjoki | 144 | 51 | 1 | 56 | 67 | 63 | 32 |
| Rovaniemi | 108 | 40 | 1 | 55 | 65 | 59 | 20 |
| E18 Muurla-Lohja | 216 | 71 | 1 | 44 | 71 | 57 | 0 |
| Kitee | 169 | 62 | 7 | 45 | 69 | 54 | 16 |
| Pyhäjärvi | 108 | 54 | 1 | 28 | 85 | 79 | 38 |
| Raisio | 216 | 69 | 9 | 40 | 69 | 53 | 7 |
| Viinijärvi | 144 | 43 | 0 | 60 | 47 | 43 | 21 |
| Jyväskylä | 252 | 67 | 18 | 24 | 81 | 59 | 1 |
| Suomussalmi | 114 | 23 | 0 | 81 | 24 | 22 | 11 |
| Porvoo | 214 | 42 | 3 | 55 | 45 | 36 | 3 |
| Juva | 144 | 37 | 1 | 51 | 44 | 40 | 8 |
| Kauhajoki | 108 | 40 | 1 | 36 | 57 | 57 | 25 |
| Kokkola | 108 | 47 | 0 | 36 | 52 | 51 | 33 |
| Lieto | 180 | 58 | 5 | 33 | 54 | 46 | 1 |
| Pihtipudas | 108 | 43 | 0 | 33 | 54 | 51 | 29 |
| Ii | 108 | 33 | 2 | 54 | 33 | 30 | 19 |
| Puolanka | 108 | 15 | 0 | 72 | 13 | 13 | 7 |
| Kouvola | 144 | 37 | 3 | 40 | 44 | 36 | 4 |
| Jämsä | 144 | 29 | 0 | 53 | 30 | 28 | 6 |
| Koskenkylä -Kotka | 144 | 29 | 4 | 30 | 51 | 40 | 6 |
| Alavus | 97 | 55 | 1 | 23 | 57 | 54 | 17 |
| Siikalatva | 77 | 47 | 1 | 15 | 62 | 56 | 36 |
| Virrat | 108 | 40 | 1 | 29 | 45 | 40 | 10 |
| Pieksämäki | 108 | 29 | 0 | 46 | 28 | 28 | 7 |
| Rovaniemi 17-22 | 72 | 24 | 1 | 43 | 29 | 28 | 11 |
| Raasepori | 180 | 35 | 4 | 36 | 35 | 27 | 0 |
| Karstula | 72 | 29 | 0 | 23 | 45 | 43 | 30 |
| Savonlinna | 97 | 33 | 3 | 25 | 42 | 39 | 13 |
| Hamina-Vaalimaa | 108 | 19 | 1 | 35 | 30 | 29 | 7 |
| Pello | 65 | 18 | 0 | 44 | 21 | 21 | 14 |
| Imatra | 108 | 29 | 0 | 31 | 32 | 31 | 7 |
| Kuhmo | 72 | 12 | 0 | 47 | 14 | 14 | 8 |
| Nilsiä | 72 | 30 | 0 | 25 | 33 | 31 | 21 |
| Ilomantsi | 72 | 12 | 0 | 45 | 11 | 11 | 1 |
| Mäntsälä | 108 | 27 | 0 | 25 | 30 | 24 | 2 |
| Keuruu | 71 | 24 | 1 | 26 | 28 | 25 | 15 |
| Iisalmi | 72 | 36 | 1 | 16 | 36 | 35 | 19 |
| Kangasala | 72 | 23 | 5 | 11 | 39 | 31 | 11 |
| Parkano | 72 | 24 | 0 | 19 | 27 | 26 | 14 |
| Espoo | 108 | 25 | 1 | 16 | 29 | 24 | 3 |
| Harjavalta | 72 | 15 | 0 | 27 | 17 | 17 | 1 |
| Merikarvia | 72 | 21 | 0 | 13 | 31 | 28 | 11 |
| Heinola | 72 | 19 | 2 | 22 | 22 | 21 | 3 |
| Huittinen | 72 | 17 | 0 | 18 | 16 | 16 | 2 |
| Hämeenlinna | 72 | 16 | 2 | 16 | 17 | 14 | 1 |
| Pielavesi | 36 | 11 | 0 | 18 | 15 | 15 | 9 |
| Ranua | 36 | 11 | 0 | 21 | 10 | 9 | 4 |
| Kankaanpää | 36 | 10 | 1 | 13 | 14 | 13 | 6 |
| Vantaa | 60 | 12 | 4 | 11 | 15 | 11 | 0 |
| Sastamala | 36 | 9 | 0 | 13 | 12 | 12 | 3 |
| Kiuruvesi | 36 | 11 | 0 | 16 | 9 | 8 | 2 |
| Loimaa | 36 | 8 | 0 | 12 | 8 | 8 | 1 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
