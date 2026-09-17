#!/usr/bin/env python3
"""build_matrix.py -- turn pantheon/<tradition>/relations/*.json into the interaction matrices.

    python3 tools/build_matrix.py            # every tradition folder
    python3 tools/build_matrix.py greek roman

Per tradition folder it writes:
  _relations.json   every resolved relation (a, b, kind, myth, note, source, date, tier, stated_by)
                    plus the unresolved names (beings with no dossier in the repo)
  _matrix.csv       slug x slug: number of distinct relations between the two (both directions)
  _matrix.md        one section per god: degree, then each related god with the relation kinds
                    and the myths they share; a header table of the most connected gods
and at the set root:
  _cross_pantheon.json / .md   relations whose other being has a dossier in ANOTHER folder
                               (identifications, cognates, borrowed myths)

Name resolution: every dossier's H1 name, the parenthesised aliases in it, the roster names in
make_briefs.py, and the aliases Codex reported, all normalised (lowercase, accents stripped,
"the " dropped). A name found in the same folder wins; then a unique hit in any folder; else
the relation is kept under "unresolved" with the raw name.
"""
import csv, importlib.util, json, os, re, sys, unicodedata
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SET = os.path.join(os.path.dirname(HERE), "pantheon")
# optional: --set heroes (any set laid out as <tradition>/<slug>.md with relations/ inside)
if "--set" in sys.argv:
    i = sys.argv.index("--set")
    SET = os.path.join(os.path.dirname(HERE), sys.argv[i + 1])
    del sys.argv[i:i + 2]
SKIP_DIRS = {"briefs", "__pycache__", "dossiers", "relations", "notes"}
KIN = {"parent_of", "child_of", "sibling_of", "consort_of", "ancestor_of", "descendant_of"}
INVERSE = {"parent_of": "child_of", "child_of": "parent_of", "ancestor_of": "descendant_of",
           "descendant_of": "ancestor_of", "created": "created_by", "created_by": "created",
           "killed": "killed_by", "killed_by": "killed", "seduced": "seduced_by", "seduced_by": "seduced",
           "deceived": "deceived_by", "deceived_by": "deceived", "judged": "judged_by", "judged_by": "judged",
           "rescued": "rescued_by", "rescued_by": "rescued", "punished": "punished_by", "punished_by": "punished",
           "transformed": "transformed_by", "transformed_by": "transformed", "taught": "taught_by",
           "taught_by": "taught", "served": "served_by", "served_by": "served"}
