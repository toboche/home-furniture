# Garderoba: przekazanie do zamówienia (stan 2026-11-19)

Dla rozmowy, w której składane jest zamówienie (garderoba razem z innym pomieszczeniem). Wymiary w mm, kody tylko DUŻYMI LITERAMI.
Źródło prawdy: repozytorium na `main` (`CLAUDE.md`). Dokumenty w projekcie Claude mogą być starymi kopiami.
Wymiary szafek są POTWIERDZONE w pomieszczeniu (2026-11-18 i 2026-11-19, `weryfikacja.md`). Zmiana wymiaru tylko przez `model.js`
i przeliczenie (`python3 wspolne/pipeline/run.py garderoba`), nigdy ręcznie w plikach z `wyniki/`.

## 1. Pliki
| Plik | Zawartość |
|---|---|
| `wyniki/formatki.csv` | płyta 18 mm: 30 pozycji / 45 sztuk / 21,87 m² (w tym blendy BL1–BL3) (kod, nazwa, DL, SZ, SZT, OKLEINA, NAWIERTY, UWAGI) |
| `wyniki/formatki_16mm.csv` | płyta 16 mm na skrzynki szuflad: 6 pozycji / 10 sztuk / 1,52 m², bez okleiny |
| `wyniki/kalkulator_nawierty.csv`, `wyniki/kalkulator_nawierty_16mm.csv` | nawierty w formacie kalkulatora centrum.meble.pl (14 typów formatek, 195 wierszy dla 18 mm) |
| `wyniki/arkusz_nawiertow.pdf` | rysunki wszystkich formatek z otworami (dla innego dostawcy albo do sprawdzenia) |
| `komponenty.md` | okucia z kodami Blum, złącza, drążki, kątowniki, magnesy |
| `ustalenia.md` | decyzje (sekcje z 2026-11-19 są najnowsze) |

## 2. Płyta
- 18 mm: Egger U702 ST9 Kaszmir (decyzja 2026-11-19, wcześniej W1200 ST9 Biały porcelanowy). Okleina ABS 0,8 i laser 1 mm
  na frontach w dekorze U702. Jeśli zamówienie idzie
  do innego dostawcy albo w innym dekorze, ustalić to w rozmowie o zamówieniu; wymiary formatek się nie zmieniają.
- 16 mm (skrzynki S1, S2): U702 ST9 16 mm, jeśli kalkulator ją ma; jeśli nie, pokazać użytkownikowi dostępne płyty 16 mm
  (skrzynki są wewnątrz szafek; wcześniej zgoda na inną białą). Skrzynki muszą mieć
  16 (Blum MOVENTO: bok najwyżej 16), nie zamieniać na 18.
- Rozkrój 21629487 w meble.pl (2026-11-15) jest NIEAKTUALNY: zmieniły się prawie wszystkie wymiary. Złożyć nowy.

## 3. Okleina
- Kolumna OKLEINA w `formatki.csv`: korpusy ABS 0,8, fronty F1–F4 dookoła (2DL+2SZ, w pralni laser 1 mm).
- `kalkulator_nawierty.csv` ma tylko krawędź PRZEDNIĄ (kolumna OKLEJ KRAWEDZ NR). Ręcznie dopisać DOLNE krawędzie
  stojące na kafelkach, w numeracji kalkulatora (1 góra, 2 prawa, 3 dół, 4 lewa, przy SZEROKOŚĆ = DL, WYSOKOŚĆ = SZ):
  | Formatka | Krawędź przednia (z CSV) | Dolna (dopisać) |
  |---|---|---|
  | NB-1, NB-2 | 1 | 4 |
  | NP | 1 | 4 |
  | LB2 | 1 | 2 |
  | LB1 (nie ma jej w kalkulator_nawierty.csv, bez otworów) | jedna długa krawędź | jedna krótka krawędź |
  | NO-1, NO-2 (nie ma ich w kalkulator_nawierty.csv) | brak | 3 |
- Bez okleiny: plecy NT, LT, GNT, GLT i skrzynki szuflad (16 mm).

## 4. Nawierty
- FORMATKI Z NAWIERTAMI WPISUJ WEDŁUG `kalkulator_nawierty.csv`, NIE według `formatki.csv`: jeden wiersz z LP = jedna
  formatka w kalkulatorze, kolumna KODY = elementy o identycznych nawiertach (np. NS-1, NS-2, NS-3, NK razem; NS-4, NS-5 osobno,
  bo mają konfirmaty przesunięte o 25; NW z GNG). Formatki bez nawiertów dodać z `formatki.csv`: NO-1, NO-2, F1–F4 oraz cały
  korpus dolny L poza LB2 (LB1, LT, LW, LK, LS-1..3), korpus górny GL poza GLB1 (GLB2, GLD, GLG, GLT) i blendy BL1–BL3: oba składane na miejscu
  na łącznikach od środka, bez konfirmatów. LB2 i GLB1 mają tylko nawierty środków (gniazdko, przewód wentylacyjny).
  Liczba pozycji w kalkulatorze będzie inna niż 30; zgadzać się mają sztuki (45) i m² (21,87).
- Wszystkie formatki mają poniżej 2500 mm (najdłuższa 2120), więc kalkulator meble.pl przyjmie nawierty dla wszystkich;
  wszystkie współrzędne są w pełnych mm.
