/* ========================================================================
   Wspólny silnik wizualizacji 3D dla wszystkich pomieszczeń (Three.js r128).
   Strona pomieszczenia (np. pralnia/index.html) wczytuje kolejno:
     three.min.js, OrbitControls.js, model.js (HF_MODEL), laczniki.gen.js (opcjonalnie),
     ten plik. Silnik buduje panel, scenę i wszystkie interakcje.

   HF_MODEL (pola, wszystkie wymiary w mm):
     title          tytuł panelu i karty
     room           {W,D,H}: szerokość (X), głębokość (Z), wysokość (Y)
     wallThickness  grubość ścian na rysunku (tylko wizualnie)
     openings       [{wall:'przod'|'tyl'|'lewa'|'prawa', pos, w, y, h}] otwory w ścianach
     views          {iso,front,top,left}: pozycje kamery w metrach
     conceptLayers  warstwy brył zamysłu (rysowane za płytami)
     hiddenLayers   warstwy domyślnie ukryte
     fixedLayers    warstwy, które nie rozsuwają się suwakiem
     boardLayers    warstwy płyt (kolor docelowy, fronty: nieprzezroczystość)
     boardColor     {hex,label} kolor docelowy płyt
     noOffset       RegExp nazw bez przesunięcia w buforze głębi i bez koloru płyty
     explodeParent  function(item,helpers) -> mesh | null | undefined (undefined = reguły ogólne)
     variants       [{id,label,layer?,apply(on,helpers)}]
     items          lista obiektów (opis formatu w model.js pomieszczenia)
   ======================================================================== */
(function(){
'use strict';
var M=window.HF_MODEL;
var MM=0.001;
var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});};
function set(list){var o={};(list||[]).forEach(function(k){o[k]=1;});return o;}

/* panel */
document.title=M.title;
var variants=M.variants||[];
document.body.insertAdjacentHTML('afterbegin',
'<aside id="panel" aria-label="Sterowanie widokiem">'+
'  <div class="head"><h1>'+esc(M.title)+'</h1><button id="min" type="button" aria-label="Zwiń panel">Zwiń</button></div>'+
'  <div id="body">'+
'    <div class="group"><span>Widok</span>'+
'      <div class="btns">'+
'        <button type="button" data-v="iso">Z rogu</button>'+
'        <button type="button" data-v="front">Z przodu</button>'+
'        <button type="button" data-v="top">Z góry</button>'+
'        <button type="button" data-v="left">Od lewej</button>'+
'      </div>'+
'    </div>'+
'    <div class="group"><span>Ściany</span>'+
'      <select id="walls" aria-label="Tryb ścian">'+
'        <option value="ghost">półprzezroczyste</option>'+
'        <option value="solid">pełne</option>'+
'        <option value="off">ukryte</option>'+
'      </select>'+
'    </div>'+
'    <div class="group"><span>Kolor płyt</span>'+
'      <select id="boardColor" aria-label="Kolor płyt">'+
'        <option value="target">'+esc(M.boardColor?M.boardColor.label:'docelowy')+'</option>'+
'        <option value="parts">rozróżnienie elementów</option>'+
'      </select>'+
'    </div>'+
'    <div class="group"><label class="chk"><input type="checkbox" id="frontsSolid">Fronty nieprzezroczyste</label></div>'+
(variants.length?'    <div class="group"><span>Warianty</span>'+variants.map(function(v){return '<label class="chk"><input type="checkbox" id="'+esc(v.id)+'">'+esc(v.label)+'</label>';}).join('')+'</div>':'')+
'    <div class="group"><span>Rozsunięcie elementów</span>'+
'      <input type="range" id="explode" min="0" max="100" value="0" aria-label="Rozsunięcie elementów" style="width:100%">'+
'      <button type="button" id="explodeReset" style="margin-top:6px">Złóż</button>'+
'    </div>'+
'    <div class="group"><span>Warstwy</span><div id="layers"></div></div>'+
'    <p class="hint">Obrót: przeciągnij. Przesuwanie: prawy przycisk lub dwa palce. Zoom: kółko lub szczypanie. Najedź na obiekt, żeby zobaczyć nazwę i wymiary w mm. Cmd + kółko w górę: elementy mebli się rozsuwają, Cmd + kółko w dół: składają się z powrotem (to samo robi suwak).</p>'+
'  </div>'+
'</aside>'+
'<div id="tip" role="status"></div>'+
'<div id="err">Nie udało się wczytać biblioteki 3D. Sprawdź połączenie z internetem i odśwież stronę.</div>');

