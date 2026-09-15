# Fieldata and the early computer codes (the 1950s vendor and military codes): Research Dossier

> **Standard or defining documents:** U.S. Army Signal Corps *FIELDATA Equipment Intercommunication Characteristics* memorandum, April 1959, revised August 1959; related provisions in MIL-STD-188A, 25 April 1958, followed by MIL-STD-188B (1964) and MIL-STD-188C (1969).  
> **Year:** project begun about 1956; code publicly documented in 1958–59.  
> **Bit width:** military interchange form, 7 information bits—one tag bit plus a six-bit code—normally transmitted as eight bits with parity; UNIVAC derivative, fixed six-bit characters.  
> **Repertoire:** Latin capitals, decimal digits, approximately 28 punctuation signs and simple format functions; the military code adds a 64-position supervisory half and case/extension controls. Exact supervisory assignments varied by system.  
> **Current status:** obsolete as a general interchange standard; not registered as an Internet charset. Six- and nine-bit character facilities remain documented in the ClearPath OS 2200 lineage, and FIELDATA survives in legacy data, software interfaces, conversion tools, and historical archives.

## Evidence labels

Every substantive passage below carries one or more of these labels:

- **[D—standard/document]** Contemporary standard, manual, paper, memorandum, government order, or archival record.
- **[R—scholarly reconstruction]** Later historical synthesis, especially Charles E. Mackenzie’s 1980 study.
- **[P—participant recollection]** A later account by someone involved.
- **[X—disputed]** A claim whose scope, priority, or attribution is contested or unsupported by enough independent evidence.
- **[F—folklore]** A story widely repeated without adequate contemporary documentation.
- **[M—modern reconstruction/invention]** A later chart, terminology, emulator convention, or cultural interpretation not itself part of the original specification.

“FIELDATA” was the name of an Army information-system project as well as of codes associated with it. There was therefore no single context-free “FIELDATA byte.” The most important distinction is between:

1. the Army’s **7-bit interchange scheme**, consisting of a tag bit selecting one of two 64-position halves;
2. the **primary/graphic half**, which could stand alone as a six-bit code;
3. the **UNIVAC six-bit derivative**, similar to but not identical with the Army primary half; and
4. application-specific supervisory variants used by military networks.

Conflating those produces most modern contradictions about whether FIELDATA was “six-bit,” “seven-bit,” or “eight-bit.” It could legitimately be described in all three ways, but at different layers.

---

## Basic identification

### Name

**[D/R]** Contemporary typography includes `FIELDATA`, `FIELD DATA`, and occasionally `FIELData`. The name denoted “field data” in the ordinary military sense: information gathered, processed, and communicated within a tactical field army. It was not originally an acronym with an authoritative word-by-word expansion.

### Sponsoring institution

