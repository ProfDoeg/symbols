# UTF-16 and UCS-2: research brief

Text-encodings research, Anthony 2026-09-15, separate from the atlas. Appended to
PROMPT_TEMPLATE_ENCODINGS.md by tools/codex_dossier_set.py.

---

ENCODING. UTF-16 and UCS-2: encoding 14 of 17 in this set. Give at the top the standard number, the year, the bit width, the
repertoire and the current status.

THREADS TO PULL, each to be verified against the sources and dated: the original 16-bit Unicode (UCS-2) in Windows NT (1993), Java (1995) and JavaScript, the surrogate pairs of Unicode 2.0 (1996) that made it UTF-16, the byte-order mark (U+FEFF) and the endianness problem (UTF-16LE and BE), the legacy of the 16-bit assumption in every API that counts 'characters' as code units (the emoji that break string lengths), the 'UTF-16 considered harmful' arguments and the utf8everywhere manifesto, the platforms that remain UTF-16 inside (Windows, Java, .NET, JavaScript, Qt).

STANCE. Folklore as fully as fact, labeled. Every claim labeled: documented standard or text,
participant recollection, scholarly reconstruction, disputed, folklore, modern invention. Give
the worked examples byte by byte. Where a story has one witness (the placemat, the 360's unused
ASCII bit), say so. Absence of evidence is a finding.
