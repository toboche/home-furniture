# Generuje elementy łączników do wizualizacji 3D: otwory, konfirmaty, kołki, otwory pod podpórki.
# Wejście: /tmp/parts_holes.pkl (po holes.py). Wynik: wstawiany do pralnia_3d.html między znacznikami FASTENERS BEGIN/END.
# Użycie: python3 gen_fasteners.py /ścieżka/do/pralnia_3d.html
import pickle,sys,re
parts=pickle.load(open('/tmp/parts_holes.pkl','rb'))
def inv(p,a,x):
    """współrzędna lokalna widoku z lica A -> współrzędna modelu na osi a (a = u lub v)"""
    if a==p['u'] and not p['rh']: return p['lo'][a]+p['DL']-x
    return p['lo'][a]+x
def f(x): return ('%.2f'%x).rstrip('0').rstrip('.')
items=[]
def cyl(n,layer,ax,center,r,ln,c):
    items.append("  {t:'cyl3',n:'%s',layer:'%s',ax:'%s',px:%s,py:%s,pz:%s,r:%s,len:%s,c:0x%06x},"%(n,layer,ax,f(center['x']),f(center['y']),f(center['z']),f(r),f(ln),c))
DARK=0x15181b; STEEL=0xc7a008; HEAD=0xd8b310; WOOD=0xb08a5b
nconf=nhole=nedge=ndow=npin=0
seen_dowel=set()
for p in parts:
    if 'sub' in p or p['code'].startswith('KT1'): continue
    t=p['t'];tn=p['hi'][t]-p['lo'][t];tm=(p['hi'][t]+p['lo'][t])/2
    for h in p['holes']:
        if h['kind']=='FACE':
            pos={p['u']:inv(p,p['u'],h['u']),p['v']:inv(p,p['v'],h['v'])}
            if h.get('pin') or h.get('pilot'):
                # nieprzelotowy, od lica po stronie półki (A = +t)
                top=p['hi'][t] if h['side']=='A' else p['lo'][t]
                sgn=-1 if h['side']=='A' else 1
                c=dict(pos);c[t]=top+sgn*h['depth']/2
                cyl(('Nawiert środka Ø5 x 5 pod otwór wycinany samodzielnie w %s'%p['code']) if h.get('pilot') else ('Otwór Ø5 x 10 pod podpórkę w %s'%p['code']),'Otwory',t,c,h['d']/2,h['depth']+0.6,DARK);npin+=1
                continue
            c=dict(pos);c[t]=tm
            cyl('Otwór Ø5 przelotowy w %s (pod konfirmat do %s)'%(p['code'],h['partner']),'Otwory',t,c,h['d']/2,tn+0.6,DARK);nhole+=1
            # konfirmat: od lica zewnętrznego w stronę części krawędziowej (50 mm)
            outer=p['lo'][t] if h['side']=='B' else p['hi'][t]
            dr=1 if h['side']=='B' else -1
            c2=dict(pos);c2[t]=outer+dr*25
            cyl('Konfirmat 7 x 50: %s → %s'%(p['code'],h['partner']),'Konfirmaty',t,c2,3.5,50,STEEL)
            c3=dict(pos);c3[t]=outer-dr*1
            cyl('Łeb konfirmatu: %s → %s'%(p['code'],h['partner']),'Konfirmaty',t,c3,5,2,HEAD);nconf+=1
        else:
            a_e=p['u'] if h['n_axis_is_u'] else p['v']      # oś, wzdłuż której idzie otwór
            a_a=p['v'] if h['n_axis_is_u'] else p['u']
            e0=inv(p,a_e,h['edge_coord']);e1=inv(p,a_e,h['edge_coord']+h['into']*h['depth'])
            c={a_e:(e0+e1)/2,a_a:inv(p,a_a,h['along']),t:tm}
            if h['d']>=8:
                cyl('Otwór Ø8 x 20 pod kołek w %s (do %s)'%(p['code'],h['partner']),'Otwory',a_e,c,h['d']/2,abs(e1-e0),DARK);ndow+=1
                key=tuple(sorted((p['code'],h['partner'])))+(round(c[a_a]),)
                if key not in seen_dowel:
                    seen_dowel.add(key)
                    cyl('Kołek drewniany Ø8 x 40: %s + %s'%key[:2],'Kołki',a_e,dict(c,**{a_e:e0}),4,40,WOOD)
            else:
                cyl('Otwór Ø4 x 35 w %s (czoło, konfirmat z %s)'%(p['code'],h['partner']),'Otwory',a_e,c,h['d']/2,abs(e1-e0),DARK);nedge+=1