**[D]** The project was undertaken by the U.S. Army Signal Corps, particularly the U.S. Army Signal Research and Development Laboratory at Fort Monmouth, New Jersey. Captain William F. Luebbert’s 1959 Western Joint Computer Conference paper calls FIELDATA an integrated family of Army data-processing and data-transmission equipment. [The full 1959 AFIPS proceedings preserve Luebbert’s paper at pp. 189–196](https://bitsavers.org/pdf/afips/1959-03_%2315.pdf).

### Defining instruments

**[D]**

- *Military Communication System Technical Standard*, MIL-STD-188A, 25 April 1958.
- U.S. Army Signal Corps, *FIELDATA Equipment Intercommunication Characteristics*, memorandum to the Director, Data Processing Facilities Division, April 1959; revised August 1959.
- William F. Luebbert, “Data Transmission Equipment Concepts for FIELDATA,” presented 3–5 March 1959 and printed in the 1959 Western Joint Computer Conference proceedings.
- MIL-STD-188B, 24 February 1964.
- MIL-STD-188C, 24 November 1969.

**[R]** Mackenzie treats the 1959 intercommunication memorandum as the principal code document. Surviving online catalogues and secondary charts often cite it, but a reliably searchable first-generation scan is difficult to locate. That absence matters: many web tables reproduce one representative variant as if it were uniquely canonical.

### Status

**[D]** FIELDATA is absent from the current IANA charset table; it consequently has no standard Internet MIME charset name. The registry does include numerous ASCII, ISO, IBM, national, and vendor encodings. [IANA Character Sets registry](https://www.iana.org/assignments/character-sets).

**[D]** Current ClearPath OS 2200 documentation still describes character sizes of 6, 9, or 18 bits. This establishes architectural survival of six-bit character handling, though not that modern interchange defaults to FIELDATA. [Unisys ClearPath OS 2200 glossary](https://www.support.unisys.com/2200/docs/CP20.0/PDFs/00_GLOSS.PDF).

---

# The code in detail

## The Army structure

### Logical arrangement

**[D/R]** The Army arrangement was:

```text
tag bit = 0    64 supervisory/control positions
tag bit = 1    64 primary positions: formatting, capitals,
               punctuation, digits, and case/extension functions
```

Within each half, the six-bit value was conventionally shown as:

```text
2 indicator bits | 4 detail bits
```

Thus a full interchange character was:

```text
tag | indicator | detail
 1  |     2     |   4       = 7 information bits
```

**[D]** A 1960 Army description says that for transmission the character contained eight binary digits. The coherent reading is seven code bits plus a transmission check/parity bit, not an additional repertoire bit. [September 1960 Army *Artillery* description](https://tradocfcoeccafcoepfwprod.blob.core.usgovcloudapi.net/fires-bulletin-archive/1960/SEP_1960/SEP_1960_FULL_EDITION.pdf).

### Primary half

The following is the representative Army primary layout reconstructed from the 1959 Luebbert paper and Mackenzie. Names varied slightly among documents.

| Seven-bit octal | Six-bit value | Function or graphic |
|---:|---:|---|
| 100 | 00 | MS—Master Space |
| 101 | 01 | UC—Upper Case |
| 102 | 02 | LC—Lower Case |
| 103 | 03 | Horizontal tab |
| 104 | 04 | Carriage return |
| 105 | 05 | Space |
| 106–137 | 06–37 | A–Z |
| 140–171 | 40–71 | punctuation and digits |
| 172–175 | 72–75 | further punctuation |
| 176 | 76 | Special/extension |
| 177 | 77 | Delete or idle, depending on profile |

**[D/R]** The alphabet starts at low six-bit value `06` and is contiguous through `37` octal. Digits occupy `60`–`71`. This structure is visibly related to the later “four sticks of sixteen” reasoning used in ASCII design: functions and spacing first, alphabet in dense order, punctuation and digits in regular blocks.

### Supervisory half

A representative military supervisory block is:

| Octal | Name | Meaning |
|---:|---|---|
| 000 | IDL | Idle/blank |
| 001 | CUC | Control upper case |
| 002 | CLC | Control lower case |
| 003 | CHT | Control horizontal tab |
| 004 | CCR | Control carriage return |
| 005 | CSP | Control space |
| 006–037 | a–z | alphabetic supervisory information, where supported |
| 040–051 | D0–D9 | dial/addressing functions; assignments varied |
| 052 | SCB/SOC | Start control block |
| 053 | SBK/SOB | Start block |
| 054–057 | spare/SOD/stop | profile-dependent |
| 060 | RTT | Ready to transmit |
| 061 | RTR | Ready to receive |
| 062 | NRR | Not ready to receive |
| 063 | EBE/EOBK | End blockette |
| 064 | EBK/EOB | End block |
| 065 | EOF | End file |
| 066 | ECB/EOC | End control block |
| 067 | ACK/ACR | Acknowledge receipt |
| 070 | RPT/RBK | Repeat block |
| 071–074 | ISN, NISN, CWF and spare | order varied |
| 075 | SAC | Special application control |
| 076 | SPC | Special character/extension |
| 077 | DEL | Delete |

**[D/R]** This is a representative table, not a universal one. COMLOGNET, SACCOMNET/465L, and “Standard Form” defined different controls. FIELDATA’s project-level goal was interoperability, but its supervisory layer was never stabilized sufficiently to make every nominally FIELDATA installation transparently interoperable.

That is one of the central ironies of the project: it successfully exposed the need for a common control vocabulary while demonstrating how difficult it was to impose one across incompatible military systems.

## UNIVAC six-bit FIELDATA

UNIVAC adopted a six-bit derivative corresponding broadly to the military primary half. Six characters packed exactly into a 36-bit word.

### Full UNIVAC table

**[D/M]** This table follows UNIVAC manuals as collated by John Walker. `¤` and `≠` are representative display glyphs; hardware differed.

| Octal | Bits | Character | Military-origin function or device note |
|---:|:---:|:---:|---|
| 00 | 000000 | `@` | Master Space on military equipment; sometimes displayed as inverted delta |
| 01 | 000001 | `[` | Upper Case |
| 02 | 000010 | `]` | Lower Case |
| 03 | 000011 | `#` | LF on 1107/1108 console Teletypes |
| 04 | 000100 | `Δ` | CR on 1107/1108; some sites swapped this with `@` |
| 05 | 000101 | space | Space |
| 06 | 000110 | `A` |  |
| 07 | 000111 | `B` |  |
| 10 | 001000 | `C` |  |
| 11 | 001001 | `D` |  |
| 12 | 001010 | `E` |  |
| 13 | 001011 | `F` |  |
| 14 | 001100 | `G` |  |
| 15 | 001101 | `H` |  |
| 16 | 001110 | `I` |  |
| 17 | 001111 | `J` |  |
| 20 | 010000 | `K` |  |
| 21 | 010001 | `L` |  |
| 22 | 010010 | `M` |  |
| 23 | 010011 | `N` |  |
| 24 | 010100 | `O` |  |
| 25 | 010101 | `P` |  |
| 26 | 010110 | `Q` |  |
| 27 | 010111 | `R` |  |
| 30 | 011000 | `S` |  |
| 31 | 011001 | `T` |  |
| 32 | 011010 | `U` |  |
| 33 | 011011 | `V` |  |
| 34 | 011100 | `W` |  |
| 35 | 011101 | `X` |  |
| 36 | 011110 | `Y` |  |
| 37 | 011111 | `Z` |  |
| 40 | 100000 | `)` |  |
| 41 | 100001 | `-` |  |
| 42 | 100010 | `+` |  |
| 43 | 100011 | `<` |  |
| 44 | 100100 | `=` |  |
| 45 | 100101 | `>` |  |
| 46 | 100110 | `&` |  |
| 47 | 100111 | `$` |  |
| 50 | 101000 | `*` |  |
| 51 | 101001 | `(` |  |
| 52 | 101010 | `%` |  |
| 53 | 101011 | `:` |  |
| 54 | 101100 | `?` |  |
| 55 | 101101 | `!` |  |
| 56 | 101110 | `,` |  |
| 57 | 101111 | `\` or stop sign | STOP |
| 60 | 110000 | `0` |  |
| 61 | 110001 | `1` |  |
| 62 | 110010 | `2` |  |
| 63 | 110011 | `3` |  |
| 64 | 110100 | `4` |  |
| 65 | 110101 | `5` |  |
| 66 | 110110 | `6` |  |
| 67 | 110111 | `7` |  |
| 70 | 111000 | `8` |  |
| 71 | 111001 | `9` |  |
| 72 | 111010 | `'` |  |
| 73 | 111011 | `;` |  |
| 74 | 111100 | `/` |  |
| 75 | 111101 | `.` |  |
| 76 | 111110 | `¤` | SPEC; some later mappings use `"` |
| 77 | 111111 | `≠` | IDLE; some later mappings use `_` |

The contemporary UNIVAC-derived table, card punches, and device exceptions are collected at [UNIVAC 1100 Series FIELDATA Code](https://www.fourmilab.ch/documents/univac/fieldata.html).

### Repertoire and limitations

**[D]** Native UNIVAC FIELDATA expresses:

- 26 unaccented Latin capitals;
- ten decimal digits;
- space;
- about 27 visible punctuation or mathematical characters, depending on device glyphs;
- a few device-sensitive control meanings.

It cannot natively express:

- lowercase as distinct stored letters;
- accented Latin letters;
- Greek, apart from a delta-shaped device glyph not reliably representing linguistic Greek;
- Cyrillic, Hebrew, Arabic, Indic scripts, CJK writing, combining marks, or emoji;
- a general-purpose newline character consistently across all devices;
- arbitrary binary octets without treating the word as binary rather than six-bit text.

### The case question

**[D/R]** The Army seven-bit scheme possessed UC and LC functions because its architecture could select cases or extended repertoires. The common UNIVAC six-bit set stored only capitals. Lowercase input was normally folded to uppercase or could be represented only through application-specific conventions.

**[R]** Six bits were attractive precisely because 64 states fit capitals, digits, space, and enough punctuation for business and scientific work. A true upper- and lowercase alphabet consumes 52 positions before digits or punctuation. The case problem therefore helped force the move toward seven-bit interchange.

### Collating order

**[D]** Numeric comparison of UNIVAC FIELDATA values yields:

```text
@ [ ] # Δ space A ... Z ) - + < = > & $ * ( % : ? ! , \ 0 ... 9 ' ; / . ¤ ≠
```

Thus:

- controls or special graphics sort before space;
- space sorts before letters;
- letters are contiguous in alphabetic order;
- punctuation intervenes between letters and digits;
- digits are contiguous but sort after most punctuation.

UNIVAC ALGOL documentation explicitly says string collation follows FIELDATA order. [UNIVAC 1108 ALGOL manual](https://www.fourmilab.ch/documents/univac/manuals/pdf/1108/UP-7544_1108_ALGOL_Jul68.pdf).

**[D]** IBM’s BCD machines sometimes used hardware comparison matrices or transformed sort keys because physical bit order and desired commercial collating order differed. Bemer’s 1960 survey points to the IBM 704 and 705 as examples. [Bemer, “Survey of Coded Character Representation”](https://www.ed-thelen.org/comp-hist/SurveyCodedCharacterRepresentation_Bemer_CACM_Dec1960.pdf).

### Space, newline, deletion, and idle

**Space.** `05` octal is ordinary space. `00`, Master Space, was a distinguishable all-zero state.

**Newline.** There is no universal single FIELDATA newline:

- Army primary `03` and `04` were tab/carriage-return-related controls.
- On UNIVAC 1107/1108 Teletype 35 consoles, `03` functioned as LF and `04` as CR.
- Other peripherals printed glyphs for those values.
- Consequently a file’s line structure could be record-oriented rather than encoded with an in-band newline.

**Delete/idle.** In the military seven-bit table, all ones (`177`) was DEL. In the UNIVAC six-bit derivative, `77` could mean IDLE, print `≠`, or terminate output, depending on equipment.

**[R]** Like ASCII DEL `0x7F`, an all-ones delete value was convenient on punched media: punching every position could obliterate an erroneous character. This is structural evidence for the convention. It is not evidence that FIELDATA alone invented it; all-holes erase conventions predate both FIELDATA and ASCII.

### Shift and escape mechanisms

**[D/R]** UC, LC, and SPEC were state-changing or extension functions in suitable Army profiles. They are therefore analogous to, but not identical with:

- ITA2/Baudot-style Letters and Figures shifts;
- ASCII `SO`, `SI`, and `ESC`;
- later ISO 2022 designation and invocation mechanisms.

A receiver that loses a shift character can misinterpret everything until another explicit shift restores the intended state. This is the characteristic synchronization weakness of stateful encodings.

The stand-alone UNIVAC graphical set was mostly stateless: each six-bit quantity identified one local character. Device modes could still make values such as `03`, `04`, `57`, and `77` context-dependent.

### Error detection and synchronization

**[D]** FIELDATA’s logical code does not have intrinsic Hamming-distance protection. Every one-bit alteration turns one legal code point into another legal code point.

Transmission systems supplied framing, parity, block control, acknowledgments, and retransmission:

- a parity/check bit could expand seven information bits to an eight-bit transmitted unit;
- SCB/SBK and ECB/EBK delimited blocks;
- ACK and RPT supported acknowledgement and repeat requests;
- RTT/RTR/NRR negotiated readiness.

**[D/R]** A reader entering at an arbitrary seven-bit boundary cannot infer alignment merely from the code values: all 128 patterns are potentially meaningful. Physical synchronous framing, tape tracks, character clocks, or block envelopes had to supply alignment. A reader entering mid-stream in a stateful UC/LC/SPEC mode might also lack the current repertoire state until another shift or protocol boundary.

This differs sharply from UTF-8, whose continuation-byte pattern gives limited self-synchronization. FIELDATA has fixed-width simplicity but no byte-pattern resynchronization property.

---

## Worked examples

### `FIELD DATA`

#### UNIVAC FIELDATA

| Character | Octal | Bits |
|:---:|---:|:---:|
| F | 13 | 001011 |
| I | 16 | 001110 |
| E | 12 | 001010 |
| L | 21 | 010001 |
| D | 11 | 001001 |
| space | 05 | 000101 |
| D | 11 | 001001 |
| A | 06 | 000110 |
| T | 31 | 011001 |
| A | 06 | 000110 |

Packed sequentially:

```text
001011 001110 001010 010001 001001 000101
001001 000110 011001 000110
```

The first six characters fit one 36-bit word:

```text
13 16 12 21 11 05   (octal six-bit characters)
```

The remaining four require another word or record packing convention.

#### ASCII-1968 / US-ASCII

| Character | Hex | Seven bits |
|:---:|---:|:---:|
| F | 46 | 1000110 |
| I | 49 | 1001001 |
| E | 45 | 1000101 |
| L | 4C | 1001100 |
| D | 44 | 1000100 |
| space | 20 | 0100000 |
| D | 44 | 1000100 |
| A | 41 | 1000001 |
| T | 54 | 1010100 |
| A | 41 | 1000001 |

RFC 20 transmitted these in eight-bit fields with a zero high bit. [RFC 20](https://www.rfc-editor.org/info/rfc20/).

#### DEC ASCII-derived SIXBIT

DEC’s later PDP-6/PDP-10 SIXBIT is obtained, for ordinary printable ASCII, by subtracting octal `040` and retaining six bits.

```text
F     ASCII 106₈ → SIXBIT 46₈
I     ASCII 111₈ → SIXBIT 51₈
E     ASCII 105₈ → SIXBIT 45₈
L     ASCII 114₈ → SIXBIT 54₈
D     ASCII 104₈ → SIXBIT 44₈
space ASCII 040₈ → SIXBIT 00₈
```

This SIXBIT is not FIELDATA. DEC’s name is a generic descriptive term, and its code preserves ASCII’s printable ordering rather than the UNIVAC FIELDATA assignments. A DEC educational manual gives the subtract-`040` rule and explains why six six-bit characters fit a 36-bit word. [Introduction to DECsystem-10](https://bitsavers.org/pdf/dec/pdp10/Sze_Introduction_to_DEC_System-10_1974.pdf).

### `A1\n`

| Encoding | Representation |
|---|---|
| UNIVAC FIELDATA console convention | `A=06`, `1=61`, CR=`04`, LF=`03` octal |
| ASCII | `A=41`, `1=31`, CR=`0D`, LF=`0A` hexadecimal |
| IBM 704 BCD tape | machine- and tape-translation-dependent; `A` is stored as zone `01`, digit `1`, but written to tape with zone `11` |

This example illustrates why merely agreeing that all machines had “A,” “1,” and a new line did not make their files interchangeable.

---

# Origins

## Telegraphic ancestry: Morse, Baudot, and Murray

**[D/R]** FIELDATA’s conceptual ancestors were telegraph codes rather than modern abstract character repertoires.

- Émile Baudot developed a five-unit printing-telegraph code in the 1870s.
- Donald Murray’s early-twentieth-century code reorganized assignments for keyboard and paper-tape machinery.
- International Telegraph Alphabet No. 2 standardized a Murray-derived five-bit scheme.
- Because five bits provide only 32 states, Letters and Figures shifts made most values state-dependent.

**[R]** FIELDATA inherited the idea that a code includes operational functions—shift, carriage movement, idle, signal control—not merely printed characters. Its seven-bit split between primary and supervisory halves can be understood as an attempt to enlarge and regularize that combined alphabet-and-protocol tradition.

## Hollerith and punched-card ancestry

**[D/R]** Herman Hollerith’s card systems represented values by punch position rather than initially by a compact binary integer. IBM’s later 80-column card repertoire used zone punches plus digit punches. Early computer “BCD” codes were engineered for economical conversion between six-bit memory characters and those card patterns.

This heritage explains:

- alphabetic blocks A–I, J–R, S–Z;
- special treatment of zero;
- non-contiguous punctuation;
- the frequent divergence between internal memory code and magnetic-tape code;
- commercial pressure to retain installed card punches, sorters, printers, and data archives.

## The 1950s code babel

**[D]** Bemer’s December 1960 *Communications of the ACM* survey printed a multi-page comparison of internal computer, paper-tape, and communications codes. Its announced purpose was both to give the new ASA X3.2 subcommittee working data and to demonstrate why standardization was urgent. [Original survey scan](https://www.ed-thelen.org/comp-hist/SurveyCodedCharacterRepresentation_Bemer_CACM_Dec1960.pdf).

**[P/X]** Bemer later summarized the result as “over 60 different ways” of coding the alphabet. Modern retellings often sharpen this into “IBM alone used more than sixty codes.” The published 1960 chart surveys the industry, not sixty IBM-only alphabets. IBM unquestionably maintained numerous mutually incompatible internal, card, tape, printer, and communications mappings, but I found no contemporary IBM memo demonstrating **sixty-odd IBM codes alone**.

Accordingly:

- “more than sixty codes in the industry” is supported by Bemer’s published survey and recollection;
- “more than sixty at IBM alone” is an amplified and insufficiently documented version;
- calling the situation a “Babel of codes” comes from the title of Bemer’s later historical webpage, not from the title of his 1960 article.

## IBM BCD variants

### Basic structure

**[D]** IBM 704 storage used six-bit characters, commonly described as two zone bits plus four numeric bits:

```text
zone | digit
  2  |  4
```

The mapping reflected punched cards. The 704 manual shows, for example:

| Character | Core storage | Magnetic tape |
|---|---:|---:|
| 0 | `00 0000` | `00 1010` |
| 1 | `00 0001` | `00 0001` |
| A | `01 0001` | `11 0001` |
| B | `01 0010` | `11 0010` |

The zero code was changed on tape because an all-zero character could be confused with an inter-record gap and could not satisfy the peripheral’s even-parity convention. [IBM 704 Manual, form 24-6661-2, 1955](https://bitsavers.org/pdf/ibm/704/24-6661-2_704_Manual_1955.pdf).

**[D]** “IBM BCD” therefore does not identify one stable encoding. IBM 702, 704, 705, 709, 1401, printer, card, and tape environments used related but non-identical mappings. Translation hardware and software were normal parts of the system.

### Why BCD persisted

**[R]** BCD’s virtue was compatibility with capital investment: cards, keypunches, accounting records, collators, and printers. Its defects as a universal interchange code were precisely the consequences of this strength—irregular punctuation, machine-specific translation, and a repertoire organized around one vendor’s media ecology.

## UNIVAC codes

**[D/R]** UNIVAC systems also used several character schemes. Earlier UNIVAC equipment had machine-specific six-bit and excess-three-related representations. The UNIVAC 1107/1108 line adopted the FIELDATA-derived set because a 36-bit word naturally held six characters.

**[D]** EXEC II documentation includes a selectable “BCD to Fieldata software converter,” direct evidence that production sites routinely crossed encoding boundaries. [UNIVAC 1108 EXEC II Programmer’s Reference](https://www.fourmilab.ch/documents/univac/manuals/pdf/1108/UP-4058_EXEC_II_Programmers_Ref_Man_1966.pdf).

## CDC display codes

**[D]** Control Data’s 1604 and later 6000-series systems used six-bit display codes, again with variants. On CDC 6000 systems a common 64-character arrangement placed:

```text
00–04  : 0–4
05–17  : 5–9 and basic arithmetic punctuation
20–37  : further punctuation and mathematical signs
40–71  : A–Z
72–77  : remaining punctuation
```

Exact glyphs depended on display, printer, and terminal repertoire. CDC manuals include conversion tables among 6000 display code, BCD terminals, and ASCII terminals. [CDC INTERCOM Reference Manual, 1971](https://bitsavers.org/pdf/cdc/cyber/intercom/60252800A_INTERCOM_Reference_Manual_6000_Version_3_Mar1971.pdf).

**[R]** “CDC display code” is thus a family name. Treating a modern Unicode transcription of its mathematical signs as the exact appearance of every historical installation would be a modern reconstruction.

## DEC SIXBIT

**[D]** DEC SIXBIT is principally an ASCII compression:

```text
SIXBIT = (ASCII − 040₈) mod 100₈
```

It represents the ASCII printable range `0x20–0x5F`: space, punctuation, digits, `@`, and capital letters. Lowercase input is commonly folded to capitals.

**[D]** Six characters fit in one PDP-6/PDP-10 36-bit word. This was valuable for filenames, device identifiers, and FORTRAN names.

**[R]** DEC SIXBIT belongs to the next historical phase: rather than being a rival ancestral code that shaped ASCII, it is a compact derivative of ASCII’s ordering. Confusing it with UNIVAC FIELDATA because both use six bits is an anachronism.

## The FIELDATA program, 1956–59

**[D]** By 1959 the Signal Corps envisioned a hierarchy of interoperable field equipment:

- input and output devices chosen for the military application;
- transmission equipment chosen for the available medium;
- common-language equipment performing conversion, error control, cryptographic support, and supervision;
- computers at different echelons sharing information without treating communications and data processing as separate worlds.

Luebbert’s paper describes a modular interface in which paper tape, cards, typewriters, printers, and computers could connect through common-language equipment to several modulation and transmission systems.

**[D]** A companion conference paper, “Automatic Data Processing in the Tactical Field Army,” reported that a simulation center had become operational in February 1959 and that prototype hardware was expected beginning later that year. The projected prototype system was to operate by 1963.

### Machines

**[D/R]** Machines associated with the program included:

- Sylvania’s MOBIDIC—Mobile Digital Computer;
- Philco’s BASICPAC;
- Philco’s LOGICPAC;
- the planned ARTOC graphical-output system;
- an IBM 709 used as a simulation source and sink during tests.

The Ballistic Research Laboratories’ 1961 computer survey records systems using FIELDATA-compatible tape equipment. [BRL 1961 report transcription](https://ed-thelen.org/comp-hist/BRL61-a.html).

### “First common military character set”

**[R/X]** FIELDATA is reasonably described as the first large, organized U.S. attempt to define a common military computer-and-communications character code. It should not be called the first military communications code without qualification: armed forces had long used Morse, Baudot/ITA2, teletype alphabets, cryptographic formats, and service-specific signal codes.

Its novelty lay in seeking one structured vocabulary spanning computers, tactical data links, media, and supervisory exchange.

---

# From FIELDATA to ASCII

## Formation of the standards work

**[D]** The American Standards Association established Sectional Committee X3 for computers and information processing. X3 first met on 4 August 1960; subcommittee X3.2 handled coded character sets and formats.

The principal institutional lineage was:

```text
Army and vendor codes
        ↓
EIA TR 24.4 proposals and surveys
        ↓
ASA X3 / X3.2 deliberations
        ↓
ASA X3.4-1963
        ↓
USAS X3.4-1967/1968
        ↓
ANSI X3.4 and ISO/IEC 646
```

## People and roles

### Robert W. Bemer

**[D]** Robert William Bemer (1920–2004), working at IBM in the relevant period, published:

- “A Proposal for Character Code Compatibility,” *CACM* 3(2), February 1960, pp. 71–72;
- “Survey of Coded Character Representation,” *CACM* 3(12), December 1960;
- with H. J. Smith Jr. and F. A. Williams Jr., “Design of an Improved Transmission/Data Processing Code,” May 1961.

**[P]** Bemer later claimed important responsibility for ESC, backslash, braces, and eight-bit thinking. His preserved personal history provides valuable dates and citations but is still a participant’s retrospective case for his own priority. [Preserved Bemer material and bibliography](https://www.histo.cat/sabies/bob-bemer).

### Hugh McGregor Ross

**[D/P]** British engineer Hugh McGregor Ross worked in BSI, ISO, and CCITT character-code deliberations and advocated an internationally regular code structure. Retrospective interviews sometimes call the emerging scheme the “Bemer–Ross code,” but ASCII was committee work, not a two-person invention. [Archived Ross discussion](https://archive.ph/nt5S).

### William F. Luebbert

**[D]** Luebbert documented FIELDATA’s communications architecture and the representative code. He is the clearest contemporary named expositor of the military design, though the surviving evidence does not justify naming him as its sole inventor.

### H. J. Smith Jr. and F. A. Williams Jr.

**[D]** Their 1961 paper with Bemer formalized code-placement constraints: contiguous alphabets, useful collation, adjacency of blanks, compatibility with transmission, and the organization of 64-character quadrants. [“Design of an Improved Transmission/Data Processing Code”](https://www.ed-thelen.org/comp-hist/ImprovedDataProcessingCode_BemerSmithWilliams_CACM_May1961.pdf).

### Charles E. Mackenzie

**[R]** Mackenzie was not a 1950s FIELDATA inventor. His 1980 *Coded Character Sets: History and Development* is the most substantial published reconstruction of the path from cards and BCD through FIELDATA, ASCII, and EBCDIC. [Internet Archive/Open Library record and edition data](https://openlibrary.org/books/OL4570655M/Coded_character_sets).

## How strong was FIELDATA’s influence?

**[D/R]** The strongest evidence is structural and institutional:

- FIELDATA organized a 128-position space into a 64-control/supervisory half and a 64-primary half.
- Its primary half used two indicator bits and four detail bits.
- It placed spacing and format functions at the beginning.
- It kept the Latin alphabet contiguous.
- It reserved an all-ones delete.
- FIELDATA representatives participated strongly in X3.2.
- Contemporary post-standard commentary predicted that FIELDATA would be replaced by ASCII while praising its representatives’ contribution.

A 1963 account states that FIELDATA representation on X3.2 had been “very strong and valuable” and that Department of Defense preference for national standards enabled replacement rather than parallel perpetuation. [Bemer archival published-paper collection](https://archive.computerhistory.org/resources/access/text/2021/04/102785423-05-02-acc.pdf).

**[X]** “ASCII was copied from FIELDATA” is too strong. ASCII also grew from:

- telegraph control practice;
- EIA paper-tape proposals;
- IBM and other vendor codes;
- international CCITT and ISO work;
- programming-language punctuation requirements;
- sorting and case-folding constraints.

The documented conclusion is influence and personnel continuity, not single-parent descent.

## ASCII’s design decisions

### Seven bits

**[D/R]** Seven bits gave 128 positions—enough for control characters, capitals, lowercase, digits, and punctuation—while remaining cheaper in transmission and storage than a mandatory eight-bit information code.

### The lowercase fight

**[D/R]** The 1963 standard left many positions unassigned while the committee and international bodies decided between more controls and lowercase. Later revisions placed lowercase in columns related by one bit to capitals. This allowed simple case folding.

### Controls

**[D]** ASCII established C0 controls in columns 0 and 1, space at `0x20`, visible characters through `0x7E`, and DEL at `0x7F`. Unlike FIELDATA’s application-variable supervisory half, the control positions received a national standard interpretation.

### Currency sign

**[D/R]** Dollar-sign placement reflected U.S. use; international ISO 646 national variants later substituted national currency signs and letters in designated positions. This produced mutually incompatible “ASCII-like” national sets.

### Escape

**[P/X]** Bemer credited himself with putting ESC into the emerging code, motivated by extension to future repertoires. Contemporary proposals and committee records establish that escape/extension was an active design subject. The singular “Bemer invented ESC” formula rests heavily on Bemer’s later account and should be reported as participant recollection, not uncontested sole invention.

## Publication and mandate

**[D]** ASA X3.4-1963 was approved 17 June 1963. Revisions culminated in the substantially familiar USAS X3.4-1967/1968 code.

**[D]** President Lyndon B. Johnson’s memorandum of 11 March 1968 adopted the code for federal use. It required computers and related equipment entering the federal inventory on or after 1 July 1969 to have ASCII capability, subject to scope and exceptions. It did **not** require every internal machine representation to become ASCII. [Presidential memorandum](https://www.presidency.ucsb.edu/documents/memorandum-approving-the-adoption-the-federal-government-standard-code-for-information).

**[D]** FIPS PUB 1 followed on 1 November 1968. Commerce implementation instructions were issued in March 1969. [Federal implementation publication](https://www.govinfo.gov/content/pkg/GOVPUB-C13-4ee2fd3bf7ff5240fc0fe3cd9f14af3f/pdf/GOVPUB-C13-4ee2fd3bf7ff5240fc0fe3cd9f14af3f.pdf).

---

# Adoption and decline

## Military use

**[D/R]** FIELDATA was used or planned for the Army’s late-1950s tactical information systems and influenced military communications standards. Its adoption was nonetheless fragmented:

- different systems assigned different supervisory controls;
- hardware programs proceeded on separate schedules;
- installed machines still needed converters;
- reorganization and the arrival of a national code weakened the case for a separate Army alphabet.

**[R/X]** “The FIELDATA project ended in 1962” is repeated widely, including encyclopedia-derived pages, but those pages themselves often mark the date as needing a citation. MIL-STD-188 revisions continued to mention the scheme after 1962. The safer conclusion is that the integrated computer-development program lost institutional momentum around the early 1960s, while documents and installed descendants outlived it.

## UNIVAC adoption

**[D]** The six-bit derivative became the native compact text representation of UNIVAC 1107, 1108, and later 1100-series software. Fourmilab’s compiled manual evidence documents:

- six characters per 36-bit word;
- card-punch mappings;
- console CR/LF use;
- STOP and IDLE device behavior;
- site-specific swapping of `@` and delta;
- coexistence with ASCII.

Later UNIVAC software used ASCII packed four characters per 36-bit word, normally in nine-bit slots. [UNIVAC ASCII FORTRAN reference](https://www.fourmilab.ch/documents/univac/manuals/pdf/Software/UP8244.pdf).

## IBM rejection and EBCDIC

**[D/R]** IBM did not make ASCII its universal System/360 internal code. Instead it introduced EBCDIC, an eight-bit extension of its BCD/punched-card lineage.

The “eight-bit defense” is often reduced to “IBM chose EBCDIC because ASCII was only seven-bit.” The actual pressures were broader:

- compatibility with IBM punched-card assignments;
- existing software and peripherals;
- the System/360’s eight-bit byte;
- an immediate need for 256 code positions;
- IBM’s ability to control its own migration timetable.

### The System/360 ASCII bit story

**[P/X/F]** System/360 documentation and architecture included ASCII-related facilities, and contemporary plans contemplated ASCII interchange. Retrospective accounts say the 360’s byte-width or an ASCII-adjust facility was evidence that IBM expected to use ASCII, only to retreat under compatibility pressure.

The stronger folklore says an “unused ASCII bit” was deliberately left in every 360 byte as a failed bet. That is misleading: an eight-bit byte is useful independently for binary arithmetic and 256-value character codes, and EBCDIC used all eight bits. No single unused physical bit sat idle in ordinary EBCDIC storage.

Bemer’s recollections are important testimony, but the motivational story is not independently documented as a one-cause decision.

## ARPANET

**[D]** RFC 20, written by Vint Cerf and dated 16 October 1969, proposed standard seven-bit ASCII in an eight-bit byte with the high bit zero for host-to-host primary connections. This is direct evidence that the young ARPANET needed a code independent of host-native representation. [RFC 20](https://www.rfc-editor.org/info/rfc20/).

**[D]** RFC 5198’s retrospective account says ARPANET hosts used at least BCD, EBCDIC, and emerging ASCII. Because the network was open and EBCDIC was closely tied to one manufacturer, the Network Working Group chose ASCII as an intermediate representation. Hosts translated at the boundary. [RFC 5198](https://www.rfc-editor.org/rfc/rfc5198.html).

The line ending adopted by Telnet and many Internet protocols was CR followed by LF. This preserved teleprinter mechanics in protocol long after physical carriages disappeared.

## Decline

**[D/R]** FIELDATA declined because:

- ASCII became a U.S. standard and then a federal procurement requirement;
- ASCII had both cases and a standardized control block;
- ARPANET and later Internet protocols adopted ASCII;
- UNIVAC itself added ASCII modes;
- international work converged around ISO 646 and later ISO 2022/8859 and Unicode.

It was absorbed rather than erased. Its legacies include:

- six-bit packed fields in 36-bit systems;
- archived government and scientific data;
- converters in UNIVAC/Unisys software;
- the familiar separation of control and graphic regions;
- contiguous alphabetic ordering;
- all-ones deletion;
- the broader principle that an interchange code should not simply be one machine’s internal code.

## Surviving data hazards

**[D]** A Census Bureau working paper documents recovery of old Unisys tapes by decoding alternative copies under FIELDATA and excess-three assumptions. It explains six-character words and even uses `@@@@J*` as the FIELDATA representation of decimal 1000. [Census data-recovery paper](https://www2.census.gov/ces/wp/2014/CES-WP-14-37.pdf).

This is FIELDATA’s characteristic modern failure mode: not web mojibake but archival ambiguity. A six-bit word read under the wrong mapping still produces plausible capitals and punctuation, so errors may be semantically silent.

---

# The other scripts

## Latin outside English

**[D]** Base FIELDATA has no accents or lowercase stored letters. Names such as `MÜLLER`, `GARCÍA`, `DVOŘÁK`, or `François` must be:

- stripped of diacritics;
- uppercased and transliterated;
- represented by application escape conventions;
- or stored outside the FIELDATA text field.

This loses distinctions and can make separate names collate identically.

## Greek

**[D]** A delta-shaped printer glyph does not constitute Greek support. There is no Greek alphabet, accent system, or final sigma. Sites needed transliteration, custom fonts, or non-FIELDATA codes.

## Cyrillic

**[R]** Six-bit Soviet and Eastern European codes sometimes exploited the visual similarity of Latin and Cyrillic capitals or used shift states. KOI-7 and later KOI8 are separate developments, not FIELDATA extensions.

**[F/M]** The “KOI8 trick”—that stripping the high bit leaves a readable Latin transliteration of Russian—is substantially true for deliberately corresponding letters, but not for every Cyrillic character and not a FIELDATA design principle.

## Hebrew and Arabic

FIELDATA cannot encode their letters. Even a replacement glyph table would not solve:

- right-to-left ordering;
- Arabic contextual shaping;
- combining marks;
- numerals embedded in right-to-left text;
- bidirectional punctuation.

Those require conventions above raw character identity. ISO 8859 later assigned Hebrew and Arabic character repertoires but still relied on higher-level layout conventions; Unicode eventually standardized bidi behavior separately.

## Indic scripts

A six-bit one-character/one-glyph model cannot naturally represent Indic consonant-vowel combinations, combining marks, reordering, conjuncts, or shaping. Transliteration or application-specific glyph codes were required.

## Chinese, Japanese, and Korean

Sixty-four states are radically inadequate for thousands of ideographs and syllabic characters. Historical solutions included:

- numeric telegraph codes;
- double-byte character sets;
- Japanese JIS standards and Shift_JIS/EUC-JP;
- Chinese GB, Big5, and CNS standards;
- Korean KS encodings;
- private glyph and font codes.

None was an interoperable extension of FIELDATA.

## Emoji

Emoji have no meaningful direct FIELDATA history. Any mapping of emoji into a six-bit FIELDATA value would be a private modern invention. Their inclusion in Unicode followed a different ecosystem: Japanese mobile-carrier sets, formal proposals, Unicode Technical Committee review, and standardized properties and sequences.

### Scope finding

**[D]** The requested topics Han unification, Tibetan encoding, emoji voting, UTF-8 overlong sequences, and the BOM concern Unicode’s later history. They are not disputes about FIELDATA or 1950s vendor codes. Treating them as FIELDATA controversies would falsely imply lineage or participation.

Their relevant connection is negative: FIELDATA embodies the small fixed repertoire from which later standards had to escape. ASCII, ISO 2022, ISO 8859, ISO/IEC 10646, and Unicode represent successive answers to limitations that FIELDATA could not solve.

---

# People and institutions

## Engineers and historical predecessors

- **Émile Baudot (1845–1903)** — **[R]** five-unit telegraph code and multiplex telegraphy.
- **Donald Murray (1865–1945)** — **[R]** reorganized five-unit coding for keyboard and punched-tape machinery.
- **Herman Hollerith (1860–1929)** — **[R]** punched-card tabulation; the card-code lineage later constrained IBM encodings.
- **William F. Luebbert** — **[D]** Army officer/engineer and principal published FIELDATA expositor.
- **Robert W. Bemer (1920–2004)** — **[D/P]** IBM programmer and standards advocate; surveyor of pre-ASCII codes; major X3.2 contributor.
- **H. J. Smith Jr. and F. A. Williams Jr.** — **[D]** co-authors of the 1961 placement analysis.
- **Hugh McGregor Ross (1917–2014)** — **[D/P]** British and international character-code standards participant.
- **Charles E. Mackenzie** — **[R]** author of the foundational 1980 history.
- **Vint Cerf** — **[D]** author of RFC 20’s ARPANET ASCII recommendation.

## Companies

- **IBM** — many BCD/card/tape variants; ASCII committee participation; ultimately EBCDIC for System/360.
- **Remington Rand/Sperry Rand/UNIVAC** — adopted six-bit FIELDATA for the 1100 lineage.
- **Sylvania** — MOBIDIC.
- **Philco** — BASICPAC and LOGICPAC.
- **Control Data Corporation** — six-bit display-code families.
- **Digital Equipment Corporation** — later ASCII-derived SIXBIT on 36-bit machines.
- **Teletype Corporation** — terminals whose mechanical functions strongly shaped control codes.

## Standards institutions

- **U.S. Army Signal Corps / USASRDL** — FIELDATA sponsor.
- **EIA TR 24.4** — paper-tape and transmission-code work.
- **ASA X3 and X3.2** — U.S. information-processing standards committees.
- **USASI/ANSI** — successor names/institutions publishing ASCII revisions.
- **CCITT** — international telegraph alphabets and telecommunications coordination.
- **ECMA and ISO** — international code harmonization, especially ECMA-6, ISO 646, and ISO 2022.
- **NBS/NIST** — federal standards administration.
- **ARPA Network Working Group / IETF** — ASCII and later network-text conventions.

## About the later Unicode names in the general brief

Becker, Davis, Collins, Thompson, Pike, Whistler, and the Unicode founders belong to a later dossier on Unicode/UTF-8, not to FIELDATA’s documented design committee. No primary evidence found in this search associates them with FIELDATA.

The Ken Thompson–Rob Pike placemat story concerns UTF-8’s 1992 design. Pike is a participant witness and the story is often supported principally by his own account; it should not be imported into FIELDATA history merely because both are encodings.

---

# Culture

## “Plain text”

**[R]** FIELDATA shows that “plain text” was never entirely plain. A nominal character value depended on:

- device glyph;
- case state;
- record structure;
- card-punch mapping;
- whether a value was interpreted as a graphic or machine control;
- local conversion tables.

ASCII reduced this ambiguity but did not abolish it. Unicode separates characters from glyphs more systematically, yet fonts, normalization, segmentation, directionality, and rendering remain essential.

## Programming languages

**[D]** Six-bit repertoires shaped what programmers could write:

- uppercase-only identifiers;
- short names packed into machine words;
- substitutes for mathematical notation;
- restricted punctuation;
- compiler-specific overstrikes or keyword operators.

FIELDATA supplied enough punctuation for ALGOL- and FORTRAN-era work better than many earlier commercial codes, but not enough to represent arbitrary source typography.

UNIVAC ALGOL used FIELDATA collation, and later UNIVAC COBOL explicitly distinguished ASCII and FIELDATA data items. [UNIVAC ASCII COBOL supplementary manual](https://www.fourmilab.ch/documents/univac/manuals/pdf/Software/UP8584.pdf).

## ASCII art and the demoscene

**[R]** FIELDATA itself did not produce a well-documented distinct art scene. Its limited graphics could make banners and printer patterns, as any fixed-width repertoire could, but the named traditions “ASCII art,” ANSI art, PETSCII art, and demoscene text graphics arose mainly around later terminal and microcomputer repertoires.

Calling all early printer pictures “ASCII art” is a modern generic usage; a 1950s BCD or FIELDATA printer image is more accurately “typewriter,” “line-printer,” or character art.

## Mojibake

**[M]** The Japanese word *mojibake* (“character transformation/corruption”) became a global computing term much later. FIELDATA users experienced the phenomenon—wrong glyphs and wrong translation tables—but did not ordinarily use that label.

The `@`/delta swap and `77` as IDLE versus `≠` are exemplary pre-mojibake cases. They demonstrate that the aesthetic of encoding corruption is older than the modern word.

## Political representation

**[R]** FIELDATA’s exclusions were mostly consequences of bit economy, equipment cost, U.S. military requirements, and English-language institutional context. The result nonetheless privileged a narrow repertoire and forced other languages into transliteration or private codes.

The later claim that standards bodies decide “which peoples get encoded” is politically meaningful but must be historically qualified:

- FIELDATA was not designed as a worldwide cultural registry.
- Unicode encodes writing-system elements through a public proposal and technical-review process.
- Encoding never by itself guarantees fonts, keyboards, literacy support, correct shaping, or equitable implementation.
- Code-point order is often inherited from earlier national standards; it is not a ranking of peoples.

---

# Controversies and disputes

## 1. Who invented FIELDATA?

**Verdict: open; no sole inventor established.**

**[D]** The contemporary record names an Army laboratory, institutional memoranda, and Luebbert as published expositor.

**[X]** Later summaries sometimes write as if Luebbert personally designed the code. His paper documents and explains it but does not establish exclusive authorship. Committee rosters and draft attribution for the April/August 1959 memorandum remain important archival targets.

## 2. Was it six, seven, or eight bits?

**Verdict: all three descriptions can be correct at different layers.**

- **Six:** UNIVAC’s stored graphics and the Army primary half.
- **Seven:** Army tag plus six-bit position.
- **Eight:** transmitted seven-bit character plus parity/check bit.

Any source giving one number without identifying the layer is incomplete.

## 3. Was FIELDATA the direct ancestor of ASCII?

**Verdict: influential precursor, not sole parent.**

**[D/R]** Layout resemblance, committee participation, and contemporary acknowledgment support influence.

**[X/F]** “ASCII is FIELDATA with different assignments” is false. ASCII emerged from multiple U.S. and international proposals and made materially different choices about controls, lowercase, punctuation, and extension.

## 4. Did Bemer find sixty codes at IBM alone?

**Verdict: the strongest form is unsupported.**

**[D]** His 1960 survey documents a very large industry-wide multiplicity.

**[P]** He later remembered “over 60 different ways.”

**[F]** Popular accounts increasingly say “sixty at IBM alone.” No consulted contemporary document substantiates that exact scope.

## 5. Is Bemer “the father of ASCII”?

**Verdict: honorific, not literal authorship.**

**[D]** He made major published and committee contributions.

**[P]** Many detailed priority claims derive from Bemer’s own later pages.

**[X]** ASCII was produced by X3.2 and negotiated with multiple organizations. The paternal title obscures Smith, Williams, Ross, committee officers, EIA participants, government representatives, manufacturers, and international counterparts.

The Smithsonian holds Bemer’s standards papers—correspondence, reports, minutes, and bulletins from 1959 onward—which remain the proper material for testing individual credit claims. [Smithsonian Computer Standards Collection](https://americanhistory.si.edu/collections/archival-collection/sova-nmah-ac-0310).

## 6. Was FIELDATA interoperable?

**Verdict: partially and imperfectly.**

**[D/R]** It standardized major aspects of equipment communication and a primary repertoire. But supervisory codes differed among military systems. The common-language ideal therefore exceeded deployed uniformity.

## 7. Did `0x7F` DEL come from FIELDATA?

**Verdict: plausible direct influence, not a proven unique invention.**

FIELDATA used an all-ones delete in the Army table; ASCII did too. All-holes deletion was already natural on punched tape. The assignment has a technical ancestry broader than either standard.

## 8. Did FIELDATA invent ASCII’s `ESC`?

**Verdict: related precursor, attribution uncertain.**

Military `SPC` at `076` offered extension/special-character behavior. ASCII assigned ESC at `0x1B`. Bemer’s retrospective story makes him a central advocate for escape, but the shift from FIELDATA SPC to ASCII ESC was committee design, not a demonstrated one-step renaming.

## 9. Was UNIVAC FIELDATA identical everywhere?

**Verdict: no.**

**[D]** Manuals document:

- `00` displayed as `@` or delta;
- `04` displayed as delta or `@`;
- `03`/`04` acting as LF/CR on some consoles;
- `57` printing a stop sign or backslash;
- `77` acting as idle, line terminator, or `≠`;
- later substitutions of `"`, `_`, and `^` during ASCII conversion.

This is unusually strong primary evidence against the notion of one universal glyph table.

## 10. EBCDIC as an “eight-bit defense”

**Verdict: useful slogan, inadequate causal history.**

IBM did exploit a full eight-bit space and preserved its card-code lineage. But describing EBCDIC solely as an anti-ASCII maneuver reduces compatibility, product schedule, installed base, collating requirements, and peripheral engineering to corporate obstinacy.

## 11. Han unification, Tibetan disputes, emoji, BOM, homoglyphs, and overlong UTF-8

**Verdict: not FIELDATA controversies.**

The dedicated searches combining FIELDATA with these terms produced no historically relevant primary controversy. Results were either about an unrelated modern product named “Fieldata” or generic encoding history.

Absence of evidence is informative:

- FIELDATA never attempted Han unification.
- It did not encode Tibetan.
- It had no emoji process.
- Fixed six- or seven-bit characters have no byte-order mark.
- They have no UTF-8-style overlong sequences.
- Their repertoire is too small for the modern cross-script homoglyph problem, although same-glyph/different-function device ambiguities certainly existed.

These matters should appear in dossiers on Unicode, ISO/IEC 10646, or UTF-8, not be retroactively attached to FIELDATA.

---

# Open questions

1. **Who exactly drafted each revision of *FIELDATA Equipment Intercommunication Characteristics*?**  
   The memo is cited by date and office, but accessible references do not establish a complete author/editor list.

2. **What was the exact first approved code table?**  
   The 1959 paper supplies a representative table; later military profiles varied. A dated chain of drafts is still needed.

3. **When precisely did the integrated FIELDATA program terminate?**  
   “1962” is widely repeated but inadequately sourced, while MIL-STD-188 references continued later.

4. **Which deployed systems exchanged genuinely compatible supervisory streams?**  
   Equipment compatibility claims should be tested against preserved COMLOGNET, SACCOMNET/465L, and Standard Form interface manuals.

5. **What is the primary basis for “sixty-odd codes at IBM alone”?**  
   Bemer’s published survey supports an industry-wide babel. An internal IBM memorandum with that narrower count has not been located.

6. **How much of ASCII’s exact layout came through FIELDATA delegates rather than parallel constraint-solving?**  
   X3.2 minutes, ballots, and draft comparison tables in the Smithsonian Bemer collection are the best next sources.

7. **How uniformly did UNIVAC software distinguish FIELDATA text from raw six-bit binary fields?**  
   Surviving recovery projects show that this can be ambiguous when labels and record descriptions are lost.

8. **Does current ClearPath software still expose a named FIELDATA CCS, or only compatible six-bit data types and converters?**  
   Current public documentation establishes six-bit support, but a definitive current product CHARMAP and support-status statement should come from the relevant Unisys release manual.

---

# Sources

## Contemporary standards, government material, papers, and manuals

1. William F. Luebbert, “Data Transmission Equipment Concepts for FIELDATA,” *Proceedings of the 1959 Western Joint Computer Conference*, pp. 189–196:  
   https://bitsavers.org/pdf/afips/1959-03_%2315.pdf

2. U.S. Army, *Artillery*, September 1960, “Standard FIELDATA Code Developed”:  
   https://tradocfcoeccafcoepfwprod.blob.core.usgovcloudapi.net/fires-bulletin-archive/1960/SEP_1960/SEP_1960_FULL_EDITION.pdf

3. Defense Logistics Agency ASSIST, MIL-STD document catalogue:  
   https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=108890

4. R. W. Bemer, “Survey of Coded Character Representation,” *Communications of the ACM* 3(12), December 1960, pp. 639–641:  
   https://www.ed-thelen.org/comp-hist/SurveyCodedCharacterRepresentation_Bemer_CACM_Dec1960.pdf

5. R. W. Bemer, H. J. Smith Jr., and F. A. Williams Jr., “Design of an Improved Transmission/Data Processing Code,” *Communications of the ACM* 4(5), May 1961:  
   https://www.ed-thelen.org/comp-hist/ImprovedDataProcessingCode_BemerSmithWilliams_CACM_May1961.pdf

6. *Communications of the ACM*, volume 3 bibliographic index:  
   https://www.sigmod.org/publications/dblp/db/journals/cacm/cacm3.html

7. IBM, *704 Electronic Data-Processing Machine Manual*, form 24-6661-2, 1955:  
   https://bitsavers.org/pdf/ibm/704/24-6661-2_704_Manual_1955.pdf

8. IBM, *7040/7044 Customer Engineering Handbook*, May 1964:  
   https://bitsavers.org/pdf/ibm/7040/ce/223-2640-2_7040_7044_CE_Handbook_May64.pdf

9. Sperry UNIVAC, *1108 EXEC II Programmer’s Reference Manual*, UP-4058, 1966:  
   https://www.fourmilab.ch/documents/univac/manuals/pdf/1108/UP-4058_EXEC_II_Programmers_Ref_Man_1966.pdf

10. Sperry UNIVAC, *1108 ALGOL*, UP-7544, July 1968:  
    https://www.fourmilab.ch/documents/univac/manuals/pdf/1108/UP-7544_1108_ALGOL_Jul68.pdf

11. Sperry UNIVAC, *1106/1108 Systems 4009 Display Console Programmer Reference*, 1974:  
    https://bitsavers.org/pdf/univac/1100/1108/UP-7604r1_1106_1108_Systems_4009_Display_Console_Programmer_Reference_1974.pdf

12. UNIVAC, *ASCII FORTRAN Programming Reference Manual*:  
    https://www.fourmilab.ch/documents/univac/manuals/pdf/Software/UP8244.pdf

13. UNIVAC, *ASCII COBOL Supplementary Reference Manual*:  
    https://www.fourmilab.ch/documents/univac/manuals/pdf/Software/UP8584.pdf

14. Control Data Corporation, *INTERCOM Reference Manual, 6000 Version 3*, publication 60252800A, March 1971:  
    https://bitsavers.org/pdf/cdc/cyber/intercom/60252800A_INTERCOM_Reference_Manual_6000_Version_3_Mar1971.pdf

15. CDC 1604 manual archive:  
    https://www.bitsavers.org/pdf/cdc/1604/

16. DEC PDP-6 manual archive:  
    https://www.bitsavers.org/pdf/dec/pdp6/

17. Sze, *Introduction to DEC System-10*, 1974:  
    https://bitsavers.org/pdf/dec/pdp10/Sze_Introduction_to_DEC_System-10_1974.pdf

18. Ballistic Research Laboratories, *A Third Survey of Domestic Electronic Digital Computing Systems*, 1961 transcription:  
    https://ed-thelen.org/comp-hist/BRL61-a.html

19. Lyndon B. Johnson, “Memorandum Approving the Adoption by the Federal Government of a Standard Code for Information Interchange,” 11 March 1968:  
    https://www.presidency.ucsb.edu/documents/memorandum-approving-the-adoption-the-federal-government-standard-code-for-information

20. U.S. Department of Commerce, federal implementation of ADP code and media standards, 1969:  
    https://www.govinfo.gov/content/pkg/GOVPUB-C13-4ee2fd3bf7ff5240fc0fe3cd9f14af3f/pdf/GOVPUB-C13-4ee2fd3bf7ff5240fc0fe3cd9f14af3f.pdf

21. National Bureau of Standards/NIST institutional history, including FIPS PUB 1:  
    https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication958.pdf

22. V. G. Cerf, RFC 20, “ASCII format for Network Interchange,” 16 October 1969:  
    https://www.rfc-editor.org/info/rfc20/

23. J. Klensin and M. Padlipsky, RFC 5198, “Unicode Format for Network Interchange,” March 2008, historical discussion of ARPANET coding:  
    https://www.rfc-editor.org/rfc/rfc5198.html

24. RFC Editor index:  
    https://www.rfc-editor.org/rfc-index/

25. IANA Character Sets registry:  
    https://www.iana.org/assignments/character-sets

26. Keld Simonsen, RFC 1345, “Character Mnemonics and Character Sets,” June 1992:  
    https://datatracker.ietf.org/doc/html/rfc1345

## Scholarly reconstructions and archival collections

27. Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley, 1980, ISBN 0-201-14460-3, Internet Archive/Open Library record:  
    https://openlibrary.org/books/OL4570655M/Coded_character_sets

28. Google Books bibliographic record for Mackenzie:  
    https://books.google.com/books/about/Coded_Character_Sets.html?id=6-tQAAAAMAAJ

29. Smithsonian National Museum of American History, Robert W. Bemer Computer Standards Collection, 1959–1979:  
    https://americanhistory.si.edu/collections/archival-collection/sova-nmah-ac-0310

30. Computer History Museum, Bemer published-papers archival scan, part 2:  
    https://archive.computerhistory.org/resources/access/text/2021/04/102785423-05-02-acc.pdf

31. Computer History Museum, Bemer published-papers archival scan, part 3:  
    https://archive.computerhistory.org/resources/access/text/2021/04/102785423-05-03-acc.pdf

32. NBS, *Computer Literature Bibliography, 1946–1963*:  
    https://nvlpubs.nist.gov/nistpubs/Legacy/MP/nbsmiscellaneouspub266.pdf

## Participant recollections and later technical compilations

33. Preserved collection of Bob Bemer’s ASCII-history pages and autobiographical material:  
    https://www.histo.cat/sabies/bob-bemer

34. Archived “Hugh McGregor Ross on Character Sets”:  
    https://archive.ph/nt5S

35. John Walker, “UNIVAC 1100 Series FIELDATA Character Code,” compiled 6 August 1996 from UNIVAC manuals:  
    https://www.fourmilab.ch/documents/univac/fieldata.html

36. John Walker, UNIVAC 1100/2200 instruction-set archive:  
    https://www.fourmilab.ch/documents/univac/instructions.html

37. Eric S. Raymond/J. Jennings-style annotated reconstruction, “An Annotated History of Some Character Codes”:  
    https://www.sr-ix.com/Archive/CharCodeHist/index.html

38. Wikimedia Commons modern comparative FIELDATA chart, with source notes:  
    https://commons.wikimedia.org/wiki/File:Fieldata.svg

## Modern survival and data recovery

39. Unisys, *ClearPath OS 2200 Glossary*, documenting 6-, 9-, and 18-bit character sizes:  
    https://www.support.unisys.com/2200/docs/CP20.0/PDFs/00_GLOSS.PDF

40. U.S. Census Bureau Center for Economic Studies, legacy Unisys tape reconstruction using FIELDATA and excess-three hypotheses:  
    https://www2.census.gov/ces/wp/2014/CES-WP-14-37.pdf

41. IANA Character Set Registrations:  
    https://www.iana.org/assignments/charset-reg

42. Bitsavers UNIVAC manual archive:  
    https://www.bitsavers.org/pdf/univac/

43. Bitsavers CDC 1604 archive:  
    https://www.bitsavers.org/pdf/cdc/1604/

44. Bitsavers DEC standards archive:  
    https://bitsavers.org/pdf/dec/standards/
