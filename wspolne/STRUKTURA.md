# Struktura projektu i dodawanie pomieszczeń

Uzupełnienie `README.md`: jak zbudowany jest projekt, dlaczego tak, jakie reguły musi spełniać model
i jak krok po kroku dodać nowe pomieszczenie. Założenia meblarskie (płyta, okleina, złącza, sklep): `zasady.md`.

## 1. Zasady ogólne
- **Jedno pomieszczenie = jeden katalog w katalogu głównym** (`pralnia/`, `garderoba/`, `kuchnia/`). Katalog musi być
  na pierwszym poziomie, bo `index.html` odwołuje się do `../wspolne/`.
- **Pomieszczenia są od siebie niezależne.** Każde ma własny układ współrzędnych, własne kody i własne wyniki.
  Wspólny jest tylko kod w `wspolne/`.
- **Źródłem prawdy jest repozytorium.** Decyzje: `ustalenia.md`, pomiary: `pomiary.md`, geometria: `model.js`.
  Kopie w innych miejscach (dokumenty projektu Claude, pliki pobrane na dysk) mogą być nieaktualne.
- **Pliki generowane się nie edytuje.** `laczniki.gen.js` i wszystko w `wyniki/` powstaje z `model.js` i `reguly.py`
  poleceniem `python3 wspolne/pipeline/run.py NAZWA`. Po każdej zmianie modelu: przeliczyć i zacommitować razem.
- **Kody wymiarów, formatek i frontów: tylko duże litery** (A, GZ1, KB2, F5), bez mieszania z małymi.
  Kody są lokalne dla pomieszczenia (F1 w pralni i F1 w garderobie to różne fronty).

## 2. Dlaczego tak (decyzje o strukturze)
| Decyzja | Powód |
|---|---|
| Dane modelu w `model.js` (`var HF_MODEL=…`), nie w JSON | strona otwiera się dwuklikiem z dysku; przeglądarka nie wczyta JSON przez `fetch` z `file://` |
| Silnik widoku wspólny (`wspolne/viewer/`), reguły widoku w `model.js` | poprawka widoku trafia do wszystkich pomieszczeń; wyjątki (np. wariant F8 w pralni) zostają przy swoim pomieszczeniu |
| Skrypty wspólne (`wspolne/pipeline/`), reguły w `reguly.py` pomieszczenia | ten sam algorytm konfirmatów i nawiertów; wyjątki (podpórki, kołki, zawiasy specjalne) opisane jawnie |
| Wymiary formatek liczone z modelu | jedno źródło wymiarów; opis niezgodny z modelem kończy się błędem |
| Wyniki trzymane w repozytorium | można je otworzyć bez uruchamiania skryptów; test sprawdza, że wynikają z aktualnego modelu, a diff pokazuje każdą zmianę w zamówieniu |
| Test pomija bajty PDF | PDF zależy od wersji matplotlib; jego treść w całości wynika z `otwory.json`, które jest porównywane |
| Wzorce scen 3D (`wspolne/testy/wzorce/`) | zmiana w silniku widoku nie może po cichu zmienić innego pomieszczenia |
| Wersja jednoplikowa `wyniki/<nazwa>_3d.html` | do wysłania i publikacji jako artefakt; Three.js nadal z CDN |

## 3. Pliki pomieszczenia
| Plik | Rola |
|---|---|
| `README.md` | krótki opis i lista plików |
| `pomiary.md` | tabela: KOD, WARTOŚĆ, OPIS, WCZEŚNIEJ / UWAGI; przy ponownym pomiarze stara wartość idzie do WCZEŚNIEJ |
| `ustalenia.md` | etapy, decyzje, założenia, różnice względem `wspolne/zasady.md`, dziennik zmian z datami |
| `model.js` | pokój, otwory w ścianach, bryły (`ITEMS`), widoki, warstwy, warianty |
| `reguly.py` | reguły dla skryptów (punkt 6) i opisy formatek |
| `index.html` | strona widoku: Three.js z CDN, `model.js`, `laczniki.gen.js`, `../wspolne/viewer/viewer.js` |
| `laczniki.gen.js` | generowany: otwory, konfirmaty, kołki, puszki zawiasów |
| `wyniki/formatki.csv` | lista formatek do zamówienia (KOD, NAZWA, DL, SZ, SZT, OKLEINA, NAWIERTY, UWAGI) |
| `wyniki/kalkulator_nawierty.csv` | nawierty do wpisania w kalkulatorze sklepu |
| `wyniki/arkusz_nawiertow.pdf` | rysunki nawiertów, jedna strona na typ formatki |
| `wyniki/otwory.json` | pełna lista formatek i otworów (porównywana w teście) |
| `wyniki/podsumowanie.json` | liczby: pozycje, sztuki, m², konfirmaty, kołki, widoczne łby (zaślepki), kolizje |
| `wyniki/<nazwa>_3d.html` | widok 3D w jednym pliku |

