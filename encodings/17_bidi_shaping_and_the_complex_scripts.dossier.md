# Bidirectional text and complex-script shaping: Hebrew, Arabic, the Indic scripts and the encoding of writing that is not left-to-right Latin: Research Dossier

> **Standard:** Unicode Standard 17.0.0; ISO/IEC 10646:2020 with amendments; Unicode Standard Annex #9, “Unicode Bidirectional Algorithm,” Revision 51  
> **Years:** Unicode origins, 1987–1988; Unicode 1.0, 1991; ISO/IEC 10646-1, 1993; UAX #9 first published separately, 1998–1999; current Unicode release, 9 September 2025  
> **Bit width:** 21-bit code space, U+0000–U+10FFFF. Serialized as UTF-8 (one to four 8-bit code units), UTF-16 (one or two 16-bit code units), or UTF-32 (one 32-bit code unit).  
> **Repertoire:** 159,801 assigned graphic and format characters in Unicode 17.0, covering 172 scripts; 159,629 are graphic characters and 172 are format characters.  
> **Current status:** Active, maintained, globally deployed. Unicode 17.0 supersedes earlier Unicode versions. UAX #9 is normative for conforming rendering of supported bidirectional text in the absence of an overriding higher-level protocol.  
> **Subject qualification:** This is not one character code comparable to ASCII. It is a layered system: Unicode/ISO 10646 encode abstract characters; UTFs encode code points as code units and bytes; UAX #9 determines bidirectional display order; script-specific rules and shaping engines convert characters into positioned glyphs; fonts provide those glyphs.

## Evidentiary labels

Every historical or technical assertion below is marked according to its evidentiary basis:

- **[STANDARD]** Normative or informative text in a published standard, RFC, registered character-set specification, or official code chart.
- **[DOCUMENT]** Contemporary proposal, committee paper, minutes, manual, or institutional record.
- **[RECOLLECTION]** A named participant’s retrospective account.
- **[SCHOLARLY]** Historical or technical reconstruction based on published evidence.
- **[DISPUTED]** A claim or interpretation on which contemporary participants or later specialists disagree.
- **[FOLKLORE]** A frequently repeated story for which the available evidence is anecdotal, derivative, or incomplete.
- **[MODERN]** A later practice, cultural interpretation, software convention, or newly coined characterization.
- **[FINDING]** A conclusion from comparing the cited evidence, including an absence of adequate evidence.

---

## Basic identification

### What is being encoded?