print('konfirmatów',nconf,'otw. licowych',nhole,'otw. czołowych',nedge,'otw. pod kołki',ndow,'otw. pod podpórki',npin,'kołków',len(seen_dowel))

# --- zawiasy: puszki Ø35 x 13 w tylnej stronie frontów i otwory pod wkręty płytek (2 szt., rozstaw 32, 37 mm od przedniej krawędzi ściany) ---
if len(sys.argv)>1:
    src=open(sys.argv[1],encoding='utf-8').read()
    def rows(layer):
        out=[]
        for m in re.finditer(r"\{n:'([^']*)',layer:'%s',x:([\d.]+),y:([\d.]+),z:([\d.]+),w:([\d.]+),h:([\d.]+)"%layer,src):
            out.append((m.group(1),float(m.group(2)),float(m.group(3)),float(m.group(5)),float(m.group(6))))
        return out
    fronts=[(n,x,y,w,h) for (n,x,y,w,h) in rows('Fronty') if re.match(r'F\d+:',n)]
    nh=npl=0
    for (n,x,y,w,h) in rows('Zawiasy'):
        cx,cy=x+17.5,y+17.5
        fr=[f for f in fronts if f[1]<=cx<=f[1]+f[3] and f[2]<=cy<=f[2]+f[4]][0]
        code=fr[0].split(':')[0]
        right = cx>fr[1]+fr[3]/2
        cyl('Otwór zawiasu Ø35 x 13 w %s'%code,'Otwory','z',dict(x=cx,y=cy,z=640+6.5-0.3),17.5,13.6,DARK);nh+=1
        edge=fr[1]+fr[3] if right else fr[1]
        if code=='F5':
            wall='LF5';xs,xe=1500,1512
        else:
            tgt=edge+1.5 if right else edge-1.5
            cand=[p for p in parts if p['t']=='x' and p['lo']['y']<=cy<=p['hi']['y'] and p['hi']['z']>=620 and abs((p['hi']['x'] if right else p['lo']['x'])-tgt)<0.6]
            assert cand,(code,cy)
            w_=cand[0];wall=w_['code']
            inner=w_['lo']['x'] if right else w_['hi']['x']
            xs,xe=(inner,inner+12) if right else (inner-12,inner)
        for dy in (-16,16):
            cyl('Otwór pod wkręt płytki zawiasu %s w %s (nawiert opcjonalny)'%(code,wall),'Otwory','x',dict(x=(xs+xe)/2,y=cy+dy,z=(621 if code=='F5' else 603)),2,12,DARK);npl+=1
    print('puszki',nh,'otwory płytek',npl)

block="/* FASTENERS BEGIN (generowane: etap6/gen_fasteners.py, nie edytować ręcznie) */\n"+"\n".join(items)+"\n  /* FASTENERS END */"
if len(sys.argv)>1:
    s=open(sys.argv[1],encoding='utf-8').read()
    if 'FASTENERS BEGIN' in s:
        s=re.sub(r"/\* FASTENERS BEGIN.*?/\* FASTENERS END \*/",lambda m:block,s,flags=re.S)
    else:
        i=s.index("\n];",s.index("var ITEMS"))
        s=s[:i]+"\n"+block+s[i:]
    open(sys.argv[1],'w',encoding='utf-8').write(s)