if(!window.THREE||!THREE.OrbitControls){document.getElementById('err').style.display='flex';return;}

var ROOM=M.room;
var T=M.wallThickness||100;
var ITEMS=M.items;

/* ======================= scena ======================= */
var root=document.documentElement;
function css(n){return getComputedStyle(root).getPropertyValue(n).trim();}
var scene=new THREE.Scene();
var renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});
renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));
renderer.setClearColor(0x000000,0);
document.body.appendChild(renderer.domElement);

var camera=new THREE.PerspectiveCamera(40,1,0.05,60);
var center=new THREE.Vector3(ROOM.W*MM/2,ROOM.H*MM*0.4,ROOM.D*MM/2);
var controls=new THREE.OrbitControls(camera,renderer.domElement);
controls.enableDamping=true;controls.dampingFactor=0.08;controls.screenSpacePanning=true;
controls.minDistance=0.4;controls.maxDistance=14;

scene.add(new THREE.HemisphereLight(0xffffff,0x8a9399,0.95));
var sun=new THREE.DirectionalLight(0xffffff,0.55);sun.position.set(2,4,3);scene.add(sun);

var edgeMats=[];
function edgeMat(){var m=new THREE.LineBasicMaterial({color:css('--edge')||'#2c363c'});edgeMats.push(m);return m;}
try{
  var mq=window.matchMedia('(prefers-color-scheme: dark)');
  var onTheme=function(){edgeMats.forEach(function(m){m.color.set(css('--edge')||'#2c363c');});};
  if(mq.addEventListener){mq.addEventListener('change',onTheme);}else if(mq.addListener){mq.addListener(onTheme);}
}catch(e){}

/* podłoga i ściany */
function addSlab(group,x,y,z,w,h,d,mat){
  var g=new THREE.BoxGeometry(w*MM,h*MM,d*MM);
  var m=new THREE.Mesh(g,mat);
  m.position.set((x+w/2)*MM,(y+h/2)*MM,(z+d/2)*MM);
  m.add(new THREE.LineSegments(new THREE.EdgesGeometry(g),edgeMat()));
  group.add(m);return m;
}
var floorMat=new THREE.MeshStandardMaterial({color:0xc9c3b8,roughness:.95});
addSlab(scene,-T,-40,-T,ROOM.W+2*T,40,ROOM.D+2*T,floorMat);

var wallGroup=new THREE.Group();scene.add(wallGroup);
var wallMat=new THREE.MeshStandardMaterial({color:0xd6d1c7,roughness:.95,transparent:true,opacity:.16,side:THREE.DoubleSide,depthWrite:false});
/* ściana z otworami: kawałki pełnej wysokości między otworami, potem nadproża i podokienniki */
function addWall(name){
  var alongX=(name==='tyl'||name==='przod');
  var a0=alongX?-T:0,a1=alongX?ROOM.W+T:ROOM.D+T;
  var ops=(M.openings||[]).filter(function(o){return o.wall===name;}).sort(function(a,b){return a.pos-b.pos;});
  function piece(s,len,y,h){
    if(len<=0||h<=0)return;
    if(name==='tyl')addSlab(wallGroup,s,y,-T,len,h,T,wallMat);
    else if(name==='przod')addSlab(wallGroup,s,y,ROOM.D,len,h,T,wallMat);
    else if(name==='lewa')addSlab(wallGroup,-T,y,s,T,h,len,wallMat);
    else addSlab(wallGroup,ROOM.W,y,s,T,h,len,wallMat);
  }
  var cur=a0;
  ops.forEach(function(o){piece(cur,o.pos-cur,0,ROOM.H);cur=o.pos+o.w;});
  piece(cur,a1-cur,0,ROOM.H);
  ops.forEach(function(o){var y=o.y||0;piece(o.pos,o.w,y+o.h,ROOM.H-(y+o.h));piece(o.pos,o.w,0,y);});
}
['tyl','lewa','prawa','przod'].forEach(addWall);

