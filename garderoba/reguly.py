"""Reguły garderoby dla wspólnego pipeline'u (wspolne/pipeline/run.py garderoba).
Moduły: N szafka na wprost (jeden korpus z przegrodą NP), L szafka po lewej (przód w stronę +x),
S1/S2 skrzynki szuflad (płyta 16). Fronty chowane, TIP-ON, bez uchwytów."""
import os
from formatki import F
import model as M

# warstwy modelu, w których leżą formatki korpusu (fronty są brane z warstwy 'Fronty')
WARSTWY_FORMATEK = ['Ścianki boczne', 'Ścianki tylne', 'Półki', 'Skrzynki szuflad']

# korpusy i fronty 18 mm; skrzynki szuflad 16 mm (MOVENTO: bok najwyżej 16) -> wyniki/formatki_16mm.csv
GRUBOSCI = (18, 16)


def modul_of(it):
    """moduł formatki: N, L albo skrzynka S1/S2; konfirmaty tylko w obrębie modułu"""
    n = it['n']
    return n[:2] if n.startswith('S') else n[0]


def os_przodu(p):
    """szafka po lewej (L) i jej szuflada (S2) patrzą przodem w stronę +x"""
    return 'x' if p['mod'] in ('L', 'S2') else 'z'


def pomijaj_czesc(p):
    return False


def pomijaj_polaczenie(face, edge):
    return False


def rozstaw(face, edge, domyslny):
    return domyslny


PRAWA_POLOWA = ('NS-4', 'NS-5', 'NW-2', 'NO-2')


def punkty(face, edge, zakres, pts):
    """przegroda NP: płyty po obu stronach są na tych samych wysokościach, więc konfirmaty z prawej strony
    przesuwamy o 25, żeby otwory w NP się nie pokrywały"""
    if face == 'NP' and edge in PRAWA_POLOWA:
        return [min(p + 25, zakres[1] - 25) for p in pts]
    return pts


# zawiasy frontów chowanych: prowadniki nie leżą w linii 37 od przodu boku (jak przy frontach nakładanych),
# więc nawierty pilotowe dodaje dodatkowe_otwory
ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE = {'F1', 'F2'}
PROWADNIK_OD_PRZODU = 37 + 18 + 1.5   # front chowany 18 (70T3750.TL, prowadnik krzyżakowy 0 mm): katalog Blum: cofnięcie o grubość frontu + 1,5 = 56,5


def _pilot(P, loc, code, side, pos, d, depth, partner, plate=False):
    p = P[code]
    P[code]['holes'].append(dict(kind='FACE', side=side, u=loc(p, p['u'], pos[p['u']]), v=loc(p, p['v'], pos[p['v']]),
                                 d=d, depth=depth, partner=partner, axis_n='-', pin=False, pilot=True, plate=plate))


def dodatkowe_otwory(P, parts, loc):
    """nawierty środków Ø5 × 5 pod otwory wiercone otwornicą przez użytkownika (przewód wentylacyjny w LB1,
    gniazdko w LB2) i nawierty pilotowe Ø3 × 12 pod prowadniki zawiasów frontów chowanych F1, F2"""
    dane = M.wczytaj(os.path.dirname(os.path.abspath(__file__)))
    items = dane['items']
    wylot = [i for i in items if i.get('t') == 'cyl' and i['n'].startswith('Przewód wentylacyjny')][0]
    gn = [i for i in items if i['n'].startswith('Gniazdko')][0]
    # LB1: lico wewnętrzne = +z (A); LB2: lico wewnętrzne = −z (B)
    _pilot(P, loc, 'LB1', 'A', {'x': wylot['cx'], 'y': wylot['cy']}, 5, 5, 'środek otworu na przewód wentylacyjny (wycina użytkownik)')
    _pilot(P, loc, 'LB2', 'B', {'x': gn['x'] + gn['w'] / 2, 'y': gn['y'] + gn['h'] / 2}, 5, 5, 'środek otworu na gniazdko (wycina użytkownik)')
    fronty = {i['n'].split(':')[0]: i for i in items if i.get('layer') == 'Fronty' and not i.get('t')}
    for z in [i for i in items if i.get('layer') == 'Zawiasy']:
        cx, cy = z['x'] + 17.5, z['y'] + 17.5
        fr = [f for k, f in fronty.items() if k in ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE and f['x'] <= cx <= f['x'] + f['w'] and f['y'] <= cy <= f['y'] + f['h']][0]
        lewa = cx < fr['x'] + fr['w'] / 2
        code, side = ('NB-1', 'A') if lewa else ('NB-2', 'B')
        zp = fr['z'] + fr['d'] - PROWADNIK_OD_PRZODU
        for dy in (-16, 16):
            _pilot(P, loc, code, side, {'y': cy + dy, 'z': zp}, 3, 12, 'wkręt prowadnika zawiasu ' + fr['n'].split(':')[0], plate=True)


def zawias_specjalny(code, fr, cx, cy, cyl):
    pass


# bez oklejonej krawędzi: plecy, osłony przewodów, skrzynki szuflad
BEZ_OKLEINY_PREFIKSY = ('NT', 'NO', 'LT', 'S1', 'S2')

