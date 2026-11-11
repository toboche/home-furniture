// Wypisuje dane modelu (room, title, items) z model.js jako JSON. Użycie: node dump_model.js ŚCIEŻKA/model.js
const fs = require('fs'), vm = require('vm');
const ctx = {window: {}};
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(process.argv[2], 'utf8') + '\n;this.__M = HF_MODEL;', ctx);
const M = ctx.__M;
process.stdout.write(JSON.stringify({title: M.title, room: M.room, items: M.items.filter(Boolean)}));
