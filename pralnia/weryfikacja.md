# Pralnia: lista do weryfikacji przed zamówieniem (stan 2026-11-19, model v67)

Źródła: model 3D (`index.html` albo `wyniki/pralnia_3d.html`), `wyniki/formatki.csv` (44 pozycje, 56 sztuk, 16,67 m²), `wyniki/kalkulator_nawierty.csv` (32 typy, 370 wierszy), `wyniki/arkusz_nawiertow.pdf` (32 strony), `wyniki/podsumowanie.json`, `pomiary.md`, `ustalenia.md`, `komponenty.md`, audyt `audyt/v1.md`.
Kontrola automatyczna: 428 otworów, 58 połączeń, 0 kolizji otworów; 154 konfirmaty, 14 kołków, 12 podpórek, 21 puszek. Kolizje brył: tylko zamierzone (puszki w frontach, magnesy w gniazdach, gniazdko GN1 w wycięciu).

## Zamówienie
- Koszyk 21386928 (2 970,11 zł, 2026-11-08) jest NIEAKTUALNY i nie należy go używać.
- Wycena wstępna 2026-11-15: rozkrój 21629244 (stan v58, bez nawiertów) = 2 204,10 zł; z wierceniem szacunkowo 2 850–2 950 zł. Od tego czasu: +RDW2, +LF6, +F10, pasy +3 mm, KT1 124 mm, L1B 637. Do złożenia od nowa (zamowienie.md).
- Kalkulator przyjął przy wycenie wymiary z połówką mm i formatki 100 mm. KP1 zamawiamy jako 200×129 (skracana samodzielnie). Do sprawdzenia przy wpisie: nawierty Ø3×12.

## Do dopracowania / potwierdzenia
1. F6: zaprojektowane v62 (LF6 + kątownik 40×40, wkręty 12 mm). Przy montażu sprawdzić, czy prowadniki 173H7130 mieszczą się w strefie x 1500–1545 (wymiar przyjęty, nie z karty Blum).
2. Pion: zmierzone U = 1371–1373 (v63: tył kolumny zwężony, luz 3–5 mm). Opcjonalnie: Q (gzyms przy maszynach) – 118 nie zgadza się z U.
3. Montaż prawego dołu: skręcony na podłodze i wsunięty w całości (konfirmaty PP1 → PB2/PT2 od spodu). Prześwit nad gzymsem 22 mm.
4. Odkurzacz bezprzewodowy w L1: mocowanie (bez UTRUSTA). Wysokość L1P (619 × 572, na 4 podpórkach).
5. Audyt v2 – rozstrzygnięte 2026-11-19: piloty zostają Ø3 × 12; PB2/PB3 przykręcone do prawej ściany (gzyms g-k); wieniec dolny L1WD zamówiony luzem.
6. Przy zamówieniu: oś X strony „Tył (B)” w kalkulatorze, pozycje 3 puszek F9 (zamowienie.md).

