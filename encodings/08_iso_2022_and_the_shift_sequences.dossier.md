# ISO 2022 and the escape-sequence encodings: Research Dossier

> **Standard:** ISO/IEC 2022:1994; technically identical to ECMA-35, sixth edition  
> **First edition:** ISO 2022:1973, preceded by ECMA-35:1971  
> **Bit width:** Framework for both 7-bit and 8-bit coded streams; designated graphic sets may be single-byte or fixed-length multibyte sets  
> **Repertoire:** No single repertoire. It selects registered C0/C1 control sets and G0–G3 graphic sets, including 94-, 96-, 94ⁿ-, and 96ⁿ-character sets  
> **Current status:** ISO/IEC 2022:1994 remains published, with Corrigendum 1:1999; ISO/IEC TR 2375:2024 preserves the former escape-sequence register. General-purpose use is legacy. ISO-2022-JP remains supported for Web and email compatibility; new Internet and Web content is expected to use UTF-8  
> **Principal surviving profiles:** ISO-2022-JP and descendants; some ISO-2022-KR/CN archival data; MARC-8, DICOM extended repertoires, terminal control syntax, and specialized bibliographic or broadcast systems  
> **As-of date:** 15 September 2026

## Evidentiary notation

Every substantive historical or technical claim below carries one of these labels:

- **[STD]** Normative standard, RFC, registration, or official specification.
- **[DOC]** Contemporary documentary evidence: manual, memorandum, committee document, source code, or registry.
- **[REC]** Participant recollection or oral history.
- **[SCH]** Scholarly or careful historical reconstruction.
- **[DISPUTED]** A claim for which sources assign credit or interpret events differently.
- **[FOLKLORE]** A widely repeated story not fully established by surviving contemporary evidence.
- **[MODERN]** A later cultural interpretation, metaphor, or retrospective usage.
- **[INFERENCE]** A conclusion reconstructed from several sources rather than stated directly in one.

“ISO 2022” without a hyphen means the ISO/IEC framework. Names such as “ISO-2022-JP” identify particular Internet encoding profiles; they are not synonymous with the whole standard.

---

## Basic identification

### What ISO 2022 is

**[STD]** ISO/IEC 2022 is not a character repertoire comparable to ASCII, ISO 8859-1, or Unicode. It is a structural framework for constructing 7-bit and 8-bit coded-character streams from separately defined graphic and control sets. Its core operations are:

1. **Designation:** associate a registered character set with one of four registers, G0, G1, G2, or G3.
2. **Invocation:** select which designated register currently interprets bytes in the graphic area.
3. **Single shift:** invoke one character from G2 or G3 without changing the lasting shift state.
4. **Locking shift:** change the active register until another shift occurs.
5. **Code switching:** announce or enter another coding system.

