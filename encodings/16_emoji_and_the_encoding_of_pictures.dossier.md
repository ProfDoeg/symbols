# Emoji and the encoding of pictures: Research Dossier

> **Standard:** The Unicode Standard, ISO/IEC 10646, and Unicode Technical Standard #51, *Unicode Emoji*  
> **First standardized repertoire:** Unicode 6.0, 11 October 2010  
> **Encoding width:** Unicode scalar values are abstract integers from U+0000 to U+10FFFF; UTF‑8 uses 1–4 eight-bit bytes, UTF‑16 uses one or two 16-bit code units, and UTF‑32 uses one 32-bit code unit  
> **Initial Japanese-carrier repertoire:** 722 characters: 114 already in Unicode 5.2 and 608 newly added in Unicode 6.0  
> **Current repertoire:** Emoji 17.0, released 9 September 2025; thousands of recommended characters and sequences rather than one closed character table  
> **Status:** Current, expanding, and maintained jointly through the Unicode Standard, ISO/IEC 10646 synchronization, UTS #51, the Unicode Character Database, and CLDR

## Evidentiary labels

This dossier marks claims as follows:

- **[STANDARD]** Normative standard, registered specification, formal proposal, committee minutes, or official data file.
- **[DOCUMENTED]** Contemporary corporate, museum, archival, or institutional record.
- **[RECOLLECTION]** A participant’s later account.
- **[SCHOLARLY RECONSTRUCTION]** Historical or technical interpretation assembled from records.
- **[DISPUTED]** A claim for which credible sources conflict.
- **[FOLKLORE]** A widely repeated story whose documentary basis is weak, late, or singular.
- **[MODERN INVENTION]** A retrospective slogan or conceptual category not found in the period documents.
- **[ABSENCE]** The requested proposition could not be established from the consulted primary record.

---

## Basic identification

### What “emoji encoding” actually names

**[STANDARD]** Emoji is not a separate byte encoding comparable to ASCII, ISO‑8859‑1, Shift JIS, or UTF‑8. It is a repertoire and presentation protocol layered on Unicode:

1. The Unicode Standard and ISO/IEC 10646 assign abstract characters code points.
2. UTF‑8, UTF‑16, or UTF‑32 serialize those code points.
3. UTS #51 defines emoji properties and the grammar of variation, modifier, flag, tag, and zero-width-joiner sequences.
4. CLDR supplies localized names, keywords, categories, annotations, and recommended keyboard ordering.
5. Vendors choose the actual artwork.

Thus “😂” has a stable identity, U+1F602 FACE WITH TEARS OF JOY, but Apple, Google, Microsoft, Samsung, and other vendors draw it differently.

**[STANDARD]** The standard encodes characters, not exact pictures. Unicode’s principles explicitly distinguish a character from its glyph. A proposal cannot demand a particular drawing, color, pose, or brand. Logos, named people, most specific buildings, and other protected or overly specific images are automatically declined under the current proposal rules.

### Name and etymology

**[DOCUMENTED/RECOLLECTION]** Japanese 絵文字, *emoji*, is formed from 絵, *e*, “picture,” and 文字, *moji*, “character.” It is not etymologically derived from English *emotion*, although the resemblance encouraged that interpretation outside Japan.

### Standard numbers and dates

| Instrument | Date | Function |
|---|---:|---|
| Unicode 1.0 | 1991 | Original 16-bit Unicode standard |
| ISO/IEC 10646-1 | 1993 | International Universal Coded Character Set |
| RFC 2044 | 1996 | Early Internet specification of UTF‑8 |
| RFC 2277 | 1998 | IETF policy requiring new protocols to support UTF‑8 |
| RFC 2279 | 1998 | Revised UTF‑8 definition |
| Unicode 5.2 | 2009 | Contained 114 of the eventual 722 carrier-derived emoji |
| Unicode 6.0 | 2010 | Added the remaining 608 carrier-derived characters |
| Unicode 8.0 / Emoji 1.0 | 2015 | Standardized skin-tone modifiers and formal emoji data |
| UTS #51 | first published 2015 | Defines Unicode emoji characters and sequences |
| RFC 3629 / STD 63 | 2003 | Present Internet UTF‑8 format, restricted to U+10FFFF |
| RFC 5198 | 2008 | Unicode format for network interchange |
| Unicode/Emoji 17.0 | 2025 | Current release at the time of research |

**[STANDARD]** Unicode and ISO/IEC 10646 maintain synchronized code points and repertoires. Their surrounding specifications differ: Unicode supplies extensive character properties and algorithms, while ISO/IEC 10646 is principally the coded-character-set standard.

### Bit width

There is no single “emoji bit width.”

- A Unicode scalar value needs conceptually 21 bits, though only U+0000–U+10FFFF is permitted.
- UTF‑8 uses 8-bit code units and 1–4 bytes per scalar value.
- Most standalone modern emoji require four UTF‑8 bytes.
- UTF‑16 represents most modern emoji with a surrogate pair: two 16-bit units.
- A displayed emoji may comprise many scalar values. A family or profession emoji can therefore occupy dozens of bytes while appearing as one grapheme cluster.

### Repertoire and present size

**[STANDARD]** UTS #51 records that the historical carrier union contained 722 Unicode emoji. Of those, 114 were already present in Unicode 5.2; Unicode 6.0 added the remaining 608 plus additional pictographs.

**[STANDARD]** Emoji 17.0 distinguishes:

- emoji-capable characters;
- default-text and default-emoji presentation;
- presentation sequences;
- keycap sequences;
- modifier sequences;
- regional-indicator flag sequences;
- tag sequences;
- recommended-for-general-interchange, or RGI, ZWJ sequences.

Consequently, “How many emoji are there?” has no unique answer. Counting assigned emoji characters, base pictographs, valid sequences, RGI sequences, skin-tone permutations, flags, or keyboard entries produces different totals. The Emoji 17.0 chart’s full RGI count is approximately 3,953, while the count of underlying characters is much smaller.

**[STANDARD]** Unicode 17.0 as a whole contains 159,801 graphic and format characters, of which emoji are only a small subset.

---

## The code in detail

## Code-space layout

Emoji are scattered through Unicode; they do not occupy one contiguous block.

Important ranges include:

| Range | Block or function |
|---|---|
| U+0023, U+002A, U+0030–0039 | Keycap bases `#`, `*`, and digits |
| U+00A9, U+00AE | Copyright and registered signs |
| U+200D | ZERO WIDTH JOINER |
| U+203C–U+3299, scattered | Older punctuation, arrows, dingbats, symbols, enclosed ideographs |
| U+2600–U+26FF | Miscellaneous Symbols |
| U+2700–U+27BF | Dingbats |
| U+FE0E | VARIATION SELECTOR‑15: request text presentation |
| U+FE0F | VARIATION SELECTOR‑16: request emoji presentation |
| U+1F1E6–U+1F1FF | Regional Indicator Symbols A–Z |
| U+1F300–U+1F5FF | Miscellaneous Symbols and Pictographs |
| U+1F600–U+1F64F | Emoticons |
| U+1F680–U+1F6FF | Transport and Map Symbols |
| U+1F900–U+1F9FF | Supplemental Symbols and Pictographs |
| U+1FA70–U+1FAFF | Symbols and Pictographs Extended‑A |
| U+1F3FB–U+1F3FF | Five emoji modifiers conventionally mapped to Fitzpatrick types |
| U+E0020–U+E007E | Tag characters |
| U+E007F | CANCEL TAG |

Other emoji reside in arrows, geometric shapes, enclosed alphanumerics, Mahjong tiles, playing cards, miscellaneous technical symbols, and script-specific blocks.

**[STANDARD]** The order of pictographs inside these blocks is partly historical and partly categorical. The core specification calls the general symbol order arbitrary, while noting attempts to keep similar subsets together.

### No ASCII-style control block

Emoji have no control block, newline code, delete code, space code, case distinction, shift state, or escape character of their own. They use ordinary Unicode text machinery:

- newline is normally U+000A LINE FEED, serialized as byte `0A` in UTF‑8;
- carriage return is U+000D, byte `0D`;
- space is U+0020, byte `20`;
- delete is U+007F, byte `7F`;
- case is inapplicable to pictographs, though adjacent ordinary text retains Unicode case properties;
- bidirectional controls, combining marks, ZWJ, variation selectors, and tags come from the wider Unicode repertoire.

A visible emoji sequence is not an ISO 2022 shift state. Its interpretation is local to explicit code points in the sequence.

## UTF‑8 structure

**[STANDARD: RFC 3629]**

| Scalar-value range | UTF‑8 bit structure |
|---|---|
| U+0000–U+007F | `0xxxxxxx` |
| U+0080–U+07FF | `110xxxxx 10xxxxxx` |
| U+0800–U+FFFF | `1110xxxx 10xxxxxx 10xxxxxx` |
| U+10000–U+10FFFF | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

Restrictions include:

- `C0`, `C1`, and `F5`–`FF` cannot occur in valid UTF‑8.
- Surrogate code points U+D800–U+DFFF are prohibited.
- Every scalar value has one shortest encoding.
- Overlong encodings are invalid.
- ASCII bytes retain their ASCII meanings and cannot occur inside multibyte sequences.

### Synchronization and corruption

**[STANDARD]** UTF‑8 is self-synchronizing at the code-point level:

