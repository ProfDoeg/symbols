#!/usr/bin/env python3
"""One-off, 2026-09-16: move the first 82 pantheon dossiers from dossiers/<slug>_pantheon_dossier.md
into per-tradition folders as <tradition>/<slug>.md, with git mv so history follows. Anthony:
"Separate the different pantheons so they aren't all in one pile."
"""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
FOLDERS = {
    "egyptian": "anubis osiris atum maat thoth ammit hermanubis",
    "mesopotamian": "marduk nabu apkallu",
    "canaanite": "moloch baal tanit el baal_hadad",
    "greek": "hermes clotho lachesis atropos apollo artemis poseidon urania cronos zeus hephaestus helios "
             "minotaur medusa chiron europa danae pasiphae ariadne graeae pegasus",
    "roman": "venus jupiter mercury juno minerva libertas",
    "norse": "urd_verdandi_skuld thor alvis alberich rhinemaidens dvergatal_dwarves",
    "hindu": "hayagriva vishnu brahma durga saraswati garuda ashvins krishna shiva ganesha nandi mitra varuna "
             "indra aryaman yamaraja sati",
    "abrahamic": "gabriel buraq michael satan mephistopheles the_devil lucifer christ",
    "persian": "ahriman",
    "andean": "inti pachamama mama_huaco",
    "folklore": "cthulhu rumpelstiltskin grendel tinker_bell san_guinefort",
}
n = 0
for folder, slugs in FOLDERS.items():
    os.makedirs(os.path.join(HERE, folder), exist_ok=True)
    for slug in slugs.split():
        src = os.path.join(HERE, "dossiers", f"{slug}_pantheon_dossier.md")
        dst = os.path.join(HERE, folder, f"{slug}.md")
        if not os.path.exists(src):
            print("MISSING", src); continue
        r = subprocess.run(["git", "-C", HERE, "mv", src, dst], capture_output=True, text=True)
        if r.returncode:
            print("FAIL", slug, r.stderr.strip())
        else:
            n += 1
print("moved", n)
print("left in dossiers/:", os.listdir(os.path.join(HERE, "dossiers")) if os.path.isdir(os.path.join(HERE, "dossiers")) else "folder gone")
