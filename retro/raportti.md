# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v23) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 43 (2026-10-12 – 2026-11-23), laskentoja 466118. Päivitetty 2026-11-25T14:59:08Z.

Ennuste "liukas" = indeksi ≥ 50. Vertailukohta on **kitkatotuus**: optinen kitka alle 0,6 kylmällä tiellä (enintään +1 °C) kahdessa peräkkäisessä mittauksessa eli vähintään noin tunnin. Mukana ovat vain asemat ja hetket, joilla on kelvollinen kitkamittaus (noin puolella asemista on optinen anturi); anturi, joka näyttää liukasta lämpimällä tiellä, jätetään pois. Sama määritelmä on koko Suomen yökoosteessa ja kelikeskuksen aamuvertailussa.

## Osumatarkkuus (kitkatotuus)

Asemavuorokausia, joilla kitka-anturi: 12094.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 12375 | 911 | 26286 | 241155 | 93 % | 68 % |
| +6 h | 11644 | 1852 | 37921 | 229408 | 86 % | 77 % |
| +12 h | 12005 | 1787 | 44529 | 221016 | 87 % | 79 % |

## Maakunnittain (+6 h, kitkatotuus)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|
| Pohjois-Pohjanmaa | 2600 | 499 | 4942 | 84 % | 66 % |
| Lappi | 3224 | 155 | 3456 | 95 % | 52 % |
| Keski-Suomi | 1078 | 186 | 3757 | 85 % | 78 % |
| Etelä-Pohjanmaa | 889 | 247 | 2968 | 78 % | 77 % |
| Pohjois-Savo | 1013 | 217 | 2613 | 82 % | 72 % |
| Uusimaa | 143 | 21 | 3640 | 87 % | 96 % |
| Pirkanmaa | 383 | 73 | 2288 | 84 % | 86 % |
| Pohjanmaa | 318 | 92 | 2180 | 78 % | 87 % |
| Varsinais-Suomi | 145 | 45 | 2266 | 76 % | 94 % |
| Kymenlaakso | 219 | 37 | 1806 | 86 % | 89 % |
| Pohjois-Karjala | 316 | 89 | 1415 | 78 % | 82 % |
| Keski-Pohjanmaa | 505 | 57 | 1067 | 90 % | 68 % |
| Etelä-Savo | 241 | 51 | 1155 | 83 % | 83 % |
| Satakunta | 139 | 26 | 1137 | 84 % | 89 % |
| Etelä-Karjala | 137 | 32 | 1063 | 81 % | 89 % |
| Päijät-Häme | 70 | 5 | 1033 | 93 % | 94 % |
| Kanta-Häme | 66 | 6 | 705 | 92 % | 91 % |
| Kainuu | 158 | 14 | 430 | 92 % | 73 % |

## Hälytyksen syy (+6 h, indeksi ≥ 50, kitkatotuus)

| Syy | Osui | Turha | Osui % |
|---|---|---|---|
| kuura | 2501 | 20484 | 11 % |
| tiesääennuste (Digitraffic) | 3682 | 11496 | 24 % |
| märkä tie jäätyy | 2517 | 3842 | 40 % |
| lumisade | 2884 | 1967 | 59 % |
| jäätävä sade | 60 | 132 | 31 % |

## Ohi menneet: tienpinta liukkaalla hetkellä (+6 h, kitkatotuus)

| Tienpinta | Kpl |
|---|---|
| tie −4…−1 °C | 1036 |
| tie −1…+1 °C | 549 |
| tie alle −4 °C | 267 |

## Vertailu: vanha havaintomääritelmä

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Kaikki asemat. **Jaksot eivät ole keskenään vertailukelpoisia:** Digitrafficin keli- ja varoitustieto puuttui 6.–16.11.2026, ja sinä aikana keli on johdettu tienpinnan tilasta (kuura, lumi ja jää yhtenä luokkana), mikä lisäsi mitattuja liukkaita tunteja moninkertaisesti.

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 27618 | 5750 | 51059 | 378465 | 83 % | 65 % |
| +6 h | 27831 | 5986 | 69307 | 359643 | 82 % | 71 % |
| +12 h | 28852 | 5560 | 80036 | 345937 | 84 % | 74 % |