- leading bytes begin `0`, `110`, `1110`, or `11110`;
- continuation bytes always begin `10`;
- a reader entering in midstream skips continuation bytes until it reaches the next leading byte;
- corruption normally damages one scalar value and, depending on replacement policy, a bounded number of neighboring bytes.

This does not fully synchronize an emoji sequence. A reader can recover UTF‑8 code-point boundaries while still entering midway through `👩🏽‍💻`, seeing a modifier, ZWJ, or laptop without its intended base. Grapheme and emoji-sequence boundaries require UAX #29 and UTS #51 processing.

**[STANDARD]** Emoji sequences are treated as extended grapheme clusters. Cursor motion and backspace should normally treat a supported sequence as one user-perceived unit. Actual applications have historically split them incorrectly.

### Error replacement

Invalid byte sequences are generally replaced with U+FFFD REPLACEMENT CHARACTER, `�`, encoded in UTF‑8 as `EF BF BD`. Standards prescribe rejection or replacement constraints but leave some details—such as how many replacement characters appear—to conformant implementation policy.

### Collation

UTF‑8 bytewise ordering preserves Unicode scalar-value order for valid strings. RFC 3629 warns that code-point order is almost never a culturally appropriate collation order.

Emoji keyboards therefore normally use CLDR’s curated categorical ordering rather than raw code-point order. Flags may be ordered by localized region name; raw regional-indicator order follows two-letter region identifiers, producing sequences unintuitive to ordinary users.

## Emoji presentation selectors

Some old characters precede emoji and traditionally have monochrome text glyphs:

- U+2764 HEAVY BLACK HEART: `❤`
- U+2600 BLACK SUN WITH RAYS: `☀`
- U+2708 AIRPLANE: `✈`

A selector can request presentation:

- `❤︎` = U+2764 U+FE0E, text style requested;
- `❤️` = U+2764 U+FE0F, emoji style requested.

**[STANDARD]** The request is not an absolute guarantee. Presentation depends on font and platform support.

UTF‑8:

- U+2764 `❤` → `E2 9D A4`
- U+FE0E VS15 → `EF B8 8E`
- U+FE0F VS16 → `EF B8 8F`

Thus the difference between text heart and emoji heart may be three invisible bytes.

## Skin-tone modifiers

Unicode 8.0 added:

| Character | Code point | UTF‑8 |
|---|---:|---|
| 🏻 | U+1F3FB | `F0 9F 8F BB` |
| 🏼 | U+1F3FC | `F0 9F 8F BC` |
| 🏽 | U+1F3FD | `F0 9F 8F BD` |
| 🏾 | U+1F3FE | `F0 9F 8F BE` |
| 🏿 | U+1F3FF | `F0 9F 8F BF` |

**[STANDARD]** These are named EMOJI MODIFIER FITZPATRICK TYPE‑1‑2 through TYPE‑6 and follow an eligible `Emoji_Modifier_Base`. A supporting renderer combines base and modifier into one glyph.

Example:

- `👋` = U+1F44B
- `🏿` = U+1F3FF
- `👋🏿` = U+1F44B U+1F3FF
- UTF‑8 = `F0 9F 91 8B F0 9F 8F BF`

**[DOCUMENTED]** Draft UTR #51 justified modifiers partly because carrier-derived “generic” people had often been drawn with light skin rather than silhouettes or nonhuman colors.

**[CONTROVERSY]** The Fitzpatrick scale was created to classify dermatological response to ultraviolet exposure, not to constitute a universal taxonomy of racial identity. Public-review comments questioned the mapping and argued that adding explicit tones could racialize previously generic figures. These objections are documented, while claims that modifiers either “solved” or “caused” emoji racism are interpretations, not standard findings.

## Zero-width-joiner sequences

U+200D ZERO WIDTH JOINER is encoded `E2 80 8D`.

UTS #51 defines an emoji ZWJ sequence schematically as:

```text
emoji_zwj_element (ZWJ emoji_zwj_element)+
```

A supporting renderer displays the sequence as one composite glyph. An older renderer can show the components separately, which is the intended fallback mechanism.

Examples:

- `👩‍💻` = WOMAN + ZWJ + PERSONAL COMPUTER
- `👨‍⚕️` = MAN + ZWJ + STAFF OF AESCULAPIUS + VS16
- `👩‍🚀` = WOMAN + ZWJ + ROCKET
- `🏳️‍🌈` = WHITE FLAG + VS16 + ZWJ + RAINBOW
- `👨‍👩‍👧‍👦` = MAN + ZWJ + WOMAN + ZWJ + GIRL + ZWJ + BOY

**[STANDARD]** Only a cataloged subset is RGI. Arbitrary syntactically possible combinations need not receive a single glyph.

**[DOCUMENTED]** In 2016 Google proposed profession sequences addressing the narrow and stereotyped distribution of gendered occupations. Unicode subsequently cataloged profession, gender, and expanded-family ZWJ sequences.

## Flag sequences

A country or region flag is normally not assigned its own “flag character.” It is a pair of regional indicators.

Example, United States:

- U+1F1FA REGIONAL INDICATOR SYMBOL LETTER U
- U+1F1F8 REGIONAL INDICATOR SYMBOL LETTER S
- displayed together: `🇺🇸`
- UTF‑8: `F0 9F 87 BA F0 9F 87 B8`

Germany:

- `🇩🇪` = U+1F1E9 U+1F1EA
- UTF‑8: `F0 9F 87 A9 F0 9F 87 AA`

**[STANDARD]** A regional-indicator pair represents a region identifier, not an immutable flag design. Vendors decide the displayed flag, and it may change when a polity changes its flag. Unsupported pairs should receive a generic missing-flag display rather than necessarily two boxed letters.

Validity is tied to CLDR region subtags, substantially inherited from ISO 3166 conventions. This delegates much political classification rather than eliminating politics.

Subdivision flags such as England, Scotland, and Wales use a black-flag base plus tag characters and CANCEL TAG. Only selected tag sequences are RGI.

## Keycaps

`1️⃣` is normally:

```text
U+0031 DIGIT ONE
U+FE0F VARIATION SELECTOR-16
U+20E3 COMBINING ENCLOSING KEYCAP
```

UTF‑8:

```text
31 EF B8 8F E2 83 A3
```

The plain digit remains an ASCII byte; the selector and enclosing mark transform its presentation.

## Worked example, byte by byte

Text:

```text
Hi 👩🏽‍💻!
```

followed by line feed.

| Visible part | Unicode scalar(s) | UTF‑8 bytes |
|---|---|---|
| `H` | U+0048 | `48` |
| `i` | U+0069 | `69` |
| space | U+0020 | `20` |
| `👩` | U+1F469 WOMAN | `F0 9F 91 A9` |
| `🏽` | U+1F3FD MEDIUM SKIN TONE | `F0 9F 8F BD` |
| invisible joiner | U+200D ZWJ | `E2 80 8D` |
| `💻` | U+1F4BB PERSONAL COMPUTER | `F0 9F 92 BB` |
| `!` | U+0021 | `21` |
| line feed | U+000A | `0A` |

Complete UTF‑8 stream:

```text
48 69 20 F0 9F 91 A9 F0 9F 8F BD E2 80 8D F0 9F 92 BB 21 0A
```

UTF‑16 code units:

```text
0048 0069 0020 D83D DC69 D83C DFFD 200D D83D DCBB 0021 000A
```

UTF‑32 code units:

```text
00000048 00000069 00000020 0001F469 0001F3FD
0000200D 0001F4BB 00000021 0000000A
```

In US-ASCII the phrase cannot be represented. A lossy transliteration might be:

```text
Hi [woman technologist]!
```

whose bytes would be ordinary ASCII. ISO‑8859‑1 likewise cannot encode the emoji. UTF‑8 preserves the ASCII bytes unchanged and adds multibyte Unicode sequences.

### Carrier-era comparison

**[SCHOLARLY RECONSTRUCTION, based on published carrier mappings]** The camera pictograph later unified as U+1F4F7 could appear in carrier-specific Shift JIS private-use extensions as approximately:

- DoCoMo: `F8 E2`
- KDDI/au: `F6 EE`
- SoftBank: `F9 48`
- Unicode UTF‑8 U+1F4F7: `F0 9F 93 B7`

The carrier byte values were neither mutually compatible nor semantically self-describing. A gateway needed a mapping table and sometimes a best-fit substitute.

## What emoji can and cannot express

Emoji can encode:

- conventional pictographs;
- emotions and gestures;
- objects, food, activities, weather, places, and selected symbols;
- person modifiers;
- selected family, role, gender, and accessibility combinations;
- region identifiers presented as flags.

It cannot reliably encode:

- an exact vendor illustration;
- an arbitrary photograph;
- every logo, product, person, building, flag, food, species, or gesture;
- exact facial geometry, direction, costume, color, or cultural interpretation unless standardized as a permitted distinction;
- arbitrary semantic propositions;
- the sender’s intended connotation.

The Unicode name identifies the character, not every meaning acquired in use. UTS #51 gives HONEY POT as an example: the character denotes the pictorial object, not the abstract semantic property “sweet.”

---

## Origins

## Before digital emoji

### Pictures as writing and type

Pictographs long predate electronic character codes: hieroglyphs, rebuses, printers’ ornaments, astronomical signs, map symbols, pointing hands, dingbats, and playing-card symbols all complicate any assertion that emoji “invented picture writing.”

