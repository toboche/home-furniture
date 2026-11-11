"""Reguły pomieszczenia dla wspólnego pipeline'u (wspolne/pipeline/run.py NAZWA).
Szablon: minimalny zestaw. Wzór bardziej rozbudowanych reguł: pralnia/reguly.py."""
from formatki import F

# warstwy modelu, w których leżą formatki korpusu (fronty są brane z warstwy 'Fronty')
WARSTWY_FORMATEK = ['Ścianki boczne', 'Ścianki tylne', 'Półki']


def modul_of(it):
    """moduł (pudło) formatki; konfirmaty łączą tylko formatki z tego samego modułu"""
    return it['n'][:2]   # S1, S2… z kodu


def pomijaj_czesc(p):
    """formatki bez nawiertów (np. zdejmowane tyły)"""
    return False


def pomijaj_polaczenie(face, edge):
    """styki, w których nie ma konfirmatów (np. półki na podpórkach)"""
    return False


def rozstaw(face, edge, domyslny):
    return domyslny


def punkty(face, edge, zakres, pts):
    return pts


def dodatkowe_otwory(P, parts, loc):
    """podpórki półek, kołki, nawierty środków; wzór: pralnia/reguly.py"""


ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE = set()


def zawias_specjalny(code, fr, cx, cy, cyl):
    pass


# tyły: bez oklejonej krawędzi
BEZ_OKLEINY_PREFIKSY = ('S1T',)

# łby konfirmatów zasłonięte przez bryły z tych warstw nie potrzebują zaślepek
ZASLEPKI_ZASLANIAJA = ['Fronty']

# Opisy formatek. Wymiary i ilości są liczone z modelu; jawnie (dl, sz, szt) tylko pozycje spoza modelu.
FORMATKI = [
    F('S1B', 'S1: boki', okleina='1DL', nawierty='KONFIRMATY'),
    F('S1T', 'S1: tył', okleina='', nawierty='KONFIRMATY'),
    F('S1D', 'S1: dno', okleina='1DL', nawierty='KONFIRMATY'),
    F('S1P', 'S1: półka stała', okleina='1DL', nawierty='KONFIRMATY'),
    F('S1W', 'S1: wieniec górny', okleina='1DL', nawierty='KONFIRMATY'),
    F('F1', 'Front S1', okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22,5 MM OD KRAWĘDZI'),
]
