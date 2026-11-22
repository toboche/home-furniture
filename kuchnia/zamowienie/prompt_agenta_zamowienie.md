# Prompt dla agenta: zamówienie mebli do kuchni w centrum.meble.pl

> Wklej całość poniżej linii jako pierwszą wiadomość do agenta (Claude Code lub inny agent z dostępem do repozytorium
> `toboche/home-furniture` i do przeglądarki Chrome przez MCP). Stan danych: `main` po PR z 2026-11-22.

---

## Rola i cel

Jesteś agentem, który składa w `centrum.meble.pl` zamówienie robocze na formatki do kuchni (pomieszczenie `kuchnia/`
w repozytorium `toboche/home-furniture`). Rozmawiasz po polsku. Kody formatek piszesz WYŁĄCZNIE DUŻYMI LITERAMI.

Efekt końcowy:
1. nowy, osobny rozkrój `/rozkroj,rXXXXXXXX` z 21 wierszami (24 sztuki) kuchni, zgodny 1:1 z repozytorium
   (wymiary, ilości, słoje, okleina, otwory co do 0,0 mm, puszki zawiasów),
2. ten rozkrój dodany do koszyka na koncie użytkownika, obok istniejącego `21825702` (pralnia + garderoba),
3. dokumentacja zamówienia w repozytorium wg `wspolne/zamowienia/README.md`,
4. raport dla użytkownika: numer rozkroju, kwota brutto/netto, termin, odstępstwa, rzeczy do zrobienia ręcznie.

Zamówienie pralni i garderoby (`21825702`) zostało właśnie złożone tą samą metodą. Jego przebieg, pułapki kalkulatora
i mapa DOM są opisane w `wspolne/centrum_meble.md` (sekcje 3–11) i w
`wspolne/zamowienia/2026-11-22_centrum-meble_pralnia-garderoba_21825702.md`. Przeczytaj oba pliki w całości, zanim
otworzysz przeglądarkę. Kuchnia jest ok. 4 razy mniejsza (21 wierszy zamiast 85), więc całość powinna zająć
20–40 minut.

## Granice (bezwzględne)

- NIE przechodź do kasy, nie wybieraj dostawy, nie płać. Kończysz na `/koszyk/`.
- NIE zmieniaj, nie usuwaj i nie przeliczaj rozkroju `21825702` ani innych pozycji koszyka. Jeśli dodanie kuchni
  w jakikolwiek sposób dotyka `21825702`, zatrzymaj się i zapytaj.
- NIE wpisuj haseł. Jeśli konto jest wylogowane, poproś użytkownika, żeby zalogował się sam.
- NIE klikaj weryfikacji Cloudflare („czy nie jesteś botem”) ani żadnej CAPTCHA. Poproś użytkownika, żeby ją
  przeszedł w tej samej przeglądarce, i poczekaj.
- NIE wysyłaj maili do sklepu. Mail o usłojeniu frontów tylko przygotuj (punkt 9).
- Repozytorium jest źródłem prawdy. Jeśli coś w tym prompcie nie zgadza się z plikami w `kuchnia/`, wygrywają pliki;
  zgłoś rozbieżność użytkownikowi, zanim wpiszesz dane.
- W repozytorium nie zmieniaj modelu ani katalogów innych pomieszczeń. Piszesz tylko dokumentację zamówienia.

## Narzędzia przeglądarki

Użyj **Chrome DevTools MCP** (`chrome-devtools-mcp@latest`, narzędzie `evaluate_script`) podłączonego do Chrome
użytkownika, w którym jest jego sesja `centrum.meble.pl`. Przy `21825702` dopiero `evaluate_script` dał szybkie
i bezbłędne wpisywanie i audyt (minuty zamiast godzin klikania po drzewie dostępności). Jeśli Chrome DevTools MCP nie
jest dostępny, użyj Claude in Chrome (`javascript_tool`), a w ostateczności zwykłego klikania.

