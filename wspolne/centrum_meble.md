# Jak składać zamówienia w `centrum.meble.pl` (praktyczna instrukcja)

Przewodnik opracowany na podstawie pełnego, zweryfikowanego złożenia wspólnego rozkroju dla pralni i garderoby (`21811821`, 85 pozycji / 102 sztuki / 2 grubości płyt, 2026-11-19..21). Zastępuje rozproszone założenia ze starszych wpisów — wszystkie limity, opcje i zachowania kalkulatora poniżej zostały sprawdzone bezpośrednio w interfejsie strony.

---

## 1. Podstawy i przygotowanie zlecenia

- **Kalkulator płyt meblowych:** `https://centrum.meble.pl/rozkroj,plyty-meblowe`
- **Logowanie:** przed dodaniem do koszyka zaloguj się na swoje konto (`https://centrum.meble.pl/moje_konto/`). Zapisane podglądy rozkroju (`/rozkroj,rXXXXXXXX`) działają przez ok. 60 dni i otwierają od razu pełny, edytowalny formularz.
- **Wiele płyt w jednym zleceniu:** kliknij **`DODAJ PŁYTĘ`**.
  - Wszystkie pomieszczenia korzystające z tego samego dekoru 18 mm wpisuj na **jednej płycie** (wspólna optymalizacja arkuszy wyraźnie zmniejsza odpad i liczbę arkuszy — np. dla pralni + garderoby 37,88 m² zmieściło się na 7,75 arkusza, 84,3% wykorzystania).
  - Płytę innej grubości (np. 16 mm na skrzynki szuflad Blum MOVENTO) dodaj jako drugą płytę w tym samym zleceniu.
- **Prefiksy nazw formatek:** przy wspólnym zamówieniu dla wielu pomieszczeń zawsze dodawaj prefiks pomieszczenia DUŻYMI LITERAMI (`PR-`, `GD-`, `KU-`, `PP-` — zgodnie z `wspolne/zasady.md`), bo kody lokalne (`F1`, `F2`...) powtarzają się między pokojami.
- **Źródło danych z repozytorium:**
  - Formatki z nawiertami wpisuj **według `*/wyniki/kalkulator_nawierty.csv`** (i `*_16mm.csv`), a nie według `formatki.csv` — każdy wiersz z numerem `LP` to jedna pozycja w kalkulatorze (elementy o identycznych nawiertach są już zgrupowane).
  - Formatki bez nawiertów oraz fronty dopisz z `*/wyniki/formatki.csv`.
  - Pamiętaj o ręcznych uzupełnieniach okleiny z `<pomieszczenie>/zamowienie.md` (np. dolne krawędzie stojące na kafelkach w garderobie, których `kalkulator_nawierty.csv` nie zawiera).

---

## 2. Płyty i obrzeża (sprawdzone w ofercie 2026-11)

| Materiał | Dokładna nazwa w kalkulatorze | Dostępne formaty / grubości | Uwagi |
|---|---|---|---|
| **Kaszmir 18 mm** | `Płyta meblowa EGGER U702 ST9 Kaszmir 18 mm` | `2070×2800` (cała), `2800×1032` (połówka); brak ćwiartek. Grubości: `18 mm`, `36 mm` (**brak `16 mm`**) | Na zamówienie (~7 dni rob.), ok. 350 zł brutto/arkusz |
| **Biała 16 mm (skrzynki)** | `Płyta meblowa SM W960 SM Biały Klasyczny 16 mm` | `2070×2800`, `2800×1032`. Struktura wyłącznie **`SM SemiMatt`** (wybór 16 mm przy ST7 automatycznie przełącza na SM) | Na zamówienie (~7 dni rob.), ok. 276 zł brutto/arkusz |
| **Okleina ABS 0,8 mm (U702)** | `Obrzeże ABS U702 ST9 Kaszmir 23 x 0.8 mm EGGER` | Na magazynie (`pow. 50 mb`) | Do korpusów, półek i wieńców |
| **Okleina laserowa 1,0 mm (U702)** | `Obrzeże meblowe do oklejania laserowego PRO U702 ST9 (79098) Kaszmir 23 x 1 mm REHAU` | Na magazynie (`pow. 50 mb`) | Na 4 krawędzie frontów |

