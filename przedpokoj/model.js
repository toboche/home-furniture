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
var HF=2668;           /* wysokość w linii frontów, najmniejsza (2668–2671) */
var OC=120;            /* od krawędzi 2 do ościeżnicy DM1 */
var DR1=800, DR2=2030, DR5=3;   /* D2: szerokość i wysokość skrzydła, szczelina od strony szafy */
var D=187, E=350, G=933, K=1000, RZ1=10;   /* rozdzielnica: od szczeliny D2, szerokość z ramką, dół od podłogi, wysokość, wysięg drzwiczek */
var DF1=245, DF2=1474, DF3=30;  /* otwór na kabel domofonu: środek od krawędzi 1, od podłogi, promień */
var DF4=183, DF5=1365;          /* domofon: lewy dolny róg od krawędzi 1, od podłogi */
var WL1=298, WL2=1214, WL3=70;  /* włącznik: środek od krawędzi 1, od podłogi, ramka (ok.) */

/* założenia i decyzje (ustalenia.md) */
var XO=1000;           /* położenie szczeliny D2 w modelu (umowny kawałek przedpokoju na lewo od D2) */
var P=18;              /* płyta */
var LUZG=1;            /* luz pod sufitem: montaż od góry, górne korpusy dopasowane do sufitu (2026-11-12) */
var LUZK=2;            /* luz między korpusem górnym a dolnym (dolne wsuwane pod zamontowane górne) */
var ODS=2;             /* odsunięcie korpusów 775 od ściany: front w płaszczyźnie zaślepki (u góry dystans do 8) */
var ZK=B;              /* przód korpusów szafy i pawlacza: 777 (korpus 775) */
var ZF=ZK+P;           /* płaszczyzna frontów i zaślepki: 795 */
var YT=H-LUZG;         /* góra korpusów: 2663 */
var YFT=HF-LUZG;        /* góra frontów górnych i zaślepki: 2667 (fronty równo od sufitu w linii frontów) */
var YP=YT-500;         /* podział góra / dół (dół pawlacza i szafy górnej): 2163 */
var YD=YP-LUZK;        /* góra korpusu szafy dół: 2161 */
var XS0=XO+20;         /* szezlong: 20 od szczeliny D2 */
var XS1=XS0+520;       /* szezlong szerokość 520 → 540 */
var XT0=XS1;           /* szafa wysoka od boku szezlonga */
var XT1=XO+A;          /* przylega do boku pionu: 1100 (szerokość 560) */
var ZS=ZF;             /* szezlong: front w linii pozostałych frontów (795) */
var YN=177;            /* wnęka na buty: 0–177 */
var YB=412, YS=430, YC=460;     /* szezlong: spód blatu, góra blatu, góra poduszki (30) */
var ZN=80;             /* szafka nad szezlongiem: korpus 80 (zawiasy i TIP-ON), lico frontu 98 */
var XZ0=XO+A+1.5;      /* zaślepka: 3 mm od frontu szafy (zaczyna się 1,5 za narożnikiem pionu) */
var XZ1=XO+A+C-2;      /* zaślepka: 2 mm od ściany z DM1 */
var DMW=900, DMH=2000; /* DM1 w świetle (ZAŁOŻENIE, nominalnie 90/200) */

var W=XO+A+C, DD=B+F;  /* umowny pokój: 2528 × 2012 */
var WB=XS1-XS0-2*P;    /* wnętrze szafki nad szezlongiem i pawlacza: 484 */
var XW=XS1;           /* styk den szezlonga i szafy nad wnęką (x 540): wspólna wnęka bez boków pośrodku */
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

var BOK=0xcdbb95, TYL=0x9c8b6e, POL=0xe6d7b8, FR=0x2f9e8f, SKR=0xc9a227;

/* Skrzynki szuflad Blum MOVENTO (prowadnice pod szufladą, NL 700): płyta 16 (boki MOVENTO najwyżej 16),
   szerokość wewnętrzna LW − 42 (zewnętrzna LW − 10, po 5 luzu), długość NL − 10 = 690, dno 13 nad dolną krawędzią boków,
   dno między bokami na całą długość, czoło i tył skrzynki między bokami, stoją na dnie. Formatki 16 mm (reguly.GRUBOSCI). */
