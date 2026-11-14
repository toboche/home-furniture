/* ========================================================================
   KUCHNIA: DANE MODELU 3D (wszystko w milimetrach)
   Ściana tylna (z = 0) = ściana główna z płytkami, zlewem i płytą. Ściana lewa (x = 0) = ściana wnęki przy słupku
   z piekarnikiem. Po prawej ścianka (pion) na x = A, głęboka na L; dalej pokój jest umowny.
   Układ: X od ściany lewej ku ściance, Y od podłogi w górę, Z od ściany głównej w głąb kuchni.
   Wymiary z pomiary.md. Opis formatu ITEMS: wspolne/STRUKTURA.md, punkt 4.
   Projektujemy: półkę z LED na płytkach (P1, P3), szafkę okapową SO z okapem DUO 55 i frontem F1,
   wąską otwartą szafkę WS z zamkniętą skrzynką na rurę okapu. Reszta kuchni istnieje (warstwa „Kuchnia istniejąca”).
   ======================================================================== */
var HF_MODEL=(function(){
'use strict';
/* pomiary (pomiary.md) */
var A=3208;            /* ściana główna: narożnik → ścianka */
var C=911;             /* góra blatu */
var D=600;             /* pas płytek */
var E=257, F=590;      /* płyta grzewcza: ścianka → prawa krawędź, szerokość */
var H=754;             /* blat → dno szafek górnych nad wnęką */
var I=624;             /* szafki górne nad wnęką: głębokość wzdłuż ściany głównej */
var J=805;             /* wnęka: narożnik → bok słupka */
var K=629;             /* głębokość blatu */
var L=657;             /* głębokość ścianki */
var M=1169;            /* góra płytek → sufit */
var ZA1=356, ZA2=487;  /* przewód okapu: od ścianki, od sufitu */
var RU=130, RU2=32, RU3=38;      /* rura okapu w ściance: średnica zewnętrzna, od ściany głównej, od sufitu */
var KR=130, KR2=323, KR3=175;    /* otwór wentylacji grawitacyjnej w ściance */

/* założenia i decyzje (ustalenia.md) */
var P=18, PP=36;       /* płyta korpusów, płyta półki z LED */
var YP=C+D;            /* góra płytek = dół półki i szafek: 1511 */
var YS=YP+M;           /* sufit: 2680 */
var LUZS=2;            /* luz pod sufitem (2026-11-14) */
var YT=YS-LUZS;        /* góra korpusów: 2678 */
var GK=300;            /* głębokość korpusów SO i WS (kratka: wolne do 303) */
var XH=A-E-F/2;        /* oś płyty grzewczej: 2656 */
var SOW=552;           /* szafka okapowa: 516 w świetle (okap A + 2) */
var XSO=XH-SOW/2;      /* 2380 */
var XWS=XSO+SOW;       /* 2932 */
var LUZP=2;            /* ZAŁOŻENIE: luz wąskiej szafki do ścianki */
var XWE=A-LUZP;        /* prawy bok wąskiej szafki: 3206 (szerokość 274) */
var ZRU=RU2+RU/2;      /* oś rury okapu od ściany głównej: 97 */
var YRU=YS-RU3-RU/2;   /* oś rury okapu: 2577 */
var YSK=YS-RU3-RU-10;  /* góra dna skrzynki na rurę (10 pod rurą): 2502 */
var ZWY=GK-250+93+75;  /* ZAŁOŻENIE: oś wylotu okapu od ściany głównej (korpus okapu dosunięty do przodu): 218 */
var ZPI=ZRU+12.5;      /* oś pionu Ø150 (redukcja mimośrodowa: +12,5 od osi Ø125): 109,5 */
var YRD=2400;          /* ZAŁOŻENIE: dół redukcji 150/125 (pod kolanem 90°) */
var ZSK=RU2+RU+10;     /* tył zaślepki skrzynki (10 przed rurą): 172 */
var YSOP=2150;         /* ZAŁOŻENIE: półka nad okapem (dół), pod nią redukcja i przesunięcie rury do tyłu */
var NPW=2;             /* półki w wąskiej szafce (równe przegrody; 2026-11-14: 3 → 2) */
var LP1=J-2;           /* półka P1 wzdłuż ściany lewej: 803 */
var GP1=400, GP3=200;  /* głębokości półek */

var BOK=0xcdbb95, TYL=0x9c8b6e, POL=0xe6d7b8, FR=0x2f9e8f, IST=0x8a6f55, LED=0xffd66b, RURA=0xb8bcc2;

/* zawiasy: środek puszki 22,5 od krawędzi frontu, skrajne 100 od końców, pozostałe równo */
function zawiasy(nazwa,fx,fy,fw,fh,strona,n,zt){
  var out=[],x=(strona==='lewa')?fx+5:fx+fw-40;
  for(var i=0;i<n;i++){
    var cy=fy+100+i*(fh-200)/(n-1);
    out.push({n:'Zawias: '+nazwa+' ('+strona+')',layer:'Zawiasy',x:x,y:cy-17.5,z:zt+1,w:35,h:35,d:11,c:0x2b3034});
  }
  return out;
}

var ITEMS=[];
function add(a){ITEMS.push.apply(ITEMS,a);}

/* ---- otoczenie: ścianka, istniejąca kuchnia, instalacje ---- */
add([
  {n:'Ścianka (pion)',layer:'Ścianka',x:A,y:0,z:0,w:300,h:YS,d:L,c:0xd9d4cc},
  {n:'Blat (istniejący)',layer:'Kuchnia istniejąca',x:0,y:C-38,z:0,w:A,h:38,d:K,c:0xe7e1d6},
  {n:'Blat we wnęce (istniejący)',layer:'Kuchnia istniejąca',x:0,y:C-38,z:K,w:I,h:38,d:J-K,c:0xe7e1d6},
  {n:'Szafki dolne (istniejące)',layer:'Kuchnia istniejąca',x:I,y:0,z:0,w:A-I,h:C-38,d:K-20,c:IST,o:0.5},
  {n:'Szafki dolne we wnęce (istniejące)',layer:'Kuchnia istniejąca',x:0,y:0,z:0,w:I,h:C-38,d:J-20,c:IST,o:0.5},
  {n:'Pas płytek (istniejący)',layer:'Kuchnia istniejąca',x:I,y:C,z:0,w:A-I,h:D,d:8,c:0xf2f0ea},
  {n:'Pas płytek we wnęce (istniejący)',layer:'Kuchnia istniejąca',x:0,y:C,z:0,w:8,h:D,d:J,c:0xf2f0ea},
  {n:'Szafki górne nad wnęką (istniejące)',layer:'Kuchnia istniejąca',x:0,y:C+H,z:0,w:I,h:YS-C-H,d:J,c:IST,o:0.5},
  {n:'Słupek z piekarnikiem (istniejący, szerokość umowna)',layer:'Kuchnia istniejąca',x:0,y:0,z:J,w:I,h:YS,d:600,c:IST,o:0.5},
  {n:'Płyta grzewcza (istniejąca)',layer:'Kuchnia istniejąca',x:A-E-F,y:C,z:30,w:F,h:6,d:520,c:0x1d1d1f},
  {n:'Przewód zasilający okap (ZA1, ZA2)',layer:'Instalacje',x:A-ZA1-10,y:YS-ZA2-10,z:0,w:20,h:20,d:30,c:0xd85a30},
  {n:'Kabel LED 24 V (przesuwny)',layer:'Instalacje',x:0,y:YP+PP/2-5,z:J-60,w:30,h:10,d:10,c:0xd85a30},
  {t:'cyl3',n:'Rura okapu w ściance (RU, Ø125 wewn.)',layer:'Instalacje',ax:'x',px:A+40,py:YRU,pz:ZRU,r:RU/2,len:80,c:RURA},
  {t:'cyl3',n:'Otwór wentylacji grawitacyjnej z kratką (KR, nie zasłaniać)',layer:'Instalacje',ax:'x',px:A-4,py:YS-KR3-KR/2,pz:KR2+KR/2,r:KR/2+20,len:8,c:0xf0f0f0}
]);

/* ---- półka z LED na płytkach (płyta 36, z meble.pl, oklejona) ---- */
add([
  {n:'P1: Półka LED, ściana lewa (803 × 400)',layer:'Półka LED',x:0,y:YP,z:0,w:GP1,h:PP,d:LP1,c:POL},
  {n:'P3: Półka LED, ściana główna (1980 × 200)',layer:'Półka LED',x:GP1,y:YP,z:0,w:XSO-GP1,h:PP,d:GP3,c:POL},
  {n:'Profil LED pod P1',layer:'LED',x:GP1-60,y:YP-1,z:GP3-60,w:12,h:8,d:LP1-GP3+40,c:LED},
  {n:'Profil LED pod P3',layer:'LED',x:GP1-60,y:YP-1,z:GP3-60,w:XSO-GP1+40,h:8,d:12,c:LED}
]);

/* ---- szafka okapowa SO: bez dna (okap między bokami), plecy między bokami, wieniec, półka nad okapem ---- */
add([
  {n:'SOB-1: SO: bok lewy',layer:'Ścianki boczne',x:XSO,y:YP,z:0,w:P,h:YT-YP,d:GK,c:BOK},
  {n:'SOB-2: SO: bok prawy',layer:'Ścianki boczne',x:XWS-P,y:YP,z:0,w:P,h:YT-YP,d:GK,c:BOK},
  {n:'SOT: SO: tył',layer:'Ścianki tylne',x:XSO+P,y:YP,z:0,w:SOW-2*P,h:YT-YP,d:P,c:TYL},
  {n:'SOW: SO: wieniec górny',layer:'Półki',x:XSO+P,y:YT-P,z:P,w:SOW-2*P,h:P,d:GK-P,c:POL},
  {n:'SOP: SO: półka nad okapem (otwór na rurę)',layer:'Półki',x:XSO+P,y:YSOP,z:P,w:SOW-2*P,h:P,d:GK-P,c:POL},
  {n:'F1: Front szafki okapowej (549 × 1164)',layer:'Fronty',x:XSO+1.5,y:YP+1.5,z:GK,w:SOW-3,h:YT-YP-3,d:P,c:FR,o:0.55}
]);
add(zawiasy('F1',XSO+1.5,YP+1.5,SOW-3,YT-YP-3,'prawa',3,GK));

/* okap DUO 55: szkło pod korpusem szafki, korpus 514 × 250 × 263 dosunięty do przodu (ZAŁOŻENIE) */
add([
  {n:'Okap DUO 55: szkło 550 × 290',layer:'Okap',x:XH-275,y:YP-4,z:GK-290,w:550,h:4,d:290,c:0x26282b},
  {n:'Okap DUO 55: korpus 514 × 250 × 263',layer:'Okap',x:XH-257,y:YP,z:GK-250,w:514,h:263,d:250,c:0x6f7377},
  {t:'cyl3',n:'Wylot okapu Ø150 + łącznik, rura spiro Ø150',layer:'Rura okapu',ax:'y',px:XH,py:YP+263+60,pz:ZWY,r:75,len:120,c:RURA},
  {t:'cyl3',n:'Przesunięcie do tyłu: 2 kolana 45° Ø150 (schemat), pod półką SOP',layer:'Rura okapu',ax:'z',px:XH,py:YP+263+230,pz:(ZWY+ZPI)/2,r:75,len:ZWY-ZPI+150,c:RURA},
  {t:'cyl3',n:'Rura spiro Ø150: pion przy ścianie (z matą akustyczną)',layer:'Rura okapu',ax:'y',px:XH,py:(YP+263+230+YRD)/2,pz:ZPI,r:75,len:YRD-(YP+263+230),c:RURA},
  {t:'cyl3',n:'Redukcja mimośrodowa 150/125 (spiro, uszczelka), płaską stroną do ściany głównej',layer:'Rura okapu',ax:'y',px:XH,py:YRD+50,pz:ZRU+6,r:69,len:100,c:RURA},
  {t:'cyl3',n:'Rura spiro Ø125: kolano 90° tłoczone pod sufitem',layer:'Rura okapu',ax:'y',px:XH,py:(YRD+100+YRU)/2,pz:ZRU,r:62.5,len:YRU-YRD-100,c:RURA},
  {t:'cyl3',n:'Rura Ø125 spiro: poziomo do ścianki, przez SOB-2, WSB-1, WSB-2',layer:'Rura okapu',ax:'x',px:(XH+A)/2,py:YRU,pz:ZRU,r:62.5,len:A-XH,c:RURA}
]);

/* ---- wąska szafka WS: bez frontu, dno, wieniec, 3 półki, skrzynka na rurę cofnięta (płytka półka przed nią) ---- */
var ywn=YP+P, ysd=YSK-P, prz=(ysd-ywn-NPW*P)/(NPW+1);
add([
  {n:'WSB-1: WS: bok lewy',layer:'Ścianki boczne',x:XWS,y:YP,z:0,w:P,h:YT-YP,d:GK,c:BOK},
  {n:'WSB-2: WS: bok prawy (przy ściance)',layer:'Ścianki boczne',x:XWE-P,y:YP,z:0,w:P,h:YT-YP,d:GK,c:BOK},
  {n:'WST: WS: tył',layer:'Ścianki tylne',x:XWS+P,y:YP,z:0,w:XWE-XWS-2*P,h:YT-YP,d:P,c:TYL},
  {n:'WSD: WS: dno',layer:'Półki',x:XWS+P,y:YP,z:P,w:XWE-XWS-2*P,h:P,d:GK-P,c:POL},
  {n:'WSW: WS: wieniec górny',layer:'Półki',x:XWS+P,y:YT-P,z:P,w:XWE-XWS-2*P,h:P,d:GK-P,c:POL},
  {n:'WSS: WS: dno skrzynki na rurę (płytka półka przed zaślepką)',layer:'Półki',x:XWS+P,y:ysd,z:P,w:XWE-XWS-2*P,h:P,d:GK-P,c:POL},
  {n:'WSZ: WS: zaślepka skrzynki na rurę',layer:'Ścianki tylne',x:XWS+P,y:YSK,z:ZSK,w:XWE-XWS-2*P,h:YT-P-YSK,d:P,c:TYL}
]);
for(var k=1;k<=NPW;k++){
  ITEMS.push({n:'WSP-'+k+': WS: półka',layer:'Półki',x:XWS+P,y:ywn+k*prz+(k-1)*P,z:P,w:XWE-XWS-2*P,h:P,d:GK-P,c:POL});
}

return {
  title:'Kuchnia 3D: półka LED, szafka okapowa, wąska szafka',
  room:{W:A+700,D:2200,H:YS},
  wallThickness:100,
  openings:[],
  views:{iso:[4.8,2.9,4.2],front:[2.0,2.0,4.6],top:[2.0,6.5,1.4],left:[-2.6,2.0,1.2]},
  conceptLayers:[],
  hiddenLayers:[],
  fixedLayers:['Ścianka','Kuchnia istniejąca','Instalacje'],
  boardLayers:['Półki','Ścianki boczne','Ścianki tylne','Fronty','Półka LED'],
  boardColor:{hex:0x8b6a4f,label:'docelowy: Egger H3710 ST12 Orzech Carini naturalny'},
  variants:[],
  items:ITEMS
};
})();
