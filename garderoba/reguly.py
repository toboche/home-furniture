"""Reguły garderoby dla wspólnego pipeline'u (wspolne/pipeline/run.py garderoba).
Moduły: N / L korpusy dolne (0–2120) szafki na wprost i po lewej (L przodem w stronę +x), GN / GL korpusy górne
(2120–2582), S1/S2 skrzynki szuflad (płyta 16). Fronty chowane, TIP-ON, bez uchwytów.
Wszystkie wymiary i położenia otworów w pełnych mm (kalkulator meble.pl)."""
import math
import os
from formatki import F
import model as M

# warstwy modelu, w których leżą formatki korpusu (fronty są brane z warstwy 'Fronty')
WARSTWY_FORMATEK = ['Ścianki boczne', 'Ścianki tylne', 'Półki', 'Skrzynki szuflad']

# korpusy i fronty 18 mm; skrzynki szuflad 16 mm (MOVENTO: bok najwyżej 16) -> wyniki/formatki_16mm.csv
GRUBOSCI = (18, 16)


def modul_of(it):
    """moduł formatki: N, L (dolne), GN, GL (górne) albo skrzynka S1/S2; konfirmaty tylko w obrębie modułu
    (korpus górny łączy się z dolnym wkrętami przez dno, nie konfirmatami)"""
    n = it['n']
    return n[:2] if n[0] in 'SG' else n[0]


def os_przodu(p):
    """szafka po lewej (L) i jej szuflada (S2) patrzą przodem w stronę +x"""
    return 'x' if p['mod'] in ('L', 'GL', 'S2') else 'z'


def pomijaj_czesc(p):
    return False


def pomijaj_polaczenie(face, edge):
    """bez konfirmatów:
    - osłony przewodów NO-1, NO-2 są zdejmowane (kątowniki u góry, magnesy na dole);
    - korpus dolny L składany na miejscu (boki LB1, LB2 i plecy LT bez dostępu z zewnątrz): łączniki narożne od środka
      (decyzja 2026-11-19, audyt v2 GD-01);
    - korpus górny GL też składany na miejscu (podnoszenie złożonego GL między frontem N a ścianą przednią ma 2–6 mm luzu,
      audyt v3 GD3-06, decyzja 2026-11-19); korpusy N i GN zostają na konfirmatach"""
    if face.startswith('NO') or edge.startswith('NO'):
        return True
    return (face[0] == 'L' and edge[0] == 'L') or (face[:2] == 'GL' and edge[:2] == 'GL')


def rozstaw(face, edge, domyslny):
    return domyslny


PRAWA_POLOWA = ('NS-4', 'NS-5')

# skrzynki szuflad: konfirmaty dna z dala od zaczepów T51.7601 (przód, przy bokach) i od strefy TIP-ON BLUMOTION
# (tył, 125 od boków); przód skrzynki leży zawsze na końcu 'hi' zakresu
SKR_BOK_DNO_OD_PRZODU = 100    # bok -> dno: przedni konfirmat 100 od przodu skrzynki (był 50)
SKR_DNO_CZOLO_OD_BOKU = 100    # dno -> czoło: 100 od boków (było 50)
SKR_DNO_TYL_OD_BOKU = 135      # dno -> tył: 135 od boków (było 50)


def _zaokr(v):
    return math.floor(v + 0.5)


def _od_brzegow(lo, hi, m):
    """punkty m od obu końców, a przy długim styku dodatkowo środek"""
    pts = [lo + m, hi - m]
    if hi - lo - 2 * m > 400:
        pts.insert(1, (lo + hi) / 2)
    return pts


def punkty(face, edge, zakres, pts):
    """przegroda NP: płyty po obu stronach są na tych samych wysokościach, więc konfirmaty z prawej strony
    przesuwamy o 25, żeby otwory w NP się nie pokrywały; skrzynki szuflad wg stref okuć Blum;
    na końcu wszystko zaokrąglone do pełnych mm"""
    lo, hi = zakres
    if face == 'NP' and edge in PRAWA_POLOWA:
        pts = [min(p + 25, hi - 25) for p in pts]
    elif face[:2] in ('S1', 'S2'):
        if face[2] == 'B' and edge[2] == 'D':
            pts = [pts[0], hi - SKR_BOK_DNO_OD_PRZODU]
        elif face[2] == 'D' and edge.endswith('C-1'):
            pts = _od_brzegow(lo, hi, SKR_DNO_CZOLO_OD_BOKU)
        elif face[2] == 'D' and edge.endswith('C-2'):
            pts = _od_brzegow(lo, hi, SKR_DNO_TYL_OD_BOKU)
    return [_zaokr(p) for p in pts]


