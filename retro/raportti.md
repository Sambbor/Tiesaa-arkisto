# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v18) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 37 (2026-10-12 – 2026-11-17), laskentoja 398017. Päivitetty 2026-11-19T13:50:40Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 10373.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 6183 | 257 | 26533 | 206570 | 96 % | 81 % |
| +6 h | 5749 | 792 | 33140 | 199977 | 88 % | 85 % |
| +12 h | 5930 | 742 | 35909 | 195612 | 89 % | 86 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 1706 | 235 | 4564 | 88 % | 73 % |
| Lappi | 2060 | 80 | 3388 | 96 % | 62 % |
| Keski-Suomi | 397 | 101 | 3427 | 80 % | 90 % |
| Etelä-Pohjanmaa | 282 | 85 | 2691 | 77 % | 91 % |
| Pohjois-Savo | 397 | 101 | 2376 | 80 % | 86 % |
| Uusimaa | 9 | 5 | 2775 | 64 % | 100 % |
| Pirkanmaa | 77 | 10 | 2006 | 89 % | 96 % |
| Pohjanmaa | 132 | 42 | 1753 | 76 % | 93 % |
| Varsinais-Suomi | 5 | 7 | 1749 | 42 % | 100 % |
| Kymenlaakso | 51 | 12 | 1514 | 81 % | 97 % |
| Pohjois-Karjala | 118 | 40 | 1283 | 75 % | 92 % |
| Keski-Pohjanmaa | 243 | 20 | 988 | 92 % | 80 % |
| Etelä-Savo | 95 | 22 | 902 | 81 % | 90 % |
| Etelä-Karjala | 73 | 23 | 888 | 76 % | 92 % |
| Satakunta | 13 | 0 | 917 | 100 % | 99 % |
| Päijät-Häme | 5 | 4 | 878 | 56 % | 99 % |
| Kanta-Häme | 0 | 0 | 650 | – % | 100 % |
| Kainuu | 86 | 5 | 391 | 95 % | 82 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 1722 | 17864 | 9 % |
| tiesääennuste (Digitraffic) | 1256 | 7637 | 14 % |
| lumisade | 1507 | 2316 | 39 % |
| märkä tie jäätyy | 1058 | 2718 | 28 % |
| lumi / sohjo | 69 | 1435 | 5 % |
| jäätävä sade | 137 | 1170 | 10 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 452 |
| tie −1…+1 °C | 186 |
| tie alle −4 °C | 154 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 17302 | 1139 | 48016 | 328368 | 94 % | 74 % |
| +6 h | 15547 | 3156 | 59316 | 316697 | 83 % | 79 % |
| +12 h | 16190 | 2920 | 64334 | 308911 | 85 % | 80 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 6773 | 833 | 8830 | 89 % |
| Pohjois-Pohjanmaa | 3326 | 700 | 7736 | 83 % |
| Finavia lentokentät | 562 | 454 | 5022 | 55 % |
| Etelä-Pohjanmaa | 488 | 104 | 4336 | 82 % |
| Kainuu | 1154 | 176 | 3143 | 87 % |
| Keski-Suomi | 536 | 101 | 3727 | 84 % |
| Pohjois-Savo | 801 | 152 | 3406 | 84 % |
| Pohjois-Karjala | 551 | 124 | 3516 | 82 % |
| Uusimaa | 36 | 27 | 3489 | 57 % |
| Varsinais-Suomi | 115 | 40 | 2904 | 74 % |
| Pirkanmaa | 144 | 29 | 2621 | 83 % |
| Pohjanmaa | 195 | 48 | 2092 | 80 % |
| Keski-Pohjanmaa | 454 | 38 | 1662 | 92 % |
| Etelä-Savo | 158 | 38 | 1756 | 81 % |
| Kymenlaakso | 84 | 28 | 1566 | 75 % |
| Etelä-Karjala | 120 | 245 | 990 | 33 % |
| Päijät-Häme | 17 | 3 | 962 | 85 % |
| Satakunta | 25 | 13 | 916 | 66 % |
| Kanta-Häme | 8 | 3 | 642 | 73 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 6382 | 32160 |
| tiesääennuste (Digitraffic) | 3640 | 13339 |
| lumisade | 3434 | 4694 |
| märkä tie jäätyy | 1605 | 4651 |
| jäätävä sade | 333 | 2235 |
| lumi / sohjo | 153 | 2237 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 1991 |
| varoitus häly | 557 |
| kitka < 0,45 | 318 |
| jäätä tiellä | 125 |
| keli lumi | 93 |
| keli kuura | 72 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 19361 | 2377 (12 %) | 38832 | 0 (0 %) | 3737 (10 %) | 6969 (18 %) |
| 0,5–2 | 5195 | 636 (12 %) | 10092 | 0 (0 %) | 2655 (26 %) | 1866 (18 %) |
| 2–4 | 3689 | 473 (13 %) | 7764 | 0 (0 %) | 1879 (24 %) | 1651 (21 %) |
| 4–8 | 4011 | 507 (13 %) | 8782 | 2 (0 %) | 1999 (23 %) | 1916 (22 %) |
| yli 8 | 5730 | 1097 (19 %) | 14888 | 472 (3 %) | 2301 (15 %) | 3930 (26 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 8333 | 20 % (18 % / 12975) | 13455 | 20 % (23 % / 22121) |
| −4…−2 | 2235 | 20 % (15 % / 3745) | 4146 | 30 % (32 % / 6802) |
| −6…−4 | 327 | 45 % (29 % / 552) | 966 | 66 % (55 % / 1669) |
| −8…−6 | 33 | 73 % (68 % / 44) | 358 | 70 % (62 % / 489) |
| alle −8 | 0 | – (73 % / 22) | 541 | 84 % (77 % / 659) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 31 päivältä, 14385 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 3727 | 948 |
| Vain urakka suolasi | 212 | 4 |
| Vain ennuste hälytti | 5155 | 1301 |
| Kumpikaan ei | 5291 | 23 |

Suolauskertoja 4251: ennuste hälytti 0–12 h ennen 3742 kertaa (88 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 942 kertaa (22 %).
Liukkaista asemavuorokausista 2276: suolattu ennen ensimmäistä liukasta mittausta 533, vasta sen jälkeen (6 h sisällä) 282.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2636 | 514 | 90 | 913 | 621 | 481 | 65 |
| Oulu | 434 | 211 | 21 | 119 | 195 | 151 | 62 |
| Kuopio | 341 | 134 | 0 | 92 | 169 | 158 | 52 |
| Kajaani | 248 | 130 | 0 | 59 | 165 | 157 | 48 |
| Kittilä | 243 | 0 | 0 | 222 | 0 | 0 | 0 |
| Kemi | 242 | 78 | 1 | 129 | 85 | 82 | 32 |
| Raahe/Ylivieska | 270 | 103 | 6 | 91 | 121 | 110 | 51 |
| Lapua | 279 | 115 | 8 | 79 | 125 | 107 | 39 |
| Salo | 341 | 84 | 0 | 105 | 86 | 71 | 7 |
| Ivalo | 186 | 1 | 0 | 174 | 1 | 1 | 0 |
| Seinäjoki | 232 | 87 | 0 | 76 | 97 | 96 | 21 |
| Tampere | 279 | 58 | 5 | 83 | 87 | 78 | 9 |
| Joensuu | 217 | 58 | 6 | 88 | 82 | 65 | 22 |
| Kotka | 310 | 40 | 4 | 114 | 52 | 45 | 7 |
| Pudasjärvi-Taivalkoski | 155 | 61 | 1 | 79 | 72 | 68 | 20 |
| Espoo 19-24 | 415 | 65 | 5 | 79 | 65 | 54 | 0 |
| Nummi | 279 | 69 | 5 | 73 | 71 | 65 | 5 |
| Kuusamo | 155 | 36 | 0 | 99 | 41 | 41 | 35 |
| Kristiinankaupunki | 217 | 77 | 2 | 61 | 77 | 68 | 9 |
| Paimio | 279 | 56 | 2 | 73 | 61 | 53 | 1 |
| Veteli | 155 | 49 | 0 | 61 | 63 | 61 | 30 |
| Orivesi | 177 | 62 | 0 | 44 | 79 | 73 | 15 |
| Lappeenranta | 186 | 45 | 1 | 56 | 66 | 63 | 23 |
| Kemijärvi-Posio | 133 | 14 | 0 | 107 | 15 | 15 | 6 |
| Hyvinkää | 217 | 45 | 0 | 67 | 51 | 45 | 4 |
| Sodankylä | 124 | 0 | 0 | 117 | 0 | 0 | 0 |
| Nurmes | 155 | 48 | 0 | 74 | 40 | 38 | 15 |
| Mikkeli | 175 | 50 | 0 | 57 | 54 | 53 | 13 |
| Äänekoski | 155 | 46 | 0 | 55 | 55 | 51 | 24 |
| Lahti | 186 | 58 | 1 | 47 | 61 | 53 | 6 |
| Pori | 186 | 46 | 1 | 48 | 58 | 47 | 12 |
| Vaasa | 124 | 47 | 4 | 31 | 73 | 60 | 10 |
| Suonenjoki | 124 | 39 | 1 | 51 | 48 | 47 | 16 |
| Rovaniemi | 93 | 36 | 1 | 44 | 54 | 48 | 12 |
| E18 Muurla-Lohja | 186 | 54 | 0 | 46 | 50 | 43 | 0 |
| Kitee | 144 | 55 | 4 | 38 | 54 | 41 | 9 |
| Viinijärvi | 124 | 29 | 0 | 59 | 31 | 28 | 15 |
| Juva | 124 | 31 | 1 | 48 | 38 | 35 | 6 |
| Porvoo | 184 | 28 | 1 | 54 | 31 | 26 | 2 |
| Raisio | 186 | 55 | 6 | 33 | 52 | 39 | 3 |
| Pyhäjärvi | 93 | 42 | 0 | 26 | 58 | 55 | 16 |
| Suomussalmi | 94 | 19 | 0 | 65 | 18 | 16 | 6 |
| Jyväskylä | 217 | 51 | 13 | 29 | 51 | 37 | 0 |
| Jämsä | 124 | 25 | 0 | 53 | 26 | 26 | 2 |
| Kokkola | 93 | 33 | 0 | 36 | 36 | 36 | 19 |
| Puolanka | 93 | 10 | 0 | 62 | 10 | 10 | 5 |
| Kouvola | 124 | 28 | 0 | 39 | 32 | 29 | 3 |
| Kauhajoki | 93 | 32 | 0 | 32 | 39 | 39 | 11 |
| Ii | 93 | 28 | 1 | 46 | 25 | 24 | 15 |
| Pihtipudas | 93 | 31 | 0 | 33 | 36 | 34 | 12 |
| Lieto | 155 | 43 | 5 | 29 | 39 | 31 | 0 |
| Pieksämäki | 93 | 23 | 0 | 42 | 22 | 22 | 6 |
| Virrat | 93 | 30 | 1 | 30 | 32 | 29 | 5 |
| Rovaniemi 17-22 | 62 | 21 | 0 | 38 | 24 | 24 | 7 |
| Koskenkylä -Kotka | 124 | 19 | 2 | 31 | 30 | 23 | 0 |
| Alavus | 77 | 40 | 0 | 23 | 38 | 36 | 5 |
| Savonlinna | 82 | 28 | 0 | 24 | 34 | 33 | 10 |
| Imatra | 93 | 23 | 0 | 33 | 25 | 24 | 3 |
| Raasepori | 155 | 26 | 3 | 33 | 24 | 19 | 0 |
| Hamina-Vaalimaa | 93 | 13 | 1 | 33 | 20 | 19 | 2 |
| Pello | 55 | 10 | 0 | 42 | 11 | 11 | 6 |
| Karstula | 62 | 21 | 0 | 22 | 30 | 29 | 15 |
| Kuhmo | 62 | 10 | 0 | 39 | 11 | 11 | 5 |
| Nilsiä | 62 | 21 | 0 | 25 | 24 | 23 | 13 |
| Siikalatva | 62 | 34 | 1 | 13 | 35 | 32 | 14 |
| Mäntsälä | 93 | 18 | 0 | 27 | 20 | 17 | 2 |
| Ilomantsi | 62 | 9 | 0 | 39 | 8 | 8 | 0 |
| Keuruu | 62 | 19 | 1 | 23 | 23 | 22 | 11 |
| Kangasala | 62 | 19 | 2 | 10 | 31 | 27 | 6 |
| Iisalmi | 62 | 29 | 0 | 14 | 26 | 26 | 11 |
| Espoo | 93 | 16 | 1 | 20 | 18 | 14 | 0 |
| Parkano | 62 | 18 | 0 | 21 | 16 | 15 | 5 |
| Heinola | 62 | 16 | 0 | 20 | 16 | 16 | 1 |
| Harjavalta | 62 | 12 | 0 | 21 | 12 | 12 | 0 |
| Merikarvia | 62 | 17 | 0 | 11 | 22 | 19 | 4 |
| Hämeenlinna | 62 | 11 | 1 | 19 | 11 | 10 | 1 |
| Huittinen | 62 | 13 | 0 | 16 | 12 | 12 | 0 |
| Pielavesi | 31 | 8 | 0 | 16 | 12 | 12 | 6 |
| Ranua | 31 | 9 | 0 | 18 | 8 | 7 | 3 |
| Kankaanpää | 31 | 9 | 0 | 11 | 10 | 10 | 3 |
| Kiuruvesi | 31 | 9 | 0 | 13 | 8 | 8 | 2 |
| Vantaa | 50 | 8 | 3 | 9 | 10 | 6 | 0 |
| Loimaa | 31 | 5 | 0 | 13 | 5 | 5 | 1 |
| Sastamala | 31 | 7 | 0 | 11 | 7 | 7 | 0 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
