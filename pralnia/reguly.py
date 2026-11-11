"""Reguły pralni dla wspólnego pipeline'u (wspolne/pipeline/run.py pralnia).
Wszystko, co dotyczy tylko tego pomieszczenia: podział na moduły, wyjątki w konfirmatach,
podpórki i kołki, nawierty środków, zawias F5 na F6, opisy formatek."""
import re
from formatki import F

# warstwy modelu, w których leżą formatki korpusu (fronty są brane z warstwy 'Fronty')
WARSTWY_FORMATEK = ['Ścianki boczne', 'Ścianki tylne', 'Półki']


def modul_of(it):
    """moduł (pudło) formatki; konfirmaty łączą tylko formatki z jednego modułu"""
    cx = it['x'] + it['w'] / 2; cy = it['y'] + it['h'] / 2
    if cx < 620: return 'L1' if cy < 1743 else 'L2'
    if cx < 1215: return 'NW'
    return 'RD' if cy < 1743 - 0.01 else 'RB'


# zdejmowane tyły kolumny KT1A/B/C: bez nawiertów, na kątownikach i magnesach
def pomijaj_czesc(p):
    return p['code'].startswith('KT1')


PINNED = re.compile(r'^(KP|PP)2-[12]$')   # półki na wciskanych podpórkach: bez konfirmatów


def pomijaj_polaczenie(face, edge):
    if face.startswith('KT1') or edge.startswith('KT1'): return True
    if PINNED.match(face) or PINNED.match(edge): return True
    return False


def rozstaw(face, edge, domyslny):
    return 200 if 'KB1' in (face, edge) else domyslny   # KB1: gęstszy rozstaw (3 konfirmaty zamiast 2)


def punkty(face, edge, zakres, pts):
    # wieniec 100 mm: 2 konfirmaty na koniec
    if ({face, edge} & {'L1W', 'RDW'}) and 90 <= zakres[1] - zakres[0] <= 110:
        return [zakres[0] + 25, zakres[1] - 25]
    return pts


def dodatkowe_otwory(P, parts, loc):
    # --- podpórki półek (otwory Ø5 nieprzelotowe w KB2 i PB2) i kołki łączące KP z PP (Ø8 w czołach) ---
    PIN_D=5; PIN_DEPTH=10; PIN_PITCH=32; PIN_RANGE=2
    DOWEL_D=8; DOWEL_DEPTH=20
    LEVELS={'KP2-1':922,'KP2-2':1355,'PP2-1':922,'PP2-2':1355}
    for lvl in (922,1355):
        # KB2 (lico A = +x, od strony półki), kolumny przy z=233 i z=590
        for pc,side,zs in (('KB2','A',(213,355,417,590)),('PB2','B',(417,590))):
            p=P[pc]
            for z in zs:
                for k in range(-PIN_RANGE,PIN_RANGE+1):
                    y=lvl-3+k*PIN_PITCH
                    pu=p['u']; pv=p['v']
                    val={'y':y,'z':z}
                    p['holes'].append(dict(kind='FACE',side=side,u=loc(p,pu,val[pu]),v=loc(p,pv,val[pv]),d=PIN_D,depth=PIN_DEPTH,partner='podpórka',axis_n='x',pin=True))
    # kołki Ø8 w styku KP/PP wzdłuż osi Z (PP z przodu na całą szerokość, KP z tyłu kolumny), 2 szt. na x=1270 i x=1340
    for kp,pp,ze in (('KP1','PP1',367),('KP2-1','PP2-1',385),('KP2-2','PP2-2',385),('KP3-1','PP3-1',385),('KP3-2','PP3-2',385),('KP3-3','PP3-3',385)):
        for code in (kp,pp):
            p=P[code]
            assert 'z' in (p['u'],p['v'])
            eu=(p['u']=='z')
            ec=loc(p,'z',ze)
            L=p['DL'] if eu else p['SZ']
            into=-1 if ec>=L-0.01 else 1
            for x in (1270,1340):
                p['holes'].append(dict(kind='EDGE',n_axis_is_u=eu,edge_coord=ec,along=loc(p,'x',x),depth=DOWEL_DEPTH,d=DOWEL_D,partner=(pp if code==kp else kp),into=into))

    # kołki Ø8 x 20 w styku KB1/KB2 (współpłaszczyznowe boki kolumny, czoła na y=489), 2 szt. – dodatkowe połączenie KB1
    for code in ('KB1','KB2'):
        p=P[code]
        eu=(p['u']=='y'); assert 'y' in (p['u'],p['v'])
        ec=loc(p,'y',489)
        L=p['DL'] if eu else p['SZ']
        into=-1 if ec>=L-0.01 else 1
        for z in (480,600):
            p['holes'].append(dict(kind='EDGE',n_axis_is_u=eu,edge_coord=ec,along=loc(p,'z',z),depth=DOWEL_DEPTH,d=DOWEL_D,partner=('KB2' if code=='KB1' else 'KB1'),into=into))

    # --- nawierty pilotowe (środek) pod otwory wycinane samodzielnie: Ø5 nieprzelotowe, głębokość 5 mm, od strony wycinania ---
    PILOT_D=5; PILOT_DEPTH=5
    def pilot(code,side,y,other_axis,val):
        p=P[code]; pos={'y':y,other_axis:val}
        p['holes'].append(dict(kind='FACE',side=side,u=loc(p,p['u'],pos[p['u']]),v=loc(p,p['v'],pos[p['v']]),d=PILOT_D,depth=PILOT_DEPTH,partner='środek otworu wycinanego samodzielnie',axis_n='-',pin=False,pilot=True))
    pilot('PT3','A',2409,'x',1616)   # Ø130 pod kanał, od strony wnętrza (+z)
    pilot('L1B2','A',918,'z',242)    # wycięcie 100 x 100 pod gniazdko GN1 (y 868-968, z 192-292 od tyłu), od wnętrza (+x)


