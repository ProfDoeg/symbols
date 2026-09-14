#!/usr/bin/env python3
"""Write one brief per memory system into memoria/briefs/, from systems.json and the matching
section of CATALOG.md (principle, components, Yates's pages and words, lineage, dossier note)."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "briefs")

systems = json.load(open(os.path.join(HERE, "systems.json")))
catalog = open(os.path.join(HERE, "CATALOG.md")).read()


def section(n):
    """the '## N. ...' section of CATALOG.md, without the heading"""
    m = re.search(rf"^## {n}\. .*?$", catalog, flags=re.M)
    if not m:
        return ""
    rest = catalog[m.end():]
    nxt = re.search(r"^## ", rest, flags=re.M)
    return rest[: nxt.start() if nxt else None].strip()


SIGNS = {}
for s in systems:
    slug = f"{s['n']:02d}_{s['slug']}"
    status = (f"system {s['n']} of 45 in the memoria catalogue; exponent: {s['exponent']}; date: {s['date']}; "
              f"source text: {s['source_text']}; Yates: {s['yates_pages']}")
    pointers = "the catalogue entry follows, built from Yates by four readers; every line of it is a lead to verify against the primary text and the scholarship:\n\n" + section(s["n"])
    SIGNS[slug] = (s["name"], status, pointers)

ORDER = list(SIGNS.keys())

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for slug, (name, status, pointers) in SIGNS.items():
        text = f"""# {name}: research brief

Memory-systems research, Anthony 2026-09-14, separate from the atlas. Appended to
PROMPT_TEMPLATE_MEMORIA.md by tools/codex_dossier_set.py.

---

SYSTEM. {name}: {status}. Give at the top the name, the exponent, the date, the source text and
the principle in one sentence.

THREADS TO PULL: {pointers}

STANCE. Yates is the starting point, never the last word: confirm or correct her against the
primary text and the scholarship since 1966. Every claim labeled: documented text, scholarly
reconstruction, tradition, Yates's interpretation, disputed, legend, modern invention. Quote the
primary sources in the original with a gloss and the edition. Absence of evidence is a finding.
"""
        open(os.path.join(OUT, f"{slug}.brief.md"), "w").write(text)
    print("wrote", len(SIGNS), "briefs")
