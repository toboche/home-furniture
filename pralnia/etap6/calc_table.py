import pickle,collections,csv
parts=pickle.load(open('/tmp/parts_holes.pkl','rb'))
def loc(p,a,val):
    x=val-p['lo'][a]
    if a==p['u'] and not p['rh']: x=p['DL']-x
    return x
def sig(p):
    hs=[]
    for h in p['holes']:
        if h['kind']=='FACE': hs.append(('F',h['side'],round(h['u'],1),round(h['v'],1),h.get('depth',0),h.get('d',5)))
        else: hs.append(('E',h['n_axis_is_u'],round(h['edge_coord'],1),round(h['along'],1),h.get('d',4),h.get('depth',35)))
    return (round(p['DL'],1),round(p['SZ'],1),tuple(sorted(hs)),p['hi']['z'] if False else 0)
def front_edge(p):
    if p['code'].startswith(('L1T','L2T','NWT','PT','KT')): return None
    for ax in ('u','v'):
        if p[ax]=='z':
            val=loc(p,'z',p['hi']['z'])
            if ax=='u': return 2 if abs(val-p['DL'])<0.01 else 4
            return 1 if abs(val-p['SZ'])<0.01 else 3
    return None
rows=[]
groups=collections.OrderedDict()
for p in parts:
    if not p['holes'] or p['code'].startswith('KT1'): continue
    k=(sig(p),front_edge(p))
    groups.setdefault(k,[]).append(p)
out=[['LP','FORMATKA','KODY','SZT','SZER=DL','WYS=SZ','OKLEJ KRAWEDZ NR','RODZAJ','POWIERZCHNIA/KRAWEDZ','X lub ODLEGLOSC OD 0','Y','SREDNICA','GLEBOKOSC']]
for i,(k,pl) in enumerate(groups.items(),1):
    p=pl[0];nm=p['code'].split('-')[0] if len(pl)>1 and all(q['code'].split('-')[0]==p['code'].split('-')[0] for q in pl) else p['code']
    fe=k[1]
    base=[i,nm,', '.join(q['code'] for q in pl),len(pl),p['DL'],p['SZ'],fe or 'brak']
    first=True
    for h in sorted(p['holes'],key=lambda h:(h['kind']!='FACE',h.get('side',''),h.get('u',h.get('edge_coord',0)),h.get('v',h.get('along',0)))):
        if h['kind']=='FACE':
            out.append((base if first else ['']*7)+['PLASZCZYZNA','Przód' if h['side']=='A' else 'Tył',round(h['u'],1),round(h['v'],1),h.get('d',5),h.get('depth','przelotowo')])
        else:
            if h['n_axis_is_u']: en=4 if h['edge_coord']<1 else 2
            else: en=3 if h['edge_coord']<1 else 1
            out.append((base if first else ['']*7)+['CZOŁO','Krawędź %d'%en,round(h['along'],1),'',h.get('d',4),h.get('depth',35)])
        first=False
with open('kalkulator_nawierty.csv','w',newline='',encoding='utf-8-sig') as f:
    csv.writer(f,delimiter=';').writerows(out)
print(len(groups),'typów formatek,',len(out)-1,'wierszy')
pickle.dump(groups,open('/tmp/groups.pkl','wb'))