Zasady automatyzacji (z `wspolne/centrum_meble.md`, sekcja 10):
- wywołuj funkcje strony (`setTypFrontu`, `changeSelectPuszka`, `dodajNawiert`, `skopiujNawiert`, `przelicz` itd.)
  i ustawiaj pola po ID (`#szer_{b}_{f}`, `#wiercenia_w_plaszczyznie_{b}_{f}_{r}_…`, `#wiercenia_w_czole_…`),
  po każdej zmianie wywołując ich zdarzenia `onblur`/`onchange`, tak jak robi to strona,
- ściśle sekwencyjnie: po każdym zdarzeniu czekaj, aż zniknie `div.blockUI`, i dodaj 400–500 ms przerwy;
  nigdy równolegle,
- rozwinięty tylko jeden wiersz naraz (`pokazUkryjFormatke`),
- zmiany w sesji PHP są ulotne do `Przelicz koszty`: po każdej partii klikaj `przelicz()` i zapisuj nowy numer
  `/rozkroj,rXXXXXXXX` (checkpoint),
- nie używaj lokatorów szukających po tekście na całej stronie.

## Dane wejściowe z repozytorium

Najpierw `git pull` na `main`, potem uruchom:
```
python3 wspolne/pipeline/run.py --wszystkie --sprawdz
```
Wynik musi być zgodny („wyniki zgodne z repozytorium”). Jeśli nie, zatrzymaj się.

Pliki:
- `kuchnia/wyniki/kalkulator_nawierty.csv`: 12 pozycji z otworami (każdy wiersz z numerem `LP` = jeden wiersz
  w kalkulatorze; LP11 to 4 identyczne sztuki WSD, WSS, WSP-1, WSP-2). Kolumny: `SZER=DL`, `WYS=SZ`, `OKLEJ KRAWEDZ NR`,
  `RODZAJ` (`PLASZCZYZNA`/`CZOŁO`), `POWIERZCHNIA/KRAWEDZ` (`Przód`/`Tył`/`Krawędź N`), `X lub ODLEGLOSC OD 0`, `Y`,
  `SREDNICA`, `GLEBOKOSC` (`przelotowo` = `przelot`). Plik ma BOM, czytaj jako `utf-8-sig`.
- `kuchnia/wyniki/formatki.csv`: wszystkie 15 pozycji / 18 szt. / 4,43 m² (stąd SOD, WSZ i F1, które nie mają wierszy
  w `kalkulator_nawierty.csv`, oraz kolumna UWAGI).
- `kuchnia/zamowienie/fronty_metod.csv`: 6 frontów szuflad IKEA METOD (FM1–FM6) z otworami.
- `kuchnia/ustalenia.md` (decyzje, szczególnie wpisy o F1, METOD i półkach P1/P3), `kuchnia/komponenty.md`,
  `kuchnia/wyniki/podsumowanie.json`, `kuchnia/wyniki/arkusz_nawiertow.pdf`.
- `kuchnia/zamowienie/wycena.md`: stara wycena, NIEAKTUALNA (tylko orientacyjnie).

Przygotuj deterministycznie w Pythonie (bez ręcznego przepisywania) w katalogu roboczym poza repozytorium:
- `import_ku_18mm.csv` do `WCZYTAJ PLIK` (format z `wspolne/centrum_meble.md`, sekcja 3; nazwy z prefiksem `KU-`),
- `order_spec.json`: pełna specyfikacja 21 wierszy (wymiary, SZT, słoje, krawędzie, szablon, lista otworów,
  puszki) z asercjami sum z punktu „Sumy kontrolne”.

## Parametry zlecenia

- Płyta (jedna płyta w nowym rozkroju): `Płyta meblowa EGGER H3710 ST12 Orzech Carini naturalny 18 mm`.
- Okleina: `Obrzeże ABS H3710 ST12 Orzech Carini naturalny 23 x 0.8 mm EGGER` na wszystkich oklejanych krawędziach,
  także na F1 i frontach METOD (bez laserowej 1,0 mm: wyłącza `Wręgowanie`, a fronty METOD mają otwory).
  Przy frontach METOD użytkownik zamawiał wcześniej kolejność „kryjące długie”: jeśli kalkulator ma taką opcję,
  wybierz ją dla FM1–FM6 i F1; jeśli nie ma, zapisz to w raporcie.
