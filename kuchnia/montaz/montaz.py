"""Montaż kuchni krok po kroku: buduje jednoplikową stronę 3D montaz_3d.html z model.js i listy kroków poniżej.
Uruchom z katalogu głównego: python3 kuchnia/montaz/montaz.py (po każdej zmianie model.js albo kolejności montażu).
Kolejność i warunki montażu: kuchnia/ustalenia.md (2026-11-24) i kuchnia/komponenty.md."""
import json
import os

TU = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(TU, '..', 'model.js')
WYJ = os.path.join(TU, 'montaz_3d.html')

# Każdy krok: tytuł, opis (lista punktów), nowe = prefiksy nazw elementów modelu pokazywanych w tym kroku,
# ukryj = prefiksy elementów chwilowo ukrytych (np. kratka), wysun = przesunięcie nowych elementów w z (mm), kamera.
SO_KAM = {'cel': [2780, 2080, 150], 'oko': [3900, 2500, 2300]}
POLKA_KAM = {'cel': [1100, 1550, 200], 'oko': [2200, 2500, 2200]}
KROKI = [
    dict(tytul='Przygotowanie formatek', kamera=SO_KAM, nowe=[], opis=[
        'Przed montażem, na stole, płyta podparta: otwór Ø160 w SOB-2 (otwornicą z obu stron, środek nawiercony przez sklep), '
        'wycięcie U w WSB-2 (R70) i w SOP, wycięcie 100 × 140 w WST od prawej krawędzi, wycięcie i podcięcie 25 × 25 w SOD, '
        'podcięcie 25 × 25 w SOP, otwór Ø25 w SOT.',
        'Otwory konfirmatów Ø5 przelotowe poszerzyć do Ø7, łby pogłębić fazownikiem ok. 0,5 poniżej lica.',
        'P1 i P3: otwory Ø8 × 35 pod pręty pogłębić do 85 (statyw / prowadnica), wyfrezować rowki LED 17,2 × 6.',
        'Krawędzie wycięć przy okapie zabezpieczyć silikonem lub lakierem.']),
    dict(tytul='Pręty M8 pod półkę', kamera=POLKA_KAM, nowe=['Pręt M8'], opis=[
        'Otwory Ø10 × 80 w ścianie lewej (3) i głównej (5) wg karty kotwy; 4 mm nad płytkami: zaczynać bez udaru.',
        'Pręty w otworach półki, półka jako szablon: pręty wsunąć w otwory z żywicą, końce od strony półki owinięte taśmą.',
        'P3 dopasować na równo z P1 przed związaniem żywicy; po związaniu półki zdjąć.']),
    dict(tytul='Półki P1 i P3 z LED', kamera=POLKA_KAM, nowe=['P1:', 'P3:', 'Profil LED', 'Kołnierz profilu'], opis=[
        'Na stole: profile MasterLED z taśmą wcisnąć w rowki od spodu (narożniki cięte pod 45°).',
        'P1 nasunąć na pręty ze ściany lewej i przykręcić przez bok słupka (wkręty do 4 × 40), kabel LED w rowek przy słupku.',
        'P3 nasunąć na pręty w kierunku ściany głównej, styk z P1 spiąć od spodu 2 łącznikami płaskimi (wkręty 3,5 × 12).']),
    dict(tytul='Złożenie szafki okapowej SO', kamera=SO_KAM, nowe=['SOB-1', 'SOB-2', 'SOT:', 'SOW:'], opis=[
        'Na podłodze: SOB-1 (widoczny bok) z SOT i SOW na mimośrodach Minifix i kołkach z klejem, SOB-2 na konfirmatach.',
        'SOD, SOP i front jeszcze nie: półki są na podpórkach, front na końcu.']),
    dict(tytul='SO na ścianie', kamera=SO_KAM, nowe=[], podswietl=['SOT:'], opis=[
        'SO dosunąć do ściany głównej i P3, przykręcić przez SOT 4 wkrętami 6 × 70 z kołkami Ø8: 2 ok. 40 pod wieńcem,'
        ' 2 nisko nad miejscem SOD (Y ok. 1830), z dala od pionu rury.',
        'Wkręty wkręcać przed okapem i rurami (górny prawy jest za poziomą rurą).']),
    dict(tytul='Złożenie skrzyni WS', kamera=SO_KAM, nowe=['WSB-2', 'WST:', 'WSD:', 'WSS:', 'WSW:'], wysun=450,
         ukryj=['Otwór wentylacji'], opis=[
        'Na podłodze, bez lewego boku: WST, WSB-2, WSD, WSS, WSW na konfirmatach (w WSB-2 trzeba je wkręcić teraz, '
        'na miejscu do ścianki są tylko 2 mm). Przy cięciu WST podeprzeć płytę.',
        'Zdjąć ramkę kratki wentylacyjnej w ściance: wystaje ok. 8 i zahaczyłaby o WSB-2.']),
    dict(tytul='Wsunięcie WS i przykręcenie', kamera=SO_KAM, nowe=[], podswietl=['WSB-2', 'WST:', 'WSD:', 'WSS:', 'WSW:'],
         ukryj=['Otwór wentylacji'], opis=[
        'WS wsunąć od przodu wzdłuż SOB-2: WSB-2 mija rurę ze ścianki wycięciem U, WST wycięciem 100 × 140.',
        'Przymiarka: zaznaczyć 4 punkty przez WST, wysunąć WS, wywiercić i osadzić kołki Ø8, wsunąć ponownie.',
        'WST przykręcić 4 wkrętami 6 × 70 (górne na lewo od wycięcia, długim bitem), od wnętrza SO konfirmaty SOB-2 → WSD i WSS.',
        'Założyć z powrotem ramkę kratki (luz 6).']),
    dict(tytul='Okap DUO 55', kamera=SO_KAM, nowe=['Okap DUO 55'], opis=[
        'Na korpus okapu pasy Alubutylu 2 mm (z dala od otworów wentylacyjnych, tabliczki i punktów przykręcenia).',
        'Okap wsunąć od dołu między boki, przykręcić 4 wkrętami Ø4 × 18 z dystansami EPDM 3,5–4 i podkładkami EPDM pod łbami.',
        'Przewód zasilający przez otwór Ø25 w SOT do puszki nad SOP, złączki Wago (L, N, PE).']),
    dict(tytul='Kanał okapu', kamera=SO_KAM, nowe=['Króciec', 'Przejście do pionu', 'Rura spiro', 'Kolano 90', 'Redukcja'], opis=[
        'Rura Ø150 na króciec (taśma EPDM / butylowa + aluminiowa, bez opaski i blachowkrętów), 2 kolana 15° na mufie,'
        ' pion, kolano 90°, poziom przez Ø160 w SOB-2, redukcja RSLL-150-125 wąskim końcem w rurę ze ścianki.',
        'Alubutyl 2 mm na blachę, pianka kauczukowa 6–10 mm na pionie i poziomie w SO; przy SOD, SOP, w otworze Ø160 '
        'i w skrzynce WS tylko Alubutyl. Pion na 2 obejmach z gumą do SOT.']),
    dict(tytul='Półki na podpórkach', kamera=SO_KAM, nowe=['SOD:', 'SOP:', 'WSP-'], opis=[
        'Podpórki płaskie Ø5 w otwory (16 szt.).',
        'SOD wsunąć nad okapem bez wkrętów (wycięciem od przodu wokół rury), SOP wokół pionu, obie z luzem do rury.',
        'SOP, WSP-1 i WSP-2 przykręcić od spodu do podpórek wkrętami Ø3 × 12.']),
    dict(tytul='Zaślepka skrzynki WSZ', kamera=SO_KAM, nowe=['Listwa oporowa', 'Zatrzask', 'WSZ:'], opis=[
        'Po rurze i redukcji: listwa 10 × 10 na WSS (klej polimerowy), 2 krótkie zatrzaski push-to-open pod WSW (wkręty 3,5 × 15),'
        ' linka zabezpieczająca WSZ do spodu WSW.',
        'WSZ wstawić na listwę i docisnąć do zatrzasków.']),
    dict(tytul='Front F1', kamera=SO_KAM, nowe=['F1:', 'Zawias'], opis=[
        'Prowadniki 173L6100 w nawierty w SOB-2 (wkręty 3,5 × 15, w razie luzu Ø4 × 16), zawiasy CLIP top w puszki F1.',
        'TIP-ON z adapterem na SOB-1 ok. Y 1850. Front zapiąć na prowadniki, wyregulować: szczelina do korpusu 2,5–3.']),
]

