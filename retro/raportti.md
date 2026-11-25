# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v22) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 43 (2026-10-12 – 2026-11-23), laskentoja 466118. Päivitetty 2026-11-25T06:11:30Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 12094.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 12754 | 532 | 28279 | 239162 | 96 % | 69 % |
| +6 h | 11746 | 1750 | 38319 | 229010 | 87 % | 77 % |
| +12 h | 12019 | 1773 | 44569 | 220976 | 87 % | 79 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 2652 | 447 | 5098 | 86 % | 66 % |
| Lappi | 3246 | 133 | 3504 | 96 % | 52 % |
| Keski-Suomi | 1079 | 185 | 3789 | 85 % | 78 % |
| Etelä-Pohjanmaa | 891 | 245 | 2976 | 78 % | 77 % |
| Pohjois-Savo | 1013 | 217 | 2617 | 82 % | 72 % |
| Uusimaa | 143 | 21 | 3642 | 87 % | 96 % |
| Pirkanmaa | 403 | 53 | 2319 | 88 % | 85 % |
| Pohjanmaa | 318 | 92 | 2198 | 78 % | 87 % |
| Varsinais-Suomi | 147 | 43 | 2312 | 77 % | 94 % |
| Kymenlaakso | 219 | 37 | 1811 | 86 % | 89 % |
| Pohjois-Karjala | 316 | 89 | 1430 | 78 % | 82 % |
| Keski-Pohjanmaa | 505 | 57 | 1067 | 90 % | 68 % |
| Etelä-Savo | 244 | 48 | 1159 | 84 % | 83 % |
| Satakunta | 139 | 26 | 1156 | 84 % | 89 % |
| Etelä-Karjala | 137 | 32 | 1063 | 81 % | 89 % |
| Päijät-Häme | 70 | 5 | 1043 | 93 % | 94 % |
| Kanta-Häme | 66 | 6 | 705 | 92 % | 91 % |
| Kainuu | 158 | 14 | 430 | 92 % | 73 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 2490 | 20405 | 11 % |
| tiesääennuste (Digitraffic) | 3549 | 11378 | 24 % |
| märkä tie jäätyy | 2778 | 4450 | 38 % |
| lumisade | 2869 | 1954 | 59 % |
| jäätävä sade | 60 | 132 | 31 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 977 |
| tie −1…+1 °C | 548 |
| tie alle −4 °C | 225 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 31531 | 1837 | 55560 | 373964 | 94 % | 64 % |
| +6 h | 27914 | 5903 | 70604 | 358346 | 83 % | 72 % |
| +12 h | 28885 | 5527 | 80140 | 345833 | 84 % | 74 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 10256 | 1206 | 9766 | 89 % |
| Pohjois-Pohjanmaa | 4930 | 1204 | 9257 | 80 % |
| Finavia lentokentät | 1468 | 1030 | 6153 | 59 % |
| Etelä-Pohjanmaa | 1346 | 321 | 4999 | 81 % |
| Kainuu | 2086 | 369 | 3825 | 85 % |
| Pohjois-Savo | 1666 | 405 | 3842 | 80 % |
| Pohjois-Karjala | 1223 | 240 | 4213 | 84 % |
| Keski-Suomi | 1304 | 195 | 4109 | 87 % |
| Uusimaa | 216 | 51 | 4496 | 81 % |
| Varsinais-Suomi | 328 | 118 | 3944 | 74 % |
| Pirkanmaa | 535 | 97 | 3111 | 85 % |
| Pohjanmaa | 507 | 118 | 2714 | 81 % |
| Keski-Pohjanmaa | 851 | 94 | 1886 | 90 % |
| Etelä-Savo | 351 | 68 | 2283 | 84 % |
| Kymenlaakso | 278 | 63 | 1871 | 82 % |
| Etelä-Karjala | 211 | 254 | 1176 | 45 % |
| Satakunta | 191 | 51 | 1113 | 79 % |
| Päijät-Häme | 86 | 9 | 1156 | 91 % |
| Kanta-Häme | 81 | 10 | 690 | 89 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 9012 | 36417 |
| tiesääennuste (Digitraffic) | 8975 | 21005 |
| märkä tie jäätyy | 3877 | 8950 |
| lumisade | 5866 | 3936 |
| jäätävä sade | 184 | 296 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 3213 |
| kitka < 0,45 | 867 |
| varoitus häly | 713 |
| keli lumi | 672 |
| jäätä tiellä | 359 |
| keli kuura | 79 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 28912 | 5739 (20 %) | 56887 | 0 (0 %) | 4239 (7 %) | 14559 (26 %) |
| 0,5–2 | 6872 | 1135 (17 %) | 13362 | 0 (0 %) | 2970 (22 %) | 3026 (23 %) |
| 2–4 | 4722 | 864 (18 %) | 10092 | 0 (0 %) | 2065 (20 %) | 2573 (25 %) |
| 4–8 | 4938 | 879 (18 %) | 11099 | 2 (0 %) | 2165 (20 %) | 2955 (27 %) |
| yli 8 | 6551 | 1642 (25 %) | 17729 | 732 (4 %) | 2629 (15 %) | 5746 (32 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 14465 | 29 % (27 % / 21495) | 23058 | 31 % (32 % / 35942) |
| −4…−2 | 2682 | 22 % (17 % / 4500) | 5383 | 35 % (36 % / 8671) |
| −6…−4 | 373 | 42 % (27 % / 638) | 1367 | 63 % (55 % / 2219) |
| −8…−6 | 33 | 73 % (51 % / 81) | 568 | 74 % (63 % / 788) |
| alle −8 | 0 | – (65 % / 48) | 845 | 90 % (80 % / 1073) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 37 päivältä, 17228 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 5152 | 1868 |
| Vain urakka suolasi | 354 | 7 |
| Vain ennuste hälytti | 5725 | 1782 |
| Kumpikaan ei | 5997 | 25 |

Suolauskertoja 6514: ennuste hälytti 0–12 h ennen 5735 kertaa (88 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 2167 kertaa (33 %).
Liukkaista asemavuorokausista 3682: suolattu ennen ensimmäistä liukasta mittausta 1091, vasta sen jälkeen (6 h sisällä) 544.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 3162 | 710 | 121 | 1066 | 923 | 728 | 195 |
| Oulu | 518 | 249 | 28 | 150 | 256 | 200 | 99 |
| Kuopio | 407 | 183 | 11 | 92 | 271 | 241 | 124 |
| Raahe/Ylivieska | 324 | 148 | 7 | 92 | 197 | 182 | 106 |
| Kajaani | 296 | 171 | 0 | 64 | 225 | 217 | 83 |
| Kemi | 290 | 102 | 2 | 143 | 126 | 121 | 58 |
| Kittilä | 288 | 0 | 0 | 266 | 0 | 0 | 0 |
| Lapua | 333 | 151 | 16 | 85 | 177 | 150 | 81 |
| Salo | 407 | 123 | 1 | 106 | 147 | 128 | 21 |
| Seinäjoki | 280 | 116 | 2 | 82 | 153 | 148 | 73 |
| Kotka | 370 | 69 | 6 | 119 | 110 | 99 | 26 |
| Tampere | 334 | 88 | 13 | 82 | 145 | 125 | 37 |
| Ivalo | 222 | 1 | 0 | 210 | 1 | 1 | 0 |
| Espoo 19-24 | 499 | 105 | 14 | 72 | 131 | 115 | 21 |
| Joensuu | 257 | 85 | 8 | 84 | 111 | 90 | 40 |
| Pudasjärvi-Taivalkoski | 185 | 71 | 1 | 99 | 92 | 88 | 32 |
| Nummi | 333 | 103 | 8 | 66 | 119 | 107 | 13 |
| Kristiinankaupunki | 259 | 104 | 2 | 65 | 116 | 107 | 34 |
| Paimio | 333 | 85 | 4 | 76 | 97 | 85 | 8 |
| Kuusamo | 185 | 38 | 0 | 127 | 43 | 43 | 37 |
| Lappeenranta | 222 | 64 | 5 | 62 | 99 | 91 | 35 |
| Orivesi | 213 | 85 | 1 | 36 | 121 | 111 | 42 |
| Veteli | 185 | 69 | 1 | 69 | 87 | 83 | 52 |
| Kemijärvi-Posio | 163 | 15 | 0 | 136 | 16 | 16 | 7 |
| Pori | 222 | 66 | 3 | 46 | 104 | 84 | 34 |
| Hyvinkää | 259 | 69 | 4 | 61 | 85 | 75 | 14 |
| Nurmes | 185 | 63 | 0 | 88 | 58 | 55 | 29 |
| Mikkeli | 211 | 69 | 0 | 61 | 84 | 82 | 27 |
| Äänekoski | 185 | 69 | 0 | 55 | 87 | 82 | 51 |
| Sodankylä | 148 | 0 | 0 | 141 | 0 | 0 | 0 |
| Lahti | 222 | 78 | 5 | 44 | 96 | 83 | 17 |
| Vaasa | 148 | 58 | 4 | 44 | 91 | 75 | 23 |
| Suonenjoki | 148 | 54 | 1 | 57 | 75 | 71 | 40 |
| E18 Muurla-Lohja | 222 | 77 | 1 | 44 | 84 | 68 | 2 |
| Rovaniemi | 111 | 40 | 1 | 58 | 65 | 59 | 20 |
| Raisio | 222 | 75 | 9 | 40 | 79 | 61 | 15 |
| Kitee | 174 | 67 | 7 | 45 | 74 | 59 | 21 |
| Viinijärvi | 148 | 47 | 0 | 60 | 57 | 53 | 30 |
| Pyhäjärvi | 111 | 56 | 1 | 29 | 87 | 80 | 40 |
| Porvoo | 220 | 48 | 3 | 55 | 60 | 51 | 13 |
| Jyväskylä | 259 | 74 | 18 | 24 | 90 | 67 | 4 |
| Suomussalmi | 118 | 23 | 0 | 85 | 24 | 22 | 11 |
| Juva | 148 | 40 | 1 | 52 | 52 | 48 | 15 |
| Kauhajoki | 111 | 43 | 1 | 36 | 63 | 63 | 30 |
| Kouvola | 148 | 41 | 3 | 40 | 57 | 48 | 13 |
| Pihtipudas | 111 | 46 | 0 | 33 | 61 | 58 | 34 |
| Lieto | 185 | 63 | 5 | 33 | 60 | 51 | 5 |
| Kokkola | 111 | 50 | 0 | 36 | 57 | 55 | 38 |
| Koskenkylä -Kotka | 148 | 33 | 4 | 30 | 60 | 49 | 11 |
| Ii | 111 | 33 | 2 | 57 | 33 | 30 | 19 |
| Puolanka | 111 | 16 | 0 | 74 | 14 | 14 | 8 |
| Jämsä | 148 | 33 | 0 | 53 | 34 | 32 | 9 |
| Alavus | 101 | 59 | 1 | 23 | 63 | 60 | 22 |
| Pieksämäki | 111 | 32 | 0 | 46 | 34 | 34 | 13 |
| Siikalatva | 80 | 49 | 1 | 16 | 64 | 58 | 38 |
| Virrat | 111 | 43 | 1 | 29 | 49 | 44 | 14 |
| Savonlinna | 100 | 36 | 3 | 25 | 52 | 49 | 23 |
| Raasepori | 185 | 37 | 4 | 39 | 37 | 29 | 1 |
| Rovaniemi 17-22 | 74 | 24 | 1 | 45 | 29 | 28 | 11 |
| Hamina-Vaalimaa | 111 | 22 | 1 | 35 | 37 | 36 | 13 |
| Karstula | 74 | 31 | 0 | 23 | 48 | 46 | 33 |
| Imatra | 111 | 32 | 0 | 31 | 38 | 37 | 13 |
| Pello | 67 | 18 | 0 | 46 | 21 | 21 | 14 |
| Kuhmo | 74 | 13 | 0 | 48 | 15 | 15 | 9 |
| Mäntsälä | 111 | 30 | 0 | 25 | 36 | 30 | 5 |
| Nilsiä | 74 | 31 | 0 | 26 | 34 | 32 | 22 |
| Ilomantsi | 74 | 13 | 0 | 46 | 12 | 12 | 1 |
| Keuruu | 72 | 25 | 1 | 26 | 29 | 26 | 16 |
| Kangasala | 74 | 25 | 5 | 11 | 43 | 34 | 14 |
| Iisalmi | 74 | 36 | 1 | 18 | 36 | 35 | 19 |
| Parkano | 74 | 26 | 0 | 19 | 34 | 33 | 21 |
| Espoo | 111 | 28 | 1 | 16 | 35 | 27 | 4 |
| Harjavalta | 74 | 17 | 0 | 27 | 22 | 21 | 6 |
| Heinola | 74 | 21 | 2 | 22 | 27 | 26 | 7 |
| Merikarvia | 74 | 23 | 0 | 13 | 35 | 31 | 12 |
| Hämeenlinna | 74 | 18 | 2 | 16 | 23 | 20 | 5 |
| Huittinen | 74 | 19 | 0 | 18 | 18 | 18 | 3 |
| Pielavesi | 37 | 12 | 0 | 18 | 17 | 17 | 11 |
| Ranua | 37 | 11 | 0 | 22 | 10 | 9 | 4 |
| Vantaa | 63 | 14 | 5 | 11 | 17 | 13 | 2 |
| Kankaanpää | 37 | 11 | 1 | 13 | 15 | 14 | 7 |
| Kiuruvesi | 37 | 11 | 0 | 17 | 9 | 8 | 2 |
| Sastamala | 37 | 10 | 0 | 13 | 12 | 12 | 3 |
| Loimaa | 37 | 9 | 0 | 12 | 9 | 9 | 2 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
