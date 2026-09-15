# The East Asian double-byte encodings: Shift-JIS, EUC, GB 2312, GBK, Big5: Research Dossier

> **Scope.** This dossier concerns the principal pre-Unicode multibyte encodings of Japanese, Korean, simplified Chinese, and traditional Chinese text: Shift-JIS, the EUC family, GB 2312 and GBK, and Big5. GB 18030, HKSCS, Windows code pages, ISO-2022, and Unicode are included where they explain those systems’ origins, deployment, incompatibilities, or survival.
>
> **Evidence labels**
>
> - **[STD]** normative standard, RFC, registry, or official specification.
> - **[DOC]** contemporaneous manual, mapping table, institutional history, or government record.
> - **[RECOLLECTION]** participant’s later account.
> - **[SCHOLARLY]** historical or technical reconstruction.
> - **[DISPUTED]** competing accounts or a claim whose evidence is incomplete.
> - **[FOLKLORE]** widely repeated story lacking adequate primary documentation.
> - **[MODERN]** behavior established retrospectively by browsers, Unicode mappings, or contemporary compatibility specifications rather than by the original encoding.

---

## Basic identification

| Name | Standard or defining document | First year | Code-unit width and character length | Principal repertoire | Status in 2026 |
|---|---|---:|---|---|---|
| **Shift-JIS** | Initially an industry encoding; JIS X 0208:1997 Appendix 1 later documented the transformation. IANA: `Shift_JIS`; Microsoft variant CP932; web form also called Windows-31J | **1982** | 8-bit bytes; one or two bytes per character | JIS X 0201 Roman and half-width katakana plus JIS X 0208; vendor forms add NEC/IBM characters | Legacy but still required for web decoding; UTF-8 preferred for new material |
| **EUC-JP** | Extended Unix Code packed format; registered by IANA; standardized through OSF, Unix International, and Unix System Laboratories Pacific profiles | c. **1980s** | 8-bit bytes; one, two, or three bytes | ASCII/JIS Roman, JIS X 0208, half-width katakana, optionally JIS X 0212 | Legacy Unix/Japanese interchange encoding; web decoder remains required |
| **EUC-KR** | EUC profile of KS C 5601-1987, now KS X 1001 | **1987-era profile** | 8-bit bytes; one or two bytes in strict EUC-KR | ASCII/KS X 1003 plus KS X 1001: 2,350 Hangul syllables, 4,888 Hanja codes, symbols | Strict repertoire obsolete; the web label denotes the larger Windows-949/UHC mapping |
| **EUC-CN / “GB2312” encoding** | EUC representation of **GB 2312-1980**, ISO-IR 58 | **1980/1981** | 8-bit bytes; one or two bytes | 6,763 simplified-oriented Han characters plus 682 symbols and letters | GB/T 2312 remains an official recommended standard, but GBK/GB 18030 supersede it in general interchange |
| **GBK** | *Chinese Internal Code Specification* (汉字内码扩展规范), Chinese IT Standardization Technical Committee, 1995; commonly Microsoft CP936 | **1995** | 8-bit bytes; one or two bytes | GB 2312 plus the Unicode 2.1-era BMP repertoire needed in China, including the main CJK Unified Ideographs block | Officially superseded by GB 18030; still pervasive as CP936 and as the web meaning of many “GB2312” labels |
| **Big5** | Industry specification prepared under Taiwan’s Institute for Information Industry; Big5-1984; later Big5-2003 and vendor variants | **1984** | 8-bit bytes; one or two bytes | Traditional Chinese: 13,053 Han code assignments, 13,051 unique Han characters, plus symbols | Legacy de facto standard; retained in Taiwan/Hong Kong data and mandated as a browser decoder |
| **Big5-HKSCS** | Hong Kong Supplementary Character Set, 1999, revised 2001, 2004, 2008 | **1999** | Big5-compatible one/two-byte form, with assigned extension areas | Big5 plus Cantonese, personal-name, place-name, government, and other Hong Kong characters | Maintained primarily through Unicode mappings; the web’s Big5 decoder incorporates HKSCS and common extensions |
| **GB 18030** | GB 18030-2000, -2005, and mandatory **GB 18030-2022** | **2000** | One, two, or four bytes | Compatibility with GBK plus algorithmic coverage tied to ISO/IEC 10646/Unicode, with edition-specific mappings | Current mandatory Chinese national encoding standard; effective 1 August 2023 for the 2022 edition |

**[STD]** GB 2312 was published on 9 March 1980 and implemented on 1 May 1981. In 2017 it changed from mandatory `GB` to recommended `GB/T` status. China’s standards catalogue nevertheless lists GB/T 2312-1980 as current. [Chinese national standards catalogue](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=5664A728BD9D523DE3B99BC37AC7A2CC)

