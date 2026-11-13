# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v17) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 31 (2026-10-12 – 2026-11-11), laskentoja 330378. Päivitetty 2026-11-13T12:35:52Z.

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Ennuste "liukas" = indeksi ≥ 50.

## Osumatarkkuus

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 7380 | 945 | 31576 | 287296 | 89 % | 81 % |
| +6 h | 6402 | 2030 | 42424 | 276240 | 76 % | 87 % |
| +12 h | 6525 | 2078 | 45968 | 270172 | 76 % | 88 % |

## Maakunnittain (+6 h)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 3270 | 497 | 7325 | 87 % |
| Pohjois-Pohjanmaa | 1014 | 451 | 5500 | 69 % |
| Finavia lentokentät | 302 | 414 | 2914 | 42 % |
| Etelä-Pohjanmaa | 189 | 64 | 2975 | 75 % |
| Keski-Suomi | 154 | 32 | 2734 | 83 % |
| Pohjois-Savo | 283 | 76 | 2456 | 79 % |
| Kainuu | 376 | 98 | 2338 | 79 % |
| Pohjois-Karjala | 165 | 57 | 2341 | 74 % |
| Uusimaa | 23 | 8 | 2514 | 74 % |
| Varsinais-Suomi | 94 | 28 | 2166 | 77 % |
| Pirkanmaa | 79 | 16 | 1803 | 83 % |
| Pohjanmaa | 85 | 10 | 1433 | 89 % |
| Keski-Pohjanmaa | 186 | 19 | 1183 | 91 % |
| Etelä-Savo | 49 | 11 | 1209 | 82 % |
| Kymenlaakso | 62 | 15 | 1148 | 81 % |
| Etelä-Karjala | 44 | 227 | 655 | 16 % |
| Satakunta | 11 | 5 | 671 | 69 % |
| Päijät-Häme | 11 | 1 | 631 | 92 % |
| Kanta-Häme | 5 | 1 | 428 | 83 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 4339 | 28853 |
| tiesääennuste (Digitraffic) | 1072 | 8505 |
| märkä tie jäätyy | 538 | 3153 |
| lumisade | 351 | 801 |
| jäätävä sade | 87 | 659 |
| lumi / sohjo | 15 | 453 |

## Ohi menneet: mitä asema mittasi (+6 h)

