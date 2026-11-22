# Rejestr zamówień (`wspolne/zamowienia/`)

Centralny katalog wszystkich zamówień (płyty z rozkrojem i CNC, okucia/akcesoria, blaty, fronty, oświetlenie) dla wszystkich pomieszczeń w repozytorium `home-furniture`.
Zaprojektowany tak, aby **użytkownik i każdy agent LLM** (w dowolnej rozmowie dla `pralnia/`, `garderoba/`, `przedpokoj/`, `kuchnia/` itd.) mógł w jednym miejscu sprawdzić: co już jest zamówione lub w koszyku, za ile, z jakim terminem, jakie były odstępstwa względem modeli oraz które rewizje zostały zastąpione.

---

## 1. Tabela zbiorcza zamówień

> **Zasada statusów:**
> - `robocze w koszyku` — wprowadzone do koszyka u dostawcy, **nieopłacone** (czeka na potwierdzenie/płatność użytkownika)
> - `złożone` — opłacone / w realizacji u dostawcy
> - `dostarczone` — odebrane i zweryfikowane po dostawie
> - `zastąpione` — historyczna rewizja wycofana z koszyka i zastąpiona nowszym numerem (zostaje w tabeli dla pełnego śladu audytowego)

| Data | ID / Numer | Sklep / Dostawca | Pomieszczenia | Kategoria | Status | Kwota brutto | Planowana wysyłka / dostawa | Audyt | Szczegóły i manifest |
|---|---|---|---|---|---|---:|---|---|---|
| 2026-11-22 | **`21825702`** ([link](https://centrum.meble.pl/rozkroj,r21825702)) | `centrum.meble.pl` | `pralnia`, `garderoba` | płyty 18/16 mm + okleina + CNC | **`robocze w koszyku`** *(PREMIUM +standard)* | `5 924,63 PLN` | `10.12.2026` *(ważny do 20.01.2027)* | **85/85 + 620/620 (100% live DOM + wydruk)** | [2026-11-22_centrum-meble_pralnia-garderoba_21825702.md](2026-11-22_centrum-meble_pralnia-garderoba_21825702.md) |
| 2026-11-21 | ~~`21811821`~~ | `centrum.meble.pl` | `pralnia`, `garderoba` | płyty 18/16 mm + okleina + CNC | `zastąpione` przez `21825702` *(usunięte z koszyka)* | `5 924,63 PLN` | — | 84/85 *(1 błąd: `GD-S2D` #3 `x=357→417`)* | historia w [2026-11-22_centrum-meble_pralnia-garderoba_21825702.md](2026-11-22_centrum-meble_pralnia-garderoba_21825702.md) |

---

## 2. Jak dodawać kolejne zamówienia (standard dla ludzi i agentów LLM)

1. **Konwencja nazwy pliku:**
   ```
   YYYY-MM-DD_<dostawca>_<pomieszczenia>_<id-lub-temat>.md
   ```
   Przykłady:
   - `2026-11-22_centrum-meble_pralnia-garderoba_21825702.md`
   - `2026-11-25_blum-okucia_pralnia-garderoba_01.md`
   - `2026-11-28_centrum-meble_przedpokoj_21910042.md`
   - `2026-12-01_centrum-meble_kuchnia_21920510.md`
2. **Wymagane sekcje w pliku zamówienia:**
   1. **Metadane zlecenia** (numer, link, status, ważność, kwota brutto/netto, planowana wysyłka, commit/gałąź bazowa z repozytorium).
   2. **Rozbicie kosztów i materiałów** (dokładnie z koszyka / faktury / podsumowania dostawcy).
   3. **Sumy kontrolne vs repozytorium** (liczby pozycji, sztuk, m², wierceń lub okuć porównane z `wyniki/podsumowanie.json` / `komponenty.md`).
   4. **Kontrole i audyt** (co zweryfikowano przed dodaniem do koszyka i po audycie końcowym).
   5. **Wykaz odstępstw względem repozytorium i ocena wpływu** (pogrupowane per pomieszczenie, z listą prac ręcznych po dostawie).
   6. **Historia rewizji i poprawek** (jeśli zamówienie zastępuje wcześniejszy draft/rozkrój — dokładnie co i dlaczego zmieniono).
   7. **Kompletny manifest pozycji** (kody `DUŻYMI LITERAMI` z prefiksami pomieszczeń przy zamówieniach wspólnych: `PR-`, `GD-`, `PP-`, `KU-`).
3. **Aktualizacje po utworzeniu lub zmianie zamówienia:**
   - Dopisz lub zaktualizuj wiersz w tabeli w `wspolne/zamowienia/README.md`.
   - Jeśli zmieniasz istniejący rozkrój/koszyk na nowy numer ID: oznacz stary wiersz jako `zastąpione`, dodaj nowy jako aktualny i opisz powód zmiany w historii rewizji.
   - Dopisz krótki wpis z datą i linkiem do pliku w `<pomieszczenie>/ustalenia.md` dla każdego pomieszczenia objętego zamówieniem.
   - Zacommituj i wypchnij od razu na `main`.
4. **Instrukcje techniczne konkretnych sklepów:**
   - Kalkulator rozkroju i CNC `centrum.meble.pl`: [wspolne/centrum_meble.md](../centrum_meble.md).
