# home-furniture

Projekty mebli na wymiar do mieszkania: model 3D, lista formatek, nawierty i ustalenia.
Każde pomieszczenie ma swój katalog; silnik wizualizacji i skrypty są wspólne.

Dokumentacja: `wspolne/STRUKTURA.md` (struktura, decyzje, reguły modelu, nowe pomieszczenie krok po kroku),
`wspolne/zasady.md` (założenia meblarskie), `CLAUDE.md` (zasady dla kolejnych rozmów z Claude).

## Pomieszczenia
- `pralnia/`: szafki do pralni (płyta Egger W1200 ST9 18 mm, centrum.meble.pl), przed zamówieniem
- `garderoba/`: szafy do garderoby, start (pomiary)
- `przedpokoj/`: szafa z szezlongiem przy drzwiach wejściowych, konstrukcja wstępna
- `kuchnia/`: półka z LED, szafka okapowa (Ciarko DUO 55) i wąska szafka; płyta Egger H3710 Orzech Carini, konstrukcja wstępna
- `szablon/`: punkt wyjścia dla nowego pomieszczenia (jedna przykładowa szafka)

## Układ katalogu pomieszczenia
| Plik | Co zawiera | Kto edytuje |
|---|---|---|
| `ustalenia.md` | decyzje i założenia (źródło prawdy) | ręcznie |
| `pomiary.md` | zmierzone wymiary: KOD, wartość, wcześniejsze odczyty | ręcznie |
| `model.js` | dane modelu 3D: pokój, otwory, bryły (`ITEMS`), warianty | ręcznie |
| `reguly.py` | reguły pomieszczenia dla skryptów: moduły, wyjątki, opisy formatek | ręcznie |
| `index.html` | strona widoku 3D (wczytuje model i wspólny silnik) | rzadko |
| `laczniki.gen.js` | otwory, konfirmaty, kołki, puszki zawiasów do widoku 3D | generowany |
| `wyniki/` | `formatki.csv`, `kalkulator_nawierty.csv`, `arkusz_nawiertow.pdf`, `otwory.json`, `podsumowanie.json`, `<pomieszczenie>_3d.html` (widok w jednym pliku) | generowane |
| `komponenty.md`, `weryfikacja.md`, … | zestawienia i listy kontrolne | ręcznie |

## Wspólne
- `wspolne/zasady.md`: założenia domyślne dla wszystkich pomieszczeń (płyta, okleina, szczeliny, złącza, sklep). Pomieszczenie może je nadpisać w swoim `ustalenia.md`.
- `wspolne/viewer/`: silnik widoku 3D (Three.js r128 z CDN): panel, warstwy, rozsunięcie, warianty, numeracja.
- `wspolne/pipeline/`: przeliczenie modelu na formatki i nawierty.
- `wspolne/testy/`: test widoku 3D bez WebGL (atrapa Three.js) i wzorce scen.

## Po każdej zmianie w modelu
```
python3 wspolne/pipeline/run.py pralnia            # przelicza laczniki.gen.js i wyniki/
python3 wspolne/pipeline/run.py --wszystkie --sprawdz
```
Potem commit razem z wynikami. GitHub Actions (`.github/workflows/test.yml`) przy każdym pushu sprawdza,
że wyniki w repozytorium wynikają z aktualnych modeli i że widoki 3D zgadzają się ze wzorcami
(`wspolne/testy/wzorce/`). Zmiana w `wspolne/`, która po cichu zmieniłaby pralnię, kończy się błędem testu.
Zamierzona zmiana widoku: odśwież wzorzec poleceniem
`python3 wspolne/testy/scena.py pralnia/index.html wspolne/testy/wzorce/pralnia_scena.json`.

Wymagania: Python 3 z matplotlib, Node.js; do testu widoku Playwright z Chromium.

## Nowe pomieszczenie
Skrót (pełna wersja: `wspolne/STRUKTURA.md`, punkt 7):
1. Skopiuj `szablon/` pod nową nazwą, usuń `wyniki/` i `laczniki.gen.js`.
2. Uzupełnij `pomiary.md` i `ustalenia.md`, potem `model.js` (wymiary jako stałe z pomiarów) i `reguly.py`.
3. `python3 wspolne/pipeline/run.py NAZWA`, wzorzec sceny: `python3 wspolne/testy/scena.py NAZWA/index.html wspolne/testy/wzorce/NAZWA_scena.json`
   (bez wzorca test w GitHub Actions nie przejdzie).

## Praca równoległa
Każde pomieszczenie na osobnej gałęzi (np. `garderoba/...`). Konflikty mogą się pojawić tylko w `wspolne/`;
test regresji pilnuje, żeby zmiany tam nie zmieniały wyników innych pomieszczeń.
Kody wymiarów i formatek (A, B, F1…) są lokalne dla pomieszczenia; przy wspólnym zamówieniu kilku
pomieszczeń trzeba dodać prefiks (np. `GD-F1`).