SYMMETRIC = {"sibling_of", "consort_of", "fought", "allied", "contest", "identified_with", "shared_myth", "other", "theft", "gift"}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower().strip()
    s = re.sub(r"^(the|el|la|los|las|le|les|der|die|das)\s+", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


def folders():
    return [t for t in sorted(os.listdir(SET)) if os.path.isdir(os.path.join(SET, t)) and t not in SKIP_DIRS]


def dossier_name(path):
    for line in open(path, errors="ignore"):
        if line.startswith("# "):
            return line[2:].replace(": Research Dossier", "").strip()
    return os.path.basename(path)[:-3]


def alias_forms(name):
    """'Hayagriva (the asura)' -> ['hayagriva the asura', 'hayagriva', 'the asura']; also split ' / ' and ' and '."""
    out = {norm(name)}
    base = re.sub(r"\(.*?\)", "", name).strip()
    out.add(norm(base))
    for inner in re.findall(r"\((.*?)\)", name):
        for part in re.split(r",|;|/|\s+and\s+|\s+y\s+|\s+&\s+", inner):
            out.add(norm(part))
    for part in re.split(r"\s*/\s*", base):
        out.add(norm(part))
    for part in re.split(r"\s+and\s+|\s+y\s+|\s+&\s+", base):
        out.add(norm(part))
    return {a for a in out if a and len(a) > 2}


def build_index():
    """norm name -> set of (folder, slug)."""
    idx = defaultdict(set)
    spec = importlib.util.spec_from_file_location("mb", os.path.join(SET, "make_briefs.py"))
    mb = importlib.util.module_from_spec(spec); spec.loader.exec_module(mb)
    for folder in folders():
        d = os.path.join(SET, folder)
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md") or f.startswith("_"):
                continue
            slug = f[:-3]
            for a in alias_forms(dossier_name(os.path.join(d, f))):
                idx[a].add((folder, slug))
            idx[norm(slug.replace("_", " "))].add((folder, slug))
            if slug in mb.SIGNS:
                for a in alias_forms(mb.SIGNS[slug][0]):
                    idx[a].add((folder, slug))
    return idx


ALIASES_FILE = os.path.join(SET, "ALIASES.json")   # optional: {"folder": {"raw name": "slug"}}
MANUAL = json.load(open(ALIASES_FILE)) if os.path.exists(ALIASES_FILE) else {}


def resolve(idx, folder, name, aliases, folder_keys):
    """Exact same-folder hit, then exact unique hit anywhere, then a manual alias, then a close
    spelling match within the same folder (difflib, cutoff 0.86: Cinteotl -> centeotl,
    Tecuciztecatl -> tecciztecatl, Pahtecatl -> patecatl)."""
    import difflib
    cands = [norm(name)] + [norm(a) for a in aliases or []]
    for c in cands:
        hits = idx.get(c, set())
        same = [h for h in hits if h[0] == folder]
        if len(same) == 1:
            return same[0]
    for c in cands:
        hits = idx.get(c, set())
        if len(hits) == 1:
            return next(iter(hits))
    m = MANUAL.get(folder, {}).get(name) or MANUAL.get(folder, {}).get(norm(name))
    if m:
        return (folder, m)
    for c in cands:
        if len(c) < 5:
            continue
        close = difflib.get_close_matches(c, folder_keys, n=1, cutoff=0.86)
        if close:
            same = [h for h in idx[close[0]] if h[0] == folder]
            if len(same) == 1:
                return same[0]
    return None


def canon(a, b, kind):
    """Orient a relation so the pair is sorted and the kind is expressed from the first element."""
    if a <= b:
        return a, b, kind
    return b, a, INVERSE.get(kind, kind)


def main(only):
    idx = build_index()
    cross = []
    for folder in folders():
        if only and folder not in only:
            continue
        reldir = os.path.join(SET, folder, "relations")
        if not os.path.isdir(reldir):
            continue
        edges = {}       # (a, b, kind, myth-norm) -> record
        unresolved = defaultdict(list)
        gods = set()
        folder_keys = [k for k, hits in idx.items() if any(h[0] == folder for h in hits)]
        for f in sorted(os.listdir(reldir)):
            if not f.endswith(".json"):
                continue
            data = json.load(open(os.path.join(reldir, f)))
            subj = data["subject"]; gods.add(subj)
            for r in data["relations"]:
                hit = resolve(idx, folder, r.get("other", ""), r.get("other_aliases"), folder_keys)
                if hit is None:
                    unresolved[r.get("other", "")].append({"stated_by": subj, **{k: r.get(k, "") for k in ("kind", "myth", "note", "source", "date", "tier")}})
                    continue
                ofolder, oslug = hit
                if ofolder != folder:
                    cross.append({"folder_a": folder, "a": subj, "folder_b": ofolder, "b": oslug, **{k: r.get(k, "") for k in ("kind", "myth", "note", "source", "date", "tier")}})
                    continue
                if oslug == subj:
                    continue
                a, b, kind = canon(subj, oslug, r.get("kind", "other"))
                key = (a, b, kind, norm(r.get("myth", ""))[:40])
                rec = edges.get(key)
                if rec is None:
                    edges[key] = {"a": a, "b": b, "kind": kind, "myth": r.get("myth", ""), "note": r.get("note", ""),
                                  "source": r.get("source", ""), "date": r.get("date", ""), "tier": r.get("tier", ""),
                                  "stated_by": [subj]}
                elif subj not in rec["stated_by"]:
                    rec["stated_by"].append(subj)
        recs = sorted(edges.values(), key=lambda e: (e["a"], e["b"], e["kind"]))
        # matrix of distinct relations per pair
        pair = defaultdict(int)
        for e in recs:
            pair[(e["a"], e["b"])] += 1
        slugs = sorted(gods)
        with open(os.path.join(SET, folder, "_matrix.csv"), "w", newline="") as fh:
            w = csv.writer(fh); w.writerow([""] + slugs)
            for x in slugs:
                w.writerow([x] + [pair.get((min(x, y), max(x, y)), 0) if x != y else "" for y in slugs])
        json.dump({"folder": folder, "gods": slugs, "relations": recs,
                   "unresolved": {k: v for k, v in sorted(unresolved.items())}},
                  open(os.path.join(SET, folder, "_relations.json"), "w"), ensure_ascii=False, indent=1)
        # markdown
        by_god = defaultdict(lambda: defaultdict(list))
        for e in recs:
            by_god[e["a"]][e["b"]].append(e)
            by_god[e["b"]][e["a"]].append({**e, "kind": INVERSE.get(e["kind"], e["kind"])})
        degree = {g: len(by_god[g]) for g in slugs}
        kin_edges = sum(1 for e in recs if e["kind"] in KIN)
        lines = [f"# {folder}: interaction matrix", "",
                 f"{len(slugs)} gods, {len(recs)} distinct relations ({kin_edges} kinship, {len(recs) - kin_edges} meetings, myths and identifications), "
                 f"{sum(len(v) for v in unresolved.values())} mentions of beings without a dossier here. "
                 f"Built by tools/build_matrix.py from relations/*.json (Codex extraction of each dossier's genealogy and interaction sections). "
                 f"Matrix of counts in _matrix.csv; full records with sources in _relations.json.", "",
                 "## Most connected", "", "| god | relations with | distinct gods |", "|---|---|---|"]
        for g in sorted(slugs, key=lambda g: -degree[g])[:15]:
            lines.append(f"| {g} | {sum(len(v) for v in by_god[g].values())} | {degree[g]} |")
        lines += ["", "## Each god", ""]
        for g in slugs:
            lines.append(f"### {g}  ({degree[g]} gods)")
            for other in sorted(by_god[g], key=lambda o: (-len(by_god[g][o]), o)):
                es = by_god[g][other]
                kinds = sorted({e["kind"] for e in es})
                myths = sorted({e["myth"] for e in es if e["myth"]})
                tail = ("; " + "; ".join(myths[:4])) if myths else ""
                lines.append(f"- **{other}**: {', '.join(kinds)}{tail}")
            lines.append("")
        if unresolved:
            lines += ["## Named but without a dossier here", ""]
            for name, ments in sorted(unresolved.items(), key=lambda kv: -len(kv[1]))[:60]:
                lines.append(f"- {name} ({len(ments)}): " + ", ".join(sorted({m['stated_by'] for m in ments})[:8]))
        open(os.path.join(SET, folder, "_matrix.md"), "w").write("\n".join(lines) + "\n")
        print(f"{folder:14s} gods {len(slugs):4d} relations {len(recs):5d} unresolved names {len(unresolved):4d}")
    if not only:
        json.dump(cross, open(os.path.join(SET, "_cross_pantheon.json"), "w"), ensure_ascii=False, indent=1)
        lines = ["# Cross-pantheon relations", "", f"{len(cross)} relations whose other being has its dossier in another folder (identifications, cognates, borrowed myths).", ""]
        byp = defaultdict(list)
        for c in cross:
            byp[(c["folder_a"], c["folder_b"])].append(c)
        for (fa, fb), cs in sorted(byp.items(), key=lambda kv: -len(kv[1])):
            lines.append(f"## {fa} -> {fb} ({len(cs)})"); lines.append("")
            for c in sorted(cs, key=lambda c: (c["a"], c["b"])):
                lines.append(f"- {c['a']} -> {c['b']}: {c['kind']}" + (f"; {c['myth']}" if c['myth'] else "") + (f" ({c['source']})" if c['source'] else ""))
            lines.append("")
        open(os.path.join(SET, "_cross_pantheon.md"), "w").write("\n".join(lines) + "\n")
        print("cross-pantheon relations", len(cross))


if __name__ == "__main__":
    main(set(sys.argv[1:]))
