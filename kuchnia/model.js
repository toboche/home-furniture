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
var A=3206;            /* ściana główna: narożnik → ścianka (zmierzone 2026-11-19, było 3208) */
var C=911;             /* góra blatu */
var D=600;             /* pas płytek */
var E=257, F=590;      /* płyta grzewcza: ścianka → prawa krawędź, szerokość */
var H=754;             /* blat → dno szafek górnych nad wnęką */
var I=624;             /* szafki górne nad wnęką: głębokość wzdłuż ściany głównej */
var J=805;             /* wnęka: narożnik → bok słupka */
var K=629;             /* głębokość blatu */
var L=657;             /* głębokość ścianki */
var M=1156;            /* góra płytek → sufit: najniższy punkt (przy kratce, zmierzone 2026-11-19: 1156–1158; było 1169) */
var PLW=12;            /* płytki wystają przed ścianę 9–12 (zmierzone 2026-11-18): w modelu 12 */
var ZA1=356, ZA2=487;  /* przewód okapu: od ścianki, od sufitu */
var RU=130, RU2=32, RU3=38;      /* rura okapu w ściance: średnica zewnętrzna, od ściany głównej, od sufitu */
var KR=130, KR2=323, KR3=175;    /* otwór wentylacji grawitacyjnej w ściance */

/* założenia i decyzje (ustalenia.md) */
var P=18, PP=18;       /* płyta korpusów, płyta półki z LED (2026-11-15: 36 → 18) */
var YP=C+D;            /* góra płytek = dół półki i szafek: 1511 */
var YS=YP+M;           /* sufit: 2667 */
var LUZS=2;            /* luz pod sufitem (2026-11-14) */
var YT=YS-LUZS;        /* góra korpusów: 2665 */
var GK=300;            /* głębokość korpusu WS (kratka: wolne do 303) */
var GKS=GK+4;          /* głębokość korpusu SO: 304, kołnierz okapu (z 14–304) mija płytki wystające 9–12 (2026-11-18) */
var XH=A-E-F/2;        /* oś płyty grzewczej: 2654 */
var SOW=552;           /* szafka okapowa: 516 w świetle (okap A + 2) */
var XSO=XH-SOW/2;      /* 2378 */
var XWS=XSO+SOW;       /* 2930 */
var LUZP=2;            /* ZAŁOŻENIE: luz wąskiej szafki do ścianki */
var XWE=A-LUZP;        /* prawy bok wąskiej szafki: 3204 (szerokość 274) */
var ZRU=RU2+RU/2;      /* oś rury okapu od ściany głównej: 97 */
var YRU=YS-RU3-RU/2;   /* oś rury okapu: 2564 (RU5 = 988 od płytek) */
var YSK=YRU-75-10;     /* góra dna skrzynki na rurę (10 pod końcem Ø150 redukcji; 2026-11-16: było 2502): 2479 */
var OKW=513, OKG=253, OKH=265;  /* korpus okapu DUO 55 (rysunek techniczny) */
var OKF=19;            /* kołnierz wystaje przed lico przodu korpusu (zmierzone 2026-11-18; z nitami efektywnie 16,5–17) */
var OKZ=GKS-OKF-OKG;   /* tył korpusu: 32 (przód 285) */
var OKK=1.5;           /* grubość kołnierza (zmierzone 2026-11-18) */
var ZWY=GKS-290+49+75;  /* oś wylotu Ø150: 49 od tylnej krawędzi kołnierza do tylnej krawędzi wylotu (zmierzone 2026-11-18): 138 */
var YOK=YP+OKH;        /* góra korpusu okapu: 1776 */
var ZPI=ZRU+12.5;      /* oś pionu Ø150 (redukcja mimośrodowa: +12,5 od osi Ø125): 109,5 */
var RU4=115;           /* rura w ściance wystaje ze ścianki (zmierzone 2026-11-18): koniec na X 3091, w wąskiej szafce */
var LRD=120;           /* ZAŁOŻENIE: długość redukcji */
var XRD=A-RU4-LRD;     /* redukcja 150/125 w wąskiej szafce, wąskim końcem w rurze ze ściany: od 2971 */
var ZSK=195;           /* tył zaślepki skrzynki (10 przed końcem Ø150 redukcji, oś z 109,5; 2026-11-16: było 172) */
var YSOD=YOK+10;       /* półka wkładana tuż nad okapem (dół), 10 zapasu (2026-11-16): 1786 */
var YSOP=YSOD+P+300;   /* półka nad okapem na podpórkach od 2026-11-24 (dół): przegroda ok. 300 nad SOD (2026-11-16; było 2150): 2104 */
var SZT=2;             /* szczelina front F1 – korpus pod TIP-ON (domyślnie 2,0, min. 1,5; audyt v2 KU-04) */
var YZ1=1850;          /* dolny zawias F1: nad okapem i SOD (audyt v1 KU-02, wariant A, 2026-11-18) */
var YZ2=2210;          /* środkowy zawias F1: nad SOP (było 1950) */
var NPW=2;             /* półki w wąskiej szafce (równe przegrody; 2026-11-14: 3 → 2) */
var LP1=J-1;           /* półka P1 wzdłuż ściany lewej: 804 (2026-11-15: luz 2 → 1) */
var GP1=400, GP3=200;  /* głębokości półek */
/* Profil LED MasterLED wpuszczany 12 mm (2026-11-15): kołnierz 23,6, korpus 16,9, wys. 7 (korpus ok. 5,5 + kołnierz ok. 1,5).
   Rowek 17,2 × 6, 30,5–47,7 od krawędzi półki (2026-11-23, było 18,2 × 6 od 30; oś bez zmian), frezuje użytkownik (meble.pl nie robi wręgów zachodzących na siebie). */
