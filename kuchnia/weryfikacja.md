# Kuchnia: weryfikacja projektu przed zamówieniem (2026-11-18)

Stan: `main` po PR #26 (audyt v1 i decyzje z 2026-11-18). Sprawdzone na przeliczonym modelu
(`run.py kuchnia`, `--wszystkie --sprawdz`, `scena.py`) oraz skryptami: przecięcia brył modelu (prostopadłościany,
rury jako obrys) i odległości otworów od wycięć wykonywanych przez użytkownika (otwory Ø160, wycięcia U).

**Werdykt: projekt spójny, ZAMÓWIENIE DOPIERO PO pomiarach weryfikacyjnych w mieszkaniu** (arkusz „Kuchnia: pomiary
weryfikacyjne przed zamówieniem”: z 31 pozycji zmierzone 7, reszta otwarta, w tym długości ścian, sufit i wnęka).

## 1. Wyniki automatyczne
| SPRAWDZENIE | WYNIK |
|---|---|
| Kolizje otworów (pipeline) | 0 |
| Wszystkie pomieszczenia zgodne z modelami (`--sprawdz`) | tak |
| Test widoku (`scena.py`) | 0 błędów JS, wzorzec aktualny |
| Konfirmaty / kołki / podpórki / widoczne łby | 50 / 8 / 4 / 0 |
| Otwory w pobliżu wycięć (SOB-2, WSB-1 Ø160; WSB-2, SOP wycięcia U; SOT Ø25) | żaden otwór bliżej niż 15 mm od krawędzi wycięcia |
| Przecięcia brył | tylko zamierzone (rura w otworach, pręty i profile LED w półkach, puszki zawiasów we froncie) |

## 2. Przegląd ręczny (w kolejności montażu)
| MIEJSCE | SPRAWDZONE | WYNIK |
|---|---|---|
| Okap w SO | korpus 513 (z nitami) w 516, kołnierz z 14–304 nad płytkami do 12 | OK: 1,5 z boków, 2 z tyłu nad płytkami |
| Wkręty okapu | nawierty Ø3 × 5 Y 1592, z 250 i 70; wkręt 3,5 × 16 wchodzi ok. 13 w bok 18 | OK, widoczny SOB-1 nie przebity |
| Zawiasy F1 | Y 1850, 2210, 2576,5: prowadniki nad okapem (do 1776), SOD (1786–1804) i SOP (2104–2122) | OK |
| TIP-ON | 956.1004 na SOB-1 ok. Y 1850, przy przodzie: nad okapem i SOD; F1 2 przed korpusem (2026-11-19) | OK |
| Przejście wylot → pion | pochylenie ok. 2,6° (28,5 na ok. 625); otwór w SOP na z 124; wycięcie SOD R85 wokół z 138 | OK, kolana 15° jako zapas |
| Pion, kolano, poziom Ø150 | tył pionu z 34,5 (plecy do 18, mata 10 mieści się); góra poziomu 2652 pod SOW 2660 | OK; nad poziomem mata do 5 mm |
| Otwory Ø160 w SOB-2, WSB-1 | konfirmaty wieńców przed otworem (z 215, 265), nad otworem 21 mm boku | OK |
| Skrzynka WS | redukcja z 34,5–184,5 przed WSZ (z 195), dno 2492 pod rurą 2502, WSW 2660 | OK, bez maty w skrzynce |
| Rura ze ścianki | wystaje 115 (do X 3093), redukcja wąskim końcem w nią; WSB-2 z wycięciem U R70 | OK, szafkę nasuwa się na rurę od przodu |
| Kratka | WS 300 głębokości, kratka od 303 | OK (SO 304 nie sięga do ścianki) |
| Zasilanie okapu | otwór Ø25 w SOT (X 2852, Y 2193) nad SOP; przewód w dół przez wycięcie U w SOP | POPRAWIONE: w SOD dopisane podcięcie 25 × 25 w tylnym prawym narożniku na przewód |
| Mocowanie SO i WS | po 4 wkręty 6 × 70 przez plecy, SO z WS skręcone | OK, wkręcać przed okapem |
| P1 | 3 pręty od ściany lewej + wkręty przez słupek + łączniki do P3; pręty poza rowkami LED | OK |
| P3 | 5 prętów, rowek LED z 151,8–170, pręty z 0–80 | OK |
| Profil LED przy słupku | kołnierz profilu wchodził 1,5 w płytki na ścianie lewej (wystają do 12) | POPRAWIONE: profil zaczyna się 13 od ściany lewej, rowek dalej od ściany (wejście kabla) |
| Pręty a płytki | oś pręta 9 nad górną krawędzią płytek: otwór Ø10 kończy się 4 nad płytkami | uwaga przy wierceniu (nie wykruszyć krawędzi płytek) |
| Okleina w kalkulatorze | P1 krawędź 804 od kuchni, P3 krawędź 1980, korpusy 1DL | OK |
| F1 w kalkulatorze | pipeline nie generuje frontów: puszki Ø35 × 13 337,5 / 697,5 / 1064 od dołu, 22,5 od prawej krawędzi wpisać ręcznie | do zrobienia przy zamówieniu |
| Fronty METOD | 6 frontów, słoje na wysokość, FM1 142 celowo | OK; wymiary szafek METOD do potwierdzenia (V30) |
| Wycena | nieaktualna (SOD, otwory P1/P3, zmiany z audytu) | przeliczyć przy zamówieniu |

## 3. Przed zamówieniem
1. Pomiary z arkusza (zwłaszcza V1–V8, V10–V16, V21, V23–V25, V30–V31). Każda różnica wraca do `pomiary.md` i modelu.
2. Rozstaw prętów: zaznaczyć na ścianie i sprawdzić gniazdka i przewody (V23–V25); bez wykrywacza zbrojenia
   rozważyć wywiercenie otworów w ścianie przed zamówieniem i podanie rzeczywistych położeń.
3. Wpis do kalkulatora meble.pl (formatki z CSV, okleina, nawierty z `wyniki/kalkulator_nawierty.csv`, puszki F1
   ręcznie, fronty METOD z `zamowienie/fronty_metod.csv`) i aktualna wycena.
4. Mail do meble.pl: rysunek dopasowania usłojenia frontów METOD.

## 4. Do zrobienia w `wspolne/` (osobny PR, audyt sekcja C)
Kontrola kolizji otworów z pełną średnicą wycięć (tu sprawdzone skryptem), fronty w `otwory.json` i kalkulatorze,
okleina vs `BEZ_OKLEINY_PREFIKSY`.