## Pomiary kontrolne (czy zabudowa się zmieści) – lista z 2026-11-18, WYKONANE 2026-11-18: wszystkie OK
Mierzyć w mm, w kilku miejscach; liczy się najgorszy wynik (najmniejsza szerokość, najniższy sufit, najbardziej wystający punkt).
| KOD | CO I GDZIE | MODEL | DOBRY WYNIK |
|---|---|---|---|
| A | lewa ↔ prawa ściana: wys. ok. 0,1 / 1,0 / 1,7 / 2,6 m, przy tylnej ścianie i ok. 0,65 m od niej | 1739 | ≥ 1735 (1733–1734: na styk; < 1733: do zmiany) |
| B | lewa ściana → lewy bok maszyn (najbardziej wystający punkt) | 618 | ≥ 616 |
| BP | prawa ściana → prawy bok maszyn (najbardziej wystający punkt) | 523 | ≥ 519 |
| C | szerokość maszyn w najszerszym miejscu | 598 | ≤ 604 |
| U | lewa ściana → lewy bok pionu | 1371 | ≥ 1369 (zmierzone 1371–1373: OK) |
| GZ1 | lewa ściana → lewy bok gzymsu na prawej ścianie | 1666 | ≥ 1665 |
| J | sufit: nad całą zabudową i ok. 0,5 m przed frontami | 2660 | ≥ 2658 (szafki do 2655; zmierzone min. 2661, przyjęte 2660: OK) |
| H | najwyższy punkt suszarki (z zestawem łączącym) | 1713 | ≤ 1738 |
| X | najwyższy punkt gzymsu na pionie | 467 | ≤ 486 (zmierzone 467: OK) |
| GZ3 | najwyższy punkt gzymsu na prawej ścianie | 466 | ≤ 486 |
| PD | różnica poziomu podłogi pod L1 (x 0–0,62 m) i pod prawym dołem (x 1,22–1,74 m) | 0 | ≤ 3 (podkładki) |
| V | tylna ściana → przód pionu, wys. 0,5 / 1,5 / 2,5 m | 362 | ≤ 365 |
| GZ2 | tylna ściana → przód gzymsu na pionie | 435 | ≤ 438 |
| TS | tylna ściana za L1/L2 i nad maszynami: odchyłka od płaszczyzny | 0 | ≤ 3 |
| E | tylna ściana → przód maszyn (drzwiczki) | 658 | ≤ 658 (więcej: maszyny wystają przed fronty) |
| GN1 | gniazdko w L1: krawędzie od podłogi / od tylnej ściany | 878–958 / 202–282 | dół ≥ 873, góra ≤ 963, tył ≥ 197, przód ≤ 287 |
| GN3 | gniazdko przy L1: tylna krawędź od tylnej ściany | 665 | ≥ 660 |
| ZW | zawór z pokrętłem: wysięg od tylnej ściany; wysokość | 160; 777–837 | wysięg ≤ 162; wysokość w 515–910 |
| GP | gniazdka za maszynami z wtyczkami: wysięg; wysokość | 60; 977–1037 | wysięg ≤ 162; wysokość w 948–1343 |
| WN | środek otworu wentylacyjnego: od prawej ściany / od sufitu | 115 / 243 | ± 2 (zmierzone: OK) |
Transport: największe płyty L1B1/L1B2 1743 × 637 – drzwi 805 × 2016 OK; sprawdzić korytarz i zakręty.

## Uwagi konstrukcyjne (stałe)
- Moduły lewy, wnęka i kolumna stykają się (0 mm), bez dodatkowych luzów: składać na sucho przed dokręceniem.
- Luzy: lewa ściana 5 mm, prawa 3 mm, tył 3–5, sufit 5 (korpusy do 2655, J = 2660). Maszyny: 3 mm z lewej, 5 z prawej, można je przesuwać (ok. 4 mm po bokach).
- Montaż L1 jako ostatni; gniazdo GN3/GN4 natynkowe (15 mm) koliduje z L1B2 przy wsuwaniu – zdjąć na czas montażu albo złożyć L1 na miejscu.
- Model 3D nie był oglądany wizualnie przez Claude (brak biblioteki w środowisku): proszę obejrzeć warstwy „Kątowniki pod KT1" (nowe podpory), „Dodatki" (kuweta we wnęce), RDW2, kanał i kratkę.

## Do osobnego PR w `wspolne/` (audyt v1, Sekcja C)
- `otwory.py`: kontrola kolizji otworów lico A – lico B (suma głębokości > grubości lub przelot) i krawędź–krawędź prostopadle, promień wycięć wokół pilotów Ø5×5.
- `kalkulator.py`: udokumentować/sprawdzić układ współrzędnych strony „Tył” względem kalkulatora meble.pl; spójne zaokrąglanie połówkowych współrzędnych par kołków.
- `arkusz_pdf.py`: opis średnic/głębokości wg rzeczywistych otworów (nie stałe „Ø4, 35 mm"), piloty Ø3×12 i Ø5×5 nie jako „pod podpórki".