**[STANDARD]** Unicode inherited many pictorial characters from earlier typography and standards:

- zodiac and astronomical signs;
- Zapf Dingbats;
- ARIB Japanese broadcasting symbols;
- Wingdings and Webdings symbols;
- enclosed ideographs and Japanese signage.

Emoji therefore grew by unifying a Japanese mobile pictograph practice with a much older coded-symbol tradition.

### Telegraph codes and ASCII ancestry

The deeper character-encoding lineage runs through:

- Émile Baudot’s five-bit telegraph code;
- Donald Murray’s modifications and keyboard-oriented teleprinter practice;
- CCITT International Telegraph Alphabets;
- punched-card systems associated with Herman Hollerith;
- IBM BCD-derived codes and EBCDIC;
- ASCII, standardized as ASA X3.4-1963 and revised in 1965, 1967, and 1968;
- ECMA‑6 and ISO/IEC 646;
- ISO 2022 escape and shift mechanisms;
- national ISO 646 variants;
- ISO 8859 eight-bit families;
- Japanese JIS X 0208, Shift JIS, EUC-JP, and ISO‑2022‑JP;
- Unicode and ISO/IEC 10646.

These predecessors explain why emoji first appeared in private-use spaces of Japanese encodings and why Unicode compatibility mattered.

Bob Bemer, Charles Mackenzie, Hugh McGregor Ross, Tom Van Vleck, and others are central to ASCII history, but **[ABSENCE]** no evidence links Bemer, Baudot, Murray, or Hollerith directly to the design of emoji. Treating them as emoji designers would collapse ancestry into authorship.

## Japanese precedents

### Pager hearts and pictorial services

**[RECOLLECTION]** Kurita later described Japanese pager culture, including the popularity and removal of a heart symbol from a DoCoMo pager, as evidence that compact visual cues mattered socially.

**[CAUTION]** This is a participant’s retrospective explanation. It is plausible and repeatedly published, but it is not equivalent to a dated design memorandum establishing a single causal origin.

Earlier digital icons, terminal pictograms, Videotex mosaics, dingbat fonts, electronic toys, and Japanese device glyphs make any absolute “first digital emoji” claim unstable.

### SoftBank/J-Phone, 1997

**[DISPUTED FIRST]** In 2019 Emojipedia examined a surviving SkyWalker DP‑211SW handset and its documentation and reported a 90-icon J‑Phone/SoftBank set from 1997, including a color pile-of-poo animation. Its designers remain unidentified.

Evidence:

- physical-device and manual evidence;
- a release predating DoCoMo’s 1999 i-mode set;
- later acknowledgment that the canonical chronology required correction.

Limitations:

- “emoji” was not necessarily the contemporary marketing name;
- its influence on the later interoperable repertoire is less fully documented;
- no named designer or internal design file was located in the consulted record.

The safe conclusion is that SoftBank has the strongest surviving claim to an earlier Japanese mobile-phone emoji set, while Kurita’s DoCoMo set remains the best-documented and most historically influential named design.

### Kurita and DoCoMo, 1999

**[DOCUMENTED/RECOLLECTION]** Shigetaka Kurita, working on NTT DoCoMo’s i-mode project, designed a set of 176 monochrome glyphs on a 12×12 grid. DoCoMo’s later institutional interview says the set was completed in about one month.

Kurita cited sources including:

- weather pictograms;
- manga conventions;
- street and transportation signs;
- symbols already understood in Japanese public life.

The set included weather, vehicles, sports, technologies, phases of the moon, hearts, faces, and culturally specific signs.

**[RECOLLECTION]** Kurita has described the immediate design work as his. The wider i-mode service was a corporate project involving Takeshi Natsuno and others. “Kurita invented emoji alone” overstates the institutional and technological context.

### Incompatible carriers

DoCoMo, KDDI/au, and J‑Phone/SoftBank expanded distinct sets.

**[STANDARD: L2/08-081 and L2/09-025]** Their symbols were encoded in carrier-specific private-use extensions to Shift JIS; KDDI also used a carrier-specific ISO‑2022‑JP scheme. Similar-looking glyphs had different codes, mappings could be one-way, and some symbols had no counterpart.

Consequences included:

- missing boxes or text when crossing carriers;
- accidental substitution of a different picture;
- conversion gateways;
- later carrier mapping agreements;
- Unicode Private Use Area mappings by early smartphone software.

This is the precise technical problem Unicode ultimately addressed.

### The failed or dormant 2000 approach

**[DOCUMENTED, SECONDARY INSTITUTIONAL REPORT]** An ICANN study reports that a proposal to encode DoCoMo emoji was raised in 2000 but did not proceed because widespread future use was uncertain and Japanese carrier support was lacking.

**[ABSENCE]** The consulted search did not recover a complete public 2000 proposal bearing the evidentiary weight of L2/07-257 or L2/09-025. The claim should therefore not be narrated as a fully documented formal rejection without locating that document.

## Unicode’s origins, 1987–1993

**[DOCUMENTED BY UNICODE HISTORY]**

- September 1987: Joe Becker of Xerox and Mark Davis of Apple discussed multilingual coding.
- December 1987: earliest documented use of “Unicode,” coined by Becker from “unique, universal, and uniform.”
- February/August 1988: Becker’s *Unicode 88* articulated a 16-bit universal character scheme.
- Lee Collins investigated fixed-width two-byte representation.
- Ken Whistler, Mike Kernaghan, Asmus Freytag, Rick McGowan, Joan Aliprand, and others joined the work.
- 3 January 1991: Unicode, Inc. incorporated in California.
- 1991: Unicode 1.0 appeared.
- 1993: ISO/IEC 10646-1 established the UCS after Unicode and ISO groups reconciled competing designs.

The initial corporate participants included Apple, Xerox, IBM, Microsoft, NeXT, Sun, Novell, Metaphor, GO, and the Research Libraries Group.

### The 16-bit assumption

**[DOCUMENTED]** Early Unicode promoted a fixed-width 16-bit model capable of about 65,000 characters. This was attractive to implementers but insufficient for all historic, rare, and variant characters.

The later architecture introduced:

- surrogate pairs in UTF‑16;
- 17 planes from U+0000 through U+10FFFF;
- UTF‑32;
- supplementary-plane allocations containing most modern emoji.

Emoji thus arrived after the “one character equals one 16-bit word” model had already broken down.

### ISO versus Unicode

**[SCHOLARLY RECONSTRUCTION]** Early ISO 10646 work entertained a much larger multi-octet code structure, while Unicode stressed practical 16-bit implementation. Their merger avoided rival universal repertoires. ISO/IEC JTC 1/SC 2/WG 2 and the Unicode Technical Committee have since coordinated code-point assignments.

The simplified story that “Unicode defeated ISO” is misleading: the current system is an institutional and technical synchronization, albeit one arising from substantial architectural negotiation.

## UTF‑8, 1992

**[STANDARD + PARTICIPANT RECOLLECTION]** RFC 3629 says Ken Thompson devised UTF‑8 in September 1992, guided by criteria from Rob Pike, for Plan 9. It passed through the names FSS-UTF, FSS/UTF, and UTF‑2 before becoming UTF‑8.

**[RECOLLECTION]** Pike’s account says he and Thompson worked out the form during an evening after an X/Open meeting; the famous version places Thompson’s construction on a placemat at a New Jersey diner.

**[SINGLE-WITNESS CAUTION]** The placemat story is a participant recollection, not supported by a surviving placemat or contemporaneous photograph in the sources consulted. RFC 3629 confirms the designers and month but not the physical anecdote.

UTF‑8’s crucial properties—ASCII identity, unambiguous lead and continuation bytes, code-point-order preservation, and recovery from arbitrary byte positions—made supplementary-plane emoji practical on byte-oriented networks.

## Google, Apple, and Unicode, 2006–2010

### Google’s conversion work

**[DOCUMENTED]** Google began work around 2006 on transporting Japanese carrier emoji through Gmail and related services. It constructed cross-carrier mappings and initially used Unicode private-use values.

### 2007 proposal

**[STANDARD/COMMITTEE RECORD]**

- May 2007: the Unicode Technical Committee approved proceeding with symbol work and formed a Symbols Subcommittee.
- 3 August 2007: Kat Momoi, Mark Davis, and Markus Scherer of Google submitted L2/07-257, *Working Draft Proposal for Encoding Emoji Symbols*.
- August 2007: UTC agreed to support encoding emoji according to principles developed by the subcommittee.

This is better described as a Google-led Unicode proposal than a joint Google-and-Apple proposal at its beginning.

### Apple joins

Peter Edberg and Yasuo Kida of Apple subsequently participated. Apple needed Japanese carrier compatibility for the iPhone, particularly through SoftBank.

### 2008 working draft

L2/08-081 explicitly describes symbols used by DoCoMo, KDDI, and SoftBank plus nine Google symbols, noting their private-use Shift JIS and ISO‑2022‑JP encodings.

### 2009 consolidated proposal

L2/09-025, dated 30 January 2009, lists Markus Scherer, Mark Davis, Kat Momoi, and Darick Tong of Google. Related records include Apple participation by Peter Edberg and Yasuo Kida.

It attempted:

