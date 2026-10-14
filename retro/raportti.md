# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v10) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 1 (2026-10-12 – 2026-10-12), laskentoja 5370. Päivitetty 2026-10-14T21:00:19Z.

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Ennuste "liukas" = indeksi ≥ 50.

## Osumatarkkuus

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 75 | 21 | 538 | 4733 | 78 % | 88 % |
| +6 h | 111 | 46 | 1090 | 4118 | 71 % | 91 % |
| +12 h | 113 | 23 | 1583 | 3646 | 83 % | 93 % |

## Maakunnittain (+6 h)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 31 | 5 | 290 | 86 % |
| Pohjois-Pohjanmaa | 21 | 7 | 222 | 75 % |
| Finavia lentokentät | 12 | 18 | 93 | 40 % |
| Kainuu | 13 | 1 | 98 | 93 % |
| Etelä-Pohjanmaa | 0 | 0 | 109 | – % |
| Pohjanmaa | 19 | 0 | 87 | 100 % |
| Keski-Pohjanmaa | 1 | 0 | 67 | 100 % |
| Pohjois-Savo | 12 | 15 | 28 | 44 % |
| Pohjois-Karjala | 2 | 0 | 37 | 100 % |
| Keski-Suomi | 0 | 0 | 38 | – % |
| Satakunta | 0 | 0 | 14 | – % |
| Pirkanmaa | 0 | 0 | 4 | – % |
| Etelä-Savo | 0 | 0 | 3 | – % |

## Hälytyksen syy (+6 h, indeksi ≥ 50)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 93 | 696 |
| tiesääennuste (Digitraffic) | 9 | 251 |
| märkä tie jäätyy | 9 | 142 |
| lumisade | 0 | 1 |

## Ohi menneet: mitä asema mittasi (+6 h)

| Havainto | Kpl |
|---|---|
| keli jää | 32 |
| varoitus häly | 12 |
| keli lumi | 2 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kuinka usein asema mittasi kuuraa tiellä (keli kuura), antoi Kuura-varoituksen (kuuraava tilanne: tie kastepisteen alapuolella) tai mittasi liukasta samalla hetkellä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta |
|---|---|---|---|---|
| 0–0,5 | 1305 | 0 (0 %) | 131 (10 %) | 25 (2 %) |
| 0,5–2 | 88 | 0 (0 %) | 65 (74 %) | 9 (10 %) |
| 2–4 | 41 | 0 (0 %) | 27 (66 %) | 9 (22 %) |
| 4–8 | 24 | 0 (0 %) | 10 (42 %) | 6 (25 %) |
| yli 8 | 13 | 5 (38 %) | 0 (0 %) | 13 (100 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä. "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja | liukasta | Ei suolaa: tunteja | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 2 | 100 % | 119 | 18 % |
| −4…−2 | 2 | 0 % | 78 | 15 % |
| −6…−4 | 0 | – | 5 | 20 % |

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0). Säännöt: Sambbor/Vantaakeli, collector/collect.mjs.