### Pułapki okleiny `1,0 mm klejenie bezspoinowe`
1. **Radio `1,0 mm klejenie bezspoinowe` jest widoczne TYLKO gdy checkbox „chcę okleić formatkę różnymi obrzeżami” (`rozne_obrzeza`) jest ODZNACZONY.** Gdy jest zaznaczony, formularz pokazuje wyłącznie `0,8 mm` i `2,0 mm`.
2. Okleina bezspoinowa `1,0 mm` **wyłącza szablon `Wręgowanie i nawierty`** — można z nią używać tylko `Formatka bez nawiertów` oraz szablonów frontów (`Front lewy`, `Front prawy` itp.).

---

## 3. Import listy formatek z CSV (`WCZYTAJ PLIK`)

Import CSV pozwala wczytać od razu wszystkie wiersze (nazwy, wymiary, ilości) jednym kliknięciem zamiast ręcznego dodawania kilkudziesięciu pozycji.

- **Format pliku CSV** (separator `;`, wg `meblepl_przykladowy_rozkroj.csv`):
  ```text
  Nazwa (nie wpływa na rozkrój);Szerokość;Oklejanie szerokości;Wysokość;Oklejanie wysokość;Grubość płyty;Ilość sztuk;Słoje
  PR-PP1;499;-;273;-;18;1;0
  ```
- **Kolumna `Słoje`:** dla dekorów jednolitych bez usłojenia (`U702 ST9`, `W960 SM`) zawsze wpisuj **`0`** (bez znaczenia — kalkulator może swobodnie obracać formatki i oszczędza arkusze).
- **Ważna pułapka importu CSV:** nawet gdy w kolumnach oklejania wpiszesz `-` (brak okleiny), **kalkulator po imporcie potrafi domyślnie zaznaczyć krawędzie `3` (dół) i `4` (lewa) w `0,8 mm`**! Po imporcie CSV należy **na każdym wierszu ręcznie zweryfikować i poprawić zaznaczone krawędzie oraz grubość obrzeża** (dla frontów przełączyć na 4 krawędzie i `1,0 mm klejenie bezspoinowe`, dla pleców i skrzynek odznaczyć wszystko).

---

## 4. Limity wymiarowe kalkulatora (zweryfikowane na wartościach granicznych)

| Operacja | Zweryfikowany limit | Zachowanie kalkulatora |
|---|---|---|
| **Szablon nawiertów (`Wręgowanie i nawierty`)** | **`max(Szer, Wys) ≥ 240 mm` ORAZ `min(Szer, Wys) ≥ 100 mm`** (włącznie; orientacja bez znaczenia: `240×100` i `100×240` przechodzą) | Przy `239×100` lub `240×99` pojawia się pomarańczowe ostrzeżenie `Zalecany rozmiar to 240x100mm.` i sekcja `Szablon nawiertów` znika całkowicie. Dotyczy zarówno płyty 18 mm, jak i 16 mm (płyta 16 mm `492×151` przechodzi bez ostrzeżeń). |
| **Samo cięcie bez nawiertów poniżej `240 × 100 mm`** | Akceptowane (przetestowane dla `184×126`, `202×125`, `200×60`) | `Przelicz koszty` przechodzi bez blokady. W małym czystym rozkroju `PREMIUM` sklep dolicza `Cięcie płyty (docięcie)` `8,73 zł brutto/szt.`, natomiast w dużym zleceniu `PREMIUM (+standard)` małe nie-wiercone formatki mogą trafić do puli `+standard` bez dopłaty docięcia. |
| **Maksymalna długość dla nawiertów** | `≤ 2500 mm` | Powyżej 2500 mm szablony nawiertów są niedostępne (stąd podział wysokich szaf na korpus dolny i górny). |

> **Pułapka UI przy poprawianiu wymiaru:** jeśli wiersz miał wcześniej wymiar `< 240×100` (lub błąd w polu `Ilość sztuk`) i został potem powiększony do `≥ 240×100`, ostrzeżenie znika, ale sekcja `Szablon nawiertów` może pozostać ukryta. Dla formatek wymagających nawiertów zawsze wpisuj od razu docelowe wymiary `≥ 240×100` na nowym wierszu.