ZAWSZE = ['Ścianka', 'Kuchnia istniejąca', 'Instalacje']

HTML = r'''<!DOCTYPE html>
<html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kuchnia: montaż krok po kroku</title>
<style>
html,body{margin:0;height:100%;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;color:#1f1d1a;background:#f4f1ea}
#app{display:flex;height:100%}
#panel{width:360px;max-width:42vw;overflow:auto;padding:16px 18px;box-sizing:border-box;background:#fbfaf6;border-right:1px solid #ddd6c8}
#view{flex:1;position:relative;min-width:0}
canvas{display:block}
h1{font-size:18px;font-weight:600;margin:0 0 4px}
.sub{font-size:13px;color:#6b665c;margin-bottom:12px}
ol{padding-left:22px;margin:8px 0 14px}
ol li{font-size:14px;padding:3px 0;cursor:pointer;color:#6b665c}
ol li.on{color:#1f1d1a;font-weight:600}
ol li.done{color:#3d3a34}
#nav{display:flex;gap:8px;margin:6px 0 12px}
button{font:inherit;font-size:14px;padding:6px 12px;border:1px solid #c9c1b1;border-radius:8px;background:#fff;cursor:pointer}
button:disabled{opacity:.4;cursor:default}
#opis h2{font-size:16px;margin:0 0 6px}
#opis ul{padding-left:18px;margin:0}
#opis li{font-size:14px;line-height:1.5;margin-bottom:6px}
.leg{font-size:12px;color:#6b665c;margin-top:14px;line-height:1.6}
.sw{display:inline-block;width:11px;height:11px;border-radius:2px;vertical-align:-1px;margin-right:4px}
@media (max-width:720px){#app{flex-direction:column}#panel{width:auto;max-width:none;height:46%;border-right:0;border-bottom:1px solid #ddd6c8}}
</style></head><body>
<div id="app"><aside id="panel">
<h1>Kuchnia: montaż krok po kroku</h1>
<div class="sub">SO, WS, półka LED. Przeciągnij widok, by obrócić; kółko lub dwa palce: przybliżenie.</div>
<div id="nav"><button id="prev" type="button">Wstecz</button><button id="next" type="button">Dalej</button></div>
<div id="opis"></div>
<ol id="lista"></ol>
<div class="leg"><span class="sw" style="background:#f2a623"></span>nowe w tym kroku &nbsp; <span class="sw" style="background:#8b6a4f"></span>zamontowane &nbsp; <span class="sw" style="background:#c9c3b8"></span>istniejące<br>
Źródło: model.js i ustalenia.md w repozytorium (stan __STAN__). Elementy WS w kroku 6 pokazane przed wsunięciem.</div>
</aside><div id="view"></div></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script>
__MODEL__
</script>
<script>
(function(){
var M=HF_MODEL, KROKI=__KROKI__, ZAWSZE=__ZAWSZE__, MM=0.001;
var view=document.getElementById('view');
var scene=new THREE.Scene(); scene.background=new THREE.Color(0xf4f1ea);
var cam=new THREE.PerspectiveCamera(40,1,0.05,60);
var ren=new THREE.WebGLRenderer({antialias:true}); ren.setPixelRatio(Math.min(2,window.devicePixelRatio||1)); view.appendChild(ren.domElement);
var ctl=new THREE.OrbitControls(cam,ren.domElement); ctl.enableDamping=true;
scene.add(new THREE.HemisphereLight(0xffffff,0x8a8378,0.9)); var dl=new THREE.DirectionalLight(0xffffff,0.55); dl.position.set(2,5,4); scene.add(dl);
var wm=new THREE.MeshStandardMaterial({color:0xe3ded3,roughness:1,side:THREE.DoubleSide});
var W=M.room.W*MM,H=M.room.H*MM;
var w1=new THREE.Mesh(new THREE.PlaneGeometry(W,H),wm); w1.position.set(W/2,H/2,-0.001); scene.add(w1);
var w2=new THREE.Mesh(new THREE.PlaneGeometry(2.2,H),wm); w2.rotation.y=Math.PI/2; w2.position.set(-0.001,H/2,1.1); scene.add(w2);
var fl=new THREE.Mesh(new THREE.PlaneGeometry(W,2.2),new THREE.MeshStandardMaterial({color:0xcfc8bb,roughness:1})); fl.rotation.x=-Math.PI/2; fl.position.set(W/2,0,1.1); scene.add(fl);
var BOARD=0x8b6a4f, NEW=0xf2a623;
function starts(n,list){for(var i=0;i<list.length;i++){if(n.indexOf(list[i])===0)return true;}return false;}
function build(it){
  var g,m=new THREE.MeshStandardMaterial({color:it.c,roughness:.85,transparent:true,opacity:1}),mesh;
  if(it.t==='cyl3'){g=new THREE.CylinderGeometry(it.r*MM,it.r*MM,it.len*MM,20);mesh=new THREE.Mesh(g,m);
    if(it.ax==='x')mesh.rotation.z=Math.PI/2;else if(it.ax==='z')mesh.rotation.x=Math.PI/2;else if(it.rx)mesh.rotation.x=it.rx;
    mesh.position.set(it.px*MM,it.py*MM,it.pz*MM);}
  else if(it.t==='cyl'){g=new THREE.CylinderGeometry(it.r*MM,it.r*MM,it.len*MM,24);mesh=new THREE.Mesh(g,m);mesh.rotation.x=Math.PI/2;
    mesh.position.set(it.cx*MM,it.cy*MM,(it.z+it.len/2)*MM);}
  else{g=new THREE.BoxGeometry(it.w*MM,it.h*MM,it.d*MM);mesh=new THREE.Mesh(g,m);
    mesh.position.set((it.x+it.w/2)*MM,(it.y+it.h/2)*MM,(it.z+it.d/2)*MM);
    mesh.add(new THREE.LineSegments(new THREE.EdgesGeometry(g),new THREE.LineBasicMaterial({color:0x3a342c,transparent:true,opacity:.45})));}
  mesh.userData.base=mesh.position.clone(); mesh.userData.it=it; return mesh;
}
var meshes=M.items.map(function(it){var m=build(it);scene.add(m);return m;});
var krokElem=meshes.map(function(m){var n=m.userData.it.n,L=m.userData.it.layer;
  if(ZAWSZE.indexOf(L)>=0)return -1;
  for(var k=0;k<KROKI.length;k++){if(starts(n,KROKI[k].nowe))return k;} return 99;});
var cur=0, lista=document.getElementById('lista');
KROKI.forEach(function(k,i){var li=document.createElement('li');li.textContent=k.tytul;li.onclick=function(){go(i);};lista.appendChild(li);});
function go(i){
  cur=Math.max(0,Math.min(KROKI.length-1,i)); var K=KROKI[cur];
  meshes.forEach(function(m,j){var it=m.userData.it,ks=krokElem[j],mat=m.material;
    m.position.copy(m.userData.base);
    var vis=(ks===-1)||(ks<=cur); if(K.ukryj&&starts(it.n,K.ukryj))vis=false; m.visible=vis; if(!vis)return;
    var nowy=(ks===cur)||(K.podswietl&&starts(it.n,K.podswietl));
    if(ks===-1){mat.color.setHex(it.layer==='Kuchnia istniejąca'?0xc9c3b8:it.c);mat.opacity=it.layer==='Kuchnia istniejąca'?.55:1;}
    else{var plyta=/^(SO|WS|P1|P3|F1)/.test(it.n)&&!it.t;mat.color.setHex(nowy?NEW:(plyta?BOARD:it.c));mat.opacity=1;}
    if(K.wysun&&ks===cur)m.position.z+=K.wysun*MM;
  });
  var c=K.kamera; ctl.target.set(c.cel[0]*MM,c.cel[1]*MM,c.cel[2]*MM); cam.position.set(c.oko[0]*MM,c.oko[1]*MM,c.oko[2]*MM); ctl.update();
  document.getElementById('opis').innerHTML='<h2>Krok '+(cur+1)+' z '+KROKI.length+': '+K.tytul+'</h2><ul>'+K.opis.map(function(t){return '<li>'+t+'</li>';}).join('')+'</ul>';
  [].forEach.call(lista.children,function(li,j){li.className=(j===cur?'on':(j<cur?'done':''));});
  document.getElementById('prev').disabled=cur===0; document.getElementById('next').disabled=cur===KROKI.length-1;
}
document.getElementById('prev').onclick=function(){go(cur-1);}; document.getElementById('next').onclick=function(){go(cur+1);};
document.addEventListener('keydown',function(e){if(e.key==='ArrowRight')go(cur+1);if(e.key==='ArrowLeft')go(cur-1);});
function size(){var w=view.clientWidth,h=view.clientHeight;ren.setSize(w,h);cam.aspect=w/Math.max(1,h);cam.updateProjectionMatrix();}
window.addEventListener('resize',size); size(); go(0);
(function loop(){requestAnimationFrame(loop);ctl.update();ren.render(scene,cam);})();
})();
</script></body></html>
'''


def main():
    model = open(MODEL, encoding='utf-8').read()
    import subprocess
    stan = subprocess.run(['git', 'log', '-1', '--format=%cs %h', '--', MODEL], capture_output=True, text=True,
                          cwd=TU).stdout.strip() or 'bieżący'
    html = (HTML.replace('__MODEL__', model).replace('__KROKI__', json.dumps(KROKI, ensure_ascii=False))
            .replace('__ZAWSZE__', json.dumps(ZAWSZE, ensure_ascii=False)).replace('__STAN__', stan))
    open(WYJ, 'w', encoding='utf-8').write(html)
    print('zapisano', WYJ, len(KROKI), 'kroków')


if __name__ == '__main__':
    main()
