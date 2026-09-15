# UTF-16 and UCS-2: Research Dossier

> **Standard:** Unicode Standard 1.0/1.1; ISO/IEC 10646-1:1993; UTF-16 added through ISO/IEC 10646-1 Amendment 1 and Unicode 2.0; Internet serialization specified by RFC 2781  
> **Years:** UCS-2 architecture, 1991–1993; surrogate proposal, 1994; UTF-16 publication, 1996; RFC serialization, 2000  
> **Bit width:** UCS-2: fixed 16-bit code values. UTF-16: variable-width, one or two 16-bit code units—two or four bytes when serialized  
> **Repertoire:** UCS-2: at most the Basic Multilingual Plane, U+0000–U+FFFF, historically excluding any interpretation of surrogate pairs. UTF-16: every Unicode scalar value, U+0000–U+D7FF and U+E000–U+10FFFF  
> **Current status:** UTF-16 is a current Unicode and ISO/IEC 10646 encoding form. UCS-2 is obsolete terminology and cannot represent supplementary characters. Unicode 17.0, released September 9, 2025, contains 159,801 graphic and format characters; ISO/IEC 10646:2020 with published amendments remains the current ISO edition pending replacement.

## Evidentiary labels

Claims below are marked as follows:

- **[Standard]** Normative or descriptive text in a published standard, RFC, or official specification.
- **[Document]** Contemporary proposal, manual, committee paper, corporate documentation, or dated archive.
- **[Participant recollection]** A later account by someone involved.
- **[Scholarly reconstruction]** A historian’s or scholar’s synthesis based on documents and testimony.
- **[Disputed]** A claim for which credible participants or records materially disagree.
- **[Folklore]** A widely repeated story whose documentary basis is absent or weak.
- **[Modern argument]** A later technical or political interpretation, manifesto, slogan, or criticism.
- **[Finding: absence]** A requested story for which no UTF-16/UCS-2-specific primary evidence was found.

These labels describe the kind of evidence, not whether a position is good or bad.

---

## Basic identification

### Names and distinctions

**[Standard]** Unicode is a coded character set and character-processing standard. UTF-16 is one encoding form for Unicode scalar values. “UTF-16BE,” “UTF-16LE,” and “UTF-16” are encoding schemes for serializing UTF-16 code units as bytes. These levels must not be conflated:

| Level | Example | Meaning |
|---|---|---|
| Abstract character | LATIN CAPITAL LETTER A | A textual element |
| Code point | U+0041 | Its Unicode number |
| Code unit | `0041` | One 16-bit UTF-16 unit |
| Serialized bytes | `00 41` or `41 00` | Big- or little-endian representation |
| Glyph | A | A rendered shape chosen by a font |