---

## 5. Szablon `Wręgowanie i nawierty` — osie, średnice i szybkie wpisywanie

### Układ współrzędnych (100% zgodny z naszym pipeline'em)
- Początek układu **`(0, 0)`** leży w **lewym dolnym rogu widoku z Przodu (A)**:
  - `X` rośnie w prawo wzdłuż `Szer` (od Krawędzi `4` ku Krawędzi `2`),
  - `Y` rośnie w górę wzdłuż `Wys` (od Krawędzi `3` ku Krawędzi `1`).
- **Numeracja krawędzi:** `1` = góra (`top`), `2` = prawa (`right`), `3` = dół (`bottom`), `4` = lewa (`left`).
- **Strona „Tył (B)” NIE odbija osi X ani Y!** Kalkulator pokazuje stronę B jako rzut rentgenowski („na wylot” od przodu): czarne kropki = `Przód (A)`, czerwone kropki = `Tył (B)`. Współrzędne z `kalkulator_nawierty.csv` wpisuje się wprost, **bez przeliczania `DL − X`**.
- **Współrzędne dziesiętne** (`.5`, `.6`, `.7`) są akceptowane i zapisywane dokładnie (bez zaokrąglania i bez obcinania) w płaszczyźnie, w czole i jako skok `wielowiertu`.

### Dostępne średnice i głębokości
- **Wiercenie w płaszczyźnie:** średnice **`3, 5, 8, 10, 15, 20, 35 mm`** (brak `4` i `7 mm`); głębokość `2–15 mm` lub `przelotowo` (`przelot`).
  - Konfirmaty: `Ø5 przelotowo` (do poszerzenia do `Ø7` po dostawie w płytach 18 mm; w skrzynkach 16 mm pod konfirmaty `5×40` tylko pogłębić stożkowo pod łeb).
  - Piloty prowadników zawiasów: `Ø3 × 12 mm`.
  - Podpórki półek: `Ø5 × 10 mm`.
  - Nawierty środków pod otwornicę / wyrzynarkę: `Ø5 × 5 mm`.
- **Wiercenie w czole (boku):** średnice **`4` i `8 mm`**; głębokość `2–35 mm`, **zawsze w połowie grubości płyty** (konfirmaty `Ø4 × 35 mm`, kołki `Ø8 × 20 mm`). Otwory przesunięte względem osi grubości (np. haki MOVENTO `7 mm` od spodu dna `16 mm`) trzeba wiercić ręcznie wzornikiem.

### Jak wpisywać 3× szybciej (bez utraty dokładności)
1. **`Typ nawiertu: wielowiert`** — działa zarówno w **płaszczyźnie** (`Kierunek: w osi X` / `w osi Y`), jak i w **czole**! Przyjmuje już **`2` otwory** oraz **skoki dziesiętne** (np. `32`, `259.5`, `270.7`, `328.6`). Pozwala zamienić szeregi podpórek, pary pilotów prowadników i rzędy konfirmatów w pojedyncze wpisy z dokładnością `0,0 mm`.
2. **`Skopiuj i odbij`:**
   - `Skopiuj i odbij w Y (w poziomie)` (`skopiujNawiert(..., 'Y')`) odbija otwór w poziomie: **`X → Szer − X`** (względem pionowej osi Y).
   - `Skopiuj i odbij w X (w pionie)` (`skopiujNawiert(..., 'X')`) odbija otwór w pionie: **`Y → Wys − Y`**.
3. **Kontrola wizualna na podglądzie SVG przed zwinięciem wiersza:**
   - Liczba kółek w `#plyta_wiercenie_w_czole_{b}_{f}` = `2` (legenda) + łączna liczba otworów w płaszczyźnie (czarne = Przód, czerwone = Tył).
   - Czerwone krótkie kreski na krawędziach = liczba otworów w czole.
   - Gruba czarna linia na obwodzie = oklejone krawędzie.

---

## 6. Szablony frontów (`Front lewy` / `Front prawy`)

