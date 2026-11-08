import pickle,math,collections,csv,os,json
parts,J=pickle.load(open('/tmp/joints.pkl','rb'))
P={p['code']:p for p in parts}
AX='xyz'
import re
PINNED=re.compile(r'^(KP|PP)2-[12]$')
SPACING=400; MARGIN=50; EDGE_DEPTH=35; D=5; DE=4
def axes_of(p):
    inpl=[a for a in AX if a!=p['t']]
    dim=lambda a:{'x':p['hi']['x']-p['lo']['x'],'y':p['hi']['y']-p['lo']['y'],'z':p['hi']['z']-p['lo']['z']}[a]
    inpl.sort(key=lambda a:(-dim(a),AX.index(a)))
    return inpl[0],inpl[1]
def right_handed(u,v,t):
    perm=[AX.index(u),AX.index(v),AX.index(t)]
    inv=sum(1 for i in range(3) for j in range(i+1,3) if perm[i]>perm[j])
    return inv%2==0
for p in parts:
    p['u'],p['v']=axes_of(p)
    p['DL']=p['hi'][p['u']]-p['lo'][p['u']]; p['SZ']=p['hi'][p['v']]-p['lo'][p['v']]
    p['rh']=right_handed(p['u'],p['v'],p['t'])
    p['holes']=[]   # (typ,'A'/'B'/'E', u,v, info)
def loc(p,a,val):
    """współrzędna lokalna widoku z lica A dla wartości modelu val na osi a (a = u lub v)"""
    x=val-p['lo'][a]
    if a==p['u'] and not p['rh']: x=p['DL']-x
    return x
def spread(lo,hi):
    L=hi-lo
    if L<150: return [ (lo+hi)/2 ]
    n=math.ceil((L-2*MARGIN)/SPACING)+1
    if n<2:n=2
    return [lo+MARGIN+i*(L-2*MARGIN)/(n-1) for i in range(n)]
# scal styki tych samych par
grp=collections.OrderedDict()
for j in J:
    f,e=j['face']['code'],j['edge']['code']
    if f.startswith('KT1') or e.startswith('KT1'): continue
    if PINNED.match(f) or PINNED.match(e): continue   # półki na wciskanych podpórkach: bez konfirmatów
    k=(f,e,j['n'],round(j['pos'],2))
    if k not in grp: grp[k]=dict(j)
    else:
        for a,(lo,hi) in j['ov'].items():
            lo0,hi0=grp[k]['ov'][a]; grp[k]['ov'][a]=(min(lo,lo0),max(hi,hi0))
rows=[]
for k,j in grp.items():
    face,edge,n=j['face'],j['edge'],j['n']
    oth=[a for a in AX if a!=n]
    ext={a:j['ov'][a] for a in oth}
    along=max(oth,key=lambda a:ext[a][1]-ext[a][0])
    across=[a for a in oth if a!=along][0]
    mid=(ext[across][0]+ext[across][1])/2
    pts=spread(*ext[along])
    # strona części licowej: otwór od strony przeciwnej do styku
    edge_above = abs(face['hi'][n]-j['pos'])<0.01   # część krawędziowa leży po stronie +n
    side='B' if edge_above else 'A'      # A = lico po stronie +t (t==n)
    for pv in pts:
        # współrzędne na części licowej (osie u,v tej części odpowiadają along/across)
        fu=face['u'];fv=face['v']
        val={along:pv,across:mid}
        fu_l=loc(face,fu,val[fu]);fv_l=loc(face,fv,val[fv])
        face['holes'].append(dict(kind='FACE',side=side,u=fu_l,v=fv_l,d=D,partner=edge['code'],axis_n=n))
        # część krawędziowa: kraniec na której osi?
        eu,ev=edge['u'],edge['v']
        # krawędź prostopadła do n: n jest osią u lub v części krawędziowej
        edge_at_hi = abs(edge['hi'][n]-j['pos'])<0.01
        e_l=loc(edge,along,pv)   # pozycja wzdłuż krawędzi
        # pozycja krawędzi w widoku
        if n==eu: ed_pos=loc(edge,eu,edge['hi'][eu] if edge_at_hi else edge['lo'][eu])
        else: ed_pos=loc(edge,ev,edge['hi'][ev] if edge_at_hi else edge['lo'][ev])
        edge['holes'].append(dict(kind='EDGE',n_axis_is_u=(n==eu),edge_coord=ed_pos,along=e_l,depth=EDGE_DEPTH,d=DE,partner=face['code'],
            into=( -1 if ed_pos>0 and (n==eu and ed_pos>=edge['DL']-0.01 or n==ev and ed_pos>=edge['SZ']-0.01) else 1)))

