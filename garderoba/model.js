/* ========================================================================
   GARDEROBA (A/P02 07): DANE MODELU 3D (wszystko w milimetrach)
   Patrząc od drzwi: ściana tylna = na wprost (przewody wodne), lewa = z gzymsem, przednia = z drzwiami.
   Układ: X od lewej ściany ku prawej, Y od podłogi w górę, Z od tylnej ściany ku drzwiom.
   Wymiary z pomiary.md (najmniejsze odczyty), decyzje z ustalenia.md.
   Formatki (płyta 18 i skrzynki 16) mają nazwy 'KOD: opis'; format: wspolne/STRUKTURA.md, punkt 4.
   Moduły: N / L = dolne korpusy szafki na wprost i po lewej (0–2120), GN / GL = górne korpusy (2120–2583),
   S1/S2 = skrzynki szuflad. Wszystkie wymiary formatek i otworów w pełnych mm.
   ======================================================================== */
var HF_MODEL=(function(){
'use strict';
/* ---------- pomiary (pomiary.md) ---------- */
var A=1825;            /* szerokość: lewa–prawa ściana przy ścianie przedniej */
var AT=1829;           /* szerokość przy ścianie tylnej (PX + pion–prawa ściana, najmniejsza): tu stoi szafka na wprost */
var G=1490;            /* głębokość: tylna–przednia ściana */
var J=2586;            /* wysokość, najmniejsza (przy drzwiach) */
var PX=692, PXM=700;   /* wysięg pionu od lewej ściany: przy podłodze / największy (lico pionu nie jest pionowe) */
var PZ=563, PZM=573;   /* wysięg pionu od tylnej ściany: najmniejszy / największy */
var T=925;             /* od lica pionu do ściany przedniej (najmniejszy) */
var TP=1491;           /* ściana przednia przy lewej ścianie, od tylnej: najmniejsze PZ + T na tej samej wysokości (563 + 928 na 400) */
var DX=164, DW=694, DH=2014;   /* drzwi: od prawej ściany, szerokość i wysokość w świetle ościeżnicy */
var W1=2415, W2=317, W3=130, W4=120;   /* wylot wentylacyjny: wysokość środka, od lewej ściany, średnica, wysięg od lica pionu */
var GZ1=333, GZ2=129, GZ3=927;         /* gzyms: wysokość, wysięg od lewej ściany, długość od pionu */
var GR3=135, GR4=55;                   /* rura w gzymsie: góra od podłogi, wysięg poza lico gzymsu */
var R1=513, R2=613, R3=180, R4=50;     /* przewody wodne: od prawej ściany, wysokość po zagięciu, wysięg (ok.) */
var E1=210, E2=195;                    /* przyszłe gniazdko na ścianie przedniej: środek od lewej ściany, od podłogi */
var L1=1131, L2=1000;                  /* lampa (oczko): środek od tylnej ściany, od lewej ściany */

/* ---------- założenia (ustalenia.md) ---------- */
var P=18, PS=16;       /* płyta korpusów i frontów / skrzynek szuflad */
var LUZ=3;             /* luz: od pionu, przy prawej ścianie i ścianie przedniej */
var LUZS=4;            /* luz pod sufitem (2026-11-18: 4 zamiast 3, łatwiejsze wsuwanie korpusów górnych) */
var ODS=5;             /* odsunięcie korpusu od ściany za nim (regulacja przy montażu) */
var SZCZ=2;            /* szczelina wokół frontów chowanych (2026-11-18: 2 zamiast 3, więcej regulacji zawiasów) */
var HW=2120;           /* górna powierzchnia wieńca części otwartej = góra korpusów dolnych, dół korpusów górnych */
var HG=J-LUZS;         /* góra szafek: 2582 */
var ZF=PZM+LUZ;        /* płaszczyzna przodu szafki na wprost = tył boku LB1: 576 (3 przed najdalszym punktem pionu; do 2026-11-18: PZ + 3 + 18 = 583) */
var XL=PXM+LUZ;        /* płaszczyzna przodu szafki po lewej = lewy bok szafki na wprost: 703 */
var XP=AT-LUZ-1;       /* prawy bok szafki na wprost: 1825 (luz 4 przy prawej ścianie; szerokość 1122, połowy po 534) */
var XM=(XL+XP)/2;      /* oś przegrody: 1264 (połowy po 534) */
var ZP=TP-LUZ;         /* koniec szafki po lewej przy ścianie przedniej: 1488 (do 2026-11-19: PZ + T − 3 = 1485) */
var HD=HW-P-65;        /* oś drążka: 65 pod spodem wieńca = 2037 */
var HK1=1000;          /* przedział na krótsze kurtki (połowa lewa szafki na wprost, szafka po lewej) */
var YP=[GZ1+2];        /* spody półek na buty: 335 (2 mm nad gzymsem), dalej dwa przedziały po równo */
var SZD=208;           /* przedział szuflady */
var ZO=R4+5;           /* tylne lico osłony przewodów: 55 od ściany */
var WYC1=GZ2+GR4+5, WYC2=GZ2+5, WYCH=YP[0];   /* wycięcia boków L wokół gzymsu (od ściany lewej): przy pionie (z rurą) do 189, przy ścianie przedniej do 134; wysokość 335 */
var NL1=500, NL2=600;  /* prowadnice MOVENTO 760H (40 kg, NL do 600): SZ1, SZ2 (audyt v1: NL 650 jest tylko w 766H) */
var HSK=180;           /* wysokość boków skrzynek (≤ przedział − 23 = 185, katalog Blum) */
(function(){var b2=(HW-P-HK1-P-SZD-(YP[0]+P)-2*P)/2;YP.push(YP[0]+P+Math.floor(b2));YP.push(YP[0]+2*P+2*b2);})();   /* 335, 596, 858 (przedziały 243 i 244) */
var YK=HW-P-HK1-P;     /* spód płyty pod kurtkami: 1084 */

var C={bok:0xcdbb95,tyl:0xb9a37a,pol:0xd8c7a3,front:0x2f9e8f,skr:0xb08a5b};
var ITEMS=[
  /* ===== Pomieszczenie ===== */
  {n:'Pion (wysięg '+PXM+' od lewej ściany, '+PZ+' od tylnej; przy podłodze '+PX+')',layer:'Pion i gzyms',x:0,y:0,z:0,w:PXM,h:J,d:PZM,c:0xd9d4ca},
  {n:'Gzyms ('+GZ2+' × '+GZ1+', długość '+GZ3+')',layer:'Pion i gzyms',x:0,y:0,z:G-GZ3,w:GZ2,h:GZ1,d:GZ3,c:0xc7c1b5},
  {n:'Rura wystająca z gzymsu (wysięg '+GR4+', do '+GR3+' od podłogi; szerokość 80 założona)',layer:'Osprzęt',x:GZ2,y:0,z:G-GZ3,w:GR4,h:GR3,d:80,c:0xb08d57},
  /* przewód docięty 3 przed bokiem GLB1 (wysięg 10 zamiast 120), żeby korpus górny GL dało się wsunąć wzdłuż X;
     połączenie z kratką krótką tuleją przez otwór w GLB1 po ustawieniu korpusu (audyt v2, GD-08) */
  {t:'cyl',n:'Przewód wentylacyjny Ø'+W3+' docięty do '+(ZF-LUZ)+' od ściany tylnej, 3 przed bokiem GLB1 (było '+W4+' od pionu)',layer:'Osprzęt',cx:W2,cy:W1,z:PZ,r:W3/2,len:ZF-LUZ-PZ,c:0x6b7b8c},
  {t:'cyl',n:'Tuleja Ø125 przez otwór w GLB1 do kratki (wkładana po ustawieniu korpusu GL)',layer:'Osprzęt',cx:W2,cy:W1,z:ZF-LUZ,r:62,len:LUZ+P,c:0x8a96a3},
  {n:'Przewód wodny R1 ('+R1+' od prawej ściany, do ok. '+R3+', wysięg ok. '+R4+')',layer:'Osprzęt',x:AT-R1-20,y:0,z:0,w:40,h:R3,d:R4,c:0xc0392b},
  {n:'Przewód wodny R2 ('+R2+' od prawej ściany, do ok. '+R3+', wysięg ok. '+R4+')',layer:'Osprzęt',x:AT-R2-20,y:0,z:0,w:40,h:R3,d:R4,c:0x2e5fb3},
  {n:'Gniazdko (E1 '+E1+' od lewej ściany, E2 '+E2+' od podłogi)',layer:'Osprzęt',x:E1-40,y:E2-40,z:TP-2,w:80,h:80,d:2,c:0xe58a2b},   /* lico ściany przy lewej: TP; wysięg osprzętu do sprawdzenia */
  {t:'cyl3',n:'Lampa (oczko) '+L2+' od lewej ściany, '+L1+' od tylnej',layer:'Osprzęt',ax:'y',px:L2,py:J-3,pz:L1,r:40,len:6,c:0xe0a526},

  /* ===== Szafka na wprost, korpus dolny N (0–2120): przegroda NP na pół, plecy 18 na całą szerokość, bez dna ===== */
  {n:'NB-1: bok lewy dolny (przy pionie)',layer:'Ścianki boczne',x:XL,y:0,z:ODS,w:P,h:HW,d:ZF-ODS,c:C.bok},
  {n:'NB-2: bok prawy dolny (przy prawej ścianie)',layer:'Ścianki boczne',x:XP-P,y:0,z:ODS,w:P,h:HW,d:ZF-ODS,c:C.bok},
  {n:'NP: przegroda środkowa dolna (od podłogi do wieńca NW)',layer:'Ścianki boczne',x:XM-P/2,y:0,z:ODS+P,w:P,h:HW-P,d:ZF-ODS-P,c:C.bok},
  {n:'NT: plecy dolne (nad osłoną przewodów, do wieńca NW)',layer:'Ścianki tylne',x:XL+P,y:YP[0],z:ODS,w:XP-XL-2*P,h:HW-P-YP[0],d:P,c:C.tyl},
  {n:'NW: wieniec dolnego korpusu na '+HW+' (sufit części otwartej)',layer:'Półki',x:XL+P,y:HW-P,z:ODS,w:XP-XL-2*P,h:P,d:ZF-ODS,c:C.pol},

  /* ===== Szafka na wprost, korpus górny GN (2120–2583): dno, przegroda, plecy, wieniec, fronty F1 F2 ===== */
  {n:'GNB-1: bok lewy górny (przy pionie; zawiasy F1)',layer:'Ścianki boczne',x:XL,y:HW,z:ODS,w:P,h:HG-HW,d:ZF-ODS,c:C.bok},
  {n:'GNB-2: bok prawy górny (przy prawej ścianie; zawiasy F2)',layer:'Ścianki boczne',x:XP-P,y:HW,z:ODS,w:P,h:HG-HW,d:ZF-ODS,c:C.bok},
  {n:'GND: dno korpusu górnego',layer:'Półki',x:XL+P,y:HW,z:ODS,w:XP-XL-2*P,h:P,d:ZF-ODS,c:C.pol},
  {n:'GNG: wieniec górny',layer:'Półki',x:XL+P,y:HG-P,z:ODS,w:XP-XL-2*P,h:P,d:ZF-ODS,c:C.pol},
  {n:'GNP: przegroda środkowa górna',layer:'Ścianki boczne',x:XM-P/2,y:HW+P,z:ODS+P,w:P,h:HG-HW-2*P,d:ZF-ODS-P,c:C.bok},
  {n:'GNT: plecy górne',layer:'Ścianki tylne',x:XL+P,y:HW+P,z:ODS,w:XP-XL-2*P,h:HG-HW-2*P,d:P,c:C.tyl},

  /* ===== Szafka po lewej, korpus dolny L (0–2120): boki z wycięciem wokół gzymsu, plecy 18 nad gzymsem ===== */
  {n:'LB1: bok dolny przy pionie (wycięcie '+(WYC1-ODS)+' × '+WYCH+' wokół gzymsu i rury)',layer:'Ścianki boczne',x:ODS,y:0,z:ZF,w:XL-ODS,h:HW,d:P,c:C.bok},
  {n:'LB2: bok dolny przy ścianie przedniej (wycięcie '+(WYC2-ODS)+' × '+WYCH+' wokół gzymsu; otwór na gniazdko)',layer:'Ścianki boczne',x:ODS,y:0,z:ZP-P,w:XL-ODS,h:HW,d:P,c:C.bok},
  {n:'LT: plecy dolne (nad gzymsem, do wieńca LW)',layer:'Ścianki tylne',x:ODS,y:YP[0],z:ZF+P,w:P,h:HW-P-YP[0],d:ZP-ZF-2*P,c:C.tyl},
  {n:'LW: wieniec dolnego korpusu na '+HW,layer:'Półki',x:ODS,y:HW-P,z:ZF+P,w:XL-ODS,h:P,d:ZP-ZF-2*P,c:C.pol},
  {n:'LK: płyta pod kurtkami',layer:'Półki',x:ODS+P,y:YK,z:ZF+P,w:XL-ODS-P,h:P,d:ZP-ZF-2*P,c:C.pol},

  /* ===== Szafka po lewej, korpus górny GL (2120–2583): otwarta półka bez frontów ===== */
  {n:'GLB1: bok górny przy pionie (otwór na przewód wentylacyjny)',layer:'Ścianki boczne',x:ODS,y:HW,z:ZF,w:XL-ODS,h:HG-HW,d:P,c:C.bok},
  {n:'GLB2: bok górny przy ścianie przedniej',layer:'Ścianki boczne',x:ODS,y:HW,z:ZP-P,w:XL-ODS,h:HG-HW,d:P,c:C.bok},
  {n:'GLD: dno korpusu górnego',layer:'Półki',x:ODS,y:HW,z:ZF+P,w:XL-ODS,h:P,d:ZP-ZF-2*P,c:C.pol},
  {n:'GLG: wieniec górny',layer:'Półki',x:ODS,y:HG-P,z:ZF+P,w:XL-ODS,h:P,d:ZP-ZF-2*P,c:C.pol},
  {n:'GLT: plecy górne',layer:'Ścianki tylne',x:ODS,y:HW+P,z:ZF+P,w:P,h:HG-HW-2*P,d:ZP-ZF-2*P,c:C.tyl},

  /* wycięcia w bokach L: tylko poglądowo (formatki są prostokątami, wycięcie w uwagach do zamówienia) */
  {n:'Wycięcie w LB1 ('+(WYC1-ODS)+' × '+WYCH+', narożnik dolny przy ścianie)',layer:'Wycięcia',x:ODS,y:0,z:ZF-0.5,w:WYC1-ODS,h:WYCH,d:P+1,c:0xd23c3c,o:0.45},
  {n:'Wycięcie w LB2 ('+(WYC2-ODS)+' × '+WYCH+', narożnik dolny przy ścianie)',layer:'Wycięcia',x:ODS,y:0,z:ZP-P-0.5,w:WYC2-ODS,h:WYCH,d:P+1,c:0xd23c3c,o:0.45},
  /* kratka prostokątna nasunięta na przewód wentylacyjny, od strony półek (wymiar 180 × 180 ZAŁOŻONY) */
  {n:'Kratka wentylacyjna prostokątna na przewodzie Ø'+W3+' (180 × 180 założone)',layer:'Osprzęt',x:W2-90,y:W1-90,z:ZF+P,w:180,h:180,d:8,c:0xe0a526},

  /* drążki na kurtki Ø25 */
  {t:'cyl3',n:'Drążek na kurtki N, połowa lewa (oś '+HD+')',layer:'Drążki',ax:'x',px:(XL+P+XM-P/2)/2,py:HD,pz:(ODS+P+ZF)/2,r:12.5,len:XM-P/2-XL-P,c:0x9aa5ad},
  {t:'cyl3',n:'Drążek na dłuższe kurtki N, połowa prawa (oś '+HD+')',layer:'Drążki',ax:'x',px:(XM+P/2+XP-P)/2,py:HD,pz:(ODS+P+ZF)/2,r:12.5,len:XP-P-XM-P/2,c:0x9aa5ad},
  {t:'cyl3',n:'Drążek na kurtki L, wzdłuż ściany (oś '+HD+')',layer:'Drążki',ax:'z',px:(ODS+P+XL)/2,py:HD,pz:(ZF+ZP)/2,r:12.5,len:ZP-ZF-2*P,c:0x9aa5ad}
];

function add(it){ITEMS.push(it);return it;}

/* ---------- połowy szafki N ---------- */
var H1={x0:XL+P,x1:XM-P/2}, H2={x0:XM+P/2,x1:XP-P}, ZW=ODS+P;   /* wnętrze: od lica pleców 23 do 583 */
var ns=0;
function polkaN(h,y,opis){ns++;add({n:'NS-'+ns+': półka nad butami ('+opis+')',layer:'Półki',x:h.x0,y:y,z:ZW,w:h.x1-h.x0,h:P,d:ZF-ZW,c:C.pol});}
[[H1,'1'],[H2,'2']].forEach(function(q){
  var h=q[0];
  add({n:'NO-'+q[1]+': osłona przewodów wodnych, zdejmowana (0–'+YP[0]+', '+ZO+'–'+(ZO+P)+' od ściany)',layer:'Ścianki tylne',x:h.x0,y:0,z:ZO,w:h.x1-h.x0,h:YP[0],d:P,c:C.tyl});
  /* osłona bez konfirmatów: u góry 2 kątowniki pod półką (od strony pokoju, niewidoczne), na dole 2 zatrzaski magnetyczne
     na bokach za osłoną (blaszki na tylnym licu osłony); zdjęcie: odkręcić kątowniki, odciągnąć dół od magnesów */
  [h.x0+60,h.x1-80].forEach(function(x){add({n:'Kątownik osłony NO-'+q[1]+' (pod półką, wkręty w półkę i osłonę)',layer:'Osprzęt',x:x,y:YP[0]-20,z:ZO+P,w:20,h:20,d:20,c:0x8a8f94});});
  [[h.x0,1],[h.x1-12,-1]].forEach(function(m){add({n:'Zatrzask magnetyczny osłony NO-'+q[1]+' (na boku, za osłoną)',layer:'Osprzęt',x:m[0],y:40,z:ZO-14,w:12,h:30,d:14,c:0x5a6068});});
});
polkaN(H1,YP[0],'połowa lewa, 1');polkaN(H1,YP[1],'połowa lewa, 2');polkaN(H1,YP[2],'połowa lewa, 3');
polkaN(H2,YP[0],'połowa prawa, 1');polkaN(H2,YP[1],'połowa prawa, 2; dno przedziału na dłuższe kurtki');
add({n:'NK: płyta pod kurtkami (połowa lewa)',layer:'Półki',x:H1.x0,y:YK,z:ZW,w:H1.x1-H1.x0,h:P,d:ZF-ZW,c:C.pol});
for(var i=0;i<3;i++){add({n:'LS-'+(i+1)+': półka nad butami '+(i+1),layer:'Półki',x:ODS+P,y:YP[i],z:ZF+P,w:XL-ODS-P,h:P,d:ZP-ZF-2*P,c:C.pol});}

/* ---------- fronty górne N: chowane, TIP-ON, zawiasy po zewnętrznych stronach ---------- */
var YF0=HW+P+SZCZ, YF1=HG-P-SZCZ;   /* 2140–2563: między dnem GND a wieńcem GNG */
function zawiasy(fx,fw,lewa){var cx=lewa?fx+22.5:fx+fw-22.5;[YF0+100,YF1-100].forEach(function(cy){
  add({n:'Zawias wpuszczany ('+(lewa?'lewa':'prawa')+')',layer:'Zawiasy',x:cx-17.5,y:cy-17.5,z:ZF-P+1,w:35,h:35,d:11,c:0x2b3034});});}
add({n:'F1: front górny, połowa lewa (chowany, TIP-ON)',layer:'Fronty',x:H1.x0+SZCZ,y:YF0,z:ZF-P,w:H1.x1-H1.x0-2*SZCZ,h:YF1-YF0,d:P,c:C.front,o:0.55});
add({n:'F2: front górny, połowa prawa (chowany, TIP-ON)',layer:'Fronty',x:H2.x0+SZCZ,y:YF0,z:ZF-P,w:H2.x1-H2.x0-2*SZCZ,h:YF1-YF0,d:P,c:C.front,o:0.55});
zawiasy(H1.x0+SZCZ,H1.x1-H1.x0-2*SZCZ,true);
zawiasy(H2.x0+SZCZ,H2.x1-H2.x0-2*SZCZ,false);

/* ---------- szuflady: Blum MOVENTO do TIP-ON BLUMOTION, skrzynki 16, fronty chowane ----------
   Katalog Blum (drewniane skrzynki, bok 16): szer. wewn. = LW − 42, długość = NL − 10, dno wpuszczone 13,
   prześwit pod skrzynką 16, nad skrzynką min. 7 (wysokość skrzynki ≤ przedział − 23); głębokość za frontem chowanym
   przyjęta z zapasem ≥ NL + 7 (katalog: NL + X + 3, +3 z regulacją głębokości).
   Tył skrzynki stoi na dnie, dno sięga do końca boków: wariant Blum „bez podcięć” (option – no notching), zgodny z TIP-ON
   BLUMOTION (pod dnem wolne 13 na całej szerokości, katalog wymaga podcięć min. 125); otwory Ø6 × 10 pod haki prowadnic
   w tylnej krawędzi dna, 7 nad spodem dna (20 nad dolną krawędzią boków), 11 od wewnętrznego lica boków.
   Pola sz/rola/ruch/skok: kontrola kolizji przy otwieraniu (garderoba/sprawdz_szuflady.js). */
function szuflada(kod,fkod,opis,przodX,LW,NL,y0,b){
  /* b: {x0,x1,z0,z1} wnętrze przedziału; przód na x1 (przodX) albo z1 */
  var SKW=LW-42,DB=NL-10,yb=y0+16,REC=13,fh=SZD-2*SZCZ,r=przodX?'x':'z';
  var tag=function(it,rola){it.sz=fkod;it.rola=rola;it.ruch=r;it.skok=NL;return add(it);};
  var H=HSK, HC=H-REC-PS;   /* czoło i tył skrzynki stoją na dnie */
  if(przodX){
    var zc=(b.z0+b.z1)/2, z0=zc-SKW/2-PS, xf=b.x1-P, x0=xf-DB;
    tag({n:fkod+': front szuflady '+opis+' (chowany, TIP-ON)',layer:'Fronty',x:xf,y:y0+SZCZ,z:b.z0+SZCZ,w:P,h:fh,d:b.z1-b.z0-2*SZCZ,c:C.front,o:0.8},'front');
    tag({n:kod+'B-1: skrzynka '+opis+': bok',layer:'Skrzynki szuflad',x:x0,y:yb,z:z0,w:DB,h:H,d:PS,c:C.skr},'skrzynka');
    tag({n:kod+'B-2: skrzynka '+opis+': bok',layer:'Skrzynki szuflad',x:x0,y:yb,z:z0+PS+SKW,w:DB,h:H,d:PS,c:C.skr},'skrzynka');
    tag({n:kod+'D: skrzynka '+opis+': dno',layer:'Skrzynki szuflad',x:x0,y:yb+REC,z:z0+PS,w:DB,h:PS,d:SKW,c:C.skr},'skrzynka');
    tag({n:kod+'C-1: skrzynka '+opis+': czoło',layer:'Skrzynki szuflad',x:xf-PS,y:yb+REC+PS,z:z0+PS,w:PS,h:HC,d:SKW,c:C.skr},'skrzynka');
    tag({n:kod+'C-2: skrzynka '+opis+': tył',layer:'Skrzynki szuflad',x:x0,y:yb+REC+PS,z:z0+PS,w:PS,h:HC,d:SKW,c:C.skr},'skrzynka');
  }else{
    var xc=(b.x0+b.x1)/2, x0b=xc-SKW/2-PS, zf=b.z1-P, z0b=zf-DB;
    tag({n:fkod+': front szuflady '+opis+' (chowany, TIP-ON)',layer:'Fronty',x:b.x0+SZCZ,y:y0+SZCZ,z:zf,w:b.x1-b.x0-2*SZCZ,h:fh,d:P,c:C.front,o:0.8},'front');
    tag({n:kod+'B-1: skrzynka '+opis+': bok',layer:'Skrzynki szuflad',x:x0b,y:yb,z:z0b,w:PS,h:H,d:DB,c:C.skr},'skrzynka');
    tag({n:kod+'B-2: skrzynka '+opis+': bok',layer:'Skrzynki szuflad',x:x0b+PS+SKW,y:yb,z:z0b,w:PS,h:H,d:DB,c:C.skr},'skrzynka');
    tag({n:kod+'D: skrzynka '+opis+': dno',layer:'Skrzynki szuflad',x:x0b+PS,y:yb+REC,z:z0b,w:SKW,h:PS,d:DB,c:C.skr},'skrzynka');
    tag({n:kod+'C-1: skrzynka '+opis+': czoło',layer:'Skrzynki szuflad',x:x0b+PS,y:yb+REC+PS,z:zf-PS,w:SKW,h:HC,d:PS,c:C.skr},'skrzynka');
    tag({n:kod+'C-2: skrzynka '+opis+': tył',layer:'Skrzynki szuflad',x:x0b+PS,y:yb+REC+PS,z:z0b,w:SKW,h:HC,d:PS,c:C.skr},'skrzynka');
  }
}
var YS=YP[2]+P;   /* dół przedziału szuflady: 876 */
szuflada('S1','F3','SZ1 (N, połowa lewa)',false,H1.x1-H1.x0,NL1,YS,{x0:H1.x0,x1:H1.x1,z0:ZW,z1:ZF});
szuflada('S2','F4','SZ2 (L)',true,ZP-ZF-2*P,NL2,YS,{x0:ODS+P,x1:XL,z0:ZF+P,z1:ZP-P});

return {
  title:'Garderoba 3D',
  room:{W:AT,D:G,H:J},   /* ściany rysowane prosto: szerokość przy ścianie tylnej (przy przedniej A = 1825) */
  wallThickness:100,
  openings:[{wall:'przod',pos:A-DX-DW,w:DW,y:0,h:DH}],
  views:{iso:[3.3,2.7,3.6],front:[0.91,1.3,4.9],top:[0.91,5.6,1.15],left:[-3.6,1.5,0.75]},
  conceptLayers:[],
  hiddenLayers:[],
  fixedLayers:['Pion i gzyms','Osprzęt','Wycięcia'],
  boardLayers:['Półki','Ścianki boczne','Ścianki tylne','Fronty'],
  boardColor:{hex:0xeeece5,label:'docelowy: Egger W1200 ST9 Biały porcelanowy'},
  variants:[],
  items:ITEMS
};
})();
