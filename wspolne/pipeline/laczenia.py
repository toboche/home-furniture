"""Wykrywanie styków płyt w obrębie jednego modułu (połączenia konfirmatowe lico–czoło)."""
EPS = 0.01
MIN_STYK = 5   # mm: minimalne nakładanie się w obu kierunkach płaszczyzny styku


def _boxes(p):
    if 'sub' in p:
        return [dict(lo={'x': q['x'], 'y': q['y'], 'z': q['z']}, hi={'x': q['x'] + q['w'], 'y': q['y'] + q['h'], 'z': q['z'] + q['d']}) for q in p['sub']]
    return [dict(lo=p['lo'], hi=p['hi'])]


def wykryj(parts, log=print):
    contacts = []
    for i, A in enumerate(parts):
        for B in parts[i + 1:]:
            if A['mod'] != B['mod']:
                continue
            for ba in _boxes(A):
                for bb in _boxes(B):
                    for n in 'xyz':
                        # płaszczyzna styku prostopadła do n
                        for (s1, s2) in ((ba, bb), (bb, ba)):
                            if abs(s1['hi'][n] - s2['lo'][n]) < EPS:
                                ov = {}
                                ok = True
                                for a in 'xyz':
                                    if a == n:
                                        continue
                                    lo = max(ba['lo'][a], bb['lo'][a]); hi = min(ba['hi'][a], bb['hi'][a])
                                    if hi - lo < MIN_STYK:
                                        ok = False; break
                                    ov[a] = (lo, hi)
                                if ok:
                                    contacts.append((A, B, n, (s1['hi'][n]), ov))
    log('styków:', len(contacts))
    J = []
    for A, B, n, pos, ov in contacts:
        # część "licowa" ma oś cienką = n
        fa = [X for X in (A, B) if X['t'] == n]
        if len(fa) != 1:
            continue  # płyta na płycie lub krawędź do krawędzi
        face = fa[0]; edge = B if face is A else A
        J.append(dict(face=face, edge=edge, n=n, pos=pos, ov=ov))
    log('połączeń konfirmatowych:', len(J))
    return J