- **UWAGA NA ORIENTACJĘ `Szer × Wys`:** pliki `formatki.csv` sortują wymiary jako `DL ≥ SZ`, natomiast szablony frontów wiercą zawiasy **ZAWSZE wzdłuż pionowej krawędzi `Wys`**!
  - Front szerszy niż wyższy (np. `PR-F1` `609×454,5`, `GD-F1` `530×422`): `Szer = 609`, `Wys = 454.5`.
  - Front wyższy niż szerszy (np. `PR-F5` `274,5×454,5`, `PR-F8` `439×493,5`, `PR-F9` `514×1240,5`, `PR-F10` `609×1737`): `Szer = szerokość frontu`, `Wys = wysokość frontu` (krawędź zawiasowa!).
- **Parametry zawiasów Blum INSERTA:**
  - `Typ zawiasu`: **`BLUM puszka 35mm (inserta)`** (puszka Ø35×13,5 + 2×Ø8 co 45 mm — nie wybierać wariantu na wkręty).
  - `Odległość od krawędzi`: **`22.50`** (`22.5mm od środka nawiertu(5mm od brzegu)`).
- **Pozycje puszek `x1..x4`:**
  - **`x1` i `x3`** mierzone są **OD GÓRY** frontu!
  - **`x2` i `x4`** mierzone są **OD DOŁU** frontu!
  - Dla 3 puszek (np. `PR-F9`, `Wys = 1240,5 mm`) domyślna opcja `symetrycznie` ustawia `x3 = 620.3`. Jeśli prowadniki w boku korpusu są na `620,0 mm` od dołu, przełącz `x3` na **`ręcznie`** i wpisz **`620.5`** (`1240,5 − 620,0 = 620,5`).
  - Dla 4 puszek (np. `PR-F10`, `Wys = 1737 mm`, środki od dołu `100 / 612 / 1125 / 1637`): `x1 = od góry 100`, `x2 = od dołu 100`, `x3 = ręcznie 612` (`1737 − 1125`), `x4 = ręcznie 612`.

---

## 7. Praca z dużym zleceniem (60–90 formatek) — jak nie stracić pracy i uniknąć blokad

Przy ~85 pozycjach w jednym formularzu każda zmiana pola (`blur`/`change`) wywołuje `ajaxRequest,validFormatka`, które potrafi wysyłać ~150–205 KB danych sesji PHP. Poniższe zasady pozwalają przejść cały proces bez straty danych:

1. **Zapisuj punkty kontrolne co 3–5 formatek przez `Przelicz koszty`:**
   - Każde `Przelicz koszty` tworzy nowy, trwały numer i URL `/rozkroj,rXXXXXXXX` po stronie serwera.
   - Dzięki temu przy timeoutach sieciowych lub wyzwaniu Cloudflare tracisz co najwyżej bieżące 2–3 wiersze, nigdy całość.
2. **Zawsze miej rozwinięty TYLKO 1 wiersz naraz:**
   - Zwijaj formatkę po weryfikacji SVG (zwinięty wiersz ma ~330 znaków w DOM; rozwinięty 20–40 KB).
3. **Unikaj wywoływania Cloudflare (HTTP 429 / 403):**
   - Nie otwieraj wielu kart `/wyszukiwarka/` ani podstron produktów — sprawdzaj dostępność płyt i obrzeży bezpośrednio w kalkulatorze.
   - Przy automatyzacji zachowaj sekwencyjność (nigdy równoległych żądań AJAX), czekaj na zniknięcie `div.blockUI` i dodawaj ~400–500 ms przerwy między żądaniami.
   - Gdyby Cloudflare pojawił się w trakcie edycji na AJAX-ie: otwórz `https://centrum.meble.pl/` w **drugiej karcie** (nie przeładowuj od razu kalkulatora), przejdź weryfikację, a dopiero potem kontynuuj.
4. **Długie sesje automatyzacji przeglądarki:**
   - Używaj wyłącznie dokładnych selektorów ID / `[onclick=...]` (np. `#formatka_1_23 .belka`, `#obrzeze_top_1_23`, `#wiercenia_w_plaszczyznie_1_23_1_wsp_x`), nigdy wolnego skanowania tekstu (`getByText`).
   - Przy otwieraniu zapisanego dużego rozkroju (`/rozkroj,rXXXXXXXX`) ustaw timeout nawigacji min. `25 s` (strona ładuje się ~12–15 s).
   - Co ~700–1000 kroków (po zapisaniu checkpointu `Przelicz koszty`) otwieraj nowy URL `/rozkroj,rXXXXXXXX` w świeżej sesji/karcie, żeby uniknąć degradacji pamięci przeglądarki.

