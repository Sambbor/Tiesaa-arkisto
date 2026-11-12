# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v17) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 30 (2026-10-12 – 2026-11-10), laskentoja 319144. Päivitetty 2026-11-12T13:12:19Z.

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Ennuste "liukas" = indeksi ≥ 50.

## Osumatarkkuus

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 5408 | 810 | 30194 | 279570 | 87 % | 85 % |
| +6 h | 4673 | 1491 | 41254 | 268461 | 76 % | 90 % |
| +12 h | 4555 | 1591 | 44320 | 263065 | 74 % | 91 % |

## Maakunnittain (+6 h)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 2259 | 249 | 7752 | 90 % |
| Pohjois-Pohjanmaa | 698 | 240 | 5392 | 74 % |
| Finavia lentokentät | 302 | 414 | 2680 | 42 % |
| Etelä-Pohjanmaa | 137 | 63 | 2693 | 69 % |
| Keski-Suomi | 132 | 32 | 2549 | 80 % |
| Kainuu | 281 | 49 | 2351 | 85 % |
| Pohjois-Savo | 235 | 70 | 2254 | 77 % |
| Uusimaa | 19 | 8 | 2496 | 70 % |
| Pohjois-Karjala | 113 | 37 | 2176 | 75 % |
| Varsinais-Suomi | 78 | 26 | 2093 | 75 % |
| Pirkanmaa | 72 | 16 | 1786 | 82 % |
| Pohjanmaa | 55 | 10 | 1291 | 85 % |
| Keski-Pohjanmaa | 110 | 17 | 1161 | 87 % |
| Etelä-Savo | 49 | 11 | 1166 | 82 % |
| Kymenlaakso | 62 | 15 | 1131 | 81 % |
| Etelä-Karjala | 44 | 227 | 615 | 16 % |
| Satakunta | 11 | 5 | 671 | 69 % |
| Päijät-Häme | 11 | 1 | 576 | 92 % |
| Kanta-Häme | 5 | 1 | 421 | 83 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 3411 | 29406 |
| tiesääennuste (Digitraffic) | 595 | 8016 |
| märkä tie jäätyy | 435 | 2733 |
| jäätävä sade | 65 | 536 |
| lumisade | 160 | 376 |
| lumi / sohjo | 7 | 187 |

## Ohi menneet: mitä asema mittasi (+6 h)