- cross-carrier semantic mapping;
- unification with existing Unicode symbols;
- avoidance of encoding mere glyph variants;
- allocation of new characters where no adequate Unicode equivalent existed;
- round-trip compatibility where possible.

### Unicode 6.0, 2010

**[STANDARD]** Unicode 6.0 was released on 11 October 2010.

UTS #51’s later historical account states:

- the union contained 722 carrier-derived Unicode emoji;
- 114 were already in Unicode 5.2;
- 608 were newly encoded in Unicode 6.0;
- additional pictographic characters not counted in that carrier union were also present.

Therefore “Unicode added 722 emoji in 2010” is convenient but technically imprecise. Unicode 6.0 established the recognizable standardized carrier repertoire, but not all 722 received new code points in that release.

---

## Adoption and expansion

## Japanese mobile adoption

The Japanese carriers made emoji ordinary in mobile mail before Unicode standardized them. Carrier conversion systems gradually mapped incoming competitors’ symbols to local equivalents.

In 2008 the iPhone 3G entered Japan through SoftBank. Apple’s first emoji implementation was consequently closely related to SoftBank compatibility and was initially hidden or restricted outside Japan.

## Global smartphone adoption

Apple exposed the emoji keyboard broadly in iOS 5 in 2011. Android vendors and messaging systems expanded support in the same period.

**[SCHOLARLY RECONSTRUCTION]** Unicode 6.0 supplied interoperable identities; smartphone keyboards and platform fonts supplied mass discoverability. Neither alone explains the global adoption.

Emoji survived transportation through:

- SMS/MMS gateways;
- email;
- web pages;
- social networks;
- copy and paste;
- databases;
- filenames and source code;
- push notifications.

The transition from private carrier codes to Unicode was therefore absorption, not replacement of emoji themselves.

## UTS #51 and Emoji 1.0, 2015

Unicode published the first formal emoji technical report and versioned emoji data in 2015. It defined distinctions that had previously been inconsistently inferred by vendors:

- emoji versus text presentation;
- eligible modifier bases;
- valid sequences;
- implementation guidance;
- data files for interoperable support.

## Skin tone, 2015

Unicode 8.0 and Emoji 1.0 introduced five modifier characters. Their sequence design prevented the need to encode a separate code point for every base/skin combination, although the number of displayed RGI combinations still grew substantially.

## ZWJ families, roles, and professions, 2015–2017

Early family emoji often encoded heterosexual and gendered configurations. ZWJ sequences made same-sex couples, varied families, and professions possible without assigning every visible combination a new atomic character.

In 2016 a Google team including Rachel Been, Nicole Bleuel, Agustin Fonts, and Mark Davis proposed expanded professional representation. UTS #51 revisions cataloged profession, role, gender, and family sequences.

Fallback is deliberate:

```text
woman + ZWJ + microscope
```

can render as one woman-scientist glyph when supported or as a woman, joiner behavior, and microscope components on an older system.

## Flags

The original Japanese carriers included a small, commercially relevant set of national flags. Unicode’s regional-indicator mechanism generalized the model so that valid region codes could be represented without assigning a political “country character” for each.

The scheme did not eliminate controversy:

- ISO/CLDR recognition governs eligibility;
- territories may receive identifiers while stateless peoples do not;
- vendors can suppress a flag in particular markets;
- political changes require artwork updates;
- subnational flags are mostly unsupported.

In 2022 the Emoji Subcommittee announced it would no longer accept ordinary proposals for new region flags, arguing that one-off additions create further exclusion and that region-code-derived flags should be handled systematically.

## Worldwide text infrastructure

Emoji adoption was carried by UTF‑8’s wider success.

**[STANDARD]** RFC 2277, January 1998, requires IETF protocols to be capable of UTF‑8 for text. RFC 3629 standardized present four-byte UTF‑8 in 2003. RFC 5198 supplies a Unicode network-interchange profile.

**[DOCUMENTED SURVEY]** W3Techs reported in September 2026 that UTF‑8 was declared by 99.1% of websites whose encoding it could identify, and 99.3% among the top million. The figure is a survey result under W3Techs’ methodology, not a census of every byte on the Web.

The W3C recommends UTF‑8; modern Web encoding specifications converge legacy labels and require UTF‑8 for new formats and protocols.

## Current status

Emoji remain actively extended. Emoji 17.0 was released with Unicode 17.0 in September 2025. UTS #51, emoji data files, CLDR annotations, platform fonts, and keyboard updates form a release pipeline.

The original carrier encodings have declined, but their inheritance remains visible in:

- Japanese buttons and ideographic signs;
- convenience-store and hot-spring symbols;
- carrier-derived faces, weather signs, and zodiac symbols;
- mappings retained for archival conversion;
- Unicode names and compatibility decisions that cannot later be removed.

---

## Vendor design differences

## Character versus glyph

The most important rule is:

```text
Unicode standardizes identity and sequence; vendors draw the image.
```

Consequently:

- color and shading vary;
- people have different hair, clothing, and poses;
- objects differ by local industrial design;
- facial expressions may be interpreted differently;
- a sent character can acquire a different emotional force on the recipient’s platform.

Empirical studies have found cross-platform sentiment disagreement for some faces. That is not a byte-decoding error: both systems decoded the same Unicode scalar value but supplied materially different glyphs.

## The pistol that became a water pistol

U+1F52B’s immutable Unicode character name is PISTOL.

- Apple changed its glyph from a firearm to a green water pistol in iOS 10 in 2016.
- WhatsApp, Samsung, Twitter, Google, and others subsequently adopted toy- or water-gun renderings, especially in 2017–2018.
- For a transition period, the same code point could appear as a toy gun to a sender and a revolver to a recipient.
- Some platforms have since changed direction again.

**[DOCUMENTED]** Apple’s redesign is visible in released fonts and contemporary reporting.

**[INTERPRETATION]** It was widely read as a gun-control statement. Apple did not establish an official semantic change in Unicode.

**[CORRECTION]** Unicode did not change the formal character name from PISTOL to WATER PISTOL; immutable character names generally cannot be altered. CLDR keywords or short names and vendor artwork may say “water pistol.” Claims that “Unicode officially renamed the character” conflate these layers.

## Google’s blobs

Google’s early Android emoji used rounded, gumdrop-like “blob” figures. In 2017 Google shifted toward more circular faces and human-shaped designs closer to the broad vendor norm.

**[DOCUMENTED]** The font releases establish the visual change.

**[INTERPRETATION]** Calling it “Google surrendering to Apple style” is journalistic shorthand. Interoperability and consistent emotional legibility were cited concerns, but the standard did not mandate Apple’s design.

## Other consequential differences

- 🙏 has been drawn and read as prayer, thanks, pleading, or a high five.
- 😤 has a Unicode identity historically described through “look of triumph,” but many users read it as anger or frustration.
- 🔫 has alternated between realistic firearm, ray gun, and water pistol.
- 🍔 ingredient order has varied by platform.
- 🥟 and other foods reveal culturally specific assumptions in their drawings.
- flags can be omitted or altered according to regional policy.

These are semantic-pragmatic differences, not differences in encoded text.

---

## Proposal process and institutional structure

## The Unicode Consortium

Unicode, Inc. is a California nonprofit consortium incorporated in 1991. It is not a United Nations body, government agency, or universal legislature.

Its voting membership has historically included large technology companies, smaller firms, governments and governmental bodies, universities, nonprofit organizations, and individual members. Technical work also relies heavily on invited experts and volunteers.

Emoji were initially handled by symbols work and later by the Emoji Subcommittee. Current materials refer to the Emoji Standard & Research Working Group, which advises the Unicode Technical Committee. The UTC has final technical authority within the Consortium process; ISO/IEC JTC 1/SC 2/WG 2 handles corresponding character additions to ISO/IEC 10646.

## Present proposal criteria

**[STANDARD]** Current guidelines ask whether a candidate:

- has demonstrably high expected usage;
- expresses multiple concepts;
- works productively with other emoji;
- breaks new conceptual ground;
- is visually distinctive at small sizes;
- completes an incomplete category;
- is required for compatibility with an existing widely used system.

Exclusion factors include:

- already representable;
- overly specific;
- one member of an open-ended series;
- transient;
- merely justified by an existing analogous emoji.

Automatically declined categories include:

- logos and brands;
- most copyrighted or trademark-dependent images;
- UI icons and signage;
- named living or historic people;
- most particular buildings and landmarks;
- deities;
- ordinary region-flag proposals lacking the required systematic identifier basis;
- images containing text;
- demands for an exact design;
- proposals lacking necessary image rights.

The proposer must supply small color and black-and-white sample art and grant broad, perpetual rights needed for standardization.

**[STANDARD]** Once encoded, a character cannot be removed merely because it becomes unpopular. That stability requirement makes present admission stricter than the original compatibility-driven carrier import.

## Rejections

Unicode publishes proposal status and many decision documents, but the completeness and detail of rejection explanations vary.

Examples of recurrent rejection reasons include:

- “already represented”;
- low or poorly demonstrated frequency;
- indistinct at emoji size;
- a brand or particular object model;
- opening an unbounded series;
- transient Internet fashion;
- sufficient expression through an existing character or sequence.

**[CRITIQUE]** Researchers and advocates argue that requiring search-frequency evidence advantages concepts already legible in English-language commercial search engines and communities with proposal-writing expertise.