var G16=16, REC=13, SKL=690;
function skrzynka(kod,opis,xl,lw,yb,h,dyst,cof){
  /* dyst: dystans pod prawą prowadnicą (szuflady wewnętrzne, od strony zawiasów); cof: cofnięcie skrzynki za przód korpusu */
  dyst=dyst||0; cof=cof||0;
  var x0=xl+5, ow=lw-dyst-10, sk=ow-2*G16, z0=ZK-cof-SKL;
  return [
    {n:kod+'B-1: '+opis+': bok lewy',layer:'Skrzynki szuflad',x:x0,y:yb,z:z0,w:G16,h:h,d:SKL,c:SKR},
    {n:kod+'B-2: '+opis+': bok prawy',layer:'Skrzynki szuflad',x:x0+ow-G16,y:yb,z:z0,w:G16,h:h,d:SKL,c:SKR},
    {n:kod+'D: '+opis+': dno',layer:'Skrzynki szuflad',x:x0+G16,y:yb+REC,z:z0,w:sk,h:G16,d:SKL,c:SKR},
    {n:kod+'C-1: '+opis+': czoło skrzynki',layer:'Skrzynki szuflad',x:x0+G16,y:yb+REC+G16,z:z0+SKL-G16,w:sk,h:h-REC-G16,d:G16,c:SKR},
    {n:kod+'C-2: '+opis+': tył skrzynki',layer:'Skrzynki szuflad',x:x0+G16,y:yb+REC+G16,z:z0,w:sk,h:h-REC-G16,d:G16,c:SKR}
  ];
}
/* szuflady wewnętrzne szafy (za jednymi drzwiami F4) */
var YS0=YN+P, SL=300;                       /* 3 przedziały po 300 od dna szafy: 195–495, 495–795, 795–1095 (2026-11-13) */
var HSK=250;                                /* wysokość boku skrzynek S1–S3 (3 nad dnem przedziału, 47 luzu nad skrzynką) */
var YPK=YS0+3*SL+P;                         /* góra półki nad szufladami: 1113 */
var DYS=20, COF=25;                         /* dystans pod prowadnicą od strony zawiasów F4; cofnięcie skrzynek za przód korpusu */

var ITEMS=[
  /* ===== Pomieszczenie ===== */
  {n:'Pion EI60 (wysięg '+B+' przy podłodze, '+BG+' przy suficie; czoło '+C+')',layer:'Pion',x:XO+A,y:0,z:0,w:C,h:H,d:B,c:0xd9d4ca},
  {n:'Rozdzielnica z ramką ('+E+' × '+K+', od '+G+'; drzwiczki wystają '+RZ1+', zawiasy po prawej)',layer:'Osprzęt',x:XO+D,y:G,z:0,w:E,h:K,d:RZ1,c:0xb0b4b8},
  {n:'Listwa przypodłogowa L 40 × 16 (zostaje lub do zdjęcia)',layer:'Osprzęt',x:XO-200,y:0,z:0,w:200+A,h:40,d:16,c:0xf4f4f4,o:0.8},

  /* ===== Szezlong SZ (x 20–540 od szczeliny D2), front w linii frontów: wnęka na buty, szuflada TIP-ON BLUMOTION, blat, poduszka.
     Prawy bok SZBP stoi na dnie SZD (bez części we wnęce). Wnęka pod szezlongiem i szafą jest wspólna (od SZBL do SDBP);
     dna SZD i SDD stykają się czołami na x 540: 2 kołki Ø8, 2 płaskowniki stalowe od spodu, 2 nóżki regulowane pod stykiem. ===== */
  {n:'SZBL: Szezlong: bok lewy (od D2, do podłogi)',layer:'Ścianki boczne',x:XS0,y:0,z:ODS,w:P,h:YB,d:ZK-ODS,c:BOK},
  {n:'SZBP: Szezlong: bok prawy (na dnie SZD, bez części we wnęce)',layer:'Ścianki boczne',x:XS1-P,y:YN+P,z:ODS,w:P,h:YB-YN-P,d:ZK-ODS,c:BOK},
  {n:'SZW: Szezlong: blat (pod poduszką)',layer:'Półki',x:XS0,y:YB,z:ODS,w:XS1-XS0,h:P,d:ZK-ODS,c:POL},
  {n:'SZD: Szezlong: dno szuflady nad wnęką (pod prawym bokiem, do styku z SDD)',layer:'Półki',x:XS0+P,y:YN,z:ODS,w:XW-XS0-P,h:P,d:ZK-ODS,c:POL},
  {n:'SZT: Szezlong: tył',layer:'Ścianki tylne',x:XS0+P,y:YN+P,z:ODS,w:WB,h:YB-YN-P,d:P,c:TYL,o:0.9},
  {n:'Płaskownik stalowy 200 × 30 × 4 pod stykiem SZD/SDD (z 60)',layer:'Łączniki i nóżki',x:XW-100,y:YN-4,z:60,w:200,h:4,d:30,c:0x9aa5ad},
  {n:'Płaskownik stalowy 200 × 30 × 4 pod stykiem SZD/SDD (z 690)',layer:'Łączniki i nóżki',x:XW-100,y:YN-4,z:690,w:200,h:4,d:30,c:0x9aa5ad},
  {t:'cyl3',n:'Nóżka regulowana pod stykiem den (tył, z 100)',layer:'Łączniki i nóżki',ax:'y',px:XW,py:(YN-4)/2,pz:100,r:15,len:YN-4,c:0x6b7b8c},
  {t:'cyl3',n:'Nóżka regulowana pod stykiem den (przód, 150 za frontem korpusu)',layer:'Łączniki i nóżki',ax:'y',px:XW,py:(YN-4)/2,pz:ZK-150,r:15,len:YN-4,c:0x6b7b8c},
  {n:'F1: Szuflada szezlonga (517 × 253), TIP-ON BLUMOTION',layer:'Fronty',x:XS0+1.5,y:YN,z:ZK,w:XS1-XS0-3,h:YS-YN,d:P,c:FR,o:0.55},
  {n:'Poduszka siedziska (30)',layer:'Tapicerka',x:XS0,y:YS,z:ZN+P,w:XS1-XS0,h:YC-YS,d:ZF-ZN-P,c:0x2b2b2b},

  /* ===== Szafka nad szezlongiem NS: korpus 80, bez tyłu (rozdzielnica), drzwi TIP-ON z zawiasami od D2 ===== */
  {n:'NSB-1: Nad szezlongiem: bok lewy',layer:'Ścianki boczne',x:XS0,y:YS+LUZK,z:0,w:P,h:YP-YS-LUZK,d:ZN,c:BOK},
  {n:'NSB-2: Nad szezlongiem: bok prawy',layer:'Ścianki boczne',x:XS1-P,y:YS+LUZK,z:0,w:P,h:YP-YS-LUZK,d:ZN,c:BOK},
  {n:'NSD: Nad szezlongiem: dno',layer:'Półki',x:XS0+P,y:YS+LUZK,z:0,w:WB,h:P,d:ZN,c:POL},
  {n:'NSW: Nad szezlongiem: wieniec',layer:'Półki',x:XS0+P,y:YP-P,z:0,w:WB,h:P,d:ZN,c:POL},
  {n:'F2: Drzwi nad szezlongiem (517 × 1700), zawiasy od D2, TIP-ON',layer:'Fronty',x:XS0+1.5,y:YC+1.5,z:ZN,w:XS1-XS0-3,h:YP-1.5-(YC+1.5),d:P,c:FR,o:0.55},

  /* ===== Pawlacz PW nad szezlongiem: 500 od sufitu, front w linii szafy ===== */
  {n:'PWB-1: Pawlacz: bok lewy',layer:'Ścianki boczne',x:XS0,y:YP,z:ODS,w:P,h:YT-YP,d:ZK-ODS,c:BOK},
  {n:'PWB-2: Pawlacz: bok prawy',layer:'Ścianki boczne',x:XS1-P,y:YP,z:ODS,w:P,h:YT-YP,d:ZK-ODS,c:BOK},
  {n:'PWD: Pawlacz: dno',layer:'Półki',x:XS0+P,y:YP,z:ODS,w:WB,h:P,d:ZK-ODS,c:POL},
  {n:'PWW: Pawlacz: wieniec górny',layer:'Półki',x:XS0+P,y:YT-P,z:ODS,w:WB,h:P,d:ZK-ODS,c:POL},
  {n:'PWT: Pawlacz: tył',layer:'Ścianki tylne',x:XS0+P,y:YP+P,z:ODS,w:WB,h:YT-YP-2*P,d:P,c:TYL,o:0.9},
  {n:'F3: Pawlacz (517 × 502,5; góra 1 pod sufitem w linii frontów), zawiasy od D2, TIP-ON',layer:'Fronty',x:XS0+1.5,y:YP+1.5,z:ZK,w:XS1-XS0-3,h:YFT-YP-1.5,d:P,c:FR,o:0.55},

  /* ===== Szafa wysoka, część dolna SD: wnęka 177, półki 300 (z szufladą) i 300, drążek na kurtki ===== */
  {n:'SDBL: Szafa dół: bok lewy (na dnie SDD, bez części we wnęce)',layer:'Ścianki boczne',x:XT0,y:YN+P,z:ODS,w:P,h:YD-YN-P,d:ZK-ODS,c:BOK},
  {n:'SDBP: Szafa dół: bok prawy (przy pionie, do podłogi)',layer:'Ścianki boczne',x:XT1-P,y:0,z:ODS,w:P,h:YD,d:ZK-ODS,c:BOK},
  {n:'SDD: Szafa dół: dno nad wnęką (pod lewym bokiem, od styku z SZD)',layer:'Półki',x:XW,y:YN,z:ODS,w:XT1-P-XW,h:P,d:ZK-ODS,c:POL},
  {n:'SDW: Szafa dół: wieniec górny',layer:'Półki',x:XT0+P,y:YD-P,z:ODS,w:WT,h:P,d:ZK-ODS,c:POL},
  {n:'SDT: Szafa dół: tył',layer:'Ścianki tylne',x:XT0+P,y:YN+P,z:ODS,w:WT,h:YD-P-(YN+P),d:P,c:TYL,o:0.9},
  {n:'SDP: Szafa dół: półka stała nad szufladami (1095 do 1113)',layer:'Półki',x:XT0+P,y:YPK-P,z:ODS+P,w:WT,h:P,d:ZK-ODS-P,c:POL},
  {t:'cyl3',n:'Drążek na kurtki Ø25 (oś 2093, 50 pod wieńcem)',layer:'Wyposażenie',ax:'x',px:(XT0+XT1)/2,py:YD-P-50,pz:(ODS+P+ZK)/2,r:12.5,len:WT,c:0x9aa5ad},
  {n:'F4: Szafa dół: jedne drzwi (557 × 1984,5), szuflady wewnętrzne za nimi, zawiasy po prawej, TIP-ON',layer:'Fronty',x:XT0+1.5,y:YN,z:ZK,w:XT1-XT0-3,h:YP-1.5-YN,d:P,c:FR,o:0.55},

  /* ===== Szafa wysoka, część górna SG: bez półki ===== */
  {n:'SGB-1: Szafa góra: bok lewy',layer:'Ścianki boczne',x:XT0,y:YP,z:ODS,w:P,h:YT-YP,d:ZK-ODS,c:BOK},
  {n:'SGB-2: Szafa góra: bok prawy (przy pionie)',layer:'Ścianki boczne',x:XT1-P,y:YP,z:ODS,w:P,h:YT-YP,d:ZK-ODS,c:BOK},
  {n:'SGD: Szafa góra: dno',layer:'Półki',x:XT0+P,y:YP,z:ODS,w:WT,h:P,d:ZK-ODS,c:POL},
  {n:'SGW: Szafa góra: wieniec górny',layer:'Półki',x:XT0+P,y:YT-P,z:ODS,w:WT,h:P,d:ZK-ODS,c:POL},
  {n:'SGT: Szafa góra: tył',layer:'Ścianki tylne',x:XT0+P,y:YP+P,z:ODS,w:WT,h:YT-YP-2*P,d:P,c:TYL,o:0.9},
  {n:'F5: Szafa góra (557 × 502,5; góra 1 pod sufitem w linii frontów), zawiasy po prawej, TIP-ON',layer:'Fronty',x:XT0+1.5,y:YP+1.5,z:ZK,w:XT1-XT0-3,h:YFT-YP-1.5,d:P,c:FR,o:0.55},

  /* ===== Zaślepka na czole pionu: przyklejona, od podłogi do sufitu, otwory na kabel domofonu i pod włącznik ===== */
  {n:'F6: Zaślepka na czole pionu (424,5 × 2667), klejona, bez zawiasów',layer:'Fronty',x:XZ0,y:0,z:ZK,w:XZ1-XZ0,h:YFT,d:P,c:FR,o:0.55},
  {t:'cyl',n:'Otwór Ø60 na kabel domofonu w zaślepce (DF1, DF2)',layer:'Otwory w zaślepce',cx:XO+A+DF1,cy:DF2,z:ZK-0.5,r:DF3,len:P+1,c:0x15181b},
  {t:'cyl',n:'Otwór Ø60 pod dystans włącznika w zaślepce (WL1, WL2; średnica standardowej puszki podtynkowej)',layer:'Otwory w zaślepce',cx:XO+A+WL1,cy:WL2,z:ZK-0.5,r:30,len:P+1,c:0x15181b},
  {n:'Domofon na zaślepce (DF4, DF5; 125 × 165 założone)',layer:'Osprzęt',x:XO+A+DF4,y:DF5,z:ZF,w:125,h:165,d:25,c:0xf4f4f4},
  {n:'Włącznik światła na zaślepce (WL1, WL2; ramka ok. '+WL3+')',layer:'Osprzęt',x:XO+A+WL1-WL3/2,y:WL2-WL3/2,z:ZF,w:WL3,h:WL3,d:12,c:0xc8a46a}
];

