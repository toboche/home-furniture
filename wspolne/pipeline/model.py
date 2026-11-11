"""Wczytanie modelu pomieszczenia (model.js) i zamiana płyt 18 mm na formatki."""
import json, os, re, subprocess

TU = os.path.dirname(os.path.abspath(__file__))
GRUBOSC = 18


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


def formatki(items, warstwy, modul_of):
    """Płyty z warstw formatek: każda bryła z kodem 'KOD:' lub 'KOD-1:' i jednym wymiarem równym 18 mm."""
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
        cienkie = [a for a in 'xyz' if abs(dims[a] - GRUBOSC) < 1e-6]
        assert cienkie, 'formatka bez wymiaru 18 mm: ' + it['n']
        p['t'] = cienkie[0]
        lo = {'x': p['x'], 'y': p['y'], 'z': p['z']}
        p['lo'] = lo
        p['hi'] = {a: lo[a] + dims[a] for a in 'xyz'}
        parts.append(p)
    return parts
