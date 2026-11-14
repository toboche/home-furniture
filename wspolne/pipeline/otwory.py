"""Otwory w formatkach: konfirmaty w stykach, nawierty pilotowe pod prowadniki zawiasów, kontrola kolizji.
Otwory szczególne dla pomieszczenia (podpórki, kołki, nawierty środków) dodaje funkcja
reguly.dodatkowe_otwory(P, parts, loc) z katalogu pomieszczenia."""
import collections, math, re
from model import bryly

AX = 'xyz'
SPACING = 400      # mm: docelowy rozstaw konfirmatów
MARGIN = 50        # mm: pierwszy konfirmat od końca styku
EDGE_DEPTH = 35    # mm: głębokość otworu w czole
D = 5              # Ø otworu w licu (poszerzany do Ø7 samodzielnie)
DE = 4             # Ø otworu w czole
PLATE_D = 3; PLATE_DEPTH = 12        # nawierty pilotowe pod wkręty prowadników
PLATE_OD_FRONTU = 37                 # mm: linia wkrętów od tylnego lica frontu
PLATE_ROZSTAW = 32


def axes_of(p):
    inpl = [a for a in AX if a != p['t']]
    dim = lambda a: {'x': p['hi']['x'] - p['lo']['x'], 'y': p['hi']['y'] - p['lo']['y'], 'z': p['hi']['z'] - p['lo']['z']}[a]
    inpl.sort(key=lambda a: (-dim(a), AX.index(a)))
    return inpl[0], inpl[1]


def right_handed(u, v, t):
    perm = [AX.index(u), AX.index(v), AX.index(t)]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
    return inv % 2 == 0


def przygotuj(parts):
    for p in parts:
        p['u'], p['v'] = axes_of(p)
        p['DL'] = p['hi'][p['u']] - p['lo'][p['u']]; p['SZ'] = p['hi'][p['v']] - p['lo'][p['v']]
        p['rh'] = right_handed(p['u'], p['v'], p['t'])
        p['holes'] = []


def loc(p, a, val):
    """współrzędna lokalna widoku z lica A dla wartości modelu val na osi a (a = u lub v)"""
    x = val - p['lo'][a]
    if a == p['u'] and not p['rh']:
        x = p['DL'] - x
    return x


def spread(lo, hi, SPACING=SPACING):
    L = hi - lo
    if L < 150:
        return [(lo + hi) / 2]
    n = math.ceil((L - 2 * MARGIN) / SPACING) + 1
    if n < 2:
        n = 2
    return [lo + MARGIN + i * (L - 2 * MARGIN) / (n - 1) for i in range(n)]


def konfirmaty(parts, J, R):
    """Otwory pod konfirmaty w każdym połączeniu lico–czoło. Zwraca liczbę połączeń."""
    grp = collections.OrderedDict()
    for j in J:
        f, e = j['face']['code'], j['edge']['code']
        if R.pomijaj_polaczenie(f, e):
            continue
        k = (f, e, j['n'], round(j['pos'], 2))
        if k not in grp:
            grp[k] = dict(j)
        else:
            for a, (lo, hi) in j['ov'].items():
                lo0, hi0 = grp[k]['ov'][a]; grp[k]['ov'][a] = (min(lo, lo0), max(hi, hi0))
    for k, j in grp.items():
        face, edge, n = j['face'], j['edge'], j['n']
        oth = [a for a in AX if a != n]
        ext = {a: j['ov'][a] for a in oth}
        along = max(oth, key=lambda a: ext[a][1] - ext[a][0])
        across = [a for a in oth if a != along][0]
        mid = (ext[across][0] + ext[across][1]) / 2
        pts = spread(*ext[along], SPACING=R.rozstaw(face['code'], edge['code'], SPACING))
        pts = R.punkty(face['code'], edge['code'], ext[along], pts)
        # strona części licowej: otwór od strony przeciwnej do styku
        edge_above = abs(face['hi'][n] - j['pos']) < 0.01   # część krawędziowa leży po stronie +n
        side = 'B' if edge_above else 'A'      # A = lico po stronie +t (t==n)
        for pv in pts:
            fu = face['u']; fv = face['v']
            val = {along: pv, across: mid}
            fu_l = loc(face, fu, val[fu]); fv_l = loc(face, fv, val[fv])
            face['holes'].append(dict(kind='FACE', side=side, u=fu_l, v=fv_l, d=D, partner=edge['code'], axis_n=n))
            eu, ev = edge['u'], edge['v']
            edge_at_hi = abs(edge['hi'][n] - j['pos']) < 0.01
            e_l = loc(edge, along, pv)   # pozycja wzdłuż krawędzi
            if n == eu:
                ed_pos = loc(edge, eu, edge['hi'][eu] if edge_at_hi else edge['lo'][eu])
            else:
                ed_pos = loc(edge, ev, edge['hi'][ev] if edge_at_hi else edge['lo'][ev])
            edge['holes'].append(dict(kind='EDGE', n_axis_is_u=(n == eu), edge_coord=ed_pos, along=e_l, depth=EDGE_DEPTH, d=DE, partner=face['code'],
                into=(-1 if ed_pos > 0 and (n == eu and ed_pos >= edge['DL'] - 0.01 or n == ev and ed_pos >= edge['SZ'] - 0.01) else 1)))
    return len(grp)