**[RESPONSE IN OFFICIAL MATERIAL]** Unicode says anyone may submit, that current criteria are intended to predict broad use, and that inherited carrier characters would not necessarily pass today’s rules.

Both propositions can be true: formal access can be open while practical participation remains unequal.

---

## The other scripts

Emoji cannot be understood apart from Unicode’s larger purpose: encoding the world’s writing systems.

## ASCII and Western European limitations

ASCII’s 128 positions encode English letters, digits, punctuation, and controls but cannot directly express accented European alphabets, Greek, Cyrillic, Hebrew, Arabic, Indic scripts, CJK, or emoji.

ISO 646 national variants replaced a few ASCII punctuation positions with national letters or currency signs. ISO 8859 families supplied separate eight-bit repertoires, but one document still could not freely mix every script.

Vendor code pages multiplied incompatible interpretations of bytes `80`–`FF`, creating the conditions for mojibake.

## Cyrillic

Solutions included:

- ISO‑8859‑5;
- KOI8‑R and KOI8‑U;
- Windows‑1251;
- IBM and Macintosh Cyrillic pages.

**[DOCUMENTED DESIGN TRICK]** KOI8 was arranged so that stripping the high bit from Cyrillic text produced roughly corresponding Latin letters, leaving a transliterable-looking residue rather than arbitrary punctuation. Calling this complete “readability after bit stripping” is folklore-level exaggeration; the correspondence is approximate.

Unicode assigns Cyrillic characters independent scalar values and supports mixing them with Latin, Greek, and emoji.

## Greek

Greek appeared in ISO‑8859‑7 and vendor pages. Unicode separates Greek letters from Latin even where glyphs resemble one another because they belong to distinct scripts and have distinct textual identities.

That principled separation creates legitimate multilingual representation but also permits mixed-script confusable identifiers.

## Hebrew and Arabic

Legacy solutions included ISO‑8859‑8 and ISO‑8859‑6, IBM code pages, Windows‑1255 and Windows‑1256, and national/vendor encodings.

Unicode normally stores text in logical order. UAX #9 computes visual bidirectional presentation for Hebrew and Arabic mixed with left-to-right text.

Arabic shaping is contextual: a base letter’s presentation depends on its neighbors. Unicode encodes underlying letters and joining properties rather than requiring authors to choose isolated, initial, medial, or final display forms, though Arabic presentation-form compatibility characters remain for round-trip reasons.

Emoji participate in bidi layout mainly as neutral or other symbols. Incorrect isolation around emoji, numbers, and punctuation can reorder visible material or create spoofing risks.

## Indic scripts

Many Indic scripts encode consonants, vowels, dependent marks, viramas, and joining behavior rather than every printed syllable as an atomic character. Rendering engines perform reordering, ligation, and shaping.

Emoji do not replace this model. An Indic-script sentence containing emoji remains a mixed stream requiring Unicode normalization, segmentation, script shaping, bidi rules where relevant, and emoji-cluster handling.

## Chinese, Japanese, and Korean

Pre-Unicode systems included:

- GB 2312, GBK, and later GB 18030 for Chinese;
- Big5 and CNS 11643 for Traditional Chinese;
- JIS X 0208, Shift JIS, EUC‑JP, and ISO‑2022‑JP for Japanese;
- KS X 1001, EUC‑KR, and Johab for Korean.

These solved local requirements but were mutually incompatible and often stateful or variable-width.

Unicode’s CJK Unified Ideographs encode historically related Han characters under shared code points when the applicable unification rules treat them as the same abstract character. Language-sensitive fonts supply preferred glyph forms.

Emoji’s Japanese carrier codes initially lived inside the same vendor-specific ecosystem. Their standardization was consequently a small-scale replay of Unicode’s larger compatibility mission.

## What emoji did for other scripts

Emoji do not add missing alphabets or supply language-neutral translations. They coexist with scripts.

Claims that emoji are “the first universal language” obscure:

- divergent meanings across communities;
- cultural knowledge needed to interpret images;
- accessibility dependence on localized labels;
- different vendor drawings;
- absence of productive syntax comparable to a natural language;
- the older international spread of numerals, mathematical notation, traffic signs, and other symbol systems.

**[MODERN INVENTION]** “Emoji are the first new script adopted worldwide” is an attractive slogan but not a standards category or established historical finding. Unicode classifies emoji predominantly as symbols, not as one script with a `Script` property, grammar, or orthography. Their global adoption is remarkable; calling them a “new script” is metaphorical.

---

## People and institutions

### Direct emoji contributors

- **Shigetaka Kurita** — designer of DoCoMo’s documented 176-glyph 1999 set.
- **Yuko Sasahara** — member of the DoCoMo project team appearing in NTT’s institutional history.
- **Kat Momoi** — Google internationalization specialist and co-author of the 2007 proposal.
- **Mark Davis** — Unicode co-founder, long-serving president and later CTO; Google engineer; proposal and emoji-specification contributor.
- **Markus Scherer** — Google internationalization engineer and proposal co-author.
- **Darick Tong** — co-author of the January 2009 Google proposal.
- **Peter Edberg** — Apple internationalization engineer involved in Unicode emoji work.
- **Yasuo Kida** — Apple engineer and Unicode participant involved in Japanese and emoji standardization.
- **Rachel Been, Nicole Bleuel, Agustin Fonts** — Google contributors to the 2016 profession-emoji proposal.
- **Jennifer Daniel** — later Emoji Subcommittee chair and author/editor of proposals addressing gender consistency and emoji policy.

### Unicode founders and editors

- **Joe Becker** — Xerox engineer; coined “Unicode” and wrote *Unicode 88*.
- **Lee Collins** — Xerox and Apple engineer; developed early architectural principles.
- **Mark Davis** — Apple engineer at Unicode’s origin.
- **Ken Whistler** — early contributor, editor, secretary, and major technical author.
- **Mike Kernaghan, Bill English, Asmus Freytag, Joan Aliprand, Rick McGowan** — organizational, editorial, character-database, and technical contributors.

### UTF‑8

- **Ken Thompson** — devised UTF‑8’s bit structure in September 1992.
- **Rob Pike** — supplied design criteria, implemented Plan 9 work, and preserved the best-known participant account.
- **François Yergeau** — author of RFC 2044, RFC 2279, and RFC 3629.

### Earlier encoding history

- **Émile Baudot** — five-bit telegraph code.
- **Donald Murray** — teleprinter-oriented modifications.
- **Herman Hollerith** — punched-card tabulation and coding ancestry.
- **Bob Bemer** — influential ASCII advocate and committee contributor.
- **Charles E. Mackenzie** — IBM engineer and historian, author of *Coded Character Sets: History and Development*.
- **Hugh McGregor Ross** — standards contributor associated with ISO character-set work and later Unicode/ISO discussions.

### Institutions

- **ASA/ANSI X3.4** — ASCII.
- **ECMA** — ECMA‑6 and related international character-code standards.
- **ISO/IEC JTC 1/SC 2/WG 2** — Universal Coded Character Set maintenance.
- **CCITT/ITU‑T** — international telegraph alphabets and telecommunications standards.
- **IBM** — punched-card, BCD, EBCDIC, code pages, and Unicode participation.
- **DEC, Bell Labs, Xerox, Apple, Microsoft, Google** — terminal, operating-system, character-set, Unicode, UTF‑8, smartphone, and emoji implementations.
- **NTT DoCoMo, KDDI/au, J‑Phone/SoftBank** — Japanese carrier repertoires.
- **IETF** — Internet charset and UTF‑8 standards.
- **W3C/WHATWG** — Web encoding requirements.
- **Unicode Consortium** — Unicode, UTS #51, CLDR, and emoji proposal process.
- **MoMA** — acquired the Kurita set in 2016 as a work of communication design.

### Requested-name clarification

**[ABSENCE]** The brief mentions “Davis” and “Collins,” both directly central to Unicode. It also mentions “Whistler,” likewise central. It does not provide enough identifying context for every possible engineer named “Collins” or “Davis” in earlier ASCII committee history; this dossier avoids conflating Unicode’s Lee Collins and Mark Davis with unrelated namesakes.

---

## Culture

## Emoticons, kaomoji, and emoji

Scott Fahlman’s 1982 `:-)` and `:-(` proposal is a well-documented early network use of sideways emoticons, not the origin of all typographic faces.

Japanese kaomoji such as:

```text
(^_^)
(>_<)
¯\_(ツ)_/¯
```

use a wider character repertoire and are read upright. Carrier emoji converted common visual functions into single selectable pictographs.

Emoji therefore did not simply replace emoticons. The forms coexist:

- emoticons are sequences of ordinary characters;
- emoji are standardized characters or sequences with pictographic presentation;
- stickers and reaction images are external graphic objects, not plain-text characters.

## ASCII art and the demoscene

ASCII art uses printable monospaced characters to construct images. ANSI art adds terminal color and cursor-control conventions. PETSCII, ATASCII, teletext mosaics, IBM code-page line drawing, and platform-specific block characters widened the medium.

The demoscene exploited exact character-cell grids, palette attributes, font ROMs, and display hardware. Its works are sensitive to encoding and font: translating bytes without preserving the intended code page can destroy the picture.

Emoji invert part of this tradition. ASCII art builds one picture from many textual glyphs; an emoji renderer builds one displayed picture from one or several abstract characters.

## “Plain text”

