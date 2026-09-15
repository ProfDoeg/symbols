# ISO 646 and the seven-bit national variants (the # $ @ [ \ ] wars): Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| Standard | ISO 646; current designation ISO/IEC 646:1991 |
| Title | *Information technology — ISO 7-bit coded character set for information interchange* |
| First international edition | ISO 646:1973, developed by ISO/TC 97 |
| Pre-standard forms | ECMA-6, first edition April 1965; second edition June 1967; ISO Recommendation R 646; CCITT International Alphabet No. 5 |
| Current edition | ISO/IEC 646:1991, third edition, published 16 December 1991 |
| Bit width | 7 bits: 128 bit combinations, normally stored in an 8-bit octet with the high bit zero |
| Repertoire | 33 control positions including DEL, SPACE, 26 uppercase and 26 lowercase Latin letters, ten digits, and punctuation/symbols; intended for Latin-script alphabets |
| National flexibility | Ten generally replaceable graphic positions, plus two restricted-choice positions—twelve variable positions in the usual account |
| International Reference Version | The 1973/1983 IRV used `¤` at 0x24 and, in the 1973 registration, overline at 0x7E; the 1991 IRV is effectively ASCII |
| Related standards | ANSI/ASA X3.4; ECMA-6; CCITT V.3 and ITU-T T.50; ISO/IEC 2022/ECMA-35; ISO 2375; ISO/IEC 8859; ISO/IEC 10646 |
| Status in 2026 | Formally current: ISO states that the 1991 edition was confirmed in 2020. Operationally legacy, but its ASCII-compatible invariant core is embedded in Internet protocols, programming languages, Unicode, and UTF-8. |

