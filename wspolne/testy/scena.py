"""Zrzut sceny 3D bez WebGL: otwiera stronę pomieszczenia w Chrome z atrapą Three.js
i zapisuje graf sceny po kolejnych akcjach w panelu (wariant, rozsunięcie, kolory, warstwy).

Użycie: python3 wspolne/testy/scena.py ŚCIEŻKA/index.html WYNIK.json
Zrzut i porównanie ze wzorcem: python3 wspolne/testy/scena.py ŚCIEŻKA/index.html WYNIK.json WZORZEC.json
Porównanie dwóch zrzutów: python3 wspolne/testy/scena.py --diff A.json B.json
Tekstury numerów (zależne od czcionek systemu) nie są porównywane.
"""
import json, os, sys

MOCK = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'three_mock.js')


def zrzut(html, out):
    from playwright.sync_api import sync_playwright
    mock = open(MOCK, encoding='utf-8').read()
    with sync_playwright() as p:
        exe = os.environ.get('CHROME', '/usr/bin/google-chrome')
        b = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None, args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': 1200, 'height': 800})
        errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.route('**/three.min.js', lambda r: r.fulfill(body=mock, content_type='application/javascript'))
        pg.route('**/OrbitControls.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
        pg.goto('file://' + os.path.abspath(html))
        pg.wait_for_timeout(300)
        res = {'bledy': errs}

        def snap(k):
            pg.wait_for_timeout(60)
            res[k] = pg.evaluate('window.__dump()')

        res['panel'] = pg.evaluate("""(()=>{var b=document.getElementById('panel');
            return {tekst:b.innerText, kontrolki:[].map.call(b.querySelectorAll('input,select,button'),
              e=>[e.tagName,e.id||'',e.type||'',e.checked===undefined?null:e.checked,e.value||'',e.getAttribute('data-v')||''])};})()""")
        snap('start')
        cbs = pg.evaluate("[].map.call(document.querySelectorAll('#panel input[type=checkbox]'),e=>e.id)")
        var_ids = [i for i in cbs if i and i.startswith('variant')]
        for v in var_ids:
            pg.check('#' + v)
            snap('wariant_' + v)
            pg.uncheck('#' + v)
        pg.evaluate("(()=>{var s=document.getElementById('explode');s.value=50;s.dispatchEvent(new Event('input'));})()")
        snap('rozsuniecie_50')
        pg.click('#explodeReset')
        pg.select_option('#boardColor', 'parts')
        pg.check('#frontsSolid')
        pg.select_option('#walls', 'solid')
        snap('kolory_sciany')
        pg.select_option('#walls', 'off')
        pg.evaluate("""(()=>{[].forEach.call(document.querySelectorAll('#layers label'),l=>{
            if(l.textContent==='Fronty'||l.textContent==='Konfirmaty'){var c=l.querySelector('input');c.checked=!c.checked;c.dispatchEvent(new Event('change'));}});})()""")
        snap('warstwy')
        for v in var_ids:
            pg.check('#' + v)
            snap('warstwy_wariant_' + v)
        for k in ('iso', 'front', 'top', 'left'):
            pg.click('[data-v=%s]' % k)
        res['bledy'] = errs
        b.close()
    json.dump(res, open(out, 'w'), ensure_ascii=False)
    print('zrzut:', out, 'obiektów:', len(res['start']), 'błędy JS:', len(errs))
    for e in errs:
        print('  ', e)
    return not errs


def diff(a, b):
    A = json.load(open(a)); B = json.load(open(b))
    ok = True
    for k in sorted(set(A) | set(B)):
        if A.get(k) != B.get(k):
            ok = False
            x, y = A.get(k), B.get(k)
            if isinstance(x, list) and isinstance(y, list):
                n = sum(1 for i in range(max(len(x), len(y))) if (x[i] if i < len(x) else None) != (y[i] if i < len(y) else None))
                print('RÓŻNICA', k, 'elementów:', len(x), len(y), 'różnych pozycji:', n)
                for i in range(max(len(x), len(y))):
                    xi = x[i] if i < len(x) else None; yi = y[i] if i < len(y) else None
                    if xi != yi:
                        print('  pierwsza:', i, '\n   A', xi, '\n   B', yi); break
            else:
                print('RÓŻNICA', k, '\n   A', str(x)[:600], '\n   B', str(y)[:600])
    print('IDENTYCZNE' if ok else 'SĄ RÓŻNICE')
    return ok


if __name__ == '__main__':
    if sys.argv[1] == '--diff':
        sys.exit(0 if diff(sys.argv[2], sys.argv[3]) else 1)
    ok = zrzut(sys.argv[1], sys.argv[2])
    if len(sys.argv) > 3:   # wzorzec do porównania
        ok = diff(sys.argv[3], sys.argv[2]) and ok
    sys.exit(0 if ok else 1)
