# Garderoba: przekazanie do zamówienia (stan 2026-11-18)

Dla rozmowy, w której składane jest zamówienie (garderoba razem z innym pomieszczeniem). Wymiary w mm, kody tylko DUŻYMI LITERAMI.
Źródło prawdy: repozytorium na `main` (`CLAUDE.md`). Dokumenty w projekcie Claude mogą być starymi kopiami.
Wymiary szafek są POTWIERDZONE w pomieszczeniu (2026-11-18, `weryfikacja.md`). Zmiana wymiaru tylko przez `model.js`
i przeliczenie (`python3 wspolne/pipeline/run.py garderoba`), nigdy ręcznie w plikach z `wyniki/`.

## 1. Pliki
| Plik | Zawartość |
|---|---|
| `wyniki/formatki.csv` | płyta 18 mm: 27 pozycji / 36 sztuk / 21,17 m² (kod, nazwa, DL, SZ, SZT, OKLEINA, NAWIERTY, UWAGI) |
| `wyniki/formatki_16mm.csv` | płyta 16 mm na skrzynki szuflad: 6 pozycji / 10 sztuk / 1,52 m², bez okleiny |
| `wyniki/kalkulator_nawierty.csv`, `wyniki/kalkulator_nawierty_16mm.csv` | nawierty w formacie kalkulatora centrum.meble.pl (21 typów formatek, 317 wierszy dla 18 mm) |
| `wyniki/arkusz_nawiertow.pdf` | rysunki wszystkich formatek z otworami (dla innego dostawcy albo do sprawdzenia) |
| `komponenty.md` | okucia z kodami Blum, złącza, drążki, kątowniki, magnesy |
| `ustalenia.md` | decyzje (sekcje z 2026-11-18 są najnowsze) |

## 2. Płyta
- 18 mm: założony dekor jak w pralni, Egger W1200 ST9 Biały porcelanowy (`ustalenia.md`). Jeśli zamówienie idzie
  do innego dostawcy albo w innym dekorze, ustalić to w rozmowie o zamówieniu; wymiary formatek się nie zmieniają.
- 16 mm (skrzynki S1, S2): W1200 nie ma 16 mm, użytkownik zgodził się na INNĄ BIAŁĄ PŁYTĘ 16 mm. Skrzynki muszą mieć
  16 (Blum MOVENTO: bok najwyżej 16), nie zamieniać na 18.
- Rozkrój 21629487 w meble.pl (2026-11-15) jest NIEAKTUALNY: zmieniły się prawie wszystkie wymiary. Złożyć nowy.

## 3. Okleina
- Kolumna OKLEINA w `formatki.csv`: korpusy ABS 0,8, fronty F1–F4 dookoła (2DL+2SZ, w pralni laser 1 mm).
- `kalkulator_nawierty.csv` ma tylko krawędź PRZEDNIĄ (kolumna OKLEJ KRAWEDZ NR). Ręcznie dopisać DOLNE krawędzie
  stojące na kafelkach: NB (2 szt.), NP, LB1, LB2 (1SZ, dół) i NO (2 szt., 1DL, dół).
- Bez okleiny: plecy NT, LT, GNT, GLT i skrzynki szuflad (16 mm).

## 4. Nawierty
- Wszystkie formatki mają poniżej 2500 mm (najdłuższa 2120), więc kalkulator meble.pl przyjmie nawierty dla wszystkich;
  wszystkie współrzędne są w pełnych mm.
- Fronty F1, F2: szablon zawiasów Blum (F1 LEWY, F2 PRAWY), 2 puszki Ø35, środek 22,5 od krawędzi, 100 od końców frontu.
  F3, F4: bez nawiertów.
- Nawierty pilotowe Ø3 × 12 pod prowadniki zawiasów: w GNB-1 i GNB-2 (są w CSV).
- Nawierty środków Ø5 × 5 pod otwory wiercone przez użytkownika otwornicą: GLB1 (przewód wentylacyjny Ø130, otwór ok. Ø135)
  i LB2 (gniazdko). Same otwory robi użytkownik.
- Skrzynki szuflad, robi użytkownik wzornikiem Blum T65.1000.02 (nie ma ich w CSV): otwory pod zaczepy T51.7601 pod dnem
  z przodu oraz 2 otwory Ø6 × 10 pod haki prowadnic w TYLNEJ KRAWĘDZI dna S1D i S2D (7 nad spodem dna, 11 od wewnętrznego
  lica boków). Kalkulator meble.pl wierci w krawędzi tylko w osi grubości (8 zamiast 7), dlatego lepiej wzornikiem.

## 5. Obróbka poza standardem (zgłosić dostawcy albo zrobić samemu)
- LB1: wycięcie dolnego narożnika po stronie ściany lewej (krawędź tylna, przeciwna do oklejonej przedniej):
  184 wzdłuż dolnej krawędzi × 335 w górę (wokół gzymsu i rury).
- LB2: to samo wycięcie 129 × 335 (wokół gzymsu).
- Pozostałe formatki są prostokątami.

## 6. Okucia i drobne elementy
Pełna lista z kodami: `komponenty.md`. W skrócie: 4 zawiasy 70T3750.TL + 4 prowadniki 173L6100 + 8 wkrętów 609.1500,
2 ograniczniki 86° 70T3553 (F2), 2 TIP-ON 956.1004 + 2 adaptery 956.1201, MOVENTO 760H5000S i 760H6000S z TIP-ON BLUMOTION
T60L7340 (L1), zaczepy T51.7601, adaptery T60.1125W i wałki T60.000D; konfirmaty 7 × 50: 230 + zapas; zaślepki ok. 6;
3 drążki Ø25 (534, 534, 873); 4 kątowniki i 4 zatrzaski magnetyczne do osłon NO; wkręty 4 × 30 (ok. 10) łączące korpusy
górne z dolnymi; kratka wentylacyjna; mocowanie do ścian do ustalenia.

## 7. Pułapki
- `wyniki/podsumowanie.json` podaje 45 zaślepek: to błąd skryptu (nie widzi, że łby na LB1, LB2, GLB1, GLB2 zasłania ściana
  i pion). Kupić ok. 6 (`komponenty.md`). Poprawka czeka na osobny PR w `wspolne/`.
- Korpusy: każda szafka to korpus dolny (0–2120: N, L) i górny (2120–2582: GN, GL). Kody GN… i GL… to formatki korpusów
  górnych, nie pomyłka.
- Szafka na wprost ma 1122 szerokości (połowy 534); wcześniejsze dokumenty mogą mieć 1116 albo 1117.
- Po złożeniu zamówienia porównać liczbę pozycji, sztuk i m² z punktem 1 i wpisać numer rozkroju i cenę do `ustalenia.md`.
