# Zestawienie okuć i elementów (pralnia) – stan v58 (do przeglądu, niewypchnięty), 2026-11-11
Wersja robocza do niezależnej weryfikacji. Wymiary w mm. Kody wymiarów wielkimi literami.

## Płyta
- Egger W1200 ST9 „Biały porcelanowy" 18 mm, centrum.meble.pl; 40 pozycji / 52 sztuki / 15,55 m² (formatki.csv, razem z L1P).
- Okleina: fronty 1,0 mm bezszwowa (szablony zawiasów), reszta ABS 0,8 mm z nawiertami.

## Zawiasy i prowadniki (Blum)
| Element | Kod | Ilość | Uwagi |
|---|---|---|---|
| Zawias nakładany 110°, INSERTA, soft-close | 71B3590 | 15 | F1, F2, F3, F4, F7, F8 po 2; F9 ×3 (razem 15). Puszka Ø35×13, odległość 22,5 od krawędzi, 2 otwory Ø8 co 45 (INSERTA – wybór typu w kalkulatorze meble.pl) |
| Prowadnik krzyżakowy 37/32 do wkrętów (przykręcany do ścianki) | 173H7100 | 15 | wkręty 609.1700 (17 mm), bez nawiertu |
| Zawias do drzwi równoległych 95° (F5↔F6) | 79B9590 | 2 | prowadnik na tylnej ściance F6, linia wkrętów 21,5 od lewej krawędzi F6 |
| Prowadnik do 79B9590 | 173H7130 | 2 | dystans 3 mm, wys. 11,5 (potwierdzone katalogiem: ustawienie fabryczne 79B9590) |
| Wkręty do F6 | 609.1500 (15 mm) | 4+ | |
| Zaślepki (opcjonalnie) | 70.1503 / 70T3504 | – | |

Wszystkie 17 zawiasów: CLIP top BLUMOTION (samodomykanie).

Weryfikacja nawiertów: wszystkie 15 prowadników mieści się w ściankach (y zawiasu ±28), brak konfliktu z innymi otworami; pod wkręty prowadników nawierty pilotowe Ø3×12 (nieprzelotowe, w wewnętrznym licu ścianki, 2 na zawias, rozstaw 32, 37 od przedniej krawędzi ścianki): 30 szt. w planach/kalkulatorze (arkusz_nawiertow.pdf, kalkulator_nawierty.csv). Prowadnik F5 w F6 (2 otwory, X 1521,5; Y 2299 i 2552 ±16): front, więc bez nawiertu w kalkulatorze – wiercisz sam wg znaczników w modelu.

## Złącza
- Konfirmaty 7×50: 146 szt. (łby wpuszczone fazownikiem na równo z licem). Zaślepki tylko na widocznych łbach: 19 miejsc (kupić 20); pozostałe 127 łbów jest ukrytych przy ścianie pokoju, sąsiednim module, maszynie lub pionie (skrypt etap6/zaslepki.py).
- Kołki Ø8×40: 14 szt. + klej (12 w parach KP/PP: po 2 na poziom × 6 poziomów, 2 w styku KB1/KB2); otwory Ø8×20 w krawędzi.
- Podpórki półek Ø5×10 wciskane: 12 (poziomy 922 i 1355: po 4 w KB2 – z 213, 355, 417, 590 – i po 2 w PB2 – z 417, 590); otwory 60 szt., siatka 32 mm. Poziom 489 bez podpórek (konfirmaty).
- Kątowniki 25×25: 6 pod F6 (przesunięte: prawy górny y 2550, lewe x 1510) + 6 za płytami KT1A/B/C (po 2 na płytę, na boku KB2, ramię za płytą).
- Magnesy neodymowe Ø10×3: 6 szt. (po 2 na KT1A/B/C), gniazda Ø10×3 wiercisz sam w tylnej ściance płyt; siła trzymania do potwierdzenia (płyta ok. 0,5 kg).
- Zdejmowane tyły kolumny (wymiary do koszyka): KT1A 407×127, KT1B 407×127, KT1C 350×127.
- Nawierty środków Ø5×5 (PT3, L1B2): pod otwory do wykonania samodzielnie. Środek GN1 w L1B2: z 242 (poprawione z 245).

## Uchwyty
- GUBBARP 116 biały: 8 szt. (sprawdzić opakowanie); otwory wierci użytkownik.

## Wyposażenie L1 (w zamówieniu)
- IKEA UTRUSTA wnętrze szafy gospodarczej 140 cm, nr 105.808.24 (≈400 zł): 330 × 1335 × 530, wysuwane na prowadnicach, udźwig 25 kg; ustawione przy lewej ścianie L1. Zawiasów UTRUSTA nie kupujemy (zawiasy z Bluma). Do sprawdzenia w instrukcji IKEA przed zamówieniem: prowadnice (czy w zestawie, czy osobno), hak, otwory w bokach 18 mm.
- Półka luzem L1P: 619 × 574 mm, 18 mm, okleina ABS 0,8 na jednej krawędzi 574, BEZ nawiertów (ani w szafce, ani w półce); ewentualne nawierty robi użytkownik.

## Do doprecyzowania
- Wkręty/kołki do ściany (6×80 + kołki Ø8), kanał Ø125, kratka Ø150.
