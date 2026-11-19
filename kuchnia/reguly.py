"""Reguły kuchni dla wspólnego pipeline'u (wspolne/pipeline/run.py kuchnia).
Moduły: SO szafka okapowa (bez dna, okap DUO 55 między bokami), WS wąska szafka otwarta ze skrzynką na rurę,
P1 i P3 półka z LED z płyty 18 mm na prętach M8 w betonie (otwory Ø8 x 35 w czołach przy ścianach, pogłębia użytkownik)."""
from formatki import F

# warstwy modelu, w których leżą formatki korpusu (fronty są brane z warstwy 'Fronty')
WARSTWY_FORMATEK = ['Ścianki boczne', 'Ścianki tylne', 'Półki', 'Półka LED']

# wszystko z płyty 18 mm (półka z LED: 36 → 18, 2026-11-15)
GRUBOSCI = (18,)


def modul_of(it):
    """moduł = dwa pierwsze znaki kodu (SO, WS, P1, P3); konfirmaty tylko w obrębie modułu"""
    return it['n'][:2]


def pomijaj_czesc(p):
    """wszystkie formatki z nawiertami; P1 i P3 tylko otwory w czołach pod pręty M8, 2026-11-16"""
    return False


# lewy bok szafki okapowej SOB-1 jest widoczny (nad półką P3): bez konfirmatów, złącza mimośrodowe + kołki (2026-11-14)
BOK_CZYSTY = 'SOB-1'
X_BOK_CZYSTY = 2398       # wewnętrzne lico SOB-1 (model.js: XSO + P)


def pomijaj_polaczenie(face, edge):
    """SOB-1: mimośrody; SOD: na podpórkach; WSZ: zaślepka skrzynki zdejmowana od przodu (dostęp do redukcji), audyt v1 KU-07"""
    return face == BOK_CZYSTY or edge == BOK_CZYSTY or 'SOD' in (face, edge) or 'WSZ' in (face, edge)


def rozstaw(face, edge, domyslny):
    return domyslny


def punkty(face, edge, zakres, pts):
    """audyt v1: SOP-SOT bez konfirmatu w osi otworu Ø170 (KU-03); wieńce SOW/WSW do SOB-2/WSB-1 skręcane
    przed otworem Ø160 pod rurę (z 30-190), żeby konfirmat nie stał nad otworem (KU-14)"""
    if {face, edge} == {'SOT', 'SOP'}:
        return [p for p in pts if abs(p - X_OKAP) > 95]
    if (face, edge) in (('SOB-2', 'SOW'), ('WSB-1', 'WSW'), ('WSB-2', 'WSW')):
        return [215, 265]
    if (face, edge) == ('WSB-2', 'WST'):     # wycięcie w WSB-2 od tyłu na rurę ze ścianki (Y 2507-2647)
        return [p for p in pts if not 2490 <= p <= 2665]
    return pts


def os_przodu(p):
    """P1 leży przy ścianie lewej: przód (oklejona krawędź 804) od strony +x (audyt v1 KU-05)"""
    return 'x' if p['code'] == 'P1' else 'z'


