"""Wersja jednoplikowa widoku 3D: index.html pomieszczenia z wklejonymi viewer.css, model.js, laczniki.gen.js i viewer.js.
Biblioteka Three.js nadal ładuje się z CDN (wymaga internetu)."""
import os, re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def zapisz(kat, laczniki_gen, cel):
    html = open(os.path.join(kat, 'index.html'), encoding='utf-8').read()

    def plik(src):
        if os.path.basename(src) == 'laczniki.gen.js':
            return laczniki_gen
        return os.path.normpath(os.path.join(kat, src))

    def css(m):
        return '<style>\n' + open(plik(m.group(1)), encoding='utf-8').read() + '</style>'

    def js(m):
        src = m.group(1)
        if src.startswith('http'):
            return m.group(0)
        return '<script>\n' + open(plik(src), encoding='utf-8').read().replace('</script', '<\\/script') + '</script>'

    html = re.sub(r'<link rel="stylesheet" href="([^"]+)">', css, html)
    html = re.sub(r'<script src="([^"]+)"></script>', js, html)
    html = re.sub(r'<!--.*?-->\n?', '', html, flags=re.S)
    with open(cel, 'w', encoding='utf-8') as fh:
        fh.write(html)
