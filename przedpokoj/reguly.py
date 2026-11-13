"""Reguły przedpokoju dla wspólnego pipeline'u (wspolne/pipeline/run.py przedpokoj).
Moduły (korpusy osobno, łatwiejszy montaż): SZ szezlong, NS szafka nad szezlongiem, PW pawlacz,
SD szafa wysoka dół, SG szafa wysoka góra. Fronty bez uchwytów (TIP-ON), zaślepka F6 klejona do pionu."""
from formatki import F

# warstwy modelu, w których leżą formatki korpusu (fronty są brane z warstwy 'Fronty')
WARSTWY_FORMATEK = ['Ścianki boczne', 'Ścianki tylne', 'Półki']


def modul_of(it):
    """moduł (korpus) formatki = dwie pierwsze litery kodu; konfirmaty tylko w obrębie modułu"""
    return it['n'][:2]


def pomijaj_czesc(p):
    return False


def pomijaj_polaczenie(face, edge):
    return False


def rozstaw(face, edge, domyslny):
    return domyslny


def punkty(face, edge, zakres, pts):
    return pts


def dodatkowe_otwory(P, parts, loc):
    """kołki Ø8 x 20 w czołach den SZD i SDD na styku x 540 (wspólna wnęka bez boków pośrodku);
    otwory w zaślepce F6 wierci użytkownik (okleina bezspoinowa, kalkulator nie zaznaczy środka)"""
    X_STYK = 1540
    for code, partner in (('SZD', 'SDD'), ('SDD', 'SZD')):
        p = P[code]
        eu = (p['u'] == 'x')
        ec = loc(p, 'x', X_STYK)
        L = p['DL'] if eu else p['SZ']
        into = -1 if ec >= L - 0.01 else 1
        for z in (150, 630):
            p['holes'].append(dict(kind='EDGE', n_axis_is_u=eu, edge_coord=ec, along=loc(p, 'z', z),
                                   depth=20, d=8, partner=partner, into=into))


ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE = set()


def zawias_specjalny(code, fr, cx, cy, cyl):
    pass


# tyły: bez oklejonej krawędzi
BEZ_OKLEINY_PREFIKSY = ('SZT', 'PWT', 'SDT', 'SGT')

# łby konfirmatów zasłonięte przez bryły z tych warstw nie potrzebują zaślepek
ZASLEPKI_ZASLANIAJA = ['Pion', 'Fronty', 'Tapicerka']

PDF_LICA = {'x': ('PRAWA (od strony pionu)', 'LEWA (od strony D2)'), 'y': ('GÓRNA', 'DOLNA'),
            'z': ('PRZEDNIA (od strony przedpokoju)', 'TYLNA (do ściany)')}

ZAW = 'PUSZKA Ø35, ŚRODEK 22,5 MM OD KRAWĘDZI'