var LRO=30.5, LRW=17.2, LRG=6, LKW=23.6, LKH=1.5;
var LRA=LRO+LRW/2;     /* oś rowka od krawędzi półki: 39,1 */
var ZLS=LP1-LRA;       /* oś profilu przy słupku (od ściany głównej) */
var PR=4;              /* pręty gwintowane M8 kl. 8.8 na kotwie chemicznej w betonie (2026-11-16; wcześniej wsporniki ukryte Ø10) */
var WB=80;             /* część pręta w betonie */
var WT=80;             /* część trzpienia w półce: 80 (decyzja użytkownika 2026-11-16) */

var BOK=0xcdbb95, TYL=0x9c8b6e, POL=0xe6d7b8, FR=0x2f9e8f, IST=0x8a6f55, LED=0xffd66b, RURA=0xb8bcc2;

/* zawiasy: środek puszki 22,5 od krawędzi frontu, skrajne 100 od końców, pozostałe równo */
function zawiasy(nazwa,fx,fy,fw,fh,strona,n,zt,ys){
  var out=[],x=(strona==='lewa')?fx+5:fx+fw-40;
  for(var i=0;i<n;i++){
    var cy=ys?ys[i]:fy+100+i*(fh-200)/(n-1);
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
  {n:'Pas płytek (istniejący, wystaje 9–12)',layer:'Kuchnia istniejąca',x:I,y:C,z:0,w:A-I,h:D,d:PLW,c:0xf2f0ea},
  {n:'Pas płytek we wnęce (istniejący, wystaje 9–12)',layer:'Kuchnia istniejąca',x:0,y:C,z:0,w:PLW,h:D,d:J,c:0xf2f0ea},
  {n:'Szafki górne nad wnęką (istniejące)',layer:'Kuchnia istniejąca',x:0,y:C+H,z:0,w:I,h:YS-C-H,d:J,c:IST,o:0.5},
  {n:'Słupek z piekarnikiem (istniejący, szerokość umowna)',layer:'Kuchnia istniejąca',x:0,y:0,z:J,w:I,h:YS,d:600,c:IST,o:0.5},
  {n:'Płyta grzewcza (istniejąca)',layer:'Kuchnia istniejąca',x:A-E-F,y:C,z:30,w:F,h:6,d:520,c:0x1d1d1f},
  {n:'Przewód zasilający okap (ZA1, ZA2)',layer:'Instalacje',x:A-ZA1-10,y:YS-ZA2-10,z:0,w:20,h:20,d:30,c:0xd85a30},
  {n:'Kabel LED 24 V, 3 żyły CCT (przesuwny, wprowadzany w rowek przy słupku)',layer:'Instalacje',x:0,y:YP,z:ZLS-5,w:30,h:10,d:10,c:0xd85a30},
  {t:'cyl3',n:'Rura okapu ze ścianki (RU, Ø125 wewn., wystaje 115)',layer:'Instalacje',ax:'x',px:A-RU4/2+20,py:YRU,pz:ZRU,r:RU/2,len:RU4+40,c:RURA},
  {t:'cyl3',n:'Otwór wentylacji grawitacyjnej z kratką (KR, nie zasłaniać)',layer:'Instalacje',ax:'x',px:A-4,py:YS-KR3-KR/2,pz:KR2+KR/2,r:KR/2+20,len:8,c:0xf0f0f0}
]);

