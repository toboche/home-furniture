# Kuchnia: parametry zamówienia w centrum.meble.pl

Źródło dla agenta zamówienia (`zamowienie/prompt_agenta_zamowienie.md`). Wymiary, ilości i otwory: `wyniki/kalkulator_nawierty.csv`,
`wyniki/formatki.csv`, `zamowienie/fronty_metod.csv`. Ten plik dodaje to, czego pipeline nie eksportuje: słoje, okleinę frontów, szablon F1.
Stan: 2026-11-23, po audycie v6 (KU6-02, KU6-03); słoje potwierdzone, MAXIMERA Ø5 × 12.

## Płyta i okleina
- Płyta: `Płyta meblowa EGGER H3710 ST12 Orzech Carini naturalny 18 mm` (dekor usłojony, kolumna `Słoje` nigdy `0`).
- Okleina wszędzie: `Obrzeże ABS H3710 ST12 Orzech Carini naturalny 23 x 0.8 mm EGGER`, także F1 i fronty METOD
  (jak istniejąca kuchnia; laserowa 1,0 mm wyłącza `Wręgowanie`, a fronty METOD mają otwory). Fronty: kolejność „kryjące długie”, jeśli kalkulator ją oferuje.

## Słoje (potwierdzone przez użytkownika 2026-11-23)
Zasada: na elementach pionowych słoje pionowo (jak F1 i istniejąca kuchnia), na poziomych równolegle do przedniej krawędzi.
`SZER × WYS` w kalkulatorze = `SZER=DL × WYS=SZ` z `kalkulator_nawierty.csv` (F1 i fronty METOD: szerokość × wysokość frontu).
Znaczenie wartości `Słoje` w kalkulatorze (na szerokość / na wysokość, kody CSV) sprawdzić na wierszu testowym.

| WIERSZ | KOD | SZT | SZER × WYS | SŁOJE NA MEBLU | SŁOJE W KALKULATORZE | OKLEINA (KRAWĘDZIE) | SZABLON |
|---:|---|---:|---|---|---|---|---|
| 1 | KU-P1 | 1 | 804 × 400 | wzdłuż 804 (przód) | NA SZEROKOŚĆ | 1 | Wręgowanie |
| 2 | KU-P3 | 1 | 1978 × 200 | wzdłuż 1978 | NA SZEROKOŚĆ | 1 | Wręgowanie |
| 3 | KU-SOB-1 | 1 | 1154 × 304 | pionowo | NA SZEROKOŚĆ | 1 | Wręgowanie |
| 4 | KU-SOB-2 | 1 | 1154 × 304 | pionowo | NA SZEROKOŚĆ | 1 | Wręgowanie |
| 5 | KU-SOT | 1 | 1154 × 516 | pionowo | NA SZEROKOŚĆ | brak | Wręgowanie |
| 6 | KU-SOW | 1 | 516 × 286 | lewo–prawo | NA SZEROKOŚĆ | 1 | Wręgowanie |
| 7 | KU-SOP | 1 | 516 × 286 | lewo–prawo | NA SZEROKOŚĆ | 1 | Wręgowanie |
| 8 | KU-WSB-1 | 1 | 1154 × 300 | pionowo | NA SZEROKOŚĆ | 1 | Wręgowanie |
| 9 | KU-WSB-2 | 1 | 1154 × 300 | pionowo | NA SZEROKOŚĆ | 1 | Wręgowanie |
| 10 | KU-WST | 1 | 1154 × 238 | pionowo | NA SZEROKOŚĆ | brak | Wręgowanie |
| 11 | KU-WSD, WSS, WSP-1, WSP-2 | 4 | 282 × 238 | lewo–prawo (wzdłuż 238) | NA WYSOKOŚĆ | 2 (238, przód) | Wręgowanie |
| 12 | KU-WSW | 1 | 282 × 238 | lewo–prawo (wzdłuż 238) | NA WYSOKOŚĆ | 2 (238, przód) | Wręgowanie |
| 13 | KU-SOD | 1 | 514 × 284 | lewo–prawo | NA SZEROKOŚĆ | 1 (514, przód) | bez nawiertów |
| 14 | KU-WSZ | 1 | 236 × 165 | pionowo (jak F1) | NA WYSOKOŚĆ | brak | bez nawiertów |
| 15 | KU-F1 | 1 | 549 × 1151 | pionowo | NA WYSOKOŚĆ | 1, 2, 3, 4 | Front prawy |
| 16–21 | KU-FM1–FM6 („usłojenie 21a–21c, 22a–22c”) | 6 | 597 × 142 / 397 / 397 / 197 / 197 / 397 | pionowo, ciągłe w kolumnie | NA WYSOKOŚĆ | 1, 2, 3, 4 | Wręgowanie (Tył) |

## Front F1 (549 × 1151)
- Zawiasy po prawej (na SOB-2), Blum CLIP top 70T3550.TL na wkręty: szablon `Front prawy`, `Typ zawiasu` = `BLUM puszka 35mm (wkręty)`,
  `Odległość od krawędzi` = `22.50`, 3 puszki: `x1` (od góry) = `100`, `x2` (od dołu, ręcznie) = `337.5`, `x3` (od góry, ręcznie) = `453.5`
  (środki 337,5 / 697,5 / 1051 od dołu). Nie `symetrycznie`. Sprawdzić na podglądzie SVG, że puszki są przy prawej krawędzi.
- Gdyby kalkulator nie miał wariantu na wkręty: `Wręgowanie i nawierty`, `Tył (B)`, 3 × Ø35 × 13 w X = 526,5, Y = 337,5 / 697,5 / 1051
  (otwory pod wkręty puszki nawierca użytkownik).

## Sumy kontrolne
21 wierszy, 24 szt.; `Usługa wiercenia`: 1 szt. front z szablonem zawiasów + 21 szt. `Wręgowanie` (15 z wierszy 1–12 + 6 frontów METOD);
otwory: 136 wpisów / 154 z SZT w wierszach 1–12, 56 we frontach METOD, 3 puszki F1.