# zawiasy, które nie mają prowadnika w ściance szafki
ZAWIASY_BEZ_PROWADNIKA_W_SCIANCE = {'F5'}


def zawias_specjalny(code, fr, cx, cy, cyl):
    """F5: Blum 79B9590 do drzwi równoległych, prowadnik na tyle frontu F6 (linia wkrętów X 1521,5)"""
    if code == 'F5':
        for dy in (-16, 16):
            cyl('Otwór pod wkręt prowadnika zawiasu F5 w F6 (nawiert opcjonalny, tył F6)', 'Otwory', 'z', dict(x=1521.5, y=cy + dy, z=646), 2, 12, 0x15181b)


# tyły: bez oklejonej krawędzi
BEZ_OKLEINY_PREFIKSY = ('L1T', 'L2T', 'NWT', 'PT', 'KT')

# łby konfirmatów zasłonięte przez bryły z tych warstw nie potrzebują zaślepek
ZASLEPKI_ZASLANIAJA = ['Maszyny', 'Pion i gzyms', 'Fronty']

PDF_LICA = {'x': ('PRAWA (od strony maszyn/prawej ściany)', 'LEWA'), 'y': ('GÓRNA', 'DOLNA'), 'z': ('PRZEDNIA (od strony pokoju)', 'TYLNA (do ściany)')}
PDF_OPIS = ("Każda strona = jeden typ formatki. Wymiary w mm, liczone od lewej (U) i dołu (V) rysunku.\n"
    "Rysunek jest widokiem z lica A. Lico A, lico B i krawędź oklejona są opisane na każdej stronie.\n"
    "Czerwone kółka: otwory Ø5 przelotowo w licu A (w kalkulatorze: Przód); po dostawie poszerzyć do Ø7. Niebieskie: lico B (w kalkulatorze: Tył).\n"
    "Zielone paski: otwory w czole Ø4 x 35 mm (cienkie) lub Ø8 x 20 mm pod kołki (grube), w połowie grubości płyty (kalkulator: Wiercenie w czole). Czerwone/niebieskie przerywane: otwory Ø5 NIEPRZELOTOWE, głębokość 10 mm, pod wciskane podpórki półek.\n"
    "Pomarańczowa gruba krawędź: oklejona (przód mebla). Kody części zgodne z numeracją w wizualizacji 3D.\n"
    "W kalkulatorze: SZER = DL, WYS = SZ; X, Y od lewego dolnego rogu widoku z lica A; krawędzie 1 góra, 2 prawa, 3 dół, 4 lewa.\nZawiasy frontów (F1-F9): szablony Front lewy/prawy w kalkulatorze, w tym arkuszu ich nie ma. Tabela do wpisania: kalkulator_nawierty.csv.")

