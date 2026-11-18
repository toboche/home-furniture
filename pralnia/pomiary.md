# Pralnia: pomiary (mm)

Zmierzone wymiary pokoju, maszyn i instalacji. Decyzje projektowe są w `ustalenia.md`.
Kody tylko dużymi literami. Przy ponownym pomiarze: nowa wartość w kolumnie WARTOŚĆ, poprzednia do WCZEŚNIEJ,
potem zmiana w `model.js` i `python3 wspolne/pipeline/run.py pralnia`.

Układ: X od lewej ściany ku prawej, Y od podłogi w górę, Z od tylnej ściany ku wejściu.

## Pokój
| KOD | WARTOŚĆ | OPIS | WCZEŚNIEJ / UWAGI |
|---|---|---|---|
| A | 1739 | szerokość pokoju od ściany do ściany, najmniejsza, przyjęta w projekcie | najszerszy punkt 1744; prawa ściana: odchyłki 2-3 mm |
| G | 1497 | głębokość pokoju | |
| J | 2660 | wysokość przyjęta w projekcie: najniższy punkt 2661 (jedno miejsce, lewy przedni róg przy lewej ścianie), przyjęte 1 mm mniej (pomiar kontrolny 2026-11-18) | 2661, 2665; korpusy i fronty do 2652, luz 8 mm |
| – | 823 / 805 / 2016 | otwór wejściowy: od lewej ściany / szerokość / wysokość | drzwi otwierają się na zewnątrz |

## Pion, gzyms (obudowa przewodów od podłogi), wywiew
| KOD | WARTOŚĆ | OPIS | WCZEŚNIEJ / UWAGI |
|---|---|---|---|
| U | 1371–1373 | od lewej ściany do lewego boku pionu, na różnych wysokościach (pomiar 2026-11-18); w modelu 1371 | 1372, 1379; model wcześniej 1376 |
| P | 371 | szerokość pionu | |
| V | 362 | wysięg pionu od tylnej ściany | podane 0,362 m |
| Q | 118 | gzyms po stronie maszyn | przy U = 1371 i krawędzi gzymsu 1258 (maszyny do 1216 + R 42) wychodzi 113 – do sprawdzenia, nie wpływa na szafki |
| X | 467 | najwyższy punkt gzymsu na pionie (pod PP1/KP1), pomiar 2026-11-18 | 489 |
| GZ1 | 73 | szerokość gzymsu na prawej ścianie | |
| GZ2 | 73 | szerokość gzymsu na froncie pionu | |
| GZ3 | 466 | wysokość gzymsu na prawej ścianie | |
| GZ4 | 680 | długość gzymsu na prawej ścianie, od frontu pionu | |
| D | 490 | od krawędzi gzymsu do prawej ściany | |
| WN1, WN2 | 115, 243 | środek otworu wentylacyjnego: od prawej ściany, od sufitu (pomiar 2026-11-18); w modelu x 1624, y 2418 (od sufitu nad otworem 2661) | wcześniej M, N = 121, 53 (niejasne), model x 1616, y 2409 |
| KR | 123 | kratka wentylacyjna (kupiona): króciec Ø123, wchodzi do rury Ø125 | |

## Maszyny (pralka Bosch WGG244EPL, suszarka Bosch WQG245DEPL, oryginalny zestaw łączący)
| KOD | WARTOŚĆ | OPIS | WCZEŚNIEJ / UWAGI |
|---|---|---|---|
| B | 618 | od lewej ściany do maszyn (maszyny równoległe do lewej ściany) | 619, 620, 623; potwierdzone na wysokości 0, 1 i 2 m |
| C | 598 | szerokość maszyn z kart produktów | zmierzone 584 (ryflowania obudowy) |
| E | 658 | głębokość maszyn z frontem | |
| H | 1713 | wysokość kolumny pralka + suszarka | |
| R | 42 | szczelina między prawym bokiem maszyn a gzymsem | |
| – | 530 | od maszyny do prawej ściany | 531-532; 2-3 mm różnicy wzdłuż ściany |
| – | 159 | szczelina maszyny–pion powyżej gzymsu (cała zasłonięta) | |

## Instalacje
| KOD | WARTOŚĆ | OPIS | WCZEŚNIEJ / UWAGI |
|---|---|---|---|
| GN1, GN2 | 202, 878 | gniazdko 1 na lewej ścianie: najbliższa krawędź od tylnej ściany, od podłogi | w środku lewej szafki |
| GN3, GN4 | 665, 179 | gniazdko 2 na lewej ścianie: najbliższa krawędź od tylnej ściany, od podłogi | 664; poza szafką; natynkowe, wysunięcie 15 |
| ZW1, ZW2 | 837, 160 | zawór: górna krawędź od podłogi, wysięg od tylnej ściany | wysięg z zapasem |
| GP1, GP2 | 1037, 60 | gniazdka za maszynami: najwyższy punkt, wysięg od tylnej ściany | |
| ZB1, ZB2, ZB3 | 160, 160, 1070 | zabudowa szczeliny nad gzymsem (zawór i gniazdka) | ZB3 wcześniej 1050 |

Ściany: tylna beton, boczne pustaki.
