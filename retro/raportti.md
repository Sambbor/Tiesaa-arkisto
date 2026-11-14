# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v17) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 32 (2026-10-12 – 2026-11-12), laskentoja 341623. Päivitetty 2026-11-14T06:11:33Z.

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Ennuste "liukas" = indeksi ≥ 50.

## Osumatarkkuus

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 8353 | 962 | 33658 | 295468 | 90 % | 80 % |
| +6 h | 7283 | 2227 | 44598 | 284233 | 77 % | 86 % |
| +12 h | 7631 | 2274 | 48989 | 277090 | 77 % | 87 % |

## Maakunnittain (+6 h)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 3516 | 626 | 7501 | 85 % |
| Pohjois-Pohjanmaa | 1476 | 516 | 5937 | 74 % |
| Finavia lentokentät | 302 | 414 | 3163 | 42 % |
| Etelä-Pohjanmaa | 196 | 64 | 3061 | 75 % |
| Kainuu | 451 | 100 | 2557 | 82 % |
| Keski-Suomi | 159 | 32 | 2862 | 83 % |
| Pohjois-Savo | 314 | 76 | 2652 | 81 % |
| Pohjois-Karjala | 174 | 57 | 2537 | 75 % |
| Uusimaa | 23 | 9 | 2545 | 72 % |
| Varsinais-Suomi | 95 | 28 | 2227 | 77 % |
| Pirkanmaa | 79 | 16 | 1856 | 83 % |
| Pohjanmaa | 89 | 10 | 1498 | 90 % |
| Keski-Pohjanmaa | 220 | 19 | 1332 | 92 % |
| Etelä-Savo | 50 | 11 | 1240 | 82 % |
| Kymenlaakso | 63 | 15 | 1156 | 81 % |
| Etelä-Karjala | 48 | 227 | 682 | 17 % |
| Satakunta | 11 | 5 | 685 | 69 % |
| Päijät-Häme | 12 | 1 | 653 | 92 % |
| Kanta-Häme | 5 | 1 | 454 | 83 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 4455 | 29013 |
| tiesääennuste (Digitraffic) | 1393 | 9182 |
| märkä tie jäätyy | 648 | 3313 |
| lumisade | 662 | 1429 |
| lumi / sohjo | 21 | 890 |
| jäätävä sade | 104 | 771 |

## Ohi menneet: mitä asema mittasi (+6 h)

