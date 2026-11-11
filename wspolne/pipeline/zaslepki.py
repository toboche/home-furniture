"""Klasyfikacja łbów konfirmatów: widoczne (potrzebna zaślepka) i ukryte (przy ścianie pokoju, sąsiedniej bryle)."""
import collections
from model import bryly
from laczniki_3d import inv

TOL = 6.0     # mm: łeb zasłonięty, jeśli 6 mm od lica jest inna bryła (szczeliny do 6 mm są niewidoczne)
SUFIT = 12    # mm: przy suficie łeb jest niewidoczny, jeśli lico jest bliżej niż 12 mm


def policz(parts, items, room, R, log=print):
    boxes = [(p['code'], p['lo'], p['hi']) for p in parts]
    for warstwa in R.ZASLEPKI_ZASLANIAJA:
        for (n, x, y, z, w, h, d) in bryly(items, warstwa):
            boxes.append((n[:20], {'x': x, 'y': y, 'z': z}, {'x': x + w, 'y': y + h, 'z': z + d}))
    W, D, H = room['W'], room['D'], room['H']
    res = collections.Counter(); vis = []; hid = []
    for p in parts:
        if 'sub' in p or R.pomijaj_czesc(p):
            continue
        t = p['t']
        for h in p['holes']:
            if h['kind'] != 'FACE' or h.get('pin') or h.get('pilot'):
                continue
            pos = {p['u']: inv(p, p['u'], h['u']), p['v']: inv(p, p['v'], h['v'])}
            outer = p['lo'][t] if h['side'] == 'B' else p['hi'][t]
            sg = -1 if h['side'] == 'B' else 1
            q = dict(pos); q[t] = outer + sg * TOL
            hidden = False
            if t == 'x' and (q['x'] < TOL or q['x'] > W - TOL): hidden = True    # lewa i prawa ściana
            if t == 'z' and (q['z'] < TOL or q['z'] > D - TOL): hidden = True    # tylna i przednia ściana
            if t == 'y' and q['y'] > H - SUFIT: hidden = True                     # sufit
            for c, lo, hi in boxes:
                if c == p['code']:
                    continue
                if all(lo[a] - 1e-6 <= q[a] <= hi[a] + 1e-6 for a in 'xyz'):
                    hidden = True; break
            (hid if hidden else vis).append((p['code'], h['partner'], round(q['x']), round(q['y']), round(q['z'])))
            res['ukryte' if hidden else 'widoczne'] += 1
    log('łby konfirmatów:', dict(res))
    by = collections.Counter(v[0] for v in vis)
    log('widoczne wg części:', dict(by))
    return dict(widoczne=len(vis), ukryte=len(hid), widoczne_wg_czesci=dict(sorted(by.items())), widoczne_miejsca=sorted(set(vis)))