Unicode’s plain-text ideal does not mean “visually plain” or “ASCII only.” It means that the data identifies characters and standardized textual relationships, leaving exact typography to rendering.

Emoji test the boundary:

- their usual presentation is colorful;
- many are meaningful only as images;
- ZWJ sequences request ligated artwork;
- vendors can substantially change appearance;
- nevertheless the underlying objects remain searchable, copyable, serializable text.

The result is a deliberately hybrid system: picture-like display carried through character-based infrastructure.

## Mojibake

*Mojibake* (文字化け, “character transformation/garbling”) arises when bytes are decoded under the wrong character encoding.

For example, UTF‑8 `😂` is:

```text
F0 9F 98 82
```

If interpreted incorrectly as Windows‑1252, software may display characters resembling:

```text
ðŸ˜‚
```

Re-encoding that damage can produce multiple layers of corruption.

Mojibake has become:

- an error signature;
- an aesthetic of broken networks and retro computing;
- a device in glitch art;
- an intentional marker of alienation or platform decay;
- a forensic clue to the sequence of mistaken encodings.

**[CULTURAL INTERPRETATION]** Intentional mojibake is an aesthetic reuse of encoding failure, not a formal character-set property.

## Emoji as literature

Emoji have been used for:

- rebus writing;
- translations and adaptations of literary works;
- social-media poetry;
- visual punctuation;
- reaction and stance marking;
- censorship avoidance;
- community-coded euphemisms;
- search and tagging;
- political mobilization.

Their meaning depends heavily on placement, repetition, platform, generation, and community. A code point can be stable while usage changes rapidly.

## Oxford Word of the Year, 2015

**[DOCUMENTED]** Oxford Dictionaries selected 😂 FACE WITH TEARS OF JOY as its 2015 Word of the Year, working with SwiftKey usage data. Contemporary reporting described it as nearly 20% of emoji use in the surveyed US and UK data.

Clarifications:

- the selection came from Oxford Dictionaries, not an amendment declaring the symbol an English lexical word in the historical Oxford English Dictionary;
- it was an editorial “Word of the Year” judgment;
- its cultural importance is clear, but the event does not establish that emoji constitute a natural language.

## MoMA, 2016

**[DOCUMENTED]** In 2016 the Museum of Modern Art acquired Kurita’s 176 original 12×12 DoCoMo designs. MoMA treats the acquisition as design history, analogous in part to its earlier acquisition of the `@` sign.

The acquisition helped canonize Kurita’s set internationally. It does not prove chronological priority over the 1997 SoftBank set; MoMA’s description repeats the then-standard account of “the original emoji.”

---

## Controversies and disputes

## Who made the first emoji?

### Claim A: Kurita, 1999

Carried by:

- DoCoMo histories;
- Kurita interviews;
- MoMA’s acquisition text;
- journalism and popular histories before 2019.

Evidence:

- named designer;
- coherent surviving 176-glyph design;
- corporate service context;
- enormous influence;
- participant testimony.

### Claim B: SoftBank/J‑Phone, 1997

Carried principally after:

- Emojipedia’s 2019 examination of the SkyWalker DP‑211SW and documentation;
- later corrective histories.

Evidence:

- surviving handset and manual;
- apparent deployment two years earlier;
- distinct 90-icon set.

Weaknesses:

- designers unidentified;
- contemporary terminology and exact service scope less clear;
- fewer internal records publicly recovered.

### Finding

**[DISPUTED FIRST]** SoftBank currently has the strongest material claim to the earliest known Japanese mobile-phone emoji set of this lineage. Kurita has the strongest claim to the first famous, named, systematically documented and historically catalytic set. “Inventor of emoji” remains useful shorthand only when qualified.

### Still earlier candidates

Earlier pictographic terminals, Japanese devices, Zapf Dingbats, Videotex, teletext, and symbol fonts are sometimes promoted as “the true first emoji.”

**[CATEGORY DISPUTE]** Whether they count depends on whether *emoji* means:

- any encoded pictograph;
- a selectable mobile-phone pictograph;
- a Japanese text character called emoji;
- the direct ancestor of the Unicode carrier set;
- a colorful inline image used in messaging.

There is no neutral definition that makes every “first” claim commensurable.

## Google versus Apple credit

**[DOCUMENTED]**

- Google authors produced the August 2007 working proposal.
- Apple engineers joined the subsequent effort.
- The January 2009 proposal record is principally Google-authored, with Apple participation elsewhere in the submission and committee history.
- Both companies had commercial interoperability reasons.

Therefore “Apple invented Unicode emoji” is false, while “Google and Apple jointly brought emoji to Unicode” is broadly fair only for the later phase. The 2007 initiative was Google-led.

## Unicode 6.0’s “722 new emoji”

**[CORRECTION]** The 722 figure is the historical union corresponding to carrier sets, not the exact count of brand-new Unicode 6.0 code points. UTS #51 says 114 were already in Unicode 5.2 and 608 were added in Unicode 6.0.

## Private club and corporate power

### Critique

The Consortium has been described as a private club because:

- it is a private nonprofit rather than a treaty organization;
- full voting participation historically required membership resources;
- major technology firms supply substantial staff and funding;
- emoji decisions affect billions of users;
- proposal preparation favors applicants with time, English proficiency, research capacity, and standards knowledge.

The phrase “shadowy emoji overlords,” amplified in press coverage, is humorous rhetoric rather than an institutional description.

### Counterevidence and qualification

- proposals and many committee documents are public;
- anyone may formally submit;
- individual and nonprofit membership categories exist;
- ISO national-body procedures separately participate in character encoding;
- Unicode’s work extends far beyond emoji to digitally disadvantaged scripts;
- many contributors are volunteers, scholars, or language-community experts.

**[BALANCED FINDING]** Formal openness does not erase disparities in practical influence; corporate participation does not by itself prove that decisions are dictated by corporate marketing.

## Cultural politics of food

The original repertoire necessarily overrepresents Japanese mobile life:

- rice balls;
- curry rice;
- ramen;
- sake;
- Japanese “reserved,” “vacancy,” “discount,” and “acceptable” buttons;
- love hotel and hot-spring imagery.

Later additions reflected campaigns for tacos, burritos, dumplings, flatbread, paella, fondue, and other foods.

Critiques argue that:

- food is a major carrier of cultural identity;
- the repertoire often treats one visual form as representative of a diverse cuisine;
- US and Japanese commercial contexts have disproportionate visibility;
- search-volume criteria may reproduce those disparities.

Unicode’s response is structural rather than philosophical: candidates must be distinctive, broadly useful, not overly specific, and not open-ended. This inevitably leaves representational arguments unresolved.

## Flag politics

Flags expose the impossibility of neutral completeness:

- recognized states and territories inherit machine-readable region codes;
- stateless nations and cultural regions often do not;
- governments contest symbols and territorial status;
- vendors suppress politically sensitive flags;
- adding one exceptional flag strengthens claims for many others.

The Tibetan-flag campaign illustrates the problem. Advocates describe it as the flag of a people and political identity; the ordinary regional-indicator mechanism has no eligible independent region code for Tibet.

**[STANDARD]** Unicode’s flag syntax represents identifiers, not endorsement of sovereignty.

**[CRITIQUE]** Reliance on ISO/CLDR still imports geopolitical decisions made elsewhere.

Both statements are correct.

## Skin tone and racialization

Positive assessments emphasize:

- visible inclusion;
- user self-representation;
- a compact modifier mechanism;
- combinability rather than separate atomic characters.

Critiques emphasize:

- a dermatological scale repurposed as racial imagery;
- difficulty representing mixed or context-dependent identity;
- the risk that default yellow becomes racially marked once alternatives exist;
- hostile or ironic deployment of particular tones;
- combinatorial inconsistency in multi-person sequences.

The standard encodes options; it cannot determine their social use.

## Gender and family

Early glyphs often treated male figures as occupational defaults and women through beauty, marriage, or dance roles. ZWJ sequences expanded gendered professions and couples.

Later policy moved toward explicit gender-neutral defaults and more generic family silhouettes.

Critiques pull in opposing directions:

- too little representation;
- too many combinatorial choices;
- reliance on binary gender symbols;
- loss of recognizable specific family forms;
- keyboards becoming unwieldy.

This is not merely a code-space problem. Sequence design can avoid assigning new atomic characters, but keyboards, artwork, search terms, and social interpretation still bear the complexity.

## Han unification

Han unification is not an emoji policy, but it is central to controversy about Unicode’s cultural authority.

**[STANDARD/HISTORICAL RECORD]** Unicode and ISO unified ideographs judged to represent the same abstract Han character across Chinese, Japanese, Korean, and Vietnamese source standards. Regional glyph differences are normally handled through fonts and language context.

### Objections

Japanese and other critics have argued that:

- regional glyph forms may be semantically or bibliographically important;
- unification privileges an abstract character model over particular print traditions;
- missing language metadata can yield an inappropriate glyph;
- the rhetoric of “same character” can conceal difficult historical judgments.

### Standards response

Unicode’s published history says:

- rules drew on national standards including JIS;
- the CJK Joint Research Group and later Ideographic Rapporteur Group coordinated sources;
- source separation and variation mechanisms preserve distinctions where criteria require them;
- duplicating every regional glyph would burden searching, interchange, and equivalence.

### Finding

