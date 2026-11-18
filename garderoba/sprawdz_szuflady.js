// Sprawdza, czy każda szuflada otwiera się na pełny wysuw, gdy pozostałe są zamknięte, i niczego nie zahacza.
// Użycie: node garderoba/sprawdz_szuflady.js   (wynik 0 = brak kolizji)
const fs = require('fs'), vm = require('vm'), path = require('path');
const ctx = {window: {}}; vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname, 'model.js'), 'utf8') + ';this.M=HF_MODEL;', ctx);
const M = ctx.M, R = M.room, items = M.items.filter(Boolean);
// bryły zamysłu (całe objętości szafek) nie są przeszkodą; płyty (wieniec) tak
const OBJETOSCI = /^(Szafki na wprost|Szafka po lewej) \(zamysł\)$/;
const box = it => ({x0: it.x, x1: it.x + it.w, y0: it.y, y1: it.y + it.h, z0: it.z, z1: it.z + it.d, n: it.n});
const przeszkody = items.filter(it => !it.t && !it.sz && !(OBJETOSCI.test(it.layer) && !/wieniec/.test(it.n))).map(box)
  .concat((M.boki || []).map(box));
const kolizja = (a, b) => ['x', 'y', 'z'].every(k => Math.min(a[k + '1'], b[k + '1']) - Math.max(a[k + '0'], b[k + '0']) > 0.01);
const kody = [...new Set(items.filter(i => i.sz).map(i => i.sz))];
let bledy = 0;
for (const kod of kody) {
  const ruch = items.filter(i => i.sz === kod), os = ruch[0].ruch, skok = ruch[0].skok;
  const inne = items.filter(i => i.sz && i.sz !== kod).map(box);      // pozostałe szuflady zamknięte
  let min = Infinity, kol = new Set();
  for (let t = 0; t <= skok; t += 5) {
    for (const it of ruch) {
      const b = box(it); b[os + '0'] += t; b[os + '1'] += t;
      if (b.x0 < 0 || b.z0 < 0 || b.x1 > R.W || b.z1 > R.D) kol.add(`${it.n} poza pokojem przy wysuwie ${t}`);
      for (const p of przeszkody.concat(inne)) if (kolizja(b, p)) kol.add(`${it.n} ↔ ${p.n} przy wysuwie ${t}`);
      // najmniejszy luz do przeszkód w kierunkach poprzecznych (dla czytelności raportu)
      for (const p of przeszkody.concat(inne)) {
        const ov = k => Math.min(b[k + '1'], p[k + '1']) - Math.max(b[k + '0'], p[k + '0']);
        const kier = ['x', 'y', 'z'].filter(k => k !== os);
        if (ov(os) > 0.01 && ov(kier[0]) > 0.01 && ov(kier[1]) <= 0.01) min = Math.min(min, -ov(kier[1]));
        if (ov(os) > 0.01 && ov(kier[1]) > 0.01 && ov(kier[0]) <= 0.01) min = Math.min(min, -ov(kier[0]));
      }
    }
  }
  console.log(`${kod}: wysuw ${skok} wzdłuż ${os.toUpperCase()}: ` + (kol.size ? 'KOLIZJE' : `bez kolizji (najmniejszy luz boczny ${min.toFixed(1)} mm)`));
  for (const k of [...kol].slice(0, 10)) console.log('   ', k);
  bledy += kol.size;
}
// jednoczesne otwarcie dwóch szuflad: tylko ostrzeżenie (szuflady narożne SZ1 i SZ2 wysuwają się w ten sam narożnik)
const przesun = (it, t) => { const b = box(it); b[it.ruch + '0'] += t; b[it.ruch + '1'] += t; return b; };
for (let i = 0; i < kody.length; i++) for (let j = i + 1; j < kody.length; j++) {
  const a = items.filter(it => it.sz === kody[i]), b = items.filter(it => it.sz === kody[j]);
  // najmniejszy wysuw drugiej szuflady, przy którym zahacza o pierwszą wysuniętą do końca (i odwrotnie)
  const prog = (ruch, stoi) => { for (let t = 0; t <= ruch[0].skok; t += 5)
    if (ruch.some(r => stoi.some(s => kolizja(przesun(r, t), przesun(s, s.skok))))) return t; return null; };
  const ab = prog(b, a), ba = prog(a, b);
  if (ab === null && ba === null) console.log(`${kody[i]} + ${kody[j]} jednocześnie: bez kolizji`);
  else console.log(`UWAGA ${kody[i]} + ${kody[j]} jednocześnie: kolizja (${kody[j]} zahacza o otwartą ${kody[i]} przy wysuwie ${ab}, `
    + `${kody[i]} o otwartą ${kody[j]} przy wysuwie ${ba}); nie otwierać obu naraz`);
}
process.exit(bledy ? 1 : 0);
