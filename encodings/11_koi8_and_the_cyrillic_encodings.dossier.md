# KOI8 and the Cyrillic encodings: Research Dossier

> **Standard:** GOST 19768-74 for the ancestral KOI-7/KOI-8; RFC 1489 for KOI8-R; RFC 2319 for KOI8-U  
> **Years:** 1974; KOI8-R registered July 1993; KOI8-U history begins in 1992, registered April 1998  
> **Width:** KOI-7: 7 bits, with repertoire switching in some implementations; KOI-8, KOI8-R, KOI8-U: fixed-width 8-bit single-byte encodings  
> **Repertoire:** ASCII in bytes `00–7F`, plus Russian Cyrillic, box drawing, block graphics, and a few mathematical signs in `80–FF`; KOI8-U substitutes four Ukrainian letter pairs for box-drawing characters  
> **Current status:** Registered and still decoded by browsers and operating-system libraries for compatibility, but obsolete for newly created interchange. UTF-8 is the required encoding for new web formats and dominates the measured public web.

## Evidence labels

Claims below carry one of these labels:

- **[STANDARD]** Normative standard, registry, or standards-track text.
- **[DOCUMENT]** Contemporary technical document or published mapping.
- **[RECOLLECTION]** Participant’s later account.
- **[RECONSTRUCTION]** Later historical synthesis based on technical evidence.
- **[DISPUTED]** Conflicting accounts or uncertain credit.
- **[FOLKLORE]** Widely repeated story with inadequate primary corroboration.
- **[MODERN]** Current implementation, usage, or cultural evidence.

“RFC” does not automatically mean Internet Standard. RFC 1489 and RFC 2319 are Informational documents.

---

## 1. Basic identification

### 1.1 The name

**[STANDARD]** КОИ abbreviates Russian *Код для обмена и обработки информации*, “Code for Information Interchange and Processing.” “8” means eight bits. The historical typography varies among `КОИ-8`, `KOI-8`, and later Internet-style names `KOI8-R` and `KOI8-U`.

The family is not one immutable code:

| Name | Authority/date | Description |
|---|---|---|
| KOI-7 | GOST 19768-74, 1974 | Seven-bit Cyrillic/Latin arrangement, principally uppercase Cyrillic |
| Old KOI-8 | GOST 19768-74, 1974 | Eight-bit combination of an ASCII-like lower half with Cyrillic in the upper half |
| ISO-IR-111 / first ECMA-113 | ISO registration, 1985; ECMA, 1986 | Multilingual Cyrillic extension retaining the KOI correspondence |
| Revised GOST / ISO-IR-153 | GOST revision, 1987; related CMEA standard ST SEV 358-88 | Alphabetically ordered successor, incompatible with old KOI-8 |
| KOI8-R | RFC 1489, July 1993 | Russian Internet/Unix form, including Ё/ё and extensive pseudographics |
| KOI8-U | Ukrainian community adoption, 1992 and 1995; RFC 2319, 1998 | KOI8-R plus Є/є, І/і, Ї/ї, Ґ/ґ |
| KOI8-RU | Later registration outside the core RFC pair | Adds Ukrainian letters and Belarusian Ў/ў |
| KOI8-T | Later regional variant | Tajik Cyrillic |
| KOI8-F / “KOI8 Unified” | Vendor proposal | Attempted pan-Slavic combination; little deployment |

