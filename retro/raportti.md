# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v19) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 40 (2026-10-12 – 2026-11-20), laskentoja 432100. Päivitetty 2026-11-22T12:49:43Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 11232.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 7331 | 272 | 30278 | 222224 | 96 % | 81 % |
| +6 h | 6909 | 857 | 37550 | 214896 | 89 % | 84 % |
| +12 h | 7176 | 799 | 41257 | 209498 | 90 % | 85 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 1948 | 257 | 5603 | 88 % | 74 % |
| Lappi | 2632 | 108 | 3680 | 96 % | 58 % |
| Keski-Suomi | 492 | 103 | 3915 | 83 % | 89 % |
| Etelä-Pohjanmaa | 332 | 85 | 3164 | 80 % | 91 % |
| Pohjois-Savo | 488 | 107 | 2832 | 82 % | 85 % |
| Uusimaa | 19 | 6 | 2940 | 76 % | 99 % |
| Pirkanmaa | 96 | 10 | 2230 | 91 % | 96 % |
| Pohjanmaa | 157 | 42 | 2129 | 79 % | 93 % |
| Varsinais-Suomi | 5 | 7 | 1897 | 42 % | 100 % |
| Pohjois-Karjala | 128 | 42 | 1533 | 75 % | 92 % |
| Kymenlaakso | 51 | 12 | 1520 | 81 % | 97 % |
| Keski-Pohjanmaa | 275 | 21 | 1127 | 93 % | 80 % |
| Etelä-Savo | 109 | 25 | 987 | 81 % | 90 % |
| Satakunta | 13 | 0 | 1009 | 100 % | 99 % |
| Etelä-Karjala | 73 | 23 | 912 | 76 % | 93 % |
| Päijät-Häme | 5 | 4 | 916 | 56 % | 99 % |
| Kanta-Häme | 0 | 0 | 660 | – % | 100 % |
| Kainuu | 86 | 5 | 496 | 95 % | 85 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 2041 | 18347 | 10 % |
| tiesääennuste (Digitraffic) | 1473 | 9688 | 13 % |
| lumisade | 1952 | 3304 | 37 % |
| märkä tie jäätyy | 1279 | 3926 | 25 % |
| lumi / sohjo | 106 | 2174 | 5 % |
| jäätävä sade | 58 | 111 | 34 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 492 |
| tie −1…+1 °C | 211 |
| tie alle −4 °C | 154 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 21194 | 1200 | 54926 | 351573 | 95 % | 72 % |
| +6 h | 19204 | 3535 | 67238 | 338800 | 84 % | 78 % |
| +12 h | 19987 | 3244 | 73916 | 329252 | 86 % | 79 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 8570 | 913 | 9472 | 90 % |
| Pohjois-Pohjanmaa | 3856 | 785 | 9399 | 83 % |
| Finavia lentokentät | 944 | 579 | 5816 | 62 % |
| Etelä-Pohjanmaa | 564 | 106 | 5078 | 84 % |
| Kainuu | 1459 | 238 | 3709 | 86 % |
| Pohjois-Savo | 965 | 157 | 4014 | 86 % |
| Keski-Suomi | 653 | 101 | 4258 | 87 % |
| Pohjois-Karjala | 667 | 138 | 4166 | 83 % |
| Uusimaa | 51 | 28 | 3702 | 65 % |
| Varsinais-Suomi | 120 | 41 | 3116 | 75 % |
| Pirkanmaa | 172 | 31 | 2921 | 85 % |
| Pohjanmaa | 247 | 48 | 2546 | 84 % |
| Keski-Pohjanmaa | 521 | 40 | 1878 | 93 % |
| Etelä-Savo | 161 | 38 | 1916 | 81 % |
| Kymenlaakso | 84 | 28 | 1572 | 75 % |
| Etelä-Karjala | 120 | 245 | 1017 | 33 % |
| Satakunta | 25 | 13 | 1008 | 66 % |
| Päijät-Häme | 17 | 3 | 998 | 85 % |
| Kanta-Häme | 8 | 3 | 652 | 73 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 7534 | 33573 |
| tiesääennuste (Digitraffic) | 4614 | 16980 |
| lumisade | 4681 | 6348 |
| märkä tie jäätyy | 2000 | 6811 |
| lumi / sohjo | 200 | 3265 |
| jäätävä sade | 175 | 261 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 2249 |
| varoitus häly | 568 |
| kitka < 0,45 | 351 |
| jäätä tiellä | 151 |
| keli lumi | 144 |
| keli kuura | 72 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 21237 | 2749 (13 %) | 43223 | 0 (0 %) | 3809 (9 %) | 8390 (19 %) |
| 0,5–2 | 5705 | 807 (14 %) | 11230 | 0 (0 %) | 2703 (24 %) | 2311 (21 %) |
| 2–4 | 3959 | 586 (15 %) | 8599 | 0 (0 %) | 1914 (22 %) | 1989 (23 %) |
| 4–8 | 4304 | 646 (15 %) | 9839 | 2 (0 %) | 2063 (21 %) | 2431 (25 %) |
| yli 8 | 6089 | 1340 (22 %) | 16342 | 494 (3 %) | 2424 (15 %) | 4900 (30 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 9322 | 20 % (19 % / 14731) | 15772 | 22 % (25 % / 26381) |
| −4…−2 | 2258 | 21 % (16 % / 3850) | 4299 | 32 % (33 % / 7087) |
| −6…−4 | 327 | 45 % (29 % / 556) | 1067 | 69 % (58 % / 1798) |
| −8…−6 | 33 | 73 % (68 % / 44) | 416 | 74 % (66 % / 547) |
| alle −8 | 0 | – (73 % / 22) | 579 | 85 % (79 % / 697) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 34 päivältä, 15808 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 4218 | 1148 |
| Vain urakka suolasi | 241 | 4 |
| Vain ennuste hälytti | 5769 | 1512 |
| Kumpikaan ei | 5580 | 23 |

Suolauskertoja 4752: ennuste hälytti 0–12 h ennen 4201 kertaa (88 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 1172 kertaa (25 %).
Liukkaista asemavuorokausista 2687: suolattu ennen ensimmäistä liukasta mittausta 596, vasta sen jälkeen (6 h sisällä) 387.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2898 | 575 | 99 | 1047 | 689 | 537 | 96 |
| Oulu | 476 | 237 | 21 | 135 | 238 | 188 | 88 |
| Kuopio | 374 | 163 | 0 | 93 | 202 | 191 | 58 |
| Kajaani | 272 | 154 | 0 | 59 | 194 | 186 | 55 |
| Kemi | 266 | 102 | 1 | 128 | 125 | 120 | 57 |
| Raahe/Ylivieska | 297 | 128 | 6 | 89 | 161 | 148 | 71 |
| Kittilä | 267 | 0 | 0 | 246 | 0 | 0 | 0 |
| Lapua | 306 | 128 | 12 | 88 | 137 | 115 | 43 |
| Salo | 374 | 95 | 0 | 109 | 102 | 87 | 7 |
| Seinäjoki | 256 | 97 | 0 | 86 | 107 | 106 | 27 |
| Ivalo | 204 | 1 | 0 | 192 | 1 | 1 | 0 |
| Tampere | 306 | 64 | 9 | 93 | 93 | 84 | 11 |
| Joensuu | 238 | 68 | 6 | 97 | 86 | 69 | 22 |
| Kotka | 340 | 41 | 5 | 124 | 52 | 45 | 7 |
| Pudasjärvi-Taivalkoski | 170 | 71 | 1 | 84 | 92 | 88 | 32 |
| Kristiinankaupunki | 238 | 83 | 2 | 76 | 81 | 72 | 10 |
| Kuusamo | 170 | 38 | 0 | 112 | 43 | 43 | 37 |
| Espoo 19-24 | 457 | 71 | 6 | 87 | 66 | 55 | 0 |
| Paimio | 306 | 64 | 2 | 81 | 71 | 63 | 1 |
| Nummi | 306 | 79 | 5 | 79 | 72 | 65 | 5 |
| Orivesi | 195 | 67 | 1 | 52 | 86 | 80 | 20 |
| Kemijärvi-Posio | 148 | 15 | 0 | 121 | 16 | 16 | 7 |
| Lappeenranta | 204 | 50 | 1 | 67 | 69 | 65 | 23 |
| Veteli | 170 | 58 | 0 | 67 | 69 | 66 | 34 |
| Nurmes | 170 | 51 | 0 | 86 | 43 | 41 | 15 |
| Sodankylä | 136 | 0 | 0 | 129 | 0 | 0 | 0 |
| Hyvinkää | 238 | 52 | 0 | 72 | 51 | 45 | 4 |
| Pori | 204 | 50 | 1 | 60 | 61 | 49 | 13 |
| Äänekoski | 170 | 54 | 0 | 62 | 59 | 55 | 28 |
| Lahti | 204 | 62 | 3 | 59 | 61 | 53 | 6 |
| Mikkeli | 193 | 51 | 0 | 64 | 55 | 54 | 13 |
| Vaasa | 136 | 48 | 4 | 42 | 74 | 61 | 10 |
| Rovaniemi | 102 | 40 | 1 | 49 | 65 | 59 | 20 |
| Suonenjoki | 136 | 45 | 1 | 57 | 55 | 53 | 20 |
| Kitee | 159 | 58 | 6 | 48 | 59 | 44 | 9 |
| E18 Muurla-Lohja | 204 | 60 | 0 | 51 | 54 | 46 | 0 |
| Viinijärvi | 136 | 36 | 0 | 64 | 37 | 34 | 15 |
| Juva | 136 | 31 | 1 | 58 | 38 | 34 | 6 |
| Raisio | 204 | 61 | 6 | 43 | 52 | 39 | 3 |
| Pyhäjärvi | 102 | 49 | 0 | 28 | 67 | 63 | 20 |
| Suomussalmi | 106 | 21 | 0 | 75 | 20 | 18 | 7 |
| Porvoo | 202 | 33 | 1 | 57 | 31 | 26 | 2 |
| Jämsä | 136 | 26 | 0 | 59 | 27 | 27 | 3 |
| Jyväskylä | 238 | 58 | 13 | 31 | 53 | 39 | 0 |
| Ii | 102 | 34 | 1 | 49 | 33 | 32 | 19 |
| Kauhajoki | 102 | 35 | 0 | 38 | 43 | 43 | 12 |
| Kokkola | 102 | 41 | 0 | 37 | 43 | 43 | 25 |
| Puolanka | 102 | 14 | 0 | 67 | 13 | 13 | 7 |
| Kouvola | 136 | 32 | 0 | 45 | 32 | 29 | 3 |
| Pihtipudas | 102 | 37 | 0 | 36 | 40 | 38 | 16 |
| Lieto | 170 | 48 | 5 | 36 | 39 | 31 | 0 |
| Pieksämäki | 102 | 23 | 0 | 50 | 22 | 22 | 6 |
| Virrat | 102 | 34 | 1 | 35 | 36 | 33 | 7 |
| Rovaniemi 17-22 | 68 | 25 | 0 | 40 | 29 | 29 | 11 |
| Savonlinna | 91 | 30 | 0 | 31 | 36 | 34 | 10 |
| Alavus | 89 | 48 | 0 | 23 | 44 | 42 | 9 |
| Raasepori | 170 | 28 | 3 | 38 | 24 | 19 | 0 |
| Koskenkylä -Kotka | 136 | 22 | 3 | 32 | 30 | 23 | 0 |
| Imatra | 102 | 23 | 0 | 36 | 25 | 24 | 3 |
| Siikalatva | 71 | 41 | 1 | 15 | 46 | 41 | 20 |
| Pello | 61 | 16 | 0 | 42 | 19 | 19 | 12 |
| Karstula | 68 | 25 | 0 | 24 | 33 | 32 | 18 |
| Hamina-Vaalimaa | 102 | 13 | 1 | 36 | 20 | 19 | 2 |
| Kuhmo | 68 | 11 | 0 | 44 | 12 | 12 | 6 |
| Nilsiä | 68 | 26 | 0 | 26 | 29 | 28 | 17 |
| Ilomantsi | 68 | 11 | 0 | 43 | 10 | 10 | 1 |
| Keuruu | 68 | 21 | 1 | 27 | 25 | 24 | 13 |
| Mäntsälä | 102 | 21 | 0 | 28 | 20 | 17 | 2 |
| Iisalmi | 68 | 33 | 0 | 16 | 29 | 28 | 12 |
| Kangasala | 68 | 20 | 4 | 12 | 32 | 28 | 7 |
| Parkano | 68 | 20 | 0 | 23 | 18 | 17 | 7 |
| Espoo | 102 | 19 | 1 | 21 | 19 | 14 | 0 |
| Harjavalta | 68 | 12 | 0 | 27 | 12 | 12 | 0 |
| Heinola | 68 | 16 | 1 | 23 | 16 | 16 | 1 |
| Merikarvia | 68 | 17 | 0 | 16 | 22 | 19 | 4 |
| Hämeenlinna | 68 | 12 | 2 | 23 | 11 | 10 | 1 |
| Huittinen | 68 | 13 | 0 | 21 | 12 | 12 | 0 |
| Pielavesi | 34 | 9 | 0 | 18 | 12 | 12 | 6 |
| Ranua | 34 | 11 | 0 | 19 | 10 | 9 | 4 |
| Kankaanpää | 34 | 9 | 0 | 14 | 10 | 10 | 3 |
| Kiuruvesi | 34 | 11 | 0 | 14 | 9 | 8 | 2 |
| Vantaa | 56 | 9 | 3 | 11 | 11 | 7 | 0 |
| Sastamala | 34 | 7 | 0 | 13 | 7 | 7 | 0 |
| Loimaa | 34 | 6 | 0 | 14 | 5 | 5 | 1 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
