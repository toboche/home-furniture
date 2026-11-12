# Przedpokój: ustalenia

Oznaczenia wymiarów na rysunkach i w tabelach: TYLKO DUŻE LITERY.
Założenia domyślne: `wspolne/zasady.md`; różnice zapisujemy tutaj. Pomiary: `pomiary.md`. Źródła: `zrodla/`.

## Pomieszczenie
- Przedpokój A/P02 01 (rzut: `zrodla/rzut_z_zaznaczona_szafa.png`, szafa zaznaczona na zielono). Wymiary z rzutu poglądowe.
- Szafa w narożniku między drzwiami łazienki D2 a pionem EI60, obok drzwi wejściowych DM1, ze zintegrowanym szezlongiem.
  Część szafy zasłania rozdzielnicę: trzeba zapewnić do niej dostęp.
- Układ modelu: ściana tylna (z = 0) = ściana z D2 i rozdzielnicą; ściana prawa (x = W) = ściana z DM1;
  pion w narożniku tylnej i prawej. Lewa i przednia ściana są umowne (przedpokój ciągnie się dalej).
  X w pomiarach od szczeliny D2; w modelu ta szczelina leży na x = XO = 1000.
- D2 (łazienka) otwiera się do przedpokoju, zawiasy od strony szafy; otwarte skrzydło dochodzi do szezlonga.
  Kolizja zaakceptowana, ta część ma pozostać użyteczna. DM1 otwiera się do środka, zawiasy po stronie dalszej od szafy.
- Podłoga docelowa położona (płytki 60 × 60). Białe listwy przypodłogowe zostają, można je zdjąć, jeśli przeszkadzają.
- Na czole pionu: domofon (na okrągłym zaczepie, kabel ze ściany) i włącznik światła.

## Bryła (decyzje 2026-11-12)
- Wzór: `zrodla/wzor_zabudowy.jpg` (szezlong z tapicerowanym siedziskiem, wysoka szafa do sufitu, zaślepka na pionie
  z domofonem i włącznikiem, otwarta wnęka na buty u dołu). Wprowadzamy zmiany opisane niżej.
- Szafa do sufitu (luz 3 mm, góra korpusów 2661).
- Korpusy szafy i pawlacza: głębokość 775. Front w jednej płaszczyźnie z zaślepką na pionie (z = 795).
  W modelu korpusy odsunięte od ściany o 2 (przy podłodze); pion przy suficie wystaje do 783, więc u góry użytkownik
  dokłada dystans (do 8), żeby całość licowała się z licem pionu.
- Fronty bez uchwytów, otwierane TIP-ON. Fronty na razie białe; kolor do decyzji.
- Fronty = wymiar korpusu minus 3 mm: 3 mm odstępu między frontami i między frontem a zaślepką.
- Otwarta wnęka na buty 0–177 pod szezlongiem i pod szafą; fronty nad wnęką kończą się równo z jej krawędzią.

### Szezlong SZ (X 20–540)
- Odstęp 20 od szczeliny D2. Szerokość 520, głębokość 500 z frontem, wysokość 460 razem z poduszką 30 (poduszka: założenie).
- Wnęka 0–177, dno 177–195, szuflada 195–412 (ok. 177 w środku), blat 412–430, poduszka 430–460.
- Siedzisko jest schowkiem na buty: szuflada od frontu, push to open (założenie: szuflada, nie klapa).
- Front szuflady F1 zasłania krawędź blatu: 177–430.
- D2 otwiera się do ok. 92°; klamka (70) mija szezlong przed jego frontem.

### Szafka nad szezlongiem NS (zasłania rozdzielnicę)
- Korpus 50, lico frontu 68 od ściany (do sprawdzenia z zawiasami). Bez tyłu (rozdzielnica).
- Stoi na blacie szezlonga (od 430), drzwi F2 od 461,5 (nad poduszką) do 2159,5, zawiasy od D2.
- Drzwiczki rozdzielnicy (zawiasy po prawej, krawędź ok. X 507) otwierają się przy prawym boku NS (X 522). Prawy bok NS
  leży na ramce rozdzielnicy (X 522–537): ramka musi być równo ze ścianą (do sprawdzenia).