## 4. Model (`model.js`)
Układ: **X od lewej ściany ku prawej, Y od podłogi w górę, Z od tylnej ściany ku wejściu**, wszystko w mm.
Ściany: `tyl` (z = 0), `przod` (z = D), `lewa` (x = 0), `prawa` (x = W). Które fizyczne ściany są „lewą” i „tylną”,
zapisuje się na początku `ustalenia.md` pomieszczenia.

Pola `HF_MODEL` (pełny opis w nagłówku `wspolne/viewer/viewer.js`): `title`, `room {W,D,H}`, `wallThickness`,
`openings [{wall,pos,w,y,h}]`, `views`, `conceptLayers`, `hiddenLayers`, `fixedLayers`, `boardLayers`,
`boardColor`, `noOffset`, `explodeParent`, `variants`, `items`.

Bryły w `ITEMS`:
- prostopadłościan `{n, layer, x, y, z, w, h, d, c, o}`: (x, y, z) to róg o najmniejszych współrzędnych, w/h/d wzdłuż X/Y/Z;
- walec wzdłuż Z `{t:'cyl', n, layer, cx, cy, z, r, len, c}`; walec wzdłuż dowolnej osi `{t:'cyl3', n, layer, ax, px, py, pz, r, len, c}`.

Wymiary wpisuje się jako stałe z `pomiary.md` na początku pliku i z nich liczy położenia (`x:A-B`), żeby ponowny
pomiar zmieniał jedną liczbę. (Pralnia ma liczby wpisane wprost, bo powstała wcześniej.)

### Reguły, których wymagają skrypty
Jeśli model ich nie spełnia, nawierty nie powstaną albo wyjdą błędne. Sprawdzaj `podsumowanie.json` i widok 3D.

1. **Formatka** to prostopadłościan w jednej z warstw `WARSTWY_FORMATEK` (zwykle `Ścianki boczne`, `Ścianki tylne`,
   `Półki`) z **jednym wymiarem równym dokładnie 18** i nazwą zaczynającą się od kodu: `KOD: opis` albo
   `KOD-1: opis`, `KOD-2: opis` dla kilku sztuk o tym samym wymiarze. Wszystkie bryły o tym samym kodzie bazowym
   muszą mieć te same wymiary.
2. **Front** to prostopadłościan w warstwie `Fronty` z nazwą `F1: opis`, `F2: opis`… (kod wyłącznie `F` + liczba).
   Fronty trafiają do `formatki.csv`, ale nie dostają konfirmatów.
3. **Konfirmaty** powstają automatycznie w każdym styku dwóch formatek z **tego samego modułu**
   (`reguly.modul_of`), gdy:
   - lico jednej dotyka czoła drugiej: płaszczyzny styku równe z dokładnością do 0,01 mm,
     nakładanie co najmniej 5 mm w obu pozostałych kierunkach;
   - tylko jedna z dwóch płyt jest cienka w kierunku styku (lico do lica albo czoło do czoła nie daje konfirmatu).

   Rozstaw: co ok. 400 mm, 50 mm od końców; styk krótszy niż 150 mm dostaje jeden konfirmat pośrodku.
   W płycie licowej powstaje otwór Ø5 przelotowy, w czole drugiej Ø4 x 35.
4. **Moduły nie łączą się konfirmatami między sobą.** Styk dwóch modułów (np. sąsiednie szafki) nie daje otworów.
   `modul_of` dostaje bryłę i zwraca nazwę modułu; zwykle wystarcza położenie środka albo prefiks kodu.