# środki otworów wycinanych samodzielnie: Ø5 x 5 od strony wycinania (sklep), otwór wycina użytkownik
PILOT_D = 5
PILOT_DEPTH = 5
X_OKAP = 2656        # oś płyty i okapu (model.js: XH)
Y_RURA = 2577        # oś rury okapu (YRU)
Z_RURA = 97          # oś rury okapu od ściany głównej (ZRU)
Z_PION = 109.5       # oś pionu i poziomu Ø150 w SO (ZPI)
Y_SOD = 1786         # dół półki wkładanej SOD (model.js: YSOD)
Y_SOP = 2104         # dół półki SOP (model.js: YSOP)
Z_SOP_OTW = 124      # środek otworu w SOP: pochylona rura (z 138 przy wylocie → 109,5 przy kolanie) na wysokości SOP
Y_OKW = 1592         # otwory montażowe okapu: 81 nad dołem korpusu (YP)
Z_OKW = (250, 70)    # 35 i 215 od lica przodu korpusu okapu (z 285)
X_ZA = 2852          # przewód okapu: A - ZA1
Y_ZA = 2193          # przewód okapu: YS - ZA2


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
    pilot('SOP', 'A', {'x': X_OKAP, 'z': Z_SOP_OTW})
    # otwory montażowe okapu: nawierty pilotowe Ø3 x 5 od wnętrza SO, po 2 w każdym boku (2026-11-18)
    for code, side in (('SOB-1', 'A'), ('SOB-2', 'B')):
        q = P[code]
        for z in Z_OKW:
            pos = {'y': Y_OKW, 'z': z}
            q['holes'].append(dict(kind='FACE', side=side, u=loc(q, q['u'], pos[q['u']]), v=loc(q, q['v'], pos[q['v']]),
                                   d=3, depth=5, partner='wkręt okapu 3,5 x 16', axis_n='-', pin=False, pilot=True,
                                   opis='Nawiert pilotowy Ø3 x 5 pod wkręt okapu'))
    # zaślepka WSZ zdejmowana: 2 kołki Ø8 wklejone w dolne czoło WSZ, wchodzą w otwory Ø8 x 12 w WSS (KU-07, 2026-11-18)
    wsz, wss = P['WSZ'], P['WSS']
    for x in (3000, 3138):
        eu = (wsz['u'] == 'y')
        ec = loc(wsz, 'y', 2492)
        L = wsz['DL'] if eu else wsz['SZ']
        wsz['holes'].append(dict(kind='EDGE', n_axis_is_u=eu, edge_coord=ec, along=loc(wsz, 'x', x),
                                 depth=16, d=8, partner='WSS', into=(-1 if ec >= L - 0.01 else 1)))
        wss['holes'].append(dict(kind='FACE', side='A', u=loc(wss, wss['u'], {'x': x, 'z': 204}[wss['u']]),
                                 v=loc(wss, wss['v'], {'x': x, 'z': 204}[wss['v']]), d=8, depth=12, partner='WSZ',
                                 axis_n='-', pin=True, opis='Otwór Ø8 x 12 pod kołek zaślepki WSZ'))
    # przewód zasilający okap wychodzi ze ściany głównej za plecami SOT (ZA1, ZA2): środek otworu Ø25 (audyt v1 KU-10)
    q = P['SOT']
    q['holes'].append(dict(kind='FACE', side='A', u=loc(q, q['u'], {'x': X_ZA, 'y': Y_ZA}[q['u']]),
                           v=loc(q, q['v'], {'x': X_ZA, 'y': Y_ZA}[q['v']]), d=PILOT_D, depth=PILOT_DEPTH,
                           partner='środek otworu Ø25 pod przewód zasilający okap', axis_n='-', pin=False, pilot=True))

    # --- SOB-1: złącza mimośrodowe (np. Häfele Minifix 15) + kołki Ø8 x 30 ---
    # obudowa Ø15 x 14 (Häfele: 13,5 ± 0,5) w licu łączonej płyty, 24 od styku; trzpień B 24, gwint Euro Ø5 x 11 w wewnętrznym licu SOB-1;
    # otwór Ø8 x 33 w czole łączonej płyty do obudowy; kołki 8 x 30: Ø8 x 10 w widocznym SOB-1, Ø8 x 22 w czole
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
            face(q, side, {'x': X_BOK_CZYSTY + MF_ODL, along_ax: a}, 15, 14, BOK_CZYSTY, 'Otwór Ø15 x 14 pod obudowę mimośrodu')
            edge(q, along_ax, a, 8, MF_ODL + 9, BOK_CZYSTY, 'Otwór Ø8 x 33 pod trzpień mimośrodu', True)
            face(bok, 'A', {mid_ax: mid, along_ax: a}, 5, 11, code, 'Otwór Ø5 x 11 pod trzpień mimośrodu (do %s)' % code)
        for a in kolki:
            edge(q, along_ax, a, 8, 22, BOK_CZYSTY)
            face(bok, 'A', {mid_ax: mid, along_ax: a}, 8, 10, code, 'Otwór Ø8 x 10 pod kołek (do %s)' % code)

    # --- półka LED: otwory Ø8 x 35 w czołach przy ścianach pod pręty M8 (pogłębia użytkownik do 85) ---
    def czolo(code, n_ax, n_val, al_ax, vals, depth, opis=None):
        q = P[code]
        eu = (q['u'] == n_ax)
        ec = loc(q, n_ax, n_val)
        L = q['DL'] if eu else q['SZ']
        for a in vals:
            h = dict(kind='EDGE', n_axis_is_u=eu, edge_coord=ec, along=loc(q, al_ax, a), depth=depth, d=8,
                     partner=('ściana: pręt M8' if opis else 'P1/P3: kołek'), into=(-1 if ec >= L - 0.01 else 1))
            if opis:
                h['opis'] = opis
            q['holes'].append(h)
    PRET = 'Otwór Ø8 x 35 pod pręt M8 (pogłębia użytkownik do 85)'
    czolo('P3', 'z', 0, 'x', [400 + v for v in (150, 570, 990, 1410, 1830)], 35, PRET)
    czolo('P1', 'x', 0, 'z', (150, 400, 650), 35, PRET)

    zlacze('SOT', 'A', 'z', 9, 'y', (1580, 2040, 2610), (1830, 2350))      # tył: obudowy od wnętrza (+z)
    zlacze('SOW', 'B', 'y', 2669, 'z', (159,), (60, 260))                   # wieniec: obudowy od spodu
    zlacze('SOP', 'A', 'y', Y_SOP + 9, 'z', (159,), (60, 260))                   # półka: obudowy od góry


ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE = set()


