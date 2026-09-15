# ISO 2022 and the escape-sequence encodings: research brief

Text-encodings research, Anthony 2026-09-15, separate from the atlas. Appended to
PROMPT_TEMPLATE_ENCODINGS.md by tools/codex_dossier_set.py.

---

ENCODING. ISO 2022 and the escape-sequence encodings: encoding 8 of 17 in this set. Give at the top the standard number, the year, the bit width, the
repertoire and the current status.

THREADS TO PULL, each to be verified against the sources and dated: the ISO/IEC 2022 framework of 1973 (ECMA-35): the G0-G3 sets, the escape sequences that switch character sets, the 94- and 96-character sets, the C0 and C1 controls; its use for the East Asian encodings (ISO-2022-JP in Japanese email, ISO-2022-KR, ISO-2022-CN), the terminal escape sequences (VT100, ANSI X3.64) that descend from it, the elegance and the fragility of stateful encodings, the reason UTF-8 won.

STANCE. Folklore as fully as fact, labeled. Every claim labeled: documented standard or text,
participant recollection, scholarly reconstruction, disputed, folklore, modern invention. Give
the worked examples byte by byte. Where a story has one witness (the placemat, the 360's unused
ASCII bit), say so. Absence of evidence is a finding.
