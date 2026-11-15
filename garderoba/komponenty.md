# Garderoba: okucia i elementy (stan 2026-11-15, konstrukcja)
Wymiary w mm. Kody tylko dużymi literami. Płyty: `wyniki/formatki.csv` (18 mm, 19 pozycji / 28 sztuk / 20,0 m²)
i `wyniki/formatki_16mm.csv` (skrzynki szuflad, 6 pozycji / 10 sztuk / 1,56 m²); nawierty: `wyniki/kalkulator_nawierty*.csv`.

## Zawiasy i TIP-ON (fronty górne F1, F2: chowane, bez uchwytów)
| Pozycja | Ilość | Uwagi |
|---|---|---|
| Blum CLIP top 110° do frontów chowanych (wpuszczanych), BEZ sprężyny | 4 | TIP-ON wymaga zawiasów bez sprężyny; F1 po lewej (NB-1), F2 po prawej (NB-2); puszka Ø35, 22,5 od krawędzi, 100 od końców frontu. Numer katalogowy do potwierdzenia |
| Prowadnik Blum CLIP prosty | 4 | linia wkrętów 55 od przedniej krawędzi boku (37 + grubość frontu; DO POTWIERDZENIA w katalogu dla frontów chowanych); nawierty pilotowe Ø3 × 12 w kalkulatorze |
| Blum TIP-ON do drzwi + adapter | 2 | po stronie przeciwnej do zawiasów, czyli na przegrodzie NP (z obu stron), przy górze frontu |
| Ogranicznik kąta otwarcia (np. 86° / 95°) | 1 | F2: przy 110° front oparłby się o prawą ścianę (dotyka przy ok. 92°) |

## Szuflady: Blum MOVENTO do TIP-ON BLUMOTION (kryte prowadnice, pełny wysuw, otwieranie naciśnięciem)
| Pozycja | Ilość | Uwagi |
|---|---|---|
| MOVENTO do TIP-ON BLUMOTION, NL 500 | 1 kpl. | SZ1 (N, połowa lewa); LW 531,5, głębokość wnętrza 542 (min. NL + 3 = 503) |
| MOVENTO do TIP-ON BLUMOTION, NL 650 | 1 kpl. | SZ2 (L, wysuw w stronę pokoju); LW 859, głębokość wnętrza 664 (min. 653) |
| TIP-ON BLUMOTION do MOVENTO, jednostka + zabierak | 2 kpl. | jednostka wg szerokości i ciężaru szuflady (katalog Blum) |
| Synchronizator TIP-ON BLUMOTION (wałek) | 2 | szerokość wnętrza 531,5 i 859 |
| Zaczepy / regulatory frontu MOVENTO | 2 kpl. | do skrzynek drewnianych, front chowany |

Skrzynki według katalogu Blum (bok 16): szerokość wewnętrzna = LW − 42 (489,5 i 817), długość = NL − 10 (490 i 640),
dno wpuszczone 13, prześwit pod skrzynką 16, wysokość boków 180 (najwyżej przedział 208 − 23 = 185), czoło i tył stoją na dnie.
Kontrola otwierania: `node garderoba/sprawdz_szuflady.js` (każda szuflada na pełny wysuw przy zamkniętej drugiej): brak kolizji.

## Złącza i pozostałe
| Pozycja | Ilość | Uwagi |
|---|---|---|
| Konfirmaty 7 × 50 | 224 | N 120, L 68, skrzynki 36; + zapas |
| Zaślepki konfirmatów | ok. 12 | widoczne łby: przegroda NP (6) i półki nad osłonami przewodów (6). Skrypt podaje 72, bo nie widzi, że łby na zewnętrznych licach LB1 i LB2 (50) zasłania pion i ściana, a łby pod dnami skrzynek (10) są niewidoczne |
| Drążki Ø25 z uchwytami | 3 | N połowa lewa 531,5, N połowa prawa 531,5, L wzdłuż ściany 859; oś 2037 |
| Wkręty i kołki do ściany (przez plecy NT i LT) | – | rodzaj zależy od ścian (do ustalenia) |
| Kratka wentylacyjna prostokątna nasuwana na przewód Ø130 | 1 | na wewnętrznym licu LB1; otwór w LB1 wierci użytkownik |