**[STD]** GB 18030-2022 is a mandatory national standard, not merely a voluntary Internet charset. Chinese authorities formally announced the revision in July 2022. [Standardization Administration of China announcement](https://www.sac.gov.cn/Standards/Release/art/2022/art_3555a3d3ce1c49dfb06a2c615a1d1190.html)

**[MODERN]** On the web, these names no longer necessarily denote historically pure encodings. WHATWG maps labels to a deliberately consolidated set: “GB2312” labels select **GBK**; “EUC-KR” selects a mapping incorporating **Windows-949/UHC**; “Shift_JIS” uses a JIS X 0208 index containing former NEC and IBM extensions; and “Big5” incorporates HKSCS and other deployed extensions. [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/)

---

## The code in detail

### 1. The common architectural problem

**[STD]** ASCII and ISO 646 supply only 128 seven-bit positions. Even an unstructured eight-bit set supplies only 256. Japanese, Korean, and Chinese require thousands of graphic characters, before variants, personal-name characters, historical forms, kana, Hangul, punctuation, Greek, Cyrillic, or technical symbols are counted.

The key standards therefore separated two things:

1. a **coded character set or repertoire**, often arranged as a 94×94 matrix; and
2. an **encoding form** that puts matrix coordinates into byte streams.

A 94×94 set has 8,836 potential positions. In ISO-2022 notation, each coordinate uses `0x21–0x7E`; row 1 cell 1 is `21 21`, row 94 cell 94 is `7E 7E`. The exclusion of C0 controls, space, and `DEL` permitted use in seven-bit communication systems.

**[STD]** ISO 2022 could announce and invoke such sets with escape sequences. EUC instead sets the high bit on matrix bytes, normally changing `21–7E` to `A1–FE`. Shift-JIS mathematically folds the JIS matrix into discontinuous lead- and trail-byte ranges that coexist with JIS X 0201.

This makes “double-byte character set” historically understandable but technically imprecise. Shift-JIS and the EUCs are **variable-length multibyte encodings**: ASCII remains one byte; Shift-JIS kana are one byte; EUC-JP can use three. GB 18030 additionally uses four-byte sequences.

---

### 2. JIS X 0208: the repertoire beneath Shift-JIS and EUC-JP

#### Original table

**[DOC]** JIS C 6226-1978 defined 6,802 assigned characters:

- 453 non-kanji;
- 2,965 Level 1 kanji;
- 3,384 Level 2 kanji.

The IPSJ institutional history says the standard arose from work beginning in 1969 and a 1971 provisional list, with later corpus and administrative studies. [IPSJ Computer Museum history](https://museum.ipsj.or.jp/en/computer/main/0111.html)

The often-seen figure **6,879** describes later JIS X 0208 editions, not the original 1978 assignment count.

A compact structural map is:

| JIS rows (*ku*) | Contents |
|---|---|
| 1–2 | punctuation and symbols |
| 3 | full-width Roman letters and digits |
| 4 | hiragana |
| 5 | katakana |
| 6 | Greek |
| 7 | Cyrillic |
| 8 | box drawing |
| 9–15 | mostly unassigned/reserved |
| 16–47 | Level 1 kanji |
| 48–84 | Level 2 kanji |
| 85–94 | originally unassigned or reserved; subsequently important to extensions |

**[DOC]** Level 1 was ordered by a selected representative Japanese reading in *gojūon* order. Level 2 was ordered by Kangxi radical and stroke count. Variants were sometimes placed adjacent to a reference form. This is a table order useful for lookup and conversion, not a generally adequate linguistic collation.

**[STD]** Later revisions include JIS C 6226-1983, renaming to JIS X 0208 in 1987, and revisions in 1990 and 1997. RFC 1468 records the old and new names and distinguishes escape designation for the 1978 and 1983 editions. [RFC 1468](https://www.rfc-editor.org/rfc/rfc1468.html)

#### Expressive limits

**[STD]** JIS X 0208 contains hiragana, katakana, Greek, Cyrillic, symbols, and thousands of kanji, but it is not a complete Japanese repertoire. Historical characters, many personal-name variants, obscure kanji, Ainu extensions, and later-added characters require JIS X 0212, JIS X 0213, vendor gaiji, or Unicode.

**[DOC]** Its encoded order does not reproduce dictionary collation, locale-sensitive collation, or modern Unicode collation. Bytewise sorting separates single-byte Roman characters, kana, and kanji according to encoding geometry, not Japanese lexical order.

---

### 3. Shift-JIS

#### Byte layout

The historically central byte classes are:

| Byte range | Meaning |
|---|---|
| `00–1F` | C0 controls |
| `20` | space |
| `21–7E` | JIS Roman/ASCII-range graphics |
| `7F` | delete; excluded as a trail byte |
| `80` | unused in strict original Shift-JIS; assigned by some vendor/web forms |
| `81–9F` | first-byte range for double-byte characters |
| `A0` | normally unused |
| `A1–DF` | one-byte half-width katakana |
| `E0–EF` | additional double-byte lead range in original JIS X 0208 Shift-JIS |
| `F0–FC` | vendor/user-defined or later extension leads, depending on variant |
| `FD–FF` | generally invalid |

A double-byte trail is:

- `40–7E`, or
- `80–FC`.

`7F` is deliberately skipped. Consequently a trail byte can look like ASCII punctuation, a digit, or a letter.

**[STD]** The modern web decoder accepts leads `81–9F` and `E0–FC` and trails `40–7E` or `80–FC`. Its pointer calculation uses 188 trail positions per lead. [WHATWG Shift_JIS decoder](https://encoding.spec.whatwg.org/#shift_jis-decoder)

#### Why it is called “Shift”

**[SCHOLARLY]** The JIS 94×94 coordinates are transformed—“shifted”—into gaps around the JIS X 0201 single-byte ranges. It is not stateful shifting like ISO 2022’s `SI`, `SO`, or `ESC`; no persistent shift state exists. Each valid lead identifies a following trail.

For JIS bytes `j1 j2` in `21–7E`, the transformation combines two JIS rows into one Shift-JIS lead range and divides odd and even rows across lower and upper trail regions. The result economizes byte space and avoids explicit escape sequences.

#### ASCII compatibility and the `5C` problem

**[STD]** JIS X 0201 Roman replaces ASCII backslash at `0x5C` with **YEN SIGN** and ASCII tilde at `0x7E` with **OVERLINE**. RFC 1468 states this explicitly. [RFC 1468](https://www.rfc-editor.org/rfc/rfc1468.html)

**[MODERN]** Microsoft and web mappings generally decode single-byte `5C` as Unicode `U+005C REVERSE SOLIDUS`, while Japanese fonts and historical interfaces may display it as `¥`. Thus byte identity, Unicode identity, and glyph appearance can disagree.

**[DOC]** The more dangerous “5C problem” is that `0x5C` is also a legal **second byte** in Shift-JIS. Software that scans bytes without respecting character boundaries may mistake it for:

- a C/Java-style escape introducer;
- a DOS/Windows path separator;
- a quoting escape in SQL or another language.

For example, a two-byte Japanese character ending in `5C` can be broken if a program inserts another backslash or interprets the trail as syntax. The same general issue applies to trail bytes `22` (`"`), `27` (`'`), and other ASCII delimiters in encodings whose decoders accept them.

**[STD/MODERN]** WHATWG records a 2011 attack using an invalid Shift-JIS lead plus a quotation-mark byte to create disagreement between a producer’s validation and a consumer’s decoding. Its mandated error behavior is intended to remove such divergences. [WHATWG security background](https://encoding.spec.whatwg.org/#security-background)

#### Half-width katakana

**[STD]** Bytes `A1–DF` encode the JIS X 0201 katakana set as one byte each. “Half-width” reflects terminal and typesetting cell conventions: these forms occupied one cell where ideographic and full-width kana normally occupied two. The width distinction became entrenched in data and interfaces even though it is fundamentally presentation-related.

They cannot by themselves represent every ordinary katakana spelling elegantly; voiced marks may be separate spacing characters. Unicode preserves compatibility characters `U+FF61–U+FF9F` for round-trip fidelity.

#### Controls and elementary characters

In ordinary Shift-JIS-family text:

- NUL = `00`
- horizontal tab = `09`
- LF = `0A`
- CR = `0D`
- CRLF = `0D 0A`
- space = `20`
- DEL = `7F`

No escape sequence is required to enter or leave double-byte mode. Case exists only for embedded Roman, Greek, or Cyrillic alphabets; Japanese kana and kanji have no uppercase/lowercase distinction.

#### Error and synchronization behavior

**[STD]** A decoder knows a multibyte character only after seeing a valid lead. If the following byte is invalid, modern decoders emit an error/replacement character and may reconsider the offending byte according to their specified algorithm.

**[SCHOLARLY]** Shift-JIS is only locally self-synchronizing. Starting at an arbitrary byte is ambiguous because many legal trail bytes also look like ASCII and some overlap kana/lead domains. A parser normally recovers after one plausible lead/trail decision, but there is no UTF-8-like invariant saying that continuation bytes can never be initial bytes. Corruption can therefore shift interpretation or expose syntax.

**[RECOLLECTION]** Mark Davis’s account of Unicode’s early years says Apple experiments found Shift-JIS “difficult and easy to corrupt.” That is a retrospective participant statement, not the text of JIS. [Unicode early-years history](https://www.unicode.org/history/earlyyears.html)

---

### 4. EUC: Extended Unix Code

#### Design principle

**[STD]** EUC is an encoding framework derived from ISO 2022’s code-set model but designed for Unix eight-bit processing without repeated designation escape sequences. Code set 0 occupies ASCII/GL; code set 1 is normally invoked in GR by setting the high bit; code sets 2 and 3 use single-shift bytes `8E` and `8F`.

The four logical sets are:

| Set | Normal EUC representation |
|---|---|
| CS0 | one byte, ordinarily `00–7F` |
| CS1 | national two-byte set, ordinarily `A1–FE A1–FE` |
| CS2 | `8E` followed by set-specific bytes |
| CS3 | `8F` followed by set-specific bytes, often two more bytes |

No persistent state survives between characters. `8E` and `8F` are per-character introducers, not open-ended modes.

#### EUC-JP

| Bytes | Repertoire |
|---|---|
| `00–7F` | ASCII or JIS X 0201 Roman, depending on profile/mapping |
| `A1–FE A1–FE` | JIS X 0208 |
| `8E A1–DF` | JIS X 0201 half-width katakana |
| `8F A1–FE A1–FE` | JIS X 0212 supplementary characters |

**[STD]** IANA attributes its registered packed form to OSF, Unix International, and Unix System Laboratories Pacific. [IANA Character Sets registry](https://www.iana.org/assignments/character-sets)

**[DOC]** An ARIB specification gives the same ranges and identifies `20` as space, `7F` as delete, `0D 0A` as newline, and `09` as tab. [ARIB STD-B24 EUC-JP table](https://www.arib.or.jp/english/html/overview/doc/6-STD-B24v6_4-2p3-1-E1.pdf)

**[SCHOLARLY]** EUC-JP is easier to recognize and resynchronize than Shift-JIS because its two-byte graphic bytes normally have the high bit set and ASCII remains in `00–7F`. Nevertheless, corruption involving `8E`, `8F`, or missing bytes can consume the wrong number of following bytes.

#### EUC-CN

Strict EUC-CN is simple:

- ASCII: `00–7F`
- GB 2312: `A1–FE A1–FE`

A GB 2312 matrix position is encoded by adding `0x80` to each seven-bit coordinate. Thus row 16, cell 1 is `B0 A1`.

**[MODERN]** This strict meaning is frequently obscured by the label `gb2312`, which browsers interpret as GBK for compatibility with deployed Chinese pages.

#### EUC-KR

Strict EUC-KR is similarly:

- ASCII/KS X 1003: `00–7F`
- KS X 1001: `A1–FE A1–FE`

The 1987 KS repertoire contains:

- symbols and punctuation;
- Hangul jamo;
- Roman, Greek, Cyrillic, hiragana, and katakana;
- 2,350 precomposed Hangul syllables;
- 4,888 Hanja code positions, representing 4,620 unique Hanja because readings caused duplication.

**[DOC]** Microsoft documentation identifies 2,350 Hangul, 4,888 Hanja, and 986 other characters in Wansung/KS C 5601-1987. [Archived Microsoft Knowledge Base article](https://ftp.zx.net.nz/pub/archive/ftp.microsoft.com/MISC/KB/en-us/170/557.HTM)

**[STD/MODERN]** The web Encoding Standard’s `EUC-KR` index includes Unified Hangul Code/Windows-949 extensions and covers all 11,172 modern precomposed Hangul syllables. That is not the original strict EUC-KR repertoire. [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/)

#### EUC-TW

Though not one of the five names in the title, EUC-TW completes the design picture. It encodes CNS 11643 plane 1 with two bytes; other planes use a four-byte form beginning with `8E`, followed by a plane selector and two row/cell bytes. It illustrates that “EUC” is a framework, not one repertoire.

---

### 5. GB 2312

#### Repertoire and table

**[STD]** GB 2312-1980, *信息交换用汉字编码字符集 基本集* (“Coded Chinese Graphic Character Set for Information Interchange—Primary Set”), assigns:

- 6,763 Han characters;
- 682 non-Han graphics;
- 7,445 assigned characters in all.

Its 94×94 layout is:

| Rows | Contents |
|---|---|
| 1–9 | punctuation, mathematical and technical symbols, digits and Roman letters, Japanese kana, Greek, Cyrillic, Pinyin forms, Bopomofo |
| 10–15 | unassigned |
| 16–55 | Level 1: 3,755 common Han characters, ordered primarily by Pinyin |
| 56–87 | Level 2: 3,008 less-common Han characters, ordered by radical and stroke count |
| 88–94 | unassigned |

**[STD]** The official record says the former Ministry of Electronics Industry and State Bureau of Standards organized the work. It does not identify a single inventor. [SAC history](https://www.sac.gov.cn/jdbnhbz/bzgs/art/2021/art_5e8ba919bec34784b55960ea23175ad3.html)

#### What it represents—and omits

**[STD]** GB 2312 was designed as a **basic set** for the simplified-character environment of the PRC. It includes the most frequently needed simplified forms but is not an encoding of “the Chinese language” in full.

It cannot reliably represent:

- many traditional forms;
- numerous rare, historical, religious, and dialect characters;
- many personal and place names;
- later scientific or administrative additions;
- all characters used in Hong Kong, Taiwan, Japan, Korea, or premodern literature.

**[SCHOLARLY]** Claims that it covers “99.99% of Chinese text” usually refer to aggregate character frequency in selected modern corpora. They do not imply coverage of 99.99% of names, documents, or distinct characters. The figure must not be treated as a guarantee.

**[DISPUTED]** A later Taiwanese account says the appearance of CCCII in 1980 pressured the PRC into rapidly preparing GB 2312. This is an interesting regional interpretation but is not substantiated by the Chinese standard’s official history or a contemporaneous committee record located here. [Academia Sinica-hosted character-code history](https://idv.sinica.edu.tw/bear/charcodes/Section12.htm)

---

### 6. GBK

#### Structure

GBK keeps ASCII single bytes and broadens the two-byte space:

| Component | Range |
|---|---|
| ASCII | `00–7F` |
| Lead byte | `81–FE` |
| Trail byte | `40–7E` or `80–FE` |
| Excluded trail | `7F` |

This permits 126×190 theoretical double-byte combinations, far more than GB 2312’s 94×94 matrix.

**[STD/DOC]** The 1995 *Chinese Internal Code Specification* was prepared by the Chinese IT Standardization Technical Committee. It provided a migration path from GB 2312 and GB 13000.1-93/Unicode-era repertoire requirements. [IANA GBK registration dossier](https://data.iana.org/archive/ietf-charsets/msg01038.html)

**[DOC]** Microsoft CP936 is its most influential implementation. CP936 historically began as a GB 2312 code page and was expanded for GBK; Microsoft also assigned the euro sign at single byte `80`, which is outside strict GBK.

**[MODERN]** Browser `GBK` incorporates deployed CP936-like behavior, including `80 → U+20AC`. Labels such as `chinese`, `gb2312`, `gb_2312-80`, `iso-ir-58`, and `x-gbk` select the web GBK decoder. This compatibility choice deliberately sacrifices the narrower historical meaning of GB 2312.

#### Expressive limits

GBK substantially expanded traditional characters and CJK coverage, but its finite two-byte space could not cover all of ISO/IEC 10646. It also inherited ambiguity from multiple vendor mappings and private-use assignments. GB 18030 was designed to remove the repertoire ceiling.

---

### 7. GB 18030: GBK’s mandatory successor

GB 18030 uses:

| Form | Pattern |
|---|---|
| ASCII | `00–7F` |
| Two-byte | GBK-compatible lead/trail combinations |
| Four-byte | `81–FE 30–39 81–FE 30–39` |

The four-byte form provides an algorithmically indexed space large enough for Unicode/ISO 10646 coverage.

**[STD]** GB 18030-2000 became mandatory for relevant products sold in China; later editions were issued in 2005 and 2022. The 2022 standard updates coverage through later CJK extensions and defines implementation levels.

**[QUALIFICATION]** “GB 18030 encodes all of Unicode” is broadly correct as a repertoire statement for the Unicode edition targeted by the applicable GB 18030 revision. It does **not** mean every Unicode scalar uses two bytes, nor that every historical edition maps every later Unicode assignment. Edition identification matters.

**[DOC/CONTROVERSY]** Unicode’s Peter Constable documented mapping changes in GB 18030-2022 that are disruptive to implementations attempting both Unicode round-trip behavior and CESI conformance. This is a technical standards conflict, not merely an implementation bug. [Unicode L2/22-274](https://www.unicode.org/L2/L2022/22274-disruptive-changes.pdf)

---

### 8. Big5

#### Byte layout

| Component | Range |
|---|---|
| ASCII | `00–7F` |
| Lead byte | conventionally `81–FE`; original assigned core largely `A1–F9` |
| Low trail block | `40–7E` |
| High trail block | `A1–FE` |
| Gap | `7F–A0` is not a trail range |

Each lead supports 157 possible trails: 63 in `40–7E` and 94 in `A1–FE`.

The original core includes:

- punctuation, symbols, and phonetic material;
- 5,401 frequently used Han characters;
- 7,652 less-common Han assignments;
- 13,053 Han assignments, but 13,051 unique Han characters because two were duplicated.

Within the two Han frequency groups, ordering is principally by stroke count and then radical. This table order is not an adequate Mandarin, Cantonese, or dictionary collation.

#### Scope

Big5 is traditional-Chinese oriented, serving Taiwan and later Hong Kong deployments. It does not provide complete coverage of:

- all CNS 11643 planes;
- Cantonese-specific characters;
- all personal and place names;
- rare historical ideographs;
- every traditional/simplified correspondence;
- Japanese kana/kanji distinctions or Korean Hangul.

Reserved and user-defined areas therefore became fertile ground for incompatible extensions.

#### Name and “Big Five” story

**[DOC]** Taiwan’s official CNS service identifies Big5-1984 as the earliest Institute for Information Industry version. [Taiwan CNS 11643 character-code history](https://www.cns11643.gov.tw/pageView.jsp?ID=9)

**[DOC]** The Chinese Digitalization Technology Promotion Foundation says III planned Big5 in 1984 to avoid control ranges and provide a common PC internal code for five major application packages. [CMEX account](https://www.cmex.org.tw/page.jsp?ID=30&SN=chinese&la=0)

**[DISPUTED/FOLKLORE]** “Big5 was named after the five companies that created it” and “after five major software packages” both circulate. The official Taiwanese account consulted here supports the **five major packages** explanation more directly. The identities and institutional roles of an exact canonical “five companies” are not established by the primary material located. The company-origin form should therefore be repeated only as folklore or a secondary reconstruction.

#### Vendor variants

Important variants include:

- Big5-ETen;
- Microsoft CP950;
- IBM Big5 mappings;
- Big5-2003;
- Big5-HKSCS;
- user-defined characters and font-bound gaiji.

Two documents labeled “Big5” can consequently assign the same bytes differently. Conversion through a generic Unicode table may lose or alter vendor/private characters.

---

### 9. HKSCS

**[DOC]** Hong Kong’s government created the Government Common Character Set in 1995 for interdepartmental use. In 1998 it began revising it for public use; the result was published as HKSCS in September 1999. HKSCS-2001 added 116 characters, and HKSCS-2004 added 123 more. [Hong Kong government HKSCS history](https://www.ccli.gov.hk/en/hkscs/what_is_hkscs.html)

HKSCS covers locally necessary material—especially Cantonese characters, names, and Hong Kong administrative usage—that base Big5 omitted. Successive editions aligned characters with ISO/IEC 10646, replacing early private-use mappings where standardized Unicode positions became available.

**[MODERN]** WHATWG’s single Big5 index combines Big5, HKSCS, and common deployed extensions. That is useful for recovering web content but is not an exact edition of Big5-1984, HKSCS-1999, or CP950.

---

## Worked byte-by-byte examples

All hexadecimal bytes below are shown in stream order.

### Example A: Japanese `日本語` — “Japanese language”

| Character | Unicode | Shift-JIS / CP932 | EUC-JP | UTF-8 |
|---|---:|---:|---:|---:|
| 日 | U+65E5 | `93 FA` | `C6 FC` | `E6 97 A5` |
| 本 | U+672C | `96 7B` | `CB DC` | `E6 9C AC` |
| 語 | U+8A9E | `8C EA` | `B8 EC` | `E8 AA 9E` |
| Full string | — | `93 FA 96 7B 8C EA` | `C6 FC CB DC B8 EC` | `E6 97 A5 E6 9C AC E8 AA 9E` |

The Shift-JIS bytes demonstrate the structural hazard: `7B` in `96 7B` is a trail byte but is ASCII `{` when viewed in isolation.

Add ASCII punctuation and newline:

`日本語.\r\n`

- Shift-JIS: `93 FA 96 7B 8C EA 2E 0D 0A`
- EUC-JP: `C6 FC CB DC B8 EC 2E 0D 0A`
- UTF-8: `E6 97 A5 E6 9C AC E8 AA 9E 2E 0D 0A`

Space and punctuation remain ASCII bytes in all three examples.

### Example B: Simplified Chinese `中国` — “China”

| Character | Unicode | GB 2312/EUC-CN | GBK | UTF-8 |
|---|---:|---:|---:|---:|
| 中 | U+4E2D | `D6 D0` | `D6 D0` | `E4 B8 AD` |
| 国 | U+56FD | `B9 FA` | `B9 FA` | `E5 9B BD` |
| Full string | — | `D6 D0 B9 FA` | `D6 D0 B9 FA` | `E4 B8 AD E5 9B BD` |

GBK preserves GB 2312 byte assignments, which made migration practical.

The traditional form `中國` cannot be represented wholly in GB 2312 because `國` is outside its simplified basic repertoire. GBK and Big5 can represent it.

### Example C: Traditional Chinese `中文` — “Chinese writing/language”

| Character | Unicode | Big5 | GB 2312/GBK | UTF-8 |
|---|---:|---:|---:|---:|
| 中 | U+4E2D | `A4 A4` | `D6 D0` | `E4 B8 AD` |
| 文 | U+6587 | `A4 E5` | `CE C4` | `E6 96 87` |
| Full string | — | `A4 A4 A4 E5` | `D6 D0 CE C4` | `E4 B8 AD E6 96 87` |

This illustrates why “double-byte Chinese” is not one encoding. The same characters have unrelated byte values in Big5 and GB-family encodings.

### Example D: Korean `한국` — “Korea”

| Character | Unicode | EUC-KR | UTF-8 |
|---|---:|---:|---:|
| 한 | U+D55C | `C7 D1` | `ED 95 9C` |
| 국 | U+AD6D | `B1 B9` | `EA B5 AD` |
| Full string | — | `C7 D1 B1 B9` | `ED 95 9C EA B5 AD` |

Strict EUC-KR cannot encode all 11,172 modern Hangul syllables. Windows-949/UHC and the modern web `EUC-KR` decoder extend it.

### Example E: half-width and ordinary katakana

For half-width `ｶ` (`U+FF76`):

- Shift-JIS: `B6`
- EUC-JP: `8E B6`
- UTF-8: `EF BD B6`

For full-width `カ` (`U+30AB`):

- Shift-JIS: `83 4A`
- EUC-JP: `A5 AB`
- UTF-8: `E3 82 AB`

The two are compatibility-related but not bytewise or semantically identical. Normalization can change their representation.

---

## Escape and shift mechanisms

### ISO-2022-JP as the contrast case

Shift-JIS and EUC are most clearly understood beside the stateful encoding used in Japanese mail.

**[STD]** RFC 1468 defines:

| Escape sequence | Character set |
|---|---|
| `ESC ( B` = `1B 28 42` | ASCII |
| `ESC ( J` = `1B 28 4A` | JIS X 0201 Roman |
| `ESC $ @` = `1B 24 40` | JIS C 6226-1978 |
| `ESC $ B` = `1B 24 42` | JIS X 0208-1983 |

The stream begins in ASCII. After `ESC $ B`, pairs of `21–7E` bytes represent Japanese characters until `ESC ( B` or `ESC ( J` returns to a single-byte set. RFC 1468 specifies CRLF as `0D 0A` and forbids splitting a double-byte character during line wrapping.

**[STD]** ISO-2022-JP intentionally omits JIS X 0201 half-width kana. It was first specified and used in JUNET and then documented for Internet mail in 1993. [RFC 1468](https://www.rfc-editor.org/rfc/rfc1468.html)

**Synchronization comparison**

- ISO-2022-JP: corruption of or entry after an escape can leave the reader in the wrong state for an indefinite span.
- Shift-JIS: no persistent state, but lead/trail ambiguity impedes arbitrary entry.
- EUC: no persistent state; high-bit partitioning gives stronger local boundaries, subject to SS2/SS3.
- UTF-8: continuation bytes have a distinct bit pattern, giving better bounded resynchronization when strict decoding is used.

---

## Origins: chronology and institutions

### Precursors

**[STD/SCHOLARLY]** The immediate architectural ancestors were ISO 646 and ISO 2022, not Baudot, Murray, Hollerith, or EBCDIC in any direct design lineage. Telegraph codes and punched-card systems form the longer history of coded text, but the item-specific technical ancestry is:

`ASCII / ISO 646 national variants → ISO 2022 code extension → national 94×94 CJK repertoires → Shift-JIS and EUC byte encodings → vendor supersets → Unicode and GB 18030`

Claims about Bemer, the “eight-bit war,” EBCDIC’s naming, or the Thompson–Pike placemat concern ASCII/Unicode/UTF-8 history rather than the documented creation of these East Asian encodings. No evidence was found that those episodes directly determined Shift-JIS, EUC, GB 2312, GBK, or Big5. Omitting them as causal episodes is therefore an evidence-based scope decision, not an assertion that they are unimportant elsewhere.

### 1967–1978: ISO architecture and Japanese standardization

**[DOC]** IPSJ’s reconstruction dates Japanese work as follows:

- 1967: ISO R 646 highlighted the 128-position limitation.
- December 1969: IPSJ formed a Kanji Code Committee.
- 1971: a provisional 6,086-character table was produced, initially radical-ordered.
- March 1974: Japan’s Administrative Management Agency completed a frequency and suitability study containing 2,817 characters.
- April 1974: the Agency of Industrial Science and Technology commissioned JIPDEC to standardize a kanji interchange code.
- March 1976: Moriguchi Shigeichi’s committee delivered a draft based on 37 references, place names, and personal names.
- January 1978: JIS C 6226-1978 was established.
- September 1978: Toshiba announced the JW-10 Japanese-language word processor.

People explicitly documented in this chain include:

- **Wada Hiroshi**, chair of the IPSJ Standards Committee, who proposed studying an ISO R 646 extension;
- **Hayashi Ohki**, linguist and Ministry of Education school inspector, who led the early Kanji Code Committee;
- **Kusakabe Jutaro**, whose contemporary-language kanji table was a major input;
- **Moriguchi Shigeichi**, chair of the later standardization and JIS expert committees.

[IPSJ Computer Museum](https://museum.ipsj.or.jp/en/computer/main/0111.html)

### 1980–1981: GB 2312

**[STD]** China’s State Bureau of Standards published GB 2312 in 1980 and implemented it in 1981. An accessible scan preserves the full 170-page table. [GB 2312 scan](https://commons.wikimedia.org/wiki/File%3AGB_2312%E2%80%9480.pdf)

**[DOC]** The official retrospective credits coordinated work organized by the former Ministry of Electronics Industry and State Bureau of Standards and notes that the work received a national science-and-technology progress award. It does not name a sole inventor.

**[OPEN EVIDENCE ISSUE]** Popular histories sometimes attach prominent Chinese computing figures to “Chinese character encoding” generally. No committee roster or primary record located in this research justifies crediting Wang Xuan—or another single engineer—as inventor of GB 2312. Wang’s documented importance to computerized Chinese typesetting should not be silently converted into authorship of this standard.

### 1982–1983: Shift-JIS

**[DOC]** An IANA charset-registration clarification by Murata Makoto states:

- ASCII Corporation invented Shift-JIS in 1982;
- it was first used in **MBASICplus** on Mitsubishi’s MULTI-16 running CP/M-86;
- in 1983 ASCII, Mitsubishi, IBM Japan, and Microsoft agreed to use it as an internal Japanese PC representation;
- NEC, Apple, DEC, IBM, and others later adopted bases with their own extensions.

[IANA mailing-list record](https://data.iana.org/archive/ietf-charsets/msg00616.html)

**[DOC]** A Japanese Electronic Publishing Association account dates the developer announcement to December 1982 and implementation with Japanese MS-DOS 2.0 to 1983. [JEPA account](https://www.jepa.or.jp/keyperson_message/201408_408/)

**[DISPUTED CREDIT]** Sources differ in shorthand attribution: “ASCII Corporation,” “Microsoft,” or “ASCII and Microsoft.” The best located record supports cooperative development and deployment, not an adequately documented lone inventor. Kazuhiko Nishi’s corporate role in ASCII–Microsoft cooperation is established, but no primary design memo located here proves that he personally devised the byte transformation. Individual inventor claims should remain qualified.

**[FOLKLORE]** Precise stories that the trail-byte gaps were chosen primarily to protect C-language punctuation or that one named programmer devised the scheme in a single sitting are plausible engineering reconstructions but lack a located contemporaneous memo comparable to a patent or meeting minute.

### Early-to-mid 1980s: EUC

**[STD/DOC]** EUC grew in the Unix internationalization environment as an eight-bit packing of ISO-2022 code sets. Its Japanese registered form is attributed by IANA to OSF, Unix International, and Unix System Laboratories Pacific.

**[OPEN EVIDENCE ISSUE]** No single inventor or uniquely dated first “EUC memo” was found in the consulted primary registry materials. Assertions that “AT&T invented EUC” are too broad unless tied to a specific Unix manual or source release. Its history appears institutional and iterative.

### 1984: Big5

**[DOC]** Taiwan’s Institute for Information Industry developed Big5 as a common internal code for PC applications. It became a de facto rather than initially national standard.

**[SCHOLARLY]** Its success over more capacious or formally structured rivals reflects installed software, fonts, input methods, and exchange practice. A character encoding becomes infrastructure through compatible products, not only through committee authority.

### 1987–1992: Korean standards and rivals

**[STD/DOC]** KS C 5601-1987 adopted a fixed set of 2,350 precomposed Hangul syllables, often called *Wansung* (“completed-form”). The selection could not represent all 11,172 modern syllables.

A rival philosophy, **Johab** (“combination-form”), encoded initial, medial, and final Hangul components within structured 16-bit values. It was included in a later KS annex. Microsoft’s UHC/Windows-949 instead extended the Wansung byte space so all modern precomposed syllables could be represented while preserving EUC-KR assignments.

**[CONTROVERSY]** The Korean “completed versus combining” dispute was partly technical and partly industrial. Wansung simplified table lookup but excluded valid syllables; Johab mirrored Hangul composition more systematically but was incompatible with established tables. UHC was a vendor compromise that won broad deployment without being identical to strict EUC-KR.

### 1993–2000: Unicode convergence, GBK, and HKSCS

- 1993: GB 13000.1 adopted the ISO/IEC 10646 framework in China.
- 1995: GBK expanded GB 2312-compatible byte space.
- 1995: Hong Kong created GCCS.
- 1997: JIS X 0208 Appendix 1 formally documented Shift-JIS.
- 1999: HKSCS replaced GCCS as a public Hong Kong supplement.
- 2000: GB 18030 supplied a migration-compatible encoding capable of reaching the universal repertoire.

---

## Adoption and decline

### Japan

**[DOC]** Shift-JIS was closely associated with Japanese personal computers, MS-DOS, Windows, classic Macintosh variants, and locally produced applications. EUC-JP became characteristic of Unix systems. ISO-2022-JP dominated Internet mail and news because it remained seven-bit clean.

This produced a three-way Japanese coexistence:

- Shift-JIS on PCs and files;
- EUC-JP on Unix;
- ISO-2022-JP in mail/network interchange.

Each used largely the same JIS repertoire but encoded it differently. Conversion errors became an ordinary user experience.

**[STD]** RFC 1468 says ISO-2022-JP was first specified for JUNET and was already widely used in Japanese IP communities by 1993. RFC 2237’s 1997 extension noted both proprietary Japanese character sets and a “tendency to use Unicode,” while observing that Unicode was not yet widely used. [RFC 2237](https://www.rfc-editor.org/rfc/rfc2237.html)

**[SCHOLARLY]** Japanese resistance to rapid Unicode replacement was not a simple rejection of internationalization. Existing systems offered stable round trips, mature input methods, fonts, printer workflows, and exact vendor characters. Early Unicode mappings sometimes failed those properties; language-dependent Han glyph display and distrust of unification reinforced caution.

### Mainland China

GB 2312 became the baseline simplified-Chinese set. DOS and early Windows environments used national and vendor implementations; Windows CP936 evolved into a GBK implementation. GBK preserved GB 2312 byte assignments while vastly expanding the repertoire.

GB 18030 then made compatibility with universal character coverage a regulatory requirement. Modern Chinese systems may use Unicode internally while accepting GBK/GB 18030 at file, API, browser, database, or protocol boundaries.

### Taiwan and Hong Kong

Big5 became the dominant traditional-Chinese PC encoding in Taiwan through industrial adoption. ETen, Microsoft, IBM, and user-defined variants fragmented its margins.

Hong Kong used Big5 but needed Cantonese and local administrative characters. GCCS/HKSCS filled the gap. Successive HKSCS editions moved characters from private-use conventions to standardized ISO 10646 positions.

### Korea

Strict EUC-KR served Unix and interchange; Windows-949/UHC became the broader PC encoding. The scarcity of Hangul syllables in KS C 5601 was a decisive limitation. Unicode’s algorithmic modern Hangul model ultimately supplied a stable universal solution, although compatibility mappings remain essential.

### Internet policy and the web

**[STD]** MIME’s RFC 1341 made charset labels a routine part of Internet media types in 1992. RFC 1468 registered ISO-2022-JP usage. IANA’s charset registry records Shift_JIS, EUC-JP, EUC-KR, GBK, Big5-HKSCS, and historical aliases. [IANA registry](https://www.iana.org/assignments/character-sets)

**[STD]** RFC 2277, issued in January 1998, requires standards-track Internet protocols handling text to be able to use UTF-8; use of legacy charsets is permitted for existing protocols and datastores, but lack of UTF-8 support requires exceptional justification. [RFC 2277](https://www.rfc-editor.org/rfc/rfc2277.html)

**[STD/MODERN]** WHATWG requires UTF-8 for new formats but requires browsers to decode a closed list of legacy encodings, including GBK, Big5, Shift_JIS, EUC-JP, and EUC-KR. The HTML Standard likewise requires user agents to support those deployed decoders. [HTML Standard](https://html.spec.whatwg.org/multipage/parsing.html)

**[DOC]** W3Techs reported UTF-8 on approximately 99% of measured websites in 2026; its methodology measures sites whose encoding it can identify, not all stored files or private enterprise data. [W3Techs historical encoding trend](https://w3techs.com/technologies/history_overview/character_encoding/ms/y)

Thus “decline” is not disappearance. The survivors include:

- browser decoding;
- old web pages and mail archives;
- filenames and ZIP metadata;
- database columns and export formats;
- Windows “ANSI” code-page APIs;
- printers, embedded devices, games, and ROMs;
- government and financial archives;
- source code and asset pipelines;
- conversion tables preserving vendor gaiji.

---

## The other scripts

### Latin

All the encodings preserve an ASCII-like single-byte region, but “ASCII-compatible” requires qualification:

- JIS X 0201 assigns yen and overline semantics to `5C` and `7E`;
- Korean national variants historically display `5C` as won;
- Microsoft/Unicode mappings often preserve `U+005C` while fonts change the glyph.

Case applies to Latin letters in the usual way, but byte ordering is not locale collation.

### Greek and Cyrillic

JIS X 0208, GB 2312, and KS X 1001 include limited Greek and Cyrillic blocks. These are not comprehensive encodings for modern Greek, Russian, Bulgarian, or other languages:

- diacritics and language-specific letters may be absent;
- compatibility/full-width forms may differ from ordinary single-byte or Unicode letters;
- sorting and case mapping are not supplied by encoding order.

EUC and Shift-JIS are therefore not sensible general Greek or Cyrillic encodings merely because the repertoire contains subsets.

### Hebrew and Arabic

The named East Asian repertoires generally do not support usable Hebrew or Arabic. They supply no comprehensive letters, combining marks, bidirectional semantics, or contextual shaping.

Even where a vendor extension could assign glyphs, an encoding table alone cannot solve Arabic joining or the Unicode bidirectional problem. Those require text-processing rules and fonts.

### Indic scripts

They are essentially absent. Indic writing requires consonants, dependent vowels, viramas, combining behavior, clusters, and shaping. A fixed CJK double-byte table designed around preselected graphic characters offers neither adequate repertoire nor the modern character-model machinery.

### Chinese

- GB 2312: simplified-oriented basic set.
- GBK: broad simplified and traditional coverage, incorporating the main Unicode-era CJK block.
- Big5: traditional-oriented Taiwan repertoire.
- HKSCS: Hong Kong/Cantonese and local supplement.
- CNS 11643/EUC-TW: multi-plane Taiwanese standard.
- GB 18030: universal-repertoire bridge.

No legacy table captures every historical, dialectal, name, or variant character.

### Japanese

JIS-based systems combine:

- Latin/JIS Roman;
- hiragana;
- full-width and half-width katakana;
- selected kanji;
- symbols.

Their largest shortcomings were rare kanji, name characters, variants, and vendor gaiji. JIS X 0212 and X 0213 extended the standardized repertoire, but not every encoding supported them equally.

### Korean

KS X 1001’s 2,350-syllable Wansung set omitted valid modern syllables. Johab represented Hangul composition structurally; UHC extended byte assignments; Unicode encodes all 11,172 modern syllables and also provides jamo for decomposed representation.

### Emoji

None of the original encodings has a general emoji model. Japanese mobile carriers placed pictographs in vendor/private areas, later submitting repertoires for Unicode standardization. Emoji’s historical path is therefore analogous to gaiji in one respect—vendor characters became interchange requirements—but it postdates the core Shift-JIS/EUC designs.

**[MODERN]** Emoji in contemporary Japanese text normally require Unicode. Encoding them into Shift-JIS generally produces failure, replacement, an application-specific private code, or lossy transliteration.

---

## People and institutions

### Documented participants

- **Wada Hiroshi** — IPSJ Standards Committee chair; proposed research on extending ISO R 646 for kanji.
- **Hayashi Ohki** — linguist and Ministry of Education inspector; led the early Japanese Kanji Code Committee.
- **Kusakabe Jutaro** — compiler whose kanji-frequency material informed the provisional Japanese list.
- **Moriguchi Shigeichi** — chaired the Japanese drafting and JIS expert committees leading to JIS C 6226-1978.
- **Kazuhiko Nishi** — ASCII Corporation co-founder and central actor in ASCII–Microsoft cooperation; important institutional context, but personal authorship of the Shift-JIS transformation is not proven by a located design record.
- **Murata Makoto** — later supplied a detailed IANA clarification about Shift-JIS origins and deployment; this is a valuable retrospective technical account.
- **Jun Murai, Mark Crispin, Erik van der Poel** — authors of RFC 1468, which documented ISO-2022-JP Internet practice.
- **Ken Lunde** — documented East Asian character sets, mappings, and implementation practice; his work is a major scholarly/engineering reconstruction rather than the original authority for every national standard.
- **Mark Davis and Lee Collins** — participants in early Unicode work whose retrospective accounts illuminate dissatisfaction with legacy multibyte systems.
- **Peter Constable** — documented Unicode interoperability concerns arising from GB 18030-2022.

### Institutions

- **ISO and ISO/IEC JTC 1** — ISO 646, ISO 2022, ISO/IEC 10646.
- **IPSJ, JIPDEC, AIST, and JISC/JSA** — Japanese repertoire development and standardization.
- **ASCII Corporation, Microsoft, Mitsubishi, IBM Japan** — early Shift-JIS deployment agreement.
- **AT&T/Unix institutions, OSF, Unix International, USL Pacific** — EUC development and standardization context.
- **State Bureau of Standards, CESI, and Chinese IT standardization committees** — GB 2312, GBK, and GB 18030.
- **Institute for Information Industry** — Big5.
- **Hong Kong government language and IT bodies** — GCCS/HKSCS.
- **Korean standards bodies and Microsoft Korea/Windows ecosystem** — KS C 5601, Johab, and UHC deployment.
- **IETF and IANA** — Internet charset documentation and registration.
- **Unicode Consortium and ISO/IEC JTC 1/SC 2/WG 2/IRG** — universal repertoire and Han unification.
- **W3C and WHATWG** — web-compatible decoding behavior.

### Absence of evidence

The available institutional accounts are much better at naming committee chairs and organizations than individual byte-layout engineers. A historian should resist manufacturing heroic inventors where the records show collaborative committee and vendor work.

No evidence located in this pass establishes direct roles for Baudot, Murray, Hollerith, Bemer, Mackenzie, Becker, Thompson, Pike, or Whistler in designing these five encoding families. Mackenzie’s 1980 history is valuable background to coded-character-set development; Thompson and Pike are central to UTF-8; Whistler to Unicode. They belong to the larger 17-encoding narrative, not necessarily the authorship of this item.

---

## Culture

### `文字化け`—mojibake

`文字化け` literally combines “characters/writing” and *bake*, “transform/change into another form,” with overtones of something becoming strange or ghostlike. It denotes text rendered as unintended characters because bytes and decoder disagree.

Typical causes include:

- Shift-JIS read as EUC-JP;
- EUC-JP read as Shift-JIS;
- UTF-8 read as CP932;
- Big5 read as GBK, or vice versa;
- repeated encode/decode cycles;
- wrong HTTP or MIME labels;
- vendor-extension bytes passed through a standard-only converter.

**[CULTURAL FACT]** Japanese users encountered enough mutually incompatible encodings that the failure acquired an ordinary word rather than remaining specialist jargon. The term later entered English technical language untranslated.

**[OPEN EVIDENCE ISSUE]** Modern dictionaries and histories define the word, but this search did not locate a securely dated earliest printed use. Claims of a specific inventor or first coinage should be treated as unproved.

### Aesthetics of corruption

**[SCHOLARLY]** Mojibake became more than an error category. Artists, game designers, glitch aesthetics, and Internet communities use apparently corrupted CJK text to signal technological breakdown, secrecy, horror, or alienness. The effect depends on cultural memory: what was once a mundane mail/browser failure became a visual genre.

Deliberate “mojibake generators” are a modern invention. They often reproduce a UTF-8/legacy mismatch, not historically authentic random corruption.

### Plain text and hidden machinery

These encodings complicate the ideal of “plain text.” A byte sequence is not self-interpreting:

- `A4 A4 A4 E5` is meaningful Big5;
- the same bytes mean something else or fail elsewhere;
- `5C` may be a backslash code point, a yen glyph, a won glyph, or a trail byte;
- a “GB2312” label on the web commonly means GBK.

Plain text therefore depends on external agreements: encoding label, version, vendor mapping, language, normalization, line-ending convention, and font.

### Computing vernacular

Legacy encodings shaped:

- full-width versus half-width typography;
- two-column terminal assumptions;
- Japanese kaomoji and text art;
- byte-count limits in bulletin boards and games;
- filename length and path bugs;
- gaiji editors and user-created fonts;
- database schemas where “one character = two bytes” was treated as an invariant.

That invariant fails even within EUC-JP and fails completely after UTF-8, supplementary Unicode characters, combining sequences, and emoji.

---

## Controversies and disputes

### 1. Shift-JIS credit

**Documented:** ASCII Corporation introduced it in 1982; MBASICplus/MULTI-16 is the earliest deployment identified in the IANA account; ASCII, Mitsubishi, IBM Japan, and Microsoft agreed on PC use in 1983.

**Disputed:** whether shorthand credit should go to Microsoft, ASCII Corporation, or both.

**Evidence assessment:** no located contemporaneous design memo or signed committee record identifies a sole engineer. Corporate joint credit is safer than a personal “inventor” claim.

### 2. Big5’s name

**Documented:** III prepared the 1984 encoding for a Taiwanese PC software environment involving five major packages.

**Folklore/secondary account:** it was named for five companies.

**Evidence assessment:** official Taiwanese sources consulted favor the package explanation. The “five companies” form remains possible but insufficiently evidenced.

### 3. GB 2312 as complete Chinese

**Modern misconception:** because nearly every ordinary simplified-Chinese sentence can be encoded, GB 2312 is sometimes described as “the Chinese character set.”

**Documented contradiction:** its title calls it a basic set; the table contains 6,763 Han characters and visibly excludes many names, traditional forms, and historical characters.

### 4. “GB2312” versus GBK

**Documented historical distinction:** GB 2312 is a 94×94 repertoire; GBK is a later, larger two-byte encoding.

**Modern web invention:** browsers map `gb2312` and many associated labels to GBK because real pages and Windows software used those labels for CP936/GBK data.

This is pragmatic interoperability, but it makes labels unreliable as historical evidence.

### 5. EUC-KR versus Windows-949

The same label problem appears in Korean:

- strict EUC-KR encodes KS X 1001;
- Windows-949 adds thousands of Hangul syllables;
- WHATWG calls its consolidated decoder EUC-KR and aliases `windows-949` to it.

A browser’s successful decoding does not prove a file conformed to original EUC-KR.

### 6. Han unification

**[STD/DOC]** Unicode’s official history says:

- Xerox began a Han cross-reference database in 1986;
- Apple began a parallel effort in 1988;
- the databases merged in 1989;
- the Unicode Working Group proposed the repertoire to ANSI X3L2 in September 1989;
- ad hoc meetings occurred in Beijing in 1989 and Seoul in 1990;
- the CJK Joint Research Group first met in Tokyo in July 1991;
- the Unified Repertoire and Ordering was completed on 27 March 1992;
- it entered Unicode 1.0 Volume 2 and ISO/IEC 10646-1:1993.

[Unicode Appendix E](https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/)

The core principle was to encode a character once when Chinese, Japanese, Korean, or Vietnamese source standards represented the same abstract Han character, while preserving distinctions needed for source round trips. Regional glyph style was expected to come from language-sensitive fonts.

**Pro-unification documented position:** encoding the same abstract Han character separately merely because it occurs in GB, JIS, KS, and CNS sources would resemble separately encoding Latin `A` for ASCII, EBCDIC, and each national standard. [Unicode Technical Note 26](https://www.unicode.org/notes/tn26/)

**Japanese and scholarly objections:**

- source standards sometimes distinguished forms inconsistently;
- a single code point can display with a Chinese-looking glyph in Japanese text when language/font metadata is absent;
- bibliographic and historical work may need distinctions treated as typographic by the standard;
- round-trip mappings evolved and were sometimes disputed;
- early Unicode was perceived as controlled by North American corporations before full governmental CJK participation.

**Qualification:** the claim that “Americans merged Chinese and Japanese without East Asian participation” is historically false if applied to the completed URO: Chinese, Japanese, and Korean national representatives participated in the CJK-JRG. It does describe an anxiety about the composition of the earliest Unicode consortium and initial corporate drafts.

**Documented ongoing politics:** UTC and WG2 records show debates over JIS X 0213 mappings, source separation, additional kanji, and unification criteria. [UTC 81 minutes](https://www.unicode.org/L2/L1999/99260.htm)

**Balanced finding:** Han unification enabled a workable universal repertoire and avoided enormous duplication; it also moved some distinctions from character codes into fonts, language tagging, variation sequences, and specialist protocols. Both consequences are real.

### 7. Vendor extensions

NEC and IBM extensions to Shift-JIS, CP936 additions to GBK, UHC additions to EUC-KR, and ETen/CP950/HKSCS additions to Big5 demonstrate a recurring political economy:

1. a national set omits real customer characters;
2. a vendor assigns unused positions;
3. documents depend on them;
4. competitors choose different assignments;
5. Unicode must map the deployed variants;
6. web standards consolidate behavior retrospectively.

Calling vendor extensions merely “nonstandard” misses their social authority; calling them “the standard” erases interoperability failures.

### 8. Security

#### Syntax-byte collisions

Shift-JIS, GBK, Big5, and Windows-949 allow many ASCII-valued bytes as trails. Byte-oriented sanitizers can disagree with character decoders about quotes, backslashes, and delimiters.

Mitigations include:

- decode once with a strict, named decoder;
- validate decoded characters rather than raw bytes;
- use one canonical encoding internally;
- reject malformed sequences consistently;
- avoid decode–filter–reinterpret pipelines.

#### Encoding disagreement

WHATWG identifies producer/consumer disagreement as a security class. If one component treats an invalid pair as two bytes and another replaces it as one invalid sequence, syntax boundaries can change.

#### Homoglyphs

Legacy CJK encodings include full-width forms, Greek, Cyrillic, Roman letters, compatibility ideographs, and visually similar punctuation. Unicode expands the possible repertoire and thus the attack surface, but homoglyph confusion did not begin with Unicode.

#### Overlong UTF-8

**[STD]** Overlong UTF-8 is not a flaw peculiar to the East Asian encodings, but it mattered during migration. RFC 3629 requires rejection of invalid sequences such as `C0 80` for NUL and cites real security consequences. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html)

#### BOM

The byte-order mark belongs principally to UTF-16/UTF-32 and optionally UTF-8, not to these legacy encodings. A UTF-8 BOM misread as Shift-JIS or GBK becomes mojibake. Conversely, heuristic detectors may mistake legacy bytes for Unicode when metadata is absent.

---

## Collation, equality, and round trips

None of these byte orders is a satisfactory universal collation:

- JIS Level 1 uses Japanese representative readings; Level 2 uses radical/stroke.
- GB 2312 Level 1 uses Pinyin; Level 2 uses radical/stroke.
- Big5 separates frequency groups and uses stroke/radical ordering.
- KS X 1001 places Hangul and Hanja in repertoire-specific orders.
- vendor extensions occur in leftover areas unrelated to linguistic order.
- ASCII sorts separately from full-width equivalents.

Bytewise comparison can therefore put visually related or canonically corresponding characters far apart.

Round-trip conversion also depends on the exact variant:

- JIS Roman `5C`/`7E` versus ASCII semantics;
- wave dash and related CP932/JIS mapping disputes;
- duplicated Big5 characters;
- HKSCS private-use mappings promoted to standardized Unicode;
- CP936’s euro;
- duplicated Korean Hanja codes;
- Unicode compatibility ideographs and variation selectors;
- GB 18030 edition changes.

A converter described only as “Shift-JIS to Unicode” is underspecified. One must ask: JIS Appendix Shift-JIS, CP932, IBM-943, WHATWG Shift_JIS, or another mapping?

---

## Open questions

1. **Who performed the exact Shift-JIS byte-layout design?**  
   Corporate and deployment chronology is reasonably documented, but a contemporaneous engineering memo naming the individual designers has not been located.

2. **What is the definitive origin of the name “Big5”?**  
   Taiwanese institutional sources support the five-package story; the five-company story remains widespread but insufficiently sourced.

3. **Who sat on every GB 2312 drafting subcommittee, and what corpora determined inclusion?**  
   The standard and official retrospective establish institutional sponsorship and counts but do not provide a readily accessible full deliberative archive.

4. **What is the earliest dated appearance of `文字化け` in print or software documentation?**  
   Its meaning and cultural use are well attested; its coinage is not.

5. **What was the first normative EUC specification?**  
   The registry records the Unix institutional standardizers, but published accounts often blur early Unix implementations, AT&T documentation, OSF specifications, and later IANA registrations.

6. **How much “resistance to Unicode” in Japan was ideological versus economic?**  
   Participant accounts and technical disputes are documented; quantitative evidence separating cultural objection, installed-base cost, font availability, round-trip defects, and vendor strategy remains limited.

7. **Which historical vendor gaiji can still be losslessly recovered?**  
   This is collection-specific. Fonts, conversion tables, application versions, and local institutional documentation may be required.

8. **How should GB 18030-2022 mapping changes be reconciled with old Unicode round trips?**  
   Unicode committee documents identify the problem; deployed systems must choose mappings according to edition and conformance target.

---

## Conclusions

The East Asian double-byte encodings were not primitive attempts at Unicode. They were carefully engineered answers to a different environment:

- seven-bit communication standards;
- eight-bit Unix and PC storage;
- fixed terminal cells;
- small memories;
- national repertoires;
- vendor-controlled fonts;
- software expecting ASCII punctuation and controls.

JIS X 0208, GB 2312, KS X 1001, and Big5 selected which thousands of characters counted as operationally necessary. Shift-JIS and EUC then made those tables usable in byte-oriented systems. Their strongest virtue—compatibility with existing ASCII-oriented software—also produced their most durable hazards: ambiguous boundaries, punctuation-valued trail bytes, national glyph substitutions, variant mappings, and labels whose meaning drifted with vendor practice.

Unicode did not simply erase them. It absorbed their repertoires, source distinctions, duplicates, compatibility forms, private-use migrations, and political arguments. GB 18030 wrapped universal coverage in a GBK-compatible national encoding. WHATWG converted messy browser behavior into a retrospective interoperability standard. Modern UTF-8 dominance therefore rests partly on decades of mapping work from these legacy systems.

Their continuing significance is less in new document creation than in the interpretation of old bytes. A file’s bytes preserve not only characters but an institutional history: which national table, which computer industry, which vendor extension, which language community, and which moment in the transition from local code pages to universal text.

---

## Sources consulted

### Standards, RFCs, registries, and official specifications

1. Chinese national standards catalogue, **GB/T 2312-1980**:  
   https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=5664A728BD9D523DE3B99BC37AC7A2CC

2. Scan of **GB 2312-1980**, 170 pages:  
   https://commons.wikimedia.org/wiki/File%3AGB_2312%E2%80%9480.pdf

3. Ministry of Education of the PRC, archived GB 2312 copy:  
   https://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201206/t20120601_136847.html

4. Standardization Administration of China, history of Chinese information-technology standards:  
   https://www.sac.gov.cn/jdbnhbz/bzgs/art/2021/art_5e8ba919bec34784b55960ea23175ad3.html

5. Standardization Administration of China, **GB 18030-2022** announcement:  
   https://www.sac.gov.cn/Standards/Release/art/2022/art_3555a3d3ce1c49dfb06a2c615a1d1190.html

6. IANA Character Sets registry:  
   https://www.iana.org/assignments/character-sets

7. IANA archive, application/technical history for **GBK**:  
   https://data.iana.org/archive/ietf-charsets/msg01038.html

8. IANA archive, clarification of **Shift-JIS** history by Murata Makoto:  
   https://data.iana.org/archive/ietf-charsets/msg00616.html

9. RFC 1341, *MIME: Mechanisms for Specifying and Describing the Format of Internet Message Bodies*:  
   https://www.rfc-editor.org/rfc/rfc1341.html

10. RFC 1345, *Character Mnemonics and Character Sets*:  
    https://www.rfc-editor.org/rfc/rfc1345.html

11. RFC 1468, *Japanese Character Encoding for Internet Messages*:  
    https://www.rfc-editor.org/rfc/rfc1468.html

12. RFC 2237, *Japanese Character Encoding for Internet Messages*:  
    https://www.rfc-editor.org/rfc/rfc2237.html

13. RFC 2277, *IETF Policy on Character Sets and Languages*:  
    https://www.rfc-editor.org/rfc/rfc2277.html

14. RFC 2279, *UTF-8, a transformation format of ISO 10646*:  
    https://www.rfc-editor.org/rfc/rfc2279.html

15. RFC 3629, *UTF-8, a transformation format of ISO 10646*:  
    https://www.rfc-editor.org/rfc/rfc3629.html

16. WHATWG, living **Encoding Standard**:  
    https://encoding.spec.whatwg.org/

17. WHATWG, HTML character-encoding requirements:  
    https://html.spec.whatwg.org/multipage/parsing.html

18. W3C, *Encoding* technical report edition:  
    https://www.w3.org/International/docs/encoding/

19. ARIB STD-B24, EUC-JP layout and control table:  
    https://www.arib.or.jp/english/html/overview/doc/6-STD-B24v6_4-2p3-1-E1.pdf

20. ISO International Register material for coded character sets:  
    https://itscj.ipsj.or.jp/english/vbcqpr00000004qn-att/ISO-IR.pdf

21. ISO-IR 58, registered GB 2312 repertoire:  
    https://itscj.ipsj.or.jp/ir/058.pdf

22. ISO-IR 87, JIS C 6226-1983 registration:  
    https://itscj.ipsj.or.jp/ir/087.pdf

### Japanese institutional and participant histories

23. IPSJ Computer Museum, *Establishment of JIS C 6226*:  
    https://museum.ipsj.or.jp/en/computer/main/0111.html

24. Original Japanese edition of the IPSJ history:  
    https://museum.ipsj.or.jp/computer/main/0111.html

25. Japanese Electronic Publishing Association, Shift-JIS chronology:  
    https://www.jepa.or.jp/keyperson_message/201408_408/

26. Unicode Consortium, *Early Years of Unicode*:  
    https://www.unicode.org/history/earlyyears.html

27. Unicode Consortium, Han Unification History, Appendix E:  
    https://www.unicode.org/versions/Unicode16.0.0/core-spec/appendix-e/

28. Unicode Technical Note #26, *On the Encoding of Latin, Greek, Cyrillic, and Han*:  
    https://www.unicode.org/notes/tn26/

29. Unicode FAQ, Chinese and Japanese/Han unification:  
    https://unicode.org/faq/han_cjk.html

30. Unicode Technical Report #17, *Unicode Character Encoding Model*:  
    https://www.unicode.org/reports/tr17/

31. UTC 81/L2 178 minutes, JIS X 0213 mapping discussion:  
    https://www.unicode.org/L2/L1999/99260.htm

32. Unicode L2/01-192, *Problems on Interoperativity between Unicode and CJK Local Encodings*:  
    https://www.unicode.org/L2/L2001/01192-unicode-cjk.htm

### Chinese and Taiwanese sources

33. Taiwan CNS 11643 service, character-code introduction and Big5 versions:  
    https://www.cns11643.gov.tw/pageView.jsp?ID=9

34. Chinese Digitalization Technology Promotion Foundation, Big5/GB/CNS history:  
    https://www.cmex.org.tw/page.jsp?ID=30&SN=chinese&la=0

35. Institute for Information Industry, institutional history:  
    https://www.iii.org.tw/en/about/iii/overview

36. Academia Sinica-hosted historical account of GB 2312, GBK, and GB 18030:  
    https://idv.sinica.edu.tw/bear/charcodes/Section12.htm

37. Unicode IRG scan of the GBK 1.0 specification:  
    https://www.unicode.org/irg/docs/n0278-GBKv1.pdf

38. Peter Constable, Unicode L2/22-274, *Disruptive Changes in GB 18030-2022*:  
    https://www.unicode.org/L2/L2022/22274-disruptive-changes.pdf

39. Unicode L2/23-003, industry recommendations for GB 18030 testing and certification:  
    https://www.unicode.org/L2/L2023/23003-gb18030-recommendations.pdf

### Hong Kong sources

40. Hong Kong Government, *What is Hong Kong Supplementary Character Set?*:  
    https://www.ccli.gov.hk/en/hkscs/what_is_hkscs.html

41. Hong Kong Government, archived HKSCS editions and mapping tables:  
    https://www.ccli.gov.hk/en/archive/

### Korean and vendor documentation

42. Archived Microsoft Knowledge Base, *INFO: Hangul (Korean) Character Sets*:  
    https://ftp.zx.net.nz/pub/archive/ftp.microsoft.com/MISC/KB/en-us/170/557.HTM

43. Korean government, public-information-system Hangul processing guidance:  
    https://m.korea.kr/expertWeb/resources/files/data/document_file/2010/%EA%B3%B5%EA%B3%B5%20%EC%A0%95%EB%B3%B4%EC%8B%9C%EC%8A%A4%ED%85%9C%20%ED%95%9C%EA%B8%80%20%EC%B2%98%EB%A6%AC%20%EA%B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8.pdf

44. Microsoft, code-page overview and CP932/CP936 examples:  
    https://learn.microsoft.com/en-us/globalization/encoding/code-pages

### Web adoption and modern compatibility

45. W3Techs, historical character-encoding trends:  
    https://w3techs.com/technologies/history_overview/character_encoding/ms/y

46. W3Techs, UTF-8 usage by site ranking:  
    https://w3techs.com/technologies/breakdown/en-utf8/ranking

47. WHATWG historical Web Encodings survey:  
    https://wiki.whatwg.org/wiki/Web_Encodings

### Secondary technical reconstructions used cautiously

48. Ken Lunde-related CJK character-code notes archive:  
    https://resources.oreilly.com/examples/9781565922242/-/blame/master/doc/cjk.inf-062995

49. Linux `charsets(7)` overview:  
    https://man7.org/linux/man-pages/man7/charsets.7.html

50. CJK Codes, KS C 5601 structural summary:  
    https://www.ibiblio.org/pub/packages/ccic/software/info/cjk-codes/KSC.html
