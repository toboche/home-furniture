# Pralnia: przekazanie do zamówienia (stan 2026-11-19, model v69)

Dla rozmowy, w której składane jest zamówienie (pralnia razem z innym pomieszczeniem). Wymiary w mm, kody tylko DUŻYMI LITERAMI.
Źródło prawdy: repozytorium na `main` (`CLAUDE.md`). Dokumenty w projekcie Claude mogą być starymi kopiami.
Wymiary są POTWIERDZONE pomiarami kontrolnymi w pomieszczeniu (2026-11-18, `weryfikacja.md`). Zmiana wymiaru tylko przez
`model.js` / `reguly.py` i przeliczenie (`python3 wspolne/pipeline/run.py pralnia`), nigdy ręcznie w plikach z `wyniki/`.

## 1. Pliki
| Plik | Zawartość |
|---|---|
| `wyniki/formatki.csv` | płyta 18 mm: 44 pozycje / 56 sztuk / 16,69 m² (KOD, NAZWA, DL, SZ, SZT, OKLEINA, NAWIERTY, UWAGI) |
| `wyniki/kalkulator_nawierty.csv` | nawierty w formacie kalkulatora centrum.meble.pl: 32 typy formatek, 370 wierszy |
| `wyniki/arkusz_nawiertow.pdf` | rysunki formatek z otworami (32 strony; dla innego dostawcy albo do sprawdzenia) |
| `komponenty.md` | okucia z kodami Blum, złącza, kątowniki, magnesy, uchwyty |
| `ustalenia.md` | decyzje (sekcje z 2026-11-18 są najnowsze) |

## 2. Płyta
- Wszystko z jednej płyty: Egger W1200 ST9 Biały porcelanowy 18 mm (centrum.meble.pl, format 2070 × 2800). Jeśli drugie
  pomieszczenie ma ten sam dekor, wspólny rozkrój zmniejszy liczbę arkuszy.
- Przy wspólnym zamówieniu dodać prefiks do kodów (np. `PR-F1`, `PR-KB2`), bo kody powtarzają się między pomieszczeniami
  (`wspolne/zasady.md`).
- Rozkroje 21386928 (koszyk z 2026-11-08) i 21629244 (wycena z 2026-11-15) są NIEAKTUALNE. Złożyć nowy.

## 3. Okleina
- Kolumna OKLEINA w `formatki.csv`: `1DL` (jedna długa krawędź, przód), `1SZ` (jedna krótka), `2DL+2SZ` (dookoła), pusta = bez okleiny.
- Fronty F1–F10: okleina 1,0 mm bezspoinowa (laser) dookoła. Reszta: ABS 0,8 mm.
- `kalkulator_nawierty.csv` podaje numer oklejanej krawędzi (kolumna OKLEJ KRAWEDZ NR; `brak` = bez okleiny).
- Import CSV w meble.pl (2026-11-15) NIE przenosi okleiny: po wczytaniu formatek ustawić krawędzie ręcznie i sprawdzić.
- Bez okleiny: plecy (L1T, L2T, NWT, PT1–PT3, KT1A/B/C, KT2), półki tylne kolumny KP1–KP3, listwa LF6.

## 4. Nawierty
- Formatki korpusu: szablon „Wręgowanie i nawierty”, dane z `kalkulator_nawierty.csv`.
  - Lico: Ø5 przelotowo pod konfirmaty (użytkownik poszerza do Ø7 po dostawie).
  - Czoło: Ø4 × 35 pod konfirmaty, Ø8 × 20 pod kołki.
  - Ø5 × 10 pod podpórki półek (KB2, PB2).
  - Ø3 × 12 piloty pod prowadniki zawiasów (30 szt.). Jeśli kalkulator nie przyjmie Ø3 × 12: NIE zamieniać na Ø4 (wkręt 3,5 by nie trzymał) – usunąć te piloty z zamówienia (użytkownik nawierci Ø2–2,5 ręcznie).
  - Ø5 × 5 nawierty środków (PT3, L1B2).
- Wymiary z połówką mm (F5 274,5; F6 236,5; F8 493,5; F9 1240,5; fronty pasa 454,5): kalkulator przyjął takie wartości przy wycenie 2026-11-15.
- KP1: kalkulator nie przyjmuje formatek < 200 mm. Wpisać 200 × 126 (zamiast 184 × 126) i X otworów w krawędzi 3 powiększyć o 16
  (66 i 150); naddatek 16 mm po stronie krawędzi 4 (tył, bez otworów) użytkownik odcina sam.