**Evidence label — documented standard:** ISO describes the current standard as a set of 128 control and graphic characters applicable to Latin-script alphabets. ECMA-6 describes the same 7-bit structure, its mandatory positions, national options, and code-extension facility. The ISO catalogue records the 1973 first edition and the current third edition. [ISO/IEC 646:1991 catalogue](https://www.iso.org/standard/4777.html), [ISO 646:1973 catalogue](https://www.iso.org/standard/2823.html), [ECMA-6 archive and editions](https://ecma-international.org/publications-and-standards/standards/ecma-6/)

The phrase “international ASCII” is a useful historical shorthand, not the formal name. ISO 646 was closely coordinated with American ASCII but was a framework containing an IRV and multiple national versions, not simply a renaming of every edition of ASCII.

---

## The code in detail

### 1. Bit structure

A character is represented by seven bits, conventionally `b7…b1`. ECMA-6 expresses positions as `x/y`:

- `x`, the column, is the value of bits `b7 b6 b5`, weighted 4, 2, 1.
- `y`, the row, is the value of bits `b4 b3 b2 b1`, weighted 8, 4, 2, 1.
- Thus position `5/12` means binary `1011100`, hexadecimal `5C`.

There are eight columns and sixteen rows. In modern hexadecimal notation:

- `00–1F`: C0 control characters.
- `20`: SPACE.
- `21–7E`: 94 graphic positions.
- `7F`: DELETE.
- An eighth storage or transmission bit could be zero, ignored, or used for parity depending on the surrounding standard. It was not part of the seven-bit character value.

**Evidence label — documented standard:** This organization appears explicitly in ECMA-6. [ECMA-6, sixth edition PDF](https://www.ecma-international.org/wp-content/uploads/ECMA-6_6th_edition_december_1991.pdf)

### 2. Complete 1991 International Reference Version

The table below is simultaneously the 1991 ISO 646 IRV and the familiar 7-bit ASCII table.

| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `00` | NUL | SOH | STX | ETX | EOT | ENQ | ACK | BEL | BS | HT | LF | VT | FF | CR | SO | SI |
| `10` | DLE | DC1 | DC2 | DC3 | DC4 | NAK | SYN | ETB | CAN | EM | SUB | ESC | FS | GS | RS | US |
| `20` | SP | ! | " | # | $ | % | & | ' | ( | ) | * | + | , | - | . | / |
| `30` | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | : | ; | < | = | > | ? |
| `40` | @ | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
| `50` | P | Q | R | S | T | U | V | W | X | Y | Z | [ | `\` | ] | ^ | _ |
| `60` | ` | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o |
| `70` | p | q | r | s | t | u | v | w | x | y | z | { | \| | } | ~ | DEL |

### 3. Control characters

| Hex | Name | Original functional idea |
|---:|---|---|
| `00` | NUL | Idle/fill; no character |
| `01–03` | SOH, STX, ETX | Start of heading/text; end of text |
| `04` | EOT | End of transmission |
| `05–06` | ENQ, ACK | Enquiry and acknowledgement |
| `07` | BEL | Audible or visible attention signal |
| `08` | BS | Move printing position backward |
| `09` | HT | Horizontal tabulation |
| `0A` | LF | Line feed |
| `0B` | VT | Vertical tabulation |
| `0C` | FF | Form feed |
| `0D` | CR | Carriage return |
| `0E–0F` | SO, SI | Shift out/shift in |
| `10` | DLE | Data-link escape |
| `11–14` | DC1–DC4 | Device-control functions; DC1/DC3 became XON/XOFF |
| `15` | NAK | Negative acknowledgement |
| `16` | SYN | Synchronous-idle/synchronization |
| `17` | ETB | End of transmission block |
| `18–1A` | CAN, EM, SUB | Cancel, end of medium, substitute |
| `1B` | ESC | Introduce a control or code-extension sequence |
| `1C–1F` | FS, GS, RS, US | File, group, record, unit separators |
| `7F` | DEL | Erasure/deletion |

These meanings were designed for teleprinters, communications links, data blocks, and record-oriented media. Modern software retains only a subset with consistent meanings.

**Documented standard:** RFC 20 reproduces the ASCII names and says binary value defines relative sequence for interchange collation. It also cautions that the standard does not prescribe a typeface. [RFC 20](https://www.rfc-editor.org/rfc/rfc20.html)

### 4. Newline, space, NUL, and deletion

- **SPACE:** `0x20`, a graphic-set member but normally nonprinting. It advances the printing position.
- **NUL:** `0x00`, historically useful as fill or idle time. It does not mean end-of-string in ISO 646; that is a C-language convention.
- **Newline:** ISO 646 supplies CR and LF as separate controls. A line ending was not inherently one character across every system. Teleprinter practice commonly used CR followed by LF. Unix later used LF, classic Mac OS CR, and Internet text protocols standardized CRLF.
- **DELETE:** `0x7F`, all seven bits set. On punched paper tape, punching all remaining holes could obliterate a mistaken character. It is therefore at the end rather than among `00–1F`.

**Evidence labels:**

- **Documented standard/text:** RFC 20 specifies CR and LF separately. MIME later declares CRLF canonical for Internet text and says national ISO 646 variations are not US-ASCII. [RFC 20](https://www.rfc-editor.org/rfc/rfc20.html), [RFC 1341](https://www.rfc-editor.org/rfc/rfc1341.html)
- **Scholarly reconstruction:** The paper-tape explanation of DEL is supported by the physical medium and standard histories, including Mackenzie; it should not be inflated into the claim that every ASCII design decision followed paper-tape practice.
- **Modern misconception:** “ASCII newline is `0A`” describes Unix practice, not the full interchange standard.

### 5. Letters, case, and collation

Digits occupy `30–39`; uppercase letters `41–5A`; lowercase letters `61–7A`. The bit difference between corresponding ASCII letters is `0x20`: `A = 0x41`, `a = 0x61`.

This was convenient for case conversion, although blindly toggling bit `0x20` also transforms punctuation. Binary collation yields:

1. punctuation and digits,
2. uppercase letters,
3. more punctuation,
4. lowercase letters,
5. final punctuation.

Thus binary order is not natural-language collation. `Z` precedes `a`; accented letters in national variants fall at punctuation positions, not beside their base letters.

**Documented text:** RFC 20 §6.3 defines the relative sequence, if used for collation, by binary values. It does not claim that this is linguistically correct.

### 6. What ISO 646 can and cannot express

The invariant repertoire can express unaccented English and many machine-oriented identifiers. A chosen national version can add a handful of letters needed by one Latin orthography.

It cannot simultaneously encode:

- all accented Latin letters used across Europe;
- ordinary multilingual Latin text;
- Greek, Cyrillic, Hebrew, Arabic, or Indic alphabets in the base repertoire;
- Chinese, Japanese, or Korean writing;
- combining-mark sequences generally;
- mathematical and technical symbol inventories;
- emoji;
- script direction, shaping, normalization, language, font, or document structure.

Overstriking offered a limited analogue workaround: ISO 646:1973 permitted some accent-like graphics to combine with a base character using BACKSPACE. That was device behavior rather than a robust abstract-character model. Later ECMA-94/ISO 8859 expressly prohibited using controls such as BACKSPACE to represent composite characters.

### 7. The variable positions: ten, twelve, or thirteen?

The conventional twelve-position list is:

`23 24 40 5B 5C 5D 5E 60 7B 7C 7D 7E`

Their ASCII graphics are:

`# $ @ [ \ ] ^ ` { | } ~`

The distinction matters:

- `0x23` was restricted to `#` or `£`.
- `0x24` was restricted to `$` or the generic currency sign `¤`.
- Ten other positions were “national-use” options.
- Some actual registered sets went beyond the clean rule or exploited older options. Therefore tables sometimes speak of ten national-use positions, twelve variable positions, or show a larger comparison set.

**Documented standard:** ISO 646:1973 states that national standardization bodies control national-use allocations and permits positions `5/14`, `6/0`, and `7/14` to be reassigned when eight, nine, or ten positions are needed. [ISO 646:1973 scan](https://cdn.standards.iteh.ai/samples/2823/380b0375541d4a87baaaf782673762b1/ISO-646-1973.pdf)

**Finding:** The popular phrase “twelve characters left entirely free” is imprecise. Two were constrained choices.

### 8. Representative national versions

Only differing positions are shown. Values are hex.

| Version and registration | Replacements relative to ASCII |
|---|---|
| IRV 1973/1983, ISO-IR 2 | `24=¤`; registered older form also used `7E=overline` |
| United Kingdom, BS 4730, ISO-IR 4 | `23=£` |
| Sweden/Finland, SEN 850200-B, ISO-IR 10 | `24=¤`, `5B=Ä`, `5C=Ö`, `5D=Å`, `7B=ä`, `7C=ö`, `7D=å`, `7E=overline` |
| Sweden, SEN 850200-C, ISO-IR 11 | additionally `40=É`, `60=é`, and `5E/7E=Ü/ü` in the registered table |
| Japan Roman, JIS C 6220/JIS X 0201, ISO-IR 14 | `5C=¥`, `7E=overline` |
| Italy, ISO-IR 15 | `23=£`, `40=§`, `5B=°`, `5C=ç`, `5D=é`, `60=ù`, `7B=à`, `7C=ò`, `7D=è`, `7E=ì` |
| Spain, ISO-IR 17 | `23=£`, `40=§`, `5B=¡`, `5C=Ñ`, `5D=¿`, `7B=°`, `7C=ñ`, `7D=ç` |
| Germany, DIN 66003, ISO-IR 21 | `40=§`, `5B=Ä`, `5C=Ö`, `5D=Ü`, `7B=ä`, `7C=ö`, `7D=ü`, `7E=ß` |
| France, NF Z 62-010:1982, ISO-IR 69 | `23=£`, `40=à`, `5B=°`, `5C=ç`, `5D=§`, `60=µ`, `7B=é`, `7C=ù`, `7D=è`, `7E=¨` |
| Norway, NS 4551-1, ISO-IR 60 | `5B=Æ`, `5C=Ø`, `5D=Å`, `7B=æ`, `7C=ø`, `7D=å`, `7E=macron` |
| China, GB 1988-80/89, ISO-IR 57 | `24=¥/yuan sign`, `7E=overline` |

**Documented text:** RFC 1345 transcribes the ECMA registry tables and aliases, including DIN 66003, NF Z 62-010, the Nordic standards, JIS Roman, Italy, Spain, and ASCII. [RFC 1345 character-set tables](https://www.rfc-editor.org/rfc/rfc1345.html)

**Qualification:** Glyph identity for `¥` versus a Chinese yuan sign and for overline versus macron is partly dependent on the historical standard’s glyph conventions. Unicode character names should not simply be projected backward.

### 9. Escape and shift mechanisms

ISO 646 itself reserves:

- `ESC` at `0x1B`;
- `SO` at `0x0E`;
- `SI` at `0x0F`.

The systematic machinery is ISO 2022/ECMA-35:

- coded sets can be designated into registers G0, G1, G2, and G3 by escape sequences;
- locking shifts select a set for subsequent characters;
- single shifts select G2 or G3 for one character;
- in seven-bit operation, the active graphic set is invoked into `0x21–0x7E`;
- an escape sequence can designate, for example, ASCII with `ESC ( B`.

Registered ISO 646 sets have designators. Examples from RFC 1345 include:

- ASCII/ISO-IR 6: `ESC ( B` = `1B 28 42`;
- German ISO-IR 21: `ESC ( K` = `1B 28 4B`;
- French ISO-IR 69: `ESC ( f` = `1B 28 66`;
- JIS Roman ISO-IR 14: `ESC ( J` = `1B 28 4A`.

ISO-2022-JP illustrates the larger scheme: `ESC $ B` selects the two-byte JIS X 0208 set; `ESC ( B` returns to ASCII.

**Documented standards:** [ECMA-35 PDF](https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf), [ISO/IEC 2022 catalogue text](https://www.iso.org/obp/ui#iso:std:iso-iec:2022:ed-4:v1:en), [RFC 1468](https://www.rfc-editor.org/rfc/rfc1468.html)

### 10. Error detection, synchronization, and recovery

Bare ISO 646 has no intrinsic framing or checksum:

- every seven-bit pattern is legal;
- a flipped bit normally turns one legal character into another;
- parity, block checks, retransmission, or framing belong to the communication system;
- in fixed seven-bit or eight-bit storage, a reader that loses one whole character can resume on the next externally known character boundary;
- in an unframed serial bitstream, the code itself cannot recover bit alignment.

Stateful ISO 2022 is more fragile. Corruption of an escape designation or shift can make all following bytes display under the wrong set. Recovery requires:

- a valid resetting designation such as `ESC ( B`;
- a line or protocol boundary whose profile specifies state reset;
- out-of-band knowledge.

RFC 1468 deliberately limits the damage in ISO-2022-JP by requiring a return to ASCII before a line-ending and at the end of text.

This differs sharply from UTF-8. UTF-8 continuation bytes have a distinctive `10xxxxxx` form, so a decoder can generally re-establish sequence boundaries after at most a few bytes. ISO 646’s fixed width is simple once byte boundaries exist, but provides no bit-level self-synchronization signature.

### 11. Worked examples

#### Example A: `München`

In German DIN 66003:

| Character | Code | Bits |
|---|---:|---|
| M | `4D` | `1001101` |
| ü | `7D` | `1111101` |
| n | `6E` | `1101110` |
| c | `63` | `1100011` |
| h | `68` | `1101000` |
| e | `65` | `1100101` |
| n | `6E` | `1101110` |

Bytes: `4D 7D 6E 63 68 65 6E`

If misread as ASCII, the same bytes display as:

`M}nchen`

In ISO-8859-1:

`4D FC 6E 63 68 65 6E`

In UTF-8:

`4D C3 BC 6E 63 68 65 6E`

The national version saves one byte for `ü`, but destroys the ASCII meaning of `}` at the same value.

#### Example B: `KÖLN`

German DIN 66003:

`K 4B`, `Ö 5C`, `L 4C`, `N 4E`

Bytes: `4B 5C 4C 4E`

Misread as ASCII:

`K\LN`

UTF-8:

`4B C3 96 4C 4E`

#### Example C: Japanese price text `¥100`

JIS X 0201 Roman:

| Character | Code |
|---|---:|
| ¥ | `5C` |
| 1 | `31` |
| 0 | `30` |
| 0 | `30` |

Bytes: `5C 31 30 30`

Read as ASCII, it becomes `\100`. In UTF-8, the yen sign is `C2 A5`, followed by `31 30 30`.

This collision survives in Japanese fonts, terminals, Windows APIs, and source displays: an underlying U+005C REVERSE SOLIDUS may be drawn as a yen-shaped glyph. It does not follow that every visible yen sign in a Japanese path is encoded as U+00A5.

#### Example D: a C fragment

ASCII source:

```c
{ a[i] = '\n'; }
```

Hexadecimal:

```text
7B 20 61 5B 69 5D 20 3D 20 27 5C 6E 27 3B 20 7D
```

Displayed under German DIN 66003:

```text
ä aÄiÜ = 'Ön'; ü
```

This is the national-variant collision in concentrated form: braces, brackets, and backslash become letters.

ANSI/ISO C therefore defined trigraphs:

| Trigraph | Intended character |
|---|---|
| `??=` | `#` |
| `??/` | `\` |
| `??'` | `^` |
| `??(` | `[` |
| `??)` | `]` |
| `??!` | `|` |
| `??<` | `{` |
| `??>` | `}` |
| `??-` | `~` |

A portable spelling could therefore become:

```c
??< a??(i??) = '??/n'; ??>
```

**Documented committee rationale:** The C rationale says these source characters were absent from some ISO 646 repertoires and candidly makes no claim that trigraph-bearing programs are attractive. [ANSI C rationale copy](https://www.lysator.liu.se/c/rat/title.html)

**Folklore versus evidence:** The specimen `ä aÄiÜ = 'Ön'; ü` is widely repeated. It is technically accurate as a byte-for-byte display transformation, but evidence that programmers commonly wrote substantial C programs in that appearance is thin. More often, programmers selected an ASCII terminal mode, used vendor extensions, or endured awkward keyboard access. The code sample should be treated as demonstration, not usage statistics.

---

## Origins

### 1. Telegraph ancestry: Baudot and Murray

Émile Baudot’s 1870s five-unit telegraph code represented 32 bit patterns and used shift states to obtain letters and figures. Donald Murray’s early twentieth-century adaptation reorganized the code for keyboard and perforated-tape operation. The CCITT International Telegraph Alphabet No. 2 descended from this family.

These systems established:

- compact fixed-length binary character patterns;
- letter/figure shift states;
- teleprinter controls;
- the possibility that one pattern’s meaning depends on prior state.

ISO 646 replaced the five-bit scarcity with 128 combinations, allowing uppercase, lowercase, digits, punctuation, and controls without a normal letters/figures shift. SO, SI, and ESC nevertheless preserve the stateful communications lineage.

**Scholarly reconstruction:** Mackenzie’s 1980 history is the strongest synthetic treatment among the requested sources. It connects telegraph, punched-card, BCD, FIELDATA, ASCII, and EBCDIC developments without reducing ASCII to a single inventor. [Mackenzie catalogue and Internet Archive identifier](https://openlibrary.org/books/OL4570655M/Coded_character_sets)

### 2. Hollerith and punched-card ancestry

Herman Hollerith’s punched-card systems represented data by hole positions rather than a uniform binary character code. IBM’s card codes, BCD-derived sets, and printer arrangements later shaped expectations concerning:

- digit and letter zones;
- collating sequence;
- compatibility with installed card equipment;
- translation between external interchange and internal machine codes.

ASCII was therefore not designed on a blank slate. The committee had to reconcile telecommunications, paper tape, punched cards, programming-language punctuation, and computer input/output equipment.

### 3. The American standards process, 1960–1963

**Documented chronology:**

- ASA Sectional Committee X3 on Computers and Information Processing was formed in 1960.
- X3 first met on 4 August 1960.
- X3.2, Codes and Input-Output, first met on 4 October, chaired by I. C. Liggett of IBM.
- Work proceeded through X3.2 and working group X3.2.4.
- ASA X3.4-1963 was approved in June 1963 after substantial controversy.
- The 1963 table left many positions unassigned pending further work.
- The fuller 1967/1968 revisions assigned all 128 patterns and aligned the American code with ISO and CCITT work.

A contemporary federal chronology says the 1963 standard was approved “after considerable controversy” and that the revision followed two years of research and international deliberation. [US federal chronology preserved in CIA FOIA](https://www.cia.gov/readingroom/document/cia-rdp78-04723a000200020028-3)

### 4. Bob Bemer and the single-inventor problem

Robert W. Bemer was a major advocate and contributor. He worked at IBM and later UNIVAC, Bull, GE, and Honeywell. His retrospective accounts credit him with pushing:

- seven rather than six bits;
- lowercase;
- ESC;
- programming punctuation including backslash and braces;
- international coordination, notably with Hugh McGregor Ross.

**Participant recollection:** Bemer said the code was for a time called the “Bemer–Ross code” in Europe and described his advocacy for ESC and alphabet extension.

**Documented counterweight:** The IEEE Computer Society’s biography explicitly says Bemer “was not the inventor of ASCII”; a committee surveyed candidates and constructed a new code. [IEEE Computer Society biography](https://history.computer.org/pioneers/bemer.html)

**Finding:** “Father of ASCII” is an honorific popularized in biographies and obituaries, not an accurate statement of sole authorship. Surviving committee records support major contribution, not solitary invention.

### 5. Hugh McGregor Ross and European coordination

British engineer Hugh McGregor Ross participated in European and international work and acted as an important bridge between American proposals, ECMA, and ISO. Bemer’s recollection supplies the “Bemer–Ross” anecdote.

**Evidence status:** Ross’s influence is documented, but the colloquial name rests substantially on Bemer’s later testimony. It should not be presented as a formal contemporary title without a dated primary document bearing it.

### 6. Why seven bits?

Six bits allow only 64 combinations—barely enough for uppercase letters, digits, a small punctuation set, and controls. Seven bits allow 128. Contemporary hardware often carried a parity bit in an eight-bit transmission unit, making seven information bits a practical compromise.

The extra capacity supported lowercase and more controls while fitting telecommunication practice.

**Participant/technical reconstruction:** Bemer’s IEEE biography states that the eighth circuit bit was commonly a check or error bit.

**Controversy:** The phrase “eight-bit versus seven-bit war” compresses several different disputes:

1. seven data bits plus parity versus eight information bits;
2. compact interchange versus richer national repertoires;
3. ASCII versus IBM EBCDIC;
4. later 8-bit ISO and vendor code pages.

There was no single decisive meeting encompassing all four.

### 7. Lowercase

The 1963 standard did not yet assign the modern full lowercase block. Lowercase competed with demands for more control functions and with equipment whose printers had only capitals. By the 1967 revision, lowercase occupied `61–7A`.

**Documented fact:** The 1963 and 1967 tables differ materially.

**Participant recollection:** Bemer portrayed lowercase as something he vigorously defended.

**Caution:** Claims that one individual “invented lowercase ASCII” confuse advocacy, committee allocation, and pre-existing lowercase typewriter practice.

### 8. International development: ECMA, ISO, and CCITT

ECMA Technical Committee 1 worked on coded character sets from December 1960. ECMA-6 editions appeared in:

- April 1965;
- June 1967;
- July 1970;
- August 1973;
- March 1985;
- December 1991.

ISO/TC 97 developed ISO 646; CCITT standardized the related International Alphabet No. 5 as V.3, later T.50. A joint ISO/TC 97/SC2 and CCITT meeting in Paris in April 1966 coordinated remaining differences.

ISO 646:1973 became the first formal International Standard edition. It did not merely impose the American punctuation set: it preserved a common invariant core and permitted national alphabet extensions.

### 9. The currency-sign compromise

The early IRV placed `¤`, the generic CURRENCY SIGN, at `0x24`, where ASCII had `$`. National versions could choose the locally appropriate sign. The hope was that an abstract currency placeholder would avoid granting the dollar international privilege.

In practice:

- users needed specific currency symbols;
- equipment overwhelmingly supported the ASCII dollar;
- the generic sign was unfamiliar;
- the 1991 IRV adopted `$`, making IRV equivalent to ASCII at this point.

**Documented:** The 1973 standard permits the currency sign at `2/4`; RFC 1345 records `Cu` in the 1983 IRV and `$` in ASCII/1991 IRV.

**Interpretation:** Calling this a “defeat” for `¤` is reasonable historical interpretation, not language found in the standard.

---

## Adoption and decline

### 1. Early equipment and networks

ASCII appeared commercially in 1963 in the Bell System/AT&T TWX environment associated with the Teletype Model 33. Terminals, minicomputers, paper-tape equipment, and communications systems increasingly adopted it.

DEC systems and terminals became especially important vectors for ASCII-shaped terminal conventions, though DEC also developed National Replacement Character Sets that repeated the ISO 646 strategy at display time.

### 2. IBM and EBCDIC

IBM introduced EBCDIC for System/360 in 1964, retaining compatibility with IBM punched-card and BCD traditions. EBCDIC used eight bits but did not provide a single universal 256-character graphic repertoire: portions served controls, and many national/vendor code pages followed.

**Documented fact:** System/360 entrenched EBCDIC in IBM mainframe environments while ASCII spread in telecommunications, minicomputers, Unix, and networks.

**“Eight-bit defense” folklore:** Retellings sometimes say IBM defeated ASCII by insisting that System/360 was already “eight bit,” or that an unused ASCII bit was deliberately wasted. The defensible core is that IBM prioritized installed-base compatibility and an eight-bit internal code. A neat quotation or one-meeting ultimatum is not established by the sources consulted here.

**Absence-of-evidence finding:** I found no primary IBM manual or committee minute substantiating the strongest conspiratorial version—that IBM intentionally chose EBCDIC chiefly to sabotage ASCII. Mackenzie documents structural and compatibility reasons; later polemic supplies much of the motive story.

### 3. The 1968 US federal mandate

FIPS PUB 1 was issued on 1 November 1968 after President Lyndon B. Johnson approved the recommendation in a memorandum dated 11 March 1968. It adopted X3.4-1967 and part of the 1968 revision.

The implementation schedule required computers and related configurations entering the federal inventory on or after 1 July 1969 to have ASCII capability.

**Documented primary source:** [FIPS PUB 1 scan](https://www.govinfo.gov/content/pkg/GOVPUB-C13-c47f33121f089063e752faa11af234aa/pdf/GOVPUB-C13-c47f33121f089063e752faa11af234aa.pdf)

This was a capability mandate, not proof that every federal file instantly became ASCII. NIST’s retrospective judges federal purchasing power probably the single most important reason for broad adoption. That wording is an institutional historical assessment, not a contemporaneous measurement. [NIST history](https://nvlpubs.nist.gov/nistpubs/sp958-lide/html/172-173.html)

### 4. ARPANET and RFC 20

Vint Cerf’s RFC 20, dated 16 October 1969, proposed standard seven-bit ASCII in an eight-bit byte whose high bit was zero for Host-to-Host primary connections. It reproduced USAS X3.4-1968.

This helped make strict US-ASCII—not an unidentified ISO 646 national version—the Internet’s reference text code.

### 5. Unix and C

Unix selected ASCII-oriented byte strings and control conventions. C’s syntax used almost every contested punctuation character:

`# [ ] \ ^ { | } ~`

This was efficient in ASCII but hostile to national ISO 646 terminals. The result was a division:

- natural-language users wanted `ä ö å`, `æ ø å`, or `é è ç`;
- programmers needed braces, brackets, vertical bar, backslash, tilde, and number sign;
- changing a terminal or font’s national mode could transform readable source into apparent accented prose.

Trigraphs were the standardized escape hatch, but were unpopular and rarely pleasant to read. C++17 removed trigraphs; C23 also removed them. Digraphs and alternative tokens preserve less extreme solutions.

### 6. National replacement character sets in terminals

DEC VT200-series National Replacement Character Sets and similar terminal mechanisms could reinterpret designated positions according to a selected country. This allowed the same seven-bit connection to display localized letters without transferring eight-bit data.

It also reproduced the central failure: bytes alone were insufficient. A saved file or terminal transcript needed knowledge of the active national set.

### 7. Transition to eight-bit codes

By the 1980s, storage and communications increasingly offered eight clean bits. ECMA-94 appeared in 1985 and became the basis of ISO 8859 Parts 1–4. ISO 8859 retained ASCII in the lower half and added 96 graphic positions in the upper half.

Advantages over national ISO 646 included:

- braces and accented letters could coexist;
- one byte still represented one character within a selected part;
- major European language groups received practical repertoires.

Limitations remained:

- multiple mutually incompatible 8859 parts;
- vendor deviations such as Windows-1252;
- no universal mixture of scripts;
- continued dependence on an external charset label.

**Documented standard:** [ECMA-94](https://ecma-international.org/publications-and-standards/standards/ecma-94/), [ISO 8859-1 catalogue](https://www.iso.org/standard/28245.html)

### 8. Email and Usenet ghosts

Original Internet mail paths assumed seven-bit data. National ISO 646 text could pass physically but be rendered incorrectly at the destination.

MIME, RFC 1341 in 1992, was explicit:

- US-ASCII meant exact ANSI X3.4 correspondence;
- national ISO 646 variants were not ASCII;
- their use in Internet mail was discouraged;
- ISO 646 charset names were deliberately omitted in favor of ISO 8859 replacements;
- quoted-printable and Base64 carried bytes safely through seven-bit transports.

Old Usenet and email therefore preserve several ghosts:

- brace-like characters standing for Nordic letters;
- raw eight-bit bytes with no charset declaration;
- quoted-printable artifacts such as `=E4`;
- mojibake after ISO-8859-1/Windows-1252/UTF-8 confusion;
- ASCII transliterations such as `ae`, `oe`, `ss`, or `aa`.

### 9. Unicode and UTF-8 absorption

Unicode and ISO/IEC 10646 shifted the objective from choosing a small national repertoire to assigning stable identities across scripts.

UTF-8 preserves ISO 646/ASCII bytes exactly for `00–7F`. This is ISO 646’s greatest survival:

- ASCII protocol keywords remain byte-for-byte UTF-8;
- source files containing only the invariant characters need no conversion;
- delimiters in markup and programming languages retain their old values.

RFC milestones include:

- RFC 2044, UTF-8, 1996;
- RFC 2279, revised UTF-8, 1998;
- RFC 3629, modern one-to-four-byte UTF-8, 2003;
- RFC 5198, Network Unicode, 2008.

RFC 3629 limits UTF-8 to Unicode’s `U+0000–U+10FFFF` range. RFC 5198 defines a normalized network interchange profile and treats ISO 646:1991 as generally equivalent to ASCII.

### 10. The web

W3C guidance recommends UTF-8 unless exceptional constraints apply. It notes that all browsers process text internally as Unicode.

Reported adoption:

- Google’s January 2012 sample found over 60% of pages directly using UTF-8, or roughly 80% if ASCII-only pages—valid UTF-8—were included.
- W3C reported W3Techs figures of 86% in 2016, 96.1% in 2021, and 97.9% in 2023.
- W3Techs reported 99.1% of websites with a known encoding using UTF-8 on 11 September 2026.

The final number is a third-party survey with a documented methodology and denominator, not a count of every web resource. [W3C usage history](https://www.w3.org/International/questions/qa-who-uses-unicode.en.html), [W3Techs 2026](https://w3techs.com/technologies/breakdown/en-utf8/ranking)

### 11. What survives

ISO 646 survives through:

- the ASCII-compatible first 128 Unicode code points;
- UTF-8’s identical one-byte representation for them;
- C0 controls, especially TAB, LF, CR, ESC, and BEL;
- `0x7F` as DEL;
- terminal escape sequences;
- Internet protocol syntax;
- C-family and Unix punctuation;
- keyboard legends and scan-to-character translation traditions;
- Japanese yen/backslash display ambiguity;
- charset labels, conversion tables, old filenames, archives, and databases;
- the expectation that “plain text” has invisible external assumptions.

Keyboard scan codes themselves are not ASCII: they identify keys or events, which software then maps to characters. Saying “keyboards use ASCII codes” is a persistent modern misconception.

---

## The other scripts

ISO 646’s national mechanism was suitable only for small modifications of Latin alphabets. Larger departures required an entirely different 7-bit set, an ISO 2022 designation, transliteration, overstriking, or vendor-specific encoding.

### Cyrillic

Solutions included KOI-7, later KOI8 variants, ISO-IR Cyrillic sets, ISO 8859-5, DOS/Windows code pages, and Soviet national standards.

The celebrated **KOI8 trick** belongs chiefly to eight-bit KOI8-R: stripping the high bit from Cyrillic text yields a roughly readable Latin transliteration because Cyrillic letters were arranged over phonetically corresponding ASCII letters.

**Documented property:** The mapping can be demonstrated from the table.

**Folklore risk:** It was a designed degradation feature, but broad claims that it always made damaged Russian “readable” exaggerate matters; only approximate transliteration survives, and punctuation or letter distinctions may not.

### Greek

Seven-bit Greek sets replaced Latin letters or national positions; ISO 2022 could designate them. Later solutions included ELOT 928, ISO 8859-7, DOS/Windows code pages, and Unicode.

A whole Greek alphabet cannot be fitted into ISO 646’s ten national-use positions while preserving both Latin cases.

### Hebrew

Seven-bit Hebrew encodings generally repurposed a larger graphic block. They did not solve bidirectional layout merely by assigning characters.

Hebrew presents two separable problems:

1. character identity;
2. visual order in right-to-left text containing left-to-right numbers or Latin text.

Early systems used visual-order storage, implicit conventions, terminal behavior, or application-specific reordering. Unicode later standardized bidirectional properties and the Unicode Bidirectional Algorithm.

### Arabic

Arabic adds contextual shaping and joining to bidirectionality. ISO 646 cannot express the full alphabet through national replacement positions. ASMO 449 and later ISO 8859-6 supplied character codes, while presentation systems handled joining and contextual glyph forms.

**Documented modern guidance:** W3C warns that supporting a Unicode encoding does not by itself ensure correct display: Arabic and Indic scripts require character-to-glyph processing. [W3C encoding guidance](https://www.w3.org/International/questions/qa-choosing-encodings.en)

### Indic scripts

Indic writing requires consonant-vowel combinations, dependent marks, reordering, conjuncts, and shaping. A seven-bit national substitution table is fundamentally insufficient.

ISCII used an eight-bit architecture for several Indian scripts, exploiting structural similarities. Unicode later encoded script characters and properties while fonts and shaping engines produce glyph clusters.

The byte count, character count, grapheme count, and displayed glyph count may all differ.

### Chinese

GB 1988 was a Chinese ISO 646 variant only for the Latin/basic portion; it did not encode Chinese ideographs. GB 2312-80 used a 94-by-94 two-byte structure and contained 7,445 assigned characters according to RFC 1922, including 6,763 hanzi in common descriptions.

RFC 1922 says GB 1988 differed from ISO 646 in currency/yuan and tilde/overline positions and discouraged its separate Internet use because ASCII plus GB 2312 covered its functions. [RFC 1922](https://www.rfc-editor.org/rfc/rfc1922.html)

Later systems included GBK, GB 18030, Big5, CNS 11643, and Unicode.

### Japanese

JIS X 0201 had:

- a Roman set, ISO-IR 14, with yen at `5C` and overline at `7E`;
- a halfwidth katakana set in its broader eight-bit form.

JIS X 0208 encoded kanji, hiragana, katakana, and symbols in a two-byte 94-by-94 set. ISO-2022-JP shifted between ASCII/JIS Roman and JIS X 0208 with escape sequences.

Shift_JIS and EUC-JP provided alternative byte encodings. Their coexistence produced detection failures and mojibake.

### Korean

Korean solutions included KS C 5601/KS X 1001, EUC-KR, Johab, vendor encodings, and Unicode. Encoding modern Hangul raises a design choice between:

- precomposed syllables;
- algorithmic composition from jamo;
- compatibility with existing standards.

Seven-bit ISO 646 could represent at most transliteration without wholesale code switching.

### Emoji

Emoji are historically remote from ISO 646 but illuminate the same institutional problem: finite coded space, installed vendor practice, and disagreement over which signs merit interchange identity.

Japanese mobile carriers first used incompatible private/vendor emoji sets. Unicode incorporated emoji through proposals, compatibility mappings, and UTC/ISO processes. Modern emoji often form sequences using variation selectors, modifiers, zero-width joiners, or regional indicators; “one visible emoji equals one character” is often false.

---

## People and institutions

### People

- **Émile Baudot (1845–1903):** developed the five-unit telegraph code associated with his name in the 1870s.
- **Donald Murray (1865–1945):** adapted five-unit telegraph coding for keyboard and paper-tape operation.
- **Herman Hollerith (1860–1929):** developed punched-card tabulation systems whose descendants shaped IBM data processing.
- **Robert W. Bemer (1920–2004):** IBM and later UNIVAC/GE/Honeywell engineer; advocate for seven bits, lowercase, ESC, and programming punctuation; later prolific narrator of ASCII history.
- **Hugh McGregor Ross (1917–2014):** British computer standards engineer and international collaborator.
- **I. C. Liggett:** IBM representative and first chair of X3.2, according to surviving histories.
- **John Auwaerter:** Teletype engineer and important working-group participant/chair in ASCII development.
- **Charles E. Mackenzie:** IBM engineer and author of the 1980 documentary history *Coded Character Sets: History and Development*.
- **Vint Cerf:** author of RFC 20 at UCLA in 1969.
- **Keld Simonsen:** author of RFC 1345’s character-set and mnemonic catalogue.
- **Ned Freed and Nathaniel Borenstein:** principal MIME authors.
- **Ken Thompson and Rob Pike:** designed UTF-8 at Bell Labs in 1992.
- **Joe Becker, Lee Collins, and Mark Davis:** central figures in the early Unicode project and Consortium.
- **Ken Whistler:** Unicode editor and long-serving technical participant.

The brief names “Davis” and “Collins”; these refer most plausibly to Mark Davis and Lee Collins. “Becker” refers to Joseph D. Becker of Xerox.

### Institutions

- **ASA/USASI/ANSI:** successive names around the American national standards process.
- **ECMA:** European computer manufacturers’ standards organization; ECMA-6 and ECMA-35 were central to ISO 646/2022.
- **ISO/IEC:** international standardization, initially through ISO/TC 97 and later JTC 1/SC 2.
- **CCITT/ITU-T:** telecommunications standardization; International Alphabet No. 5, V.3, and T.50.
- **IBM:** ASCII committee participant but commercial champion of EBCDIC on mainframes.
- **Teletype/AT&T:** terminal and network deployment.
- **DEC:** ASCII minicomputers and terminals plus national replacement sets.
- **Bell Labs:** Unix, C, and later UTF-8.
- **Xerox and Apple:** important early Unicode institutional homes.
- **Unicode Consortium:** industry-led maintenance and extension of Unicode.
- **IETF:** Internet charset, MIME, UTF-8, identifier, security, and protocol standards.
- **W3C/WHATWG:** web encoding rules and UTF-8 promotion.

---

## Culture

### 1. “Plain text”

ISO 646 strengthened an ideal of text as portable character values independent of a particular machine. Yet its national variants expose the incompleteness of that ideal:

```text
5C
```

means backslash in ASCII, yen in JIS Roman, Ö in DIN 66003, Ø in Norwegian ISO 646, and ç in several Latin national tables.

A byte stream was never fully self-describing. “Plain text” requires a repertoire/encoding agreement, and often language, direction, normalization, and line-ending conventions as well.

### 2. ASCII art

Monospaced terminals and printers turned the ASCII graphic block into a drawing vocabulary. Slashes, backslashes, underscores, bars, punctuation, and overprinting produced diagrams, faces, signatures, and large letterforms.

National variants could deform art: a backslash stroke might become `Ö`, `Ø`, `ç`, or `¥`. ASCII art therefore quietly assumes the American/IRV graphic assignments, not merely seven-bit transport.

### 3. Demoscene and text graphics

The demoscene extended textual graphics through PETSCII, ATASCII, IBM code page 437, ANSI terminal color escapes, and custom fonts. Much “ASCII art” is technically ANSI art, CP437 art, Shift_JIS art, or Unicode block art.

**Cultural reconstruction:** Communities often use “ASCII” aesthetically to mean fixed-grid text imagery, even where the bytes are not ASCII. This is folk taxonomy rather than standards terminology.

### 4. Mojibake

*Mojibake*—文字化け, roughly “character corruption/transformation”—names text decoded under the wrong encoding. ISO 646 variants are an early pure example: the same valid byte is assigned another valid graphic, so there is no decoding error to detect.

Later characteristic forms include:

- UTF-8 `C3 BC` decoded as Windows-1252 → `Ã¼`;
- Windows-1252 quotation marks decoded as ISO-8859-1 controls;
- Japanese Shift_JIS interpreted as EUC-JP or vice versa;
- visible yen/backslash substitution.

Mojibake became an intentional aesthetic in glitch art, online pseudonyms, vaporwave typography, and “zalgo” or corrupted-text styles. These modern aesthetics imitate accidental encoding failure but often use valid Unicode deliberately.

### 5. Programming punctuation as cultural power

ASCII’s braces, brackets, backslash, vertical bar, tilde, number sign, dollar, and at sign became central syntax:

- C, C++, Java, JavaScript, Rust, and many successors;
- Unix paths and shell syntax;
- regular expressions;
- email addresses;
- URLs and URI escapes;
- markup and configuration languages.

The national variants reveal a feedback loop: punctuation selected for American programming languages became globally indispensable, making it progressively harder to replace those positions with national letters.

### 6. Unicode as a political institution

Encoding is not simply discovery. Committees decide:

- whether a proposed sign is a character, glyph, sequence, or formatting effect;
- how it is named;
- which existing standard it must remain compatible with;
- whether visually similar forms are unified;
- what gets encoded first;
- who has the expertise and resources to submit a successful proposal.

Calling Unicode “political” is therefore descriptively accurate. It does not imply that every decision is arbitrary. UTC and ISO/IEC JTC 1/SC 2 operate through proposals, evidence, ballots, liaison, stability rules, and compatibility constraints.

The unequal capacity of communities to document scripts and participate remains a genuine institutional concern.

---

## Controversies and disputes

### 1. Who invented ASCII?

- **Documented:** it was produced by ASA X3 committees and working groups.
- **Participant recollection:** Bemer vigorously promoted key features.
- **Popular credit:** “father of ASCII.”
- **Overclaim:** “Bemer invented ASCII.”
- **Evidence judgment:** committee authorship is strongest; Bemer deserves prominent but not exclusive credit.

### 2. The “Bemer–Ross code”

- **Source type:** Bemer’s retrospective recollection.
- **Claim:** Europeans temporarily used this informal name.
- **Corroboration:** Ross’s participation and influence are documented.
- **Missing evidence:** no formal standard with that title was located.
- **Classification:** plausible participant recollection, not established official nomenclature.

### 3. The “# $ @ [ \ ] wars”

The phrase is modern editorial shorthand, not a known formal name for one historical controversy. It accurately captures recurrent allocation conflict:

- programmers needed syntax;
- national bodies needed alphabetic letters;
- Britain wanted `£`;
- ISO sought `¤`;
- Japan and China used currency signs;
- several languages reused brackets and braces.

**Dedicated-search finding:** Searches for the exact dossier title and combinations with “history,” “dispute,” “credit,” “controversy,” “mojibake,” and “security” did not uncover a contemporary event called the “# $ @ [ \ ] wars.” Treat it as a useful modern label.

### 4. “International ASCII,” 1967–1973

- **Documented:** American, ECMA, ISO, and CCITT work was deliberately coordinated.
- **Accurate shorthand:** ISO 646 internationalized the basic ASCII architecture.
- **Misleading implication:** every ISO 646 file was byte-semantically ASCII.
- **Resolution:** the 1991 IRV became identical to ASCII, while national versions remained distinguishable registered sets.

### 5. Scandinavian programmer misery

- **Documented technical cause:** Nordic letters occupied bracket/brace positions.
- **Documented remedy:** C trigraphs.
- **Participant/community recollection:** programmers used ASCII modes or wrote natural-language text with brace substitutions.
- **Folklore:** lurid source examples are often demonstrations repeated without usage evidence.
- **Finding:** the portability problem was real; its everyday incidence is poorly quantified.

### 6. Yen versus backslash

- **Documented:** JIS X 0201 Roman assigns yen to `0x5C`.
- **Later compatibility fact:** Unicode assigns reverse solidus to U+005C and yen sign to U+00A5, but Japanese environments may display U+005C with a yen-like glyph for compatibility.
- **Modern confusion:** a visible yen glyph does not prove the stored character is U+00A5.
- **Security/usability issue:** paths, source escapes, and copy/paste may be misunderstood even when the underlying code point is unchanged.

### 7. EBCDIC and IBM

- **Documented:** IBM participated in standards work but adopted EBCDIC for System/360.
- **Scholarly account:** punched-card compatibility, translation, printers, and installed equipment were central.
- **Polemic/folklore:** IBM chose EBCDIC solely to lock customers in or to defeat ASCII.
- **Finding:** vendor strategy may have benefited from incompatibility, but the consulted primary material does not establish the single-motive claim.

### 8. UTF-8’s placemat story

Rob Pike recounts that he and Ken Thompson designed UTF-8 during a September 1992 conversation in a New Jersey diner, with Thompson sketching it on a placemat and implementing it that night or shortly afterward.

- **Source type:** participant recollection by Pike.
- **Corroborated core:** Thompson and Pike created the design, it was rapidly implemented in Plan 9, and FSS/UTF proposals provide documentary context.
- **Fragile detail:** the placemat is effectively a one-participant anecdote in its familiar form; the original placemat has not been produced.
- **Classification:** credible but singly witnessed anecdote, not a surviving design document.

### 9. Han unification

Unicode/ISO 10646 assigns unified code points to many Han ideographs shared historically among Chinese, Japanese, Korean, and Vietnamese traditions, while glyph selection may vary by language or font.

**Arguments for:**

- shared historical character identity;
- compatibility with existing CJK standards;
- avoidance of needless duplication;
- glyph variation is normally handled by fonts.

**Objections:**

- regional glyph distinctions can be semantically, educationally, or culturally important;
- language-tag or font-dependent rendering can be unreliable;
- unification was perceived by some Japanese users as subordinating national typographic forms;
- compatibility ideographs and variation sequences make the model more complicated than the slogan suggests.

**Evidence classification:** The controversy is real and documented in Unicode/ISO records and participant accounts. Claims that Unicode “encoded Chinese and deleted Japanese” are polemical simplifications; claims that all differences are merely font style are also too simple.

This controversy belongs to ISO 646’s long afterlife because it poses the same question at vastly larger scale: when are two visual forms “the same character” for interchange?

### 10. Unicode’s 16-bit assumption

Early Unicode aimed at a 16-bit universal character space, while the contemporary ISO 10646 project contemplated a larger multi-octet architecture. The projects converged on a common repertoire, but Unicode exhausted the Basic Multilingual Plane and added supplementary planes represented in UTF-16 by surrogate pairs.

- **Documented:** current Unicode has code points through U+10FFFF and UTF-16 uses surrogate pairs outside the BMP.
- **Historical judgment:** “Unicode promised every character would always be 16 bits” reflects genuine early design expectations.
- **Overstatement:** it does not describe modern Unicode or UTF-8.

### 11. Byte-order mark

U+FEFF originated as ZERO WIDTH NO-BREAK SPACE and, when serialized at the beginning of UTF-16 or UTF-32, can signal byte order. UTF-8 has no byte-order ambiguity, so its BOM is only a signature.

Controversies include:

- useful encoding detection versus unwanted invisible bytes;
- shell scripts and protocol parsers treating `EF BB BF` as data;
- concatenation placing U+FEFF inside text;
- differing application policies.

W3C documents that a UTF-8 BOM can determine HTML encoding and that UTF-16 HTML effectively requires byte-order information. [W3C HTML encoding declarations](https://www.w3.org/International/questions/qa-html-encoding-declarations.en)

### 12. Overlong UTF-8

Earlier UTF-8 decoders sometimes accepted a character encoded with more bytes than necessary. Thus `/`, NUL, or another security-sensitive ASCII character could have both canonical and overlong representations.

Attack pattern:

1. a filter looks for canonical ASCII `/` or NUL;
2. an overlong sequence passes the filter;
3. a downstream decoder reduces it to the forbidden character.

RFC 3629 requires shortest-form encoding and rejects surrogate values and code points beyond U+10FFFF. Overlong forms are invalid UTF-8.

### 13. Homoglyph and identifier attacks

Unicode permits visually similar characters from different scripts: Latin `a`, Cyrillic `а`, and Greek `α` are distinct. Attacks may exploit:

- mixed-script domain names;
- source-code identifiers;
- bidirectional controls;
- normalization differences;
- invisible or default-ignorable characters.

ISO 646 largely avoided cross-script homoglyphs by excluding other scripts, but national variants demonstrated the predecessor problem: identical bytes could appear as different glyphs, and identical-looking glyphs could carry environment-dependent semantics.

### 14. Emoji and Consortium power

Criticism holds that:

- corporations and popular campaigns can devote greater resources to proposals;
- the encoded repertoire reflects market demand unevenly;
- approval can appear like a vote on cultural worth;
- flags and identity symbols create geopolitical disputes.

The Consortium’s formal position is that encoding establishes interchange characters, not endorsement, and that proposals must meet selection criteria.

**Clarification:** There is no single public popular “emoji vote” that determines the standard. UTC decisions, vendor participation, proposal evidence, and ISO synchronization form the actual process. Online campaigns influence attention but are not ballots.

### 15. Tibetan and CJK disputes

Tibetan encoding debates concerned decomposition, stacks, transliteration, and compatibility with national or scholarly models. CJK disputes concerned character identity, regional forms, legacy mappings, and ordering.

These are historically distinct from ISO 646. Their relevance is institutional: the move from national tables to one universal repertoire did not eliminate politics; it moved disputes from byte positions into character identity, normalization, variants, and rendering.

### 16. ISO versus Unicode

Early ISO 10646 and Unicode differed in architecture and institutional culture. They ultimately synchronized character assignments.

- Unicode supplies a full standard including properties, normalization, bidirectionality, algorithms, and conformance.
- ISO/IEC 10646 supplies the internationally balloted Universal Coded Character Set.
- Neither simply “defeated” the other.
- Vendor adoption of Unicode and UTF-8 gave the joint repertoire practical dominance.

### 17. Vendor code pages

DOS, IBM, Microsoft, Apple, DEC, and others created code pages that filled practical gaps faster than international standardization. Benefits included working local software and graphic symbols. Costs included:

- conflicting mappings for the same byte;
- mislabeled “ANSI” encodings;
- irreversible conversion;
- filename and archive ambiguity;
- mojibake.

National ISO 646 variants were the small-scale ancestor of this code-page ecology.

---

## Open questions

1. **Complete committee attribution:** Published histories name Bemer, Ross, Liggett, Auwaerter, and others, but a definitive prosopography would require full X3.2/X3.2.4 attendance lists, proposal papers, ballots, and correspondence.

2. **Earliest documentary use of “Bemer–Ross code”:** The familiar account comes from Bemer. A contemporaneous European memorandum using the term has not been located here.

3. **Quantifying national-variant use:** Registration proves standardization, not market share. Terminal sales, telecommunications tariffs, national procurement files, and surviving media would be needed to distinguish official adoption from actual use.

4. **Which DIN 66003 edition introduced each mapping:** Later registries give the stable table, but edition-level German documentation should be consulted before assigning every mapping to the earliest DIN publication.

5. **French variants:** NF Z 62-010 changed between the 1973 ISO-IR 25 and 1982 ISO-IR 69 registrations. Secondary tables frequently collapse them.

6. **“Programmer misery” evidence:** The technical conflict and trigraph rationale are documented; representative workplace diaries, source archives, and surveys are scarce.

7. **The placemat:** Pike’s account is persuasive participant testimony, but no physical placemat or independent eyewitness account anchors the picturesque detail.

8. **IBM motive claims:** The business consequences of EBCDIC are plain. Strong intentional-lock-in narratives need contemporary executive or engineering evidence.

9. **National glyph semantics:** Historical standards often specified graphic forms under typographic conventions unlike Unicode’s later abstract-character model. Mapping overline/macron, yen/yuan, accent/quotation, and vertical-line variants may require consulting the original national plates.

10. **Archival rendering:** Scanned tables can silently inherit OCR errors. For legal or preservation conversion, the original printed national standard and registered ISO-IR chart should control over RFC or web transcriptions.

11. **Exact title search result:** No historical source located used “the # $ @ [ \ ] wars” as an event name. Its earliest coinage remains open; it appears to be a modern descriptive title.

---

## Sources

### Primary standards and official catalogues

- ISO, *ISO 646:1973 — 7-bit coded character set for information-processing interchange*:  
  https://www.iso.org/standard/2823.html

- Public scan of ISO 646:1973:  
  https://cdn.standards.iteh.ai/samples/2823/380b0375541d4a87baaaf782673762b1/ISO-646-1973.pdf

- ISO, *ISO/IEC 646:1991 — Information technology — ISO 7-bit coded character set for information interchange*, edition 3:  
  https://www.iso.org/standard/4777.html

- ECMA International, ECMA-6 editions archive:  
  https://ecma-international.org/publications-and-standards/standards/ecma-6/

- ECMA International, *ECMA-6, 7-bit coded character set*, sixth edition, December 1991:  
  https://www.ecma-international.org/wp-content/uploads/ECMA-6_6th_edition_december_1991.pdf

- ECMA International, ECMA-35, *Character Code Structure and Extension Techniques*, sixth edition, December 1994:  
  https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf

- ISO/IEC 2022 official browsing page:  
  https://www.iso.org/obp/ui#iso:std:iso-iec:2022:ed-4:v1:en

- ECMA International, ECMA-94, *8-bit single-byte coded graphic character sets—Latin alphabets No. 1 to No. 4*:  
  https://ecma-international.org/publications-and-standards/standards/ecma-94/

- ISO, ISO/IEC 8859-1:1998 catalogue, including earlier-edition record:  
  https://www.iso.org/standard/28245.html

- ITU-T, T.50, *International Reference Alphabet*:  
  https://www.itu.int/rec/T-REC-T.50/en

- IANA Character Sets registry:  
  https://www.iana.org/assignments/character-sets/character-sets.xhtml

- Chinese national standards service, GB/T 1988-1998:  
  https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D7C469D3A7E05397BE0A0AB82A

### American standards and federal adoption

- FIPS PUB 1, *Code for Information Interchange*, 1 November 1968:  
  https://www.govinfo.gov/content/pkg/GOVPUB-C13-c47f33121f089063e752faa11af234aa/pdf/GOVPUB-C13-c47f33121f089063e752faa11af234aa.pdf

- FIPS PUB 1-2 and historical notes:  
  https://www.govinfo.gov/content/pkg/GOVPUB-C13-f191ad6d48efb6c69f1c254cd91f2b08/pdf/GOVPUB-C13-f191ad6d48efb6c69f1c254cd91f2b08.pdf

- NIST historical account of ASCII and FIPS adoption:  
  https://nvlpubs.nist.gov/nistpubs/sp958-lide/html/172-173.html

- US government chronology of ASCII development, preserved in CIA FOIA:  
  https://www.cia.gov/readingroom/document/cia-rdp78-04723a000200020028-3

### RFCs and Internet standards

- RFC 20, Vint Cerf, *ASCII format for Network Interchange*, October 1969:  
  https://www.rfc-editor.org/rfc/rfc20.html

- RFC 1341, Nathaniel Borenstein and Ned Freed, *MIME*, June 1992:  
  https://www.rfc-editor.org/rfc/rfc1341.html

- RFC 1345, Keld Simonsen, *Character Mnemonics & Character Sets*, June 1992:  
  https://www.rfc-editor.org/rfc/rfc1345.html

- RFC 1468, Jun Murai, Mark Crispin, and Erik van der Poel, *Japanese Character Encoding for Internet Messages*, June 1993:  
  https://www.rfc-editor.org/rfc/rfc1468.html

- RFC 1922, *Chinese Character Encoding for Internet Messages*, March 1996:  
  https://www.rfc-editor.org/rfc/rfc1922.html

- RFC 2044, *UTF-8, a transformation format of Unicode and ISO 10646*, October 1996:  
  https://www.rfc-editor.org/rfc/rfc2044.html

- RFC 2045, MIME Part One, November 1996:  
  https://www.rfc-editor.org/rfc/rfc2045.html

- RFC 2279, *UTF-8, a transformation format of ISO 10646*, January 1998:  
  https://www.rfc-editor.org/rfc/rfc2279.html

- RFC 3629, François Yergeau, *UTF-8, a transformation format of ISO 10646*, November 2003:  
  https://www.rfc-editor.org/rfc/rfc3629.html

- RFC 5198, *Unicode Format for Network Interchange*, March 2008:  
  https://www.rfc-editor.org/rfc/rfc5198.html

### Historical reconstructions and participant accounts

- Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley, 1980, ISBN 0-201-14460-3, Internet Archive identifier `codedcharacterse00unse`:  
  https://archive.org/details/codedcharacterse00unse

- Open Library bibliographic record for Mackenzie:  
  https://openlibrary.org/books/OL4570655M/Coded_character_sets

- IEEE Computer Society, Robert W. Bemer biography:  
  https://history.computer.org/pioneers/bemer.html

- Computer History Museum archival collection, Bemer papers and historical writings:  
  https://archive.computerhistory.org/resources/access/text/2021/04/102785423-05-03-acc.pdf

- Computer History Museum, 1960s Internet history:  
  https://www.computerhistory.org/internethistory/1960s/

- Rob Pike, *UTF-8 history*:  
  https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt

- Plan 9 UTF history mirror and documentary material:  
  https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt

- Unicode Consortium history:  
  https://home.unicode.org/about-unicode/history-of-unicode/

- Unicode Consortium, current core specification and ISO 10646 relationship:  
  https://www.unicode.org/versions/latest/core-spec/

### National-set tables and registry transcriptions

- RFC 1345 tables for ISO-IR 2, 4, 6, 10, 11, 14, 15, 17, 21, 60, 69, and others:  
  https://www.rfc-editor.org/rfc/rfc1345.html

- IANA registry aliases for ISO 646 national sets:  
  https://www.iana.org/assignments/character-sets/character-sets.xhtml

- GNU/Aspell historical ISO 646 table, archived:  
  https://web.archive.org/web/20160530181116/http://aspell.net/charsets/iso646.html

### Unicode, web, and internationalization

- W3C, *Choosing & applying a character encoding*:  
  https://www.w3.org/International/questions/qa-choosing-encodings.en

- W3C, *Who uses Unicode?*:  
  https://www.w3.org/International/questions/qa-who-uses-unicode.en.html

- W3C, *Declaring character encodings in HTML*:  
  https://www.w3.org/International/questions/qa-html-encoding-declarations.en

- W3C, *Character Sets and Encodings*:  
  https://www.w3.org/International/getting-started/characters.en

- W3C, *Internationalization Quick Tips*:  
  https://www.w3.org/International/quicktips/Overview

- W3Techs, UTF-8 usage by ranking, dated 11 September 2026 when consulted:  
  https://w3techs.com/technologies/breakdown/en-utf8/ranking

- Unicode Standard Annex #9, *Unicode Bidirectional Algorithm*:  
  https://www.unicode.org/reports/tr9/

- Unicode Standard Annex #15, *Unicode Normalization Forms*:  
  https://www.unicode.org/reports/tr15/

- Unicode Technical Standard #39, *Unicode Security Mechanisms*:  
  https://www.unicode.org/reports/tr39/

- Unicode Consortium, emoji proposals and submission guidance:  
  https://unicode.org/emoji/proposals.html

- Unicode Consortium, UTC document register and minutes portal:  
  https://www.unicode.org/L2/

### Programming-language consequences

- ANSI C Rationale, trigraph discussion and source character-set constraints:  
  https://www.lysator.liu.se/c/rat/title.html

- ISO C working-group document index:  
  https://www.open-std.org/jtc1/sc22/wg14/www/docs/

### Secondary indexes used only to locate primary material

- ISO/IEC 646 overview and national-version index:  
  https://en.wikipedia.org/wiki/ISO/IEC_646

- ASCII overview and bibliography:  
  https://en.wikipedia.org/wiki/ASCII

These two index pages were not used as substitutes for the standards, RFCs, or historical records above.