# --- podpórki półek (otwory Ø5 nieprzelotowe w KB2 i PB2) i kołki łączące KP z PP (Ø8 w czołach) ---
PIN_D=5; PIN_DEPTH=10; PIN_PITCH=32; PIN_RANGE=2
DOWEL_D=8; DOWEL_DEPTH=20
LEVELS={'KP2-1':922,'KP2-2':1355,'PP2-1':922,'PP2-2':1355}
for lvl in (922,1355):
    # KB2 (lico A = +x, od strony półki), kolumny przy z=233 i z=590
    for pc,side,zs in (('KB2','A',(233,590)),('PB2','B',(417,590))):
        p=P[pc]
        for z in zs:
            for k in range(-PIN_RANGE,PIN_RANGE+1):
                y=lvl-3+k*PIN_PITCH
                pu=p['u']; pv=p['v']
                val={'y':y,'z':z}
                p['holes'].append(dict(kind='FACE',side=side,u=loc(p,pu,val[pu]),v=loc(p,pv,val[pv]),d=PIN_D,depth=PIN_DEPTH,partner='podpórka',axis_n='x',pin=True))
# kołki w czołach par KP-PP (x=1371), 2 szt. w obszarze zakładki z 385..640
for kp,pp in (('KP1','PP1'),('KP2-1','PP2-1'),('KP2-2','PP2-2')):
    for code,xe in ((kp,1371),(pp,1371)):
        p=P[code]
        eu=(p['u']=='x'); assert 'x' in (p['u'],p['v'])
        ec=loc(p,'x',xe)
        L=p['DL'] if eu else p['SZ']
        into=-1 if ec>=L-0.01 else 1
        oa='z'
        for z in (435,590):
            p['holes'].append(dict(kind='EDGE',n_axis_is_u=eu,edge_coord=ec,along=loc(p,oa,z),depth=DOWEL_DEPTH,d=DOWEL_D,partner=(pp if code==kp else kp),into=into))

# --- nawierty pilotowe (środek) pod otwory wycinane samodzielnie: Ø5 nieprzelotowe, głębokość 5 mm, od strony wycinania ---
PILOT_D=5; PILOT_DEPTH=5
def pilot(code,side,y,other_axis,val):
    p=P[code]; pos={'y':y,other_axis:val}
    p['holes'].append(dict(kind='FACE',side=side,u=loc(p,p['u'],pos[p['u']]),v=loc(p,p['v'],pos[p['v']]),d=PILOT_D,depth=PILOT_DEPTH,partner='środek otworu wycinanego samodzielnie',axis_n='-',pin=False,pilot=True))
pilot('PT3','A',2409,'x',1616)   # Ø130 pod kanał, od strony wnętrza (+z)
pilot('L1B2','A',918,'z',245)    # wycięcie 100 x 100 pod gniazdko GN1 (y 868-968, z 192-292 od tyłu), od wnętrza (+x)
# kontrola kolizji
issues=[]
for p in parts:
    if p['code'].startswith('KT1'): continue
    fh=[h for h in p['holes'] if h['kind']=='FACE']
    eh=[h for h in p['holes'] if h['kind']=='EDGE']
    for i,a in enumerate(fh):
        for b in fh[i+1:]:
            if a['side']==b['side'] and math.hypot(a['u']-b['u'],a['v']-b['v'])<20: issues.append((p['code'],'dwa otwory licowe blisko',a['u'],a['v'],b['u'],b['v']))
    for i,a in enumerate(eh):
        for b in eh[i+1:]:
            if a['n_axis_is_u']==b['n_axis_is_u'] and abs(a['edge_coord']-b['edge_coord'])<1 and abs(a['along']-b['along'])<20: issues.append((p['code'],'dwa otwory krawędziowe blisko',a['along'],b['along']))
    for e in eh:
        for f in fh:
            # oś otworu krawędziowego
            if e['n_axis_is_u']:
                # otwór biegnie wzdłuż u, na v=e['along']
                if abs(f['v']-e['along'])<8:
                    lo=e['edge_coord'];hi=e['edge_coord']+e['into']*e['depth']
                    if min(lo,hi)-4<=f['u']<=max(lo,hi)+4: issues.append((p['code'],'otwór licowy przecina otwór krawędziowy',f['u'],f['v'],e['edge_coord'],e['along']))
            else:
                if abs(f['u']-e['along'])<8:
                    lo=e['edge_coord'];hi=e['edge_coord']+e['into']*e['depth']
                    if min(lo,hi)-4<=f['v']<=max(lo,hi)+4: issues.append((p['code'],'otwór licowy przecina otwór krawędziowy',f['u'],f['v'],e['edge_coord'],e['along']))
print('uwagi:',len(issues))
for i in issues[:30]: print(i)
pickle.dump(parts,open('/tmp/parts_holes.pkl','wb'))
tot=sum(len(p['holes']) for p in parts if not p['code'].startswith('KT1'))
print('otworów łącznie:',tot,'połączeń:',len(grp))
