# Unicode and ISO 10646: Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| Name | **The Unicode Standard**; **ISO/IEC 10646, Universal Coded Character Set (UCS)** |
| Foundational proposal | Joseph D. Becker, **Unicode 88**, final draft dated 29 August 1988 |
| First Unicode edition | **Unicode 1.0**, Volume 1 in October 1991; Volume 2, covering Han characters, in June 1992 |
| First synchronized international standard | **ISO/IEC 10646-1:1993**; Unicode 1.1 aligned Unicode with it |
| Current Unicode edition | **Unicode 17.0.0**, 9 September 2025 |
| Current ISO edition | **ISO/IEC 10646:2020**, sixth edition, with Amendments 1:2023 and 2:2025; revision is under development |
| Abstract code width | **21 significant bits**, code points U+0000–U+10FFFF |
| Encoding forms | **UTF-8:** 8-bit code units, one to four bytes; **UTF-16:** 16-bit code units, one or two units; **UTF-32:** 32-bit code units, one unit |
| Repertoire, Unicode 17.0 | **159,801 assigned graphic and format characters**: 159,629 graphic and 172 format characters, plus 65 control-code assignments. The codespace also contains private-use, surrogate, noncharacter and reserved code points |
| Status | Current, actively maintained, synchronized in repertoire and code-point assignments between Unicode and ISO/IEC 10646 |
| Scope | Abstract characters and selected format controls—not fonts, arbitrary glyphs, logos, personal inventions, keyboard scan codes, language semantics or general page layout |

