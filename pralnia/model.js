/* ========================================================================
   PRALNIA: DANE MODELU 3D (wszystko w milimetrach)
   Układ: X od lewej ściany ku prawej, Y od podłogi w górę,
          Z od tylnej ściany ku wejściu.
   Silnik wizualizacji: wspolne/viewer/viewer.js (wspólny dla wszystkich pomieszczeń).
   Łączniki (otwory, konfirmaty, kołki, puszki zawiasów) są generowane do laczniki.gen.js
   przez: python3 wspolne/pipeline/run.py pralnia   (nie dopisywać ich tutaj ręcznie).

   Aby dodać szafę lub dodatek, dopisz obiekt do tablicy ITEMS:
     prostopadłościan: {n:'Nazwa', layer:'Warstwa', x,y,z (minimalny róg), w,h,d, c:0xRRGGBB, o:1}
       w = szerokość (X), h = wysokość (Y), d = głębokość (Z), o = przezroczystość 0–1
     walec wzdłuż Z:    {t:'cyl', n:'Nazwa', layer:'Warstwa', cx,cy (środek), z (początek), r, len, c:0xRRGGBB}
     walec wzdłuż osi:  {t:'cyl3', n, layer, ax:'x'|'y'|'z', px,py,pz (środek), r, len, c}
   Formatki (płyty 18 mm) mają nazwę zaczynającą się od kodu: 'KOD: opis' lub 'KOD-1: opis'.
   ======================================================================== */
