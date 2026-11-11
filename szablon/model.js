/* ========================================================================
   SZABLON POMIESZCZENIA: dane modelu 3D (wszystko w milimetrach)
   Skopiuj katalog szablon/ jako nowe pomieszczenie (np. garderoba/), podmień ROOM, otwory i ITEMS.
   Układ: X od lewej ściany ku prawej, Y od podłogi w górę, Z od tylnej ściany ku wejściu.
   Ściany: 'tyl' (z = 0), 'przod' (z = D), 'lewa' (x = 0), 'prawa' (x = W).
   Wymiary wpisuj jako stałe z pomiarów (pomiary.md) i licz z nich położenia, np. x:A-B.

   Obiekty w ITEMS:
     prostopadłościan: {n:'Nazwa', layer:'Warstwa', x,y,z (minimalny róg), w,h,d, c:0xRRGGBB, o:1}
       w = szerokość (X), h = wysokość (Y), d = głębokość (Z), o = przezroczystość 0–1
     walec wzdłuż Z:    {t:'cyl', n, layer, cx,cy (środek), z (początek), r, len, c}
   Formatki (płyta 18 mm) leżą w warstwach 'Ścianki boczne', 'Ścianki tylne', 'Półki'
   i mają nazwę 'KOD: opis' albo 'KOD-1: opis' (kilka sztuk tego samego wymiaru).
   Fronty: warstwa 'Fronty', nazwa 'F1: opis'. Zawiasy: warstwa 'Zawiasy', bryła 35 × 35 przy krawędzi frontu.
   Łączniki generuje: python3 wspolne/pipeline/run.py NAZWA_KATALOGU
   ======================================================================== */
var HF_MODEL=(function(){
'use strict';
/* pomiary (pomiary.md) */
var A=1200;   /* szerokość pokoju */
var G=1000;   /* głębokość pokoju */
var J=2500;   /* wysokość pokoju */
/* założenia */
var P=18;     /* grubość płyty */
var SZ=600, WYS=2000, GL=500; /* szafka przykładowa: szerokość, wysokość, głębokość korpusu */

var ITEMS=[
  /* Szafka przykładowa S1 przy lewej i tylnej ścianie */
  {n:'S1B-1: S1: bok lewy',layer:'Ścianki boczne',x:0,y:0,z:0,w:P,h:WYS,d:GL,c:0xcdbb95},
  {n:'S1B-2: S1: bok prawy',layer:'Ścianki boczne',x:SZ-P,y:0,z:0,w:P,h:WYS,d:GL,c:0xcdbb95},
  {n:'S1T: S1: tył',layer:'Ścianki tylne',x:P,y:0,z:0,w:SZ-2*P,h:WYS,d:P,c:0xb9a37a},
  {n:'S1D: S1: dno',layer:'Półki',x:P,y:0,z:P,w:SZ-2*P,h:P,d:GL-P,c:0xd8c7a3},
  {n:'S1P: S1: półka',layer:'Półki',x:P,y:1000,z:P,w:SZ-2*P,h:P,d:GL-P,c:0xd8c7a3},
  {n:'S1W: S1: wieniec górny',layer:'Półki',x:P,y:WYS-P,z:P,w:SZ-2*P,h:P,d:GL-P,c:0xd8c7a3},
  {n:'F1: Front S1 (597 × 1997)',layer:'Fronty',x:1.5,y:1.5,z:GL,w:SZ-3,h:WYS-3,d:P,c:0x2f9e8f,o:0.55},
  {n:'Zawias F1 (lewa)',layer:'Zawiasy',x:6.5,y:100,z:GL+1,w:35,h:35,d:11,c:0x2b3034},
  {n:'Zawias F1 (lewa)',layer:'Zawiasy',x:6.5,y:WYS-135,z:GL+1,w:35,h:35,d:11,c:0x2b3034}
];

return {
  title:'Szablon 3D',
  room:{W:A,D:G,H:J},
  wallThickness:100,
  openings:[{wall:'przod',pos:700,w:800,y:0,h:2000}],   /* drzwi: 700 od lewej ściany, 800 × 2000 */
  views:{iso:[2.6,2.4,3.0],front:[0.6,1.25,4.2],top:[0.6,5.2,0.8],left:[-3.2,1.4,0.5]},
  conceptLayers:[],
  hiddenLayers:[],
  fixedLayers:[],
  boardLayers:['Półki','Ścianki boczne','Ścianki tylne','Fronty'],
  boardColor:{hex:0xeeece5,label:'docelowy: Egger W1200 ST9 Biały porcelanowy'},
  variants:[],
  items:ITEMS
};
})();