---

## 8. Kontrola końcowa przed dodaniem do koszyka

Przed kliknięciem **`Do koszyka`** sprawdź w `Podsumowanie kosztów zlecenia`:
1. **Wariant cięcia:** `PREMIUM (+standard)` (dokładność 0,3 mm) vs `Standard` (0,5 mm).
2. **Płyty i grubości:** każda płyta z właściwym dekorem i grubością (zwłaszcza `16 mm` dla skrzynek — nie zamieniać na `18 mm`) oraz rozsądna liczba arkuszy.
3. **Obrzeża:** obecne oba typy (`ABS 0,8 mm` i `1,0 mm laserowe REHAU`) i status dostępności (`pow. 50 mb`).
4. **Liczba wierconych sztuk (`Usługa wiercenia`):**
   - Pierwszy wiersz (`~12,42 zł/szt.` brutto) = **liczba frontów z szablonem zawiasów**.
   - Drugi wiersz (`~13,65 zł/szt.` brutto) = **łączna liczba sztuk (uwzględniając `SZT`!) wszystkich formatek z `Wręgowaniem i nawiertami` ze wszystkich płyt**.
   - Porównaj obie liczby z sumą kontrolną z `kalkulator_nawierty*.csv` i `zamowienie.md` — to najpewniejszy szybki test, że żaden wiersz nie został pominięty!
5. **Koszyk (`/koszyk/`):** po kliknięciu `Do koszyka` sprawdź, że w koszyku jest właściwy numer rozkroju, termin, kwota i opcja odpadów (`NIE chcę odpadów` / `+5 PLN`). Zatrzymaj się na `/koszyk/` — **bez przechodzenia do kasy i bez płatności** aż do niezależnej weryfikacji przez użytkowników/agentów pomieszczeń.

---

## 9. Jak przebiegało składanie zamówienia `21811821` (workflow krok po kroku)

Poniższy schemat zadziałał skutecznie dla wspólnego zamówienia **85 pozycji / 102 sztuk / 715 otworów CNC + 25 puszek zawiasów** na dwóch grubościach płyt i może służyć jako punkt wyjścia dla kolejnych pomieszczeń (kuchnia, przedpokój itp.):

1. **Przygotowanie danych poza przeglądarką (Python, deterministycznie — zero ręcznego przepisywania):**
   - Pobranie najnowszego `main` i automatyczne porównanie `formatki*.csv`, `kalkulator_nawierty*.csv`, `podsumowanie.json` oraz wyjątków z `zamowienie.md` (ręczne dolne krawędzie okleiny, orientacja `Szer × Wys` frontów, prefiksy `PR-`/`GD-`).
   - Równoległe uruchomienie niezależnego **audytora odstępstw** (tryb tylko do odczytu), który weryfikuje sumy kontrolne i na bieżąco ocenia wpływ każdego ograniczenia kalkulatora na cały projekt (geometria, okucia, montaż).
   - Wygenerowanie 3 plików roboczych:
     - `board1_18mm.csv` i `board2_16mm.csv` do masowego wczytania wierszy przez `WCZYTAJ PLIK` (`Słoje = 0`, krawędzie `-` do późniejszego ustawienia),
     - `order_spec.json` — pełna specyfikacja wszystkich pozycji z asercjami sum sztuk, m² i otworów,
     - `fast_plan.json` — kompresja otworów w serie **`wielowiert`** (po X, po Y i w czole) z **automatycznym testem round-trip**: po rozwinięciu serii zbiór otworów musi się zgadzać co do `0,0 mm` z `kalkulator_nawierty*.csv`!