The current standard explicitly warns that these codes are designed for sequential forward processing. Random access, reverse traversal, and fixed-record processing may require special handling. That warning is the standard’s own concise statement of the central defect of stateful encodings. [ISO catalogue](https://www.iso.org/standard/22747.html), [ISO online text](https://www.iso.org/obp/ui?_escaped_fragment_=iso:std:iso-iec:2022:ed-4:v1:en), [ECMA-35 PDF](https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf).

### Editions and equivalents

**[STD]**

| Date | Document | Significance |
|---|---|---|
| December 1971 | ECMA-35, first edition | First published ECMA code-extension framework |
| 1973 | ISO 2022:1973 | First ISO edition, *Code extension techniques for use with the ISO 7-bit coded character set* |
| 1974 | ANSI X3.41-1974 | Closely corresponding American code-extension standard |
| 1980 | ECMA-35, second edition | Extended revision |
| 1982 | ECMA-35, third edition | Further revision |
| March 1985 | ECMA-35, fourth edition | Text later made identical to ISO 2022:1986 |
| 1986 | ISO 2022:1986, third ISO edition | Added or consolidated 7- and 8-bit structures |
| June 1993 | ECMA-35, fifth edition | Transitional revision |
| December 1994 | ECMA-35, sixth edition; ISO/IEC 2022:1994 | Current base text; substantially reorganized |
| 1999 | ISO/IEC 2022:1994/Cor.1 | Corrigendum |
| 2024 | ISO/IEC TR 2375:2024 | Preserves registered escape sequences and sets formerly maintained under ISO 2375 |

ECMA says its 1985 text was identical to ISO 2022:1986 and that its 1994 sixth edition is fully identical to ISO/IEC 2022:1994. ISO says the 1994 edition was prepared as ECMA-35 and fast-tracked through ISO/IEC JTC 1. [ECMA-35 archive](https://ecma-international.org/publications-and-standards/standards/ecma-35/), [ISO foreword](https://www.iso.org/obp/ui?_escaped_fragment_=iso:std:iso-iec:2022:ed-4:v1:en), [ISO/IEC TR 2375:2024](https://www.iso.org/standard/85288.html).

**[STD]** National or regional counterparts have included ANSI X3.41, JIS X 0202, and GB/T 2311. The framework also underlies parts of ISO/IEC 4873, ISO/IEC 10367, ISO 8859, and the registered repertoire system administered under ISO 2375.

### Status in 2026

**[STD]** ISO’s catalogue still marks ISO/IEC 2022:1994 as published rather than withdrawn. That means it remains a valid standard, not that ISO recommends it for new general-purpose text systems. [ISO catalogue](https://www.iso.org/standard/22747.html).

**[STD]** The Web Encoding Standard defines a precise compatibility decoder and encoder for ISO-2022-JP, and HTML user agents must support that named encoding. At the same time, W3C authoring guidance says documents must not use ISO-2022-based encodings and should use UTF-8. [WHATWG Encoding](https://encoding.spec.whatwg.org/), [HTML parsing requirements](https://html.spec.whatwg.org/multipage/parsing.html), [W3C encoding guidance](https://www.w3.org/International/questions/qa-choosing-encodings).

**[DOC]** W3Techs reported on 11 September 2026 that UTF-8 was used by 99.1% of sites whose encoding it could determine. This is a survey of detectable public websites, not a census of email archives, local files, terminals, medical records, or library databases. [W3Techs](https://w3techs.com/technologies/breakdown/en-utf8/ranking).

---

# The code in detail

## The conceptual machine

ISO 2022 should be pictured as six named registers feeding four byte regions:

| Register or area | 7-bit representation | 8-bit representation | Purpose |
|---|---:|---:|---|
| CL | `00–1F` | `00–1F` | C0 controls |
| GL | `20–7F` | `20–7F` | Invoked G set on the left |
| CR | — | `80–9F` | C1 controls, if represented directly |
| GR | — | `A0–FF` | Invoked G set on the right |
| G0 | usually available to GL | may be invoked to GL | 94 or 94ⁿ graphics |
| G1–G3 | invoked by shifts | may be invoked to GL or GR | 94/96 or multibyte graphics |

**[STD]** The C0 set occupies columns 00 and 01. C1 occupies columns 08 and 09 in an 8-bit code, or its functions can be represented in 7-bit form as `ESC Fe`. G0 is a 94- or 94ⁿ-character set. G1–G3 may be 94-, 96-, 94ⁿ-, or 96ⁿ-character sets. [ECMA-35 §7 and Table 1](https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf).

### The 7-bit layout

```text
Hex       00–1F          20           21–7E            7F
          ┌──────────────┬────────────┬────────────────┬─────────┐
Meaning   │ C0 / CL      │ SPACE or   │ GL: active     │ DELETE  │
          │ controls     │ 96-set pos │ G0–G3 graphics │ or set  │
          └──────────────┴────────────┴────────────────┴─────────┘
```

Only one graphic register is invoked into GL at a time in a 7-bit stream.

### The 8-bit layout

```text
Hex       00–1F     20–7F       80–9F      A0–FF
          ┌────────┬────────────┬──────────┬────────────┐
Meaning   │ C0/CL  │ GL         │ C1/CR    │ GR         │
          │        │ active G   │ or unused│ active G   │
          └────────┴────────────┴──────────┴────────────┘
```

At most two G registers can be invoked simultaneously in the ordinary 8-bit structure: one in GL and one in GR.

## 94- and 96-character sets

**[STD]**

- A one-byte **94-set** uses `21–7E` in GL or `A1–FE` in GR.
- A one-byte **96-set** uses `20–7F` in GL or `A0–FF` in GR.
- A two-byte **94²-set** has up to 8,836 positions: both bytes are `21–7E` or both are `A1–FE`.
- More generally, 94ⁿ and 96ⁿ sets are allowed.

For a 94-set invoked in GL, `20` remains SPACE and `7F` remains DELETE. A 96-set consumes those positions, so ordinary SPACE and DELETE are not representable while that 96-set remains invoked there. [ECMA-35 §§6.3, 8.3, 9.3](https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf).

This explains why JIS X 0208, GB 2312, and KS X 1001 naturally appear as 94×94 grids: byte one selects a row and byte two a cell, each numbered 1–94 and transmitted as that number plus `0x20`.

## Designation versus invocation

This distinction is essential.

- **Designation** loads a set into G0, G1, G2, or G3.
- **Invocation** makes one of those registers active in GL or GR.

An escape sequence such as `ESC $ ) C` can designate KS X 1001 into G1 without immediately printing Korean. `SO` then invokes G1 in GL; `SI` returns GL to G0.

By contrast, ISO-2022-JP commonly designates a double-byte set directly into G0. Because G0 is already active in GL, designation effectively changes the meaning of following bytes immediately. This is why its familiar `ESC $ B` is often colloquially described as “switch to Japanese,” although the formal operation is “designate JIS X 0208-1983 to G0.”

## Escape-sequence grammar

**[STD]** An ISO 2022 escape sequence has:

```text
ESC I...I F
```

where:

- `ESC` is byte `1B`;
- every intermediate byte `I` is in `20–2F`;
- the final byte `F` is in `30–7E`;
- the sequence contains at least ESC plus a final byte.

Bytes `00–1F`, `7F`, and, in an 8-bit code, `80–FF`, cannot be intermediate or final bytes. The meaning is determined by the intermediate byte or bytes and the final byte, not by whatever graphics those bytes display as individually. [ECMA-35 §13](https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf).

Frequently encountered designation forms are:

| Sequence form | Meaning |
|---|---|
| `ESC ( F` | Designate a 94-set to G0 |
| `ESC ) F` | Designate a 94-set to G1 |
| `ESC * F` | Designate a 94-set to G2 |
| `ESC + F` | Designate a 94-set to G3 |
| `ESC - F` | Designate a 96-set to G1 |
| `ESC . F` | Designate a 96-set to G2 |
| `ESC / F` | Designate a 96-set to G3 |
| `ESC $ ( F` | Designate a multibyte 94-set to G0 |
| `ESC $ ) F` | Designate a multibyte 94-set to G1 |
| `ESC $ * F` | Designate a multibyte 94-set to G2 |
| `ESC $ + F` | Designate a multibyte 94-set to G3 |

**[STD]** Three early multibyte G0 registrations retain shorter forms `ESC $ F`; ECMA-35 explicitly identifies this as a historical exception created when its first edition permitted multibyte sets only in G0. That exception produced the famous Japanese `ESC $ @`, `ESC $ A`, and `ESC $ B` patterns. [ECMA-35 §14.3.3 note 46](https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf).

## Shift functions

| Function | 7-bit bytes | 8-bit form | Effect |
|---|---:|---:|---|
| SI / LS0 | `0F` | `0F` | Invoke G0 in GL |
| SO / LS1 | `0E` | `0E` | Invoke G1 in GL |
| LS2 | `ESC n` = `1B 6E` | same | Invoke G2 in GL |
| LS3 | `ESC o` = `1B 6F` | same | Invoke G3 in GL |
| SS2 | `ESC N` = `1B 4E` | often `8E` | Use one character from G2 |
| SS3 | `ESC O` = `1B 4F` | often `8F` | Use one character from G3 |
| LS1R | `ESC ~` = `1B 7E` | same | Invoke G1 in GR |
| LS2R | `ESC }` = `1B 7D` | same | Invoke G2 in GR |
| LS3R | `ESC \|` = `1B 7C` | same | Invoke G3 in GR |

**[STD]** SS2 or SS3 affects only the immediately following one-byte or fixed-length multibyte graphic character; the former shift state then resumes. Locking shifts persist. [ECMA-35 §§7.3, 8.4, 9.4](https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf).

## C0 and C1 controls

**[STD]** ISO 2022 provides slots and invocation rules, not one compulsory complete list of control meanings. In the most familiar ASCII/ISO 6429 environment:

- `00` is NUL.
- `09` is horizontal tab.
- `0A` is LF.
- `0D` is CR.
- `0E` and `0F` are SO and SI.
- `1B` is ESC.
- `7F` is DEL.
- In an 8-bit representation, C1 can occupy `80–9F`.
- In 7-bit form, C1 functions are represented as `ESC 40` through `ESC 5F`.

The C1 mapping is the reason `ESC [` is the 7-bit representation of CSI, Control Sequence Introducer: the corresponding 8-bit C1 byte is `9B`.

## Newline, space, deletion, and case

### Newline

**[STD]** ISO 2022 itself does not decree one universal file newline. Profiles do. Internet profiles use the Internet convention CRLF, bytes `0D 0A`. RFC 1468’s grammar explicitly defines CRLF for ISO-2022-JP. RFC 5198 later retained CRLF for Net-Unicode. [RFC 1468](https://www.rfc-editor.org/rfc/rfc1468.html), [RFC 5198](https://www.rfc-editor.org/rfc/rfc5198.html).

Unix files commonly use LF alone; classic Mac systems used CR; these are surrounding system conventions rather than alternative ISO 2022 graphic characters.

### Space

**[STD]** With a 94-set active in GL, byte `20` remains SPACE. With a 96-set active in GL, it is the set’s first position instead. Restricted profiles often require a reset before SPACE precisely to make seeking and line processing less ambiguous. ISO-2022-JP-2 requires a switch to ASCII or JIS Roman before an ordinary space or most controls. [RFC 1554](https://www.rfc-editor.org/rfc/rfc1554.html).

### Deletion

**[STD]** With a 94-set active in GL, `7F` is DELETE, inherited from the 7-bit environment. DEL historically meant a punched-tape character whose all-one holes could obliterate a previous character; ISO 2022 preserves the position structurally. In a 96-set invoked over GL, `7F` instead belongs to that set.

### Case

**[STD]** The framework has no uppercase/lowercase rule and no case-folding operation. Case depends on the designated repertoire. ASCII supplies separate uppercase and lowercase ranges; JIS X 0208 supplies many Japanese characters for which Latin case is irrelevant; Hebrew and Arabic have no uppercase/lowercase distinction; Greek and Cyrillic registered sets can include case pairs.

Charset labels such as `ISO-2022-JP` are case-insensitive in Internet registries; encoded text is not.

## Repertoire and expressiveness

**[STD]** The abstract framework can address a very large collection of registered sets, but a concrete stream can use only sets allowed by its profile and understood by both parties.

Thus:

- ISO-2022-JP cannot encode arbitrary Unicode.
- Original ISO-2022-JP covers ASCII, JIS X 0201 Roman, JIS X 0208-1978, and JIS X 0208-1983.
- It excludes JIS X 0201 half-width kana in the RFC 1468 profile.
- ISO-2022-JP-2 adds JIS X 0212, GB 2312, KS C 5601, and selected ISO 8859 sets.
- ISO-2022-KR covers ASCII plus KS C 5601-1987.
- ISO-2022-CN covers ASCII, GB 2312, and the first two CNS 11643 planes.
- ISO-2022-CN-EXT adds further GB and CNS sets.

Emoji, most historic scripts, arbitrary mathematical characters, and most later CJK additions cannot be expressed in those classic profiles. One could formally use ISO 2022’s “designate other coding system” machinery to enter a Unicode transformation format, but at that point Unicode, not the original G-set repertoire, carries the characters.

## Collating order

**[STD]** ISO 2022 does not define a universal linguistic collation. Binary sorting compares encoded bytes and therefore also compares escape sequences, designation choices, and state changes. Two byte strings may display the same characters while sorting differently because they use different redundant designations.

**[INFERENCE]** Consequently, bytewise sorting of unrestricted ISO 2022 data is not even reliably equivalent to sorting by abstract character sequence. Applications must decode first and apply a repertoire- and language-aware collation. This problem is stronger than ASCII’s merely crude binary order.

## Error behavior and synchronization

### Inside escape sequences

**[STD]** Because intermediate bytes occupy `20–2F` and finals `30–7E`, a parser can recognize the end of a syntactically valid escape sequence when it reaches the first final byte. ECMA-35 says forbidden bytes may occur through error but leaves recovery policy to the application.

### Inside multibyte graphics

For a 94² set, each graphic consumes two bytes from `21–7E`. A lost or inserted byte reverses byte-pair alignment until a control or escape transition is recognized. Because lead and trail bytes occupy the same range, their roles cannot be inferred locally.

### Lost state

A reader beginning in the middle of:

```text
1B 24 42 24 22 24 24 ...
```

cannot know from `24 22 24 24` alone whether those bytes mean ASCII punctuation (`$"$$`) or Japanese double-byte cells (`あい`). It needs earlier state or a later reset.

### Recovery boundaries

**[STD]** ISO-2022-JP was deliberately profiled to improve recovery:

- starts in ASCII;
- must return to ASCII at the end of each line;
- must end in ASCII;
- SI and SO are prohibited;
- Japanese bytes come in explicit two-byte segments;
- ESC remains recognizable because it lies outside `21–7E`.

RFC 1468 therefore permits line-by-line recovery after a lost or corrupted previous line. ISO-2022-JP-2 similarly clears relevant state at line boundaries and explains that random-seeking applications may assume lines begin in ASCII. [RFC 1468](https://www.rfc-editor.org/rfc/rfc1468.html), [RFC 1554](https://www.rfc-editor.org/rfc/rfc1554.html).

**[INFERENCE]** These reset rules mitigate but do not eliminate fragility. Corruption inside a line can reinterpret every following printable byte until the next recognized escape sequence or newline reset. A maliciously inserted ESC can change the interpretation of subsequent syntax.

### Comparison with UTF-8

UTF-8 continuation bytes have the distinct form `10xxxxxx`, so a reader can find a new character boundary after skipping at most a few bytes. ISO 2022’s ordinary data bytes do not identify the current set or their position within a pair. UTF-8 is therefore locally self-synchronizing in a way a general ISO 2022 stream is not.

That property, ASCII byte compatibility, stateless substring behavior, absence of byte-order dependence, and universal repertoire are central reasons UTF-8 displaced escape-switched encodings in general software.

---

# Worked examples

## Example 1: `ABCあいうえde 12かきく\n`

This example is documented byte-for-byte by a Japanese teaching source; the annotations below correct its two accidentally reversed prose labels for `ESC $ B` and `ESC ( B`. [Documented example](https://www.seiai.ed.jp/sys/text/cs/chp02/c02a020.html).

### ISO-2022-JP

```text
41 42 43
1B 24 42
24 22 24 24 24 26 24 28
1B 28 42
64 65 20 31 32
1B 24 42
24 2B 24 2D 24 2F
1B 28 42
0A
```

Byte-by-byte:

| Bytes | Interpretation |
|---|---|
| `41` | `A` in ASCII |
| `42` | `B` |
| `43` | `C` |
| `1B 24 42` | `ESC $ B`: designate JIS X 0208-1983 to G0 |
| `24 22` | JIS row-cell for `あ` |
| `24 24` | `い` |
| `24 26` | `う` |
| `24 28` | `え` |
| `1B 28 42` | `ESC ( B`: designate ASCII to G0 |
| `64 65` | `de` |
| `20` | SPACE |
| `31 32` | `12` |
| `1B 24 42` | enter JIS X 0208-1983 |
| `24 2B` | `か` |
| `24 2D` | `き` |
| `24 2F` | `く` |
| `1B 28 42` | restore ASCII |
| `0A` | LF in this local-file example |

If the first escape were lost, the kana bytes would display under ASCII as:

```text
24 22 24 24 24 26 24 28
 $  "  $  $  $  &  $  (
```

That is a compact demonstration of state loss.

### UTF-8 comparison

```text
41 42 43
E3 81 82 E3 81 84 E3 81 86 E3 81 88
64 65 20 31 32
E3 81 8B E3 81 8D E3 81 8F
0A
```

Each hiragana character is independently represented by three bytes beginning `E3`; no persistent charset state exists.

### Shift_JIS comparison

```text
41 42 43
82 A0 82 A2 82 A4 82 A6
64 65 20 31 32
82 A9 82 AB 82 AD
0A
```

Shift_JIS avoids escape-state changes but is not cleanly self-synchronizing: lead and trail ranges overlap other byte classes, and some byte values can be either single-byte characters or parts of double-byte characters. Mark Davis later recalled this ambiguity as a motivating experience behind Apple’s interest in Unicode. [Unicode early-years history](https://www.unicode.org/history/earlyyears.html).

## Example 2: `日本語`

### ISO-2022-JP

```text
1B 24 42  46 7C  4B 5C  38 6C  1B 28 42
```

| Bytes | Meaning |
|---|---|
| `1B 24 42` | designate JIS X 0208-1983 |
| `46 7C` | 日 |
| `4B 5C` | 本 |
| `38 6C` | 語 |
| `1B 28 42` | restore ASCII |

### Shift_JIS

```text
93 FA 96 7B 8C EA
```

### UTF-8

```text
E6 97 A5 E6 9C AC E8 AA 9E
```

ISO-2022-JP requires 12 bytes here, including the two three-byte state changes. Shift_JIS needs six and UTF-8 nine. If a longer Japanese run follows one entrance sequence, ISO-2022-JP amortizes its escape overhead.

## Example 3: Korean `가`

KS X 1001 row 16, cell 1 is transmitted as `30 21` in its 7-bit 94×94 representation.

### ISO-2022-KR

```text
1B 24 29 43  0E  30 21  0F
```

| Bytes | Meaning |
|---|---|
| `1B 24 29 43` | `ESC $ ) C`: designate KS C 5601-1987 to G1 |
| `0E` | SO: invoke G1 in GL |
| `30 21` | 가 |
| `0F` | SI: return to G0/ASCII |

RFC 1557 requires the designation once near the beginning of the body, so a real message normally does not repeat it for every word. [RFC 1557](https://www.rfc-editor.org/rfc/rfc1557.html).

### EUC-KR

```text
B0 A1
```

### UTF-8

```text
EA B0 80
```

## Example 4: Chinese `中`

GB 2312 encodes 中 as row bytes `56 50` in 7-bit form, or `D6 D0` with the high bits set in EUC-CN/GB2312 form.

### ISO-2022-CN

```text
1B 24 29 41  0E  56 50  0F
```

| Bytes | Meaning |
|---|---|
| `1B 24 29 41` | designate GB 2312 to the SO/G1 register |
| `0E` | SO |
| `56 50` | 中 |
| `0F` | SI |

### GB2312/EUC-CN

```text
D6 D0
```

### UTF-8

```text
E4 B8 AD
```

RFC 1922 also defines SS2 and SS3 designations for CNS 11643 planes and an extended profile for additional GB/CNS material. [RFC 1922](https://www.rfc-editor.org/rfc/rfc1922.html).

---

# Origins

## Long ancestry: Baudot, Murray, Hollerith, and shift codes

**[SCH]** ISO 2022 belongs to a lineage in which a small physical code space was multiplied through state. Émile Baudot’s five-unit telegraph code and Donald Murray’s later teleprinter arrangements used letter and figure shifts: the same five-bit combinations meant different things depending on an earlier shift character. Hollerith punched-card codes similarly tied characters to physical punch patterns rather than to a universal abstract repertoire.

These predecessors did not use ISO 2022’s designation grammar, but they established the engineering idea that state could trade decoder complexity for a larger repertoire. Charles E. Mackenzie’s *Coded Character Sets: History and Development* is the principal book-length reconstruction of this ancestry. [Mackenzie catalogue record](https://books.google.com/books/about/Coded_Character_Sets.html?id=6-tQAAAAMAAJ).

## ASCII and the creation of ESC

### The standards setting

**[DOC]** The American Standards Association convened Committee X3 in January 1960 for computers and information processing. ASCII work proceeded principally through X3.2. The first published ASCII standard was ASA X3.4-1963; revised forms followed in 1967 and 1968.

**[REC]** Bob Bemer later said that he drafted language calling for both a single interchange code and “orderly provision for expansion and alternatives,” and that he proposed a self-identifying identifier—the ESCAPE character—to reach alternate coding tables. His retrospective page cites his 1959–61 papers and the 1972 Honeywell Computer Journal article. [Archived Bemer ESC history](https://web.archive.org/web/20110708075700/https://www.bobbemer.com/ESCAPE.HTM).

**[DOC]** Bemer’s contemporary paper with H. J. Smith Jr. and F. A. Williams, “Design of an Improved Transmission/Data Processing Code,” appeared in *Communications of the ACM* in May 1961. Surviving accounts place ESC in an IBM proposal by May 1961 and in the X3 proposal shown to the US Department of Defense in June 1961. Its position changed before settling at `1/11`, hexadecimal `1B`.

**[DISPUTED]** “Bemer invented ESC” is plausible and supported by his early publication and committee participation, but much public wording ultimately descends from Bemer’s own later recollection. Committee standards are collective work, and no evidence found in this search establishes that the entire later ISO 2022 designation-and-invocation system was designed by Bemer alone. The strongest defensible credit is: Bemer was an early documented advocate and public expositor of an escape mechanism in the ASCII project.

## Why seven bits?

**[SCH]** The early interchange problem sat between:

- five- and six-bit telegraph or business-machine codes;
- seven-bit proposals capable of upper- and lowercase Latin plus controls;
- eight-bit proposals with 256 positions;
- machines using 6-, 7-, 8-, 9-, or word-packed characters;
- IBM’s punch-card-derived encodings.

ASCII’s seven bits provided 128 positions while permitting parity in an eight-channel communication unit. The resulting 32 C0 controls, 94 ordinary graphics, SPACE, and DEL became the base geometry later generalized by ISO 2022.

### Lowercase

**[SCH]** Lowercase was contentious because it consumed 26 scarce positions and much contemporary hardware printed capitals only. The 1963 ASCII edition did not yet contain the final lowercase arrangement; lowercase became standard in later revisions. ISO 2022 did not resolve the fight by enlarging ASCII itself. Instead, it offered an extensible structure in which another registered graphic set could be reached without redefining the base transport.

### Controls

The separation of controls into columns 0 and 1 made the entire printable middle block regular. ESC, SI, and SO became structural tools. CR and LF remained inherited physical-device concepts, which is why newline conventions still expose typewriter and teleprinter ancestry.

## ISO 646 and ECMA-6

**[STD]** ECMA-6 and ISO 646 standardized the seven-bit table internationally. ISO 646 permitted national variants that replaced a limited set of punctuation positions with national letters or currency symbols. This enabled French, German, Scandinavian, and other national use but made a byte such as `5B` potentially mean `[` or a national character.

RFC 1345 later identified an invariant 83-graphic subset shared across the national variants and used it for portable character mnemonics. [RFC 1345](https://www.rfc-editor.org/rfc/rfc1345.html).

### Currency signs

**[SCH]** The dollar sign, pound sign, generic currency sign, and national letters competed for the limited variant positions. The eventual multiplicity of ISO 646 variants demonstrated both the usefulness and danger of changing a table by context. ISO 2022 made context explicit through registered designations, but only when software preserved and interpreted the escape sequence correctly.

## IBM, EBCDIC, and the eight-bit alternative

**[DOC]** IBM introduced System/360 and EBCDIC in 1964. EBCDIC was eight-bit but derived from IBM card and BCD lineages; it did not preserve ASCII’s contiguous letter and punctuation layout.

IBM’s own conversion documentation shows non-bijective and irregular mappings: some EBCDIC controls have no ASCII equivalent, and punctuation resides at different positions. [IBM conversion table](https://www.ibm.com/docs/en/iis/11.3.0?topic=tables-ebcdic-ascii), [IBM conversion irregularities](https://www.ibm.com/docs/en/zos/2.5.0?topic=codes-conversion-irregularities).

**[FOLKLORE/DISPUTED]** A familiar “eight-bit defense” says EBCDIC prevailed at IBM because ASCII “wasted” an eighth bit or because System/360 was inherently eight-bit. The surviving record is more complicated:

- System/360 made the eight-bit byte commercially decisive.
- Early models contained an “ASCII mode” bit related to decimal-zone handling.
- Software and peripherals nevertheless standardized around EBCDIC.
- ASCII streams often used the eighth transmitted bit for parity or packed seven-bit characters into non-eight-bit words.

The slogan is a retrospective simplification, not a sufficient causal account. No primary source found in this pass supports the claim that one unused ASCII bit alone decided IBM’s encoding policy.

## ECMA-35 and ISO 2022

**[STD]** ECMA published ECMA-35’s first edition in December 1971. ISO published ISO 2022 in 1973. A 1970s NBS survey described ISO 2022:1973, ANSI X3.41-1974, FIPS PUB 35, and ECMA-35 as technically corresponding extension standards. [NBS survey](https://www.govinfo.gov/content/pkg/GOVPUB-C13-70a19496f137a595f58799edcefe12e9/pdf/GOVPUB-C13-70a19496f137a595f58799edcefe12e9.pdf).

**[STD]** ISO/IEC 2022:1994 says ECMA/TC1 contributed numerous papers to ISO/TC97/SC2’s working group responsible for ISO 2022. The surviving public text does not name one sole editor or chair as “designer of ISO 2022.”

**[OPEN EVIDENCE FINDING]** In the sources consulted, no primary committee history comparable to the ASCII oral histories assigns the G0–G3 architecture to one identifiable engineer. The responsible bodies—ECMA/TC1 and ISO/TC97/SC2, later ISO/IEC JTC 1/SC 2—are documented; individual authorship remains poorly exposed in the public record.

## ISO 2375: the registry

**[STD]** ISO 2022 defined syntax but relied on ISO 2375 registration to assign final bytes to repertoires and functions. A registration identified the defining document and the escape sequence that designated it; it did not magically make every receiver support that set.

The former register included:

- ASCII as ISO-IR 6;
- JIS Roman as ISO-IR 14;
- JIS X 0208-1978 as ISO-IR 42;
- GB 2312 as ISO-IR 58;
- JIS X 0208-1983 as ISO-IR 87;
- KS C 5601-1987 as ISO-IR 149;
- JIS X 0212 as ISO-IR 159.

ISO/IEC TR 2375:2024 now collects registrations formerly published by the registration authority. [IANA charset registry](https://www.iana.org/assignments/character-sets), [ISO/IEC TR 2375](https://www.iso.org/standard/85288.html).

## The 8-bit compromise: ISO 4873, ECMA-43, and ISO 8859

**[STD]** ISO/IEC 4873 and ECMA-43 constrained the broad ISO 2022 model for more predictable eight-bit codes. In the familiar level-1 form, ASCII occupies the left half and a supplementary 96-set occupies the right half. ISO 8859’s parts are fixed eight-bit instances of this design.

This answered one side of the “seven versus eight” problem:

- no per-word escape overhead;
- simple byte indexing;
- 191 or so printable characters;
- but only a limited repertoire per code page.

ISO 8859-1, -5, -6, -7, and -8 supported Western Latin, Cyrillic, Arabic, Greek, and Hebrew respectively, while other parts added further Latin repertoires. Mixing scripts remained limited, and language-sensitive shaping or bidirectionality remained outside the coded table.

---

# Adoption and decline

## US federal adoption of ASCII

**[DOC]** On 11 March 1968 President Lyndon Johnson directed that computers and related configurations entering the federal inventory after 1 July 1969 be capable of using ASCII and ancillary standards. The Commerce Department’s March 1969 memorandum implemented the requirement. It was a capability mandate, not an immediate order to destroy or convert every existing EBCDIC installation. [FIPS PUB 7 appendix](https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub7.pdf), [NBS institutional history](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication925.pdf).

## ARPANET and RFC 20

**[STD]** Vint Cerf’s RFC 20, dated 16 October 1969, selected seven-bit ASCII in an eight-bit field with the high bit zero for host-to-host interchange. It reproduced USAS X3.4-1968 and explicitly defined binary-value ordering as the relative sequence for collation. [RFC 20](https://www.rfc-editor.org/rfc/rfc20.html).

This 7-bit network inheritance later made ISO 2022’s East Asian profiles attractive: they could carry thousands of characters while every transmitted byte remained below `80`.

## Terminals: ANSI X3.64, ECMA-48, and the VT100

### Relationship to ISO 2022

**[STD]** Terminal control sequences are not character-set switching itself. ANSI X3.64 and its international counterpart ECMA-48/ISO 6429 define cursor movement, erasure, rendition, modes, and other control functions. ECMA-48 explicitly says its coded representations operate in codes structured according to ECMA-35. [ECMA-48](https://ecma-international.org/publications-and-standards/standards/ecma-48/), [ISO/IEC 6429](https://www.iso.org/fr/standard/12782.html).

Thus the relationship is:

```text
ECMA-35 / ISO 2022
    provides the code-space and escape/control syntax
                  │
                  └── ECMA-48 / ISO 6429 / ANSI X3.64
                      assigns terminal and imaging functions
                                  │
                                  └── VT100 and descendants implement a subset
```

### CSI

A terminal control sequence usually has:

```text
CSI P...P I...I F
```

where CSI is either C1 byte `9B` or its seven-bit form `ESC [` (`1B 5B`); parameters occupy `30–3F`, intermediates `20–2F`, and the final is `40–7E`.

For example:

```text
1B 5B 33 31 6D
ESC [  3  1  m
```

selects red foreground in common terminal practice.

**[DOC]** The VT100, introduced by DEC in 1978, popularized a subset of ANSI X3.64. It was not the first terminal implementing the standard, but it became the most imitated. Surviving terminal manuals describe `ESC [` as the seven-bit CSI representation and document numeric and selective parameters. [VT terminal archive](https://vt100.net/), [ANSI-terminal explanation](https://vt100.net/annarbor/aaa-ug/section13.html).

**[INFERENCE]** Modern “ANSI escape codes” therefore survive ISO 2022’s structural grammar even on UTF-8 terminals. UTF-8 replaced its repertoire-switching role but did not remove the utility of ESC-introduced device commands.

## Japanese networking and ISO-2022-JP

### JUNET

**[STD]** RFC 1468 says the encoding later named ISO-2022-JP was first specified and used in JUNET and was already widely used in Japanese IP communities before its June 1993 RFC registration. Authors were Jun Murai, Mark Crispin, and Erik van der Poel. [RFC 1468](https://www.rfc-editor.org/rfc/rfc1468.html).

The profile’s allowed sets are:

| Escape sequence | Set |
|---|---|
| `ESC ( B` | ASCII, ISO-IR 6 |
| `ESC ( J` | JIS X 0201 Roman, ISO-IR 14 |
| `ESC $ @` | JIS X 0208-1978, ISO-IR 42 |
| `ESC $ B` | JIS X 0208-1983, ISO-IR 87 |

It is entirely seven-bit and therefore required no MIME content-transfer encoding merely to survive seven-bit SMTP.

**[STD]** RFC 1468 also records interoperability damage already present by 1993:

- some JUNET systems incorrectly used `ESC ( H`, officially assigned to a Swedish set;
- some renderers failed to distinguish ASCII from JIS Roman or the 1978 and 1983 JIS sets;
- relays were forbidden to normalize those apparently equivalent sequences;
- the JIS X 0201 kana set was excluded.

This is unusually valuable contemporary evidence of the difference between elegant formal registration and deployed behavior.

### MIME

**[STD]** RFC 1341 introduced MIME in June 1992; subsequent MIME specifications allowed bodies to identify a `charset`. RFC 1468 registered:

```text
Content-Type: text/plain; charset=iso-2022-jp
```

For encoded words in headers, it recommended MIME’s `B` form. Stateful escape bytes could otherwise interact badly with header parsers and line folding.

### Extensions

- **RFC 1554 (December 1993):** ISO-2022-JP-2, adding multilingual 94- and 96-sets.
- **RFC 2237 (November 1997):** ISO-2022-JP-1, adding JIS X 0212.
- Later Japanese standards defined ISO-2022-JP-3 and ISO-2022-JP-2004 for JIS X 0213, but these did not achieve the original profile’s Internet ubiquity.

RFC 1554 discourages JIS Roman except for compatibility and requires ASCII at the end. It explicitly discusses line-start state so pagers and editors can seek. [RFC 1554](https://www.rfc-editor.org/rfc/rfc1554.html), [RFC 2237](https://www.rfc-editor.org/rfc/rfc2237.html).

## ISO-2022-KR

**[STD]** RFC 1557, by U. Choi, K. Chon, and H. Park, appeared in December 1993. It defines ASCII plus KS C 5601-1987.

The Korean set is designated once with:

```text
ESC $ ) C
1B 24 29 43
```

SO (`0E`) enters Korean G1; SI (`0F`) returns to ASCII G0. Lines must return appropriately around CRLF. The design remains seven-bit and therefore suited the old SMTP path. [RFC 1557](https://www.rfc-editor.org/rfc/rfc1557.html).

EUC-KR used essentially the same 94×94 Korean repertoire with high bits set, avoiding persistent shift state on eight-bit-clean systems.

## ISO-2022-CN and ISO-2022-CN-EXT

**[STD]** RFC 1922 appeared in March 1996. Its six authors were H. F. Zhu, D. Y. Hu, Z. G. Wang, T. C. Kao, W. C. H. Chang, and Mark Crispin.

ISO-2022-CN includes:

- ASCII;
- GB 2312-80 for simplified Chinese;
- the first two CNS 11643 planes for traditional Chinese.

ISO-2022-CN-EXT adds further GB repertoires and CNS planes. Designations load sets for SO, SS2, or SS3; SI, SO, SS2, and SS3 select them. RFC 1922 predicted that ISO 10646 might become preferred once widely available. [RFC 1922](https://www.rfc-editor.org/rfc/rfc1922.html).

That prediction was accurate, but ISO-2022-CN never matched ISO-2022-JP’s deployment.

## Bibliographic systems

### MARC-8

**[STD]** MARC-8 uses an ISO-2022-like multi-set model for library catalogue data. The Library of Congress maintains its character tables, escape sequences, and mappings to Unicode. Its East Asian set alone spans more than 200 chart pages. [Library of Congress MARC-8 tables](https://www.loc.gov/marc/specifications/specchartables.html).

MARC-8 illustrates where designation remained useful: controlled institutional interchange among systems that agreed on a finite repertoire and exact conventions.

## X11 Compound Text

**[DOC]** X Consortium Compound Text used an ISO 2022-derived interchange form to carry multilingual text selections between X clients. It combined standard and private designation sequences. UTF-8 properties later displaced it in most Unix desktop practice.

## DICOM

**[STD]** DICOM still permits ISO/IEC 2022 code extension for selected textual value representations. The applicable repertoires must be named in the Specific Character Set data element, and implementations must state conformance. [DICOM PS3.5 §6](https://dicom.nema.org/medical/dicom/2022b/output/chtml/part05/chapter_6.html).

This is an important surviving non-email use because medical data persists for decades and must round-trip through legacy systems.

## Why it declined

ISO 2022’s advantages were real:

- seven-bit transport safety;
- reuse of national standards;
- incremental adoption;
- efficient long runs of characters from one 94×94 set;
- explicit in-band identification;
- ability to reserve ASCII controls and punctuation.

Its liabilities became more important as software changed:

1. **Statefulness:** a substring has no fixed meaning without preceding state.
2. **Random access:** seeking to byte N requires scanning from a known reset.
3. **Fragile concatenation:** two valid fragments may not concatenate validly unless states are reset.
4. **Editing cost:** inserting ASCII into a Japanese run requires state changes.
5. **Search and filenames:** bytewise POSIX operations assume context-free byte strings.
6. **Many equivalent forms:** designation and shift choices can encode equivalent displayed text differently.
7. **Incomplete repertoires:** each profile still needs an agreed finite list.
8. **Security:** parsers, filters, and renderers may disagree about state transitions.
9. **Implementation burden:** every allowed repertoire requires mapping tables and error rules.

Markus Kuhn’s Unix analysis states the POSIX objection plainly: substring matching and filenames require bytes to have meanings independent of preceding shift sequences. [Kuhn’s ISO 2022/POSIX discussion](https://www.cl.cam.ac.uk/~mgk25/ucs/iso2022-wc.html).

## IETF migration to Unicode

### RFC 2277

**[STD]** BCP 18/RFC 2277, January 1998, requires Internet protocols to identify the charset of text and to be able to use UTF-8. It defines “charset” in the MIME/IANA sense as the complete mapping from octets to characters, explicitly noting that this differs from ISO terminology. [RFC 2277](https://www.rfc-editor.org/rfc/rfc2277.html).

### RFC 5198

**[STD]** RFC 5198, March 2008, defines Net-Unicode as UTF-8, normally NFC-normalized, with CRLF lines. It discourages older country- or language-specific encodings and prohibits C1 controls in Net-Unicode. [RFC 5198](https://www.rfc-editor.org/rfc/rfc5198.html).

### Internationalized email

**[STD]** RFCs 6530–6532 in February 2012 made direct UTF-8 possible in internationalized email addresses and most header values when SMTPUTF8 is available. RFC 6532 argues that MIME encoded words and arbitrary charset choices introduce complexity and processing errors. [RFC 6530](https://www.rfc-editor.org/rfc/rfc6530.html), [RFC 6531](https://www.rfc-editor.org/rfc/rfc6531.html), [RFC 6532](https://www.rfc-editor.org/rfc/rfc6532.html).

ISO-2022-JP remains valid in ordinary MIME bodies and encoded words, but it is no longer the architectural destination.

---

# The other scripts

## A framework, not a universal solution

ISO 2022 could designate many scripts, but only if:

- someone standardized an appropriate repertoire;
- it was registered;
- sender and receiver implemented it;
- the selected profile permitted it;
- directionality, shaping, and combining behavior were separately defined.

The framework solved coded selection. It did not by itself solve writing-system semantics.

## Cyrillic

**[STD]** Cyrillic appeared in national ISO 646 variants, KOI families, vendor codes, ISO 8859-5, and ECMA-113. ECMA-113 says its Cyrillic repertoire covered Bulgarian, Belarusian, Macedonian, Russian, Serbian, and pre-1990 Ukrainian orthography. [ECMA-113](https://dev.ecma-international.org/wp-content/uploads/ECMA-113_3rd_edition_december_1999.pdf).

### The KOI8 trick

**[SCH/FOLKLORE]** KOI8’s celebrated trick is that clearing the high bit of Russian text produces a rough Latin transliteration rather than random punctuation. This was intentional in the KOI family’s letter ordering, useful on unreliable seven-bit paths. The exact phrase “KOI8 trick” is later folklore, but the structural property is directly testable from the table.

ISO 2022 offered a different answer: preserve seven-bit bytes and explicitly invoke a Cyrillic set. KOI8-R and later Windows-1251 proved more convenient on eight-bit systems because they were stateless.

## Greek

Greek could be carried through registered Greek 7-bit sets, ISO 8859-7, or ECMA-118. National variants competed over accents and monotonic versus polytonic requirements. A fixed 96-set was adequate for modern monotonic Greek but not for every historical or scholarly combination without extensions or combining marks.

## Hebrew

Hebrew needs right-to-left layout but little contextual shaping. ISO 8859-8 and ECMA-121 encoded characters; they did not by themselves settle whether bytes were stored in visual order or logical order.

Legacy visually ordered Hebrew stored characters in screen order, making editing and mixed-direction text difficult. Modern Unicode uses logical order plus the Unicode Bidirectional Algorithm. W3C explicitly advises against visually ordered ISO-8859-8 in new content. [W3C encoding guidance](https://www.w3.org/International/questions/qa-choosing-encodings), [Unicode bidi FAQ](https://www.unicode.org/faq/bidi.html).

## Arabic

Arabic compounds three problems:

1. right-to-left paragraph direction;
2. embedded left-to-right numbers and Latin text;
3. contextual glyph shaping and ligation.

ECMA-114/ISO 8859-6 could provide Arabic character codes, but rendering behavior had to be specified separately. Some vendor encodings stored presentation forms; others stored abstract letters. Unicode’s modern model stores mostly logical characters, applies bidirectional ordering, and shapes afterward. [UAX #9](https://www.unicode.org/reports/tr9/), [Unicode Arabic FAQ](https://www.unicode.org/faq/arabic.html).

**[INFERENCE]** Escape designation was orthogonal to these issues. Selecting “Arabic” does not tell software how joining, mirrored punctuation, combining marks, or mixed-direction selection should work.

## Indic scripts

Indic scripts require reordering, conjunct formation, vowel placement, and font shaping. A fixed table can encode consonants and signs, but visual order is not a simple byte-to-glyph lookup.

ISO 2022 could transport a registered Indic set, yet no ISO-2022 Indic profile obtained global adoption comparable to the Japanese email profile. ISCII instead provided an Indian standard with script switching and a shared phonetic layout; vendor font encodings also proliferated. Unicode eventually supplied a common abstract-character model, while shaping engines perform script-specific layout.

W3C cautions that even Unicode encoding support does not guarantee correct Arabic or Indic display; rendering rules remain necessary. [W3C guidance](https://www.w3.org/International/questions/qa-choosing-encodings).

## Chinese

GB 2312, CNS 11643, Big5, CCCII, and vendor variants divided the space by jurisdiction, repertoire, and implementation.

- GB 2312 primarily served simplified Chinese.
- CNS 11643 was plane-based and served traditional Chinese requirements.
- Big5 became dominant in Taiwan and Hong Kong personal computing despite not being an ISO 2022 94×94 profile.
- ISO-2022-CN attempted to combine GB and CNS under one seven-bit state machine.
- RFC 1922 claimed its base profile covered all Chinese characters found in contemporary Big5, while CN-EXT added further standards.

The multiplicity of designation choices was politically inclusive but operationally heavy.

## Japanese

Japanese required at least ASCII/Roman, hiragana, katakana, and thousands of kanji. Competing encodings optimized different environments:

| Encoding | Strategy |
|---|---|
| ISO-2022-JP | Seven-bit, escape-designated JIS sets |
| EUC-JP | High-bit, largely stateless packaging of JIS sets |
| Shift_JIS | Mixed single/double-byte vendor encoding optimized for Japanese PCs |
| Unicode/UTF-8 | Universal repertoire, stateless transformation |

ISO-2022-JP’s ability to survive seven-bit mail made it the Internet winner for a time; Shift_JIS won much PC and web content; EUC-JP was common on Unix; UTF-8 ultimately absorbed all three through mapping.

## Korean

KS C 5601/KS X 1001 could be packaged as ISO-2022-KR or EUC-KR. Johab represented Hangul compositionally in a different layout. Unicode later encoded both modern Hangul syllables and conjoining jamo, avoiding a transport-level shift state.

## Tibetan and other less-supported scripts

**[SCH]** Tibetan encoding disputes concerned repertoire completeness, character-versus-glyph analysis, ordering, and compatibility with national or scholarly systems. These are predominantly Unicode/ISO 10646 allocation disputes, not disputes over ISO 2022 mechanics.

**[OPEN EVIDENCE FINDING]** The dedicated search found no persuasive primary evidence that Tibetan was a significant deployed ISO 2022 escape-profile ecosystem. Claims that “ISO 2022 failed Tibetan” should therefore be phrased narrowly: the framework never produced a widely interoperable Tibetan profile; it did not itself prohibit one.

## Emoji

Classic ISO-2022-JP/KR/CN cannot encode modern emoji. Japanese mobile carriers originally used private vendor repertoires and mappings. Unicode later encoded emoji through formal proposals and UTC/ISO processes.

The “emoji vote” belongs to Unicode governance, not to ISO 2022. ISO 2022’s registry could in principle designate a private graphic set, but recipients would need the same private agreement, defeating universal interchange.

---

# People and institutions

## Directly relevant figures

### Bob Bemer (1920–2004)

**[DOC/REC]** IBM engineer, later at UNIVAC, Bull, GE, and Honeywell; member of American and international character-code work. He advocated ESC, lowercase, backslash, braces, and international coordination. His preserved pages are valuable participant testimony but should not be mistaken for neutral committee minutes. [Bemer archive](https://web.archive.org/web/20150801005415/http://bobbemer.com/), [Computer History Museum archival item](https://archive.computerhistory.org/resources/access/text/2019/02/102785427-05-02-acc.pdf).

### Charles E. Mackenzie

**[SCH]** IBM engineer and author of *Coded Character Sets: History and Development* (Addison-Wesley, 1980). His book reconstructs telegraph, punched-card, BCD, ASCII, EBCDIC, and related development from documents and participant knowledge. It remains indispensable, although it predates Unicode and ISO-2022-JP.

### Jun Murai, Mark Crispin, and Erik van der Poel

**[STD]** Authors of RFC 1468 and formalizers of ISO-2022-JP for Internet messages. The RFC credits JUNET practice rather than claiming to have invented the underlying Japanese encoding in 1993.

### Masataka Ohta and Ken’ichi Handa

**[STD]** Authors of RFC 1554, ISO-2022-JP-2.

### U. Choi, K. Chon, and H. Park

**[STD]** Authors of RFC 1557, ISO-2022-KR/EUC-KR email conventions.

### H. F. Zhu and coauthors

**[STD]** Authors of RFC 1922, ISO-2022-CN and ISO-2022-CN-EXT.

### Keld Simonsen

**[DOC]** Author of RFC 1345, which catalogued numerous registered, national, and vendor character sets and built portable mnemonics from the invariant ISO 646 subset.

## Broader lineage

### Émile Baudot and Donald Murray

**[SCH]** Early telegraph-code designers whose letter/figure shift systems demonstrated stateful repertoire enlargement.

### Herman Hollerith

**[SCH]** Developed punched-card tabulation systems whose character encodings influenced IBM’s BCD and EBCDIC lineage.

### Hugh McGregor Ross

**[SCH]** British standards participant associated with early ASCII and ISO character-code coordination. Public histories often mention him alongside Bemer, but the sources examined here do not assign him a particular ISO 2022 sequence.

### Ken Thompson and Rob Pike

**[REC/DOC]** Bell Labs engineers responsible for the decisive 1992 form of UTF-8, the stateless successor that addressed many ISO 2022 operational weaknesses.

Rob Pike’s 2003 account says Ken Thompson designed the encoding in Pike’s presence on 2 September 1992 at a New Jersey diner, writing it on a placemat; they implemented it for Plan 9 over the following days. Archived September 1992 mail corroborates the rapid implementation and transmission of the proposal, but the placemat itself has not surfaced publicly.

**[DISPUTED]** Early descriptions sometimes credited the X/Open FSS-UTF authors—Gary Miller, Greger Leijonhufvud, and John Entenmann—more broadly with UTF-8. The best reconstruction distinguishes:

- X/Open’s earlier FSS-UTF proposal and requirements;
- Thompson’s new self-synchronizing byte structure;
- Pike’s design criteria and eyewitness/implementation role;
- X/Open’s subsequent standardization.

Thus “Ken Thompson invented UTF-8 on a placemat” is supported participant recollection with documentary aftermath, but the physical placemat is folklore-level absent evidence. [Pike history archive](https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt), [Pike–Thompson Plan 9 paper](https://9p.io/sources/plan9/sys/doc/utf.ms), [RFC-history discussion](https://data.iana.org/archive/ietf-charsets/msg01387.html), [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html).

## Unicode founders and standards editors

**[DOC/REC]** Unicode’s groundwork began in late 1987 with Joe Becker of Xerox, Lee Collins, then at Xerox, and Mark Davis of Apple. Becker’s *Unicode 88* articulated the early architecture. The Unicode Consortium incorporated in California in January 1991. Kenneth Whistler became one of its principal technical editors. [Unicode history](https://www.unicode.org/history/), [Early years](https://www.unicode.org/history/earlyyears.html), [Unicode 88](https://www.unicode.org/history/Unicode88.pdf).

### The 16-bit assumption

**[DOC]** Early Unicode pursued a uniform 16-bit code and expected 65,536 positions to suffice through unification and careful allocation. The Unicode history pages acknowledge earlier ISO proposals for an international two-byte set and fixed-width processing goals.

The assumption failed as the required repertoire grew. Unicode 2.0 adopted surrogates for UTF-16, making it variable-width for supplementary characters. RFC 5198 now calls UCS-2 obsolete and strongly discourages it. This was a major design reversal, although the 16-bit code unit survived in Windows, Java, JavaScript, and other APIs.

## Institutions

- **ASA/USASI/ANSI:** American standardization of ASCII and X3.41.
- **ECMA:** ECMA-6, ECMA-35, ECMA-43, ECMA-48, and script repertoires; TC1 was central.
- **ISO/IEC:** ISO 646, 2022, 2375, 4873, 6429, 8859, and 10646.
- **CCITT/ITU-T:** International telegraph alphabets and later text communication recommendations.
- **IBM:** BCD/EBCDIC, System/360, standards participation.
- **DEC:** VT terminals and widespread ANSI/ECMA terminal-control implementation.
- **Bell Labs:** Unix, Plan 9, UTF-8.
- **Xerox and Apple:** early Unicode work.
- **IETF:** RFC charset profiles, MIME, UTF-8 policy, internationalized email.
- **W3C and WHATWG:** Web internationalization guidance and compatibility decoding.
- **Unicode Consortium:** repertoire, properties, algorithms, security guidance, and emoji administration.

---

# Culture

## “Plain text” as a negotiated ideal

**[MODERN]** ISO 2022 exposes a paradox in “plain text.” The bytes may contain only seven-bit values, yet their meanings depend on invisible prior commands and external registry knowledge. What looks like `$B$"` in a dump may be an escape suffix and a Japanese character.

Unicode moved state out of repertoire selection, but plain text still depends on:

- encoding identification;
- normalization;
- directionality;
- shaping;
- fonts;
- grapheme segmentation;
- line-ending conventions.

“Plain text” is therefore not absence of protocol; it is a protocol sufficiently familiar to become invisible.

## ASCII and ANSI art

ASCII art uses printable characters as image elements. ANSI art adds ECMA-48/ANSI X3.64 terminal commands for color, cursor movement, and rendition.

**[INFERENCE]** ANSI art is a cultural descendant of the same in-band-control architecture as ISO 2022, but not usually of its G0–G3 charset switching. The terminal interprets ESC sequences as commands while printable bytes remain art material.

BBS culture and the demoscene exploited this boundary deliberately: a file was simultaneously text, a terminal program, and an animation. The modern terminal still supports much of this grammar.

## Mojibake

“Mojibake” (文字化け, approximately “transformed/garbled characters”) names text decoded under the wrong encoding or state.

Common paths include:

- Shift_JIS bytes decoded as Windows-1252;
- UTF-8 bytes decoded as Latin-1 or Windows-1252;
- ISO-2022-JP escape bytes stripped, exposed, or ignored;
- JIS Roman `5C` displayed as backslash on one system and yen on another;
- repeated UTF-8/legacy transcoding.

**[MODERN]** Designers and artists later adopted mojibake as a glitch aesthetic. That is a cultural reuse of failure, not an intended feature of the standards. No primary source found here dates one canonical “first mojibake artwork.”

## The backslash/yen problem

JIS X 0201 Roman assigns byte `5C` to YEN SIGN and `7E` to OVERLINE, where ASCII has backslash and tilde. Many Japanese systems nevertheless used ASCII-compatible fonts or semantics in programming contexts.

The Web Encoding Standard therefore treats ISO-2022-JP’s Roman state specially:

- `5C` maps to U+00A5 YEN SIGN;
- `7E` maps to U+203E OVERLINE;
- the encoder returns to ASCII for ordinary backslash or tilde.

This is one of the most visible living consequences of national ISO 646 variation. [WHATWG Encoding](https://encoding.spec.whatwg.org/).

## Filenames and code-page legacy

ISO 2022 state was ill suited to filenames because:

- `/`, `\`, and other ASCII bytes have structural meanings;
- path components are accessed as substrings;
- directory operations seek and compare without an initial stream reset;
- a filename fragment cannot safely inherit state from another.

Stateless Shift_JIS, EUC, Windows code pages, and later UTF-8 were more practical, although each created its own ambiguous-byte or locale problems. Mojibake in ZIP files, old archives, and network shares is the durable residue of storing bytes without durable charset metadata.

---

# Controversies and disputes

## Was ISO 2022 elegant or overengineered?

**[DOC]** The standard has a rigorous orthogonal structure: designate sets, invoke them, transform between seven- and eight-bit forms, and register identifiers centrally.

**[SCH]** Admirers call this elegant because one mechanism handles national alphabets, multibyte ideographs, controls, and even switches to other coding systems. Critics call it combinatorially excessive because profiles must constrain a huge state machine before interoperability is possible.

Both readings are supported:

- ISO-2022-JP shows successful, disciplined profiling.
- RFC 1468 simultaneously records erroneous unregistered behavior and implementations that collapsed distinct designations.
- Unicode UTS #22 later described ISO 2022 encodings as “very stateful” and infeasible to express fully in one simple mapping file. [UTS #22](https://www.unicode.org/reports/tr22/tr22-4.html).

## Bemer and the ownership of ESC

**[REC]** Bemer repeatedly identified ESC as one of his principal contributions and described his early expansion concept.

**[DISPUTED]** Calling him “the inventor of escape sequences” without qualification overstates the record:

- shifted telegraph codes predated him;
- ASCII and ISO standards were committee products;
- ISO 2022’s mature grammar was created through ECMA and ISO working groups;
- Bemer’s best-known detailed narratives were written decades later.

The defensible formulation is “Bemer was an early, documented proposer and advocate of ASCII ESC and extensible code tables.”

## ISO-2022-JP identity disputes

### `ESC ( B` versus `ESC ( J`

They may display alike for most Latin text, but they differ at `5C` and `7E`. Relays that treated them as interchangeable could corrupt yen signs, overlines, backslashes, or tildes.

### `ESC $ @` versus `ESC $ B`

These select the 1978 and 1983 JIS X 0208 editions. Some systems displayed them identically, but RFC 1468 forbade relays to rewrite them because character assignments and mappings were not wholly identical.

### Erroneous `ESC ( H`

RFC 1468 records its use in old JUNET messages while noting that the sequence was officially registered for Swedish. This is documented misuse, not folklore.

### Half-width kana

RFC 1468 excludes JIS X 0201 kana; some later software nevertheless accepted or emitted `ESC ( I`. WHATWG’s compatibility decoder recognizes a katakana state because deployed Web content forced browsers to handle it. This is a classic difference between an IETF profile and the compatibility encoding reconstructed from browsers.

## Security: encoding-state disagreement

Stateful encodings create a security boundary whenever two components decode differently.

Possible patterns include:

1. a filter scans bytes as ASCII while a browser enters Japanese state;
2. a sanitizer and renderer disagree about malformed escape recovery;
3. an escape sequence crosses a buffer or MIME folding boundary;
4. a decoder falls back to ASCII at a different point from another decoder;
5. a charset override causes bytes previously considered harmless to become markup.

**[DOC]** Mozilla bug 1224505 documented a possible XSS path involving malformed ISO-2022-JP escape handling and encoding override. The Web Encoding Standard’s decoder now specifies error and state transitions algorithmically to force interoperable behavior. Its encoder rejects ESC, SI, and SO in sensitive states “to prevent attacks.” [Mozilla bug 1224505](https://bugzilla.mozilla.org/show_bug.cgi?id=1224505), [WHATWG Encoding](https://encoding.spec.whatwg.org/).

## CVE-2024-2961: ISO-2022-CN-EXT and glibc

**[DOC]** In 2024 glibc disclosed that `iconv()` in versions through 2.39 could overrun the caller’s output buffer by up to four bytes when converting to ISO-2022-CN-EXT. Bounds checks existed for the SO designation but were missing for SS2 and SS3 designation outputs. Fixed escape bytes such as `$+I` or `$*H` could overwrite adjacent memory. [glibc advisory via oss-security](https://seclists.org/oss-sec/2024/q2/137), [Red Hat tracker](https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2024-2961).

This was an implementation bug, not proof that every stateful encoding is inherently memory-unsafe. It nevertheless illustrates how state-triggered, variable-length escape emission complicates buffer accounting.

## UTF-8 security: overlong forms

UTF-8 won partly through synchronization, but early specifications permitted more forms than modern UTF-8.

**[STD]** RFC 3629 prohibits:

- overlong encodings;
- UTF-16 surrogate code points;
- code points above U+10FFFF;
- five- and six-byte sequences.

It cites the overlong `C0 80` representation of NUL as dangerous because one component might validate bytes while another decodes them as U+0000. It also notes a 2001 Web-server virus that exploited invalid UTF-8 handling. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html).

This controversy is relevant because “UTF-8 is self-synchronizing” does not mean “every permissive UTF-8 decoder is secure.” Canonical decoding rules are essential.

## The BOM

The byte-order mark arose from fixed-width Unicode encodings:

- `FE FF` indicates UTF-16 big-endian;
- `FF FE` indicates little-endian when read bytewise;
- in UTF-8, U+FEFF becomes `EF BB BF`, where it is a signature, not a byte-order necessity.

**[STD]** RFC 3629 says protocols should forbid or explicitly permit a UTF-8 signature rather than strip it blindly. RFC 5198 forbids BOM at the beginning of Net-Unicode strings. Unix practice often rejects it because it breaks leading magic such as `#!`. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html), [RFC 5198](https://www.rfc-editor.org/rfc/rfc5198.html), [Kuhn FAQ](https://www.cl.cam.ac.uk/~mgk25/unicode.html).

**[MODERN]** The phrase “UTF-8 BOM” is technically entrenched but conceptually misleading: UTF-8 has no byte-order choice.

## Han unification

This is a Unicode/ISO 10646 controversy, but it explains the universal replacement for ISO 2022’s separate national sets.

**[DOC]** Unicode’s official history says Lee Collins played a major role in early Han unification. In 1991 the CJK Joint Research Group chose GB 13000 as the basis of the Unified Repertoire and Ordering and used unification rules developed with Japanese participation, including Professor Miyazawa Akira. URO 2.0 was completed on 27 March 1992 and entered Unicode 1.0 volume 2 and ISO/IEC 10646-1:1993. [Unicode Appendix E](https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/).

### The objection

**[DISPUTED]** Critics, particularly in Japan, argued that unifying characters across national source standards:

- obscured region-specific glyph distinctions;
- made correct typography depend on language metadata and fonts;
- encoded a Chinese-centered or Western engineering interpretation of kanji;
- constrained rare, personal, historical, or variant forms.

### The defense

**[DOC]** Unicode’s technical defense is that it unified characters judged abstractly identical while leaving glyph style to fonts, much as Latin `A` is unified across languages. It did not intentionally unify simplified characters with distinct traditional characters merely because they were related. [Unicode Technical Note 26](https://www.unicode.org/notes/tn26/).

### Evidence assessment

The formal history demonstrates multinational ISO participation; it does not show that all Japanese users or experts agreed with the result. Conversely, popular claims that “Unicode encoded Chinese glyphs and forced Japanese to display them” omit the character/glyph distinction and modern language-sensitive font mechanisms. The controversy is partly technical and partly about who gets to define equivalence.

## Unicode as a political institution

**[MODERN/SCH]** Character encoding determines which names, scripts, symbols, and distinctions can travel through ordinary software. Allocation order, proposal requirements, source evidence, normalization stability, and compatibility policy therefore distribute practical visibility.

The Unicode Consortium is simultaneously:

- a technical standards body;
- a membership organization containing major vendors;
- a liaison participant in ISO/IEC 10646;
- a repository of script expertise;
- a gatekeeper constrained by stability promises.

Critics emphasize vendor influence, proposal burdens, and delayed support for minority or historic scripts. Defenders emphasize public proposals, expert review, ISO balloting, stability, and the impossibility of encoding every glyph or private distinction as a character.

This political interpretation should not be mistaken for evidence that ISO 2022 was culturally neutral: its dependence on national standards and registered repertoires merely located political choices elsewhere.

## Emoji and the Consortium

Emoji entered Unicode partly because Japanese carrier symbols were already in widespread interchange and required round-trip mapping. Subsequent emoji additions involve UTC proposals, evidence of expected usage, property assignments, and coordination with ISO/IEC JTC 1/SC 2/WG 2.

**[DISPUTED/MODERN]** “A committee votes on whether an idea exists” is a popular caricature. The committee votes on standardized interchange characters, not on whether a concept may be expressed. Yet rejection or delay plainly affects universal keyboard, font, and protocol support. Both observations are true.

## ISO versus Unicode

**[SCH]** Early Unicode and the original ISO 10646 project began with different architectures and institutional cultures. A merger aligned their repertoires and code values by the early 1990s.

The result was not simply “Unicode defeated ISO”:

- ISO/IEC 10646 remains the international coded-character standard.
- The Unicode Standard shares its code points but supplies more properties, algorithms, and implementation guidance.
- ISO national-body voting and Unicode Consortium technical processes continue in coordination.
- UTF-8 is standardized in Unicode, ISO/IEC 10646, and IETF RFCs.

ISO 2022 itself even registered ways to designate other coding systems, including UTF-8, but universal Unicode text made continual G-set switching unnecessary.

---

# Why UTF-8 won

The outcome is best understood as an engineering comparison:

| Property | ISO 2022 profiles | UTF-8 |
|---|---|---|
| ASCII bytes | Preserved in ASCII state | Preserved everywhere |
| Persistent state | Usually yes | No |
| Random access | Requires known state/reset | Boundary found locally |
| Repertoire | Profile-dependent | Entire Unicode codespace |
| Byte order | None in 7/8-bit form | None |
| Seven-bit clean | Yes for JP/KR/CN profiles | No; needs 8-bit transport or transfer encoding |
| Long CJK runs | Often 2 bytes/character plus escapes | Usually 3 bytes/character |
| Mixed scripts | Requires designations and common profile | Direct |
| Concatenation | Must reconcile end/start state | Safe if both strings are valid |
| Error locality | May persist to next reset | Usually limited to nearby invalid sequence |
| POSIX filenames | Poor fit | Strong fit |
| Canonical representation | Multiple possible state paths | One shortest byte sequence per code point |
| Rendering algorithms | External | Also external |

**[INFERENCE]** ISO 2022 optimized scarce channels and installed national standards. UTF-8 optimized software composition and a universal abstract repertoire. Once eight-bit-clean storage and transport became normal, the former optimization ceased to dominate.

The historical adoption curve supports this explanation:

- 1998: IETF required protocol support for UTF-8.
- 2008: W3C discussion reported UTF-8 overtaking older Web encodings.
- 2010: W3C reported Unicode-encoded pages above 50%.
- 2012: Google’s multibillion-page sample placed UTF-8 above 60%; including ASCII as valid UTF-8 raised the Unicode-compatible share further.
- January 2023: W3C’s summary cited 97.9%.
- September 2026: W3Techs reported 99.1% among sites with known encodings.

[W3C 2008 report](https://www.w3.org/qa/2008/05/utf8-web-growth.html), [W3C 2010 update](https://www.w3.org/blog/International/2010/09/03/updated_article_who_uses_unicode/), [W3C usage summary](https://www.w3.org/International/questions/qa-who-uses-unicode.en.html), [W3Techs 2026](https://w3techs.com/technologies/breakdown/en-utf8/ranking).

---

# Open questions and negative findings

1. **Individual authorship of G0–G3.**  
   The standards identify ECMA/TC1 and ISO/TC97/SC2 working groups, but the public sources consulted do not identify one engineer who invented the complete register model.

2. **Complete ECMA/ISO committee minutes.**  
   The free ECMA editions establish the published chronology, but a full reconstruction of debates would require working papers, national comments, and minutes not exposed in the catalogues searched.

3. **The earliest exact JUNET specification.**  
   RFC 1468 says JUNET first specified and used the encoding, but the original JUNET document was not recovered in this search. The RFC is authoritative for the Internet profile but retrospective about the preceding deployment.

4. **Deployment measurements.**  
   Reliable present-day percentages for ISO-2022-JP email are unavailable because private mail corpora are not observable. Web figures cannot be substituted for email prevalence.

5. **Bemer’s precise share of ESC.**  
   His early publications and recollections are strong evidence of advocacy, but surviving public committee documentation does not warrant exclusive ownership of every escape-sequence development.

6. **The UTF-8 placemat.**  
   Pike’s eyewitness account and archived follow-up mail support the event; the placemat itself is absent. The anecdote should remain labeled participant recollection, not physical documentary proof.

7. **Tibetan and ISO 2022.**  
   No evidence was found of a major interoperable ISO 2022 Tibetan profile. Most documented Tibetan controversies belong to Unicode/ISO 10646 repertoire design.

8. **Mojibake’s first artistic use.**  
   The phenomenon is old; its self-conscious use as an aesthetic is diffuse. No defensible single inventor or first artwork emerged.

9. **Keyboard scan codes.**  
   Modern keyboard scan codes are not generally ASCII or ISO 2022. Keyboard firmware reports physical keys or usage identifiers; software later maps them to characters. Claims that ASCII “survives as keyboard scan codes” are usually folklore or shorthand, although ASCII control traditions influenced terminal key behavior.

10. **“ISO 2022 caused ANSI escape codes.”**  
    The precise relationship is structural, not sole authorship: ECMA-48/ISO 6429 and ANSI X3.64 assign imaging functions within an ECMA-35/ISO-2022-compatible control architecture.

---

# Sources

## Standards and official catalogues

1. ISO, *ISO/IEC 2022:1994 — Information technology — Character code structure and extension techniques*, fourth edition, December 1994:  
   https://www.iso.org/standard/22747.html

2. ISO Online Browsing Platform, ISO/IEC 2022:1994 foreword, introduction, and contents:  
   https://www.iso.org/obp/ui?_escaped_fragment_=iso:std:iso-iec:2022:ed-4:v1:en

3. Ecma International, ECMA-35 standard page and edition archive:  
   https://ecma-international.org/publications-and-standards/standards/ecma-35/

4. Ecma International, *ECMA-35, Character Code Structure and Extension Techniques*, sixth edition, December 1994, complete PDF:  
   https://www.ecma-international.org/wp-content/uploads/ECMA-35_6th_edition_december_1994.pdf

5. ISO, *ISO/IEC TR 2375:2024 — Registered escape sequences and coded character sets*:  
   https://www.iso.org/standard/85288.html

6. ANSI Webstore, INCITS adoption and reaffirmation history for ISO/IEC 2022:1994:  
   https://webstore.ansi.org/standards/incits/incitsisoiec20221994r2018

7. US National Bureau of Standards, *A Survey of Standardization Efforts of Coded Character Sets for Text Processing*:  
   https://www.govinfo.gov/content/pkg/GOVPUB-C13-70a19496f137a595f58799edcefe12e9/pdf/GOVPUB-C13-70a19496f137a595f58799edcefe12e9.pdf

8. US federal publication containing ANSI X3.41 and related standards listing:  
   https://www.govinfo.gov/content/pkg/GOVPUB-C13-f9965f0a3acd204886a71b56c7c491e3/pdf/GOVPUB-C13-f9965f0a3acd204886a71b56c7c491e3.pdf

9. ANSI X3.4-1977 scan:  
   https://www.govinfo.gov/content/pkg/GOVPUB-C13-cbabedfeed07da3dd8ebf1c6173d0260/pdf/GOVPUB-C13-cbabedfeed07da3dd8ebf1c6173d0260.pdf

10. ANSI X3.4-1986 scan:  
    https://www.bitsavers.org/pdf/ansi/X3/X3.004-1986_7-Bit_ASCII.pdf

11. Ecma International, ECMA-48 standard page:  
    https://ecma-international.org/publications-and-standards/standards/ecma-48/

12. Ecma International, *ECMA-48, Control Functions for Coded Character Sets*, fifth edition, June 1991:  
    https://ecma-international.org/wp-content/uploads/ECMA-48_5th_edition_june_1991.pdf

13. ISO, ISO/IEC 6429:1992 catalogue page:  
    https://www.iso.org/fr/standard/12782.html

14. Ecma International, ECMA-113 Latin/Cyrillic alphabet:  
    https://dev.ecma-international.org/wp-content/uploads/ECMA-113_3rd_edition_december_1999.pdf

15. ISO/IEC JTC 1/SC 2 committee page:  
    https://www.iso.org/committee/45050.html

16. IANA, Character Sets registry:  
    https://www.iana.org/assignments/character-sets

17. IANA, legacy character-set registration material:  
    https://www.iana.org/assignments/charset-reg

18. CEN/TC304, *Guide to the Use of Character Sets in Europe*, Annex A:  
    https://www.open-std.org/CEN/TC304/guidecharactersets/guideannexa.html

19. CEN/TC304, UCS and ISO 2022 DOCS discussion, Annex B:  
    https://open-std.org/CEN/TC304/guidecharactersets/guideannexb.html

20. DICOM PS3.5, Chapter 6, character repertoires and ISO 2022 extension:  
    https://dicom.nema.org/medical/dicom/2022b/output/chtml/part05/chapter_6.html

21. Library of Congress, MARC-8 code tables and specifications:  
    https://www.loc.gov/marc/specifications/specchartables.html

## RFCs and Internet standards

22. Vint Cerf, RFC 20, *ASCII Format for Network Interchange*, October 1969:  
    https://www.rfc-editor.org/rfc/rfc20.html

23. Keld Simonsen, RFC 1345, *Character Mnemonics and Character Sets*, June 1992:  
    https://www.rfc-editor.org/rfc/rfc1345.html

24. Jun Murai, Mark Crispin, Erik van der Poel, RFC 1468, *Japanese Character Encoding for Internet Messages*, June 1993:  
    https://www.rfc-editor.org/rfc/rfc1468.html

25. Masataka Ohta and Ken’ichi Handa, RFC 1554, *ISO-2022-JP-2: Multilingual Extension of ISO-2022-JP*, December 1993:  
    https://www.rfc-editor.org/rfc/rfc1554.html

26. U. Choi, K. Chon, H. Park, RFC 1557, *Korean Character Encoding for Internet Messages*, December 1993:  
    https://www.rfc-editor.org/rfc/rfc1557.html

27. H. F. Zhu et al., RFC 1922, *Chinese Character Encoding for Internet Messages*, March 1996:  
    https://www.rfc-editor.org/rfc/rfc1922.html

28. C. Weider et al., RFC 2130, *Report of the IAB Character Set Workshop*, April 1997:  
    https://www.rfc-editor.org/rfc/rfc2130.html

29. K. Tamaru, RFC 2237, *Japanese Character Encoding for Internet Messages*, November 1997:  
    https://www.rfc-editor.org/rfc/rfc2237.html

30. Harald Alvestrand, RFC 2277/BCP 18, *IETF Policy on Character Sets and Languages*, January 1998:  
    https://www.rfc-editor.org/rfc/rfc2277.html

31. François Yergeau, RFC 3629, *UTF-8, a Transformation Format of ISO 10646*, November 2003:  
    https://www.rfc-editor.org/rfc/rfc3629.html

32. John Klensin and Mike Padlipsky, RFC 5198, *Unicode Format for Network Interchange*, March 2008:  
    https://www.rfc-editor.org/rfc/rfc5198.html

33. John Klensin and Y. Ko, RFC 6530, *Overview and Framework for Internationalized Email*, February 2012:  
    https://www.rfc-editor.org/rfc/rfc6530.html

34. Jiankang Yao and Wei Mao, RFC 6531, *SMTP Extension for Internationalized Email*:  
    https://www.rfc-editor.org/rfc/rfc6531.html

35. A. Yang, S. Steele, N. Freed, RFC 6532, *Internationalized Email Headers*:  
    https://www.rfc-editor.org/rfc/rfc6532.html

36. RFC 2070, *Internationalization of Hypertext Markup Language*:  
    https://www.rfc-editor.org/rfc/rfc2070.html

37. RFC 2157, *Mapping between X.400 and RFC-822/MIME Message Bodies*:  
    https://www.rfc-editor.org/rfc/rfc2157.html

## Web standards and deployment evidence

38. WHATWG, *Encoding Standard*:  
    https://encoding.spec.whatwg.org/

39. WHATWG, *HTML Living Standard*, parsing and required encodings:  
    https://html.spec.whatwg.org/multipage/parsing.html

40. W3C, *Choosing and Applying a Character Encoding*:  
    https://www.w3.org/International/questions/qa-choosing-encodings

41. W3C, *Who Uses Unicode?*:  
    https://www.w3.org/International/questions/qa-who-uses-unicode.en.html

42. W3C, *UTF-8 Growth on the Web*, 2008:  
    https://www.w3.org/qa/2008/05/utf8-web-growth.html

43. W3C Internationalization Blog, Unicode usage update, 2010:  
    https://www.w3.org/blog/International/2010/09/03/updated_article_who_uses_unicode/

44. W3C, HTML 4.01 character-set chapter:  
    https://www.w3.org/TR/html401/charset.html

45. W3Techs, UTF-8 usage by site ranking, September 2026:  
    https://w3techs.com/technologies/breakdown/en-utf8/ranking

46. W3Techs technology overview:  
    https://w3techs.com/

47. W3C, Japanese XML Profile, second edition:  
    https://www.w3.org/submissions/japanese-xml/

## Unicode sources

48. Unicode Consortium, History Corner:  
    https://www.unicode.org/history/

49. Unicode Consortium, *Early Years of Unicode*:  
    https://www.unicode.org/history/earlyyears.html

50. Unicode Consortium, release and publication chronology:  
    https://www.unicode.org/history/publicationdates.html

51. Joseph D. Becker, *Unicode 88*:  
    https://www.unicode.org/history/Unicode88.pdf

52. Unicode Standard 16.0, Appendix E, *Han Unification History*:  
    https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/

53. Unicode Technical Note #26, *On the Encoding of Latin, Greek, Cyrillic, and Han*:  
    https://www.unicode.org/notes/tn26/

54. Unicode Standard, CJK chapter from version 12.1:  
    https://www.unicode.org/versions/Unicode12.1.0/ch18.pdf

55. Unicode Standard Annex #9, *Unicode Bidirectional Algorithm*:  
    https://www.unicode.org/reports/tr9/

56. Unicode Arabic FAQ:  
    https://www.unicode.org/faq/arabic.html

57. Unicode bidi FAQ:  
    https://www.unicode.org/faq/bidi.html

58. Unicode Technical Report #36, *Unicode Security Considerations*:  
    https://www.unicode.org/reports/tr36/

59. Unicode Technical Standard #39, *Unicode Security Mechanisms*:  
    https://www.unicode.org/reports/tr39/

60. Unicode Technical Standard #22, *CharMapML*, discussion of stateful ISO 2022 mappings:  
    https://www.unicode.org/reports/tr22/tr22-4.html

61. Unicode mailing-list archive, historical answers by participants:  
    https://www.unicode.org/mail-arch/unicode-ml/y2002-m02/0110.html

## UTF-8 origin material

62. Rob Pike, *UTF-8 History*, participant account and archived correspondence:  
    https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt

63. Rob Pike and Ken Thompson, Plan 9 paper source, *Hello World or Καλημέρα κόσμε or こんにちは 世界*:  
    https://9p.io/sources/plan9/sys/doc/utf.ms

64. Markus Kuhn, IETF charset-list discussion correcting UTF-8 credit, June 2003:  
    https://data.iana.org/archive/ietf-charsets/msg01387.html

65. Markus Kuhn, *UTF-8 and Unicode FAQ for Unix/Linux*:  
    https://www.cl.cam.ac.uk/~mgk25/unicode.html

66. Markus Kuhn, ISO 2022, `wchar_t`, and POSIX filename requirements:  
    https://www.cl.cam.ac.uk/~mgk25/ucs/iso2022-wc.html

## ASCII, IBM, and institutional history

67. Bob Bemer site, preserved collection:  
    https://web.archive.org/web/20150801005415/http://bobbemer.com/

68. Bob Bemer, *That Powerful ESCAPE Character*, archived copy:  
    https://web.archive.org/web/20110708075700/https://www.bobbemer.com/ESCAPE.HTM

69. Computer History Museum archival material referring to Bemer and ASCII:  
    https://archive.computerhistory.org/resources/access/text/2019/02/102785427-05-02-acc.pdf

70. IBM, EBCDIC-to-ASCII conversion table:  
    https://www.ibm.com/docs/en/iis/11.3.0?topic=tables-ebcdic-ascii

71. IBM, conversion irregularities between EBCDIC and ASCII:  
    https://www.ibm.com/docs/en/zos/2.5.0?topic=codes-conversion-irregularities

72. NBS, FIPS PUB 7 with the federal ASCII implementation memorandum:  
    https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub7.pdf

73. NIST, *A Unique Institution: The National Bureau of Standards 1950–1969*:  
    https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication925.pdf

74. CIA archival record discussing federal ASCII transition, September 1968:  
    https://www.cia.gov/readingroom/document/cia-rdp78-04723a000100150043-3

75. Charles E. Mackenzie, *Coded Character Sets: History and Development*, bibliographic record:  
    https://books.google.com/books/about/Coded_Character_Sets.html?id=6-tQAAAAMAAJ

## Terminal documentation

76. VT100.net terminal-manual archive:  
    https://vt100.net/

77. Ann Arbor Ambassador manual, ANSI X3.64 syntax:  
    https://vt100.net/annarbor/aaa-ug/section13.html

78. DEC terminal historical survey:  
    https://www.vt100.net/shuford/terminal/dec.html

79. GNU Teseq manual, ECMA-35 escape-sequence recognition:  
    https://www.gnu.org/software/teseq/manual/html_node/Escape-Sequence-Recognition.html

80. GNU Teseq standards cross-reference:  
    https://www.gnu.org/software/teseq/manual/html_node/Standards.html

## Security records

81. glibc security advisory, CVE-2024-2961, via oss-security:  
    https://seclists.org/oss-sec/2024/q2/137

82. Red Hat CVE-2024-2961 tracker:  
    https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2024-2961

83. glibc ISO-2022-CN-EXT converter source:  
    https://git.zx2c4.com/glibc/tree/iconvdata/iso-2022-cn-ext.c?id=e740e5b1f0d786bdd95898b61c4a81f8f00bb063

84. Mozilla bug 1224505, possible XSS through ISO-2022-JP decoding differences:  
    https://bugzilla.mozilla.org/show_bug.cgi?id=1224505

## Worked-example source

85. Japanese instructional page with byte-by-byte ISO-2022-JP, Shift_JIS, EUC-JP, and UTF examples:  
    https://www.seiai.ed.jp/sys/text/cs/chp02/c02a020.html
