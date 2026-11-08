const fs=require('fs');
const h=fs.readFileSync('pralnia_3d.html','utf8');
const m=h.match(/var ITEMS\s*=\s*\[([\s\S]*?)\n\];/);
const items=eval('['+m[1]+']');
const out=items.filter(i=>['Ścianki boczne','Ścianki tylne','Półki'].includes(i.layer)).map(i=>({n:i.n.slice(0,60),layer:i.layer,x:i.x,y:i.y,z:i.z,w:i.w,h:i.h,d:i.d}));
fs.writeFileSync('/tmp/struct.json',JSON.stringify(out,null,0));
out.forEach((i,k)=>console.log(k,i.layer[8],i.n,'|',i.x,i.y,i.z,i.w,i.h,i.d));
