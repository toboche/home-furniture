# Kuchnia: pomiary (mm)

Kody tylko dużymi literami. Przy ponownym pomiarze: nowa wartość w WARTOŚĆ, poprzednia do WCZEŚNIEJ / UWAGI,
potem zmiana w `model.js` i `python3 wspolne/pipeline/run.py kuchnia`.

Układ pomiarów: ściana główna (z płytkami, zlewem i płytą) = ściana tylna (z = 0); ściana lewa = ściana wnęki
przy słupku z piekarnikiem (x = 0); ścianka = prostopadły pion po prawej (koniec blatu, x = A).
Y od podłogi w górę; wysokości w szafkach liczone też od górnej krawędzi płytek (Y = C + D).
Pomiary z 2026-11-12 i 2026-11-13 (rozmowa z Claude, zdjęcia kuchni).

## Pokój i istniejąca kuchnia
| KOD | WARTOŚĆ | OPIS | WCZEŚNIEJ / UWAGI |
|---|---|---|---|
| A | 3208 | długość ściany głównej, narożnik ze ścianą lewą → ścianka | |
| B | 2665 | podłoga → sufit | orientacyjnie, sufit nierówny; do obliczeń C + D + M = 2680 |
| C | 911 | wysokość górnej powierzchni blatu | |
| D | 600 | pas płytek: blat → górna krawędź płytek | |
| E | 257 | ścianka → prawa krawędź płyty grzewczej | |
| F | 590 | szerokość płyty grzewczej | |
| H | 754 | blat → dno szafek górnych nad wnęką | szczelina nad płytkami H − D = 154 |
| I | 624 | narożnik → przednia krawędź boku szafek górnych nad wnęką, wzdłuż ściany głównej | |
| J | 805 | szerokość wnęki: narożnik → bok słupka, wzdłuż ściany lewej | 628 (pomyłka przy pierwszym pomiarze, poprawione 2026-11-13) |
| K | 629 | głębokość blatu na ścianie głównej | |
| L | 657 | głębokość ścianki: ściana główna → czoło ścianki | |
| M | 1169 | góra płytek → sufit, stałe na całej szerokości szafek | |

## Instalacje
| KOD | WARTOŚĆ | OPIS | WCZEŚNIEJ / UWAGI |
|---|---|---|---|
| LED | – | kabel LED 24 V, lewy górny róg wnęki przy słupku | przesuwny, zaplanowany na wysokości półki; włącznik w home automation |
| ZA1 | 356 | przewód zasilający okap (ściana główna): od ścianki | |
| ZA2 | 487 | przewód zasilający okap: od sufitu | 682 nad płytkami |
| RU1 | 125 | rura okapu w ściance (wychodzi poziomo ze ścianki): średnica wewnętrzna | zewnętrzna 130 (pierwszy odczyt 130 był po zewnętrznej stronie) |
| RU2 | 32 | rura okapu: ściana główna → najbliższy punkt rury (po zewnętrznej) | oś 32 + 65 = 97 |
| RU3 | 38 | rura okapu: sufit → najbliższy punkt rury (po zewnętrznej) | oś 38 + 65 = 103 pod sufitem |
| KR1 | 125 | otwór wentylacji grawitacyjnej w ściance: średnica wewnętrzna | zewnętrzna 130; kratka, nie zasłaniać, otworu nie da się przesunąć |
| KR2 | 323 | otwór: ściana główna → najbliższy punkt (po zewnętrznej) | |
| KR3 | 175 | otwór: sufit → najbliższy punkt (po zewnętrznej) | |
| KR4 | 15 | wysięg ramki kratki poza otwór (w stronę ściany głównej) | do projektu 20 (zapas): wolne od ściany głównej do 303 |

## Okap Ciarko Design DUO 55 (instrukcja Uno/Duo i rysunek techniczny DUO 55)
| KOD | WARTOŚĆ | OPIS | WCZEŚNIEJ / UWAGI |
|---|---|---|---|
| OK1 | 514 | szerokość korpusu okapu (A w instrukcji) | rysunek techniczny 513 |
| OK2 | 250 | głębokość korpusu | rysunek techniczny 253 |
| OK3 | 263 | wysokość korpusu | rysunek techniczny 265 |
| OK4 | 550 × 290 | szkło / ramka na dole | |
| OK5 | 150 | wylot (średnica), wyśrodkowany na szerokości | 93 od tyłu korpusu do krawędzi wylotu |
| OK6 | 516 | wymagana szerokość wewnętrzna szafki (A + 2) | |
| OK7 | 450 | minimalna odległość od płyty indukcyjnej | gaz 650 |