### Pawlacz PW nad szezlongiem
- 500 od sufitu (2161–2661), front F3 w linii szafy wysokiej, jedno skrzydło, zawiasy od D2.
- Dół pawlacza (2161) powyżej skrzydła D2 (2030): D2 otwiera się pod nim.

### Szafa wysoka SD + SG (X 540–1097, szerokość 557)
- Luz 3 przy boku pionu (wcześniej w szkicach 560 do samego pionu).
- Korpusy osobno: dolny SD (0–2161) i górny SG (2161–2661), łatwiejszy montaż.
- Fronty bez podziału pionowego: F4 dół (554 × 1982,5), F5 góra (554 × 498,5); zawiasy po prawej (od pionu).
  Otwarte F4 wchodzi ok. 560 w przejście (1235) i może zahaczać o otwarte DM1.
- Wnętrze SD: przestrzeń 195–495 z szufladą wewnętrzną, półka 495, przestrzeń 513–813, półka 813, strefa kurtek
  831–2143 z drążkiem (oś 2093, 50 pod wieńcem). Część górna SG bez półki.

### Zaślepka na pionie F6
- Od podłogi do sufitu (0–2661), szerokość 427,5: 3 mm od frontu F4 (wystaje 1,5 poza narożnik pionu), 2 mm od ściany z DM1.
- Przyklejona mocnym klejem do czoła pionu, bez stelaża.
- Otwory wierci użytkownik: Ø60 na kabel domofonu (środek 246,5 od lewej krawędzi zaślepki, 1474 od dołu)
  i pod dystans włącznika (środek 299,5 od lewej, 1214 od dołu; średnica wg dystansu).
- Na istniejącą puszkę włącznika zostanie dodany dystans (przedłużka), włącznik montowany na licu zaślepki.

## Konstrukcja (2026-11-12)
- Płyta 18 mm (`wspolne/zasady.md`), konfirmaty w obrębie korpusu, plecy 18 między bokami.
- Moduły: SZ, NS, PW, SD, SG (kody formatek zaczynają się od nazwy modułu).
- Okucia: `komponenty.md`. Zawiasy CLIP top bez sprężyny (TIP-ON wymaga zawiasów bez sprężyny), TIP-ON do drzwi,
  prowadnice push to open w szezlongu, zwykłe prowadnice z cichym domykiem w szufladzie wewnętrznej.
- Skrzynki szuflad (warstwa „Szuflady (skrzynki)”, domyślnie ukryta) są tylko poglądowe: wymiary po wyborze prowadnic.

## Etapy
1. Wymiary: GOTOWE (2026-11-12)
2. Bryła: GOTOWE (2026-11-12)
3. Konstrukcja i formatki: wersja wstępna w modelu (2026-11-12)
4. Skrzynki szuflad, dokładne położenie TIP-ON, instrukcja montażu: DO ZROBIENIA
5. Ręczna weryfikacja przed zamówieniem: DO ZROBIENIA

## Do ustalenia
- Średnica otworu pod dystans włącznika (zależy od dystansu).
- Grubość poduszki (przyjęte 30).
- Szafka NS (korpus 50): czy płytka głębokość pozwala na prowadniki zawiasów i TIP-ON (alternatywa: zatrzask push na wieńcu).
- Ramka rozdzielnicy pod prawym bokiem NS: równo ze ścianą?
- Skrzynki szuflad i dystans 20 przy szufladzie wewnętrznej (zawiasy F4 po tej samej stronie).

## Dziennik zmian
- 2026-11-12: nowe pomieszczenie: pomiary, bryła, konstrukcja wstępna (formatki, zawiasy, wyniki).