function setWalls(mode){
  wallGroup.visible=(mode!=='off');
  var solid=(mode==='solid');
  wallMat.opacity=solid?1:0.16;
  wallMat.transparent=!solid;
  wallMat.depthWrite=solid;
  wallMat.needsUpdate=true;
}

/* obiekty */
var layers={},pick=[];
var CONCEPT_LAYERS=set(M.conceptLayers);
var HIDE_DEFAULT=set(M.hiddenLayers); /* np. bryły zamysłu: domyślnie ukryte, bo rysują dodatkowe krawędzie na frontach */
var NO_OFFSET=M.noOffset||{test:function(){return false;}};
function build(it){
  var mesh,g,o=(it.o==null?1:it.o);
  var mat=new THREE.MeshStandardMaterial({color:it.c,roughness:.85,metalness:0,transparent:o<1,opacity:o,depthWrite:!(o<1)});
  /* Współpłaszczyznowe ściany (np. zamysł szafki i front, tarcza drzwiczek i obudowa maszyny) migotały (z-fighting).
     Bryły przesuwamy lekko w głąb bufora: zamysły szafek najdalej, płyty i maszyny trochę, a walce i elementy noOffset wcale. */
  var po=1;
  if(CONCEPT_LAYERS[it.layer]){po=2;}
  if(it.t==='cyl'||it.t==='cyl3'||NO_OFFSET.test(it.n)){po=0;}
  if(po){mat.polygonOffset=true;mat.polygonOffsetFactor=po;mat.polygonOffsetUnits=po;}
  if(it.t==='cyl3'){
    g=new THREE.CylinderGeometry(it.r*MM,it.r*MM,it.len*MM,16);
    mesh=new THREE.Mesh(g,mat);
    if(it.ax==='x')mesh.rotation.z=Math.PI/2;else if(it.ax==='z')mesh.rotation.x=Math.PI/2;
    mesh.position.set(it.px*MM,it.py*MM,it.pz*MM);
  }else if(it.t==='cyl'){
    g=new THREE.CylinderGeometry(it.r*MM,it.r*MM,it.len*MM,48);
    mesh=new THREE.Mesh(g,mat);
    mesh.rotation.x=Math.PI/2;
    mesh.position.set(it.cx*MM,it.cy*MM,(it.z+it.len/2)*MM);
  }else{
    g=new THREE.BoxGeometry(it.w*MM,it.h*MM,it.d*MM);
    mesh=new THREE.Mesh(g,mat);
    mesh.position.set((it.x+it.w/2)*MM,(it.y+it.h/2)*MM,(it.z+it.d/2)*MM);
    mesh.add(new THREE.LineSegments(new THREE.EdgesGeometry(g),edgeMat()));
  }
  mesh.userData.info=it;
  return mesh;
}
ITEMS.forEach(function(it){
  var m=build(it);scene.add(m);
  var L=it.layer||'Dodatki';
  (layers[L]=layers[L]||[]).push(m);
  pick.push(m);
});

/* warstwy wariantów: poza listą warstw, widoczne tylko po włączeniu wariantu */
variants.forEach(function(v){
  v.items=v.layer?(layers[v.layer]||[]).slice():[];
  if(v.layer)delete layers[v.layer];
  v.items.forEach(function(m){m.visible=false;});
});

/* numeracja frontów (F1, F2…), kody zgodne z listą formatek */
(function(){
  var arr=[];
  ITEMS.forEach(function(it){
    var m=/^(F\d+):/.exec(it.n);
    if(!m||it.layer!=='Fronty')return;
    var c=document.createElement('canvas');c.width=c.height=128;
    var x=c.getContext('2d');
    x.fillStyle='#ffffff';x.beginPath();x.arc(64,64,60,0,Math.PI*2);x.fill();
    x.lineWidth=6;x.strokeStyle='#1d3557';x.stroke();
    x.fillStyle='#1d3557';x.font='bold 58px sans-serif';x.textAlign='center';x.textBaseline='middle';
    x.fillText(m[1],64,68);
    var sp=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(c),depthTest:false,transparent:true}));
    sp.scale.set(130*MM,130*MM,1);sp.renderOrder=10;
    sp.position.set((it.x+it.w/2)*MM,(it.y+it.h/2)*MM,(it.z+it.d+2)*MM);
    sp.userData.item=it;scene.add(sp);arr.push(sp);
  });
  if(arr.length)layers['Numeracja frontów']=arr;
})();