| Havainto | Kpl |
|---|---|
| keli jää | 786 |
| varoitus häly | 350 |
| kitka < 0,45 | 182 |
| keli kuura | 71 |
| keli lumi | 62 |
| jäätä tiellä | 40 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kuinka usein asema mittasi kuuraa tiellä (keli kuura), antoi Kuura-varoituksen (kuuraava tilanne: tie kastepisteen alapuolella) tai mittasi liukasta samalla hetkellä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta |
|---|---|---|---|---|
| 0–0,5 | 24911 | 0 (0 %) | 3710 (15 %) | 1514 (6 %) |
| 0,5–2 | 7074 | 0 (0 %) | 2628 (37 %) | 646 (9 %) |
| 2–4 | 5530 | 0 (0 %) | 1839 (33 %) | 679 (12 %) |
| 4–8 | 6487 | 2 (0 %) | 1908 (29 %) | 908 (14 %) |
| yli 8 | 11528 | 431 (4 %) | 2109 (18 %) | 1976 (17 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä. "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja | liukasta | Ei suolaa: tunteja | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 5466 | 6 % | 11577 | 15 % |
| −4…−2 | 2277 | 7 % | 4058 | 24 % |
| −6…−4 | 208 | 7 % | 677 | 39 % |
| −8…−6 | 2 | 0 % | 52 | 71 % |
| alle −8 | 0 | – | 21 | 62 % |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 24 päivältä, 11094 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 2547 | 341 |
| Vain urakka suolasi | 194 | 2 |
| Vain ennuste hälytti | 3771 | 674 |
| Kumpikaan ei | 4582 | 21 |

Suolauskertoja 2673: ennuste hälytti 0–12 h ennen 2224 kertaa (83 %), keskimäärin 7 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 204 kertaa (8 %).
Liukkaista asemavuorokausista 1038: suolattu ennen ensimmäistä liukasta mittausta 163, vasta sen jälkeen (6 h sisällä) 100.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2040 | 355 | 84 | 634 | 406 | 287 | 15 |
| Oulu | 336 | 151 | 21 | 81 | 138 | 94 | 12 |
| Kittilä | 187 | 0 | 0 | 165 | 0 | 0 | 0 |
| Kuopio | 264 | 73 | 0 | 77 | 86 | 76 | 9 |
| Kemi | 186 | 52 | 1 | 99 | 55 | 52 | 6 |
| Kajaani | 192 | 81 | 0 | 52 | 91 | 87 | 3 |
| Salo | 264 | 62 | 0 | 79 | 58 | 44 | 0 |
| Ivalo | 144 | 1 | 0 | 132 | 1 | 1 | 0 |
| Lapua | 216 | 81 | 8 | 52 | 79 | 63 | 15 |
| Raahe/Ylivieska | 207 | 58 | 6 | 73 | 58 | 47 | 6 |
| Kotka | 240 | 22 | 0 | 97 | 25 | 23 | 1 |
| Tampere | 216 | 38 | 5 | 66 | 49 | 40 | 0 |
| Seinäjoki | 176 | 56 | 0 | 53 | 59 | 58 | 6 |
| Joensuu | 168 | 32 | 6 | 65 | 46 | 30 | 1 |
| Pudasjärvi-Taivalkoski | 120 | 44 | 1 | 61 | 49 | 45 | 5 |
| Espoo 19-24 | 317 | 37 | 5 | 71 | 34 | 23 | 0 |
| Nummi | 216 | 52 | 5 | 54 | 50 | 44 | 1 |
| Paimio | 216 | 39 | 2 | 61 | 43 | 37 | 0 |
| Kuusamo | 120 | 27 | 0 | 72 | 29 | 29 | 22 |
| Kristiinankaupunki | 168 | 52 | 1 | 44 | 48 | 41 | 3 |
| Sodankylä | 96 | 0 | 0 | 89 | 0 | 0 | 0 |
| Kemijärvi-Posio | 98 | 12 | 0 | 74 | 12 | 12 | 3 |
| Orivesi | 135 | 50 | 0 | 19 | 65 | 59 | 10 |
| Hyvinkää | 168 | 33 | 0 | 48 | 32 | 26 | 0 |
| Veteli | 120 | 33 | 0 | 43 | 37 | 35 | 8 |
| Lappeenranta | 144 | 27 | 1 | 45 | 32 | 29 | 0 |
| Nurmes | 120 | 33 | 0 | 54 | 22 | 20 | 0 |
| Mikkeli | 133 | 32 | 0 | 46 | 29 | 28 | 3 |
| Rovaniemi | 72 | 32 | 1 | 27 | 47 | 41 | 7 |
| Pori | 144 | 34 | 1 | 38 | 35 | 25 | 0 |
| Vaasa | 96 | 34 | 4 | 19 | 51 | 38 | 0 |
| Lahti | 144 | 43 | 1 | 29 | 40 | 32 | 0 |
| Suonenjoki | 96 | 29 | 1 | 33 | 33 | 32 | 3 |
| Äänekoski | 120 | 36 | 0 | 30 | 36 | 32 | 5 |
| E18 Muurla-Lohja | 144 | 42 | 0 | 31 | 34 | 28 | 0 |
| Raisio | 144 | 38 | 6 | 29 | 34 | 25 | 2 |
| Porvoo | 142 | 17 | 1 | 42 | 19 | 16 | 0 |
| Suomussalmi | 72 | 13 | 0 | 49 | 12 | 11 | 2 |
| Jyväskylä | 168 | 34 | 15 | 25 | 35 | 19 | 0 |
| Juva | 96 | 22 | 1 | 34 | 26 | 23 | 0 |
| Viinijärvi | 96 | 22 | 0 | 38 | 20 | 17 | 4 |
| Kitee | 109 | 38 | 1 | 23 | 35 | 25 | 0 |
| Pyhäjärvi | 72 | 30 | 0 | 17 | 37 | 34 | 0 |
| Jämsä | 96 | 22 | 0 | 30 | 23 | 23 | 1 |
| Puolanka | 72 | 5 | 0 | 46 | 5 | 5 | 1 |
| Lieto | 120 | 30 | 3 | 26 | 24 | 20 | 0 |
| Kouvola | 96 | 16 | 0 | 33 | 16 | 14 | 0 |
| Kauhajoki | 72 | 23 | 0 | 21 | 27 | 27 | 3 |
| Ii | 72 | 17 | 1 | 36 | 11 | 10 | 5 |
| Rovaniemi 17-22 | 48 | 19 | 0 | 26 | 21 | 21 | 4 |
| Raasepori | 120 | 18 | 3 | 29 | 16 | 11 | 0 |
| Kokkola | 72 | 17 | 0 | 31 | 14 | 14 | 4 |
| Koskenkylä -Kotka | 96 | 12 | 1 | 26 | 18 | 12 | 0 |
| Pieksämäki | 72 | 16 | 0 | 30 | 14 | 14 | 3 |
| Pihtipudas | 72 | 23 | 0 | 20 | 22 | 20 | 0 |
| Imatra | 72 | 12 | 0 | 29 | 11 | 11 | 0 |
| Hamina-Vaalimaa | 72 | 7 | 0 | 29 | 10 | 10 | 0 |
| Pello | 41 | 8 | 0 | 30 | 9 | 9 | 1 |
| Virrat | 72 | 21 | 1 | 18 | 20 | 18 | 4 |
| Savonlinna | 61 | 16 | 0 | 16 | 19 | 18 | 0 |
| Kuhmo | 48 | 6 | 0 | 29 | 6 | 6 | 0 |
| Mäntsälä | 72 | 14 | 0 | 20 | 14 | 11 | 0 |
| Ilomantsi | 48 | 7 | 0 | 27 | 5 | 5 | 0 |
| Karstula | 48 | 14 | 0 | 15 | 17 | 16 | 5 |
| Kangasala | 48 | 14 | 2 | 7 | 24 | 20 | 0 |
| Espoo | 72 | 10 | 1 | 18 | 12 | 8 | 0 |
| Nilsiä | 48 | 16 | 0 | 16 | 14 | 13 | 3 |
| Siikalatva | 48 | 25 | 1 | 8 | 22 | 20 | 2 |
| Keuruu | 48 | 14 | 1 | 14 | 15 | 14 | 5 |
| Alavus | 49 | 28 | 0 | 7 | 22 | 20 | 2 |
| Harjavalta | 48 | 8 | 0 | 18 | 8 | 8 | 0 |
| Heinola | 48 | 10 | 0 | 16 | 10 | 10 | 0 |
| Iisalmi | 48 | 19 | 0 | 10 | 16 | 16 | 2 |
| Parkano | 48 | 14 | 0 | 13 | 12 | 11 | 2 |
| Huittinen | 48 | 9 | 0 | 14 | 9 | 9 | 0 |
| Merikarvia | 48 | 13 | 0 | 9 | 13 | 10 | 0 |
| Hämeenlinna | 48 | 7 | 1 | 14 | 7 | 6 | 0 |
| Pielavesi | 24 | 5 | 0 | 12 | 7 | 7 | 1 |
| Ranua | 24 | 7 | 0 | 13 | 6 | 5 | 1 |
| Kankaanpää | 24 | 6 | 0 | 9 | 6 | 6 | 1 |
| Sastamala | 24 | 5 | 0 | 10 | 5 | 5 | 0 |
| Kiuruvesi | 24 | 7 | 0 | 8 | 7 | 7 | 2 |
| Loimaa | 24 | 3 | 0 | 11 | 3 | 3 | 0 |
| Vantaa | 37 | 7 | 1 | 7 | 6 | 3 | 0 |

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0). Säännöt: Sambbor/Vantaakeli, collector/collect.mjs.
