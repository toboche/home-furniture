# Kuchnia: weryfikacja projektu przed zamówieniem (2026-11-18, aktualizacja 2026-11-19 po audytach v3 i v4)

Stan: `main` po audycie v7 (2026-11-24): WS bez WSB-1, SOP i WSP na podpórkach. Sprawdzone na przeliczonym modelu
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
| Konfirmaty / kołki / podpórki / widoczne łby | 28 / 4 / 16 / 0 w wnęce WS (2 łby SOB-2 → WSS wewnątrz SO, za F1) (stan 2026-11-24) |
| Otwory w pobliżu wycięć (SOB-2 Ø160; WSB-2, SOP wycięcia U; WST wycięcie 100 × 140; SOT Ø25) | żaden otwór bliżej niż 15 mm od krawędzi wycięcia (WST: konfirmat WSW 18,5 nad wycięciem) |
| Przecięcia brył | tylko zamierzone (rura w otworach, pręty i profile LED w półkach, puszki zawiasów we froncie) |

## 2. Przegląd ręczny (w kolejności montażu)
| MIEJSCE | SPRAWDZONE | WYNIK |
|---|---|---|
| Okap w SO | korpus 513 (z nitami) w 516, kołnierz z 14–304 nad płytkami do 12 | OK: 1,5 z boków, 2 z tyłu nad płytkami |
| Wkręty okapu | nawierty Ø3 × 5 Y 1592, z 250 i 70; od 2026-11-24 wkręty Ø4 × 18 z dystansami EPDM w obu bokach (3,5 × 16 z EPDM za płytko) | OK, sprawdzić otwór w blasze okapu |
| Zawiasy F1 | Y 1850, 2210, 2563,5 (od 2026-11-19, sufit niżej): prowadniki nad okapem (do 1776), SOD (1786–1804) i SOP (2104–2122); nawierty 37 od krawędzi SOB-2 (z 267, poprawione 2026-11-19) | OK |
| TIP-ON | 956.1004 na SOB-1 ok. Y 1850, przy przodzie: nad okapem i SOD; F1 2 przed korpusem (2026-11-19) | OK |
| Przejście wylot → pion | 28,5 do tyłu na 2 kolanach 15° Ø150 spiętych mufą, para obrócona w poziomie (pion ok. 10–20 w prawo); do ok. Y 1992 pod SOP 2104 | OK; wycięcie w SOP dopasować na miejscu |
| Pion, kolano, poziom Ø150 | tył pionu z 34,5 (plecy do 18, mata 10 mieści się); góra poziomu 2639 pod SOW 2647 (od 2026-11-19) | OK; nad poziomem mata do 5 mm |
| Otwór Ø160 w SOB-2 (od 2026-11-24 bez WSB-1) | konfirmaty wieńca SOW przed otworem (z 215, 265), konfirmaty WSS ≥ 16 od krawędzi otworu, nad otworem 21 mm boku | OK |
| Skrzynka WS | redukcja z 34,5–184,5 przed WSZ (z 195), dno 2479 pod rurą 2489, WSW 2647; WSZ 254 × 165 na dolnej listwie i 2 zatrzaskach push-to-open; listwa i zatrzaski po montażu rury | OK, w skrzynce tylko Alubutyl |
| Rura ze ścianki | wystaje 115 (do X 3091), redukcja wąskim końcem w nią; WSB-2 z wycięciem U R70 | OK: złożoną WS wsuwa się od przodu; od 2026-11-24 WST z wycięciem 100 × 140 od prawej krawędzi za rurą (bez niego WST zahacza o rurę) |
| Kratka | WS 300 głębokości, ramka kratki od 306 (zmierzone) | OK, luz 6 (SO 304 nie sięga do ścianki) |
| Zasilanie okapu | otwór Ø25 w SOT (X 2850, Y 2180) nad SOP; przewód w dół przez podcięcia 25 × 25 w tylnym prawym narożniku SOP i SOD | POPRAWIONE (SOD 2026-11-18, SOP 2026-11-19) |
| Mocowanie SO i WS | po 4 wkręty 6 × 70 przez plecy; od 2026-11-24 WS bez WSB-1, łączona z SOB-2 przez WSD i WSS (konfirmaty od wnętrza SO); kolejność i warunki montażu w `ustalenia.md` (2026-11-24) | OK: łby wpuszczone poniżej lica |
| P1 | 3 pręty od ściany lewej + wkręty przez słupek + łączniki do P3; pręty poza rowkami LED | OK |
| P3 | 5 prętów, rowek LED z 151,8–170, pręty z 0–80 | OK |
| Profil LED przy słupku | kołnierz profilu wchodził 1,5 w płytki na ścianie lewej (wystają do 12) | POPRAWIONE: profil zaczyna się 13 od ściany lewej, rowek dalej od ściany (wejście kabla) |
| Pręty a płytki | oś pręta 9 nad górną krawędzią płytek: otwór Ø10 kończy się 4 nad płytkami | uwaga przy wierceniu (nie wykruszyć krawędzi płytek) |
| Okleina w kalkulatorze | P1 krawędź 804 od kuchni, P3 krawędź 1978, korpusy pionowe 1DL, poziome elementy WS 1SZ (krawędź 256, półki 254, od przodu) | OK |
| F1 w kalkulatorze | pipeline nie generuje frontów: szablon `Front prawy` wg `zamowienie.md` (puszki 337,5 / 697,5 / 1051 od dołu, 22,5 od prawej krawędzi), zapasowo `Wręgowanie` | przy zamówieniu |
| Fronty METOD | 6 frontów, słoje na wysokość, FM1 142 przy miejscu 146 celowo (V30 potwierdzone 2026-11-23) | OK |
| Wycena | nieaktualna (SOD, otwory P1/P3, zmiany z audytu) | przeliczyć przy zamówieniu |

## 3. Przed zamówieniem
1. Pomiary L1–L5 zamknięte (2026-11-19). Pręty M8 bez skanu zbrojenia (decyzja 2026-11-23, plan awaryjny w `ustalenia.md`).
2. Wpis do kalkulatora meble.pl wg `zamowienie.md` i `zamowienie/prompt_agenta_zamowienie.md` (inny agent), weryfikacja tutaj.
3. Sprawdzić, czy wkręt Ø4 przechodzi przez otwór w blasze okapu DUO 55.
4. Mail do meble.pl: rysunek dopasowania usłojenia frontów METOD.

## 4. Do zrobienia w `wspolne/` (osobny PR, audyt sekcja C)
Kontrola kolizji otworów z pełną średnicą wycięć (tu sprawdzone skryptem), fronty w `otwory.json` i kalkulatorze,
okleina vs `BEZ_OKLEINY_PREFIKSY`. Audyt v7 C: kolizje otworów licowych z przeciwnych stron płyty (A vs B, suma głębokości), limit 20 znaków nazwy formatki w `wspolne/centrum_meble.md`.
