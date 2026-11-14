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


def pomijaj_polaczenie(face, edge):
    return False


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
    F('SOB', 'Szafka okapowa: boki (bez dna, okap między bokami)', okleina='1DL', nawierty='KONFIRMATY',
      uwagi='SOB-2: środek otworu Ø140 pod rurę; okap przykręcany 4 wkrętami 3,5 x 16 (81 nad dołem, 35 i 215 od przodu)'),
    F('SOT', 'Szafka okapowa: tył', okleina='', nawierty='KONFIRMATY'),
    F('SOW', 'Szafka okapowa: wieniec górny', okleina='1DL', nawierty='KONFIRMATY'),
    F('SOP', 'Szafka okapowa: półka nad okapem', okleina='1DL', nawierty='KONFIRMATY',
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