The current formal Unicode model appears in the [Unicode core specification](https://www.unicode.org/versions/Unicode17.0.0/UnicodeStandard-17.0.pdf) and [UTR #17](https://www.unicode.org/reports/tr17/).

**[Standard]** UCS-2 means a two-octet representation of BMP code positions. It does not assign surrogate-pair semantics to two adjacent values. It therefore cannot express U+10000 or higher. The Unicode Consortium now calls UCS-2 obsolete terminology; identical BMP text has the same 16-bit units in UCS-2 and UTF-16, which is why old APIs and documentation often blur them. See the [Unicode UTF FAQ](https://www.unicode.org/faq/utf_bom.html).

**[Standard]** UTF-16 is not “16-bit Unicode” in the sense of one character per 16 bits. It is a variable-width encoding whose code unit is 16 bits. BMP scalar values take one code unit; supplementary scalar values take a surrogate pair.

**[Standard]** A Unicode scalar value is any code point except U+D800–U+DFFF. Thus UTF-16 covers:

- U+0000–U+D7FF;
- U+E000–U+FFFF;
- U+10000–U+10FFFF through pairs.

It cannot encode surrogate code points as characters. An isolated surrogate code unit can exist in permissive APIs, filenames, or memory, but it is not well-formed UTF-16.

### Present repertoire

**[Standard]** Unicode 17.0 added 4,803 characters, bringing the graphic-plus-format total to 159,801. Its code space remains 17 planes of 65,536 positions, U+0000 through U+10FFFF. There are 2,048 surrogate code points, 66 noncharacters, large reserved ranges, and 137,468 private-use positions. The authoritative counts are in the [Unicode 17.0 character-count table](https://www.unicode.org/versions/stats/charcountv17_0.html).

**[Standard]** ISO/IEC 10646:2020 specifies UTF-8, UTF-16, and UTF-32. Amendment 1 appeared in 2023 and Amendment 2 in 2025; a replacement edition is under development. See the [ISO catalogue record](https://www.iso.org/standard/76835.html).

---

## The code in detail

### Basic Multilingual Plane layout

A complete table would contain tens of thousands of assigned characters, so its structure is more useful here.

**[Standard]** The BMP occupies U+0000–U+FFFF:

| Range | Principal role |
|---|---|
| U+0000–U+001F | C0 control-code positions |
| U+0020–U+007E | ASCII graphic repertoire |
| U+007F | DELETE |
| U+0080–U+009F | C1 control-code positions |
| U+00A0–U+024F | Latin supplements and extensions |
| U+0250–U+02FF | IPA and modifier letters |
| U+0300–U+036F | Combining diacritical marks |
| U+0370–U+052F | Greek, Coptic, Cyrillic |
| U+0530–U+058F | Armenian |
| U+0590–U+08FF | Hebrew, Arabic, Syriac, Thaana and related scripts |
| U+0900–U+0DFF | Major Indic-script blocks |
| U+0E00–U+1FFF | Southeast Asian and other alphabetic/syllabic scripts |
| U+2000–U+2BFF | Punctuation, symbols, arrows, mathematics |
| U+2E80–U+33FF | CJK radicals, punctuation, kana, bopomofo, compatibility material |
| U+3400–U+4DBF | CJK Unified Ideographs Extension A |
| U+4E00–U+9FFF | Original CJK Unified Ideographs |
| U+A000–U+D7FF | Yi, Hangul and other scripts |
| U+D800–U+DFFF | Surrogate code points; never scalar values |
| U+E000–U+F8FF | BMP Private Use Area |
| U+F900–U+FAFF | CJK Compatibility Ideographs |
| U+FB00–U+FDFF | Alphabetic and Arabic presentation forms |
| U+FE00–U+FE0F | Variation selectors |
| U+FE20–U+FEFF | Combining half marks, compatibility forms, U+FEFF |
| U+FF00–U+FFEF | Halfwidth and fullwidth forms |
| U+FFF0–U+FFFF | Specials and noncharacters |

The exact current charts are components of [Unicode 17.0](https://www.unicode.org/versions/Unicode17.0.0/).

### Surrogate structure

**[Standard]** Supplementary characters use:

- high surrogates: `D800`–`DBFF`;
- low surrogates: `DC00`–`DFFF`.

For scalar value \(U\), where \(10000_{16} \le U \le 10FFFF_{16}\):

1. Compute \(U' = U - 10000_{16}\).
2. High surrogate = `D800 + (U' >> 10)`.
3. Low surrogate = `DC00 + (U' & 03FF)`.

Reverse calculation:

\[
U = 10000_{16}
  + (\text{high}-D800_{16})\times400_{16}
  + (\text{low}-DC00_{16})
\]

The ranges are disjoint, so a high surrogate unambiguously announces that exactly one low surrogate must follow. A low surrogate cannot begin a valid scalar.

### Why the upper limit is U+10FFFF

**[Standard]** Each half contributes ten payload bits, yielding \(2^{20}=1,048,576\) supplementary values. Added to the first 65,536 positions, this gives 1,114,112 code points through U+10FFFF. Excluding the 2,048 surrogate positions leaves 1,112,064 scalar values.

**[Historical reconstruction]** The modern ceiling is therefore a consequence of the surrogate compromise, not an independently discovered natural boundary for human writing.

### No shift states

**[Standard]** UTF-16 has no locking shift, single shift, escape designation, or code-page state comparable to ISO/IEC 2022. Its only variable-length mechanism is the locally recognizable high-plus-low surrogate pair. U+FEFF at the beginning may identify byte order, but it does not switch the interpretation of subsequent code units in the way an ISO 2022 escape sequence switches designated sets.

### Controls, space, newline, deletion, and case

**[Standard]**

- NUL: U+0000 → code unit `0000`
- horizontal tab: U+0009 → `0009`
- line feed: U+000A → `000A`
- carriage return: U+000D → `000D`
- space: U+0020 → `0020`
- DELETE: U+007F → `007F`

Unicode preserves 65 positions for ISO 2022-compatible C0, C1, and DELETE controls: U+0000–001F, U+007F, and U+0080–009F. Their presence is inherited interoperability, not an instruction that every application give them terminal behavior. See [Unicode Chapter 23](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-23/).

**[Standard]** Unicode also has U+0085 NEXT LINE, U+2028 LINE SEPARATOR, and U+2029 PARAGRAPH SEPARATOR. Nevertheless, file and protocol newline conventions remain higher-level matters. Windows commonly uses CR LF; Unix-like systems commonly use LF; classic Mac OS used CR. UTF-16 itself mandates none of those conventions.

**[Standard]** Case is a character property and mapping problem, not a bit toggle. ASCII happens to place `A` at U+0041 and `a` at U+0061, twenty hexadecimal positions apart, but Unicode casing may be contextual or map one character to several. Turkish dotted/dotless I, Greek final sigma, and German sharp s defeat a universal fixed-bit case rule.

### Byte order and the BOM

**[Standard]** A 16-bit unit can be serialized most-significant byte first or least-significant byte first:

| Code unit | UTF-16BE | UTF-16LE |
|---|---|---|
| `0041` | `00 41` | `41 00` |
| `20AC` | `20 AC` | `AC 20` |
| `D83D` | `D8 3D` | `3D D8` |

**[Standard]** Initial U+FEFF produces:

- UTF-16BE BOM: `FE FF`;
- UTF-16LE BOM: `FF FE`.

U+FFFE is a noncharacter. Encountering bytes that decode as U+FFFE at the beginning is therefore a strong indication that the byte order was reversed. The Unicode Standard emphasizes that the BOM identifies order; it is not an active byte-order-switching control. See [Unicode Chapter 2](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-2/) and [Chapter 23](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-23/).

**[Standard]** RFC 2781 defines three MIME charset labels:

- `UTF-16BE`: big-endian; no BOM permitted as a signature;
- `UTF-16LE`: little-endian; no BOM permitted as a signature;
- `UTF-16`: either order; a BOM should identify it, and absent contrary protocol information the RFC defaults to big-endian.

See [RFC 2781](https://www.rfc-editor.org/rfc/rfc2781.html).

**[Historical standard]** U+FEFF was originally also ZERO WIDTH NO-BREAK SPACE. Since Unicode 3.2, U+2060 WORD JOINER is strongly preferred for that semantic use. This repairs an overloaded design in which the same code point could be file signature or content depending on position.

**[Modern argument]** BOM critics object that signatures become embedded in concatenated strings, interfere with Unix tools, and duplicate external metadata. Defenders answer that byte order otherwise cannot be inferred reliably from arbitrary UTF-16. Both positions are context-dependent: a self-describing file differs from a typed database field or network record.

### Well-formedness and errors

**[Standard]** Well-formed UTF-16 consists only of:

- non-surrogate code units; or
- a high surrogate immediately followed by a low surrogate.

These are ill-formed:

- a high surrogate at end of input;
- a high surrogate followed by a non-low-surrogate;
- a low surrogate without an immediately preceding high surrogate;
- two highs or two lows treated as one character.

Conformance clause C10 requires a process interpreting a claimed Unicode encoding form to treat ill-formed sequences as an error, not as characters. See the [Unicode core specification](https://www.unicode.org/versions/Unicode17.0.0/UnicodeStandard-17.0.pdf).

**[Standard]** Decoders may stop, report, or substitute according to their API or protocol, but must not reinterpret lone surrogates as valid scalar values. Replacement commonly uses U+FFFD, though replacement policy is not simply “part of UTF-16.”

### Synchronization and corruption

**[Analysis from standard structure]** At the code-unit level, UTF-16 is locally self-synchronizing:

- any non-surrogate is a complete scalar;
- a high surrogate expects one following low;
- a low surrogate announces that the reader is either at the second half of a pair or in malformed text.

After a damaged surrogate sequence, a decoder can ordinarily resume at the next non-surrogate or valid high-low pair. The maximum structural ambiguity is local.

**[Analysis from byte structure]** At an arbitrary byte boundary it is not self-synchronizing. Losing or inserting one byte destroys 16-bit alignment indefinitely unless an external framing boundary, BOM, length field, or recognizable structure restores it. Losing two bytes preserves code-unit alignment but deletes or changes a unit.

**[Comparison]** UTF-8 has recognizable continuation bytes and can normally regain character alignment within a few bytes. UTF-32 needs four-byte alignment. UTF-16 lies between them at the character level, but shares UTF-32’s dependence on external byte alignment.

**[Security finding]** UTF-16 has no “overlong” scalar encodings analogous to historically accepted overlong UTF-8. A scalar has one well-formed UTF-16 representation. Its characteristic encoding hazards are unpaired surrogates, inconsistent replacement, byte-order confusion, truncation between pair halves, and APIs that incorrectly treat code units as complete characters.

### Collating order

**[Standard]** UTF-16 byte or code-unit order is not linguistic collation. Numeric code-unit comparison happens to preserve scalar-value order for BMP values and, with correctly paired supplementary values, UTF-16’s surrogate mapping was constructed so that binary comparison has useful ordering properties. But it does not supply dictionary order, locale order, accent equivalence, canonical equivalence, or culturally appropriate Han ordering.

Examples:

- `Z` (`005A`) sorts before `a` (`0061`) numerically;
- precomposed `é` (`00E9`) is not binary-equal to `e + ◌́` (`0065 0301`);
- Swedish, German, and English place `ä` differently;
- CJK code-point order is allocation order, not pronunciation or dictionary order.

The Unicode Collation Algorithm and locale tailoring are separate from UTF-16.

### Worked example 1: `A€😀`

Code points:

- `A` = U+0041
- `€` = U+20AC
- `😀` = U+1F600

For U+1F600:

- \(1F600-10000=F600\)
- high ten bits: `003D`; `D800 + 003D = D83D`
- low ten bits: `0200`; `DC00 + 0200 = DE00`

| Text | UTF-16 code units | UTF-16BE bytes | UTF-16LE bytes |
|---|---|---|---|
| `A` | `0041` | `00 41` | `41 00` |
| `€` | `20AC` | `20 AC` | `AC 20` |
| `😀` | `D83D DE00` | `D8 3D DE 00` | `3D D8 00 DE` |

With BOM:

- UTF-16BE: `FE FF 00 41 20 AC D8 3D DE 00`
- UTF-16LE: `FF FE 41 00 AC 20 3D D8 00 DE`

Neighbouring encodings:

- UTF-8: `41 E2 82 AC F0 9F 98 80`
- UTF-32BE: `00 00 00 41 00 00 20 AC 00 01 F6 00`
- UCS-2: `0041 20AC` followed by **unrepresentable U+1F600**

### Worked example 2: `Hi 🌍\n`

Code points:

- `H` U+0048
- `i` U+0069
- space U+0020
- `🌍` U+1F30D
- LF U+000A

U+1F30D becomes `D83C DF0D`.

| Encoding | Bytes |
|---|---|
| UTF-16BE | `00 48 00 69 00 20 D8 3C DF 0D 00 0A` |
| UTF-16LE | `48 00 69 00 20 00 3C D8 0D DF 0A 00` |
| UTF-8 | `48 69 20 F0 9F 8C 8D 0A` |
| UTF-32BE | `00 00 00 48 00 00 00 69 00 00 00 20 00 01 F3 0D 00 00 00 0A` |

In JavaScript, Java, and .NET-style code-unit accounting:

- `"Hi 🌍\n"` has six UTF-16 code units;
- it has five Unicode code points;
- it has five ordinary grapheme clusters here.

More elaborate emoji may require several code points and many code units for one displayed cluster.

### Worked example 3: normalization

`é` can be:

- NFC: U+00E9 → UTF-16BE `00 E9`;
- decomposed: U+0065 U+0301 → UTF-16BE `00 65 03 01`.

**[Standard]** These sequences can be canonically equivalent while remaining byte- and code-unit-distinct. UTF-16 does not normalize automatically.

---

## Origins

### Before Unicode

**[Scholarly reconstruction]** UTF-16 sits at the end of a long transition from machine-specific codes toward universal interchange:

- Baudot’s five-bit telegraph code and Murray’s modifications used shifts because 32 states could not hold letters, figures, and controls simultaneously.
- Hollerith card encodings associated characters with punch patterns rather than a clean binary alphabet.
- CCITT telegraph alphabets standardized limited repertoires with letter/figure shifts.
- ASCII standardized a seven-bit US-oriented interchange repertoire.
- EBCDIC preserved IBM punched-card and BCD lineage in an eight-bit family.
- ISO/IEC 646 national variants reused a few ASCII positions for national letters and currency symbols.
- ISO/IEC 2022 supplied escape-based designation and shift machinery.
- ISO/IEC 8859 provided mutually incompatible eight-bit Latin, Greek, Cyrillic, Hebrew, and Arabic sets.
- East Asian systems developed fixed or variable two-byte standards and vendor encodings such as JIS X 0208, Shift_JIS, EUC-JP, GB 2312, Big5, KS C 5601, and EUC-KR.

Charles E. Mackenzie’s *Coded Character Sets: History and Development* documents the pre-Unicode lineage through 1980. It therefore cannot document Unicode’s design, but it is an important reconstruction of the technical and committee world Unicode inherited. See the [Internet Archive/Open Library edition record](https://openlibrary.org/books/OL4570655M/Coded_character_sets).

### Xerox antecedents

**[Document]** Xerox’s 1980 Star environment and Xerox Character Code Standard supplied important practical antecedents. XCCS evolved from multilingual work at Xerox and included 16-bit character representations plus compression arrangements.

**[Participant recollection]** Unicode’s official “Early Years” history says Dave Opstad reported in September 1987 that seven years of XCCS compression experience favored fixed-width processing. This recollection supports why the designers valued direct indexing and uniform-width storage, though it was published retrospectively by the institution whose history it celebrates. See [Early Years of Unicode](https://www.unicode.org/history/earlyyears.html).

### 1984 ISO two-byte goal

**[Document quoted in official history]** ISO/TC97/SC2 N1436, 1984, called for an international two-byte graphic character set and asked that programming languages be able to use the same storage for each character. This shows that “universal 16-bit text” was not invented solely at Apple or Xerox.

**[Finding: limitation]** The accessible evidence here is Unicode’s quotation and attribution of N1436, rather than an independently retrieved complete scan. The wording should therefore be cited through the [Unicode history summary](https://www.unicode.org/history/summary.html), not treated as a directly inspected original.

### 1987–1988: Unicode begins

**[Document and participant recollection]** Unicode’s official chronology identifies the initiating engineers as:

- Joseph D. Becker of Xerox;
- Lee Collins, initially at Xerox and then Apple;
- Mark Davis of Apple.

Initial discussions occurred in late 1987. Becker coined “Unicode” in December 1987 to suggest “unique, universal, and uniform.”

**[Document]** In February 1988, Becker produced the initial *Unicode 88* paper; its dated public version is August 29, 1988. It proposed what it called “wide-body ASCII,” a pure 16-bit multilingual system, and anticipated a future in which 5-, 7-, 8-, and 14-bit text architectures would disappear. The original is available as [Unicode 88](https://www.unicode.org/history/Unicode88.pdf).

**[Document]** The early design investigations compared fixed- and mixed-width access, estimated system-wide storage costs of two-byte text, and counted alphabetic repertoires. Lee Collins’s internal Apple alternative was called “High Text,” contrasted with ASCII “Lower Text.”

**[Participant recollection]** Davis later recalled pushing the project to assign actual codes so it would not remain abstract and credited Collins as the prime force behind early Unified Han work. The quotation first appears in Laura Wideburg’s 1995 interviews, republished in Unicode’s 1998 historical pages.

### Why 16 bits looked sufficient

**[Document]** Unicode 88’s stated aim was a code for the characters of all modern text-processing languages in a fixed 16-bit unit. Its estimates depended on:

- unifying duplicate characters;
- encoding characters rather than glyph variants;
- combining accents dynamically;
- unifying related Han characters used across Chinese, Japanese, and Korean;
- reserving compatibility and private-use regions while still fitting the whole repertoire into 65,536 positions.

**[Historical reconstruction]** The 16-bit choice was not simply an arithmetic mistake. It was a systems design optimized for contemporary memory, APIs, font technology, and direct indexing. Its failure was predictive: the repertoire expanded to historic scripts, rare ideographs, symbols, and emoji beyond the original “modern-use” estimates.

### Han unification and the 16-bit budget

**[Document]** In June 1988, Apple, Xerox, and Research Libraries Group participants met to formulate Han-unification criteria. Apple acquired RLG’s East Asian Character Code database; Collins correlated it with Xerox material and national standards.

**[Standard history]** The original repertoire treated characters shared across national sources as one abstract Han character when identity criteria were met, while leaving regional glyph form to fonts. Unicode’s current [Han Unification History](https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/) traces the work through the CJK Joint Research Group and later Ideographic Rapporteur Group.

**[Modern defense]** Unicode Technical Note #26 argues that regional glyph variation is comparable to within-script variation elsewhere and that separate national duplication would require equivalence tables for searching and processing. See [UTN #26](https://www.unicode.org/notes/tn26/).

**[Disputed]** Critics, especially in Japanese scholarly and typographic contexts, have argued that distinctions treated as glyph variants can carry documentary, personal-name, historical, or national importance. “Han unification destroyed Japanese writing” is an overstatement; “all objections are merely font misunderstandings” is also too simple. Source separation, compatibility ideographs, variation sequences, and later disunifications demonstrate that identity decisions can be revisited.

### Formation of the Consortium

**[Document]** Unicode, Inc. was incorporated in California on January 3, 1991. The official history credits Mike Kernaghan, Bill English, Mark Davis, and Asmus Freytag with organizing much of the business side. The early institutional membership involved Apple, Xerox, Microsoft, IBM, Sun, Metaphor, NeXT, Novell, and others at different stages. See the [Unicode History Corner](https://www.unicode.org/history/) and [history summary](https://www.unicode.org/history/summary.html).

### Unicode 1.0

**[Standard]** Unicode 1.0 Volume 1 appeared in October 1991; Volume 2, including complete CJK material, followed in June 1992. It was a 16-bit standard. The archival scans and code charts are available from the [Unicode 1.0 archive](https://www.unicode.org/versions/Unicode1.0.0/).

**[Document]** The Unicode archive preserves a sequence of drafts:

- Unicode Working Draft, August 1990;
- Unicode Preview, October 1990;
- public final-review draft, December 1990;
- pre-copy-edit Version 1 draft, May 7, 1991;
- Unicode 1.0 publication, October 1991.

See the [publication chronology](https://www.unicode.org/history/publicationdates.html).

### The rival ISO 10646 architecture

**[Document and participant reconstruction]** ISO’s first DIS 10646 pursued a larger multi-octet architecture and initially differed from Unicode in code structure, repertoire, Han treatment, combining marks, and restrictions on byte values. It could conceptually accommodate far more than one 16-bit plane but was more cumbersome for systems built around 16-bit characters.

**[Participant recollection]** Kenneth Whistler and Otto Stolz later gave this merger chronology:

- May 1991: an informal Unicode/WG2 meeting in San Francisco;
- June 1991: the first DIS 10646 ballot failed;
- June 3, 1991: Ed Hart drafted a “10646M” merger proposal;
- August 19–23, 1991: the Geneva WG2 meeting accepted the core compromise;
- October 1991: SC2 authorized a replacement DIS;
- 1993: ISO/IEC 10646-1 was published.

Stolz supplied a remembered ballot of 8 yes, 11 no, and 2 abstentions among participating members, with many negative comments calling for one universal code. These are participant accounts preserved in the [Unicode mailing-list history answers](https://www.unicode.org/mail-arch/unicode-ml/y2002-m02/0110.html), not the ballot papers themselves.

### The merger result: UCS-2 and UCS-4

**[Standard]** ISO/IEC 10646-1:1993 specified a universal coded character set whose BMP matched Unicode 1.1. UCS-2 represented that plane with 16-bit values. UCS-4 expressed the larger ISO architecture with four octets.

**[Standard]** Unicode 1.1 and ISO/IEC 10646-1:1993 had identical character names and code positions. Unicode additionally specified properties and algorithms; ISO specified coded-repertoire architecture and encoding forms. Their committees committed to synchronization, which continues. See [Unicode Appendix C](https://unicode.org/versions/Unicode17.0.0/core-spec/appendix-c/) and the [Unicode/ISO FAQ](https://www.unicode.org/faq/unicode_iso.html).

**[Historical reconstruction]** The merger was not one party simply defeating the other. ISO retained a larger conceptual space; Unicode retained a 16-bit BMP and much of its repertoire and processing model. UCS-2 became the practical bridge.

### The pressure beyond 65,536

**[Historical reconstruction]** By the early 1990s it was clear that the BMP could not hold every historic script, rare Han form, specialist symbol, and future character while preserving existing allocations and stability. Existing 16-bit implementations made abandoning 16-bit code units expensive.

### 1994: the surrogate amendment

**[Document]** WG2 N970, dated February 7, 1994, proposed UTF-16 through Amendment 1 to ISO/IEC 10646-1. Mark Davis was project editor. This dating comes from Kenneth Whistler’s historical account in the Unicode mailing-list archive.

**[Historical reconstruction]** Surrogates were a compatibility compromise:

- preserve every existing non-surrogate BMP value as one 16-bit unit;
- reserve 2,048 BMP values as pair components;
- reach sixteen supplementary planes;
- avoid expanding all existing strings and APIs to 32-bit units.

### 1996: Unicode 2.0

**[Standard]** Unicode 2.0 was released in July 1996 and published by Addison-Wesley. It incorporated surrogates and the enlarged code space. From this point Unicode was no longer a fixed 16-bit character encoding. See the [Unicode version history](https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-d/) and [release dates](https://www.unicode.org/history/publicationdates.html).

**[Terminological reconstruction]** “UCS-2 became UTF-16” is convenient but imprecise. Existing well-formed BMP text remained byte-for-byte compatible at the code-unit level. The interpretation of valid pairs and the reachable repertoire changed. A UCS-2 implementation remains unable to understand supplementary values.

### 2000: RFC 2781

**[Standard]** Paul Hoffman and François Yergeau published RFC 2781 in February 2000. It defined Internet serialization, error handling, BOM behavior, and the `UTF-16`, `UTF-16BE`, and `UTF-16LE` charset registrations. The RFC is Informational, not an Internet Standard, but is the definitive IETF registration document.

---

## Adoption and decline

### Windows NT, 1993

**[Document]** Windows NT 3.1, released in July 1993, adopted 16-bit Unicode throughout its native “wide” Win32 API. Helen Custer’s contemporary *Inside Windows NT* shows a U+0000–U+FFFF Unicode layout and says NT used Unicode to avoid code-page limitations. See the [1993 book scan](https://www.bitsavers.org/pdf/microsoft/windows_NT_3.1/Custer_Inside_Windows_NT_1993.pdf).

**[Historical precision]** In 1993 this was effectively Unicode 1.x/UCS-2. Calling the original NT design UTF-16 is anachronistic because surrogate semantics were not yet published.

**[Document]** Win32 provided parallel `A` functions for local/code-page strings and `W` functions for 16-bit strings. Current documentation states that `WCHAR` and Windows `wchar_t` are 16-bit UTF-16 code units and must not be assumed to be whole characters. See [Working with Strings](https://learn.microsoft.com/en-us/windows/win32/learnwin32/working-with-strings).

**[Historical reconstruction]** Windows later gained surrogate-aware components without changing the ABI. That compatibility success is also the origin of its permanent code-unit-counting burden.

### Java, 1995

**[Document]** Java 1.0’s `char` was an unsigned 16-bit value designed under the original fixed-width Unicode assumption. Early Java used Unicode 1.1.5. When Unicode 2.0 added supplementary characters, Java retained `char` for source and binary compatibility.

**[Standard/platform documentation]** Modern Java defines `String`, `StringBuffer`, and `char[]` as sequences of UTF-16 code units. Supplementary-aware APIs use `int` code points and methods such as `codePointAt`. A single `char` cannot represent a supplementary scalar. See [Java Character](https://docs.oracle.com/en/java/javase/26/docs/api/java.base/java/lang/Character.html) and the [Java Language Specification history](https://docs.oracle.com/javase/specs/jls/se6/html/lexical.html).

### JavaScript

**[Standard]** ECMAScript strings are ordered sequences of 16-bit unsigned integer values. The standard deliberately permits any such values, including lone surrogates. `length` counts elements/code units, not scalar values or grapheme clusters. See [ECMAScript String values](https://tc39.es/ecma262/2022/multipage/ecmascript-data-types-and-values.html).

**[Historical reconstruction]** JavaScript inherited the 16-bit model during the mid-1990s, when Java and browser technology were being designed around contemporary Unicode. Later editions added code-point escapes, iteration by code point, `codePointAt`, and well-formedness helpers without changing string indexing.

Example:

```javascript
"😀".length              // 2
[..."😀"].length         // 1 code point
"👨‍👩‍👧‍👦".length       // 11 UTF-16 code units
```

The family emoji is one extended grapheme cluster composed from multiple scalars joined by U+200D.

### .NET

**[Platform documentation]** .NET stores `System.String` as contiguous 16-bit `Char` values. It can contain unpaired surrogates. `System.Text.Rune`, introduced in .NET Core 3.0, provides scalar-value operations; text-element APIs handle grapheme clusters. See Microsoft’s [character-encoding introduction](https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-encoding-introduction).

### Qt

**[Platform documentation]** `QString` stores 16-bit `QChar` values, each one UTF-16 code unit; supplementary characters use pairs. Qt also exposes UTF-8 and UCS-4 conversion APIs. See [QString documentation](https://doc.qt.io/qt-6/qstring.html).

### XML and document formats

**[Standard]** XML permits UTF-8 and UTF-16 and defines signature-based recognition. UTF-16 was consequently common in XML-oriented Windows and Java systems, office formats, and interchange where a two-byte-native parser was attractive.

**[Modern practice]** Network and document ecosystems now overwhelmingly prefer UTF-8. The WHATWG Encoding Standard requires UTF-8 for new formats and protocols and retains UTF-16 decoding mainly for compatibility. See the [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/).

### Internet policy

**[Standard]** RFC 2277, published in 1998, requires new IETF protocols to be able to use UTF-8 and mandates charset labeling where needed. It permits other ISO 10646 encodings, including UTF-16, but makes UTF-8 the universal interoperability baseline. See [RFC 2277](https://www.rfc-editor.org/rfc/rfc2277.html).

**[Standard]** RFC 5198 defines a UTF-8, NFC-oriented “Net-Unicode” profile for network interchange. See [RFC 5198](https://www.rfc-editor.org/rfc/rfc5198.html).

**[Registry]** IANA retains registrations for `ISO-10646-UCS-2`, `UTF-16`, `UTF-16BE`, and `UTF-16LE`. Registration does not imply recommendation. See the [IANA Character Sets registry](https://www.iana.org/assignments/character-sets).

### The web’s drift to UTF-8

**[Measured modern source]** W3Techs reported UTF-8 at approximately 98.9–99.0% of sites in its mid-to-late-2026 series. Its figures concern detected or declared website encodings within its sampling methodology, not all stored text worldwide. See [W3Techs UTF-8 statistics](https://w3techs.com/technologies/details/en-utf8) and [historical trends](https://w3techs.com/technologies/history_overview/character_encoding).

**[Historical reconstruction]** UTF-8 won Web interchange because it:

- preserves ASCII bytes;
- has no byte-order question;
- is compact for ASCII-heavy markup and source code;
- fits byte-oriented C, Unix, URLs, and Internet protocols;
- can recover character boundaries from its lead/continuation structure;
- became mandatory or strongly preferred in standards.

This did not remove UTF-16 from browser engines: ECMAScript’s observable string abstraction remains 16-bit even where engines internally compress Latin-1 strings.

### Present Windows direction

**[Platform documentation]** Windows remains natively UTF-16 across core `W` APIs. Since Windows 10 version 1903, applications can opt into UTF-8 as their active process code page. Microsoft recommends UTF-8 for cross-platform compatibility while documenting conversion at Win32 boundaries. See [Use UTF-8 code pages in Windows apps](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/use-utf8-code-page).

### What survives

UTF-16’s strongest surviving domains are:

- native Windows API strings and many Windows filesystem interfaces;
- Java strings and `char`;
- .NET strings and `Char`;
- ECMAScript’s observable string model;
- Qt’s `QString`;
- many Objective-C/Cocoa and Core Foundation APIs historically centered on 16-bit units;
- ICU’s `UChar` APIs;
- databases, office formats, and application file formats that chose “wide Unicode.”

UCS-2 survives mostly as:

- old documentation saying “Unicode character” when it means a 16-bit unit;
- database type names;
- network or library charset aliases;
- BMP-only implementations;
- filenames or APIs that permit arbitrary 16-bit values;
- bugs that split surrogate pairs.

---

## The legacy of the 16-bit assumption

### “Character” length

**[Standard/platform fact]** Java `String.length()`, JavaScript `.length`, .NET `String.Length`, Windows buffer counts, and many Qt methods count 16-bit units. For `😀`, the answer is two.

**[Modern critique]** This is often described as UTF-16 “breaking string length.” More precisely, the old API contract exposes code units, while programmers frequently expect user-perceived characters.

Even code-point counting is not user-character counting:

| Text | UTF-16 units | Scalar values | Grapheme clusters |
|---|---:|---:|---:|
| `A` | 1 | 1 | 1 |
| `😀` | 2 | 1 | 1 |
| `é` | 2 | 2 | 1 |
| `🇺🇳` | 4 | 2 | 1 |
| `👨‍👩‍👧‍👦` | 11 | 7 | 1 |

**[Standard]** Grapheme boundaries are specified separately by Unicode Standard Annex #29. No UTF can make all human-perceived characters fixed-width because combining marks, joiners, flags, and script-specific sequences exist independently of encoding width.

### Ill-formed internal strings

**[Platform documentation]** ECMAScript and .NET can contain lone surrogates. Windows filenames and APIs may preserve arbitrary 16-bit sequences. Strict conversion to UTF-8 cannot map those surrogate values as Unicode scalar values.

**[Modern engineering practice]** Systems sometimes use replacement, reject the name, or adopt a lossless non-standard escape such as surrogate-pass or WTF-8. Such representations solve round-trip engineering problems but are not conformant UTF-8 interchange.

### Compatibility encodings

**[Standard]** CESU-8 encodes each UTF-16 code unit separately in an eight-bit form, so a supplementary scalar becomes two three-byte sequences rather than one four-byte UTF-8 sequence. It was standardized as a compatibility scheme in UTR #26, not as UTF-8. See [UTR #26](https://www.unicode.org/reports/tr26/).

**[Modern reconstruction]** CESU-8 and WTF-8 exist largely because 16-bit APIs can contain surrogate-based structures that do not map cleanly to scalar-value UTF-8.

---

## The other scripts

UTF-16 does not itself “handle” script behavior. It represents Unicode code points. Unicode character properties, shaping engines, fonts, input methods, collation, normalization, and bidirectional layout do the remaining work.

### Cyrillic and Greek

**[Standard]** The BMP includes modern Greek, Coptic, Cyrillic, and extensive historical additions. UTF-16 represents most of these in one code unit. Accented text may use precomposed characters or combining sequences.

**[Historical context]** Before Unicode, ISO/IEC 8859-5, Windows-1251, CP866, Macintosh Cyrillic, KOI7, and KOI8 variants competed. Greek likewise had ISO 8859-7, ELOT-derived systems, DOS and Windows pages.

**[Folklore with real structural basis]** KOI8-R was deliberately arranged so that clearing the high bit of Cyrillic text produced a partly intelligible Latin transliteration-like result. That useful degradation property belongs to KOI8, not UTF-16.

### Hebrew

**[Standard]** Hebrew is encoded in logical order. Consonants, punctuation, and combining points occupy BMP positions. The Unicode Bidirectional Algorithm reorders right-to-left text for display while preserving logical storage. Hebrew’s five final letters are separately encoded because they are orthographic character distinctions rather than contextual glyph selection. See [Unicode Chapter 9](https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-9/) and [UAX #9](https://www.unicode.org/reports/tr9/).

**[Historical context]** ISO 8859-8 and vendor Hebrew code pages were small repertoires and varied between visual-order and logical-order practice. Unicode’s logical-order model improved interoperable editing but demanded bidi-aware rendering.

### Arabic

**[Standard]** Arabic letters are generally encoded by semantic identity, not as four separate isolated/initial/medial/final forms. A shaping engine selects contextual glyphs. Arabic is stored in logical order and rendered with bidi processing.

**[Compatibility fact]** Arabic Presentation Forms remain in Unicode chiefly for round-trip compatibility with older standards. They are not the preferred model for ordinary text.

**[Historical context]** ASMO 449, ECMA-114, ISO 8859-6, DOS/Windows Arabic code pages, and presentation-form encodings supplied earlier partial solutions.

### Indic scripts

**[Standard]** Devanagari and related scripts encode consonants, dependent vowels, viramas, signs, and combining marks. Rendering may reorder glyphs, form conjuncts, suppress inherent vowels, and select contextual shapes. One displayed syllable can therefore contain several code points and UTF-16 units.

**[Important distinction]** A BMP Indic cluster may use only single code-unit scalars and still defeat “one unit equals one visible character.” Surrogates are not the only source of string-complexity.

**[Historical context]** India’s ISCII shared positions across multiple scripts using script selection. Unicode instead allocated distinct script blocks while preserving related structural principles.

### Chinese, Japanese, and Korean

**[Standard]** BMP UCS-2 originally accommodated a large unified CJK repertoire, kana, bopomofo, Hangul, punctuation, and compatibility forms. It did not contain all rare or historical ideographs. Most later CJK extensions occupy supplementary planes and therefore require UTF-16 surrogate pairs.

Unicode 17.0 counts 102,998 Han characters under its detailed counting method. The majority of CJK Extension B and subsequent extensions are supplementary. See the [Unicode 17 character counts](https://www.unicode.org/versions/stats/charcountv17_0.html).

**[Historical context]**

- Japan: JIS X 0201, JIS X 0208, JIS X 0212, Shift_JIS, EUC-JP, ISO-2022-JP.
- Mainland China: GB 2312, GBK, GB 18030.
- Taiwan/Hong Kong: Big5 and extensions.
- Korea: KS C 5601/KS X 1001, EUC-KR, Johab, vendor unified-Hangul pages.

**[Standard]** GB 18030 supplies a national mapping capable of representing the Unicode repertoire through one-, two-, and four-byte sequences. It is not UTF-16 but is a major national compatibility and conformance layer.

### Emoji

**[Standard history]** Japanese mobile carriers used incompatible vendor extensions to Shift_JIS and ISO-2022-JP. A 2007 working proposal and a 2009 consolidated proposal mapped the carrier repertoires into Unicode. The latter requested 674 new characters; the union involved 722 carrier symbols, some already encoded. See [UTS #51](https://www.unicode.org/reports/tr51/) and the [2009 emoji proposal](https://www.unicode.org/L2/L2009/09025r2-emoji.pdf).

**[Encoding consequence]** Most emoji are supplementary and take surrogate pairs in UTF-16. Modifiers, variation selectors, regional indicators, keycap components, tag characters, and zero-width joiners create longer sequences.

**[Political fact]** The Consortium standardizes abstract characters and recommended sequences, while vendors design the colored images. Nevertheless, deciding what is encodable and which sequences receive standardized treatment has cultural consequences.

---

## People and institutions

### Directly connected to Unicode and UTF-16

- **Joseph D. Becker — [Document]:** Xerox engineer; coined “Unicode”; author of *Unicode 88*; co-originator of the architecture.
- **Lee Collins — [Document/participant testimony]:** Xerox and Apple engineer; early repertoire database and Han-unification work; Unicode technical vice-president in its early institutional period.
- **Mark Davis — [Document]:** Apple engineer and co-founder; later long-serving Consortium president; project editor of the 1994 ISO UTF-16 amendment proposal.
- **Dave Opstad — [Participant recollection]:** Xerox engineer whose XCCS experience was cited in favor of fixed-width character representation.
- **Ed Hart — [Document]:** Author of the June 3, 1991 “10646M” merger proposal.
- **Kenneth Whistler — [Document/participant recollection]:** Unicode technical director/editor and historian of the ISO/Unicode merger and surrogate chronology.
- **Joan Aliprand — [Document]:** Standards editor and participant in early Unicode and ISO work.
- **Asmus Freytag — [Document]:** Early organizational participant, Unicode editor, and contributor to technical guidance.
- **Paul Hoffman and François Yergeau — [Standard]:** Authors of RFC 2781.
- **Mike Kernaghan and Bill English — [Official history]:** Organizers of the early Consortium’s business structure.

### Intellectual and technical predecessors

- **Émile Baudot:** Five-bit telegraph code.
- **Donald Murray:** Modified teleprinter alphabet and operational conventions.
- **Herman Hollerith:** Punched-card tabulation system and card-code ancestry.
- **Bob Bemer:** Major ASCII advocate and contributor to ASCII’s repertoire and controls.
- **Charles E. Mackenzie:** IBM engineer and historian whose 1980 book reconstructs ASCII, EBCDIC, PTTC, card codes, and standards politics.

**[Finding: scope]** Baudot, Murray, Hollerith, Bemer, and Mackenzie did not design UCS-2 or UTF-16. They belong to the lineage of constraints—shift states, card compatibility, repertoire size, control functions, and interchange politics—that Unicode attempted to supersede.

### Related but not UTF-16 designers

- **Ken Thompson and Rob Pike:** Designed UTF-8’s immediate predecessor/FSS-UTF form in 1992.
- **Dave Prosser:** Proposed an earlier file-system-safe transformation.
- **Murray Sargent and other Microsoft text engineers:** Important in later Unicode-rich text and platform implementation, but not established here as originators of UTF-16.
- **Unicode Consortium members and ISO/IEC JTC 1/SC 2/WG 2 delegates:** Collectively maintain repertoire synchronization.

### Institutions

- **ASA/ANSI X3.4:** ASCII standardization; ancestral, not a UTF-16 committee.
- **ECMA:** ECMA-6/ISO 646 and later character-set/control standards; part of the interoperability lineage.
- **ISO/IEC JTC 1/SC 2/WG 2:** ISO/IEC 10646 repertoire and architecture.
- **Unicode Consortium/UTC:** Unicode properties, algorithms, repertoire decisions, and synchronization with WG2.
- **Xerox:** XCCS, Star, and Becker/Collins.
- **Apple:** Early Unicode prototypes, Collins and Davis, TrueType integration.
- **Microsoft:** Windows NT deployment and later Consortium participation.
- **Sun:** Java’s 16-bit `char` platform.
- **IBM:** EBCDIC, ISO participation, ICU, and enterprise Unicode implementation.
- **IETF:** Charset policy, MIME labels, RFC 2781, UTF-8 network preference.
- **W3C/WHATWG:** Web encoding rules and UTF-8 mandate.

---

## Culture

### “Plain text”

**[Standard design principle]** Unicode presents itself as a standard for plain text: abstract characters, logical order, and standard properties rather than font glyphs or page layout. See [Unicode Chapter 2](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-2/).

**[Modern critique]** Unicode plain text is richer than ASCII’s folk concept of plain text. Combining marks, directional controls, variation selectors, joiners, tags, and normalization make appearance and identity depend on algorithms and context.

**[Modern counterargument]** These complexities already exist in writing systems. Encoding them makes them interoperable rather than inventing them.

### Mojibake

**[Documented technical phenomenon]** Mojibake results when bytes are decoded under the wrong character encoding or repeatedly encoded/decoded. UTF-16 produces distinctive forms:

- UTF-16LE ASCII read as Latin-1 appears with NULs between letters;
- UTF-8 bytes read as Windows-1252 produce strings such as `â‚¬` for `€`;
- a BOM displayed as content can appear as `ï»¿` when UTF-8 BOM bytes are decoded as Windows-1252.

**[Modern cultural use]** Glitch artists, games, memes, and digital literature sometimes use mojibake deliberately to signal corruption, machine mediation, alienness, or damaged archives. This aesthetic is a modern reuse of interoperability failure, not a design feature.

### ASCII art and the demoscene

**[Historical reconstruction]** ASCII and code-page art depended on predictable monospace glyph grids, including vendor block characters. UTF-16 did not create a comparable art form; it mainly allowed such text to coexist with a far larger repertoire.

**[Cultural continuity]** The demoscene’s CP437 and Amiga character-art traditions survive in Unicode mapping and fonts. Mapping the bytes to Unicode preserves abstract symbols, but not automatically the original metrics, palette, raster glyphs, or terminal behavior.

### Emoji voting and public visibility

**[Standard/process fact]** Anyone can submit an emoji proposal, but acceptance uses published factors including compatibility, expected use, distinctiveness, completeness, and avoidance of overly specific or transient images. The Consortium now accepts fewer proposals and no longer accepts new flag proposals. See the [emoji proposal guidelines](https://www.unicode.org/emoji/proposals.html).

**[Modern political interpretation]** Headlines describe Unicode as an “emoji government” or “emoji overlord.” That captures the social visibility of repertoire decisions but obscures that UTC and WG2 encode characters, while Apple, Google, Microsoft, Samsung, and font makers control visible artwork.

### Unicode as a political institution

**[Documented institutional fact]** Encoding proposals require documentary evidence, representative glyphs, character identity, user-community information, and mapping or collation data. The process is jointly shaped by a nonprofit industry consortium and an international standards committee with national delegations.

**[Scholarly interpretation]** Communities with technical expertise, funding, digitized sources, national standards bodies, or corporate need can prepare proposals more readily. Encoding order therefore reflects not only linguistic antiquity or population but also documentation, advocacy, technical readiness, market pressure, and institutional access.

**[Countervailing fact]** The Consortium’s Script Encoding Initiative and related grants have supported minority and historic scripts that lack large commercial sponsors. The repertoire contains many scripts with small modern user bases.

---

## Controversies and disputes

### Was 16 bits a blunder?

**[Modern argument: prosecution]**

- The “one character = one 16-bit value” promise became false within five years.
- Surrogate handling burdened every legacy API.
- Supplementary characters receive second-class treatment in indexing, regular expressions, truncation, and UI limits.
- UTF-16 is variable-width but lacks UTF-8’s ASCII compatibility.
- For ASCII-heavy data it commonly consumes twice the space.
- Byte serialization requires endian metadata.

**[Modern argument: defense]**

- In 1988–1991, a fixed 16-bit representation dramatically simplified multilingual systems compared with stateful legacy encodings.
- It enabled early Unicode deployment in Windows NT and Java.
- The surrogate extension preserved existing BMP strings and ABI layouts.
- Many heavily used non-Latin scripts require two bytes per scalar in UTF-16 versus three in UTF-8.
- Neither UTF-8 nor UTF-32 makes grapheme operations constant-width.

**[Reconstruction]** The fairest conclusion is that 16 bits was an effective adoption strategy with long-lived compatibility costs. Calling it merely foolish ignores contemporary constraints; calling it fully adequate ignores the very existence of UTF-16.

### “UTF-16 considered harmful”

**[Modern argument]** The UTF-8 Everywhere manifesto and allied essays argue that new cross-platform software should use UTF-8 internally and convert only at unavoidable UTF-16 interfaces. Their principal claims are ASCII compatibility, one interchange representation, reduced conversion, no BOM requirement, easier Unix/C integration, and fewer accidental code-unit assumptions.

**[Modern counterargument]** Existing Windows, Java, .NET, Qt, and browser APIs cannot be redesigned without major compatibility cost. UTF-16 is efficient for some language distributions, and correct Unicode software already needs segmentation and normalization independent of encoding.

**[Evidence limitation]** “UTF-16 considered harmful” is a rhetorical family of modern engineering arguments, not a standards finding and not a measured proof that UTF-16 is always slower or larger.

### Han unification

**[Disputed]** Critics allege that Unicode conflates culturally distinct Japanese, Chinese, Korean, and Vietnamese forms, privileges certain national standards, or makes faithful historical typography impossible.

**[Standard response]** Unicode encodes abstract characters rather than glyphs, applies source-separation rules, and provides fonts, locale selection, standardized variation sequences, compatibility characters, and sometimes later disunification to preserve distinctions.

**[Evidence assessment]**

- It is documented that significant unification occurred.
- It is documented that regional glyph forms differ.
- It is documented that objections arose, particularly around Japanese scholarly and name usage.
- It is false that all CJK ideographs with similar meanings share one code point.
- It is false that selecting a Japanese-aware font solves every textual-identity problem.
- Claims that American and European votes simply “forced Chinese characters on Japan” require examination of specific WG2 ballots; popular summaries are insufficient.

### Tibetan

**[Documented chronology]** Tibetan appeared in Unicode 1.0, was removed during alignment for Unicode 1.1/ISO 10646, and was reintroduced in a different encoding in Unicode 2.0. Kenneth Whistler’s dated historical answer records this sequence.

**[Controversy]** Competing views concerned whether Tibetan should be modeled through character sequences and shaping or through larger precomposed stacks. The present model encodes components and expects rendering behavior.

**[Evidence limitation]** The public summary establishes removal and re-addition but does not substitute for a full dossier of Tibetan national-body submissions and UTC/WG2 minutes. Those records would be required to allocate individual responsibility for the dispute.

### Korean encoding disputes

**[Documented context]** Early Unicode work inherited disagreement between encoding precomposed Hangul syllables and algorithmic jamo composition. The modern standard contains 11,172 precomposed Hangul syllables plus conjoining jamo.

**[Historical consequence]** Reallocation of Hangul in early Unicode created one of the standard’s notable pre-stability incompatibilities. Later stability policies were strengthened partly because changing assigned positions is costly.

### Emoji and corporate power

**[Documented origin]** The first mass emoji repertoire entered Unicode primarily for round-trip compatibility with Japanese carrier encodings, not because a committee set out to invent pictorial speech.

**[Modern controversy]** Because large platform vendors are influential Consortium members and control deployment, critics question whether corporate interests receive disproportionate influence. The Consortium responds with public proposal criteria and open submissions.

**[Balanced finding]** The formal process is public in important respects, but not every deliberation, rejected idea, or informal negotiation has a complete public transcript. Absence of public minutes should not be filled with invented motives.

### BOM disputes

**[Standard]** BOM use is protocol-dependent. It is useful for untyped UTF-16 files, prohibited as a signature in explicitly labeled UTF-16BE/LE streams, and usually unnecessary in internally typed strings.

**[Modern dispute]** Some programs require it, others display it, and concatenation can move it into content. The dispute is not resolvable by declaring BOM universally good or bad; the correct answer depends on external labeling and protocol.

### Security

#### Lone surrogates

**[Standard/security]** Different components may disagree over accepting, replacing, preserving, or rejecting lone surrogates. An attacker can exploit mismatched interpretations across validators, filesystems, URLs, or serializers.

#### Homoglyphs

**[Standard/security]** Latin `a`, Cyrillic `а`, and Greek-like forms may look alike while remaining distinct code points. UTS #39 defines confusable-detection data and restricted identifier profiles. See [UTS #39](https://www.unicode.org/reports/tr39/).

**[Important distinction]** Homoglyph attacks are Unicode repertoire and rendering issues, not specifically UTF-16 issues. The same spoof can be represented in UTF-8.

#### Bidirectional controls

**[Standard/security]** Bidi overrides and isolates are necessary for real right-to-left text but can make displayed source differ from logical token order. Unicode’s source-code guidance recommends explicit handling. See [UTS #55](https://www.unicode.org/reports/tr55/).

#### Overlong UTF-8

**[Historical security comparison]** Early UTF-8 specifications and decoders permitted or ambiguously treated non-shortest forms, allowing filters and downstream components to see different characters. RFC 3629 and modern Unicode require shortest-form UTF-8. UTF-16 does not have overlong scalar encodings, though CESU-8 has sometimes been mistakenly accepted as UTF-8. See [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html).

#### Normalization

**[Security]** Canonically equivalent but byte-distinct names can evade naïve matching. Security-sensitive identifiers need a defined normalization and comparison profile. UTF-16 alone does not solve this.

#### Replacement policy

**[Security]** A decoder that consumes too much input when replacing an error can erase adjacent syntax. Unicode security guidance recommends preserving maximal valid subsequences and treating malformed input consistently. See [UTR #36](https://www.unicode.org/reports/tr36/).

### “The placemat” and UTF-16

**[Participant recollection]** Rob Pike recalled that Ken Thompson sketched the UTF-8 design on a placemat during dinner in September 1992, then implemented it immediately. Pike later published archived email evidence for the design chronology.

**[Finding: scope]** This is a UTF-8 origin story, not a UTF-16 story. No evidence found connects Thompson’s placemat to surrogates, UCS-2, or WG2 N970.

**[Evidence qualification]** The placemat itself was not preserved. Pike explicitly wished it had been. The event has one principal published eyewitness, supported by contemporary follow-up email and code rather than the physical artifact. Treating the surviving placemat as a museum object is folklore.

### IBM’s “unused ASCII bit”

**[Folklore/finding: absence]** Stories sometimes claim IBM defended EBCDIC or eight-bit storage because ASCII left an unused high bit. The general context—ASCII’s seven-bit width, parity use, System/360’s eight-bit byte, and EBCDIC’s 256 patterns—is documented by Mackenzie. No primary source found in this pass establishes a single decisive “unused ASCII bit” episode that caused UCS-2 or UTF-16.

### Bob Bemer and Unicode

**[Finding: scope]** Bemer’s work on ASCII, ESC, control functions, and international interchange shaped the environment Unicode inherited. No primary evidence found that he designed UCS-2, surrogate pairs, UTF-16, or the BOM. Claims extending his ASCII role into UTF-16 authorship should be rejected absent documents.

---

## Open questions

1. **The complete documentary path from WG2 N970 to final Amendment 1.**  
   The project editor and date are established, but a complete reconstruction should compare N970, national comments, dispositions, ballots, final amendment text, and UTC minutes.

2. **Who first proposed the exact 10+10-bit surrogate arithmetic?**  
   Mark Davis’s editorship is documented. Editorship alone does not prove sole invention. Publicly accessible drafts and meeting minutes should be checked before assigning exclusive credit.

3. **The earliest implementation of surrogate pairs.**  
   Unicode 2.0 establishes publication, not first experimental or shipping implementation. Candidate Microsoft, Java, ICU, and Plan 9-era libraries require dated source or release evidence.

4. **Exactly when each Windows component became surrogate-aware.**  
   Windows NT 3.1 clearly shipped a 16-bit Unicode API; “Windows moved from UCS-2 to UTF-16 in Windows 2000” is widespread but component-dependent. Kernel objects, NTFS, GDI, Uniscribe, fonts, collation, and conversion functions may have different dates.

5. **JavaScript’s direct design rationale.**  
   Current ECMAScript specifies 16-bit sequences, but a full historical proof should inspect the first Mocha/LiveScript source, Netscape design notes, and ECMA-262 first-edition minutes.

6. **Early BOM authorship.**  
   Unicode 1.x and ISO Annex F establish the convention’s early standardization, but this research did not locate a decisive memo identifying its individual inventor.

7. **Han-unification ballot narratives.**  
   Popular retellings often compress multiple ISO meetings, national positions, technical criteria, and later objections into one political vote. The primary national comments and WG2 resolutions should be published and compared.

8. **Tibetan’s removal and redesign.**  
   The high-level chronology is secure; attribution of arguments requires Tibetan proposal papers, national-body comments, and committee minutes.

9. **Private deliberation in emoji selection.**  
   Proposals and published decisions are available, but not every informal discussion or rejected suggestion has a complete public record.

10. **Historical Web percentages.**  
    W3Techs supplies a consistent series, but it is one measurement methodology. A rigorous adoption history should compare HTTP headers, HTML declarations, browser telemetry, Common Crawl, Google indexing studies, and static-file scans.

---

## Sources

### Core standards and Unicode archives

- [The Unicode Standard, Version 17.0.0](https://www.unicode.org/versions/Unicode17.0.0/UnicodeStandard-17.0.pdf)
- [Unicode 17.0 release page](https://www.unicode.org/versions/Unicode17.0.0/)
- [Unicode 17.0 character counts](https://www.unicode.org/versions/stats/charcountv17_0.html)
- [Unicode 16.0 core specification](https://www.unicode.org/versions/Unicode16.0.0/UnicodeStandard-16.0.pdf)
- [Unicode Chapter 2: General Structure](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-2/)
- [Unicode Chapter 9: Middle Eastern Scripts](https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-9/)
- [Unicode Chapter 18: East Asia](https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/)
- [Unicode Chapter 23: Special Areas and Format Characters](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-23/)
- [Unicode Appendix C: Relationship to ISO/IEC 10646](https://unicode.org/versions/Unicode17.0.0/core-spec/appendix-c/)
- [Unicode Appendix D: Version History](https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-d/)
- [Unicode Appendix E: Han Unification History](https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/)
- [Unicode 1.0 archive](https://www.unicode.org/versions/Unicode1.0.0/)
- [Unicode 1.1 archive](https://www.unicode.org/versions/Unicode1.1.0/)
- [Unicode release and publication dates](https://www.unicode.org/history/publicationdates.html)
- [Unicode UTF-8, UTF-16, UTF-32 and BOM FAQ](https://www.unicode.org/faq/utf_bom.html)
- [Unicode Basic Questions FAQ](https://www.unicode.org/faq/basic_q.html)
- [Unicode and ISO 10646 FAQ](https://www.unicode.org/faq/unicode_iso.html)
- [Unicode Private-Use and Noncharacter FAQ](https://unicode.org/faq/private_use.html)
- [UTR #17: Unicode Character Encoding Model](https://www.unicode.org/reports/tr17/)
- [UTR #26: Compatibility Encoding Scheme for UTF-16](https://www.unicode.org/reports/tr26/)
- [UTR #36: Unicode Security Considerations](https://www.unicode.org/reports/tr36/)
- [UTS #39: Unicode Security Mechanisms](https://www.unicode.org/reports/tr39/)
- [UTS #51: Unicode Emoji](https://www.unicode.org/reports/tr51/)
- [UTS #55: Unicode Source Code Handling](https://www.unicode.org/reports/tr55/)
- [UAX #9: Unicode Bidirectional Algorithm](https://www.unicode.org/reports/tr9/)
- [UTN #26: On the Encoding of Latin, Greek, Cyrillic, and Han](https://www.unicode.org/notes/tn26/)
- [Unicode emoji proposal guidelines](https://www.unicode.org/emoji/proposals.html)
- [Unicode emoji proposal index](https://unicode.org/emoji/charts/emoji-proposals.html)
- [2009 proposal for encoding emoji](https://www.unicode.org/L2/L2009/09025r2-emoji.pdf)

### Origin and institutional history

- [Unicode 88, Joseph D. Becker, August 29, 1988](https://www.unicode.org/history/Unicode88.pdf)
- [Unicode Early Years](https://www.unicode.org/history/earlyyears.html)
- [Unicode History Corner](https://www.unicode.org/history/)
- [Unicode history summary](https://www.unicode.org/history/summary.html)
- [Unicode mailing-list answers on Unicode history](https://www.unicode.org/mail-arch/unicode-ml/y2002-m02/0110.html)
- [WG2 historical document register](https://www.unicode.org/L2/Historical/wg2-n1300-doc-register.pdf)
- [ISO/IEC 10646:2020 catalogue record](https://www.iso.org/standard/76835.html)

### RFCs and Internet registries

- [RFC 20: ASCII format for network interchange](https://www.rfc-editor.org/rfc/rfc20.html)
- [RFC 1345: Character Mnemonics and Character Sets](https://www.rfc-editor.org/rfc/rfc1345.html)
- [RFC 2044: UTF-8 transformation format](https://www.rfc-editor.org/rfc/rfc2044.html)
- [RFC 2277: IETF Policy on Character Sets and Languages](https://www.rfc-editor.org/rfc/rfc2277.html)
- [RFC 2279: UTF-8, historical specification](https://www.rfc-editor.org/rfc/rfc2279.html)
- [RFC 2781: UTF-16, an encoding of ISO 10646](https://www.rfc-editor.org/rfc/rfc2781.html)
- [RFC 3629: UTF-8, current restricted form](https://www.rfc-editor.org/rfc/rfc3629.html)
- [RFC 5198: Unicode Format for Network Interchange](https://www.rfc-editor.org/rfc/rfc5198.html)
- [RFC 6365: Internationalization terminology](https://www.rfc-editor.org/rfc/rfc6365.html)
- [IANA Character Sets registry](https://www.iana.org/assignments/character-sets)
- [IANA individual charset registrations](https://www.iana.org/assignments/charset-reg)

### Platform specifications and manuals

- [Helen Custer, *Inside Windows NT*, Microsoft Press, 1993](https://www.bitsavers.org/pdf/microsoft/windows_NT_3.1/Custer_Inside_Windows_NT_1993.pdf)
- [Microsoft: Working with Strings](https://learn.microsoft.com/en-us/windows/win32/learnwin32/working-with-strings)
- [Microsoft: Unicode in Win32](https://learn.microsoft.com/en-us/windows/win32/intl/unicode)
- [Microsoft: Surrogates and Supplementary Characters](https://learn.microsoft.com/en-us/windows/win32/intl/surrogates-and-supplementary-characters)
- [Microsoft: Character encoding in .NET](https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-encoding-introduction)
- [Microsoft: Use UTF-8 code pages in Windows apps](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/use-utf8-code-page)
- [Microsoft: Code Page Identifiers](https://learn.microsoft.com/en-us/windows/win32/intl/code-page-identifiers)
- [Oracle Java Character API](https://docs.oracle.com/en/java/javase/26/docs/api/java.base/java/lang/Character.html)
- [Oracle Java supplementary-character tutorial](https://docs.oracle.com/javase/tutorial/i18n/text/supplementaryChars.html)
- [Java Language Specification, lexical structure and Unicode history](https://docs.oracle.com/javase/specs/jls/se6/html/lexical.html)
- [ECMAScript specification](https://tc39.es/ecma262/)
- [ECMAScript 2022 String type](https://tc39.es/ecma262/2022/multipage/ecmascript-data-types-and-values.html)
- [MDN JavaScript String documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- [MDN UTF-16 glossary](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
- [Qt QString documentation](https://doc.qt.io/qt-6/qstring.html)
- [ICU Unicode Basics](https://unicode-org.github.io/icu/userguide/icu/unicode.html)

### Web adoption

- [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/)
- [WHATWG HTML Standard for developers](https://html.spec.whatwg.org/dev/semantics.html)
- [W3Techs UTF-8 usage](https://w3techs.com/technologies/details/en-utf8)
- [W3Techs historical character-encoding trends](https://w3techs.com/technologies/history_overview/character_encoding)

### Historical and archival works

- [Charles E. Mackenzie, *Coded Character Sets: History and Development*, 1980 — Open Library/Internet Archive record](https://openlibrary.org/books/OL4570655M/Coded_character_sets)
- [Charles E. Mackenzie, Google Books bibliographic record](https://books.google.com/books/about/Coded_Character_Sets.html?id=6-tQAAAAMAAJ)
- [Computer History Museum Oral Histories](https://computerhistory.org/oral-histories/)
- [Computer History Museum Software History Center](https://computerhistory.org/software-history-center/)
- [Bob Bemer’s archived website](https://web.archive.org/web/20150801005415/http://bobbemer.com/)
- [Plan 9 paper: “Hello World or Καλημέρα κόσμε or こんにちは 世界”](https://web.archive.org/web/20000917055036/http://plan9.bell-labs.com/sys/doc/utf.pdf)
- [Rob Pike UTF-8 history correspondence, preserved in translation with original email metadata](https://arthurchiao.art/blog/utf-8-history-zh/)
