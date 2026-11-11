"""Arkusz nawiertów do samodzielnego wiercenia (PDF): strona tytułowa i jedna strona na typ formatki."""
import collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from otwory import loc

FACEWORD = {'x': ('PRAWA', 'LEWA'), 'y': ('GÓRNA', 'DOLNA'), 'z': ('PRZEDNIA (od strony pokoju)', 'TYLNA (do ściany)')}
OPIS = ("Każda strona = jeden typ formatki. Wymiary w mm, liczone od lewej (U) i dołu (V) rysunku.\n"
    "Rysunek jest widokiem z lica A. Lico A, lico B i krawędź oklejona są opisane na każdej stronie.\n"
    "Czerwone kółka: otwory Ø5 przelotowo w licu A (w kalkulatorze: Przód); po dostawie poszerzyć do Ø7. Niebieskie: lico B (w kalkulatorze: Tył).\n"
    "Zielone paski: otwory w czole Ø4 x 35 mm (cienkie) lub Ø8 x 20 mm pod kołki (grube), w połowie grubości płyty (kalkulator: Wiercenie w czole). Czerwone/niebieskie przerywane: otwory Ø5 NIEPRZELOTOWE, głębokość 10 mm, pod wciskane podpórki półek.\n"
    "Pomarańczowa gruba krawędź: oklejona (przód mebla). Kody części zgodne z numeracją w wizualizacji 3D.\n"
    "W kalkulatorze: SZER = DL, WYS = SZ; X, Y od lewego dolnego rogu widoku z lica A; krawędzie 1 góra, 2 prawa, 3 dół, 4 lewa.\n"
    "Zawiasy frontów: szablony Front lewy/prawy w kalkulatorze, w tym arkuszu ich nie ma. Tabela do wpisania: kalkulator_nawierty.csv.")


def sig(p):
    hs = []
    for h in p['holes']:
        if h['kind'] == 'FACE':
            hs.append(('F', h['side'], round(h['u'], 1), round(h['v'], 1), h.get('depth', 0)))
        else:
            hs.append(('E', h['n_axis_is_u'], round(h['edge_coord'], 1), round(h['along'], 1), h.get('d', 4)))
    return (round(p['DL'], 1), round(p['SZ'], 1), tuple(sorted(hs)), 'sub' in p)


def band_edge(p, R):
    """krawędź oklejona = przód (maks. z), jeśli leży w płaszczyźnie płyty; zwraca (oś_lok, wartość)"""
    if p['code'].startswith(R.BEZ_OKLEINY_PREFIKSY):
        return None
    for ax in ('u', 'v'):
        if p[ax] == 'z':
            return (ax, loc(p, 'z', p['hi']['z']))
    return None