**[STANDARD]** Unicode assigns integers called code points to abstract characters. It does not ordinarily encode particular glyph shapes. A font contains glyphs; layout software selects and positions them. One character can yield different glyphs, several characters can form one ligature glyph, and one character can yield several glyph components. The current standard illustrates this with Latin letters, Serbian and Russian forms of Cyrillic *pe*, contextual Arabic *heh*, and the optional Latin `fi` ligature. [Unicode 17.0, Chapter 2](https://www.unicode.org/versions/Unicode17.0.0/UnicodeStandard-17.0.pdf)

**[STANDARD]** The scalar-value range is:

- U+0000–U+D7FF
- U+E000–U+10FFFF

U+D800–U+DFFF are surrogate code points and are not Unicode scalar values. They are reserved as UTF-16 code units.

**[STANDARD]** Unicode 17.0 contains 159,801 assigned graphic and format characters. Its total assigned count rises to 297,334 when controls and private-use code points are included. It designates 299,448 positions when surrogates and noncharacters are counted. These totals should not be conflated: “encoded characters” in the release announcement means graphic plus format characters. [Unicode 17.0 character counts](https://www.unicode.org/versions/stats/charcountv17_0.html)

### The standards family

**[STANDARD]**

| Layer | Principal standard | Function |
|---|---|---|
| Character repertoire | Unicode 17.0; ISO/IEC 10646 | Assigns characters to code points |
| Byte representation | UTF-8, UTF-16, UTF-32; RFC 3629 for Internet UTF-8 | Maps scalar values to code units and bytes |
| Bidirectional ordering | UAX #9 | Resolves logical text into display levels and visual order |
| Normalization | UAX #15 | Defines NFC, NFD, NFKC, and NFKD equivalence forms |
| Segmentation | UAX #29; dictionary or language-specific processing where necessary | Grapheme, word, and sentence boundaries |
| Line breaking | UAX #14 plus tailoring | Line-break opportunities |
| Vertical orientation | UAX #50 | Default upright/rotated behavior in vertical layout |
| Collation | UTS #10 | Language-tailorable ordering; not code-point order |
| Security | UTS #39, UTS #55, UAX #31 | Confusables, identifiers, source-code handling |
| Font shaping | OpenType, Apple Advanced Typography, Graphite; engines such as Uniscribe, DirectWrite, CoreText and HarfBuzz | Maps character sequences to positioned glyphs |

**[FINDING]** “Unicode encodes characters, not glyphs” is a necessary architectural rule, but not a promise that encoded text alone determines typography. Arabic joining, Indic conjunct formation, mark placement, language-sensitive forms, CJK regional shapes, Mongolian variants, emoji presentation, and vertical punctuation demonstrate that fonts, language metadata, layout standards, and shaping engines are part of interoperable text behavior.

---

## The code in detail

### Code-space structure

**[STANDARD]** Unicode’s code space comprises 17 planes of 65,536 code points:

| Plane | Range | Typical contents |
|---|---:|---|
| 0, Basic Multilingual Plane | U+0000–U+FFFF | Most modern scripts, punctuation, symbols, compatibility blocks |
| 1, Supplementary Multilingual Plane | U+10000–U+1FFFF | Historic scripts, music, emoji and symbols |
| 2 and 3, Supplementary Ideographic Planes | U+20000–U+3FFFF | CJK unified ideographs and extensions |
| 4–13 | U+40000–U+DFFFF | Reserved |
| 14, Supplementary Special-purpose Plane | U+E0000–U+EFFFF | Tags, variation selectors, reserved space |
| 15–16, private-use planes | U+F0000–U+10FFFF | Private agreements |

The BMP also contains a private-use area at U+E000–U+F8FF. U+FDD0–U+FDEF and the final two code points of every plane are noncharacters.

### UTF-8 structure

**[STANDARD]** UTF-8 is stateless and byte-oriented:

| Scalar range | Byte pattern |
|---|---|
| U+0000–U+007F | `0xxxxxxx` |
| U+0080–U+07FF | `110xxxxx 10xxxxxx` |
| U+0800–U+FFFF, excluding surrogates | `1110xxxx 10xxxxxx 10xxxxxx` |
| U+10000–U+10FFFF | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

Bytes `00`–`7F` retain ASCII meanings. Bytes `80`–`BF` are continuation bytes. `C2`–`DF` begin valid two-byte sequences; `E0`–`EF` begin three-byte sequences subject to range restrictions; `F0`–`F4` begin four-byte sequences subject to restrictions. `C0`, `C1`, and `F5`–`FF` cannot occur in well-formed UTF-8.

**[STANDARD]** UTF-8 has no shift state and no byte-order issue. A decoder that starts in the middle of a stream can skip continuation bytes until it reaches an ASCII byte or legal leading byte. Damage is therefore normally localized, although the consuming protocol determines replacement and recovery behavior.

**[STANDARD]** Shortest-form encoding is mandatory. Surrogates, values above U+10FFFF, truncated sequences, isolated continuation bytes, and overlong encodings are ill-formed. RFC 3629 restricted the Internet form to four bytes and U+10FFFF. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html)

### UTF-16 and UTF-32

**[STANDARD]** UTF-16 represents BMP scalar values with one 16-bit code unit. A supplementary scalar is represented by a high surrogate `D800`–`DBFF` followed by a low surrogate `DC00`–`DFFF`. An isolated surrogate is ill-formed.

**[STANDARD]** UTF-32 uses one 32-bit code unit per scalar value. Its fixed code-unit width does not make one code unit equal to one user-perceived character: combining sequences, emoji ZWJ sequences, Indic syllables, and decomposed accents may contain several code points.

**[STANDARD]** UTF-16 and UTF-32 have big- and little-endian serialization schemes. U+FEFF at the beginning can act as a byte-order mark in unlabelled data:

| Initial bytes | Interpretation |
|---|---|
| `FE FF` | UTF-16BE BOM |
| `FF FE` | UTF-16LE BOM |
| `00 00 FE FF` | UTF-32BE BOM |
| `FF FE 00 00` | UTF-32LE BOM |
| `EF BB BF` | UTF-8 signature, not a byte-order indicator |

The Unicode FAQ advises against inserting a UTF-8 BOM into every string and notes that protocols may require, permit, or forbid it. RFC 5198 forbids an initial BOM in Net-Unicode. [Unicode BOM FAQ](https://unicode.org/faq/utf_bom.html), [RFC 5198](https://www.rfc-editor.org/rfc/rfc5198.html)

### Controls, space, newline, deletion and case

**[STANDARD]**

- U+0020 is SPACE and UTF-8 byte `20`.
- U+007F is DELETE, inherited through Unicode’s ASCII-compatible first 128 positions.
- U+000A is LINE FEED and U+000D is CARRIAGE RETURN.
- Unicode also encodes U+0085 NEXT LINE, U+2028 LINE SEPARATOR and U+2029 PARAGRAPH SEPARATOR.
- RFC 5198 requires `CR LF`—bytes `0D 0A`—when its Net-Unicode profile has a line concept; it prohibits NEL, LINE SEPARATOR and PARAGRAPH SEPARATOR as network line endings.
- U+0000 is NUL. RFC 5198 warns that it remains hostile to software using zero as a string terminator.
- Unicode contains inherited C0 and C1 controls but does not itself make every historical terminal-control interpretation appropriate for plain text.

**[STANDARD]** Case is a character property and mapping problem, not a bit flag. Hebrew and Arabic have no uppercase/lowercase distinction. Most Indic scripts likewise lack Latin-style case. Unicode supplies locale-independent default case data and language-sensitive or context-sensitive rules for scripts that have case. Code-point order is not linguistic collation order.

### Collation

**[STANDARD]** Unicode code-point order is a stable identifier order, not a universal alphabetic order. UTS #10 supplies the Unicode Collation Algorithm and tailoring mechanisms. Hebrew collation must account for points and final forms according to the chosen tailoring; Arabic ordering varies across languages and traditions; Indic dictionaries may treat consonant clusters and signs differently. Sorting UTF-8 byte strings happens to reproduce scalar order for well-formed strings, but that order is not normally user-facing dictionary order.

---

## Worked examples, byte by byte

### Hebrew: `שלום` — *shalom*, “peace/hello”

**[STANDARD]** Store Hebrew in logical reading order, not screen-column order:

| Logical position | Character | Code point | UTF-8 |
|---:|---|---:|---|
| 1 | ש SHIN | U+05E9 | `D7 A9` |
| 2 | ל LAMED | U+05DC | `D7 9C` |
| 3 | ו VAV | U+05D5 | `D7 95` |
| 4 | ם FINAL MEM | U+05DD | `D7 9D` |

Complete UTF-8:

```text
D7 A9 D7 9C D7 95 D7 9D
```

UTF-16BE:

```text
05 E9 05 DC 05 D5 05 DD
```

ISO-8859-8 logical character values:

```text
F9 EC E5 ED
```

**[STANDARD]** The Unicode backing store begins with SHIN even though the rendered word extends right-to-left. The old MIME default for `charset=ISO-8859-8`, however, was explicitly *visual*: RFC 1555 said Hebrew should be transmitted left-to-right in display order. That convention made editing, searching, and reflow difficult because line layout leaked into stored text. [RFC 1555](https://www.rfc-editor.org/rfc/rfc1555.html)

### Arabic: `سلام` — *salām*, “peace”

| Logical position | Character | Code point | UTF-8 |
|---:|---|---:|---|
| 1 | س SEEN | U+0633 | `D8 B3` |
| 2 | ل LAM | U+0644 | `D9 84` |
| 3 | ا ALEF | U+0627 | `D8 A7` |
| 4 | م MEEM | U+0645 | `D9 85` |

Complete UTF-8:

```text
D8 B3 D9 84 D8 A7 D9 85
```

UTF-16BE:

```text
06 33 06 44 06 27 06 45
```

ISO-8859-6:

```text
D3 E4 C7 E5
```

**[STANDARD]** Those four Unicode characters do not specify four isolated letter glyphs. A shaping engine determines joining forms. LAM plus ALEF can be displayed as a lam-alef ligature, but ordinary interchange should still contain U+0644 U+0627, not a presentation-form code point. The Unicode Arabic FAQ and Chapter 9 describe presentation forms as compatibility characters retained for older standards and implementations. [Arabic FAQ](https://www.unicode.org/faq/arabic.html)

### Devanagari: `हिन्दी` — *hindī*, “Hindi”

| Logical position | Character | Code point | UTF-8 |
|---:|---|---:|---|
| 1 | ह HA | U+0939 | `E0 A4 B9` |
| 2 | ि VOWEL SIGN I | U+093F | `E0 A4 BF` |
| 3 | न NA | U+0928 | `E0 A4 A8` |
| 4 | ् VIRAMA | U+094D | `E0 A5 8D` |
| 5 | द DA | U+0926 | `E0 A4 A6` |
| 6 | ी VOWEL SIGN II | U+0940 | `E0 A5 80` |

Complete UTF-8:

```text
E0 A4 B9 E0 A4 BF E0 A4 A8 E0 A5 8D E0 A4 A6 E0 A5 80
```

UTF-16BE:

```text
09 39 09 3F 09 28 09 4D 09 26 09 40
```

**[STANDARD]** VOWEL SIGN I follows HA in storage but is drawn to the left of the appropriate consonant cluster. NA + VIRAMA + DA may be rendered with conjunct or half-form behavior. Unicode therefore preserves phonetic/logical order while the shaper computes visual glyph order. [Unicode 17.0, Chapter 12](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-12/)

### A mixed-direction example

Logical string:

```text
Invoice שלום 123
```

Code-point sequence:

```text
0049 006E 0076 006F 0069 0063 0065 0020
05E9 05DC 05D5 05DD 0020 0031 0032 0033
```

UTF-8:

```text
49 6E 76 6F 69 63 65 20
D7 A9 D7 9C D7 95 D7 9D 20 31 32 33
```

**[STANDARD]** Latin letters are strong L characters; Hebrew letters are strong R; ASCII digits are EN, a weak type; spaces are neutral. UAX #9 derives embedding levels, resolves weak and neutral characters, treats paired brackets under rule N0, and reverses runs by level. Digits remain internally `1 2 3`, although the position of the numeric run relative to surrounding RTL text depends on context.

To make an inserted Hebrew field unable to affect adjacent text, plain text can use:

```text
Invoice ⟨RLI⟩שלום⟨PDI⟩ 123
```

with:

```text
RLI U+2067 = E2 81 A7
PDI U+2069 = E2 81 A9
```

In HTML, structural markup is preferred:

```html
Invoice <bdi dir="rtl">שלום</bdi> 123
```

---

## Bidirectional ordering in detail

### Logical versus visual order

**[STANDARD]** Unicode stores text in logical order: generally the order in which it is read or typed. UAX #9 maps that sequence onto resolved directional levels. It does not reverse the stored string, change character identity, perform Arabic shaping, break lines, or choose a font.

**[STANDARD]** Its principal bidi classes include:

| Kind | Classes | Examples |
|---|---|---|
| Strong | L, R, AL | Latin/Indic; Hebrew; Arabic/Syriac/Thaana |
| Weak | EN, AN, ES, ET, CS, NSM, BN | European digits, Arabic-Indic digits, separators, marks |
| Neutral | B, S, WS, ON | Paragraph separator, tab, spaces, punctuation |
| Explicit embeddings/overrides | LRE, RLE, LRO, RLO, PDF | Older directional controls |
| Isolates | LRI, RLI, FSI, PDI | Bounded inserted-direction fields |

**[STANDARD]** The broad algorithmic phases are:

1. Determine paragraph direction from the first strong character unless supplied by a higher-level protocol.
2. Process explicit embeddings, overrides and isolates.
3. Form isolating run sequences.
4. Resolve weak types, including digits and separators.
5. Resolve paired brackets and neutral characters.
6. Assign implicit levels.
7. Reset appropriate whitespace at line boundaries.
8. Reorder runs according to their resolved levels.
9. Mirror eligible glyphs at odd levels.

### Brackets and mirroring

**[STANDARD]** U+0028 is always LEFT PARENTHESIS as a character. At an odd resolved level, a renderer normally uses the mirrored `)` glyph. Unicode therefore distinguishes semantic identity from visual shape. UAX #9 uses normative `Bidi_Paired_Bracket` and `Bidi_Paired_Bracket_Type` data to recognize paired punctuation and resolve a pair together.

**[FINDING]** Calling this “reversing parentheses” is imprecise. The stored opening and closing characters do not exchange code points; glyph mirroring and run reordering produce the visual result.

### Numbers

**[STANDARD]** European digits have bidi class EN; Arabic-Indic digits generally have class AN. Both kinds are displayed internally left-to-right. Their surrounding placement is resolved from strong types and separators. This is why mixed Arabic, Hebrew, telephone numbers, dates, minus signs and currency symbols can behave unexpectedly even when every character is correctly encoded.

### Explicit controls and isolates

**[STANDARD]**

| Character | Code point | Role |
|---|---:|---|
| LRM | U+200E | Strong L directional mark |
| RLM | U+200F | Strong R directional mark |
| ALM | U+061C | Arabic-letter directional mark |
| LRE/RLE | U+202A/U+202B | Begin embedding |
| PDF | U+202C | End embedding or override |
| LRO/RLO | U+202D/U+202E | Override character direction |
| LRI/RLI | U+2066/U+2067 | Begin isolated L/R field |
| FSI | U+2068 | Isolate with first-strong direction |
| PDI | U+2069 | End isolate |

**[STANDARD]** Unicode 6.3, released in 2013, introduced isolate controls and revised paired-bracket handling. The Consortium described this as the most substantial change in that release because embeddings permitted inserted text to influence surrounding weak and neutral characters. [Unicode’s 2013 test announcement](https://blog.unicode.org/2013/06/testing-unicode-bidirectional-algorithm.html)

**[STANDARD]** W3C guidance prefers markup where structure exists and isolates for arbitrary inserted text. Embeddings are retained for compatibility but can create “spillover.” [`dir`, `<bdi>`, and Unicode controls](https://www.w3.org/International/questions/qa-bidi-unicode-controls.en.html)

### Error and synchronization behavior

**[STANDARD]** UAX #9 paragraph state resets at paragraph boundaries. Unmatched isolate initiators and unmatched PDI characters are handled by defined rules; implementations are not supposed to keep an uncontrolled global shift state across an entire file.

**[STANDARD]** Embedding depth and bracket stacks are bounded. Current UAX #9’s paired-bracket algorithm specifies a stack of exactly 63 entries. This prevents unbounded resource consumption.

**[FINDING]** UTF-8 byte recovery and bidi recovery are separate. UTF-8 can resynchronize at a leading byte, but deleting an invisible RLI, PDI, override, bracket or strong character can alter display ordering for a larger portion of the paragraph. A byte-level decoder can therefore recover syntactically while the displayed paragraph remains semantically misleading.

---

## Arabic shaping

### Nominal characters and contextual forms

**[STANDARD]** Arabic is written right-to-left, but joining and bidi are independent. Joining examines neighboring characters in logical order. A typical dual-joining letter may use isolated, initial, medial or final glyphs; right-joining letters such as ALEF do not connect on their left.

**[STANDARD]** Unicode assigns joining properties in `ArabicShaping.txt`. A minimum renderer chooses positional glyphs; sophisticated typography may additionally apply required ligatures, discretionary ligatures, mark positioning, cursive attachment, language-specific forms and calligraphic elongation. [Unicode 17.0, Chapter 9](https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-9/)

### Lam-alef

**[STANDARD]** The Arabic sequence LAM U+0644 followed by an ALEF-family character is commonly displayed with a lam-alef ligature. The ligature does not justify replacing the input sequence with U+FEFB or another presentation form. Compatibility decomposition maps such legacy forms toward their underlying letters.

### Join controls

**[STANDARD]**

- U+200C ZERO WIDTH NON-JOINER suppresses joining where joining would otherwise occur.
- U+200D ZERO WIDTH JOINER requests cursive connection or a joining-form effect where meaningful.
- These controls affect the shaping adjacency found in the original stored order, even though bidi reordering changes display positions.

They are semantically consequential format characters, not merely zero-width decoration.

### Arabic presentation forms

**[STANDARD]** Arabic Presentation Forms-A and -B contain contextual glyph forms, ligatures and spacing/tatweel forms preserved for round-trip compatibility with legacy character sets and implementations. The standard explicitly discourages their use for ordinary text. [Unicode presentation-forms FAQ](https://www.unicode.org/faq/ligature_digraph.html)

**[SCHOLARLY]** Presentation-form encoding reflects an earlier terminal and printer architecture in which the data stream sometimes carried a preselected display glyph because the output device could not infer context. Unicode inherited those forms to avoid destructive conversion of existing data, while adopting nominal-letter encoding as its normal model.

### Early Arabic codes

**[STANDARD]** ASMO 449, registered as ISO-IR 89 and standardized as ISO 9036:1987, is a seven-bit Arabic interchange code derived from ISO 646 and the Arab Standardization and Metrology Organization’s specification. ISO describes 120 mandatory characters and ISO 2022 extension controls. [ISO 9036 catalogue](https://www.iso.org/standard/16597.html)

**[DOCUMENT]** In ASMO 449, Latin letter positions were largely reassigned to nominal Arabic letters; it was not a bilingual code. It required an Arabic display environment and did not itself solve mixed-direction layout. Some symmetrical punctuation was assigned in visually reversed fashion for right-to-left use. The primary accessible preview confirms its ISO 646/ISO 2022 basis; many detailed online tables derive from later reproductions rather than the complete paywalled ISO text. [ISO 9036 preview](https://cdn.standards.iteh.ai/samples/16597/4efd6226f6a447f7b61d26a57b01db97/ISO-9036-1987.pdf)

**[STANDARD]** ECMA-114, first edition June 1986 and later ISO 8859-6, defines a single-byte Latin/Arabic repertoire. Its later edition explicitly says bidi control functions are outside the graphic-set standard. Thus a byte-to-character map alone was insufficient for display. [ECMA-114](https://ecma-international.org/publications-and-standards/standards/ecma-114/)

**[SCHOLARLY]** Vendor alternatives included IBM DOS and EBCDIC Arabic code pages, Macintosh Arabic, Microsoft Windows-1256, printer glyph sets, and “shaped” versus “unshaped” variants. These differed not only in character assignment but in whether text was stored logically, visually, or as contextual forms. Conversion without knowing that model can preserve all bytes yet reverse words or produce disconnected letters.

---

## Hebrew

### Character model

**[STANDARD]** Hebrew base letters are strong right-to-left characters. Vowel points, cantillation marks and other combining marks follow their base character in logical storage. Final KAF, MEM, NUN, PE and TSADI are separately encoded characters because their spelling identity and conventional word-final use are textual, not merely automatic font shapes.

**[STANDARD]** Hebrew presentation forms at U+FB1D–U+FB4F are chiefly compatibility characters. Normal text should generally use base letters plus combining marks. Canonically equivalent Hebrew strings can differ in code-point sequence; normalization is therefore material to comparison.

### Visual and logical legacy encodings

**[STANDARD]** ISO 8859-8 and ECMA-121 provide eight-bit Latin/Hebrew repertoires. The 2000 ECMA-121 edition identifies its relationship to ISO 8859-8. [ECMA-121 PDF](https://www.ecma-international.org/wp-content/uploads/ECMA-121_2nd_edition_december_2000.pdf)

**[STANDARD]** RFC 1555’s December 1993 MIME convention made plain `ISO-8859-8` visual order by default. RFC 1556 defined mechanisms for bidirectional MIME text. Later `ISO-8859-8-I`, Windows-1255 and Unicode practice use logical order.

**[FINDING]** “ISO-8859-8 is visual” describes a protocol convention, not a different byte-to-character map. Direction metadata and processing model distinguish visual and logical interpretations. This distinction is a recurrent source of mislabeled Hebrew data.

---

## Indic scripts

### Abugida model

**[STANDARD]** Brahmi-derived Indic scripts are normally encoded as abugidas. A consonant character carries an inherent vowel; independent vowels are used where no consonant base exists; dependent vowel signs modify consonants; a virama suppresses the inherent vowel.

**[STANDARD]** The effective rendering unit is often an orthographic syllable rather than a code point. A simplified structure is `(((C)C)C)V`, with marks. A consonant followed by virama forms a “dead” consonant, which may display with a visible virama, a half-form, a below-base form, or a conjunct ligature depending on script, language, font and shaping rules.

### Logical storage and visual reordering

**[STANDARD]** A dependent vowel is stored after its consonant even if drawn before it. Devanagari KA U+0915 plus VOWEL SIGN I U+093F is stored:

```text
0915 093F
```

but displayed with the vowel glyph to the left:

```text
कि
```

The renderer may move the vowel glyph to the far left of an entire consonant cluster, not merely swap two code points.

### ISCII

**[STANDARD]** ISCII, Indian Standard IS 13194:1991, is an eight-bit encoding that shares one code layout among several structurally related Indian scripts. An ATR mechanism announces the script represented by subsequent bytes. Its high half includes Indic letters and signs; HALANT/VIRAMA and NUKTA participate in sequences. [Unicode Indic FAQ](https://www.unicode.org/faq/indic.html)

**[STANDARD]** Unicode’s original Devanagari block preserved the relative ordering of ISCII-1988 positions. Unlike ISCII, Unicode assigns separate blocks to Devanagari, Bengali, Gurmukhi, Gujarati, Oriya/Odia, Tamil, Telugu, Kannada and Malayalam rather than switching one byte repertoire between scripts.

**[FINDING]** ISCII’s shared positions express structural kinship, but not identity of characters across scripts. Unicode chose script-specific identity while retaining a parallel ordering useful for conversion.

### Shaping engines and OpenType

**[STANDARD]** In OpenType-style processing, a shaping engine generally:

1. Segments text into script and directional runs.
2. Identifies syllables or clusters.
3. Classifies bases, consonants, viramas, vowel signs and marks.
4. Applies prescribed reordering.
5. Maps characters to nominal glyphs.
6. Applies GSUB substitutions—half forms, reph, conjuncts, contextual forms and ligatures.
7. Applies GPOS positioning and attachment.
8. Returns glyph IDs, clusters, advances and offsets.

Microsoft documents the Devanagari and Arabic pipelines in its OpenType material. [OpenType glyph processing](https://learn.microsoft.com/en-us/typography/develop/processing-part2), [Arabic OpenType development](https://learn.microsoft.com/en-gb/typography/script-development/arabic)

**[DOCUMENT]** Uniscribe appeared as Microsoft’s Windows complex-script service around the Windows 2000 era, with engines for Arabic, Hebrew, Indic, Thai and other scripts. DirectWrite later incorporated broader layout services.

**[DOCUMENT]** Apple’s Core Text sits over Core Foundation string services and Apple font technologies; Apple Advanced Typography provides contextual substitutions and positioning. Precise behavior has varied by operating-system and font version, so “CoreText renders script X” is not a complete interoperability specification.

**[DOCUMENT]** HarfBuzz is a cross-platform open-source shaper used by major browsers, Linux text stacks, Android components and many applications. Its documentation defines shaping as transforming Unicode code points into an orthographically correct two-dimensional glyph arrangement. It supports OpenType shaping models, AAT and Graphite. [HarfBuzz shaping concepts](https://harfbuzz.github.io/shaping-concepts.html)

**[FINDING]** A font is executable layout data in a limited but meaningful sense. Two conformant systems given the same Unicode string but different fonts, feature selections, language tags or shaper versions can return different glyph sequences while preserving the same text.

---

## Thai, Khmer, Tibetan and Mongolian

### Thai and Khmer

**[STANDARD]** Thai and Khmer do not regularly mark every word boundary with visible spaces. Spaces often separate larger phrases. Word selection, line breaking and cursor movement therefore may require dictionary or language-specific analysis; encoding characters is not sufficient.

**[STANDARD]** U+200B ZERO WIDTH SPACE can explicitly mark a word or line-break opportunity in languages including Thai, Khmer, Myanmar and Japanese, but it is not a universal substitute for segmentation. [Unicode 17.0, Chapter 23](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-23/)

**[STANDARD]** Khmer is Brahmi-derived and uses consonant signs, dependent vowels and subscript forms. Unicode 17 directs implementers to detailed Khmer encoding guidance. [Unicode 17.0, Chapter 16](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-16/)

### Tibetan

**[DOCUMENT]** Unicode 1.0 contained a Tibetan model based substantially on Indic-style virama behavior. During reconciliation with ISO 10646, that allocation was withdrawn. Unicode 2.0 reintroduced Tibetan with separately encoded nominal and subjoined consonant forms.

**[DOCUMENT]** Unicode Technical Report #2 records the revised Tibetan proposal, derived from a July 1992 UK ballot comment on DIS 10646. [Unicode Technical Report #2](https://www.unicode.org/standard/reports/tr2.html)

**[DISPUTED]** The central 1990s disagreement concerned whether Tibetan stacks should be represented through a virama/coeng-like mechanism or explicit subjoined letters, and whether the repertoire adequately represented traditional, Sanskrit and scholarly material. Later Chinese proposals sought large sets of precomposed Tibetan stacks or “BrdaRten” characters; critics argued that these duplicated sequences already expressible with the compositional model. [WG2 N2621](https://www.unicode.org/wg2/docs/n2621.pdf), [contemporary Unicode-list discussion](https://www.unicode.org/mail-arch/unicode-ml/y2002-m12/0224.html)

**[FINDING]** Sources document a genuine standards dispute, but slogans that Unicode “broke Tibetan” or that one national delegation single-handedly imposed the current model erase several rounds of proposals, ballot comments and Tibetan-user consultation. Some early committee records are not online, leaving the allocation’s detailed authorship incompletely reconstructable.

### Mongolian

**[STANDARD]** Traditional Mongolian is normally written vertically in columns advancing left-to-right. Unicode stores characters in logical sequence; layout determines vertical flow. The script also has joining and positional variation, much of it context- and language-dependent.

**[STANDARD]** UAX #50 defines informative vertical-orientation properties. Mongolian code-chart glyphs are shown in their vertical orientation; in horizontal display they may be rotated. OpenType fonts have historically made assumptions about whether glyphs arrive pre-rotated, requiring coordination between font and layout engine. [UAX #50](https://www.unicode.org/reports/tr50/)

**[CONTROVERSY]** Mongolian users and implementers have objected to ambiguous variation selection, inconsistent font behavior and difficulty representing traditional distinctions. These are strong tests of “characters, not glyphs”: too much semantic variation left to fonts harms interchange, while encoding every contextual glyph would reproduce the presentation-form problem.

---

## CJK vertical text

**[STANDARD]** Chinese, Japanese and Korean text can run vertically. Han ideographs and kana normally remain upright; Latin text may rotate or be set upright character-by-character; brackets and punctuation require vertical variants or rotation and positional adjustment. UAX #50 supplies defaults, while CSS Writing Modes and layout applications may override them.

**[FINDING]** Vertical CJK is not a separate encoding. Compatibility characters for vertical presentation exist because earlier standards encoded some display forms, but modern systems generally derive vertical glyphs through font features and layout.

---

## Origins and chronology

### Ancient and mechanical background

**[SCHOLARLY]** Hebrew and Arabic descend from consonantal writing traditions ultimately related to Northwest Semitic alphabets. Their right-to-left direction long predates computing. Arabic’s joining and contextual forms developed through manuscript practice; Hebrew’s consonantal base later acquired systems of points and cantillation. Unicode did not invent either directionality or combining behavior—it had to model them.

**[SCHOLARLY]** Indic abugidas descend from Brahmi traditions. Their consonant-plus-inherent-vowel structure and graphic treatment of clusters are likewise properties of writing systems, not computer embellishments.

**[DOCUMENT]** Baudot’s five-bit telegraph code, Donald Murray’s teleprinter refinements, Hollerith punched-card encodings, CCITT International Telegraph Alphabets, ASCII and EBCDIC established the earlier assumption that a character code mapped a small repertoire onto fixed device actions or glyph positions. Complex scripts exposed the limits of that assumption.

### National and vendor era, 1960s–1980s

**[STANDARD]** ASCII, ASA X3.4-1963 and its revisions, encoded 128 control and graphic positions. It had no Hebrew, Arabic or Indic letters. ISO 646 national variants could replace a small number of graphic characters, but could not create a satisfactory multilingual or mixed-script system.

**[SCHOLARLY]** Terminals and applications filled the gap through national seven-bit sets, ISO 2022 switching, eight-bit sets, vendor code pages, glyph codes, local keyboard conventions, and screen-order storage. The same byte could mean Arabic in one code page, Hebrew in another and Latin punctuation in a third.

**[STANDARD]** ISO 2022 formalized designation and invocation of coded sets through escape sequences, locking shifts and single shifts. Stateful streams could lose synchronization when an escape or shift byte was corrupted; a mid-stream reader needed an external initial state or a subsequent designation/reset sequence.

**[STANDARD]** ASMO 449/ISO 9036 addressed Arabic in seven bits. ECMA-114/ISO 8859-6 and ECMA-121/ISO 8859-8 supplied eight-bit Latin/Arabic and Latin/Hebrew repertoires. ISCII supplied an eight-bit script-shifting model for Indian scripts.

### Xerox and Unicode, 1978–1991

**[DOCUMENT]** Joe Becker’s *Unicode 88* traces an internal Xerox line from Bob Belleville’s 1978 “Universal Signs,” through the Xerox Character Code Standard maintained from 1982. Becker credited Peter Fenwick and Dave Opstad with the pure 16-bit approach and Lee Collins with ideographic unification. He called the document exploratory, not Xerox policy. [Unicode 88](https://www.unicode.org/history/Unicode88.pdf)

**[DOCUMENT]** The Unicode Consortium’s chronology places foundational conversations in late 1987 among Joe Becker at Xerox, Lee Collins—moving from Xerox to Apple—and Mark Davis at Apple. Becker coined “Unicode” for “unique, universal, and uniform” encoding. Initial principles and prototypes appeared in 1988. [Early Years of Unicode](https://www.unicode.org/history/earlyyears.html)

**[RECOLLECTION]** Davis later recalled that work on Apple KanjiTalk and Apple File Exchange made incompatible encodings a practical engineering problem. He described trials comparing fixed and variable-width representations and credited Collins as a principal force behind Han unification. These interviews were conducted years later and are participant testimony, not contemporaneous minutes.

**[DOCUMENT]** *Unicode 88*, dated 29 August 1988, proposed a fixed 16-bit “wide-body ASCII” architecture for living languages. It assumed that 65,536 positions could suffice with significant unification and exclusion of presentation variants.

**[DOCUMENT]** In 1989 a bidi subcommittee hosted by Asmus Freytag at Microsoft compared proposals associated with Mark Davis and IBM specialists. The institutional chronology confirms the committee; it does not support a simple one-person invention narrative. [Unicode 1.0 chronology](https://www.unicode.org/history/versionone.html)

**[DOCUMENT]** The Unicode Consortium incorporated in California in January 1991. Unicode 1.0 Volume 1 appeared in October 1991; its Han supplement followed in 1992.

### Unicode and ISO 10646 merger

**[DOCUMENT]** Unicode and ISO initially pursued competing universal-set architectures. Early ISO 10646 designs contemplated a much larger multi-octet space, while Unicode emphasized a fixed 16-bit repertoire convenient for then-current software.

**[SCHOLARLY]** The political and technical compromise aligned character identities and code positions in Unicode and ISO/IEC 10646. ISO/IEC 10646-1:1993 and Unicode 1.1 consequently shared the same repertoire.

**[FINDING]** “Unicode defeated ISO” and “ISO absorbed Unicode” are both oversimplifications. Unicode’s 16-bit layout strongly shaped the merged BMP; ISO supplied the international national-body process and ultimately the larger code-space framework. Both standards now maintain synchronized repertoires while retaining distinct conformance and publication structures.

### Beyond 16 bits

**[STANDARD]** Unicode was a pure 16-bit design from 1991 through the first half of the 1990s. Compatibility requirements and the scale of historic and CJK material made that ceiling untenable. Unicode 2.0, July 1996, introduced the architecture that became UTF-16: surrogate pairs extended the code space to U+10FFFF. [Unicode UTF FAQ](https://unicode.org/faq/utf_bom.html)

### UAX #9

**[DOCUMENT]** The L2 register records Mark Davis’s UTR #9 bidi proposal as L2/98-067 on 26 February 1998. A February 1999 draft, Revision 3, says it revised the Unicode 2.1 algorithm for Unicode 3.0. [L2 1998 register](https://www.unicode.org/L2/L1998/Register-1998.html), [UTR #9 Revision 3](https://www.unicode.org/reports/tr9/tr9-3.html)

**[DOCUMENT]** UTC minutes from April 1998 record a Microsoft objection that one proposed change would alter existing implementations and embedding/number interaction. June 1999 minutes appointed Davis rapporteur, required two independent implementations and sought equivalence between explicit controls and style-based implementations. [UTC #76 minutes](https://www.unicode.org/L2/L1998/98158.html), [UTC #80 minutes](https://www.unicode.org/L2/L1999/99176.htm)

**[STANDARD]** UAX #9 became an integral annex of Unicode 3.0. Revision 51 was reissued for Unicode 17.0. Its acknowledgments credit Davis with the initial version and maintenance through 2023; Ken Whistler with later maintenance; Aharon Lanin and Andrew Glass with substantial isolate work for Unicode 6.3; and Robin Leroy with substantial Unicode 15.0 work. [Current UAX #9](https://www.unicode.org/reports/tr9/)

---

## Adoption and continuing use

**[SCHOLARLY]** Early Unicode deployment was driven by system vendors: Apple, Microsoft, IBM, Sun, Xerox, Novell and others needed one internal character model across localized products. Windows APIs and Java popularized 16-bit code units, leaving the persistent but false equation “character = 16-bit `char`.”

**[STANDARD]** MIME initially permitted many registered charsets. RFC 2277 later required Internet protocols to identify character encodings and to support UTF-8 where appropriate. RFC 3629 standardized the modern four-byte UTF-8. RFC 5198 defined UTF-8 plus NFC-oriented “Net-Unicode” as an international counterpart to NVT ASCII.

**[MODERN]** Web standards converged on UTF-8, while browsers retained complex legacy decoders for compatibility. The WHATWG Encoding Standard deliberately collapses or aliases many historic labels so that all browsers decode legacy pages consistently.

**[FINDING]** Unicode did not make legacy encodings disappear. They survive in archived email, databases, removable media, filenames, terminal settings, programming-language APIs, fonts and undocumented vendor data. Mojibake results when correct bytes are decoded under the wrong character map; bidi or shaping failure can then compound the damage even after characters are recovered.

---

## What Unicode can and cannot express

**[STANDARD]** Unicode can express abstract characters, combining marks, script-specific format controls, standardized variation sequences, emoji sequences, line and paragraph separators, and private-use agreements.

**[STANDARD]** It does not by itself encode:

- A particular typeface or calligraphic hand.
- Exact glyph outlines or kerning.
- Page geometry and column order.
- Every ligature as a character.
- Arbitrary historic glyph variants.
- Language identity merely from characters.
- A universal word-segmentation or dictionary order.
- Guaranteed display when the font or shaper lacks support.

**[FINDING]** The practical unit of writing can exceed every low-level unit:

```text
byte ≠ code unit ≠ code point ≠ grapheme cluster ≠ orthographic syllable ≠ glyph ≠ word
```

Arabic lam-alef can be two code points and one glyph. A Devanagari conjunct can be several code points and one or more glyphs. An emoji family can be several emoji plus joiners and appear as one pictograph. A decomposed Hebrew consonant with points can contain several code points but behave as one user-perceived unit.

---

## People and institutions

### Individuals

**[DOCUMENT]**

- **Émile Baudot** developed a five-unit telegraph code in the 1870s.
- **Donald Murray** redesigned five-bit teleprinter coding around mechanical efficiency in the early twentieth century.
- **Herman Hollerith** developed punched-card tabulation and its coding conventions from the 1880s onward.
- **Robert W. Bemer** advocated standardized computer character coding and participated in ASCII work. His relevance here is ancestral: ASCII’s limits helped motivate universal encoding.
- **Charles E. Mackenzie** documented telegraph, punched-card, ASCII, EBCDIC and other code histories in *Coded Character Sets: History and Development* (1980).
- **Joe Becker** wrote *Unicode 88* and coined “Unicode.”
- **Lee Collins** worked on repertoire construction and Han unification at Xerox and Apple.
- **Mark Davis** co-developed the Unicode architecture, helped found the Consortium, and created and maintained the early UAX #9 text.
- **Peter Fenwick** and **Dave Opstad** were credited by Becker with the pure 16-bit design direction.
- **Asmus Freytag** hosted or participated in early bidi standardization and later worked extensively on Unicode.
- **Ken Whistler** became a principal standards editor and character-property specialist.
- **Aharon Lanin** and **Andrew Glass** contributed substantially to bidi isolates.
- **Rob Pike** and **Ken Thompson** designed UTF-8 in 1992; this affected byte encoding, not the original bidi algorithm.
- **Eric Mader**, **Murray Sargent**, **Kamal Mansour**, **Michel Suignard**, **Roozbeh Pournader**, **Behdad Esfahbod** and others contributed to complex-script layout, font technology, bidi or Arabic standards.

### Institutions

**[DOCUMENT]**

- **ASA/ANSI X3** standardized ASCII.
- **ECMA TC1** produced eight-bit coded graphic sets including ECMA-114 and ECMA-121.
- **ISO/IEC JTC 1/SC 2/WG 2** maintains ISO/IEC 10646 repertoire work.
- **IBM** produced EBCDIC and numerous national code pages and supplied bidi expertise.
- **Xerox** developed XCCS and early multilingual workstation systems.
- **Apple** supplied engineers, early prototypes, KanjiTalk experience and later AAT/Core Text.
- **Microsoft** hosted early bidi comparisons and developed Uniscribe, OpenType and DirectWrite.
- **The Unicode Consortium/UTC** standardizes characters, properties and algorithms.
- **The IETF** standardized Internet charset policy and UTF-8.
- **The W3C and WHATWG** integrated Unicode directionality and encoding behavior into HTML and CSS.
- **FreeType, HarfBuzz and open-source desktop stacks** made high-quality shaping portable across vendors.

---

## Culture

### Plain text

**[MODERN]** Unicode broadened the “plain text” ideal from “ASCII bytes without formatting” to “encoded characters plus standardized properties and algorithms.” Yet bidi controls, variation selectors, joiners and combining marks make modern plain text structurally richer than the phrase suggests.

**[FINDING]** Plain text is not presentation-free. It intentionally omits font and page layout while retaining distinctions needed for textual interchange. The boundary between character and presentation is negotiated rather than metaphysically fixed.

### Mojibake

**[MODERN]** *Mojibake*—Japanese 文字化け, roughly “character transformation”—became the common name for text decoded under the wrong encoding. Garbled Arabic and Hebrew can additionally exhibit reversal or disconnected forms; Indic mojibake may destroy syllable structure.

**[MODERN]** Artists, glitch practitioners and internet users have deliberately reused mojibake, replacement characters and combining-mark overload as an aesthetic. This is a secondary cultural use of failure modes, not an intended property of the standards.

### ASCII art and the demoscene

**[SCHOLARLY]** ASCII art and related PETSCII, ANSI and code-page art depend on fixed cell grids and exact glyph repertoires. Unicode can transcode many characters but cannot guarantee preservation of the original font metrics or block-element shapes. Accurate preservation sometimes requires the original code page and font rather than Unicode text alone.

### Emoji

**[DOCUMENT]** Emoji entered Unicode mainly for round-trip compatibility with Japanese mobile-carrier sets whose private encodings disagreed. Unicode 6.0 in 2010 supplied the first large standardized repertoire.

**[CONTROVERSY]** Public debate portrays the Consortium as “voting on pictures,” while the formal process evaluates evidence of expected use, compatibility, distinctiveness, open-endedness and representability. Vendors—not Unicode—choose color artwork. Nevertheless, encoding grants durable interchange status, and unequal proposal resources or documentation can affect which communities successfully navigate the process.

### Unicode as a political institution

**[SCHOLARLY]** Encoding determines whether a community’s texts can be reliably searched, exchanged and preserved. Script proposals consequently involve governments, scholars, vendors, religious institutions and language communities, not just software engineers.

**[FINDING]** “Unicode decides which peoples exist” is rhetorical rather than literally accurate: unencoded writing can exist in images, private fonts or markup. But lack of standardized encoding imposes significant technical and economic costs, so repertoire decisions have real distributive effects.

---

## Controversies and disputes

### “Characters, not glyphs”

**[DISPUTED]** The maxim is criticized whenever users regard a visible distinction as semantically important but Unicode treats it as font style, language-sensitive rendering or a variation. Defenders answer that encoding contextual glyphs causes duplicate spellings, harms searching and repeats the legacy Arabic presentation-form model.

**[FINDING]** Neither extreme works universally. Unicode encodes some compatibility glyph distinctions, presentation forms, variation selectors and emoji presentation selectors while declining many other visual variants. The operating principle is constrained by stability and legacy round-tripping.

### Han unification

**[DOCUMENT]** Unicode unified equivalent Han characters found in Chinese, Japanese and Korean source standards while generally preserving distinct simplified, traditional or semantically different forms. The current standard says typographic differences lie on a “Z-axis” and can be handled through fonts, language information or standardized variation sequences. [Unicode Chapter 18](https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/)

**[DISPUTED]** Japanese critics argued that regional glyph distinctions, personal-name variants and scholarly forms were not merely typography and that unification made faithful display dependent on language-tagged fonts. Later variation sequences and large CJK extensions mitigated but did not erase these objections.

**[DOCUMENT]** Unicode’s own historical defense says unification avoided duplicate encoding of the same Han character in several national standards and drew upon JIS and Chinese unification rules. [UTN #26](https://www.unicode.org/notes/tn26/), [Unicode Appendix E](https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/)

**[FINDING]** Claims that Western members simply forced unification over a uniform Japanese position are not adequately supported by the primary material reviewed here. National delegations participated in the technical unification work, but national and specialist opinion was never monolithic.

### Tibetan

**[DISPUTED]** Tibetan’s withdrawal and re-encoding are unusually visible examples of an early Unicode model being replaced. Debate persisted over compositional versus precomposed stacks and the authority of different Tibetan user groups, national bodies and scholars.

**[FINDING]** The surviving online record is incomplete. Several proposal numbers and committee records are cited in later documents but are unavailable or only indirectly reproduced. Definitive allocation-by-allocation attribution requires archival WG2 and UTC holdings.

### Indic model

**[DISPUTED]** Critics contend that the virama-based model can be difficult for users, permits canonically awkward sequences, and embeds Sanskrit grammatical terminology into scripts with different indigenous analyses. Defenders point to its relationship with ISCII, phonetic input order and avoidance of encoding every conjunct.

**[FINDING]** Many visible “Unicode bugs” in Indic text are actually combinations of invalid sequences, incomplete fonts, incorrect syllable segmentation, shaper defects and disagreements about orthography. Encoding and rendering responsibility cannot be assigned without examining the exact sequence and font.

### Bidi security

**[STANDARD]** UTR #36 identified bidi spoofing and UTF-8 canonicalization attacks. UTS #39 now carries the maintained confusable-security mechanisms. [UTR #36](https://www.unicode.org/reports/tr36/), [UTS #39](https://www.unicode.org/reports/tr39/)

**[MODERN]** “Trojan Source,” publicized in 2021, demonstrated how bidi controls in source comments and strings could make tokens appear in a different visual order from compiler processing. The technique uses standard behavior; the vulnerability lies in source tools failing to expose direction-changing controls or constrain their placement.

**[STANDARD]** Overlong UTF-8 once enabled security filters and downstream decoders to interpret the same bytes differently—for example, an overlong representation of backslash. Unicode 3.1 and RFC 3629 made such sequences unequivocally ill-formed.

**[STANDARD]** Homoglyph or confusable attacks exploit characters such as Latin `a`, Cyrillic `а`, Greek omicron and shaped-script forms. Unicode security specifications emphasize that confusability is font- and context-dependent and cannot be solved by declaring all similar-looking characters identical.

### BOM controversy

**[STANDARD]** A BOM is useful in otherwise unlabelled UTF-16/32 data. In UTF-8 it is only a signature.

**[CONTROVERSY]** UTF-8 BOMs can break Unix shebangs, protocol signatures, concatenation and binary comparison, while some Windows software historically used them to recognize UTF-8. The correct rule is protocol-specific, not “always include” or “always strip.”

### Standards politics

**[SCHOLARLY]** Unicode’s corporate consortium can move faster than an intergovernmental standards body but raises representation and access questions. ISO’s national-body structure supplies formal international legitimacy but can be slower and document access is often paywalled. Their synchronized repertoire combines both systems rather than eliminating the tension.

---

## Folklore audit

### The UTF-8 placemat

**[RECOLLECTION]** Rob Pike recounts that he and Ken Thompson designed UTF-8 during a September 1992 evening in a New Jersey diner, sketching it on a placemat and implementing it immediately for Plan 9.

**[FOLKLORE]** The placemat is famous but rests principally on Pike’s participant account; no contemporaneously archived placemat has been established in the sources reviewed. The documented facts are that Thompson and Pike designed the encoding in 1992 and that X/Open circulated the proposal that became UTF-8. The anecdote concerns UTF-8, not bidi or complex-script shaping.

### “Unicode was invented by one person”

**[FOLKLORE]** Becker is sometimes called the sole inventor because he coined the name and wrote *Unicode 88*. The contemporary proposal itself credits XCCS predecessors, Fenwick, Opstad and Collins. Institutional records add Davis and many repertoire specialists. “Inventor” is therefore an attribution choice, not a complete history.

### “Unicode reverses Arabic”

**[MODERN/FOLKLORE]** Unicode stores Arabic logically; the bidi algorithm computes visual order. Reversed Arabic usually indicates visual-order legacy data, double application of bidi, or naïve string reversal.

### “Every Arabic letter has four Unicode characters”

**[FOLKLORE]** Nominal Arabic letters normally have one character identity. Presentation-form blocks contain compatibility glyph codes, but ordinary text should not use four separate positional characters.

### “One Unicode character equals one glyph”

**[FOLKLORE]** Contradicted directly by the standard and by Arabic ligatures, Indic conjuncts, combining marks and emoji sequences.

### The “unused ASCII bit” and related stories

**[FINDING]** Stories that a spare eighth bit on a particular IBM System/360 design could simply have solved international text conflate storage width, parity, instruction architecture, interchange standards and repertoire allocation. No single-bit addition could encode the required scripts or their layout behavior. These anecdotes belong to broader ASCII/EBCDIC history and are not supported here as explanations of bidi design.

---

## Open questions

1. **Early bidi authorship.** The institutional chronology names a Microsoft-hosted comparison beginning in 1989, but the underlying Davis and IBM proposals are not all publicly accessible. Their precise algorithmic genealogy remains incompletely documented.

2. **National implementation archives.** Detailed documentation for early IBM, Wang, DEC, Apple, DOS and printer-specific Arabic/Hebrew shaped and visual code pages is scattered, inconsistently catalogued and sometimes absent from public archives.

3. **Tibetan deliberations.** Several decisive WG2 and UTC papers are referenced by number but not available online. Archive consultation is necessary to distinguish national-body positions from later summaries.

4. **User-community representation.** Committee records identify organizational votes more readily than the linguistic, religious or regional communities consulted behind them.

5. **Shaping reproducibility.** Unicode strings and OpenType fonts are preservable, but exact historical rendering may depend on a particular engine version and undocumented bug compatibility. Long-term text preservation may therefore require captured fonts, shaper versions and images in addition to characters.

6. **Mongolian distinctions.** The boundary among character identity, free variation, standardized variants and contextual forms remains difficult in practice and continues to generate implementation and community concerns.

7. **Language metadata.** Unicode intentionally does not encode language identity, yet Arabic-script, Han and Indic rendering may require it. Plain-text interchange has no universally reliable channel for that metadata.

8. **Ancient alphabet repository linkage.** The prompt refers to Hebrew and Arabic alphabets in a repository set, but no repository documents were provided for inspection and shell/file access was expressly excluded. No claim about that set’s content has therefore been made.

---

## Sources

### Unicode and ISO

- The Unicode Consortium, *The Unicode Standard, Version 17.0.0* (2025):  
  https://www.unicode.org/versions/Unicode17.0.0/
- Unicode 17.0 core specification PDF:  
  https://www.unicode.org/versions/Unicode17.0.0/UnicodeStandard-17.0.pdf
- Unicode 17.0 character counts:  
  https://www.unicode.org/versions/stats/charcountv17_0.html
- Unicode 17.0 release announcement:  
  https://blog.unicode.org/2025/09/unicode-170-release-announcement.html
- Unicode Chapter 9, Middle East-I:  
  https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-9/
- Unicode Chapter 12, South and Central Asia-I:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-12/
- Unicode Chapter 16:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-16/
- Unicode Chapter 18, East Asia:  
  https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/
- Unicode Chapter 23, Special Areas and Format Characters:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-23/
- Unicode Appendix E, Han Unification History:  
  https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/
- Unicode design principles:  
  https://www.unicode.org/standard/principles.html
- Unicode UTF-8, UTF-16, UTF-32 and BOM FAQ:  
  https://unicode.org/faq/utf_bom.html
- Unicode Arabic FAQ:  
  https://www.unicode.org/faq/arabic.html
- Unicode Indic FAQ:  
  https://www.unicode.org/faq/indic.html
- Unicode presentation-forms FAQ:  
  https://www.unicode.org/faq/ligature_digraph.html
- Unicode security FAQ:  
  https://www.unicode.org/faq/security.html
- UAX #9, Unicode Bidirectional Algorithm, Revision 51:  
  https://www.unicode.org/reports/tr9/
- Early UTR #9, Revision 3, 8 February 1999:  
  https://www.unicode.org/reports/tr9/tr9-3.html
- UTR #9, Revision 6, Unicode 3.0 text:  
  https://www.unicode.org/reports/tr9/tr9-6.html
- UAX #15, Unicode Normalization Forms:  
  https://www.unicode.org/reports/tr15/
- UTS #39, Unicode Security Mechanisms:  
  https://www.unicode.org/reports/tr39/
- UAX #41, Common References:  
  https://www.unicode.org/reports/tr41/
- UAX #50, Unicode Vertical Text Layout:  
  https://www.unicode.org/reports/tr50/
- UAX #53, Unicode Arabic Mark Rendering:  
  https://www.unicode.org/reports/tr53/
- UTR #36, Unicode Security Considerations, stabilized notice:  
  https://www.unicode.org/reports/tr36/
- UTR #36, Revision 3:  
  https://www.unicode.org/reports/tr36/tr36-3.html
- Unicode Technical Report #2, Tibetan:  
  https://www.unicode.org/standard/reports/tr2.html
- Unicode Technical Note #26, *On the Encoding of Latin, Greek, Cyrillic, and Han*:  
  https://www.unicode.org/notes/tn26/
- Unicode history portal:  
  https://www.unicode.org/history/
- Unicode release and publication chronology:  
  https://www.unicode.org/history/publicationdates.html
- *Early Years of Unicode*:  
  https://www.unicode.org/history/earlyyears.html
- Unicode 1.0 chronology:  
  https://www.unicode.org/history/versionone.html
- Joseph D. Becker, *Unicode 88* (29 August 1988):  
  https://www.unicode.org/history/Unicode88.pdf
- Unicode L2 document register, 1998:  
  https://www.unicode.org/L2/L1998/Register-1998.html
- UTC #76 minutes, April 1998:  
  https://www.unicode.org/L2/L1998/98158.html
- UTC #80 minutes, June 1999:  
  https://www.unicode.org/L2/L1999/99176.htm
- UTC #98 minutes, bidi property changes:  
  https://www.unicode.org/L2/L2004/04003.htm
- Mark Davis, L2/09-073, *Bidi Issues*:  
  https://unicode.org/L2/L2009/09073.htm
- Unicode 6.3 bidi testing announcement:  
  https://blog.unicode.org/2013/06/testing-unicode-bidirectional-algorithm.html
- WG2 N2621, Tibetan BrdaRten proposal:  
  https://www.unicode.org/wg2/docs/n2621.pdf
- WG2 N3247, comments on Tibetan proposal:  
  https://www.unicode.org/wg2/docs/n3247.pdf
- ACIP comments on Tibetan encoding, archived Unicode list:  
  https://www.unicode.org/mail-arch/unicode-ml/Archives-Old/UML003/0249.html
- Unicode-list discussion of precomposed Tibetan, 2002:  
  https://www.unicode.org/mail-arch/unicode-ml/y2002-m12/0224.html
- Unicode-list discussion of Tibetan joiner/virama design, 2013:  
  https://www.unicode.org/mail-arch/unicode-ml/y2013-m04/0026.html
- ISO 9036:1987 catalogue entry:  
  https://www.iso.org/standard/16597.html
- ISO 9036:1987 accessible preview:  
  https://cdn.standards.iteh.ai/samples/16597/4efd6226f6a447f7b61d26a57b01db97/ISO-9036-1987.pdf

### ECMA and legacy character sets

- ECMA-114, Latin/Arabic alphabet:  
  https://ecma-international.org/publications-and-standards/standards/ecma-114/
- ECMA-114, second edition PDF:  
  https://www.ecma-international.org/wp-content/uploads/ECMA-114_2nd_edition_december_2000.pdf
- ECMA-121, Latin/Hebrew alphabet, second edition PDF:  
  https://www.ecma-international.org/wp-content/uploads/ECMA-121_2nd_edition_december_2000.pdf

### IETF RFCs

- RFC 20, *ASCII Format for Network Interchange* (1969):  
  https://www.rfc-editor.org/rfc/rfc20.html
- RFC 1341, *MIME* (1992):  
  https://www.rfc-editor.org/rfc/rfc1341.html
- RFC 1345, *Character Mnemonics and Character Sets* (1992):  
  https://www.rfc-editor.org/rfc/rfc1345.html
- RFC 1555, *Hebrew Character Encoding for Internet Messages* (1993):  
  https://www.rfc-editor.org/rfc/rfc1555.html
- RFC 1556, *Handling of Bi-directional Texts in MIME* (1993):  
  https://www.rfc-editor.org/rfc/rfc1556.html
- RFC 2044, *UTF-8, a Transformation Format of Unicode and ISO 10646* (1996):  
  https://www.rfc-editor.org/rfc/rfc2044.html
- RFC 2277, *IETF Policy on Character Sets and Languages* (1998):  
  https://www.rfc-editor.org/rfc/rfc2277.html
- RFC 2279, *UTF-8* (1998):  
  https://www.rfc-editor.org/rfc/rfc2279.html
- RFC 3629, *UTF-8* (2003):  
  https://www.rfc-editor.org/rfc/rfc3629.html
- RFC 5198, *Unicode Format for Network Interchange* (2008):  
  https://www.rfc-editor.org/rfc/rfc5198.html
- IANA character-set registry:  
  https://www.iana.org/assignments/character-sets/character-sets.xhtml

### W3C and web standards

- W3C, *How to use Unicode controls for bidi text*:  
  https://www.w3.org/International/questions/qa-bidi-unicode-controls.en.html
- W3C, *Additional Requirements for Bidi in HTML & CSS*:  
  https://www.w3.org/TR/html-bidi/
- W3C, HTML bidi requirements working document:  
  https://www.w3.org/International/docs/html-bidi-requirements/
- W3C, *Authoring HTML: Handling Right-to-left Scripts*:  
  https://www.w3.org/International/docs/bp-html-bidi/editme.html
- W3C HTML5 bidi test results:  
  https://www.w3.org/International/tests/html-css/bidi-html5/results-bidi-html5
- CSS 2 Recommendation, bidi portions:  
  https://www.w3.org/TR/1998/REC-CSS2-19980512/

### Shaping engines and font technology

- Microsoft, *Developing OpenType Fonts for Arabic Script*:  
  https://learn.microsoft.com/en-gb/typography/script-development/arabic
- Microsoft, *OpenType glyph processing, part 2*:  
  https://learn.microsoft.com/en-us/typography/develop/processing-part2
- Microsoft, *Universal Shaping Engine*:  
  https://learn.microsoft.com/globalization/reference/universal-shaping-engine
- HarfBuzz manual:  
  https://harfbuzz.github.io/
- HarfBuzz, *Shaping concepts*:  
  https://harfbuzz.github.io/shaping-concepts.html
- HarfBuzz, simple shaping example:  
  https://harfbuzz.github.io/a-simple-shaping-example.html
- Apple archived text-system glossary:  
  https://developer.apple.com/library/archive/documentation/mac/pdf/Text/Glossary.pdf

### Historical works requested for follow-up archival consultation

- Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley, 1980, Internet Archive catalogue/search:  
  https://archive.org/search.php?query=Charles%20Mackenzie%20Coded%20Character%20Sets
- Computer History Museum oral-history collection:  
  https://www.computerhistory.org/collections/oralhistories/
- Internet Archive software and manuals collections:  
  https://archive.org/details/software  
  https://archive.org/details/manuals
- Rob Pike, UTF-8 history page:  
  https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt
- Unicode’s history collection, including participant interviews and merger records:  
  https://www.unicode.org/history/