/* numeracja tyłów (kody zgodne z listą formatek), pomarańczowe kółka */
(function(){
  var arr=[];
  ITEMS.forEach(function(it){
    var m=/^([A-Z0-9]+):/.exec(it.n);
    if(!m||it.layer!=='Ścianki tylne')return;
    var c=document.createElement('canvas');c.width=c.height=128;
    var x=c.getContext('2d');
    x.fillStyle='#ffe3b8';x.beginPath();x.arc(64,64,60,0,Math.PI*2);x.fill();
    x.lineWidth=6;x.strokeStyle='#b45309';x.stroke();
    x.fillStyle='#7c2d12';x.font='bold 46px sans-serif';x.textAlign='center';x.textBaseline='middle';
    x.fillText(m[1],64,68);
    var sp=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(c),depthTest:false,transparent:true}));
    sp.scale.set(120*MM,120*MM,1);sp.renderOrder=11;
    sp.position.set((it.x+it.w/2)*MM,(it.y+it.h/2)*MM,(it.z+it.d+2)*MM);
    sp.userData.item=it;scene.add(sp);arr.push(sp);
  });
  if(arr.length)layers['Numeracja tyłów']=arr;
})();

/* numeracja boków (zielone) i półek (fioletowe), kody zgodne z listą formatek; kilka brył z jednym kodem = jeden numer */
(function(){
  function badge(txt,bg,bd,fg,fs){
    var c=document.createElement('canvas');c.width=c.height=128;var x=c.getContext('2d');
    x.fillStyle=bg;x.beginPath();x.arc(64,64,60,0,Math.PI*2);x.fill();x.lineWidth=6;x.strokeStyle=bd;x.stroke();
    x.fillStyle=fg;x.font='bold '+fs+'px sans-serif';x.textAlign='center';x.textBaseline='middle';x.fillText(txt,64,68);
    var sp=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(c),depthTest:false,transparent:true}));
    sp.scale.set(110*MM,110*MM,1);sp.renderOrder=12;return sp;
  }
  function run(layerName,outName,bg,bd,fg){
    var arr=[],groups={};
    ITEMS.forEach(function(it){
      if(it.layer!==layerName)return;
      var m=/^([A-Z0-9-]+):/.exec(it.n);if(!m)return;
      (groups[m[1]]=groups[m[1]]||[]).push(it);
    });
    Object.keys(groups).forEach(function(code){
      var g=groups[code],lo=[1e9,1e9,1e9],hi=[-1e9,-1e9,-1e9];
      g.forEach(function(it){var a=[it.x,it.y,it.z],b=[it.x+it.w,it.y+it.h,it.z+it.d];
        for(var i=0;i<3;i++){lo[i]=Math.min(lo[i],a[i]);hi[i]=Math.max(hi[i],b[i]);}});
      var sp=badge(code,bg,bd,fg,code.length>4?34:42);
      sp.position.set((lo[0]+hi[0])/2*MM,(lo[1]+hi[1])/2*MM,(lo[2]+hi[2])/2*MM);
      /* numer jedzie z pierwszym elementem grupy w kolejności x rosnąco */
      g.sort(function(a,b){return a.x-b.x;});
      sp.userData.item=g[0];scene.add(sp);arr.push(sp);
    });
    if(arr.length)layers[outName]=arr;
  }
  run('Ścianki boczne','Numeracja boków','#d8f3dc','#2d6a4f','#1b4332');
  run('Półki','Numeracja półek','#e9d8fd','#6b46c1','#44337a');
})();

/* panel: warstwy */
var layersBox=document.getElementById('layers');
function applyVariants(){variants.forEach(function(v){var cb=document.getElementById(v.id);if(v.apply)v.apply(!!(cb&&cb.checked),helpers(v));});}
Object.keys(layers).forEach(function(name){
  var lab=document.createElement('label');lab.className='chk';
  var cb=document.createElement('input');cb.type='checkbox';cb.checked=!HIDE_DEFAULT[name];
  if(HIDE_DEFAULT[name]){layers[name].forEach(function(m){m.visible=false;});}
  cb.addEventListener('change',function(){layers[name].forEach(function(m){m.visible=cb.checked;});applyVariants();});
  lab.appendChild(cb);lab.appendChild(document.createTextNode(name));
  layersBox.appendChild(lab);
});
document.getElementById('walls').addEventListener('change',function(e){setWalls(e.target.value);});

