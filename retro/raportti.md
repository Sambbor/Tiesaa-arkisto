# Jälkitarkistus koko Suomen aineistolla

Kelisivun liukkaussäännöt (v10) ajettuna jälkikäteen Tiesää-arkiston asemille. Päiviä 3 (2026-10-12 – 2026-10-14), laskentoja 27032. Päivitetty 2026-10-16T05:06:19Z.

Liukas havainto = aseman mittaus (keli kuura/lumi/jää/sohjo, varoitus häly, tai tienpinnan ollessa enintään +1 °C kitka < 0,45, jäätä tai lunta). Ennuste "liukas" = indeksi ≥ 50.

## Osumatarkkuus

| Ennuste | Osumat | Ohi | Turhat | Oikein ei riskiä | Havaitsemisosuus | Turhien osuus |
|---|---|---|---|---|---|---|
| +2 h | 427 | 51 | 2862 | 23658 | 89 % | 87 % |
| +6 h | 389 | 107 | 3692 | 22805 | 78 % | 90 % |
| +12 h | 383 | 79 | 5073 | 21451 | 83 % | 93 % |

## Maakunnittain (+6 h)

| Maakunta | Osumat | Ohi | Turhat | Havaitsemisosuus |
|---|---|---|---|---|
| Lappi | 191 | 9 | 992 | 96 % |
| Pohjois-Pohjanmaa | 77 | 21 | 758 | 79 % |
| Finavia lentokentät | 26 | 46 | 318 | 36 % |
| Kainuu | 32 | 4 | 295 | 89 % |
| Pohjois-Savo | 31 | 18 | 245 | 63 % |
| Pohjois-Karjala | 4 | 4 | 265 | 50 % |
| Etelä-Pohjanmaa | 0 | 0 | 219 | – % |
| Pohjanmaa | 27 | 0 | 152 | 100 % |
| Keski-Pohjanmaa | 1 | 1 | 162 | 50 % |
| Keski-Suomi | 0 | 0 | 156 | – % |
| Etelä-Savo | 0 | 0 | 52 | – % |
| Satakunta | 0 | 0 | 32 | – % |
| Etelä-Karjala | 0 | 4 | 21 | 0 % |
| Pirkanmaa | 0 | 0 | 23 | – % |
| Päijät-Häme | 0 | 0 | 2 | – % |

## Hälytyksen syy (+6 h, indeksi ≥ 50)

| Syy | Osui | Turha |
|---|---|---|
| kuura | 237 | 1883 |
| tiesääennuste (Digitraffic) | 52 | 1295 |
| märkä tie jäätyy | 25 | 289 |
| lumisade | 63 | 75 |
| jäätävä sade | 9 | 118 |
| lumi / sohjo | 3 | 32 |

## Ohi menneet: mitä asema mittasi (+6 h)

| Havainto | Kpl |
|---|---|
| keli jää | 64 |
| varoitus häly | 34 |
| keli lumi | 9 |

## Kuura kuurakertymän mukaan

Tienpinta enintään +0,5 °C eikä suolan suojaa. Kuinka usein asema mittasi kuuraa tiellä (keli kuura), antoi Kuura-varoituksen (kuuraava tilanne: tie kastepisteen alapuolella) tai mittasi liukasta samalla hetkellä. Kertymä 4 °C·h = sääntöjen raja "mahdollisesti liukas".

| Kertymä °C·h | Tunteja | Kuura tiellä (keli) | Kuuraava tilanne (varoitus) | Liukasta |
|---|---|---|---|---|
| 0–0,5 | 4706 | 0 (0 %) | 446 (9 %) | 163 (3 %) |
| 0,5–2 | 647 | 0 (0 %) | 336 (52 %) | 79 (12 %) |
| 2–4 | 400 | 0 (0 %) | 183 (46 %) | 74 (19 %) |
| 4–8 | 374 | 0 (0 %) | 144 (39 %) | 68 (18 %) |
| yli 8 | 242 | 15 (6 %) | 62 (26 %) | 86 (36 %) |

## Märkä tie pakkasella: suolan vaikutus

Liukasta 6 tunnin sisällä. "Suolaa" = jäätymispiste ≤ −1 °C. Sääntöjen oletus: suola pitää −6 °C:een asti.

| Tienpinta °C | Suolaa: tunteja | liukasta | Ei suolaa: tunteja | liukasta |
|---|---|---|---|---|
| −2…+0,5 | 121 | 7 % | 932 | 19 % |
| −4…−2 | 20 | 0 % | 292 | 21 % |
| −6…−4 | 0 | – | 39 | 21 % |
| −8…−6 | 0 | – | 1 | 0 % |
| alle −8 | 0 | – | 3 | 0 % |

Lähde: Fintraffic / Digitraffic ja Ilmatieteen laitos (CC BY 4.0). Säännöt: Sambbor/Vantaakeli, collector/collect.mjs.
