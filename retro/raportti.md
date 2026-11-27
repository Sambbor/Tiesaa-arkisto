# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v24) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 45 (2026-10-12 – 2026-11-25), laskentoja 488973. Päivitetty 2026-11-27T06:27:52Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 12668.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 14682 | 1242 | 26969 | 251586 | 92 % | 65 % |
| +6 h | 13678 | 2560 | 39706 | 238632 | 84 % | 74 % |
| +12 h | 14162 | 2473 | 48298 | 228155 | 85 % | 77 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 3177 | 615 | 5164 | 84 % | 62 % |
| Lappi | 3704 | 179 | 3462 | 95 % | 48 % |
| Keski-Suomi | 1307 | 299 | 3893 | 81 % | 75 % |
| Etelä-Pohjanmaa | 1052 | 343 | 2998 | 75 % | 74 % |
| Pohjois-Savo | 1106 | 310 | 2697 | 78 % | 71 % |
| Uusimaa | 146 | 23 | 3757 | 86 % | 96 % |
| Pirkanmaa | 439 | 162 | 2497 | 73 % | 85 % |
| Pohjanmaa | 411 | 111 | 2388 | 79 % | 85 % |
| Varsinais-Suomi | 165 | 46 | 2407 | 78 % | 94 % |
| Kymenlaakso | 283 | 64 | 1902 | 82 % | 87 % |
| Pohjois-Karjala | 361 | 105 | 1467 | 77 % | 80 % |
| Keski-Pohjanmaa | 623 | 98 | 1094 | 86 % | 64 % |
| Etelä-Savo | 270 | 69 | 1272 | 80 % | 82 % |
| Etelä-Karjala | 157 | 51 | 1192 | 75 % | 88 % |
| Satakunta | 150 | 34 | 1207 | 82 % | 89 % |
| Päijät-Häme | 73 | 19 | 1083 | 79 % | 94 % |
| Kanta-Häme | 68 | 14 | 770 | 83 % | 92 % |
| Kainuu | 186 | 18 | 456 | 91 % | 71 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 3061 | 20755 | 13 % |
| tiesääennuste (Digitraffic) | 4496 | 12933 | 26 % |
| märkä tie jäätyy | 3200 | 3964 | 45 % |
| lumisade | 2861 | 1926 | 60 % |
| jäätävä sade | 60 | 128 | 32 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 1478 |
| tie −1…+1 °C | 615 |
| tie alle −4 °C | 467 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 30810 | 6681 | 54185 | 394060 | 82 % | 64 % |
| +6 h | 31053 | 7041 | 73944 | 373563 | 82 % | 70 % |
| +12 h | 32410 | 6417 | 87564 | 356832 | 83 % | 73 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 11291 | 1316 | 9965 | 90 % |
| Pohjois-Pohjanmaa | 5433 | 1530 | 9590 | 78 % |
| Finavia lentokentät | 1888 | 919 | 6749 | 67 % |
| Etelä-Pohjanmaa | 1516 | 396 | 5142 | 79 % |
| Kainuu | 2221 | 481 | 3995 | 82 % |
| Pohjois-Savo | 1764 | 559 | 3979 | 76 % |
| Keski-Suomi | 1499 | 319 | 4258 | 82 % |
| Pohjois-Karjala | 1363 | 327 | 4329 | 81 % |
| Uusimaa | 215 | 79 | 4601 | 73 % |
| Varsinais-Suomi | 416 | 197 | 4041 | 68 % |
| Pirkanmaa | 578 | 216 | 3329 | 73 % |
| Pohjanmaa | 578 | 125 | 3047 | 82 % |
| Keski-Pohjanmaa | 946 | 99 | 2006 | 91 % |
| Etelä-Savo | 415 | 98 | 2491 | 81 % |
| Kymenlaakso | 333 | 88 | 1980 | 79 % |
| Etelä-Karjala | 225 | 164 | 1318 | 58 % |
| Satakunta | 204 | 80 | 1162 | 72 % |
| Päijät-Häme | 86 | 19 | 1206 | 82 % |
| Kanta-Häme | 82 | 20 | 756 | 80 % |
| Ahvenanmaa | 0 | 9 | 0 | 0 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 10294 | 37775 |
| tiesääennuste (Digitraffic) | 10714 | 24890 |
| märkä tie jäätyy | 4063 | 6984 |
| lumisade | 5789 | 4007 |
| jäätävä sade | 193 | 288 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 4261 |
| kitka < 0,45 | 1472 |
| keli lumi | 801 |
| jäätä tiellä | 416 |
| keli kuura | 91 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 37278 | 7525 (20 %) | 70697 | 0 (0 %) | 0 (0 %) | 7669 (11 %) |
| 0,5–2 | 7196 | 1379 (19 %) | 13954 | 0 (0 %) | 0 (0 %) | 1631 (12 %) |
| 2–4 | 4766 | 948 (20 %) | 10247 | 0 (0 %) | 0 (0 %) | 1164 (11 %) |
| 4–8 | 4676 | 965 (21 %) | 11010 | 4 (0 %) | 0 (0 %) | 1017 (9 %) |
| yli 8 | 6049 | 1828 (30 %) | 17702 | 1123 (6 %) | 0 (0 %) | 1741 (10 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 13884 | 28 % (30 % / 15432) | 22239 | 33 % (36 % / 28156) |
| −4…−2 | 2657 | 22 % (20 % / 3050) | 6126 | 39 % (40 % / 7784) |
| −6…−4 | 398 | 33 % (28 % / 438) | 2127 | 60 % (57 % / 2737) |
| −8…−6 | 45 | 58 % (40 % / 60) | 917 | 67 % (60 % / 1200) |
| alle −8 | 1 | 0 % (0 % / 26) | 1112 | 88 % (81 % / 1343) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 39 päivältä, 18183 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 5376 | 1928 |
| Vain urakka suolasi | 418 | 15 |
| Vain ennuste hälytti | 6194 | 1961 |
| Kumpikaan ei | 6195 | 71 |

Suolauskertoja 6853: ennuste hälytti 0–12 h ennen 5925 kertaa (86 %), keskimäärin 7,5 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 2256 kertaa (33 %).
Liukkaista asemavuorokausista 3975: suolattu ennen ensimmäistä liukasta mittausta 1138, vasta sen jälkeen (6 h sisällä) 572.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 3338 | 732 | 142 | 1141 | 971 | 755 | 211 |
| Oulu | 546 | 248 | 29 | 173 | 256 | 198 | 98 |
| Kuopio | 429 | 199 | 13 | 94 | 300 | 257 | 133 |
| Raahe/Ylivieska | 342 | 155 | 7 | 102 | 204 | 189 | 111 |
| Kajaani | 312 | 171 | 1 | 78 | 226 | 215 | 83 |
| Lapua | 351 | 153 | 16 | 102 | 179 | 151 | 82 |
| Kemi | 306 | 102 | 2 | 154 | 126 | 121 | 57 |
| Kittilä | 304 | 0 | 0 | 275 | 0 | 0 | 0 |
| Salo | 429 | 123 | 1 | 118 | 147 | 129 | 21 |
| Kotka | 390 | 80 | 6 | 127 | 126 | 108 | 24 |
| Seinäjoki | 296 | 118 | 2 | 92 | 156 | 150 | 73 |
| Tampere | 354 | 99 | 15 | 83 | 158 | 128 | 44 |
| Espoo 19-24 | 527 | 108 | 22 | 85 | 143 | 117 | 21 |
| Ivalo | 234 | 1 | 0 | 222 | 1 | 1 | 0 |
| Joensuu | 271 | 92 | 9 | 87 | 122 | 97 | 47 |
| Pudasjärvi-Taivalkoski | 195 | 71 | 1 | 109 | 92 | 88 | 32 |
| Nummi | 351 | 105 | 9 | 76 | 122 | 106 | 14 |
| Kristiinankaupunki | 273 | 107 | 2 | 74 | 120 | 106 | 35 |
| Paimio | 351 | 89 | 4 | 79 | 97 | 82 | 8 |
| Lappeenranta | 234 | 75 | 5 | 62 | 114 | 105 | 37 |
| Kuusamo | 195 | 37 | 1 | 132 | 43 | 42 | 37 |
| Orivesi | 225 | 91 | 1 | 40 | 129 | 117 | 47 |
| Veteli | 195 | 70 | 1 | 78 | 88 | 84 | 47 |
| Kemijärvi-Posio | 173 | 15 | 0 | 146 | 16 | 16 | 7 |
| Hyvinkää | 273 | 78 | 7 | 63 | 98 | 85 | 17 |
| Pori | 234 | 73 | 4 | 47 | 114 | 92 | 37 |
| Mikkeli | 223 | 77 | 0 | 65 | 96 | 94 | 28 |
| Nurmes | 195 | 67 | 0 | 94 | 62 | 59 | 30 |
| Äänekoski | 197 | 79 | 1 | 56 | 100 | 93 | 62 |
| Lahti | 234 | 87 | 5 | 46 | 107 | 91 | 19 |
| Sodankylä | 156 | 0 | 0 | 149 | 0 | 0 | 0 |
| Vaasa | 156 | 58 | 4 | 52 | 91 | 75 | 23 |
| Suonenjoki | 156 | 56 | 1 | 63 | 79 | 74 | 41 |
| Kitee | 184 | 71 | 8 | 50 | 84 | 67 | 27 |
| E18 Muurla-Lohja | 234 | 76 | 2 | 48 | 84 | 67 | 2 |
| Rovaniemi | 117 | 41 | 1 | 63 | 66 | 60 | 20 |
| Jyväskylä | 273 | 73 | 26 | 29 | 97 | 66 | 4 |
| Porvoo | 232 | 49 | 3 | 62 | 62 | 51 | 13 |
| Viinijärvi | 156 | 48 | 0 | 65 | 58 | 52 | 31 |
| Pyhäjärvi | 117 | 56 | 1 | 35 | 87 | 79 | 40 |
| Raisio | 234 | 80 | 9 | 42 | 79 | 59 | 15 |
| Suomussalmi | 126 | 23 | 0 | 92 | 24 | 22 | 11 |
| Juva | 156 | 45 | 1 | 54 | 57 | 53 | 18 |
| Kouvola | 156 | 45 | 3 | 42 | 63 | 50 | 13 |
| Kauhajoki | 117 | 43 | 1 | 41 | 63 | 63 | 30 |
| Koskenkylä -Kotka | 156 | 34 | 6 | 33 | 67 | 49 | 11 |
| Pihtipudas | 117 | 50 | 0 | 35 | 65 | 62 | 35 |
| Kokkola | 117 | 51 | 0 | 41 | 58 | 56 | 37 |
| Lieto | 195 | 65 | 7 | 36 | 60 | 49 | 5 |
| Jämsä | 156 | 38 | 0 | 56 | 40 | 38 | 12 |
| Ii | 117 | 33 | 2 | 63 | 33 | 30 | 18 |
| Alavus | 109 | 59 | 1 | 30 | 63 | 60 | 21 |
| Puolanka | 117 | 16 | 0 | 75 | 14 | 14 | 6 |
| Siikalatva | 86 | 49 | 1 | 22 | 64 | 57 | 38 |
| Savonlinna | 106 | 42 | 2 | 26 | 58 | 54 | 28 |
| Virrat | 117 | 43 | 1 | 35 | 49 | 44 | 14 |
| Pieksämäki | 117 | 35 | 0 | 47 | 37 | 37 | 13 |
| Hamina-Vaalimaa | 117 | 26 | 1 | 37 | 43 | 42 | 14 |
| Raasepori | 195 | 40 | 4 | 41 | 37 | 29 | 1 |
| Imatra | 117 | 37 | 0 | 31 | 46 | 44 | 18 |
| Rovaniemi 17-22 | 78 | 24 | 1 | 47 | 29 | 28 | 11 |
| Karstula | 78 | 34 | 0 | 24 | 51 | 49 | 36 |
| Pello | 71 | 18 | 0 | 50 | 21 | 21 | 14 |
| Kuhmo | 78 | 13 | 0 | 52 | 15 | 15 | 9 |
| Mäntsälä | 117 | 30 | 0 | 29 | 36 | 27 | 5 |
| Nilsiä | 78 | 31 | 0 | 30 | 34 | 32 | 22 |
| Ilomantsi | 78 | 14 | 0 | 49 | 14 | 14 | 1 |
| Iisalmi | 78 | 36 | 1 | 22 | 36 | 35 | 19 |
| Kangasala | 78 | 26 | 7 | 10 | 47 | 35 | 15 |
| Keuruu | 75 | 26 | 1 | 27 | 30 | 26 | 15 |
| Parkano | 78 | 28 | 0 | 20 | 36 | 35 | 22 |
| Espoo | 117 | 29 | 2 | 18 | 37 | 28 | 3 |
| Harjavalta | 78 | 17 | 0 | 30 | 22 | 20 | 6 |
| Merikarvia | 78 | 24 | 0 | 16 | 36 | 32 | 12 |
| Heinola | 78 | 23 | 2 | 23 | 29 | 27 | 8 |
| Hämeenlinna | 78 | 21 | 2 | 15 | 26 | 22 | 5 |
| Huittinen | 78 | 19 | 0 | 21 | 18 | 18 | 3 |
| Pielavesi | 39 | 12 | 0 | 20 | 17 | 17 | 11 |
| Ranua | 39 | 11 | 0 | 24 | 10 | 9 | 3 |
| Vantaa | 69 | 13 | 9 | 13 | 20 | 12 | 2 |
| Kankaanpää | 39 | 11 | 1 | 15 | 15 | 13 | 5 |
| Kiuruvesi | 39 | 11 | 0 | 19 | 9 | 8 | 2 |
| Sastamala | 39 | 12 | 0 | 12 | 14 | 14 | 4 |
| Loimaa | 39 | 9 | 1 | 13 | 10 | 9 | 2 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