| Havainto | Kpl |
|---|---|
| keli jää | 1325 |
| varoitus häly | 350 |
| kitka < 0,45 | 183 |
| keli kuura | 71 |
| keli lumi | 62 |
| jäätä tiellä | 39 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kuinka usein asema mittasi kuuraa tiellä (keli kuura), antoi Kuura-varoituksen (kuuraava tilanne: tie kastepisteen alapuolella) tai mittasi liukasta samalla hetkellä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta |
|---|---|---|---|---|
| 0–0,5 | 27465 | 0 (0 %) | 3710 (14 %) | 2343 (9 %) |
| 0,5–2 | 7248 | 0 (0 %) | 2628 (36 %) | 791 (11 %) |
| 2–4 | 5632 | 0 (0 %) | 1839 (33 %) | 835 (15 %) |
| 4–8 | 6601 | 2 (0 %) | 1908 (29 %) | 1117 (17 %) |
| yli 8 | 11674 | 431 (4 %) | 2109 (18 %) | 2625 (22 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä. "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja | liukasta | Ei suolaa: tunteja | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 7973 | 5 % | 15096 | 15 % |
| −4…−2 | 2992 | 7 % | 5434 | 24 % |
| −6…−4 | 321 | 8 % | 879 | 35 % |
| −8…−6 | 21 | 48 % | 199 | 45 % |
| alle −8 | 17 | 65 % | 188 | 49 % |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 25 päivältä, 11564 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 2623 | 400 |
| Vain urakka suolasi | 197 | 2 |
| Vain ennuste hälytti | 4071 | 844 |
| Kumpikaan ei | 4673 | 22 |

Suolauskertoja 2758: ennuste hälytti 0–12 h ennen 2293 kertaa (83 %), keskimäärin 7 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 239 kertaa (9 %).
Liukkaista asemavuorokausista 1268: suolattu ennen ensimmäistä liukasta mittausta 203, vasta sen jälkeen (6 h sisällä) 119.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2126 | 361 | 85 | 690 | 414 | 292 | 15 |
| Oulu | 350 | 151 | 21 | 95 | 138 | 94 | 19 |
| Kuopio | 275 | 82 | 0 | 79 | 100 | 89 | 12 |
| Kittilä | 195 | 0 | 0 | 174 | 0 | 0 | 0 |
| Kemi | 194 | 52 | 1 | 107 | 55 | 52 | 6 |
| Kajaani | 200 | 89 | 0 | 52 | 101 | 94 | 4 |
| Salo | 275 | 62 | 0 | 90 | 58 | 44 | 1 |
| Lapua | 225 | 81 | 8 | 61 | 79 | 63 | 16 |
| Raahe/Ylivieska | 216 | 58 | 6 | 82 | 58 | 47 | 6 |
| Ivalo | 150 | 1 | 0 | 138 | 1 | 1 | 0 |
| Kotka | 250 | 22 | 0 | 101 | 25 | 23 | 1 |
| Seinäjoki | 184 | 64 | 0 | 53 | 66 | 65 | 7 |
| Joensuu | 175 | 37 | 6 | 67 | 51 | 34 | 2 |
| Tampere | 225 | 38 | 5 | 68 | 49 | 40 | 0 |
| Pudasjärvi-Taivalkoski | 125 | 44 | 1 | 66 | 49 | 45 | 6 |
| Paimio | 225 | 40 | 2 | 67 | 44 | 37 | 0 |
| Nummi | 225 | 52 | 5 | 59 | 50 | 44 | 1 |
| Espoo 19-24 | 331 | 37 | 5 | 74 | 34 | 23 | 0 |
| Kuusamo | 125 | 27 | 0 | 78 | 29 | 29 | 24 |
| Kristiinankaupunki | 175 | 53 | 2 | 48 | 50 | 42 | 3 |
| Sodankylä | 100 | 0 | 0 | 93 | 0 | 0 | 0 |
| Kemijärvi-Posio | 103 | 12 | 0 | 79 | 12 | 12 | 3 |
| Orivesi | 141 | 50 | 0 | 24 | 65 | 59 | 12 |
| Hyvinkää | 175 | 33 | 0 | 53 | 32 | 26 | 0 |
| Veteli | 125 | 33 | 0 | 48 | 37 | 35 | 9 |
| Lappeenranta | 150 | 27 | 1 | 51 | 32 | 29 | 0 |
| Mikkeli | 139 | 32 | 0 | 52 | 29 | 28 | 3 |
| Nurmes | 125 | 36 | 0 | 56 | 25 | 23 | 2 |
| Rovaniemi | 75 | 32 | 1 | 30 | 47 | 41 | 7 |
| Lahti | 150 | 43 | 1 | 35 | 40 | 32 | 0 |
| Pori | 150 | 34 | 1 | 39 | 35 | 25 | 0 |
| Vaasa | 100 | 35 | 4 | 22 | 52 | 39 | 0 |
| Äänekoski | 125 | 36 | 0 | 35 | 36 | 32 | 5 |
| E18 Muurla-Lohja | 150 | 42 | 0 | 37 | 34 | 28 | 0 |
| Suonenjoki | 100 | 30 | 1 | 36 | 34 | 33 | 4 |
| Raisio | 150 | 43 | 6 | 30 | 39 | 26 | 2 |
| Porvoo | 148 | 17 | 1 | 46 | 19 | 16 | 0 |
| Juva | 100 | 22 | 1 | 38 | 26 | 23 | 0 |
| Suomussalmi | 75 | 13 | 0 | 52 | 12 | 11 | 4 |
| Kitee | 114 | 41 | 2 | 24 | 39 | 28 | 0 |
| Viinijärvi | 100 | 22 | 0 | 42 | 20 | 17 | 4 |
| Jyväskylä | 175 | 36 | 13 | 26 | 35 | 21 | 0 |
| Jämsä | 100 | 22 | 0 | 34 | 23 | 23 | 1 |
| Pyhäjärvi | 75 | 33 | 0 | 17 | 40 | 37 | 0 |
| Lieto | 125 | 33 | 5 | 26 | 29 | 22 | 0 |
| Puolanka | 75 | 5 | 0 | 49 | 5 | 5 | 1 |
| Kouvola | 100 | 16 | 0 | 37 | 16 | 14 | 0 |
| Kauhajoki | 75 | 23 | 0 | 24 | 27 | 27 | 4 |
| Ii | 75 | 17 | 1 | 39 | 11 | 10 | 5 |
| Rovaniemi 17-22 | 50 | 19 | 0 | 28 | 21 | 21 | 4 |
| Raasepori | 125 | 18 | 3 | 32 | 16 | 11 | 0 |
| Pieksämäki | 75 | 16 | 0 | 33 | 14 | 14 | 3 |
| Kokkola | 75 | 18 | 0 | 33 | 14 | 14 | 4 |
| Pihtipudas | 75 | 25 | 0 | 21 | 24 | 22 | 0 |
| Koskenkylä -Kotka | 100 | 12 | 1 | 26 | 18 | 12 | 0 |
| Imatra | 75 | 14 | 0 | 30 | 13 | 13 | 0 |
| Virrat | 75 | 22 | 1 | 20 | 22 | 20 | 4 |
| Pello | 43 | 8 | 0 | 32 | 9 | 9 | 4 |
| Hamina-Vaalimaa | 75 | 7 | 0 | 30 | 10 | 10 | 0 |
| Savonlinna | 64 | 19 | 0 | 16 | 22 | 21 | 0 |
| Kuhmo | 50 | 6 | 0 | 31 | 6 | 6 | 0 |
| Mäntsälä | 75 | 14 | 0 | 21 | 14 | 11 | 1 |
| Ilomantsi | 50 | 7 | 0 | 29 | 5 | 5 | 0 |
| Karstula | 50 | 15 | 0 | 16 | 18 | 17 | 5 |
| Alavus | 53 | 32 | 0 | 7 | 26 | 24 | 4 |
| Kangasala | 50 | 14 | 2 | 8 | 24 | 20 | 0 |
| Nilsiä | 50 | 17 | 0 | 17 | 15 | 14 | 4 |
| Siikalatva | 50 | 25 | 1 | 10 | 22 | 20 | 2 |
| Espoo | 75 | 10 | 1 | 19 | 12 | 8 | 0 |
| Keuruu | 50 | 15 | 1 | 15 | 16 | 15 | 6 |
| Heinola | 50 | 10 | 0 | 18 | 10 | 10 | 0 |
| Iisalmi | 50 | 19 | 0 | 12 | 16 | 16 | 2 |
| Harjavalta | 50 | 8 | 0 | 19 | 8 | 8 | 0 |
| Parkano | 50 | 14 | 0 | 14 | 12 | 11 | 2 |
| Huittinen | 50 | 9 | 0 | 14 | 9 | 9 | 0 |
| Merikarvia | 50 | 13 | 0 | 9 | 13 | 10 | 0 |
| Hämeenlinna | 50 | 7 | 1 | 15 | 7 | 6 | 0 |
| Pielavesi | 25 | 5 | 0 | 13 | 7 | 7 | 1 |
| Ranua | 25 | 7 | 0 | 14 | 6 | 5 | 1 |
| Loimaa | 25 | 3 | 0 | 12 | 3 | 3 | 0 |
| Kankaanpää | 25 | 6 | 0 | 9 | 6 | 6 | 1 |
| Sastamala | 25 | 5 | 0 | 10 | 5 | 5 | 0 |
| Kiuruvesi | 25 | 8 | 0 | 8 | 7 | 7 | 2 |
| Vantaa | 38 | 7 | 1 | 7 | 6 | 3 | 0 |

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0). Säännöt: Sambbor/Vantaakeli, collector/collect.mjs.