/* kolor płyt i nieprzezroczystość frontów */
var BOARD_LAYERS=set(M.boardLayers);
var TARGET_COLOR=M.boardColor?M.boardColor.hex:0xeeece5;
var boardMeshes=[],frontMeshes=[];
pick.forEach(function(m){
  var it=m.userData.info;
  if(!BOARD_LAYERS[it.layer]||NO_OFFSET.test(it.n)){return;}
  boardMeshes.push(m);
  if(it.layer==='Fronty'){frontMeshes.push(m);}
});
function applyBoards(){
  var target=document.getElementById('boardColor').value==='target';
  var solid=document.getElementById('frontsSolid').checked;
  boardMeshes.forEach(function(m){
    m.material.color.setHex(target?TARGET_COLOR:m.userData.info.c);
  });
  frontMeshes.forEach(function(m){
    var it=m.userData.info,o=(it.o==null?1:it.o),opaque=solid||o>=1;
    m.material.opacity=opaque?1:o;
    m.material.transparent=!opaque;
    m.material.depthWrite=opaque;
    m.material.needsUpdate=true;
  });
}
document.getElementById('boardColor').addEventListener('change',applyBoards);
document.getElementById('frontsSolid').addEventListener('change',applyBoards);
applyBoards();
var bodyEl=document.getElementById('body'),minBtn=document.getElementById('min');
minBtn.addEventListener('click',function(){
  var hide=bodyEl.style.display!=='none';
  bodyEl.style.display=hide?'none':'block';
  minBtn.textContent=hide?'Rozwiń':'Zwiń';
  minBtn.setAttribute('aria-label',hide?'Rozwiń panel':'Zwiń panel');
});

/* widoki */
var VIEWS=M.views||{iso:[3.3,2.7,3.6],front:[0.87,1.35,4.9],top:[0.87,5.6,1.15],left:[-3.6,1.5,0.75]};
function setView(k){var v=VIEWS[k];camera.position.set(v[0],v[1],v[2]);controls.target.copy(center);controls.update();}
Array.prototype.forEach.call(document.querySelectorAll('[data-v]'),function(b){
  b.addEventListener('click',function(){setView(b.getAttribute('data-v'));});
});

/* podpowiedź po najechaniu */
var ray=new THREE.Raycaster(),mouse=new THREE.Vector2(),tip=document.getElementById('tip');
renderer.domElement.addEventListener('pointermove',function(e){
  var r=renderer.domElement.getBoundingClientRect();
  mouse.x=((e.clientX-r.left)/r.width)*2-1;
  mouse.y=-((e.clientY-r.top)/r.height)*2+1;
  ray.setFromCamera(mouse,camera);
  var vis=pick.filter(function(m){return m.visible;});
  var hit=ray.intersectObjects(vis,false)[0];
  if(hit){
    var it=hit.object.userData.info;
    tip.textContent=(it.t==='cyl'||it.t==='cyl3')?(it.n+' — średnica '+(it.r*2)+' mm'):(it.n+' — '+it.w+' × '+it.h+' × '+it.d+' mm (szerokość × wysokość × głębokość)');
    tip.style.display='block';
  }else{tip.style.display='none';}
});
renderer.domElement.addEventListener('pointerleave',function(){tip.style.display='none';});

/* rozmiar i pętla */
function resize(){
  var w=window.innerWidth,h=window.innerHeight;
  renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();
}
window.addEventListener('resize',resize);
resize();setWalls('ghost');setView('iso');

