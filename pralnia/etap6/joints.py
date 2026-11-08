# Wykrywanie połączeń konfirmatowych z modelu 3D i generowanie nawiertów.
import json,re,math,collections,sys
S=json.load(open('/tmp/struct.json'))
def code_of(it):
    m=re.match(r'^([A-Z0-9]+(?:-[0-9]+)?):',it['n'])
    return m.group(1) if m else None
def module_of(it):
    cx=it['x']+it['w']/2; cy=it['y']+it['h']/2
    if cx<620: return 'L1' if cy<1743 else 'L2'
    if cx<1215: return 'NW'
    return 'RD' if cy<1743-0.01 else 'RB'
parts=[]
for it in S:
    c=code_of(it)
    assert c,it['n']
    p=dict(it);p['code']=c;p['mod']=module_of(it)
    parts.append(p)
for p in parts:
    dims={'x':p['w'],'y':p['h'],'z':p['d']}
    p['t']=[a for a in 'xyz' if abs(dims[a]-18)<1e-6][0]
    lo={'x':p['x'],'y':p['y'],'z':p['z']}
    p['lo']=lo;p['hi']={a:lo[a]+dims[a] for a in 'xyz'}
def boxes(p):
    if 'sub' in p:
        return [dict(lo={'x':q['x'],'y':q['y'],'z':q['z']},hi={'x':q['x']+q['w'],'y':q['y']+q['h'],'z':q['z']+q['d']}) for q in p['sub']]
    return [dict(lo=p['lo'],hi=p['hi'])]
EPS=0.01
contacts=[]
for i,A in enumerate(parts):
    for B in parts[i+1:]:
        if A['mod']!=B['mod']: continue
        for ba in boxes(A):
            for bb in boxes(B):
                for n in 'xyz':
                    # płaszczyzna styku prostopadła do n
                    for (s1,s2) in ((ba,bb),(bb,ba)):
                        if abs(s1['hi'][n]-s2['lo'][n])<EPS:
                            ov={}
                            ok=True
                            for a in 'xyz':
                                if a==n: continue
                                lo=max(ba['lo'][a],bb['lo'][a]);hi=min(ba['hi'][a],bb['hi'][a])
                                if hi-lo<5: ok=False;break
                                ov[a]=(lo,hi)
                            if ok: contacts.append((A,B,n,(s1['hi'][n]),ov))
print('styków:',len(contacts))
J=[]
for A,B,n,pos,ov in contacts:
    # część "licowa" ma oś cienką = n
    fa=[X for X in (A,B) if X['t']==n]
    if len(fa)!=1: continue  # płyta na płycie lub krawędź do krawędzi
    face=fa[0];edge=B if face is A else A
    J.append(dict(face=face,edge=edge,n=n,pos=pos,ov=ov))
print('połączeń konfirmatowych:',len(J))
import pickle
pickle.dump((parts,J),open('/tmp/joints.pkl','wb'))
cnt=collections.Counter()
for j in J: cnt[j['face']['code']]+=1; cnt[j['edge']['code']]+=1
for p in parts: print(p['code'],p['mod'],'t=',p['t'],'połączeń:',cnt[p['code']])
