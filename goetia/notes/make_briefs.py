#!/usr/bin/env python3
"""One-off research notes for the Goetia set."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "briefs")

NOTES = [
 ("emoji_and_the_72_spirits", "Emoji and the 72 spirits of the Goetia",
  "Anthony, 2026-09-15: 'Isn't there some conspiracy about emoji relationships to the 72 demons of Solomon?' Find out whether any such theory exists: emoji mapped to the Goetic spirits or their seals, emoji as demonic sigils, numerological links (the 72 spirits; Unicode 6.0's 722 emoji of 2010; the 176 of Kurita's 1999 set; the 72 Shem angels), emoji 'summoning' claims, chaos-magic emoji sigils and hypersigils, art projects rendering the Goetic seals as emoji, and any religious or conspiracy channels (evangelical, QAnon-adjacent, Islamic) that call emoji demonic. Distinguish the joke, the art project, the chaos-magic practice and the conspiracy claim. Check the numbers people cite."),
]

SIGNS = {}
for i, (slug, name, question) in enumerate(NOTES, start=1):
    SIGNS[f"{i:02d}_{slug}"] = (name, "research note", question)

ORDER = list(SIGNS.keys())


def out_path(slug):
    return f"{slug}.note.md"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for slug, (name, status, question) in SIGNS.items():
        text = f"""# {name}: research brief

A one-off note for the Goetia set, 2026-09-15.

---

QUESTION. {name}: {question}
"""
        open(os.path.join(OUT, f"{slug}.brief.md"), "w").write(text)
    print("wrote", len(SIGNS), "briefs")
