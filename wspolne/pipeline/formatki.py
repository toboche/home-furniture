"""Lista formatek do zamówienia (formatki.csv).
Wymiary (DL, SZ) i ilości bierzemy z modelu 3D; opisy, okleinę i nawierty z reguly.FORMATKI pomieszczenia.
Pozycje spoza modelu (np. półka luzem) podają dl, sz i szt jawnie."""
import collections, csv, re
from model import GRUBOSC


def F(kod, nazwa, okleina='', nawierty='', uwagi='', dl=None, sz=None, szt=None):
    return dict(kod=kod, nazwa=nazwa, okleina=okleina, nawierty=nawierty, uwagi=uwagi, dl=dl, sz=sz, szt=szt)


def _wymiary(it):
    d = [it['w'], it['h'], it['d']]
    d.remove(GRUBOSC) if GRUBOSC in d else d.remove(min(d, key=lambda v: abs(v - GRUBOSC)))
    return max(d), min(d)


def z_modelu(items, warstwy_formatek):
    """kod bazowy -> lista (DL, SZ) wszystkich brył z tym kodem (płyty korpusu i fronty F1, F2…)."""
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
            out.setdefault(m.group(1), []).append(_wymiary(it))
    return out


def zapisz(items, R, sciezka, log=print):
    model = z_modelu(items, R.WARSTWY_FORMATEK)
    rows = []
    for e in R.FORMATKI:
        k = e['kod']
        if k in model:
            dims = set(model[k])
            assert len(dims) == 1, '%s: różne wymiary brył o tym samym kodzie: %s' % (k, sorted(dims))
            dl, sz = dims.pop(); szt = len(model[k])
            for nazwa, v, mv in (('dl', e['dl'], dl), ('sz', e['sz'], sz), ('szt', e['szt'], szt)):
                assert v is None or v == mv, '%s: %s w opisie %s, w modelu %s' % (k, nazwa, v, mv)
        else:
            assert e['dl'] is not None and e['sz'] is not None and e['szt'], '%s: brak w modelu, podaj dl, sz i szt' % k
            dl, sz, szt = max(e['dl'], e['sz']), min(e['dl'], e['sz']), e['szt']
        rows.append([k, e['nazwa'], dl, sz, szt, e['okleina'], e['nawierty'], e['uwagi']])
    brak = [k for k in model if k not in {e['kod'] for e in R.FORMATKI}]
    assert not brak, 'formatki w modelu bez opisu w reguly.FORMATKI: %s' % brak
    with open(sciezka, 'w', newline='', encoding='utf-8-sig') as fh:
        w = csv.writer(fh, delimiter=';')
        w.writerow(['KOD', 'NAZWA', 'DL', 'SZ', 'SZT', 'OKLEINA', 'NAWIERTY', 'UWAGI'])
        for r in rows:
            w.writerow(r)
    area = sum(r[2] * r[3] * r[4] / 1e6 for r in rows); n = sum(r[4] for r in rows)
    log(len(rows), 'pozycji; pole m2: %.2f' % area, 'sztuk', n)
    return dict(pozycje=len(rows), sztuki=n, m2=round(area, 2))