5. **Zawias** to prostopadłościan 35 x 35 w warstwie `Zawiasy`, którego środek (x + 17,5, y + 17,5) leży na froncie.
   Strona zawiasu wynika z połowy frontu, w której leży. Puszka Ø35 powstaje w tylnym licu frontu.
   Pod prowadnik skrypt szuka ścianki (płyta cienka w X), której zewnętrzne lico wystaje **1,5 mm poza krawędź
   frontu** (front nakładany, 3 mm szczeliny między sąsiednimi frontami), a przednia krawędź leży nie dalej niż
   20 mm za tylnym licem frontu.
   Nawierty pilotowe Ø3 x 12 wychodzą 37 mm za tylnym licem frontu, ±16 mm od środka zawiasu.
   Brak takiej ścianki kończy się błędem; wyjątki opisuje `ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE` i `zawias_specjalny`.
6. **Oklejona krawędź** to przednia krawędź formatki (największe Z), o ile leży w płaszczyźnie płyty. Tyły
   (płyty cienkie w Z) i inne formatki bez okleiny wymienia `BEZ_OKLEINY_PREFIKSY`.
7. **Zaślepki:** łeb konfirmatu jest uznany za ukryty, jeśli 6 mm od lica jest ściana pokoju (12 mm przy suficie),
   inna formatka albo bryła z warstw `ZASLEPKI_ZASLANIAJA`. Pozostałe to widoczne łby w `podsumowanie.json`.
8. **Warstwy zarezerwowane** (tworzone przez skrypty): `Otwory`, `Konfirmaty`, `Kołki`. Numeracja na rysunku
   (fronty, tyły, boki, półki) powstaje z kodów w nazwach warstw `Fronty`, `Ścianki tylne`, `Ścianki boczne`, `Półki`.

## 5. Kolejność przeliczenia (`wspolne/pipeline/run.py`)
1. `model.py`: wczytanie `model.js` (Node) i wybranie formatek.
2. `laczenia.py`: styki w obrębie modułów.
3. `otwory.py`: konfirmaty, potem `reguly.dodatkowe_otwory`, potem nawierty prowadników zawiasów, potem kontrola kolizji otworów.
4. `kalkulator.py`, `laczniki_3d.py` (z `reguly.zawias_specjalny`), `zaslepki.py`, `formatki.py`, `arkusz_pdf.py`, `pakiet.py`.

## 6. Reguły pomieszczenia (`reguly.py`)
Wymagane (szablon: `szablon/reguly.py`, rozbudowany przykład: `pralnia/reguly.py`):

| Nazwa | Co robi |
|---|---|
| `WARSTWY_FORMATEK` | lista warstw z formatkami korpusu |
| `modul_of(it)` | nazwa modułu bryły; konfirmaty tylko w obrębie modułu |
| `pomijaj_czesc(p)` | `True` dla formatek bez żadnych nawiertów (np. zdejmowane tyły) |
| `pomijaj_polaczenie(face, edge)` | `True` dla styku bez konfirmatów (np. półki na podpórkach); argumenty to kody |
| `rozstaw(face, edge, domyslny)` | rozstaw konfirmatów dla styku (mm) |
| `punkty(face, edge, zakres, pts)` | ostateczne położenia konfirmatów wzdłuż styku (np. 2 na końcach wieńca) |
| `dodatkowe_otwory(P, parts, loc)` | podpórki, kołki, nawierty środków; `P` = słownik kod → formatka |
| `ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE` | kody frontów, których zawiasy nie mają prowadnika w ściance |
| `zawias_specjalny(code, fr, cx, cy, cyl)` | dodatkowe bryły dla takich zawiasów (np. otwory w sąsiednim froncie) |
| `BEZ_OKLEINY_PREFIKSY` | krotka prefiksów kodów bez oklejonej krawędzi |
| `ZASLEPKI_ZASLANIAJA` | warstwy, które zasłaniają łby konfirmatów |
| `FORMATKI` | opisy formatek: `F(kod, nazwa, okleina, nawierty, uwagi)`; `dl`, `sz`, `szt` tylko dla pozycji spoza modelu |

