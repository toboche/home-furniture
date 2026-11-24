# Zamówienie robocze w `centrum.meble.pl`: Kuchnia (rozkrój `21928081`, 2026-11-24)

Dokument zbiorczy do niezależnej weryfikacji zamówienia przez użytkownika i agenta prowadzącego pomieszczenie `kuchnia/`.
Rejestr wszystkich zamówień: `wspolne/zamowienia/README.md`.
Praktyczna instrukcja obsługi kalkulatora `centrum.meble.pl`: `wspolne/centrum_meble.md`.

---

## 1. Metadane zlecenia

| Pole | Wartość |
|---|---|
| **Numer rozkroju (aktualny w koszyku)** | **`21928081`** *(nazwa w koszyku: `Rozkrój 21928081 (import_ku_18mm)`)* |
| **Link do podglądu / edycji** | `https://centrum.meble.pl/rozkroj,r21928081` |
| **Ważność podglądu rozkroju** | do **`22.01.2027 r.`** |
| **Status** | **`robocze w koszyku`** — **NIEOPŁACONE** (oczekuje w `/koszyk/` na weryfikację i płatność użytkownika) |
| **Status audytu** | **ZWERYFIKOWANE 100% NA ŻYWO Z SERWERA (`21/21` formatek / `23/23` szt., `164/164` unikalnych otworów / `170/170` z SZT + `3/3` puszki `KU-F1` = `173/173` operacji CNC, `0` różnic, maks. odchyłka `0,000000 mm` — live DOM + `17/17` SVG + widok wydruku `Drukuj`)** |
| **Wariant cięcia** | **`PREMIUM`** (dokładność 0,3 mm; zakładka `Standard` niedostępna z uwagi na 19 z 23 szt. z obróbką CNC, a wszystkie 23 szt. mieszczą się na tych samych `1,5` arkusza `PREMIUM`) |
| **Kwota rozkroju w koszyku** | **`1 502,24 PLN` brutto** (**`1 221,26 PLN` netto**) |
| **Czas wysyłki / realizacji** | **`13 dni roboczych`** *(orientacyjnie ok. `11.12.2026`; obie pozycje materiałowe dostępne z magazynu: płyta `10,20 szt.`, obrzeże `pow. 50 mb`)* |
| **Transport / odbiór osobisty** | **`Odbiór osobisty Kraków` (`ul. Gromadzka 54`) — `0,00 PLN`** *(brak opłaty paletowej `150 PLN` przy 1,5 arkusza i maks. długości 1978 mm; kurier `506,27 PLN`)* |
| **Opcja odpadów (`+5 PLN`)** | **Domyślnie NIEWYBRANA w koszyku** *(rekomendacja audytu: przed płatnością zaznaczyć `TAK, chcę odpady (+5 PLN)` — ok. `3,44 m²` czystej płyty `H3710 18 mm` przyda się do próbnego frezowania rowków LED `17,2 × 6` i testu pogłębiania `Ø8 × 35 → 85`)* |
| **Podstawa z repozytorium** | Gałąź `main`, commit `f73787b` (stan 2026-11-24 po PR #71 `audyt-v7`, PR #72 `montaz-krok-po-kroku` oraz finalnym audycie `kuchnia/audyt/v8.md`; `run.py --wszystkie --sprawdz` w 100% zgodny) |
| **Pliki robocze weryfikacji (poza repo)** | `/Users/toboche/AntigravityProjects/Meble/_work_kuchnia/order_spec.json`, `import_ku_18mm.csv`, `audit_r21928081_result.json` |

---

## 2. Pełne rozbicie kosztów i materiałów w koszyku (`r21928081`)

| Pozycja w podsumowaniu / koszyku | Ilość potrzebna / dostępna | Wartość brutto | Wartość netto |
|---|---|---:|---:|
| `Płyta meblowa EGGER H3710 ST12 Orzech Carini naturalny 18 mm` (`1 cała 2800×2070 + 0,5 płyty 2800×1032`) | **`1,5 szt.`** / `10,20 szt.` *(na magazynie)* | `732,41 PLN` | `595,46 PLN` |
| `Obrzeże ABS H3710 ST12 Orzech Carini naturalny 23 x 0.8 mm EGGER` | **`30 mb`** / `pow. 50 mb` *(na magazynie)* | `86,40 PLN` | `70,20 PLN` |
| `Cięcie płyty` (`PREMIUM`) | `57 mb` | `273,60 PLN` | `222,30 PLN` |
| `Oklejanie płyty` *(netto obwodu `23,082 mb` → fakturowane `24 mb`)* | `24 mb` | `150,48 PLN` | `122,40 PLN` |
| `Usługa wiercenia` *(1 szt. front `KU-F1` + 18 szt. `Wręgowanie i nawierty` po `13,65 PLN` brutto)* | **`19 szt.`** | `259,35 PLN` | `210,90 PLN` |
| **RAZEM ROZKRÓJ `21928081` W KOSZYKU** | **`23 szt.` (`60,41%` wykorzystania z `8,69 m²`)** | **`1 502,24 PLN`** | **`1 221,26 PLN`** |

*(W koszyku nie ma żadnych innych pozycji; zamówienie `86253/26` z rozkrojem `21850722` dla pralni i garderoby jest już opłacone i w realizacji.)*

---

## 3. Weryfikacja liczb kontrolnych vs `kuchnia/zamowienie.md` i `wyniki/podsumowanie.json`

| Zakres | Pozycje w plikach źródłowych | Wiersze w kalkulatorze | Sztuki (plan / zamówienie) | Powierzchnia m² (plan / zamówienie) | Okleina netto [mb] | Wiercone sztuki CNC (plan / zamówienie) | Operacje CNC z SZT (plan / zamówienie) | Status |
|---|---:|---:|---|---|---:|---|---|---:|
| **Korpusy, półki i `KU-F1` (`W1–W15`)** | `15` (`formatki.csv`) | `15` (`W10` i `W14` zgrupowane po `2 szt.`) | `17 / 17` | `4,13 / 4,13` (`4,129089`) | `12,464` (`9,064 + 3,400`) | korpusy `12 / 12` + front `1 / 1` | `114` otw. (`108` wpisów) + `3` puszki | **100% ZGODNE** |
| **Fronty szuflad METOD (`W16–W21`)** | `6` (`fronty_metod.csv`) | `6` (`usłojenie 21a`..`22c`) | `6 / 6` | `1,03 / 1,03` (`1,031019`) | `10,618` | `Wręgowanie` `6 / 6` | `56 / 56` otworów (`Tył B`, `Ø5×12`) | **100% ZGODNE** |
| **ŁĄCZNIE ZLECENIE `21928081`** | **`21`** | **`21`** | **`23 / 23`** | **`5,16 / 5,16`** (`5,160108`) | **`23,082`** *(usługa `24 mb`)* | **`19 / 19 szt.`** (`1` + `18`) | **`173 / 173`** (`170` otw. + `3` puszki) | **100% ZGODNE** |

### Rozkład wszystkich 170 otworów (z uwzględnieniem `SZT`) w wierszach `Wręgowanie i nawierty`:
- **Płaszczyzna `Przód (A)` (`40` szt.):** `Ø3×5` (`2` piloty okapu w `SOB-1`), `Ø5×5` (`4` środki wycięć w `SOB-2`, `SOT`, `SOP`, `WSB-2`), `Ø5×10` (`8` podpórki w `SOB-1`, `SOB-2`), `Ø5×11` (`4` trzpienie `Minifix` w `SOB-1`), `Ø5 przelotowo` (`15` konfirmaty w `SOB-2`, `WSB-2`), `Ø8×10` (`4` kołki w `SOB-1`), `Ø15×14` (`3` puszki `Minifix` w `SOT`).
- **Płaszczyzna `Tył (B)` (`90` szt. = `34` korpusy + `56` METOD):** `Ø3×5` (`2` piloty okapu w `SOB-2`), `Ø3×12` (`6` prowadniki `KU-F1` w `SOB-2`), `Ø5×10` (`8` podpórki w `SOB-2`, `WSB-2`), `Ø5×12` (`56` mocowania `MAXIMERA` w `FM1–FM6`), `Ø5 przelotowo` (`13` konfirmaty w `SOB-2`, `SOT`, `WST`), `Ø15×14` (`1` puszka `Minifix` w `SOW`).
- **Czoło (`40` szt. z `34` wpisów, bo `W10` ma `SZT = 2`):** `Ø4×35` (`28` szt.: `K1`: `13`, `K3`: `7`, `K4`: `8`), `Ø8×22` (`4` szt.: `K2`: `2`, `K3`: `2`), `Ø8×33` (`4` szt. kanały `Minifix`: `K2`: `1`, `K3`: `3`), `Ø8×35` (`8` szt. pręty `M8`: `K3` w `P1` [`3`] i `P3` [`5`]).

---

## 4. Kontrole obowiązkowe i audyt końcowy 100%

1. **Potrójna weryfikacja kodów kierunku `Słoje` (`H3710 ST12`):** potwierdzono w nagłówku wzorcowego pliku CSV kalkulatora, etykietach przycisków radiowych (`#sloje_1_f_1/2`) oraz wizualnie na wygenerowanym arkuszu `2800 × 2070 mm` ze strzałką kierunku usłojenia (`r21927182`), że kod **`2` = `na szerokość`** (słoje równolegle do `SZER`), a kod **`1` = `na wysokość`** (słoje równolegle do `WYS`). Żaden wiersz nie ma wartości `0`.
2. **Kolejność oklejania `kryjące długie`:** dla obrzeża `ABS 0,8 mm` przy zaznaczeniu ≥ 2 prostopadłych krawędzi kalkulator udostępnia przełącznik `Rodzaj klejenia: kryjące długie (value=1) / kryjące krótkie (value=2)`. Na froncie `KU-F1` (`W15`, kryjące pionowe `1151 mm`) oraz wszystkich frontach `FM1–FM6` (`W16–W21`, kryjące poziome `597 mm`) wybrano i zweryfikowano `kryjące długie` (`value="1"`).
3. **Front `KU-F1` (`549 × 1151`, `W15`):** wybrano natywny szablon `Front prawy` + `BLUM puszka 35mm (wkręty)` (`value="1"`, `Ø35 × 13,5 mm`), odległość `22.50 mm`, `x1 = 100` (od góry), `x2 = 337.5` (`ręcznie`, od dołu), `x3 = 453.5` (`ręcznie`, od góry → `697,5 mm` od dołu), `Uchwyt = Brak`. Na podglądzie `Tył frontu` w UI wszystkie 3 puszki znajdują się po lewej stronie rysunku (co po odwróceniu frontu licem do kuchni odpowiada prawej krawędzi `Krawędź 2` przy `SOB-2`).
4. **Pre-flight kombinacji `Minifix 15` (`Ø15×14 + Ø8×33` na wspólnej osi `X = 55`) oraz `Ø8×35` w czole:** potwierdzono akceptację przez backend (`r21927182`). Ustalono przy okazji, że maszyna Homag odrzuca wiercenie w czole na krawędzi oklejonej obrzeżem (`r21927076`) — w zamówieniu kuchni żadna formatka nie ma otworów czołowych na oklejonej krawędzi.
5. **Niezależny audyt końcowy 100% ze świeżo przeładowanego `https://centrum.meble.pl/rozkroj,r21928081` (`audit_r21928081.py`):**
   - **Live DOM (`21 / 21` wierszy):** nazwy (w tym `usłojenie 21a`..`22c` = 13 zn.), wymiary, ilości (`23` szt.), słoje (`10× na szerokość`, `11× na wysokość`), krawędzie okleiny (`3` wiersze bez okleiny: `KU-SOT`, `KU-WST`, `KU-WSZ`), obrzeże `0.80_W` `H3710 ST12`, `rodzaj_oklejania = 1`, szablony, zawiasy `KU-F1` oraz wszystkie `126` wpisów otworów płaszczyznowych i `38` wpisów otworów czołowych — **`0` różnic, maksymalna odchyłka współrzędnych = `0,000000 mm`**.
   - **Podglądy 2D SVG (`17 / 17` wierszy `Wręgowanie`):** `126` kółek, `38` czerwonych linii czołowych i pogrubienia krawędzi `stroke-width="4"` zgodne 1:1 ze specyfikacją.
   - **Widok wydruku `GET /rozkroj/go/ajaxRequest,drukuj/art21928081.html?typ_rozkroju=1`:** sparsowano wszystkie `21 / 21` wierszy (`nazwa`, `SZER × WYS`, `SZT`, klasy `rozm_border0/1/2` i obecność okleiny `H3710 ST12 0,8x23 mm`) — **`0` różnic**.

---

## 5. Wykaz odstępstw względem repozytorium i lista prac ręcznych po dostawie

### A. Odstępstwa geometryczne, materiałowe i okuciowe w rozkroju `21928081`
- **BRAK (`0` odstępstw).** Wszystkie formatki, wymiary, ilości, słoje, krawędzie okleiny (`ABS 0,8 mm H3710` z opcją `kryjące długie`), puszki zawiasu `BLUM puszka 35mm (wkręty)` na `KU-F1` oraz wszystkie `170` otworów CNC udało się wprowadzić w wariantach podstawowych, bez konieczności użycia wariantu zapasowego (`Wręgowanie` na `KU-F1`).
- **Drobne różnice prezentacyjne w podsumowaniu kalkulatora względem opisu w `prompt_agenta_zamowienie.md` (bez wpływu na produkt):**
  1. Wariant cięcia wyświetla się jako **`PREMIUM`** (bez dopisku `(+standard)` i bez zakładki `Standard`), ponieważ obecność CNC blokuje tryb `Standard`, a wszystkie 4 sztuki nienawiercane mieszczą się na tych samych `1,5` arkusza `PREMIUM`.
  2. Pozycja `Usługa wiercenia` wyświetla się jako **jedna łączna linia `19 szt.` (`259,35 PLN` brutto)** zamiast osobnych linii `1 szt.` + `18 szt.` — przy obrzeżu `ABS 0,8 mm` na `KU-F1` stawka wiercenia frontu i wręgowania jest identyczna (`13,65 PLN/szt.` brutto; na Checkpoincie A przed dodaniem wręgowań widniało dokładnie `1 szt.` za `13,65 PLN`).

### B. Planowane prace ręczne do wykonania przez użytkownika po dostawie płyt (z oceną audytora)
1. **Poszerzenie przelotowych otworów konfirmatów z `Ø5` do `Ø7 mm` (`28` szt. w `SOB-2`, `SOT`, `WSB-2`, `WST`) + fazowanie łbów o `~0,5 mm`:** rozwiercać na podkładce drewnianej; obowiązkowo wpuścić łby poniżej lica na zewnętrznym licu `SOB-2` (pod `WST`/`WSW`), zewnętrznym licu `WSB-2` (`2 mm` luzu do ścianki) oraz wewnątrz `SO` (`SOB-2 → WSD` obok korpusu okapu).
2. **Pogłębienie otworów pod pręty `M8` w czołach `KU-P1` (`3` szt.) i `KU-P3` (`5` szt.) z `Ø8 × 35` do `85 mm`:** użyć długiego wiertła `Ø8` i prowadnicy/statywu (ścianka płyty `18 mm` ma po `5,0 mm` z obu stron; fabryczny otwór CNC `35 mm` prowadzi wiertło na starcie).
3. **Wyfrezowanie rowków `17,2 × 6 mm` w spodzie `KU-P1` i `KU-P3` pod profile `MasterLED`:** oś `39,1 mm` od przednich krawędzi (`30,5..47,7 mm`) + odcinek przy słupku pod `P1` + krótkie przejście poprzeczne pod `P1` od styku z `P3`; zabezpieczyć lakierem. Profile `MasterLED` wciskać dopiero po zamontowaniu gołych półek `P1` i `P3` na prętach i spięciu ich łącznikami od spodu (`KU8-02` w `kuchnia/audyt/v8.md`).
4. **Wycięcie otworu `Ø160 mm` w `KU-SOB-2`** (wokół pilota CNC `Ø5 × 5` na `1053; 109,5`): wycinać otwornicą z obu stron na płasko podpartej płycie przed montażem (nad otworem zostaje `21 mm` boku); wewnątrz wkleić płaski pasek EPDM `~5 mm`.
5. **Wycięcie `U` w `KU-SOD` (`514 × 284`) — UWAGA KRYTYCZNA `KU8-01` z `kuchnia/audyt/v8.md`:** wyciąć otwarte **OD TYLNEJ (NIEOKLEJONEJ) KRAWĘDZI** (`szer. 170 mm` na osi `X = 257`, do półkola `R85` o środku `120 mm` od tyłu — sięga `205 mm` od tyłu), a **NIE od przodu** (cięcie od przodu rozcięłoby okleinę `1DL` i uniemożliwiło wsunięcie `SOD` za rurę `Ø150`!). Krawędzie zabezpieczyć silikonem.
6. **Wycięcia `U` od tylnej krawędzi w `KU-SOP`** (`szer. 170, R85` wokół pilota `257; 91,5` + poszerzenie o `15–20 mm` w prawo po przymiarce obróconych kolan `15°`, krawędzie silikonem) **oraz w `KU-WSB-2`** (`szer. 140, R70` wokół pilota `1053; 97` pod rurę ze ścianki).
7. **Wycięcie `100 × 140 mm` w `KU-WST`** (od prawej krawędzi, `31 mm` pod górną krawędzią `WST`): prowadzić na podpartej płycie (nad wycięciem pasek `31 mm` z konfirmatem do `WSW`).
8. **Podcięcia narożne `25 × 25 mm` w tylnym prawym rogu `KU-SOP` i `KU-SOD`** oraz **otwór `Ø25 mm` w `KU-SOT`** (wokół pilota `485; 454`, z przelotką gumową — przewód przełożyć przed dociśnięciem `SO` do ściany).
9. **Otwory pod gałki w `FM1–FM6`** oraz wyrównanie `3` zawiasów `70T3550.TL` na `KU-F1` do wspólnej długiej listwy przed wkręceniem wkrętów `3,5 × 15 mm`.

---

## 6. Historia rewizji i checkpointów sesji (2026-11-24)

1. Pre-flight na osobnych testowych rozkrojach (poza koszykiem): `21926938` / `21927076` (wykrycie blokady wiercenia w czole na oklejonej krawędzi) → `21927092` (test pustej formatki i dostępności płyty `10,20 szt.` / obrzeża `pow. 50 mb`) → `21927182` (potwierdzenie `Ø15×14 + Ø8×33` na wspólnej osi `X = 55`, `Ø8×35`, nazwy `usłojenie 21a` i kierunku słojów `1 = na wysokość` na arkuszu `2800×2070`).
2. Budowa właściwego rozkroju kuchni po imporcie `import_ku_18mm.csv` (21 wierszy):
   - **`21927388`** — Checkpoint Partia A (`W12–W15`: `KU-SOD`, `KU-WSZ`, `KU-WSP-1/2`, `KU-F1`; wiercenia `1 szt.`),
   - **`21927668`** — Checkpoint Partia B1 (`W1–W4`: `KU-P1`, `KU-P3`, `KU-SOB-1`, `KU-SOB-2`; wiercenia `5 szt.`),
   - **`21927840`** — Checkpoint Partia B2 (`W5–W8`: `KU-SOT`, `KU-SOW`, `KU-SOP`, `KU-WSB-2`; wiercenia `9 szt.`),
   - **`21927908`** — Checkpoint Partia B3 (`W9–W11`: `KU-WST`, `KU-WSD/WSS`, `KU-WSW`; wiercenia `13 szt.`),
   - **`21927987`** — Checkpoint Partia C1 (`W16–W18`: `usłojenie 21a..21c`; wiercenia `16 szt.`),
   - **`21928081`** — **Finalny rozkrój kompletny (`W1–W21`, wiercenia `19 szt.`, `1 502,24 PLN` brutto)**, zweryfikowany w 100% i dodany do `/koszyk/`.

---

## 7. Kompletny manifest 21 pozycji w rozkroju `21928081`

*Konwencja krawędzi: `1` = góra, `2` = prawa, `3` = dół, `4` = lewa. Płyta 1: `Płyta meblowa EGGER H3710 ST12 Orzech Carini naturalny 18 mm`, obrzeże `ABS H3710 ST12 23 × 0.8 mm EGGER` (`0.80_W`, na frontach `W15–W21` `kryjące długie`).*

| Nr | Kod repo | Nazwa w kalkulatorze | Szer × Wys [mm] | SZT | Słoje | Okleina | Szablon | Otwory CNC / Puszki |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | `KU-P1` | `KU-P1` | `804 × 400` | 1 | na szerokość (`2`) | `1` | Wręgowanie | płaszcz.: `0`, czoło: `3` (`K3: 3×Ø8×35`) |
| 2 | `KU-P3` | `KU-P3` | `1978 × 200` | 1 | na szerokość (`2`) | `1` | Wręgowanie | płaszcz.: `0`, czoło: `5` (`K3: 5×Ø8×35`) |
| 3 | `KU-SOB-1` | `KU-SOB-1` | `1154 × 304` | 1 | na szerokość (`2`) | `1` | Wręgowanie | płaszcz.: `14` (`Przód`), czoło: `0` |
| 4 | `KU-SOB-2` | `KU-SOB-2` | `1154 × 304` | 1 | na szerokość (`2`) | `1` | Wręgowanie | płaszcz.: `27` (`11 Przód + 16 Tył`), czoło: `0` |
| 5 | `KU-SOT` | `KU-SOT` | `1154 × 516` | 1 | na szerokość (`2`) | `brak` | Wręgowanie | płaszcz.: `7` (`4 A + 3 B`), czoło: `9` (`5 K3 + 4 K1`) |
| 6 | `KU-SOW` | `KU-SOW` | `516 × 286` | 1 | na szerokość (`2`) | `1` | Wręgowanie | płaszcz.: `1` (`Tył`), czoło: `8` (`3 K3 + 2 K4 + 3 K2`) |
| 7 | `KU-SOP` | `KU-SOP` | `514 × 284` | 1 | na szerokość (`2`) | `1` | Wręgowanie | płaszcz.: `1` (`Przód Ø5×5`), czoło: `0` |
| 8 | `KU-WSB-2` | `KU-WSB-2` | `1154 × 300` | 1 | na szerokość (`2`) | `1` | Wręgowanie | płaszcz.: `14` (`10 Przód + 4 Tył`), czoło: `0` |
| 9 | `KU-WST` | `KU-WST` | `1154 × 256` | 1 | na szerokość (`2`) | `brak` | Wręgowanie | płaszcz.: `6` (`Tył`), czoło: `3` (`K1`) |
| 10 | `KU-WSD, KU-WSS` | `KU-WSD, WSS` | `282 × 256` | 2 | na wysokość (`1`) | `2` | Wręgowanie | płaszcz.: `0`, czoło: `6` (`2 K1 + 2 K3 + 2 K4`) × `2 szt.` |
| 11 | `KU-WSW` | `KU-WSW` | `282 × 256` | 1 | na wysokość (`1`) | `2` | Wręgowanie | płaszcz.: `0`, czoło: `4` (`2 K1 + 2 K4`) |
| 12 | `KU-SOD` | `KU-SOD` | `514 × 284` | 1 | na szerokość (`2`) | `1` | bez nawiertów | — |
| 13 | `KU-WSZ` | `KU-WSZ` | `254 × 165` | 1 | na wysokość (`1`) | `brak` | bez nawiertów | — |
| 14 | `KU-WSP-1, KU-WSP-2` | `KU-WSP-1, WSP-2` | `282 × 254` | 2 | na wysokość (`1`) | `2` | bez nawiertów | — |
| 15 | `KU-F1` | `KU-F1` | `549 × 1151` | 1 | na wysokość (`1`) | `1, 2, 3, 4` | Front prawy | `BLUM puszka 35mm (wkręty)`, `y=22.50`, `x1=100`, `x2=337.5`, `x3=453.5` |
| 16 | `KU-FM1` | `usłojenie 21a` | `597 × 142` | 1 | na wysokość (`1`) | `1, 2, 3, 4` | Wręgowanie | płaszcz.: `4` (`Tył Ø5×12`), czoło: `0` |
| 17 | `KU-FM2` | `usłojenie 21b` | `597 × 397` | 1 | na wysokość (`1`) | `1, 2, 3, 4` | Wręgowanie | płaszcz.: `12` (`Tył Ø5×12`), czoło: `0` |
| 18 | `KU-FM3` | `usłojenie 21c` | `597 × 397` | 1 | na wysokość (`1`) | `1, 2, 3, 4` | Wręgowanie | płaszcz.: `12` (`Tył Ø5×12`), czoło: `0` |
| 19 | `KU-FM4` | `usłojenie 22a` | `597 × 197` | 1 | na wysokość (`1`) | `1, 2, 3, 4` | Wręgowanie | płaszcz.: `8` (`Tył Ø5×12`), czoło: `0` |
| 20 | `KU-FM5` | `usłojenie 22b` | `597 × 197` | 1 | na wysokość (`1`) | `1, 2, 3, 4` | Wręgowanie | płaszcz.: `8` (`Tył Ø5×12`), czoło: `0` |
| 21 | `KU-FM6` | `usłojenie 22c` | `597 × 397` | 1 | na wysokość (`1`) | `1, 2, 3, 4` | Wręgowanie | płaszcz.: `12` (`Tył Ø5×12`), czoło: `0` |

---

## 8. Mail do `centrum@meble.pl` po opłaceniu zamówienia (ciągłość usłojenia `21a–21c` i `22a–22c`)

Zaraz po opłaceniu zamówienia należy wysłać wiadomość na adres `centrum@meble.pl` z numerem zamówienia sklepowego oraz numerem rozkroju **`21928081`** i załącznikiem `kuchnia/zamowienie/fronty_metod_rysunek.pdf` (prośba o wycięcie frontów `usłojenie 21a, 21b, 21c` z jednego pasa płyty kolejno w pionie oraz `usłojenie 22a, 22b, 22c` z jednego pasa płyty kolejno w pionie, bez obracania góra/dół ze względu na nawierty na tyle).