- Dekor jest usłojony: kolumna `Słoje` NIE może być `0`.
- Wariant cięcia: `PREMIUM (+standard)`, jak w `21825702`. W raporcie podaj też cenę wariantu `Standard`, jeśli
  podsumowanie ją pokazuje.
- Osobny rozkrój zamiast dopisywania do `21825702`: inna płyta, więc wspólny rozkrój nie oszczędza arkuszy, a ryzykuje
  zmianę zweryfikowanego zamówienia.

### Słoje (do potwierdzenia na starcie)

Decyzje w repozytorium: F1 i fronty METOD mają słoje NA WYSOKOŚĆ (pionowo na ścianie). Dla korpusów i półek
w repozytorium nie ma wpisu; propozycja: słoje wzdłuż DL (dłuższego wymiaru) każdej formatki, czyli pionowo na bokach,
tyłach i F1, wzdłuż szerokości szafki na wieńcach, półkach i dnach, wzdłuż długości na P1 i P3. Zanim zaimportujesz CSV,
zadaj użytkownikowi jedno pytanie: czy potwierdza tę propozycję. Odpowiedź zapisz w `kuchnia/ustalenia.md`.

Kod w kolumnie `Słoje`: według wcześniejszych ustaleń `1` = słoje wzdłuż Wysokości, `2` = wzdłuż Szerokości.
Sprawdź to na jednym wierszu testowym w kalkulatorze (podgląd/oznaczenie kierunku słojów), zanim wczytasz całość.

## Lista 21 wierszy kalkulatora (Szer × Wys w mm, płyta 18 mm)

Wiersze z otworami: wymiary, krawędzie i otwory dokładnie z `kalkulator_nawierty.csv` (`Szer = DL`, `Wys = SZ`,
krawędzie wg kolumny `OKLEJ KRAWEDZ NR`: 1 = góra, 2 = prawa, 3 = dół, 4 = lewa).

| WIERSZ | NAZWA | SZER × WYS | SZT | SŁOJE | OKLEINA (KRAWĘDZIE) | SZABLON |
|---|---|---|---|---|---|---|
| 1 | KU-P1 | 804 × 400 | 1 | wzdłuż SZER | 1 | Wręgowanie: 3 otwory w czole |
| 2 | KU-P3 | 1978 × 200 | 1 | wzdłuż SZER | 1 | Wręgowanie: 5 otworów w czole |
| 3 | KU-SOB-1 | 1154 × 304 | 1 | wzdłuż SZER | 1 | Wręgowanie |
| 4 | KU-SOB-2 | 1154 × 304 | 1 | wzdłuż SZER | 1 | Wręgowanie |
| 5 | KU-SOT | 1154 × 516 | 1 | wzdłuż SZER | brak | Wręgowanie |
| 6 | KU-SOW | 516 × 286 | 1 | wzdłuż SZER | 1 | Wręgowanie |
| 7 | KU-SOP | 516 × 286 | 1 | wzdłuż SZER | 1 | Wręgowanie |
| 8 | KU-WSB-1 | 1154 × 300 | 1 | wzdłuż SZER | 1 | Wręgowanie |
| 9 | KU-WSB-2 | 1154 × 300 | 1 | wzdłuż SZER | 1 | Wręgowanie |
| 10 | KU-WST | 1154 × 238 | 1 | wzdłuż SZER | brak | Wręgowanie |
| 11 | KU-WSD, WSS, WSP-1, WSP-2 | 282 × 238 | 4 | wzdłuż SZER | 2 | Wręgowanie |
| 12 | KU-WSW | 282 × 238 | 1 | wzdłuż SZER | 2 | Wręgowanie |
| 13 | KU-SOD | 514 × 284 | 1 | wzdłuż SZER | 1 | bez nawiertów |
| 14 | KU-WSZ | 236 × 165 | 1 | wzdłuż SZER | brak | bez nawiertów |
| 15 | KU-F1 | 549 × 1151 | 1 | wzdłuż WYS | 1, 2, 3, 4 | Front prawy (patrz niżej) |
| 16 | KU-FM1 usłojenie 21a | 597 × 142 | 1 | wzdłuż WYS | 1, 2, 3, 4 | Wręgowanie: 4 otwory |
| 17 | KU-FM2 usłojenie 21b | 597 × 397 | 1 | wzdłuż WYS | 1, 2, 3, 4 | Wręgowanie: 12 otworów |
| 18 | KU-FM3 usłojenie 21c | 597 × 397 | 1 | wzdłuż WYS | 1, 2, 3, 4 | Wręgowanie: 12 otworów |
| 19 | KU-FM4 usłojenie 22a | 597 × 197 | 1 | wzdłuż WYS | 1, 2, 3, 4 | Wręgowanie: 8 otworów |
| 20 | KU-FM5 usłojenie 22b | 597 × 197 | 1 | wzdłuż WYS | 1, 2, 3, 4 | Wręgowanie: 8 otworów |
| 21 | KU-FM6 usłojenie 22c | 597 × 397 | 1 | wzdłuż WYS | 1, 2, 3, 4 | Wręgowanie: 12 otworów |

