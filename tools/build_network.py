#!/usr/bin/env python3
"""build_network.py -- turn <set>/relations/*.json (from extract_network_ties.py) into the network map.

    python3 tools/build_network.py cybernetic_elite

Writes into the set folder:
  _network.json   nodes (every subject of the set, every other party named, each resolved to a dossier
                  in this set, in another symbols set, or in the atlas when one exists) and edges
                  (resolved, oriented, deduplicated, each with kind, note, dates, money, source, tier
                  and which dossiers state it)
  _matrix.csv     node x node: number of distinct ties between the two, over the nodes with a dossier
  _network.md     the readable map: most connected, the money edges, every node's ties by tier, and
                  the parties named without a dossier anywhere

Name resolution: every dossier's H1 name and the roster names in make_briefs.py (this set), then the
H1 names of every dossier in the other symbols sets and in the atlas dossiers; normalised (lowercase,
accents stripped, "the " dropped, parenthetical aliases split). Unresolved names still become nodes,
keyed by their normalised name, so the map shows the whole cast the dossiers document.
"""
import csv, importlib.util, json, os, re, sys, unicodedata
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ATLAS = "/home/drdoeg/taller/Colegio_Invisible/working/journeys/dossiers"
INVERSE = {"funded": "funded_by", "funded_by": "funded", "employed": "employed_by", "employed_by": "employed",
           "advised": "advised_by", "advised_by": "advised", "founded": "founded_by", "founded_by": "founded",
           "introduced": "introduced_by", "introduced_by": "introduced", "published": "published_by",
           "published_by": "published", "invested_in": "invested_by", "invested_by": "invested_in",
           "donated_to": "received_from", "received_from": "donated_to", "attacked": "attacked_by",
           "attacked_by": "attacked", "investigated": "investigated_by", "investigated_by": "investigated",
           "prosecuted": "prosecuted_by", "prosecuted_by": "prosecuted", "sued": "sued_by", "sued_by": "sued",
           "accused": "accused_by", "accused_by": "accused", "interviewed": "interviewed_by",
           "interviewed_by": "interviewed", "cited": "cited_by", "cited_by": "cited", "studied_under": "taught",
           "taught": "studied_under"}
MONEY_KINDS = {"funded", "funded_by", "invested_in", "invested_by", "donated_to", "received_from", "employed", "employed_by"}
SKIP_DIRS = {"briefs", "__pycache__", "relations", "notes", "tools", ".git"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower().strip()
    s = re.sub(r"^(the|el|la|los|las)\s+", "", s)
    s = re.sub(r",?\s+(inc|incorporated|llc|ltd|corp|corporation)\.?$", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


def first_last(name):
    """'David Richard Kaczynski' -> 'david kaczynski'; 'W. Daniel (Danny) Hillis' -> 'w hillis' (also nickname forms)"""
    base = re.sub(r"\(.*?\)", "", name)
    toks = [t for t in norm(base).split() if t not in ("jr", "sr", "ii", "iii")]
    return f"{toks[0]} {toks[-1]}" if len(toks) >= 2 else None


def alias_forms(name):
    out = {norm(name)}
    base = re.sub(r"\(.*?\)", "", name).strip()
    out.add(norm(base))
    fl = first_last(name)
    if fl:
        out.add(fl)
    m = re.match(r"^\s*[A-Za-z]\.?\s+\w+\s*\((\w+)\)\s+(\w+)", name)      # 'W. Daniel (Danny) Hillis' -> 'danny hillis'
    if m:
        out.add(norm(m.group(1) + " " + m.group(2)))
    m = re.match(r"^\s*([A-Za-z]+)\s+\(([^)]+)\)\s+([A-Za-z]+)\s*$", name)  # 'Cammie (Kamie) Clark' -> 'kamie clark'
    if m:
        out.add(norm(m.group(2) + " " + m.group(3)))
    for inner in re.findall(r"\((.*?)\)", name):
        for part in re.split(r",|;|/|\s+and\s+|\s+&\s+", inner):
            out.add(norm(part))
    for part in re.split(r"\s*/\s*|:\s+", base):
        out.add(norm(part))
    return {a for a in out if a and len(a) > 2}


def h1(path):
    for line in open(path, errors="ignore"):
        if line.startswith("# "):
            return line[2:].replace(": Research Dossier", "").strip()
    return os.path.basename(path).split(".")[0]


def main(setname):
    SET = os.path.join(ROOT, setname)
    spec = importlib.util.spec_from_file_location("mb", os.path.join(SET, "make_briefs.py"))
    mb = importlib.util.module_from_spec(spec); spec.loader.exec_module(mb)
    # --- index: this set first
    idx_set, idx_ext = defaultdict(set), defaultdict(set)
    meta = {}
    for f in sorted(os.listdir(SET)):
        if f.endswith(".dossier.md"):
            slug = f[:-len(".dossier.md")]
            name = h1(os.path.join(SET, f))
            meta[slug] = {"name": mb.SIGNS[slug][0] if slug in mb.SIGNS else name, "ntype": _ntype(mb.SIGNS[slug][1]) if slug in mb.SIGNS else "person",
                          "dossier": f"{setname}/{f}"}
            for a in alias_forms(name) | alias_forms(meta[slug]["name"]) | {norm(slug.replace("_", " "))}:
                idx_set[a].add(slug)
    for slug, (name, klass, *_rest) in mb.SIGNS.items():      # briefed but not yet landed: still a node
        if slug not in meta:
            meta[slug] = {"name": name, "ntype": _ntype(klass), "dossier": None}
            for a in alias_forms(name) | {norm(slug.replace("_", " "))}:
                idx_set[a].add(slug)
    # --- index: other symbols sets and the atlas dossiers
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        if os.path.abspath(dirpath).startswith(os.path.abspath(SET)):
            continue
        for f in files:
            if f.endswith(".md") and not f.startswith("_") and f not in ("README.md", "CATALOG.md", "QUEUE.md") and "PROMPT" not in f:
                rel = os.path.relpath(os.path.join(dirpath, f), ROOT)
                key = "symbols:" + rel[:-3]
                for a in alias_forms(h1(os.path.join(dirpath, f))):
                    idx_ext[a].add(key)
    if os.path.isdir(ATLAS):
        for f in os.listdir(ATLAS):
            if f.endswith(".dossier.md"):
                key = "atlas:" + f[:-len(".dossier.md")]
                for a in alias_forms(h1(os.path.join(ATLAS, f))):
                    idx_ext[a].add(key)
    ext_name = {}

    def resolve(name):
        cands = list(alias_forms(name))
        for c in cands:
            if len(idx_set.get(c, ())) == 1:
                return next(iter(idx_set[c]))
        for c in cands:
            hits = idx_ext.get(c, set())
            if len(hits) == 1:
                k = next(iter(hits)); ext_name.setdefault(k, name); return k
        return "x:" + norm(name).replace(" ", "_")

    # --- edges
    edges, stated = {}, defaultdict(set)
    nodes = {}
    reldir = os.path.join(SET, "relations")
    for f in sorted(os.listdir(reldir)):
        if not f.endswith(".json"):
            continue
        data = json.load(open(os.path.join(reldir, f)))
        subj = data["subject"]
        for t in data["ties"]:
            other = resolve(t["other"])
            if other == subj:
                continue
            if other not in meta and other not in nodes:
                nodes[other] = {"name": ext_name.get(other, t["other"]), "ntype": t.get("other_type") or "person",
                                "dossier": _ext_path(other)}
            a, b, kind = (subj, other, t["kind"]) if subj <= other else (other, subj, INVERSE.get(t["kind"], t["kind"]))
            key = (a, b, kind, norm(t.get("note", ""))[:40])
            rec = edges.get(key)
            if rec is None:
                edges[key] = {"from": a, "to": b, "kind": kind, "note": t.get("note", ""), "dates": t.get("dates", ""),
                              "money": t.get("money", ""), "source": t.get("source", ""), "source_date": t.get("source_date", ""),
                              "tier": t.get("tier", ""), "stated_by": [subj]}
            elif subj not in rec["stated_by"]:
                rec["stated_by"].append(subj)
    recs = sorted(edges.values(), key=lambda e: (e["from"], e["to"], e["kind"]))
    all_nodes = {**{k: dict(v) for k, v in meta.items()}, **nodes}
    deg, pair = defaultdict(set), defaultdict(int)
    for e in recs:
        deg[e["from"]].add(e["to"]); deg[e["to"]].add(e["from"]); pair[(e["from"], e["to"])] += 1
    for k, v in all_nodes.items():
        v["id"] = k; v["degree"] = len(deg[k]); v["ties"] = sum(1 for e in recs if k in (e["from"], e["to"]))
    tiers = defaultdict(int)
    for e in recs:
        tiers[e["tier"] or "unlabeled"] += 1
    out = {"network": "The Cybernetic Elite", "slug": setname,
           "title": "Kaczynski, the Macy circle, Brand, Brockman, Epstein and the technological elite, 1946 to 2026",
           "summary": "Every tie the set's dossiers document between their subjects and any other named party, extracted "
                      "by tools/extract_network_ties.py from each dossier's Network section and resolved by tools/build_network.py. "
                      "Each edge carries its evidence tier; rumor is on the map as rumor.",
           "counts": {"nodes": len(all_nodes), "nodes_with_dossier": sum(1 for v in all_nodes.values() if v["dossier"]),
                      "edges": len(recs), "tiers": dict(tiers)},
           "nodes": sorted(all_nodes.values(), key=lambda v: (-v["degree"], v["id"])), "edges": recs}
    json.dump(out, open(os.path.join(SET, "_network.json"), "w"), ensure_ascii=False, indent=1)
    # matrix over dossier'd nodes
    ds = sorted(k for k, v in all_nodes.items() if v["dossier"] and v["degree"] > 0)
    with open(os.path.join(SET, "_matrix.csv"), "w", newline="") as fh:
        w = csv.writer(fh); w.writerow([""] + ds)
        for x in ds:
            w.writerow([x] + [pair.get((min(x, y), max(x, y)), 0) if x != y else "" for y in ds])
    # markdown
    by = defaultdict(lambda: defaultdict(list))
    for e in recs:
        by[e["from"]][e["to"]].append(e)
        by[e["to"]][e["from"]].append({**e, "kind": INVERSE.get(e["kind"], e["kind"])})
    nm = lambda k: all_nodes[k]["name"]
    L = [f"# {out['network']}: network map", "", out["title"] + ".", "",
         f"{len(all_nodes)} nodes ({out['counts']['nodes_with_dossier']} with a dossier here, in another symbols set or in the atlas), "
         f"{len(recs)} distinct ties. By evidence tier: " + ", ".join(f"{k} {v}" for k, v in sorted(tiers.items(), key=lambda kv: -kv[1])) + ".",
         "Built by tools/build_network.py from relations/*.json (Codex extraction of each dossier's Network section). Full records in _network.json; counts in _matrix.csv.", "",
         "## Most connected", "", "| node | ties | distinct parties | dossier |", "|---|---|---|---|"]
    for k in sorted(all_nodes, key=lambda k: (-all_nodes[k]["degree"], k))[:30]:
        v = all_nodes[k]
        L.append(f"| {v['name']} | {v['ties']} | {v['degree']} | {v['dossier'] or 'none'} |")
    money = [e for e in recs if e["money"] or e["kind"] in MONEY_KINDS]
    L += ["", f"## Money ({len(money)} ties)", "", "| from | to | kind | amount | dates | tier | source |", "|---|---|---|---|---|---|---|"]
    for e in sorted(money, key=lambda e: (e["tier"] != "primary", e["from"])):
        L.append(f"| {nm(e['from'])} | {nm(e['to'])} | {e['kind']} | {e['money']} | {e['dates']} | {e['tier']} | {e['source']} |")
    L += ["", "## Each subject", ""]
    for k in sorted(meta, key=lambda k: (-all_nodes[k]["degree"], k)):
        v = all_nodes[k]
        L.append(f"### {v['name']}  ({v['degree']} parties, {v['ties']} ties)")
        for o in sorted(by[k], key=lambda o: (-len(by[k][o]), o)):
            es = by[k][o]
            parts = "; ".join(f"{e['kind']} [{e['tier'] or '?'}]" + (f" {e['dates']}" if e["dates"] else "") + (f": {e['note']}" if e["note"] else "") for e in es[:4])
            L.append(f"- **{nm(o)}**: {parts}")
        L.append("")
    ext = [k for k, v in all_nodes.items() if k not in meta and v["dossier"]]
    L += [f"## Parties with a dossier elsewhere ({len(ext)})", ""]
    for k in sorted(ext, key=lambda k: (-all_nodes[k]["degree"], k)):
        L.append(f"- {nm(k)} ({all_nodes[k]['dossier']}): {all_nodes[k]['degree']} parties, {all_nodes[k]['ties']} ties")
    unres = [k for k, v in all_nodes.items() if k not in meta and not v["dossier"]]
    L += ["", f"## Named without a dossier anywhere ({len(unres)})", ""]
    for k in sorted(unres, key=lambda k: (-all_nodes[k]["degree"], k))[:150]:
        L.append(f"- {nm(k)} ({all_nodes[k]['ntype']}): {all_nodes[k]['degree']} parties, named by " + ", ".join(sorted(deg[k])[:6]))
    open(os.path.join(SET, "_network.md"), "w").write("\n".join(L) + "\n")
    print(f"nodes {len(all_nodes)} (dossier {out['counts']['nodes_with_dossier']}) edges {len(recs)} tiers {dict(tiers)}")


def _ntype(klass):
    k = klass.lower()
    if k.startswith("person"): return "person"
    if k.startswith("text"): return "text"
    if "company" in k: return "company"
    if "program" in k: return "program"
    if "event" in k: return "event"
    return "institution"


def _ext_path(key):
    if key.startswith("symbols:"): return key[len("symbols:"):] + ".md"
    if key.startswith("atlas:"): return "Colegio_Invisible/working/journeys/dossiers/" + key[len("atlas:"):] + ".dossier.md"
    return None


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "cybernetic_elite")
