# EBCDIC: Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| Name | Extended Binary Coded Decimal Interchange Code |
| Abbreviation | EBCDIC |
| Originator | International Business Machines Corporation (IBM) |
| First development | 1963–1964 |
| Public introduction | April 7, 1964, with the IBM System/360 |
| Standard number | No single universal EBCDIC standard number. Particular repertoires are identified by IBM code-page numbers and CCSIDs: notably IBM037/CCSID 37, IBM500/CCSID 500, and IBM1047/CCSID 1047. IANA registers these separately. |
| Unit width | 8 bits per single-byte character; 256 possible byte values |
| Original repertoire | Latin letters in both cases, decimal digits, punctuation, symbols, and numerous control functions; the exact graphic repertoire depends on the code page |
| Extensions | National single-byte pages, double-byte EBCDIC for CJK scripts, mixed SBCS/DBCS encodings using Shift Out and Shift In, and later Euro variants |
| Principal machines | IBM System/360 and descendants; System/370, 390, zSeries/IBM Z; IBM midrange families culminating in IBM i |
| Present status | Legacy but active. Still an ordinary native or interchange representation in parts of z/OS, IBM i, Db2, CICS, IMS, COBOL, terminal, print, batch, and archival workflows. It is not a general Internet or Web interchange standard. |
| Successor for general interchange | Unicode, especially UTF-8; IBM systems nevertheless continue to support EBCDIC CCSIDs and conversions |

### Evidence labels used below

- **[D—contemporary]** Contemporary IBM manual, standard, government document, or protocol specification.
- **[D—current]** Current IBM, IANA, Unicode, IETF, or W3C documentation.
- **[R—scholarly]** Historical reconstruction, especially Charles E. Mackenzie’s 1980 study or later computing histories.
- **[P—recollection]** Participant’s later recollection.
- **[Disputed]** Competing accounts or an attribution not settled by surviving documentation.
- **[Folklore]** Joke, hacker lore, or community story presented as culture rather than fact.
- **[Modern]** A later interpretation, slogan, or retrospective simplification.