# zawiasy frontów chowanych: prowadniki nie leżą w linii 37 od przodu boku (jak przy frontach nakładanych),
# więc nawierty pilotowe dodaje dodatkowe_otwory
ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE = {'F1', 'F2'}
PROWADNIK_OD_PRZODU = 57   # front chowany 18 (70T3790.TL, prowadnik krzyżakowy 0 mm): katalog Blum 37 + 18 + 1,5 = 56,5, zaokrąglone
                           # do pełnego mm w głąb (front 0,5 głębiej, korekta regulacją głębokości zawiasu)


def _pilot(P, loc, code, side, pos, d, depth, partner, plate=False):
    p = P[code]
    P[code]['holes'].append(dict(kind='FACE', side=side, u=loc(p, p['u'], pos[p['u']]), v=loc(p, p['v'], pos[p['v']]),
                                 d=d, depth=depth, partner=partner, axis_n='-', pin=False, pilot=True, plate=plate))


def dodatkowe_otwory(P, parts, loc):
    """nawierty środków Ø5 × 5 pod otwory wiercone otwornicą przez użytkownika (przewód wentylacyjny w GLB1,
    gniazdko w LB2) i nawierty pilotowe Ø3 × 12 pod prowadniki zawiasów frontów chowanych F1, F2"""
    dane = M.wczytaj(os.path.dirname(os.path.abspath(__file__)))
    items = dane['items']
    wylot = [i for i in items if i.get('t') == 'cyl' and i['n'].startswith('Przewód wentylacyjny')][0]
    gn = [i for i in items if i['n'].startswith('Gniazdko')][0]
    # GLB1 (bok górny): lico wewnętrzne = +z (A); LB2: lico wewnętrzne = −z (B)
    _pilot(P, loc, 'GLB1', 'A', {'x': wylot['cx'], 'y': wylot['cy']}, 5, 5, 'środek otworu na przewód wentylacyjny (wycina użytkownik)')
    _pilot(P, loc, 'LB2', 'B', {'x': gn['x'] + gn['w'] / 2, 'y': gn['y'] + gn['h'] / 2}, 5, 5, 'środek otworu na gniazdko (wycina użytkownik)')
    fronty = {i['n'].split(':')[0]: i for i in items if i.get('layer') == 'Fronty' and not i.get('t')}
    for z in [i for i in items if i.get('layer') == 'Zawiasy']:
        cx, cy = z['x'] + 17.5, z['y'] + 17.5
        fr = [f for k, f in fronty.items() if k in ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE and f['x'] <= cx <= f['x'] + f['w'] and f['y'] <= cy <= f['y'] + f['h']][0]
        lewa = cx < fr['x'] + fr['w'] / 2
        code, side = ('GNB-1', 'A') if lewa else ('GNB-2', 'B')
        zp = fr['z'] + fr['d'] - PROWADNIK_OD_PRZODU
        for dy in (-16, 16):
            _pilot(P, loc, code, side, {'y': cy + dy, 'z': zp}, 3, 12, 'wkręt prowadnika zawiasu ' + fr['n'].split(':')[0], plate=True)


def zawias_specjalny(code, fr, cx, cy, cyl):
    pass


# bez oklejonej krawędzi: plecy, osłony przewodów, skrzynki szuflad
BEZ_OKLEINY_PREFIKSY = ('NT', 'NO', 'LT', 'GNT', 'GLT', 'S1', 'S2')

# łby konfirmatów zasłonięte przez bryły z tych warstw nie potrzebują zaślepek
ZASLEPKI_ZASLANIAJA = ['Pion i gzyms', 'Fronty']

K = 'KONFIRMATY'
SKR = 'płyta 16; KONFIRMATY 5 × 40: otwory Ø5 w licu POGŁĘBIĆ STOŻKOWO pod łeb (łeb równo z płytą, pod dnem prześwit MOVENTO); otwory pod zaczepy MOVENTO T51.7601 wg wzornika Blum T65.1000.02'
SKR_D = SKR + '; w TYLNEJ KRAWĘDZI DNA 2 otwory Ø6 × 10 pod haki prowadnic: 7 nad spodem dna, 11 od wewnętrznego lica boków; konfirmaty dna z dala od zaczepów (100 od przodu i boków) i od strefy TIP-ON z tyłu (135 od boków)'

# Opisy formatek. Wymiary i ilości liczone z modelu (model.js).
DOL = 'DOLNA KRAWĘDŹ OKLEJONA ABS (stoi na kafelkach; w kalkulatorze dodać ręcznie), ślizgacze w razie potrzeby'
SCIANA = 'korpus górny przykręcony do dolnego wkrętami przez dno (patrz ustalenia.md)'

