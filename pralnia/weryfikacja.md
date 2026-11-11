# Pralnia: lista do weryfikacji przed zamówieniem (stan 2026-11-08, model v52)

Źródła do sprawdzenia: model 3D (index.html albo wyniki/pralnia_3d.html), wyniki/formatki.csv (40 pozycji, 52 sztuki, 15,55 m2), wyniki/kalkulator_nawierty.csv, wyniki/arkusz_nawiertow.pdf, wyniki/podsumowanie.json, pomiary.md, ustalenia.md.
Kontrola automatyczna (model): 55 elementów (ściany, tyły, półki, fronty, listwa LF5, maszyny), 0 kolizji brył; nawierty: 318 otworów, 50 połączeń, 0 kolizji.

## Do potwierdzenia (decyzje otwarte)
Rozstrzygnięte 2026-11-08: PP1+KP1 zostają na konfirmatach; prześwit 415 mm = światło między półkami; uchwyty bez otworów we frontach (wykonuje użytkownik); F9 z 3 zawiasami wystarczy; kolizja F6/LF5/Ø150 sprawdzona, brak.
Do sprawdzenia przy zakupie i montażu: F5 na zawiasie Blum 79B9590 INSERTA (do drzwi równoległych, prowadnik na tyle F6, bez listwy LF5; puszka 22,5 mm), dobór prowadnika (katalog Blum str. 144), nośność mocowania F6 (6 kątowników), pozostałe puszki 22,5 mm, INSERTA wybrana w meble.pl.

## Zamówienie w meble.pl (koszyk 21386928, 2 970,11 zł) jest NIEAKTUALNE
Różnice względem planu: F9, F10, F11 osobno (teraz jeden F9 512 x 1240,5); wymiary F1-F4, F6, F7 zmienione (F1, F2 607; F3, F4 603; F6 234,5; F7 512); półki PP2/KP2 na innych wysokościach i bez konfirmatów (otwory Ø5 x 10 pod podpórki, kołki Ø8 w czołach par); nawierty pilotowe w PT3 i L1B2; zawiasy 22,5 mm.

## Uwagi konstrukcyjne
- Moduły lewy, wnęka i kolumna stykają się (0 mm): składać na sucho przed dokręceniem.
- Luzy: lewa ściana pokoju 5 mm, prawa 3 mm, tył 3-5, sufit 9. Maszyny: 3 mm z lewej, 5 z prawej, można je przesuwać (ok. 4 mm po bokach).
- L1 bez półki (boki trzyma tył do czasu osadzenia L2); KB1 ma jedno połączenie.
- Model 3D nie był oglądany wizualnie przez Claude (brak biblioteki w środowisku): sprawdzić warstwy "Konfirmaty", "Otwory", "Kołki", "Uchwyty", "Listwa F5".

## Dodane 2026-11-08 (v55)
- KT1A/B/C: nowe wysokości 410/410/366 (patrz ustalenia). Koszyk meble.pl dodatkowo nieaktualny o te trzy pozycje.
- Ramiona kątowników w modelu nachodzą na siebie 2 mm w rogu – to geometria jednego kątownika, nie kolizja.

## Dodane 2026-11-08 (v56)
- Nawierty pilotowe prowadników Ø3×12 w ściankach (30 szt.): sprawdzić w kalkulatorze meble.pl, czy dopuszcza Ø3 i głębokość 12; w razie braku użyć Ø4. Łącznie 348 otworów, 0 kolizji.
- Zawiasy UTRUSTA nie kupujemy; wnętrze UTRUSTA w modelu to tylko wizualizacja wyposażenia L1.
- Wszystkie 17 zawiasów BLUMOTION; F5↔F6: 2 × 79B9590 + 2 × 173H7130 (dystans 3).

## Dodane 2026-11-08 (v57)
- UTRUSTA 105.808.24 w zamówieniu – sprawdzić w instrukcji IKEA prowadnice/hak/otwory w bokach.
- L1P (półka luzem 619×574, bez nawiertów) do dopisania w koszyku; KB1: 3 konfirmaty + 2 kołki.
- KT1A: prześwit między półkami 415 vs wysokość 410 (po 2 mm luzu) – sprawdzić przy montażu.

## Dodane 2026-11-11 (v58, lokalnie)
- Do pomiaru: gzyms przy poziomie 489 (czy wchodzi w obrys PP1/KP1; od tego zależy podniesienie o 3 mm), potrzeba wieńca RDW2.
- Magnesy w KT1A/B/C: potwierdzić siłę trzymania i gniazda Ø10×3 (robi użytkownik). Alternatywa: zatrzaski/rzep.
- KT1C skrócona do 350: szczelina 18 mm pod wieńcem RDW za plecami (tył kolumny), do akceptacji.
- Kalkulator meble.pl: Ø3×12 dla prowadników (jeśli niedostępne, Ø4).
- Koszyk meble.pl wymaga przeróbki także o: półki PP/KP w nowych wymiarach, KT1A/B/C 407/407/350 ×127, L1P, wieńce 2 konfirmaty.
