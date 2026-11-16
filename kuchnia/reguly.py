"""Reguły kuchni dla wspólnego pipeline'u (wspolne/pipeline/run.py kuchnia).
Moduły: SO szafka okapowa (bez dna, okap DUO 55 między bokami), WS wąska szafka otwarta ze skrzynką na rurę,
P1 i P3 półka z LED z płyty 18 mm (bez nawiertów, na wspornikach ukrytych Ø10, otwory wierci użytkownik)."""
from formatki import F

# warstwy modelu, w których leżą formatki korpusu (fronty są brane z warstwy 'Fronty')
WARSTWY_FORMATEK = ['Ścianki boczne', 'Ścianki tylne', 'Półki', 'Półka LED']

# wszystko z płyty 18 mm (półka z LED: 36 → 18, 2026-11-15)
GRUBOSCI = (18,)


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
    return face == BOK_CZYSTY or edge == BOK_CZYSTY or 'SOD' in (face, edge)


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
Z_PION = 109.5       # oś pionu i poziomu Ø150 w SO (ZPI)
Y_SOD = 1786         # dół półki wkładanej SOD (model.js: YSOD)
Y_SOP = 2104         # dół półki SOP (model.js: YSOP)


def dodatkowe_otwory(P, parts, loc):
    """otwory pod rurę (pierścień gumowy): Ø160 pod Ø150 w SOB-2 i WSB-1 (góra otworu 3 pod wieńcem), Ø170 w półce SOP, Ø140 pod Ø125 w WSB-2
    (redukcja w wąskiej szafce, 2026-11-16): sklep wierci tylko środek, otwór wycina użytkownik otwornicą.
    Podpórki Ø5 × 10 pod wkładaną półkę SOD w SOB-1 i SOB-2."""
    def pilot(code, side, pos):
        p = P[code]
        p['holes'].append(dict(kind='FACE', side=side, u=loc(p, p['u'], pos[p['u']]), v=loc(p, p['v'], pos[p['v']]),
                               d=PILOT_D, depth=PILOT_DEPTH, partner='środek otworu pod rurę okapu (Ø160 w SOB-2, WSB-1; Ø170 w SOP; Ø140 w WSB-2)',
                               axis_n='-', pin=False, pilot=True))
    for code, z in (('SOB-2', Z_PION), ('WSB-1', Z_PION), ('WSB-2', Z_RURA)):
        if code in P:
            pilot(code, 'A', {'y': Y_RURA, 'z': z})
    for code, side in (('SOB-1', 'A'), ('SOB-2', 'B')):      # lico od wnętrza SO
        q = P[code]
        for z in (50, 250):
            q['holes'].append(dict(kind='FACE', side=side, u=loc(q, q['u'], {'y': Y_SOD - 5, 'z': z}[q['u']]),
                                   v=loc(q, q['v'], {'y': Y_SOD - 5, 'z': z}[q['v']]), d=5, depth=10,
                                   partner='SOD', axis_n='-', pin=True))
    pilot('SOP', 'A', {'x': X_OKAP, 'z': Z_PION})

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

    zlacze('SOT', 'A', 'z', 9, 'y', (1580, 2040, 2610), (1830, 2350))      # tył: obudowy od wnętrza (+z)
    zlacze('SOW', 'B', 'y', 2669, 'z', (159,), (60, 260))                   # wieniec: obudowy od spodu
    zlacze('SOP', 'A', 'y', Y_SOP + 9, 'z', (159,), (60, 260))                   # półka: obudowy od góry


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
      nawierty='SOB-1: TRZPIENIE MIMOŚRODÓW + KOŁKI (bez otworów przelotowych); SOB-2: KONFIRMATY; OBA: 2 PODPÓRKI Ø5 x 10 POD SOD',
      uwagi='SOB-1 widoczny, czyste lico zewnętrzne; SOB-2: środek otworu Ø160 pod rurę Ø150; okap przykręcany 4 wkrętami 3,5 x 16 (81 nad dołem, 35 i 215 od przodu)'),
    F('SOT', 'Szafka okapowa: tył', okleina='', nawierty='KONFIRMATY + MIMOŚRODY I KOŁKI (do SOB-1)'),
    F('SOW', 'Szafka okapowa: wieniec górny', okleina='1DL', nawierty='KONFIRMATY + MIMOŚRÓD I KOŁKI (do SOB-1)'),
    F('SOD', 'Szafka okapowa: półka wkładana tuż nad okapem (na 4 podpórkach Ø5)', okleina='1DL', nawierty='BRAK',
      uwagi='wkładana po montażu okapu; wycięcie od przodu na wylot Ø150 (szer. ok. 170, do ok. 112 od tyłu, oś x na środku) wycina użytkownik'),
    F('SOP', 'Szafka okapowa: półka nad okapem', okleina='1DL', nawierty='KONFIRMATY + MIMOŚRÓD I KOŁKI (do SOB-1)',
      uwagi='środek otworu Ø170 pod pion Ø150 (oś 109,5 od ściany)'),
    F('WSB', 'Wąska szafka: boki', okleina='1DL', nawierty='KONFIRMATY',
      uwagi='środki otworów pod rurę: WSB-1 Ø160 (pod Ø150), WSB-2 Ø140 (pod Ø125)'),
    F('WST', 'Wąska szafka: tył', okleina='', nawierty='KONFIRMATY'),
    F('WSD', 'Wąska szafka: dno', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSW', 'Wąska szafka: wieniec górny', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSS', 'Wąska szafka: dno skrzynki na rurę (płytka półka przed zaślepką)', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSZ', 'Wąska szafka: zaślepka skrzynki na rurę', okleina='', nawierty='KONFIRMATY',
      uwagi='widoczne lico przednie; krawędzie schowane'),
    F('WSP', 'Wąska szafka: półki stałe', okleina='1DL', nawierty='KONFIRMATY'),
    F('P1', 'Półka LED: ściana lewa (wnęka)', okleina='1DL',
      nawierty='BRAK (otwory Ø10 pod wsporniki ukryte w krawędziach przy ścianach wierci użytkownik)',
      uwagi='okleina na długiej krawędzi od strony kuchni (804). rowki 18,2 × 6 pod profil LED w spodzie frezuje użytkownik (meble.pl nie robi wręgów zachodzących na siebie)'),
    F('P3', 'Półka LED: ściana główna', okleina='1DL',
      nawierty='BRAK (otwory Ø10 pod wsporniki ukryte w tylnej krawędzi wierci użytkownik)',
      uwagi='okleina na przedniej krawędzi (1980). rowek 18,2 × 6 pod profil LED w spodzie frezuje użytkownik (meble.pl nie robi wręgów zachodzących na siebie)'),
    F('F1', 'Front szafki okapowej, otwierany na docisk', okleina='2DL+2SZ',
      nawierty='ZAWIASY 3 SZT (PRAWA), ' + ZAW, uwagi='zawiasy bez cichego domyku + popychacz (push-to-open)'),
]
