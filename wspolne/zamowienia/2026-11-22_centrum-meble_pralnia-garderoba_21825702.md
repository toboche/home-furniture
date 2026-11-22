# Zamówienie robocze w `centrum.meble.pl`: Pralnia + Garderoba (rozkrój `21825702`, 2026-11-22)

Dokument zbiorczy do niezależnej weryfikacji zamówienia przez agentów prowadzących pomieszczenia `pralnia/` i `garderoba/`.
Rejestr wszystkich zamówień: `wspolne/zamowienia/README.md`.
Praktyczna instrukcja obsługi kalkulatora `centrum.meble.pl`: `wspolne/centrum_meble.md`.

---

## 1. Metadane zlecenia

| Pole | Wartość |
|---|---|
| **Numer rozkroju (aktualny)** | **`21825702`** *(zastępuje rewizję `21811821` usuniętą z koszyka po audycie 100%)* |
| **Link do podglądu / edycji** | `https://centrum.meble.pl/rozkroj,r21825702` |
| **Ważność podglądu rozkroju** | do **`20.01.2027 r.`** |
| **Status** | **Robocze zamówienie w koszyku (`/koszyk/`) na koncie użytkownika — NIE opłacone, NIE sfinalizowane** |
| **Status audytu** | **ZWERYFIKOWANE 100% (`85/85` formatek, `620/620` unikalnych definicji otworów / `715/715` otworów z SZT)** |
| **Wariant cięcia** | **`PREMIUM (+standard)`** (dokładność 0,3 mm) |
| **Do zapłaty (koszyk)** | **`5 924,63 PLN` brutto** (**`4 816,74 PLN` netto**), transport: `0 PLN` (odbiór osobisty / przed wyborem dostawy) |
| **Czas realizacji / planowana wysyłka** | `14 dni roboczych` / planowany termin wysyłki: **`10.12.2026`** |
| **Opcja odpadów (`+5 PLN`)** | Niewybrana (`+5 PLN` nie doliczone) |
| **Podstawa z repozytorium** | Gałąź `main`, commit `d3ca20d` (stan 2026-11-19: `pralnia` v70 + `garderoba` po audycie v5 i PR #47–#49) |

---

## 2. Pełne rozbicie kosztów i materiałów z koszyka (`21825702`)

| Pozycja w koszyku / podsumowaniu | Ilość | Wartość brutto | Wartość netto |
|---|---:|---:|---:|
| `Płyta meblowa EGGER U702 ST9 Kaszmir 18 mm` (`6,5 + 1,25 szt.`) | **`7,75 szt.`** | `2 769,70 PLN` | `2 251,77 PLN` |
| `Płyta meblowa SM W960 SM Biały Klasyczny 16 mm` | **`0,5 szt.`** | `137,91 PLN` | `112,12 PLN` |
| `Obrzeże ABS U702 ST9 Kaszmir 23 x 0.8 mm EGGER` (`55 + 10 mb`, na magazynie `pow. 50 mb`) | **`65 mb`** | `108,55 PLN` | `88,40 PLN` |
| `Obrzeże meblowe do oklejania laserowego PRO U702 ST9 (79098) Kaszmir 23 x 1 mm REHAU` (`pow. 50 mb`) | **`45 mb`** | `246,15 PLN` | `200,25 PLN` |
| `Cięcie płyty` (PREMIUM) | `192 mb` | `921,60 PLN` | `748,80 PLN` |
| `Cięcie płyty` (+standard) | `37 mb` | `163,91 PLN` | `133,20 PLN` |
| `Oklejanie płyty` | `4 mb` | `27,56 PLN` | `22,40 PLN` |
| `Oklejanie płyty +` (laserowe 1,0 mm) | `31 mb` | `251,72 PLN` | `204,60 PLN` |
| `Oklejanie płyty` | `48 mb` | `300,96 PLN` | `244,80 PLN` |
| `Usługa wiercenia` — fronty z zawiasami (`Blum INSERTA`) | **`11 szt.`** | `136,62 PLN` | `111,10 PLN` |
| `Usługa wiercenia` — formatki korpusów (`Wręgowanie i nawierty`) | **`63 szt.`** | `859,95 PLN` | `699,30 PLN` |
| **RAZEM (`Do zapłaty`)** | | **`5 924,63 PLN`** | **`4 816,74 PLN`** |

---

## 3. Weryfikacja liczb kontrolnych vs `zamowienie.md` i `podsumowanie.json`

| Zakres | Pozycje (`formatki*.csv`) | Pozycje w kalkulatorze | Sztuki (plan / zamówienie) | Powierzchnia m² (plan / zamówienie) | Wiercone sztuki CNC (plan / zamówienie) | Status |
|---|---:|---:|---|---|---|---:|
| **Pralnia 18 mm (`PR-`)** | 44 | 47 *(rozbite `L2B`, `NWB`, `PP3-2`)* | `56 / 56` | `16,69 / 16,69` (`16,6853`) | korpusy `41 → 34` *(−7 szt. Wariant B)*; fronty `9 / 9` (`21` puszek) | **ZGODNE** *(z odstępstwem Wariant B)* |
| **Garderoba 18 mm (`GD-`)** | 27 | 28 *(zgrupowane wg `kalkulator_nawierty.csv`)* | `36 / 36` | `21,19 / 21,19` (`21,1941`) | korpusy `19 / 19` (`244` otw.); fronty `2 / 2` (`4` puszki) | **100% ZGODNE** |
| **RAZEM Płyta 1 (`18 mm U702 ST9`)** | **71** | **75** | **`92 / 92`** | **`37,88 / 37,88`** (`37,8793`) | korpusy **`53`**, fronty **`11`** | **100% ZGODNE** |
| **Płyta 2 (`16 mm W960 SM` — Garderoba)** | **6** | **10** | **`10 / 10`** | **`1,52 / 1,52`** (`1,5224`) | korpusy **`10 / 10`** (`68` otw.) | **100% ZGODNE** |
| **ŁĄCZNIE ZLECENIE `21825702`** | **77** | **85** | **`102 / 102`** | **`39,40 / 39,40`** | **`63 szt.` korpusów + `11 szt.` frontów = `74 szt.`** | **100% ZGODNE z koszykiem!** |

---

## 4. Kontrole obowiązkowe wykonane przed i w trakcie składania zamówienia

1. **Oś X i Y dla strony „Tył (B)” (`PR-PB2`, podgląd 2D + SVG):** potwierdzono, że `centrum.meble.pl` **NIE odbija** osi X ani Y na stronie „Tył (B)” (widok rentgenowski od Przodu A, `(0,0)` w lewym dolnym rogu — zgodny 1:1 z `kalkulator_nawierty.csv` i `arkusz_nawiertow.pdf`).
2. **Współrzędne dziesiętne (`.5`, `.6`, `.7`):** kalkulator zachowuje ułamki dokładnie, bez zaokrągleń i obcinania (zero dryftu między licem a czołem, także na `PR-KB1 ↔ PR-PT1` `244,5`).
3. **Średnice otworów:** wszystkie wymagane średnice (`Ø3×12`, `Ø5×5`, `Ø5×10`, `Ø5 przelotowo` w płaszczyźnie; `Ø4×35`, `Ø8×20` w czole) zostały przyjęte bez zamiany `Ø3` na `Ø4`.
4. **Okleina ręcznie po imporcie CSV:** import CSV zaznaczył domyślnie krawędzie `3` i `4` w `0,8 mm` — poprawiono ręcznie i zweryfikowano na **wszystkich 85 wierszach** (w tym odznaczone plecy/skrzynki, dolne krawędzie garderoby oraz `1,0 mm` bezspoinowe na wszystkich 14 frontach).
5. **Puszki zawiasów `PR-F9`, `PR-F10`, `GD-F1`, `GD-F2`:** wszystkie 11 frontów ma `BLUM puszka 35mm (inserta)` i odległość `22,5 mm`; na `PR-F9` ustawiono ręcznie `x3 = 620.5` od góry (`620,0 mm` od dołu, 0,0 mm odchyłki od prowadnika w `PR-PB2`), a na `PR-F10` ręcznie `x3 = 612`, `x4 = 612` (`100 / 612 / 1125 / 1637` od dołu).
6. **Płyta 16 mm na skrzynki garderoby:** zweryfikowano `16,0 mm` (`W960 SM Biały Klasyczny`, bez okleiny); formatki `GD-S1C-1/2` (`492×151`) i `GD-S2C-1/2` (`834×151`) przeszły z pełnymi nawiertami bez błędów i ostrzeżeń.

---

## 5. Wykaz wszystkich odstępstw względem repozytorium i ocena wpływu na projekt

### A. Pralnia (`pralnia/`)

1. **Próg nawiertów CNC w kalkulatorze to `240 × 100 mm` (nie `200 mm`) → decyzja użytkownika: Wariant B**
   - **Co odbiega od `pralnia/zamowienie.md`:** `zamowienie.md` pkt 4 zakładało minimum `200 mm` i kazało powiększyć tylko `KP1` do `200×126`. W rzeczywistości kalkulator ukrywa `Szablon nawiertów` dla każdej formatki z `max < 240` lub `min < 100`, co objęło **4 pozycje (7 sztuk)**: `PR-KP1` (`184×126`), `PR-KP2` (`202×125`, 2 szt.), `PR-KP3` (`202×126`, 3 szt.) i `PR-LF6` (`200×60`).
   - **Zastosowane rozwiązanie (Wariant B, zatwierdzony przez użytkownika):** wszystkie 4 pozycje zamówiono w **dokładnych wymiarach z modelu `pralnia/model.js`, BEZ nawiertów CNC**.
   - **Wpływ na wymiary i geometrię:** **ZERO** — 100% zgodności 1:1 z `model.js` i `formatki.csv` (`16,69 m²`), **odpada docinanie `KP1` z `200` do `184`**.
   - **Wpływ na koszt:** w mieszanym zleceniu `PREMIUM (+standard)` te elementy trafiły do puli `+standard` (`37 mb` cięcia) — **nie naliczono** dopłaty `docięcie 8,73 zł/szt.`, a dodatkowo zaoszczędzono `7 × 13,65 = 95,55 zł brutto` na wierceniu CNC.
   - **Wpływ na montaż — 25 otworów krawędziowych do wywiercenia ręcznie po dostawie** (w osi grubości 18 mm, `9 mm` od lica, wg `pralnia/wyniki/arkusz_nawiertow.pdf`):

| Formatka (szt.) | Wymiar [mm] | Krawędź (`arkusz_nawiertow.pdf`) | Otwór | Pozycja od krawędzi [mm] | Liczba otw. | Partner CNC i sposób wykonania |
|---|---:|---|---|---|---:|---|
| `PR-KP1` (1) | `184 × 126` | Kraw. 2 (przód do `PP1`) | **Ø8 × 21–22** *(model 20)* | **`31` i `101`** od kraw. przy `KB2` *(od pionu `25`!)* | 2 | `PR-PP1` CNC → znaczniki Ø8 + kołkownica |
| `PR-KP1` (1) | `184 × 126` | Kraw. 3 (lewy bok do `KB2`) | **Ø4 × 35** | **`50` i `134`** od tyłu (kraw. 4) | 2 | `PR-KB2` (`X=9; Y=68, 152`) → transfer przez otw. Ø5 CNC |
| `PR-KP2` (2) | `202 × 125` | Kraw. 2 (przód do `PP2`) | **Ø8 × 21–22** *(model 20)* | **`30` i `100`** od kraw. przy `KB2` *(od pionu `25`!)* | 4 | `PR-PP2-1/2` CNC → znaczniki Ø8 + kołkownica |
| `PR-KP3` (3) | `202 × 126` | Kraw. 2 (przód do `PP3`) | **Ø8 × 21–22** *(model 20)* | **`31` i `101`** od kraw. przy `KB3` *(od pionu `25`!)* | 6 | `PR-PP3-1/2/3` CNC → znaczniki Ø8 + kołkownica |
| `PR-KP3` (3) | `202 × 126` | Kraw. 3 (lewy bok do `KB3`) | **Ø4 × 35** | **`50` i `152`** od tyłu (kraw. 4) | 6 | `PR-KB3` (`X=9,456,903; Y=68,170`) → transfer przez otw. Ø5 CNC |
| `PR-KP3` (3) | `202 × 126` | Kraw. 4 (tył do `KT2`) | **Ø4 × 35** | **`63`** (dokładnie środek `126`) | 3 | `PR-KT2` (`X=9,456,903; Y=63`) → transfer przez otw. Ø5 CNC |
| `PR-LF6` (1) | `200 × 60` | Kraw. 3 (dół na `PP3-2`) | **Ø4 × 35** | **`50` i `150`** od końców | 2 | `PR-PP3-2` (`X=65,165; Y=246`) → transfer przez otw. Ø5 CNC |
| **RAZEM** | **7 szt.** | | **12× Ø8 + 13× Ø4** | | **25** | **12× kołkownica + 13× transfer przez CNC** |

   - **Zalecenia montażowe (audyt):**
     1. Kołki `KP ↔ PP`: otwory są asymetryczne (`30/31 mm` od boku `KB2/KB3`, `25 mm` od pionu). Użyć znaczników Ø8 + prostej kołkownicy 18 mm, wiercić na `21–22 mm` (zapas na klej PVAc dla kołka `Ø8×40`) i złożyć na sucho przed klejeniem.
     2. Konfirmaty (13× Ø4×35): najpierw spasować kołki `KP ↔ PP`, a otwory Ø4×35 przewiercać przez fabryczne otwory CNC Ø5 w `KB2`, `KB3`, `KT2`, `PP3-2` **PRZED** ich rozwierceniem do Ø7 (otwór Ø5 działa jako ciasna tuleja prowadząca wiertło Ø4).

2. **Prefiks kodów w pralni i garderobie:**
   - W prompcie pralni pojawiło się `GA-`, natomiast `wspolne/zasady.md` i dokumentacja garderoby wymagają **`GD-`**. Zastosowano konsekwentnie **`PR-`** (pralnia) i **`GD-`** (garderoba). Brak wpływu na geometrię.

### B. Garderoba (`garderoba/`)

1. **Płyta 16 mm na skrzynki szuflad (`GD-S1*`, `GD-S2*`):**
   - `garderoba/zamowienie.md` pkt 2 dopuszczało `U702 ST9 16 mm`, jeśli jest w sklepie. Sklep nie oferuje `U702 ST9` w grubości 16 mm (tylko 18 i 36 mm).
   - Zgodnie z decyzją użytkownika (pudła szuflad zostają jak planowane poprzednio — białe 16 mm) zamówiono **`Płyta meblowa SM W960 SM Biały Klasyczny 16 mm`** (`0,5` arkusza, `137,91 PLN` brutto, struktura `SM SemiMatt`, bez okleiny, pełne CNC `68/68` otworów).
   - **Wpływ techniczny:** **ZERO** (zachowana krytyczna grubość `16 mm` pod Blum MOVENTO). **Wpływ wizualny:** pomijalny (skrzynki schowane za chowanymi frontami `GD-F3`, `GD-F4` w kolorze Kaszmir U702).
2. **Wycięcia narożników `GD-LB1` (`184×335`) i `GD-LB2` (`129×335`):**
   - Zamówione jako pełne prostokąty `2120×698` z okleiną kraw. `1 + 2` (w `GD-LB2` nawiert środka `Ø5×5` pod gniazdko), bo kształt L blokuje szablon nawiertów i pełne oklejanie. Zgodne z `garderoba/zamowienie.md` pkt 5 — wycięcia wykonuje użytkownik.
3. **Uwaga przy zakupie okuć (poza tym rozkrojem):**
   - `garderoba/komponenty.md` nadal wymienia „łączniki narożne białe” (sprzed zmiany dekoru z W1200 na U702 Kaszmir). Przy zakupie okuć dobrać łączniki narożne i zaślepki w kolorze **kaszmir / szarobeżowym**.

### C. Wspólne (`PR` + `GD`)

- **Wariant cięcia `PREMIUM (+standard)`:** zatwierdzony przez użytkownika — pozytywny wpływ na pasowanie styków 0 mm w pralni, luzów 3 mm przy ścianach, szczelin 2 mm frontów chowanych garderoby oraz skrzynek MOVENTO.
- **Czas realizacji:** obie płyty (`U702 ST9 18 mm` i `W960 SM 16 mm`) mają status na zamówienie (`0 szt` od ręki), stąd `Czas wykonania rozkroju: 14 dni roboczych` (planowana wysyłka `10.12.2026`). Oba obrzeża (`ABS 0,8 mm` i `REHAU PRO 1,0 mm`) są na magazynie (`pow. 50 mb`).

---

## 6. Problemy napotkane podczas składania zamówienia i ich rozwiązanie

1. **Próg nawiertów `240 × 100 mm`** (ukrycie szablonu dla `PR-KP1/KP2/KP3/LF6`) → zatrzymano wpisywanie, audytor ocenił warianty B vs C1/C2, użytkownik wybrał **Wariant B**.
2. **Domyślne zaznaczanie krawędzi `3` i `4` przez import CSV** → każdą z 85 formatek poprawiono ręcznie i zweryfikowano na podglądzie SVG.
3. **Ukryty wybór `1,0 mm klejenie bezspoinowe`** przy zaznaczonym „różnymi obrzeżami” → odznaczano `rozne_obrzeza` i wybierano `1,0 mm` na wszystkich 14 frontach.
4. **Blokady Cloudflare (HTTP 429 / 403 `cf-mitigated: challenge`)** przy wyszukiwarce `/wyszukiwarka/` oraz szybkich seriach AJAX → zaniechano korzystania z wyszukiwarki, wprowadzono sekwencyjne żądania z przerwami i 2 razy użytkownik ręcznie przeszedł weryfikację Cloudflare.
5. **Wydajność 85-wierszowego formularza (~205 KB POST na pole) i degradacja długich sesji przeglądarki (>1000 kroków)** → skompresowano otwory w wierszach `15–75` przez `wielowiert` (`0,0 mm` dokładności, 480 otworów → ~190 wpisów) oraz zapisywano kolejne trwałe punkty kontrolne `Przelicz koszty` co kilka wierszy w świeżych sesjach:
   `21758906` → `21761020` → `21765736` → `21787712` → `21791256` → `21803057` → `21810807` → `21811821` → **`21825702`** (finalny w koszyku po audycie 100%).

---

## 6a. Historia rewizji i pełny audyt transkryptów (2026-11-22)

Po zapisaniu rewizji `21811821` przeprowadzono **pełny audyt kryminalistyczny (forensic audit)** wszystkich **3 181 skryptów przeglądarkowych** z 5 sesji (odtworzenie stanu każdego pola przez `JavaScriptCore` + weryfikacja odczytów DOM i zrzutów ekranu) względem kanonicznej specyfikacji wygenerowanej z `formatki.csv` / `kalkulator_nawierty*.csv`:

1. **Wynik audytu `21811821`:**
   - **84 / 85 formatek (100% Pralni `47/47` + `37/38` Garderoby):** pełna zgodność co do `0,01 mm` wszystkich wymiarów, oklein (`0,8 mm` / `1,0 mm` laser), szablonów frontów (`11` Blum INSERTA) i `619 / 620` unikalnych otworów CNC.
   - **Wykryto 1 błąd na Płycie 2 (`W960 SM 16 mm`), Formatce 8 — `GD-S2D` (`834 × 590`, dno szuflady S2):** w otworze płaszczyznowym #3 (`Tył`, Ø5 przelotowo — środkowy konfirmat `GD-S2D → GD-S2C-2`) wpisano `x = 357 mm, y = 8 mm` (pomyłkowo z bliźniaczego `GD-S1D`) zamiast wymaganego **`x = 417 mm, y = 8 mm`**. Liczba kółek SVG (6) nie wyłapała błędu, dopiero pełna rekonstrukcja współrzędnych i zrzut ekranu z audytu.
2. **Chirurgiczna poprawka (`21811821` → `21825702`, 2026-11-22):**
   - Na `https://centrum.meble.pl/rozkroj,r21811821` zmieniono **wyłącznie** pole `#wiercenia_w_plaszczyznie_2_8_3_wsp_x` z `357` na **`417`** (żadna inna formatka, krawędź, zawias ani otwór nie były dotykane).
   - Zweryfikowano na podglądzie DOM i SVG wszystkie 6 otworów płaszczyznowych `GD-S2D` (`100/582`, `135/8`, **`417/8`**, `417/582`, `699/8`, `734/582` — wszystkie `Tył, Ø5, przelot`), wszystkie 4 otwory krawędziowe (`K4: 50, 490`; `K2: 50, 490`, `Ø4×35`) oraz brak okleiny.
   - Przeliczono rozkrój → nowy numer **`21825702`** (`https://centrum.meble.pl/rozkroj,r21825702`, ważny do `20.01.2027 r.`), wszystkie pozycje i kwota **`5 924,63 PLN` brutto** identyczne.
   - Dodano `21825702` (`PREMIUM (+standard)`) do `/koszyk/` i usunięto zastąpiony `21811821` — w koszyku znajduje się wyłącznie **`Rozkrój 21825702`** (stan **85/85 formatek, 620/620 otworów = 100% zgodności**).

---

## 7. Kompletny manifest 85 pozycji w rozkroju `21825702` (do audytu pomieszczeń)

*Konwencja krawędzi: `1` = góra, `2` = prawa, `3` = dół, `4` = lewa. Na frontach `x1, x3` mierzone od góry, `x2, x4` od dołu. Wszystkie otwory płaszczyznowe i krawędziowe z tabeli poniżej zostały wprowadzone wg `*/wyniki/kalkulator_nawierty*.csv` i zweryfikowane co do liczby kropek/kresek na podglądzie SVG każdego wiersza.*

### Płyta 1: Egger U702 ST9 Kaszmir 18 mm (75 pozycji / 92 szt. / 37,88 m²)

| Nr | Kod w kalkulatorze | Szer × Wys [mm] | SZT | Okleina | Szablon | Otwory / Puszki |
|---:|---|---:|---:|---|---|---|
| 1 | `PR-PP1` | 499 × 273 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 8, czoło: 4 |
| 2 | `PR-KP1` | 184 × 126 | 1 | brak | bez nawiertów | — *(Wariant B: 4 otw. ręcznie)* |
| 3 | `PR-PP2` | 479 × 255 | 2 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 2 |
| 4 | `PR-KP2` | 202 × 125 | 2 | brak | bez nawiertów | — *(Wariant B: 2×2 otw. ręcznie)* |
| 5 | `PR-PP3-1, PR-PP3-3` | 481 × 255 | 2 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 8 |
| 6 | `PR-KP3` | 202 × 126 | 3 | brak | bez nawiertów | — *(Wariant B: 3×5 otw. ręcznie)* |
| 7 | `PR-PP3-2` | 481 × 255 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 2, czoło: 8 |
| 8 | `PR-L2P` | 619 × 576 | 3 | 2 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 9 |
| 9 | `PR-NWP` | 617 × 570 | 3 | 2 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 9 |
| 10 | `PR-L1W` | 576 × 100 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 4 |
| 11 | `PR-LF6` | 200 × 60 | 1 | brak | bez nawiertów | — *(Wariant B: 2 otw. ręcznie)* |
| 12 | `PR-RDW` | 481 × 100 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 4 |
| 13 | `PR-RDW2` | 481 × 100 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 6 |
| 14 | `PR-L1B1` | 1743 × 637 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 8, czoło: 0 |
| 15 | `PR-L2B-1` | 912 × 637 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 21, czoło: 0 |
| 16 | `PR-L2B-2` | 912 × 637 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 13, czoło: 0 |
| 17 | `PR-NWB-1` | 912 × 635 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 13, czoło: 0 |
| 18 | `PR-NWB-2` | 912 × 635 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 21, czoło: 0 |
| 19 | `PR-KB1` | 489 × 200 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 3, czoło: 2 |
| 20 | `PR-KB2` | 1254 × 475 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 48, czoło: 2 |
| 21 | `PR-KB3` | 912 × 475 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 16, czoło: 0 |
| 22 | `PR-PB1` | 489 × 200 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 6, czoło: 2 |
| 23 | `PR-PB2` | 1236 × 273 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 34, czoło: 2 |
| 24 | `PR-PB3` | 912 × 273 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 14, czoło: 0 |
| 25 | `PR-L1T` | 1743 × 576 | 1 | brak | Wręgowanie | płaszczyzna: 0, czoło: 12 |
| 26 | `PR-L2T` | 912 × 576 | 1 | brak | Wręgowanie | płaszczyzna: 9, czoło: 8 |
| 27 | `PR-NWT` | 912 × 570 | 1 | brak | Wręgowanie | płaszczyzna: 9, czoło: 8 |
| 28 | `PR-PT1` | 489 × 406 | 1 | brak | Wręgowanie | płaszczyzna: 0, czoło: 7 |
| 29 | `PR-KT2` | 912 × 126 | 1 | brak | Wręgowanie | płaszczyzna: 3, czoło: 4 |
| 30 | `PR-PT2` | 1236 × 349 | 1 | brak | Wręgowanie | płaszczyzna: 2, czoło: 6 |
| 31 | `PR-PT3` | 912 × 349 | 1 | brak | Wręgowanie | płaszczyzna: 7, czoło: 4 |
| 32 | `PR-L1B2` | 1743 × 637 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 9, czoło: 0 |
| 33 | `PR-KT1A` | 405 × 121 | 1 | brak | bez nawiertów | — |
| 34 | `PR-KT1B` | 405 × 121 | 1 | brak | bez nawiertów | — |
| 35 | `PR-KT1C` | 347 × 121 | 1 | brak | bez nawiertów | — |
| 36 | `PR-L1P` | 619 × 574 | 1 | 2 (0,8 mm ABS) | bez nawiertów | — |
| 37 | `PR-L1WD` | 575 × 100 | 1 | 1 (0,8 mm ABS) | bez nawiertów | — |
| 38 | `PR-F1` | 609 × 454.5 | 1 | 1,2,3,4 (1,0 mm laser) | Front lewy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 39 | `PR-F2` | 609 × 454.5 | 1 | 1,2,3,4 (1,0 mm laser) | Front lewy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 40 | `PR-F3` | 603 × 454.5 | 1 | 1,2,3,4 (1,0 mm laser) | Front prawy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 41 | `PR-F4` | 603 × 454.5 | 1 | 1,2,3,4 (1,0 mm laser) | Front prawy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 42 | `PR-F5` | 274.5 × 454.5 | 1 | 1,2,3,4 (1,0 mm laser) | Front prawy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 43 | `PR-F6` | 236.5 × 454.5 | 1 | 1,2,3,4 (1,0 mm laser) | bez nawiertów | — |
| 44 | `PR-F7` | 514 × 454.5 | 1 | 1,2,3,4 (1,0 mm laser) | Front prawy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 45 | `PR-F8` | 439 × 493.5 | 1 | 1,2,3,4 (1,0 mm laser) | Front prawy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 46 | `PR-F9` | 514 × 1240.5 | 1 | 1,2,3,4 (1,0 mm laser) | Front prawy | Blum INSERTA 22,5 mm (x1=100, x2=100, x3=620.5) |
| 47 | `PR-F10` | 609 × 1737 | 1 | 1,2,3,4 (1,0 mm laser) | Front prawy | Blum INSERTA 22,5 mm (x1=100, x2=100, x3=612, x4=612) |
| 48 | `GD-NB-1` | 2120 × 571 | 1 | 1,4 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 21, czoło: 0 |
| 49 | `GD-NB-2` | 2120 × 571 | 1 | 1,4 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 15, czoło: 0 |
| 50 | `GD-NP` | 2102 × 553 | 1 | 1,4 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 18, czoło: 9 |
| 51 | `GD-NT` | 1767 × 1086 | 1 | brak | Wręgowanie | płaszczyzna: 24, czoło: 16 |
| 52 | `GD-NW, GD-GNG` | 1086 × 571 | 2 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 7, czoło: 6 |
| 53 | `GD-GNB-1` | 571 × 462 | 1 | 4 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 12, czoło: 0 |
| 54 | `GD-GNB-2` | 571 × 462 | 1 | 4 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 12, czoło: 0 |
| 55 | `GD-GND` | 1086 × 571 | 1 | 1 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 7, czoło: 6 |
| 56 | `GD-GNP` | 553 × 426 | 1 | 4 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 8 |
| 57 | `GD-GNT` | 1086 × 426 | 1 | brak | Wręgowanie | płaszczyzna: 2, czoło: 12 |
| 58 | `GD-LB2` | 2120 × 698 | 1 | 1,2 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 1, czoło: 0 |
| 59 | `GD-GLB1` | 698 × 462 | 1 | 2 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 1, czoło: 0 |
| 60 | `GD-NS-1..3, GD-NK` | 553 × 534 | 4 | 2 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 9 |
| 61 | `GD-NS-4, GD-NS-5` | 553 × 534 | 2 | 2 (0,8 mm ABS) | Wręgowanie | płaszczyzna: 0, czoło: 9 |
| 62 | `GD-NO-1, GD-NO-2` | 534 × 335 | 2 | 3 (0,8 mm ABS) | bez nawiertów | — |
| 63 | `GD-LB1` | 2120 × 698 | 1 | 1,2 (0,8 mm ABS) | bez nawiertów | — |
| 64 | `GD-LT` | 1767 × 876 | 1 | brak | bez nawiertów | — |
| 65 | `GD-LW` | 876 × 698 | 1 | 1 (0,8 mm ABS) | bez nawiertów | — |
| 66 | `GD-LS-1..3` | 876 × 680 | 3 | 1 (0,8 mm ABS) | bez nawiertów | — |
| 67 | `GD-LK` | 876 × 680 | 1 | 1 (0,8 mm ABS) | bez nawiertów | — |
| 68 | `GD-GLB2` | 698 × 462 | 1 | 2 (0,8 mm ABS) | bez nawiertów | — |
| 69 | `GD-GLD` | 876 × 698 | 1 | 1 (0,8 mm ABS) | bez nawiertów | — |
| 70 | `GD-GLG` | 876 × 698 | 1 | 1 (0,8 mm ABS) | bez nawiertów | — |
| 71 | `GD-GLT` | 876 × 426 | 1 | brak | bez nawiertów | — |
| 72 | `GD-F1` | 530 × 422 | 1 | 1,2,3,4 (1,0 mm laser) | Front lewy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 73 | `GD-F2` | 530 × 422 | 1 | 1,2,3,4 (1,0 mm laser) | Front prawy | Blum INSERTA 22,5 mm (x1=100, x2=100) |
| 74 | `GD-F3` | 530 × 204 | 1 | 1,2,3,4 (1,0 mm laser) | bez nawiertów | — |
| 75 | `GD-F4` | 872 × 204 | 1 | 1,2,3,4 (1,0 mm laser) | bez nawiertów | — |

### Płyta 2: Egger W960 SM Biały Klasyczny 16 mm (10 pozycji / 10 szt. / 1,52 m²)

| Nr | Kod w kalkulatorze | Szer × Wys [mm] | SZT | Okleina | Szablon | Otwory / Puszki |
|---:|---|---:|---:|---|---|---|
| 1 | `GD-S1B-1` | 490 × 180 | 1 | brak | Wręgowanie | płaszczyzna: 6, czoło: 0 |
| 2 | `GD-S1B-2` | 490 × 180 | 1 | brak | Wręgowanie | płaszczyzna: 6, czoło: 0 |
| 3 | `GD-S1D` | 492 × 490 | 1 | brak | Wręgowanie | płaszczyzna: 4, czoło: 4 |
| 4 | `GD-S1C-1` | 492 × 151 | 1 | brak | Wręgowanie | płaszczyzna: 0, czoło: 6 |
| 5 | `GD-S1C-2` | 492 × 151 | 1 | brak | Wręgowanie | płaszczyzna: 0, czoło: 6 |
| 6 | `GD-S2B-1` | 590 × 180 | 1 | brak | Wręgowanie | płaszczyzna: 6, czoło: 0 |
| 7 | `GD-S2B-2` | 590 × 180 | 1 | brak | Wręgowanie | płaszczyzna: 6, czoło: 0 |
| 8 | `GD-S2D` | 834 × 590 | 1 | brak | Wręgowanie | płaszczyzna: 6, czoło: 4 |
| 9 | `GD-S2C-1` | 834 × 151 | 1 | brak | Wręgowanie | płaszczyzna: 0, czoło: 7 |
| 10 | `GD-S2C-2` | 834 × 151 | 1 | brak | Wręgowanie | płaszczyzna: 0, czoło: 7 |