**Evidence label — documented standard:** Unicode 17.0 defines the range U+0000–U+10FFFF and the three encoding forms. Its official count is 159,801 graphic-plus-format characters, including 102,998 Han characters when all unified, compatibility and extension counts are combined. ISO describes its current edition as ISO/IEC 10646:2020, Edition 6, amended in 2023 and 2025. [Unicode 17.0 version page](https://www.unicode.org/versions/Unicode17.0.0/), [Unicode 17.0 character counts](https://www.unicode.org/versions/stats/charcountv17_0.html), [ISO/IEC 10646:2020 catalogue record](https://www.iso.org/standard/76835.html).

A fundamental distinction is necessary:

- **Unicode/10646 is a coded character set and text-processing architecture.**
- **UTF-8, UTF-16 and UTF-32 are encodings of that set.**
- A code point is not necessarily a user-perceived character, glyph, byte or storage cell.
- One grapheme such as `é`, a Devanagari consonant cluster, an emoji flag or a family emoji can comprise several code points.
- Conversely, compatibility characters sometimes give separately encoded forms to what could otherwise be treated as styled versions of other characters.

Unicode and ISO/IEC 10646 assign the same characters to the same code points. Unicode additionally standardizes extensive properties, algorithms and conformance rules: normalization, bidirectional ordering, case conversion, segmentation, line breaking, identifiers, emoji sequences and security profiles. ISO 10646 concentrates on the UCS repertoire, architecture and encoding forms. Their version numbers and publication cycles need not coincide.

---

## Evidentiary convention

Every historical assertion below is marked, explicitly or by paragraph, as one of:

- **[STANDARD]** Normative standard, RFC, committee record or contemporary proposal.
- **[CONTEMPORARY]** Documentary evidence produced at or near the event.
- **[RECOLLECTION]** Later testimony by a participant.
- **[SCHOLARLY]** Historical reconstruction based on records and interviews.
- **[DISPUTED]** Substantial disagreement exists over interpretation, priority or consequences.
- **[FOLKLORE]** A widely repeated anecdote for which evidence is limited.
- **[MODERN INVENTION]** A later slogan or simplification not found in the early record.
- **[FINDING: ABSENCE]** The searched record did not substantiate a claim.

These labels distinguish the kind of evidence, not its truth or moral value.

---

# The code in detail

## 1. Codespace and planes

Unicode’s codespace is the inclusive integer range:

```text
U+000000–U+10FFFF
```

That is 1,114,112 possible code points, conventionally arranged as 17 planes of 65,536 positions each:

| Plane | Range | Conventional role |
|---:|---|---|
| 0 | U+0000–U+FFFF | Basic Multilingual Plane, BMP |
| 1 | U+10000–U+1FFFF | Supplementary Multilingual Plane, SMP: historic and constructed scripts, music, mathematics, emoji and symbols |
| 2 | U+20000–U+2FFFF | Supplementary Ideographic Plane, SIP |
| 3 | U+30000–U+3FFFF | Tertiary Ideographic Plane, TIP |
| 4–13 | U+40000–U+DFFFF | Reserved |
| 14 | U+E0000–U+EFFFF | Supplementary Special-purpose Plane, including tags and variation selectors |
| 15 | U+F0000–U+FFFFF | Supplementary Private Use Area-A |
| 16 | U+100000–U+10FFFF | Supplementary Private Use Area-B |

**[STANDARD]** ISO/IEC 10646:2020 explicitly identifies the BMP, SMP, SIP, TIP and Supplementary Special-purpose Plane and defines UTF-8, UTF-16 and UTF-32. [ISO catalogue](https://www.iso.org/standard/76835.html).

### Special ranges

- U+0000–U+007F: ASCII-compatible Basic Latin and C0 controls.
- U+0080–U+009F: C1 control positions.
- U+D800–U+DFFF: 2,048 surrogate code points, reserved for UTF-16 machinery and not Unicode scalar values.
- U+E000–U+F8FF: BMP Private Use Area.
- U+FDD0–U+FDEF and the last two positions of every plane: 66 noncharacters.
- U+FFFE and U+FFFF are therefore not assignable characters.
- U+FEFF is ZERO WIDTH NO-BREAK SPACE/BYTE ORDER MARK, although WORD JOINER U+2060 supersedes its in-text word-joining use.

Unicode scalar values are all code points except U+D800–U+DFFF.

## 2. What is encoded

**[STANDARD]** Unicode’s governing model is “characters, not glyphs.” It assigns identities to abstract characters and gives them properties; a font and shaping system choose glyphs. The distinction is central to the current core specification. [Unicode 17.0, Chapter 1](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-1/).

The repertoire covers, among much else:

- Latin, Greek, Cyrillic, Armenian and Georgian;
- Hebrew, Arabic, Syriac, Thaana and other right-to-left scripts;
- the major Indic and Southeast Asian Brahmic scripts;
- Han ideographs, kana, hangul and bopomofo;
- historic scripts from cuneiform and Egyptian hieroglyphs to Linear A and Old Persian;
- mathematical alphanumerics and operators;
- punctuation, currency, technical, musical and religious symbols;
- emoji and the characters from which emoji sequences are constructed;
- format controls for bidirectionality, joining, variation selection and other textual processes.

It cannot, by itself, express:

- arbitrary glyph shape, typeface, color or calligraphy;
- general document layout;
- every logo or personal symbol;
- unencoded characters;
- pronunciation, language, sorting convention or semantic interpretation;
- all user-perceived symbols as single code points;
- arbitrary images.

Fonts, OpenType shaping, markup, language tags, locale data and higher-level protocols supply these layers.

## 3. No single “Unicode table”

The repertoire is too large for a useful single printed table. Its structure is published as:

1. block code charts;
2. the Unicode Character Database;
3. names lists and property files;
4. normative algorithms and annexes;
5. ISO 10646 code tables.

Blocks are editorial ranges, not reliable semantic categories. Script membership is represented by properties and can cross block boundaries. “Common” punctuation and “Inherited” combining marks may be used by several scripts.

## 4. UTF-8

### Byte structure

| Scalar-value range | UTF-8 bit pattern | Length |
|---|---|---:|
| U+0000–U+007F | `0xxxxxxx` | 1 byte |
| U+0080–U+07FF | `110xxxxx 10xxxxxx` | 2 |
| U+0800–U+FFFF, excluding surrogates | `1110xxxx 10xxxxxx 10xxxxxx` | 3 |
| U+10000–U+10FFFF | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` | 4 |

Valid leading-byte ranges are more restrictive than the bit diagram alone suggests:

```text
00–7F                       ASCII
C2–DF 80–BF                 two-byte sequence
E0 A0–BF 80–BF              three-byte sequence, no overlong form
E1–EC 80–BF 80–BF
ED 80–9F 80–BF              excludes surrogates
EE–EF 80–BF 80–BF
F0 90–BF 80–BF 80–BF        no overlong form
F1–F3 80–BF 80–BF 80–BF
F4 80–8F 80–BF 80–BF        stops at U+10FFFF
```

`C0`, `C1`, `F5`–`FF`, isolated `80`–`BF`, overlong sequences and UTF-8 encodings of surrogates are invalid.

### Synchronization and errors

UTF-8 is self-synchronizing at the code-point level:

- ASCII bytes begin `0`;
- leading bytes begin `11`;
- continuation bytes begin `10`;
- scanning backward at most three continuation bytes finds a candidate boundary;
- a continuation byte can never be mistaken for ASCII or a leading byte.

Corruption normally damages the containing sequence, not every subsequent character. Insertions or deletions may affect a small locality before boundaries are rediscovered.

**[STANDARD]** Unicode defines processing in terms of ill-formed subsequences and “maximal subparts.” A decoder must not interpret overlong sequences, surrogate encodings or values beyond U+10FFFF as characters. Recovery policy may reject input or replace ill-formed maximal subparts—commonly with U+FFFD REPLACEMENT CHARACTER. [Unicode 17.0 core specification](https://www.unicode.org/versions/Unicode17.0.0/UnicodeStandard-17.0.pdf), [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html).

Self-synchronization does not solve grapheme boundaries. Starting on a combining mark, joiner or emoji modifier can still begin in the middle of a user-perceived character.

## 5. UTF-16

BMP scalar values are one 16-bit code unit. Supplementary values use a surrogate pair.

For scalar value `U` above U+FFFF:

```text
V = U - 0x10000
high = 0xD800 + (V >> 10)
low  = 0xDC00 + (V & 0x3FF)
```

Ranges:

```text
High surrogates: D800–DBFF
Low surrogates:  DC00–DFFF
```

Because the ranges are disjoint, a well-formed reader can identify lone and reversed surrogates. At an arbitrary 16-bit boundary, at most one code unit of inspection is needed to know whether the reader has landed on the low half of a pair. At an arbitrary *byte* boundary, synchronization additionally depends on recovering 16-bit alignment and byte order.

UTF-16BE and UTF-16LE fix byte order. Unsuffixed UTF-16 can employ an initial BOM:

```text
FE FF  UTF-16BE BOM
FF FE  UTF-16LE representation of U+FEFF
```

`FF FE` cannot represent an ordinary Unicode character under big-endian interpretation, so it signals reversal.

## 6. UTF-32

Each scalar value occupies a 32-bit code unit:

```text
UTF-32BE: 00 01 F3 0D  for U+1F30D EARTH GLOBE EUROPE-AFRICA
UTF-32LE: 0D F3 01 00
```

It offers constant code-point width but not constant grapheme width. It uses roughly four times the storage of ASCII for English text and can lose four-byte alignment after byte insertion or deletion. Valid units must be at most `0010FFFF` and not in the surrogate range.

BOMs:

```text
00 00 FE FF  UTF-32BE
FF FE 00 00  UTF-32LE
```

## 7. The byte-order mark

**[STANDARD]** U+FEFF at the beginning of a UTF-16 or UTF-32 stream can identify byte order. In UTF-8 its bytes are `EF BB BF`; UTF-8 has no byte-order ambiguity, so RFC 3629 says a protocol should forbid or permit it explicitly and otherwise recommends against adding it when the character set is already known. It may be stripped only at the beginning under the applicable protocol. [Unicode Chapter 23](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-23/), [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html).

**[DISPUTED practice]:** Microsoft’s use of a UTF-8 “signature” made UTF-8 detection convenient in some workflows but caused failures in Unix scripts, concatenated data and protocols expecting the first byte to be syntax. Calling it a “BOM” in UTF-8 is conventional but semantically misleading: no byte order is being marked.

## 8. Newline, space and deletion

Unicode preserves ASCII’s values:

| Function | Code point | UTF-8 |
|---|---:|---|
| NUL | U+0000 | `00` |
| Horizontal tab | U+0009 | `09` |
| Line feed | U+000A | `0A` |
| Carriage return | U+000D | `0D` |
| Space | U+0020 | `20` |
| Delete | U+007F | `7F` |
| Next line | U+0085 | `C2 85` |
| Line separator | U+2028 | `E2 80 A8` |
| Paragraph separator | U+2029 | `E2 80 A9` |
| Replacement character | U+FFFD | `EF BF BD` |

Unicode does not decree one operating-system newline convention. Unix conventionally uses LF; traditional Mac systems used CR; DOS and Windows conventionally use CR LF. Protocols can impose their own rule.

U+007F retains the ASCII DEL code-point identity. Unicode does not assign it a visible erasure glyph or make it a keyboard scan code. Its punched-tape “all holes” origin belongs to ASCII’s ancestry, not to a new Unicode design choice.

## 9. Escape and shift states

UTF-8, UTF-16 and UTF-32 have **no character-set shift state**. A character’s interpretation does not depend on an earlier SO, SI, ESC or ISO 2022 designation sequence.

ASCII controls such as ESC U+001B, SHIFT OUT U+000E and SHIFT IN U+000F remain encoded for compatibility, but Unicode does not use them to change repertoire. This statelessness contrasts with ISO-2022-JP, stateful EBCDIC DBCS systems and seven-bit national switching schemes.

Higher-level formatting controls—including bidi isolates and variation selectors—do affect interpretation or display, but they do not switch the underlying coded character set.

## 10. Case

Unicode encodes uppercase, lowercase and titlecase characters separately where the writing system uses them. It supplies:

- simple and full case mappings;
- language-independent default casing;
- case folding for caseless matching;
- contextual and language-sensitive special casing.

There is no universal fixed offset between cases. Examples:

- ASCII `A`/`a` differ by 0x20.
- German `ß` can uppercase to the sequence `SS`, while capital `ẞ` is separately encoded.
- Greek sigma lowercases contextually to `σ` or final `ς`.
- Turkish dotted and dotless I require language-sensitive handling.

A code-point comparison is therefore not a linguistically correct caseless comparison.

## 11. Collation

**[STANDARD]** Code-point order is not a general alphabetic sorting order. Unicode does not imply that Swedish, German, Hindi, Chinese or emoji should sort by numerical code point. The Unicode Collation Algorithm and the Default Unicode Collation Element Table provide a tailorable default; CLDR supplies locale tailorings.

The original designers did consider ordering. Unicode’s history records that early drafts alphabetized within scripts and briefly used a Mark Davis “Gray code” proposal for Han. In 1989 the group moved toward existing ISO and national orderings. That historical arrangement remains visible, but stability prevents wholesale reordering. [Unicode Version 1 chronology](https://www.unicode.org/history/versionone.html).

## 12. Normalization

Some abstract text has more than one Unicode representation:

```text
é = U+00E9
é = U+0065 U+0301
```

The four normalization forms are:

| Form | Operation |
|---|---|
| NFD | Canonical decomposition and canonical ordering |
| NFC | Canonical decomposition, ordering, then composition where defined |
| NFKD | Compatibility decomposition and ordering |
| NFKC | Compatibility decomposition, ordering, then composition |

**[STANDARD]** NFC/NFD preserve canonical equivalence. NFKC/NFKD can erase distinctions such as fullwidth forms, circled numbers and typographic mathematical alphabets and must not be applied blindly. Normalization was precisely standardized in UTR #15 for Unicode 3.0 in 1999; its current specification is UAX #15. [Original UTR #15 revision 18](https://www.unicode.org/standard/reports/tr15/tr15-18.html), [current UAX #15](https://www.unicode.org/reports/tr15/).

**[CONTROVERSY and institutional lesson]:** Unicode 1.1 relocated Korean Hangul syllables for Unicode 2.0. RFC 3629 calls the episode the “Korean mess.” The incompatibility helped produce the stringent modern stability policies. It is one of the clearest cases where early standards work damaged existing data in order to repair architecture.

## 13. Bidirectional text

Unicode stores Hebrew and Arabic mainly in logical reading order. The Unicode Bidirectional Algorithm computes display order from character bidi classes, embedding levels and explicit controls. Modern isolates reduce spillover between nested direction runs.

The result is neither “reverse Arabic” nor simply “right-to-left bytes.” Numbers may remain left-to-right inside Arabic text, and punctuation can acquire direction contextually.

**[STANDARD]:** UAX #9 is normative for Unicode conformance where bidi processing is performed. Mark Davis created its initial version; the current annex acknowledges Aharon Lanin, Andrew Glass, Ken Whistler, Robin Leroy and many Arabic and Hebrew specialists. [UAX #9](https://www.unicode.org/reports/tr9/).

## 14. Worked example

Text:

```text
Hi, 世界 🌍
```

### Code points

| Character | Code point | Name |
|---|---:|---|
| `H` | U+0048 | LATIN CAPITAL LETTER H |
| `i` | U+0069 | LATIN SMALL LETTER I |
| `,` | U+002C | COMMA |
| space | U+0020 | SPACE |
| `世` | U+4E16 | CJK UNIFIED IDEOGRAPH-4E16 |
| `界` | U+754C | CJK UNIFIED IDEOGRAPH-754C |
| space | U+0020 | SPACE |
| `🌍` | U+1F30D | EARTH GLOBE EUROPE-AFRICA |

### UTF-8, byte by byte

```text
H       48
i       69
,       2C
SPACE   20
世      E4 B8 96
界      E7 95 8C
SPACE   20
🌍      F0 9F 8C 8D
```

Complete stream:

```text
48 69 2C 20 E4 B8 96 E7 95 8C 20 F0 9F 8C 8D
```

### UTF-16BE

```text
H       00 48
i       00 69
,       00 2C
SPACE   00 20
世      4E 16
界      75 4C
SPACE   00 20
🌍      D8 3C DF 0D
```

For U+1F30D:

```text
U - 10000 = 0F30D
high surrogate = D83C
low surrogate  = DF0D
```

Complete stream without BOM:

```text
00 48 00 69 00 2C 00 20 4E 16 75 4C 00 20 D8 3C DF 0D
```

### UTF-32BE

```text
00 00 00 48
00 00 00 69
00 00 00 2C
00 00 00 20
00 00 4E 16
00 00 75 4C
00 00 00 20
00 01 F3 0D
```

### Comparison with neighboring legacy encodings

ASCII encodes the prefix:

```text
Hi,   = 48 69 2C 20
```

but cannot encode `世界` or `🌍`.

ISO-8859-1 likewise cannot encode those characters. A replacement-based conversion might produce:

```text
48 69 2C 20 3F 3F 20 3F
H  i  ,     ?  ?     ?
```

but that byte sequence represents destructive substitution, not the original text.

GB18030 can represent the Chinese and emoji characters, but it is a separate variable-length encoding with different byte assignments. UTF-8’s principal interoperability advantage is that every ASCII-only string has exactly its ASCII byte representation.

### Normalization example

Text:

```text
Café
```

NFC code points and UTF-8:

```text
U+0043  C   43
U+0061  a   61
U+0066  f   66
U+00E9  é   C3 A9
```

NFD:

```text
U+0043  C                         43
U+0061  a                         61
U+0066  f                         66
U+0065  e                         65
U+0301  COMBINING ACUTE ACCENT    CC 81
```

The UTF-8 byte strings differ although the two Unicode strings are canonically equivalent.

---

# Origins

## 1. Long ancestry

Unicode did not spring from a single earlier code. Its background includes telegraph codes, punched cards, ASCII, EBCDIC, ISO 646/2022/8859, East Asian multibyte standards and workstation-internal character systems.

### Baudot and Murray

**[SCHOLARLY]:** Émile Baudot’s five-unit telegraph alphabet of the 1870s and Donald Murray’s early-twentieth-century modifications used letters/figures shift states to obtain more symbols from 32 patterns. These systems demonstrate the old compromise among repertoire, fixed width and transmission cost.

Unicode rejected repertoire shifts as a basic encoding model. UTF encodings are variable in storage length, but a scalar value has a context-independent identity.

### Hollerith

**[SCHOLARLY]:** Herman Hollerith’s punched-card systems represented data through hole positions rather than a single standardized binary character code. Their importance to Unicode is institutional and industrial—especially through IBM—not a direct bit-level descent.

### ASCII, ISO 646 and ISO 2022

ASCII—ASA X3.4-1963, revised 1965 and 1967/1968—established the lower 128 positions that Unicode preserves unchanged. ECMA-6 and ISO 646 internationalized the seven-bit structure, sometimes allowing national substitutions. ISO 2022 created a general architecture for designating and shifting among character sets. ISO 8859 supplied several eight-bit single-byte repertoires.

This produced interoperability within bounded communities but not a single global character identity. The same byte could mean different characters under different code pages.

### EBCDIC and vendor codes

IBM’s EBCDIC evolved from punched-card-oriented BCD families and used eight bits. Its noncontiguous letter ranges and multiple code pages complicated interchange with ASCII and later Unicode.

**[FOLKLORE/qualified]:** The “EBCDIC eight-bit defense”—that IBM could answer seven-bit ASCII advocates by advertising a larger eight-bit code—is a plausible characterization of contemporary commercial politics, but it should not substitute for IBM design records. EBCDIC’s layout also preserved compatibility with existing equipment and software; it was not merely a marketing stunt.

**[FINDING: ABSENCE]:** No primary Unicode source examined establishes a direct causal line from a particular IBM “eight bit” slogan to Unicode’s design.

### East Asian standards

Japanese Shift-JIS, EUC-JP and ISO-2022-JP; Chinese GB and Big5; Korean KS encodings; and vendor extensions offered large repertoires through multibyte or shifted representations. They were effective locally but mutually incompatible.

**[RECOLLECTION]:** Mark Davis says his practical conversion experience came from Apple’s KanjiTalk work in Sapporo around 1985. He and Ken Krugler initially misunderstood Shift-JIS as uniformly double-byte and discovered that some byte values could occur as independent characters or as parts of multibyte characters. The account first appears in a 1998 Laura Wideburg interview reproduced on Unicode’s history page. It is useful participant evidence, but not an engineering log. [Early Years of Unicode](https://www.unicode.org/history/earlyyears.html).

## 2. Xerox and Apple, 1987–1988

**[DOCUMENTED institutional history]:** Unicode traces its groundwork to late 1987 discussions among:

- Joseph D. Becker at Xerox;
- Lee Collins, then at Xerox and subsequently associated with Apple’s work;
- Mark Davis at Apple.

They compared fixed- and mixed-width access, estimated system storage for two-byte text and counted characters in world alphabets. Xerox Star’s multilingual work and East Asian two-byte standards were antecedents. [Early Years](https://www.unicode.org/history/earlyyears.html).

### Unicode 88

Becker drafted the proposal in February 1988 and issued the final **Unicode 88** on 29 August 1988. He presented its principles to `/usr/group`’s International Subcommittee in Dallas that August and later to standards bodies.

**[CONTEMPORARY]:** The document explicitly credits Becker with the general proposal, Lee Collins with ideographic unification and Peter Fenwick and Dave Opstad with other contributions. It describes Unicode as a potential “new ASCII” and advocates pure 16-bit character codes. [Unicode 88](https://www.unicode.org/history/Unicode88.pdf).

**[CREDIT]:** Becker is properly credited with naming Unicode and authoring its manifesto. Collins and Davis were not secondary bystanders: the Consortium’s account says the three derived the basic architecture. In a 2002 mailing-list exchange, Kenneth Whistler identified Becker and Collins as especially instrumental; Becker immediately insisted that Davis also be credited and called his own manifesto the intentional inception of the specific initiative. This is unusually transparent evidence of how priority was negotiated by the participants themselves. [2002 history correspondence](https://www.unicode.org/mail-arch/unicode-ml/y2002-m02/0110.html).

### “Sixteen bits are enough”

**[CONTEMPORARY fact]:** Unicode 88 proposed a 16-bit codespace of 65,536 values and argued that contemporary character counts could fit.

**[MODERN INVENTION/oversimplification]:** The phrase “sixteen bits ought to be enough for anybody” is often presented like an authenticated quotation. The early proposal undeniably embodies the assumption, but the slogan is not established by the searched primary record as Becker’s verbatim statement.

The 16-bit decision was technically attractive because it offered:

- fixed-width indexing;
- simple array and string implementations;
- compactness compared with 32-bit storage;
- room far beyond contemporary eight-bit code pages;
- compatibility with a “wide character” model.

Its weaknesses were underestimation of:

- historic scripts;
- rare and personal-name Han ideographs;
- compatibility characters required for round trips;
- notation and symbol collections;
- future additions;
- the political cost of deciding which characters merited scarce BMP space.

## 3. Han work, 1988–1990

In July 1988 Apple bought the Research Libraries Group’s CJK database for study. Xerox already held unified-Han data for font work. Collins developed Apple’s database; Becker and Collins correlated the Apple/RLG and Xerox materials.

In September 1988 Becker and Collins argued before ANSI X3L2 for Han unification and for use of the C0/C1 areas in the developing ISO code. By August 1989 they had merged their Han databases, preserving distinctions present in source standards while unifying selected cross-standard counterparts.

**[DOCUMENTED by later institutional chronology]:** These dates come from Unicode’s reconstruction, which relied on corporate and committee records plus interviews. [Version 1 chronology](https://www.unicode.org/history/versionone.html).

## 4. Formation of the working group and Consortium

By 1989–1990 the working group included people from Apple, Xerox, Metaphor, RLG, Sun and Microsoft. Important contributors included:

- Ken Whistler;
- Mike Kernaghan;
- Asmus Freytag;
- Michel Suignard;
- Karen Smith-Yoshimura;
- Joan Aliprand;
- Glenn Wright.

Mike Kernaghan, Bill English, Mark Davis and Asmus Freytag organized the business structure. Unicode, Inc. was incorporated in California on **3 January 1991**.

**[DOCUMENTED institutional account]:** [Unicode history summary](https://www.unicode.org/history/summary.html), [History Corner](https://www.unicode.org/history/).

Early corporate members included Apple, Microsoft, IBM, Sun, Digital, Lotus, Novell, NeXT and others at different stages. Membership changed over time, so a list of “founders” must not be confused with every contributor to the standard.

## 5. ISO’s Universal Coded Character Set project

ISO/IEC JTC 1/SC 2/WG 2 pursued a universal multiple-octet coded character set during the 1980s. An ISO principle recorded in 1984 called for an international two-byte graphic character set and equal storage per character. The original ISO project was therefore not a reaction invented after Unicode.

Its first Draft International Standard—commonly called **DIS 10646-1**—had a complex multi-octet architecture and differed incompatibly from Unicode in repertoire, coding structure and character model.

The first DIS failed its ballot in June 1991.

## 6. The 1991–1993 merger

The merger was a process, not a single treaty.

### Timeline

- **May 1991, San Francisco:** after WG2 meeting 19, ISO and Unicode supporters held an informal ad hoc meeting.
- **30 May/3 June 1991:** Edwin Hart circulated merger document 10646M/91-01 and associated drafts.
- **June 1991:** the first DIS 10646 ballot failed.
- **August 1991, Geneva:** WG2 accepted key compromises including Han unification, combining characters, Unicode repertoire additions and removal of certain byte-value restrictions.
- **October 1991, Paris:** further agreement and trust-building.
- **1992:** a revised DIS proceeded.
- **1993:** ISO/IEC 10646-1:1993 was published.
- **Unicode 1.1:** aligned Unicode’s code points and repertoire with the international standard.

**[CONTEMPORARY]:** Hart’s memo explicitly says the world was too small for two incompatible multi-octet standards and records consensus among participants from eight countries and more than twelve enterprises. [Hart memo](https://www.unicode.org/history/hartmemo.html).

**[RECOLLECTION]:** In a 1995 interview Hart described distrust between the “Unicode” and “ISO” camps, characterized ISO’s design as “big-frame” and Unicode’s as “workstation,” and emphasized his role as neutral facilitator. He names Mike Ksar, Masami Hasegawa, Lee Collins, Ken Whistler and IBM representative Isai Scheinberg. [Hart interview](https://www.unicode.org/history/hartinterview.html).

**[DISPUTED credit]:** Popular accounts sometimes say Unicode defeated ISO; others say ISO absorbed Unicode. Neither is technically adequate. Unicode accepted ISO ordering, naming and the UCS codespace; ISO accepted Unicode’s repertoire architecture, combining characters and unified Han approach. The organizations remained separate but synchronized.

## 7. Unicode 1.0 and 1.1

Unicode 1.0’s first volume appeared in October 1991. Its second volume, containing Han material, followed in June 1992. Unicode 1.1 incorporated merger changes and aligned with ISO/IEC 10646-1:1993.

The early standard already contained Latin, Greek, Cyrillic, Armenian, Hebrew, Arabic, major Indic scripts, Thai, Lao, Georgian, kana, bopomofo, hangul, Tibetan and unified Han, although coverage and character properties were much less mature than today.

**[STANDARD/history]:** [Unicode publication dates](https://www.unicode.org/history/publicationdates.html), [Unicode 1.1 archive](https://www.unicode.org/versions/Unicode1.1.0/).

## 8. UTF-8, 1992–1993

ISO 10646’s large character numbers needed a file- and Unix-friendly byte representation. Earlier transformation proposals circulated through X/Open, including FSS-UTF.

### The Thompson–Pike design

**[RECOLLECTION, single principal narrative]:** Rob Pike’s 2003 account says that on 2 September 1992 he and Ken Thompson discussed the problem in a New Jersey diner. Thompson designed the recognizable self-synchronizing prefix structure on a placemat; they returned to Bell Labs, implemented it rapidly in Plan 9 and reported the result to X/Open. [Pike, “UTF-8 history”](https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt).

The encoding was successively called FSS-UTF, UTF-2 and UTF-8. It was publicly presented in the Plan 9 context at the January 1993 USENIX meeting.

**[FOLKLORE, well-founded but limited]:** “UTF-8 was invented on a placemat” is supported principally by Pike’s participant recollection about Thompson’s act of design. No surviving placemat is in the cited record. The anecdote should not erase the preceding X/Open proposals or subsequent standardization work.

**[CREDIT]:** Thompson devised the decisive byte pattern; Pike specified requirements, witnessed the design and co-implemented the Plan 9 conversion. F. Yergeau authored the Internet RFC specifications.

## 9. RFC lineage

- RFC 20 (1969): ASCII format for network interchange.
- RFC 1341 (1992): MIME, enabling charset labeling.
- RFC 1345 (1992): character mnemonics and coded-character-set registrations.
- RFC 2044 (1996): early UTF-8 specification.
- RFC 2279 (1998): revised UTF-8, allowing historical five- and six-byte forms.
- RFC 2277 (1998): IETF charset policy; new text protocols must be able to use UTF-8.
- RFC 2781 (2000): UTF-16.
- RFC 3629 (2003): modern UTF-8, restricted to U+10FFFF and one to four bytes.
- RFC 5198 (2008): Unicode format for network interchange, specifying normalized UTF-8 profiles.

**[STANDARD]:** RFC 2277 says protocols “MUST be able to use” UTF-8 for all text. It does not say that every existing protocol or stored file must default exclusively to UTF-8. [RFC 2277](https://www.rfc-editor.org/rfc/rfc2277.html).

RFC 3629 made Unicode’s definition normative, excluded surrogates and values above U+10FFFF, prohibited overlong forms and discussed BOM and security. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html).

## 10. Expansion beyond 16 bits

By the early 1990s it was clear that the BMP could not hold the desired repertoire.

Unicode and ISO reserved U+D800–U+DFFF for surrogate pairs. UTF-16 maps 1,048,576 supplementary values through those 2,048 code units. Added to the 65,536 BMP positions, this creates the 17-plane range ending at U+10FFFF.

- Surrogates were developed through ISO/Unicode negotiations and amendments.
- Unicode 2.0, published in 1996, incorporated the enlarged architecture.
- UTF-16 was subsequently standardized by Unicode, ISO 10646 and RFC 2781.
- RFC 3629 later restricted UTF-8 to the same range.

**[DISPUTED interpretation]:** Surrogates can be described either as an elegant compatibility extension preserving existing 16-bit APIs or as permanent technical debt created by the original 16-bit assumption. Both descriptions identify real properties.

---

# Adoption and consolidation

## 1. Early operating systems and platforms

Unicode gained traction because major software vendors participated before standardization was complete.

- Microsoft Windows NT adopted a 16-bit wide-character model based on early Unicode/UCS-2.
- Apple incorporated Unicode into text technologies while retaining legacy Macintosh encodings for compatibility.
- IBM developed conversion infrastructure and later used Unicode across products, Java and ICU.
- Sun and Java adopted 16-bit `char`, later interpreted as UTF-16 code units.
- Plan 9 adopted UTF-8 system-wide in the early 1990s.
- Unix and Linux communities gradually favored UTF-8 because ASCII files and APIs remained largely usable.
- ICU, originating in industry work including Taligent/IBM, made Unicode properties, conversion, collation and formatting broadly available.

The initial Windows and Java idea that one 16-bit `char` equals one character became false for supplementary characters and was already incomplete for combining sequences.

## 2. Internet and email

MIME made encodings labelable but initially supported a large variety of charsets. Mislabeling, missing labels and incorrect defaults generated mojibake.

RFC 2277 established UTF-8 capability as IETF best practice in 1998. RFC 3629 stabilized modern UTF-8 in 2003. RFC 5198 recommended NFC-based UTF-8 for network interchange while recognizing protocol-specific needs. [RFC 5198](https://www.rfc-editor.org/rfc/rfc5198/).

IANA’s charset registry preserves names and aliases for legacy interoperability. “Unicode” is therefore not generally a sufficient MIME encoding label: `UTF-8`, `UTF-16LE` and other concrete forms matter.

## 3. The Web

HTML began amid ISO-8859-1 and Windows-1252 practice, with East Asian regional encodings also common. Browsers developed elaborate sniffing behavior because deployed labels were frequently absent or false.

The Web’s eventual convergence on UTF-8 was driven by:

- ASCII compatibility;
- universal repertoire;
- browser and server support;
- XML and HTML internationalization;
- database and language-runtime defaults;
- the declining need for byte-saving single-language encodings;
- security and interoperability advantages of one encoding.

**[MEASUREMENT, methodology-dependent]:** W3Techs reported on 11 September 2026 that UTF-8 was used by **99.1% of websites whose encoding it could identify**, and 99.3% among its top-million cohort. This is not a census of every file on the Web and should not be quoted without its denominator. [W3Techs UTF-8 survey](https://w3techs.com/technologies/breakdown/en-utf8/ranking).

## 4. Filesystems and filenames

Modern Unix-like filesystems often store filenames as uninterpreted byte sequences, while user space conventionally treats them as UTF-8. macOS historically used a decomposed Unicode convention in filesystem APIs. Windows stores filenames in UTF-16.

Consequences include:

- filenames that look identical but normalize differently;
- byte sequences valid on one Unix system but invalid as UTF-8;
- inaccessible or mangled names after cross-platform transfer;
- APIs exposing code units rather than grapheme clusters;
- legacy code-page names becoming mojibake under a new locale.

## 5. Databases and programming languages

Unicode is now the standard internal or interchange model in Java, JavaScript, .NET, Python 3, Swift, Rust, Go and modern database systems, but internal representations differ:

- Java and JavaScript expose UTF-16 code units in many APIs.
- Go strings are byte sequences conventionally containing UTF-8.
- Rust strings require well-formed UTF-8.
- Python 3 uses an implementation-dependent compact representation while presenting strings as Unicode code points.
- databases distinguish encoding, collation and normalization policy.

This matters because “string length” can mean bytes, code units, scalar values or grapheme clusters.

## 6. What survived from older codes

Unicode absorbed rather than erased much of the earlier world:

- ASCII’s first 128 code points remain invariant.
- C0/C1 control identities remain.
- ISO 8859-1 maps directly to U+0000–U+00FF by code-point number, although UTF-8 byte values differ above ASCII.
- compatibility characters preserve round trips with legacy sets.
- private-use characters support closed agreements.
- mapping tables and code pages remain necessary for archival data and old protocols.
- CR, LF, TAB, ESC, DEL and other early control conventions remain embedded in software.

Keyboard scan codes are not Unicode, although keyboard layouts ultimately produce Unicode text.

---

# The other scripts

## 1. Cyrillic

Pre-Unicode Cyrillic environments used encodings including ISO 8859-5, IBM and DOS code pages, Windows-1251, Mac Cyrillic and the KOI family.

### The KOI8 “trick”

**[DOCUMENTED technical property; anecdotal attribution varies]:** KOI8-R arranges Russian letters so that clearing the high bit produces a roughly readable Latin transliteration rather than meaningless punctuation. For example, Cyrillic letter positions were chosen to correspond approximately to visually or phonetically related ASCII letters.

**[FOLKLORE qualification]:** This is often called a clever emergency communications feature, but claims about exactly who first proposed the trick and which failure scenario motivated it require contemporary Soviet/Russian standards documentation. Its existence is verifiable from the table; its heroic origin stories are less secure.

Unicode gives Cyrillic independent code points and supplies case and normalization properties. It does not transliterate Cyrillic into Latin.

## 2. Greek

ASCII and many national seven-bit variants could not represent full Greek alongside English. ISO 8859-7 and vendor pages supplied regional solutions. Unicode encodes Greek as a separate script even where letters resemble Latin.

This separation is semantically correct but creates confusable identifiers: Latin `A`, Greek `Α` and Cyrillic `А` are distinct characters with similar glyphs.

## 3. Hebrew and Arabic

Legacy systems used ISO 8859-8, ISO 8859-6, DOS and Windows pages, often with visual-order or presentation-form conventions.

Unicode’s preferred model is:

- logical-order storage;
- base letters plus combining marks;
- contextual shaping performed by the renderer;
- the Bidirectional Algorithm for display order;
- joining controls only where needed;
- presentation forms retained chiefly for compatibility.

It can encode vocalization and Qur’anic marks, but correct rendering requires shaping, mark positioning, fonts and language-aware software. Encoding a script is not the same as supporting it well.

## 4. Indic scripts

Unicode generally encodes Indic scripts according to an underlying-character model: consonants, dependent vowels, virama and signs. Renderers reorder and combine these into displayed syllables and conjuncts.

Advantages include searchable linguistic structure and reuse of common shaping logic. Costs include:

- a user-perceived akshara spanning many code points;
- cursor and deletion problems in naive software;
- several canonically or visually similar sequences;
- script-specific shaping rules;
- disagreements about whether the character model reflects indigenous analysis or implementation convenience.

Legacy Indian solutions included ISCII and numerous font encodings that assigned Latin byte positions to Indic glyph fragments. Such font encodings could display text but were not semantically interoperable.

## 5. Tibetan

Unicode encodes Tibetan principally through base characters and combining signs rather than a separate precomposed code point for every stack.

**[CONTROVERSY]:** Proposals in the early 2000s sought hundreds of precomposed “brda rten” forms. WG2 document N2624 criticized a proposal for 962 precomposed Tibetan characters, while N2635 defended the existing compositional model using evidence from large Tibetan electronic corpora. The disagreement concerned input, collation, canonical representation and whether stacks were characters or glyph sequences—not whether Tibetan deserved encoding. [WG2 N2624](https://www.unicode.org/wg2/docs/n2624.pdf), [WG2 N2635/L2-03-322](https://www.unicode.org/L2/L2003/03322-n2635-chilton-tibetan.pdf).

**[FINDING]:** “The Tibetan encoding dispute” is not one single event. It comprises the original block design, later corrections, precomposed-stack proposals, collation issues and community implementation experience.

## 6. Chinese, Japanese and Korean

Before Unicode:

- mainland China used GB standards;
- Taiwan and Hong Kong widely used Big5 and extensions;
- Japan used JIS, Shift-JIS, EUC-JP and ISO-2022-JP;
- Korea used KS standards, EUC-KR and vendor encodings;
- vendors added characters in incompatible private regions.

Unicode/10646’s unified Han repertoire assigns one code point to characters judged to share abstract identity across these sources. A Japanese font can render a Japanese glyph style and a Chinese font a Chinese style.

Language tagging, font selection and variation sequences may be necessary where typography matters.

Hangul is encoded both as conjoining jamo and as 11,172 algorithmically related precomposed modern syllables. The relocation before Unicode 2.0 caused the “Korean mess” already noted.

## 7. Emoji

Emoji originated in Japanese carrier systems, encoded through vendor-defined Shift-JIS and private-use mappings.

**[STANDARD history]:**

- 2000: Graham Asher submitted NTT DoCoMo pictographs as L2/00-152.
- 2006: Google began internal Unicode private-use mappings.
- May–August 2007: Unicode expanded its symbols scope and formed a subcommittee.
- L2/07-257: Kat Momoi, Mark Davis and Markus Scherer prepared an early carrier-emoji proposal.
- January 2009: Google and Apple authors jointly proposed the major mapping set.
- Unicode 5.2 encoded characters associated with ARIB.
- Unicode 6.0 in 2010 added the remaining 608 characters from the 722-character Japanese carrier union that were not already encoded.

[UTS #51 history](https://www.unicode.org/reports/tr51/), [L2/07-257](https://www.unicode.org/L2/L2007/07257-emoji-wd.html), [L2/09-025](https://www.unicode.org/L2/L2009/09025-emoji.pdf).

Modern emoji employ:

- individual code points;
- variation selector-16 for emoji presentation;
- skin-tone modifiers;
- regional-indicator pairs for flags;
- zero-width-joiner sequences;
- tag sequences;
- keycap and other standardized sequences.

Therefore the “number of emoji” depends on whether one counts characters, recommended sequences, components or vendor-supported glyphs.

---

# Scripts encoded over time

A complete character-by-character chronology would reproduce the versioned database. The major stages are:

| Period/version | Major development |
|---|---|
| Unicode 1.0, 1991–92 | Core modern European, Middle Eastern, Indic and East Asian scripts; unified Han |
| Unicode 1.1, 1993 | Alignment with ISO/IEC 10646-1:1993 |
| Unicode 2.0, 1996 | Surrogates and supplementary architecture; Hangul relocation |
| Unicode 3.0, 1999 | Major expansion including Cherokee, Ethiopic, Canadian Aboriginal Syllabics, Khmer, Mongolian, Myanmar, Ogham, Runic, Sinhala, Syriac, Thaana and Yi |
| Unicode 3.1, 2001 | First supplementary-plane characters, including large CJK Extension B |
| Unicode 4.x, 2003–08 | Historic scripts, musical and mathematical collections; Shavian and many SMP scripts |
| Unicode 5.x, 2006–09 | More historic scripts, Phags-pa, N’Ko, Vai, Bamum; initial explicitly emoji-related additions |
| Unicode 6.0, 2010 | Major Japanese-carrier emoji set and further scripts |
| Unicode 7–10, 2014–17 | Numerous historic and minority scripts; expanded emoji |
| Unicode 11–14, 2018–21 | Continued historic, African and Asian script additions and emoji |
| Unicode 15–16, 2022–24 | Kawi, Nag Mundari, Tulu-Tigalari, Todhri and others |
| Unicode 17.0, 2025 | Sidetic, Tolong Siki, Beria Erfe and Tai Yo; 4,803 characters added |

The definitive chronology is Unicode Appendix C and the individual version pages. [Unicode 17 Appendix C](https://www.unicode.org/versions/Unicode17.0.0/core-spec/appendix-c/).

### Shavian, Klingon and Tengwar

- **Shavian is encoded** at U+10450–U+1047F in the SMP.
- **Klingon pIqaD was formally rejected** by the UTC in 2001 because the submitted script lacked demonstrated earnest community use and published textual evidence.
- **Tengwar is not encoded as of Unicode 17.0.** It has been proposed and roadmapped, but roadmap reservation is not character assignment.

**[CORRECTION TO THE BRIEF]:** The phrase “Tengwar and Shavian in the SMP” is true only if “in the SMP” loosely includes roadmap proposals. In the actual standard Shavian is encoded; Tengwar is not. [Klingon rejection paper L2/01-212](https://www.unicode.org/L2/L2001/01212-RejectKlingon.html), [SMP roadmap](https://www.unicode.org/roadmaps/smp/).

---

# Han unification

## 1. The design

Han characters used in Chinese, Japanese, Korean, Vietnamese and other traditions share a historical script but exhibit regional glyph forms and divergent local standards.

Unicode/10646 unifies source forms when committees judge them to represent the same abstract ideograph. It does not generally unify merely similar meanings or unrelated characters that happen to look alike.

The original work passed from Xerox, Apple and RLG databases into international work. The CJK Joint Research Group became the Ideographic Rapporteur Group, which continues to evaluate national and expert submissions.

## 2. Source Separation Rule

The source-separation rule preserves distinct code points when a primary source standard distinguishes characters, even if ordinary unification rules might otherwise combine them. This supports round-trip conversion.

This creates an apparent paradox:

- Unicode is criticized for unifying variants that users want separated.
- It is also criticized for separately encoding variants that look like duplicates.

Both outcomes follow from balancing abstract identity, glyph variation and source compatibility.

**[STANDARD]:** Unicode Chapter 18 gives concrete examples in which visually close “sword” ideographs remain separate because Japanese or Chinese source standards separated them. [Unicode 17 Chapter 18](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/).

## 3. Japanese objections

**[DISPUTED]:** Japanese criticism has included several distinguishable arguments:

1. regional glyph forms may carry cultural and typographic significance;
2. language cannot always be inferred from a bare unified code point;
3. early font selection produced visibly “Chinese” glyphs in Japanese text;
4. source standards contained distinctions that unification could threaten;
5. American and European corporate influence appeared disproportionate;
6. rare Japanese personal-name and historical forms were inadequately covered.

Defenders respond that:

- the IRG includes East Asian national bodies and experts;
- the process avoids duplicate encoding of the same character, not forcible merging of languages;
- regional glyph variation belongs partly to fonts and language metadata;
- the source-separation rule preserves source distinctions;
- thousands of additional ideographs and standardized variants have since been encoded.

Unicode Technical Note #26 presents the defense, emphasizing that Chinese, Japanese and Korean participants conducted the detailed work. Because it is an official Unicode note by a central standards editor, it is valuable technical evidence but not a neutral history of opposition. [UTN #26](https://www.unicode.org/notes/tn26/).

**[DISPUTED historical claim]:** Some popular accounts say Western ISO votes imposed Han unification against Japan. The primary record found here shows more complexity: the Japanese delegation supplied unification rules associated with Professor Miyazawa Akira, while Japanese institutions and users still raised substantial objections. “Japan supported” and “Japan opposed” are both too coarse; delegations, vendors, typographers and the public were not one actor. [Unicode Han history](https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/), [Hart memo](https://www.unicode.org/history/hartmemo.html).

---

# Design principles

## Characters, not glyphs

This principle makes interchange independent of a particular font, but the boundary is negotiated rather than metaphysical. Compatibility characters, mathematical alphabets, emoji presentation and variation selectors show that appearance can acquire encoded significance where interchange demands it.

## Plain text

Unicode defines plain text as a sequence of encoded characters without assuming a particular visual appearance. Yet rendering may depend on:

- fonts;
- shaping engines;
- language;
- bidi processing;
- normalization;
- emoji presentation;
- higher-level markup.

“Plain text” is therefore a layered technical ideal, not “text with no interpretation.”

## Logical order

Arabic, Hebrew and Indic text is generally stored in logical rather than final visual order. This improves editing and processing but requires complex rendering algorithms.

## Round-trip compatibility

Compatibility characters and source-separation decisions preserve conversions from legacy standards. They also make the repertoire less conceptually pure and necessitate normalization distinctions.

## Stability

After the disruptive Hangul relocation, Unicode adopted strong invariants:

- assigned characters are not removed;
- names are immutable except through formal aliases;
- canonical decompositions and normalization are tightly constrained;
- code points do not move;
- normalization results remain stable.

**[STANDARD]:** [Unicode stability policies](https://www.unicode.org/policies/stability_policy.html).

---

# People and institutions

## Principal people

### Joseph D. Becker

Xerox engineer; named Unicode and wrote **Unicode 88**. Advocated a fixed-width universal code and worked with Collins on unified Han.

### Lee Collins

Worked at Xerox and Apple; central architect of Han unification and the early character database. Presented the project to companies and standards committees.

### Mark Davis

Apple engineer, co-designer and business organizer; later IBM and Google. Co-founded the Consortium, created the initial Bidirectional Algorithm and became a long-serving president and technical leader. His recollections are indispensable but must be identified as participant testimony.

### Ken Whistler

Metaphor and later Sybase/SAP; editor and architect of the standard, major historian of the merger and author/editor of technical material. His accounts combine direct participation with later institutional reconstruction.

### Asmus Freytag

Early contributor, technical director and editor; worked on properties, line breaking, symbols and standardization.

### Mike Kernaghan and Bill English

Important in organizing Unicode, Inc.’s early business structure.

### Edwin Hart

SHARE representative and US standards participant who convened and facilitated the 1991 merger discussions.

### Mike Ksar and Masami Hasegawa

Important ISO/WG2 participants and editors in the 10646 process.

### Ken Thompson and Rob Pike

Bell Labs engineers responsible for UTF-8’s decisive design and its first system-wide implementation in Plan 9.

### François Yergeau

Author of RFCs 2044, 2279 and 3629 specifying UTF-8 for Internet use.

### Michel Suignard

Microsoft representative, standards editor and major contributor to mappings, symbols, emoji and security work.

### Joan Aliprand and Karen Smith-Yoshimura

Research Libraries Group participants who contributed bibliographic, East Asian and character-set expertise.

### Rick McGowan

Long-serving Unicode participant involved in proposal review, public communications and the Klingon rejection recommendation.

### Emoji contributors

Kat Momoi, Markus Scherer, Darick Tong, Yasuo Kida, Peter Edberg and others authored the formative Google/Apple carrier-emoji proposals.

### Earlier-code figures

Baudot, Murray, Hollerith, Bob Bemer and Charles E. Mackenzie belong to the longer history of character coding. Bemer was a leading ASCII advocate and public historian; Mackenzie’s *Coded Character Sets, History and Development* remains a major technical reconstruction of pre-Unicode standards.

## Institutions

- **ASA/ANSI X3 and X3L2:** US coded-character standards.
- **ECMA:** ECMA-6, ECMA-35 and related standards that fed ISO work.
- **ISO/IEC JTC 1/SC 2/WG 2:** custodian of ISO/IEC 10646.
- **IRG:** international expert group for ideographic repertoire work.
- **Unicode Consortium/UTC:** maintains Unicode properties, algorithms and repertoire in coordination with WG2.
- **Xerox and Apple:** origin sites of the Unicode initiative.
- **IBM, Microsoft, Sun, DEC and other vendors:** early corporate adopters and standards participants.
- **Bell Labs:** UTF-8 and Plan 9.
- **RLG:** source databases and bibliographic expertise.
- **IETF/IANA:** network standards and charset registration.
- **W3C and WHATWG:** Web character architecture and HTML behavior.
- **National bodies:** formally vote in ISO and submit script and repertoire requirements.

## Governance and membership

The Unicode Consortium is a California nonprofit membership corporation. Technical work is performed through committees and working groups. Organizational members at qualifying levels appoint voting delegates; individual and institutional experts can participate through proposals, public review and various membership channels.

UTC voting is therefore neither a one-company decree nor a direct vote of all users. It is a technical membership process in which corporations possessing implementation resources have historically been prominent.

**[STANDARD/procedural]:** Current procedures define quorum and weighted voting through organizational members in regular attendance and recognize working groups for CJK, emoji, CLDR and digitally disadvantaged languages. [Unicode technical committee procedures](https://www.unicode.org/consortium/tc-procedures.html).

ISO provides a second governance path through national bodies and WG2. Synchronization means repertoire decisions require extensive coordination, but organizational authority remains distinct.

---

# Culture

## 1. ASCII art, ANSI art and the demoscene

Unicode inherited ASCII’s repertoire, so traditional ASCII art remains valid Unicode text. The larger repertoire enabled:

- box-drawing and block-character art;
- Braille-pattern “pixels”;
- mathematical and script mixing;
- emoji mosaics;
- increasingly elaborate terminal interfaces.

The demoscene and bulletin-board cultures often used IBM code-page characters rather than strict ASCII. Calling all such work “ASCII art” is culturally conventional but technically imprecise.

## 2. Mojibake

*Mojibake*—Japanese 文字化け, approximately “character transformation/corruption”—occurs when bytes are decoded using the wrong encoding or when text undergoes a mismatched conversion.

Example: UTF-8 `é` is `C3 A9`. Interpreted as Windows-1252, those bytes display as `Ã©`. Re-encoding that display can compound the corruption.

Mojibake became:

- an everyday sign of failed globalization;
- a source of forensic clues about conversion paths;
- an intentional aesthetic in glitch art, memes and music;
- a visual shorthand for “computer corruption.”

**[CULTURAL reconstruction]:** Intentional mojibake is not a feature of Unicode. It is a modern reuse of encoding failure as style.

## 3. The plain-text ideal

Unicode greatly strengthens the idea that one text file can be exchanged worldwide without agreeing on a national code page. It simultaneously reveals that text is never entirely context-free:

- segmentation depends on script rules;
- collation depends on locale;
- bidi display depends on paragraph context;
- appearance depends on fonts;
- emoji meaning depends partly on vendor glyphs and culture;
- canonical equivalence means identical-looking strings may differ in code points.

“Plain text” survives, but as standardized abstract structure rather than bare self-evident bytes.

## 4. Emoji politics

Emoji transformed an obscure infrastructure consortium into a visible cultural gatekeeper.

Criticisms include:

- early repertoires reflected Japanese carrier history and US technology companies;
- gender, occupation, disability, food and family representation were uneven;
- membership fees and corporate staffing affect who can sustain participation;
- irreversible encoding makes committees conservative;
- media often attribute glyph design to Unicode although Apple, Google and other vendors draw the images.

Countervailing facts include:

- anyone can submit a proposal;
- proposals and many committee documents are public;
- selection is based on interoperability, expected use, distinctiveness and other published factors;
- encoding a character does not dictate its exact image;
- ISO national bodies also participate in repertoire standardization.

**[MODERN MEDIA FRAME]:** “The emoji committee decides which images may exist” is rhetorically effective but technically false. It decides which interoperable character identities and sequences enter the standard; vendors decide glyph artwork, and images outside Unicode remain unrestricted.

---

# Controversies and disputes

## 1. Who invented Unicode?

**Documented minimum:** Becker, Collins and Davis developed the basic architecture in 1987–88; Becker named it and wrote Unicode 88.

**Disputed emphasis:** Becker stressed the manifesto as intentional inception. Institutional histories emphasize the three-person architecture and the larger working group.

**Finding:** No responsible account should assign sole invention without explaining the different contributions.

## 2. Did Unicode defeat ISO 10646?

**Finding:** No. The failed 1991 DIS created leverage for compromise, but the result incorporated both architectures. ISO supplied international legitimacy, national-body participation, a larger codespace and aspects of naming and order; Unicode supplied an implementable repertoire and processing model backed by vendors.

## 3. Was 16-bit Unicode a blunder?

**Bad consequence:** UTF-16 surrogate pairs complicate indexing, regular expressions and APIs.

**Good consequence:** The original fixed-width model helped obtain early implementation commitments, while surrogates preserved existing 16-bit data and APIs.

**Evidence:** Early documents explicitly favored 16 bits; the popular taunting slogan is not authenticated.

## 4. Han unification

The controversy is substantive rather than a simple misunderstanding. Abstract-character unification reduced duplication and made the original repertoire feasible. It also delegated region-specific shape to fonts and language context that software often failed to supply.

A Japanese user shown a mainland-Chinese glyph is experiencing a real implementation defect even if the abstract encoding decision is defensible.

The official narrative’s emphasis on national participation rebuts claims of wholly unilateral Western imposition but does not prove unanimous East Asian acceptance.

## 5. Tibetan and other encoding models

Tibetan stack proposals expose the tension between:

- atomic user-perceived units;
- compositional linguistic analysis;
- efficient input and collation;
- rendering-system capabilities;
- stability of deployed data.

Similar arguments recur in Indic, Myanmar, Mongolian, Egyptian hieroglyphic and musical notation work. “Character versus glyph” is a policy principle applied through negotiation, not an algorithm that answers every proposal.

## 6. Emoji and corporate power

Corporate members supply engineering resources and control major platforms; this gives them practical influence. Yet character additions must remain interoperable and synchronized with ISO, proposals may originate outside corporations, and Unicode does not control every vendor’s glyph.

Both “private companies control language” and “the Consortium is merely neutral plumbing” omit part of the institutional reality.

## 7. BOM disputes

A BOM can make UTF-16/32 byte order self-describing. In UTF-8 it can aid signature-based detection but may break software expecting immediate syntax. The conflict is between robustness in one ecosystem and composability in another.

## 8. Overlong UTF-8 and invalid sequences

Old UTF-8 descriptions permitted multiple representations through overlong forms or allowed values beyond the modern codespace. Attackers could exploit inconsistent validation—for example, one layer might treat `C0 80` as NUL while another failed to recognize it.

RFC 3629:

- limits UTF-8 to four bytes;
- forbids overlong sequences;
- forbids surrogate encodings;
- caps values at U+10FFFF;
- requires protection against invalid decoding.

The RFC records a 2001 Web-server worm exploiting malformed UTF-8, making this more than a hypothetical concern. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html).

## 9. Homoglyph and confusable attacks

Unicode contains distinct characters that look alike:

```text
Latin a      U+0061
Cyrillic а   U+0430
```

An attacker can construct a visually deceptive identifier or domain name. Combining marks, bidi controls, invisible characters and normalization differences create further attack surfaces.

**[STANDARD]:** UTS #39 defines restriction levels, confusable mappings and identifier “skeletons.” It warns that confusability can never be solved perfectly because arbitrary fonts can map any code point to any glyph. [UTS #39](https://www.unicode.org/reports/tr39/).

UTR #36 introduced much of the security analysis but was stabilized in 2014; Unicode now warns that parts are superseded by UTS #39, UTS #55 and UAX #31. [UTR #36 status](https://www.unicode.org/reports/tr36/).

Unicode did not invent visual spoofing; ASCII `paypa1` already resembles `paypal`. Unicode enlarges the relevant repertoire and supplies mechanisms for mitigation.

## 10. Bidirectional attacks

Bidi controls can make source code display in an order different from its logical token order. This became widely publicized as the “Trojan Source” class of attacks.

The controls have legitimate use in mixed-direction text. The security failure occurs when programming tools, review interfaces and identifier policies expose misleading visual structure. Mitigation belongs partly in language specifications and editors, not in deleting bidi support needed by real languages.

## 11. Stability versus correction

Once a character is encoded, its code point and name normally cannot be changed. Errors are handled through annotations, aliases, properties or additional characters.

Benefits:

- old text remains decodable;
- databases and identifiers retain meaning;
- normalization remains stable.

Costs:

- mistakes become permanent;
- misleading names survive;
- duplicate and compatibility characters accumulate;
- users may wait for corrective additions rather than clean replacement.

## 12. Vendor codes and private use

Private-use areas solve coordination within a closed community but have no universal semantics. The same private-use code point can mean a corporate logo, Klingon letter, icon or nothing at all.

Emoji’s migration from carrier-specific private-use mappings into standardized code points demonstrates both the usefulness and ultimate limit of private agreements.

---

# Adoption, displacement and what “won”

Unicode did not replace every encoding at once. It won at several layers:

1. **Abstract repertoire:** most modern software identifies characters by Unicode code point.
2. **Internet interchange:** UTF-8 became the near-universal encoding.
3. **Platform internals:** UTF-16 remained important in Windows, Java and JavaScript; UTF-8 and adaptive representations gained ground elsewhere.
4. **Standards:** ISO 10646 and Unicode synchronized instead of competing.
5. **Legacy conversion:** old code pages survived as mappings and archival obligations.

The result is not an encoding monoculture in memory, but a common character identity with a dominant interchange form.

---

# Open questions

1. **Early archives:** How much unpublished Xerox and Apple correspondence survives that could distinguish contemporaneous design decisions from later institutional narrative?

2. **Unicode 88 drafting:** Becker said he drafted the proposal in February 1988 and finalized it in August. Surviving intermediate drafts could clarify how Collins’s, Davis’s, Fenwick’s and Opstad’s contributions entered the text.

3. **The placemat:** Pike’s recollection is credible participant evidence, but no independent contemporary artifact or surviving placemat has been identified here.

4. **Japanese positions:** More Japanese-language national-body minutes, trade-press reports and user testimony are needed to replace broad claims that “Japan” either accepted or rejected Han unification.

5. **Corporate influence:** Membership lists and formal votes are only part of influence. A complete institutional history would compare paid engineering time, proposal authorship, national delegation composition and implementation control.

6. **Script coverage:** Counting encoded scripts does not measure practical support. Fonts, keyboards, shaping, spellchecking, search and digital corpora remain uneven, especially for minority and historic writing systems.

7. **Character counts:** Counts depend on whether controls, private-use positions, format characters, sequences or named character aliases are included. Any reported number needs a declared counting rule.

8. **Emoji representation:** It remains difficult to balance cultural inclusion, long-term expected use, finite review capacity and a stability rule that makes additions effectively permanent.

9. **Grapheme-oriented APIs:** Much mainstream software still exposes bytes or UTF-16 units where users expect characters. Whether future APIs can make grapheme clusters convenient without hiding necessary structure remains an engineering question.

10. **Normalization and identifiers:** Global interoperability favors normalization and broad repertoire; secure identifiers often require restricted profiles. No single policy is appropriate to prose, filenames, programming identifiers and domain names alike.

11. **Tengwar:** It remains proposed/roadmapped but unencoded. Future acceptance would depend on evidence of textual use, a stable character model and committee approval; roadmap presence is not a promise.

12. **Version 18 and ISO revision:** ISO/IEC 10646:2020 is marked for revision, while Unicode continues annual releases. Exact future synchronization will be determined by the two organizations’ ballots and publication schedules.

---

# Sources

The following are the principal editions and URLs consulted. ISO’s catalogue page was used where the complete standard text was not freely exposed through ordinary Web access.

## Unicode standards, databases and policies

- The Unicode Consortium, *The Unicode Standard, Version 17.0.0*, 2025:  
  https://www.unicode.org/versions/Unicode17.0.0/
- Complete Unicode 17.0 Core Specification PDF:  
  https://www.unicode.org/versions/Unicode17.0.0/UnicodeStandard-17.0.pdf
- Unicode 17.0 Core Specification HTML:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/
- Chapter 1, “Introduction”:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-1/
- Chapter 5, “Implementation Guidelines”:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-5/
- Chapter 18, “East Asia”:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/
- Chapter 23, “Special Areas and Format Characters”:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-23/
- Appendix C, “Relationship to ISO/IEC 10646”:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/appendix-c/
- Unicode 17.0 character counts:  
  https://www.unicode.org/versions/stats/charcountv17_0.html
- Unicode Character Database:  
  https://www.unicode.org/ucd/
- Code charts:  
  https://www.unicode.org/charts/
- Character encoding stability policy:  
  https://www.unicode.org/policies/stability_policy.html
- UAX #9, *Unicode Bidirectional Algorithm*:  
  https://www.unicode.org/reports/tr9/
- UAX #15, *Unicode Normalization Forms*:  
  https://www.unicode.org/reports/tr15/
- UTR #15 Revision 18, Unicode 3.0-era normalization specification, 11 November 1999:  
  https://www.unicode.org/standard/reports/tr15/tr15-18.html
- UAX #29, *Unicode Text Segmentation*:  
  https://www.unicode.org/reports/tr29/
- UAX #31, *Unicode Identifiers and Syntax*:  
  https://www.unicode.org/reports/tr31/
- UTR #36, *Unicode Security Considerations*, stabilized status page:  
  https://www.unicode.org/reports/tr36/
- UTS #39, *Unicode Security Mechanisms*:  
  https://www.unicode.org/reports/tr39/
- UTS #51, *Unicode Emoji*:  
  https://www.unicode.org/reports/tr51/
- Unicode Collation Algorithm, UTS #10:  
  https://www.unicode.org/reports/tr10/
- Unicode Technical Note #26, *On the Encoding of Latin, Greek, Cyrillic, and Han*:  
  https://www.unicode.org/notes/tn26/
- Unicode FAQ, Unicode and ISO 10646:  
  https://www.unicode.org/faq/unicode_iso.html
- Unicode security FAQ:  
  https://www.unicode.org/faq/security.html
- Unicode normalization FAQ:  
  https://www.unicode.org/faq/normalization.html
- Unicode Technical Committee procedures:  
  https://www.unicode.org/consortium/tc-procedures.html
- Unicode membership information:  
  https://www.unicode.org/consortium/membership.html
- Unicode SMP roadmap:  
  https://www.unicode.org/roadmaps/smp/

## Historical Unicode sources

- Joseph D. Becker, *Unicode 88*, 29 August 1988:  
  https://www.unicode.org/history/Unicode88.pdf
- Unicode History Corner:  
  https://www.unicode.org/history/
- *Early Years of Unicode*:  
  https://www.unicode.org/history/earlyyears.html
- Unicode historical summary:  
  https://www.unicode.org/history/summary.html
- Unicode Version 1 chronology:  
  https://www.unicode.org/history/versionone.html
- Unicode release and publication dates:  
  https://www.unicode.org/history/publicationdates.html
- Unicode 1.0 archive:  
  https://www.unicode.org/versions/Unicode1.0.0/
- Unicode 1.1 archive and merger account:  
  https://www.unicode.org/versions/Unicode1.1.0/
- Unicode mailing-list archive, “Answers about Unicode history,” February 2002:  
  https://www.unicode.org/mail-arch/unicode-ml/y2002-m02/0110.html
- Edwin Hart, “10646-Unicode Merger,” document 10646M/91-01, 30 May 1991:  
  https://www.unicode.org/history/hartmemo.html
- Laura Wideburg, “An Interview with Ed Hart,” 16 October 1995:  
  https://www.unicode.org/history/hartinterview.html
- Historical X3L2 document register, 1991:  
  https://www.unicode.org/L2/OldDocRegisters/X3L2-docreg-1991.pdf
- Unicode 1.0 merger chapter:  
  https://www.unicode.org/versions/Unicode1.0.0/V2ch01.pdf
- Han unification history, Appendix E of Unicode 16.0:  
  https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/

## ISO and WG2

- ISO, *ISO/IEC 10646:2020, Information technology—Universal coded character set (UCS)*, Edition 6:  
  https://www.iso.org/standard/76835.html
- ISO/IEC 10646:2020 Amendment 1:2023:  
  https://www.iso.org/standard/83362.html
- ISO/IEC JTC 1/SC 2/WG 2 document repository:  
  https://www.unicode.org/wg2/docs/
- WG2 N2624, comments on proposed Tibetan BrdaRten encoding, 24 September 2003:  
  https://www.unicode.org/wg2/docs/n2624.pdf
- WG2 N2635/L2/03-322, Tibetan encoding-model response, 2003:  
  https://www.unicode.org/L2/L2003/03322-n2635-chilton-tibetan.pdf
- Historical merger document 10646M29:  
  https://www.unicode.org/L2/Historical/EdHart-X3L2-Arch-2004-02-12/merger/10646M29-doc.pdf

## UTF and Internet standards

- Rob Pike, “UTF-8 history,” participant recollection dated 30 April 2003:  
  https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt
- RFC 20, *ASCII Format for Network Interchange*, October 1969:  
  https://www.rfc-editor.org/rfc/rfc20.html
- RFC 1341, *MIME*, June 1992:  
  https://www.rfc-editor.org/rfc/rfc1341.html
- RFC 1345, *Character Mnemonics and Character Sets*, June 1992:  
  https://www.rfc-editor.org/rfc/rfc1345.html
- RFC 2044, *UTF-8, a Transformation Format of Unicode and ISO 10646*, October 1996:  
  https://www.rfc-editor.org/rfc/rfc2044.html
- RFC 2277, *IETF Policy on Character Sets and Languages*, January 1998:  
  https://www.rfc-editor.org/rfc/rfc2277.html
- RFC 2279, *UTF-8, a Transformation Format of ISO 10646*, January 1998:  
  https://www.rfc-editor.org/rfc/rfc2279.html
- RFC 2781, *UTF-16, an Encoding of ISO 10646*, February 2000:  
  https://www.rfc-editor.org/rfc/rfc2781.html
- RFC 3629, *UTF-8, a Transformation Format of ISO 10646*, November 2003:  
  https://www.rfc-editor.org/rfc/rfc3629.html
- RFC 5198, *Unicode Format for Network Interchange*, March 2008:  
  https://www.rfc-editor.org/rfc/rfc5198.html
- IANA Character Sets registry:  
  https://www.iana.org/assignments/character-sets/character-sets.xhtml

## Emoji and constructed-script documents

- L2/07-257, Momoi, Davis and Scherer, *Working Draft Proposal for Encoding Emoji Symbols*, 3 August 2007:  
  https://www.unicode.org/L2/L2007/07257-emoji-wd.html
- L2/09-025, Scherer, Davis, Momoi, Tong, Kida and Edberg, *Proposal for Encoding Emoji Symbols*, 30 January 2009:  
  https://www.unicode.org/L2/L2009/09025-emoji.pdf
- L2/01-212, Rick McGowan, *Proposal to Formally Reject Klingon for Encoding*, 18 May 2001:  
  https://www.unicode.org/L2/L2001/01212-RejectKlingon.html
- Unicode emoji charts:  
  https://www.unicode.org/emoji/charts/

## Earlier character-code histories and standards

- Charles E. Mackenzie, *Coded Character Sets, History and Development*, Addison-Wesley, 1980, Internet Archive record:  
  https://archive.org/details/codedcharacterse0000mack
- ECMA-6, *7-bit Coded Character Set*:  
  https://ecma-international.org/publications-and-standards/standards/ecma-6/
- ECMA-35, *Character Code Structure and Extension Techniques*:  
  https://ecma-international.org/publications-and-standards/standards/ecma-35/
- ISO catalogue search for ISO/IEC 646:  
  https://www.iso.org/search.html?q=ISO%2FIEC%20646
- ISO catalogue search for ISO/IEC 2022:  
  https://www.iso.org/search.html?q=ISO%2FIEC%202022
- ISO catalogue search for ISO/IEC 8859:  
  https://www.iso.org/search.html?q=ISO%2FIEC%208859
- IBM documentation portal, character data representation and code pages:  
  https://www.ibm.com/docs/
- Computer History Museum oral histories collection:  
  https://www.computerhistory.org/collections/oralhistories/

## Adoption and Web measurement

- W3Techs, UTF-8 usage broken down by ranking, measured 11 September 2026:  
  https://w3techs.com/technologies/breakdown/en-utf8/ranking
- W3C, *Character Model for the World Wide Web: Fundamentals*:  
  https://www.w3.org/TR/charmod/
- WHATWG HTML Living Standard, character encodings:  
  https://html.spec.whatwg.org/multipage/parsing.html#character-encodings
- Encoding Standard:  
  https://encoding.spec.whatwg.org/