# łby konfirmatów zasłonięte przez bryły z tych warstw nie potrzebują zaślepek
ZASLEPKI_ZASLANIAJA = ['Pion i gzyms', 'Fronty']

K = 'KONFIRMATY'
SKR = 'płyta 16; otwory pod zaczepy MOVENTO T51.7601 wg wzornika Blum T65.1000.02'
SKR_D = SKR + '; w TYLNEJ KRAWĘDZI DNA 2 otwory Ø6 × 10 pod haki prowadnic: 7 nad spodem dna, 11 od wewnętrznego lica boków'

# Opisy formatek. Wymiary i ilości liczone z modelu (model.js).
FORMATKI = [
    # szafka na wprost N
    F('NB', 'N: boki (lewy przy pionie, prawy przy prawej ścianie)', okleina='1DL',
      nawierty=K + ' + NAWIERTY PILOTOWE Ø3 × 12 POD PROWADNIKI ZAWIASÓW (F1 w NB-1, F2 w NB-2)'),
    F('NP', 'N: przegroda środkowa (od podłogi do wieńca górnego)', okleina='1DL', nawierty=K),
    F('NT', 'N: plecy (od 335 do wieńca górnego, nad osłonami przewodów)', okleina='', nawierty=K),
    F('NG', 'N: wieniec górny', okleina='1DL', nawierty=K),
    F('NW', 'N: wieniec na 2120 (półka części górnej), 2 połowy', okleina='1SZ', nawierty=K),
    F('NS', 'N: półki nad butami (335, 596,5, 858 w połowie lewej; 335, 596,5 w prawej)', okleina='1SZ', nawierty=K),
    F('NK', 'N: płyta pod kurtkami, połowa lewa (1084)', okleina='1SZ', nawierty=K),
    F('NO', 'N: osłony przewodów wodnych (od podłogi do 335, 55 od ściany)', okleina='', nawierty=K),
    # szafka po lewej L
    F('LB1', 'L: bok przy pionie', okleina='1DL', nawierty=K + ' + NAWIERT ŚRODKA Ø5 × 5',
      uwagi='WYCIĘCIE NAROŻNIKA 184 × 335 (dolny narożnik przy ścianie lewej, wokół gzymsu i rury): w kalkulatorze jako wycięcie '
            'albo wykonuje użytkownik; otwór na przewód wentylacyjny Ø130 (np. Ø135) wierci użytkownik otwornicą wg nawiertu środka'),
    F('LB2', 'L: bok przy ścianie przedniej', okleina='1DL', nawierty=K + ' + NAWIERT ŚRODKA Ø5 × 5',
      uwagi='WYCIĘCIE NAROŻNIKA 129 × 335 (dolny narożnik przy ścianie lewej, wokół gzymsu): w kalkulatorze jako wycięcie '
            'albo wykonuje użytkownik; otwór na gniazdko wierci użytkownik otwornicą wg nawiertu środka'),
    F('LT', 'L: plecy (od 335 do wieńca górnego, nad gzymsem)', okleina='', nawierty=K),
    F('LG', 'L: wieniec górny', okleina='1DL', nawierty=K),
    F('LW', 'L: wieniec na 2120 (półka części górnej)', okleina='1DL', nawierty=K),
    F('LS', 'L: półki nad butami (335, 596,5, 858)', okleina='1DL', nawierty=K),
    F('LK', 'L: płyta pod kurtkami (1084)', okleina='1DL', nawierty=K),
    # fronty
    F('F1', 'Front górny N, połowa lewa (chowany, TIP-ON, zawiasy po lewej)', okleina='2DL+2SZ',
      nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI (zawias do frontu chowanego)'),
    F('F2', 'Front górny N, połowa prawa (chowany, TIP-ON, zawiasy po prawej)', okleina='2DL+2SZ',
      nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI (zawias do frontu chowanego)'),
    F('F3', 'Front szuflady SZ1 (N, połowa lewa; chowany, TIP-ON BLUMOTION)', okleina='2DL+2SZ',
      nawierty='BRAK (mocowanie frontu MOVENTO na wkręty)'),
    F('F4', 'Front szuflady SZ2 (L; chowany, TIP-ON BLUMOTION)', okleina='2DL+2SZ',
      nawierty='BRAK (mocowanie frontu MOVENTO na wkręty)'),
    # skrzynki szuflad (płyta 16)
    F('S1B', 'Szuflada SZ1: boki skrzynki (MOVENTO 500, wysokość 180)', okleina='', nawierty=K, uwagi=SKR),
    F('S1D', 'Szuflada SZ1: dno skrzynki (13 nad dolną krawędzią boków, do końca boków)', okleina='', nawierty=K, uwagi=SKR_D),
    F('S1C', 'Szuflada SZ1: czoło i tył skrzynki (stoją na dnie)', okleina='', nawierty=K, uwagi=SKR),
    F('S2B', 'Szuflada SZ2: boki skrzynki (MOVENTO 600, wysokość 180)', okleina='', nawierty=K, uwagi=SKR),
    F('S2D', 'Szuflada SZ2: dno skrzynki (13 nad dolną krawędzią boków, do końca boków)', okleina='', nawierty=K, uwagi=SKR_D),
    F('S2C', 'Szuflada SZ2: czoło i tył skrzynki (stoją na dnie)', okleina='', nawierty=K, uwagi=SKR),
]