/* Rozsuwanie mebli: tylko przesunięcia, żadnych zmian wymiarów. Warstwy fixedLayers zostają na miejscu. */
var movers=[];
function front(re){return movers.filter(function(m){return m.userData.info.layer==='Fronty'&&m.userData.info.t!=='cyl'&&re.test(m.userData.info.n);})[0];}
function back(re){return movers.filter(function(m){return m.userData.info.layer==='Ścianki tylne'&&re.test(m.userData.info.n);})[0];}
function layerOn(name){var ls=layersBox.querySelectorAll('label'),r=true;Array.prototype.forEach.call(ls,function(l){if(l.textContent===name)r=l.querySelector('input').checked;});return r;}
function helpers(v){return {pick:pick,layers:layers,layerOn:layerOn,front:front,back:back,variantItems:(v&&v.items)||[]};}
(function(){
  var FIXED=set(M.fixedLayers);
  variants.forEach(function(v){if(v.layer)FIXED[v.layer]=1;});
  var F=new THREE.Vector3(1.0,0.6,2.0); /* im większa liczba, tym mocniej rozsuwa w danej osi */
  movers=pick.filter(function(m){return !FIXED[m.userData.info.layer];});
  movers.forEach(function(m){m.userData.base=m.position.clone();});
  var mn=new THREE.Vector3(1e9,1e9,1e9),mx=new THREE.Vector3(-1e9,-1e9,-1e9);
  movers.forEach(function(m){mn.min(m.userData.base);mx.max(m.userData.base);});
  var C=mn.clone().add(mx).multiplyScalar(.5);
  /* okucia jadą razem z elementem, do którego należą */
  function piece2(code){return movers.filter(function(m){var q=m.userData.info;return (q.layer==='Ścianki boczne'||q.layer==='Ścianki tylne'||q.layer==='Półki'||q.layer==='Fronty'||q.layer==='Listwa F5')&&q.t!=='cyl'&&q.n.indexOf(code+':')===0;})[0]||null;}
  var h=helpers();
  movers.forEach(function(m){
    var it=m.userData.info,par=M.explodeParent?M.explodeParent(it,h):undefined;
    if(par===undefined){
      par=null;
      if(it.layer==='Zawiasy'||it.layer==='Uchwyty'){
        var cx=it.x+it.w/2,cy=it.y+it.h/2;
        par=movers.filter(function(f){var q=f.userData.info;return q.layer==='Fronty'&&q.t!=='cyl'&&q.w&&cx>=q.x&&cx<=q.x+q.w&&cy>=q.y&&cy<=q.y+q.h;})[0]||null;
      }else if(it.layer==='Konfirmaty'||it.layer==='Otwory'||it.layer==='Kołki'){
        var mm=/(?:w |: |Kołek Ø8 x 40: )([A-Z0-9]+(?:-[0-9]+)?)/.exec(it.n);
        par=mm?piece2(mm[1]):null;
      }
    }
    m.userData.parent=par;
  });
  var byItem=new Map();pick.forEach(function(m){byItem.set(m.userData.info,m);});
  var sprites=[].concat(layers['Numeracja frontów']||[],layers['Numeracja tyłów']||[],layers['Numeracja boków']||[],layers['Numeracja półek']||[]);
  sprites.forEach(function(sp){sp.userData.base=sp.position.clone();sp.userData.owner=byItem.get(sp.userData.item)||null;});
  var t=0,slider=document.getElementById('explode');
  function disp(m){var b=m.userData.parent?m.userData.parent.userData.base:m.userData.base;
    return new THREE.Vector3((b.x-C.x)*F.x*t,(b.y-C.y)*F.y*t,(b.z-C.z)*F.z*t);}
  function apply(){
    movers.forEach(function(m){m.position.copy(m.userData.base).add(disp(m));});
    sprites.forEach(function(sp){var o=sp.userData.owner;sp.position.copy(sp.userData.base);if(o&&o.userData.base)sp.position.add(disp(o));});
    if(slider)slider.value=Math.round(t*100);
  }
  window.addEventListener('wheel',function(e){
    if(!e.metaKey||e.target!==renderer.domElement)return;
    e.preventDefault();e.stopImmediatePropagation();
    t=Math.max(0,Math.min(1,t-e.deltaY*0.0015)); /* kółko w górę (deltaY < 0) rozsuwa */
    apply();
  },{passive:false,capture:true});
  if(slider)slider.addEventListener('input',function(){t=slider.value/100;apply();});
  var rb=document.getElementById('explodeReset');
  if(rb)rb.addEventListener('click',function(){t=0;apply();});
})();
/* warianty */
variants.forEach(function(v){var cb=document.getElementById(v.id);if(cb)cb.addEventListener('change',function(){if(v.apply)v.apply(cb.checked,helpers(v));});});
(function loop(){requestAnimationFrame(loop);controls.update();renderer.render(scene,camera);})();
})();