/* ---- półka z LED na płytkach (płyta 18, z meble.pl, oklejona) ---- */
add([
  {n:'P1: Półka LED, ściana lewa (804 × 400)',layer:'Półka LED',x:0,y:YP,z:0,w:GP1,h:PP,d:LP1,c:POL},
  {n:'P3: Półka LED, ściana główna (1978 × 200)',layer:'Półka LED',x:GP1,y:YP,z:0,w:XSO-GP1,h:PP,d:GP3,c:POL},
  {n:'Profil LED wpuszczany pod P1, wzdłuż przodu (rowek 17,2 × 6)',layer:'LED',x:GP1-LRO-LRW,y:YP,z:GP3-LRO-LRW,w:LRW,h:LRG,d:LP1-LRO-(GP3-LRO-LRW),c:LED},
  {n:'Profil LED wpuszczany pod P1 przy słupku (od kabla w ścianie lewej; zaczyna się za płytkami)',layer:'LED',x:PLW+1,y:YP,z:LP1-LRO-LRW,w:GP1-LRO-PLW-1,h:LRG,d:LRW,c:LED},
  {n:'Profil LED wpuszczany pod P3 (rowek 17,2 × 6)',layer:'LED',x:GP1-LRO-LRW,y:YP,z:GP3-LRO-LRW,w:XSO-(GP1-LRO-LRW)-20,h:LRG,d:LRW,c:LED},
  {n:'Kołnierz profilu LED pod P1, wzdłuż przodu',layer:'LED',x:GP1-LRA-LKW/2,y:YP-LKH,z:GP3-LRA-LKW/2,w:LKW,h:LKH,d:ZLS-(GP3-LRA)+LKW,c:LED},
  {n:'Kołnierz profilu LED pod P1 przy słupku',layer:'LED',x:PLW+1,y:YP-LKH,z:ZLS-LKW/2,w:GP1-LRA-LKW/2-PLW-1,h:LKH,d:LKW,c:LED},
  {n:'Kołnierz profilu LED pod P3',layer:'LED',x:GP1-LRA-LKW/2,y:YP-LKH,z:GP3-LRA-LKW/2,w:XSO-(GP1-LRA-LKW/2)-20,h:LKH,d:LKW,c:LED}
]);

/* pręty M8 (2026-11-16): 80 w betonie (kotwa chemiczna) + 80 w półce; otwór w półce Ø8: 35 meble.pl, pogłębia użytkownik do 85 */
[150,570,990,1410,1830].forEach(function(xp){
  ITEMS.push({t:'cyl3',n:'Pręt M8 × 160 pod P3, x od lewego końca P3 '+xp,layer:'Mocowanie półki',ax:'z',px:GP1+xp,py:YP+PP/2,pz:(WT-WB)/2,r:PR,len:WT+WB,c:0x555555});
});
[150,400,650].forEach(function(zp){
  ITEMS.push({t:'cyl3',n:'Pręt M8 × 160 pod P1 (ściana lewa)',layer:'Mocowanie półki',ax:'x',px:(WT-WB)/2,py:YP+PP/2,pz:zp,r:PR,len:WT+WB,c:0x555555});
});
/* bez prętów od ściany głównej pod P1: prostopadłych prętów nie da się nasunąć naraz (audyt v1 KU-01, 2026-11-18) */

