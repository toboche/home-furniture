"""Reguły kuchni dla wspólnego pipeline'u (wspolne/pipeline/run.py kuchnia).
Moduły: SO szafka okapowa (bez dna, okap DUO 55 między bokami), WS wąska szafka otwarta ze skrzynką na rurę,
P1 i P3 półka z LED z płyty 36 mm (bez nawiertów, mocowana na prętach w ścianie, otwory wierci użytkownik)."""
from formatki import F

# warstwy modelu, w których leżą formatki korpusu (fronty są brane z warstwy 'Fronty')
WARSTWY_FORMATEK = ['Ścianki boczne', 'Ścianki tylne', 'Półki', 'Półka LED']

# korpusy i fronty 18 mm; półka z LED 36 mm -> wyniki/formatki_36mm.csv
GRUBOSCI = (18, 36)


def modul_of(it):
    """moduł = dwa pierwsze znaki kodu (SO, WS, P1, P3); konfirmaty tylko w obrębie modułu"""
    return it['n'][:2]


def pomijaj_czesc(p):
    """półka z LED: bez nawiertów w zamówieniu (pręty i rowek na kabel robi użytkownik)"""
    return p['code'] in ('P1', 'P3')


# lewy bok szafki okapowej SOB-1 jest widoczny (nad półką P3): bez konfirmatów, złącza mimośrodowe + kołki (2026-11-14)
BOK_CZYSTY = 'SOB-1'
X_BOK_CZYSTY = 2398       # wewnętrzne lico SOB-1 (model.js: XSO + P)


def pomijaj_polaczenie(face, edge):
    return face == BOK_CZYSTY or edge == BOK_CZYSTY


def rozstaw(face, edge, domyslny):
    return domyslny


def punkty(face, edge, zakres, pts):
    return pts


# środki otworów wycinanych samodzielnie: Ø5 x 5 od strony wycinania (sklep), otwór wycina użytkownik
PILOT_D = 5
PILOT_DEPTH = 5
X_OKAP = 2656        # oś płyty i okapu (model.js: XH)
Y_RURA = 2577        # oś rury okapu (YRU)
Z_RURA = 97          # oś rury okapu od ściany głównej (ZRU)


def dodatkowe_otwory(P, parts, loc):
    """otwory ok. Ø140 pod rurę Ø125 (z kolanami i obejmami) w bokach SOB-2, WSB-1, WSB-2 i w półce SOP:
    sklep wierci tylko środek, otwór wycina użytkownik otwornicą"""
    def pilot(code, side, pos):
        p = P[code]
        p['holes'].append(dict(kind='FACE', side=side, u=loc(p, p['u'], pos[p['u']]), v=loc(p, p['v'], pos[p['v']]),
                               d=PILOT_D, depth=PILOT_DEPTH, partner='środek otworu Ø140 pod rurę okapu',
                               axis_n='-', pin=False, pilot=True))
    for code in ('SOB-2', 'WSB-1', 'WSB-2'):
        if code in P:
            pilot(code, 'A', {'y': Y_RURA, 'z': Z_RURA})
    pilot('SOP', 'A', {'x': X_OKAP, 'z': Z_RURA})

    # --- SOB-1: złącza mimośrodowe (np. Häfele Minifix 15) + kołki Ø8 x 30 ---
    # obudowa Ø15 x 13 w licu łączonej płyty, 24 od styku; trzpień: Ø5 x 11 w wewnętrznym licu SOB-1;
    # otwór Ø8 x 33 w czole łączonej płyty do obudowy; kołki: Ø8 x 12 w SOB-1, Ø8 x 20 w czole
    MF_ODL = 24
    bok = P[BOK_CZYSTY]

    def face(q, side, pos, d, depth, partner, opis):
        q['holes'].append(dict(kind='FACE', side=side, u=loc(q, q['u'], pos[q['u']]), v=loc(q, q['v'], pos[q['v']]),
                               d=d, depth=depth, partner=partner, axis_n='-', pin=True, opis=opis))

    def edge(q, along_ax, along_val, d, depth, partner, opis=None, do_obudowy=False):
        eu = (q['u'] == 'x')
        ec = loc(q, 'x', X_BOK_CZYSTY)
        L = q['DL'] if eu else q['SZ']
        h = dict(kind='EDGE', n_axis_is_u=eu, edge_coord=ec, along=loc(q, along_ax, along_val), depth=depth, d=d,
                 partner=partner, into=(-1 if ec >= L - 0.01 else 1))
        if opis:
            h['opis'] = opis
        if do_obudowy:
            h['do_obudowy'] = True
        q['holes'].append(h)

    def zlacze(code, side, mid_ax, mid, along_ax, mf, kolki):
        q = P[code]
        for a in mf:
            face(q, side, {'x': X_BOK_CZYSTY + MF_ODL, along_ax: a}, 15, 13, BOK_CZYSTY, 'Otwór Ø15 x 13 pod obudowę mimośrodu')
            edge(q, along_ax, a, 8, MF_ODL + 9, BOK_CZYSTY, 'Otwór Ø8 x 33 pod trzpień mimośrodu', True)
            face(bok, 'A', {mid_ax: mid, along_ax: a}, 5, 11, code, 'Otwór Ø5 x 11 pod trzpień mimośrodu (do %s)' % code)
        for a in kolki:
            edge(q, along_ax, a, 8, 20, BOK_CZYSTY)
            face(bok, 'A', {mid_ax: mid, along_ax: a}, 8, 12, code, 'Otwór Ø8 x 12 pod kołek (do %s)' % code)

    zlacze('SOT', 'A', 'z', 9, 'y', (1580, 2095, 2610), (1830, 2350))      # tył: obudowy od wnętrza (+z)
    zlacze('SOW', 'B', 'y', 2669, 'z', (159,), (60, 260))                   # wieniec: obudowy od spodu
    zlacze('SOP', 'A', 'y', 2159, 'z', (159,), (60, 260))                   # półka: obudowy od góry


ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE = set()