**[STANDARD]** RFC 1489 calls `koi8-r` a de facto standard for “Unix and global network applications in the former Soviet Union,” not an international standard. It identifies the Society of Unix User Groups and the RELCOM Development Team as the registering parties. [RFC 1489](https://www.rfc-editor.org/rfc/rfc1489.html)

**[STANDARD]** IANA presently retains KOI8-R as MIBenum 2084 and KOI8-U as 2088. Registration means that software can identify old data unambiguously; it does not mean that either is recommended for new data. [IANA Character Sets registry](https://www.iana.org/assignments/character-sets)

**[MODERN]** The WHATWG Encoding Standard defines interoperable decoders for KOI8-R and KOI8-U and recognizes old labels such as `koi`, `koi8`, `koi8-r`, `cskoi8r`, `koi8-u`, and `koi8-ru`. The same specification requires UTF-8 exclusively for new protocols and formats. [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/)

---

## 2. The code in detail

## 2.1 Fundamental structure

### KOI8-R

**[STANDARD]** KOI8-R is a stateless, fixed-width single-byte code:

| Byte range | Function |
|---|---|
| `00–1F` | ASCII C0 controls |
| `20–7E` | ASCII printable repertoire |
| `7F` | DEL |
| `80–9F` | Box drawing, blocks, mathematics, NBSP |
| `A0–BF` | Double-line box drawing, Ё/ё, copyright |
| `C0–DF` | Lowercase Russian Cyrillic |
| `E0–FF` | Uppercase Russian Cyrillic |

Every character occupies exactly one byte. No lead byte, continuation byte, escape sequence, or byte-order marker exists.

RFC 1489 states that `00–7F` “fully” coincides with ASCII. Thus KOI8-R has:

- NUL `00`
- TAB `09`
- LF `0A`
- CR `0D`
- ESC `1B`
- SPACE `20`
- ordinary dollar sign `$` at `24`
- DEL `7F`

This is a difference from the literal 1974 GOST arrangement commonly reconstructed as using the general currency sign `¤` where ASCII has `$`. RFC 1489’s registered KOI8-R uses ASCII `$`.

### The full KOI8-R upper half

The authoritative Unicode correspondences below come from RFC 1489 and the Unicode mapping file. Historical RFC names such as “IU,” “IA,” and “YERI” have been normalized here to the current characters.

| Hex | Character | Hex | Character | Hex | Character | Hex | Character |
|---:|:---:|---:|:---:|---:|:---:|---:|:---:|
| 80 | ─ | 81 | │ | 82 | ┌ | 83 | ┐ |
| 84 | └ | 85 | ┘ | 86 | ├ | 87 | ┤ |
| 88 | ┬ | 89 | ┴ | 8A | ┼ | 8B | ▀ |
| 8C | ▄ | 8D | █ | 8E | ▌ | 8F | ▐ |
| 90 | ░ | 91 | ▒ | 92 | ▓ | 93 | ⌠ |
| 94 | ■ | 95 | ∙ | 96 | √ | 97 | ≈ |
| 98 | ≤ | 99 | ≥ | 9A | NBSP | 9B | ⌡ |
| 9C | ° | 9D | ² | 9E | · | 9F | ÷ |
| A0 | ═ | A1 | ║ | A2 | ╒ | A3 | ё |
| A4 | ╓ | A5 | ╔ | A6 | ╕ | A7 | ╖ |
| A8 | ╗ | A9 | ╘ | AA | ╙ | AB | ╚ |
| AC | ╛ | AD | ╜ | AE | ╝ | AF | ╞ |
| B0 | ╟ | B1 | ╠ | B2 | ╡ | B3 | Ё |
| B4 | ╢ | B5 | ╣ | B6 | ╤ | B7 | ╥ |
| B8 | ╦ | B9 | ╧ | BA | ╨ | BB | ╩ |
| BC | ╪ | BD | ╫ | BE | ╬ | BF | © |
| C0 | ю | C1 | а | C2 | б | C3 | ц |
| C4 | д | C5 | е | C6 | ф | C7 | г |
| C8 | х | C9 | и | CA | й | CB | к |
| CC | л | CD | м | CE | н | CF | о |
| D0 | п | D1 | я | D2 | р | D3 | с |
| D4 | т | D5 | у | D6 | ж | D7 | в |
| D8 | ь | D9 | ы | DA | з | DB | ш |
| DC | э | DD | щ | DE | ч | DF | ъ |
| E0 | Ю | E1 | А | E2 | Б | E3 | Ц |
| E4 | Д | E5 | Е | E6 | Ф | E7 | Г |
| E8 | Х | E9 | И | EA | Й | EB | К |
| EC | Л | ED | М | EE | Н | EF | О |
| F0 | П | F1 | Я | F2 | Р | F3 | С |
| F4 | Т | F5 | У | F6 | Ж | F7 | В |
| F8 | Ь | F9 | Ы | FA | З | FB | Ш |
| FC | Э | FD | Щ | FE | Ч | FF | Ъ |

Sources: [RFC 1489 table](https://www.rfc-editor.org/rfc/rfc1489.html), [Unicode KOI8-R mapping](https://www.unicode.org/Public/MAPPINGS/VENDORS/MISC/KOI8-R.TXT).

### Case

**[STANDARD]** KOI8-R places lowercase Russian at `C0–DF` and capitals at `E0–FF`. For the 32 basic Russian letters, changing case is usually equivalent to toggling bit `0x20`, just as ASCII changes `A` to `a`. Ё/ё are the exceptions: `A3`/`B3`.

**[RECONSTRUCTION]** This case orientation looks reversed if one thinks of the high-bit-stripping property: lowercase Cyrillic maps to ASCII capitals and Cyrillic capitals to ASCII lowercase. It is not an accidental implementation bug.

### Collating order

**[DOCUMENT]** Raw byte sorting is not Russian dictionary order. From `E1` onward, KOI8-R capitals read:

`А Б Ц Д Е Ф Г Х И Й К Л М Н О П Я Р С Т У Ж В Ь Ы З Ш Э Щ Ч Ъ`

That is an ASCII-correspondence order, not Russian:

`А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я`.

Therefore a bytewise sort puts Ц before Д, Ф before Г, Я before Р, and so forth. Proper sorting always required language-aware tables or conversion.

## 2.2 The “KOI8 trick”

**[DOCUMENT]** Clearing bit 7—the numeric `0x80` bit—of most Russian letters produces ASCII letters chosen as rough phonetic counterparts. For example:

```text
KOI8-R:  Русский Текст
Bytes:   F2 D5 D3 D3 CB C9 CA 20 F4 C5 CB D3 D4
& 7F:    72 55 53 53 4B 49 4A 20 74 45 4B 53 54
ASCII:   rUSSKIJ tEKST
```

A reader encountering a damaged seven-bit path sees case-inverted pseudo-transliteration rather than arbitrary punctuation.

The correspondence is approximate:

- Р → `r`, С → `s`, Т → `t`
- У → `u`, К → `k`, И → `i`
- Ж → `v` or `V` by code position, not a conventional modern transliteration
- Х → `h`, Ц → `c`, Ч → `~` after stripping, depending on the exact member of the family
- Ь, Ы, Ъ necessarily receive imperfect Latin stand-ins

**[STANDARD]** RFC 1489 prints the mapping but does **not** explain this property or claim that Chernov invented it.

**[RECONSTRUCTION]** Roman Czyborra’s “Cyrillic Charset Soup,” published in 1998, is an early widely accessible account explicitly describing decipherability after bit stripping and tracing the principle to GOST 19768-74. C-Kermit documentation likewise calls the result “Short KOI” and gives a transliteration example.

**[DISPUTED CREDIT]** It is therefore misleading to say that Chernov invented the bit-stripping trick in 1993. The correspondence is present in the 1974 KOI family and has antecedents in Soviet telegraph practice. Chernov registered and stabilized the particular KOI8-R repertoire used on the Internet.

**[FOLKLORE]** The stronger story—“KOI8-R was deliberately created in 1993 so Russian mail would survive American seven-bit routers”—is common in popular retellings. The engineering benefit is real; the 1993-origin version is not supported by RFC 1489. No located contemporary design memo by Chernov assigns the original idea to him.

## 2.3 KOI8-U differences

**[STANDARD]** KOI8-U preserves every Russian letter in KOI8-R and replaces eight box-drawing positions with four Ukrainian letter pairs:

| Byte | KOI8-R | KOI8-U | Unicode |
|---:|:---:|:---:|---:|
| A4 | ╓ | є | U+0454 |
| A6 | ╕ | і | U+0456 |
| A7 | ╖ | ї | U+0457 |
| AD | ╜ | ґ | U+0491 |
| B4 | ╢ | Є | U+0404 |
| B6 | ╤ | І | U+0406 |
| B7 | ╥ | Ї | U+0407 |
| BD | ╫ | Ґ | U+0490 |

RFC 2319 says that the first three Ukrainian pairs were adopted at a conference of Ukrainian ISP postmasters in Slavsk in autumn 1992, on a proposal presented by Igor Sviridov of Kyiv and Stas Vorony of Kharkiv. Ґ/ґ was added in June 1995. [RFC 2319](https://www.rfc-editor.org/rfc/rfc2319.html)

**[STANDARD]** RFC 2319 describes KOI8-U as a de facto Ukrainian Internet standard used in mail, Usenet news, and the Web. It too is Informational, not an IETF standards-track mandate.

## 2.4 What KOI8-R can and cannot express

**[STANDARD]** It directly expresses:

- all 33 modern Russian letters when Ё is counted separately;
- upper- and lowercase Latin ASCII;
- ASCII digits and punctuation;
- ASCII control characters;
- box and block graphics useful on character-cell terminals;
- a small set of mathematical signs;
- NBSP and ©.

It cannot directly express:

- Ukrainian Є, І, Ї, Ґ—hence KOI8-U;
- Belarusian Ў or a distinct Cyrillic І—hence KOI8-RU or other variants;
- Serbian Ј, Љ, Њ, Ћ, Џ and Macedonian Ѓ, Ѕ, Ј, Љ, Њ, Ќ, Џ;
- most non-Russian Cyrillic used in Central Asia, the Caucasus, Siberia, or historical Slavonic;
- accented Latin alphabets beyond plain ASCII;
- Greek, Hebrew, Arabic, Indic scripts, CJK characters, combining marks, typographic quotation marks, or emoji;
- a general mechanism for arbitrary composition.

**[DOCUMENT]** KOI8-R is nevertheless sufficient for modern Bulgarian’s letter inventory, because modern Bulgarian uses a subset of the Russian basic Cyrillic letters and does not require Ё. Glyph style is a separate typographic issue: Bulgarian forms of several lowercase letters can differ from Russian forms without requiring separate character codes.

## 2.5 Shift and escape mechanisms

### KOI8-R and KOI8-U

**[STANDARD]** None. They are stateless single-byte encodings. Bytes `0E` and `0F` retain ASCII’s SO and SI control identities, and `1B` remains ESC, but RFC 1489 does not use them to switch KOI8-R repertoires.

### KOI-7

**[RECONSTRUCTION]** KOI-7 existed in variants normally described as N0/N1 or Latin/Cyrillic sets. Cyrillic occupied positions corresponding to Latin graphics. Equipment could select the Latin or Cyrillic repertoire externally or through shift conventions, commonly SO/SI in terminal practice. This is stateful behavior at the terminal or code-extension level, unlike KOI8-R itself.

**[CAUTION]** Implementations varied. It is unsafe to infer a terminal’s exact SO/SI protocol merely from a statement that it used “KOI-7.” GOST tables, ISO 2022 designation, and a particular terminal’s keyboard/display state are distinct layers.

### ISO 2022 relationship

**[STANDARD]** ISO 2022/ECMA-35 defines a general architecture for designating and invoking 94- or 96-character graphic sets with ESC, SI, SO, and related controls. ISO-IR-111 received an ISO registry identity usable within that framework. Plain KOI8-R mail normally used raw eight-bit bytes plus a MIME charset declaration, not ISO-2022 escape switching. [ECMA-35](https://ecma-international.org/publications-and-standards/standards/ecma-35/)

## 2.6 Error and synchronization properties

**[RECONSTRUCTION]**

- Every byte is independently aligned. Starting in the middle of a KOI8-R file loses at most the earlier context, not byte synchronization.
- Insertion or deletion of a byte alters one character and shifts external byte offsets, but every later byte still decodes independently.
- A bit error changes one character. There is no built-in checksum, parity requirement, or invalid-byte detector: all 256 values have defined roles under the RFC mapping.
- A reader cannot infer KOI8-R reliably from byte structure alone. The same byte sequence is structurally valid in CP866, Windows-1251, ISO-8859-5, or a Western code page.
- Clearing the high bit is lossy but often leaves rough transliteration. Setting or flipping it does not have a similarly useful guarantee.
- Charset misidentification produces systematic mojibake, frequently more damaging than random corruption because every Cyrillic byte is reinterpreted consistently as the wrong character.

This differs from UTF-8. UTF-8 continuation-byte patterns provide limited resynchronization and make many byte strings invalid, whereas KOI8-R has no structural validity test.

## 2.7 Newline, space, and deletion

**[STANDARD]**

| Function | Byte | Notes |
|---|---:|---|
| NUL | `00` | Same as ASCII |
| Horizontal tab | `09` | Same as ASCII |
| Line feed | `0A` | Unix newline |
| Carriage return | `0D` | Used with LF in Internet CRLF |
| Space | `20` | Ordinary breaking space |
| No-break space | `9A` | KOI8-R mapping |
| Delete | `7F` | ASCII DEL |
| Escape | `1B` | ASCII ESC; no KOI8-R shift meaning |

Unix KOI8-R files conventionally used LF. Internet mail protocols used CRLF at the transport syntax level. DOS text used CRLF regardless of whether its Cyrillic bytes were CP866 or another code page.

The historical significance of `7F` comes from punched tape: an all-ones position could be produced by punching every hole, allowing a character to be obliterated. KOI8-R inherits the value through ASCII; it does not introduce a new deletion mechanism.

## 2.8 Worked examples

### Example A: “Привет, мир!”

The Unicode characters are:

```text
П   р   и   в   е   т   ,  SP  м   и   р   !
041F 0440 0438 0432 0435 0442 002C 0020 043C 0438 0440 0021
```

#### KOI8-R

```text
П   р   и   в   е   т   ,   SP  м   и   р   !
F0  D2  C9  D7  C5  D4  2C  20  CD  C9  D2  21
```

Bit stripping:

```text
70 52 49 57 45 54 2C 20 4D 49 52 21
 p  R  I  W  E  T  ,     M  I  R  !
```

`pRIWET, MIR!` is imperfect but recognizable to a reader familiar with the convention.

#### Windows-1251

```text
П   р   и   в   е   т   ,   SP  м   и   р   !
CF  F0  E8  E2  E5  F2  2C  20  EC  E8  F0  21
```

#### CP866

```text
П   р   и   в   е   т   ,   SP  м   и   р   !
8F  E0  A8  A2  A5  E2  2C  20  AC  A8  E0  21
```

#### UTF-8

```text
П       р       и       в       е       т       ,  SP  м       и       р       !
D0 9F   D1 80   D0 B8   D0 B2   D0 B5   D1 82   2C 20  D0 BC   D0 B8   D1 80   21
```

Consequences:

- KOI8-R, CP866, and Windows-1251 require one byte per Russian letter.
- UTF-8 requires two bytes for each character in the basic Cyrillic block but permits all Unicode scripts in one encoding.
- ASCII punctuation is byte-identical in all four.
- None of the three legacy byte strings identifies itself.

### Example B: Ukrainian “Ґанок і їжа”

```text
Characters: Ґ   а   н   о   к  SP  і  SP  ї   ж   а
Unicode:    0490 0430 043D 043E 043A 0020 0456 0020 0457 0436 0430
KOI8-U:     BD   C1   CE   CF   CB   20   A6   20   A7   D6   C1
UTF-8:      D2 90 D0 B0 D0 BD D0 BE D0 BA 20 D1 96 20 D1 97 D0 B6 D0 B0
```

KOI8-R cannot encode `Ґ`, `і`, or `ї`. Substitution with visually similar Latin `I/i` was historically practiced for some missing letters, but this destroys script identity and round-trip fidelity.

### Example C: Four-way Russian mojibake

Take the KOI8-R bytes for `Привет`:

```text
F0 D2 C9 D7 C5 D4
```

Interpreting those bytes under the wrong tables produces approximately:

| Decoder incorrectly chosen | Display |
|---|---|
| KOI8-R, correct | Привет |
| Windows-1251 | рТЙЧЕФ |
| CP866 | ≡╥╔╫┼╘ |
| ISO-8859-5 | рвЩзхд |

Exact glyph appearance can vary with browser mappings, fonts, and whether C1 positions are displayed. The important fact is that conversion is deterministic: “garbage” has a recoverable algebra when the original bytes have not been re-encoded repeatedly.

---

## 3. Origins

## 3.1 Telegraph ancestry

**[DOCUMENT]** Five-bit telegraph codes had only 32 bit patterns and therefore used shift states. Émile Baudot’s nineteenth-century code and Donald Murray’s early twentieth-century keyboard-oriented revision were ancestors of CCITT International Telegraph Alphabet No. 2, standardized in 1932.

**[RECONSTRUCTION]** The Soviet MTK-2 adaptation added a Cyrillic state to figures and Latin states. Since the physical code positions were scarce, Cyrillic characters were associated with Latin positions by phonetic or conventional equivalence. That correspondence—rather than Cyrillic alphabetic order—was inherited by KOI-7 and KOI-8.

**[CAUTION]** Calling KOI8 “Baudot extended to eight bits” is too simple. Baudot/Murray/ITA2 supplied the culture of shift-state telegraphy and correspondence tables; KOI-7’s immediate framework was the seven-bit interchange-code generation represented by ISO 646/ASCII.

## 3.2 ASCII, ISO 646, and national substitution

**[STANDARD]** ASA X3.4-1963 established the American seven-bit code later called ASCII. A revised ASCII appeared in 1967/1968. ECMA Technical Committee 1 published the first ECMA-6 in 1965, and ISO 646 followed as the international seven-bit framework in 1973.

**[RECONSTRUCTION]** ISO 646 deliberately permitted national replacement of a small number of graphic positions. That was adequate for modest Latin-script additions but not for two complete alphabets with case. Cyrillic systems therefore used:

1. replacement of a Latin alphabet by Cyrillic in seven bits;
2. terminal shift states;
3. eight-bit codes placing Latin below and Cyrillic above;
4. later, multibyte or universal codes.

**[DOCUMENT]** Charles E. Mackenzie’s *Coded Character Sets: History and Development* (1980) remains an important reconstruction of the ASCII/EBCDIC standards process and of the six-, seven-, and eight-bit debate. It is not a detailed Soviet KOI history; using it as direct authority for KOI’s authorship would exceed its evidence.

## 3.3 KOI-7 and GOST 19768-74

**[STANDARD]** GOST 19768-74, “Eight-bit codes for information interchange and processing,” standardized Soviet seven- and eight-bit arrangements in 1974 and took effect during the following standardization cycle.

**[RECONSTRUCTION]** KOI-7 placed uppercase Cyrillic at positions corresponding to Latin letters. Repertoire-switching permitted Latin and Cyrillic use on constrained terminals. The shortage of positions explains omissions and compromises:

- no complete independent uppercase/lowercase Cyrillic pair in a single seven-bit graphic set;
- Ё was frequently omitted or treated as Е, reflecting ordinary Russian practice as well as code-space pressure;
- one end position conflicted with DEL, contributing to the treatment or omission of uppercase Ъ in old arrangements;
- punctuation and national substitutions varied among profiles.

**[OPEN CREDIT QUESTION]** The located public copy of GOST 19768-74 specifies the code but does not give a plainly attributable individual designer equivalent to “Andrey Chernov designed KOI8-R.” No reliable primary source located here identifies a single inventor of KOI-7 or old KOI-8. Attribution should remain institutional: Soviet state standardization bodies and their contributing technical organizations.

## 3.4 Old KOI-8

**[STANDARD/RECONSTRUCTION]** Old KOI-8 combined an ISO-646-like Latin half with a Cyrillic upper half whose positions preserved KOI correspondence. It thereby allowed both scripts without maintaining a shift state.

The literal GOST form was not identical to RFC 1489:

- the currency sign versus dollar position differed in surviving descriptions;
- Ё/ё and full case coverage were incomplete or varied;
- upper-half control and graphic assignments were not the later KOI8-R pseudographic repertoire.

The “KOI8 trick” belongs at least to this 1974 layer.

## 3.5 DKOI and IBM influence

**[DOCUMENT]** GOST 19768-74 also concerned ДКОИ, a processing/interchange code shaped by the IBM mainframe environment. Soviet and CMEA machines copied, emulated, or interoperated with IBM and DEC designs, leading to both ASCII-family and EBCDIC-family encodings.

**[RECONSTRUCTION]** DKOI should not be conflated with Internet KOI8-R. It belonged to a mainframe-oriented code family and could merge visually identical Latin and Cyrillic letters in some variants. This saved positions but made linguistic identity ambiguous.

**[FOLKLORE]** General ASCII histories contain stories that EBCDIC existed because IBM needed to defend its “eight-bit” investment or that System/360’s eighth bit was “unused ASCII space.” These are not KOI-specific design evidence. Mackenzie documents genuine commercial and architectural constraints, but simple one-line motives erase the relationship between card codes, BCDIC, PTTC, printer repertoires, and System/360 compatibility.

## 3.6 ECMA-113, ISO-IR-111, and the 1987 break

**[STANDARD]** ISO-IR-111 was registered in 1985. The first edition of ECMA-113, June 1986, created an eight-bit Latin/Cyrillic set based on the 1974 GOST arrangement, adding Belarusian, Ukrainian, Serbian, and Macedonian letters in available positions.

**[STANDARD]** ECMA’s own historical foreword says:

- the first edition was based on GOST 19768-74;
- GOST was revised in 1987;
- ECMA-113 second edition, June 1988, was prepared with Russian experts to agree with that revision;
- ISO/IEC 8859-5:1988 was technically identical to the second edition;
- ECMA-113 third edition, 1999, is technically identical to ISO/IEC 8859-5:1999.

[ECMA-113 editions and foreword](https://ecma-international.org/publications-and-standards/standards/ecma-113/)

**[DISPUTED/NAMING CONFUSION]** “ECMA Cyrillic,” `ISO-IR-111`, and `ISO-8859-5` are sometimes treated as synonyms. Historically that is wrong:

- ISO-IR-111 / first ECMA-113 followed KOI order.
- Revised ECMA-113 / ISO-8859-5 followed the revised, alphabetically arranged scheme.
- RFC 1345 and subsequent registries inherited aliases that can obscure the break.

This confusion is documented in later charset-registry discussions and reconstructed carefully by Czyborra.

## 3.7 Demos, RELCOM, and KOI8-R

**[RECONSTRUCTION]** Roman Czyborra reports that Demos, while porting Cyrillic support to PC Unix/Xenix in the late 1980s, developed the repertoire that became KOI8-R: Russian letters and Ё/ё combined with block and box graphics derived from PC terminal practice.

**[STANDARD]** By July 1993, RFC 1489 said that KOI8-R already had a “very large user community,” including RELCOM, and was factually the de facto code for Unix and global networking in the former USSR. That wording demonstrates that RFC 1489 registered an established practice rather than creating it on publication day.

**[DISPUTED CREDIT]** Andrey Aleksandrovich Chernov is properly credited as:

- RFC 1489’s author;
- a RELCOM/Demos engineer;
- the person who registered and fixed the published Internet definition;
- a major implementer and promoter of KOI8-R.

The stronger claim that he alone invented every byte assignment is not stated in RFC 1489. The best reconstruction assigns the immediate code-page work to the Demos milieu and the registration/stabilization to Chernov. No located Demos design memo supplies a complete authorship roster.

## 3.8 MIME pressure

**[STANDARD]** RFC 1341, the first MIME specification in 1992, listed standardized character sets and gave ISO-8859 families privileged visibility. RFC 1345, also 1992, catalogued a large number of character sets and mnemonics.

**[RECONSTRUCTION]** The divergence between officially favored ISO-8859-5 and actual RELCOM/Unix KOI use created a practical registration problem. RFC 1489 solved the naming problem: mail could say:

```text
Content-Type: text/plain; charset=koi8-r
Content-Transfer-Encoding: 8bit
```

or use quoted-printable/base64 where the transport was not eight-bit clean.

**[STANDARD]** RFC 2046 later formalized that non-ASCII text must identify its charset and that eight-bit bodies may require a content-transfer encoding over seven-bit mail transports. [RFC 2046](https://www.rfc-editor.org/rfc/rfc2046.html)

---

## 4. Adoption and decline

## 4.1 Soviet machines and terminals

**[RECONSTRUCTION]** KOI variants appeared on Soviet and CMEA minicomputers, mainframes, teletypes, punched-tape equipment, and terminals. DEC-compatible systems such as the SM EVM/DVK world and Unix-derived Soviet systems often had keyboard or display modes for Latin and Cyrillic. Precise byte semantics depended on terminal ROM, operating system, and GOST revision.

The encoding’s structure suited these systems:

- ASCII program text remained unchanged;
- Russian text needed one byte per letter;
- fixed-width terminal cells needed no shaping engine;
- bit-mapped font ROMs could replace or supplement Latin glyphs;
- line drawing supported menus and tables.

**[CAUTION]** Assertions that a named Soviet terminal used “KOI8” require its manual or character-ROM dump. Modern photographs showing Cyrillic do not by themselves distinguish KOI-7 shifting, old KOI-8, DKOI, or a vendor table.

## 4.2 Unix, DEMOS, and RELCOM

**[STANDARD]** RFC 1489’s evidence is direct: by 1993 KOI8-R was used by RELCOM and was the de facto encoding for Unix and global-network applications across the former USSR.

Typical deployment included:

- terminal fonts and X11 fonts labeled `koi8-r`;
- Unix locales such as `ru_RU.KOI8-R`;
- mail and Usenet;
- RELCOM newsgroups;
- text editors and conversion utilities;
- web pages served with `charset=koi8-r`;
- FreeBSD and other Unix-like systems.

**[DOCUMENT]** X11 font documentation retained registry names such as `koi8-r` and `koi8-e`; Linux continues to ship a `koi8-r(7)` manual page describing the table. [Linux `koi8-r(7)`](https://www.man7.org/linux/man-pages/man7/koi8-r.7.html)

## 4.3 DOS and CP866

**[DOCUMENT]** The principal DOS rival was the “Alternative” Cyrillic code page, standardized by IBM/Microsoft as CP866. A Soviet research group—V. M. Bryabrin, I. Ya. Landau, and M. E. Nemenman—is credited in the 1986 journal article “On a coding system for personal computers” with the alternative arrangement developed in the Academy of Sciences computing environment.

CP866’s design goals differed from KOI8-R:

- Cyrillic is largely in native alphabetic order.
- Much of CP437’s box drawing survives at the same byte positions.
- This allowed Western DOS applications’ borders and panels to remain intact.
- Lowercase Cyrillic is split around the pseudographic region, complicating range tests.

IBM documentation currently identifies 866 as “MS-DOS Russian” or “PC data: Cyrillic, Russia.” [IBM code-page documentation](https://www.ibm.com/docs/en/cics-tg-zos/10.1.0?topic=reference-code-pages)

**[RECONSTRUCTION]** CP866 was natural for local DOS files and console applications. KOI8-R was natural for Unix and network mail. Moving files between those environments without conversion was one major source of mojibake.

## 4.4 Windows-1251

**[DOCUMENT]** Windows-1251 preserved ASCII below `80`, placed the 64 basic Russian Cyrillic letters contiguously in alphabetic order at `C0–FF`, and used `80–BF` for punctuation and additional Cyrillic letters.

Advantages over KOI8-R included:

- simple alphabetic ranges for Russian;
- Serbian, Macedonian, Ukrainian, and Belarusian letters;
- typographic punctuation useful in GUI documents.

It sacrificed KOI8’s seven-bit transliteration and its dense box-graphics repertoire.

The Unicode Consortium preserves Microsoft’s 15 April 1998 CP1251-to-Unicode mapping, with Shawn Steele as contact. [Microsoft CP1251 mapping](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP1251.TXT)

**[RECONSTRUCTION]** With Windows becoming the dominant Russian desktop platform, Windows-1251 became a common encoding for word-processing files and Web authoring. Web servers, Unix mail, and Windows clients thereby maintained two large ecosystems in parallel.

## 4.5 ISO 8859-5

**[STANDARD]** ISO/IEC 8859-5:1988, superseded by the 1999 second edition, defines a 191-character Latin/Cyrillic graphic set. The ISO catalogue says the 1999 edition covers typical office use in Belarusian, Bulgarian, English, Macedonian, Russian, Serbian, and Ukrainian, but notes that two then-recent Ukrainian letters are absent. It remains a published, confirmed standard. [ISO/IEC 8859-5:1999](https://www.iso.org/standard/28249.html)

**[RECONSTRUCTION]** ISO-8859-5 had standards legitimacy and alphabetic ordering but never displaced KOI8-R on Russian Unix/network systems or CP866/Windows-1251 on Microsoft platforms. Reasons included installed bases, missing or inconvenient national letters, lack of box graphics, and the cost of converting existing software and fonts.

“Never used” is too strong. It appeared in standards, Unix locales, MIME, libraries, and some data. “Never became the dominant Russian Internet code” is supportable.

## 4.6 Macintosh Cyrillic

**[DOCUMENT]** Apple’s Mac Cyrillic encoding was another ASCII-compatible single-byte table, with Apple-specific typographic punctuation and Cyrillic assignments. It was used on classic Mac OS and was incompatible byte-for-byte with KOI8-R, CP866, Windows-1251, and ISO-8859-5. Apple’s historical mappings are preserved by Unicode. [Unicode Apple mappings directory](https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/)

Its market share was smaller, but its presence turns the conventional “four Cyrillic encodings” story into five or more whenever Macintosh and regional variants are counted.

## 4.7 The 1990s “Cyrillic charset soup”

**[DOCUMENT/RECONSTRUCTION]** By 1998 Roman Czyborra described a “Cyrillic Charset Soup” consisting of:

- old and new GOST forms;
- KOI8-R and KOI8-U;
- ISO-IR-111;
- ISO-8859-5;
- DOS alternative/CP866;
- Windows-1251;
- Macintosh Cyrillic;
- Bulgarian, Serbian, Ukrainian, Belarusian, and vendor variants.

This account appeared online by 1998 and was announced to Unicode, IETF charset, Mozilla, and standards mailing lists on 15 June 1998. It is a contemporary technical synthesis rather than a later Wikipedia invention. [Announcement](https://data.iana.org/archive/ietf-charsets/msg00575.html), [Cyrillic Charset Soup](https://www.czyborra.com/charsets/cyrillic.html)

### “Krakozyabry”

**[DOCUMENT/FOLKLORE]** Russian speakers called unreadable encoding debris *кракозябры* or *крокозябры*, roughly “weird squiggle-creatures.” The spelling and etymology vary. It is the Russian counterpart of Japanese *mojibake*.

The four most important transformations were commonly:

```text
KOI8-R ↔ Windows-1251
KOI8-R ↔ CP866
Windows-1251 ↔ CP866
any of these ↔ ISO-8859-5
```

Mac Cyrillic, accidental Western decoding, and repeated conversion added more.

“Four-way mojibake” is a useful cultural shorthand, not a formally bounded technical classification.

### Recovery

**[RECONSTRUCTION]** If bytes were merely decoded using the wrong table, recovery is exact:

1. encode the displayed wrong characters back through the wrongly chosen encoding;
2. decode those bytes with the original encoding.

If the display was copied through a lossy path, unsupported characters became `?`, or conversion happened more than once, recovery may require language statistics. Russian-specific “universal decoders” used letter-frequency and bigram scoring to select among KOI8-R, CP866, CP1251, and ISO-8859-5.

## 4.8 Unicode resolution

**[STANDARD]** Unicode began in 1987–1988 through work by Joe Becker of Xerox and Lee Collins and Mark Davis of Apple. Unicode, Inc. was incorporated on 3 January 1991. The first officers included Davis, Mike Kernaghan, Becker, Ken Whistler, and Bill English. [Unicode history](https://www.unicode.org/history/), [summary narrative](https://www.unicode.org/history/summary.html)

**[STANDARD]** Unicode’s Cyrillic block was based principally on ISO/IEC 8859-5, not on KOI8 byte order. Modern Unicode has extended blocks for historical and minority-language Cyrillic, combining marks, and phonetic modifiers. [Unicode Cyrillic chapter](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-7/)

Unicode did not choose one legacy byte table as the universal byte encoding. It assigned abstract code points:

```text
А U+0410
а U+0430
Ё U+0401
ё U+0451
Ґ U+0490
ґ U+0491
```

Legacy tables became conversion mappings.

## 4.9 UTF-8 and decline

**[STANDARD]** UTF-8 was devised by Ken Thompson and Rob Pike in 1992 and documented for Internet use by RFC 2044 in 1996, RFC 2279 in 1998, and RFC 3629 in 2003. It preserves ASCII bytes and encodes Cyrillic with two-byte sequences.

**[RECOLLECTION]** Pike’s history says Thompson designed the encoding during a New Jersey diner discussion, writing it on a placemat, after which Pike and Thompson implemented it in Plan 9. This is a participant account and the placemat story essentially rests on that small witness circle; no independently archived placemat has been produced. The algorithm and rapid Plan 9 implementation are well documented, but the physical anecdote should remain labeled recollection.

**[STANDARD]** RFC 2277, the IETF character-set policy, requires protocols to identify encodings and says they must be able to use UTF-8. RFC 5198 defines a normalized UTF-8 “Net-Unicode” format with CRLF line endings and prohibits an initial BOM in that profile. [RFC 2277](https://www.rfc-editor.org/rfc/rfc2277.html), [RFC 5198](https://www.rfc-editor.org/rfc/rfc5198.html)

**[MODERN]** WHATWG retains KOI8 decoders only for deployed content and mandates UTF-8 for new web formats. As measured on 11 September 2026, W3Techs reports UTF-8 on 99.1% of websites whose encoding it can identify. This is a web survey, not a measurement of private archives, mailboxes, filenames, or embedded systems. [W3Techs UTF-8 statistics](https://w3techs.com/technologies/breakdown/en-utf8/ranking)

## 4.10 What survives

**[MODERN]**

- IANA names and MIBenum identifiers.
- Browser decoders.
- `iconv`, ICU, language runtimes, mail readers, and archive tools.
- Unix locale and manual-page compatibility.
- Old Usenet, email, FTP, web, BBS, FidoNet, and source archives.
- Filenames stored without reliable charset metadata.
- Database fields and backup media.
- Fonts and terminal emulators.
- Converter folklore and the vocabulary of *krakozyabry*.
- Box-drawing aesthetics in preserved text-mode material.
- The general lesson that “byte,” “character,” and “glyph” are not synonyms.

---

## 5. The other scripts

KOI8-R itself does not “handle” other scripts; one must change encodings, transliterate, or use Unicode.

## 5.1 Other Cyrillic languages

### Ukrainian

KOI8-U added four necessary pairs. Its 1992/1995 evolution reflects orthographic politics: Ґ had been suppressed under Soviet policy and was restored to the Ukrainian alphabet in 1990. RFC 2319 explicitly records the 1995 code-page addition.

### Belarusian

KOI8-R lacks Ў/ў and a distinct Cyrillic І/і. KOI8-RU added Ў/ў alongside the Ukrainian additions. Earlier systems often reused Latin `I`, a visually plausible but semantically lossy substitution.

### Serbian and Macedonian

KOI8-R lacks their distinctive letters. ISO-IR-111 and Windows-1251 supplied wider South-Slavic repertoires. Vendor and national KOI variants also existed, but none acquired KOI8-R’s broad Internet identity.

### Bulgarian

Modern Bulgarian can be represented by KOI8-R’s character inventory. Bulgarian typography may require locally appropriate glyph forms, particularly in lowercase italic and upright styles, but Unicode character encoding normally treats those as font/language presentation, not different abstract letters.

### Central Asian, Caucasian, and minority Cyrillic

KOI8-R’s 128-byte upper half has no room for the many letters used in Kazakh, Kyrgyz, Tajik, Tatar, Bashkir, Mongolian Cyrillic, Abkhaz, Chechen, and other orthographies. KOI8-T, local code pages, modified fonts, and later national standards supplied partial solutions. Unicode ultimately encoded these as a larger Cyrillic repertoire.

## 5.2 Greek

ISO 8859-7 and vendor Greek pages performed the same broad job for Greek that Cyrillic code pages performed for Russian: ASCII below, national graphics above. KOI8-R cannot mix Greek and Russian except by transliteration or an external repertoire switch.

## 5.3 Hebrew and Arabic

**[STANDARD]** ISO 8859-8 encoded Hebrew letters; ISO 8859-6 encoded Arabic. Encoding letters was not enough to settle ordering and shaping:

- Hebrew and Arabic run right-to-left while numbers and embedded Latin run left-to-right.
- Early data could be stored in visual display order or logical reading order.
- RFC 2046 notes that the raw ISO-8859-6 and -8 repertoires did not by themselves define a canonical bidirectional representation and distinguishes MIME profiles.
- Arabic glyphs change with joining context; vendor encodings sometimes stored presentation forms rather than abstract letters.

Unicode separated abstract character identity from the Unicode Bidirectional Algorithm and shaping behavior, while retaining compatibility characters for round trips with legacy standards.

## 5.4 Indic scripts

Devanagari and related scripts use combining vowels, conjuncts, reordering, and contextual shaping. A KOI8-like one-byte table could cover only a severely constrained subset or would need font-specific hacks. ISCII used common code positions and script selection; Unicode encoded scripts separately and left cluster shaping to rendering systems.

Unicode’s own chronology records that in December 1990 its South Asian subcommittee chose logical order, added length marks, and incorporated feedback from H. M. Ross. That is institutional history, not proof that all Indic communities accepted every decision without controversy. [Unicode Version 1 chronology](https://www.unicode.org/history/versionone.html)

## 5.5 Chinese, Japanese, and Korean

Thousands of ideographs could not fit in an eight-bit single-byte code. National solutions included:

- JIS X 0208 and Shift_JIS/EUC-JP;
- GB 2312, GBK, and GB18030;
- Big5;
- KS X 1001, EUC-KR, and vendor extensions;
- ISO 2022 escape-state encodings.

These systems used double-byte zones, variable-width encodings, escape designation, or much larger coded spaces.

Unicode/ISO 10646 unified many Chinese-origin characters across Chinese, Japanese, Korean, and historical Vietnamese sources when they were judged to be the same abstract Han character. Regional glyph differences were generally delegated to fonts and language tagging.

## 5.6 Emoji

KOI8-R has no emoji. At most it can make emoticons from ASCII punctuation or pictures from block characters.

Emoji entered Unicode through proposals based substantially on Japanese mobile-carrier repertoires. Modern emoji presentation depends on variation selectors, standardized sequences, skin-tone modifiers, zero-width joiners, and properties beyond a simple code table. Encoding approval is governed through the Unicode Technical Committee and proposal process, not a popular vote in the literal sense.

---

## 6. People and institutions

## 6.1 Directly relevant to KOI

### Andrey Aleksandrovich Chernov, 1966–2017

**[DOCUMENT]** Russian programmer, Demos/RELCOM contributor, FreeBSD developer, author of RFC 1489. RFC 1489 lists him as “Andrew A. Chernov,” RELCOM Development Team, Moscow.

**[RECONSTRUCTION]** His central achievement was standardizing an already deployed Russian Unix/network code page sufficiently for MIME and interoperable software. Later biographical accounts often compress “author of the registration” into “inventor of KOI8-R.”

### Igor Sviridov and Stas Vorony

**[STANDARD]** Named by RFC 2319 as presenters of the KOI8-U proposal adopted by Ukrainian ISP postmasters in Slavsk in autumn 1992: Sviridov from Kyiv, Vorony from Kharkiv.

### KOI8-U Working Group

**[STANDARD]** Collective author of RFC 2319. The document’s group authorship is itself evidence against assigning KOI8-U to a single inventor.

### V. M. Bryabrin, I. Ya. Landau, M. E. Nemenman

**[DOCUMENT]** Authors associated with the Soviet “Alternative” PC encoding that became the basis of CP866, published in *Mikroprotsessornye sredstva i sistemy* in 1986.

### Roman Czyborra

**[DOCUMENT]** Author of the 1998 “Cyrillic Charset Soup,” an influential near-contemporary reconstruction. His work is technically detailed and openly “slightly opinionated,” as his mailing-list announcement states; it should be checked against standards for normative claims.

## 6.2 Telegraph and early interchange background

- **Émile Baudot, 1845–1903:** devised a five-unit telegraph code.
- **Donald Murray, 1865–1945:** developed a keyboard and paper-tape-oriented revision that influenced teleprinter codes.
- **Herman Hollerith, 1860–1929:** punched-card systems influenced later commercial data-processing codes.
- **CCITT:** standardized international telegraph alphabets, including ITA2 in 1932.
- **ASA/ANSI X3.4:** produced and revised ASCII.
- **ECMA TC1:** developed ECMA-6, ECMA-35, ECMA-113, and related coded-character standards.
- **ISO/IEC JTC 1/SC 2:** maintained ISO 646, ISO 2022, ISO 8859, and ISO/IEC 10646 work.
- **IBM:** EBCDIC, DOS code-page registration, mainframe and PC conversion tables.
- **DEC:** terminal/minicomputer influence, especially significant for Soviet compatible hardware.
- **Bell Labs:** Unix, Plan 9, and the institutional setting for UTF-8’s invention.

## 6.3 ASCII historians and designers

**[DOCUMENT/RECONSTRUCTION]**

- Bob Bemer was a major advocate and participant in ASCII standardization and later publicized its history.
- Hugh McGregor Ross and others participated in international standardization.
- Charles E. Mackenzie documented ASCII and EBCDIC’s committee and corporate development in 1980.

**[CAUTION]** Popular histories sometimes call Bemer “the inventor of ASCII.” ASCII was a committee product. Bemer made major proposals and advocacy contributions, but sole-inventor language is disputed by the documentary record.

## 6.4 Unicode and UTF-8

**[STANDARD/INSTITUTIONAL HISTORY]**

- Joe Becker, Xerox: coined “Unicode” in the documented 1987–1988 period and wrote *Unicode 88*.
- Lee Collins, Apple: early architecture and Han database work.
- Mark Davis, Apple: co-founder and first Consortium president.
- Ken Whistler, Metaphor/Sybase: database, editorial, property, and standards work; first secretary.
- Mike Kernaghan: first vice-president and organizational work.
- Bill English: first treasurer.
- Karen Smith-Yoshimura and Joan Aliprand, Research Libraries Group: bibliographic and CJK contributions.
- Asmus Freytag and Michel Suignard, Microsoft: mappings, bidirectional and standards work.
- Ken Thompson and Rob Pike, Bell Labs: UTF-8 design and implementation.

The Unicode Consortium’s own history is an institutional source and participant-curated record. It is indispensable but not disinterested external historiography.

---

## 7. Culture

## 7.1 “Plain text”

KOI8-R illustrates that “plain text” is never merely an unqualified byte stream. The bytes need at least:

- an encoding identity;
- a line-ending convention;
- a font with the intended glyphs;
- often a language;
- sometimes normalization, directionality, and shaping rules.

ASCII’s apparent plainness came from widespread agreement on defaults. Russian computing exposed those defaults because an English-readable lower half coexisted with several incompatible upper halves.

Unicode’s “plain text” ideal moved agreement from 256-entry local tables to universal code points, but fonts, normalization, grapheme boundaries, bidirectionality, and emoji sequences remain interpretive layers.

## 7.2 Pseudographics and terminal culture

KOI8-R dedicates 61 of its upper-half positions to box drawing, blocks, shading, mathematics, or symbols. This made it useful for:

- full-screen terminal interfaces;
- borders and tables;
- status panels;
- BBS screens;
- text-mode diagrams;
- primitive visual art.

**[RECONSTRUCTION]** These assignments connect KOI8-R culturally to CP437/CP866 text mode, although their byte layouts differ. The repertoire reflects an era when a “character set” was also a practical graphics palette.

**[CAUTION]** ASCII art, ANSI art, and the demoscene overlap but are not synonymous:

- strict ASCII art uses the ASCII repertoire;
- ANSI art normally adds terminal color/control sequences and often CP437-style block characters;
- KOI8 art can use its own pseudographics;
- demoscene art is a social and technical practice spanning many platforms and encodings.

Evidence for a distinct, large “KOI8 art movement” is thin. It is safer to say that KOI8-R’s pseudographics enabled text-mode visual practices in the same technological ecology.

## 7.3 Mojibake as vernacular

*Krakozyabry* became a cultural shorthand for post-Soviet computing’s interoperability failures. It appeared in troubleshooting guides, jokes, converter sites, browser menus, and visual memories of the 1990s Runet.

**[FOLKLORE/MODERN INVENTION]** Contemporary retro sites often reproduce canonical mangled strings as if one form were universal. In reality the result depends on:

- source code page;
- mistaken destination code page;
- font;
- C1-control handling;
- browser recovery rules;
- whether bytes were re-encoded after the first mistake.

Thus a screenshot may be culturally authentic without proving the claimed exact conversion path.

## 7.4 Code-page identity

Choosing an encoding could signal platform and community:

| Encoding | Typical association |
|---|---|
| KOI8-R | Unix, RELCOM, mail, Usenet, early Runet |
| CP866 | DOS, console programs, BBS software |
| Windows-1251 | Windows desktop and authored web pages |
| ISO-8859-5 | Formal international standards and some Unix/MIME use |
| Mac Cyrillic | Classic Macintosh |
| KOI8-U | Ukrainian Internet community |

These were tendencies, not hard boundaries. Gateways and converters made mixed environments routine.

## 7.5 Encoding as politics

A code table distributes scarce positions. KOI8-R privileged:

- Russian over other Cyrillic languages;
- modern Russian over historical orthography;
- terminal graphics over Ukrainian or Serbian letters;
- compatibility with ASCII correspondence over native collation.

These are observable design effects. They do not by themselves prove hostile intent. KOI8-U’s replacement of decorative graphics with restored Ukrainian letters is an unusually clear example of technical allocation tracking linguistic and political change.

Unicode changed the scarcity model but not the institutional question. Scripts require documentation, proposals, review, names, properties, and implementers. Communities with archival access and standards expertise can navigate that process more easily than poorly documented or marginalized traditions.

---

## 8. Controversies and disputes

## 8.1 Who invented KOI8-R?

**Documented minimum:** Chernov authored RFC 1489 in 1993 and registered the table on behalf of a deployed RELCOM/Unix community.

**Historical reconstruction:** The immediate repertoire was developed in Demos’s late-1980s Unix localization work.

**Earlier layer:** The high-bit correspondence was already fundamental to 1974 KOI-8.

**Unsupported simplification:** Chernov invented KOI8 and its seven-bit-survival trick from scratch in 1993.

No located primary Demos memo settles every byte’s individual authorship.

## 8.2 Was bit-stripping the reason for the layout?

**Documented effect:** Clearing bit 7 produces a rough Latin rendering.

**Strong historical inference:** The systematic positional correspondence is deliberate and predates KOI8-R.

**Open question:** The public GOST materials located do not expose committee minutes stating precisely which designers selected each equivalence or ranking their motives—telegraph continuity, seven-bit survivability, hardware simplicity, or all three.

## 8.3 ISO-IR-111 versus ISO-8859-5

This is a genuine documentary trap. The first ECMA-113 was KOI-related; its successor was deliberately changed after the 1987 GOST revision and became ISO-8859-5. Later aliases and summaries collapse them. ECMA’s foreword is the strongest readily accessible evidence for the chronology.

## 8.4 Russian versus Ukrainian and Belarusian requirements

KOI8-R’s name correctly says “R”: it is Russian, not universal Cyrillic. Treating Latin `I` as Ukrainian/Belarusian І or omitting Ґ may display acceptably in some fonts but is not lossless character encoding.

KOI8-U’s history also warns against timeless repertoire claims. The 1992 proposal was completed in 1995 after Ґ’s restoration and practical demand made the omission untenable.

## 8.5 Bulgarian and Serbian variants

Bulgarian requires Russian-compatible characters but often different preferred glyph forms. Serbian requires distinct letters. A font-only “Serbian KOI8” that repurposes Russian positions may render desired text locally but destroys semantic interoperability. Vendor tables bearing similar names need byte-level identification.

## 8.6 Han unification

This is not a KOI design controversy, but it illuminates the universal-code solution that replaced code pages.

**[STANDARD/INSTITUTIONAL HISTORY]** Unicode’s records trace Han-unification database work to Xerox and Apple in 1986–1988, especially Lee Collins, with Research Libraries Group data and later national-standard mappings.

**[CONTROVERSY]** Japanese critics argued that unifying Chinese, Japanese, and Korean forms under one code point ignored culturally meaningful glyph distinctions or privileged Chinese source forms. Supporters answered that the encoded unit was an abstract character and that language-sensitive fonts should supply regional glyphs.

Both positions describe real layers:

- Unicode does unify many historically related national-standard characters.
- Unicode also preserves distinctions where source standards or round-trip rules require them.
- Fonts and language metadata remain necessary.
- Poor font fallback can display a regionally inappropriate glyph even when the underlying text is semantically correct.

“Unicode stores Chinese characters and merely draws them Japanese” is too crude; “Han unification caused no Japanese objection” is false.

## 8.7 Tibetan and CJK repertoire disputes

**[RECONSTRUCTION]** Tibetan standardization involved competing models for character order, stacks, and legacy data. CJK expansion continually raises evidence questions about glyph variants, source separation, national submissions, and unification. These disputes concern whether a difference is a character distinction or a glyph/style distinction—the same conceptual boundary visible on a smaller scale in Bulgarian Cyrillic.

No evidence was found connecting these controversies directly to KOI8 committees. Their relevance is comparative and belongs to Unicode’s replacement regime.

## 8.8 Emoji and Consortium power

**[DOCUMENT]** Emoji proposals are evaluated through documented criteria and UTC decisions. Vendors and public demand have influenced proposals, but there is no simple plebiscite.

Criticisms include:

- corporate members’ influence;
- uneven representation;
- cultural stereotyping;
- the burden placed on communities to produce evidence;
- permanence once characters are encoded;
- vendor control over final artwork.

Countervailing facts include:

- published proposal procedures;
- public document registers;
- stability requirements;
- multi-vendor interoperability;
- rejection and revision of proposals.

“The Unicode Consortium votes on which peoples exist” is rhetoric, not a literal description. Yet repertoire decisions can determine whether a community’s text works in standard software, so the political stakes are real.

## 8.9 Encoding and Unicode security

### Wrong-charset attacks

**[STANDARD/MODERN]** WHATWG notes that disagreements about encoding can hide syntax characters. Its example uses a Shift_JIS lead byte to mask a quotation mark from one parser. Similar parser differentials can occur whenever security filters and consumers decode bytes differently.

KOI8-R has no multibyte masking state, but an attacker can still exploit:

- a server and browser choosing different charsets;
- Unicode conversion before versus after filtering;
- visually similar Cyrillic and Latin letters;
- filename decoding discrepancies.

### Homoglyphs

Cyrillic `а`, `е`, `о`, `р`, `с`, `у`, and `х` can resemble Latin letters. KOI’s entire correspondence idea makes that resemblance vivid. Unicode preserves the scripts as distinct characters, which is linguistically correct but enables lookalike identifiers such as mixed-script domain names.

Unicode Technical Standard #39 defines confusable “skeleton” mappings and script-restriction mechanisms, while acknowledging that confusability depends on fonts and cannot be eliminated completely. [UTS #39](https://www.unicode.org/reports/tr39/)

### Overlong UTF-8

**[STANDARD]** Early or defective decoders accepted non-shortest encodings such as `C0 80` for NUL. A filter might reject an ordinary NUL while a later decoder reconstructed one. RFC 3629 requires rejection of invalid sequences and discusses their security consequences. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html)

KOI8-R has no overlong sequences because every character is one byte. It also lacks UTF-8’s structural invalidity checks.

### BOM

KOI8-R has no BOM. UTF-16’s endianness made U+FEFF useful as a signature, while UTF-8 needs no byte-order indicator. A UTF-8 BOM can create problems in shell scripts, protocol headers, and concatenated text. RFC 5198 forbids it in Net-Unicode strings.

### Normalization

KOI8-R generally provides one representation for each covered Russian letter and no combining marks, avoiding canonical-equivalence ambiguity within its small repertoire. Unicode’s greater expressiveness permits composed and decomposed sequences; RFC 5198 recommends NFC for interchange and warns that filters must not assume input is normalized.

## 8.10 The “sixteen-bit Unicode” assumption

**[STANDARD/INSTITUTIONAL HISTORY]** Unicode was initially promoted as a fixed-width 16-bit encoding for more than 60,000 graphic characters. Unicode’s own history quotes that original purpose.

CJK growth and additional scripts exceeded that model. UTF-16 introduced surrogate pairs; UTF-8 and UTF-32 address the full range through different code-unit structures.

**[CONTROVERSY]** Critics correctly note that APIs built around 16-bit “characters” still split supplementary code points. Defenders correctly note that Unicode abstract characters were expanded without breaking existing assigned code points. The early fixed-width processing promise did not survive, while code-point stability largely did.

---

## 9. Open questions and evidentiary limits

1. **Individual authorship of GOST 19768-74:** No accessible primary committee roster or design minutes located here identify the individuals who selected KOI-7/KOI-8 positions.

2. **Exact path from MTK-2 to KOI-7:** The positional resemblance and later technical histories support descent, but a dated Soviet memo explicitly walking through every adopted correspondence remains to be located.

3. **KOI8-R byte-level authorship:** RFC 1489 identifies Chernov as author and RELCOM as his organization; Czyborra identifies late-1980s Demos development. A surviving Demos design memorandum, source-control history, or multi-participant oral history would sharpen credit.

4. **First printed explanation of the bit-stripping trick:** The property exists in the 1974 arrangement. The earliest located explicit online explanation is Czyborra’s 1998 account, with C-Kermit documentation also describing “Short KOI.” An earlier Soviet manual almost certainly may describe the correspondence, but one was not verified here.

5. **Quantitative market shares:** Contemporary claims such as “85% of Soviet PC respondents used the Alternative encoding in 1989” circulate with references to Russian technical literature, but the underlying survey was not independently inspected here. Platform associations are firmer than precise percentages.

6. **First use and etymology of *krakozyabry*:** The term is abundantly attested in later technical vernacular, but no defensible first occurrence or single etymology was found.

7. **Bulgarian and Serbian KOI variants:** Numerous tables were implemented in fonts and local software. Similar names do not guarantee identical mappings. Each artifact needs its own table or ROM dump.

8. **Demoscene claims:** Text-mode graphics and encoding-specific art are documented broadly. Evidence for a coherent, separately organized “KOI8-R art scene” is inadequate; it should not be invented from the presence of pseudographics.

9. **Archived Soviet hardware behavior:** GOST conformance does not prove what a particular machine actually emitted. Manuals, punched media, binaries, and character-generator ROMs remain the best artifact-level sources.

10. **Folklore transmission:** The claim that Chernov invented the high-bit trick appears in many later summaries, but RFC 1489 itself does not say it. Pinning down the first person to attach that older feature specifically to Chernov requires deeper archive work in early Runet pages and newsgroups.

---

## 10. Chronology

| Date | Event | Evidence |
|---|---|---|
| 1870s | Baudot develops five-unit telegraph code | Historical documentation |
| 1901 onward | Murray adapts five-bit telegraph coding for keyboard/paper-tape operation | Historical documentation |
| 1932 | CCITT standardizes ITA2 | Standards history |
| Soviet teleprinter era | MTK-2 uses Latin, Cyrillic, and figures states | Technical reconstruction |
| 1963 | ASA X3.4-1963 ASCII | Standard |
| 1965 | First ECMA-6 | ECMA record |
| 1967–1968 | Revised ASCII; federal adoption era in the United States | Standard and government history |
| 1969 | RFC 20 publishes ASCII format for network interchange | RFC |
| 1973 | First ISO 646 edition | ISO history |
| 1974 | GOST 19768-74 standardizes KOI-7/old KOI-8 and related interchange codes | GOST |
| 1979/1981 | ISO 5427 bibliographic Cyrillic extensions | ISO documentation |
| 1985 | KOI-related multilingual Cyrillic registered as ISO-IR-111 | ISO register |
| June 1986 | ECMA-113 first edition, based on GOST 19768-74 | ECMA |
| 1986 | Soviet “Alternative” PC encoding described in print | Contemporary article |
| 1987 | GOST revision abandons old KOI ordering for a revised arrangement | GOST/ECMA |
| June 1988 | ECMA-113 second edition aligned with revised GOST | ECMA |
| December 1988 | ISO/IEC 8859-5:1988 published | ISO catalogue |
| Late 1980s | Demos Unix work produces the immediate KOI8-R repertoire | Later technical reconstruction |
| 1990 | Ukrainian Ґ restored officially; CP866 standardization era | National/platform history |
| 1990–1991 | Unicode drafts and Consortium incorporation | Unicode records |
| Autumn 1992 | Ukrainian ISP postmasters adopt initial KOI8-U proposal | RFC 2319 |
| September 1992 | Thompson and Pike develop UTF-8 for Plan 9 | Participant account and implementation history |
| July 1993 | RFC 1489 registers KOI8-R | RFC |
| June 1995 | KOI8-U completed with Ґ/ґ | RFC 2319 |
| October 1996 | RFC 2044 publishes UTF-8 for ISO 10646 | RFC |
| November 1996 | MIME RFC 2045/2046 revision | RFC |
| 1998 | RFC 2279 revises UTF-8; RFC 2319 registers KOI8-U; “Cyrillic Charset Soup” published | RFCs/contemporary web |
| January 1999 | ISO/IEC 8859-5:1999 published | ISO |
| 2003 | RFC 3629 restricts UTF-8 to U+10FFFF and excludes overlong/surrogate encodings | RFC |
| 2008 | RFC 5198 defines Net-Unicode | RFC |
| 2010s | UTF-8 becomes overwhelmingly dominant on the public Web | Web surveys |
| 2020s | KOI8 remains in registries and decoders but is a legacy input format | IANA/WHATWG/current libraries |
| September 2026 | W3Techs measures UTF-8 at 99.1% of sites with known encoding | Modern survey |

---

## 11. Findings

The best-supported reconstruction is:

1. KOI8-R is the Internet-era member of a Soviet encoding lineage, not a design created wholly in 1993.

2. Its defining structural idea is the positional correspondence between Cyrillic and ASCII Latin. The famous seven-bit “transliteration” is real, intentionally useful, and inherited from old KOI practice.

3. GOST 19768-74 is the institutional origin of old KOI-7/KOI-8. The individual Soviet designers remain insufficiently documented in accessible sources.

4. Andrey Chernov’s documented role is decisive but narrower than folklore: he authored RFC 1489 and registered/stabilized the Demos/RELCOM code page already used across the Unix-connected former USSR.

5. KOI8-R is technically simple and robust with respect to byte synchronization, but cannot identify itself, detect malformed data, sort Russian correctly by raw byte order, or represent multilingual text.

6. CP866 won the DOS console niche, Windows-1251 the Windows desktop niche, KOI8-R the Unix/mail/early-Runet niche, and ISO-8859-5 the formal-standard niche without becoming dominant.

7. KOI8-U demonstrates how a community could extend KOI8-R by trading pseudographics for nationally necessary letters. Its chronology is unusually well documented in RFC 2319.

8. The 1990s “charset soup” was not random. Each table optimized a different inheritance: telegraph/ASCII correspondence, DOS pseudographics, Windows typography, international standardization, or national repertoire.

9. Unicode resolved the repertoire fragmentation by assigning characters independently of legacy bytes; UTF-8 resolved Internet interchange while retaining ASCII compatibility. It did not erase legacy data or the politics of deciding character identity.

10. KOI8 survives less as a living authoring choice than as an archival obligation, an aesthetic of terminal-era computing, and a compact lesson in how infrastructure embodies linguistic priorities.

---

## 12. Sources consulted

### Primary standards, RFCs, and registries

- GOST 19768-93 scan, including historical relationship to GOST 19768-74:  
  https://files.stroyinf.ru/Data/279/27941.pdf

- GOST 27464-87 catalogue and scan, citing KOI-7 and KOI-8 standards:  
  https://internet-law.ru/gosts/gost/19753/

- RFC 20, *ASCII format for Network Interchange* (1969):  
  https://www.rfc-editor.org/rfc/rfc20.html

- RFC 1341, original MIME specification (1992):  
  https://www.rfc-editor.org/rfc/rfc1341.html

- RFC 1345, *Character Mnemonics and Character Sets* (1992):  
  https://www.rfc-editor.org/rfc/rfc1345.html

- RFC 1489, Andrey Chernov, *Registration of a Cyrillic Character Set* (1993):  
  https://www.rfc-editor.org/rfc/rfc1489.html

- RFC 2044, *UTF-8, a transformation format of Unicode and ISO 10646* (1996):  
  https://www.rfc-editor.org/rfc/rfc2044.html

- RFC 2045, MIME Part One (1996):  
  https://www.rfc-editor.org/rfc/rfc2045.html

- RFC 2046, MIME Part Two (1996):  
  https://www.rfc-editor.org/rfc/rfc2046.html

- RFC 2277, *IETF Policy on Character Sets and Languages* (1998):  
  https://www.rfc-editor.org/rfc/rfc2277.html

- RFC 2279, UTF-8 revision (1998):  
  https://www.rfc-editor.org/rfc/rfc2279.html

- RFC 2319, KOI8-U Working Group, *Ukrainian Character Set KOI8-U* (1998):  
  https://www.rfc-editor.org/rfc/rfc2319.html

- RFC 2781, UTF-16 (2000):  
  https://www.rfc-editor.org/rfc/rfc2781.html

- RFC 2978, IANA charset registration procedures (2000):  
  https://www.rfc-editor.org/rfc/rfc2978.html

- RFC 3629, UTF-8 (2003):  
  https://www.rfc-editor.org/rfc/rfc3629.html

- RFC 5198, *Unicode Format for Network Interchange* (2008):  
  https://www.rfc-editor.org/rfc/rfc5198.html

- IANA Character Sets registry:  
  https://www.iana.org/assignments/character-sets

- IANA non-RFC charset registrations:  
  https://www.iana.org/assignments/charset-reg

- WHATWG Encoding Standard:  
  https://encoding.spec.whatwg.org/

### ECMA and ISO

- ECMA-6, seven-bit coded character set:  
  https://ecma-international.org/publications-and-standards/standards/ecma-6/

- ECMA-35 / ISO 2022 code-extension structure:  
  https://ecma-international.org/publications-and-standards/standards/ecma-35/

- ECMA-113 archive, editions 1–3:  
  https://ecma-international.org/publications-and-standards/standards/ecma-113/

- ECMA-113 third edition PDF and historical foreword:  
  https://www.ecma-international.org/wp-content/uploads/ECMA-113_3rd_edition_december_1999.pdf

- ISO/IEC 8859-5:1988 catalogue:  
  https://www.iso.org/standard/16342.html

- ISO/IEC 8859-5:1999 catalogue and abstract:  
  https://www.iso.org/standard/28249.html

- ISO/IEC 10646:2020 catalogue:  
  https://www.iso.org/standard/76835.html

- ISO/IEC JTC 1/SC 2 catalogue:  
  https://www.iso.org/committee/45050/x/catalogue/

### Authoritative mapping tables and implementation documentation

- Unicode KOI8-R mapping:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MISC/KOI8-R.TXT

- Microsoft CP1251 mapping:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP1251.TXT

- Microsoft/IBM CP866 mapping:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/PC/CP866.TXT

- Apple mapping archive, including Cyrillic and Ukrainian:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/APPLE/

- Microsoft Macintosh mapping archive:  
  https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/MAC/

- Linux `koi8-r(7)` manual:  
  https://www.man7.org/linux/man-pages/man7/koi8-r.7.html

- Linux `koi8-u(7)` manual:  
  https://www.man7.org/linux/man-pages/man7/koi8-u.7.html

- IBM code-page support:  
  https://www.ibm.com/docs/en/txseries/9.1.0?topic=communications-code-page-support

- IBM CCSID values:  
  https://www.ibm.com/docs/en/i/7.4.0?topic=reference-ccsid-values

- IBM code-page reference identifying CP866:  
  https://www.ibm.com/docs/en/cics-tg-zos/10.1.0?topic=reference-code-pages

- IBM code-set documentation identifying the Alternative variant:  
  https://www.ibm.com/docs/en/informix-servers/14.10.0?topic=files-supported-code-set-names-used-by

- X11 font encoding documentation:  
  https://www.x.org/archive/X11R6.8.1/PDF/fonts.pdf

### Unicode history and technical material

- Unicode History Corner:  
  https://www.unicode.org/history/

- Unicode summary narrative:  
  https://www.unicode.org/history/summary.html

- Unicode Version 1 chronology:  
  https://www.unicode.org/history/versionone.html

- Unicode release and publication dates:  
  https://www.unicode.org/history/publicationdates.html

- *Early Years of Unicode*:  
  https://www.unicode.org/history/earlyyears.html

- Ed Hart memo on the ISO/Unicode merger:  
  https://www.unicode.org/history/hartmemo.html

- Unicode 17 Cyrillic chapter:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-7/

- Unicode Technical Reports index:  
  https://www.unicode.org/reports/

- Unicode Technical Report #36, security considerations:  
  https://www.unicode.org/reports/tr36/

- Unicode Technical Standard #39, security mechanisms and confusables:  
  https://www.unicode.org/reports/tr39/

### Historical books and reconstructions

- Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley, 1980, ISBN 0-201-14460-3, Internet Archive record:  
  https://archive.org/details/codedcharacterse00unse

- Open Library bibliographic record for Mackenzie:  
  https://openlibrary.org/books/OL4570655M/Coded_character_sets

- Searchable PDF copy of Mackenzie:  
  https://hcs64.com/files/Mackenzie%20-%20Coded%20Character%20Sets%20History%20and%20Development.pdf

- Roman Czyborra, *The Cyrillic Charset Soup* (1998):  
  https://www.czyborra.com/charsets/cyrillic.html

- Czyborra’s 15 June 1998 charset-soup announcement:  
  https://data.iana.org/archive/ietf-charsets/msg00575.html

- IANA mailing-list discussion of ISO-IR-111 / ECMA-Cyrillic naming:  
  https://data.iana.org/archive/ietf-charsets/msg01352.html

- C-Kermit manual, comparative Cyrillic tables and “Short KOI”:  
  https://www.kermitproject.org/onlinebooks/usingckermit3e.pdf

- Historical KOI8-R reference archive at Lib.ru:  
  https://www.lib.ru/CYRILLIC/koi8.html

### Adoption, culture, and modern use

- W3Techs UTF-8 usage, measured September 2026:  
  https://w3techs.com/technologies/breakdown/en-utf8/ranking

- Galza, Russian BBS/demoscene ASCII-art archive and history:  
  https://galza.org/

- Markku Reunanen, demoscene research discussing text art:  
  https://www.kameli.net/demoresearch2/reunanen-licthesis.pdf

- Media Art History proceedings discussing text-mode art:  
  https://www.mediaarthistory.org/wp-content/uploads/2011/07/ReLive09proceedings.pdf

- Contemporary retro-cultural account of Runet encodings and *krakozyabry*:  
  https://dialup.folkup.city/docs/culture/kodirovki/

### Secondary indexes used to locate primary material

The following were used as indexes or leads, not as substitutes for the standards:

- KOI-8 overview:  
  https://en.wikipedia.org/wiki/KOI-8

- KOI8-R overview:  
  https://en.wikipedia.org/wiki/KOI8-R

- KOI8-U overview:  
  https://en.wikipedia.org/wiki/KOI8-U

- KOI8-RU overview:  
  https://en.wikipedia.org/wiki/KOI8-RU

- CP866 overview and bibliography:  
  https://en.wikipedia.org/wiki/Code_page_866

- ISO-IR-111 overview and naming issue:  
  https://en.wikipedia.org/wiki/ISO-IR-111

- ISO-IR-153 overview and registry ambiguity:  
  https://en.wikipedia.org/wiki/ISO-IR-153

- ISO/IEC 8859-5 overview:  
  https://en.wikipedia.org/wiki/ISO/IEC_8859-5

- Andrey Chernov biography and cited references:  
  https://en.wikipedia.org/wiki/Andrei_Chernov

- ANSI-art background:  
  https://en.wikipedia.org/wiki/ANSI_art