- Fronty F1, F2 (530 × 422, zawiasy na krawędzi 422): szablon zawiasów Blum INSERTA (F1 LEWY, F2 PRAWY), 2 puszki Ø35,
  środek 22,5 od krawędzi, środki puszek 100 i 322 od dolnej krawędzi frontu. Zawiasy 70T3790.TL (INSERTA, bez sprężyny):
  w kalkulatorze wybrać wariant INSERTA (puszka Ø35 × 13 + 2 × Ø8 co 45), NIE wariant na wkręty.
  F3, F4: bez nawiertów.
- Nawierty pilotowe Ø3 × 12 pod prowadniki zawiasów: w GNB-1 i GNB-2 (są w CSV). Jeśli kalkulator nie przyjmie Ø3,
  pominąć je (użytkownik wywierci sam); Ø4 za słabo trzyma wkręt 3,5.
- Nawierty środków Ø5 × 5 pod otwory wiercone przez użytkownika otwornicą: GLB1 (przewód wentylacyjny Ø130, otwór ok. Ø135)
  i LB2 (gniazdko). Same otwory robi użytkownik. Przewód wentylacyjny skrócony do 3 przed GLB1, z kratką łączy go tuleja.
- Skrzynki szuflad, robi użytkownik wzornikiem Blum T65.1000.02 (nie ma ich w CSV): otwory pod zaczepy T51.7601 pod dnem
  z przodu oraz 2 otwory Ø6 × 10 pod haki prowadnic w TYLNEJ KRAWĘDZI dna S1D i S2D (7 nad spodem dna, 11 od wewnętrznego
  lica boków). Kalkulator meble.pl wierci w krawędzi tylko w osi grubości (8 zamiast 7), dlatego lepiej wzornikiem.

## 5. Obróbka poza standardem (zgłosić dostawcy albo zrobić samemu)
- LB1: wycięcie dolnego narożnika po stronie ściany lewej (krawędź tylna, przeciwna do oklejonej przedniej):
  184 wzdłuż dolnej krawędzi × 335 w górę (wokół gzymsu i rury).
- LB2: to samo wycięcie 129 × 335 (wokół gzymsu). Otwór na gniazdko (środek 210 od ściany lewej i 195 od podłogi, wg nawiertu
  środka) wierci użytkownik: ok. Ø66–68 pod pierścień dystansowy gniazda wpuszczanego, po przymiarce nad puszką w ścianie
  (`ustalenia.md`); w zamówieniu tylko nawiert środka Ø5 × 5.
- Pozostałe formatki są prostokątami.

## 6. Okucia i drobne elementy
Pełna lista z kodami: `komponenty.md`. W skrócie: 4 zawiasy 70T3790.TL (INSERTA) + 4 prowadniki 173L6100 + 8 wkrętów 609.1500,
4 ograniczniki 86° 70T3553 (F1 i F2), 2 TIP-ON 956.1004 + 2 adaptery 956.1201, MOVENTO 760H5000S i 760H6000S z TIP-ON BLUMOTION
T60L7340 (L1), zaczepy T51.7601, adaptery T60.000D (w komplecie) i 1 wałek T60.1125W (docięty na 267 i 609); konfirmaty 7 × 50: 117 + zapas (korpusy N, GN) i 5 × 40: 34 + zapas (skrzynki); ok. 55 łączników narożnych do korpusów
L i GL i 220–260 wkrętów 3,5 × 15 do nich; zaślepki ok. 6;
3 drążki Ø25 (534, 534, 876); 4 kątowniki i 4 zatrzaski magnetyczne do osłon NO; wkręty 4 × 30 (ok. 10) łączące korpusy
górne z dolnymi; kratka wentylacyjna; mocowanie do ścian do ustalenia.

## 7. Pułapki
- BLENDY BL1–BL3 (dodatek 2026-11-22, nie ma ich w modelu 3D ani w plikach nawiertów, są w `formatki.csv`): pasy 60 mm
  z tej samej płyty 18 mm, BEZ okleiny, bez nawiertów, po 3 szt.: BL1 2120 × 60, BL2 480 × 60, BL3 1150 × 60. W kalkulatorze
  nazwy GD-BL1, GD-BL2, GD-BL3. Jeśli kalkulator nie przyjmie szerokości 60, zapytać użytkownika.
- Skrzynki szuflad: otwory Ø5 pod konfirmaty 5 × 40 trzeba po dostawie pogłębić stożkowo (łeb równo z płytą), inaczej
  łby pod dnem zmniejszą prześwit MOVENTO.
- Płyta 16 mm innego producenta: sprawdzić u dostawcy minimalne wymiary formatki z nawiertami (S1C, S2C mają 151 szerokości).
- Kalkulator: po wpisaniu nawiertów obejrzeć podgląd 2D strony „Tył (B)”, czy otwory nie są odbite względem
  `arkusz_nawiertow.pdf`. Formatki z otworami na stronie „Tył”: 18 mm NB-1, NP, NT, GNB-1, GNB-2, GND, GNT, LB2;
  16 mm S1B-1, S1D, S2B-1, S2D.
- `wyniki/podsumowanie.json` podaje 16 zaślepek: skrypt liczy też łby pod dnami skrzynek (10), których nie widać. Kupić ok. 6
  (`komponenty.md`). Poprawka czeka na osobny PR w `wspolne/`.
- Korpusy: każda szafka to korpus dolny (0–2120: N, L) i górny (2120–2582: GN, GL). Kody GN… i GL… to formatki korpusów
  górnych, nie pomyłka.
- Szafka na wprost ma 1122 szerokości (połowy 534); wcześniejsze dokumenty mogą mieć 1116 albo 1117.
- Po złożeniu zamówienia porównać liczbę pozycji, sztuk i m² z punktem 1 i wpisać numer rozkroju i cenę do `ustalenia.md`.
