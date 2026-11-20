# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v18) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 38 (2026-10-12 – 2026-11-18), laskentoja 409344. Päivitetty 2026-11-20T13:32:48Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 10656.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 6598 | 258 | 27315 | 212147 | 96 % | 81 % |
| +6 h | 6095 | 795 | 33835 | 205708 | 88 % | 85 % |
| +12 h | 6191 | 745 | 36705 | 201328 | 89 % | 86 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 1794 | 236 | 4884 | 88 % | 73 % |
| Lappi | 2312 | 81 | 3487 | 97 % | 60 % |
| Keski-Suomi | 398 | 101 | 3442 | 80 % | 90 % |
| Etelä-Pohjanmaa | 282 | 85 | 2721 | 77 % | 91 % |
| Pohjois-Savo | 402 | 102 | 2436 | 80 % | 86 % |
| Uusimaa | 9 | 5 | 2775 | 64 % | 100 % |
| Pirkanmaa | 77 | 10 | 2011 | 89 % | 96 % |
| Pohjanmaa | 132 | 42 | 1806 | 76 % | 93 % |
| Varsinais-Suomi | 5 | 7 | 1754 | 42 % | 100 % |
| Kymenlaakso | 51 | 12 | 1514 | 81 % | 97 % |
| Pohjois-Karjala | 118 | 40 | 1323 | 75 % | 92 % |
| Keski-Pohjanmaa | 243 | 20 | 1012 | 92 % | 81 % |
| Etelä-Savo | 95 | 22 | 904 | 81 % | 90 % |
| Etelä-Karjala | 73 | 23 | 890 | 76 % | 92 % |
| Satakunta | 13 | 0 | 922 | 100 % | 99 % |
| Päijät-Häme | 5 | 4 | 879 | 56 % | 99 % |
| Kanta-Häme | 0 | 0 | 651 | – % | 100 % |
| Kainuu | 86 | 5 | 424 | 95 % | 83 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 1841 | 17979 | 9 % |
| tiesääennuste (Digitraffic) | 1266 | 7761 | 14 % |
| lumisade | 1688 | 2447 | 41 % |
| märkä tie jäätyy | 1083 | 2796 | 28 % |
| lumi / sohjo | 72 | 1553 | 4 % |
| jäätävä sade | 145 | 1299 | 10 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 453 |
| tie −1…+1 °C | 188 |
| tie alle −4 °C | 154 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 18809 | 1148 | 49626 | 336566 | 94 % | 73 % |
| +6 h | 16873 | 3181 | 60851 | 325136 | 84 % | 78 % |
| +12 h | 17267 | 2939 | 66153 | 317322 | 85 % | 79 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 7566 | 836 | 9009 | 90 % |
| Pohjois-Pohjanmaa | 3536 | 703 | 8253 | 83 % |
| Finavia lentokentät | 744 | 473 | 5205 | 61 % |
| Etelä-Pohjanmaa | 488 | 104 | 4369 | 82 % |
| Kainuu | 1269 | 176 | 3355 | 88 % |
| Pohjois-Savo | 808 | 152 | 3518 | 84 % |
| Keski-Suomi | 537 | 101 | 3743 | 84 % |
| Pohjois-Karjala | 568 | 124 | 3666 | 82 % |
| Uusimaa | 36 | 27 | 3489 | 57 % |
| Varsinais-Suomi | 115 | 40 | 2910 | 74 % |
| Pirkanmaa | 144 | 29 | 2632 | 83 % |
| Pohjanmaa | 195 | 48 | 2151 | 80 % |
| Keski-Pohjanmaa | 455 | 38 | 1702 | 92 % |
| Etelä-Savo | 158 | 38 | 1764 | 81 % |
| Kymenlaakso | 84 | 28 | 1566 | 75 % |
| Etelä-Karjala | 120 | 245 | 992 | 33 % |
| Päijät-Häme | 17 | 3 | 963 | 85 % |
| Satakunta | 25 | 13 | 921 | 66 % |
| Kanta-Häme | 8 | 3 | 643 | 73 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 6762 | 32466 |
| tiesääennuste (Digitraffic) | 3745 | 13667 |
| lumisade | 4135 | 5026 |
| märkä tie jäätyy | 1685 | 4817 |
| jäätävä sade | 385 | 2453 |
| lumi / sohjo | 161 | 2422 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 2013 |
| varoitus häly | 557 |
| kitka < 0,45 | 319 |
| jäätä tiellä | 126 |
| keli lumi | 94 |
| keli kuura | 72 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 19570 | 2486 (13 %) | 39502 | 0 (0 %) | 3754 (10 %) | 7375 (19 %) |
| 0,5–2 | 5350 | 707 (13 %) | 10481 | 0 (0 %) | 2664 (25 %) | 2068 (20 %) |
| 2–4 | 3798 | 516 (14 %) | 8127 | 0 (0 %) | 1882 (23 %) | 1843 (23 %) |
| 4–8 | 4178 | 598 (14 %) | 9331 | 2 (0 %) | 2011 (22 %) | 2231 (24 %) |
| yli 8 | 5841 | 1164 (20 %) | 15347 | 475 (3 %) | 2307 (15 %) | 4265 (28 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 8635 | 20 % (18 % / 13439) | 13907 | 21 % (24 % / 23060) |
| −4…−2 | 2251 | 21 % (16 % / 3776) | 4227 | 31 % (33 % / 6910) |
| −6…−4 | 327 | 45 % (29 % / 554) | 1015 | 67 % (57 % / 1745) |
| −8…−6 | 33 | 73 % (68 % / 44) | 375 | 71 % (63 % / 506) |
| alle −8 | 0 | – (73 % / 22) | 549 | 84 % (78 % / 667) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 32 päivältä, 14858 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 3841 | 1022 |
| Vain urakka suolasi | 217 | 4 |
| Vain ennuste hälytti | 5333 | 1360 |
| Kumpikaan ei | 5467 | 23 |

Suolauskertoja 4418: ennuste hälytti 0–12 h ennen 3895 kertaa (88 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 1059 kertaa (24 %).
Liukkaista asemavuorokausista 2409: suolattu ennen ensimmäistä liukasta mittausta 556, vasta sen jälkeen (6 h sisällä) 318.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2722 | 528 | 90 | 949 | 636 | 496 | 76 |
| Oulu | 448 | 224 | 21 | 120 | 222 | 175 | 84 |
| Kuopio | 352 | 143 | 0 | 94 | 179 | 168 | 53 |
| Kajaani | 256 | 138 | 0 | 59 | 176 | 168 | 53 |
| Raahe/Ylivieska | 279 | 112 | 6 | 91 | 143 | 130 | 67 |
| Kemi | 250 | 86 | 1 | 129 | 102 | 99 | 49 |
| Kittilä | 251 | 0 | 0 | 230 | 0 | 0 | 0 |
| Lapua | 288 | 116 | 12 | 82 | 130 | 108 | 40 |
| Salo | 352 | 84 | 0 | 107 | 86 | 71 | 7 |
| Ivalo | 192 | 1 | 0 | 180 | 1 | 1 | 0 |
| Seinäjoki | 240 | 87 | 0 | 80 | 97 | 96 | 21 |
| Tampere | 288 | 58 | 5 | 88 | 87 | 78 | 9 |
| Joensuu | 224 | 62 | 6 | 91 | 82 | 65 | 22 |
| Kotka | 320 | 40 | 4 | 115 | 52 | 45 | 7 |
| Pudasjärvi-Taivalkoski | 160 | 65 | 1 | 80 | 83 | 79 | 31 |
| Nummi | 288 | 69 | 5 | 74 | 71 | 65 | 5 |
| Kristiinankaupunki | 224 | 77 | 2 | 68 | 77 | 68 | 9 |
| Kuusamo | 160 | 36 | 0 | 104 | 41 | 41 | 35 |
| Espoo 19-24 | 429 | 65 | 5 | 79 | 65 | 54 | 0 |
| Paimio | 288 | 56 | 2 | 73 | 61 | 53 | 1 |
| Veteli | 160 | 50 | 0 | 65 | 64 | 61 | 31 |
| Orivesi | 183 | 62 | 0 | 48 | 79 | 73 | 15 |
| Kemijärvi-Posio | 138 | 15 | 0 | 111 | 16 | 16 | 7 |
| Lappeenranta | 192 | 47 | 1 | 58 | 66 | 63 | 23 |
| Sodankylä | 128 | 0 | 0 | 121 | 0 | 0 | 0 |
| Hyvinkää | 224 | 45 | 0 | 68 | 51 | 45 | 4 |
| Nurmes | 160 | 51 | 0 | 76 | 43 | 41 | 15 |
| Äänekoski | 160 | 46 | 0 | 60 | 55 | 51 | 24 |
| Lahti | 192 | 58 | 1 | 53 | 61 | 53 | 6 |
| Mikkeli | 181 | 50 | 0 | 58 | 54 | 53 | 13 |
| Pori | 192 | 46 | 1 | 53 | 58 | 47 | 12 |
| Vaasa | 128 | 47 | 4 | 35 | 73 | 60 | 10 |
| Suonenjoki | 128 | 40 | 1 | 54 | 50 | 49 | 18 |
| Rovaniemi | 96 | 38 | 1 | 45 | 59 | 53 | 17 |
| Kitee | 149 | 59 | 5 | 38 | 59 | 45 | 9 |
| E18 Muurla-Lohja | 192 | 54 | 0 | 46 | 50 | 43 | 0 |
| Viinijärvi | 128 | 33 | 0 | 59 | 34 | 31 | 15 |
| Raisio | 192 | 55 | 6 | 37 | 52 | 39 | 3 |
| Juva | 128 | 31 | 1 | 50 | 38 | 35 | 6 |
| Pyhäjärvi | 96 | 45 | 0 | 26 | 62 | 59 | 19 |
| Suomussalmi | 98 | 20 | 0 | 68 | 19 | 17 | 7 |
| Porvoo | 190 | 28 | 1 | 54 | 31 | 26 | 2 |
| Jyväskylä | 224 | 51 | 13 | 29 | 51 | 37 | 0 |
| Jämsä | 128 | 25 | 0 | 53 | 26 | 26 | 2 |
| Kokkola | 96 | 35 | 0 | 37 | 40 | 40 | 23 |
| Ii | 96 | 29 | 1 | 48 | 27 | 26 | 17 |
| Kouvola | 128 | 28 | 0 | 42 | 32 | 29 | 3 |
| Kauhajoki | 96 | 32 | 0 | 35 | 39 | 39 | 11 |
| Puolanka | 96 | 12 | 0 | 63 | 11 | 11 | 6 |
| Pihtipudas | 96 | 31 | 0 | 36 | 36 | 34 | 12 |
| Lieto | 160 | 43 | 5 | 31 | 39 | 31 | 0 |
| Pieksämäki | 96 | 23 | 0 | 44 | 22 | 22 | 6 |
| Virrat | 96 | 30 | 1 | 33 | 32 | 29 | 5 |
| Rovaniemi 17-22 | 64 | 23 | 0 | 38 | 26 | 26 | 9 |
| Koskenkylä -Kotka | 128 | 19 | 2 | 31 | 30 | 23 | 0 |
| Savonlinna | 85 | 30 | 0 | 25 | 36 | 34 | 10 |
| Alavus | 81 | 40 | 0 | 23 | 38 | 36 | 5 |
| Imatra | 96 | 23 | 0 | 34 | 25 | 24 | 3 |
| Raasepori | 160 | 26 | 3 | 33 | 24 | 19 | 0 |
| Karstula | 64 | 21 | 0 | 24 | 30 | 29 | 15 |
| Siikalatva | 65 | 37 | 1 | 13 | 41 | 36 | 19 |
| Pello | 57 | 12 | 0 | 42 | 12 | 12 | 7 |
| Hamina-Vaalimaa | 96 | 13 | 1 | 33 | 20 | 19 | 2 |
| Kuhmo | 64 | 11 | 0 | 40 | 12 | 12 | 6 |
| Nilsiä | 64 | 23 | 0 | 25 | 26 | 25 | 15 |
| Ilomantsi | 64 | 10 | 0 | 40 | 9 | 9 | 0 |
| Keuruu | 64 | 19 | 1 | 25 | 23 | 22 | 11 |
| Mäntsälä | 96 | 18 | 0 | 27 | 20 | 17 | 2 |
| Kangasala | 64 | 19 | 2 | 11 | 31 | 27 | 6 |
| Iisalmi | 64 | 31 | 0 | 14 | 27 | 27 | 12 |
| Espoo | 96 | 16 | 1 | 20 | 18 | 14 | 0 |
| Parkano | 64 | 18 | 0 | 21 | 16 | 15 | 5 |
| Heinola | 64 | 16 | 0 | 21 | 16 | 16 | 1 |
| Harjavalta | 64 | 12 | 0 | 23 | 12 | 12 | 0 |
| Merikarvia | 64 | 17 | 0 | 12 | 22 | 19 | 4 |
| Hämeenlinna | 64 | 11 | 1 | 21 | 11 | 10 | 1 |
| Huittinen | 64 | 13 | 0 | 17 | 12 | 12 | 0 |
| Pielavesi | 32 | 8 | 0 | 17 | 12 | 12 | 6 |
| Ranua | 32 | 10 | 0 | 18 | 9 | 8 | 4 |
| Kankaanpää | 32 | 9 | 0 | 12 | 10 | 10 | 3 |
| Kiuruvesi | 32 | 10 | 0 | 13 | 8 | 8 | 2 |
| Vantaa | 52 | 8 | 3 | 9 | 10 | 6 | 0 |
| Loimaa | 32 | 5 | 0 | 13 | 5 | 5 | 1 |
| Sastamala | 32 | 7 | 0 | 11 | 7 | 7 | 0 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