Opcjonalne: `PDF_LICA` (opisy lic w arkuszu), `PDF_OPIS` (tekst strony tytułowej arkusza).

Otwory dodawane w `dodatkowe_otwory` (współrzędne lokalne płyty, liczone funkcją `loc(p, oś, wartość_modelu)`;
osie płyty `p['u']` = dłuższa, `p['v']` = krótsza; lico A = strona +oś grubości):
- w licu, nieprzelotowy: `dict(kind='FACE', side='A'|'B', u, v, d, depth, partner, axis_n, pin=True)` dla podpórek
  albo `pilot=True` dla nawiertów środka (oba wymagają `depth`); otwór w licu bez `pin` i `pilot` jest traktowany
  jak otwór pod konfirmat i rysowany z konfirmatem;
- w czole: `dict(kind='EDGE', n_axis_is_u, edge_coord, along, depth, d, partner, into)`; `d` = 8 oznacza kołek.

## 7. Nowe pomieszczenie krok po kroku
1. **Gałąź:** `git checkout -b NAZWA/start` od aktualnego `main`.
2. **Katalog:** `cp -r szablon NAZWA`, usuń `NAZWA/wyniki/` i `NAZWA/laczniki.gen.js`.
   W `index.html` popraw `<title>` i komentarz. W `README.md` opis pomieszczenia.
3. **Pomiary:** wypełnij `pomiary.md` (zdjęcia z wymiarem w nazwie pliku; miernik laserowy w metrach, kątownik w mm).
   Na początku `ustalenia.md` zapisz, która ściana jest lewa, a która tylna.
4. **Pusty pokój:** w `model.js` ustaw stałe z pomiarów, `room`, `openings`, `views`, przeszkody (piony, gzymsy,
   gniazdka, rury) jako bryły w osobnych warstwach. `ITEMS` może jeszcze nie mieć formatek;
   `FORMATKI` w `reguly.py` jest wtedy pustą listą.
5. **Potrzeby i koncepcja:** w `ustalenia.md`; bryły zamysłu jako półprzezroczyste prostopadłościany
   w warstwach z `conceptLayers` (bez kodów w nazwach, więc skrypty ich nie biorą).
6. **Konstrukcja:** formatki zgodnie z punktem 4 (reguły), fronty, zawiasy, reguły w `reguly.py`, opisy w `FORMATKI`.
7. **Przeliczenie:** `python3 wspolne/pipeline/run.py NAZWA`; sprawdź `wyniki/podsumowanie.json`
   (kolizje otworów = 0) i widok `NAZWA/index.html`.
8. **Wzorzec sceny:** `python3 wspolne/testy/scena.py NAZWA/index.html wspolne/testy/wzorce/NAZWA_scena.json`.
   Bez wzorca test w GitHub Actions nie przejdzie (sprawdza każdy katalog z `model.js`).
9. **Kontrola całości:** `python3 wspolne/pipeline/run.py --wszystkie --sprawdz`, commit, push, PR do `main`.
10. **Zestawienia:** `komponenty.md` (okucia), instrukcja montażu, `weryfikacja.md` przed zamówieniem.

## 8. Praca równoległa
- Każde pomieszczenie na własnych gałęziach (`garderoba/...`, `kuchnia/...`), PR do `main`.
- Zmiany w `wspolne/` osobnym PR (gałąź `wspolne/...`), scalanym przed zmianami pomieszczeń, które z nich korzystają.
  Potem gałęzie pomieszczeń robią rebase na `main`.
- Zmiana we `wspolne/`, która zmienia wyniki lub scenę innego pomieszczenia, zatrzyma się na teście. Jeśli jest
  zamierzona: przelicz to pomieszczenie, odśwież jego wzorzec sceny i opisz zmianę w jego `ustalenia.md`.
- Konflikt w pliku generowanym (`laczniki.gen.js`, `wyniki/`, wzorzec sceny) rozwiązuje się przeliczeniem,
  nie ręcznym scalaniem.
- Wspólne zamówienie kilku pomieszczeń: prefiks pomieszczenia przed kodem (np. `GD-F1`).