| Havainto | Kpl |
|---|---|
| keli jää | 1514 |
| varoitus häly | 351 |
| kitka < 0,45 | 190 |
| keli kuura | 71 |
| keli lumi | 62 |
| jäätä tiellä | 39 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kuinka usein asema mittasi kuuraa tiellä (keli kuura), antoi Kuura-varoituksen (kuuraava tilanne: tie kastepisteen alapuolella) tai mittasi liukasta samalla hetkellä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta |
|---|---|---|---|---|
| 0–0,5 | 29984 | 0 (0 %) | 3710 (12 %) | 2995 (10 %) |
| 0,5–2 | 7466 | 0 (0 %) | 2628 (35 %) | 858 (11 %) |
| 2–4 | 5776 | 0 (0 %) | 1839 (32 %) | 881 (15 %) |
| 4–8 | 6687 | 2 (0 %) | 1908 (29 %) | 1139 (17 %) |
| yli 8 | 11801 | 431 (4 %) | 2109 (18 %) | 2699 (23 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä. "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja | liukasta | Ei suolaa: tunteja | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 8438 | 7 % | 15537 | 15 % |
| −4…−2 | 3059 | 9 % | 5563 | 25 % |
| −6…−4 | 343 | 10 % | 940 | 37 % |
| −8…−6 | 22 | 50 % | 262 | 42 % |
| alle −8 | 19 | 68 % | 300 | 55 % |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 26 päivältä, 12034 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 2749 | 457 |
| Vain urakka suolasi | 203 | 2 |
| Vain ennuste hälytti | 4336 | 898 |
| Kumpikaan ei | 4746 | 22 |

Suolauskertoja 2835: ennuste hälytti 0–12 h ennen 2365 kertaa (83 %), keskimäärin 7 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 289 kertaa (10 %).
Liukkaista asemavuorokausista 1379: suolattu ennen ensimmäistä liukasta mittausta 208, vasta sen jälkeen (6 h sisällä) 138.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 2211 | 372 | 85 | 745 | 418 | 295 | 18 |
| Oulu | 364 | 163 | 21 | 97 | 138 | 94 | 19 |
| Kuopio | 286 | 91 | 0 | 81 | 110 | 99 | 12 |
| Kittilä | 203 | 0 | 0 | 182 | 0 | 0 | 0 |
| Kemi | 202 | 52 | 1 | 115 | 55 | 52 | 6 |
| Kajaani | 208 | 97 | 0 | 52 | 112 | 105 | 14 |
| Salo | 286 | 62 | 0 | 101 | 58 | 44 | 1 |
| Lapua | 234 | 85 | 8 | 66 | 84 | 68 | 21 |
| Raahe/Ylivieska | 225 | 67 | 6 | 82 | 67 | 56 | 14 |
| Ivalo | 156 | 1 | 0 | 144 | 1 | 1 | 0 |
| Kotka | 260 | 23 | 4 | 101 | 29 | 24 | 1 |
| Joensuu | 182 | 38 | 6 | 73 | 52 | 35 | 2 |
| Tampere | 234 | 42 | 5 | 73 | 49 | 40 | 0 |
| Seinäjoki | 192 | 70 | 0 | 55 | 67 | 66 | 8 |
| Pudasjärvi-Taivalkoski | 130 | 44 | 1 | 71 | 49 | 45 | 6 |
| Nummi | 234 | 52 | 5 | 68 | 50 | 44 | 1 |
| Paimio | 234 | 40 | 2 | 72 | 44 | 37 | 0 |
| Kuusamo | 130 | 27 | 0 | 83 | 29 | 29 | 24 |
| Espoo 19-24 | 345 | 37 | 5 | 76 | 34 | 23 | 0 |
| Kristiinankaupunki | 182 | 53 | 2 | 55 | 50 | 42 | 3 |
| Sodankylä | 104 | 0 | 0 | 97 | 0 | 0 | 0 |
| Kemijärvi-Posio | 108 | 12 | 0 | 84 | 12 | 12 | 3 |
| Orivesi | 147 | 50 | 0 | 30 | 65 | 59 | 12 |
| Veteli | 130 | 38 | 0 | 48 | 44 | 42 | 16 |
| Hyvinkää | 182 | 33 | 0 | 59 | 32 | 26 | 0 |
| Nurmes | 130 | 38 | 0 | 59 | 27 | 25 | 4 |
| Lappeenranta | 156 | 33 | 1 | 51 | 33 | 30 | 0 |
| Mikkeli | 145 | 38 | 0 | 52 | 29 | 28 | 3 |
| Pori | 156 | 34 | 1 | 45 | 35 | 25 | 0 |
| Rovaniemi | 78 | 32 | 1 | 33 | 47 | 41 | 7 |
| Lahti | 156 | 46 | 1 | 38 | 40 | 32 | 0 |
| Vaasa | 104 | 36 | 4 | 25 | 53 | 40 | 0 |
| E18 Muurla-Lohja | 156 | 42 | 0 | 43 | 34 | 28 | 0 |
| Äänekoski | 130 | 36 | 0 | 40 | 36 | 32 | 5 |
| Suonenjoki | 104 | 30 | 1 | 40 | 34 | 33 | 4 |
| Raisio | 156 | 43 | 6 | 33 | 39 | 26 | 2 |
| Kitee | 119 | 41 | 2 | 29 | 39 | 28 | 0 |
| Suomussalmi | 78 | 13 | 0 | 55 | 12 | 11 | 4 |
| Porvoo | 154 | 18 | 1 | 47 | 19 | 16 | 0 |
| Viinijärvi | 104 | 22 | 0 | 46 | 20 | 17 | 4 |
| Juva | 104 | 25 | 1 | 39 | 26 | 23 | 0 |
| Jyväskylä | 182 | 36 | 13 | 26 | 35 | 21 | 0 |
| Jämsä | 104 | 22 | 0 | 38 | 23 | 23 | 1 |
| Pyhäjärvi | 78 | 36 | 0 | 17 | 42 | 39 | 1 |
| Lieto | 130 | 33 | 5 | 29 | 29 | 22 | 0 |
| Puolanka | 78 | 5 | 0 | 52 | 5 | 5 | 1 |
| Kouvola | 104 | 20 | 0 | 37 | 16 | 14 | 0 |
| Ii | 78 | 18 | 1 | 41 | 12 | 11 | 6 |
| Kokkola | 78 | 21 | 0 | 33 | 18 | 18 | 8 |
| Kauhajoki | 78 | 26 | 0 | 24 | 27 | 27 | 4 |
| Rovaniemi 17-22 | 52 | 19 | 0 | 30 | 21 | 21 | 4 |
| Pieksämäki | 78 | 17 | 0 | 35 | 14 | 14 | 3 |
| Raasepori | 130 | 18 | 3 | 32 | 16 | 11 | 0 |
| Pihtipudas | 78 | 25 | 0 | 24 | 24 | 22 | 0 |
| Imatra | 78 | 17 | 0 | 30 | 15 | 15 | 0 |
| Koskenkylä -Kotka | 104 | 12 | 2 | 26 | 18 | 12 | 0 |
| Virrat | 78 | 23 | 1 | 22 | 22 | 20 | 4 |
| Pello | 45 | 8 | 0 | 34 | 9 | 9 | 4 |
| Hamina-Vaalimaa | 78 | 7 | 1 | 30 | 11 | 10 | 0 |
| Savonlinna | 67 | 20 | 0 | 18 | 22 | 21 | 0 |
| Kuhmo | 52 | 7 | 0 | 32 | 7 | 7 | 1 |
| Karstula | 52 | 17 | 0 | 16 | 21 | 20 | 6 |
| Alavus | 57 | 32 | 0 | 11 | 26 | 24 | 4 |
| Mäntsälä | 78 | 14 | 0 | 22 | 14 | 11 | 1 |
| Ilomantsi | 52 | 7 | 0 | 31 | 5 | 5 | 0 |
| Nilsiä | 52 | 18 | 0 | 18 | 17 | 16 | 6 |
| Siikalatva | 52 | 27 | 1 | 10 | 24 | 22 | 4 |
| Kangasala | 52 | 15 | 2 | 9 | 24 | 20 | 0 |
| Keuruu | 52 | 15 | 1 | 17 | 16 | 15 | 6 |
| Espoo | 78 | 10 | 1 | 20 | 12 | 8 | 0 |
| Iisalmi | 52 | 21 | 0 | 12 | 18 | 18 | 4 |
| Harjavalta | 52 | 8 | 0 | 21 | 8 | 8 | 0 |
| Parkano | 52 | 14 | 0 | 16 | 12 | 11 | 2 |
| Heinola | 52 | 12 | 0 | 18 | 10 | 10 | 0 |
| Huittinen | 52 | 9 | 0 | 16 | 9 | 9 | 0 |
| Merikarvia | 52 | 13 | 0 | 11 | 13 | 10 | 0 |
| Hämeenlinna | 52 | 7 | 1 | 17 | 7 | 6 | 0 |
| Pielavesi | 26 | 5 | 0 | 14 | 7 | 7 | 1 |
| Ranua | 26 | 7 | 0 | 15 | 6 | 5 | 1 |
| Loimaa | 26 | 3 | 0 | 13 | 3 | 3 | 0 |
| Kiuruvesi | 26 | 9 | 0 | 8 | 8 | 8 | 2 |
| Kankaanpää | 26 | 7 | 0 | 9 | 6 | 6 | 1 |
| Sastamala | 26 | 6 | 0 | 10 | 5 | 5 | 0 |
| Vantaa | 40 | 7 | 1 | 7 | 6 | 3 | 0 |

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0). Säännöt: Sambbor/Vantaakeli, collector/collect.mjs.