**[CONTROVERSY]** “Unicode made Japanese look Chinese” is an oversimplification. So is the claim that unification has no cultural cost. The standard encodes abstract character identities; typography and language tagging remain indispensable.

## Tibetan and other script disputes

Tibetan encoding involved debate over character decomposition, ordering, stacks, and compatibility with established textual practice. Similar controversies have occurred for Sinhala, Indic scripts, Mongolian variation behavior, CJK variants, and minority or historic scripts.

**[ABSENCE]** The contested-material search found no primary evidence that Tibetan-script encoding disputes directly determined the emoji design. Tibetan flag politics and Tibetan script encoding are separate questions and should not be merged simply because both involve “Tibet.”

## The Korean mess

RFC 3629 records that Unicode 2.0 and ISO/IEC 10646 Amendment 5 moved and expanded Hangul assignments. The committees judged that little deployed data existed, but the incompatible change became known as the “Korean mess.” Stability policies thereafter pledged against moving encoded characters.

This history explains why obsolete, unpopular, or awkward emoji generally cannot simply be reassigned or deleted.

## Security

### Overlong UTF‑8

Earlier permissive decoders could accept multiple byte sequences for one scalar value, such as `C0 80` for U+0000. Attackers could evade filters that checked one representation while downstream software decoded another.

**[STANDARD]** RFC 3629 prohibits overlong forms, surrogates, and values above U+10FFFF. Decoders must reject invalid sequences.

### Homoglyph and confusable attacks

Unicode contains distinct characters that look alike:

- Latin `a` versus Cyrillic `а`;
- Latin `o`, Greek omicron, and Cyrillic `о`;
- digits and letterlike symbols;
- emoji or symbol glyphs resembling UI controls.

UTR #36 and UTS #39 describe confusables and identifier-security profiles.

The security problem is not that Unicode mistakenly gives the same code to different scripts; often the danger arises because correct script separation creates distinct codes with similar glyphs.

### Invisible characters

ZWJ, variation selectors, bidi controls, combining marks, and tags can make strings that:

- look identical but compare unequal;
- render differently across systems;
- confound cursor movement and length limits;
- bypass naive filters;
- hide material in identifiers or logs.

Emoji sequences increase the gap between byte length, code-point count, UTF‑16 length, grapheme count, and displayed-glyph count.

### Bidirectional attacks

Bidi controls can reorder displayed source code or identifiers without changing logical storage. Emoji may participate as neutral symbols around the attack but are not the root mechanism.

### The BOM

UTF‑16 and UTF‑32 use U+FEFF at the beginning of a stream to indicate byte order. In UTF‑8 it serializes as `EF BB BF`; byte order is irrelevant, so it acts only as a signature.

RFC 3629 warns that stripping or retaining it can affect concatenation, signatures, counts, and protocol processing. It recommends that protocols already fixed to UTF‑8 generally forbid it as unnecessary.

The “BOM breaks Unix scripts” complaint is grounded in practice: interpreters expecting `#!` at the first bytes may fail when `EF BB BF` precedes it. But the BOM is not intrinsically corrupt; the failure is an interface mismatch.

### Spoofed emoji sequences

Unsupported ZWJ sequences may collapse on one platform and expose components on another. Flags may display as letters or missing boxes. Security-sensitive software should not infer identity, nationality, consent, threat, or legal meaning solely from a rendered emoji.

---

## Open questions

1. **Who designed the 1997 J‑Phone/SoftBank set?**  
   No named designer was established in the sources consulted.

2. **Are there earlier direct mobile-emoji ancestors?**  
   Handset, pager, PDA, Videotex, and Japanese appliance archives remain incompletely cataloged. Claims of an earliest set are therefore provisional.

3. **Where is the complete 2000 DoCoMo-to-Unicode submission?**  
   Later institutional accounts mention it, but a complete authoritative proposal was not recovered here.

4. **What exactly did Japanese carriers call their early sets at release?**  
   Later use of “emoji” may normalize terminology that varied by carrier and product.

5. **How much of Kurita’s inspiration can be independently documented?**  
   Manga, signage, weather icons, and pager culture are well-established recollections, but surviving dated sketches and internal memos would allow a firmer reconstruction.

6. **How should counts be reported?**  
   A stable convention distinguishing encoded characters, emoji-capable characters, RGI sequences, and keyboard entries remains necessary.

7. **Can proposal evidence be made less commercially and linguistically biased?**  
   Current search metrics are practical but imperfect proxies for global demand.

8. **Can flag representation ever be both systematic and politically satisfactory?**  
   Delegation to region-code authorities avoids ad hoc Unicode decisions while inheriting those authorities’ exclusions.

9. **How should rendering stability be balanced with vendor freedom?**  
   Pistol demonstrates that semantic interoperability can be affected without changing a single code point.

10. **How should archives preserve emoji?**  
    Preserving bytes is insufficient. Historically accurate reconstruction may require Unicode version, emoji data version, font, vendor artwork, shaping engine, locale, and platform behavior.

11. **Are emoji a script, language, vocabulary, or interface?**  
    Standards classify them principally as symbols and sequences. Cultural descriptions remain contested and metaphorical.

12. **What does a “universal pictorial language” leave out?**  
    Accessibility, cultural convention, local gesture meanings, and linguistic context all resist universality.

---

## Concise chronology

| Date | Event |
|---:|---|
| 1870s | Baudot develops a five-bit telegraph code |
| early 1900s | Murray modifies teleprinter coding practice |
| 1963 | ASA X3.4-1963 ASCII |
| 1968 | US federal ASCII procurement mandate takes effect; ASCII becomes central to network computing |
| 1971 | RFC 20 records ASCII use in the ARPA network |
| 1982 | Scott Fahlman posts `:-)` and `:-(` proposal |
| 1987 | Becker, Collins, and Davis begin Unicode work |
| 1988 | Becker publishes *Unicode 88* |
| 1991 | Unicode Consortium incorporated; Unicode 1.0 |
| 1992 | Thompson and Pike develop UTF‑8 for Plan 9 |
| 1993 | ISO/IEC 10646-1 |
| 1996 | RFC 2044 |
| 1997 | Surviving evidence places a 90-icon J‑Phone/SoftBank set on DP‑211SW |
| 1998 | RFC 2277 makes UTF‑8 support IETF policy; RFC 2279 revises UTF‑8 |
| 1999 | Kurita’s 176 12×12 DoCoMo i-mode set |
| 2000 | Reported early DoCoMo encoding approach does not advance |
| 2003 | RFC 3629 defines modern four-byte UTF‑8 |
| c. 2005 | Japanese carriers increasingly map competitors’ emoji |
| 2006 | Google begins carrier-emoji conversion work |
| May 2007 | UTC agrees to proceed and forms symbols work |
| Aug. 2007 | Momoi, Davis, and Scherer submit L2/07-257 |
| 2008 | Apple launches Japanese iPhone through SoftBank; L2/08-081 develops proposal |
| Jan. 2009 | L2/09-025 consolidated Google proposal |
| 2009 | Unicode 5.2 contains 114 members of eventual carrier union |
| 11 Oct. 2010 | Unicode 6.0 adds remaining 608 carrier-derived characters |
| 2011 | Apple exposes emoji keyboard internationally in iOS 5 |
| 2014–2015 | UTR/UTS #51 drafted and established |
| June 2015 | Emoji 1.0 and Unicode 8.0; five skin-tone modifiers |
| Nov. 2015 | Oxford Dictionaries selects 😂 as Word of the Year |
| 2016 | Profession and gender ZWJ expansion; Apple redraws pistol as water gun |
| 2016 | MoMA acquires Kurita’s 176-glyph set |
| 2017 | Google replaces blob-style people and faces |
| 2017–2018 | Major vendors converge on water-pistol rendering |
| 2019 | Physical-handset research publicizes SoftBank’s 1997 priority claim |
| 2022 | Unicode announces an end to ordinary new flag proposals |
| 9 Sept. 2025 | Unicode and Emoji 17.0 released |
| Sept. 2026 | W3Techs reports UTF‑8 on 99.1% of identifiable websites |

---

## Sources consulted

### Unicode and ISO foundations

- Unicode Standard 17.0 core specification:  
  https://www.unicode.org/versions/Unicode17.0.0/UnicodeStandard-17.0.pdf
- Unicode 17.0 landing page:  
  https://www.unicode.org/versions/Unicode17.0.0/
- Unicode Chapter 22, Symbols:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-22/
- Unicode Chapter 18, East Asia:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/
- Unicode principles:  
  https://www.unicode.org/standard/principles.html
- Unicode history:  
  https://www.unicode.org/history/
- Early years of Unicode:  
  https://www.unicode.org/history/earlyyears.html
- Unicode 1.0 chronology:  
  https://www.unicode.org/history/versionone.html
- Unicode history summary:  
  https://www.unicode.org/history/summary.html
- Unicode publication chronology:  
  https://www.unicode.org/history/publicationdates.html
- Unicode character counts 17.0:  
  https://www.unicode.org/versions/stats/charcountv17_0.html
- ISO/IEC 10646 catalogue search:  
  https://www.iso.org/standard/76835.html
- WG2 principles and procedures, N2352R:  
  https://www.unicode.org/wg2/docs/n2352r.html
- Han Unification History, Appendix E:  
  https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/
- UTN #26, *On the Encoding of Latin, Greek, Cyrillic, and Han*:  
  https://www.unicode.org/notes/tn26/