/* ---- szafka okapowa SO: bez dna (okap między bokami), plecy między bokami, wieniec, półka nad okapem ---- */
add([
  {n:'SOB-1: SO: bok lewy',layer:'Ścianki boczne',x:XSO,y:YP,z:0,w:P,h:YT-YP,d:GKS,c:BOK},
  {n:'SOB-2: SO: bok prawy',layer:'Ścianki boczne',x:XWS-P,y:YP,z:0,w:P,h:YT-YP,d:GKS,c:BOK},
  {n:'SOT: SO: tył',layer:'Ścianki tylne',x:XSO+P,y:YP,z:0,w:SOW-2*P,h:YT-YP,d:P,c:TYL},
  {n:'SOW: SO: wieniec górny',layer:'Półki',x:XSO+P,y:YT-P,z:P,w:SOW-2*P,h:P,d:GKS-P,c:POL},
  {n:'SOD: SO: półka wkładana tuż nad okapem, na podpórkach, z wycięciem od przodu na wylot (wkładana po montażu okapu)',layer:'Półki',x:XSO+P+1,y:YSOD,z:P,w:SOW-2*P-2,h:P,d:GKS-P-2,c:POL},
  {n:'SOP: SO: półka nad okapem na 4 podpórkach, luz 1 z boków, 2 cofnięta od przodu (2026-11-24; wycięcie U na rurę)',layer:'Półki',x:XSO+P+1,y:YSOP,z:P,w:SOW-2*P-2,h:P,d:GKS-P-2,c:POL},
  {n:'F1: Front szafki okapowej (549 × 1151), 2 przed korpusem (szczelina TIP-ON)',layer:'Fronty',x:XSO+1.5,y:YP+1.5,z:GKS+SZT,w:SOW-3,h:YT-YP-3,d:P,c:FR,o:0.55}
]);
add(zawiasy('F1',XSO+1.5,YP+1.5,SOW-3,YT-YP-3,'prawa',3,GKS+SZT,[YZ1,YZ2,YT-1.5-100]));

/* okap DUO 55: kołnierz 551 × 290 pod korpusem szafki (dno), korpus 513 × 253 × 265 na środku kołnierza (2026-11-16) */
var YKL=YRU-150;       /* początek kolana 90° Ø150 (R ok. 1D): 2414 */
var YKR=YOK+26;        /* góra króćca wylotu (26 nad korpusem): 1802 */
var KL15=22;           /* część kolana 15° w osi pionu (schemat widoku) */
var YPR=YKR+40+150;    /* koniec przejścia do pionu (odcinek na króćcu ok. 40 + 2 kolana 15° z odcinkiem ok. 150): 1992 */
add([
  {n:'Okap DUO 55: kołnierz ze szkłem 551 × 290 × 1,5 (dno szafki, widoczny od spodu)',layer:'Okap',x:XH-275.5,y:YP-OKK,z:GKS-290,w:551,h:OKK,d:290,c:0x26282b},
  {n:'Okap DUO 55: korpus 513 × 253 × 265',layer:'Okap',x:XH-OKW/2,y:YP,z:OKZ,w:OKW,h:OKH,d:OKG,c:0x6f7377},
  {t:'cyl3',n:'Króciec wylotu okapu Ø148,5 × 26 + odcinek rury spiro Ø150 nasunięty na króciec, dół kolana 15°',layer:'Rura okapu',ax:'y',px:XH,py:(YOK+YKR+40+KL15)/2,pz:ZWY,r:75,len:YKR+40+KL15-YOK,c:RURA},
  {t:'cyl3',n:'Przejście do pionu o 28,5 w głąb: 2 kolana 15° Ø150 spięte mufą (odcinek pochylony ok. 15°); para obrócona w poziomie, pion ok. 10–20 w prawo (w modelu bez przesunięcia w prawo)',layer:'Rura okapu',ax:'y',rx:-Math.atan2(ZWY-ZPI,YPR-YKR-40-2*KL15),px:XH,py:(YKR+40+YPR)/2,pz:(ZWY+ZPI)/2,r:75,len:Math.sqrt(Math.pow(YPR-YKR-40-2*KL15,2)+Math.pow(ZWY-ZPI,2)),c:RURA},
  {t:'cyl3',n:'Rura spiro Ø150: pion przy ścianie przez SOP (z matą akustyczną), od górnego kolana 15°',layer:'Rura okapu',ax:'y',px:XH,py:(YPR-KL15+YKL)/2,pz:ZPI,r:75,len:YKL-YPR+KL15,c:RURA},
  {t:'cyl3',n:'Kolano 90° Ø150 tłoczone pod sufitem (schemat)',layer:'Rura okapu',ax:'y',px:XH,py:(YKL+YRU)/2,pz:ZPI,r:75,len:YRU-YKL,c:RURA},
  {t:'cyl3',n:'Rura spiro Ø150: poziomo przez SOB-2 (otwór Ø160) do skrzynki WS',layer:'Rura okapu',ax:'x',px:(XH+XRD)/2,py:YRU,pz:ZPI,r:75,len:XRD-XH,c:RURA},
  {t:'cyl3',n:'Redukcja mimośrodowa 150/125 (spiro, uszczelka), płaską stroną do ściany głównej, wąskim końcem w rurze ze ścianki',layer:'Rura okapu',ax:'x',px:XRD+LRD/2,py:YRU,pz:ZRU+6,r:69,len:LRD,c:RURA}
]);

