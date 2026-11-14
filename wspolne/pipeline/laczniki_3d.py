"""Bryły łączników do wizualizacji 3D (otwory, konfirmaty, kołki, podpórki, puszki zawiasów) -> laczniki.gen.js."""
import re
from model import bryly
from otwory import front_zawiasu

DARK = 0x15181b; STEEL = 0xc7a008; HEAD = 0xd8b310; WOOD = 0xb08a5b


def inv(p, a, x):
    """współrzędna lokalna widoku z lica A -> współrzędna modelu na osi a (a = u lub v)"""
    if a == p['u'] and not p['rh']:
        return p['lo'][a] + p['DL'] - x
    return p['lo'][a] + x


def f(x):
    return ('%.2f' % x).rstrip('0').rstrip('.')


def generuj(parts, items, R, log=print):
    out = []

    def cyl(n, layer, ax, center, r, ln, c):
        out.append("  {t:'cyl3',n:'%s',layer:'%s',ax:'%s',px:%s,py:%s,pz:%s,r:%s,len:%s,c:0x%06x}," % (n, layer, ax, f(center['x']), f(center['y']), f(center['z']), f(r), f(ln), c))

    nconf = nhole = nedge = ndow = npin = 0
    seen_dowel = set()
    for p in parts:
        if 'sub' in p or R.pomijaj_czesc(p):
            continue
        t = p['t']; tn = p['hi'][t] - p['lo'][t]; tm = (p['hi'][t] + p['lo'][t]) / 2
        for h in p['holes']:
            if h['kind'] == 'FACE':
                pos = {p['u']: inv(p, p['u'], h['u']), p['v']: inv(p, p['v'], h['v'])}
                if h.get('pin') or h.get('pilot'):
                    # nieprzelotowy, od lica po stronie półki (A = +t)
                    top = p['hi'][t] if h['side'] == 'A' else p['lo'][t]
                    sgn = -1 if h['side'] == 'A' else 1
                    c = dict(pos); c[t] = top + sgn * h['depth'] / 2
                    nazwa = h['opis'] + ' w ' + p['code'] if h.get('opis') else (((('Nawiert pilotowy Ø3 x 12 pod wkręt prowadnika (%s) w %s' % (h['partner'][-2:], p['code'])) if h.get('plate') else ('Nawiert środka Ø5 x 5 pod otwór wycinany samodzielnie w %s' % p['code'])) if h.get('pilot') else ('Otwór Ø5 x 10 pod podpórkę w %s' % p['code'])))
                    cyl(nazwa, 'Otwory', t, c, h['d'] / 2, h['depth'] + 0.6, DARK); npin += 1
                    continue
                c = dict(pos); c[t] = tm
                cyl('Otwór Ø5 przelotowy w %s (pod konfirmat do %s)' % (p['code'], h['partner']), 'Otwory', t, c, h['d'] / 2, tn + 0.6, DARK); nhole += 1
                # konfirmat: od lica zewnętrznego w stronę części krawędziowej (50 mm)
                outer = p['lo'][t] if h['side'] == 'B' else p['hi'][t]
                dr = 1 if h['side'] == 'B' else -1
                c2 = dict(pos); c2[t] = outer + dr * 25
                cyl('Konfirmat 7 x 50: %s → %s' % (p['code'], h['partner']), 'Konfirmaty', t, c2, 3.5, 50, STEEL)
                c3 = dict(pos); c3[t] = outer + dr * 1   # łeb zlicowany z lica (wpuszczony fazownikiem)
                cyl('Łeb konfirmatu: %s → %s' % (p['code'], h['partner']), 'Konfirmaty', t, c3, 5, 2, HEAD); nconf += 1
            else:
                a_e = p['u'] if h['n_axis_is_u'] else p['v']      # oś, wzdłuż której idzie otwór
                a_a = p['v'] if h['n_axis_is_u'] else p['u']
                e0 = inv(p, a_e, h['edge_coord']); e1 = inv(p, a_e, h['edge_coord'] + h['into'] * h['depth'])
                c = {a_e: (e0 + e1) / 2, a_a: inv(p, a_a, h['along']), t: tm}
                if h.get('opis'):
                    # otwór opisany w reguly.dodatkowe_otwory (np. pod trzpień złącza mimośrodowego), bez kołka
                    cyl('%s w %s (do %s)' % (h['opis'], p['code'], h['partner']), 'Otwory', a_e, c, h['d'] / 2, abs(e1 - e0), DARK); nedge += 1
                elif h['d'] >= 8:
                    cyl('Otwór Ø8 x 20 pod kołek w %s (do %s)' % (p['code'], h['partner']), 'Otwory', a_e, c, h['d'] / 2, abs(e1 - e0), DARK); ndow += 1
                    key = tuple(sorted((p['code'], h['partner']))) + (round(c[a_a]),)
                    if key not in seen_dowel:
                        seen_dowel.add(key)
                        cyl('Kołek drewniany Ø8 x 40: %s + %s' % key[:2], 'Kołki', a_e, dict(c, **{a_e: e0}), 4, 40, WOOD)
                else:
                    cyl('Otwór Ø4 x 35 w %s (czoło, konfirmat z %s)' % (p['code'], h['partner']), 'Otwory', a_e, c, h['d'] / 2, abs(e1 - e0), DARK); nedge += 1
    log('konfirmatów', nconf, 'otw. licowych', nhole, 'otw. czołowych', nedge, 'otw. pod kołki', ndow, 'otw. pod podpórki', npin, 'kołków', len(seen_dowel))

    # puszki zawiasów Ø35 x 13 w tylnej stronie frontów (otwory pilotowe prowadników są na liście otworów ścianek)
    nh = 0
    for z in bryly(items, 'Zawiasy'):
        fr, cx, cy = front_zawiasu(items, z[1], z[2])
        code = fr[0].split(':')[0]
        cyl('Otwór zawiasu Ø35 x 13 w %s' % code, 'Otwory', 'z', dict(x=cx, y=cy, z=fr[3] + 6.5 - 0.3), 17.5, 13.6, DARK); nh += 1
        R.zawias_specjalny(code, fr, cx, cy, cyl)
    log('puszki', nh)
    stats = dict(konfirmaty=nconf, kolki=len(seen_dowel), otwory_pod_kolki=ndow, otwory_nieprzelotowe=npin, puszki_zawiasow=nh)
    return out, stats


def zapisz(lines, sciezka, katalog_nazwa):
    body = '\n'.join(lines).rstrip().rstrip(',')
    with open(sciezka, 'w', encoding='utf-8') as fh:
        fh.write("/* GENEROWANE: python3 wspolne/pipeline/run.py %s (nie edytować ręcznie).\n"
                 "   Otwory, konfirmaty, kołki i puszki zawiasów wyliczone z modelu (model.js). */\n"
                 "HF_MODEL.items.push(\n%s\n);\n" % (katalog_nazwa, body))
