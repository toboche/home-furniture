/* ========================================================================
   GARDEROBA (A/P02 07): DANE MODELU 3D (wszystko w milimetrach)
   Patrząc od drzwi: ściana tylna = na wprost (przewody wodne), lewa = z gzymsem, przednia = z drzwiami.
   Układ: X od lewej ściany ku prawej, Y od podłogi w górę, Z od tylnej ściany ku drzwiom.
   Wymiary z pomiary.md (najmniejsze odczyty). Szafki: na razie tylko bryły (zamysł), bez wnętrza i bez formatek.
   Opis formatu ITEMS: wspolne/STRUKTURA.md, punkt 4.
   ======================================================================== */
var HF_MODEL=(function(){
'use strict';
/* pomiary (pomiary.md) */
var A=1825;            /* szerokość: lewa–prawa ściana */
var G=1490;            /* głębokość: tylna–przednia ściana */
var J=2586;            /* wysokość, najmniejsza (przy drzwiach) */
var PX=692, PXM=702;   /* wysięg pionu od lewej ściany: przy podłodze / największy (lico pionu nie jest pionowe) */
var PZ=562;            /* wysięg pionu od tylnej ściany */
var DX=164, DW=694, DH=2014;   /* drzwi: od prawej ściany, szerokość i wysokość w świetle ościeżnicy */
var W1=2415, W2=317, W3=130, W4=120;   /* wylot wentylacyjny: wysokość środka, od lewej ściany, średnica, wysięg od lica pionu */
var GZ1=333, GZ2=129, GZ3=927;         /* gzyms: wysokość, wysięg od lewej ściany, długość od pionu */
var GR3=135, GR4=55;                   /* rura w gzymsie: góra od podłogi, wysięg poza lico gzymsu */
var R1=513, R2=613, R3=180, R4=50;     /* przewody wodne: od prawej ściany, wysokość po zagięciu, wysięg (ok.) */
var E1=210, E2=195;                    /* przyszłe gniazdko na ścianie przedniej: środek od lewej ściany, od podłogi */
var L1=1131, L2=1000;                  /* lampa (oczko): środek od tylnej ściany, od lewej ściany */
var T=919;                             /* od lica pionu do ściany przedniej (najmniejszy) */

/* założenia szafek (ustalenia.md, 2026-11-11) */
var P=18;              /* płyta */
var LUZ=3;             /* luz: od pionu, pod sufitem, przy ścianie przedniej */
var ODS=5;             /* odsunięcie korpusu od ściany na regulację przy montażu (ZAŁOŻENIE, do potwierdzenia) */
var HW=2120;           /* górna powierzchnia wieńca części otwartej */
var HG=J-LUZ;          /* góra szafek: 2583 */
var ZK=PZ+LUZ;         /* przód korpusu górnej części szafek na wprost: 565 */
var ZF=ZK+P;           /* płaszczyzna frontów szafek na wprost: 583 */
var XL=PXM+LUZ;        /* przód szafki po lewej (bez frontów): 705 */
var XP=A-LUZ;          /* prawy bok szafek na wprost: 1822 */
var XM=(XL+XP)/2;      /* podział na 2 moduły */
var ZP=PZ+T-LUZ;       /* koniec szafki po lewej przy ścianie przedniej: 562 + 919 − 3 = 1478 */

var ITEMS=[
  /* Pion (PX przy podłodze 692, wyżej do 702: rysowany z największym wysięgiem PXM) */
  {n:'Pion (wysięg '+PXM+' od lewej ściany, '+PZ+' od tylnej; przy podłodze '+PX+')',layer:'Pion i gzyms',x:0,y:0,z:0,w:PXM,h:J,d:PZ,c:0xd9d4ca},
  /* Gzyms wzdłuż lewej ściany od pionu do ściany przedniej */
  {n:'Gzyms ('+GZ2+' × '+GZ1+', długość '+GZ3+')',layer:'Pion i gzyms',x:0,y:0,z:G-GZ3,w:GZ2,h:GZ1,d:GZ3,c:0xc7c1b5},
  /* Rura w gzymsie przy licu pionu; wymiar wzdłuż gzymsu (80) ZAŁOŻONY, nie mierzony */
  {n:'Rura wystająca z gzymsu (wysięg '+GR4+', do '+GR3+' od podłogi; szerokość 80 założona)',layer:'Osprzęt',x:GZ2,y:0,z:G-GZ3,w:GR4,h:GR3,d:80,c:0xb08d57},

  /* Wylot wentylacyjny na licu pionu (strona do drzwi); na wylocie kratka, wylot można dociąć */
  {t:'cyl',n:'Wylot wentylacyjny Ø'+W3+' (wysięg '+W4+', można dociąć)',layer:'Osprzęt',cx:W2,cy:W1,z:PZ,r:W3/2,len:W4,c:0x6b7b8c},

  /* Przewody wodne na ścianie tylnej, zagięte w dół i na boki; szerokość 40 założona */
  {n:'Przewód wodny R1 ('+R1+' od prawej ściany, do ok. '+R3+', wysięg ok. '+R4+')',layer:'Osprzęt',x:A-R1-20,y:0,z:0,w:40,h:R3,d:R4,c:0xc0392b},
  {n:'Przewód wodny R2 ('+R2+' od prawej ściany, do ok. '+R3+', wysięg ok. '+R4+')',layer:'Osprzęt',x:A-R2-20,y:0,z:0,w:40,h:R3,d:R4,c:0x2e5fb3},

  /* Przyszłe gniazdko na ścianie przedniej (rysowane 80 × 80, grubość 15 założona) */
  {n:'Gniazdko (E1 '+E1+' od lewej ściany, E2 '+E2+' od podłogi)',layer:'Osprzęt',x:E1-40,y:E2-40,z:G-15,w:80,h:80,d:15,c:0xe58a2b},

  /* ===== Bryły szafek (zamysł, bez wnętrza) ===== */
  /* Szafki na wprost: 2 moduły od boku pionu (+3) do prawej ściany (−3). Część otwarta do HW pełnej głębokości do płaszczyzny frontów,
     część górna: korpus do ZK i fronty ZK–ZF (3 mm przerwy między frontami). Odsunięte od ściany tylnej o ODS. */
  {n:'Na wprost, moduł 1: część otwarta ('+(XM-XL)+' × '+HW+' × '+(ZF-ODS)+')',layer:'Szafki na wprost (zamysł)',x:XL,y:0,z:ODS,w:XM-XL,h:HW,d:ZF-ODS,c:0x4f84c4,o:0.25},
  {n:'Na wprost, moduł 2: część otwarta ('+(XP-XM)+' × '+HW+' × '+(ZF-ODS)+')',layer:'Szafki na wprost (zamysł)',x:XM,y:0,z:ODS,w:XP-XM,h:HW,d:ZF-ODS,c:0x4f84c4,o:0.25},
  {n:'Na wprost, moduł 1: część górna z frontem ('+(XM-XL)+' × '+(HG-HW)+', korpus do '+ZK+')',layer:'Szafki na wprost (zamysł)',x:XL,y:HW,z:ODS,w:XM-XL,h:HG-HW,d:ZK-ODS,c:0x8a6bb8,o:0.3},
  {n:'Na wprost, moduł 2: część górna z frontem ('+(XP-XM)+' × '+(HG-HW)+', korpus do '+ZK+')',layer:'Szafki na wprost (zamysł)',x:XM,y:HW,z:ODS,w:XP-XM,h:HG-HW,d:ZK-ODS,c:0x8a6bb8,o:0.3},
  {n:'Na wprost: front górny 1 (zamysł)',layer:'Fronty (zamysł)',x:XL,y:HW+1.5,z:ZK,w:XM-XL-1.5,h:HG-HW-1.5,d:P,c:0x2f9e8f,o:0.55},
  {n:'Na wprost: front górny 2 (zamysł)',layer:'Fronty (zamysł)',x:XM+1.5,y:HW+1.5,z:ZK,w:XP-XM-1.5,h:HG-HW-1.5,d:P,c:0x2f9e8f,o:0.55},
  /* Szafka po lewej: od lewej ściany (ODS) do XL, od płaszczyzny frontów szafek na wprost (ZF) do ściany przedniej (−3); góra bez frontów.
     Nad gzymsem i rurą (część otwarta) – rozwiązanie do ustalenia. */
  {n:'Po lewej: część otwarta ('+(XL-ODS)+' × '+HW+' × '+(ZP-ZF)+'; gzyms i rura do rozwiązania)',layer:'Szafka po lewej (zamysł)',x:ODS,y:0,z:ZF,w:XL-ODS,h:HW,d:ZP-ZF,c:0x4fa36a,o:0.25},
  {n:'Po lewej: część górna bez frontów ('+(XL-ODS)+' × '+(HG-HW)+' × '+(ZP-ZF)+')',layer:'Szafka po lewej (zamysł)',x:ODS,y:HW,z:ZF,w:XL-ODS,h:HG-HW,d:ZP-ZF,c:0x7fbf7f,o:0.3},

  /* Lampa: oczko w suficie */
  {t:'cyl3',n:'Lampa (oczko) '+L2+' od lewej ściany, '+L1+' od tylnej',layer:'Osprzęt',ax:'y',px:L2,py:J-3,pz:L1,r:40,len:6,c:0xe0a526}
];

return {
  title:'Garderoba 3D',
  room:{W:A,D:G,H:J},
  wallThickness:100,
  openings:[{wall:'przod',pos:A-DX-DW,w:DW,y:0,h:DH}],
  views:{iso:[3.3,2.7,3.6],front:[0.91,1.3,4.9],top:[0.91,5.6,1.15],left:[-3.6,1.5,0.75]},
  conceptLayers:['Szafki na wprost (zamysł)','Szafka po lewej (zamysł)'],
  hiddenLayers:[],
  fixedLayers:['Pion i gzyms','Osprzęt'],
  boardLayers:['Półki','Ścianki boczne','Ścianki tylne','Fronty'],
  boardColor:{hex:0xeeece5,label:'docelowy: Egger W1200 ST9 Biały porcelanowy'},
  variants:[],
  items:ITEMS
};
})();