Tabela to skrót. Jeśli wymiar, SZT lub krawędź różni się od plików, wygrywają pliki i zgłaszasz rozbieżność.
Kalkulator po imporcie CSV potrafi sam zaznaczyć krawędzie 3 i 4 w 0,8 mm: popraw okleinę w każdym wierszu
(wiersze 5, 10 i 14 bez okleiny).

### Otwory w korpusach i półkach (wiersze 1–12)

Wpisuj wprost z `kalkulator_nawierty.csv`, bez przeliczania: strona `Tył (B)` w kalkulatorze NIE jest odbita
(rzut „na wylot” od przodu, początek w lewym dolnym rogu widoku z przodu), tak samo jak w naszym CSV.
Wszystkie średnice i głębokości są w zakresie kalkulatora (płaszczyzna: Ø3, 5, 8, 15 do 15 mm lub przelot;
czoło: Ø4 i Ø8 do 35 mm). Rozkład, który ma się zgadzać po wpisaniu (liczba wpisów w CSV):

| RODZAJ | STRONA / KRAWĘDŹ | Ø × GŁĘB. | WPISÓW |
|---|---|---|---|
| płaszczyzna | Przód | 5 × przelot | 21 |
| płaszczyzna | Tył | 5 × przelot | 29 |
| płaszczyzna | Przód / Tył | 15 × 14 (Minifix) | 4 / 1 |
| płaszczyzna | Przód | 8 × 10 (kołki) | 6 |
| płaszczyzna | Przód / Tył | 5 × 10 (podpórki) | 2 / 2 |
| płaszczyzna | Przód | 5 × 11 | 5 |
| płaszczyzna | Przód | 5 × 5 (środki otworów pod rurę) | 5 |
| płaszczyzna | Przód / Tył | 3 × 5 (piloty wkrętów okapu) | 2 / 2 |
| płaszczyzna | Tył | 3 × 12 (piloty prowadników zawiasów) | 6 |
| czoło | Krawędź 1 / 3 / 4 | 4 × 35 (konfirmaty) | 11 / 13 / 8 |
| czoło | Krawędź 2 / 3 | 8 × 22 (kołki) | 4 / 2 |
| czoło | Krawędź 2 / 3 | 8 × 33 (Minifix) | 2 / 3 |
| czoło | Krawędź 3 | 8 × 35 (pręty M8 w P1 i P3) | 8 |

Razem 136 wpisów, 154 otwory z uwzględnieniem SZT. Policz tę tabelę sam z CSV i porównaj (jeśli CSV się zmienił,
wygrywa CSV). `wielowiert` i `skopiujNawiert` są dozwolone, ale przy tej wielkości zamówienia pojedyncze wpisy
przez `evaluate_script` są prostsze; jeśli kompresujesz serie, zrób test round-trip do 0,0 mm.

Bez wręgów i bez dodatkowych otworów: rowki pod profile LED w P1 i P3, otwory Ø160/Ø170, wycięcia U, wycięcie w SOD
i otwór na przewód w SOT robi użytkownik sam (w CSV są tylko nawierty środków Ø5 × 5).