2. **Testy przedstartowe (pre-flight) na czystym kalkulatorze (zanim wczytasz 85 wierszy):**
   - Logowanie na konto użytkownika i sprawdzenie, że koszyk nie zawiera nieoczekiwanych pozycji.
   - Kontrola dostępności płyt i obu obrzeży (`0,8 mm` i `1,0 mm klejenie bezspoinowe`) bezpośrednio w kalkulatorze (bez otwierania `/wyszukiwarka/`).
   - **Test 2D / SVG strony „Tył (B)”** na jednej asymetrycznej formatce (np. `PR-PB2`) + test współrzędnych dziesiętnych (`.5`, `.6`, `.7`).
   - **Test wartości granicznych** na najmniejszych formatkach (wykrył próg `240 × 100 mm`, dzięki czemu użytkownik podjął decyzję o Wariancie B zanim wpisaliśmy resztę).
   - **Test szablonów frontów** (`PR-F9` 3 puszki, `PR-F10` 4 puszki, `GD-F1` front szerszy niż wyższy).
3. **Masowy import obu płyt:**
   - Wczytanie `board1_18mm.csv` na Płycie 1 (`U702 ST9 18 mm`), kliknięcie `DODAJ PŁYTĘ`, wybór `W960 SM 16 mm`, wczytanie `board2_16mm.csv` na Płycie 2.
4. **Uzupełnianie w krótkich partiach z trwałym checkpointem po każdej partii:**
   - Najpierw mniejsza płyta (`16 mm`, 10 wierszy) oraz wszystkie formatki **bez `Wręgowania`** (zwykłe formatki + 14 frontów z okleiną `1,0 mm` i 11 szablonami Blum INSERTA) → `Przelicz koszty` (szybko potwierdza w podsumowaniu `45 mb` lasera i `11 szt.` wierceń frontów).
   - Następnie formatki z `Wręgowaniem i nawiertami` w paczkach po **2–5 wierszy** (~15–30 wpisów `wielowiert` na paczkę): rozwiń wiersz → popraw okleinę → wybierz `Wręgowanie` → wpisz serie `wielowiert` → zweryfikuj liczbę `<circle>` i `<line>` w SVG → zwiń wiersz → po paczce kliknij **`Przelicz koszty`** i zapisz nowy numer `/rozkroj,rXXXXXXXX`.
   - Po każdej paczce sprawdzaj, czy `Usługa wiercenia` w `Podsumowanie kosztów zlecenia` wzrosła dokładnie o sumę `SZT` właśnie ukończonych wierszy.
   - Co ~700–1000 kroków otwieraj najnowszy zapisany URL `/rozkroj,rXXXXXXXX` w świeżej sesji przeglądarki.
5. **Finalizacja robocza w koszyku:**
   - Po ostatniej paczce finalne `Przelicz koszty`, pełny odczyt wszystkich linii `Podsumowanie kosztów zlecenia` (sprawdzenie `63 szt.` korpusów + `11 szt.` frontów, obu płyt, obu obrzeży, ceny brutto/netto), kliknięcie **`Do koszyka`** na wariancie `PREMIUM (+standard)`, weryfikacja `/koszyk/` i stop (bez kasy i płatności).

---

## 10. Mapa techniczna DOM, ID pól i mechaniki AJAX kalkulatora

Przydatna dla kolejnych agentów i ewentualnych skryptów automatyzujących (`b` = numer płyty `1, 2…`, `f` = numer wiersza `1..N`, `r` = numer wpisu otworu `1, 2…`):

