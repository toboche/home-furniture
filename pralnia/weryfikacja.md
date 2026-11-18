# Pralnia: lista do weryfikacji przed zamówieniem (stan 2026-11-18, model v63)

Źródła: model 3D (`index.html` albo `wyniki/pralnia_3d.html`), `wyniki/formatki.csv` (41 pozycji, 53 sztuki, 15,38 m²), `wyniki/kalkulator_nawierty.csv` (32 typy, 366 wierszy), `wyniki/arkusz_nawiertow.pdf` (32 strony), `wyniki/podsumowanie.json`, `pomiary.md`, `ustalenia.md`, `komponenty.md`, audyt `audyt/v1.md`.
Kontrola automatyczna: 424 otwory, 58 połączeń, 0 kolizji otworów; 154 konfirmaty, 14 kołków, 12 podpórek, 15 puszek. Kolizje brył: tylko zamierzone (puszki w frontach, magnesy w gniazdach, gniazdko GN1 w wycięciu).

## Zamówienie
- Koszyk 21386928 (2 970,11 zł, 2026-11-08) jest NIEAKTUALNY i nie należy go używać.
- Wycena wstępna 2026-11-15: rozkrój 21629244 (stan v58, bez nawiertów) = 2 204,10 zł; z wierceniem szacunkowo 2 850–2 950 zł. Od tego czasu: +RDW2, +LF6, −F8, KT1 124 mm. Do przeliczenia.
- Kalkulator przyjął przy wycenie wymiary z połówką mm i formatki 100 mm. KP1 zamawiamy jako 200×129 (skracana samodzielnie). Do sprawdzenia przy wpisie: nawierty Ø3×12.

## Do dopracowania / potwierdzenia
1. F6: zaprojektowane v62 (LF6 + kątownik 40×40, wkręty 12 mm). Przy montażu sprawdzić, czy prowadniki 173H7130 mieszczą się w strefie x 1500–1545 (wymiar przyjęty, nie z karty Blum).
2. Pion: zmierzone U = 1371–1373 (v63: tył kolumny zwężony, luz 3–5 mm). Opcjonalnie: Q (gzyms przy maszynach) – 118 nie zgadza się z U.
3. Montaż prawego dołu: skręcony na podłodze i wsunięty w całości (konfirmaty PP1 → PB2/PT2 od spodu). Prześwit nad gzymsem 22 mm.
4. Odkurzacz bezprzewodowy w L1: mocowanie (bez UTRUSTA). Wysokość i podparcie L1P.

## Pomiary weryfikacyjne
- V; A i G w kilku punktach; J w kilku punktach (także nad otworem wentylacyjnym).
- GN1 (środek), GN3/GN4 i wysunięcie wtyczek; zawór ZW (wysięg); GP1/GP2.
- Pion ścian i poziom podłogi; listwy przypodłogowe; droga transportu (L1B1/L1B2 1743×655).

## Uwagi konstrukcyjne (stałe)
- Moduły lewy, wnęka i kolumna stykają się (0 mm), bez dodatkowych luzów: składać na sucho przed dokręceniem.
- Luzy: lewa ściana 5 mm, prawa 3 mm, tył 3–5, sufit 9 (korpusy do 2652). Maszyny: 3 mm z lewej, 5 z prawej, można je przesuwać (ok. 4 mm po bokach).
- Montaż L1 jako ostatni; gniazdo GN3/GN4 natynkowe (15 mm) koliduje z L1B2 przy wsuwaniu – zdjąć na czas montażu albo złożyć L1 na miejscu.
- Model 3D nie był oglądany wizualnie przez Claude (brak biblioteki w środowisku): proszę obejrzeć warstwy „Kątowniki pod KT1" (nowe podpory), „Dodatki" (kuweta we wnęce), RDW2, kanał i kratkę.

## Do osobnego PR w `wspolne/` (audyt v1, Sekcja C)
- `otwory.py`: kontrola kolizji otworów lico A – lico B (suma głębokości > grubości lub przelot) i krawędź–krawędź prostopadle, promień wycięć wokół pilotów Ø5×5.
- `arkusz_pdf.py`: opis średnic/głębokości wg rzeczywistych otworów (nie stałe „Ø4, 35 mm"), piloty Ø3×12 i Ø5×5 nie jako „pod podpórki".
