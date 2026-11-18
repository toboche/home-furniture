# Garderoba: okucia i elementy (stan 2026-11-18, po audycie v1)
Wymiary w mm. Kody tylko dużymi literami. Płyty: `wyniki/formatki.csv` (18 mm, 19 pozycji / 28 sztuk / 20,0 m²)
i `wyniki/formatki_16mm.csv` (skrzynki szuflad, 6 pozycji / 10 sztuk / 1,51 m²); nawierty: `wyniki/kalkulator_nawierty*.csv`.

## Zawiasy i TIP-ON (fronty górne F1, F2: chowane, bez uchwytów)
Kody katalogowe Blum według audytu v1 i katalogu; przed zakupem potwierdzić u sprzedawcy (kolor i dostępność).
| Pozycja | Kod Blum | Ilość | Uwagi |
|---|---|---|---|
| Zawias CLIP top 110°, front wpuszczany, BEZ sprężyny, puszka na wkręty | 70T3750.TL | 4 | TIP-ON wymaga zawiasów bez sprężyny; F1 po lewej (NB-1), F2 po prawej (NB-2); puszka Ø35, 22,5 od krawędzi, 100 od końców frontu |
| Prowadnik krzyżakowy CLIP 0 mm, na wkręty | 173L6100 (albo 173H7100 / 175H7100) | 4 | NIE prowadnik prosty: wkręty w pionie ±16 (32); linia wkrętów 56,5 od przedniej krawędzi boku (37 + front 18 + 1,5, katalog Blum dla frontów wpuszczanych); nawierty pilotowe Ø3 × 12 w `kalkulator_nawierty.csv` |
| Wkręty do płyty Ø3,5 × 15 | 609.1500 | 8 | do prowadników |
| Ogranicznik kąta otwarcia 86° | 70T3553 | 2 | F2 (na oba zawiasy): przy 110° front oparłby się o prawą ścianę (dotyka przy ok. 92°). Ogranicznika 95° w katalogu nie ma |
| TIP-ON do drzwi, wersja krótka z magnesem (z płytkami do frontu: klejoną i wkręcaną) | 956.1004 | 2 | po stronie przeciwnej do zawiasów, czyli na przegrodzie NP, przy górze frontu |
| Adapter prosty do TIP-ON, wersja krótka | 956.1201 | 2 | przy frontach wpuszczanych cofnięty o 22 + grubość frontu = 40 od przedniej krawędzi NP |

UWAGA NP (18): adaptery F1 i F2 wkręca się w tę samą płytę z dwóch stron; wkręty 15 z obu stron spotkałyby się w środku.
Adaptery montujemy na różnych wysokościach (różnica co najmniej 30 w osi Y) albo wkrętami 3,5 × 13.
Szczelina wokół F1, F2 to SZCZ = 3: zawias 70T3750.TL z prowadnikiem 0 mm daje ok. 1,5–2 nominalnie, więc 3 zużywa ok. 1–1,5
z regulacji bocznej ±2 (zostaje ok. 0,5–1). Do decyzji: zostawić 3, zmniejszyć do 2 albo prowadnik z dystansem (patrz `ustalenia.md`).

## Szuflady: Blum MOVENTO do TIP-ON BLUMOTION (kryte prowadnice, pełny wysuw, otwieranie naciśnięciem)
| Pozycja | Kod Blum | Ilość | Uwagi |
|---|---|---|---|
| MOVENTO BLUMOTION S, 40 kg, NL 500 | 760H5000S | 1 kpl. (L+P) | SZ1 (N, połowa lewa); LW 531,5; za frontem 542 (min. NL + 7 = 507) |
| MOVENTO BLUMOTION S, 40 kg, NL 600 | 760H6000S | 1 kpl. (L+P) | SZ2 (L, wysuw w stronę pokoju); LW 859; za frontem 664 (min. 607). NL 650 jest tylko w serii 766H z jednostką L5 (min. 35 kg), dlatego 600 |
| TIP-ON BLUMOTION do MOVENTO, jednostka L1 (do 20 kg, NL 350–600) | T60L7340 | 2 kpl. | SZ1 i SZ2 (czapki, rękawiczki). Przy obciążeniu SZ2 ponad 20 kg: L3 T60L7540 (15–40 kg) |
| Zaczepy frontu MOVENTO z regulacją boczną (L+P) | T51.7601 | 2 kpl. | pod dnem skrzynki z przodu; otwory wg wzornika T65.1000.02 |
| Adaptery synchronizacji TIP-ON BLUMOTION | T60.1125W | 2 kpl. | SZ1, SZ2 |
| Wałek synchronizacji (do docięcia) | T60.000D | 2 | długość wg instrukcji Blum dla LW 531,5 i 859 (audyt: LW − 267 = 264,5 i 592; do potwierdzenia) |

Skrzynki według katalogu Blum (bok 16): szerokość wewnętrzna = LW − 42 (489,5 i 817), długość = NL − 10 (490 i 590),
dno wpuszczone 13, prześwit pod skrzynką 16, wysokość boków 180 (najwyżej przedział 208 − 23 = 185).
Wariant Blum „bez podcięć”: czoło i tył stoją na dnie, dno sięga do końca boków, więc pod dnem jest wolne 13 na całej
szerokości (TIP-ON BLUMOTION wymaga podcięć tyłu min. 125). Haki prowadnic: 2 otwory Ø6 × 10 w TYLNEJ KRAWĘDZI DNA,
7 nad spodem dna (20 nad dolną krawędzią boków), 11 od wewnętrznego lica boków (wzornik Blum).
Kontrola otwierania: `node garderoba/sprawdz_szuflady.js`. Każda szuflada sama: brak kolizji. SZ1 i SZ2 razem: kolizja
(narożnik), nie otwierać obu naraz.

## Złącza i pozostałe
| Pozycja | Ilość | Uwagi |
|---|---|---|
| Konfirmaty 7 × 50 | 224 | N 120, L 68, skrzynki 36; + zapas |
| Zaślepki konfirmatów | ok. 12 | widoczne łby: przegroda NP (6) i półki nad osłonami przewodów (6). Skrypt podaje 72, bo nie widzi, że łby na zewnętrznych licach LB1 i LB2 (50) zasłania pion i ściana, a łby pod dnami skrzynek (10) są niewidoczne; poprawka skryptu w osobnym PR `wspolne/` (audyt v1, sekcja C) |
| Drążki Ø25 z uchwytami | 3 | N połowa lewa 531,5, N połowa prawa 531,5, L wzdłuż ściany 859; oś 2037 |
| Wkręty i kołki do ściany (przez plecy NT i LT) | – | rodzaj zależy od ścian (do ustalenia) |
| Kratka wentylacyjna prostokątna nasuwana na przewód Ø130 | 1 | na wewnętrznym licu LB1; otwór w LB1 wierci użytkownik |