FORMATKI = [
    # szafka na wprost: korpus dolny N
    F('NB', 'N dół: boki (lewy przy pionie, prawy przy prawej ścianie)', okleina='1DL + 1SZ (dół)', nawierty=K, uwagi=DOL),
    F('NP', 'N dół: przegroda środkowa (od podłogi do wieńca NW)', okleina='1DL + 1SZ (dół)', nawierty=K, uwagi=DOL),
    F('NT', 'N dół: plecy (od 335 do wieńca NW, nad osłonami przewodów)', okleina='', nawierty=K),
    F('NW', 'N dół: wieniec na 2120 (sufit części otwartej, cała szerokość)', okleina='1DL', nawierty=K),
    F('NS', 'N dół: półki nad butami (335, 596, 858 w połowie lewej; 335, 596 w prawej)', okleina='1SZ', nawierty=K),
    F('NK', 'N dół: płyta pod kurtkami, połowa lewa (1084)', okleina='1SZ', nawierty=K),
    F('NO', 'N dół: osłony przewodów wodnych, zdejmowane (od podłogi do 335, 55 od ściany)', okleina='1DL (dół)', nawierty='BRAK',
      uwagi='bez konfirmatów: u góry 2 kątowniki pod półką, na dole 2 zatrzaski magnetyczne (blaszki na tylnym licu); ' + DOL),
    # szafka na wprost: korpus górny GN
    F('GNB', 'N góra: boki (zawiasy F1 w GNB-1, F2 w GNB-2)', okleina='1SZ', nawierty=K + ' + NAWIERTY PILOTOWE Ø3 × 12 POD PROWADNIKI ZAWIASÓW'),
    F('GND', 'N góra: dno', okleina='1DL', nawierty=K, uwagi=SCIANA),
    F('GNG', 'N góra: wieniec górny', okleina='1DL', nawierty=K),
    F('GNP', 'N góra: przegroda środkowa (TIP-ON F1 i F2 z obu stron)', okleina='1SZ', nawierty=K),
    F('GNT', 'N góra: plecy', okleina='', nawierty=K),
    # szafka po lewej: korpus dolny L
    F('LB1', 'L dół: bok przy pionie', okleina='1DL + 1SZ (dół)', nawierty='BRAK (łączniki od środka)',
      uwagi='WYCIĘCIE NAROŻNIKA 184 × 335 (dolny narożnik przy ścianie lewej, wokół gzymsu i rury): w kalkulatorze jako wycięcie '
            'albo wykonuje użytkownik; ' + DOL),
    F('LB2', 'L dół: bok przy ścianie przedniej', okleina='1DL + 1SZ (dół)', nawierty='NAWIERT ŚRODKA Ø5 × 5 (łączniki od środka)',
      uwagi='WYCIĘCIE NAROŻNIKA 129 × 335 (dolny narożnik przy ścianie lewej, wokół gzymsu): w kalkulatorze jako wycięcie '
            'albo wykonuje użytkownik; otwór ok. Ø60 pod gniazdo wpuszczane wierci użytkownik po przymiarce, nad puszką w ścianie (wg nawiertu środka); ' + DOL),
    F('LT', 'L dół: plecy (od 335 do wieńca LW, nad gzymsem)', okleina='', nawierty='BRAK (łączniki od środka)'),
    F('LW', 'L dół: wieniec na 2120 (sufit części otwartej)', okleina='1DL', nawierty='BRAK (łączniki od środka)'),
    F('LS', 'L dół: półki nad butami (335, 596, 858)', okleina='1DL', nawierty='BRAK (łączniki od środka)'),
    F('LK', 'L dół: płyta pod kurtkami (1084)', okleina='1DL', nawierty='BRAK (łączniki od środka)'),
    # szafka po lewej: korpus górny GL (otwarta półka)
    F('GLB1', 'L góra: bok przy pionie', okleina='1SZ', nawierty='NAWIERT ŚRODKA Ø5 × 5 (łączniki od środka)',
      uwagi='otwór na przewód wentylacyjny Ø130 (np. Ø135) wierci użytkownik otwornicą wg nawiertu środka'),
    F('GLB2', 'L góra: bok przy ścianie przedniej', okleina='1SZ', nawierty='BRAK (łączniki od środka)'),
    F('GLD', 'L góra: dno', okleina='1DL', nawierty='BRAK (łączniki od środka)', uwagi=SCIANA),
    F('GLG', 'L góra: wieniec górny', okleina='1DL', nawierty='BRAK (łączniki od środka)'),
    F('GLT', 'L góra: plecy', okleina='', nawierty='BRAK (łączniki od środka)'),
    # fronty
    F('F1', 'Front górny N, połowa lewa (chowany, TIP-ON, zawiasy po lewej)', okleina='2DL+2SZ',
      nawierty='SZABLON FRONT LEWY: 2 ZAWIASY BLUM INSERTA (70T3790.TL), PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI, 100 OD KOŃCÓW'),
    F('F2', 'Front górny N, połowa prawa (chowany, TIP-ON, zawiasy po prawej)', okleina='2DL+2SZ',
      nawierty='SZABLON FRONT PRAWY: 2 ZAWIASY BLUM INSERTA (70T3790.TL), PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI, 100 OD KOŃCÓW'),
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