A crucial preliminary finding is that “EBCDIC” is a family, not one timeless 256-character table. Statements such as “byte `BA` means `[` in EBCDIC” are incomplete unless the code page or CCSID is named. In IBM037 it does; in IBM500 it does not. IBM’s present documentation explicitly distinguishes invariant from variant EBCDIC characters and lists CCSIDs 37, 500, and 1047 as examples. **[D—current]** ([IBM Db2: EBCDIC](https://www.ibm.com/docs/en/db2-for-zos/13.0.0?topic=schemes-ebcdic), [IANA character-set registry](https://www.iana.org/assignments/character-sets))

---

## The code in detail

### 1. Basic structure

Ordinary single-byte EBCDIC is a fixed-width, eight-bit code:

```text
bit positions:  0 1 2 3 4 5 6 7
byte range:     00–FF hexadecimal
possibilities:  256
```

The common presentation as a 16×16 table is historically revealing. The high nibble selects a group and the low nibble a position within it. Unlike ASCII, graphics do not occupy one nearly continuous interval. Large areas below `40` are controls; letters occupy several blocks inherited from punched-card zone/digit organization.

Broadly:

| Bytes | Common role |
|---|---|
| `00–3F` | Control functions, communications controls, format controls, device-oriented functions; assignments have varied |
| `40` | Space |
| `41–7F` | Punctuation, symbols, accented letters, and some controls or reserved positions depending on page |
| `81–89` | Lowercase `a–i` |
| `91–99` | Lowercase `j–r` |
| `A2–A9` | Lowercase `s–z` |
| `C1–C9` | Uppercase `A–I` |
| `D1–D9` | Uppercase `J–R` |
| `E2–E9` | Uppercase `S–Z` |
| `F0–F9` | Digits `0–9` |
| `FF` | Eight Ones, commonly abbreviated EO; not ASCII DEL |

The three-part alphabet is the conspicuous EBCDIC signature. It is not arbitrary decoration: it preserves the organization of IBM punched-card encodings, in which alphabetic characters combined a zone punch with a digit punch. Mackenzie devotes separate chapters to BCDIC, EBCDIC’s structure, its sequence, its “duals,” and its card representation. **[R—scholarly]** ([Mackenzie scan](https://hcs64.com/files/Mackenzie%20-%20Coded%20Character%20Sets%20History%20and%20Development.pdf), [Open Library record](https://openlibrary.org/books/OL4570655M/Coded_character_sets))

### 2. Representative full graphic table: IBM037

The following is the graphic portion of IBM code page 37, traditionally used for the United States, Canada, the Netherlands, Portugal, Brazil, Australia, and New Zealand. Column headings are the high hexadecimal digit and row headings the low digit. `SP` is space, `RSP` is required/nonbreaking space, `SHY` soft hyphen, and `EO` Eight Ones.

| Low \ High | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | SP | `&` | `-` | `ø` | `Ø` | `°` | `µ` | `^` | `{` | `}` | `\` | `0` |
| 1 | RSP | `é` | `/` | `É` | `a` | `j` | `~` | `£` | `A` | `J` | `÷` | `1` |
| 2 | `â` | `ê` | `Â` | `Ê` | `b` | `k` | `s` | `¥` | `B` | `K` | `S` | `2` |
| 3 | `ä` | `ë` | `Ä` | `Ë` | `c` | `l` | `t` | `·` | `C` | `L` | `T` | `3` |
| 4 | `à` | `è` | `À` | `È` | `d` | `m` | `u` | `©` | `D` | `M` | `U` | `4` |
| 5 | `á` | `í` | `Á` | `Í` | `e` | `n` | `v` | `§` | `E` | `N` | `V` | `5` |
| 6 | `ã` | `î` | `Ã` | `Î` | `f` | `o` | `w` | `¶` | `F` | `O` | `W` | `6` |
| 7 | `å` | `ï` | `Å` | `Ï` | `g` | `p` | `x` | `¼` | `G` | `P` | `X` | `7` |
| 8 | `ç` | `ì` | `Ç` | `Ì` | `h` | `q` | `y` | `½` | `H` | `Q` | `Y` | `8` |
| 9 | `ñ` | `ß` | `Ñ` | `` ` `` | `i` | `r` | `z` | `¾` | `I` | `R` | `Z` | `9` |
| A | `¢` | `!` | `¦` | `:` | `«` | `ª` | `¡` | `[` | SHY | `¹` | `²` | `³` |
| B | `.` | `$` | `,` | `#` | `»` | `º` | `¿` | `]` | `ô` | `û` | `Ô` | `Û` |
| C | `<` | `*` | `%` | `@` | `ð` | `æ` | `Ð` | `¯` | `ö` | `ü` | `Ö` | `Ü` |
| D | `(` | `)` | `_` | `'` | `ý` | `¸` | `Ý` | `¨` | `ò` | `ù` | `Ò` | `Ù` |
| E | `+` | `;` | `>` | `=` | `þ` | `Æ` | `Þ` | `´` | `ó` | `ú` | `Ó` | `Ú` |
| F | `|` | `¬` | `?` | `"` | `±` | `¤` | `®` | `×` | `õ` | `ÿ` | `Õ` | EO |

This table is documented by IBM; Unicode also publishes a machine-readable CP037 mapping. **[D—current]** ([IBM code-page-37 table](https://www.ibm.com/docs/en/db2-for-zos/13.0.0?topic=schemes-ebcdic), [Unicode CP037 mapping directory](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/EBCDIC/))

Some displayed details depend on how a modern Unicode mapping treats historical graphic distinctions. For example, overline/macron, quotation marks, required space, and control names have not always been mapped identically by every conversion library. A mapping file is therefore part of a conversion contract, not merely an illustration.

### 3. Controls

The low quarter is not simply “ASCII controls in different locations.” It contains a mixture of functions inherited or adapted from communications, punched-card, terminal, printer, and data-processing practice.

Common assignments include:

| Byte | Name or role |
|---:|---|
| `00` | NUL |
| `01` | SOH |
| `02` | STX |
| `03` | ETX |
| `05` | HT |
| `07` | DEL in common modern mappings |
| `0B` | VT |
| `0C` | FF |
| `0D` | CR |
| `0E` | SO, Shift Out |
| `0F` | SI, Shift In |
| `10` | DLE |
| `11–13` | DC1–DC3 |
| `15` | NL, New Line |
| `16` | BS |
| `18` | CAN |
| `19` | EM |
| `1B` | CU1 |
| `1C–1F` | field/group/record/unit separators |
| `25` | LF in IBM’s ASCII-compatible control mapping |
| `26` | ETB |
| `27` | ESC |
| `2D` | ENQ |
| `2E` | ACK |
| `2F` | BEL |
| `32` | SYN in common tables |
| `37` | EOT |
| `3F` | SUB in common tables |

The exact names and Unicode equivalents in `00–3F` require a specific IBM control-character convention. IBM itself warns, in effect, against treating all EBCDIC controls as a simple relocation of the ISO 6429 C0/C1 sets. **[D—current]**

#### Newline

EBCDIC has a particularly important distinction:

- `15` is the native EBCDIC **NL** control used as `'\n'` by IBM C runtimes and many mainframe text conventions.
- `25` may be identified as **LF**.
- Record-oriented mainframe datasets often have no newline byte at all. Record length, access method, or dataset organization supplies the boundary.
- When converted to Unix text, an EBCDIC record boundary or `15` commonly becomes ASCII/UTF-8 `0A`.
- When converted to Internet text, the target protocol may demand `CR LF`, not merely LF.

IBM’s C runtime table gives `'\n' = 15`, `'\r' = 0D`, `'\t' = 05`, and space `40`. **[D—current]** ([IBM runtime character set](https://www.ibm.com/docs/en/i/7.4.0?topic=considerations-runtime-character-set), [IBM character tables](https://www.ibm.com/docs/en/z-netview/6.3.0?topic=processing-character-tables))

This is a frequent migration trap: decoding bytes and reconstructing records are separate operations.

#### Space, deletion, and “all ones”

- Space is `40`, not ASCII `20`.
- Common EBCDIC-to-Unicode tables map a DEL function at `07`, not `7F`.
- `FF`, the all-one byte that is ASCII DEL’s position only in seven-bit ASCII, is EBCDIC **EO** or Eight Ones.
- Thus the teleprinter/paper-tape rationale for ASCII DEL—overpunch every hole to ones—is not preserved at EBCDIC’s `FF`.

The slogan “EBCDIC has DEL at `FF` because all bits are one” is therefore false for the standard code pages examined. It is usually an ASCII intuition projected onto EBCDIC. **[Modern misconception]**

### 4. Case

EBCDIC assigned both uppercase and lowercase Latin alphabets:

```text
lowercase: 81–89, 91–99, A2–A9
uppercase: C1–C9, D1–D9, E2–E9
```

The code therefore did not intrinsically require case shifting. But many card punches, printers, terminals, applications, and datasets supported only uppercase or restricted repertoires. “EBCDIC was uppercase-only” is consequently wrong as a statement about the eight-bit code, but can accurately describe a device or installation subset. **[D—contemporary; R—scholarly]**

Japanese code page 290 is a notable exception to the normal invariant positions for lowercase Latin letters. IBM calls this out in current documentation. **[D—current]**

### 5. Collating order

If raw unsigned byte values are used as the sort keys, the broad order is:

```text
controls
space and punctuation
lowercase a–z
uppercase A–Z
digits 0–9
```

Within each Latin alphabet, letters retain alphabetic order despite the three gaps:

```text
a…i < j…r < s…z
A…I < J…R < S…Z
```

This differs sharply from ASCII’s:

```text
space/punctuation < digits < uppercase < lowercase
```

Consequences include:

- digits sort after letters in raw EBCDIC;
- lowercase sorts before uppercase;
- punctuation order differs from ASCII;
- translating bytes without separately specifying collation can change database and report order;
- national-page variants change the positions of some punctuation and accented letters;
- language-sensitive Db2 collations need not use raw EBCDIC order.

IBM still publishes an IBM037 EBCDIC collating sequence. **[D—current]** ([IBM EBCDIC sequence](https://www.ibm.com/docs/en/zos/3.1.0?topic=sequences-ebcdic))

The common complaint that EBCDIC’s alphabet is “not contiguous” is true in a numerical sense but sometimes overstated: each case is split into three ordered runs, and comparisons across the gaps still preserve A-to-Z order.

### 6. Escape and shift mechanisms

#### ESC

EBCDIC commonly assigns ESC at `27`. Its mere presence does not make EBCDIC a universal ISO 2022-style designation system. Whether ESC introduces a terminal command, data-stream function, or code extension is protocol-dependent.

#### SBCS/DBCS shifting

IBM’s East Asian mixed encodings use:

```text
0E  Shift Out: following bytes are interpreted in DBCS state
0F  Shift In:  return to SBCS state
```

Within the DBCS state:

- each graphic character occupies exactly two bytes;
- ordinary valid byte values are generally `41–FE` in each position;
- `4040` is the DBCS blank;
- `42C1` is, in IBM’s documented convention, a double-byte form corresponding to SBCS `A`;
- pure graphic fields may omit SO/SI because field metadata already establishes the representation.

**[D—current]** ([IBM DBCS overview](https://www.ibm.com/docs/en/cics-ts/6.x?topic=support-dbcs-general-description), [IBM SO/SI documentation](https://www.ibm.com/docs/en/cobol-zos/6.5.0?topic=registers-shift-out-shift-in), [IBM mixed DBCS fields](https://www.ibm.com/docs/en/ims/15.5.0?topic=messages-mixed-dbcs-ebcdic-fields))

This was not a single worldwide EBCDIC repertoire. A mixed CCSID identifies an associated SBCS page, a DBCS page, and the encoding scheme needed to interpret them.

### 7. Synchronization and corruption

#### Single-byte EBCDIC

SBCS EBCDIC is trivially self-synchronizing at byte boundaries: every byte is one character or control. If a reader begins at an arbitrary byte boundary, it can decode the next byte without scanning for a lead-byte pattern.

But that limited property should not be confused with error detection:

- all 256 byte values may be meaningful;
- there is no embedded checksum;
- a bit flip usually becomes another valid character;
- a missing or inserted byte shifts fixed fields and record layouts;
- the code alone cannot identify the correct code page;
- record-oriented files may require external metadata to locate records;
- packed decimal, binary integers, floating point, text, and zoned decimal may coexist in one record.

Thus EBCDIC is byte-synchronized but not semantically self-identifying or error-detecting.

#### Mixed EBCDIC DBCS

Mixed SBCS/DBCS is stateful. Loss or corruption of `0E` or `0F` can cause following bytes to be paired or interpreted in the wrong state. Recovery normally depends on:

- encountering a trustworthy SI;
- reaching a field or record boundary whose metadata resets the state;
- validating that DBCS bytes occur in legal pairs and ranges;
- knowing the enclosing data format.

A mid-stream reader cannot always infer the correct state from the next byte because many values are legal in both modes. This is weaker resynchronization than UTF-8’s distinguishable lead and continuation-byte pattern. **[Technical inference from IBM’s documented state rules]**

### 8. What it expresses—and what it does not

A single EBCDIC SBCS page has at most 256 positions, many consumed by controls and invariant Latin syntax. It can therefore support:

- basic Latin letters and digits;
- one selected collection of accents, currency signs, punctuation, and national letters;
- a single non-Latin alphabet in specialized pages, often at the expense of other letters or symbols.

It cannot simultaneously encode the full repertoires of Latin, Cyrillic, Greek, Hebrew, Arabic, Indic scripts, CJK ideographs, historic scripts, mathematical symbols, and emoji. Nor does a byte encoding by itself provide:

- bidirectional layout;
- Arabic contextual shaping;
- Indic conjunct formation and reordering;
- normalization;
- grapheme-cluster boundaries;
- font selection;
- culturally correct collation.

Those are character-model, layout, and higher-level protocol matters.

### 9. Worked examples

All EBCDIC examples below explicitly use IBM037 unless stated otherwise.

#### “HELLO”

| Character | IBM037 | ASCII | UTF-8 |
|---|---:|---:|---:|
| H | `C8` | `48` | `48` |
| E | `C5` | `45` | `45` |
| L | `D3` | `4C` | `4C` |
| L | `D3` | `4C` | `4C` |
| O | `D6` | `4F` | `4F` |

```text
IBM037: C8 C5 D3 D3 D6
ASCII:  48 45 4C 4C 4F
UTF-8:  48 45 4C 4C 4F
```

#### “Hello, world!\n”

| Character | IBM037 | ASCII/UTF-8 |
|---|---:|---:|
| H | `C8` | `48` |
| e | `85` | `65` |
| l | `93` | `6C` |
| l | `93` | `6C` |
| o | `96` | `6F` |
| , | `6B` | `2C` |
| space | `40` | `20` |
| w | `A6` | `77` |
| o | `96` | `6F` |
| r | `99` | `72` |
| l | `93` | `6C` |
| d | `84` | `64` |
| ! | `5A` | `21` |
| newline | `15` | `0A` |

```text
IBM037: C8 85 93 93 96 6B 40 A6 96 99 93 84 5A 15
ASCII:  48 65 6C 6C 6F 2C 20 77 6F 72 6C 64 21 0A
UTF-8:  48 65 6C 6C 6F 2C 20 77 6F 72 6C 64 21 0A
```

If the mainframe object is a fixed or variable-length record, the final `15` may not be stored; the record boundary itself represents the line.

#### “£100”

```text
IBM037: B1 F1 F0 F0
ASCII:  not representable in seven-bit ASCII
UTF-8:  C2 A3 31 30 30
```

#### “€100”

IBM037 has no euro sign. CCSID 1140 is the Euro update of CCSID 37 and places `€` at `9F`, replacing the generic currency sign `¤`.

```text
IBM037:       not representable without substitution
IBM1140:      9F F1 F0 F0
UTF-8:        E2 82 AC 31 30 30
```

IBM documents the Euro pages as CCSIDs 1140–1149, corresponding to older national EBCDIC pages 37, 273, 277, 278, 280, 284, 285, 297, 500, and 871. **[D—current]** ([IBM supported CCSIDs](https://www.ibm.com/docs/en/developer-for-zos/17.0.x?topic=codegenproperty-supported-code-pages-ccsids))

#### Conversion ambiguity

In IBM037:

```text
BA = [
BB = ]
C0 = {
D0 = }
```

IBM’s table of variant characters shows that those same byte values display differently under IBM1047, IBM285, IBM293, IBM500, IBM297, and IBM273. Therefore:

```text
bytes + the word “EBCDIC” ≠ fully identified text
bytes + exact CCSID       = decodable text
```

**[D—current]** ([IBM variant characters](https://www.ibm.com/docs/en/cics-ts/6.x?topic=attributes-variant-characters))

---

## Origins

## 1. Before EBCDIC: telegraphy and punched cards

### Baudot and Murray

Émile Baudot’s five-unit telegraph code of the 1870s used shift states to obtain more symbols than five bits could directly represent. Donald Murray’s early-twentieth-century teleprinter adaptations rearranged assignments with mechanical efficiency and typing frequency in mind. The later CCITT International Telegraph Alphabet No. 2 preserved the Letters/Figures shift principle.

These codes are intellectual ancestors of all compact character coding but not a direct bitwise parent of EBCDIC. **[R—scholarly]**

### Hollerith

Herman Hollerith’s punched-card work began in the late nineteenth century and became foundational to IBM’s tabulating business. In the later 80-column IBM card, each column had twelve punch positions: rows 12, 11, 0, and 1–9. A character could be represented by a digit punch alone or a combination of a zone punch and digit punch.

Alphabetic groups naturally reflected zone combinations:

- one zone plus digits 1–9 for one run;
- another zone plus digits 1–9 for the next;
- a third pattern plus digits 2–9 for the final eight letters.

This is the material reason behind the familiar 9 + 9 + 8 grouping. **[R—scholarly, supported by IBM card-code structure]**

The common statement that the split exists simply because IBM engineers “forgot to make letters contiguous” is folklore. The organization instead preserved economically valuable compatibility with card equipment, sorting practices, and translation logic.

### BCD and BCDIC

IBM’s six-bit Binary-Coded Decimal family encoded 64 possible values. It served machines including the IBM 702/705 and 704-era families in differing variants. “BCD,” “BCDIC,” and “BCD interchange code” are sometimes used loosely in later sources; Mackenzie carefully distinguishes their structures and translation relationships.

Six bits could hold uppercase letters, digits, and limited punctuation, but not a generous mixed-case international repertoire. By the late 1950s, programming languages, communications, printers, and international interchange were pressing beyond 64 characters. **[R—scholarly]**

## 2. Bemer’s 256-character proposal

In September 1959, Robert W. Bemer published “A Proposal for a Generalized Card Code for 256 Characters,” *Communications of the ACM*, volume 2, number 9, pages 19–23. The paper is documentary evidence that Bemer advocated an eight-bit, 256-character approach before EBCDIC and ASCII were finalized. **[D—contemporary]** ([DBLP bibliographic entry](https://dblp.org/rec/journals/cacm/Bemer59.html), [NIST historical bibliography](https://nvlpubs.nist.gov/nistpubs/Legacy/MP/nbsmiscellaneouspub266.pdf))

It does **not**, by itself, establish that Bemer designed EBCDIC. His better documented role was in IBM programming standards and the American ASCII process, and he later became one of EBCDIC’s most forceful critics.

Attribution should therefore be stated as follows:

- IBM designed EBCDIC for System/360. **[D/R]**
- Bemer earlier argued for an eight-bit generalized card code and influenced character-code standardization. **[D]**
- Bemer was not shown by the sources examined to be EBCDIC’s sole designer. **[Absence-of-evidence finding]**
- No surviving IBM committee roster or design memorandum found in this research establishes a compact named “EBCDIC committee” comparable to ASA X3.2’s documented ASCII work.

## 3. ASCII develops in parallel

The American Standards Association’s X3 organization began formal work on a standard interchange code in 1961, principally through subcommittee X3.2. The first approved American Standard was ASA X3.4-1963.

Bemer represented IBM interests during important parts of this work and championed features including ESC. Hugh McGregor Ross worked on British and international code questions. Other participants and editors contributed materially; calling Bemer the sole “inventor of ASCII” is a journalistic simplification, though his influence was exceptional. **[D—committee records; P; R]**

The relationship is often misstated:

> EBCDIC is not “extended ASCII.”

Both matured in 1963–1964, but EBCDIC extended IBM’s BCD/card lineage while ASCII came through national communications and data-processing standardization.

Relevant neighboring standards were:

- **ASA X3.4-1963**: first ASCII standard;
- **USAS X3.4-1967/1968**: revised ASCII;
- **ECMA-6**: ECMA’s seven-bit coded character set, harmonized internationally;
- **ISO Recommendation R 646**, later **ISO/IEC 646**: seven-bit international code with national-use positions;
- **CCITT International Telegraph Alphabets**: telecommunications predecessors and contemporaries;
- later **ISO/IEC 2022**: mechanisms for code extension and designation.

None of these was the defining standard for IBM037. They form the rival interchange lineage.

## 4. The System/360 decision, 1963–1964

IBM formed its SPREAD task force in 1961 to plan a unified computer family. The eventual System/360 architecture, publicly announced April 7, 1964, standardized an eight-bit byte and unified scientific and commercial product lines. IBM identifies Gene Amdahl as chief architect and Fred Brooks, Bob Evans, and Erich Bloch as principal project leaders. **[D—IBM corporate history]** ([IBM System/360 history](https://www.ibm.com/history/system-360))

EBCDIC was devised inside IBM during 1963–1964 and announced with this system. Its design balanced:

- 256 code positions;
- continuation of IBM card and BCDIC relationships;
- uppercase and lowercase;
- decimal arithmetic and zoned-decimal conventions;
- printer, terminal, card, tape, and communications controls;
- rapid delivery of an enormous compatible hardware family.

### Why not ASCII?

There are several evidentiary layers.

#### What the architecture proves

Original System/360 architecture included an ASCII-mode bit in the Program Status Word affecting zoned-decimal operations. A System/360 Model 30 field-engineering manual describes decimal operations as occurring in EBCDIC mode when the bit was zero and ASCII mode when it was one. Later System/370 documentation says System/360 provided for USASCII-8 mode and that System/370 removed the corresponding meaning. **[D—contemporary]** ([System/360 Model 30 field manual](https://bitsavers.org/pdf/ibm/360/fe/2030/Y24-3360-1_2030_FE_Theory_Opns_Jun67.pdf), [System/370 Principles of Operation](https://bitsavers.org/pdf/ibm/370/princOps/GA22-7000-0_370_Principles_Of_Operation_Jun70.pdf))

This is strong evidence that ASCII support was seriously contemplated. It does not prove that the entire System/360 could switch all I/O and software transparently between the codes. Character interpretation was distributed among CPU instructions, peripheral hardware, translation tables, operating systems, and applications.

Modern z/Architecture documentation makes the broader point explicit: nearly all instructions process arbitrary byte values, so the architecture can process EBCDIC, ASCII, or another eight-bit code, even though it was originally designed to support EBCDIC. **[D—current]** ([z/Architecture Principles of Operation](https://www.ibm.com/docs/en/SSQ2R2_15.0.0/com.ibm.tpf.toolkit.hlasm.doc/dz9zr006.pdf))

#### Bemer’s account

In later interviews and autobiographical writings, Bemer said that Fred Brooks told him IBM’s printers and card equipment could not be made ready for ASCII in time. He described IBM’s retreat to EBCDIC with anger and portrayed it as a historic lost opportunity. **[P—recollection]**

This account was widely repeated by the 1999 CNN history of ASCII and later IEEE histories and blogs. The later telling is consistent with the unused architectural ASCII provision and the launch timetable, but the colorful dialogue rests substantially on Bemer’s recollection. **[Single-witness caution]** ([1999 CNN ASCII history copy](https://ptacts.uspto.gov/ptacts/public-informations/petitions/1461550/download-documents?artifactId=hhB8ZC9r_LcrvpsosB63OXTj_-tT_kff374Iel8lyTwRAmn4oZ7h0p0), [IEEE Computer Society Bemer profile](https://history.computer.org/pioneers/bemer.html))

#### Customer and installed-base explanations

Later recollections also say major IBM customers resisted losing card-code compatibility. That is economically plausible and consistent with the immense installed base, but the sources found here do not provide a single dated executive decision memorandum saying “customers forced EBCDIC.” **[P/R; not fully documented]**

#### “IBM invented EBCDIC to sabotage ASCII”

This is popular anti-IBM folklore. The evidence is less theatrical:

- IBM participated in ASCII standardization.
- System/360 retained an architectural ASCII-mode provision.
- ASCII’s finalization and peripheral readiness collided with the System/360 schedule.
- IBM nevertheless chose and shipped the proprietary family-compatible code.
- System/360’s enormous success then entrenched it.

IBM’s conduct can be criticized as producing incompatibility without assuming a conspiracy for which no primary decision record was found. **[Folklore versus documented record]**

## 5. Why eight bits?

The System/360’s eight-bit byte was large enough for:

- both Latin cases;
- digits and programming punctuation;
- controls;
- national or application variants;
- straightforward hexadecimal representation;
- packed and zoned decimal conventions.

Bemer’s 1959 paper is prior evidence for a 256-character card code, but “Bemer invented the eight-bit byte” is disputed. Werner Buchholz coined “byte” during IBM Stretch work in 1956, initially for a variable-sized group; System/360’s architectural success made the eight-bit byte dominant. The exact division of credit among antecedent proposals, Stretch, Bemer’s code work, and System/360 should not be collapsed into one first. **[Disputed credit; R]**

---

## Adoption and decline

## 1. Immediate adoption

System/360 orders exceeded IBM’s expectations and the architecture rapidly became the dominant business-computing platform. Software and data compatibility across the family gave EBCDIC an installed base no committee vote alone could dislodge. **[D—IBM; R]**

It spread through:

- OS/360 and successors;
- DOS/360;
- card readers and punches, including the IBM 029 ecosystem;
- line printers;
- magnetic tapes;
- 3270-family display terminals;
- CICS transaction processing;
- IMS and Db2;
- COBOL, PL/I, assembler, RPG, and mainframe Fortran environments;
- later System/370, 308x, 390, and z/Architecture systems;
- IBM midrange systems and IBM i;
- compatible or plug-compatible systems from other manufacturers.

RCA Spectra 70, ICL System 4, and compatible Fujitsu systems are commonly cited examples, but individual models and pages must be checked rather than assuming universal IBM037 compatibility. **[R]**

## 2. ASCII’s governmental and network victory

President Lyndon B. Johnson’s March 11, 1968 memorandum approved the US standard Code for Information Interchange as a federal standard. FIPS PUB 1, issued November 1, 1968, adopted ASCII and required computers and related configurations entering federal inventory on or after July 1, 1969 to have the capability to use it. The requirement was capability, not proof that every internal file must instantly be converted. **[D—contemporary]** ([FIPS PUB 1](https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub1.pdf), [Johnson memorandum](https://www.presidency.ucsb.edu/documents/memorandum-approving-the-adoption-the-federal-government-standard-code-for-information))

RFC 20, issued by Vint Cerf on October 16, 1969, specified seven-bit ASCII in an eight-bit byte with the high bit zero for ARPANET Host-Host primary connections. **[D—protocol]** ([RFC 20](https://www.rfc-editor.org/info/rfc20/))

These measures gave ASCII the decisive advantage in government procurement, minicomputers, terminals, Unix, and network protocols. EBCDIC remained powerful inside IBM installations but lost the contest to become the universal interchange code.

## 3. Conversion becomes an industry

Because EBCDIC was not an ASCII superset, conversion required a complete table rather than merely clearing a high bit. The recurring work included:

- identifying the exact source CCSID;
- translating graphic characters;
- deciding how to map controls;
- converting `15` or record boundaries to the target newline convention;
- distinguishing text fields from packed decimal and binary data;
- mapping bracket, brace, backslash, pipe, tilde, currency, and national letters;
- choosing substitution behavior for unmappable characters;
- preserving fixed record lengths;
- handling SO/SI and DBCS pairs;
- maintaining collation or deliberately changing it.

IBM still documents customizable EBCDIC-to-ASCII mappings. In one published conversion table, characters not representable in seven-bit ASCII become ASCII `1A` SUB. **[D—current]** ([IBM EBCDIC-to-ASCII table](https://www.ibm.com/docs/en/iis/11.3.0?topic=tables-ebcdic-ascii), [IBM customized mapping](https://www.ibm.com/docs/en/i/7.6.0?topic=support-customizing-ebcdic-ascii-code-page-mapping))

“ASCII-to-EBCDIC conversion” was therefore never one operation. A correct specification resembles:

```text
IBM037 record data
→ interpret RDW/fixed-record structure
→ convert selected text fields to Unicode
→ serialize as UTF-8 with CRLF or LF
```

not:

```text
translate every byte in the file
```

## 4. Code pages and CCSIDs

Important pages include:

| CCSID/page | Role |
|---:|---|
| 37 | US/Canada and several other Latin locales |
| 273 | Germany/Austria |
| 277 | Denmark/Norway |
| 278 | Finland/Sweden |
| 280 | Italy |
| 284 | Spain/Latin America |
| 285 | United Kingdom |
| 297 | France |
| 420 | Arabic |
| 424 | Hebrew |
| 500 | International EBCDIC |
| 838 | Thai |
| 870 | Latin-2 multilingual |
| 875 | Greek |
| 880 / 1025 | Cyrillic families |
| 930 | Japanese, Katakana-based mixed EBCDIC |
| 933 | Korean mixed EBCDIC |
| 935 | Simplified Chinese mixed EBCDIC |
| 937 | Traditional Chinese mixed EBCDIC |
| 939 | Japanese, Latin-based mixed EBCDIC |
| 1026 | Turkish |
| 1047 | Latin-1/Open Systems EBCDIC |
| 1140–1149 | Euro updates of major Western pages |
| 1200 | UTF-16 in IBM CCSID nomenclature |
| 1208 | UTF-8 |

IBM’s CCSID is not merely a synonym for “code page.” It identifies a coded representation, potentially combining a character set, code page, and encoding scheme. **[D—current]**

IBM1047 is especially significant to Unix System Services and open-systems source code because it places programming punctuation more conveniently than IBM037. Confusing 37 and 1047 commonly corrupts brackets and related symbols.

IANA registers IBM037, IBM500, IBM1047, and many other IBM names and aliases. IBM037’s aliases include `cp037`, `ebcdic-cp-us`, and `csIBM037`. **[D—registry]** ([IANA registry](https://www.iana.org/assignments/character-sets))

RFC 1345 catalogued many character sets and mnemonic representations and became an important source for IANA’s historical EBCDIC registrations. **[D—protocol catalogue]** ([RFC 1345](https://www.rfc-editor.org/rfc/rfc1345.html))

## 5. Unicode and Web-era decline

ISO/IEC 8859’s single-byte families and vendor PC pages solved portions of the international problem but remained mutually exclusive repertoires. Unicode and ISO/IEC 10646 ultimately provided a common coded character set.

The IETF’s January 1998 RFC 2277 required new protocols to be able to use UTF-8, subject to its standards-policy rules. RFC 3629 later restricted standard UTF-8 to Unicode scalar values through `U+10FFFF` and prohibited malformed and overlong representations. RFC 5198 defined a normalized UTF-8 format for network interchange. **[D—protocol]** ([RFC 2277](https://www.rfc-editor.org/info/rfc2277/), [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html), [RFC 5198](https://www.rfc-editor.org/info/rfc5198/))

The W3C recommends UTF-8 for Web documents. W3Techs—not the W3C—reported on September 11, 2026 that UTF-8 was used by 99.1% of websites whose encoding it could identify. The institutional names are often confused. **[D—current survey, with methodological limitation]** ([W3C encoding advice](https://www.w3.org/International/questions/qa-choosing-encodings.en), [W3Techs survey](https://w3techs.com/technologies/breakdown/en-utf8/ranking))

EBCDIC was never a serious native Web encoding. Gateways, HTTP servers, XML processors, Java runtimes, and database drivers on IBM systems normally convert at boundaries.

## 6. What survives

Current IBM documentation still says EBCDIC is typically used on IBM zSystems/z/OS and iSeries/System i. CICS continues to default some code-page-sensitive processing to CCSID 37; Db2 distinguishes EBCDIC, ASCII, and Unicode data; COBOL and assembler document SO/SI and DBCS behavior. **[D—current]**

Surviving domains include:

- decades-old application data;
- COBOL source and load workflows;
- VSAM and sequential datasets;
- CICS and IMS messages;
- Db2 EBCDIC tables;
- 3270 data streams;
- JES spool and print output;
- bank, insurance, government, airline, reservation, and logistics back ends;
- tape archives;
- intercompany batch files.

Claims such as “all banks run EBCDIC” or “airlines cannot function without EBCDIC” are exaggerations. Public evidence supports continuing IBM mainframe deployment in these sectors, but not a universal census of every institution’s internal CCSIDs. **[Modern generalization; evidence limited]**

---

## The other scripts

## 1. National Latin pages

EBCDIC’s first international strategy was substitution: keep common letters and digits stable while changing selected punctuation and accented positions for a country.

This produced practical local support but serious interchange costs:

- identical bytes could display as different symbols;
- source code containing brackets or currency characters could break;
- a file labeled only “EBCDIC” was under-specified;
- round trips through ASCII could lose characters;
- visually identical repertoire descriptions could use different positions.

The Euro pages demonstrate both adaptability and scarcity: IBM replaced the generic currency sign in established pages because there was no universally unused position.

## 2. Greek and Cyrillic

IBM supplied Greek pages such as 423 and 875, and Cyrillic pages including 880, 1025, 1123, and later Euro variants. A single-byte page can encode one selected alphabet plus controls and a Latin subset, but not every historic letter, combining mark, phonetic extension, minority-language requirement, and scholarly character.

National and vendor rivals included:

- ISO 8859-5 for Cyrillic;
- ISO 8859-7 for Greek;
- DOS and Windows pages;
- KOI7 and KOI8 families;
- Macintosh encodings;
- local standards.

The famous **KOI8 trick**—arranging Cyrillic so stripping the high bit produced a roughly readable Latin transliteration—is not an EBCDIC property. It illustrates a rival design optimized for degraded seven-bit channels. Calling it an EBCDIC feature is modern conflation.

## 3. Hebrew and Arabic

IBM420 and IBM918 served Arabic uses; IBM424 served Hebrew. Encoding the letters did not solve presentation.

Hebrew and Arabic require bidirectional processing when mixed with Latin and numbers. Arabic additionally requires joining and contextual glyph shaping. Legacy systems variously stored:

- logical order;
- visual display order;
- presentation-shaped forms;
- locally mirrored punctuation;
- terminal-dependent forms.

Consequently, conversion to Unicode is not always a direct table lookup. A converter may need to know whether the legacy data is logically ordered or already arranged for an old display.

Unicode later standardized the bidirectional algorithm and encoded Arabic base characters separately from most presentation behavior. EBCDIC pages predate that unified model. **[D/R]**

## 4. Indic scripts and Thai

Thai received host EBCDIC pages such as 838 and 1160. Indic scripts posed harder problems because consonant-vowel ordering, combining marks, conjuncts, and shaping do not map cleanly onto a simple Western one-byte typewriter model.

Vendor systems could encode selected characters, glyphs, or presentation forms, but interoperable rendering required higher-level rules. Unicode’s character model plus shaping engines eventually supplied a broader framework. EBCDIC itself contains no Indic shaping algorithm.

## 5. Chinese, Japanese, and Korean

Thousands of ideographs could not fit into an SBCS page. IBM therefore developed DBCS and mixed EBCDIC families:

- 930 and 939 for Japanese;
- 933 for Korean;
- 935 for Simplified Chinese;
- 937 for Traditional Chinese.

Mixed data uses SO `0E` and SI `0F`; pure graphic fields may rely on field metadata. The solution allowed mainframe applications to process CJK text but introduced statefulness, larger tables, language-specific CCSID combinations, and conversion complexity.

Japanese environments also faced competition from JIS X 0201, JIS X 0208, Shift_JIS, EUC-JP, and vendor extensions. Chinese environments used GB and Big5 families; Korean systems used national and vendor encodings. Unicode absorbed characters from these standards but did not preserve their byte layouts.

## 6. Emoji

No traditional EBCDIC SBCS page can represent modern emoji as a general repertoire. An IBM application normally stores or exchanges them in UTF-8, UTF-16, or another Unicode form, potentially using IBM CCSIDs 1208 or 1200.

Emoji’s origins in Japanese mobile-carrier sets and their later Unicode encoding are not part of EBCDIC’s design history. Emoji proposals and votes belong to the Unicode Technical Committee process. Treating EBCDIC’s lack of emoji as an original defect would be anachronistic; the relevant criticism is the continuing cost of fields whose schema still permits only a narrow legacy CCSID.

---

## People and institutions

### Herman Hollerith (1860–1929)

Developed punched-card tabulating machinery used for the 1890 US census and founded a business that ultimately became part of IBM. His card technology is EBCDIC’s deep material ancestor, although neither EBCDIC nor electronic stored-program computers existed in his lifetime. **[D/R]**

### Émile Baudot (1845–1903)

Developed a five-unit telegraph code and multiplex telegraph system. He belongs to the prehistory of coded communications and shift states, not EBCDIC’s direct design team. **[R]**

### Donald Murray (1865–1945)

Adapted five-unit telegraph coding for keyboard and printing machinery; his work influenced later teleprinter alphabets and CCITT ITA2. **[R]**

### Robert W. Bemer (1920–2004)

IBM manager for programming research and corporate logical-system standards; later at Univac, GE, and Honeywell. He published the 1959 generalized 256-character card-code proposal, participated in ASCII work, strongly advocated ESC, and later condemned IBM’s choice of EBCDIC. His autobiographical accounts are indispensable but should be labeled participant recollection. **[D/P]**

### Charles E. Mackenzie

IBM engineer and author of *Coded Character Sets: History and Development* (Addison-Wesley, 1980, ISBN 0-201-14460-3). His 513-page work is the fullest technical reconstruction located for BCDIC, EBCDIC, PTTC, ASCII, and punched-card translation relationships. It is a secondary history written by an expert with institutional proximity, not a contemporary EBCDIC design memorandum. **[R—scholarly]**

### Gene Amdahl (1922–2015)

Chief architect of System/360 according to IBM. This is not equivalent to being personally credited as EBCDIC’s table designer. **[D]**

### Frederick P. Brooks Jr. (1931–2022)

System/360 project leader and later author of *The Mythical Man-Month*. In Bemer’s recollection, Brooks communicated the peripheral-readiness reason for not shipping ASCII. The quotation is participant testimony, not an independently preserved 1964 transcript. **[P]**

### Bob Evans and Erich Bloch

Principal System/360 leaders named in IBM’s institutional history alongside Brooks; crucial to the platform that entrenched EBCDIC, but not individually established by the sources examined as authors of its table. **[D; absence-of-evidence caution]**

### Vint Cerf

Author of RFC 20 in 1969, specifying ASCII for early network interchange. His relevance is to the standard EBCDIC lost to in networking, not to EBCDIC’s internal design. **[D]**

### ASA/USASI/ANSI and X3

The American Standards Association became the United States of America Standards Institute and then ANSI. Its X3 organization produced ASCII through a committee process. Confusing that process with IBM’s EBCDIC development is historically inaccurate.

### ECMA and ISO

ECMA-6 and ISO 646 developed the international seven-bit lineage. ISO/IEC 2022 standardized extension techniques; ISO 8859 standardized later eight-bit single-byte families; ISO/IEC 10646 converged with Unicode. EBCDIC pages coexist with these standards but are not editions of them.

### IBM

IBM was EBCDIC’s creator, principal steward, and overwhelmingly important implementer. Its later Character Data Representation Architecture and CCSID system imposed disciplined identifiers on what had become a large code-page ecology.

### DEC, Bell Labs, Xerox, and Apple

These institutions matter mainly to the rival history:

- DEC’s minicomputers reinforced ASCII;
- Bell Labs’ Unix and C assumed ASCII-like properties in much software;
- Xerox researchers contributed to multilingual computing and influenced Unicode-era thinking;
- Apple was among the companies whose engineers participated in early Unicode work.

They were not EBCDIC’s designers.

### Unicode founders and editors

Unicode’s early institutional history includes Joe Becker of Xerox and Lee Collins and Mark Davis of Apple, among others. The Unicode Consortium was incorporated in 1991. Ken Whistler became one of its most important standards editors; Mark Davis became a long-serving president.

These people belong to EBCDIC’s replacement and conversion history, not its origin. Likewise, Ken Thompson and Rob Pike designed UTF-8 at Bell Labs in 1992. Pike’s later account of Thompson sketching the encoding on a placemat is a participant recollection with unusually direct provenance, but it has no role in EBCDIC’s 1963–1964 creation.

The placemat story should not be imported into EBCDIC’s origins merely because both are eight-bit encodings.

---

## Culture

## 1. “Plain text” was never plain

EBCDIC exposes the dependence of text on metadata. A byte sequence alone does not say:

- which EBCDIC page;
- which control convention;
- whether records supply newlines;
- whether fields are SBCS, mixed, or graphic DBCS;
- whether numeric-looking bytes are display text, zoned decimal, or packed decimal;
- whether visual-order Arabic/Hebrew is stored;
- whether a terminal data stream contains commands.

The Unix-era ideal of “plain text” often silently meant ASCII-compatible, line-oriented bytes. On a mainframe, a perfectly ordinary text dataset could be record-oriented EBCDIC without delimiters. Neither form is metaphysically plainer; each embeds different platform assumptions.

## 2. EBCDIC art

Character pictures printed on IBM line printers are sometimes retrospectively called ASCII art. If the source and printer chain used EBCDIC, “EBCDIC art” is technically more exact.

The cultural form depended as much on:

- printer character trains;
- overprinting;
- carriage-control characters;
- fixed-width typography;
- fanfold paper;
- line and page dimensions;

as on the character code. “ASCII art” later became a generic genre label, so both descriptions may appear in archives. **[Folklore/terminological drift]**

## 3. Hacker hostility

EBCDIC became a stock emblem of proprietary incompatibility in Unix culture. Common complaints focused on:

- noncontiguous letter ranges;
- digits following letters;
- variant punctuation;
- conversion tables;
- newline differences;
- IBM lock-in.

A 4.3BSD Reno-era fortune joked that EBCDIC would not die. **[Folklore, traceable by the 1990s]** Later retellings commonly render the idea as “EBCDIC is dead—long live EBCDIC.”

The joke is culturally revealing but not a usage statistic. EBCDIC survived because application data, operational procedures, hardware compatibility, and business risk survived.

## 4. Mojibake

“Mojibake” describes text displayed under the wrong encoding. EBCDIC produces an especially dramatic form because its letters are far from ASCII positions: an EBCDIC word opened as Windows-1252 does not merely lose accents; it becomes punctuation and accented gibberish.

Mojibake later became an intentional aesthetic in glitch art, online typography, demoscene work, and fiction. That aesthetic is modern; historical operators experienced the same underlying failures as damaged reports, bad tapes, terminal garbage, or mistranslation rather than under today’s Japanese-derived label.

## 5. Software assumptions

A surprising amount of portable software assumed ASCII arithmetic:

```c
digit = ch - '0';
uppercase = lowercase - 0x20;
is_letter = ch >= 'A' && ch <= 'Z';
```

The first expression happens to work for EBCDIC digits because `F0–F9` are contiguous. The case conversion and single-range alphabet tests do not. Standards-conforming C libraries provide functions such as `isalpha()` and `toupper()` partly so programs do not need to assume ASCII layout.

Conversely, mainframe software may assume:

- blank is `40`;
- digits carry an `F` zone;
- newline is `15`;
- records, not terminators, define lines;
- `0E/0F` switch DBCS state.

Porting fails in both directions when these assumptions remain implicit.

---

## Controversies and disputes

## 1. Who “designed EBCDIC”?

**Documented:** IBM devised it in 1963–1964 for System/360.

**Not established:** a single inventor, chair, or named committee with sole authorship.

**Often confused:** Bemer’s earlier 256-character card-code proposal and ASCII leadership.

**Assessment:** Credit IBM’s System/360-era development organization collectively unless a dated internal design record supplies narrower attribution. Bemer is a precursor and critic, not securely the sole EBCDIC designer. **[Open attribution]**

## 2. Was EBCDIC older than ASCII?

The answer depends on the verb:

- ASCII’s first approved standard, ASA X3.4-1963, predates System/360’s public announcement.
- EBCDIC design was underway in 1963 and 1964.
- Its BCDIC/card ancestors are much older.
- EBCDIC was not simply IBM’s settled production code long before ASCII.

“EBCDIC is older than ASCII” is therefore an imprecise modern slogan. Its ancestry is older; the named eight-bit EBCDIC and standardized ASCII were contemporaries. **[R]**

## 3. The unused System/360 ASCII bit

**Documented:** System/360 had a PSW mode related to ASCII-8 versus EBCDIC decimal operations; System/370 removed it.

**Overstatement:** “Flip one bit and the whole mainframe became ASCII.”

The bit affected defined CPU behavior, especially zoned decimal, not every peripheral, application, card code, literal, and operating-system table. **[D versus folklore]**

## 4. Bemer’s fury and Brooks’s explanation

Bemer’s story is a firsthand recollection later disseminated by interviews and popular histories. The hardware record corroborates that ASCII was contemplated, and the timetable explanation is plausible. No independent transcript of the reported 1964 conversation was found. **[P—single witness, partially corroborated]**

## 5. “EBCDIC was an eight-bit defense against ASCII”

This phrase appears in varying forms: IBM needed eight bits; IBM used the eighth bit to protect its installed base; IBM deliberately defeated a seven-bit public standard.

What is supported:

- EBCDIC used eight bits;
- card compatibility was a central structural concern;
- IBM shipped it instead of ASCII;
- the decision entrenched proprietary incompatibility.

What is not demonstrated by the located primary record:

- a formal IBM strategy document describing EBCDIC as an anti-ASCII weapon.

The “defense” formulation is best labeled an interpretive metaphor, sometimes hostile folklore, not a quotation from the design specification. **[Modern interpretation]**

## 6. Is EBCDIC badly designed?

Arguments against it:

- letters are split into blocks;
- punctuation differs across pages;
- raw collation surprises ASCII-trained programmers;
- controls and newline conventions are awkward in open interchange;
- it is not an ASCII superset;
- stateful DBCS recovery is fragile;
- page identification is essential.

Arguments in historical context:

- it preserved card and BCDIC relationships;
- digits and alphabetic runs suited IBM commercial processing;
- it provided 256 positions and both cases;
- fixed-width SBCS processing is simple;
- it permitted a rapid migration into a compatible system family;
- its persistence testifies to operational utility, though not universal elegance.

Calling it either “insane” or “perfectly optimal” substitutes present allegiance for historical requirements. **[Contested evaluation]**

## 7. Han unification

Han unification is a Unicode/ISO 10646 controversy, not an EBCDIC design controversy. Unicode assigns unified code points to characters judged to share an abstract Han identity across Chinese, Japanese, Korean, and sometimes Vietnamese traditions; fonts and locale determine glyph form.

Japanese objections have included:

- loss of glyph distinctions important to names and scholarship;
- discomfort with locale-dependent rendering;
- national standards’ distinctions being mapped together;
- political concern over which bodies define equivalence.

Defenses emphasize:

- character/glyph separation;
- finite encoding space and interoperability;
- preservation of distinctions where character identity differs;
- variation selectors and specialized mechanisms.

EBCDIC DBCS avoided “one universal Han repertoire” by using language- and market-specific pages, but that produced incompatible code spaces and conversion problems. It is therefore not a simple pre-Unicode solution that escaped politics.

## 8. Tibetan and other Unicode disputes

Tibetan encoding controversies concerned decomposition, ordering, compatibility, and representation of stacks in Unicode/ISO 10646. They postdate EBCDIC’s formation. Their relevance is comparative: every supposedly technical encoding decision can determine what users must treat as a character, sequence, glyph, or error.

No evidence was found that Tibetan disputes materially influenced EBCDIC’s original table. **[Absence-of-evidence finding]**

## 9. Emoji governance

Emoji proposals are reviewed through Unicode Consortium processes, with input from vendors and national/international standardization. Criticism focuses on:

- corporate influence;
- uneven representation;
- the difficulty of removing encoded symbols;
- culturally specific imagery;
- skin-tone, gender, family, flag, and identity choices.

The Consortium argues that encoding is based on interchange need and stability criteria, not endorsement. These controversies describe Unicode as a political institution; they do not retroactively attach to IBM’s 1964 code.

## 10. Security

### Homoglyphs

Unicode enables identifiers containing visually confusable characters from multiple scripts. EBCDIC’s smaller pages reduce the number of available confusables within one page but do not eliminate spoofing: `O/0`, `I/l/1`, punctuation variants, and terminal glyph differences remain.

Cross-system conversion may introduce new confusables or collapse distinct characters. Security therefore depends on identifier profiles and display policy, not on declaring one encoding “safe.”

### Overlong UTF-8

Early UTF-8 specifications permitted or insufficiently excluded forms in which one scalar value could have multiple byte sequences. Attackers could exploit inconsistent validation—for example, a filter rejecting canonical `/` while a downstream decoder accepted an overlong representation. RFC 3629 requires shortest-form encoding and restricts UTF-8 to `U+10FFFF`.

This is a UTF-8 controversy, not an EBCDIC one. SBCS EBCDIC has exactly one byte per code point within a page, but conversion chains can still disagree over controls, substitutes, and variant graphics.

### BOM

A byte-order mark is relevant to UTF-16/UTF-32 byte order and sometimes used as a UTF-8 signature. EBCDIC has no inherent BOM. An EBCDIC dataset’s identity usually comes from catalog metadata, a CCSID field, application convention, or external agreement.

Adding UTF-8 BOM bytes `EF BB BF` to an EBCDIC file does not identify it as EBCDIC and may be read as three EBCDIC characters. W3C documentation notes both BOM precedence and practical cautions. **[D—current]**

### Translation as a security boundary

EBCDIC conversion can become security-relevant when:

- a filter and parser use different CCSIDs;
- brackets, backslashes, or pipes change under the wrong page;
- a substitute character conceals rejected data;
- record boundaries are reconstructed differently;
- SO/SI is malformed;
- text conversion is mistakenly applied to binary fields;
- validation occurs before rather than after canonical Unicode conversion.

These are inference-backed engineering risks rather than a single named historical EBCDIC exploit class.

---

## Dedicated contested-material pass: findings

Searches were conducted for EBCDIC combined with *history*, *dispute*, *credit*, *controversy*, *ASCII bit*, *Bob Bemer*, *dead*, *mojibake*, *security*, and the Unicode controversies named in the brief.

The findings were:

1. **Origin credit remains collective.** IBM and 1963–1964 are well supported; a definitive individual EBCDIC inventor was not found.

2. **The ASCII-mode bit is real.** Contemporary manuals establish it. Claims that it transformed every aspect of the system are later exaggeration.

3. **Bemer’s confrontation story has one principal witness.** Later writers repeated it, but its dialogue and emotional detail trace primarily to Bemer.

4. **No documentary “anti-ASCII conspiracy” was found.** Schedule, peripherals, compatibility, and commercial inertia explain the outcome without requiring one.

5. **The letter blocks reflect punched-card structure.** The claim is supported by technical reconstruction, although popular accounts sometimes embellish the physical explanation with an unsupported claim that adjacent holes would have destroyed cards.

6. **“EBCDIC is dead” is recurrent folklore, disproved as a literal claim by current IBM product documentation.** Its real meaning is usually “EBCDIC has lost general-purpose interchange.”

7. **Han, Tibetan, emoji, BOM, and overlong UTF-8 controversies are not EBCDIC-origin controversies.** They belong in a comparative dossier only insofar as Unicode replaced the code-page model.

8. **No EBCDIC equivalent of the Thompson–Pike placemat story was found.** Importing that anecdote would be modern invention.

9. **No primary evidence was found for a single moment at which the banking or airline industries mandated EBCDIC.** Adoption followed IBM platforms and applications rather than one industry-wide standard.

10. **“EBCDIC art” is historically plausible but sparsely catalogued as a separate genre.** Much period output is archived under the generic label “ASCII art” or “printer art.”

---

## Open questions

1. Which surviving IBM records identify the individual engineers who assigned every original EBCDIC position?

2. Is there an extant 1963–1964 design memo recording the final EBCDIC-versus-ASCII decision, its signatories, rejected alternatives, and delivery constraints?

3. Can Bemer’s account of his conversation with Brooks be corroborated through Brooks’s papers, IBM correspondence, or another participant?

4. Which precise original System/360 announcement manual first printed the final EBCDIC table, and did prerelease editions differ?

5. How many original System/360 peripherals implemented any operational ASCII mode, as opposed to the CPU’s decimal-mode provision?

6. Which EBCDIC control assignments changed between the first System/360 manuals, IBM’s later CECP pages, CDRA, and current Unicode mappings?

7. How should archives preserve record structure, CCSID, device controls, and mixed binary/text schemas so that “conversion to UTF-8” does not destroy semantics?

8. How much production data remains in each EBCDIC CCSID? IBM documents support, but no credible public worldwide inventory was found.

9. Which printer-art and demoscene archives can establish a continuous, self-identified EBCDIC-art tradition rather than retrospective relabeling?

10. Which “EBCDIC is dead” joke is earliest? A 1990-era Unix fortune is readily traceable, but earlier oral or printed versions may exist.

---

## Sources

### Primary and institutional sources

- IBM, “The IBM System/360”:  
  https://www.ibm.com/history/system-360

- IBM, *z/Architecture Principles of Operation*:  
  https://www.ibm.com/docs/en/SSQ2R2_15.0.0/com.ibm.tpf.toolkit.hlasm.doc/dz9zr006.pdf

- IBM, *System/360 Model 30 Field Engineering Theory of Operation*, Y24-3360-1:  
  https://bitsavers.org/pdf/ibm/360/fe/2030/Y24-3360-1_2030_FE_Theory_Opns_Jun67.pdf

- IBM, *System/370 Principles of Operation*, GA22-7000-0, June 1970:  
  https://bitsavers.org/pdf/ibm/370/princOps/GA22-7000-0_370_Principles_Of_Operation_Jun70.pdf

- IBM, “EBCDIC,” Db2 for z/OS documentation, including IBM037 table:  
  https://www.ibm.com/docs/en/db2-for-zos/13.0.0?topic=schemes-ebcdic

- IBM, “Runtime Character Set”:  
  https://www.ibm.com/docs/en/i/7.4.0?topic=considerations-runtime-character-set

- IBM, “Character Tables”:  
  https://www.ibm.com/docs/en/z-netview/6.3.0?topic=processing-character-tables

- IBM, “EBCDIC collating sequence”:  
  https://www.ibm.com/docs/en/zos/3.1.0?topic=sequences-ebcdic

- IBM, “Variant characters”:  
  https://www.ibm.com/docs/en/cics-ts/6.x?topic=attributes-variant-characters

- IBM, “Supported code pages (CCSIDs)”:  
  https://www.ibm.com/docs/en/developer-for-zos/17.0.x?topic=codegenproperty-supported-code-pages-ccsids

- IBM, “Host supported code pages”:  
  https://www.ibm.com/docs/en/applinx/12.1.0?topic=reference-host-supported-code-pages

- IBM, “EBCDIC to ASCII”:  
  https://www.ibm.com/docs/en/iis/11.3.0?topic=tables-ebcdic-ascii

- IBM, “Customizing EBCDIC-to-ASCII code page mapping”:  
  https://www.ibm.com/docs/en/i/7.6.0?topic=support-customizing-ebcdic-ascii-code-page-mapping

- IBM, “SHIFT-OUT and SHIFT-IN”:  
  https://www.ibm.com/docs/en/cobol-zos/6.5.0?topic=registers-shift-out-shift-in

- IBM, “Double-byte character set notation”:  
  https://www.ibm.com/docs/en/hla-and-tf/1.6.0?topic=introduction-double-byte-character-set-notation

- IBM, “DBCS: general description”:  
  https://www.ibm.com/docs/en/cics-ts/6.x?topic=support-dbcs-general-description

- IBM, “Mixed DBCS/EBCDIC fields”:  
  https://www.ibm.com/docs/en/ims/15.5.0?topic=messages-mixed-dbcs-ebcdic-fields

- IBM, “DBCS field data types”:  
  https://www.ibm.com/docs/en/i/7.6.0?topic=considerations-dbcs-field-data-types

- IANA, “Character Sets” registry:  
  https://www.iana.org/assignments/character-sets

- IANA, additional character-set registrations:  
  https://www.iana.org/assignments/charset-reg

- Unicode Consortium, CP037, CP500, and related mapping files:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/EBCDIC/

- Vint Cerf, RFC 20, *ASCII Format for Network Interchange*, October 16, 1969:  
  https://www.rfc-editor.org/info/rfc20/

- Keld Simonsen, RFC 1345, *Character Mnemonics and Character Sets*, June 1992:  
  https://www.rfc-editor.org/rfc/rfc1345.html

- Harald Alvestrand, RFC 2277, *IETF Policy on Character Sets and Languages*, January 1998:  
  https://www.rfc-editor.org/info/rfc2277/

- François Yergeau, RFC 3629, *UTF-8, a Transformation Format of ISO 10646*, November 2003:  
  https://www.rfc-editor.org/rfc/rfc3629.html

- John Klensin and Melinda Whistler, RFC 5198, *Unicode Format for Network Interchange*, March 2008:  
  https://www.rfc-editor.org/info/rfc5198/

- National Bureau of Standards, FIPS PUB 1, *Code for Information Interchange*, November 1, 1968:  
  https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub1.pdf

- Lyndon B. Johnson, “Memorandum Approving the Adoption by the Federal Government of a Standard Code for Information Interchange,” March 11, 1968:  
  https://www.presidency.ucsb.edu/documents/memorandum-approving-the-adoption-the-federal-government-standard-code-for-information

- NIST, “ITL History Timeline”:  
  https://www.nist.gov/itl/about-itl/itl-history-timeline-1950-present

- CIA/NBS archival memorandum, “Formation and First Meeting of Working Group on Transition to Federal ADP Standards,” July 1, 1968:  
  https://www.cia.gov/readingroom/document/cia-rdp78-04723a000100150023-5

- W3C, “Declaring character encodings in HTML”:  
  https://www.w3.org/International/questions/qa-html-encoding-declarations.en

- W3C, “Choosing and applying a character encoding”:  
  https://www.w3.org/International/questions/qa-choosing-encodings.en

- W3C, “Who uses Unicode?”:  
  https://www.w3.org/International/questions/qa-who-uses-unicode.en.html

- W3C, HTML 4.01, “Document Representation”:  
  https://www.w3.org/TR/html401/charset.html

- W3Techs, UTF-8 usage survey:  
  https://w3techs.com/technologies/breakdown/en-utf8/ranking

### Historical studies and participant material

- Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley, 1980, ISBN 0-201-14460-3, scan:  
  https://hcs64.com/files/Mackenzie%20-%20Coded%20Character%20Sets%20History%20and%20Development.pdf

- Mackenzie bibliographic and lending record, Internet Archive/Open Library:  
  https://openlibrary.org/books/OL4570655M/Coded_character_sets

- Mackenzie Google Books record and contents:  
  https://books.google.com/books/about/Coded_Character_Sets.html?id=6-tQAAAAMAAJ

- Robert W. Bemer, “A Proposal for a Generalized Card Code for 256 Characters,” *Communications of the ACM* 2(9), September 1959, pp. 19–23, bibliographic record:  
  https://dblp.org/rec/journals/cacm/Bemer59.html

- NIST, *Computer Literature Bibliography 1946 to 1963*, including Bemer’s paper:  
  https://nvlpubs.nist.gov/nistpubs/Legacy/MP/nbsmiscellaneouspub266.pdf

- IEEE Computer Society, “Computer Pioneers—Robert W. Bemer”:  
  https://history.computer.org/pioneers/bemer.html

- IEEE Computer Society, Bemer profile PDF and bibliography:  
  https://history.computer.org/pioneers/pdfs/B/Bemer.pdf

- Bemer historical papers in the Computer History Museum collection:  
  https://archive.computerhistory.org/resources/access/text/2021/04/102785423-05-03-acc.pdf

- Computer History Museum, Bemer historical file:  
  https://archive.computerhistory.org/resources/access/text/2019/02/102785380-05-01-acc.pdf

- 1999 CNN account of ASCII and Bemer’s System/360 recollection, preserved copy:  
  https://ptacts.uspto.gov/ptacts/public-informations/petitions/1461550/download-documents?artifactId=hhB8ZC9r_LcrvpsosB63OXTj_-tT_kff374Iel8lyTwRAmn4oZ7h0p0

- Engineering and Technology History Wiki, “ASCII”:  
  https://ethw.org/ASCII

- Paul E. Ceruzzi, *A History of Modern Computing*, second edition, scanned copy consulted for context:  
  https://pdfarchive.kunaldawn.com/archive/computer_engineering/A_History_of_Modern_Computing_History_of_Computing_2nd_-_Paul_E_Ceruzzi.pdf

- “The Evolution of Character Codes, 1874–1968,” bibliography and archival references:  
  https://citeseerx.ist.psu.edu/document?doi=0ffa27720b572a9efdba6425b8e9a7c885a14c0d&repid=rep1&type=pdf

### Indexes and folklore leads checked but not treated as primary authority

- Wikipedia, “EBCDIC”:  
  https://en.wikipedia.org/wiki/EBCDIC

- Computer History Wiki, “Extended Binary Coded Decimal Interchange Code”:  
  https://gunkies.org/wiki/Extended_Binary_Coded_Decimal_Interchange_Code

- Google Groups archive, “Origins of EBCDIC”:  
  https://groups.google.com/g/comp.society.folklore/c/ZdjGnCUU5WU

- Steve Bellovin, historical commentary on System/360 character-code choices:  
  https://www.cs.columbia.edu/~smb/blog/control/index.html

- LongEx Mainframe Quarterly, “Lost in Translation 1—EBCDIC Code Pages”:  
  https://www.longpelaexpertise.com.au/ezine/LostinTranslation1.php

- FTI Consulting, “Reviving Data’s Dead Language: EBCDIC”:  
  https://www.fticonsulting.com/insights/fti-journal/reviving-datas-dead-language-ebcdic
