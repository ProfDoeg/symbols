# The text-encoding dossier prompt (how machines have written letters)

Anthony, 2026-09-15: "the history of text encodings for computers, like the contemporary
equivalent… utf-8 and the like." One dossier per encoding or code. `[NAME]` is the only
substitution point; the per-encoding brief follows.

---

[NAME]
Please conduct a comprehensive, source-driven research dossier on this text encoding or
character code, its design, its history and its use. I want the fullest reconstructable
account, from the earliest proposal to the present, chronologically and in detail. Include,
wherever available:

- THE CODE ITSELF: the bit width and structure, the full table or its structure (give the
  table where it is small enough, otherwise the layout: the control block, the printable
  block, the shift states, the byte ranges), what characters it covers and what it cannot
  express, the collating order it implies, the escape and shift mechanisms, the error and
  synchronization properties (how a corrupted or mid-stream reader recovers), the encoding
  of newline, space, deletion, the case question; worked examples of a word or a sentence
  encoded byte by byte, with the same text in one or two neighbouring encodings for
  comparison
- ORIGINS: who designed it, when, in which committee, company, standard or memo (with the
  document numbers: the ASA X3.4 of 1963, ECMA-6, ISO/IEC 646, 2022, 8859, 10646, the RFCs,
  the Unicode Technical Reports, the IBM manuals, the CCITT alphabets); the earlier code it
  grew from and the rivals it beat or lost to; the design decisions and the fights over them
  (lowercase, the control characters, the currency sign, the eight-bit vs seven-bit war,
  Han unification, the 16-bit assumption, the byte-order mark); the anecdotes with their
  sources (Bemer's memos, the Thompson-Pike placemat, the KOI8 trick, the EBCDIC "eight
  bit" defense)
- ADOPTION AND DECLINE: who used it, on which machines, networks and operating systems,
  when it became mandatory or default (the 1968 US federal ASCII mandate, RFC 20, the web's
  drift to UTF-8 and the W3C figures, the IETF's charset rules), how it was replaced or
  absorbed, and what survives of it (control codes, keyboard scan codes, the 0x7F, the
  legacy of code pages in filenames and mojibake)
- THE OTHER SCRIPTS: how this encoding handled or failed the non-Latin scripts (Cyrillic,
  Greek, Hebrew and Arabic with their bidirectionality, the Indic scripts with their shaping,
  Chinese, Japanese and Korean with their thousands of characters, emoji), and the national
  and vendor solutions that filled the gap
- PEOPLE: the engineers, committee chairs, standards editors and companies, with dates
  (Baudot, Murray, Hollerith, Bemer, Mackenzie, Becker, Davis, Collins, Thompson, Pike,
  Whistler, the Unicode Consortium's founders), and the institutions (ASA/ANSI, ECMA, ISO,
  IBM, DEC, Bell Labs, Xerox, Apple, the IETF, the W3C)
- CULTURE: the encoding in software and literature (mojibake as an aesthetic, the ASCII art
  and the demoscene, the emoji vote, the "plain text" ideal, Unicode as a political
  institution deciding which scripts and peoples get encoded and in what order)
- CONTROVERSIES: the disputed firsts and credits, the Han unification debate and the
  Japanese objections, the emoji and the Consortium, the CJK and Tibetan encoding
  disputes, the security issues (homoglyph attacks, the BOM, overlong UTF-8 sequences), the
  standards politics (ISO vs Unicode, the vendor codes)

Include the good and the bad without judgment, and folklore as fully as fact.
For every significant claim distinguish documented text or standard, scholarly
reconstruction, participant recollection, disputed claim, folklore and modern invention, and
say which sources carry it, when the account first appears, who spread it, and what evidence
exists. Do not use summaries as substitutes for the sources; trace to the standards, the RFCs,
the memos and the oral histories (Bemer's own pages, the Computer History Museum oral
histories, Mackenzie's Coded Character Sets, History and Development (1980), Pike's account of
UTF-8's origin, the Unicode Consortium's history page and technical notes, the IETF RFC
archive, the ECMA and ISO catalogues, the Internet Archive for the manuals).

Structure the dossier as: Basic identification (name, standard number, year, bit width,
repertoire, status); The code in detail (with the table or layout and worked examples);
Origins (dated, placed, with the documents); Adoption and decline; The other scripts;
People; Culture; Controversies and disputes; Open questions; Sources (full list of URLs and
editions consulted).
Length: as long as the material requires; for ASCII, Unicode or UTF-8 a thousand lines is not
too many.
