# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v18) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 36 (2026-10-12 – 2026-11-16), laskentoja 386732. Päivitetty 2026-11-18T06:11:24Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 10094.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 5700 | 249 | 25321 | 201591 | 96 % | 82 % |
| +6 h | 5239 | 775 | 31952 | 195010 | 87 % | 86 % |
| +12 h | 5382 | 729 | 34663 | 190734 | 88 % | 87 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 1576 | 234 | 4224 | 87 % | 73 % |
| Lappi | 1785 | 69 | 3322 | 96 % | 65 % |
| Keski-Suomi | 388 | 100 | 3270 | 80 % | 89 % |
| Uusimaa | 9 | 5 | 2775 | 64 % | 100 % |
| Etelä-Pohjanmaa | 268 | 85 | 2421 | 76 % | 90 % |
| Pohjois-Savo | 378 | 99 | 2282 | 79 % | 86 % |
| Pirkanmaa | 77 | 10 | 1995 | 89 % | 96 % |
| Pohjanmaa | 108 | 42 | 1635 | 72 % | 94 % |
| Varsinais-Suomi | 5 | 7 | 1747 | 42 % | 100 % |
| Kymenlaakso | 51 | 12 | 1514 | 81 % | 97 % |
| Pohjois-Karjala | 110 | 40 | 1265 | 73 % | 92 % |
| Keski-Pohjanmaa | 217 | 20 | 921 | 92 % | 81 % |
| Etelä-Savo | 95 | 20 | 900 | 83 % | 90 % |
| Etelä-Karjala | 73 | 23 | 888 | 76 % | 92 % |
| Satakunta | 13 | 0 | 917 | 100 % | 99 % |
| Päijät-Häme | 5 | 4 | 878 | 56 % | 99 % |
| Kanta-Häme | 0 | 0 | 650 | – % | 100 % |
| Kainuu | 81 | 5 | 348 | 94 % | 81 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 1656 | 17805 | 9 % |
| tiesääennuste (Digitraffic) | 1127 | 7442 | 13 % |
| märkä tie jäätyy | 956 | 2650 | 27 % |
| lumisade | 1344 | 1979 | 40 % |
| lumi / sohjo | 52 | 1200 | 4 % |
| jäätävä sade | 104 | 876 | 11 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 444 |
| tie −1…+1 °C | 180 |
| tie alle −4 °C | 151 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 16009 | 1133 | 45428 | 320971 | 93 % | 74 % |
| +6 h | 14183 | 3082 | 56814 | 309356 | 82 % | 80 % |
| +12 h | 14649 | 2866 | 61856 | 301704 | 84 % | 81 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 6162 | 795 | 8527 | 89 % |
| Pohjois-Pohjanmaa | 3062 | 699 | 7186 | 81 % |
| Finavia lentokentät | 387 | 428 | 4791 | 47 % |
| Etelä-Pohjanmaa | 464 | 104 | 3925 | 82 % |
| Keski-Suomi | 524 | 100 | 3560 | 84 % |
| Pohjois-Savo | 767 | 149 | 3227 | 84 % |
| Kainuu | 1019 | 176 | 2906 | 85 % |
| Pohjois-Karjala | 514 | 121 | 3374 | 81 % |
| Uusimaa | 36 | 27 | 3489 | 57 % |
| Varsinais-Suomi | 115 | 40 | 2902 | 74 % |
| Pirkanmaa | 144 | 29 | 2602 | 83 % |
| Pohjanmaa | 167 | 48 | 1949 | 78 % |
| Keski-Pohjanmaa | 411 | 38 | 1553 | 92 % |
| Etelä-Savo | 157 | 37 | 1747 | 81 % |
| Kymenlaakso | 84 | 28 | 1566 | 75 % |
| Etelä-Karjala | 120 | 244 | 990 | 33 % |
| Päijät-Häme | 17 | 3 | 962 | 85 % |
| Satakunta | 25 | 13 | 916 | 66 % |
| Kanta-Häme | 8 | 3 | 642 | 73 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 6147 | 31931 |
| tiesääennuste (Digitraffic) | 3248 | 12937 |
| lumisade | 2944 | 3997 |
| märkä tie jäätyy | 1456 | 4404 |
| jäätävä sade | 269 | 1720 |
| lumi / sohjo | 119 | 1825 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 1955 |
| varoitus häly | 549 |
| kitka < 0,45 | 312 |
| jäätä tiellä | 118 |
| keli lumi | 76 |
| keli kuura | 72 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 18784 | 2133 (11 %) | 37516 | 0 (0 %) | 3713 (10 %) | 6360 (17 %) |
| 0,5–2 | 4991 | 556 (11 %) | 9581 | 0 (0 %) | 2636 (28 %) | 1676 (17 %) |
| 2–4 | 3589 | 443 (12 %) | 7423 | 0 (0 %) | 1859 (25 %) | 1527 (21 %) |
| 4–8 | 3949 | 482 (12 %) | 8471 | 2 (0 %) | 1976 (23 %) | 1785 (21 %) |
| yli 8 | 5597 | 1054 (19 %) | 14512 | 457 (3 %) | 2237 (15 %) | 3791 (26 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 8083 | 19 % (17 % / 12471) | 12800 | 19 % (22 % / 20770) |
| −4…−2 | 2214 | 20 % (15 % / 3719) | 4025 | 29 % (30 % / 6607) |
| −6…−4 | 321 | 44 % (28 % / 543) | 901 | 63 % (53 % / 1526) |
| −8…−6 | 29 | 69 % (65 % / 40) | 326 | 67 % (59 % / 447) |
| alle −8 | 0 | – (73 % / 22) | 499 | 83 % (76 % / 615) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 30 päivältä, 13914 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 3619 | 880 |
| Vain urakka suolasi | 211 | 4 |
| Vain ennuste hälytti | 4988 | 1210 |
| Kumpikaan ei | 5096 | 23 |

Suolauskertoja 4152: ennuste hälytti 0–12 h ennen 3651 kertaa (88 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 906 kertaa (22 %).
Liukkaista asemavuorokausista 2117: suolattu ennen ensimmäistä liukasta mittausta 502, vasta sen jälkeen (6 h sisällä) 250.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2551 | 501 | 90 | 876 | 616 | 477 | 62 |
| Oulu | 420 | 198 | 21 | 118 | 194 | 150 | 62 |
| Kuopio | 330 | 124 | 0 | 91 | 156 | 145 | 49 |
| Kittilä | 235 | 0 | 0 | 214 | 0 | 0 | 0 |
| Raahe/Ylivieska | 261 | 94 | 6 | 91 | 120 | 109 | 50 |
| Kemi | 234 | 75 | 1 | 124 | 85 | 82 | 32 |
| Kajaani | 240 | 122 | 0 | 59 | 144 | 136 | 41 |
| Lapua | 270 | 108 | 8 | 77 | 115 | 99 | 38 |
| Salo | 330 | 84 | 0 | 104 | 86 | 71 | 7 |
| Tampere | 270 | 58 | 5 | 83 | 87 | 78 | 9 |
| Ivalo | 180 | 1 | 0 | 168 | 1 | 1 | 0 |
| Kotka | 300 | 40 | 4 | 114 | 52 | 45 | 7 |
| Seinäjoki | 224 | 87 | 0 | 68 | 97 | 96 | 21 |
| Joensuu | 210 | 52 | 6 | 87 | 75 | 58 | 18 |
| Pudasjärvi-Taivalkoski | 150 | 57 | 1 | 78 | 67 | 63 | 19 |
| Espoo 19-24 | 401 | 65 | 5 | 79 | 65 | 54 | 0 |
| Nummi | 270 | 69 | 5 | 73 | 71 | 65 | 5 |
| Kuusamo | 150 | 36 | 0 | 94 | 41 | 41 | 35 |
| Paimio | 270 | 56 | 2 | 73 | 61 | 53 | 1 |
| Kristiinankaupunki | 210 | 72 | 2 | 59 | 70 | 62 | 7 |
| Lappeenranta | 180 | 45 | 1 | 56 | 66 | 63 | 23 |
| Veteli | 150 | 47 | 0 | 58 | 61 | 59 | 28 |
| Hyvinkää | 210 | 45 | 0 | 67 | 51 | 45 | 4 |
| Orivesi | 171 | 62 | 0 | 39 | 79 | 73 | 15 |
| Kemijärvi-Posio | 128 | 14 | 0 | 102 | 15 | 15 | 6 |
| Sodankylä | 120 | 0 | 0 | 113 | 0 | 0 | 0 |
| Mikkeli | 169 | 50 | 0 | 57 | 54 | 53 | 13 |
| Nurmes | 150 | 46 | 0 | 71 | 38 | 36 | 14 |
| Lahti | 180 | 58 | 1 | 45 | 61 | 53 | 6 |
| Äänekoski | 150 | 46 | 0 | 50 | 55 | 51 | 24 |
| Pori | 180 | 46 | 1 | 46 | 58 | 47 | 12 |
| Vaasa | 120 | 47 | 4 | 27 | 73 | 60 | 10 |
| E18 Muurla-Lohja | 180 | 54 | 0 | 46 | 50 | 43 | 0 |
| Rovaniemi | 90 | 36 | 1 | 41 | 54 | 48 | 12 |
| Suonenjoki | 120 | 37 | 1 | 49 | 44 | 43 | 14 |
| Kitee | 139 | 51 | 3 | 38 | 49 | 38 | 7 |
| Viinijärvi | 120 | 29 | 0 | 55 | 31 | 28 | 15 |
| Porvoo | 178 | 28 | 1 | 54 | 31 | 26 | 2 |
| Raisio | 180 | 55 | 6 | 33 | 52 | 39 | 3 |
| Juva | 120 | 31 | 1 | 45 | 38 | 35 | 6 |
| Pyhäjärvi | 90 | 41 | 0 | 24 | 58 | 55 | 16 |
| Jyväskylä | 210 | 51 | 13 | 29 | 51 | 37 | 0 |
| Suomussalmi | 90 | 17 | 0 | 63 | 15 | 14 | 6 |
| Jämsä | 120 | 25 | 0 | 49 | 26 | 26 | 2 |
| Kouvola | 120 | 28 | 0 | 39 | 32 | 29 | 3 |
| Kokkola | 90 | 30 | 0 | 36 | 33 | 33 | 17 |
| Puolanka | 90 | 9 | 0 | 60 | 9 | 9 | 5 |
| Lieto | 150 | 43 | 5 | 29 | 39 | 31 | 0 |
| Kauhajoki | 90 | 32 | 0 | 29 | 39 | 39 | 11 |
| Ii | 90 | 26 | 1 | 45 | 23 | 22 | 15 |
| Pihtipudas | 90 | 31 | 0 | 30 | 36 | 34 | 12 |
| Koskenkylä -Kotka | 120 | 19 | 2 | 31 | 30 | 23 | 0 |
| Pieksämäki | 90 | 23 | 0 | 39 | 22 | 22 | 6 |
| Rovaniemi 17-22 | 60 | 21 | 0 | 36 | 24 | 24 | 7 |
| Virrat | 90 | 29 | 1 | 28 | 31 | 29 | 5 |
| Raasepori | 150 | 26 | 3 | 33 | 24 | 19 | 0 |
| Savonlinna | 79 | 26 | 0 | 23 | 34 | 33 | 10 |
| Imatra | 90 | 23 | 0 | 32 | 25 | 24 | 3 |
| Alavus | 73 | 40 | 0 | 19 | 38 | 36 | 5 |
| Hamina-Vaalimaa | 90 | 13 | 1 | 33 | 20 | 19 | 2 |
| Pello | 53 | 8 | 0 | 42 | 9 | 9 | 4 |
| Karstula | 60 | 21 | 0 | 20 | 30 | 29 | 15 |
| Siikalatva | 60 | 32 | 1 | 13 | 35 | 32 | 14 |
| Kuhmo | 60 | 9 | 0 | 38 | 10 | 10 | 4 |
| Mäntsälä | 90 | 18 | 0 | 27 | 20 | 17 | 2 |
| Nilsiä | 60 | 21 | 0 | 23 | 24 | 23 | 13 |
| Ilomantsi | 60 | 9 | 0 | 37 | 8 | 8 | 0 |
| Keuruu | 60 | 19 | 1 | 21 | 23 | 22 | 11 |
| Kangasala | 60 | 19 | 2 | 10 | 31 | 27 | 6 |
| Espoo | 90 | 16 | 1 | 20 | 18 | 14 | 0 |
| Iisalmi | 60 | 27 | 0 | 14 | 24 | 24 | 10 |
| Heinola | 60 | 16 | 0 | 20 | 16 | 16 | 1 |
| Parkano | 60 | 18 | 0 | 19 | 16 | 15 | 5 |
| Harjavalta | 60 | 12 | 0 | 21 | 12 | 12 | 0 |
| Merikarvia | 60 | 17 | 0 | 11 | 22 | 19 | 4 |
| Hämeenlinna | 60 | 11 | 1 | 19 | 11 | 10 | 1 |
| Huittinen | 60 | 13 | 0 | 16 | 12 | 12 | 0 |
| Pielavesi | 30 | 7 | 0 | 16 | 11 | 11 | 5 |
| Ranua | 30 | 9 | 0 | 17 | 8 | 7 | 3 |
| Kankaanpää | 30 | 9 | 0 | 10 | 10 | 10 | 3 |
| Kiuruvesi | 30 | 9 | 0 | 12 | 8 | 8 | 2 |
| Vantaa | 48 | 8 | 3 | 9 | 10 | 6 | 0 |
| Loimaa | 30 | 5 | 0 | 13 | 5 | 5 | 1 |
| Sastamala | 30 | 7 | 0 | 11 | 7 | 7 | 0 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