### Maakunnittain (+6 h, vanha määritelmä)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 10231 | 1231 | 9496 | 89 % |
| Pohjois-Pohjanmaa | 4861 | 1273 | 8881 | 79 % |
| Finavia lentokentät | 1560 | 938 | 6222 | 62 % |
| Etelä-Pohjanmaa | 1342 | 325 | 4951 | 81 % |
| Kainuu | 2059 | 396 | 3682 | 84 % |
| Pohjois-Savo | 1665 | 406 | 3814 | 80 % |
| Pohjois-Karjala | 1218 | 245 | 4123 | 83 % |
| Keski-Suomi | 1296 | 203 | 4071 | 86 % |
| Uusimaa | 216 | 51 | 4450 | 81 % |
| Varsinais-Suomi | 322 | 124 | 3791 | 72 % |
| Pirkanmaa | 515 | 117 | 3046 | 81 % |
| Pohjanmaa | 507 | 118 | 2678 | 81 % |
| Keski-Pohjanmaa | 851 | 94 | 1866 | 90 % |
| Etelä-Savo | 350 | 69 | 2268 | 84 % |
| Kymenlaakso | 275 | 66 | 1864 | 81 % |
| Etelä-Karjala | 208 | 257 | 1173 | 45 % |
| Satakunta | 188 | 54 | 1097 | 78 % |
| Päijät-Häme | 86 | 9 | 1144 | 91 % |
| Kanta-Häme | 81 | 10 | 690 | 89 % |

### Hälytyksen syy (+6 h, vanha määritelmä)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 9091 | 36767 |
| tiesääennuste (Digitraffic) | 9245 | 21707 |
| märkä tie jäätyy | 3450 | 6578 |
| lumisade | 5861 | 3959 |
| jäätävä sade | 184 | 296 |

### Ohi menneet: mitä asema mittasi (+6 h, vanha määritelmä)

