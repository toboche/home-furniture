# Pralnia: lista do weryfikacji przed zamówieniem (stan 2026-11-08, model v52)

Źródła do sprawdzenia: model 3D (model3d/index.html), etap6/formatki.csv (40 pozycji, 52 sztuki, 15,2 m2), etap6/kalkulator_nawierty.csv, etap6/arkusz_nawiertow.pdf, ustalenia.md.
Kontrola automatyczna (model): 55 elementów (ściany, tyły, półki, fronty, listwa LF5, maszyny), 0 kolizji brył; nawierty: 318 otworów, 50 połączeń, 0 kolizji.

## Do potwierdzenia (decyzje otwarte)
1. PP1+KP1 (poziom 489) na konfirmatach, bo na nich stoją KB2/PB2. Czy mają też być na podpórkach?
2. Prześwit 415 mm = światło między półkami (PP1 góra 507, PP2-1 922-940, PP2-2 1355-1373, do pasa 1743 zostaje 370).
3. Pozycje uchwytów GUBBARP (robocze): pionowo, 30 mm od wolnej krawędzi, rzędy górne 50 od dołu, dolne 50 od góry, F9 środek ok. 1050 od podłogi.
4. Liczba zawiasów F9 (3 szt. dla 1240,5 mm) wg tabeli Blum.
5. F5: zawias wpuszczany (Blum 71B3790 INSERTA lub 71B3750) na listwie LF5; odległość puszki 22,5; karta Blum (HIO71B3790-spec.pdf): rozstaw otworów płytki i wpuszczenie. Kolizja lewego kątownika dolnego F6 (X 1540) z LF5 i otworem Ø150 (od X 1541).
6. Zawiasy: wszystkie puszki 22,5 mm od krawędzi, nakładanie 16 mm (potrzebne 16,5, korekta +/- 2 mm). W meble.pl wybrać typ INSERTA zgodnie z wybranym zawiasem.

## Zamówienie w meble.pl (koszyk 21386928, 2 970,11 zł) jest NIEAKTUALNE
Różnice względem planu: F9, F10, F11 osobno (teraz jeden F9 512 x 1240,5); wymiary F1-F4, F6, F7 zmienione (F1, F2 607; F3, F4 603; F6 234,5; F7 512); nowa listwa LF5 (427,5 x 60); półki PP2/KP2 na innych wysokościach i bez konfirmatów (otwory Ø5 x 10 pod podpórki, kołki Ø8 w czołach par); nawierty pilotowe w PT3 i L1B2; zawiasy 22,5 mm.

## Uwagi konstrukcyjne
- Moduły lewy, wnęka i kolumna stykają się (0 mm): składać na sucho przed dokręceniem.
- Luzy: lewa ściana pokoju 5 mm, prawa 3 mm, tył 3-5, sufit 9. Maszyny: 3 mm z lewej, 5 z prawej, można je przesuwać (ok. 4 mm po bokach).
- L1 bez półki (boki trzyma tył do czasu osadzenia L2); KB1 ma jedno połączenie.
- Model 3D nie był oglądany wizualnie przez Claude (brak biblioteki w środowisku): sprawdzić warstwy "Konfirmaty", "Otwory", "Kołki", "Uchwyty", "Listwa F5".
