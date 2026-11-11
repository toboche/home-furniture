# Klasyfikacja łbów konfirmatów: widoczne (zaślepka) i ukryte (przy ścianie pokoju, sąsiednim module, maszynie, pionie).
# Użycie: python3 zaslepki.py /ścieżka/do/pralnia_3d.html  (po holes.py)
import pickle,re,sys,json,collections
parts=pickle.load(open('/tmp/parts_holes.pkl','rb'))
src=open(sys.argv[1],encoding='utf-8').read()
def inv(p,a,x):
    if a==p['u'] and not p['rh']: return p['lo'][a]+p['DL']-x
    return p['lo'][a]+x
boxes=[]
for p in parts:
    boxes.append((p['code'],p['lo'],p['hi']))
for m in re.finditer(r"\{n:'([^']*)',layer:'(Maszyny|Pion i gzyms|Fronty)',x:([-\d.]+),y:([-\d.]+),z:([-\d.]+),w:([\d.]+),h:([\d.]+),d:([\d.]+)",src):
    n=m.group(1);x,y,z,w,h,d=map(float,m.groups()[2:])
    boxes.append((n[:20],{'x':x,'y':y,'z':z},{'x':x+w,'y':y+h,'z':z+d}))
TOL=6.0     # mm: łeb zasłonięty, jeśli 6 mm od lica jest inna bryła (szczeliny do 6 mm są niewidoczne)
ROOM=dict(x=6.0,z=6.0)   # ściana pokoju: lewa (x=0), tylna (z=0)
CEIL=2661-12
res=collections.Counter(); vis=[]; hid=[]
for p in parts:
    if 'sub' in p or p['code'].startswith('KT1'): continue
    t=p['t']
    for h in p['holes']:
        if h['kind']!='FACE' or h.get('pin') or h.get('pilot'): continue
        pos={p['u']:inv(p,p['u'],h['u']),p['v']:inv(p,p['v'],h['v'])}
        outer=p['lo'][t] if h['side']=='B' else p['hi'][t]
        sg=-1 if h['side']=='B' else 1
        q=dict(pos);q[t]=outer+sg*TOL
        hidden=False
        if q['x']<ROOM['x'] and t=='x': hidden=True
        if q['z']<ROOM['z'] and t=='z': hidden=True
        if t=='x' and q['x']>1733: hidden=True   # prawa ściana pokoju (x=1739)
        if t=='y' and q['y']>CEIL: hidden=True
        for c,lo,hi in boxes:
            if c==p['code']: continue
            if all(lo[a]-1e-6<=q[a]<=hi[a]+1e-6 for a in 'xyz'): hidden=True;break
        (hid if hidden else vis).append((p['code'],h['partner'],round(q['x']),round(q['y']),round(q['z'])))
        res['ukryte' if hidden else 'widoczne']+=1
print(dict(res))
by=collections.Counter(v[0] for v in vis)
print('widoczne wg części:',dict(by)); print(sorted(set(vis)))
json.dump(dict(visible=len(vis),hidden=len(hid)),open('/tmp/zaslepki.json','w'))
