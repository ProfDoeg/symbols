# NETWORK_PROMPT.md

The extraction prompt for the cybernetic_elite network map (Anthony, 2026-09-28: "map the
social / power / financial network detailed in the video"). tools/extract_network_ties.py sends
the part after `---` followed by one dossier, with no web search, and parses the JSON array Codex
prints. tools/build_network.py then resolves names to slugs (in this set, then in every other
dossier set and the atlas) and writes `_network.json`, `_matrix.csv`, `_matrix.md`.

---

You are extracting a tie graph from ONE research dossier on a person, institution, program or
text in the twentieth- and twenty-first-century history of cybernetics, computing, intelligence,
elite finance and their scandals. The dossier follows. Read all of it, especially the section
"The Network" (one entry per documented tie) and "Money and Power".

Output ONLY a JSON array, no prose before or after, no markdown fence. Each element is one tie
between the dossier's subject and ONE other named party: a person, institution, foundation, fund,
company, agency, program, publication, event or text. Use this shape exactly:

{"other": "<the other party's full name as the dossier gives it; full personal names, never a bare surname>",
 "other_type": "<one of: person | institution | company | foundation | agency | program | publication | event | text | place>",
 "kind": "<one of: funded | funded_by | employed | employed_by | advised | advised_by | married | related_to | board_of | founded | founded_by | member_of | introduced | introduced_by | corresponded | met | flew_with | co_authored | published | published_by | invested_in | invested_by | donated_to | received_from | attacked | attacked_by | investigated | investigated_by | prosecuted | prosecuted_by | sued | sued_by | accused | accused_by | testified_about | interviewed | interviewed_by | cited | cited_by | studied_under | taught | protected | recruited | other>",
 "note": "<one line, at most 30 words, saying what the tie is>",
 "dates": "<the years of the tie as the dossier gives them, at most 10 words>",
 "money": "<the amount if the dossier gives one, with currency and year, else empty string>",
 "source": "<the document or reporting the dossier cites for it, at most 15 words>",
 "source_date": "<date of that source as the dossier gives it, at most 6 words>",
 "tier": "<one of: primary | journalism | alleged | subject_claim | rumor | disproved>"}

Rules:
- One element per distinct tie; if the same two parties have several distinct ties (introduced
  AND later corresponded; funded AND sat on the board), give several elements.
- "kind" is from the subject's point of view: if the subject is John Brockman and the other is
  Jeffrey Epstein whom he introduced to others, kind is "introduced"; if the subject is David
  Gelernter and Brockman introduced him to Epstein, kind is "introduced_by" with other = John Brockman.
- Tier follows the dossier's own labels: "primary" for court filings, depositions, flight logs,
  tax and SEC filings, congressional testimony, declassified files, contemporaneous correspondence,
  corporate registries, the institution's own records; "journalism" for named reporters with sources;
  "alleged" for lawsuits and named accusers; "subject_claim" for memoirs and interviews of the
  subject; "rumor" for conspiracy or unsourced material; "disproved" where the dossier says so.
- Include ties the dossier reports as rumor or as disproved, with that tier; do not omit them and
  do not upgrade them.
- Do not invent ties the dossier does not state. Empty array [] is a valid answer.
- Give every person's full name (Jeffrey Epstein, not Epstein; Stewart Brand, not Brand).

The dossier:
