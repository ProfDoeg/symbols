#!/usr/bin/env python3
"""build_hero_god.py -- the hero-to-god relations within each mythic tradition.

Reads heroes/<tradition>/_relations.json (the god_relations that tools/build_matrix.py resolved
against the pantheon) and writes, for every tradition that has both a heroes folder and a
pantheon folder (biblical and arabic heroes map to the abrahamic gods):

  heroes/<tradition>/_gods.csv     heroes x gods: number of distinct relations
  heroes/<tradition>/_gods.md      each hero's gods (kinds, myths), then each god's heroes
  pantheon/<tradition>/_heroes.md  the same table from the gods' side, kept beside the gods

Relations with gods of OTHER traditions are not merged (Anthony: cross-pantheon links are chosen
strategically); they are listed at the end of heroes/_hero_god_cross.md as raw material.
"""
import csv, json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HEROES = os.path.join(ROOT, "heroes")
PANTHEON = os.path.join(ROOT, "pantheon")
SKIP = {"briefs", "__pycache__", "relations", "notes", "dossiers"}
MAP = {"biblical": "abrahamic", "arabic": "abrahamic"}   # hero folder -> pantheon folder when names differ

cross = []
summary = []
for trad in sorted(os.listdir(HEROES)):
    hdir = os.path.join(HEROES, trad)
    rel = os.path.join(hdir, "_relations.json")
    if not os.path.isdir(hdir) or trad in SKIP or not os.path.exists(rel):
        continue
    gtrad = MAP.get(trad, trad)
    gdir = os.path.join(PANTHEON, gtrad)
    data = json.load(open(rel))
    heroes = data["gods"]                      # the builder's name for the folder's subjects
    edges = {}                                 # (hero, god, kind, myth) -> record
    for e in data.get("god_relations", []):
        gfolder, gslug = e["god"].split("/", 1)
        if gfolder != gtrad:
            cross.append({"hero_folder": trad, **e})
            continue
        key = (e["a"], gslug, e["kind"], (e.get("myth") or "")[:40].lower())
        edges.setdefault(key, {"hero": e["a"], "god": gslug, **{k: e.get(k, "") for k in ("kind", "myth", "note", "source", "date", "tier")}})
    recs = sorted(edges.values(), key=lambda r: (r["hero"], r["god"], r["kind"]))
    if not os.path.isdir(gdir):
        continue
    gods_all = sorted(f[:-3] for f in os.listdir(gdir) if f.endswith(".md") and not f.startswith("_"))
    pair = defaultdict(int)
    by_hero = defaultdict(lambda: defaultdict(list))
    by_god = defaultdict(lambda: defaultdict(list))
    for r in recs:
        pair[(r["hero"], r["god"])] += 1
        by_hero[r["hero"]][r["god"]].append(r)
        by_god[r["god"]][r["hero"]].append(r)
    gods_used = sorted(by_god)
    with open(os.path.join(hdir, "_gods.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow([""] + gods_used)
        for h in heroes:
            w.writerow([h] + [pair.get((h, g), 0) for g in gods_used])
    n_gods_touched = len(gods_used)
    head = [f"{len(heroes)} heroes, {n_gods_touched} of the {len(gods_all)} gods of pantheon/{gtrad} touched, {len(recs)} distinct hero-to-god relations. "
            f"Built by tools/build_hero_god.py from _relations.json (relations with gods of other traditions are not merged; see heroes/_hero_god_cross.md)."]
    # hero side
    lines = [f"# {trad}: heroes and their gods", ""] + head + ["", "## Gods most involved with the heroes", "", "| god | relations | heroes |", "|---|---|---|"]
    for g in sorted(gods_used, key=lambda g: (-len(by_god[g]), g))[:20]:
        lines.append(f"| {g} | {sum(len(v) for v in by_god[g].values())} | {len(by_god[g])} |")
    lines += ["", "## Each hero", ""]
    for h in heroes:
        lines.append(f"### {h}  ({len(by_hero[h])} gods)")
        for g in sorted(by_hero[h], key=lambda o: (-len(by_hero[h][o]), o)):
            es = by_hero[h][g]
            kinds = sorted({e["kind"] for e in es}); myths = sorted({e["myth"] for e in es if e["myth"]})
            lines.append(f"- **{g}**: {', '.join(kinds)}" + (("; " + "; ".join(myths[:4])) if myths else ""))
        lines.append("")
    lines += ["## Each god's heroes", ""]
    for g in gods_used:
        lines.append(f"### {g}  ({len(by_god[g])} heroes)")
        for h in sorted(by_god[g], key=lambda o: (-len(by_god[g][o]), o)):
            es = by_god[g][h]
            kinds = sorted({e["kind"] for e in es}); myths = sorted({e["myth"] for e in es if e["myth"]})
            lines.append(f"- **{h}**: {', '.join(kinds)}" + (("; " + "; ".join(myths[:3])) if myths else ""))
        lines.append("")
    open(os.path.join(hdir, "_gods.md"), "w").write("\n".join(lines) + "\n")
    # god side
    glines = [f"# {gtrad}: the gods and their heroes (from heroes/{trad})", ""] + head + ["", "## Each god", ""]
    for g in gods_used:
        glines.append(f"### {g}  ({len(by_god[g])} heroes)")
        for h in sorted(by_god[g], key=lambda o: (-len(by_god[g][o]), o)):
            es = by_god[g][h]
            kinds = sorted({e["kind"] for e in es}); myths = sorted({e["myth"] for e in es if e["myth"]})
            glines.append(f"- **{h}**: {', '.join(kinds)}" + (("; " + "; ".join(myths[:3])) if myths else ""))
        glines.append("")
    gout = os.path.join(gdir, f"_heroes{'' if gtrad == trad else '_' + trad}.md")
    open(gout, "w").write("\n".join(glines) + "\n")
    json.dump({"heroes_folder": trad, "gods_folder": gtrad, "relations": recs}, open(os.path.join(hdir, "_gods.json"), "w"), ensure_ascii=False, indent=1)
    summary.append((trad, gtrad, len(heroes), n_gods_touched, len(gods_all), len(recs)))
    print(f"{trad:14s} -> {gtrad:14s} heroes {len(heroes):3d} gods touched {n_gods_touched:3d}/{len(gods_all):3d} relations {len(recs):4d}")

lines = ["# Hero-to-god relations across traditions (not merged)", "", f"{len(cross)} relations where a hero's dossier names a god of another tradition. Raw material only.", ""]
byp = defaultdict(list)
for c in cross:
    byp[(c["hero_folder"], c["god"].split("/")[0])].append(c)
for (hf, gf), cs in sorted(byp.items(), key=lambda kv: -len(kv[1])):
    lines.append(f"## {hf} heroes -> {gf} gods ({len(cs)})"); lines.append("")
    for c in sorted(cs, key=lambda c: (c["a"], c["god"])):
        lines.append(f"- {c['a']} -> {c['god'].split('/')[1]}: {c['kind']}" + (f"; {c['myth']}" if c.get("myth") else ""))
    lines.append("")
open(os.path.join(HEROES, "_hero_god_cross.md"), "w").write("\n".join(lines) + "\n")
print("cross-tradition hero-god relations", len(cross))
