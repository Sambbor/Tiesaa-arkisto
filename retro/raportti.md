# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v20) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 41 (2026-10-12 – 2026-11-21), laskentoja 443433. Päivitetty 2026-11-23T06:21:56Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 11518.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 8563 | 365 | 29846 | 228173 | 96 % | 78 % |
| +6 h | 8219 | 1086 | 37695 | 220050 | 88 % | 82 % |
| +12 h | 8773 | 1027 | 42191 | 213577 | 90 % | 83 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 2278 | 296 | 5688 | 89 % | 71 % |
| Lappi | 2835 | 116 | 3751 | 96 % | 57 % |
| Keski-Suomi | 642 | 135 | 3650 | 83 % | 85 % |
| Etelä-Pohjanmaa | 532 | 103 | 2990 | 84 % | 85 % |
| Pohjois-Savo | 630 | 164 | 2639 | 79 % | 81 % |
| Uusimaa | 20 | 9 | 3363 | 69 % | 99 % |
| Pohjanmaa | 242 | 53 | 2108 | 82 % | 90 % |
| Pirkanmaa | 113 | 22 | 2160 | 84 % | 95 % |
| Varsinais-Suomi | 5 | 7 | 2072 | 42 % | 100 % |
| Kymenlaakso | 77 | 13 | 1642 | 86 % | 96 % |
| Pohjois-Karjala | 116 | 61 | 1487 | 66 % | 93 % |
| Keski-Pohjanmaa | 371 | 22 | 1119 | 94 % | 75 % |
| Etelä-Savo | 108 | 39 | 1004 | 73 % | 90 % |
| Satakunta | 59 | 4 | 1013 | 94 % | 94 % |
| Etelä-Karjala | 72 | 25 | 934 | 74 % | 93 % |
| Päijät-Häme | 4 | 5 | 917 | 44 % | 100 % |
| Kanta-Häme | 0 | 0 | 662 | – % | 100 % |
| Kainuu | 115 | 12 | 496 | 91 % | 81 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 2128 | 18748 | 10 % |
| tiesääennuste (Digitraffic) | 2480 | 12420 | 17 % |
| märkä tie jäätyy | 1750 | 5202 | 25 % |
| lumisade | 1802 | 1196 | 60 % |
| jäätävä sade | 59 | 129 | 31 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 524 |
| tie −1…+1 °C | 405 |
| tie alle −4 °C | 157 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 23896 | 1410 | 54254 | 360663 | 94 % | 69 % |
| +6 h | 21796 | 4163 | 67395 | 346749 | 84 % | 76 % |
| +12 h | 23078 | 3837 | 75146 | 335664 | 86 % | 77 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 9109 | 987 | 9677 | 90 % |
| Pohjois-Pohjanmaa | 4379 | 905 | 9538 | 83 % |
| Finavia lentokentät | 1099 | 704 | 5597 | 61 % |
| Etelä-Pohjanmaa | 826 | 128 | 4853 | 87 % |
| Kainuu | 1733 | 270 | 3706 | 87 % |
| Pohjois-Savo | 1179 | 234 | 3813 | 83 % |
| Pohjois-Karjala | 764 | 190 | 4031 | 80 % |
| Keski-Suomi | 812 | 134 | 3963 | 86 % |
| Uusimaa | 51 | 35 | 4242 | 59 % |
| Varsinais-Suomi | 133 | 44 | 3387 | 75 % |
| Pirkanmaa | 182 | 55 | 2834 | 77 % |
| Pohjanmaa | 368 | 72 | 2539 | 84 % |
| Keski-Pohjanmaa | 665 | 44 | 1889 | 94 % |
| Etelä-Savo | 170 | 43 | 1913 | 80 % |
| Kymenlaakso | 108 | 33 | 1704 | 77 % |
| Etelä-Karjala | 117 | 250 | 1045 | 32 % |
| Satakunta | 79 | 26 | 1004 | 75 % |
| Päijät-Häme | 15 | 5 | 1005 | 75 % |
| Kanta-Häme | 7 | 4 | 655 | 64 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 7852 | 34346 |
| tiesääennuste (Digitraffic) | 6744 | 21113 |
| märkä tie jäätyy | 2753 | 8838 |
| lumisade | 4266 | 2805 |
| jäätävä sade | 181 | 293 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 2441 |
| varoitus häly | 612 |
| kitka < 0,45 | 469 |
| keli lumi | 313 |
| jäätä tiellä | 256 |
| keli kuura | 72 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 23021 | 3438 (15 %) | 46866 | 0 (0 %) | 3939 (8 %) | 10156 (22 %) |
| 0,5–2 | 6231 | 909 (15 %) | 12166 | 0 (0 %) | 2832 (23 %) | 2543 (21 %) |
| 2–4 | 4306 | 679 (16 %) | 9249 | 0 (0 %) | 1984 (21 %) | 2205 (24 %) |
| 4–8 | 4566 | 713 (16 %) | 10323 | 2 (0 %) | 2102 (20 %) | 2583 (25 %) |
| yli 8 | 6140 | 1355 (22 %) | 16450 | 494 (3 %) | 2436 (15 %) | 4923 (30 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 10196 | 22 % (21 % / 15915) | 17962 | 25 % (27 % / 29474) |
| −4…−2 | 2359 | 21 % (16 % / 4049) | 4626 | 34 % (34 % / 7610) |
| −6…−4 | 330 | 45 % (29 % / 561) | 1073 | 69 % (58 % / 1811) |
| −8…−6 | 33 | 73 % (68 % / 44) | 426 | 74 % (66 % / 569) |
| alle −8 | 0 | – (73 % / 22) | 641 | 86 % (80 % / 762) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 35 päivältä, 16281 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 4523 | 1319 |
| Vain urakka suolasi | 290 | 6 |
| Vain ennuste hälytti | 5636 | 1590 |
| Kumpikaan ei | 5832 | 24 |

Suolauskertoja 5311: ennuste hälytti 0–12 h ennen 4659 kertaa (88 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 1363 kertaa (26 %).
Liukkaista asemavuorokausista 2939: suolattu ennen ensimmäistä liukasta mittausta 670, vasta sen jälkeen (6 h sisällä) 429.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2986 | 613 | 115 | 1016 | 764 | 589 | 116 |
| Oulu | 490 | 246 | 22 | 139 | 244 | 194 | 93 |
| Kuopio | 385 | 163 | 11 | 92 | 230 | 201 | 84 |
| Raahe/Ylivieska | 306 | 137 | 6 | 89 | 177 | 164 | 87 |
| Kajaani | 280 | 162 | 0 | 57 | 205 | 197 | 64 |
| Kemi | 274 | 103 | 1 | 135 | 126 | 121 | 58 |
| Kittilä | 274 | 0 | 0 | 253 | 0 | 0 | 0 |
| Lapua | 315 | 134 | 15 | 87 | 139 | 113 | 45 |
| Salo | 385 | 106 | 0 | 104 | 118 | 100 | 7 |
| Tampere | 315 | 70 | 12 | 88 | 111 | 93 | 11 |
| Ivalo | 210 | 1 | 0 | 198 | 1 | 1 | 0 |
| Seinäjoki | 264 | 103 | 2 | 82 | 115 | 111 | 35 |
| Kotka | 350 | 50 | 5 | 121 | 68 | 60 | 9 |
| Joensuu | 244 | 73 | 7 | 93 | 90 | 72 | 25 |
| Pudasjärvi-Taivalkoski | 175 | 71 | 1 | 89 | 92 | 88 | 32 |
| Espoo 19-24 | 471 | 85 | 6 | 85 | 91 | 80 | 14 |
| Nummi | 315 | 87 | 6 | 73 | 95 | 88 | 5 |
| Paimio | 315 | 72 | 2 | 77 | 84 | 76 | 1 |
| Kuusamo | 175 | 38 | 0 | 117 | 43 | 43 | 37 |
| Kristiinankaupunki | 245 | 90 | 2 | 69 | 90 | 81 | 14 |
| Lappeenranta | 210 | 53 | 4 | 65 | 80 | 74 | 24 |
| Veteli | 175 | 62 | 0 | 68 | 76 | 73 | 41 |
| Kemijärvi-Posio | 153 | 15 | 0 | 126 | 16 | 16 | 7 |
| Hyvinkää | 245 | 59 | 0 | 68 | 66 | 60 | 4 |
| Nurmes | 175 | 54 | 0 | 87 | 47 | 45 | 19 |
| Sodankylä | 140 | 0 | 0 | 133 | 0 | 0 | 0 |
| Orivesi | 201 | 73 | 1 | 38 | 93 | 87 | 20 |
| Mikkeli | 199 | 57 | 0 | 62 | 64 | 62 | 13 |
| Pori | 210 | 56 | 1 | 52 | 73 | 57 | 14 |
| Äänekoski | 175 | 59 | 0 | 56 | 68 | 64 | 34 |
| Lahti | 210 | 68 | 3 | 45 | 74 | 63 | 6 |
| Suonenjoki | 140 | 48 | 1 | 56 | 63 | 59 | 28 |
| Vaasa | 140 | 51 | 4 | 43 | 76 | 62 | 12 |
| Rovaniemi | 105 | 40 | 1 | 52 | 65 | 59 | 20 |
| E18 Muurla-Lohja | 210 | 66 | 0 | 45 | 65 | 54 | 0 |
| Kitee | 164 | 58 | 6 | 49 | 59 | 44 | 9 |
| Viinijärvi | 140 | 39 | 0 | 64 | 41 | 38 | 18 |
| Raisio | 210 | 67 | 6 | 40 | 64 | 50 | 4 |
| Pyhäjärvi | 105 | 52 | 0 | 28 | 75 | 71 | 28 |
| Jyväskylä | 245 | 65 | 13 | 31 | 70 | 55 | 1 |
| Suomussalmi | 110 | 22 | 0 | 78 | 21 | 19 | 8 |
| Porvoo | 208 | 38 | 1 | 58 | 40 | 32 | 2 |
| Juva | 140 | 34 | 1 | 50 | 42 | 38 | 6 |
| Ii | 105 | 34 | 1 | 52 | 33 | 32 | 19 |
| Kokkola | 105 | 44 | 0 | 37 | 46 | 46 | 27 |
| Kauhajoki | 105 | 37 | 1 | 36 | 47 | 47 | 15 |
| Puolanka | 105 | 14 | 0 | 70 | 13 | 13 | 7 |
| Lieto | 175 | 53 | 5 | 33 | 49 | 41 | 0 |
| Kouvola | 140 | 35 | 1 | 41 | 39 | 35 | 3 |
| Pihtipudas | 105 | 40 | 0 | 35 | 45 | 43 | 20 |
| Jämsä | 140 | 26 | 0 | 52 | 27 | 27 | 3 |
| Koskenkylä -Kotka | 140 | 26 | 3 | 31 | 41 | 31 | 0 |
| Pieksämäki | 105 | 26 | 0 | 46 | 25 | 25 | 6 |
| Rovaniemi 17-22 | 70 | 25 | 0 | 42 | 29 | 29 | 11 |
| Raasepori | 175 | 31 | 3 | 40 | 29 | 24 | 0 |
| Virrat | 105 | 37 | 1 | 29 | 39 | 34 | 7 |
| Alavus | 93 | 51 | 1 | 23 | 45 | 42 | 9 |
| Siikalatva | 74 | 44 | 1 | 15 | 52 | 47 | 26 |
| Savonlinna | 94 | 30 | 3 | 25 | 39 | 37 | 10 |
| Hamina-Vaalimaa | 105 | 16 | 1 | 36 | 27 | 26 | 6 |
| Pello | 63 | 18 | 0 | 42 | 21 | 21 | 14 |
| Karstula | 70 | 27 | 0 | 23 | 38 | 36 | 23 |
| Imatra | 105 | 26 | 0 | 33 | 26 | 25 | 3 |
| Kuhmo | 70 | 11 | 0 | 46 | 12 | 12 | 6 |
| Nilsiä | 70 | 28 | 0 | 25 | 32 | 30 | 20 |
| Mäntsälä | 105 | 24 | 0 | 27 | 28 | 24 | 2 |
| Ilomantsi | 70 | 11 | 0 | 44 | 10 | 10 | 1 |
| Keuruu | 70 | 23 | 1 | 26 | 27 | 24 | 14 |
| Iisalmi | 70 | 35 | 0 | 16 | 31 | 30 | 14 |
| Kangasala | 70 | 22 | 4 | 11 | 35 | 29 | 7 |
| Espoo | 105 | 22 | 1 | 20 | 25 | 20 | 3 |
| Heinola | 70 | 17 | 2 | 22 | 20 | 19 | 1 |
| Parkano | 70 | 22 | 0 | 19 | 22 | 21 | 9 |
| Harjavalta | 70 | 13 | 0 | 27 | 13 | 13 | 0 |
| Merikarvia | 70 | 19 | 0 | 13 | 24 | 21 | 4 |
| Hämeenlinna | 70 | 14 | 2 | 19 | 15 | 12 | 1 |
| Huittinen | 70 | 15 | 0 | 19 | 14 | 14 | 0 |
| Pielavesi | 35 | 10 | 0 | 18 | 13 | 13 | 7 |
| Ranua | 35 | 11 | 0 | 20 | 10 | 9 | 4 |
| Kankaanpää | 35 | 9 | 1 | 14 | 11 | 10 | 3 |
| Vantaa | 58 | 11 | 3 | 11 | 13 | 9 | 0 |
| Kiuruvesi | 35 | 11 | 0 | 15 | 9 | 8 | 2 |
| Sastamala | 35 | 8 | 0 | 13 | 9 | 9 | 0 |
| Loimaa | 35 | 7 | 0 | 12 | 7 | 7 | 1 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