### Selektory i funkcje JS w wierszu formatki
| Element | Selektor / `name` | Wywoływana funkcja / uwagi |
|---|---|---|
| Kontener i nagłówek wiersza | `#formatka_{b}_{f}`, `#formatka_{b}_{f} .belka` | `pokazUkryjFormatke('{b}_{f}')` — zwinięty wiersz znika z DOM (`~330` znaków), stan trzymany w sesji PHP |
| Wymiary, ilość, nazwa | `#szer_{b}_{f}`, `#wys_{b}_{f}`, `#ilosc_{b}_{f}`, `#nazwa_formatki_{b}_{f}` | `onblur`: `setSize('{b}_{f}', ..., 'checkMpr_szer'/'checkMpr_wys')`, `validIlosc('{b}_{f}')` |
| Okleina — przełączniki | `#obrzeze_all_{b}_{f}`, `#rozne_obrzeza_{b}_{f}` | `checkAll('{b}_{f}')`, `validForm('{b}','{f}')`; dla `1,0 mm` `rozne_obrzeza` **musi być odznaczone** |
| Okleina — krawędzie | `#obrzeze_top_{b}_{f}` (`1`), `#obrzeze_right_{b}_{f}` (`2`), `#obrzeze_bottom_{b}_{f}` (`3`), `#obrzeze_left_{b}_{f}` (`4`) | `onclick`: `setSize('{b}_{f}')` |
| Okleina — grubość | `#obrzeze_gr_{b}_{f}_all-1` (`0,8 mm`), `-2` (`1,0 mm bezspoinowe`), `-3` (`2,0 mm`) | `onclick`: `validForm1('{b}_{f}')`; zawsze sprawdzać tekst etykiety przed wyborem |
| Szablony nawiertów | przyciski z `onclick="setTypFrontu('{b}_{f}', ...)"` | m.in. `pusty` (bez nawiertów), `wregowanie`, `front_lewy`, `front_prawy` |
| Fronty — zawiasy | `#typ_zawiasu_{b}_{f}`, `#puszka_y_sel_{b}_{f}`, `#puszka_x{1..4}_sel_{b}_{f}`, `#puszka_x{1..4}_{b}_{f}` | `changeSelectPuszka(val, '{b}_{f}', 'x1'..'x4'\|'y')`; `y = 22.50`; ręczna pozycja: `sel = 'recznie'` |
| `Wręgowanie` — sekcje | `wiercenie_w_plaszczyznie[{b}][{f}]`, `wiercenie_w_czole[{b}][{f}]` | `onclick`: `validForm('{b}','{f}')` |
| Płaszczyzna — pola wpisu `r` | `#wiercenia_w_plaszczyznie_{b}_{f}_{r}_{powierzchnia\|wsp_x\|wsp_y\|srednica\|glebokosc\|typ_nawiertu\|ilosc\|odleglosc\|kierunek}` | `powierzchnia`: `'A'` (Przód) / `'B'` (Tył); `glebokosc`: `'2'..'15'` lub `'przelot'`; `typ_nawiertu`: `'pojedynczy'` / `'wielowiert'` |
| Czoło — pola wpisu `r` | `#wiercenia_w_czole_{b}_{f}_{r}_{krawedz\|odleglosc_x\|srednica\|glebokosc\|typ_nawiertu\|ilosc\|odleglosc}` | `krawedz`: `'top'` (1), `'right'` (2), `'bottom'` (3), `'left'` (4); `srednica`: `'4'` / `'8'` |
| Dodaj / kopiuj / usuń otwór | `[onclick="dodajNawiert('{b}','{f}','wiercenia_w_plaszczyznie');"]` (lub `'wiercenia_w_czole'`), `[onclick="skopiujNawiert('{b}', '{f}','wiercenia_w_plaszczyznie', '{r}', 'Y');"]` | `dodajNawiert` wymaga wypełnionego bieżącego wiersza (inaczej modal `Wypełnij wymagane pola`); `'Y'` odbija `X → Szer−X`, `'X'` odbija `Y → Wys−Y` |
| Podgląd 2D SVG | `#plyta_wiercenie_w_czole_{b}_{f}` | `<circle>` = `2` (legenda) + otwory płaszczyzny; `<line>` = `10` (osie/ramka) + otwory czoła; `stroke-width="4"` = okleina |
| Akcje globalne | `#fileupload_{b}`, `dodajPlyte()`, `[onclick="przelicz();"]` | `przelicz()` zapisuje trwały rozkrój `/rozkroj,rXXXXXXXX` (wyświetla formularz + `Podsumowanie kosztów` + `Do koszyka`) |

### Zachowanie AJAX i pułapki automatyzacji
- Każde zdarzenie `onblur` / `onchange` / `onkeyup` na polach otworów wywołuje `POST /rozkroj/go/ajaxRequest,validFormatka,...`, który wysyła cały stan formularza (~150–205 KB przy 85 wierszach) i wyświetla nakładkę **`div.blockUI`**.
- **Zawsze czekaj na ukrycie `div.blockUI`** przed kolejną akcją i dodawaj ~400–500 ms pauzy; nigdy nie uruchamiaj równoległych żądań.
- Unikaj lokatorów skanujących tekst (`getByText`) — na dużej stronie powodują timeouty; używaj wyłącznie bezpośrednich ID i selektorów `[onclick=...]`.
- **Stan w sesji PHP jest ulotny:** zwinięte wiersze znikają z DOM i siedzą tylko w sesji PHP do czasu kliknięcia `Przelicz koszty`. Przeładowanie `/rozkroj,rXXXXXXXX` przed kliknięciem `Przelicz koszty` cofa wszystkie niezapisane zmiany do ostatniego checkpointu.

