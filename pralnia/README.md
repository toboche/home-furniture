# Szafki do pralni
- `ustalenia.md`: wszystkie decyzje i wymiary (źródło prawdy)
- `pomiary.md`: zmierzone wymiary z historią odczytów
- `index.html`: model 3D (otwórz w przeglądarce z katalogu repozytorium, wymaga internetu dla Three.js)
- `wyniki/pralnia_3d.html`: ten sam model w jednym pliku (do wysłania albo publikacji)
- `wyniki/`: `formatki.csv`, `kalkulator_nawierty.csv`, `arkusz_nawiertow.pdf`, `otwory.json`, `podsumowanie.json` (liczby konfirmatów, kołków, zaślepek, otworów)
- `model.js`: dane modelu; `reguly.py`: reguły pralni dla skryptów (moduły, podpórki, kołki, zawias F5, opisy formatek)
- `komponenty.md`, `weryfikacja.md`, `audyt_niezaaplikowane.md`: zestawienie okuć, lista kontrolna, audyt
- Wersja online: https://claude.ai/artifact/2xJwuq8PedpcNFw95TNouU

Po zmianie w `model.js` lub `reguly.py`: `python3 wspolne/pipeline/run.py pralnia` (z katalogu głównego repozytorium).