### Front F1 (wiersz 15)

- `Szer = 549`, `Wys = 1151` (zawiasy wiercone wzdłuż Wys).
- Szablon `Front prawy`: zawiasy po prawej stronie patrząc na front od strony kuchni (na boku SOB-2). Zawiasy
  w garderobie F2 „PRAWY” były wpisane tym szablonem. Na podglądzie SVG sprawdź, że puszki są przy prawej krawędzi
  (Krawędź 2); jeśli widać inaczej, zatrzymaj się i zapytaj.
- `Typ zawiasu`: `BLUM puszka 35mm (wkręty)` (Blum CLIP top 70T3550.TL na wkręty, NIE `inserta`).
- `Odległość od krawędzi`: `22.50`.
- 3 puszki, środki 337,5 / 697,5 / 1051 od dołu frontu (100 od góry):
  `x1` (od góry) = `100`, `x2` (od dołu) = `337.5` (`ręcznie`), `x3` (od góry, `ręcznie`) = `453.5`
  (1151 − 697,5). Nie zostawiaj `symetrycznie` (stawia środkową puszkę w połowie frontu).
- Okleina 0,8 mm na 4 krawędziach.

### Fronty METOD (wiersze 16–21)

- Wymiary, nazwy i otwory z `kuchnia/zamowienie/fronty_metod.csv`: otwory Ø5 × 13 na stronie `Tył (B)`
  na X = 32 i 565 oraz Y z kolumny NAWIERTY. CSV podaje X od lewego dolnego rogu widoku od tyłu; otwory są symetryczne
  względem środka szerokości (32 + 565 = 597), więc w kalkulatorze wpisujesz te same liczby bez odbijania. Y liczony
  od dolnej krawędzi frontu.
- Nazwy „usłojenie 21a … 22c” zostają w nazwie wiersza (po nich sklep dopasuje usłojenie, patrz punkt 9).

## Sumy kontrolne (przed `Do koszyka`)

- 21 wierszy, 24 sztuki, ok. 5,46 m² (4,43 z `podsumowanie.json` + 6 frontów METOD; policz dokładnie w `order_spec.json`).
- W `Podsumowanie kosztów zlecenia`:
  - `Usługa wiercenia` dla frontów z szablonem zawiasów: **1 szt.** (F1),
  - `Usługa wiercenia` dla `Wręgowania i nawiertów`: **21 szt.** (15 sztuk z wierszy 1–12 + 6 frontów METOD),
  - jedna płyta H3710 18 mm, jedno obrzeże ABS H3710 0,8 mm (sprawdź dostępność, np. `pow. 50 mb`; jeśli brak lub
    długi termin, zgłoś).
- Otwory: 136 wpisów / 154 z SZT w wierszach 1–12, 56 otworów we frontach METOD, 3 puszki w F1.

## Przebieg

1. **Pre-flight.** Przeczytaj pliki z sekcji „Dane wejściowe”. Sprawdź logowanie (`/moje_konto/`) i zawartość koszyka:
   ma tam być `21825702` (5 924,63 PLN) i nic nieoczekiwanego. Zapisz stan koszyka. Zadaj użytkownikowi pytanie
   o słoje (jedno pytanie, z propozycją).
2. **Test na czystym kalkulatorze** (`https://centrum.meble.pl/rozkroj,plyty-meblowe`): wybierz płytę H3710 ST12
   18 mm i obrzeże H3710 0,8 mm. Na jednym wierszu testowym sprawdź kod `Słoje`, a na F1 szablon `Front prawy`
   z wkrętami i ręcznymi `x2`/`x3` (podgląd SVG). Usuń wiersz testowy albo zacznij od nowa.
3. **Import** `import_ku_18mm.csv` przez `WCZYTAJ PLIK`. Sprawdź 21 wierszy, wymiary, SZT i słoje.
4. **Partia A:** wiersze bez wręgowania (13, 14, 15): okleina, szablon, F1. `Przelicz koszty`, zapisz numer
   rozkroju, sprawdź `Usługa wiercenia` frontów = 1 szt.
5. **Partie B:** wiersze 1–12 w paczkach po 3–4: rozwiń wiersz, popraw okleinę, `Wręgowanie`, wpisz otwory, sprawdź
   SVG (`<circle>` = 2 + otwory w płaszczyźnie, czerwone kreski = otwory w czole, gruba linia = okleina), zwiń.
   Po paczce `Przelicz koszty`, zapisz numer rozkroju, sprawdź przyrost `Usługa wiercenia` o SZT paczki.
6. **Partia C:** fronty METOD 16–21 tak samo.
7. **Audyt końcowy 100%** (wzorzec z `wspolne/centrum_meble.md`, sekcja 11 pkt 7): na ostatnim `/rozkroj,r<ID>`
   odczytaj przez `evaluate_script` cały DOM wszystkich wierszy (wymiary, SZT, słoje, krawędzie i grubość obrzeża,
   szablon, `typ_zawiasu`, `puszka_x*`, wszystkie wpisy otworów) i porównaj automatycznie z `order_spec.json`
   (wymagane 0 różnic, odchyłka 0,00 mm). Dodatkowo sparsuj widok wydruku
   `/rozkroj/go/ajaxRequest,drukuj/art<ID>.html?typ_rozkroju=1`. Różnice popraw i powtórz audyt.
8. **Koszyk:** ostatni `Przelicz koszty`, przeczytaj wszystkie linie podsumowania, `Do koszyka` w wariancie
   `PREMIUM (+standard)`, otwórz `/koszyk/` i sprawdź: nowy numer rozkroju, kwota, termin, opcja odpadów
   (domyślnie niewybrana) oraz że `21825702` jest nienaruszony (ta sama kwota). Stop.
9. **Mail o usłojeniu (szkic, nie wysyłaj):** prośba, żeby fronty „usłojenie 21a, 21b, 21c” i „22a, 22b, 22c”
   wyciąć z jednego pasa płyty kolejno w pionie, tak by usłojenie przechodziło między frontami w kolumnie, z numerem
   rozkroju i załącznikiem `kuchnia/zamowienie/fronty_metod_rysunek.pdf`. Szkic pokaż użytkownikowi.
10. **Dokumentacja** wg `wspolne/zamowienia/README.md`: plik
    `wspolne/zamowienia/2026-11-DD_centrum-meble_kuchnia_<ID>.md` (metadane, koszty z koszyka, sumy kontrolne
    vs repozytorium, kontrole i audyt, odstępstwa, historia rewizji z numerami checkpointów, manifest wierszy z prefiksem
    `KU-`), wiersz w tabeli rejestru w `wspolne/zamowienia/README.md`, wpis z datą w `kuchnia/ustalenia.md`
    (numer rozkroju, kwota, słoje, wariant). Commit i push według zasad z `CLAUDE.md` i `wspolne/zamowienia/README.md`.

## Kiedy się zatrzymać i zapytać

- rozbieżność między tym promptem a plikami repozytorium, albo `run.py --sprawdz` niezgodny,
- kalkulator nie przyjmuje wartości (średnica, głębokość, pozycja puszki, wymiar) albo nie ma płyty/obrzeża H3710,
- jakakolwiek zmiana w `21825702` lub nieoczekiwana pozycja w koszyku,
- logowanie lub Cloudflare (użytkownik robi to sam),
- audyt końcowy z różnicami, których nie umiesz usunąć.

## Raport końcowy dla użytkownika

Krótko: numer rozkroju i link, kwota brutto/netto (i `Standard`, jeśli widoczna), termin realizacji, wynik audytu
(0 różnic), lista rzeczy do zrobienia ręcznie po dostawie (z `kuchnia/komponenty.md` i kolumny UWAGI: poszerzenie
konfirmatów do Ø7, pogłębienie otworów prętów do 85, rowki LED, otwory Ø160/Ø170 i wycięcia U, wycięcie SOD, otwór
na przewód w SOT), szkic maila o usłojeniu i informacja, że koszyk czeka na płatność przez użytkownika.