- Minimalna formatka: przy wycenie 2026-11-15 kalkulator podał 199,8 × 59,8 mm (dla oklejanej); audyt v2 podaje 240 × 100. LF6 (200 × 60, bez okleiny) nie był testowany – jeśli kalkulator go odrzuci, zamówić 240 × 100 bez nawiertów, a konfirmaty i docięcie zrobić samemu (pozycje otworów: arkusz_nawiertow.pdf).
- PP3-2 ma inne nawierty niż PP3-1 i PP3-3 (konfirmaty do LF6): w kalkulatorze osobna formatka.
- Strona „Tył (B)”: przed wpisaniem wszystkich otworów sprawdzić na podglądzie 2D jednej formatki (np. PB2), czy kalkulator nie odbija osi X dla otworów od tyłu. Jeśli odbija – zatrzymać się i ustalić to z użytkownikiem.
- F10: 4 puszki na 100 / 612 / 1125 / 1637 od dołu (szablon Front prawy) – sprawdzić na podglądzie.
- Ułamkowe współrzędne otworów (ok. 80 wierszy z .1–.9 mm w kalkulator_nawierty.csv): sprawdzić, że kalkulator je przyjmuje; jeśli zaokrągla, różnica < 0,5 mm jest bez znaczenia.
- F9: sprawdzić na podglądzie, że szablon stawia 3 puszki na 100 / 620 / 1140,5 od dołu (prowadniki w PB2 są pod te pozycje); jeśli szablon ustawia je inaczej – wpisać pozycje ręcznie.
- Bez nawiertów: KT1A/B/C (zdejmowane, na kątownikach i magnesach), L1P (półka luzem), L1WD (wieniec zapasowy, luzem), F6 (front stały).
- Fronty (szablon „Wręgowanie i nawierty” niedostępny przy okleinie bezspoinowej, więc szablony zawiasów): zawiasy Blum INSERTA,
  puszka Ø35, środek 22,5 mm od krawędzi. Środki puszek od dolnej krawędzi frontu:
  | Front | Szablon | Puszki | Środki od dołu |
  |---|---|---|---|
  | F1, F2 | Front lewy | 2 | 100; 354,5 |
  | F3, F4, F5, F7 | Front prawy | 2 | 100; 354,5 |
  | F8 (zapasowy) | Front prawy | 2 | 100; 393,5 |
  | F9 | Front prawy | 3 | 100; 620; 1140,5 |
  | F10 (zapasowy, L1) | Front prawy | 4 | 100; 612; 1125; 1637 |
  | F6 | brak (otwór Ø127 robi użytkownik) | – | – |

## 5. Obróbka poza standardem (robi użytkownik)
- L1B2: wycięcie 100 × 100 pod gniazdko GN1 (od dołu 868–968, od tylnej krawędzi formatki 189–289, środek 918 / 239), nawiert środka ze sklepu.
- F6: otwór Ø127 otwornicą, środek 126 od lewej i 217,5 od dolnej krawędzi (237 od górnej); nawiertu środka sklep nie zrobi.
- PT3: otwór Ø127 pod rurę Ø125, środek 255 od lewej i 237 od górnej (nawiert środka ze sklepu; wiercić wg rzeczywistego położenia rury).
- KP1: skrócenie z 200 do 184.
- KT1A/B/C: gniazda Ø10 × 3 pod magnesy. Uchwyty GUBBARP: otwory we frontach.

## 6. Okucia i drobne elementy
Pełna lista z kodami: `komponenty.md`. W skrócie:
- Zawiasy Blum: 71B3590 – 13 sztuk plus 6 na zapas (F8, F10); 79B9590 – 2 (F5 na F6).
- Prowadniki: 173H7100 – 13 plus 6 na zapas; 173H7130 – 2.
- Wkręty do prowadników: 609.1500, ok. 40 sztuk.
- Ograniczniki 70T3553: 9 plus 2 do F8.
- Złącza: konfirmaty 7 × 50 – 154 plus zapas, zaślepki ok. 27, kołki Ø8 × 40 – 14, podpórki Ø5 – 16 (12 pod PP2/KP2 + 4 pod L1P).
- Kątowniki: 25 × 25 – 12, 40 × 40 – 1.
- Magnesy Ø10 × 3: 6.
- Uchwyty GUBBARP: 9 (w tym 2 na zapas).
- Mocowanie do ścian: 8 × kołek Ø8 + wkręt 6×80 do betonu (NW ×4, L1 ×2, L2 ×2), 4 × kołek do pustaków (PB2 ×2, PB3 ×2), twarde dystanse 3/5 mm.
- Pasy do dolnych szafek: 8 wkrętów 4 × 40 (od góry, przez dolną półkę pasa).
- Pozostałe: wkręty 3,5 × 12/15/30, kanał Ø125, podkładki poziomujące, podkładka 23 mm pod PP1.

## 7. Pułapki
- F8 i F10 to fronty NA ZAPAS (kuweta stoi we wnęce F8, L1 może zostać otwarta), ale są w zamówieniu z puszkami. Dla F8 są też
  nawierty prowadników w PB1; dla F10 celowo NIE ma nawiertów w L1B1.
- Szerokości z 2026-11-19 (v69): lewa szafka 612 (fronty F1, F2, F10 609), tył kolumny 121–126, prawa część szersza o 2 mm (F6 236,5, F7 i F9 514). Starsze dokumenty mają 607 / 124–132 / 512.
- Boki L1B1, L1B2 mają głębokość 637 (nie 655 jak w starszych dokumentach) – z przodu miejsce na F10.
- Pas (L2, wnęka nad maszynami, prawy pas) ma 912 wysokości (nie 909), fronty pasa 454,5 (nie 453).
- `wyniki/podsumowanie.json`: 26 widocznych łbów konfirmatów; 8 z nich jest w wąskich szczelinach (patrz `komponenty.md`), zaślepki ok. 27.
- Po złożeniu zamówienia porównać liczbę pozycji, sztuk i m² z punktem 1 i wpisać numer rozkroju i cenę do `ustalenia.md`.
