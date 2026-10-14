# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v9) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 1 (2026-10-12 – 2026-10-12), laskentoja 5370. Päivitetty 2026-10-14T20:50:26Z.

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly tai kuura, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Ennuste "liukas" = indeksi ≥ 50.

## Osumatarkkuus

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 340 | 131 | 358 | 4538 | 72 % | 51 % |
| +6 h | 518 | 302 | 683 | 3862 | 63 % | 57 % |
| +12 h | 495 | 196 | 1201 | 3473 | 72 % | 71 % |

## Maakunnittain (+6 h)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 120 | 24 | 201 | 83 % |
| Pohjois-Pohjanmaa | 119 | 73 | 124 | 62 % |
| Finavia lentokentät | 47 | 82 | 58 | 36 % |
| Kainuu | 57 | 28 | 54 | 67 % |
| Etelä-Pohjanmaa | 36 | 8 | 73 | 82 % |
| Pohjanmaa | 40 | 1 | 66 | 98 % |
| Pohjois-Savo | 33 | 41 | 7 | 45 % |
| Keski-Pohjanmaa | 43 | 3 | 25 | 93 % |
| Keski-Suomi | 15 | 10 | 23 | 60 % |
| Pohjois-Karjala | 7 | 6 | 32 | 54 % |
| Pirkanmaa | 0 | 25 | 4 | 0 % |
| Satakunta | 1 | 1 | 13 | 50 % |
| Etelä-Savo | 0 | 0 | 3 | – % |

## Hälytyksen syy (+6 h, indeksi ≥ 50)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 371 | 418 |
| tiesääennuste (Digitraffic) | 90 | 170 |
| märkä tie jäätyy | 56 | 95 |
| lumisade | 1 | 0 |

## Ohi menneet: mitä asema mittasi (+6 h)

| Havainto | Kpl |
|---|---|
| varoitus kuura | 256 |
| keli jää | 32 |
| varoitus häly | 12 |
| keli lumi | 2 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kuinka usein asema mittasi kuuraa (keli kuura tai kuuravaroitus) tai liukasta samalla hetkellä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja | Kuuraa | Liukasta |
|---|---|---|---|
| 0–0,5 | 1305 | 131 (10 %) | 156 (12 %) |
| 0,5–2 | 88 | 65 (74 %) | 74 (84 %) |
| 2–4 | 41 | 27 (66 %) | 35 (85 %) |
| 4–8 | 24 | 10 (42 %) | 16 (67 %) |
| yli 8 | 13 | 5 (38 %) | 13 (100 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä. "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja | liukasta | Ei suolaa: tunteja | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 2 | 100 % | 118 | 62 % |
| −4…−2 | 2 | 0 % | 78 | 64 % |
| −6…−4 | 0 | – | 5 | 80 % |

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0). Säännöt: Sambbor/Vantaakeli, collector/collect.mjs.
