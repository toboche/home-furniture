# Założenia wspólne dla wszystkich pomieszczeń

Wartości domyślne przyjęte w pralni. Nowe pomieszczenie zaczyna od nich; każdą różnicę zapisuje
w swoim `ustalenia.md` (tam jest źródło prawdy dla pomieszczenia).

## Oznaczenia
- Kody wymiarów, formatek i frontów na rysunkach i w tabelach: TYLKO DUŻE LITERY (A, GZ1, F5, KB2).
- Wymiary w mm. Kody są lokalne dla pomieszczenia; przy wspólnym zamówieniu prefiks (np. `GD-F1`).
- Układ współrzędnych modelu: X od lewej ściany ku prawej, Y od podłogi w górę, Z od tylnej ściany ku wejściu.

## Materiał i sklep
- Płyta Egger 18 mm cięta na wymiar w centrum.meble.pl (w pralni: W1200 ST9 Biały porcelanowy na wszystkie elementy).
- Zamówienie: wszystkie elementy z nawiertami. Wymiary formatek podawane z okleiną.
- Okleina: fronty bezspoinowa 1 mm, pozostałe widoczne krawędzie ABS.
- Kalkulator sklepu wierci Ø5 w powierzchni i Ø4 w krawędzi; Ø7 w powierzchni nie do zamówienia,
  otwory pod konfirmaty poszerza się samodzielnie. Puszki zawiasów Ø35 wybierane w kalkulatorze (szablony frontów).
- Otwory większe (np. kratka, gniazdko) wycina się samodzielnie; sklep robi tylko nawiert środka Ø5 x 5.

## Konstrukcja
- Moduły korpusów stykają się bez przerw; fronty mają 3 mm odstępu między sobą.
- Złącza korpusu: konfirmaty 7 x 50, łby wpuszczone na równo z licem; zaślepki w kolorze płyty tylko na widocznych łbach.
- Plecy z tej samej płyty 18 mm, wpuszczone między boki, równo z tylną krawędzią.
- Fronty 18 mm, nakładane. Zawiasy Blum CLIP top BLUMOTION (soft-close), puszka Ø35 22,5 mm od krawędzi frontu.
- Wysokie szafki: pod sufitem luz na wsunięcie modułu (w pralni projekt 3 mm poniżej najniższego punktu sufitu).
- Mocowanie do ściany: wkręty przez plecy, głowice w otwartych szafkach pod zaślepkami.

## Proces
1. Pomiary (`pomiary.md`, zdjęcia z wymiarem w nazwie pliku).
2. Wizualizacja pustego pokoju, potrzeby, koncepcja.
3. Konstrukcja w `model.js`, reguły w `reguly.py`, przeliczenie `python3 wspolne/pipeline/run.py NAZWA`.
4. Zestawienie okuć, instrukcja montażu.
5. Ręczna, niezależna weryfikacja wymiarów i składania przed zamówieniem; drobne poprawki od razu w modelu i ustaleniach.
