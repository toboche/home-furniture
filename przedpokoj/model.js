/* ========================================================================
   PRZEDPOKÓJ (A/P02 01): DANE MODELU 3D (wszystko w milimetrach)
   Ściana tylna (z = 0) = ściana z drzwiami łazienki D2 i rozdzielnicą. Ściana prawa (x = W) = ściana z drzwiami
   wejściowymi DM1. W narożniku tylnej i prawej ściany: pion EI60. Lewa ściana i ściana przednia są umowne
   (przedpokój ciągnie się dalej; modelujemy tylko fragment przy szafie).
   Układ: X od lewej ku prawej, Y od podłogi w górę, Z od ściany z D2 w głąb przedpokoju.
   X w pomiarach liczony od szczeliny przy ościeżnicy D2 (od strony szafy); w modelu to x = XO.
   Wymiary z pomiary.md (najmniejsze odczyty). Opis formatu ITEMS: wspolne/STRUKTURA.md, punkt 4.
   ======================================================================== */
var HF_MODEL=(function(){
'use strict';
/* pomiary (pomiary.md) */
var A=1100;            /* ściana od szczeliny D2 do narożnika z pionem */
var B=777, BG=783;     /* wysięg pionu od ściany z D2: przy podłodze / przy suficie */
var C=428;             /* czoło pionu: od krawędzi 1 (narożnik pionu) do ściany z DM1 */
var F=1235;            /* od czoła pionu do przeciwległej ściany */
var H=2664;            /* wysokość, najmniejsza (zakres 2664–2669) */
var OC=120;            /* od krawędzi 2 do ościeżnicy DM1 */
var DR1=800, DR2=2030, DR5=3;   /* D2: szerokość i wysokość skrzydła, szczelina od strony szafy */
var D=187, E=350, G=933, K=1000, RZ1=10;   /* rozdzielnica: od szczeliny D2, szerokość z ramką, dół od podłogi, wysokość, wysięg drzwiczek */
var DF1=245, DF2=1474, DF3=30;  /* otwór na kabel domofonu: środek od krawędzi 1, od podłogi, promień */
var DF4=183, DF5=1365;          /* domofon: lewy dolny róg od krawędzi 1, od podłogi */
var WL1=298, WL2=1214, WL3=70;  /* włącznik: środek od krawędzi 1, od podłogi, ramka (ok.) */

/* założenia i decyzje (ustalenia.md) */
var XO=1000;           /* położenie szczeliny D2 w modelu (umowny kawałek przedpokoju na lewo od D2) */
var P=18;              /* płyta */
var LUZ=3;             /* luz pod sufitem i przy boku pionu */
var ODS=2;             /* odsunięcie korpusów 775 od ściany: front w płaszczyźnie zaślepki (u góry dystans do 8) */
var ZK=B;              /* przód korpusów szafy i pawlacza: 777 (korpus 775) */
var ZF=ZK+P;           /* płaszczyzna frontów i zaślepki: 795 */
var YT=H-LUZ;          /* góra korpusów: 2661 */
var YP=YT-500;         /* podział góra / dół (dół pawlacza): 2161 */
var XS0=XO+20;         /* szezlong: 20 od szczeliny D2 */
var XS1=XS0+520;       /* szezlong szerokość 520 → 540 */
var XT0=XS1;           /* szafa wysoka od boku szezlonga */
var XT1=XO+A-LUZ;      /* do boku pionu z luzem 3: 1097 (szerokość 557) */
var ZS=500;            /* głębokość szezlonga (z frontem) */
var YN=177;            /* wnęka na buty: 0–177 */
var YB=412, YS=430, YC=460;     /* szezlong: spód blatu, góra blatu, góra poduszki (30) */
var ZN=50;             /* szafka nad szezlongiem: korpus 50, lico frontu 68 */
var XZ0=XO+A-1.5;      /* zaślepka: 3 mm od frontów szafy (1,5 poza narożnik pionu) */
var XZ1=XO+A+C-2;      /* zaślepka: 2 mm od ściany z DM1 */
var DMW=900, DMH=2000; /* DM1 w świetle (ZAŁOŻENIE, nominalnie 90/200) */

var W=XO+A+C, DD=B+F;  /* umowny pokój: 2528 × 2012 */
var WB=XS1-XS0-2*P;    /* wnętrze szezlonga, szafki nad nim i pawlacza: 484 */
var WT=XT1-XT0-2*P;    /* wnętrze szafy wysokiej: 521 */

/* zawiasy: środek puszki 22,5 od krawędzi frontu, skrajne 100 od końców, pozostałe równo */
function zawiasy(nazwa,fx,fy,fw,fh,strona,n){
  var out=[],x=(strona==='lewa')?fx+5:fx+fw-40;
  for(var i=0;i<n;i++){
    var cy=fy+100+i*(fh-200)/(n-1);
    out.push({n:'Zawias: '+nazwa+' ('+strona+')',layer:'Zawiasy',x:x,y:cy-17.5,z:ZF-P+1,w:35,h:35,d:11,c:0x2b3034});
  }
  return out;
}
function zawiasyN(nazwa,fx,fy,fw,fh,strona,n,z){
  return zawiasy(nazwa,fx,fy,fw,fh,strona,n).map(function(it){it.z=z+1;return it;});
}

var BOK=0xcdbb95, TYL=0x9c8b6e, POL=0xe6d7b8, FR=0x2f9e8f;

var ITEMS=[
  /* ===== Pomieszczenie ===== */
  {n:'Pion EI60 (wysięg '+B+' przy podłodze, '+BG+' przy suficie; czoło '+C+')',layer:'Pion',x:XO+A,y:0,z:0,w:C,h:H,d:B,c:0xd9d4ca},
  {n:'Rozdzielnica z ramką ('+E+' × '+K+', od '+G+'; drzwiczki wystają '+RZ1+', zawiasy po prawej)',layer:'Osprzęt',x:XO+D,y:G,z:0,w:E,h:K,d:RZ1,c:0xb0b4b8},
  {n:'Listwa przypodłogowa L 40 × 16 (zostaje lub do zdjęcia)',layer:'Osprzęt',x:XO-200,y:0,z:0,w:200+A,h:40,d:16,c:0xf4f4f4,o:0.8},

  /* ===== Szezlong SZ (x 20–540 od szczeliny D2): wnęka na buty, szuflada TIP-ON, blat, poduszka ===== */
  {n:'SZB-1: Szezlong: bok lewy (od D2)',layer:'Ścianki boczne',x:XS0,y:0,z:0,w:P,h:YB,d:ZS-P,c:BOK},
  {n:'SZB-2: Szezlong: bok prawy',layer:'Ścianki boczne',x:XS1-P,y:0,z:0,w:P,h:YB,d:ZS-P,c:BOK},
  {n:'SZW: Szezlong: blat (pod poduszką)',layer:'Półki',x:XS0,y:YB,z:0,w:XS1-XS0,h:P,d:ZS-P,c:POL},
  {n:'SZD: Szezlong: dno szuflady (nad wnęką)',layer:'Półki',x:XS0+P,y:YN,z:0,w:WB,h:P,d:ZS-P,c:POL},
  {n:'SZT: Szezlong: tył',layer:'Ścianki tylne',x:XS0+P,y:YN+P,z:0,w:WB,h:YB-YN-P,d:P,c:TYL,o:0.9},
  {n:'F1: Szuflada szezlonga (517 × 253), TIP-ON',layer:'Fronty',x:XS0+1.5,y:YN,z:ZS-P,w:XS1-XS0-3,h:YS-YN,d:P,c:FR,o:0.55},
  {n:'Skrzynka szuflady szezlonga (prowadnice push to open 450; wymiary po wyborze prowadnic)',layer:'Szuflady (skrzynki)',x:XS0+P+13,y:YN+P+13,z:P+10,w:WB-26,h:YB-YN-P-40,d:450,c:0xc9a227,o:0.45},
  {n:'Poduszka siedziska (30)',layer:'Tapicerka',x:XS0,y:YS,z:ZN+P,w:XS1-XS0,h:YC-YS,d:ZS-ZN-P,c:0x2b2b2b},

  /* ===== Szafka nad szezlongiem NS: korpus 50, bez tyłu (rozdzielnica), drzwi TIP-ON z zawiasami od D2 ===== */
  {n:'NSB-1: Nad szezlongiem: bok lewy',layer:'Ścianki boczne',x:XS0,y:YS,z:0,w:P,h:YP-YS,d:ZN,c:BOK},
  {n:'NSB-2: Nad szezlongiem: bok prawy',layer:'Ścianki boczne',x:XS1-P,y:YS,z:0,w:P,h:YP-YS,d:ZN,c:BOK},
  {n:'NSD: Nad szezlongiem: dno',layer:'Półki',x:XS0+P,y:YS,z:0,w:WB,h:P,d:ZN,c:POL},
  {n:'NSW: Nad szezlongiem: wieniec',layer:'Półki',x:XS0+P,y:YP-P,z:0,w:WB,h:P,d:ZN,c:POL},
  {n:'F2: Drzwi nad szezlongiem (517 × 1698), zawiasy od D2, TIP-ON',layer:'Fronty',x:XS0+1.5,y:YC+1.5,z:ZN,w:XS1-XS0-3,h:YP-1.5-(YC+1.5),d:P,c:FR,o:0.55},

  /* ===== Pawlacz PW nad szezlongiem: 500 od sufitu, front w linii szafy ===== */
  {n:'PWB-1: Pawlacz: bok lewy',layer:'Ścianki boczne',x:XS0,y:YP,z:ODS,w:P,h:YT-YP,d:ZK-ODS,c:BOK},
  {n:'PWB-2: Pawlacz: bok prawy',layer:'Ścianki boczne',x:XS1-P,y:YP,z:ODS,w:P,h:YT-YP,d:ZK-ODS,c:BOK},
  {n:'PWD: Pawlacz: dno',layer:'Półki',x:XS0+P,y:YP,z:ODS,w:WB,h:P,d:ZK-ODS,c:POL},
  {n:'PWW: Pawlacz: wieniec górny',layer:'Półki',x:XS0+P,y:YT-P,z:ODS,w:WB,h:P,d:ZK-ODS,c:POL},
  {n:'PWT: Pawlacz: tył',layer:'Ścianki tylne',x:XS0+P,y:YP+P,z:ODS,w:WB,h:YT-YP-2*P,d:P,c:TYL,o:0.9},
  {n:'F3: Pawlacz (517 × 498,5), zawiasy od D2, TIP-ON',layer:'Fronty',x:XS0+1.5,y:YP+1.5,z:ZK,w:XS1-XS0-3,h:YT-YP-1.5,d:P,c:FR,o:0.55},

  /* ===== Szafa wysoka, część dolna SD: wnęka 177, półki 300 (z szufladą) i 300, drążek na kurtki ===== */
  {n:'SDB-1: Szafa dół: bok lewy',layer:'Ścianki boczne',x:XT0,y:0,z:ODS,w:P,h:YP,d:ZK-ODS,c:BOK},
  {n:'SDB-2: Szafa dół: bok prawy (przy pionie)',layer:'Ścianki boczne',x:XT1-P,y:0,z:ODS,w:P,h:YP,d:ZK-ODS,c:BOK},
  {n:'SDD: Szafa dół: dno (nad wnęką)',layer:'Półki',x:XT0+P,y:YN,z:ODS,w:WT,h:P,d:ZK-ODS,c:POL},
  {n:'SDW: Szafa dół: wieniec górny',layer:'Półki',x:XT0+P,y:YP-P,z:ODS,w:WT,h:P,d:ZK-ODS,c:POL},
  {n:'SDT: Szafa dół: tył',layer:'Ścianki tylne',x:XT0+P,y:YN+P,z:ODS,w:WT,h:YP-P-(YN+P),d:P,c:TYL,o:0.9},
  {n:'SDP-1: Szafa dół: półka stała (495, nad szufladą)',layer:'Półki',x:XT0+P,y:YN+P+300,z:ODS+P,w:WT,h:P,d:ZK-ODS-P,c:POL},
  {n:'SDP-2: Szafa dół: półka stała (813)',layer:'Półki',x:XT0+P,y:YN+P+300+P+300,z:ODS+P,w:WT,h:P,d:ZK-ODS-P,c:POL},
  {t:'cyl3',n:'Drążek na kurtki Ø25 (oś 2093, 50 pod wieńcem)',layer:'Wyposażenie',ax:'x',px:(XT0+XT1)/2,py:YP-P-50,pz:(ODS+P+ZK)/2,r:12.5,len:WT,c:0x9aa5ad},
  {n:'Szuflada wewnętrzna (za drzwiami; dystans 20 od boku z zawiasami; prowadnice 500)',layer:'Szuflady (skrzynki)',x:XT0+P+13,y:YN+P+15,z:ODS+P+10,w:WT-26-20,h:200,d:500,c:0xc9a227,o:0.45},
  {n:'F4: Szafa dół (554 × 1982,5), zawiasy po prawej, TIP-ON',layer:'Fronty',x:XT0+1.5,y:YN,z:ZK,w:XT1-XT0-3,h:YP-1.5-YN,d:P,c:FR,o:0.55},

  /* ===== Szafa wysoka, część górna SG: bez półki ===== */
  {n:'SGB-1: Szafa góra: bok lewy',layer:'Ścianki boczne',x:XT0,y:YP,z:ODS,w:P,h:YT-YP,d:ZK-ODS,c:BOK},
  {n:'SGB-2: Szafa góra: bok prawy (przy pionie)',layer:'Ścianki boczne',x:XT1-P,y:YP,z:ODS,w:P,h:YT-YP,d:ZK-ODS,c:BOK},
  {n:'SGD: Szafa góra: dno',layer:'Półki',x:XT0+P,y:YP,z:ODS,w:WT,h:P,d:ZK-ODS,c:POL},
  {n:'SGW: Szafa góra: wieniec górny',layer:'Półki',x:XT0+P,y:YT-P,z:ODS,w:WT,h:P,d:ZK-ODS,c:POL},
  {n:'SGT: Szafa góra: tył',layer:'Ścianki tylne',x:XT0+P,y:YP+P,z:ODS,w:WT,h:YT-YP-2*P,d:P,c:TYL,o:0.9},
  {n:'F5: Szafa góra (554 × 498,5), zawiasy po prawej, TIP-ON',layer:'Fronty',x:XT0+1.5,y:YP+1.5,z:ZK,w:XT1-XT0-3,h:YT-YP-1.5,d:P,c:FR,o:0.55},

  /* ===== Zaślepka na czole pionu: przyklejona, od podłogi do sufitu, otwory na kabel domofonu i pod włącznik ===== */
  {n:'F6: Zaślepka na czole pionu (427,5 × 2661), klejona, bez zawiasów',layer:'Fronty',x:XZ0,y:0,z:ZK,w:XZ1-XZ0,h:YT,d:P,c:FR,o:0.55},
  {t:'cyl',n:'Otwór Ø60 na kabel domofonu w zaślepce (DF1, DF2)',layer:'Otwory w zaślepce',cx:XO+A+DF1,cy:DF2,z:ZK-0.5,r:DF3,len:P+1,c:0x15181b},
  {t:'cyl',n:'Otwór pod dystans włącznika w zaślepce (WL1, WL2; średnica wg dystansu)',layer:'Otwory w zaślepce',cx:XO+A+WL1,cy:WL2,z:ZK-0.5,r:34,len:P+1,c:0x15181b},
  {n:'Domofon na zaślepce (DF4, DF5; 125 × 165 założone)',layer:'Osprzęt',x:XO+A+DF4,y:DF5,z:ZF,w:125,h:165,d:25,c:0xf4f4f4},
  {n:'Włącznik światła na zaślepce (WL1, WL2; ramka ok. '+WL3+')',layer:'Osprzęt',x:XO+A+WL1-WL3/2,y:WL2-WL3/2,z:ZF,w:WL3,h:WL3,d:12,c:0xc8a46a}
];

/* zawiasy: CLIP top bez sprężyny + TIP-ON (komponenty.md) */
ITEMS=ITEMS
  .concat(zawiasyN('nad szezlongiem',XS0+1.5,YC+1.5,XS1-XS0-3,YP-1.5-(YC+1.5),'lewa',4,ZN))
  .concat(zawiasyN('pawlacz',XS0+1.5,YP+1.5,XS1-XS0-3,YT-YP-1.5,'lewa',2,ZK))
  .concat(zawiasyN('szafa dół',XT0+1.5,YN,XT1-XT0-3,YP-1.5-YN,'prawa',4,ZK))
  .concat(zawiasyN('szafa góra',XT0+1.5,YP+1.5,XT1-XT0-3,YT-YP-1.5,'prawa',2,ZK));

return {
  title:'Przedpokój 3D',
  room:{W:W,D:DD,H:H},
  wallThickness:100,
  openings:[
    {wall:'tyl',pos:XO-DR1-2*DR5,w:DR1+2*DR5,y:0,h:DR2+DR5},   /* D2 (łazienka), w świetle ok. skrzydło + szczeliny */
    {wall:'prawa',pos:B+OC,w:DMW,y:0,h:DMH}                  /* DM1 (wejście), wymiar w świetle założony */
  ],
  views:{iso:[3.9,2.7,4.3],front:[1.5,1.4,5.0],top:[1.5,5.8,1.1],left:[-3.2,1.5,1.0]},
  conceptLayers:[],
  hiddenLayers:['Szuflady (skrzynki)'],
  fixedLayers:['Pion','Osprzęt'],
  boardLayers:['Półki','Ścianki boczne','Ścianki tylne','Fronty'],
  boardColor:{hex:0xeeece5,label:'fronty na razie białe (kolor do decyzji)'},
  variants:[],
  items:ITEMS
};
})();
