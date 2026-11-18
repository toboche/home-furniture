# Pralnia: lista do weryfikacji przed zamówieniem (stan 2026-11-18, model v61)

Źródła: model 3D (`index.html` albo `wyniki/pralnia_3d.html`), `wyniki/formatki.csv` (40 pozycji, 52 sztuki, 15,38 m²), `wyniki/kalkulator_nawierty.csv` (30 typów, 354 wiersze), `wyniki/arkusz_nawiertow.pdf` (30 stron), `wyniki/podsumowanie.json`, `pomiary.md`, `ustalenia.md`, `komponenty.md`, audyt `audyt/v1.md`.
Kontrola automatyczna: 420 otworów, 57 połączeń, 0 kolizji otworów; 152 konfirmaty, 14 kołków, 12 podpórek, 15 puszek. Kolizje brył: tylko zamierzone (puszki w frontach, magnesy w gniazdach, gniazdko GN1 w wycięciu).

## Zamówienie
- Koszyk 21386928 (2 970,11 zł, 2026-11-08) jest NIEAKTUALNY i nie należy go używać.
- Wycena wstępna 2026-11-15: rozkrój 21629244 (stan v58, bez nawiertów) = 2 204,10 zł; z wierceniem szacunkowo 2 850–2 950 zł. Od tego czasu: +RDW2, −F8, KT1 124 mm. Do przeliczenia.
- Kalkulator przyjął przy wycenie wymiary z połówką mm i formatki 100 mm. KP1 zamawiamy jako 200×132 (skracana samodzielnie). Do sprawdzenia przy wpisie: nawierty Ø3×12.

## Do dopracowania / potwierdzenia
1. F6 (zostaje 79B9590 + 173H7130 na F6): listwa oporowa za F6 zamiast 2 małych kątowników przy x 1510, długość wkrętów w F6, ogranicznik na F3 (F3 otwarty ponad ok. 92° trafia w uchwyt F5).
2. Pion: U na 3 wysokościach i P (pomiary.md: U + P = 1743 > A = 1739; model pion od x 1376). Przy U = 1372 luz KT2/KP1/KP3 do pionu spada z 5 do 1 mm.
3. Wentylacja: wysokość sufitu nad otworem (przyjęto J = 2661 → y 2418); średnica otwornicy do F6 (przyjęto Ø127).
4. Montaż prawego dołu: skręcony na podłodze i wsunięty w całości (konfirmaty PP1 → PB2/PT2 od spodu). Prześwit nad gzymsem 22 mm.
5. Odkurzacz bezprzewodowy w L1: mocowanie (bez UTRUSTA). Wysokość i podparcie L1P.

## Pomiary weryfikacyjne
- Pion U (dół, środek, góra), P, V; A i G w kilku punktach; J w kilku punktach (także nad otworem wentylacyjnym).
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
