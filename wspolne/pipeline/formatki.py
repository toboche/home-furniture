"""Lista formatek do zamówienia (formatki.csv).
Wymiary (DL, SZ) i ilości bierzemy z modelu 3D; opisy, okleinę i nawierty z reguly.FORMATKI pomieszczenia.
Pozycje spoza modelu (np. półka luzem) podają dl, sz i szt jawnie (i grubość, jeśli inna niż 18).
Płyta 18 mm trafia do formatki.csv; płyty innej grubości (reguly.GRUBOSCI) do osobnych plików formatki_<g>mm.csv,
bo w sklepie to osobny materiał. Pomieszczenie tylko z płytą 18 mm ma wyniki takie jak wcześniej."""
import collections, csv, os, re
from model import GRUBOSC, grubosc_bryly


def F(kod, nazwa, okleina='', nawierty='', uwagi='', dl=None, sz=None, szt=None, grubosc=None):
    return dict(kod=kod, nazwa=nazwa, okleina=okleina, nawierty=nawierty, uwagi=uwagi, dl=dl, sz=sz, szt=szt, grubosc=grubosc)


def _wymiary(it, grubosci=(GRUBOSC,)):
    """(DL, SZ, grubość) bryły; bez pasującej grubości: pomija wymiar najbliższy 18 (jak wcześniej)"""
    d = [it['w'], it['h'], it['d']]
    t, g = grubosc_bryly(it, grubosci)
    if t:
        d.remove({'x': it['w'], 'y': it['h'], 'z': it['d']}[t])
    else:
        g = GRUBOSC
        d.remove(min(d, key=lambda v: abs(v - GRUBOSC)))
    return max(d), min(d), g


def z_modelu(items, warstwy_formatek, grubosci=(GRUBOSC,)):
    """kod bazowy -> lista (DL, SZ, grubość) wszystkich brył z tym kodem (płyty korpusu i fronty F1, F2…)."""
    out = collections.OrderedDict()
    for it in items:
        if 't' in it:
            continue
        if it.get('layer') in warstwy_formatek:
            m = re.match(r'^([A-Z0-9]+)(?:-[0-9]+)?:', it['n'])
        elif it.get('layer') == 'Fronty':
            m = re.match(r'^(F\d+):', it['n'])
        else:
            continue
        if m:
            out.setdefault(m.group(1), []).append(_wymiary(it, grubosci))
    return out


def plik_grubosci(sciezka, g):
    """formatki.csv dla 18 mm, formatki_16mm.csv dla 16 mm itd."""
    if g == GRUBOSC:
        return sciezka
    base, ext = os.path.splitext(sciezka)
    return '%s_%gmm%s' % (base, g, ext)


def zapisz(items, R, sciezka, log=print, grubosci=(GRUBOSC,)):
    """Zapisuje formatki.csv (18 mm) i formatki_<g>mm.csv (inne grubości). Zwraca podsumowanie płyty 18 mm
    i słownik {g: podsumowanie} dla pozostałych grubości."""
    model = z_modelu(items, R.WARSTWY_FORMATEK, grubosci)
    rows = []
    for e in R.FORMATKI:
        k = e['kod']
        if k in model:
            dims = set(model[k])
            assert len(dims) == 1, '%s: różne wymiary brył o tym samym kodzie: %s' % (k, sorted(dims))
            dl, sz, g = dims.pop(); szt = len(model[k])
            for nazwa, v, mv in (('dl', e['dl'], dl), ('sz', e['sz'], sz), ('szt', e['szt'], szt)):
                assert v is None or v == mv, '%s: %s w opisie %s, w modelu %s' % (k, nazwa, v, mv)
        else:
            assert e['dl'] is not None and e['sz'] is not None and e['szt'], '%s: brak w modelu, podaj dl, sz i szt' % k
            dl, sz, szt = max(e['dl'], e['sz']), min(e['dl'], e['sz']), e['szt']
            g = e['grubosc'] or GRUBOSC
        rows.append((g, [k, e['nazwa'], dl, sz, szt, e['okleina'], e['nawierty'], e['uwagi']]))
    brak = [k for k in model if k not in {e['kod'] for e in R.FORMATKI}]
    assert not brak, 'formatki w modelu bez opisu w reguly.FORMATKI: %s' % brak
    wyniki = {}
    for g in sorted({gr for gr, _ in rows} | {GRUBOSC}, key=lambda v: (v != GRUBOSC, v)):   # 18 mm zawsze (choćby pusty plik)
        rr = [r for gr, r in rows if gr == g]
        with open(plik_grubosci(sciezka, g), 'w', newline='', encoding='utf-8-sig') as fh:
            w = csv.writer(fh, delimiter=';')
            w.writerow(['KOD', 'NAZWA', 'DL', 'SZ', 'SZT', 'OKLEINA', 'NAWIERTY', 'UWAGI'])
            for r in rr:
                w.writerow(r)
        area = sum(r[2] * r[3] * r[4] / 1e6 for r in rr); n = sum(r[4] for r in rr)
        log(len(rr), 'pozycji; pole m2: %.2f' % area, 'sztuk', n, '' if g == GRUBOSC else '(płyta %g mm)' % g)
        wyniki[g] = dict(pozycje=len(rr), sztuki=n, m2=round(area, 2))
    return wyniki.pop(GRUBOSC), wyniki
