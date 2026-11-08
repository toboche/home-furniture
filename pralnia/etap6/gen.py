import csv
# Wymiary z modelu 3D (pralnia_3d.html), płyta 18 mm. DL = dłuższy wymiar, SZ = krótszy.
# OKL = krawędzie oklejane ABS 1 mm bezspoinowe. NAW = rodzaj nawiertów.
P=[]
def add(k,n,a,b,q,okl,naw,u=''):
    P.append([k,n,max(a,b),min(a,b),q,okl,naw,u])
K='KONFIRMATY'
# L1
add('L1B1','L1: bok prawy (przy maszynach)',1743,655,1,'1DL',K)
add('L1B2','L1: bok lewy (całość; wycięcie pod GN1 100x100 robi użytkownik: od dołu 868-968, od tyłu 192-292)',1743,655,1,'1DL',K,'pod gniazdko GN1 wycina użytkownik')
add('L1T','L1: tył',1743,574,1,'',K)
# L2
add('L2B','L2: boki pasa',909,637,2,'1DL',K)
add('L2T','L2: tył pasa',909,574,1,'',K)
add('L2P','L2: półki stałe (spód, środek, góra)',619,574,3,'1SZ',K)
# wnęka
add('NWB','Wnęka nad maszynami: boki',909,635,2,'1DL',K)
add('NWT','Wnęka: tył',909,570,1,'',K)
add('NWP','Wnęka: półki stałe (spód, środek, góra)',617,570,3,'1SZ',K)
# kolumna / prawa
add('KB1','Kolumna: bok lewy, dół',489,200,1,'1DL',K)
add('KB2','Kolumna: bok lewy, środek i góra (+ szeregi otworów Ø5 x 10 pod podpórki półek KP2)',1254,475,1,'1DL',K)
add('KB3','Kolumna: bok lewy, pas',909,475,1,'1DL',K)
add('PB1','Prawa: bok prawy, dół (przy gzymsie)',489,200,1,'1DL',K)
add('PB2','Prawa: bok prawy, góra (+ szeregi otworów Ø5 x 10 pod podpórki półek PP2)',1236,273,1,'1DL',K)
add('PB3','Prawa: bok prawy, pas',909,273,1,'1DL',K)
# plecy prawe
add('PT1','Prawa dół: tył',489,406,1,'',K)
add('KT1A','Kolumna: tył dolny (zawór ZW1/ZW2), zdejmowany bez narzędzi',390,132,1,'',K,'kątowniki 25x25 z pokrętłami')
add('KT1B','Kolumna: tył środkowy (gniazdka GP1/GP2), zdejmowany',390,132,1,'',K,'kątowniki 25x25 z wkrętami')
add('KT1C','Kolumna: tył górny, zdejmowany',408,132,1,'',K,'kątowniki 25x25 z wkrętami')
add('KT2','Kolumna: tył, pas',909,132,1,'',K)
add('PT2','Prawa: tył, dół i środek',1236,347,1,'',K)
add('PT3','Prawa: tył, pas (otwór Ø130 pod kanał wierci użytkownik: środek 245 od lewej krawędzi, 243 od górnej)',909,347,1,'',K)
# półki kolumny (KP) i prawe (PP): osobne prostokąty zamiast półek L
add('KP1','Półka kolumny, poziom 489',457,132,1,'1SZ',K)
add('KP2','Półka kolumny, poziomy 922 i 1355 (na wciskanych podpórkach; łączona kołkami Ø8 z PP2 w jedną półkę L)',457,132,2,'1SZ','KOŁKI Ø8 W CZOLE (do PP2); BEZ KONFIRMATÓW')
add('KP3','Półka kolumny, pas: 1743, 2188,5, 2634',457,132,3,'1SZ',K)
add('PP1','Półka prawa, poziom 489 (do 1736)',365,255,1,'1DL',K)
add('PP2','Półka prawa, poziomy 922 i 1355 (na wciskanych podpórkach; łączona kołkami Ø8 z KP2)',347,255,2,'1DL','KOŁKI Ø8 W CZOLE (do KP2); BEZ KONFIRMATÓW')
add('PP3','Półka prawa, pas: 1743, 2188,5, 2634',347,255,3,'1DL',K)
# wieńce górne (usztywnienie dolnych szafek)
add('L1W','L1: wieniec górny, przód',574,100,1,'1DL',K)
add('RDW','Prawa dolna: wieniec górny, przód',479,100,1,'1DL',K)
add('LF5','Listwa pod zawiasy F5 (płytki Blum 71B3790), za lewą krawędzią F6; do F6 dwoma kątownikami 25x25',427.5,60,1,'','BRAK','poza kalkulatorem szerokość 60 < 100: ostrzeżenie modalne')
# fronty
F=[('F1','Front L: góra',608.5,453),('F2','Front L: dół',608.5,453),
   ('F3','Front wnęka: góra',605,453),('F4','Front wnęka: dół',605,453),
   ('F5','Front P pas: góra, otwierany',274.5,453),('F6','Front P pas: góra, stały z kratką Ø150',236,453),
   ('F7','Front P pas: dół',513.5,453),
   ('F8','Front P dół: rząd 1 (przy gzymsie)',439,493.5),('F9','Front P dół: jeden wysoki (dawne F9+F10+F11)',513.5,1240.5)]
for k,n,w,h in F:
    naw=('ZAWIASY 3 SZT, PUSZKA Ø35' if k=='F9' else 'ZAWIASY 2 SZT, PUSZKA Ø35') if k!='F6' else 'BRAK; otwór Ø150 własnoręcznie otwornicą'
    add(k,n,w,h,1,'2DL+2SZ',naw,'' if k=='F6' else (('zawiasy po PRAWEJ, płytki na LF5; ' if k=='F5' else '')+'uchwyt GUBBARP 116 mm: otwory samodzielnie, bez nawiertów' + ('; zawiasy po PRAWEJ' if k in ('F3','F4') else '')))
w=csv.writer(open('formatki.csv','w',newline='',encoding='utf-8-sig'),delimiter=';')
w.writerow(['KOD','NAZWA','DL','SZ','SZT','OKLEINA','NAWIERTY','UWAGI'])
for r in P: w.writerow(r)
area=0;n=0
for r in P:
    if isinstance(r[2],(int,float)): area+=r[2]*r[3]*r[4]/1e6; n+=r[4]
print(len(P),'pozycji (bez L); pole prostokątów m2:',round(area,2),'sztuk',n)