---

## 11. Wnioski i konkretne ulepszenia na kolejne zamówienia (roadmap)

Doświadczenia z zamówienia `21811821` pokazały kilka wąskich gardeł, które warto usunąć przed zamawianiem kolejnych pomieszczeń (`kuchnia/`, `przedpokoj/`):

1. **Eksport gotowego `wielowiert` i paczki zamówieniowej w `wspolne/pipeline/`:**
   - Rozszerzyć `kalkulator.py` (albo dodać skrypt `wspolne/pipeline/zamowienie_export.py`), który dla wskazanych pomieszczeń generuje od razu:
     - pliki `board_<grubosc>mm.csv` w dokładnym formacie `centrum.meble.pl` (z prefiksami `PR-`/`GD-`/`KU-`/`PP-`, `Słoje = 0` dla dekorów uni i właściwą orientacją `Szer × Wys` dla frontów),
     - skompresowany `kalkulator_wielowiert.json` (z wbudowanym testem round-trip `0,0 mm`) — w `21811821` skróciło to liczbę wpisywanych pozycji z `480` do `192` (~2,5× mniej akcji!).
2. **Automatyczna kontrola progu `240 × 100 mm` w `wspolne/pipeline/run.py`:**
   - Dodać w `run.py` ostrzeżenie dla każdej formatki z otworami, której `max(DL, SZ) < 240` lub `min(DL, SZ) < 100` (oraz `> 2500 mm`), żeby decyzję o wariancie (ręczne wiercenie vs powiększenie do 240 mm) podejmować już na etapie projektu, nie dopiero w kalkulatorze.
3. **Obsługa wielu oklejanych krawędzi w `kalkulator.py`:**
   - Zamiast ręcznych tabel wyjątków w `zamowienie.md` (jak dolne krawędzie garderoby na kafelkach), zapisywać pełną listę oklejanych krawędzi w `reguly.py` i eksportować ją wprost do `kalkulator_nawierty.csv` / JSON-a.
4. **Szybsza automatyzacja przeglądarki (dostęp do JS / `evaluate`):**
   - W `21811821` wbudowana przeglądarka (`webview_browser`) blokowała `page.evaluate`, a każdy krok miał 13–29 s narzutu na skanowanie drzewa dostępności (co wydłużyło wpisywanie 85 wierszy do wielu godzin i wymagało restartu sesji co ~1000 kroków).
   - Przy kolejnych dużych zamówieniach warto skonfigurować **Chrome DevTools MCP / Puppeteer** (Node.js + `chrome-devtools-mcp` w `mcp_config.json`) z możliwością wypełniania pól jednego wiersza pojedynczym skryptem (z zachowaniem sekwencyjności i oczekiwania na `div.blockUI`), co powinno skrócić cały proces do **ok. 20–30 minut**.
5. **Rozdzielenie płyt różnych grubości przy bardzo dużych zamówieniach (>80–100 pozycji):**
   - Płyty o różnej grubości lub różnym dekorze (`18 mm U702` vs `16 mm W960`) **nie dzielą ze sobą arkuszy**. W jednym zleceniu jest wygodniej w koszyku, ale każdy dodatkowy wiersz powiększa POST `validFormatka`. Przy 3+ pomieszczeniach warto rozważyć osobny rozkrój dla mniejszej płyty (np. 16 mm) w tym samym koszyku — lżejszy formularz bez utraty optymalizacji arkuszy 18 mm (przed decyzją sprawdzić jedynie, czy sklep nie dubluje opłat transportowych).
6. **Sprawdzenie aktualności kolorów okuć w `komponenty.md` po zmianie dekoru płyty:**
   - Zmiana płyty (np. `W1200 → U702 Kaszmir`) powinna mieć checklistę obejmującą również zaślepki konfirmatów, łączniki narożne i uchwyty we wszystkich `komponenty.md`.

