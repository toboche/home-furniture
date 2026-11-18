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
| RU4 | 115 | rura okapu wystaje ze ścianki (koniec na X 3093, w wąskiej szafce) | zmierzone 2026-11-18 |
| PL1 | 9–12 | płytki wystają przed ścianę nad nimi (ryflowane) | zmierzone 2026-11-18; w modelu wcześniej 8 |
| KR1 | 125 | otwór wentylacji grawitacyjnej w ściance: średnica wewnętrzna | zewnętrzna 130; kratka, nie zasłaniać, otworu nie da się przesunąć |
| KR2 | 323 | otwór: ściana główna → najbliższy punkt (po zewnętrznej) | |
| KR3 | 175 | otwór: sufit → najbliższy punkt (po zewnętrznej) | |
| KR4 | 15 | wysięg ramki kratki poza otwór (w stronę ściany głównej) | do projektu 20 (zapas): wolne od ściany głównej do 303 |

## Okap Ciarko Design DUO 55 (instrukcja Uno/Duo i rysunek techniczny DUO 55)
| KOD | WARTOŚĆ | OPIS | WCZEŚNIEJ / UWAGI |
|---|---|---|---|
| OK1 | 513 | szerokość korpusu okapu (rysunek, potwierdzone na okapie 2026-11-18) | 514 (A w instrukcji); zmiana 2026-11-16 |
| OK2 | 253 | głębokość korpusu (rysunek techniczny) | 250; zmiana 2026-11-16 |
| OK3 | 265 | wysokość korpusu (rysunek techniczny) | 263; zmiana 2026-11-16 |
| OK4 | 551 × 290 × 1,5 | kołnierz (ramka ze szkłem) na dole, widoczny od spodu: dno szafki; grubość 1,5 zmierzona na okapie | 550 × 290 (instrukcja); 551 z rysunku 2026-11-16; grubość w modelu 4 do 2026-11-18 |
| OK5 | 150 | wylot (średnica), wyśrodkowany na szerokości; 94 od tylnej krawędzi kołnierza do krawędzi wylotu | zmierzone 2026-11-18; wcześniej 94 od tyłu korpusu (rysunek), 93 (instrukcja) |
| OK6 | 516 | wymagana szerokość wewnętrzna szafki (A + 2) | |
| OK8 | 19 / 18,5 | wysięg kołnierza poza korpus: z boków (551 − 513) / 2, z przodu i z tyłu (290 − 253) / 2 | kołnierz na środku (użytkownik, 2026-11-16) |
| OK9 | 26 | wysokość króćca wylotu ponad korpus (okap, 2026-11-18) | |
| OK10 | 35 / 215, 81 | otwory montażowe w boku korpusu: od przodu korpusu (bez kołnierza); 81 nad dołem korpusu; 2 na bok | potwierdzone na okapie 2026-11-18 |
| OK11 | 148,5 | średnica zewnętrzna króćca wylotu; rura nachodzi na króciec | zmierzone 2026-11-18 |
| OK7 | 450 | minimalna odległość od płyty indukcyjnej | gaz 650 |