| Havainto | Kpl |
|---|---|
| keli jää | 3281 |
| kitka < 0,45 | 906 |
| varoitus häly | 719 |
| keli lumi | 641 |
| jäätä tiellä | 360 |
| keli kuura | 79 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kitkatotuus = kuinka usein tie oli samalla hetkellä kitkan mukaan liukas (vain tunnit, joilla on kitkamittaus). Vertailuna aseman keli kuura, Kuura-varoitus (kuuraava tilanne: tie kastepisteen alapuolella) ja vanha havaintomääritelmä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja, joilla kitka | Liukasta (kitkatotuus) | Tunteja kaikkiaan | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta (vanha) |
|---|---|---|---|---|---|---|
| 0–0,5 | 28912 | 5739 (20 %) | 56887 | 0 (0 %) | 4239 (7 %) | 5929 (10 %) |
| 0,5–2 | 6872 | 1135 (17 %) | 13362 | 0 (0 %) | 2970 (22 %) | 1364 (10 %) |
| 2–4 | 4722 | 864 (18 %) | 10092 | 0 (0 %) | 2065 (20 %) | 1032 (10 %) |
| 4–8 | 4938 | 879 (18 %) | 11099 | 2 (0 %) | 2165 (20 %) | 969 (9 %) |
| yli 8 | 6551 | 1642 (25 %) | 17729 | 732 (4 %) | 2629 (15 %) | 1503 (8 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä kitkatotuuden mukaan (suluissa vanha määritelmä, kaikki tunnit). "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja, joilla kitka | liukasta | Ei suolaa: tunteja, joilla kitka | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 12160 | 29 % (32 % / 13608) | 19941 | 32 % (37 % / 25565) |
| −4…−2 | 2210 | 22 % (21 % / 2501) | 4508 | 37 % (42 % / 5918) |
| −6…−4 | 324 | 39 % (34 % / 349) | 1269 | 63 % (60 % / 1671) |
| −8…−6 | 32 | 59 % (43 % / 47) | 579 | 68 % (63 % / 778) |
| alle −8 | 0 | – (0 % / 25) | 837 | 89 % (80 % / 972) |

## Ennuste vs. urakoiden suolaukset

Toteumat (Harjan suolauskirjaukset 2 km säteellä asemasta) 37 päivältä, 17228 asemavuorokautta. Ennuste hälytti = indeksi ≥ 50 jollakin ennustepituudella vuorokauden aikana. Urakka suolasi = suolauskerta vuorokauden aikana tai 6 h sen jälkeen.

| | Asemavuorokausia | Joista asema mittasi liukasta |
|---|---|---|
| Ennuste hälytti ja urakka suolasi | 5142 | 1862 |
| Vain urakka suolasi | 364 | 13 |
| Vain ennuste hälytti | 5660 | 1731 |
| Kumpikaan ei | 6062 | 76 |

Suolauskertoja 6514: ennuste hälytti 0–12 h ennen 5714 kertaa (88 %), keskimäärin 7,6 h ennen suolausta. Asema oli mitannut liukasta jo ennen suolausta (12 h sisällä) 2167 kertaa (33 %).
Liukkaista asemavuorokausista 3682: suolattu ennen ensimmäistä liukasta mittausta 1091, vasta sen jälkeen (6 h sisällä) 544.

### Urakoittain

| Urakka | Asemavrk | Molemmat | Vain suolaus | Vain ennuste | Suolauskertoja | Ennuste ennakoi | Liukasta jo ennen suolausta |
|---|---|---|---|---|---|---|---|
| tuntematon | 3162 | 702 | 129 | 1044 | 923 | 726 | 195 |
| Oulu | 518 | 249 | 28 | 148 | 256 | 199 | 99 |
| Kuopio | 407 | 182 | 12 | 90 | 271 | 240 | 124 |
| Raahe/Ylivieska | 324 | 148 | 7 | 91 | 197 | 182 | 106 |
| Kajaani | 296 | 171 | 0 | 63 | 225 | 214 | 83 |
| Kemi | 290 | 102 | 2 | 141 | 126 | 121 | 58 |
| Lapua | 333 | 151 | 16 | 86 | 177 | 149 | 81 |
| Kittilä | 288 | 0 | 0 | 260 | 0 | 0 | 0 |
| Salo | 407 | 123 | 1 | 104 | 147 | 130 | 21 |
| Seinäjoki | 280 | 116 | 2 | 81 | 153 | 148 | 73 |
| Kotka | 370 | 69 | 6 | 119 | 110 | 99 | 26 |
| Tampere | 334 | 88 | 13 | 79 | 145 | 124 | 37 |
| Ivalo | 222 | 1 | 0 | 210 | 1 | 1 | 0 |
| Espoo 19-24 | 499 | 105 | 14 | 72 | 131 | 115 | 21 |
| Joensuu | 257 | 85 | 8 | 84 | 111 | 89 | 40 |
| Pudasjärvi-Taivalkoski | 185 | 71 | 1 | 99 | 92 | 88 | 32 |
| Nummi | 333 | 103 | 8 | 66 | 119 | 106 | 13 |
| Kristiinankaupunki | 259 | 104 | 2 | 65 | 116 | 105 | 34 |
| Paimio | 333 | 85 | 4 | 73 | 97 | 83 | 8 |
| Kuusamo | 185 | 37 | 1 | 122 | 43 | 42 | 37 |
| Lappeenranta | 222 | 64 | 5 | 62 | 99 | 91 | 35 |
| Orivesi | 213 | 85 | 1 | 35 | 121 | 110 | 42 |
| Veteli | 185 | 69 | 1 | 69 | 87 | 83 | 52 |
| Kemijärvi-Posio | 163 | 15 | 0 | 136 | 16 | 16 | 7 |
| Pori | 222 | 66 | 3 | 46 | 104 | 84 | 34 |
| Hyvinkää | 259 | 69 | 4 | 61 | 85 | 75 | 14 |
| Nurmes | 185 | 63 | 0 | 88 | 58 | 55 | 29 |
| Mikkeli | 211 | 69 | 0 | 61 | 84 | 82 | 27 |
| Äänekoski | 185 | 69 | 0 | 55 | 87 | 82 | 51 |
| Sodankylä | 148 | 0 | 0 | 141 | 0 | 0 | 0 |
| Lahti | 222 | 78 | 5 | 44 | 96 | 83 | 17 |
| Vaasa | 148 | 58 | 4 | 44 | 91 | 75 | 23 |
| Suonenjoki | 148 | 54 | 1 | 57 | 75 | 71 | 40 |
| E18 Muurla-Lohja | 222 | 77 | 1 | 43 | 84 | 69 | 2 |
| Rovaniemi | 111 | 40 | 1 | 58 | 65 | 59 | 20 |
| Kitee | 174 | 66 | 8 | 45 | 74 | 58 | 21 |
| Raisio | 222 | 75 | 9 | 39 | 79 | 59 | 15 |
| Viinijärvi | 148 | 47 | 0 | 59 | 57 | 53 | 30 |
| Pyhäjärvi | 111 | 56 | 1 | 29 | 87 | 80 | 40 |
| Porvoo | 220 | 48 | 3 | 55 | 60 | 51 | 13 |
| Jyväskylä | 259 | 74 | 18 | 24 | 90 | 67 | 4 |
| Suomussalmi | 118 | 23 | 0 | 84 | 24 | 22 | 11 |
| Juva | 148 | 40 | 1 | 51 | 52 | 48 | 15 |
| Kauhajoki | 111 | 43 | 1 | 36 | 63 | 63 | 30 |
| Kouvola | 148 | 41 | 3 | 39 | 57 | 48 | 13 |
| Pihtipudas | 111 | 46 | 0 | 33 | 61 | 58 | 34 |
| Kokkola | 111 | 50 | 0 | 36 | 57 | 55 | 38 |
| Lieto | 185 | 62 | 6 | 32 | 60 | 50 | 5 |
| Koskenkylä -Kotka | 148 | 33 | 4 | 30 | 60 | 49 | 11 |
| Ii | 111 | 33 | 2 | 57 | 33 | 30 | 19 |
| Jämsä | 148 | 33 | 0 | 53 | 34 | 32 | 9 |
| Alavus | 101 | 59 | 1 | 23 | 63 | 60 | 22 |
| Puolanka | 111 | 16 | 0 | 70 | 14 | 14 | 8 |
| Pieksämäki | 111 | 32 | 0 | 46 | 34 | 34 | 13 |
| Siikalatva | 80 | 49 | 1 | 16 | 64 | 57 | 38 |
| Virrat | 111 | 43 | 1 | 29 | 49 | 44 | 14 |
| Savonlinna | 100 | 38 | 1 | 25 | 52 | 49 | 23 |
| Raasepori | 185 | 37 | 4 | 39 | 37 | 29 | 1 |
| Hamina-Vaalimaa | 111 | 22 | 1 | 35 | 37 | 36 | 13 |
| Rovaniemi 17-22 | 74 | 24 | 1 | 43 | 29 | 28 | 11 |
| Karstula | 74 | 31 | 0 | 23 | 48 | 46 | 33 |
| Imatra | 111 | 32 | 0 | 31 | 38 | 37 | 13 |
| Pello | 67 | 18 | 0 | 46 | 21 | 21 | 14 |
| Kuhmo | 74 | 13 | 0 | 48 | 15 | 15 | 9 |
| Mäntsälä | 111 | 30 | 0 | 25 | 36 | 30 | 5 |
| Nilsiä | 74 | 31 | 0 | 26 | 34 | 32 | 22 |
| Ilomantsi | 74 | 13 | 0 | 46 | 12 | 12 | 1 |
| Keuruu | 72 | 25 | 1 | 26 | 29 | 26 | 16 |
| Kangasala | 74 | 25 | 5 | 11 | 43 | 34 | 14 |
| Iisalmi | 74 | 36 | 1 | 18 | 36 | 35 | 19 |
| Parkano | 74 | 26 | 0 | 18 | 34 | 33 | 21 |
| Espoo | 111 | 28 | 1 | 16 | 35 | 27 | 4 |
| Harjavalta | 74 | 17 | 0 | 27 | 22 | 20 | 6 |
| Heinola | 74 | 21 | 2 | 22 | 27 | 26 | 7 |
| Merikarvia | 74 | 23 | 0 | 13 | 35 | 31 | 12 |
| Hämeenlinna | 74 | 18 | 2 | 16 | 23 | 20 | 5 |
| Huittinen | 74 | 19 | 0 | 18 | 18 | 18 | 3 |
| Pielavesi | 37 | 12 | 0 | 18 | 17 | 17 | 11 |
| Ranua | 37 | 11 | 0 | 22 | 10 | 9 | 4 |
| Vantaa | 63 | 14 | 5 | 11 | 17 | 13 | 2 |
| Kankaanpää | 37 | 11 | 1 | 13 | 15 | 13 | 7 |
| Kiuruvesi | 37 | 11 | 0 | 17 | 9 | 8 | 2 |
| Sastamala | 37 | 10 | 0 | 12 | 12 | 12 | 3 |
| Loimaa | 37 | 9 | 0 | 12 | 9 | 9 | 2 |

Suolausvertailun "asema mittasi liukasta" käyttää vielä vanhaa havaintomääritelmää.

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0).