/* ---- wąska szafka WS: bez lewego boku (2026-11-24: WSB-1 usunięty, lewą ścianką jest SOB-2), dno, wieniec,
   2 półki na podpórkach, skrzynka na rurę cofnięta (płytka półka przed nią) ---- */
var ywn=YP+P, ysd=YSK-P, prz=(ysd-ywn-NPW*P)/(NPW+1);
var WSW_=XWE-XWS-P;    /* światło wnęki WS: 256 (od SOB-2 do WSB-2) */
add([
  {n:'WSB-2: WS: bok prawy (przy ściance)',layer:'Ścianki boczne',x:XWE-P,y:YP,z:0,w:P,h:YT-YP,d:GK,c:BOK},
  {n:'WST: WS: tył (od SOB-2 do WSB-2)',layer:'Ścianki tylne',x:XWS,y:YP,z:0,w:WSW_,h:YT-YP,d:P,c:TYL},
  {n:'WSD: WS: dno',layer:'Półki',x:XWS,y:YP,z:P,w:WSW_,h:P,d:GK-P,c:POL},
  {n:'WSW: WS: wieniec górny',layer:'Półki',x:XWS,y:YT-P,z:P,w:WSW_,h:P,d:GK-P,c:POL},
  {n:'WSS: WS: dno skrzynki na rurę (płytka półka przed zaślepką)',layer:'Półki',x:XWS,y:ysd,z:P,w:WSW_,h:P,d:GK-P,c:POL},
  {n:'WSZ: WS: zaślepka skrzynki na rurę (zdejmowana, luz 1 z boków i 3 u góry)',layer:'Ścianki tylne',x:XWS+1,y:YSK,z:ZSK,w:WSW_-2,h:YT-P-YSK-3,d:P,c:TYL},
  {n:'Listwa oporowa 10 × 10 pod WSZ (na WSS)',layer:'Mocowanie półki',x:XWS+1,y:YSK,z:ZSK-10,w:WSW_-2,h:10,d:10,c:0x555555},
  {n:'Zatrzask dociskowy push-to-open pod WSW (2 szt., schemat)',layer:'Mocowanie półki',x:XWS+40,y:YT-P-12,z:ZSK-40,w:WSW_-80,h:12,d:40,c:0x555555}
]);
for(var k=1;k<=NPW;k++){
  ITEMS.push({n:'WSP-'+k+': WS: półka na 4 podpórkach (luz 1 z boków)',layer:'Półki',x:XWS+1,y:ywn+k*prz+(k-1)*P,z:P,w:WSW_-2,h:P,d:GK-P,c:POL});
}

/* kierunek słojów w widoku (zamowienie.md, potwierdzone 2026-11-23): pionowe elementy pionowo, poziome równolegle do przodu */
var SLOJE={'SOB-1':'y','SOB-2':'y','SOT':'y','WSB-2':'y','WST':'y','WSZ':'y','F1':'y',
  'SOW':'x','SOP':'x','SOD':'x','WSD':'x','WSS':'x','WSW':'x','WSP-1':'x','WSP-2':'x','P3':'x','P1':'z'};
ITEMS.forEach(function(it){var k=it.n.split(':')[0];if(SLOJE[k]&&!it.t)it.sloje=SLOJE[k];});

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