var HF_MODEL=(function(){
'use strict';
var ROOM={W:1739,D:1497,H:2661};
var DOOR={x:823,w:805,h:2016};

var ITEMS=[
  /* Maszyny: B = 618, C = 598, głębokość z drzwiczkami 658 od ściany */
  {n:'Pralka (Bosch WGG244)',layer:'Maszyny',x:618,y:0,z:10,w:598,h:848,d:636,c:0xf1f2f0},
  {n:'Zestaw łączący',layer:'Maszyny',x:618,y:848,z:10,w:598,h:23,d:636,c:0x8a9096},
  {n:'Suszarka (Bosch WQG245)',layer:'Maszyny',x:618,y:871,z:10,w:598,h:842,d:648,c:0xf1f2f0},
  {t:'cyl',n:'Drzwiczki pralki',layer:'Maszyny',cx:917,cy:424,z:634,r:150,len:12,c:0xaebdc6},
  {t:'cyl',n:'Drzwiczki suszarki',layer:'Maszyny',cx:917,cy:1300,z:646,r:165,len:12,c:0xaebdc6},

  /* Pion i gzyms: R = 42, Q = 118, GZ1 = 73, GZ2 = 73, X = 489, GZ3 = 466, GZ4 = 680 */
  {n:'Pion',layer:'Pion i gzyms',x:1376,y:0,z:0,w:363,h:2661,d:362,c:0xd9d4ca},
  {n:'Gzyms przy maszynach (118)',layer:'Pion i gzyms',x:1258,y:0,z:0,w:118,h:489,d:435,c:0xc7c1b5},
  {n:'Gzyms na froncie pionu (73)',layer:'Pion i gzyms',x:1376,y:0,z:362,w:363,h:489,d:73,c:0xc7c1b5},
  {n:'Gzyms na prawej ścianie (73 × 680)',layer:'Pion i gzyms',x:1666,y:0,z:435,w:73,h:466,d:607,c:0xc7c1b5},

  /* Osprzęt: GN1–GN4, ZW1, ZW2, GP1, GP2, otwór K, L, M, N */
  {n:'Gniazdko 1 (GN1, GN2)',layer:'Osprzęt',x:0,y:878,z:202,w:15,h:80,d:80,c:0xe58a2b},
  {n:'Gniazdko 2 (GN3, GN4)',layer:'Osprzęt',x:0,y:179,z:665,w:15,h:80,d:80,c:0xe58a2b},
  {n:'Zawór (ZW1, ZW2)',layer:'Osprzęt',x:1240,y:777,z:0,w:50,h:60,d:160,c:0xb08d57},
  {n:'Gniazdka za maszynami (GP1, GP2)',layer:'Osprzęt',x:1305,y:977,z:0,w:60,h:60,d:60,c:0xe58a2b},
  {t:'cyl',n:'Otwór wentylacyjny (M, N)',layer:'Osprzęt',cx:1616,cy:2409,z:362,r:60.5,len:2,c:0x2b3034},

  /* Zabudowa szczeliny nad gzymsem: ZB1 = 160, ZB2 = 160, ZB3 = 1070 */
  {n:'Zabudowa ZB (zamysł)',layer:'Zabudowa ZB',x:1216,y:489,z:0,w:160,h:581,d:160,c:0xe0a526,o:0.3},

  /* Szafka po lewej (zamysł): Z = 610, Y = 658, wysokość J − 3 */
  {n:'Szafka lewa (zamysł)',layer:'Szafka lewa',x:5,y:0,z:0,w:610,h:2658,d:658,c:0x4f84c4,o:0.32},

  /* Szafka prawa (zamysł), front równo z maszynami na z = 658, głębokość zmienna.
     Kolumna serwisowa nad szczeliną ZB1 (x 1221 do 1371) ze zdejmowanym tyłem = panel ZB. Bez przegrody między kolumną a częścią przed pionem: półki w kształcie L (część przy szczelinie x 1239 do 1371 plus część przed pionem od x 1371).
     Wcięcie 73 × 466 przy prawej ścianie (gzyms), cofnięcie dołu przed gzyms (z = 440). */
  {n:'Prawa: kolumna dół (218 głęb.)',layer:'Szafka prawa',x:1221,y:0,z:440,w:150,h:489,d:218,c:0x4fa36a,o:0.32},
  {n:'Prawa: kolumna serwisowa przed ZB (493 głęb.)',layer:'Szafka prawa',x:1221,y:489,z:165,w:150,h:581,d:493,c:0x4fa36a,o:0.32},
  {n:'Prawa: kolumna nad ZB (493 głęb.)',layer:'Szafka prawa',x:1221,y:1075,z:165,w:150,h:1583,d:493,c:0x4fa36a,o:0.32},
  {n:'Prawa: dół z wcięciem na gzyms (218 głęb.)',layer:'Szafka prawa',x:1376,y:0,z:440,w:287,h:466,d:218,c:0x4fa36a,o:0.32},
  {n:'Prawa: pas nad gzymsem prawej ściany (218 głęb.)',layer:'Szafka prawa',x:1376,y:466,z:440,w:360,h:23,d:218,c:0x4fa36a,o:0.32},
  {n:'Prawa: góra przed pionem (291 głęb.)',layer:'Szafka prawa',x:1376,y:489,z:367,w:360,h:2169,d:291,c:0x4fa36a,o:0.32},
  {n:'Wentylowany fragment przy otworze (zamysł)',layer:'Szafka prawa',x:1546,y:2339,z:367,w:140,h:140,d:291,c:0xe0a526,o:0.5},

  /* Szafka nad maszynami (zamysł): dolna krawęd 1743 = 1713 + 30, góra J − 3 = 2658, korpus 606 mm w szczelinie 608 mm, własne boki.
     Front równo z resztą na z = 658, pełna głębokość, tył na z = 5. */
  {n:'Szafka nad maszynami (korpus 606 × 915 w szczelinie 608, pełna głęb. 653)',layer:'Szafka nad maszynami',x:615,y:1743,z:5,w:606,h:915,d:653,c:0x8a6bb8,o:0.32},

  /* Kuweta w rogu naprzeciwko lewej szafki: 600 × 400 × 400, dłuższy bok wzdłuż ściany frontowej (orientacja do potwierdzenia) */
  {n:'Kuweta (600 × 400 × 400)',layer:'Dodatki',x:3,y:0,z:1094,w:600,h:400,d:400,c:0xbfa98a},

  /* Wyposażenie lewej szafki: tylko elementy o znanych wymiarach, układ wstępny */
  {n:'Suszarka na pranie, złożona (50 × 1400 × 600)',layer:'Wyposażenie',x:537,y:0,z:26,w:50,h:1400,d:600,c:0xd2b48c},
  {n:'IKEA UTRUSTA wnętrze szafy gospodarczej (330 × 1335 × 530), wysuwane na prowadnicach',layer:'Wyposażenie',x:23,y:110,z:60,w:330,h:1335,d:530,c:0x9aa5ad,o:0.3},
  {n:'Odkurzacz bezprzewodowy na haku zestawu UTRUSTA (250 × 700 × 300)',layer:'Wyposażenie',x:63,y:745,z:150,w:250,h:700,d:300,c:0x6b7b8c},
  {n:'Deska do prasowania (60 × 1400 × 400)',layer:'Wyposażenie',x:473,y:0,z:126,w:60,h:1400,d:400,c:0x8d99ae},

  /* Kosz, klasyczny odkurzacz i półka z żelazkiem: układ wstępny.
     Kosz zakładam 320 × 320 × 550 (podano 320x3230), rurę odkurzacza jako 500 ponad korpusem (do 1000 od podłogi). */
  /* Żelazko: bez osobnej półki w lewej szafce, w razie potrzeby trafia do prawej. */

  /* Fronty w pasie od 1743 do 2658: dwa rzędy po 456 z odstępem 3 mm, grubość 18, front do z = 658.
     Odstęp 3 mm między modułami (po 1,5 mm z każdej strony granicy 613 i 1221). */
  {n:'F1: Front lewa, góra (607 × 453)',layer:'Fronty',x:6.5,y:2199,z:640,w:607,h:453,d:18,c:0x2f9e8f,o:0.55},
  {n:'F2: Front lewa, dół (607 × 453)',layer:'Fronty',x:6.5,y:1743,z:640,w:607,h:453,d:18,c:0x2f9e8f,o:0.55},
  {n:'F3: Front nad maszynami, góra (603 × 453)',layer:'Fronty',x:616.5,y:2199,z:640,w:603,h:453,d:18,c:0x2f9e8f,o:0.55},
  {n:'F4: Front nad maszynami, dół (603 × 453)',layer:'Fronty',x:616.5,y:1743,z:640,w:603,h:453,d:18,c:0x2f9e8f,o:0.55},
  /* Front górny po prawej podzielony pionowo: część otwierana (zawiasy po prawej, przy linii podziału, prowadnik zawiasu Blum 79B9590 na tylnej ściance F6) i część stała z kratką, przykręcana od wewnątrz. */
  {n:'F5: Front prawa, góra, otwierany (274,5 × 453)',layer:'Fronty',x:1222.5,y:2199,z:640,w:274.5,h:453,d:18,c:0x2f9e8f,o:0.55},
  {n:'F6: Front prawa, góra, stały z kratką (234,5 × 453)',layer:'Fronty',x:1500,y:2199,z:640,w:234.5,h:453,d:18,c:0x2f9e8f,o:0.55},
  {n:'F7: Front prawa, dół (512 × 453)',layer:'Fronty',x:1222.5,y:1743,z:640,w:512,h:453,d:18,c:0x2f9e8f,o:0.55},
  {t:'cyl',n:'Kratka wywiewu Ø 150 w froncie stałym',layer:'Fronty',cx:1616,cy:2409,z:640,r:75,len:19,c:0xe0a526},
  /* Kanał wentylacyjny: rura okrągła Ø 125 od otworu w ścianie (z = 362) do tylnej strony frontu stałego (z = 640), zamocowana do szafki, uszczelniona pianką przy ścianie i przy froncie. */
  {t:'cyl',n:'Kanał wentylacyjny (rura Ø 125, z 362 do 640)',layer:'Kanał wentylacyjny',cx:1616,cy:2409,z:362,r:62.5,len:278,c:0x9aa5ad},
  /* Listwy pod wkręty frontu stałego (18 × 18), po wewnętrznej stronie przodu komory. */
  {n:'Kątownik 25×25 pod F6, bok prawy: ramię przy froncie',layer:'Kątowniki pod F6',x:1693,y:2260,z:638,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, bok prawy: ramię przy boku',layer:'Kątowniki pod F6',x:1716,y:2260,z:615,w:2,h:25,d:25,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, bok prawy: ramię przy froncie',layer:'Kątowniki pod F6',x:1693,y:2550,z:638,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, bok prawy: ramię przy boku',layer:'Kątowniki pod F6',x:1716,y:2550,z:615,w:2,h:25,d:25,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, dół: ramię przy froncie',layer:'Kątowniki pod F6',x:1510,y:2206.5,z:638,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, dół: ramię na półce',layer:'Kątowniki pod F6',x:1510,y:2206.5,z:615,w:25,h:2,d:25,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, dół: ramię przy froncie',layer:'Kątowniki pod F6',x:1680,y:2206.5,z:638,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, dół: ramię na półce',layer:'Kątowniki pod F6',x:1680,y:2206.5,z:615,w:25,h:2,d:25,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, góra: ramię przy froncie',layer:'Kątowniki pod F6',x:1510,y:2609,z:638,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, góra: ramię pod półką',layer:'Kątowniki pod F6',x:1510,y:2632,z:615,w:25,h:2,d:25,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, góra: ramię przy froncie',layer:'Kątowniki pod F6',x:1680,y:2609,z:638,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Kątownik 25×25 pod F6, góra: ramię pod półką',layer:'Kątowniki pod F6',x:1680,y:2632,z:615,w:25,h:2,d:25,c:0x9aa5ad},
  /* Fronty prawego modułu dolnego (zawiasy po prawej): przerwy 3 mm w środku płyt na 498, 910 i 1322; dolny rząd węższy (do 1661,5) przez gzyms przy prawej ścianie. */
  {n:'F8: Front prawa dolna, rząd 1 (439 × 493,5)',layer:'Fronty',x:1222.5,y:3,z:640,w:439,h:493.5,d:18,c:0x2f9e8f,o:0.55},
  {n:'F9: Front prawa dolna, jeden wysoki (512 × 1240,5)',layer:'Fronty',x:1222.5,y:499.5,z:640,w:512,h:1240.5,d:18,c:0x2f9e8f,o:0.55},

  /* Zawiasy puszkowe (otwory Ø 35; środek puszki 22,5 mm od krawędzi frontu (F5: Blum 79B9590 do drzwi równoległych, prowadnik na tyle F6, puszka 22,5 mm), po 100 mm od końców frontu). Lewa strona: fronty lewego modułu i modułu nad maszynami; prawa strona: wszystkie fronty prawego modułu. */
  {n:'Zawias: lewa, góra (lewa)',layer:'Zawiasy',x:11.5,y:2281.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: lewa, góra (lewa)',layer:'Zawiasy',x:11.5,y:2534.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: lewa, dół (lewa)',layer:'Zawiasy',x:11.5,y:1825.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: lewa, dół (lewa)',layer:'Zawiasy',x:11.5,y:2078.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: nad maszynami, góra (prawa)',layer:'Zawiasy',x:1179.5,y:2281.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: nad maszynami, góra (prawa)',layer:'Zawiasy',x:1179.5,y:2534.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: nad maszynami, dół (prawa)',layer:'Zawiasy',x:1179.5,y:1825.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: nad maszynami, dół (prawa)',layer:'Zawiasy',x:1179.5,y:2078.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa, góra (otwierany) (prawa)',layer:'Zawiasy',x:1457,y:2281.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa, góra (otwierany) (prawa)',layer:'Zawiasy',x:1457,y:2534.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa, dół (prawa)',layer:'Zawiasy',x:1694.5,y:1825.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa, dół (prawa)',layer:'Zawiasy',x:1694.5,y:2078.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa dolna, rząd 1 (prawa)',layer:'Zawiasy',x:1621.5,y:85.5,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa dolna, rząd 1 (prawa)',layer:'Zawiasy',x:1621.5,y:379.0,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa dolna, wysoki front (prawa)',layer:'Zawiasy',x:1694.5,y:582.0,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa dolna, wysoki front (prawa)',layer:'Zawiasy',x:1694.5,y:1102.0,z:641,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias: prawa dolna, wysoki front (prawa)',layer:'Zawiasy',x:1694.5,y:1622.5,z:641,w:35,h:35,d:11,c:0x2b3034},


  /* Uchwyty IKEA GUBBARP, biały, 116 mm (rozstaw otworów 96, szerokość 21, wysokość od frontu 27). Otwory pod uchwyty wykonuje użytkownik samodzielnie, nie ma ich w nawiertach. */
  {n:'Uchwyt GUBBARP przy F1',layer:'Uchwyty',x:573,y:2249,z:658,w:21,h:116,d:27,c:0xf4f4f4},
  {n:'Uchwyt GUBBARP przy F2',layer:'Uchwyty',x:573,y:2030,z:658,w:21,h:116,d:27,c:0xf4f4f4},
  {n:'Uchwyt GUBBARP przy F3',layer:'Uchwyty',x:636,y:2249,z:658,w:21,h:116,d:27,c:0xf4f4f4},
  {n:'Uchwyt GUBBARP przy F4',layer:'Uchwyty',x:636,y:2030,z:658,w:21,h:116,d:27,c:0xf4f4f4},
  {n:'Uchwyt GUBBARP przy F5',layer:'Uchwyty',x:1242,y:2249,z:658,w:21,h:116,d:27,c:0xf4f4f4},
  {n:'Uchwyt GUBBARP przy F7',layer:'Uchwyty',x:1242,y:2030,z:658,w:21,h:116,d:27,c:0xf4f4f4},
  {n:'Uchwyt GUBBARP przy F8',layer:'Uchwyty',x:1242,y:330.5,z:658,w:21,h:116,d:27,c:0xf4f4f4},
  {n:'Uchwyt GUBBARP przy F9',layer:'Uchwyty',x:1242,y:992,z:658,w:21,h:116,d:27,c:0xf4f4f4},

  /* Wciskane podpórki półek Ø5 (półka L = PP z przodu + KP z tyłu kolumny, połączone kołkami w z=385; przesuwane razem). Lewa strona opiera się na KB2 w 4 punktach (z 213 i 355 pod KP, z 417 i 590 pod PP), prawa na PB2 w 2 punktach (z 417, 590). Poziom 489 stoi na konfirmatach (bez podpórek). */
  {n:'Podpórka półki, bok KB2 (poziom 922)',layer:'Podpórki półek',x:1239,y:917,z:210,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki, bok KB2 (poziom 922)',layer:'Podpórki półek',x:1239,y:917,z:352,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki, bok KB2 (poziom 922)',layer:'Podpórki półek',x:1239,y:917,z:414,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki, bok KB2 (poziom 922)',layer:'Podpórki półek',x:1239,y:917,z:587,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki PP, bok PB2 (poziom 922)',layer:'Podpórki półek',x:1711,y:917,z:414,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki PP, bok PB2 (poziom 922)',layer:'Podpórki półek',x:1711,y:917,z:587,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki, bok KB2 (poziom 1355)',layer:'Podpórki półek',x:1239,y:1350,z:210,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki, bok KB2 (poziom 1355)',layer:'Podpórki półek',x:1239,y:1350,z:352,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki, bok KB2 (poziom 1355)',layer:'Podpórki półek',x:1239,y:1350,z:414,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki, bok KB2 (poziom 1355)',layer:'Podpórki półek',x:1239,y:1350,z:587,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki PP, bok PB2 (poziom 1355)',layer:'Podpórki półek',x:1711,y:1350,z:414,w:7,h:5,d:5,c:0xc0392b},
  {n:'Podpórka półki PP, bok PB2 (poziom 1355)',layer:'Podpórki półek',x:1711,y:1350,z:587,w:7,h:5,d:5,c:0xc0392b},

  /* Półki (płyta 18 mm). Dolne moduły stoją na kafelkach, bez płyty dolnej i bez nóżek. Spód pasa frontów (1743 do 1761) zamyka dolne moduły.
     Pas: moduły kończą się na 2652; płyty 1743, 2188,5 i 2634 (przedziały po 427,5), szczelinę 3 mm między frontami obejmuje płyta środkowa. */
  {n:'PP1: Półka przednia (489 do 507)',layer:'Półki',x:1239,y:489,z:367,w:497,h:18,d:273,c:0xe6d7b8},
  {n:'KP1: Półka kolumny, tył (489 do 507)',layer:'Półki',x:1239,y:489,z:183,w:132,h:18,d:184,c:0xe6d7b8},
  {n:'PP2-1: Półka przednia (922 do 940)',layer:'Półki',x:1239.75,y:922,z:385,w:477.5,h:18,d:255,c:0xe6d7b8},
  {n:'KP2-1: Półka kolumny, tył (922 do 940)',layer:'Półki',x:1239.75,y:922,z:183,w:130.5,h:18,d:202,c:0xe6d7b8},
  {n:'PP2-2: Półka przednia (1355 do 1373)',layer:'Półki',x:1239.75,y:1355,z:385,w:477.5,h:18,d:255,c:0xe6d7b8},
  {n:'KP2-2: Półka kolumny, tył (1355 do 1373)',layer:'Półki',x:1239.75,y:1355,z:183,w:130.5,h:18,d:202,c:0xe6d7b8},
  {n:'PP3-1: Półka przednia (1743 do 1761)',layer:'Półki',x:1239,y:1743,z:385,w:479,h:18,d:255,c:0xe6d7b8},
  {n:'KP3-1: Półka kolumny, tył (1743 do 1761)',layer:'Półki',x:1239,y:1743,z:183,w:132,h:18,d:202,c:0xe6d7b8},
  {n:'PP3-2: Półka przednia (2188,5 do 2206,5)',layer:'Półki',x:1239,y:2188.5,z:385,w:479,h:18,d:255,c:0xe6d7b8},
  {n:'KP3-2: Półka kolumny, tył (2188,5 do 2206,5)',layer:'Półki',x:1239,y:2188.5,z:183,w:132,h:18,d:202,c:0xe6d7b8},
  {n:'PP3-3: Półka przednia (2634 do 2652)',layer:'Półki',x:1239,y:2634,z:385,w:479,h:18,d:255,c:0xe6d7b8},
  {n:'KP3-3: Półka kolumny, tył (2634 do 2652)',layer:'Półki',x:1239,y:2634,z:183,w:132,h:18,d:202,c:0xe6d7b8},
  {n:'L2P-1: Pas, lewa: spód (1743 do 1761)',layer:'Półki',x:23,y:1743,z:21,w:574,h:18,d:619,c:0xe6d7b8},
  {n:'NWP-1: Pas, nad maszynami: spód (1743 do 1761)',layer:'Półki',x:633,y:1743,z:23,w:570,h:18,d:617,c:0xe6d7b8},
  {n:'L2P-2: Pas, lewa: środek (2188,5 do 2206,5)',layer:'Półki',x:23,y:2188.5,z:21,w:574,h:18,d:619,c:0xe6d7b8},
  {n:'NWP-2: Pas, nad maszynami: środek (2188,5 do 2206,5)',layer:'Półki',x:633,y:2188.5,z:23,w:570,h:18,d:617,c:0xe6d7b8},
  {n:'L2P-3: Pas, lewa: góra (2634 do 2652)',layer:'Półki',x:23,y:2634,z:21,w:574,h:18,d:619,c:0xe6d7b8},
  {n:'NWP-3: Pas, nad maszynami: góra (2634 do 2652)',layer:'Półki',x:633,y:2634,z:23,w:570,h:18,d:617,c:0xe6d7b8},
  /* Wieńce górne (usztywnienie dolnych szafek): pas 100 mm przy froncie, pod samym pasem (y 1725 do 1743), tył do z 640 (front od z 640). */
  {n:'L1W: L1: wieniec górny, przód (1725 do 1743)',layer:'Półki',x:23,y:1725,z:540,w:574,h:18,d:100,c:0xe6d7b8},
  {n:'RDW: Prawa dolna: wieniec górny, przód (1725 do 1743)',layer:'Półki',x:1239,y:1725,z:540,w:479,h:18,d:100,c:0xe6d7b8},
  /* Wariant: F8 usunięte, ta sama kuweta 600 × 400 × 400 wchodzi węższym końcem (400) we wnękę 406 × 489 × 205 (z 435 do 640); wystaje 395. Kuweta z rogu jest wtedy ukryta. */
  {n:'Kuweta w F8 (600 × 400 × 400)',layer:'Kuweta (przykład)',x:1242,y:0,z:435,w:400,h:400,d:600,c:0xbfa98a},

  /* Ścianki boczne (płyta 18 mm). Boki stoją prosto na kafelkach. Lewa ściana pokoju jest lewym bokiem dolnej lewej szafki (odkurzacz bezprzewodowy, gniazdko GN1).
     Moduł nad maszynami ma własne boki (po 1 mm luzu od boków sąsiadów). */
  {n:'L1B1: L1: bok prawy (przy maszynach)',layer:'Ścianki boczne',x:597,y:0,z:3,w:18,h:1743,d:655,c:0xcdbb95},
  {n:'L2B-1: L2: bok lewy (pas)',layer:'Ścianki boczne',x:5,y:1743,z:3,w:18,h:909,d:637,c:0xcdbb95},
  {n:'L2B-2: L2: bok prawy (pas)',layer:'Ścianki boczne',x:597,y:1743,z:3,w:18,h:909,d:637,c:0xcdbb95},
  /* Moduł nad maszynami ma własne boki: korpus 606 mm (x 614 do 1220) w szczelinie 608 mm między bokami sąsiadów, wnętrze 570 mm. */
  {n:'NWB-1: Wnęka: bok lewy (pas)',layer:'Ścianki boczne',x:615,y:1743,z:5,w:18,h:909,d:635,c:0xcdbb95},
  {n:'NWB-2: Wnęka: bok prawy (pas)',layer:'Ścianki boczne',x:1203,y:1743,z:5,w:18,h:909,d:635,c:0xcdbb95},
  {n:'KB1: Kolumna: bok lewy, dół',layer:'Ścianki boczne',x:1221,y:0,z:440,w:18,h:489,d:200,c:0xcdbb95},
  {n:'KB2: Kolumna: bok lewy, środek i góra',layer:'Ścianki boczne',x:1221,y:489,z:165,w:18,h:1254,d:475,c:0xcdbb95},
  {n:'KB3: Kolumna: bok lewy, pas',layer:'Ścianki boczne',x:1221,y:1743,z:165,w:18,h:909,d:475,c:0xcdbb95},
  {n:'PB1: Prawa: bok prawy, dół (przy gzymsie)',layer:'Ścianki boczne',x:1645,y:0,z:440,w:18,h:489,d:200,c:0xcdbb95},
  {n:'PB2: Prawa: bok prawy, góra',layer:'Ścianki boczne',x:1718,y:507,z:367,w:18,h:1236,d:273,c:0xcdbb95},
  {n:'PB3: Prawa: bok prawy, pas',layer:'Ścianki boczne',x:1718,y:1743,z:367,w:18,h:909,d:273,c:0xcdbb95},

  /* Ścianki tylne (płyta 18 mm, wpuszczone między boki, tył równo z tylną krawędzią boków). Osobna warstwa. Tył prawej szafki przy otworze wywiewu jest rozcięty (otwór 140 × 140 na 2339 do 2479). */
  {n:'L1T: L1: tył',layer:'Ścianki tylne',x:23,y:0,z:3,w:574,h:1743,d:18,c:0x9c8b6e,o:0.9},
  {n:'L2T: L2: tył (pas)',layer:'Ścianki tylne',x:23,y:1743,z:3,w:574,h:909,d:18,c:0x9c8b6e,o:0.9},
  {n:'NWT: Wnęka nad maszynami: tył',layer:'Ścianki tylne',x:633,y:1743,z:5,w:570,h:909,d:18,c:0x9c8b6e,o:0.9},
  {n:'PT1: Prawa dół: tył (kolumna i część przed pionem)',layer:'Ścianki tylne',x:1239,y:0,z:440,w:406,h:489,d:18,c:0x9c8b6e,o:0.9},
  {n:'KT1A: Kolumna: tył, zawór, zdejmowany do przodu, trzymany magnesami (y 509-916)',layer:'Ścianki tylne',x:1241.5,y:509,z:165,w:127,h:407,d:18,c:0x9c8b6e,o:0.9},
  {n:'Kątownik KT1A, ramię przy boku KB2',layer:'Kątowniki pod KT1',x:1239,y:579,z:165,w:2,h:25,d:25,c:0x9aa5ad},
  {n:'Kątownik KT1A, ramię za płytą',layer:'Kątowniki pod KT1',x:1239,y:579,z:163,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Magnes Ø10 x 3 w KT1A (gniazdo wiercisz sam)',layer:'Kątowniki pod KT1',x:1248,y:586,z:165,w:10,h:10,d:3,c:0x222222},
  {n:'Kątownik KT1A, ramię przy boku KB2',layer:'Kątowniki pod KT1',x:1239,y:804,z:165,w:2,h:25,d:25,c:0x9aa5ad},
  {n:'Kątownik KT1A, ramię za płytą',layer:'Kątowniki pod KT1',x:1239,y:804,z:163,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Magnes Ø10 x 3 w KT1A (gniazdo wiercisz sam)',layer:'Kątowniki pod KT1',x:1248,y:811,z:165,w:10,h:10,d:3,c:0x222222},
  {n:'KT1B: Kolumna: tył, gniazdka, zdejmowany do przodu, trzymany magnesami (y 942-1349)',layer:'Ścianki tylne',x:1241.5,y:942,z:165,w:127,h:407,d:18,c:0x9c8b6e,o:0.9},
  {n:'Kątownik KT1B, ramię przy boku KB2',layer:'Kątowniki pod KT1',x:1239,y:1012,z:165,w:2,h:25,d:25,c:0x9aa5ad},
  {n:'Kątownik KT1B, ramię za płytą',layer:'Kątowniki pod KT1',x:1239,y:1012,z:163,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Magnes Ø10 x 3 w KT1B (gniazdo wiercisz sam)',layer:'Kątowniki pod KT1',x:1248,y:1019,z:165,w:10,h:10,d:3,c:0x222222},
  {n:'Kątownik KT1B, ramię przy boku KB2',layer:'Kątowniki pod KT1',x:1239,y:1237,z:165,w:2,h:25,d:25,c:0x9aa5ad},
  {n:'Kątownik KT1B, ramię za płytą',layer:'Kątowniki pod KT1',x:1239,y:1237,z:163,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Magnes Ø10 x 3 w KT1B (gniazdo wiercisz sam)',layer:'Kątowniki pod KT1',x:1248,y:1244,z:165,w:10,h:10,d:3,c:0x222222},
  {n:'KT1C: Kolumna: tył, zdejmowany do przodu, trzymany magnesami (y 1375-1725)',layer:'Ścianki tylne',x:1241.5,y:1375,z:165,w:127,h:350,d:18,c:0x9c8b6e,o:0.9},
  {n:'Kątownik KT1C, ramię przy boku KB2',layer:'Kątowniki pod KT1',x:1239,y:1445,z:165,w:2,h:25,d:25,c:0x9aa5ad},
  {n:'Kątownik KT1C, ramię za płytą',layer:'Kątowniki pod KT1',x:1239,y:1445,z:163,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Magnes Ø10 x 3 w KT1C (gniazdo wiercisz sam)',layer:'Kątowniki pod KT1',x:1248,y:1452,z:165,w:10,h:10,d:3,c:0x222222},
  {n:'Kątownik KT1C, ramię przy boku KB2',layer:'Kątowniki pod KT1',x:1239,y:1688,z:165,w:2,h:25,d:25,c:0x9aa5ad},
  {n:'Kątownik KT1C, ramię za płytą',layer:'Kątowniki pod KT1',x:1239,y:1688,z:163,w:25,h:25,d:2,c:0x9aa5ad},
  {n:'Magnes Ø10 x 3 w KT1C (gniazdo wiercisz sam)',layer:'Kątowniki pod KT1',x:1248,y:1695,z:165,w:10,h:10,d:3,c:0x222222},
  {n:'KT2: Kolumna: tył, pas (1743-2652)',layer:'Ścianki tylne',x:1239,y:1743,z:165,w:132,h:909,d:18,c:0x9c8b6e,o:0.9},
  {n:'PT2: Prawa: tył, dół i środek (507-1743)',layer:'Ścianki tylne',x:1371,y:507,z:367,w:347,h:1236,d:18,c:0x9c8b6e,o:0.9},
  {n:'PT3: Prawa: tył, pas (1743-2652), otwór Ø130 pod kanał wiercony samodzielnie: środek 245 od lewej, 243 od góry krawędzi',layer:'Ścianki tylne',x:1371,y:1743,z:367,w:347,h:909,d:18,c:0x9c8b6e,o:0.9},
  /* Wzmocnienie lewej dolnej szafki: lewy bok 18 mm z wycięciem 100 × 100 pod gniazdko GN1 (z 192 do 292, y 868 do 968),
     płyta dolna 18 mm (listwy tylne zbędne, rolę ramy przejął tył 18 mm). Odkurzacz bezprzewodowy po złożeniu 700 mm, góra 1600. */
  {n:'L1B2: L1: bok lewy (jedna formatka; wycięcie pod gniazdko GN1 100×100 robi użytkownik: y 868-968, z 192-292)',layer:'Ścianki boczne',x:5,y:0,z:3,w:18,h:1743,d:655,c:0xcdbb95},
  /* Moduły dolne stoją bezpośrednio na podłodze: bez stopek, bez płyty dolnej (y = 0). */
];

return {
  title:'Pralnia 3D',
  room:ROOM,
  wallThickness:100, /* grubość ścian, tylko wizualnie */
  /* otwory w ścianach: sciana 'przod' | 'tyl' (wzdłuż X) albo 'lewa' | 'prawa' (wzdłuż Z); pos = początek wzdłuż ściany, y = dolna krawędź */
  openings:[{wall:'przod',pos:DOOR.x,w:DOOR.w,y:0,h:DOOR.h}],
  /* pozycje kamery w metrach */
  views:{iso:[3.3,2.7,3.6],front:[0.87,1.35,4.9],top:[0.87,5.6,1.15],left:[-3.6,1.5,0.75]},
  /* bryły zamysłu (rysowane za płytami); domyślnie ukryte warstwy */
  conceptLayers:['Szafka lewa','Szafka prawa','Szafka nad maszynami','Zabudowa ZB'],
  hiddenLayers:['Szafka lewa','Szafka prawa','Szafka nad maszynami'],
  /* warstwy, które nie rozsuwają się suwakiem */
  fixedLayers:['Maszyny','Pion i gzyms','Osprzęt','Zabudowa ZB','Dodatki','Szafka lewa','Szafka prawa','Szafka nad maszynami'],
  boardLayers:['Półki','Ścianki boczne','Ścianki tylne','Płyta dolna i listwy','Fronty'],
  boardColor:{hex:0xeeece5,label:'docelowy: Egger W1200 ST9 Biały porcelanowy'}, /* kolor z ekranu orientacyjny, nie z próbki */
  noOffset:/^Kratka/, /* elementy bez przesunięcia w buforze głębi i bez koloru płyty */
  /* elementy, które przy rozsuwaniu jadą razem z innym (poza regułami ogólnymi: zawiasy, uchwyty, otwory, konfirmaty, kołki) */
  explodeParent:function(it,h){
    if(/^Kątownik 25×25 pod F6/.test(it.n)||/^Kratka/.test(it.n)||/^LF5:/.test(it.n)){return h.front(/^F6:/)||null;}
    var k=/^Kątownik (KT1[ABC])/.exec(it.n);if(k){return h.back(new RegExp('^'+k[1]+':'))||null;}
    return undefined;
  },
  variants:[{
    id:'variantF8',
    label:'F8 usunięte: kuweta we wnęce zamiast w rogu (406 × 489 × 205)',
    layer:'Kuweta (przykład)', /* warstwa widoczna tylko w tym wariancie */
    apply:function(on,h){
      function inF8(it){if((it.layer!=='Zawiasy'&&it.layer!=='Uchwyty')||!it.w)return false;var cx=it.x+it.w/2,cy=it.y+it.h/2;return cx>=1222.5&&cx<=1661.5&&cy>=3&&cy<=496.5;}
      h.pick.forEach(function(m){var it=m.userData.info;
        if((it.layer==='Fronty'&&/^F8:/.test(it.n))||inF8(it)){m.visible=on?false:h.layerOn(it.layer);}});
      (h.layers['Numeracja frontów']||[]).forEach(function(sp){var it=sp.userData.item;
        if(it&&/^F8:/.test(it.n))sp.visible=on?false:h.layerOn('Numeracja frontów');});
      h.variantItems.forEach(function(m){m.visible=on;});
      h.pick.forEach(function(m){if(/^Kuweta \(600/.test(m.userData.info.n))m.visible=on?false:h.layerOn(m.userData.info.layer);});
    }
  }],
  items:ITEMS
};
})();