def zawias_specjalny(code, fr, cx, cy, cyl):
    pass


# tyły i zaślepka skrzynki: bez oklejonej krawędzi; półka LED: okleina opisana w FORMATKI
BEZ_OKLEINY_PREFIKSY = ('SOT', 'WST', 'WSZ', 'P1', 'P3')

# łby konfirmatów zasłonięte przez bryły z tych warstw nie potrzebują zaślepek
ZASLEPKI_ZASLANIAJA = ['Ścianka', 'Fronty', 'Kuchnia istniejąca', 'Okap']

PDF_LICA = {'x': ('PRAWA (od strony ścianki)', 'LEWA (od strony narożnika)'), 'y': ('GÓRNA', 'DOLNA'),
            'z': ('PRZEDNIA (od strony kuchni)', 'TYLNA (do ściany głównej)')}

ZAW = 'PUSZKA Ø35, ŚRODEK 22,5 MM OD KRAWĘDZI'

# Opisy formatek. Wymiary i ilości są liczone z modelu (model.js).
FORMATKI = [
    F('SOB', 'Szafka okapowa: boki (bez dna, okap między bokami)', okleina='1DL',
      nawierty='SOB-1: TRZPIENIE MIMOŚRODÓW + KOŁKI (bez otworów przelotowych); SOB-2: KONFIRMATY',
      uwagi='SOB-1 widoczny, czyste lico zewnętrzne; SOB-2: środek otworu Ø140 pod rurę; okap przykręcany 4 wkrętami 3,5 x 16 (81 nad dołem, 35 i 215 od przodu)'),
    F('SOT', 'Szafka okapowa: tył', okleina='', nawierty='KONFIRMATY + MIMOŚRODY I KOŁKI (do SOB-1)'),
    F('SOW', 'Szafka okapowa: wieniec górny', okleina='1DL', nawierty='KONFIRMATY + MIMOŚRÓD I KOŁKI (do SOB-1)'),
    F('SOP', 'Szafka okapowa: półka nad okapem', okleina='1DL', nawierty='KONFIRMATY + MIMOŚRÓD I KOŁKI (do SOB-1)',
      uwagi='środek otworu Ø140 pod rurę (oś 97 od ściany)'),
    F('WSB', 'Wąska szafka: boki', okleina='1DL', nawierty='KONFIRMATY',
      uwagi='środki otworów Ø140 pod rurę w obu bokach'),
    F('WST', 'Wąska szafka: tył', okleina='', nawierty='KONFIRMATY'),
    F('WSD', 'Wąska szafka: dno', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSW', 'Wąska szafka: wieniec górny', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSS', 'Wąska szafka: dno skrzynki na rurę (płytka półka przed zaślepką)', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSZ', 'Wąska szafka: zaślepka skrzynki na rurę', okleina='', nawierty='KONFIRMATY',
      uwagi='widoczne lico przednie; krawędzie schowane'),
    F('WSP', 'Wąska szafka: półki stałe', okleina='1DL', nawierty='KONFIRMATY'),
    F('P1', 'Półka LED: ściana lewa (wnęka)', okleina='1DL',
      nawierty='BRAK (pręty w tylnej krawędzi i rowek na kabel wierci użytkownik)',
      uwagi='okleina na długiej krawędzi od strony kuchni (803); płyta 36'),
    F('P3', 'Półka LED: ściana główna', okleina='1DL',
      nawierty='BRAK (pręty w tylnej krawędzi wierci użytkownik)',
      uwagi='okleina na przedniej krawędzi (1980); płyta 36'),
    F('F1', 'Front szafki okapowej, otwierany na docisk', okleina='2DL+2SZ',
      nawierty='ZAWIASY 3 SZT (PRAWA), ' + ZAW, uwagi='zawiasy bez cichego domyku + popychacz (push-to-open)'),
]