/* skrzynki szuflad: szezlong SS; szafa: wewnętrzne S1, S2, S3 w przedziałach po 300 */
ITEMS=ITEMS
  .concat(skrzynka('SS','Szuflada szezlonga',XS0+P,WB,YN+P+3,200))
  .concat(skrzynka('S1','Szafa: szuflada wewnętrzna 1',XT0+P,WT,YS0+3,HSK,DYS,COF))
  .concat(skrzynka('S2','Szafa: szuflada wewnętrzna 2',XT0+P,WT,YS0+SL+3,HSK,DYS,COF))
  .concat(skrzynka('S3','Szafa: szuflada wewnętrzna 3',XT0+P,WT,YS0+2*SL+3,HSK,DYS,COF));

/* zawiasy: CLIP top bez sprężyny + TIP-ON (komponenty.md) */
ITEMS=ITEMS
  .concat(zawiasyN('nad szezlongiem',XS0+1.5,YC+1.5,XS1-XS0-3,YP-1.5-(YC+1.5),'lewa',4,ZN))
  .concat(zawiasyN('pawlacz',XS0+1.5,YP+1.5,XS1-XS0-3,YFT-YP-1.5,'lewa',2,ZK))
  .concat(zawiasyN('szafa dół',XT0+1.5,YN,XT1-XT0-3,YP-1.5-YN,'prawa',4,ZK))
  .concat(zawiasyN('szafa góra',XT0+1.5,YP+1.5,XT1-XT0-3,YFT-YP-1.5,'prawa',2,ZK));

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
  hiddenLayers:[],
  fixedLayers:['Pion','Osprzęt'],
  boardLayers:['Półki','Ścianki boczne','Ścianki tylne','Fronty','Skrzynki szuflad'],
  boardColor:{hex:0xeeece5,label:'fronty na razie białe (kolor do decyzji)'},
  variants:[],
  items:ITEMS
};
})();
