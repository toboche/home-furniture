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
            if h.get('pin'):
                # nieprzelotowy, od lica po stronie półki (A = +t)
                top=p['hi'][t] if h['side']=='A' else p['lo'][t]
                sgn=-1 if h['side']=='A' else 1
                c=dict(pos);c[t]=top+sgn*h['depth']/2
                cyl('Otwór Ø5 x 10 pod podpórkę w %s'%p['code'],'Otwory','xyz'[0] if t=='x' else t,c,h['d']/2,h['depth']+0.6,DARK);npin+=1
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
block="/* FASTENERS BEGIN (generowane: etap6/gen_fasteners.py, nie edytować ręcznie) */\n"+"\n".join(items)+"\n  /* FASTENERS END */"
if len(sys.argv)>1:
    s=open(sys.argv[1],encoding='utf-8').read()
    if 'FASTENERS BEGIN' in s:
        s=re.sub(r"/\* FASTENERS BEGIN.*?/\* FASTENERS END \*/",lambda m:block,s,flags=re.S)
    else:
        i=s.index("\n];",s.index("var ITEMS"))
        s=s[:i]+"\n"+block+s[i:]
    open(sys.argv[1],'w',encoding='utf-8').write(s)