def zawias_specjalny(code, fr, cx, cy, cyl):
    pass


# tyły i zaślepka skrzynki: bez oklejonej krawędzi
BEZ_OKLEINY_PREFIKSY = ('SOT', 'WST', 'WSZ')

# łby konfirmatów zasłonięte przez bryły z tych warstw nie potrzebują zaślepek
ZASLEPKI_ZASLANIAJA = ['Ścianka', 'Fronty', 'Kuchnia istniejąca', 'Okap']

PDF_LICA = {'x': ('PRAWA (od strony ścianki)', 'LEWA (od strony narożnika)'), 'y': ('GÓRNA', 'DOLNA'),
            'z': ('PRZEDNIA (od strony kuchni)', 'TYLNA (do ściany głównej)')}

ZAW = 'PUSZKA Ø35, ŚRODEK 22,5 MM OD KRAWĘDZI'

# Opisy formatek. Wymiary i ilości są liczone z modelu (model.js).
FORMATKI = [
    F('SOB', 'Szafka okapowa: boki (bez dna, okap między bokami)', okleina='1DL',
      nawierty='SOB-1: TRZPIENIE MIMOŚRODÓW + KOŁKI (bez otworów przelotowych); SOB-2: KONFIRMATY; OBA: 2 PODPÓRKI Ø5 x 10 POD SOD',
      uwagi='SOB-1 widoczny, czyste lico zewnętrzne; SOB-2: środek otworu Ø160 pod rurę Ø150; okap przykręcany 4 wkrętami 3,5 x 16: nawierty pilotowe Ø3 x 5 od wnętrza na Y 1592 (81 nad dołem), z 250 i 70 (35 i 215 od lica przodu korpusu okapu)'),
    F('SOT', 'Szafka okapowa: tył', okleina='', nawierty='KONFIRMATY + MIMOŚRODY I KOŁKI (do SOB-1)',
      uwagi='środek otworu Ø25 pod przewód zasilający okap (x 2852, y 2193) wycina użytkownik'),
    F('SOW', 'Szafka okapowa: wieniec górny', okleina='1DL', nawierty='KONFIRMATY + MIMOŚRÓD I KOŁKI (do SOB-1)'),
    F('SOD', 'Szafka okapowa: półka wkładana tuż nad okapem (na 4 podpórkach Ø5)', okleina='1DL', nawierty='BRAK',
      uwagi='wkładana po montażu okapu; wycięcie od przodu na wylot Ø150: szer. 170 (oś x na środku), zakończone półkolem R85 o środku 120 od tylnej krawędzi (najgłębiej 35 od tylnej krawędzi); wycina użytkownik, krawędzie silikonem; w tylnym prawym narożniku podcięcie ok. 25 × 25 na przewód okapu'),
    F('SOP', 'Szafka okapowa: półka nad okapem', okleina='1DL', nawierty='KONFIRMATY + MIMOŚRÓD I KOŁKI (do SOB-1)',
      uwagi='środek otworu Ø170 pod rurę Ø150 (z 124 = 106 od tylnej krawędzi; rura lekko pochylona); otwór otwarty do tyłu (wycięcie U szer. 170 od tylnej krawędzi), przewód okapu przechodzi tym wycięciem; wycina użytkownik'),
    F('WSB', 'Wąska szafka: boki', okleina='1DL', nawierty='KONFIRMATY',
      uwagi='WSB-1: środek otworu Ø160 pod Ø150; WSB-2: rura ze ścianki wystaje 115, więc wycięcie U od tylnej krawędzi szer. 140 z półkolem R70 o środku w zaznaczonym punkcie (z 97), żeby szafkę dało się nasunąć na rurę; wycina użytkownik'),
    F('WST', 'Wąska szafka: tył', okleina='', nawierty='KONFIRMATY'),
    F('WSD', 'Wąska szafka: dno', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSW', 'Wąska szafka: wieniec górny', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSS', 'Wąska szafka: dno skrzynki na rurę (płytka półka przed zaślepką)', okleina='1DL', nawierty='KONFIRMATY'),
    F('WSZ', 'Wąska szafka: zaślepka skrzynki na rurę (zdejmowana)', okleina='', nawierty='BRAK',
      uwagi='widoczne lico przednie; krawędzie schowane; bez konfirmatów, zdejmowana: 2 kołki Ø8 na dole (wklejone w WSZ), 2 zatrzaski magnetyczne u góry (pod WSW)'),
    F('WSP', 'Wąska szafka: półki stałe', okleina='1DL', nawierty='KONFIRMATY'),
    F('P1', 'Półka LED: ściana lewa (wnęka)', okleina='1DL',
      nawierty='CZOŁA: 3 x Ø8 x 35 pod pręty M8 od ściany lewej (użytkownik pogłębia do 85)',
      uwagi='okleina na długiej krawędzi od strony kuchni (804); koniec przy słupku przykręcany przez bok słupka (wkręty do 4 x 40, nawierty ręczne). Rowki 18,2 × 6 pod profil LED w spodzie frezuje użytkownik (meble.pl nie robi wręgów zachodzących na siebie)'),
    F('P3', 'Półka LED: ściana główna', okleina='1DL',
      nawierty='CZOŁA: 5 x Ø8 x 35 pod pręty M8 w tylnej krawędzi (użytkownik pogłębia do 85)',
      uwagi='okleina na przedniej krawędzi (1980). Rowek 18,2 × 6 pod profil LED w spodzie frezuje użytkownik (meble.pl nie robi wręgów zachodzących na siebie)'),
    F('F1', 'Front szafki okapowej, otwierany na docisk', okleina='2DL+2SZ',
      nawierty='ZAWIASY 3 SZT (PRAWA), ' + ZAW, uwagi='3 zawiasy Blum CLIP top 110° bez sprężyny 70T3550.TL + prowadniki 173L6100, puszki 337,5, 697,5 i 1064 od dołu frontu (wszystkie nad okapem i SOD); 1 x TIP-ON 956.1004 (krótki, z magnesem) na adapterze 956.1201 na SOB-1 ok. Y 1850 (drugi w razie potrzeby); szczelina pod TIP-ON ok. 2'),
]