### Emoji standard and data

- UTS #51, *Unicode Emoji*:  
  https://www.unicode.org/reports/tr51/
- Archived UTR #51 revision with historical 722 table:  
  https://www.unicode.org/standard/reports/tr51/tr51-7.html
- Early archived UTR #51 skin-tone draft:  
  https://www.unicode.org/reports/tr51/tr51-2-archive.html
- Emoji 17.0 charts:  
  https://www.unicode.org/emoji/charts-17.0/
- Emoji 17.0 counts:  
  https://unicode.org/emoji/charts/emoji-counts.html
- Emoji proposal index:  
  https://unicode.org/emoji/charts/emoji-proposals.html
- Emoji proposal status:  
  https://www.unicode.org/emoji/emoji-proposals-status.html
- Proposal guidelines:  
  https://www.unicode.org/emoji/proposals.html
- Emoji and pictograph FAQ:  
  https://www.unicode.org/faq/emoji_dingbats.html
- Emoji 17.0 data directory:  
  https://www.unicode.org/Public/17.0.0/emoji/
- `emoji-sequences.txt`:  
  https://www.unicode.org/Public/17.0.0/emoji/emoji-sequences.txt
- `emoji-zwj-sequences.txt`:  
  https://www.unicode.org/Public/17.0.0/emoji/emoji-zwj-sequences.txt
- `emoji-test.txt`:  
  https://www.unicode.org/Public/17.0.0/emoji/emoji-test.txt
- Unicode character names charts:  
  https://unicode.org/charts/nameslist/mainList.html
- Miscellaneous Symbols and Pictographs chart:  
  https://www.unicode.org/charts/PDF/U1F300.pdf
- Transport and Map Symbols chart:  
  https://www.unicode.org/charts/PDF/U1F680.pdf
- Supplemental Symbols and Pictographs chart:  
  https://www.unicode.org/charts/PDF/U1F900.pdf

### Original Unicode emoji proposals

- L2/07-257, *Working Draft Proposal for Encoding Emoji Symbols*:  
  https://www.unicode.org/L2/L2007/07257-emoji-wd.html
- L2/08-081, working-draft proposal:  
  https://www.unicode.org/L2/L2008/08081-emoji-wd.html
- L2/09-025, *Proposal for Encoding Emoji Symbols*:  
  https://www.unicode.org/L2/L2009/09025-emoji.pdf
- L2/10-132, *Emoji Symbols: Background Data*:  
  https://unicode.org/L2/L2010/10132-emojidata.pdf
- L2/16-337, Emoji Subcommittee terminology and process:  
  https://www.unicode.org/L2/L2016/16337-terminology-process.pdf
- L2/16-160, profession emoji proposal:  
  https://www.unicode.org/L2/L2016/16160-emoji-professions.pdf
- L2/16-181, gender emoji ZWJ sequences:  
  https://www.unicode.org/L2/L2016/16181-gender-zwj-sequences.pdf
- L2/19-189, consistent gender options:  
  https://www.unicode.org/L2/L2019/19189-gender-zwj-recs.pdf
- Public review feedback concerning emoji mechanisms and diversity:  
  https://www.unicode.org/review/pri321/feedback.html
- 2008 public-review criticism, “A Very Pretty Can of Worms Indeed”:  
  https://unicode.org/mail-arch/unicode-ml/y2008-m12/0092.html
- Unicode blog, 2016 UTR #51 update:  
  https://blog.unicode.org/2016/08/proposed-update-utr-51-unicode-emoji.html
- Unicode blog, past and future of flag emoji:  
  https://blog.unicode.org/2022/03/the-past-and-future-of-flag-emoji.html

### Japanese carrier history

- NTT institutional interview with Kurita and Sasahara:  
  https://www.global.ntt/insights-hub/the-worlds-most-familiar-face/
- MoMA acquisition history:  
  https://www.moma.org/interactives/moma_through_time/2010/acquisition-of-and-emoji/
- NTT DoCoMo 2014 carrier interoperability announcement:  
  https://www.docomo.ne.jp/info/news_release/2014/04/24_00.html
- ICANN Emoji Study Group report:  
  https://itp.cdn.icann.org/en/files/committees-and-working-groups/emoji-sld-study-group-report-findings-19sep19-en.pdf
- Emojipedia, correction concerning the 1997 SoftBank set:  
  https://blog.emojipedia.org/correcting-the-record-on-the-first-emoji-set/
- USPTO-preserved copy of the correction:  
  https://ptacts.uspto.gov/ptacts/public-informations/petitions/1547642/download-documents?artifactId=9SmEQVI-_Ozs6nBHI-6mNtv8ZbAGVL-ADZJPD9RijqL73QOU0J0EgU4
- Emojipedia carrier history overview:  
  https://blog.emojipedia.org/major-moments-in-emoji-history-1995-to-2025/
- GSMA presentation on Japanese messaging interoperability:  
  https://www.gsma.com/solutions-and-impact/technologies/networks/wp-content/uploads/2018/07/MWCS18-RCS-Seminar-KDDI_DOCOMO_SoftBank-1.pdf

### UTF‑8 and Internet standards

- RFC 20, ASCII format for network interchange:  
  https://www.rfc-editor.org/rfc/rfc20
- RFC 1341, MIME:  
  https://www.rfc-editor.org/rfc/rfc1341
- RFC 1345, character mnemonics and coded sets:  
  https://www.rfc-editor.org/rfc/rfc1345
- RFC 2044, early UTF‑8 specification:  
  https://www.rfc-editor.org/rfc/rfc2044
- RFC 2277, IETF charset policy:  
  https://www.rfc-editor.org/rfc/rfc2277
- RFC 2279, revised UTF‑8:  
  https://www.rfc-editor.org/rfc/rfc2279
- RFC 3629, current Internet UTF‑8:  
  https://www.rfc-editor.org/rfc/rfc3629
- RFC 5198, Unicode network interchange:  
  https://www.rfc-editor.org/rfc/rfc5198
- IANA Character Sets registry:  
  https://www.iana.org/assignments/character-sets
- IANA charset registrations:  
  https://www.iana.org/assignments/charset-reg

### Web adoption

- W3C Encoding specification:  
  https://www.w3.org/International/docs/encoding/
- W3C, who uses Unicode:  
  https://www.w3.org/International/questions/qa-who-uses-unicode.en.html
- W3C, choosing an encoding:  
  https://www.w3.org/International/questions/qa-choosing-encodings.en
- W3C internationalization quick tips:  
  https://www.w3.org/International/quicktips/
- W3Techs UTF‑8 usage by site ranking:  
  https://w3techs.com/technologies/breakdown/en-utf8/ranking

### Security and text algorithms

- UTR #36, *Unicode Security Considerations*:  
  https://www.unicode.org/reports/tr36/
- UTS #39, *Unicode Security Mechanisms*:  
  https://www.unicode.org/reports/tr39/
- UAX #9, *Unicode Bidirectional Algorithm*:  
  https://www.unicode.org/reports/tr9/
- UAX #15, *Unicode Normalization Forms*:  
  https://www.unicode.org/reports/tr15/
- UAX #29, *Unicode Text Segmentation*:  
  https://www.unicode.org/reports/tr29/

### Cultural politics and contested material

- TIME interview with Mark Davis:  
  https://time.com/4244795/emoji-consortium-mark-davis/
- TIME on women and profession emoji:  
  https://time.com/4325949/new-emoji-women/
- TIME on Oxford’s 2015 choice:  
  https://time.com/4114886/oxford-word-of-the-year-2015-emoji/
- WIRED, emoji diversity and cultural politics:  
  https://www.wired.com/2015/11/emoji-diversity-politics-culture/
- WIRED, Tibetan and political flag disputes:  
  https://www.wired.com/story/flag-emoji-politics-tibet-china/
- Axios on the pistol transition:  
  https://www.axios.com/2018/04/11/twitters-pistol-emoji-is-now-a-water-gun
- Kimura-Thollander and Kumar, *Examining the “Global” Language of Emojis*:  
  https://static1.squarespace.com/static/59f549a3b7411c736b42936a/t/5c8b4b3b0852290d5ef83b12/1552632685811/Kimura-Thollander_Kumar_CHI2019.pdf
- Unicode FAQ on emoji and flags:  
  https://www.unicode.org/faq/emoji_dingbats.html
- Unicode proposal archive, including accepted proposal provenance:  
  https://unicode.org/emoji/charts/emoji-proposals.html

### Historical background requested in the brief

- Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley, 1980, Internet Archive record:  
  https://archive.org/details/codedcharactersets
- ECMA‑6 standard catalogue:  
  https://ecma-international.org/publications-and-standards/standards/ecma-6/
- ISO/IEC 646 catalogue search:  
  https://www.iso.org/standard/4777.html
- ISO/IEC 2022 catalogue search:  
  https://www.iso.org/standard/22747.html
- ISO/IEC 8859 series catalogue:  
  https://www.iso.org/standard/28245.html
- IBM documentation portal for EBCDIC and code pages:  
  https://www.ibm.com/docs/en/i/7.5.0?topic=information-coded-character-set-identifiers
- Rob Pike, *UTF‑8 history*:  
  https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt
- Unicode’s history pages and *Unicode 88* catalogue entry:  
  https://www.unicode.org/history/publicationdates.html
