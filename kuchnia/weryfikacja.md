# Kuchnia: weryfikacja projektu przed zamówieniem (2026-11-18, aktualizacja 2026-11-19 po audytach v3 i v4)

Stan: `main` po audytach v5 i v6 (2026-11-22). Sprawdzone na przeliczonym modelu
(`run.py kuchnia`, `--wszystkie --sprawdz`, `scena.py`) oraz skryptami: przecięcia brył modelu (prostopadłościany,
rury jako obrys) i odległości otworów od wycięć wykonywanych przez użytkownika (otwory Ø160, wycięcia U).

**Werdykt (2026-11-19): projekt spójny, pomiary L1–L5 zamknięte, meble się mieszczą. Zostaje wpis do kalkulatora i wycena.** Wcześniej: zamówienie dopiero po 5 pomiarach w mieszkaniu (arkusz „Kuchnia: pomiary weryfikacyjne
przed zamówieniem”, od 2026-11-19 tylko L1–L5: czy meble fizycznie się mieszczą; patrz `ustalenia.md`).

## 1. Wyniki automatyczne
| SPRAWDZENIE | WYNIK |
|---|---|
| Kolizje otworów (pipeline) | 0 |
| Wszystkie pomieszczenia zgodne z modelami (`--sprawdz`) | tak |
| Test widoku (`scena.py`) | 0 błędów JS, wzorzec aktualny |
| Konfirmaty / kołki / podpórki / widoczne łby | 50 / 6 / 4 / 0 (stan 2026-11-19) |
| Otwory w pobliżu wycięć (SOB-2, WSB-1 Ø160; WSB-2, SOP wycięcia U; SOT Ø25) | żaden otwór bliżej niż 15 mm od krawędzi wycięcia |
| Przecięcia brył | tylko zamierzone (rura w otworach, pręty i profile LED w półkach, puszki zawiasów we froncie) |

## 2. Przegląd ręczny (w kolejności montażu)
| MIEJSCE | SPRAWDZONE | WYNIK |
|---|---|---|
| Okap w SO | korpus 513 (z nitami) w 516, kołnierz z 14–304 nad płytkami do 12 | OK: 1,5 z boków, 2 z tyłu nad płytkami |
| Wkręty okapu | nawierty Ø3 × 5 Y 1592, z 250 i 70; w widocznym SOB-1 wkręty 3,5 × 13, w SOB-2 3,5 × 16 | OK |
| Zawiasy F1 | Y 1850, 2210, 2563,5 (od 2026-11-19, sufit niżej): prowadniki nad okapem (do 1776), SOD (1786–1804) i SOP (2104–2122); nawierty 37 od krawędzi SOB-2 (z 267, poprawione 2026-11-19) | OK |
| TIP-ON | 956.1004 na SOB-1 ok. Y 1850, przy przodzie: nad okapem i SOD; F1 2 przed korpusem (2026-11-19) | OK |
| Przejście wylot → pion | 28,5 do tyłu na 2 kolanach 15° Ø150 spiętych mufą, para obrócona w poziomie (pion ok. 10–20 w prawo); do ok. Y 1992 pod SOP 2104 | OK; wycięcie w SOP dopasować na miejscu |
| Pion, kolano, poziom Ø150 | tył pionu z 34,5 (plecy do 18, mata 10 mieści się); góra poziomu 2639 pod SOW 2647 (od 2026-11-19) | OK; nad poziomem mata do 5 mm |
| Otwory Ø160 w SOB-2, WSB-1 | konfirmaty wieńców przed otworem (z 215, 265), nad otworem 21 mm boku | OK |
| Skrzynka WS | redukcja z 34,5–184,5 przed WSZ (z 195), dno 2479 pod rurą 2489, WSW 2647 (od 2026-11-19); WSZ 236 × 165 na dolnej listwie i 2 zatrzaskach push-to-open (audyt v4) | OK, bez maty w skrzynce |
| Rura ze ścianki | wystaje 115 (do X 3091), redukcja wąskim końcem w nią; WSB-2 z wycięciem U R70 | OK, szafkę nasuwa się na rurę od przodu |
| Kratka | WS 300 głębokości, ramka kratki od 306 (zmierzone) | OK, luz 6 (SO 304 nie sięga do ścianki) |
| Zasilanie okapu | otwór Ø25 w SOT (X 2850, Y 2180) nad SOP; przewód w dół przez podcięcia 25 × 25 w tylnym prawym narożniku SOP i SOD | POPRAWIONE (SOD 2026-11-18, SOP 2026-11-19) |
| Mocowanie SO i WS | po 4 wkręty 6 × 70 przez plecy, SO z WS skręcone; na styku SOB-2 / WSB-1 łby konfirmatów naprzeciw siebie | OK: łby wpuszczone poniżej lica, wkręty łączące z dala od konfirmatów |
| P1 | 3 pręty od ściany lewej + wkręty przez słupek + łączniki do P3; pręty poza rowkami LED | OK |
| P3 | 5 prętów, rowek LED z 151,8–170, pręty z 0–80 | OK |
| Profil LED przy słupku | kołnierz profilu wchodził 1,5 w płytki na ścianie lewej (wystają do 12) | POPRAWIONE: profil zaczyna się 13 od ściany lewej, rowek dalej od ściany (wejście kabla) |
| Pręty a płytki | oś pręta 9 nad górną krawędzią płytek: otwór Ø10 kończy się 4 nad płytkami | uwaga przy wierceniu (nie wykruszyć krawędzi płytek) |
| Okleina w kalkulatorze | P1 krawędź 804 od kuchni, P3 krawędź 1978, korpusy pionowe 1DL, poziome elementy WS (WSD, WSW, WSS, WSP) 1SZ (krawędź 238 od przodu) | OK |
| F1 w kalkulatorze | pipeline nie generuje frontów: puszki Ø35 × 13 337,5 / 697,5 / 1051 od dołu (od 2026-11-19, front 1151), 22,5 od prawej krawędzi wpisać ręcznie | do zrobienia przy zamówieniu |
| Fronty METOD | 6 frontów, słoje na wysokość, FM1 142 celowo | OK; wymiary szafek METOD do potwierdzenia (V30) |
| Wycena | nieaktualna (SOD, otwory P1/P3, zmiany z audytu) | przeliczyć przy zamówieniu |

## 3. Przed zamówieniem
1. Pomiary L1–L5 z arkusza. Każda różnica wraca do `pomiary.md` i modelu.
2. Rozstaw prętów: zaznaczyć na ścianie i sprawdzić gniazdka i przewody (V23–V25); bez wykrywacza zbrojenia
   rozważyć wywiercenie otworów w ścianie przed zamówieniem i podanie rzeczywistych położeń.
3. Wpis do kalkulatora meble.pl (formatki z CSV, okleina, nawierty z `wyniki/kalkulator_nawierty.csv`, puszki F1
   ręcznie, fronty METOD z `zamowienie/fronty_metod.csv`) i aktualna wycena.
4. Mail do meble.pl: rysunek dopasowania usłojenia frontów METOD.

## 4. Do zrobienia w `wspolne/` (osobny PR, audyt sekcja C)
Kontrola kolizji otworów z pełną średnicą wycięć (tu sprawdzone skryptem), fronty w `otwory.json` i kalkulatorze,
okleina vs `BEZ_OKLEINY_PREFIKSY`.
