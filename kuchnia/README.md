# Kuchnia
Uzupełnienie istniejącej kuchni (płyta Egger H3710 Orzech Carini naturalny): półka z LED na płytkach (P1, P3, płyta 18 mm, na prętach M8),
szafka okapowa SO z okapem Ciarko Design DUO 55 i frontem F1 (push-to-open), wąska otwarta szafka WS ze skrzynką na rurę okapu.
Brakujące fronty szuflad istniejącej kuchni (IKEA METOD): `zamowienie/` (lista, rysunek dopasowania usłojenia do maila).

Pliki: `pomiary.md`, `ustalenia.md`, `model.js`, `reguly.py`, `index.html` (widok 3D), `wyniki/` (generowane:
`formatki.csv`, nawierty do kalkulatora, arkusz PDF, `kuchnia_3d.html`). Okucia i zakupy: `komponenty.md`. Weryfikacja przed zamówieniem: `weryfikacja.md`.
Audyty: `audyt/v1.md`–`v6.md` (stan wdrożenia w `ustalenia.md`, 2026-11-18 i 2026-11-19). Wycena: `zamowienie/wycena.md`. Parametry zamówienia (słoje, okleina, F1): `zamowienie.md`; prompt agenta: `zamowienie/prompt_agenta_zamowienie.md`.
Przeliczenie: `python3 wspolne/pipeline/run.py kuchnia` (z katalogu głównego).
Montaż krok po kroku (widok 3D, 12 kroków): `montaz/montaz_3d.html`, budowany z `model.js` przez `python3 kuchnia/montaz/montaz.py` (uruchomić po zmianie modelu lub kolejności montażu).
