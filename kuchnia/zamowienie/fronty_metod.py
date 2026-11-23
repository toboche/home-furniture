"""Fronty szuflad do istniejących szafek IKEA METOD (MAXIMERA): lista do kalkulatora meble.pl
i poglądowy rysunek dopasowania usłojenia do maila.
Uruchom z katalogu głównego: python3 kuchnia/zamowienie/fronty_metod.py
Źródło wymiarów i nawiertów: kuchnia/ustalenia.md (2026-11-15) i poprzednie zamówienie w meble.pl."""
import csv, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

TU = os.path.dirname(os.path.abspath(__file__))
SZER = 597                     # 600 - 3
X_OTW = (32, SZER - 32)        # od lewej krawędzi, widok od tyłu (jak w kalkulatorze)
Y_PARY = {'niska': (39, 58), 'srednia': (39, 58, 117, 136), 'wysoka': (39, 58, 117, 136, 185, 204)}
D_OTW, GL_OTW = 5, 12          # Ø5, głębokość 12 (2026-11-23 po audycie v6; było 13, w poprzednim zamówieniu 10)

# (kod, nazwa w kalkulatorze (max 20 znaków), kolumna, pozycja od góry, wysokość, szuflada)
FRONTY = [
    ('FM1', 'usłojenie 21a', 1, 1, 142, 'niska'),
    ('FM2', 'usłojenie 21b', 1, 2, 397, 'wysoka'),
    ('FM3', 'usłojenie 21c', 1, 3, 397, 'wysoka'),
    ('FM4', 'usłojenie 22a', 2, 1, 197, 'srednia'),
    ('FM5', 'usłojenie 22b', 2, 2, 197, 'srednia'),
    ('FM6', 'usłojenie 22c', 2, 3, 397, 'wysoka'),
]


def lista():
    with open(os.path.join(TU, 'fronty_metod.csv'), 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['KOD', 'NAZWA W KALKULATORZE', 'SZER', 'WYS', 'SZT', 'SŁOJE', 'OKLEINA', 'SZUFLADA',
                    'NAWIERTY (TYŁ, X;Y od lewego dolnego rogu widoku od tyłu, Ø5 x 12)'])
        for kod, nazwa, kol, poz, wys, szu in FRONTY:
            otw = ' | '.join('%d;%d' % (x, y) for x in X_OTW for y in Y_PARY[szu])
            w.writerow([kod, nazwa, SZER, wys, 1, 'na wysokość', '0,8 mm H3710, wszystkie krawędzie, kryjące długie',
                        szu.upper(), otw])


def rysunek():
    fig, ax = plt.subplots(figsize=(8.27, 11.69))
    ax.set_xlim(-150, 1550); ax.set_ylim(-260, 1300); ax.set_aspect('equal'); ax.axis('off')
    ax.text(700, 1260, 'Fronty szuflad METOD – dopasowanie usłojenia (widok od przodu)', ha='center', fontsize=12, weight='bold')
    ax.text(700, 1215, 'Egger H3710 ST12 Orzech Carini naturalny 18 mm, słoje na wysokość, okleina 0,8 mm', ha='center', fontsize=9)
    ax.text(700, 1180, 'Fronty z jednej kolumny wyciąć kolejno z jednego pasa płyty, w tej kolejności od góry,', ha='center', fontsize=9)
    ax.text(700, 1150, 'tak aby usłojenie przechodziło ciągle z frontu na front (jak przy usłojeniu 1a-1c, 2ab-2e).', ha='center', fontsize=9)
    for kol, x0 in ((1, 0), (2, 800)):
        fr = [f for f in FRONTY if f[2] == kol]
        y = 1000
        ax.text(x0 + SZER / 2, 1060, 'Kolumna %d' % kol, ha='center', fontsize=11, weight='bold')
        for kod, nazwa, _, poz, wys, szu in fr:
            yb = y - wys
            ax.add_patch(Rectangle((x0, yb), SZER, wys, fill=True, fc='#c9a27a', ec='black', lw=1))
            for gx in range(x0 + 40, x0 + SZER, 70):
                ax.plot([gx, gx + 6], [yb + 8, y - 8], color='#8b6a4f', lw=0.6)
            ax.text(x0 + SZER / 2, yb + wys / 2 + 18, nazwa, ha='center', va='center', fontsize=10, weight='bold')
            ax.text(x0 + SZER / 2, yb + wys / 2 - 18, '%d x %d (szer. x wys.)' % (SZER, wys), ha='center', va='center', fontsize=8)
            ax.text(x0 - 12, yb + wys / 2, str(poz), ha='right', va='center', fontsize=9)
            y = yb - 3
        ax.add_patch(FancyArrowPatch((x0 + SZER + 40, 990), (x0 + SZER + 40, y + 10), arrowstyle='<->', mutation_scale=10))
        ax.text(x0 + SZER + 55, (990 + y) / 2, 'ciągłe\nusłojenie', fontsize=8, va='center')
    ax.text(0, -40, 'Nawierty (tył frontu, wierci sklep): Ø5 x 12, x = 32 i 565 od lewej krawędzi (widok od tyłu),', fontsize=8.5)
    ax.text(0, -75, 'y od dolnej krawędzi: szuflada niska 39, 58; średnia 39, 58, 117, 136; wysoka 39, 58, 117, 136, 185, 204.', fontsize=8.5)
    ax.text(0, -110, 'Otworów na gałki nie wiercić. Szczeliny między frontami na rysunku: 3 mm (poglądowo).', fontsize=8.5)
    ax.text(0, -145, 'Nowa część mebli: tych kolumn nie ma na rysunku z poprzedniego zamówienia.', fontsize=8.5)
    fig.savefig(os.path.join(TU, 'fronty_metod_rysunek.pdf'))
    fig.savefig(os.path.join(TU, 'fronty_metod_rysunek.png'), dpi=110)


if __name__ == '__main__':
    lista(); rysunek()
