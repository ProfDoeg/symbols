# Code pages: 437, 850, 1252 and the vendor eight-bit sets (IBM, Microsoft, Apple, DEC): Research Dossier

## Basic identification

| Encoding | Standard/vendor designation | First documented appearance | Width and size | Repertoire | Present status |
|---|---|---:|---:|---|---|
| IBM PC character set, later **code page 437** | IBM CP/CCSID 437; IANA `IBM437`, aliases `cp437`, `csPC8CodePage437` | IBM Personal Computer Technical Reference, August 1981; the number “437” was applied later in IBM’s code-page system | Fixed 8-bit; 256 byte values | ASCII graphic repertoire; Western-European letters; Greek/math symbols; currency signs; card suits and other pictographs; extensive box and block drawing | Legacy/OEM code page; still registered, emulated, and used for DOS software, console graphics, ANSI art, archives, and some ZIP metadata |
| **Code page 850** | IBM CP/CCSID 850; IANA `IBM850`, aliases `cp850`, `csPC850Multilingual` | Developed for IBM/MS-DOS international support; exposed to ordinary users with DOS 3.3, 1987 | Fixed 8-bit; 256 byte values | ASCII plus a rearranged, nearly complete Western-European Latin-1 repertoire; fewer CP437 Greek, mathematical, and mixed-line drawing characters | Legacy DOS/OEM Western-European code page; preserved in converters and compatibility APIs |
| **Windows-1252** | Microsoft code page 1252; IANA `windows-1252`, MIBenum 2252 | Antecedent in Windows 1.0, 1985; expanded in Windows 2.0 and 3.1; euro revision shipped in the Windows 98 era | Fixed 8-bit; 251 assigned characters in the canonical mapping, five undefined bytes | ASCII, ISO-8859-1 graphics, typographic quotation marks, dashes, ligatures, trademark, euro, and several Central-European letters | Legacy Windows “ANSI” code page; still required by the web’s compatibility encoding model, but Unicode/UTF-8 is preferred |
| **Macintosh Roman / Mac OS Roman** | Apple Standard Roman; IANA `macintosh`; Microsoft CP 10000 | Original Macintosh, 1984; expanded Standard Roman documented by 1991–93; euro revision in 1998 | Fixed 8-bit; 256 values, although the earliest Macintosh set left part of the upper range unused | ASCII plus Western-European letters, typography, math, ligatures, and Apple-specific symbols including the Apple logo | Legacy classic-Mac encoding; still convertible on Apple and other platforms |
| **DEC Multinational Character Set** | DEC MCS/DEC-MCS; IANA `DEC-MCS`; IBM CCSID 1100 in later registries | VT220, 1983 | 8-bit code environment: C0, ASCII GL, C1, DEC Supplemental Graphics GR | Western-European Latin letters and signs; terminal-oriented C1 controls | Obsolete as an interchange default, but historically important in the path to ECMA-94 and ISO 8859-1 |
| **PETSCII** | Commodore proprietary set, also “CBM ASCII” | Commodore PET 2001, 1977 | 8-bit codes plus display modes and control state | Latin letters, extensive block/line graphics, keyboard symbols, cursor/color controls; model-dependent glyphs | Retrocomputing and text-art format |
| **ATASCII** | Atari proprietary “ATARI ASCII” | Atari 400/800 generation, 1979 | 8-bit, with inverse-video bit conventions and device controls | ASCII-related text, Atari graphics, cursor/editing controls | Retrocomputing and art preservation |
| **Amstrad CPC character set** | Amstrad/Locomotive proprietary firmware repertoire | CPC464, 1984 | 8-bit; ASCII printable core, controls, symbols, and redefinable glyphs | Latin text, CPC graphics, mathematical and miscellaneous signs | Platform-specific legacy repertoire |
| **Atari ST character set** | Atari/TOS vendor set | 1985 | Fixed 8-bit glyph repertoire | ASCII core; CP437-derived international and symbol area, but substantial substitutions including Hebrew | Legacy Atari ST data and ROM-font convention |

**Evidence labels used below**

- **[D—standard/text]**: directly stated in a standard, vendor manual, mapping table, registry, specification, or dated contemporary document.
- **[P—participant recollection]**: retrospective account by somebody involved.
- **[S—scholarly reconstruction]**: historical synthesis from documents or preserved implementations.
- **[Disputed]**: competing accounts or a claim contradicted by surviving evidence.
- **[Folklore]**: widely repeated without adequate period documentation.
- **[Modern reconstruction/invention]**: later mapping, name, convention, or aesthetic framework imposed on older bytes or glyphs.

The important preliminary point is that these are not one standard called “extended ASCII.” **[D/S]** They are mutually incompatible 8-bit codes sharing, to varying degrees, the 7-bit ASCII graphic block. “Extended ASCII” is a loose category, not an unambiguous charset name.

---

## The code in detail

### 1. Common architecture

CP437, CP850, Windows-1252, and Mac Roman are single-byte encodings: one byte selects one code position. No byte carries a continuation-bit count, and there is no intrinsic shift state.

For the IBM and Microsoft pages:

- `00–1F`: conventionally ASCII C0 controls in byte-stream APIs.
- `20–7E`: ASCII graphic characters.
- `7F`: ASCII DEL semantically, although IBM PC display hardware supplied a visible glyph at that cell.
- `80–FF`: vendor-specific extension.

The ambiguity between **code**, **control interpretation**, and **font glyph** is fundamental. In IBM PC video memory, every 8-bit cell value selected a glyph. In DOS character-output services, bytes such as `07`, `08`, `0A`, and `0D` could instead mean bell, backspace, line feed, and carriage return. Thus byte `01` could select a smiling-face bitmap if written directly to video RAM while remaining SOH, or being rejected/treated specially, in another interface. **[D—IBM hardware/manuals; S—comparison of display and stream APIs]**

### 2. ASCII-compatible lower half

The shared printable area is:

