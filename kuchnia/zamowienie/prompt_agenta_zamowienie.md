# Prompt dla agenta: zamówienie mebli do kuchni w centrum.meble.pl

> Wklej całość poniżej linii jako pierwszą wiadomość do agenta (Claude Code lub inny agent z dostępem do repozytorium
> `toboche/home-furniture` i do przeglądarki Chrome przez MCP). Stan danych: `main` po PR z 2026-11-22.

---

## Rola i cel

Jesteś agentem, który składa w `centrum.meble.pl` zamówienie robocze na formatki do kuchni (pomieszczenie `kuchnia/`
w repozytorium `toboche/home-furniture`). Rozmawiasz po polsku. Twoją pracę zweryfikuje niezależnie inny agent: zapisuj numery checkpointów `/rozkroj,rXXXXXXXX` i
zostaw w raporcie numer końcowego rozkroju oraz ścieżki `order_spec.json` i wyników audytu. Kody formatek piszesz WYŁĄCZNIE DUŻYMI LITERAMI.

Efekt końcowy:
1. nowy, osobny rozkrój `/rozkroj,rXXXXXXXX` z 21 wierszami (23 sztuki) kuchni, zgodny 1:1 z repozytorium
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
- `kuchnia/wyniki/kalkulator_nawierty.csv`: 11 pozycji z otworami (każdy wiersz z numerem `LP` = jeden wiersz
  w kalkulatorze; LP10 to 2 identyczne sztuki WSD i WSS). Kolumny: `SZER=DL`, `WYS=SZ`, `OKLEJ KRAWEDZ NR`,
  `RODZAJ` (`PLASZCZYZNA`/`CZOŁO`), `POWIERZCHNIA/KRAWEDZ` (`Przód`/`Tył`/`Krawędź N`), `X lub ODLEGLOSC OD 0`, `Y`,
  `SREDNICA`, `GLEBOKOSC` (`przelotowo` = `przelot`). Plik ma BOM, czytaj jako `utf-8-sig`.
- `kuchnia/wyniki/formatki.csv`: wszystkie 15 pozycji / 17 szt. / 4,13 m² (stąd SOD, WSZ, WSP i F1, które nie mają wierszy
  w `kalkulator_nawierty.csv`, oraz kolumna UWAGI).
- `kuchnia/zamowienie/fronty_metod.csv`: 6 frontów szuflad IKEA METOD (FM1–FM6) z otworami.
- `kuchnia/ustalenia.md` (decyzje, szczególnie wpisy o F1, METOD i półkach P1/P3), `kuchnia/komponenty.md`,
  `kuchnia/wyniki/podsumowanie.json`, `kuchnia/wyniki/arkusz_nawiertow.pdf`.
- `kuchnia/zamowienie.md`: słoje, okleina, krawędzie i szablon każdego wiersza, konfiguracja F1, sumy kontrolne.
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

### Słoje, okleina krawędzi i szablony

Pełna tabela 21 wierszy (kody, SZER × WYS, SZT, słoje, krawędzie z okleiną, szablon) jest w `kuchnia/zamowienie.md`
i jest częścią specyfikacji: przepisz ją do `order_spec.json`. Słoje: na elementach pionowych pionowo, na poziomych
równolegle do przodu, na F1, WSZ i frontach METOD na wysokość. Uwaga: przy `SZER = DL` boki i tyły (1154 × …) mają
słoje „na szerokość”, a poziome elementy WS (282 × 238) „na wysokość”. Słoje są potwierdzone przez użytkownika (2026-11-23). Kod w kolumnie `Słoje` CSV sprawdź na jednym wierszu testowym
(oznaczenie kierunku słojów w kalkulatorze), zanim wczytasz całość.

Wiersze z otworami: wymiary, krawędzie i otwory dokładnie z `kalkulator_nawierty.csv` (`Szer = DL`, `Wys = SZ`,
krawędzie wg kolumny `OKLEJ KRAWEDZ NR`: 1 = góra, 2 = prawa, 3 = dół, 4 = lewa). Jeśli wymiar, SZT lub krawędź
w `zamowienie.md` różni się od plików generowanych, wygrywają pliki generowane i zgłaszasz rozbieżność.
Kalkulator po imporcie CSV potrafi sam zaznaczyć krawędzie 3 i 4 w 0,8 mm: popraw okleinę w każdym wierszu
(wiersze 5, 9 i 13 bez okleiny).

### Otwory w korpusach i półkach (wiersze 1–11)

Wpisuj wprost z `kalkulator_nawierty.csv`, bez przeliczania: strona `Tył (B)` w kalkulatorze NIE jest odbita
(rzut „na wylot” od przodu, początek w lewym dolnym rogu widoku z przodu), tak samo jak w naszym CSV.
Wszystkie średnice i głębokości są w zakresie kalkulatora (płaszczyzna: Ø3, 5, 8, 15 do 15 mm lub przelot;
czoło: Ø4 i Ø8 do 35 mm). Stan 2026-11-24: 108 wpisów, 114 otworów z uwzględnieniem SZT. Policz z CSV rozkład wg rodzaju,
strony / krawędzi, średnicy i głębokości i porównaj po wpisaniu (jeśli CSV się zmienił, wygrywa CSV). `wielowiert`
i `skopiujNawiert` są dozwolone, ale przy tej wielkości zamówienia pojedyncze wpisy przez `evaluate_script` są prostsze;
jeśli kompresujesz serie, zrób test round-trip do 0,0 mm.

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

- Wymiary, nazwy i otwory z `kuchnia/zamowienie/fronty_metod.csv`: otwory Ø5 × 12 na stronie `Tył (B)`
  na X = 32 i 565 oraz Y z kolumny NAWIERTY. CSV podaje X od lewego dolnego rogu widoku od tyłu; otwory są symetryczne
  względem środka szerokości (32 + 565 = 597), więc w kalkulatorze wpisujesz te same liczby bez odbijania. Y liczony
  od dolnej krawędzi frontu.
- Nazwy „usłojenie 21a … 22c” zostają w nazwie wiersza (po nich sklep dopasuje usłojenie, patrz punkt 9).

## Sumy kontrolne (przed `Do koszyka`)

- 21 wierszy, 23 sztuki, ok. 5,16 m² (4,13 z `podsumowanie.json` + 6 frontów METOD; policz dokładnie w `order_spec.json`).
- W `Podsumowanie kosztów zlecenia`:
  - `Usługa wiercenia` dla frontów z szablonem zawiasów: **1 szt.** (F1),
  - `Usługa wiercenia` dla `Wręgowania i nawiertów`: **18 szt.** (12 sztuk z wierszy 1–11 + 6 frontów METOD),
  - jedna płyta H3710 18 mm, jedno obrzeże ABS H3710 0,8 mm (sprawdź dostępność, np. `pow. 50 mb`; jeśli brak lub
    długi termin, zgłoś).
- Otwory: 108 wpisów / 114 z SZT w wierszach 1–11, 56 otworów we frontach METOD, 3 puszki w F1.

## Przebieg

1. **Pre-flight.** Przeczytaj pliki z sekcji „Dane wejściowe”. Sprawdź logowanie (`/moje_konto/`) i zawartość koszyka:
   ma tam być `21825702` (5 924,63 PLN) i nic nieoczekiwanego. Zapisz stan koszyka. Zadaj użytkownikowi pytanie
   o słoje tylko wtedy, gdy kalkulator nie pozwala ich ustawić jak w `kuchnia/zamowienie.md`.
2. **Test na czystym kalkulatorze** (`https://centrum.meble.pl/rozkroj,plyty-meblowe`): wybierz płytę H3710 ST12
   18 mm i obrzeże H3710 0,8 mm. Na jednym wierszu testowym sprawdź kod `Słoje`, a na F1 szablon `Front prawy`
   z wkrętami i ręcznymi `x2`/`x3` (podgląd SVG). Usuń wiersz testowy albo zacznij od nowa.
3. **Import** `import_ku_18mm.csv` przez `WCZYTAJ PLIK`. Sprawdź 21 wierszy, wymiary, SZT i słoje.
4. **Partia A:** wiersze bez wręgowania (12, 13, 14, 15): okleina, szablon, F1. `Przelicz koszty`, zapisz numer
   rozkroju, sprawdź `Usługa wiercenia` frontów = 1 szt.
5. **Partie B:** wiersze 1–11 w paczkach po 3–4: rozwiń wiersz, popraw okleinę, `Wręgowanie`, wpisz otwory, sprawdź
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
