# Instrukcje dla Claude w tym repozytorium

Projekty mebli na wymiar do mieszkania, po jednym katalogu na pomieszczenie (`pralnia/`, `garderoba/`, `kuchnia/`).
Struktura, reguły modelu i dodawanie pomieszczeń: `wspolne/STRUKTURA.md`. Założenia meblarskie: `wspolne/zasady.md`.

## Zasady pracy
- Rozmowy po polsku. Kody wymiarów, formatek i frontów na rysunkach i w tabelach: TYLKO DUŻE LITERY, bez mieszania z małymi.
- Źródło prawdy to repozytorium: `ustalenia.md` (decyzje), `pomiary.md` (wymiary), `model.js` (geometria).
  Dokumenty w projekcie Claude mogą być nieaktualnymi kopiami; przy rozbieżności wygrywa repozytorium.
- Każda zmiana decyzji lub wymiaru trafia od razu do `ustalenia.md` (wpis z datą) albo `pomiary.md`
  (stara wartość do kolumny WCZEŚNIEJ), w tym samym commicie co zmiana modelu.
- Zmiany commitujemy i pushujemy na bieżąco, po każdej zakończonej zmianie, żeby użytkownik nie musiał pobierać plików.
- Wymiar, którego nie podał użytkownik, oznaczamy jako założenie i pytamy, zamiast zgadywać.

## Pomieszczenia i gałęzie
- Pracuj tylko w katalogu pomieszczenia, o które chodzi w rozmowie, na gałęzi tego pomieszczenia
  (`garderoba/...`, `kuchnia/...`), z PR do `main`. Nie zmieniaj katalogów innych pomieszczeń.
- Zmiany w `wspolne/` (silnik widoku, pipeline, testy) rób osobnym PR na gałęzi `wspolne/...` i opisz w nim,
  które pomieszczenia dotyka. Nie dokładaj ich po cichu do zmian pomieszczenia.
- Pralnia jest przed zamówieniem: zmiany w niej tylko na wyraźną prośbę użytkownika.

## Po każdej zmianie modelu lub reguł
```
python3 wspolne/pipeline/run.py NAZWA                 # przelicza laczniki.gen.js i wyniki/
python3 wspolne/pipeline/run.py --wszystkie --sprawdz # wszystkie pomieszczenia zgodne z modelami
python3 wspolne/testy/scena.py NAZWA/index.html /tmp/s.json wspolne/testy/wzorce/NAZWA_scena.json
```
- Plików generowanych (`laczniki.gen.js`, `wyniki/`, wzorce scen) nie edytuj ręcznie; konflikt w nich rozwiązuj przeliczeniem.
- Sprawdź `wyniki/podsumowanie.json` (kolizje otworów = 0, liczby konfirmatów, kołków, zaślepek) i porównaj z `komponenty.md`.
- Zamierzona zmiana widoku: odśwież wzorzec (`scena.py NAZWA/index.html wspolne/testy/wzorce/NAZWA_scena.json`)
  i napisz w opisie commita, co się zmieniło.
- Środowisko bez internetu nie wczyta Three.js z CDN: widok sprawdzaj testem `scena.py` (atrapa Three.js),
  a użytkownika poproś o obejrzenie strony.

## Nowe pomieszczenie
Kroki w `wspolne/STRUKTURA.md`, punkt 7: kopia `szablon/`, pomiary, pusty pokój, koncepcja, konstrukcja, przeliczenie,
wzorzec sceny, PR.