def zapisz(parts, R, sciezka, log=print):
    faceword = getattr(R, 'PDF_LICA', FACEWORD)
    opis = getattr(R, 'PDF_OPIS', OPIS)
    groups = collections.OrderedDict()
    for p in parts:
        if not p['holes'] or R.pomijaj_czesc(p):
            continue
        groups.setdefault(sig(p), []).append(p)
    # bez daty w metadanych: ten sam model daje ten sam plik (porównywanie w teście regresji)
    with PdfPages(sciezka, metadata={'CreationDate': None}) as pdf:
        fig = plt.figure(figsize=(11.7, 8.3)); fig.text(.05, .9, 'ARKUSZ NAWIERTÓW POD KONFIRMATY (samodzielne wiercenie)', fontsize=18, weight='bold')
        fig.text(.05, .55, opis, fontsize=11, va='top'); pdf.savefig(fig); plt.close(fig)
        for g, pl in groups.items():
            p = pl[0]; DL, SZ = p['DL'], p['SZ']
            name = p['code'].split('-')[0] if len(pl) > 1 else p['code']
            fig = plt.figure(figsize=(11.7, 8.3)); ax = fig.add_axes([.06, .2, .88, .6])
            if 'sub' in p:   # półka w kształcie L z dwóch prostokątów
                sub = sorted(p['sub'], key=lambda q: q['x']); w1 = sub[0]['w']; dt = sub[0]['d']; dr = sub[1]['d']
                pts = [(0, 0), (w1, 0), (w1, dt - dr), (DL, dt - dr), (DL, dt), (0, dt)]
                if not p['rh']:
                    pts = [(DL - a, b) for a, b in pts]
                ax.add_patch(plt.Polygon(pts, fill=False, ec='k', lw=1.5))
            else:
                ax.add_patch(plt.Rectangle((0, 0), DL, SZ, fill=False, ec='k', lw=1.5))
            be = band_edge(p, R)
            if be:
                axn, val = be
                if axn == 'u':
                    ax.plot([val, val], [0, SZ], color='orange', lw=5)
                else:
                    ax.plot([0, DL], [val, val], color='orange', lw=5)
            for h in p['holes']:
                if h['kind'] == 'FACE':
                    c = 'r' if h['side'] == 'A' else 'b'
                    ax.add_patch(plt.Circle((h['u'], h['v']), 6, fc='none', ec=c, lw=1.2, ls='--' if h.get('depth') else '-'))
                    ax.annotate('%g | %g' % (round(h['u'], 1), round(h['v'], 1)), (h['u'], h['v']), xytext=(4, 6), textcoords='offset points', fontsize=5.5, color=c)
                else:
                    ec = h['edge_coord']; al = h['along']; dp = h['depth'] * h['into']
                    if h['n_axis_is_u']:
                        ax.plot([ec, ec + dp], [al, al], color='g', lw=3 if h['d'] < 8 else 6); ax.annotate('%g' % round(al, 1), (ec, al), xytext=(2, 4), textcoords='offset points', fontsize=5.5, color='g')
                    else:
                        ax.plot([al, al], [ec, ec + dp], color='g', lw=3 if h['d'] < 8 else 6); ax.annotate('%g' % round(al, 1), (al, ec), xytext=(2, 4), textcoords='offset points', fontsize=5.5, color='g')
            ax.set_xlim(-30, DL + 30); ax.set_ylim(-30, SZ + 30); ax.set_aspect('equal'); ax.axis('off')
            a_word, b_word = faceword[p['t']]
            codes = ', '.join(q['code'] for q in pl)
            fig.text(.06, .93, '%s' % name, fontsize=22, weight='bold')
            fig.text(.06, .88, 'Kody: %s    SZT: %d    WYMIAR: %g X %g MM, PŁYTA 18 MM' % (codes, len(pl), DL, SZ), fontsize=11)
            fig.text(.06, .12, 'LICO A = strona %s.   LICO B = strona %s.' % (a_word, b_word), fontsize=11)
            fig.text(.06, .085, 'Liczby przy otworach: U | V w mm od lewego i dolnego brzegu rysunku. Zielone: odległość wzdłuż krawędzi od zera, Ø4, głębokość 35 mm.', fontsize=9)
            fig.text(.06, .055, 'Pomarańczowa krawędź = oklejona (przód mebla).' if be else 'Bez okleiny.', fontsize=9)
            W = {'x': ('PRAWEJ ŚCIANY', 'LEWEJ ŚCIANY'), 'y': ('GÓRY', 'DOŁU'), 'z': ('PRZODU (POKÓJ)', 'TYŁU (ŚCIANA)')}
            du = W[p['u']][1 if not p['rh'] else 0]; dv = W[p['v']][0]
            fig.text(.06, .025, 'OŚ U (w prawo na rysunku) rośnie w stronę %s.  OŚ V (do góry na rysunku) rośnie w stronę %s.' % (du, dv), fontsize=9)
            pdf.savefig(fig); plt.close(fig)
    log(len(groups), 'stron')
    return len(groups)