# Opisy formatek. Wymiary i ilości są liczone z modelu (model.js); jawnie tylko pozycje spoza modelu.
# OKLEINA: krawędzie oklejane (1DL = jedna długa, 2DL+2SZ = wszystkie). NAWIERTY: rodzaj nawiertów w zamówieniu.
FORMATKI = [
    F('L1B1', 'L1: bok prawy (przy maszynach)',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('L1B2', 'L1: bok lewy (całość; wycięcie pod GN1 100x100 robi użytkownik: od dołu 868-968, od tyłu 192-292)',
      okleina='1DL', nawierty='KONFIRMATY + NAWIERT ŚRODKA Ø5 x 5', uwagi='pod gniazdko GN1 wycina użytkownik'),
    F('L1T', 'L1: tył',
      okleina='', nawierty='KONFIRMATY'),
    F('L2B', 'L2: boki pasa',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('L2T', 'L2: tył pasa',
      okleina='', nawierty='KONFIRMATY'),
    F('L2P', 'L2: półki stałe (spód, środek, góra)',
      okleina='1SZ', nawierty='KONFIRMATY'),
    F('NWB', 'Wnęka nad maszynami: boki',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('NWT', 'Wnęka: tył',
      okleina='', nawierty='KONFIRMATY'),
    F('NWP', 'Wnęka: półki stałe (spód, środek, góra)',
      okleina='1SZ', nawierty='KONFIRMATY'),
    F('KB1', 'Kolumna: bok lewy, dół',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('KB2', 'Kolumna: bok lewy, środek i góra (+ szeregi otworów Ø5 x 10 pod podpórki półek KP2)',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('KB3', 'Kolumna: bok lewy, pas',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('PB1', 'Prawa: bok prawy, dół (przy gzymsie)',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('PB2', 'Prawa: bok prawy, góra (+ szeregi otworów Ø5 x 10 pod podpórki półek PP2)',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('PB3', 'Prawa: bok prawy, pas',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('PT1', 'Prawa dół: tył',
      okleina='', nawierty='KONFIRMATY'),
    F('KT1A', 'Kolumna: tył dolny (zawór ZW1/ZW2), zdejmowany bez narzędzi, y 509-916',
      okleina='', nawierty='KONFIRMATY', uwagi='2 kątowniki 25x25 za płytą na KB2 + 2 magnesy Ø10x3 (gniazda Ø10x3 wiercisz sam); szer. 127 zamiast 132 (luz na kątownik 2 mm i tolerancję)'),
    F('KT1B', 'Kolumna: tył środkowy (gniazdka GP1/GP2), zdejmowany, y 942-1349',
      okleina='', nawierty='KONFIRMATY', uwagi='2 kątowniki 25x25 za płytą na KB2 + 2 magnesy Ø10x3 (gniazda wiercisz sam)'),
    F('KT1C', 'Kolumna: tył górny, zdejmowany, y 1375-1725',
      okleina='', nawierty='KONFIRMATY', uwagi='2 kątowniki 25x25 za płytą na KB2 + 2 magnesy Ø10x3 (gniazda wiercisz sam)'),
    F('KT2', 'Kolumna: tył, pas',
      okleina='', nawierty='KONFIRMATY'),
    F('PT2', 'Prawa: tył, dół i środek',
      okleina='', nawierty='KONFIRMATY'),
    F('PT3', 'Prawa: tył, pas (otwór Ø130 pod kanał wierci użytkownik: środek 245 od lewej krawędzi, 243 od górnej)',
      okleina='', nawierty='KONFIRMATY + NAWIERT ŚRODKA Ø5 x 5'),
    F('KP1', 'Półka kolumny (tył), poziom 489: z 183 do 367; kołki Ø8 do PP1',
      okleina='', nawierty='KONFIRMATY + KOŁKI Ø8 W CZOLE (do PP1)'),
    F('KP2', 'Półka kolumny (tył), poziomy 922 i 1355: z 183 do 385 (na wciskanych podpórkach; kołki Ø8 do PP2, bez okleiny)',
      okleina='', nawierty='KOŁKI Ø8 W CZOLE (do PP2); BEZ KONFIRMATÓW'),
    F('KP3', 'Półka kolumny (tył), pas: 1743, 2188,5, 2634 (z 183 do 385; kołki Ø8 do PP3)',
      okleina='', nawierty='KONFIRMATY + KOŁKI Ø8 W CZOLE (do PP3)'),
    F('PP1', 'Półka przednia, poziom 489 (x 1239-1736, z 367-640; stoi na niej PT2/PB2)',
      okleina='1DL', nawierty='KONFIRMATY + KOŁKI Ø8 W CZOLE (do KP1)'),
    F('PP2', 'Półka przednia, poziomy 922 i 1355 (x 1239,75-1717,25, z 385-640; na wciskanych podpórkach; kołki Ø8 do KP2)',
      okleina='1DL', nawierty='KOŁKI Ø8 W CZOLE (do KP2); BEZ KONFIRMATÓW'),
    F('PP3', 'Półka przednia, pas: 1743, 2188,5, 2634 (x 1239-1718, z 385-640; kołki Ø8 do KP3)',
      okleina='1DL', nawierty='KONFIRMATY + KOŁKI Ø8 W CZOLE (do KP3)'),
    F('L1W', 'L1: wieniec górny, przód',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('L1P', 'L1: półka luzem na całą szerokość L1 (BEZ nawiertów, nie montowana w szafce; ewentualne nawierty robi użytkownik)',
      okleina='1SZ', nawierty='BEZ NAWIERTÓW', uwagi='dodatkowa płyta w zamówieniu; półka ma być na całej szerokości L1 (wewnętrzna szer. 574), głębokość jak L2P', dl=619, sz=574, szt=1),
    F('RDW', 'Prawa dolna: wieniec górny, przód',
      okleina='1DL', nawierty='KONFIRMATY'),
    F('F1', 'Front L: góra',
      okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI', uwagi='uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów'),
    F('F2', 'Front L: dół',
      okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI', uwagi='uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów'),
    F('F3', 'Front wnęka: góra',
      okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI', uwagi='uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów; zawiasy po PRAWEJ'),
    F('F4', 'Front wnęka: dół',
      okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI', uwagi='uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów; zawiasy po PRAWEJ'),
    F('F5', 'Front P pas: góra, otwierany',
      okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI', uwagi='zawiasy po PRAWEJ: Blum 79B9590 INSERTA (do drzwi równoległych); prowadnik na tylnej ściance F6, linia wkrętów 21,5 od jej lewej krawędzi, bez nawiertów; uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów'),
    F('F6', 'Front P pas: góra, stały z kratką Ø150',
      okleina='2DL+2SZ', nawierty='BRAK; otwór Ø150 własnoręcznie otwornicą', uwagi='otwór Ø150: ŚRODEK 116 MM OD LEWEJ KRAWĘDZI, 210 MM OD DOLNEJ (243 OD GÓRNEJ); nawiertu środka kalkulator nie zrobi (okleina bezspoinowa), zaznaczyć ręcznie'),
    F('F7', 'Front P pas: dół',
      okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI', uwagi='uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów'),
    F('F8', 'Front P dół: rząd 1 (przy gzymsie)',
      okleina='2DL+2SZ', nawierty='ZAWIASY 2 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI', uwagi='uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów'),
    F('F9', 'Front P dół: jeden wysoki (dawne F9+F10+F11)',
      okleina='2DL+2SZ', nawierty='ZAWIASY 3 SZT, PUSZKA Ø35, ŚRODEK 22.5 MM OD KRAWĘDZI', uwagi='uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów'),
]
