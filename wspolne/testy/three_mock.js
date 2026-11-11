/* Atrapa Three.js do testów bez WebGL i bez internetu: buduje graf sceny i pozwala go zrzucić do JSON.
   Używana tylko przez wspolne/testy/scena.py. */
(function(){
function V3(x,y,z){this.x=x||0;this.y=y||0;this.z=z||0;}
V3.prototype.set=function(x,y,z){this.x=x;this.y=y;this.z=z;return this;};
V3.prototype.copy=function(v){this.x=v.x;this.y=v.y;this.z=v.z;return this;};
V3.prototype.clone=function(){return new V3(this.x,this.y,this.z);};
V3.prototype.add=function(v){this.x+=v.x;this.y+=v.y;this.z+=v.z;return this;};
V3.prototype.multiplyScalar=function(s){this.x*=s;this.y*=s;this.z*=s;return this;};
V3.prototype.min=function(v){this.x=Math.min(this.x,v.x);this.y=Math.min(this.y,v.y);this.z=Math.min(this.z,v.z);return this;};
V3.prototype.max=function(v){this.x=Math.max(this.x,v.x);this.y=Math.max(this.y,v.y);this.z=Math.max(this.z,v.z);return this;};
function V2(){this.x=0;this.y=0;}
function Color(c){this.v=(typeof c==='number')?c:String(c);}
Color.prototype.set=function(c){this.v=(typeof c==='number')?c:String(c);return this;};
Color.prototype.setHex=function(c){this.v=c;return this;};
function Obj(type){this.type=type;this.position=new V3();this.rotation=new V3();this.scale=new V3(1,1,1);
  this.children=[];this.visible=true;this.userData={};this.renderOrder=0;}
Obj.prototype.add=function(c){this.children.push(c);return this;};
function Mat(type,o){o=o||{};this.type=type;for(var k in o){this[k]=o[k];}this.color=new Color(o.color==null?0xffffff:o.color);}
function Geo(type,args){this.type=type;this.args=args;}
var T={};
T.Vector3=V3;T.Vector2=V2;T.DoubleSide=2;
T.Scene=function(){Obj.call(this,'Scene');};T.Scene.prototype=Object.create(Obj.prototype);
T.Group=function(){Obj.call(this,'Group');};T.Group.prototype=Object.create(Obj.prototype);
T.Mesh=function(g,m){Obj.call(this,'Mesh');this.geometry=g;this.material=m;};T.Mesh.prototype=Object.create(Obj.prototype);
T.LineSegments=function(g,m){Obj.call(this,'LineSegments');this.geometry=g;this.material=m;};T.LineSegments.prototype=Object.create(Obj.prototype);
T.Sprite=function(m){Obj.call(this,'Sprite');this.material=m;};T.Sprite.prototype=Object.create(Obj.prototype);
T.HemisphereLight=function(a,b,i){Obj.call(this,'HemisphereLight');this.args=[a,b,i];};T.HemisphereLight.prototype=Object.create(Obj.prototype);
T.DirectionalLight=function(a,i){Obj.call(this,'DirectionalLight');this.args=[a,i];};T.DirectionalLight.prototype=Object.create(Obj.prototype);
T.PerspectiveCamera=function(f,a,n,fa){Obj.call(this,'Camera');this.args=[f,n,fa];this.aspect=a;};
T.PerspectiveCamera.prototype=Object.create(Obj.prototype);T.PerspectiveCamera.prototype.updateProjectionMatrix=function(){};
T.MeshStandardMaterial=function(o){Mat.call(this,'MeshStandardMaterial',o);};
T.LineBasicMaterial=function(o){Mat.call(this,'LineBasicMaterial',o);};
T.SpriteMaterial=function(o){Mat.call(this,'SpriteMaterial',o);};
T.BoxGeometry=function(){Geo.call(this,'Box',[].slice.call(arguments));};
T.CylinderGeometry=function(){Geo.call(this,'Cyl',[].slice.call(arguments));};
T.EdgesGeometry=function(g){Geo.call(this,'Edges',[g.type].concat(g.args));};
T.CanvasTexture=function(c){this.image=c;};
T.Raycaster=function(){};T.Raycaster.prototype.setFromCamera=function(){};T.Raycaster.prototype.intersectObjects=function(){return [];};
T.WebGLRenderer=function(){this.domElement=document.createElement('canvas');};
T.WebGLRenderer.prototype.setPixelRatio=function(){};T.WebGLRenderer.prototype.setClearColor=function(){};
T.WebGLRenderer.prototype.setSize=function(){};T.WebGLRenderer.prototype.render=function(s){window.__scene=s;};
T.OrbitControls=function(cam){this.target=new V3();this.object=cam;};T.OrbitControls.prototype.update=function(){};
window.THREE=T;
function r(x){return Math.round(x*1e6)/1e6;}
window.__dump=function(){
  var s=window.__scene,out=[];
  function walk(o,d){
    var e={t:o.type,d:d,p:[r(o.position.x),r(o.position.y),r(o.position.z)],r:[r(o.rotation.x),r(o.rotation.y),r(o.rotation.z)],v:o.visible};
    if(o.type==='Sprite'){e.s=[r(o.scale.x),r(o.scale.y)];e.ro=o.renderOrder;}
    if(o.geometry)e.g=[o.geometry.type].concat(o.geometry.args.map(function(a){return typeof a==='number'?r(a):a;}));
    if(o.material&&o.type!=='Sprite'){var m=o.material;e.m=[m.type,m.color.v,m.opacity,!!m.transparent,m.depthWrite,!!m.polygonOffset,m.polygonOffsetFactor||0];}
    if(o.userData&&o.userData.info)e.n=o.userData.info.n;
    if(o.args)e.a=o.args;
    out.push(e);
    o.children.forEach(function(c){walk(c,d+1);});
  }
  walk(s,0);return out;
};
})();