```text
20  SPACE  ! " # $ % & ' ( ) * + , - . /
30  0 1 2 3 4 5 6 7 8 9 : ; < = > ?
40  @ A B C D E F G H I J K L M N O
50  P Q R S T U V W X Y Z [ \ ] ^ _
60  ` a b c d e f g h i j k l m n o
70  p q r s t u v w x y z { | } ~ DEL
```

The control block inherited from ASCII is structurally:

```text
00 NUL  01 SOH  02 STX  03 ETX  04 EOT  05 ENQ  06 ACK  07 BEL
08 BS   09 HT   0A LF   0B VT   0C FF   0D CR   0E SO   0F SI
10 DLE  11 DC1  12 DC2  13 DC3  14 DC4  15 NAK  16 SYN  17 ETB
18 CAN  19 EM   1A SUB  1B ESC  1C FS   1D GS   1E RS   1F US
7F DEL
```

**Newline.** The code pages themselves do not define one universal file-newline rule. DOS and Windows text files conventionally use `0D 0A` (CR LF). Classic Mac OS conventionally used `0D` alone. Unix used `0A`. MIME later specified CRLF for canonical line breaks in `text/*`. **[D—platform and RFC 2046 rules]**

**Space.** Ordinary space is `20`. Windows-1252, Mac Roman, and DEC MCS also provide a nonbreaking space in their upper halves. CP437 does not have a semantically encoded no-break space, although mappings and display conventions sometimes treat `FF` or another visible blank as such; that is not interchangeable with a standardized NBSP. **[D/S]**

**Deletion.** ASCII `7F` is DEL. CP437’s ROM font famously displays a small-house/delta-like glyph at cell `7F`, but stream semantics can still be DEL. The exact historical glyph identification is contested below.

**Case.** All four principal pages encode upper- and lowercase Latin letters separately. Bytewise case conversion is not generally a fixed bit operation outside ASCII: accented pairs occupy unrelated positions. Case-insensitive comparison therefore requires a page-specific table. These pages cannot express modern Unicode notions such as context-sensitive Greek sigma, multi-character German `ß` uppercasing, or locale-sensitive Turkish dotted/dotless-I behavior without external rules.

### 3. CP437 upper half

The canonical Unicode reading of bytes `80–FF`, arranged by hexadecimal row, is:

```text
80 Ç ü é â ä à å ç ê ë è ï î ì Ä Å
90 É æ Æ ô ö ò û ù ÿ Ö Ü ¢ £ ¥ ₧ ƒ
A0 á í ó ú ñ Ñ ª º ¿ ⌐ ¬ ½ ¼ ¡ « »
B0 ░ ▒ ▓ │ ┤ ╡ ╢ ╖ ╕ ╣ ║ ╗ ╝ ╜ ╛ ┐
C0 └ ┴ ┬ ├ ─ ┼ ╞ ╟ ╚ ╔ ╩ ╦ ╠ ═ ╬ ╧
D0 ╨ ╤ ╥ ╙ ╘ ╒ ╓ ╫ ╪ ┘ ┌ █ ▄ ▌ ▐ ▀
E0 α ß Γ π Σ σ µ τ Φ Θ Ω δ ∞ φ ε ∩
F0 ≡ ± ≥ ≤ ⌠ ⌡ ÷ ≈ ° ∙ · √ ⁿ ² ■ NBSP*
```

`FF` deserves an asterisk: Unicode’s Microsoft/IBM mapping practice commonly maps it to U+00A0, but the original PC display cell is simply a blank-looking glyph. Assigning semantic NBSP to historical screen memory is partly a later interoperability decision. **[Modern reconstruction]**

At `00–1F` and `7F`, the IBM ROM provided:

```text
00 blank   01 ☺  02 ☻  03 ♥  04 ♦  05 ♣  06 ♠  07 •
08 ◘       09 ○  0A ◙  0B ♂  0C ♀  0D ♪  0E ♫  0F ☼
10 ►       11 ◄  12 ↕  13 ‼  14 ¶  15 §  16 ▬  17 ↨
18 ↑       19 ↓  1A →  1B ←  1C ∟  1D ↔  1E ▲  1F ▼
7F ⌂
```

That is a **display-glyph table**, not a declaration that byte `0A` ceased to mean LF in DOS streams.

#### Design logic

- `80–AF`: Western-European letters and signs.
- `B0–DF`: shading, blocks, and single, double, and mixed box junctions.
- `E0–FF`: selected Greek letters, mathematical signs, superscripts, and a solid square.
- The box block is arranged for contiguous line construction. IBM MDA’s nine-dot cells duplicated the eighth bitmap column for a designated range, preventing gaps in horizontal strokes. **[D—adapter behavior; S—relation to table arrangement]**
- Greek letters were selected chiefly for mathematics and science, not to encode ordinary Greek prose. The page lacks most Greek capitals and accents. **[S, strongly supported by repertoire]**

#### What CP437 cannot express

It cannot directly encode most Central/Eastern-European Latin orthographies, complete Greek, Cyrillic, Hebrew, Arabic, any Indic script, CJK text, combining marks, modern currency signs such as the euro, or emoji. Even Western-European coverage is incomplete. Its 256 cells are exhausted, and some are better understood as controls or presentation glyphs than abstract text characters.

### 4. CP850 upper half

CP850 retained ASCII and many CP437 cells, but traded Greek/math and mixed box drawing for Western-European letters:

```text
80 Ç ü é â ä à å ç ê ë è ï î ì Ä Å
90 É æ Æ ô ö ò û ù ÿ Ö Ü ø £ Ø × ƒ
A0 á í ó ú ñ Ñ ª º ¿ ® ¬ ½ ¼ ¡ « »
B0 ░ ▒ ▓ │ ┤ Á Â À © ╣ ║ ╗ ╝ ¢ ¥ ┐
C0 └ ┴ ┬ ├ ─ ┼ ã Ã ╚ ╔ ╩ ╦ ╠ ═ ╬ ¤
D0 ð Ð Ê Ë È ı Í Î Ï ┘ ┌ █ ▄ ¦ Ì ▀
E0 Ó ß Ô Ò õ Õ µ þ Þ Ú Û Ù ý Ý ¯ ´
F0 ≡ ± ‗ ¾ ¶ § ÷ ¸ ° ¨ · ¹ ³ ² ■ NBSP
```

**[D—IBM tables and Unicode vendor mappings]**

Its repertoire was chosen so DOS applications in Western Europe could encode substantially more national text while preserving enough line drawing for menus and forms. Programs that assumed the exact CP437 mixed-line junctions could nevertheless display letters in place of borders under CP850. **[D/S]**

CP850 is often described as “Latin-1 reordered.” That is useful but needs qualification:

- It contains the ISO-8859-1 graphic repertoire in `A0–FF`, apart from representational and historical edge cases, but at different byte positions.
- It keeps CP437 compatibility where IBM judged it valuable.
- It is not byte-compatible with ISO-8859-1 above ASCII.
- `D5` was originally dotless `ı`. CP858 later replaces that cell with `€`.

### 5. Windows-1252

Windows-1252 agrees with ISO-8859-1 at `00–7F` and `A0–FF`. Its defining divergence is its use of much of `80–9F`, which ISO 8859 reserves for C1 controls:

```text
80 €    81 undefined  82 ‚    83 ƒ
84 „    85 …          86 †    87 ‡
88 ˆ    89 ‰          8A Š    8B ‹
8C Œ    8D undefined  8E Ž    8F undefined

90 undefined  91 ‘    92 ’    93 “
94 ”          95 •    96 –    97 —
98 ˜          99 ™    9A š    9B ›
9C œ          9D undefined  9E ž  9F Ÿ
```

The `A0–FF` block is:

```text
A0 NBSP ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ SHY ® ¯
B0 ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿
C0 À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï
D0 Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß
E0 à á â ã ä å æ ç è é ê ë ì í î ï
F0 ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ
```

**[D—Microsoft/Unicode mapping]**

The five undefined bytes are `81`, `8D`, `8F`, `90`, and `9D`. Some software maps them to corresponding C1 controls for round-trip convenience; that behavior is not the canonical Windows-1252 character assignment. **[D/S]**

#### Why “ANSI” is misleading

Microsoft documentation says Windows-1252 was based on an ANSI draft that fed into ISO 8859-1, but it is not itself an ANSI standard. “ANSI code page” became Windows terminology for the locale-selected native Windows page, in contrast with the DOS/OEM page. **[D—Microsoft documentation; P—Raymond Chen’s later explanation]**

On a Western Windows installation the characteristic split was:

```text
OEM side:       CP437 in the United States, often CP850 in Western Europe
Windows side:   CP1252
Unicode side:   UTF-16 in Windows NT's native “W” APIs
```

The Win32 `A` APIs convert through the active Windows code page; `W` APIs take Unicode strings. Console and filesystem compatibility added further conversions, which is why “ANSI,” “OEM,” “console,” and “file” encoding were never safely interchangeable.

#### Euro chronology

Microsoft announced broad euro support on 29 April 1998 and assigned `€` to `80` in several Windows pages. Windows 98-era CP1252 also gained `Ž`, `ž`, and `€`. A 2003 Unicode mailing-list exchange contains an obvious participant typo claiming “May 1988”; the euro did not yet exist under that name or symbol then. The period Microsoft announcement and 1998 W3C correspondence support **1998**, not 1988. **[D; erroneous P recollection identified]**

### 6. Mac Roman

Mac Roman preserves ASCII at `00–7F` and uses `80–FF` for a differently optimized mixture of letters and desktop-publishing typography. Its upper-half structure includes:

- `80–9F`: common accented capitals/lowercase letters.
- `A0–BF`: punctuation, currency signs, mathematical signs, `†`, `°`, `¢`, `£`, `§`, `•`, `¶`, `ß`, `®`, `©`, `™`, acute/diaeresis and related marks.
- `C0–DF`: punctuation, quotation marks, ligatures `Æ/æ`, `Œ/œ`, mathematical operators, no-break space, and additional accented letters.
- `E0–FF`: typographic dashes and quotes, division, lozenge, ligatures `ﬁ/ﬂ`, punctuation, additional Latin letters, and Apple-specific/reserved positions.

The Apple vendor mapping maps Mac byte `F0` to U+F8FF, a Unicode Private Use Area value customarily rendered as the Apple logo by Apple fonts. Unicode has not standardized the corporate logo as a universal character. **[D—Apple mapping; Modern reconstruction for the PUA bridge]**

Apple’s 1993 *Inside Macintosh: Text* says Standard Roman uses `00–FF`, is built into every Macintosh, and extends the original Macintosh set by filling positions `D9–FF` that had been empty. It also warns that not every bitmap font supplied every glyph. **[D]**

In 1998 Apple’s euro update replaced the generic currency sign in the relevant Mac encodings. Therefore “Mac Roman” can identify slightly different historical revisions unless the system version is specified. **[D/S]**

### 7. DEC MCS and ISO-style 8-bit structure

The VT220 programmer documentation presents an explicitly structured 8-bit environment:

```text
00–1F  C0 controls
20–7F  ASCII graphic area GL, with DEL at 7F
80–9F  C1 controls
A0–FF  DEC Supplemental Graphic Set in GR
```

At power-up/reset the VT220 mapped DEC MCS into the full 8-bit matrix. It could also designate graphic sets into G0–G3 and invoke them through locking shifts or single shifts. In a seven-bit connection, C1 functions could be represented through escape sequences. **[D—VT220 Programmer Reference Manual]**

This differs sharply from CP437/850/1252:

- DEC’s set belongs to the ISO 2022/ECMA-35 model of designated and invoked sets.
- CP437 and CP850 normally treat each byte directly in the current page.
- Windows-1252 deliberately assigns printable characters where an ISO-style environment would place C1 controls.

DEC MCS is widely described as an ancestor of ECMA-94/ISO-8859-1. The strongest precise formulation is that ECMA and ANSI/X3L2 were exchanging industry proposals from 1982 onward, and that DEC’s already-deployed repertoire was an important industrial precursor. ECMA’s own historical introduction credits the joint ANSI/ECMA work, not DEC alone. **[D/S]**

### 8. Error detection and synchronization

For fixed single-byte pages:

- Every byte is independently aligned; a reader starting at an arbitrary byte is automatically on a character boundary.
- A deleted or inserted byte corrupts only that byte’s character alignment in a byte stream; subsequent bytes remain byte-aligned.
- There is no checksum, validity pattern, or reliable in-band charset identifier.
- Almost every byte is plausible. Consequently, reading the wrong page produces convincing but false text rather than a detectable error.
- CP1252’s five undefined byte values provide only weak diagnostics.
- ESC-based terminal languages and PETSCII-like state changes are different: losing an ESC, quote-mode, reverse-video, case-set, or color-state control can affect an indefinite following span until another command or reset restores state.
- No byte-order mark is meaningful for these one-byte encodings.

This is almost the inverse of UTF-8’s tradeoff: UTF-8 has variable-width characters but recognizable lead/continuation structure and rejects many byte strings; the old single-byte pages are immediately synchronized but semantically underdetermined.

### 9. Collation

Raw unsigned-byte order places:

```text
controls < SPACE/punctuation < digits < uppercase ASCII < lowercase ASCII < upper-half characters
```

That is not linguistically acceptable collation. For example, CP437 byte order places `é` at `82`, far after ASCII `z`; accented variants are not grouped with their bases. IBM database products therefore publish page- and territory-specific collation tables distinct from byte order. Windows similarly uses locale-aware sorting APIs. **[D]**

### 10. Worked examples

#### “Café — €5”

This example deliberately exposes repertoire differences.

**Windows-1252**

```text
C    a    f    é    SPACE  —    SPACE  €    5
43   61   66   E9   20     97   20     80   35
```

**UTF-8**

```text
C    a    f    é       SPACE  —          SPACE  €          5
43   61   66   C3 A9   20     E2 80 94   20     E2 82 AC   35
```

**CP850**

```text
C    a    f    é    SPACE
43   61   66   82   20
```

CP850 cannot encode the em dash or euro. A lossy DOS-era approximation would be:

```text
"Cafe - EUR 5" or "Café - 5"
43 61 66 82 20 2D 20 45 55 52 20 35
```

CP858 can encode the euro as `D5`, but still lacks the em dash:

```text
"Café - €5"
43 61 66 82 20 2D 20 D5 35
```

**CP437** also represents `é` as `82` but has neither `—` nor `€`.

#### “Über £5”

```text
                  Ü    b    e    r   SP   £    5
CP437             9A   62   65   72  20   9C   35
CP850             9A   62   65   72  20   9C   35
Windows-1252      DC   62   65   72  20   A3   35
UTF-8             C3 9C 62   65   72  20   C2 A3 35
```

The same visible string therefore has incompatible upper bytes even among Western pages.

#### CP437 box

A double-line box containing `OK`:

```text
╔══╗
║OK║
╚══╝
```

Bytes, with DOS CRLF:

```text
C9 CD CD BB 0D 0A
BA 4F 4B BA 0D 0A
C8 CD CD BC 0D 0A
```

If those bytes are decoded as CP1252, they become approximately:

```text
ÉÍÍ»
ºOKº
ÈÍÍ¼
```

That failure is not random corruption; it is a deterministic page mismatch.

#### Canonical mojibake

Windows-1252 apostrophe:

```text
Intended character: ’
CP1252 byte:        92
Latin-1 reading:    U+0092, a C1 control—often blank or a control box
```

UTF-8 apostrophe read as Windows-1252:

```text
’ in UTF-8:         E2 80 99
decoded as CP1252:  â € ™
displayed together: â€™
```

UTF-8 `é` read as CP1252:

```text
é in UTF-8:         C3 A9
CP1252 reading:     Ã ©
displayed:          Ã©
```

The often-seen `â€™` is therefore not “1252 read as Latin-1.” It is UTF-8 bytes read as Windows-1252. By contrast, a CP1252 smart quote read under strict Latin-1 becomes a C1 control.

---

## Origins

### 1. Before the vendor pages

The vendor pages inherit a longer history of fixed-position telegraph and data-processing codes:

- **Émile Baudot**, in the 1870s, developed a five-unit telegraph code with shift states.
- **Donald Murray** redesigned the Baudot scheme for keyboard/perforator and teleprinter use around the turn of the twentieth century; the international telegraph alphabets descended more directly from Murray’s organization than from Baudot’s original allocation.
- **Herman Hollerith’s** punched-card systems used position patterns rather than a single linear byte code but established machine-readable commercial data and durable vendor-coded repertoires.
- CCITT International Telegraph Alphabet No. 2 used five bits plus letters/figures shifts. A corrupted or missing shift could misinterpret an entire following run—one problem avoided by self-contained ASCII letters.
- Six-bit codes such as FIELDATA and vendor-specific BCD repertoires supported capitals, digits, and limited punctuation.
- ASA X3.4-1963 standardized the first ASCII; later revisions altered several positions and completed lowercase/control choices. ASCII-1968 became the durable core. RFC 20 reproduced USAS X3.4-1968 for ARPANET interchange in 1969. **[D]**

Bob Bemer is properly described as a forceful participant and advocate in ASCII’s development, not its sole inventor. Charles Mackenzie’s 1980 history reconstructs the committee work and multiple competing proposals. Claims that “Bemer invented ASCII” are later journalistic simplifications. **[S/Disputed]**

### 2. The move from seven to eight bits

Seven-bit ASCII supplied 128 positions, of which 33 were controls including DEL. It could comfortably encode modern English but not even all Western-European orthographies. National versions of ISO 646 replaced punctuation positions with local letters or signs, making programming text nonportable. ISO 2022 and ECMA-35 created escape/designation mechanisms for switching among sets.

By the late 1970s and early 1980s, eight-bit hardware made another 128 positions inexpensive. There was no single victor:

- Terminal vendors used ISO-2022-like C1/GR structures.
- Microcomputer vendors filled all positions with useful local glyphs.
- IBM assigned multiple code pages by country or script.
- Apple associated character sets with Macintosh script systems.
- Microsoft separated DOS/OEM and Windows “ANSI” families.
- East Asian systems used stateful or multibyte encodings because 256 positions were radically insufficient.

Calling this an “eight-bit war” is a useful retrospective phrase, but there was no single formal contest with one ballot and one winner. **[S]**

### 3. CP437, 1981

The original IBM PC Technical Reference documents the 256 display character codes in the 1981 machine. The name “code page 437” is retrospective: early IBM PC documentation described character codes and ROM fonts, not necessarily a field-selectable page numbered 437. IBM later registered the repertoire and names in its corporate character-data architecture. **[D/S]**

The design had several simultaneously useful purposes:

- ASCII-compatible programming and ordinary English text.
- Western-European names and words.
- scientific/mathematical notation;
- card suits, faces, arrows, gender signs, music signs, and other compact pictographs;
- lines, corners, junctions, blocks, and shades for forms and screen interfaces.

This was unusually well matched to character-cell video. The page became both a text encoding and a low-resolution graphics palette.

#### Who selected it?

A retrospective interview with IBM BIOS engineer **David J. Bradley** says Bradley, display-adapter engineer **Andy Saenz**, and PC chief engineer **Lew Eggebrecht** selected the characters in a roughly four-hour airplane meeting from Seattle to Atlanta. **[P—single retrospective account]**

Bill Gates told *Fortune* in 1995 that Microsoft was fascinated by Wang word processors and put a “funny Wang character set” with faces, boxes, and triangles into the IBM PC because it might later clone Wang-style word processing. **[P]**

These accounts do not fit neatly:

- Gates says “we,” although IBM controlled the PC hardware specification.
- Surviving WISCII tables reportedly do not contain all the smileys and box characters named in his story.
- Bradley names an IBM trio and a specific meeting.
- Neither recollection is a surviving 1981 design memo.

The safest finding is: IBM’s PC team specified the shipped repertoire; Bradley gives the only detailed selection story located here; Gates offers evidence of Wang influence or Microsoft interest, but his character-level description is partly contradicted. **[Disputed; absence of corroborating period memo is a finding]**

### 4. The `7F` house/delta dispute

Modern Unicode mappings call CP437 `7F` U+2302 HOUSE. Later IBM registries used a “small house” identity. Yet some period IBM-compatible references and fonts appear delta-like and label it delta. **[D/S]**

A modern glyph-historical investigation argues that “small house” was applied when IBM retrospectively registered the unnamed ROM repertoire around 1984, while later machines still printed or labeled a delta. That is persuasive evidence that abstract-character identity was unstable. It is not proof of the original 1981 designer’s intention. **[Modern reconstruction; original intention open]**

### 5. CP850 and DOS internationalization

The original PC page was not sufficient for Western-European business text. IBM developed PC multilingual pages, including CP850, with a broader Latin repertoire. MS-DOS/PC DOS 3.3 documentation in 1987 introduced user-visible code-page preparation and switching through:

```text
DISPLAY.SYS
PRINTER.SYS
MODE ... CODEPAGE PREPARE
MODE ... CODEPAGE SELECT
CHCP
COUNTRY.SYS
```

The manual’s worked example loads multilingual page 850 for an EGA display and printer. **[D]**

This made “code page” an ordinary DOS-administration concept rather than merely an IBM registry term. Hardware fonts complicated matters: EGA/VGA could load fonts, while printers needed matching resident/downloaded pages. A screen on CP850 and a printer on CP437 could turn accented letters into lines or vice versa.

CP850 preserved single and double boxes but removed many mixed-weight junctions. That compromise documents the competing priorities: international prose versus exact compatibility with existing text-mode interfaces. No located source records a named individual designer or a dramatic committee confrontation over each replaced cell. **[Absence of evidence]**

### 6. DEC MCS, ECMA-94, and ISO 8859

DEC shipped its MCS with the VT220 in 1983. ECMA’s history says:

- the need for standardized 8-bit graphic sets was considered urgent in 1982;
- ECMA TC1 and ANSI X3L2 exchanged working papers;
- ECMA submitted a proposal to ISO/TC97/SC2 in February 1984;
- after discussion, ECMA adopted the X3L2 coding scheme;
- ECMA-94 first edition appeared in March 1985;
- ISO 8859-1 arose from the joint ANSI/ECMA proposal.

**[D—ECMA]**

Thus “ISO Latin-1 came from DEC MCS” is directionally useful but too simple. DEC was an important deployed predecessor; formal allocation emerged from ANSI/ECMA/ISO work involving multiple industry sources. **[S]**

### 7. Windows-1252

Microsoft’s own documentation says CP1252 originated from an ANSI draft leading toward ISO 8859-1 and was implemented before the final standard. **[D]**

The reconstructable sequence is:

- **Windows 1.0, 1985:** early Windows Latin repertoire close to the then-draft Latin-1 layout.
- **Windows 2.0, 1987:** additions included typographic quotation marks and completed arithmetic signs.
- **Windows 3.1, 1992:** the now-familiar punctuation-rich `80–9F` area was substantially populated.
- **1998:** euro and Z-with-caron pair added in the final common mapping.

The precise version-by-version table is well repeated in secondary sources, but Microsoft’s current documentation does not provide a complete signed revision ledger. Contemporary SDK tables would be the strongest evidence for every transition. **[S; documentary gap]**

### 8. Macintosh Roman

The Macintosh’s 1984 character set accompanied its graphics-first typography system. Apple’s later documentation describes the original set and its expansion to Standard Roman. The repertoire gives priority to:

- accented Western-European text;
- curly quotation marks and publishing punctuation;
- mathematical and commercial symbols;
- ligatures;
- glyphs associated with Macintosh UI and branding.

Susan Kare designed influential Macintosh bitmap fonts and icons, but no located primary source establishes that she alone designed the Mac Roman code allocation. Conflating font drawing with repertoire assignment is an unsupported modern shortcut. **[Disputed/absence of evidence]**

### 9. PETSCII, ATASCII, Amstrad, and Atari ST

**PETSCII.** Commodore’s PET used an ASCII-related but incompatible repertoire from 1977. It joined letters with line/block graphics and machine-control codes. Later Commodore machines supported two display character sets: an uppercase/graphics mode and a lowercase/uppercase mode. Control codes could change case set, colors, reverse video, or cursor state. The popular expansion “PET Standard Code of Information Interchange” appears widely, but “PETSCII” itself is better treated as a vendor/community name than an external standard. **[D/S]**

**ATASCII.** Atari’s 8-bit family rearranged controls and graphics around an ASCII-related core. The high bit could select inverse video, while ANTIC-era systems could redirect character-set memory, turning text cells into programmable fonts or game tiles. **[D]**

**Amstrad CPC.** The CPC firmware documented ASCII controls and graphics but provided its own full display repertoire and facilities for redefining character matrices. Codes `80–9F` also interacted with expansion-string facilities in firmware/BASIC contexts. Its CP/M Plus character set was not identical to the native BASIC/firmware set. **[D]**

**Atari ST.** The ST ROM font is plainly CP437-influenced but replaces much of `B0–DF`, including box characters, with Hebrew and other signs. All 256 positions could have display glyphs even where APIs retained control meanings. Calling it an official numbered IBM page would be wrong. **[D/S]**

---

## Adoption and decline

### 1. IBM PC and compatibles

CP437 shipped with the IBM PC’s display adapters and was reproduced by compatible hardware. It became the default visual vocabulary of:

- BIOS and boot-time screens;
- PC DOS/MS-DOS applications;
- Norton-style file managers and text-mode IDEs;
- forms, spreadsheets, database front ends, installation programs, and games;
- BIOS setup utilities;
- terminal and BBS clients;
- direct video-memory interfaces.

The PC’s success turned the page into a de facto hardware platform convention. It was never a universal extension of ASCII.

### 2. National DOS pages

DOS 3.3’s code-page infrastructure let selected displays and printers prepare and activate pages. IBM DOS 4.0 documentation lists, among others:

- 437 and 850 for many Western locales;
- 860 Portuguese;
- 862 Hebrew;
- 863 Canadian French;
- 864 Arabic;
- 865 Nordic;
- 932 Japanese;
- 934 Korean;
- 936 Simplified Chinese;
- 938 Traditional Chinese.

**[D]**

The table also reveals the model’s limits: SBCS pages worked for one modest repertoire at a time; CJK required multibyte hardware/software variants. Switching a page could repair national text while breaking software whose interface used page-specific boxes.

### 3. OEM versus Windows

Windows maintained compatibility with DOS applications and hardware through OEM pages while giving graphical Windows applications another locale-selected page. In Western installations this often meant CP437/850 versus CP1252.

Consequences included:

- copied console text differing from GUI text;
- archive and filename APIs interpreting bytes differently;
- printers or serial devices requiring explicit conversion;
- programs assuming “one byte equals one character” while using different one-byte tables;
- “ANSI” API names surviving after Windows NT became internally Unicode.

Windows NT used Unicode internally from its first release, but compatibility and developer practice kept `A` APIs and code-page conversion alive. Modern Microsoft guidance recommends Unicode, including UTF-8 or UTF-16, instead of specific pages. **[D]**

### 4. Internet mail and protocols

RFC 20 mandated seven-bit ASCII in an eight-bit byte with the high bit zero for early ARPANET host interchange. Vendor 8-bit pages were not interoperable merely because the network could carry octets. **[D]**

MIME’s 1992–96 standards created explicit `charset` labeling and transfer encodings. RFC 2046:

- defaulted `text/plain` to US-ASCII if no charset was supplied;
- required a declared charset for 8-bit and multioctet sets;
- defined CRLF as canonical text line break;
- warned that ISO 646 national variants were not necessarily US-ASCII;
- identified ISO-8859 pages, not arbitrary vendor pages, as the initially standardized 8-bit family.

RFC 1345 registered names and mnemonic tables for a large historical collection, including IBM and Macintosh sets. **[D]**

RFC 2277, January 1998, required new IETF protocols dealing with text to support UTF-8; other registered charsets could remain where legacy data required them. **[D]**

### 5. The web

Early web content frequently omitted or misstated its encoding. CP1252 punctuation was especially common in Windows-authored HTML, even when servers declared ISO-8859-1. Browser compatibility practice eventually treated labels including `iso-8859-1`, `latin1`, and even several nominal ASCII labels as Windows-1252 in HTML. WHATWG’s Encoding Standard codifies that behavior. **[D]**

This is not a claim that ISO-8859-1 and CP1252 are identical. It is a browser decoding rule designed to match deployed content.

W3C reported:

- roughly 80% Unicode/ASCII-compatible use in Google’s 2012 sample;
- W3Techs at 86% UTF-8 in January 2016;
- 96.1% in January 2021;
- 97.9% in January 2023.

W3Techs reported 99.1% of sites with a known encoding in September 2026. Survey methodology and the denominator “sites whose encoding is known” matter. **[D—survey reports, not a census]**

### 6. ZIP filenames

PKWARE’s APPNOTE records that ZIP historically expected the original IBM PC encoding, CP437, for names and comments when no Unicode marker was present. Later specifications assign general-purpose bit 11 to UTF-8 names/comments and say UTF-8 ZIP metadata should not include a BOM. Info-ZIP also developed Unicode path/comment extra fields. **[D]**

Persistence problems arise because:

- many old writers actually used the local OEM, ANSI, Mac, or Unix locale rather than strict CP437;
- old ZIP records contain no trustworthy charset tag;
- modern extractors must choose between specification, platform heuristics, and user expectations;
- the wrong guess can alter filenames, sometimes producing security-relevant path discrepancies.

### 7. Databases and business data

Single-byte pages persist in:

- fixed-width mainframe/PC interchange;
- old DB2, dBASE, Access, FoxPro, and ERP records;
- SQL client/server conversions;
- import/export files;
- printer streams;
- device protocols;
- columns declared with a legacy collation.

The dangerous case is not an honestly tagged CP1252 column. It is a byte column successively decoded and re-encoded under different assumptions. Such data can accumulate multiple layers of mojibake that are not uniquely reversible.

### 8. What survives

- CP437 glyphs in terminal fonts, roguelikes, boot consoles, DOSBox, PC emulators, and Unicode box-drawing/block characters.
- CP850 in legacy European DOS files and converters.
- CP1252 in Windows APIs, old documents, databases, browsers’ mandatory legacy decoders, and mislabeled web data.
- Mac Roman in classic-Mac files, resource forks, HFS metadata, and conversion libraries.
- DEC MCS in terminal emulators and VMS/DEC data.
- OEM/ANSI terminology in Win32 API names and user interfaces.
- decimal Alt-code folklore, with Windows preserving distinctions between OEM-style entries and leading-zero Windows-page entries.
- `0D 0A` as Windows line ending.
- CP437 in ZIP’s historical default.
- graphical control-cell glyphs in retro fonts and iconography.

---

## The other scripts

### Cyrillic

CP437’s Greek-looking symbols cannot encode Cyrillic. DOS used pages such as 855 and 866; Windows used 1251; Macintosh had Mac Cyrillic; KOI8-R became important on Russian Unix and the Internet.

The famous “KOI8 trick” is documented as a repertoire arrangement whereby clearing the high bit of many Cyrillic bytes yields a readable Latin transliteration-like approximation. It is best understood as deliberate robustness in KOI-family design, not a property of CP437/850/1252. Claims that a single named person invented the trick require a specific source; none was established in this research. **[D for layout; open credit question]**

### Greek

CP437 includes `α Γ π Σ σ µ τ Φ Θ Ω δ φ ε` and related symbols, but not a complete prose alphabet. IBM/DOS pages 737 and 869, Windows-1253, Mac Greek, and ISO-8859-7 supplied fuller national repertoires. Mixing Greek and German under SBCS Windows still required a page change or higher-level encoding.

### Hebrew

Hebrew needs letters plus bidirectional layout. DOS page 862, Windows-1255, Mac Hebrew, ISO-8859-8, and DEC Hebrew variants encoded relevant characters, but character encoding alone did not settle ordering.

RFC 2046 explicitly noted that ISO-8859-6 and -8 mixed left-to-right Latin with right-to-left Arabic/Hebrew but did not define one canonical bidirectional storage method; MIME initially specified visual ordering for those charset labels by reference to earlier RFCs. Unicode later standardized logical-order character streams and a bidirectional algorithm. **[D]**

The Atari ST’s inclusion of Hebrew glyphs in a CP437-derived ROM did not by itself provide a complete bidi text system.

### Arabic

Arabic requires directionality, contextual shaping, joining behavior, and often marks. DOS 720/864, Windows-1256, ISO-8859-6, Mac Arabic/Farsi, and DEC variants used differing mixtures of base letters, presentation forms, and layout conventions. A byte-to-glyph table alone could not provide correct shaping. Some legacy Arabic sets encoded visual presentation forms, making conversion to logical Unicode text lossy or heuristic.

### Indic scripts

A 256-position page cannot comfortably encode Latin controls, punctuation, a large Indic script repertoire, combining vowel signs, conjunct behavior, and multiple languages. Apple created separate Macintosh script systems, including Devanagari, Gujarati, Gurmukhi, Bengali, Tamil, Telugu, Kannada, Malayalam, and others. Their input, glyph selection, and shaping depended on script managers rather than a simple Western SBCS model. Unicode’s combining-character and shaping architecture absorbed these requirements more generally.

### Chinese, Japanese, and Korean

Thousands of ideographs made single-byte vendor pages inadequate. Solutions included:

- JIS X 0201 plus JIS X 0208;
- Shift_JIS/Windows-932;
- EUC-JP and ISO-2022-JP;
- GB 2312, GBK, Windows-936, later GB 18030;
- Big5 and Windows-950;
- KS X 1001/EUC-KR and Windows-949;
- IBM mixed SBCS/DBCS host and PC pages;
- Macintosh Japanese, Traditional Chinese, Simplified Chinese, and Korean sets.

These systems used lead/trail bytes, escape designation, or multiple planes. Their error synchronization is weaker than an SBCS page: losing one byte can shift lead/trail interpretation until a plausible boundary is found.

Apple’s Unicode 1.0 mapping chapter says Macintosh Simplified Chinese was based on GB 2312, Traditional Chinese on Big5, Japanese on JIS X 0208, and describes other script-set relationships. **[D]**

### Emoji

No historical SBCS Western page can encode modern emoji. CP437’s faces, suits, gender signs, music notes, and dingbats are sometimes called “early emoji,” but that is a modern analogy. They are monochrome glyph cells without Unicode emoji properties, variation selectors, modifiers, flags, or ZWJ sequences. **[Modern analogy]**

Vendor emoji entered Unicode through proposals motivated substantially by Japanese mobile-carrier compatibility. Their standardization is a separate Unicode-era process; it did not descend technically from CP437’s smiley cells, though cultural comparisons are reasonable.

---

## People and institutions

### Relevant precursors

- **Émile Baudot** — five-unit printing-telegraph code, 1870s.
- **Donald Murray** — teleprinter-oriented redesign, early twentieth century.
- **Herman Hollerith** — punched-card tabulation and commercial machine-readable data.
- **Robert W. Bemer** — IBM/Honeywell engineer and prominent ASCII advocate; associated with ESC and other ASCII design arguments.
- **Charles E. Mackenzie** — IBM author of *Coded Character Sets: History and Development* (1980), still the essential documentary synthesis of pre-1980 codes.
- **ASA/USASI/ANSI X3 committees** — institutional producers of X3.4 ASCII.
- **ECMA TC1**, **ANSI X3L2**, **ISO/TC97/SC2** — central to eight-bit graphic-set standardization.
- **CCITT** — telegraph alphabets and communications standards.

### IBM PC and DOS

- **David J. Bradley** — IBM PC ROM BIOS engineer; participant recollection of the CP437 selection meeting.
- **Andy Saenz** — identified by Bradley as responsible for the video adapter and as a repertoire participant.
- **Lew Eggebrecht** — IBM PC chief engineer, also named by Bradley.
- **IBM Entry Systems Division** — organization that produced the PC.
- **Microsoft** — supplier of PC DOS/MS-DOS and later steward of the OEM/Windows division.
- **Bill Gates** — source of the retrospective Wang-influence story, not conclusive proof of repertoire authorship.

### Apple and DEC

- **Apple Computer** — created Macintosh script systems and vendor mappings.
- **Susan Kare** — designer of major Macintosh bitmap fonts and icons; her role should not be inflated into unsupported sole authorship of Mac Roman allocation.
- **Digital Equipment Corporation** — created DEC MCS and the VT220’s character-set architecture.
- Individual DEC MCS repertoire editors were not identified in the primary manuals consulted. **[Open archival question]**

### Unicode-era absorption

- **Joe Becker**, **Lee Collins**, and **Mark Davis** were central founders/early architects of Unicode work; Xerox and Apple were important institutional origins.
- **Unicode Consortium** formalized coordination with ISO/IEC JTC 1/SC 2 on the universal repertoire.
- **Ken Thompson** and **Rob Pike** designed UTF-8 at Bell Labs in 1992; Pike’s published recollection is the major source for the placemat story.
- **Ken Whistler** became a principal Unicode editor and technical authority.
- **IETF** established charset registration and UTF-8 policy.
- **W3C/WHATWG** drove interoperable web decoding and UTF-8 authoring guidance.

These Unicode actors did not design CP437/850/1252, but their work supplied the framework into which the pages were mapped and through which they now survive.

---

## Culture

### CP437 as a graphical medium

CP437’s blocks and junctions let programmers make windows, borders, buttons, graphs, and shading in an 80×25 grid. Its repertoire became inseparable from DOS visual culture. The distinction between “text” and “graphics” was porous: a two-byte video-memory cell could contain an 8-bit glyph selector and an attribute byte for foreground, background, brightness, and blink.

### ANSI art and BBS culture

BBS “ANSI art” normally means:

1. CP437 glyph bytes;
2. ANSI.SYS-compatible escape/control sequences;
3. PC text-mode color attributes and cursor movement.

It does not mean that ANSI standardized CP437. ANSI X3.64/ECMA-48 supplied the broad control-sequence ancestry; the artwork’s glyph palette was IBM PC-specific. **[D/S]**

TheDraw, written by Ian E. Davis and circulating from 1986, made screens, large glyph-fonts, and animations easier to author. Groups such as Aces of ANSI Art, ACiD, and iCE organized releases into artpacks around 1989–90 and afterward. Surviving packs in TEXTFILES.COM and 16colo.rs are direct cultural artifacts. Group-founding “firsts” often depend on scene-maintained histories and pack metadata, so they should be treated as participant/community documentation rather than neutral institutional records.

The 79-column convention is frequently attributed to terminal behavior in which writing the last column triggered wrapping or scrolling. It varied by terminal/BBS client and is better treated as scene practice than a property of CP437. **[Community recollection]**

### Demoscene and warez-scene overlap

NFO and FILE_ID.DIZ files used CP437/CP850-like text graphics, especially on PCs, while Amiga scenes often used Topaz-font ASCII conventions. The scenes overlapped socially and aesthetically but were not identical. “Demoscene used CP437” is therefore true for many PC artifacts, not universally true across platforms. **[S]**

### PETSCII and ATASCII art

Commodore and Atari users developed native text-art traditions using platform-specific graphic characters, colors, inverse video, cursor controls, and reprogrammable character sets. Calling these ASCII art is culturally conventional but technically imprecise.

PETSCII art remains an active practice because it treats the finite repertoire as a compositional constraint. Modern editors and Unicode approximations are preservation layers, not proof that every original graphic has one semantically exact Unicode character.

### Mojibake as failure and aesthetic

Japanese `文字化け` (*mojibake*, “character transformation/garbling”) names text rendered under the wrong encoding. It is a technical failure, but artists and designers now deliberately reproduce `Ã©`, `â€™`, black diamonds, replacement characters, and CP437 glyph collisions as markers of damaged media, globalization, retrocomputing, or network instability. That intentional usage is a modern aesthetic built from earlier accidental failures. **[Modern invention]**

### “Plain text”

The code-page era exposes the limits of the “plain text” ideal. Bytes are not self-describing text. To interpret them one needs:

- a character encoding;
- sometimes a font/glyph convention;
- newline rules;
- direction and shaping;
- terminal state;
- language-dependent collation and case behavior.

Unicode greatly reduces repertoire fragmentation, but it does not eliminate fonts, bidi, normalization, grapheme segmentation, locale, or rendering politics.

---

## Controversies and disputes

### 1. “Extended ASCII”

**Finding:** There is no unique encoding called extended ASCII.

- **Documented:** ASCII is seven-bit; IBM437, IBM850, Windows-1252, Macintosh, and DEC-MCS have separate registered names.
- **Folklore:** charts headed “extended ASCII” often silently print CP437 or CP1252.
- **Risk:** a program that accepts “ASCII” but actually processes bytes `80–FF` cannot be interpreted without another convention.

### 2. Who designed CP437?

- **Participant account 1:** Bradley names himself, Saenz, and Eggebrecht in an airplane meeting.
- **Participant account 2:** Gates attributes the “funny Wang character set” to Microsoft’s Wang interest.
- **Contrary evidence:** the known Wang repertoire does not match all glyphs Gates names.
- **Documented baseline:** IBM shipped the repertoire in its 1981 PC hardware.
- **Conclusion:** exact cell-by-cell authorship remains incompletely documented. Bradley’s is the most specific account; Gates’s is evidence of influence or memory, not a decisive authorship record.

### 3. Was CP437 created as “code page 437”?

The first PC shipped a 256-glyph hardware repertoire. Later IBM registry machinery named and numbered it. Treating “CP437” as the exact 1981 project name is anachronistic unless a period document using that number is produced. **[S]**

The popular story that IBM code-page numbers originally came from manual page numbers is widely repeated but weakly documented and cannot explain the mature numbering system consistently. It should remain folklore pending an IBM administrative source. **[Folklore/open]**

### 4. The `7F` glyph

“House,” “delta,” and visual ambiguity coexist in surviving sources. Unicode needed one abstract mapping and chose HOUSE, but that does not recover original designer intent. **[Disputed]**

### 5. CP850 versus text interfaces

CP850’s removal of CP437 junctions is sometimes described as a design mistake and sometimes as successful internationalization. The documentary fact is the repertoire tradeoff; whether prose or line fidelity deserved priority is a user-context judgment. Programs that treated glyph positions as immutable graphics were inherently code-page-dependent.

### 6. Windows-1252 as “ANSI”

Microsoft itself now calls this a historical misnomer. It originated in proximity to an ANSI draft but diverged by putting graphics in the C1 region. The label survived in `A` APIs and phrases such as “ANSI code page.” **[D]**

### 7. Windows-1252 versus Latin-1

They coincide at `00–7F` and `A0–FF`, not at `80–9F`.

- CP1252 smart quote `92` is a printable right quote.
- ISO-8859-1 `92` is C1 private-use control 2.
- HTML decoders treat the Latin-1 label as CP1252 for compatibility.
- General-purpose converters should not silently assume that web rule outside web contexts.

### 8. The euro revisions

Vendors had to displace something:

- Windows-1252 used formerly unassigned `80`.
- ISO-8859-15 replaced the generic currency sign and several less-needed Latin-1 characters.
- Mac Roman replaced its currency sign.
- CP858 replaced CP850 dotless `ı` at `D5`.

IBM PC DOS 2000 reportedly redefined its “modified 850” to include the euro, while later practice distinguishes CP858. Contemporary IBM correspondence and manuals should be checked before treating every “850 with euro” file identically. **[D/P/S; implementation variation]**

### 9. Vendor power and national coverage

The 8-bit page model made repertoire allocation visibly zero-sum. Adding `Œ` might mean removing a box junction; adding Hebrew might remove semigraphics; adding the euro displaced an existing character. Vendor market priorities determined which languages could coexist and which users needed a separate page.

This is political in the ordinary institutional sense, but not every omission proves deliberate exclusion. Hardware space, installed compatibility, keyboard input, printer support, and market size all constrained choices.

### 10. Han unification, Tibetan disputes, and emoji

These are Unicode controversies, not disputes internal to CP437/850/1252. They belong here because Unicode absorbed the pages:

- **Han unification:** Unicode/ISO 10646 encode many Chinese, Japanese, and Korean cognate ideographs at shared abstract code points, leaving regional glyph form to fonts and language context. Japanese critics argued that this erased meaningful distinctions or made correct typography dependent on external locale/font information. Defenders distinguished abstract character identity from glyph shape. Both concerns have technical substance.
- **CJK source separation:** later variation sequences, compatibility ideographs, source properties, and extension blocks address distinctions without abandoning the unified model.
- **Tibetan:** early encoding proposals and implementation choices generated disputes about character decomposition, stacks, and canonical representation. These require their own document-by-document dossier; no evidence ties them directly to the Western vendor pages.
- **Emoji:** carrier compatibility, corporate submissions, and Unicode Technical Committee voting made the Consortium a public target for criticism over representation and inclusion. Proposals are documented, but popular claims that a single company or public “emoji vote” directly decides every character oversimplify the process.

### 11. Security

#### Wrong-page interpretation

If validation occurs under one page and execution under another, punctuation or path characters can change meaning. Legacy archive filenames are especially vulnerable because an extractor may choose a different charset from the scanner.

#### Homoglyphs

Legacy pages already contain confusables: Latin `A`, Greek-like symbols, vertical bars, box strokes, currency signs, and lookalike punctuation. Unicode greatly expands the repertoire and therefore the attack surface, but the underlying problem—visual identity differing from code identity—is older.

#### C0/C1 ambiguity

A CP1252 punctuation byte interpreted as ISO-8859-1 can become a control; a CP437 control cell displayed directly can become a pictograph. Filters that validate rendered glyphs rather than bytes, or vice versa, can disagree.

#### NUL

All these pages inherit byte `00`. C-language APIs treat NUL as string termination. A parser that counts a longer field while a downstream C API stops at NUL can be exploitable. This is not unique to code pages.

#### BOM

Single-byte pages have no BOM. Prefixing `EF BB BF` to a CP1252 or CP437 file inserts three ordinary upper-half bytes. Conversely, UTF-8 software may treat those bytes as U+FEFF/signature. BOM confusion is therefore a format-detection issue at boundaries.

#### Overlong UTF-8

Overlong encodings are not a CP437/1252 feature. They arose in early permissive UTF-8 decoders, where an ASCII character could be encoded with more bytes than necessary and bypass byte-oriented filters. RFC 3629 forbids overlong sequences and restricts UTF-8 to valid Unicode scalar values. The relevance here is migration: transcoding must validate the source rather than interpreting arbitrary invalid UTF-8 as a legacy page opportunistically.

---

## Open questions

1. **Where are the surviving IBM internal memos for the 1981 repertoire?** The technical reference proves the table; Bradley supplies a recollection. A dated requirements sheet or meeting record would resolve authorship and rationale.

2. **When exactly did IBM first use the number 437 for the PC repertoire?** Later registry material is clear; the earliest dated occurrence needs archival verification.

3. **Who individually edited CP850?** DOS manuals document deployment, not cell-level authorship.

4. **What exact ANSI/X3L2 draft revision did Windows 1.0 implement?** Microsoft states the connection, but a draft-to-Windows comparison would be stronger than later summaries.

5. **Can every CP1252 revision be reconstructed from original Windows 1.0, 2.0, 3.0, 3.1, Windows 95, and Windows 98 SDK/NLS files?** This is feasible archival work and would settle secondary chronology.

6. **Who assigned Mac Roman positions?** Apple manuals document the repertoire; individual repertoire editors remain unidentified here.

7. **Who at DEC selected DEC MCS’s exact characters?** The VT220 manual documents behavior but not personal authorship.

8. **Was “small house” an intended 1981 identity, a 1984 registry interpretation, or both?** Surviving labels conflict.

9. **How many historical ZIP implementations obeyed CP437 when bit 11 was clear?** The specification does not describe actual ecosystem compliance; a corpus study is needed.

10. **Which code page dominates surviving BBS/NFO collections outside North America?** CP850 and local variants are often normalized to CP437 by modern archives, potentially erasing original byte context.

11. **How much modern “CP437 art” is a Unicode/font reconstruction?** Unicode mappings preserve characters, but cell aspect ratio, ninth-column duplication, blink, palette, and ambiguous glyph identities affect faithful rendering.

12. **What is the origin of the manual-page-number explanation for IBM code-page identifiers?** It is common folklore, but an authoritative IBM source was not located.

---

## Sources

### Original and official standards, registries, and RFCs

- RFC 20, V. G. Cerf, *ASCII Format for Network Interchange*, 16 October 1969:  
  https://www.rfc-editor.org/rfc/rfc20.html
- RFC 1345, Keld Simonsen, *Character Mnemonics and Character Sets*, June 1992:  
  https://www.rfc-editor.org/rfc/rfc1345.html
- RFC 2045, *MIME Part One: Format of Internet Message Bodies*, November 1996:  
  https://www.rfc-editor.org/rfc/rfc2045.html
- RFC 2046, *MIME Part Two: Media Types*, November 1996:  
  https://www.rfc-editor.org/rfc/rfc2046.html
- RFC 2277, Harald Alvestrand, *IETF Policy on Character Sets and Languages*, January 1998:  
  https://www.rfc-editor.org/rfc/rfc2277.html
- RFC 2278, *IANA Charset Registration Procedures*, January 1998:  
  https://www.rfc-editor.org/rfc/rfc2278.html
- RFC 3629, F. Yergeau, *UTF-8, a Transformation Format of ISO 10646*, November 2003:  
  https://www.rfc-editor.org/rfc/rfc3629.html
- RFC 5198, *Unicode Format for Network Interchange*, March 2008:  
  https://www.rfc-editor.org/rfc/rfc5198.html
- IANA Character Sets registry:  
  https://www.iana.org/assignments/character-sets/
- IANA charset registrations:  
  https://www.iana.org/assignments/charset-reg/
- ECMA-94, *8-bit Single-Byte Coded Graphic Character Sets—Latin Alphabets No. 1 to No. 4*, first edition March 1985; second edition June 1986:  
  https://ecma-international.org/publications-and-standards/standards/ecma-94/
- ECMA-94 second-edition PDF:  
  https://www.ecma-international.org/wp-content/uploads/ECMA-94_2nd_edition_june_1986.pdf
- ECMA-128 historical introduction to the 8-bit graphic-set work:  
  https://www.ecma-international.org/wp-content/uploads/ECMA-128_2nd_edition_december_1999.pdf
- ISO catalogue:  
  https://www.iso.org/standards.html

### IBM and DOS

- IBM, *Personal Computer Technical Reference*, first edition, August 1981, part no. 6025008; searchable copy/index:  
  https://thestarman.pcministry.com/asm/bios/A-5.htm
- IBM/Microsoft, *MS-DOS 3.3 User’s Guide*, 1987, Appendix E, “How to Use Code Pages”:  
  https://www.bitsavers.org/pdf/microsoft/msdos_3.3/MS-DOS_3.3_Users_Guide_198707.pdf
- IBM, *DOS 4.00 Reference*, July 1988:  
  https://bitsavers.computerhistory.org/pdf/ibm/pc/dos/84X1712_DOS_4.0_Reference_Jul88.pdf
- IBM code-page reference list:  
  https://www.ibm.com/docs/en/cics-tg-zos/10.1.0?topic=reference-code-pages
- IBM CCSID values:  
  https://www.ibm.com/docs/en/i/7.4.0?topic=reference-ccsid-values
- IBM explanation of CCSID, code page, CP437, CP1252, and CP819:  
  https://www.ibm.com/support/pages/ifs-stmf-ccsids-1252-437-and-819
- IBM CP437 collation/mapping table:  
  https://www.ibm.com/docs/en/db2/11.5.x?topic=tables-code-page-437-generic-system-437
- IBM PC code-set structure including CP850:  
  https://www.ibm.com/docs/en/aix/7.3.0?topic=support-pc-code-sets
- IBM CGM code pages 437, 850, and 819:  
  https://www.ibm.com/docs/en/gddm?topic=support-cgm-code-pages
- IBM code-page conversion guidance:  
  https://www.ibm.com/support/pages/customizing-code-page-37-850-translation-table
- Unicode vendor mapping for IBM PC CP437:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/PC/CP437.TXT
- Columbia Kermit CP437 table:  
  https://ftp.columbia.edu/kermit/cp437.html
- Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley/IBM, 1980, Internet Archive search/catalogue:  
  https://archive.org/search?query=Charles+Mackenzie+Coded+Character+Sets+History+and+Development

### Microsoft and Windows-1252

- Microsoft, “Code Pages”:  
  https://learn.microsoft.com/en-us/windows/win32/intl/code-pages
- Microsoft, “Code Page Identifiers”:  
  https://learn.microsoft.com/en-us/windows/win32/intl/code-page-identifiers
- Unicode Consortium’s Microsoft Windows mapping directory:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/
- Canonical CP1252 mapping:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP1252.TXT
- Microsoft OpenType documentation, euro currency symbol and code-page positions:  
  https://learn.microsoft.com/en-us/typography/opentype/otspec181/euro
- Microsoft press release, “Microsoft Announces Plans to Support the Euro Currency Symbol,” 29 April 1998:  
  https://news.microsoft.com/source/1998/04/29/microsoft-announces-plans-to-support-the-euro-currency-symbol/
- Chris Wendt, Microsoft, W3C mailing-list response on Windows 98 CP1252 additions, 28 August 1998:  
  https://lists.w3.org/Archives/Public/www-international/1998JulSep/0022.html
- Raymond Chen, “Why is the default 8-bit codepage called ‘ANSI’?”, 31 May 2004:  
  https://devblogs.microsoft.com/oldnewthing/20040531-00/?p=39103
- Raymond Chen, discussion of OEM/ANSI naming and filename APIs:  
  https://devblogs.microsoft.com/oldnewthing/20051027-37/?p=33593
- Raymond Chen, CP_ACP, CP_OEM, and Unicode conversion:  
  https://devblogs.microsoft.com/oldnewthing/20090115-00/?p=19483
- Unicode mailing-list exchange on the date of CP1252’s euro revision, February 2003:  
  https://www.unicode.org/mail-arch/unicode-ml/y2003-m02/0506.html
- Unicode mailing-list archive showing the late-1990s CP1252 table and contemporary web concern:  
  https://www.unicode.org/mail-arch/unicode-ml/Archives-Old/UML008/0452.html
- Columbia Kermit Windows-1252 table:  
  https://www.columbia.edu/kermit/cp1252.html

### Apple

- Apple, *Inside Macintosh: Text*, 1993:  
  https://vintageapple.org/inside_r/pdf/Text_1993.pdf
- Original *Inside Macintosh* volumes I–III scan:  
  https://puyoman.net/documentation/Inside_Macintosh.pdf
- Unicode Consortium Apple mappings directory:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/
- Apple Mac Roman mapping:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/ROMAN.TXT
- Unicode 1.0, chapter 6, Macintosh character mappings and script systems:  
  https://www.unicode.org/versions/Unicode1.0.0/ch06.pdf
- Apple Technical Note TN1150, *HFS Plus Volume Format*:  
  https://developer.apple.com/library/archive/technotes/tn/tn1150.html
- Apple developer description of Mac Roman:  
  https://developer.apple.com/documentation/coregraphics/cgtextencoding/encodingmacroman

### DEC

- DEC, *VT220 Programmer Reference Manual*, contents and code tables:  
  https://www.zx.net.nz/computers/dec/vt220/doc/vt220-rm/contents.html
- DEC MCS C0/GL table:  
  https://www.zx.net.nz/computers/dec/vt220/doc/vt220-rm/table2-3a.html
- VT220 character-set designation and invocation behavior:  
  https://www.zx.net.nz/computers/dec/vt220/doc/vt220-rm/chapter4.html
- DEC VT220 manual scan collection:  
  https://bitsavers.trailing-edge.com/pdf/dec/terminal/vt220/
- DEC MCS table with cited VMS and VT330/340 manuals:  
  https://www.columbia.edu/kermit/dec-mcs.html

### Commodore, Atari, and Amstrad

- Commodore PETSCII reference and preserved tables:  
  https://cbasereferenceguide.github.io/petscii/character-set/
- Comparative Commodore PETSCII tables:  
  https://cbasereferenceguide.github.io/petscii/character-set/commodore-petscii-character-sets.pdf
- Atari ATASCII table and documentation:  
  https://www.atariarchives.org/c3ba/appendixa.php
- Atari Assembler Editor manual with ATASCII chart:  
  https://atariwiki.org/wiki/attach/Atari%20Assembler%20Editor/ATARI%20Assembler%20Editor%20User-s%20Manual-OCR.pdf
- Atari ST technical-reference catalogue:  
  https://www.manualslib.com/products/Atari-St-4020773.html
- Amstrad CPC Firmware Guide:  
  https://www.cpcwiki.eu/imgs/0/02/CPC_firmware.pdf
- Amstrad CPC464 manual, ASCII and graphics section:  
  https://www.manualslib.com/manual/862146/Amstrad-Cpc464.html?page=227
- Amstrad CPC firmware-manual preservation page:  
  https://www.cantrell.org.uk/david/tech/cpc/cpc-firmware/download.htm

### Web, Unicode transition, and archives

- WHATWG Encoding Standard:  
  https://encoding.spec.whatwg.org/
- WHATWG HTML parsing and supported legacy encodings:  
  https://html.spec.whatwg.org/multipage/parsing.html
- W3C, “Who uses Unicode?” with historical web figures:  
  https://www.w3.org/International/questions/qa-who-uses-unicode.en.html
- W3Techs UTF-8 usage report:  
  https://w3techs.com/technologies/breakdown/en-utf8/ranking
- PKWARE ZIP Application Note landing page:  
  https://support.pkware.com/pkzip/appnote
- Preserved APPNOTE text containing Appendix D, historical CP437 and UTF-8 bit 11:  
  https://gist.github.com/danicat/207ce39725fc0513bba8ba553e868bb8
- Common ZIP specification:  
  https://commonzip.org/spec/
- Info-ZIP Unicode extra-field documentation:  
  https://sources.debian.org/src/zip/3.0-6/proginfo/extrafld.txt/
- Unicode character-mapping inventory, Unicode Technical Committee document L2/99-325:  
  https://www.unicode.org/L2/L1999/99325-N.htm

### Cultural and contested-material archives

- ANSI/BBS technical and cultural overview:  
  https://www.bbsgames.org/wiki/ANSI_art
- ANSI-BBS server/client specification, including CP437 assumptions:  
  https://ansi-bbs.org/ansi-bbs-core-server.html
- 16colo.rs preservation project source:  
  https://github.com/16colo-rs/16c
- Sixteen Colors organization:  
  https://github.com/sixteencolors
- TEXTFILES.COM art-scene archive:  
  http://artscene.textfiles.com/
- Acheron, “Abbreviated History of the Underground Computer Art Scene,” a late-1990s community history:  
  https://www.acheron.org/articles/ar-history.shtml
- Modern investigation of CP437’s `7F` house/delta identity:  
  https://blog.glyphdrawing.club/why-is-there-a-small-house-in-ibm-s-code-page-437/
- IBM PC Technical Reference and retro-document archive index at Bitsavers:  
  https://bitsavers.org/
- Computer History Museum oral histories catalogue:  
  https://www.computerhistory.org/collections/oralhistories/
- Bob Bemer material, preserved-site search at the Internet Archive:  
  https://web.archive.org/web/*/http://www.bobbemer.com/*
- Unicode Consortium history:  
  https://home.unicode.org/about-unicode/history-of-unicode/
- Unicode technical reports:  
  https://www.unicode.org/reports/
- Unicode Technical Committee document register and minutes:  
  https://www.unicode.org/L2/
- Unicode emoji proposals and submission material:  
  https://unicode.org/emoji/proposals.html
- Rob Pike, UTF-8 history material:  
  https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt
