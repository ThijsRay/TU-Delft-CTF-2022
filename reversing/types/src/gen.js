function make() {
    return {
        steps: [],
        ok() {
            this.steps.push("[OOk]")
        },
        lit(val) {
            this.steps.push(`[OLit, ${val}]`);
        },
        add() {
            this.steps.push(`[OAdd]`);
        },
        sub() {
            this.steps.push(`[OSub]`);
        },
        ifz(fna, fnb) {
            const a = make();
            const b = make();
            fna(a);
            fnb(b);
            this.steps.push(`[OIfz, ${a.export()}, ${b.export()}]`);
        },
        export() {
            return this.steps.reverse().reduce((p, c) => `Cons<${c}, ${p}>`, 'Nil');
        }
    };
}

const alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_";
const ascii = {};
let inverse = "{";
for (let i = 0; i < alphabet.length; i++) ascii[alphabet[i]] = i;
for (let i = 0; i < alphabet.length; i++) inverse += i + ":\"" + alphabet[i] + "\",";
console.log("type Lookup = " + JSON.stringify(ascii) + ";");
console.log("type LookupInv = " + inverse.slice(0, -1) + "};");

const flag = "wh0_n33ds_4_js_runt1m3_wh3n_u_h4v3_typ3s";
for (let i = 0; i < flag.length; i++) {
    console.log("type Flag" + i.toString().padStart(2, "0") + " = Ascii<'" + flag[i] + "'>;");
}

function emit(prog, idx) {
    if (idx === flag.length) {
        prog.ok();
        return;
    }

    prog.lit("Flag" + idx.toString().padStart(2, "0"));

    let curval = alphabet.indexOf(flag[idx]);
    for (let i = 0; i < 3; i++) {
        const val = 10 + Math.floor(Math.random() * 20);
        if (!val) continue;
        curval += val;
        if (val < 0) {
            prog.lit(-val);
            prog.sub();
        } else {
            prog.lit(val);
            prog.add();
        }
    }
    if (curval > 0) {
        prog.lit(curval);
        prog.sub();
    } else {
        prog.lit(-curval);
        prog.add();
    }
    prog.ifz(
        p => emit(p, idx + 1),
        p => { }
    );
}

const prog = make();
emit(prog, 0);
console.log("type Program = " + prog.export() + ";");