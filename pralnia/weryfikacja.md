# Pralnia: lista do weryfikacji przed zamówieniem (stan 2026-11-18, model v60)

Źródła: model 3D (`index.html` albo `wyniki/pralnia_3d.html`), `wyniki/formatki.csv` (41 pozycji, 53 sztuki, 15,60 m²), `wyniki/kalkulator_nawierty.csv` (30 typów, 358 wierszy), `wyniki/arkusz_nawiertow.pdf` (30 stron), `wyniki/podsumowanie.json`, `pomiary.md`, `ustalenia.md`, `komponenty.md`, audyt `audyt/v1.md`.
Kontrola automatyczna: 424 otwory, 57 połączeń, 0 kolizji otworów; 152 konfirmaty, 14 kołków, 12 podpórek, 17 puszek.

## Zamówienie
- Koszyk 21386928 (2 970,11 zł, 2026-11-08) jest NIEAKTUALNY i nie należy go używać.
- Wycena wstępna 2026-11-15: rozkrój 21629244 (formatki v58 bez nawiertów, KP1 jako 200×132) = 2 204,10 zł; z wierceniem szacunkowo 2 850–2 950 zł. Bez RDW2. Nie w koszyku.
- Przed zamówieniem sprawdzić w kalkulatorze: wymiary z połówką mm (KP2 130,5; PP2 477,5; F5 274,5; F6 234,5; F8 493,5; F9 1240,5 – przy wycenie 2026-11-15 przyjęte bez błędu), formatki 100 mm (L1W, RDW, RDW2 – przyjęte), KP1 184 < 200 (odrzucona), nawierty Ø3×12.

## Decyzje otwarte (audyt v1, Sekcja B i część A)
1. L1 / UTRUSTA (B1, P0): wymiary 356 × 1345 × 569 wg instrukcji IKEA, szyny przykręcane do dna (L1 nie ma dna), kolizja wysuwu z kuwetą w rogu i z wtyczkami GN1, GN3/GN4. Do decyzji: dno L1D, strona UTRUSTA (lewa/prawa), miejsce kuwety, głębokość i podparcie L1P.
2. Gzyms i pion (B2, P1): pomiary X (najwyższy punkt gzymsu pod PP1/KP1), U na 3 wysokościach, Q/D. Rozbieżność: pomiary.md U = 1372, P = 371 a model pion od x 1376, szer. 363 (gzyms od 1258). Od tego zależą: podniesienie poziomu 489 o 3 mm i luz KT2/KP1/KP3 (5 mm albo 1 mm). Kolejność montażu prawego dołu (konfirmaty PP1 → PB2/PT2 od spodu): moduł skręcany na podłodze i wsuwany w całości albo inne złącza.
3. F5 ↔ F6 (B3, P1): zostaje 79B9590 na F6 (wtedy wzmocnienie F6 listwą, krótsze wkręty, ogranicznik na F3) czy zawiasy F5 po lewej na KB3 (71B3590 + 173H7100)?
4. Wentylacja i kalkulator (B4): kratka – króciec Ø125 czy Ø150 (otwór w F6); ponowny pomiar środka otworu w ścianie (y 2409; M = 121, N = 53 niejasne).
5. KT1A/B/C (A2, P1): sposób mocowania (magnesy / zatrzaski / kątownik podpierający od dołu), luz na łby wkrętów kątowników (0,5 mm), luz KT1C pod RDW/RDW2 (0 mm) i KT1A/B pod podpórkami (1 mm).
6. Ograniczniki 86° (A1): F9 przy 86° – przekładanie półek PP2+KP2 wymaga wysunięcia i pochylenia albo wypięcia F9 z prowadników. Do akceptacji.
7. KP1 184×132: kalkulator nie przyjmuje formatki < 200 mm; zamówić 200 i skrócić samodzielnie, wyciąć z odpadu albo zmienić konstrukcję.
8. Luz między modułami 0 mm przy odchyłce prawej ściany 2–3 mm (P2): czy zostawić zapas 2–3 mm na wnęce NW (po pomiarach A na kilku wysokościach).

## Pomiary weryfikacyjne (przed decyzjami 1, 2, 4, 8)
- Gzyms X na całej szerokości (z 362–435 i przy kolumnie), U (dół, środek, góra), Q, D, P, V; A i G w kilku punktach; J w kilku punktach.
- GN1 (środek), GN3/GN4 i wysunięcie wtyczek; zawór ZW (wysięg z wtyczkami/kranem); GP1/GP2; środek otworu wentylacyjnego.
- Pion ścian i poziom podłogi; listwy przypodłogowe; droga transportu (L1B1/L1B2 1743×655).

## Uwagi konstrukcyjne (stałe)
- Moduły lewy, wnęka i kolumna stykają się (0 mm): składać na sucho przed dokręceniem.
- Luzy: lewa ściana 5 mm, prawa 3 mm, tył 3–5, sufit 9 (korpusy do 2652). Maszyny: 3 mm z lewej, 5 z prawej, można je przesuwać (ok. 4 mm po bokach).
- Montaż L1 jako ostatni; gniazdo GN3/GN4 natynkowe (15 mm) koliduje z L1B2 przy wsuwaniu – zdjąć na czas montażu albo złożyć L1 na miejscu.
- Model 3D nie był oglądany wizualnie przez Claude (brak biblioteki w środowisku): proszę obejrzeć warstwy „Konfirmaty", „Otwory", „Kołki", „Uchwyty", „Kątowniki pod KT1", „Kątowniki pod F6" i RDW2.

## Do osobnego PR w `wspolne/` (audyt v1, Sekcja C)
- `otwory.py`: kontrola kolizji otworów lico A – lico B (suma głębokości > grubości lub przelot) i krawędź–krawędź prostopadle, promień wycięć wokół pilotów Ø5×5.
- `arkusz_pdf.py`: opis średnic/głębokości wg rzeczywistych otworów (nie stałe „Ø4, 35 mm"), piloty Ø3×12 i Ø5×5 nie jako „pod podpórki".
