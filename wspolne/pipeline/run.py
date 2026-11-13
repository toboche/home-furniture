"""Pełne przeliczenie pomieszczenia z modelu 3D.

    python3 wspolne/pipeline/run.py pralnia            # przelicza i zapisuje wyniki
    python3 wspolne/pipeline/run.py pralnia --sprawdz  # przelicza do katalogu tymczasowego i porównuje
                                                        # z plikami w repozytorium (test regresji; PDF pomijany,
                                                        # bo zależy od wersji matplotlib, a jego treść wynika z otwory.json)
    python3 wspolne/pipeline/run.py --wszystkie --sprawdz

Wejście (katalog pomieszczenia): model.js (dane 3D), reguly.py (reguły pomieszczenia).
Wyjście: laczniki.gen.js (łączniki do widoku 3D) oraz wyniki/:
    formatki.csv, kalkulator_nawierty.csv, arkusz_nawiertow.pdf, otwory.json, podsumowanie.json,
    <pomieszczenie>_3d.html (wersja jednoplikowa widoku do wysłania lub publikacji).
    Płyty o grubości innej niż 18 mm (reguly.GRUBOSCI, np. skrzynki szuflad 16 mm) dostają osobne
    formatki_<g>mm.csv i kalkulator_nawierty_<g>mm.csv; w podsumowaniu klucze formatki_<g>mm i kalkulator_<g>mm.
"""
import filecmp, importlib, json, os, shutil, sys, tempfile

TU = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(TU))
sys.path.insert(0, TU)

import model as M, laczenia, otwory, kalkulator, arkusz_pdf, laczniki_3d, zaslepki, formatki, pakiet


def pomieszczenia():
    return sorted(d for d in os.listdir(REPO) if os.path.isfile(os.path.join(REPO, d, 'model.js')) and os.path.isfile(os.path.join(REPO, d, 'reguly.py')))


def _round(o):
    if isinstance(o, dict): return {k: _round(v) for k, v in sorted(o.items())}
    if isinstance(o, (list, tuple)): return [_round(v) for v in o]
    if isinstance(o, float): return round(o, 6)
    return o


def przelicz(nazwa, cel, cel_gen, log=print):
    """cel: katalog na wyniki/, cel_gen: ścieżka laczniki.gen.js"""
    kat = os.path.join(REPO, nazwa)
    sys.path.insert(0, kat)
    if 'reguly' in sys.modules: del sys.modules['reguly']
    R = importlib.import_module('reguly')
    sys.path.remove(kat)
    dane = M.wczytaj(kat)
    items = dane['items']
    os.makedirs(cel, exist_ok=True)

    grubosci = M.grubosci_z(R)
    parts = M.formatki(items, R.WARSTWY_FORMATEK, R.modul_of, grubosci)
    J = laczenia.wykryj(parts, log)
    otwory.przygotuj(parts)
    n_pol = otwory.konfirmaty(parts, J, R)
    P = {p['code']: p for p in parts}
    R.dodatkowe_otwory(P, parts, otwory.loc)
    otwory.prowadniki(parts, items, R, log)
    uwagi = otwory.kolizje(parts, R)
    log('kolizje otworów:', len(uwagi))
    for u in uwagi[:30]: log('  ', u)
    tot = sum(len(p['holes']) for p in parts if not R.pomijaj_czesc(p))
    log('otworów łącznie:', tot, 'połączeń:', n_pol)

    s_kalk, s_kalk_inne = kalkulator.zapisz(parts, R, os.path.join(cel, 'kalkulator_nawierty.csv'), log)
    lines, s_lacz = laczniki_3d.generuj(parts, items, R, log)
    laczniki_3d.zapisz(lines, cel_gen, nazwa)
    s_zasl = zaslepki.policz(parts, items, dane['room'], R, log)
    s_form, s_form_inne = formatki.zapisz(items, R, os.path.join(cel, 'formatki.csv'), log, grubosci)
    strony = arkusz_pdf.zapisz(parts, R, os.path.join(cel, 'arkusz_nawiertow.pdf'), log)

    klucze = ('code', 'mod', 't', 'lo', 'hi', 'u', 'v', 'DL', 'SZ', 'rh', 'holes')
    # grubość zapisujemy tylko dla płyt innych niż 18 mm (pliki pomieszczeń z samą płytą 18 bez zmian)
    json.dump(_round([dict({k: p[k] for k in klucze}, **({'g': p['g']} if p.get('g', M.GRUBOSC) != M.GRUBOSC else {})) for p in parts]),
              open(os.path.join(cel, 'otwory.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    s_zasl['widoczne_miejsca'] = ['%s → %s (x %d, y %d, z %d)' % v for v in s_zasl['widoczne_miejsca']]
    pods = dict(formatki=s_form, kalkulator=s_kalk, laczniki=s_lacz, zaslepki=s_zasl, polaczenia=n_pol,
                otwory_lacznie=tot, kolizje_otworow=len(uwagi), strony_arkusza=strony)
    for g, s in s_form_inne.items():
        pods['formatki_%gmm' % g] = s
    for g, s in s_kalk_inne.items():
        pods['kalkulator_%gmm' % g] = s
    with open(os.path.join(cel, 'podsumowanie.json'), 'w', encoding='utf-8') as fh:
        json.dump(pods, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    pakiet.zapisz(kat, cel_gen, os.path.join(cel, '%s_3d.html' % os.path.basename(nazwa)))
    return pods


def sprawdz(nazwa):
    kat = os.path.join(REPO, nazwa)
    tmp = tempfile.mkdtemp()
    try:
        przelicz(nazwa, os.path.join(tmp, 'wyniki'), os.path.join(tmp, 'laczniki.gen.js'), log=lambda *a: None)
        rozne = []
        pary = [(os.path.join(tmp, 'laczniki.gen.js'), os.path.join(kat, 'laczniki.gen.js'))]
        for f in sorted(os.listdir(os.path.join(tmp, 'wyniki'))):
            if f.endswith('.pdf'):
                continue   # PDF zależy od wersji matplotlib; jego treść w całości wynika z otwory.json, które jest porównywane
            pary.append((os.path.join(tmp, 'wyniki', f), os.path.join(kat, 'wyniki', f)))
        for a, b in pary:
            if not os.path.exists(b) or not filecmp.cmp(a, b, shallow=False):
                rozne.append(os.path.relpath(b, REPO))
        if rozne:
            print('%s: wyniki NIEAKTUALNE albo zmienione względem repozytorium:' % nazwa)
            for r in rozne: print('   ', r)
            print('   Jeśli zmiana jest zamierzona: python3 wspolne/pipeline/run.py %s, potem commit.' % nazwa)
            return False
        print('%s: wyniki zgodne z repozytorium (%d plików)' % (nazwa, len(pary)))
        return True
    finally:
        shutil.rmtree(tmp)


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if '--wszystkie' in sys.argv: args = pomieszczenia()
    if not args:
        print(__doc__); sys.exit(2)
    if '--sprawdz' in sys.argv:
        sys.exit(0 if all([sprawdz(n) for n in args]) else 1)
    for n in args:
        kat = os.path.join(REPO, n)
        przelicz(n, os.path.join(kat, 'wyniki'), os.path.join(kat, 'laczniki.gen.js'))
