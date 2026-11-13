"""Wczytanie modelu pomieszczenia (model.js) i zamiana płyt na formatki.
Grubości płyt: reguly.GRUBOSCI pomieszczenia (domyślnie tylko 18 mm); pierwsza na liście to płyta podstawowa."""
import json, os, re, subprocess

TU = os.path.dirname(os.path.abspath(__file__))
GRUBOSC = 18      # płyta podstawowa (korpusy i fronty)


def wczytaj(katalog):
    """Zwraca dict z polami room, title i items (bez funkcji, tak jak w model.js)."""
    out = subprocess.run(['node', os.path.join(TU, 'dump_model.js'), os.path.join(katalog, 'model.js')],
                         check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def kod(it):
    m = re.match(r'^([A-Z0-9]+(?:-[0-9]+)?):', it['n'])
    return m.group(1) if m else None


def bryly(items, warstwa):
    """Prostopadłościany danej warstwy jako krotki (n, x, y, z, w, h, d) z liczbami float."""
    return [(i['n'],) + tuple(float(i[k]) for k in 'xyzwhd')
            for i in items if i.get('layer') == warstwa and 't' not in i]


def grubosci_z(R):
    """grubości płyt pomieszczenia: reguly.GRUBOSCI (krotka w mm), domyślnie (18,)"""
    return tuple(getattr(R, 'GRUBOSCI', (GRUBOSC,)))


def grubosc_bryly(it, grubosci=(GRUBOSC,)):
    """(oś grubości, grubość) bryły: pierwsza grubość z listy, której równy jest któryś wymiar; (None, None) gdy brak"""
    dims = {'x': it['w'], 'y': it['h'], 'z': it['d']}
    for g in grubosci:
        cienkie = [a for a in 'xyz' if abs(dims[a] - g) < 1e-6]
        if cienkie:
            return cienkie[0], g
    return None, None


def formatki(items, warstwy, modul_of, grubosci=(GRUBOSC,)):
    """Płyty z warstw formatek: każda bryła z kodem 'KOD:' lub 'KOD-1:' i jednym wymiarem równym grubości płyty
    (18 mm albo inna z reguly.GRUBOSCI). p['g'] = grubość płyty."""
    parts = []
    for it in items:
        if it.get('layer') not in warstwy:
            continue
        p = {k: it[k] for k in ('n', 'layer', 'x', 'y', 'z', 'w', 'h', 'd')}
        p['n'] = p['n'][:60]
        c = kod(p)
        assert c, 'formatka bez kodu: ' + it['n']
        p['code'] = c
        p['mod'] = modul_of(p)
        dims = {'x': p['w'], 'y': p['h'], 'z': p['d']}
        t, g = grubosc_bryly(p, grubosci)
        assert t, 'formatka bez wymiaru %s mm: %s' % ('/'.join('%g' % v for v in grubosci), it['n'])
        p['t'] = t; p['g'] = g
        lo = {'x': p['x'], 'y': p['y'], 'z': p['z']}
        p['lo'] = lo
        p['hi'] = {a: lo[a] + dims[a] for a in 'xyz'}
        parts.append(p)
    return parts
