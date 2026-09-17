# RELATIONS_PROMPT.md

The extraction prompt for the pantheon interaction matrix (Anthony, 2026-09-17: "For each
pantheon let's map the interaction matrix. Shared myths, meetings, heredity relationship").
tools/extract_relations.py sends the part after `---` followed by one dossier, with no web
search, and parses the JSON array Codex prints. tools/build_matrix.py then resolves names to
slugs and writes the per-pantheon matrices.

---

You are extracting a relation graph from ONE research dossier on a divine being. The dossier
follows. Read all of it, especially the sections "Genealogy and Relations to Other Divine
Beings" (with its subsection listing every documented god-god interaction) and "Major Myths
and Narrative Cycles".

Output ONLY a JSON array, no prose before or after, no markdown fence. Each element is one
relation between the dossier's subject and ONE other named divine or mythical being (god,
goddess, spirit, demon, monster, hero-god, angel, collective such as "the Muses"; NOT human
authors, kings, saints or scholars unless the dossier treats them as divine beings). Use this
shape exactly:

{"other": "<the other being's most common name, as the dossier spells it>",
 "other_aliases": ["<other names the dossier gives for the same being>"],
 "kind": "<one of: parent_of | child_of | sibling_of | consort_of | ancestor_of | descendant_of | created | created_by | fought | killed | killed_by | allied | seduced | seduced_by | deceived | deceived_by | judged | judged_by | rescued | rescued_by | punished | punished_by | transformed | transformed_by | contest | theft | gift | taught | taught_by | served | served_by | identified_with | shared_myth | other>",
 "myth": "<the episode or myth in which the relation occurs, in at most 12 words; empty string if purely genealogical>",
 "note": "<one line, at most 25 words, saying what happens between them>",
 "source": "<the primary text or evidence the dossier cites for it, at most 12 words>",
 "date": "<date of that source as the dossier gives it, at most 8 words>",
 "tier": "<one of: attested | canonical | regional_variant | late_accretion | syncretism | modern>"}

Rules:
- One element per relation; if two beings share several distinct relations (sister AND consort;
  fought AND later allied), give several elements. Do not merge distinct episodes.
- "kind" is from the subject's point of view: if the dossier's subject is Zeus and the other is
  Cronus, kind is child_of; if the subject is Cronus and the other is Zeus, kind is parent_of.
- Kinship goes in the kinship kinds; "shared_myth" is only for joint appearances with no more
  specific verb; "identified_with" is for interpretatio and syncretism (Hermes = Thoth = Mercury).
- Conflicting genealogies are separate elements, each with its own source and tier.
- Include beings from OTHER pantheons when the dossier documents the link (Aphrodite with
  Astarte, Mithra with Mithras, Baal with Zeus); the builder sorts them.
- Do not invent relations the dossier does not state. If the dossier says an interaction is
  absent, do not add it. Empty array [] is a valid answer.
- Keep names in Latin script as the dossier gives them (Zeus, not Ζεύς); Sanskrit and Arabic
  names in their common transliteration.

The dossier:
