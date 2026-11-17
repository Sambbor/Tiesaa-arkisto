# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v18) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 35 (2026-10-12 – 2026-11-15), laskentoja 375457. Päivitetty 2026-11-17T06:23:54Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 9815.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 5459 | 239 | 24906 | 195568 | 96 % | 82 % |
| +6 h | 4962 | 773 | 31267 | 189292 | 87 % | 86 % |
| +12 h | 5059 | 717 | 33632 | 185428 | 88 % | 87 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 1549 | 232 | 3961 | 87 % | 72 % |
| Lappi | 1556 | 69 | 3212 | 96 % | 67 % |
| Keski-Suomi | 377 | 100 | 3211 | 79 % | 89 % |
| Uusimaa | 9 | 5 | 2775 | 64 % | 100 % |
| Etelä-Pohjanmaa | 268 | 85 | 2388 | 76 % | 90 % |
| Pohjois-Savo | 376 | 99 | 2240 | 79 % | 86 % |
| Pirkanmaa | 77 | 10 | 1987 | 89 % | 96 % |
| Varsinais-Suomi | 5 | 7 | 1747 | 42 % | 100 % |
| Pohjanmaa | 108 | 42 | 1568 | 72 % | 94 % |
| Kymenlaakso | 51 | 12 | 1514 | 81 % | 97 % |
| Pohjois-Karjala | 102 | 40 | 1215 | 72 % | 92 % |
| Keski-Pohjanmaa | 217 | 20 | 888 | 92 % | 80 % |
| Etelä-Savo | 95 | 20 | 900 | 83 % | 90 % |
| Etelä-Karjala | 73 | 23 | 886 | 76 % | 92 % |
| Satakunta | 13 | 0 | 913 | 100 % | 99 % |
| Päijät-Häme | 5 | 4 | 878 | 56 % | 99 % |
| Kanta-Häme | 0 | 0 | 650 | – % | 100 % |
| Kainuu | 81 | 5 | 334 | 94 % | 80 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 1488 | 17515 | 8 % |
| tiesääennuste (Digitraffic) | 1088 | 7381 | 13 % |
| märkä tie jäätyy | 917 | 2603 | 26 % |
| lumisade | 1328 | 1922 | 41 % |
| lumi / sohjo | 40 | 1090 | 4 % |
| jäätävä sade | 101 | 756 | 12 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 443 |
| tie −1…+1 °C | 179 |
| tie alle −4 °C | 151 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 15297 | 1112 | 44243 | 311619 | 93 % | 74 % |
| +6 h | 13418 | 3024 | 55155 | 300572 | 82 % | 80 % |
| +12 h | 13740 | 2813 | 59609 | 293653 | 83 % | 81 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 5614 | 766 | 8149 | 88 % |
| Pohjois-Pohjanmaa | 2984 | 686 | 6776 | 81 % |
| Finavia lentokentät | 302 | 414 | 4587 | 42 % |
| Etelä-Pohjanmaa | 462 | 104 | 3860 | 82 % |
| Keski-Suomi | 509 | 100 | 3494 | 84 % |
| Pohjois-Savo | 760 | 149 | 3163 | 84 % |
| Kainuu | 1009 | 176 | 2771 | 85 % |
| Pohjois-Karjala | 497 | 120 | 3207 | 81 % |
| Uusimaa | 36 | 27 | 3489 | 57 % |
| Varsinais-Suomi | 115 | 40 | 2902 | 74 % |
| Pirkanmaa | 143 | 29 | 2581 | 83 % |
| Pohjanmaa | 167 | 48 | 1856 | 78 % |
| Keski-Pohjanmaa | 411 | 38 | 1507 | 92 % |
| Etelä-Savo | 155 | 36 | 1743 | 81 % |
| Kymenlaakso | 84 | 28 | 1566 | 75 % |
| Etelä-Karjala | 120 | 244 | 988 | 33 % |
| Päijät-Häme | 17 | 3 | 962 | 85 % |
| Satakunta | 25 | 13 | 912 | 66 % |
| Kanta-Häme | 8 | 3 | 642 | 73 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 5642 | 31199 |
| tiesääennuste (Digitraffic) | 3148 | 12821 |
| lumisade | 2885 | 3805 |
| märkä tie jäätyy | 1406 | 4305 |
| jäätävä sade | 248 | 1437 |
| lumi / sohjo | 89 | 1588 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 1918 |
| varoitus häly | 549 |
| kitka < 0,45 | 309 |
| jäätä tiellä | 115 |
| keli kuura | 71 |
| keli lumi | 62 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 18705 | 2082 (11 %) | 37315 | 0 (0 %) | 3710 (10 %) | 6233 (17 %) |
| 0,5–2 | 4944 | 553 (11 %) | 9452 | 0 (0 %) | 2628 (28 %) | 1657 (18 %) |
| 2–4 | 3544 | 433 (12 %) | 7300 | 0 (0 %) | 1839 (25 %) | 1503 (21 %) |
| 4–8 | 3868 | 452 (12 %) | 8230 | 2 (0 %) | 1908 (23 %) | 1727 (21 %) |
| yli 8 | 5336 | 940 (18 %) | 13525 | 431 (3 %) | 2109 (16 %) | 3358 (25 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 7975 | 19 % (17 % / 12253) | 12542 | 19 % (22 % / 20095) |
| −4…−2 | 2173 | 20 % (14 % / 3653) | 3956 | 28 % (30 % / 6509) |
| −6…−4 | 312 | 42 % (26 % / 528) | 878 | 63 % (52 % / 1474) |
| −8…−6 | 28 | 68 % (64 % / 39) | 318 | 66 % (59 % / 429) |
| alle −8 | 0 | – (73 % / 22) | 429 | 80 % (73 % / 537) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 29 päivältä, 13444 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 3525 | 862 |
| Vain urakka suolasi | 207 | 2 |
| Vain ennuste hälytti | 4822 | 1167 |
| Kumpikaan ei | 4890 | 23 |

Suolauskertoja 4059: ennuste hälytti 0–12 h ennen 3564 kertaa (88 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 888 kertaa (22 %).
Liukkaista asemavuorokausista 2054: suolattu ennen ensimmäistä liukasta mittausta 490, vasta sen jälkeen (6 h sisällä) 245.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2466 | 488 | 87 | 842 | 595 | 460 | 56 |
| Oulu | 406 | 186 | 21 | 116 | 182 | 138 | 62 |
| Kuopio | 319 | 113 | 0 | 91 | 152 | 141 | 49 |
| Kittilä | 227 | 0 | 0 | 206 | 0 | 0 | 0 |
| Kajaani | 232 | 114 | 0 | 59 | 143 | 136 | 41 |
| Raahe/Ylivieska | 252 | 85 | 6 | 91 | 110 | 99 | 50 |
| Kemi | 226 | 68 | 1 | 123 | 76 | 73 | 27 |
| Salo | 319 | 84 | 0 | 104 | 86 | 71 | 7 |
| Lapua | 261 | 103 | 8 | 73 | 110 | 94 | 38 |
| Tampere | 261 | 58 | 5 | 82 | 87 | 78 | 9 |
| Kotka | 290 | 40 | 4 | 114 | 52 | 45 | 7 |
| Ivalo | 174 | 1 | 0 | 162 | 1 | 1 | 0 |
| Seinäjoki | 216 | 86 | 0 | 61 | 96 | 95 | 21 |
| Joensuu | 203 | 52 | 6 | 80 | 75 | 58 | 18 |
| Espoo 19-24 | 387 | 65 | 5 | 79 | 65 | 54 | 0 |
| Nummi | 261 | 69 | 5 | 73 | 71 | 65 | 5 |
| Pudasjärvi-Taivalkoski | 145 | 53 | 1 | 77 | 62 | 58 | 19 |
| Paimio | 261 | 56 | 2 | 73 | 61 | 53 | 1 |
| Kuusamo | 145 | 33 | 0 | 92 | 37 | 37 | 32 |
| Lappeenranta | 174 | 45 | 1 | 56 | 66 | 63 | 23 |
| Kristiinankaupunki | 203 | 67 | 2 | 57 | 65 | 57 | 7 |
| Hyvinkää | 203 | 45 | 0 | 67 | 51 | 45 | 4 |
| Orivesi | 165 | 62 | 0 | 36 | 79 | 73 | 15 |
| Veteli | 145 | 47 | 0 | 53 | 61 | 59 | 28 |
| Mikkeli | 163 | 50 | 0 | 57 | 54 | 53 | 13 |
| Kemijärvi-Posio | 123 | 13 | 0 | 98 | 13 | 13 | 4 |
| Sodankylä | 116 | 0 | 0 | 109 | 0 | 0 | 0 |
| Lahti | 174 | 58 | 1 | 44 | 61 | 53 | 6 |
| Nurmes | 145 | 46 | 0 | 66 | 38 | 36 | 14 |
| Pori | 174 | 46 | 1 | 45 | 58 | 47 | 12 |
| Äänekoski | 145 | 46 | 0 | 45 | 55 | 51 | 24 |
| Vaasa | 116 | 44 | 4 | 26 | 70 | 57 | 10 |
| E18 Muurla-Lohja | 174 | 54 | 0 | 46 | 50 | 43 | 0 |
| Rovaniemi | 87 | 34 | 1 | 40 | 51 | 45 | 11 |
| Suonenjoki | 116 | 36 | 1 | 46 | 44 | 43 | 14 |
| Porvoo | 172 | 28 | 1 | 54 | 31 | 26 | 2 |
| Raisio | 174 | 55 | 6 | 33 | 52 | 39 | 3 |
| Juva | 116 | 31 | 1 | 45 | 38 | 35 | 6 |
| Kitee | 134 | 51 | 2 | 34 | 49 | 38 | 7 |
| Viinijärvi | 116 | 29 | 0 | 51 | 31 | 28 | 15 |
| Jyväskylä | 203 | 51 | 13 | 29 | 51 | 37 | 0 |
| Pyhäjärvi | 87 | 41 | 0 | 21 | 58 | 55 | 16 |
| Suomussalmi | 87 | 16 | 0 | 61 | 15 | 14 | 6 |
| Jämsä | 116 | 25 | 0 | 47 | 26 | 26 | 2 |
| Kouvola | 116 | 28 | 0 | 39 | 32 | 29 | 3 |
| Lieto | 145 | 43 | 5 | 29 | 39 | 31 | 0 |
| Kokkola | 87 | 27 | 0 | 36 | 30 | 30 | 17 |
| Puolanka | 87 | 9 | 0 | 57 | 9 | 9 | 5 |
| Kauhajoki | 87 | 32 | 0 | 26 | 39 | 39 | 11 |
| Ii | 87 | 24 | 1 | 44 | 21 | 20 | 15 |
| Pihtipudas | 87 | 31 | 0 | 27 | 36 | 34 | 12 |
| Koskenkylä -Kotka | 116 | 19 | 2 | 31 | 30 | 23 | 0 |
| Pieksämäki | 87 | 23 | 0 | 37 | 22 | 22 | 6 |
| Rovaniemi 17-22 | 58 | 21 | 0 | 34 | 24 | 24 | 7 |
| Raasepori | 145 | 26 | 3 | 33 | 24 | 19 | 0 |
| Imatra | 87 | 23 | 0 | 31 | 25 | 24 | 3 |
| Virrat | 87 | 28 | 1 | 26 | 30 | 28 | 5 |
| Savonlinna | 76 | 26 | 0 | 21 | 34 | 33 | 10 |
| Hamina-Vaalimaa | 87 | 13 | 1 | 33 | 20 | 19 | 2 |
| Alavus | 69 | 40 | 0 | 15 | 38 | 36 | 5 |
| Pello | 51 | 8 | 0 | 40 | 9 | 9 | 4 |
| Karstula | 58 | 21 | 0 | 18 | 30 | 29 | 15 |
| Mäntsälä | 87 | 18 | 0 | 27 | 20 | 17 | 2 |
| Siikalatva | 58 | 31 | 1 | 12 | 34 | 32 | 14 |
| Kuhmo | 58 | 9 | 0 | 36 | 10 | 10 | 4 |
| Nilsiä | 58 | 21 | 0 | 21 | 24 | 23 | 13 |
| Ilomantsi | 58 | 9 | 0 | 35 | 8 | 8 | 0 |
| Keuruu | 58 | 19 | 1 | 19 | 23 | 22 | 11 |
| Kangasala | 58 | 19 | 2 | 10 | 31 | 27 | 6 |
| Espoo | 87 | 16 | 1 | 20 | 18 | 14 | 0 |
| Heinola | 58 | 16 | 0 | 20 | 16 | 16 | 1 |
| Iisalmi | 58 | 27 | 0 | 12 | 24 | 24 | 10 |
| Harjavalta | 58 | 12 | 0 | 21 | 12 | 12 | 0 |
| Parkano | 58 | 18 | 0 | 17 | 16 | 15 | 5 |
| Merikarvia | 58 | 17 | 0 | 11 | 22 | 19 | 4 |
| Hämeenlinna | 58 | 11 | 1 | 19 | 11 | 10 | 1 |
| Huittinen | 58 | 13 | 0 | 16 | 12 | 12 | 0 |
| Pielavesi | 29 | 7 | 0 | 15 | 11 | 11 | 5 |
| Ranua | 29 | 8 | 0 | 17 | 7 | 6 | 2 |
| Vantaa | 46 | 8 | 3 | 9 | 10 | 6 | 0 |
| Kankaanpää | 29 | 9 | 0 | 9 | 10 | 10 | 3 |
| Kiuruvesi | 29 | 9 | 0 | 11 | 8 | 8 | 2 |
| Loimaa | 29 | 5 | 0 | 13 | 5 | 5 | 1 |
| Sastamala | 29 | 7 | 0 | 11 | 7 | 7 | 0 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