def front_zawiasu(items, x, y):
    """Front (n, x, y, z, w, h), na którym leży zawias o lewym dolnym rogu (x, y); puszka Ø35, środek x+17,5."""
    cx, cy = x + 17.5, y + 17.5
    fr = [f for f in bryly(items, 'Fronty') if re.match(r'F\d+:', f[0])]
    f = [f for f in fr if f[1] <= cx <= f[1] + f[4] and f[2] <= cy <= f[2] + f[5]][0]
    return f, cx, cy


def prowadniki(parts, items, R, log=print):
    """Nawierty pilotowe Ø3 x 12 pod wkręty prowadników zawiasów (2 na zawias) w wewnętrznym licu ścianki."""
    PLATE_LOG = []
    for z in bryly(items, 'Zawiasy'):
        fr, cx, cy = front_zawiasu(items, z[1], z[2])
        code = fr[0].split(':')[0]
        if code in R.ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE:
            continue
        fx, fz, fw = fr[1], fr[3], fr[4]
        right = cx > fx + fw / 2
        edge = fx + fw if right else fx
        tgt = edge + 1.5 if right else edge - 1.5
        cand = [p for p in parts if p['t'] == 'x' and p['lo']['y'] <= cy <= p['hi']['y'] and p['hi']['z'] >= fz - 20 and abs((p['hi']['x'] if right else p['lo']['x']) - tgt) < 0.6]
        assert cand, (code, cy)
        w_ = cand[0]
        side = 'B' if right else 'A'       # lico po stronie wnętrza szafki (prawa ścianka: lico -x = B; lewa: +x = A)
        zp = fz - PLATE_OD_FRONTU
        zp = int(zp) if zp == int(zp) else zp
        for dy in (-PLATE_ROZSTAW // 2, PLATE_ROZSTAW // 2):
            pos = {'y': cy + dy, 'z': zp}
            w_['holes'].append(dict(kind='FACE', side=side, u=loc(w_, w_['u'], pos[w_['u']]), v=loc(w_, w_['v'], pos[w_['v']]), d=PLATE_D, depth=PLATE_DEPTH, partner='wkręt prowadnika zawiasu ' + code, axis_n='-', pin=False, pilot=True, plate=True))
        PLATE_LOG.append((code, w_['code'], cy))
    log('nawierty prowadników:', len(PLATE_LOG) * 2, 'w', len(PLATE_LOG), 'zawiasach')


def kolizje(parts, R):
    issues = []
    for p in parts:
        if R.pomijaj_czesc(p):
            continue
        fh = [h for h in p['holes'] if h['kind'] == 'FACE']
        eh = [h for h in p['holes'] if h['kind'] == 'EDGE']
        for i, a in enumerate(fh):
            for b in fh[i + 1:]:
                if a['side'] == b['side'] and math.hypot(a['u'] - b['u'], a['v'] - b['v']) < 20:
                    issues.append((p['code'], 'dwa otwory licowe blisko', a['u'], a['v'], b['u'], b['v']))
        for i, a in enumerate(eh):
            for b in eh[i + 1:]:
                if a['n_axis_is_u'] == b['n_axis_is_u'] and abs(a['edge_coord'] - b['edge_coord']) < 1 and abs(a['along'] - b['along']) < 20:
                    issues.append((p['code'], 'dwa otwory krawędziowe blisko', a['along'], b['along']))
        for e in eh:
            if e.get('do_obudowy'):
                continue   # zamierzone: otwór pod trzpień mimośrodu wchodzi do obudowy Ø15 w licu
            for f in fh:
                if e['n_axis_is_u']:
                    if abs(f['v'] - e['along']) < 8:
                        lo = e['edge_coord']; hi = e['edge_coord'] + e['into'] * e['depth']
                        if min(lo, hi) - 4 <= f['u'] <= max(lo, hi) + 4:
                            issues.append((p['code'], 'otwór licowy przecina otwór krawędziowy', f['u'], f['v'], e['edge_coord'], e['along']))
                else:
                    if abs(f['u'] - e['along']) < 8:
                        lo = e['edge_coord']; hi = e['edge_coord'] + e['into'] * e['depth']
                        if min(lo, hi) - 4 <= f['v'] <= max(lo, hi) + 4:
                            issues.append((p['code'], 'otwór licowy przecina otwór krawędziowy', f['u'], f['v'], e['edge_coord'], e['along']))
    return issues
