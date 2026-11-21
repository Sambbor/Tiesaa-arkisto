# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v19) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 39 (2026-10-12 – 2026-11-19), laskentoja 420722. Päivitetty 2026-11-21T12:58:12Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 10944.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 6948 | 271 | 28479 | 217520 | 96 % | 80 % |
| +6 h | 6482 | 835 | 35458 | 210558 | 89 % | 85 % |
| +12 h | 6613 | 774 | 38871 | 205611 | 90 % | 85 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 1848 | 253 | 5157 | 88 % | 74 % |
| Lappi | 2463 | 94 | 3558 | 96 % | 59 % |
| Keski-Suomi | 451 | 103 | 3670 | 81 % | 89 % |
| Etelä-Pohjanmaa | 323 | 85 | 2885 | 79 % | 90 % |
| Pohjois-Savo | 421 | 105 | 2649 | 80 % | 86 % |
| Uusimaa | 9 | 5 | 2770 | 64 % | 100 % |
| Pirkanmaa | 96 | 10 | 2180 | 91 % | 96 % |
| Pohjanmaa | 154 | 42 | 1929 | 79 % | 93 % |
| Varsinais-Suomi | 5 | 7 | 1792 | 42 % | 100 % |
| Pohjois-Karjala | 116 | 42 | 1439 | 73 % | 93 % |
| Kymenlaakso | 51 | 12 | 1506 | 81 % | 97 % |
| Keski-Pohjanmaa | 264 | 21 | 1044 | 93 % | 80 % |
| Etelä-Savo | 104 | 24 | 967 | 81 % | 90 % |
| Etelä-Karjala | 73 | 23 | 906 | 76 % | 93 % |
| Satakunta | 13 | 0 | 986 | 100 % | 99 % |
| Päijät-Häme | 5 | 4 | 912 | 56 % | 99 % |
| Kanta-Häme | 0 | 0 | 650 | – % | 100 % |
| Kainuu | 86 | 5 | 458 | 95 % | 84 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 2001 | 18263 | 10 % |
| tiesääennuste (Digitraffic) | 1335 | 8796 | 13 % |
| märkä tie jäätyy | 1183 | 3583 | 25 % |
| lumisade | 1820 | 2802 | 39 % |
| lumi / sohjo | 87 | 1905 | 4 % |
| jäätävä sade | 56 | 109 | 34 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 476 |
| tie −1…+1 °C | 205 |
| tie alle −4 °C | 154 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 19878 | 1183 | 51782 | 344680 | 94 % | 72 % |
| +6 h | 17949 | 3328 | 63688 | 332450 | 84 % | 78 % |
| +12 h | 18489 | 3048 | 69842 | 323676 | 86 % | 79 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 8069 | 859 | 9204 | 90 % |
| Pohjois-Pohjanmaa | 3655 | 745 | 8719 | 83 % |
| Finavia lentokentät | 841 | 522 | 5478 | 62 % |
| Etelä-Pohjanmaa | 528 | 106 | 4644 | 83 % |
| Kainuu | 1362 | 191 | 3519 | 88 % |
| Pohjois-Savo | 848 | 153 | 3774 | 85 % |
| Keski-Suomi | 600 | 101 | 3990 | 86 % |
| Pohjois-Karjala | 592 | 135 | 3953 | 81 % |
| Uusimaa | 36 | 27 | 3486 | 57 % |
| Varsinais-Suomi | 115 | 40 | 2951 | 74 % |
| Pirkanmaa | 172 | 31 | 2841 | 85 % |
| Pohjanmaa | 229 | 48 | 2307 | 83 % |
| Keski-Pohjanmaa | 487 | 40 | 1758 | 92 % |
| Etelä-Savo | 161 | 38 | 1874 | 81 % |
| Kymenlaakso | 84 | 28 | 1558 | 75 % |
| Etelä-Karjala | 120 | 245 | 1011 | 33 % |
| Satakunta | 25 | 13 | 985 | 66 % |
| Päijät-Häme | 17 | 3 | 994 | 85 % |
| Kanta-Häme | 8 | 3 | 642 | 73 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 7340 | 33300 |
| tiesääennuste (Digitraffic) | 4037 | 15470 |
| lumisade | 4345 | 5618 |
| märkä tie jäätyy | 1867 | 6167 |
| lumi / sohjo | 187 | 2875 |
| jäätävä sade | 173 | 258 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 2098 |
| varoitus häly | 566 |
| kitka < 0,45 | 340 |
| jäätä tiellä | 141 |
| keli lumi | 111 |
| keli kuura | 72 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 20234 | 2539 (13 %) | 40884 | 0 (0 %) | 3766 (9 %) | 7592 (19 %) |
| 0,5–2 | 5532 | 758 (14 %) | 10854 | 0 (0 %) | 2667 (25 %) | 2185 (20 %) |
| 2–4 | 3853 | 542 (14 %) | 8327 | 0 (0 %) | 1893 (23 %) | 1905 (23 %) |
| 4–8 | 4237 | 621 (15 %) | 9568 | 2 (0 %) | 2039 (21 %) | 2328 (24 %) |
| yli 8 | 6047 | 1309 (22 %) | 16124 | 482 (3 %) | 2385 (15 %) | 4768 (30 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 8856 | 20 % (18 % / 13965) | 14765 | 22 % (24 % / 24649) |
| −4…−2 | 2254 | 21 % (16 % / 3806) | 4252 | 32 % (33 % / 6943) |
| −6…−4 | 327 | 45 % (29 % / 554) | 1060 | 69 % (58 % / 1790) |
| −8…−6 | 33 | 73 % (68 % / 44) | 381 | 71 % (63 % / 512) |
| alle −8 | 0 | – (73 % / 22) | 549 | 84 % (78 % / 667) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 33 päivältä, 15333 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 4011 | 1091 |
| Vain urakka suolasi | 219 | 4 |
| Vain ennuste hälytti | 5542 | 1426 |
| Kumpikaan ei | 5561 | 23 |

Suolauskertoja 4592: ennuste hälytti 0–12 h ennen 4053 kertaa (88 %), keskimäärin 7,7 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 1108 kertaa (24 %).
Liukkaista asemavuorokausista 2544: suolattu ennen ensimmäistä liukasta mittausta 571, vasta sen jälkeen (6 h sisällä) 357.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2810 | 544 | 90 | 1002 | 655 | 513 | 86 |
| Oulu | 462 | 237 | 21 | 121 | 238 | 188 | 88 |
| Kuopio | 363 | 154 | 0 | 91 | 193 | 182 | 53 |
| Kajaani | 264 | 146 | 0 | 59 | 185 | 177 | 53 |
| Kemi | 258 | 94 | 1 | 128 | 115 | 110 | 50 |
| Raahe/Ylivieska | 288 | 121 | 6 | 87 | 153 | 140 | 67 |
| Kittilä | 259 | 0 | 0 | 238 | 0 | 0 | 0 |
| Lapua | 297 | 122 | 12 | 85 | 130 | 108 | 40 |
| Salo | 363 | 84 | 0 | 109 | 86 | 71 | 7 |
| Ivalo | 198 | 1 | 0 | 186 | 1 | 1 | 0 |
| Seinäjoki | 248 | 95 | 0 | 80 | 105 | 104 | 25 |
| Tampere | 297 | 64 | 5 | 91 | 93 | 84 | 11 |
| Joensuu | 231 | 66 | 6 | 92 | 86 | 69 | 22 |
| Pudasjärvi-Taivalkoski | 165 | 69 | 1 | 81 | 89 | 85 | 31 |
| Kotka | 330 | 40 | 4 | 117 | 52 | 45 | 7 |
| Nummi | 297 | 70 | 5 | 79 | 72 | 65 | 5 |
| Kuusamo | 165 | 38 | 0 | 107 | 43 | 43 | 37 |
| Kristiinankaupunki | 231 | 80 | 2 | 72 | 77 | 68 | 9 |
| Espoo 19-24 | 443 | 64 | 6 | 81 | 65 | 54 | 0 |
| Paimio | 297 | 56 | 2 | 80 | 61 | 53 | 1 |
| Orivesi | 189 | 67 | 0 | 48 | 86 | 80 | 20 |
| Kemijärvi-Posio | 143 | 15 | 0 | 116 | 16 | 16 | 7 |
| Lappeenranta | 198 | 50 | 1 | 61 | 69 | 65 | 23 |
| Veteli | 165 | 54 | 0 | 66 | 64 | 61 | 31 |
| Sodankylä | 132 | 0 | 0 | 125 | 0 | 0 | 0 |
| Nurmes | 165 | 51 | 0 | 81 | 43 | 41 | 15 |
| Hyvinkää | 231 | 45 | 0 | 72 | 51 | 45 | 4 |
| Lahti | 198 | 58 | 1 | 59 | 61 | 53 | 6 |
| Pori | 198 | 46 | 1 | 59 | 58 | 47 | 12 |
| Mikkeli | 187 | 51 | 0 | 62 | 55 | 54 | 13 |
| Äänekoski | 165 | 50 | 0 | 61 | 55 | 51 | 24 |
| Vaasa | 132 | 48 | 4 | 38 | 74 | 61 | 10 |
| Rovaniemi | 99 | 40 | 1 | 46 | 65 | 59 | 20 |
| Suonenjoki | 132 | 42 | 1 | 56 | 53 | 51 | 18 |
| Kitee | 154 | 58 | 6 | 43 | 59 | 44 | 9 |
| E18 Muurla-Lohja | 198 | 54 | 0 | 51 | 50 | 42 | 0 |
| Viinijärvi | 132 | 36 | 0 | 60 | 37 | 34 | 15 |
| Raisio | 198 | 55 | 6 | 43 | 52 | 39 | 3 |
| Juva | 132 | 31 | 1 | 54 | 38 | 34 | 6 |
| Pyhäjärvi | 99 | 48 | 0 | 26 | 66 | 62 | 19 |
| Suomussalmi | 102 | 21 | 0 | 71 | 20 | 18 | 7 |
| Porvoo | 196 | 28 | 1 | 56 | 31 | 26 | 2 |
| Jämsä | 132 | 26 | 0 | 56 | 27 | 27 | 3 |
| Jyväskylä | 231 | 51 | 13 | 31 | 51 | 37 | 0 |
| Ii | 99 | 32 | 1 | 48 | 31 | 30 | 17 |
| Kauhajoki | 99 | 35 | 0 | 35 | 43 | 43 | 12 |
| Kouvola | 132 | 28 | 0 | 45 | 32 | 29 | 3 |
| Kokkola | 99 | 38 | 0 | 37 | 40 | 40 | 23 |
| Puolanka | 99 | 14 | 0 | 64 | 13 | 13 | 7 |
| Lieto | 165 | 43 | 5 | 36 | 39 | 31 | 0 |
| Pihtipudas | 99 | 34 | 0 | 36 | 36 | 34 | 12 |
| Pieksämäki | 99 | 23 | 0 | 47 | 22 | 22 | 6 |
| Virrat | 99 | 33 | 1 | 33 | 35 | 32 | 7 |
| Rovaniemi 17-22 | 66 | 25 | 0 | 38 | 29 | 29 | 11 |
| Savonlinna | 88 | 30 | 0 | 28 | 36 | 34 | 10 |
| Koskenkylä -Kotka | 132 | 19 | 2 | 32 | 30 | 23 | 0 |
| Imatra | 99 | 23 | 0 | 36 | 25 | 24 | 3 |
| Alavus | 85 | 44 | 0 | 23 | 38 | 36 | 5 |
| Raasepori | 165 | 26 | 3 | 35 | 24 | 19 | 0 |
| Siikalatva | 68 | 40 | 1 | 13 | 45 | 40 | 19 |
| Pello | 59 | 14 | 0 | 42 | 16 | 16 | 11 |
| Karstula | 66 | 23 | 0 | 24 | 31 | 30 | 16 |
| Kuhmo | 66 | 11 | 0 | 42 | 12 | 12 | 6 |
| Hamina-Vaalimaa | 99 | 13 | 1 | 33 | 20 | 19 | 2 |
| Nilsiä | 66 | 25 | 0 | 25 | 27 | 26 | 15 |
| Ilomantsi | 66 | 11 | 0 | 41 | 10 | 10 | 1 |
| Keuruu | 66 | 21 | 1 | 25 | 25 | 24 | 13 |
| Mäntsälä | 99 | 18 | 0 | 28 | 20 | 17 | 2 |
| Kangasala | 66 | 20 | 2 | 12 | 32 | 28 | 7 |
| Iisalmi | 66 | 33 | 0 | 14 | 29 | 28 | 12 |
| Parkano | 66 | 20 | 0 | 21 | 18 | 17 | 7 |
| Heinola | 66 | 16 | 0 | 23 | 16 | 16 | 1 |
| Espoo | 99 | 17 | 1 | 20 | 18 | 14 | 0 |
| Harjavalta | 66 | 12 | 0 | 25 | 12 | 12 | 0 |
| Merikarvia | 66 | 17 | 0 | 14 | 22 | 19 | 4 |
| Hämeenlinna | 66 | 11 | 1 | 23 | 11 | 10 | 1 |
| Huittinen | 66 | 13 | 0 | 19 | 12 | 12 | 0 |
| Pielavesi | 33 | 8 | 0 | 18 | 12 | 12 | 6 |
| Ranua | 33 | 11 | 0 | 18 | 10 | 9 | 4 |
| Kankaanpää | 33 | 9 | 0 | 13 | 10 | 10 | 3 |
| Kiuruvesi | 33 | 11 | 0 | 13 | 9 | 8 | 2 |
| Vantaa | 54 | 8 | 3 | 10 | 10 | 6 | 0 |
| Loimaa | 33 | 5 | 0 | 14 | 5 | 5 | 1 |
| Sastamala | 33 | 7 | 0 | 12 | 7 | 7 | 0 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