# Opisy formatek. Wymiary i ilości są liczone z modelu (model.js).
FORMATKI = [
    F('SZBL', 'Szezlong: bok lewy (od D2, stoi na podłodze, wnęka 0-177)', okleina='1SZ', nawierty='KONFIRMATY',
      uwagi='okleina na krawędzi przedniej (pionowej)'),
    F('SZBP', 'Szezlong: bok prawy (stoi na dnie SZD)', okleina='1SZ', nawierty='KONFIRMATY',
      uwagi='skręcony z SDBL 3 śrubami łącznikowymi'),
    F('SZW', 'Szezlong: blat pod poduszką (na bokach)', okleina='1SZ+1DL', nawierty='KONFIRMATY'),
    F('SZD', 'Szezlong: dno szuflady nad wnęką (do styku z SDD na x 540)', okleina='1SZ',
      nawierty='KONFIRMATY + KOŁKI Ø8 W CZOLE (do SDD)', uwagi='od spodu 2 płaskowniki na styku z SDD, pod stykiem 2 nóżki'),
    F('SZT', 'Szezlong: tył', okleina='', nawierty='KONFIRMATY'),
    F('NSB', 'Szafka nad szezlongiem: boki (głębokość 80)', okleina='1DL', nawierty='KONFIRMATY',
      uwagi='prowadniki zawiasów F2 w lewym boku; bez tyłu (rozdzielnica)'),
    F('NSD', 'Szafka nad szezlongiem: dno', okleina='1DL', nawierty='KONFIRMATY'),
    F('NSW', 'Szafka nad szezlongiem: wieniec', okleina='1DL', nawierty='KONFIRMATY'),
    F('PWB', 'Pawlacz: boki', okleina='1DL+1SZ', nawierty='KONFIRMATY',
      uwagi='okleina: krawędź przednia i dolna (widoczna od spodu)'),
    F('PWD', 'Pawlacz: dno', okleina='1SZ', nawierty='KONFIRMATY'),
    F('PWW', 'Pawlacz: wieniec górny', okleina='1SZ', nawierty='KONFIRMATY'),
    F('PWT', 'Pawlacz: tył', okleina='', nawierty='KONFIRMATY'),
    F('SDBL', 'Szafa dół: bok lewy (stoi na dnie SDD)', okleina='1DL', nawierty='KONFIRMATY'),
    F('SDBP', 'Szafa dół: bok prawy przy pionie (stoi na podłodze, wnęka 0-177)', okleina='1DL', nawierty='KONFIRMATY',
      uwagi='prowadniki zawiasów F4'),
    F('SDD', 'Szafa dół: dno nad wnęką (od styku z SZD na x 540)', okleina='1SZ',
      nawierty='KONFIRMATY + KOŁKI Ø8 W CZOLE (do SZD)'),
    F('SDW', 'Szafa dół: wieniec górny', okleina='1SZ', nawierty='KONFIRMATY'),
    F('SDT', 'Szafa dół: tył', okleina='', nawierty='KONFIRMATY'),
    F('SDP', 'Szafa dół: półki stałe (495 i 813)', okleina='1SZ', nawierty='KONFIRMATY'),
    F('SGB', 'Szafa góra: boki', okleina='1SZ', nawierty='KONFIRMATY'),
    F('SGD', 'Szafa góra: dno', okleina='1SZ', nawierty='KONFIRMATY'),
    F('SGW', 'Szafa góra: wieniec górny', okleina='1SZ', nawierty='KONFIRMATY'),
    F('SGT', 'Szafa góra: tył', okleina='', nawierty='KONFIRMATY'),
    F('F1', 'Front szuflady szezlonga (zasłania krawędź blatu)', okleina='2DL+2SZ', nawierty='BRAK (mocowanie frontu MOVENTO na wkręty)'),
    F('F2', 'Drzwi nad szezlongiem, zawiasy po LEWEJ (od D2)', okleina='2DL+2SZ', nawierty='ZAWIASY 4 SZT, ' + ZAW,
      uwagi='TIP-ON, zawiasy bez sprężyny'),
    F('F3', 'Front pawlacza, zawiasy po LEWEJ (od D2)', okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, ' + ZAW,
      uwagi='TIP-ON, zawiasy bez sprężyny'),
    F('F4', 'Front szafy, dół, zawiasy po PRAWEJ (od pionu)', okleina='2DL+2SZ', nawierty='ZAWIASY 4 SZT, ' + ZAW,
      uwagi='TIP-ON (2 szt.), zawiasy bez sprężyny'),
    F('F5', 'Front szafy, góra, zawiasy po PRAWEJ (od pionu)', okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, ' + ZAW,
      uwagi='TIP-ON, zawiasy bez sprężyny'),
    F('F6', 'Zaślepka na czole pionu (klejona, od podłogi do sufitu)', okleina='2DL+2SZ', nawierty='BRAK; otwory wierci użytkownik',
      uwagi='góra 1 mm pod sufitem w linii frontów; dwa otwory Ø60: kabel domofonu (środek 243,5 od lewej krawędzi, 1474 od dołu) i dystans włącznika (środek 296,5 od lewej, 1214 od dołu)'),
]
