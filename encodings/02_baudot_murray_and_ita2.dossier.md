# Baudot, Murray and the five-bit teleprinter codes (ITA2): Research Dossier

> **Standard:** International Telegraph Alphabet No. 2, currently ITU-T Recommendation S.1  
> **Standardized:** Developed by the CCIT in 1929–1931; promulgated internationally in the 1932 Madrid Telegraph Regulations  
> **Width:** Five binary signal elements per coded combination; normally transmitted asynchronously with start and stop elements  
> **Repertoire:** 26 Latin letters in one shift state; digits, punctuation, and controls in another; three figure-case positions reserved for national/private use  
> **Current status:** ITU-T S.1 (03/1993) remains formally **in force**. Obsolete for general computing and mostly displaced in public telecommunications, but still encountered in amateur RTTY, historical machinery, specialist radio systems, and some regulatory definitions.

---

## Method and evidentiary labels

This dossier distinguishes the following kinds of evidence:

- **[STANDARD]** Primary normative standard, regulation, patent, or official administrative document.
- **[CONTEMPORARY]** Technical writing or manual published during the system’s active development or use.
- **[RECONSTRUCTION]** Later scholarly or archival reconstruction based on contemporary documents.
- **[PARTICIPANT]** Recollection by someone who took part in the events.
- **[DISPUTED]** A contested attribution or chronology with conflicting evidence.
- **[FOLKLORE]** A widely repeated story for which firm contemporary support has not been found.
- **[MODERN]** A later convention, implementation choice, or retrospective terminology.

The principal reconstruction is Eric Fischer’s *The Evolution of Character Codes, 1874–1968*. Its value is that it cites Baudot’s own 1877 article, early patents, CCIT proceedings, Post Office publications, and surviving company material. Charles E. Mackenzie’s *Coded Character Sets: History and Development* is indispensable for the later transition from telegraph codes to ASCII, but its main detailed emphasis is the computer-code era rather than the earliest Baudot machinery.

A persistent terminology problem must be stated at the outset:

> **The original Baudot alphabet, Murray’s successive codes, national “Baudot” or Teletype codes, and CCITT/ITU ITA2 are related but not bit-for-bit identical.**

Calling all of them “Baudot code” is historically understandable but technically unsafe.

---

# Basic identification

## Names

**[STANDARD]** The formal name is **International Telegraph Alphabet No. 2**, abbreviated **ITA2**. In older documents it appears as:

- *International Telegraph Alphabet No. 2*
- *International Telegraphy Alphabet No. 2*
- *Alphabet No. 2*
- *CCIT No. 2* or, later, *CCITT No. 2*
- *CCITT-2*
- national-language equivalents such as Russian МТК-2

**[COMMON USAGE]** “Baudot,” “Baudot–Murray,” “Murray code,” “five-level code,” and “five-unit code” are often used loosely for ITA2 or a national derivative.

**[TECHNICAL CAUTION]** “Five-level” describes the two-valued choice in each of five signal positions. “Five-bit” is convenient modern language, but early engineers spoke of *units*, *elements*, *impulses*, *marks and spaces*, or *levels*. The word *bit* itself was coined much later, in 1947–1948.

## Standards and dates

- **1874:** Émile Baudot’s French patent no. 103,898, *Système de télégraphie rapide*. The exact code embodied in this first patent is a disputed point.
- **1876–1877:** Baudot’s mature five-unit system is documented; his 1877 paper, *Des Appareils Télégraphiques à Signaux Indépendants*, describes the system.
- **1900–1902:** Donald Murray’s US patents document his page printer, automatic transmitter, and keyboard perforator.
- **1926:** The newly established CCIT begins work on standardized telegraph alphabets and adopts *baud* as a unit name.
- **1929:** CCIT’s second Berlin meeting recommends separate alphabets for synchronous multiplex and start-stop working; surviving drafts differ from final ITA2.
- **1931:** CCIT resolves to base the start-stop alphabet more directly on Murray-derived practice.
- **1932:** The Madrid Telegraph Regulations publish the adopted international alphabets.
- **1948:** CCIT accepts a US proposal that Alphabet No. 2 become the general five-unit code for international telegraphy.
- **1957:** CCIT and CCIF merge to become CCITT.
- **1984, 1988, 1993:** Later S.1 editions and amendments regularize the repertoire and provisions, including optional mixed-case extension arrangements.
- **Present:** ITU lists Recommendation S.1 (03/1993) as in force.

The common claim that ITA2 “was standardized in 1924” appears frequently in secondary sources, but the documentary chain examined here supports 1929 committee action, a decisive 1931 revision, and formal publication in the 1932 Madrid regulations. No primary 1924 ITA2 text was located. That date should therefore be treated as **[DISPUTED/PROBABLY ERRONEOUS]**.

---

# The code in detail

## Logical structure

Five binary elements provide only \(2^5 = 32\) combinations. ITA2 therefore uses a small state machine:

1. **Letters state:** most combinations print A–Z.
2. **Figures state:** the same combinations print digits, punctuation, or operate controls.
3. **LTRS** and **FIGS** combinations change the state without advancing the printing position.
4. Space, CR, LF, and NUL are state-independent.
5. Several figure-case assignments were deliberately left for national or private use.

The shift is *locking*: unlike a mechanical typewriter Shift key, FIGS is sent once and remains effective until LTRS is received.

## Bit-order convention

**[STANDARD]** ITU-T S.1 numbers elements `1 2 3 4 5` in transmission order and writes their conditions as `A` or `Z`:

- `A` = start polarity, no tape perforation, binary 0
- `Z` = stop polarity, perforation, binary 1

Modern tables usually display the corresponding integer with the most significant bit at the left. Since element 1 is sent first and conventionally treated as the least significant bit, the visible binary digits appear reversed relative to ITU’s `12345` transmission-order notation.

Example:

- ITU element order for `A`: `ZZAAA`
- transmitted first to last: `1 1 0 0 0`
- conventional numeric display: `00011`
- integer value: 3

A bare string such as `11000` is consequently ambiguous unless its author says whether it is transmission order or ordinary binary display.

## Full ITA2 table

The following uses the common modern convention: five-bit numeric value, most significant bit on the left. On the wire, the rightmost bit—element 1—is sent first.

| Dec | Binary | Letters state | Figures state, international S.1 |
|---:|:---:|---|---|
| 0 | `00000` | NUL / all-space | NUL / all-space |
| 1 | `00001` | E | 3 |
| 2 | `00010` | LF | LF |
| 3 | `00011` | A | `-` |
| 4 | `00100` | SPACE | SPACE |
| 5 | `00101` | S | apostrophe |
| 6 | `00110` | I | 8 |
| 7 | `00111` | U | 7 |
| 8 | `01000` | CR | CR |
| 9 | `01001` | D | WRU / enquiry |
| 10 | `01010` | R | 4 |
| 11 | `01011` | J | audible signal / BEL |
| 12 | `01100` | N | comma |
| 13 | `01101` | F | national/private use |
| 14 | `01110` | C | colon |
| 15 | `01111` | K | `(` |
| 16 | `10000` | T | 5 |
| 17 | `10001` | Z | `+` |
| 18 | `10010` | L | `)` |
| 19 | `10011` | W | 2 |
| 20 | `10100` | H | national/private use |
| 21 | `10101` | Y | 6 |
| 22 | `10110` | P | 0 |
| 23 | `10111` | Q | 1 |
| 24 | `11000` | O | 9 |
| 25 | `11001` | B | `?` |
| 26 | `11010` | G | national/private use |
| 27 | `11011` | FIGS | FIGS |
| 28 | `11100` | M | `.` |
| 29 | `11101` | X | `/` |
| 30 | `11110` | V | `=` |
| 31 | `11111` | LTRS | LTRS |

This table follows ITU-T S.1 (03/1993). Older or national tables may place `£`, `$`, `!`, `&`, quotation marks, semicolon, or other characters in the three nationally assignable positions or substitute them elsewhere.

### USTTY differences

A widely used American Teletype/USTTY figures set normally included:

- `00101` / S → BEL in some arrangements
- `01001` / D → `$`
- `01011` / J → apostrophe or BEL, depending on equipment
- `01101` / F → `!`
- `10100` / H → `#`
- `11010` / G → `&`
- `11110` / V → `;` rather than ITA2 `=`

Exact assignments must be identified from the machine’s typebox, keyboard, or governing manual. “Baudot” is not enough metadata.

## Repertoire and expressive limits

**[STANDARD]** S.1 provides:

- 26 Latin alphabetic characters
- digits 0–9
- `. , : ? ’ + - / = ( )`
- three positions for national/private graphic characters
- WRU, audible signal, CR, LF, LTRS, FIGS, SPACE, and NUL

It cannot directly and unambiguously represent:

- both uppercase and lowercase in ordinary two-state use
- accented Latin alphabets in full
- Greek, Cyrillic, Hebrew, Arabic, or Indic repertoires
- Chinese characters, Japanese kana plus kanji, or Korean Hangul/Hanja
- arbitrary mathematical notation
- modern typographic punctuation
- emoji
- combining marks
- language tags or normalization distinctions

**[STANDARD]** S.1 explicitly declines to define whether the alphabetic glyphs print as capitals or lowercase. In practice, ordinary teleprinters normally printed a single case, overwhelmingly capitals.

**[STANDARD]** Recommendation S.2 later defined sequences permitting teleprinters with both capital and small letters while retaining compatibility with single-case machines. That is an extension protocol, not evidence that ordinary historical ITA2 encoded case as an intrinsic property.

## Controls

### NUL: `00000`

All five tape positions are unpunched. It causes no printing and normally no tape-position movement.

Blank tape and an encoded NUL are physically indistinguishable. That makes NUL useful as leader or unused material, but it also means blank regions do not carry a visually countable row unless sprocket-feed progression supplies the timing.

S.1 prohibits ordinary combination 32 use during the communication phase of international telex, while allowing national or bilaterally agreed control uses.

### SPACE: `00100`

Space is a real spacing character. Unlike NUL, it advances the carriage.

“Unshift on space” is an implementation or operating convention found in some RTTY equipment: receiving SPACE also restores Letters state. It improves readability when a FIGS-to-LTRS transition has been lost, but damages figure groups separated by spaces. It is not an inherent property of the S.1 table.

### CR: `01000`

Carriage return moves the carriage to the left margin without advancing the paper.

### LF: `00010`

Line feed advances the paper without returning the carriage.

A new line therefore normally requires the pair:

```text
CR LF
01000 00010
```

The functions are separate because the receiving machine is literally controlling two mechanical motions. Their survival as distinct ASCII and Unicode-compatible control codes is a direct teleprinter legacy.

### FIGS: `11011`

Locks the receiver in the figures/punctuation state.

### LTRS: `11111`

Locks the receiver in the letters state.

Because `11111` punches every data position, an erroneous tape row could be overpunched to all holes. The resulting combination becomes LTRS, which does not print or space. It is therefore often described as “erasure” or “delete.”

This correction has limits:

- It prevents the erroneous tape row from printing when the corrected tape is later transmitted.
- It does not erase a character already printed.
- It also forces Letters state, so an operator may have to repunch FIGS afterward.
- ITA2 has no separate deletion code equivalent in semantics to an editing operation.

ASCII’s `DEL` at `0x7F`, likewise all seven holes, generalized this paper-tape overpunch property. The physical rationale is documented; claims that ITA2 LTRS could securely “destroy messages” are later embellishment unless tied to a specific procedure.

### WRU: figures-D

The “Who are you?” function participates in the sequence that triggers the remote telex terminal’s answerback unit. The machine responds with its stored station identity, providing operational assurance that the intended subscriber is connected.

S.1 identifies the international WRU sequence through Recommendations S.6, S.8, and the U-series switching rules. Treating figures-D alone as universally identical on every national machine is unsafe.

### BEL: figures-J

Operates an audible signal. Some machines also print a symbol.

## Collating order

ITA2 defines no useful universal alphabetic collation.

If raw five-bit numeric values are sorted in Letters state, the rough sequence is:

```text
NUL, E, LF, A, SPACE, S, I, U, CR, D, R, J,
N, F, C, K, T, Z, L, W, H, Y, P, Q, O, B,
G, FIGS, M, X, V, LTRS
```

That is approximately the famous `ETA...` frequency-oriented order, not alphabetical order. In Figures state the same numeric sequence denotes a different collection of digits, signs, national characters, and controls.

A stream also has state: `00001` means E after LTRS but 3 after FIGS. Sorting encoded units without interpreting shifts does not sort characters. Fischer reports that computer designers regarded this sequence as unsuitable for data processing, one pressure behind later codes with contiguous digits and alphabetic blocks.

## Paper tape

Five data positions were punched across the tape, with a smaller continuous feed or sprocket hole track used mechanically to move the tape. A punched data hole represents one binary condition; an unpunched position the other.

The important distinction is:

- **five data holes/positions** encode the character;
- the feed hole is mechanical and is not a sixth data bit;
- start and stop elements belong to serial transmission framing and are not normally extra data columns in each five-unit tape row.

Murray’s method separated composition from transmission:

1. An operator typed on a typewriter-like keyboard.
2. A perforator punched five-unit rows.
3. The tape could be checked, queued, spliced, or corrected.
4. A transmitter-distributor read it faster and more regularly than direct manual signaling.

This store-and-forward medium improved line utilization and decoupled typist rhythm from line timing.

## On-wire framing and synchronization

The logical character is five units, but start-stop apparatus normally transmitted:

```text
idle MARK | START SPACE | 5 data elements, least-significant first | STOP MARK
```

Many historical 45.45-baud systems use approximately 1.5 stop-unit intervals, giving 7.5 unit intervals per character. Other apparatus and services used different stop durations.

### What start-stop framing repairs

Each start transition launches the receiver’s selector timing. The stop interval lets it return to rest. Thus a receiver can regain character boundary at a later valid start, rather than requiring Baudot’s original continuously synchronized distributor to remain in phase indefinitely.

### What it does not repair

ITA2 has:

- no parity bit
- no checksum
- no error-correcting redundancy at the alphabet level
- no unambiguous self-synchronizing bit pattern
- no intrinsic declaration of the current shift state

A flipped data element generally becomes another valid character or control. A false or missed start can garble a character but later start bits may restore framing. A corrupted FIGS or LTRS is worse: all subsequent dual-use combinations may be interpreted in the wrong state until another explicit shift is received.

Operational countermeasures included:

- starting transmission with LTRS or FIGS
- retransmitting shift characters
- doubling shifts in noisy radio work
- “unshift on space”
- sending recognizable test material
- requesting repetition
- answerback and higher-layer message procedures

**[STANDARD]** S.1 requires the first transmitted combination after receiving characters or when beginning transmission to be LTRS or FIGS, as far as applicable to the equipment. This is state synchronization, not error detection.

**[OPERATOR PRACTICE]** Doubling shifts and unshift-on-space are documented operational techniques, but not properties of the base alphabet.

## Worked example 1: `HELLO, WORLD 123.`

Assume international ITA2, an initial Letters shift, and conventional binary display.

| Step | Character/action | State after unit | Decimal | Binary |
|---:|---|---|---:|:---:|
| 1 | LTRS | Letters | 31 | `11111` |
| 2 | H | Letters | 20 | `10100` |
| 3 | E | Letters | 1 | `00001` |
| 4 | L | Letters | 18 | `10010` |
| 5 | L | Letters | 18 | `10010` |
| 6 | O | Letters | 24 | `11000` |
| 7 | FIGS | Figures | 27 | `11011` |
| 8 | comma | Figures | 12 | `01100` |
| 9 | SPACE | Figures | 4 | `00100` |
| 10 | LTRS | Letters | 31 | `11111` |
| 11 | W | Letters | 19 | `10011` |
| 12 | O | Letters | 24 | `11000` |
| 13 | R | Letters | 10 | `01010` |
| 14 | L | Letters | 18 | `10010` |
| 15 | D | Letters | 9 | `01001` |
| 16 | SPACE | Letters | 4 | `00100` |
| 17 | FIGS | Figures | 27 | `11011` |
| 18 | 1 | Figures | 23 | `10111` |
| 19 | 2 | Figures | 19 | `10011` |
| 20 | 3 | Figures | 1 | `00001` |
| 21 | full stop | Figures | 28 | `11100` |

Five-unit stream:

```text
11111 10100 00001 10010 10010 11000 11011
01100 00100 11111 10011 11000 01010 10010
01001 00100 11011 10111 10011 00001 11100
```

Notice that:

- comma requires entry to Figures state;
- W and digit 2 share `10011`;
- E and digit 3 share `00001`;
- O and digit 9 share `11000`;
- punctuation can force extra shift traffic;
- if the LTRS after the comma is lost, `WORLD` becomes approximately `29/4)` under the figures interpretation.

If stored naïvely in eight-bit computer octets with the top three bits zero, the values would be:

```text
1F 14 01 12 12 18 1B 0C 04 1F 13 18 0A 12 09 04 1B 17 13 01 1C
```

That packing is a modern storage convention, not the historical line representation.

### ASCII comparison

ASCII/UTF-8 for the same all-ASCII text needs no shifts:

```text
H  E  L  L  O  ,  SP W  O  R  L  D  SP 1  2  3  .
48 45 4C 4C 4F 2C 20 57 4F 52 4C 44 20 31 32 33 2E
```

ASCII uses 17 seven-bit characters, conventionally stored as 17 octets. The ITA2 example uses 21 five-unit combinations because four state changes are present. On an asynchronous line, framing overhead must also be counted.

UTF-8 produces the identical octets because ASCII is its invariant one-byte subset.

## Worked example 2: case and an unrepresentable character

Input:

```text
Baudot café ☎
```

Ordinary ITA2 can encode only an approximation:

```text
BAUDOT CAFE
```

It loses:

- the distinction between `B` and `b`;
- the acute accent in `é`;
- the telephone symbol;
- any typography distinguishing apostrophe variants or dash lengths.

A transliteration or agreed national character could preserve some information, but it would no longer be universally interpretable ITA2.

UTF-8 preserves the Unicode text:

```text
B   42
a   61
u   75
d   64
o   6F
t   74
SP  20
c   63
a   61
f   66
é   C3 A9
SP  20
☎   E2 98 8E
```

---

# Origins

## Before Baudot

### Telegraphic predecessors

**[DOCUMENTED HISTORY]** Baudot did not invent electrical telegraphy, printing telegraphy, binary signaling, or multiplexing in isolation.

Relevant predecessors include:

- Morse-family variable-length telegraph codes
- David Edward Hughes’s printing telegraph and synchronized typewheel
- Bernard Meyer’s multiplexing distributor
- five-element signaling ideas associated with Gauss and Weber
- paper-tape automatic telegraphy, especially Wheatstone apparatus

The importance of Baudot’s mature system lies in its integration of:

- fixed-length two-state character combinations;
- a five-key human input method;
- synchronized time-division multiplexing;
- automatic printing of received text.

Fischer calls Baudot’s apparatus the first widely adopted device to represent letters, numbers, and symbols as uniform-length binary sequences. “First digital communication” is a modern honorific, not a contemporary category, and should not be allowed to erase earlier binary or discrete signaling systems.

## Émile Baudot, 1872–1877

Jean-Maurice-Émile Baudot was born on 11 September 1845 at Magneux, France, and died on 28 March 1903. He entered the French postal and telegraph administration in 1870 and began work on his multiplex printing system around 1872.

### The 1874 patent

**[STANDARD/PATENT RECORD]** Baudot obtained French patent no. 103,898, *Système de télégraphie rapide*, on 17 June 1874.

**[DISPUTED DETAIL]** It is frequently said that this patent contains “Baudot’s five-bit code.” Fischer states that he had not obtained the patent and inferred from Baudot’s later writing that the early machine probably used a six-unit code. Other modern accounts assert that the 1874 patent was initially six-unit and the five-unit form arrived in 1876.

The safe reconstruction is:

- 1874 securely dates Baudot’s patented rapid printing/multiplex system;
- the mature five-unit system is securely documented by 1876–1877;
- treating every feature of the later Baudot alphabet as unquestionably present in the first patent overstates the surviving evidence.

### The piano keyboard

**[CONTEMPORARY/RECONSTRUCTION]** The mature transmitter used five piano-like keys. Operators used two fingers of one hand and three of the other to form combinations. They had to memorize the code and strike the appropriate chord in cadence with the multiplex distributor.

After a combination was entered, the keys remained locked until the distributor reached that operator’s time slot. An audible cadence indication told the operator when the next character could be entered. Typical working speed was about 30 words per minute per operator.

The familiar description of “five keys, one for each bit” is essentially accurate, but the word *bit* is retrospective.

### Why Baudot’s alphabet had its order

Baudot’s assignment was adapted to manual chord entry. Frequent letters were generally given combinations intended to reduce difficult finger movements or key changes. The arrangement is not the later ITA2 numeric table.

**[IMPORTANT CORRECTION]** The original Baudot code and ITA2 are not interchangeable. A tape or bitstream in one decoded under the other produces nonsense.

### Adoption

The French administration tested Baudot’s prototype in the mid-1870s and adopted versions of the system. It spread to other European administrations and was used on terrestrial and submarine routes. British Post Office versions had inland and continental substitutions.

The system was synchronous at the multiplex level: sending and receiving distributors had to maintain unison. Its strengths were efficient use of an expensive circuit and immediate printing; its weakness was the specialized, cadence-trained operator.

## The Mimault priority dispute

**[DISPUTED, CONTEMPORARY LEGAL CONTROVERSY]** Jean or Bernard Mimault asserted priority over aspects of Baudot’s apparatus/code. A French civil tribunal reportedly found for Mimault and regarded Baudot’s patents as improvements, but that judgment was later reversed or rescinded, with costs assessed against Mimault.

Later biographies add the extraordinary sequence that Mimault wounded two École Polytechnique students, demanded official recognition and money, and after rejection murdered Jules Raynaud, the head of a commission examining his demands.

This dispute is real enough to reject an uncomplicated lone-inventor legend, but online retellings often cite one another. The present research located later historical accounts, not the full trial record or patent-comparison dossier. Precise technical priority between Mimault and Baudot therefore remains an open archival question.

## Donald Murray, 1899–1912

Donald Murray was a New Zealand journalist and inventor, usually dated 1865 or 1866–1945. He moved from Australia to New York around 1899; the addresses in his US patent filings support that chronology.

### What Murray changed

Murray’s fundamental operational move was to put a typewriter-like keyboard and punched tape between the typist and the line.

The operator no longer formed five-element chords in distributor cadence. Pressing one ordinary key caused the perforator to punch the corresponding code row. An automatic reader later transmitted the tape.

Murray consequently optimized the code for machinery and paper rather than for finger chords:

- common letters received combinations with fewer punched holes;
- rarer letters could use more holes;
- the arrangement preserved tape strength and reduced punching work/wear;
- digits were paired with letters so they could appear in ordinary keyboard order;
- carriage return, line feed, and other machine operations received combinations.

### Murray patents

Primary US documents include:

- US 638,591, *Actuating Mechanism for Key-Operated Machines* (1899)
- US 653,934, *Page-Printing Telegraph* (1900)
- US 653,936, *Page-Printing Telegraph* (1900)
- US 670,964, *Telegraphy*, filed 17 January 1901 and issued 2 April 1901
- US 685,427 (1901)
- US 698,845 (1902)
- US 710,163, *Keyboard Perforator* (1902)

US 670,964 explicitly describes automatic paper-tape transmission, unit-duration impulses and their multiples, an electromagnetic receiving perforator, and apparatus for keeping the receiver in unison.

### Did Murray invent Letters/Figures shift?

**[DISPUTED TERMINOLOGY]** Many summaries say Murray “introduced” LTRS and FIGS. That is too simple. Baudot-family systems already used alternate letter and figure functions or spaces. Murray redesigned and operationalized the shift structure for typewriter keyboard, paper tape, and page-printer use. The final ITA2 allocation was produced by committee after further Baudot-, Murray-, Morkrum-, Western Union-, and national-system evolution.

Thus:

- Baudot deserves credit for the early successful five-unit family and multiplex system.
- Murray deserves credit for a distinct automatic printing-telegraph architecture and influential rearranged code.
- CCIT deserves credit for ITA2 as the negotiated international table.
- Calling ITA2 “Baudot” is conventional ancestry, not exact authorship.

## Morkrum, Kleinschmidt, Teletype, and Western Union

In the United States, Morkrum and Kleinschmidt companies developed start-stop printers and related apparatus. Morkrum-Kleinschmidt became the Teletype Corporation and was acquired by AT&T in 1930.

Western Union evaluated printing systems and adopted Murray multiplex equipment following a recommendation dated 16 January 1912. The surviving Western Union history describes the desired system as using:

1. a five-unit shifted alphabet;
2. keyboard perforators;
3. perforated-tape reception;
4. printing from the received slip.

US systems evolved their own code assignments. Fischer found Morkrum/Teletype code tables in 1931 bulletins but could not document exactly when the familiar later US five-level table first displaced earlier variants. That gap should be retained rather than filled with an invented date.

## Start-stop telegraphy

Baudot’s multiplex required continuously synchronized distributors. Start-stop teleprinters instead framed each character so the receiver could restart its timing independently.

The invention of practical start-stop machinery involved several engineers and firms; it should not be attributed solely to either Baudot or Murray. Morkrum/Kleinschmidt development is especially important in the US lineage.

The conceptual legacy is enormous: asynchronous serial ports still use idle, start, data, optional parity, and stop intervals, even though their character codes and electronics have changed.

---

# International standardization

## CCIT, 1926

The *Comité Consultatif International des Communications Télégraphiques* first met in Berlin in November 1926. One problem was the proliferation of mutually incompatible five-unit codes.

Delegate Stahl reviewed existing codes and proposed a frequency-based international alphabet. The French delegation objected that operators on the large installed base of Baudot equipment could not reasonably be retrained for an entirely new table.

Other disagreements included:

- French concern for compatibility with Baudot practice;
- British preference for paired “letter space” and “figure space” arrangements;
- Soviet need for extra letters in Cyrillic;
- Czechoslovak concern about accented characters;
- F. G. Creed’s proposal to consider six units.

Creed’s six-unit suggestion did not prevail. The five-unit installed base constrained the standard.

## Berlin, 1929

At the second CCIT meeting, a subcommittee reportedly deliberated for only a few hours before producing a proposed Alphabet No. 2 combining much of Baudot’s letter allocation with English Murray letter/figure pairings and national positions.

The intended division was:

- Alphabet No. 1 for synchronous multiplex systems;
- Alphabet No. 2 for start-stop apparatus.

**[DOCUMENTED DISPUTE]** The USSR vigorously opposed standardizing both proposals. Cyrillic required more letter positions than the Latin-only letter case could provide, making the placement and behavior of spaces and shifts materially important.

The British also planned a public teleprinter exchange using ordinary-office subscribers, for whom an American-style keyboard with distinct space and shift keys was preferable to systems with dual space bars.

## 1931 revision

At a June 1931 meeting, the committee resolved to replace the earlier proposed Alphabet No. 2 with a table more directly based on Murray practice. The final table includes the familiar sequence in which E and T have one-hole combinations.

## Madrid, 1932

**[STANDARD]** The 1932 Madrid Telegraph Regulations formally published International Telegraph Alphabets Nos. 1 and 2.

The Madrid conference also reorganized international telecommunications governance, combining telegraph and radiotelegraph conventions under the International Telecommunication Union name.

The phrase “CCITT standardized ITA2 in 1932” is slightly anachronistic:

- the responsible technical body was then **CCIT**;
- **CCITT** was formed in 1957 by merging CCIT with the telephone committee CCIF;
- modern ITU-T editions preserve the alphabet through Recommendation S.1.

## 1948 and later

In May 1948 the United States proposed adoption, with reservations, of Alphabet No. 2 as the general five-unit code for international telegraphy; CCIT accepted.

At the same meeting, a British proposal to use the unused combination as a third shift received support but was deferred for study. Expansion pressure persisted.

In 1956–1958 the committees considered whether six units were needed for diacritics and data-processing functions. A Warsaw meeting judged a new alphabet premature but identified acute, grave, circumflex, diaeresis/umlaut, and tilde among required marks.

S.2 eventually provided an extended shift scheme for uppercase and lowercase, but only in 1988—far too late to change ordinary ITA2’s cultural identity as uppercase telegraph text.

---

# Adoption and use

## Government and commercial telegraphy

Baudot multiplex installations served national administrations and international circuits. Murray-derived automatic tape systems improved throughput on busy routes.

Paper tape permitted:

- preparation before circuit time was available;
- rapid automatic sending;
- retransmission;
- mechanical relay or reperforation between routes;
- storage and queuing;
- editing by overpunching an erroneous row to all holes.

## Western Union

Western Union’s 1912 recommendation favored Murray’s basic operating model. The company subsequently used Murray and related five-unit systems extensively.

The phrase “Western Union adopted Baudot” can conceal three layers:

1. adoption of five-unit printing-telegraph principles;
2. adoption of Murray multiplex apparatus;
3. later compatibility with American Teletype/ITA2-related codes.

These did not necessarily use one immutable table.

## Teletype machines

Prominent five-level machines included:

- Teletype Model 14 tape printers and transmitter-distributors
- Model 15 page printer, introduced around 1930
- Model 19, combining a Model 15 with tape facilities
- Model 26
- Model 28 family, commercially introduced in the early 1950s
- Model 31 compact tape printer
- Model 32, the five-level sibling of the ASCII Model 33

The Model 15 became a principal US military and news-service machine during the Second World War. Approximately 200,000 are commonly reported as manufactured, though that figure should be treated as company-history reconstruction rather than a standard.

The Model 28’s replaceable typebox and mechanical “stunt box” made it adaptable to different code figures and control functions.

## News wires

Press services used receive-only teleprinters to distribute stories to newspapers and broadcasters. The distinctive clatter became an audible signifier of breaking news; recordings of teleprinters continued to be used after the machinery itself disappeared.

The lack of lowercase and typesetting controls was costly for newspapers. TeleTypeSetter systems consequently used six-level codes to carry richer typesetting instructions and mixed-case copy.

## Military and cryptographic systems

Five-unit teleprinter traffic was attractive for machine cryptography because each character was already a fixed five-element vector. Systems such as the German Lorenz machine combined teleprinter data with generated key streams.

At Bletchley Park, British cryptanalysts displayed teleprinter codes in “reflection” or Gray-like order for analytic convenience. This is not a different ITA2 transmission order.

A corrupted shift character was especially troublesome in ciphertext recovery and noisy radio operation because its effect persisted. Operators sometimes sent repeated shifts.

## Telex and Gentex

Telex provided switched subscriber-to-subscriber teleprinter service. It developed from European public teleprinter networks in the early 1930s and expanded internationally after the Second World War.

Typical telex operation used:

- ITA2
- 50 baud
- start-stop signaling
- page-printing teleprinters
- answerback identifiers
- dial or automatic switching

ITU-T S.1 says ITA2 is defined for the international public telegram service in F.1 and specified for telex in F.60.

**Gentex** applied switched teleprinter networking within or between telegraph administrations rather than ordinary private subscribers.

Telex’s advantages included:

- immediate written delivery;
- automatic answerback;
- durable sender and receiver copies;
- worldwide addressing and interconnection;
- legal and commercial familiarity.

## TWX

AT&T’s Teletypewriter Exchange Service, TWX, is related but not identical to international telex. Early TWX used five-level machines; the direct-dial network introduced in 1962 also drove adoption of higher-speed equipment and larger codes. Model 33 and Model 35 ASCII machines belong to that later transition.

## Telecommunications for deaf users

Surplus Teletype machines and acoustic couplers were crucial in the development of telephone text communication for deaf people. Robert Weitbrecht and organizations including Teletypewriters for the Deaf helped establish networks using five-level machines.

A 1974 TDI manual explicitly discusses Model 15, 28, and 32 equipment, nominal 45.45-baud/60-wpm operation, and the practical maintenance of donated machines.

Later TTY/TDD protocols and devices were not all precisely ITA2; Baudot-derived codes, speed, stop-bit, and character assignments varied. “TTY” can mean teleprinter generally, a deaf telecommunications device, or the Unix terminal abstraction, and must be contextualized.

## Radioteletype

Radio teletype maps the two signal conditions to radio modulation, commonly frequency-shift keying.

Typical amateur HF RTTY today uses:

- ITA2 or USTTY-compatible characters
- 45.45 baud
- 170 Hz shift
- mark and space tones or FSK frequencies
- uppercase presentation
- repeated LTRS/FIGS or unshift-on-space options

The ITU describes narrow-band direct-printing amateur operation with five-level ITA2, 170 Hz FSK separation, and approximately 45.45 bit/s. The US amateur rules expressly list the five-unit start-stop ITA2 code defined in ITU-T F.1, “commonly known as Baudot.”

Thus survival in amateur radio is **documented current practice**, not merely nostalgia.

## Maritime and specialist use

Radiotelex and narrow-band direct-printing systems survived in maritime, meteorological, military, aviation, and point-to-point services after public telex declined. Some systems add error detection or retransmission at a higher layer rather than changing ITA2 itself.

Statements that ITA2 remains universally central to maritime safety should be qualified: modern GMDSS includes satellite and digital selective systems with other encodings, while legacy or specialist NBDP remains only part of the landscape.

---

# Replacement and decline

## Why five units became insufficient

The same economy that made five units attractive imposed severe limitations:

- shift state made errors persistent;
- controls and printable characters competed for 32 combinations;
- national alphabets were incompatible;
- no ordinary lowercase;
- poor raw collation;
- too little punctuation for programming;
- no inherent error check;
- conversion between variants required contextual knowledge;
- computer storage and processing benefited from direct, stateless character numbers.

## Six-bit alternatives

Before seven-bit ASCII prevailed, many systems used six-bit codes:

- TeleTypeSetter
- FIELDATA
- IBM BCD-derived sets
- proprietary computer and punched-card codes
- Japanese six-unit teleprinter systems

Six bits provide 64 combinations, often enough for one case, digits, punctuation, and controls without ITA2-style letter/figure shifting, but still not enough for globally comprehensive text.

## ASCII

The American Standards Association’s X3 committee developed ASCII through subcommittee X3.2. The first standard was **ASA X3.4-1963**. The major revised form was **USAS X3.4-1967/1968**, with lowercase and the familiar modern layout.

ASCII did not instantaneously “replace Baudot in 1963.” Rather:

- 1963 marks publication of the first ASCII standard;
- ASCII-capable commercial terminals emerged during the 1960s;
- federal procurement and network rules accelerated adoption;
- telex, RTTY, military, and installed teleprinter systems continued using five-unit codes for decades.

### Federal mandate

On 11 March 1968, President Lyndon B. Johnson approved federal use of standard interchange code and media standards. New federal computer configurations acquired from 1 July 1969 had to be capable of using ASCII where the specified media applied.

FIPS PUB 1, issued 1 November 1968, adopted the code. Calling this a blanket 1968 ban on EBCDIC or mandatory internal ASCII representation would be wrong; the requirement was capability and interchange-oriented.

### ARPANET

RFC 20, issued by Vint Cerf on 16 October 1969, proposed standard seven-bit ASCII embedded in an eight-bit byte with the high bit zero for host-to-host interchange. It reproduced USAS X3.4-1968.

## ITA2’s direct legacies in ASCII

Several ASCII features preserve teleprinter history:

- NUL
- BEL
- CR
- LF
- shift concepts such as SI and SO, although not ITA2 LTRS/FIGS semantics
- DEL as the all-holes paper-tape rubout
- serial communication terminology: mark, space, start, stop
- terminal control conventions
- uppercase wire-service aesthetics
- CRLF as a compound newline

ASCII was deliberately organized into useful numeric blocks. Digits and letters collate in contiguous sequences, unlike ITA2’s frequency-oriented arrangement.

## EBCDIC and the “eight-bit defense”

IBM’s EBCDIC was a separate eight-bit development rooted in punched-card and BCDIC traditions, not a direct enlargement of ITA2. The folklore that IBM chose “eight bits merely to defeat ASCII” oversimplifies a transition involving System/360 byte architecture, compatibility with IBM card codes, six-bit predecessors, and commercial installed bases.

No direct ITA2-specific primary document substantiating a pithy “eight-bit defense” quotation was located in this research. It belongs to the broader ASCII/EBCDIC dossier.

## ISO and ECMA successors

The five-unit problem fed into work on larger international alphabets:

- **ECMA-6:** seven-bit coded character set
- **ISO 646:** international seven-bit code with national positions
- **CCITT International Alphabet No. 5**, later International Reference Alphabet
- **ISO 2022:** code-extension techniques and designation of character sets
- **ISO 8859:** eight-bit single-byte graphic sets
- **ISO/IEC 10646:** universal coded character set
- **Unicode:** synchronized universal character repertoire
- **UTF-8:** variable-length Unicode transformation compatible with ASCII bytes

ISO 646’s national positions echo ITA2’s compromise: reserve a small number of shared positions for local currency signs or letters. That approach produced incompatibilities such as `#`, `£`, and national letters occupying the same value in different variants.

## Telex decline

Fax, electronic mail, packet data, private corporate networks, and later the Internet displaced telex. Decline varied by country; there is no single worldwide shutdown date. Some national networks ended in the 1990s or later, while gateways, maritime services, and private systems persisted.

Therefore “ITA2 ended in 1963” is false. It ceased to be the future of general information interchange in the 1960s, but remained operational infrastructure long afterward.

---

# The other scripts

## Structural problem

An ordinary two-state ITA2 machine has 26 dual-use printable positions. The Letters side is essentially exhausted by A–Z. International Figures uses many of the other meanings for digits, punctuation, and functions.

Non-Latin use therefore required one or more of:

- transliteration into Latin letters;
- national reassignment;
- extra shift states;
- omission of punctuation;
- codebooks mapping words or characters to digit groups;
- wider six-, seven-, or eight-unit codes;
- an entirely different telegraph alphabet.

## Accented Latin scripts

Three figure-case positions were left undefined for national/private use. Administrations placed accented letters and currency signs there, but three positions were radically insufficient for many European orthographies.

Consequences included:

- omission of diacritics;
- substitutions such as `AE`, `OE`, or national conventions;
- incompatible national typeboxes;
- information loss during international conversion;
- special bilateral agreements.

At the 1926 standardization discussions, the Czechoslovak delegation explicitly raised the neglected accented-letter problem. The installed five-unit base prevailed over a general solution.

## Cyrillic and MTK-2

The Soviet/Russian **MTK-2** derivative added a third shift state for Cyrillic. Combination `00000`, NUL in standard ITA2, could select Russian letters. Latin and Cyrillic letters were paired where possible, while extra Cyrillic characters occupied positions otherwise used for punctuation or controls.

This provided practical Russian teleprinter support but illustrates the cost of stateful extension:

- an additional persistent mode;
- fewer signs;
- incompatibility with a strict international decoder;
- catastrophic-looking output if the wrong shift state is assumed.

The Soviet delegation’s objections during CCIT work were therefore technical and linguistic, not merely nationalist resistance.

## Greek

Greek required a national alphabet or transliteration. Twenty-four basic Greek letters fit numerically into a 26-position letter case, but accents, final sigma distinctions, punctuation, and Latin interchange complicate the arrangement. No single universal Greek ITA2 table emerged as the international repertoire.

## Hebrew

Hebrew could be assigned to a national letters set, but ITA2 itself provides no bidirectional model. A teleprinter is fundamentally a sequential physical printer.

Possible strategies were:

- transliteration;
- machines printing right-to-left;
- entering or transmitting characters in visual order suitable for a particular printer;
- reversing text through an operator or intermediate device.

These approaches encode glyph sequences, not modern logical-order bidirectional text. Mixing Hebrew with Latin or numbers is especially problematic.

## Arabic

Arabic presents both directionality and contextual shaping. Ordinary ITA2 has no concept of:

- joining behavior;
- isolated, initial, medial, or final forms;
- combining marks;
- right-to-left embedding;
- bidirectional runs.

National Arabic teleprinters could use type forms or presentation-form encodings and mechanical direction conventions, but these were device-specific solutions. Transliteration was another fallback. They should not be described as features of international ITA2.

## Indic scripts

Indic writing systems require more consonants and vowels than one ITA2 letters state and normally combine base letters, dependent vowel signs, viramas, and conjuncts. Five-unit ITA2 supplies neither adequate repertoire nor a shaping model.

Romanization, codebooks, or specialized wider codes were necessary. Modern Unicode generally encodes underlying characters in logical order and delegates shaping to software—a fundamentally different abstraction.

## Chinese

A five-unit alphabet cannot directly encode thousands of Chinese characters.

Chinese telegraphy used a codebook system. Septime Auguste Viguier published an influential Chinese telegraph code in 1872, based on numbered entries; later Chinese Commercial Code systems represented characters by four decimal digits. Those digits could then be sent over Morse or teleprinter circuits.

The codebook is therefore an application-layer encoding over the transport alphabet. ITA2 carries the digits; it does not itself encode the Han character.

Codebooks had political and practical consequences:

- only listed characters were available;
- ordering reflected dictionary and administrative choices;
- additions and simplification policies created mainland/Taiwan divergences;
- operators had to encode and decode manually or with specialized machinery.

## Japanese

Japan used Morse-derived Wabun code for kana and developed domestic teleprinter encodings beyond ITA2. A documented 1925 Japanese public-telegram system used a six-unit code and a multi-shift typebar arrangement supporting alphanumerics, kana, and other symbols.

Kanji posed the same scale problem as Chinese. Specialized kanji teleprinters emerged later; Japan’s Computer Museum records a 1955 joint development by Shinko and *Asahi Shimbun* and a commercial SC-4 system in 1958.

## Korean

Hangul syllables can be represented through jamo composition, but ITA2 has neither sufficient repertoire nor a composition model. Romanization, codebooks, or national wider codes were required. Hanja introduces the full ideographic scale problem.

## Emoji

Emoji are wholly outside ITA2’s design domain. A textual name such as `SMILE` can be sent; the pictograph cannot.

The “emoji vote,” Unicode Technical Committee proposals, and Consortium membership politics belong to Unicode’s governance history. They have no historical role in the design of ITA2.

---

# People and institutions

## Émile Baudot

- **1845–1903**
- French postal and telegraph employee
- integrated fixed-length signaling, five-key operation, multiplex distribution, and printing
- received the 1874 rapid-telegraph patent
- namesake of the baud

His achievement was systemic rather than the invention of every component.

## Donald Murray

- **1865/1866–1945**
- New Zealand-born journalist and inventor
- worked in Australia, the United States, and Britain
- developed automatic page-printing and tape apparatus
- replaced chorded cadence entry with typewriter-keyboard perforation
- rearranged the alphabet around paper-tape and machine constraints

The one-year birth-date discrepancy persists across secondary sources and should be resolved from civil records or a definitive biography.

## David Edward Hughes

Hughes’s printing telegraph provided an important mechanical predecessor. Baudot improved line use by replacing variable waiting for a typewheel position with uniform-length combinations and multiplex slots.

## Bernard Meyer

Meyer’s distributor work contributed to the multiplex lineage on which Baudot built.

## F. G. Creed

Creed developed successful printing telegraph equipment, participated in British telegraph engineering, and proposed considering a six-unit international alphabet during CCIT deliberations. The proposal did not prevail.

## Stahl, Booth, Feuerhahn, and national delegates

The final ITA2 table was committee work:

- **Stahl** presented a frequency-based proposal in 1926.
- **Booth**, a British delegate, explained British public-exchange keyboard requirements.
- **Feuerhahn**, of Germany, defended continued development of the earlier international-alphabet plan.
- Soviet delegates pressed Cyrillic requirements.
- Czechoslovak delegates pressed accented-letter requirements.

Their roles show why ITA2 should not be credited to a single inventor.

## Morkrum, Kleinschmidt, and Teletype

Morkrum and Kleinschmidt engineers made start-stop teleprinters commercially practical. Corporate consolidation produced the Teletype Corporation, acquired by AT&T in 1930. Its machines became synonymous in the United States with printed electrical communication.

## Western Union, AT&T, and the Post Office

- **Western Union:** adopted Murray multiplex principles and operated extensive telegraph networks.
- **AT&T/Bell System:** operated TWX and owned Teletype.
- **British Post Office:** operated Baudot, Murray, and teleprinter systems and contributed heavily to standards practice.
- **French telegraph administration:** supplied Baudot’s institutional setting and protected the installed Baudot lineage during international negotiations.

## CCIT, CCITT, ITU, and ITU-T

- International Telegraph Union founded in 1865.
- CCIT established in 1926 for telegraph technical consultation.
- Madrid 1932 reorganized international telecommunications.
- CCIT and CCIF merged into CCITT in 1957.
- ITU-T succeeded CCITT’s standardization role in 1993.

## Hollerith and IBM

Herman Hollerith’s punched-card systems belong to a parallel data-processing lineage. They influenced IBM codes and ultimately the ASCII/EBCDIC conflict, but not the initial Baudot or Murray alphabet design.

## Bemer and Mackenzie

- **Robert W. Bemer** participated in ASCII development and later published first-person historical accounts and memoranda.
- **Charles E. Mackenzie** reconstructed the history of ASCII, EBCDIC, punched-card codes, and international standardization in his 1980 book.

Neither designed ITA2. They matter because they document how computer codes departed from teleprinter constraints.

## Becker, Collins, Davis, Whistler, Thompson, and Pike

These people belong to the much later universal-encoding lineage:

- Joe Becker, Lee Collins, and Mark Davis began Unicode work in discussions between Xerox and Apple engineers in 1987.
- Ken Whistler became a major early database and editorial contributor.
- Unicode Inc. was incorporated on 3 January 1991.
- Ken Thompson devised the UTF-8 transformation in 1992 in discussion with Rob Pike.

The diner-placemat account of UTF-8 is a **[PARTICIPANT RECOLLECTION]** chiefly carried by Pike’s later account. It is not an ITA2 anecdote and has no bearing on Baudot/Murray priority.

---

# Culture

## “Plain text”

Baudot and ITA2 demonstrate that plain text is never merely natural writing. It is an institutional agreement connecting:

- electrical states;
- perforations;
- mechanical movements;
- code positions;
- shift state;
- glyphs;
- language conventions.

A five-unit tape is “plain” only when its alphabet variant, bit orientation, shift state, and control conventions are known.

## Telegram style

Uppercase telegram prose, abbreviated wording, omitted accents, and constrained punctuation arose partly from price, operational convention, and repertoire limits. ITA2 helped give machine communication its clipped visual voice.

The association of ALL CAPS with urgency or machinery outlived the hardware.

## The sound of news

Teleprinters became part of twentieth-century media iconography. Their clatter signaled a newsroom, wire service, military command center, or unfolding crisis. Recorded “teletype” sound effects persisted after electronic terminals had replaced the machines.

## Paper-tape aesthetics

Rows of holes are simultaneously text and visible machine state. They recur in museum displays, retrocomputing artwork, jewelry, tattoos, puzzles, and fictional depictions of “computer code.”

A strip labeled “Baudot” may be:

- original Baudot;
- ITA1;
- Murray;
- USTTY;
- ITA2;
- reversed bit order;
- decorative modern binary.

Decoding should begin with physical and historical identification, not an online converter.

## Literature

Harlan Ellison’s *I Have No Mouth, and I Must Scream* uses rows of punch-like marks as section separators or machine-text imagery. Online readers have identified them as ITA2-derived patterns. This is a modern interpretive claim rather than a documented statement by Ellison located here; it should be presented as literary decoding folklore unless corroborated from manuscript or author testimony.

## RTTY culture

Amateur RTTY preserves a living operational culture:

- `RYRYRY` test strings
- uppercase contacts
- compact callsigns and reports
- “diddles” or idle patterns
- repeated shifts
- visual tuning of mark and space
- software emulation of mechanical conventions

`RY` is useful because R and Y produce alternating patterns across the five channels, making it a recognizable test for polarity, timing, and channel behavior.

## Mojibake

“Mojibake” normally refers to text decoded under the wrong modern character encoding. ITA2 has an older analogue: decode ITA2 as ITA1, USTTY as international ITA2, reverse the bit order, or lose a shift, and the result becomes structured gibberish.

The error is not random. It reflects a coherent but wrong table or state. Modern software artists sometimes use mojibake aesthetically; surviving five-level garble supplies an early mechanical example of the same cultural phenomenon.

## Demoscene and ASCII art

ASCII art and demoscene text graphics descend primarily from typewriter, terminal, block-graphics, PETSCII, ATASCII, ANSI, and code-page traditions. ITA2’s tiny repertoire could make simple patterns, but it is not the principal technical ancestor of demoscene graphics.

Claims directly linking ITA2 to ANSI art should therefore be classed as broad cultural genealogy rather than documented technical descent.

---

# Controversies and disputes

## 1. “Baudot code” versus ITA2

**Finding:** The widespread name is historically legitimate but technically misleading.

- Original Baudot and ITA2 tables differ.
- Murray’s code was also not frozen in one immutable form.
- ITA2 was negotiated through CCIT proposals and national systems.
- A decoder needs the exact variant.

The phrase “Baudot code” survives because Baudot established the famous five-unit lineage and because users named technologies genealogically rather than with modern codec precision.

## 2. Was Baudot’s 1874 code five-unit?

**Finding:** Not securely established from the sources directly inspected.

- The 1874 patent date is secure.
- Baudot’s five-unit system is secure by 1876–1877.
- Fischer inferred an early six-unit form and explicitly reported not having the patent.
- Later sources sometimes collapse the patent and mature system.

Until the patent’s complete technical drawings and claims are compared with the 1877 article, “five-unit code of 1874” should be qualified.

## 3. Baudot versus Mimault

**Finding:** A genuine priority dispute existed, including litigation, but the precise technical merits are inadequately represented in common English-language accounts.

The later reversal of the ruling prevents the first judgment from being treated as settled historical priority. The violent biographical aftermath is reported in later biographies, but it should not substitute for apparatus comparison.

## 4. Did Murray invent shift?

**Finding:** The claim is overbroad.

Baudot-family systems already used alternate alphabets/functions. Murray made shift-based coding practical in a new keyboard, tape, and page-printer architecture and rearranged the pairings. ITA2’s exact shifts and assignments were standardized later.

## 5. 1924, 1929, 1931, or 1932?

These dates describe different alleged or documented milestones:

- **1924:** repeated in secondary sources; no primary ITA2 standard found here.
- **1929:** CCIT recommendation and proposed alphabets.
- **1931:** decisive change toward the Murray-based final No. 2.
- **1932:** Madrid publication and formal international regulatory status.

The best concise date for the standard is **1932**, with 1929–1931 given as development.

## 6. Did ASCII replace ITA2 in 1963?

**Finding:** Only as a statement about design succession.

ASCII’s first standard appeared in 1963. Operational replacement was gradual. Telex, news, military, deaf telecommunications, and RTTY systems continued using five-unit codes for years or decades. ITU still maintains S.1.

## 7. Error correction and “delete”

**Finding:** ITA2 has a useful tape-correction convention but no error-correcting code.

All-holes LTRS can overpunch a mistaken tape row so it does not print. It does not detect errors, restore already printed text, or prevent state damage. Calling this a security deletion primitive is a modern extrapolation.

## 8. Reversibility folklore

Some accounts note that FIGS, LTRS, and SPACE have bit-symmetric patterns and that CR/LF swap under reversal, so reversed tape may remain partly intelligible or mechanically useful.

This property depends on:

- which side is called bit 1;
- whether the tape is turned over or end-for-end;
- feed-hole asymmetry;
- the exact reader;
- national code assignments.

It is an interesting engineering observation, not proof that ITA2 was comprehensively designed to be readable backward. No CCIT design minute establishing that intention was found.

## 9. “First digital code”

Baudot is often called the inventor of digital communication or the first binary character code.

That is anachronistic if taken literally. Binary signaling, combinatorial alphabets, and earlier telegraphic systems existed. A more defensible first is:

> Baudot produced the first widely adopted integrated printing-telegraph system using uniform-length binary combinations for a general alphabetic repertoire.

Even that wording depends on how “widely adopted” and “general” are defined.

## 10. Language politics

ITA2’s 26-position letter case makes the Latin alphabet appear technically natural while treating other writing systems as extensions, transliterations, or national exceptions.

This was not merely abstract bias: the installed Baudot base, European telegraph administrations, machine cost, keyboard expectations, and international interoperability made certain compromises economically powerful.

The Soviet and Czechoslovak interventions show that linguistic exclusion was recognized during design, not discovered retrospectively.

## 11. Security

ITA2’s security weaknesses are primarily operational:

- no authentication except procedural use of answerback;
- no confidentiality;
- no integrity check;
- easy substitution through bit errors;
- persistent shift-state corruption;
- traffic analysis through timing and message format;
- reusable paper tape as exposed physical data;
- possibility of misrouting or impersonation in network procedures.

Encryption machines were layered over teleprinter streams precisely because the alphabet itself provided no secrecy.

Homoglyph attacks, Unicode bidirectional-control exploits, BOM confusion, and UTF-8 overlong sequences are not ITA2 vulnerabilities. The dedicated search found no credible historical linkage. Those are later universal-text and protocol problems.

## 12. Han unification, Tibetan disputes, emoji votes, and the Consortium

These controversies are not part of ITA2’s design history.

Their remote relevance is contrast:

- ITA2 excluded most scripts structurally.
- Unicode attempts to encode them in a shared universal repertoire.
- The political question therefore shifted from “can this script fit?” to “which abstract characters, distinctions, and properties should the standard recognize?”

The requested dedicated searches found no evidence that Han unification, Tibetan encoding disputes, emoji governance, the BOM, or overlong UTF-8 sequences influenced Baudot, Murray, or CCIT’s five-unit standard. Importing them into ITA2’s controversy section as if they did would be a modern invention.

---

# Present status and surviving legacy

## Formal status

ITU’s catalogue lists **S.1 (03/1993), International Telegraph Alphabet No. 2**, as in force.

Formal status does not imply widespread new deployment. It means the international specification remains maintained and citable for surviving services and interoperability.

## Active survival

Documented survivals include:

- amateur RTTY
- FCC recognition of ITA2 as an authorized specified amateur code
- restoration and operation of historical teleprinters
- specialist radio and narrow-band direct-printing systems
- software encoders and decoders
- museum demonstrations
- limited legacy or private telex gateways

## Conceptual survival

ITA2 survives more broadly through:

- start/stop serial framing
- mark/space terminology
- CR and LF as distinct controls
- BEL
- answerback concepts
- locking shift state
- paper-tape NUL and rubout logic
- uppercase wire-service style
- the unit name *baud*
- “TTY” terminology in operating systems and accessibility history

Unix `tty` objects do not normally speak ITA2, but their name remembers the teletypewriter as the archetypal interactive terminal.

---

# Open questions

1. **The 1874 patent’s code structure.** A high-quality examination of French patent 103,898 is needed to settle whether its filed form actually used five or six information units and which shift features were present.

2. **The Mimault litigation.** The trial record, expert reports, appellate disposition, and direct patent comparison should be located in French archives.

3. **Murray’s earliest exact table.** His patents describe machinery more clearly than they establish one canonical 1901 code table. Successive Murray tables need dated comparison.

4. **Transition from Murray/Morkrum codes to USTTY.** Fischer found 1931 Teletype bulletins but not a definitive earlier changeover record. Company archives may contain engineering orders or typebox drawings.

5. **The “1924 ITA2” claim.** Its earliest printed source and path into encyclopedias remain unidentified. It may conflate an early international recommendation with the later named standard.

6. **National ITA2 variants.** A comprehensive catalogue should reproduce each administration’s figure-case assignments with dates and equipment models.

7. **Arabic, Hebrew, and Greek teleprinters.** Secondary descriptions establish that national machines and transliteration existed, but a model-by-model corpus of code charts and directional behavior remains to be assembled from manuals.

8. **Telex shutdown chronology.** National network closure dates differ and need individual telecommunications-administration sources.

9. **Ellison’s punched-code typography.** Manuscript, typesetter, or publisher records would be needed to establish authorial intent rather than retrospective reader decoding.

10. **Intentional reversal properties.** A CCIT or manufacturer document would be necessary to distinguish deliberate reversible design from a useful emergent property.

---

# Sources

## Primary standards, regulations, patents, and official records

- ITU-T Recommendation S.1 (03/1993), *International Telegraph Alphabet No. 2*:  
  https://www.itu.int/rec/T-REC-S.1-199303-I/en

- Direct S.1 PDF:  
  https://www.itu.int/rec/dologin_pub.asp?id=T-REC-S.1-199303-I%21%21PDF-E&lang=e&type=items

- ITU-T S-series catalogue:  
  https://www.itu.int/rec/T-REC-S/en

- ITU-T Recommendation S.4, *Special use of certain characters of the International Telegraph Alphabet No. 2*:  
  https://www.itu.int/itu-t/recommendations/rec.aspx?rec=2471

- CCITT Blue Book, Series S recommendations, Melbourne 1988:  
  https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.260.43.en.1004.pdf

- CCITT Green Book, Geneva 1980, including Recommendation S.18 conversions:  
  https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.258.43.en.1024.pdf

- CCITT Red Book, Málaga-Torremolinos 1984, public telegram and telex provisions:  
  https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.259.43.en.1005.pdf

- *Telegraph Regulations, Madrid 1932*:  
  https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/1.34.48.en.100.pdf

- ITU history of the Madrid 1932 conferences:  
  https://www.itu.int/en/history/Pages/RadioConferences.aspx?conf=4.41

- ITU historical figures, Émile Baudot:  
  https://www.itu.int/en/history/Pages/HistoricalFiguresInTelecommunications.aspx

- CCITT, *50 Years of Excellence, 1956–2006*:  
  https://www.itu.int/ITU-T/50/docs/ITU-T_50.pdf

- Donald Murray, US Patent 670,964, *Telegraphy* (1901):  
  https://patents.google.com/patent/US670964A/en

- Donald Murray, US Patent 1,170,556, *Keyboard Apparatus*:  
  https://patents.google.com/patent/US1170556A/en

- US amateur regulation, 47 CFR §97.309:  
  https://www.law.cornell.edu/cfr/text/47/97.309

- ITU-R Report M.2200, describing amateur NBDP/ITA2 operation:  
  https://www.itu.int/dms_pub/itu-r/opb/rep/R-REP-M.2200-2010-PDF-E.pdf

- President Lyndon B. Johnson, 11 March 1968 federal ASCII memorandum:  
  https://www.presidency.ucsb.edu/documents/memorandum-approving-the-adoption-the-federal-government-standard-code-for-information

- NBS history of Brooks Act implementation and FIPS PUBs 1–3 and 7:  
  https://www.govinfo.gov/content/pkg/GOVPUB-C13-3e65f18fd63b6ba185f07afaf1427c99/pdf/GOVPUB-C13-3e65f18fd63b6ba185f07afaf1427c99.pdf

- NIST, *A Century of Excellence in Measurements, Standards, and Technology*:  
  https://www.govinfo.gov/content/pkg/GOVPUB-C13-310bc7b3121ed82b8f13fc15a5c9e639/pdf/GOVPUB-C13-310bc7b3121ed82b8f13fc15a5c9e639.pdf

- RFC 20, Vint Cerf, *ASCII format for Network Interchange* (1969):  
  https://www.rfc-editor.org/info/rfc20/

- IANA Character Sets Registry:  
  https://www.iana.org/assignments/character-sets

## Contemporary and reconstructed histories

- Eric Fischer, *The Evolution of Character Codes, 1874–1968*:  
  https://studylib.net/doc/8163638/the-evolution-of-character-codes--1874-1968

- Alternate Fischer PDF record:  
  https://citeseerx.ist.psu.edu/document?doi=0ffa27720b572a9efdba6425b8e9a7c885a14c0d&repid=rep1&type=pdf

- Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley, 1980, ISBN 0-201-14460-3:  
  https://archive.org/details/codedcharacterse00unse

- Open Library bibliographic record for Mackenzie:  
  https://openlibrary.org/books/OL4570655M/Coded_character_sets

- 1922 *Encyclopædia Britannica*, “Telegraph”:  
  https://en.wikisource.org/wiki/1922_Encyclop%C3%A6dia_Britannica/Telegraph

- British Post Office engineering history, “Telegraphy,” 1956:  
  https://www.britishtelephones.com/cto/history1956.htm

- Original PDF of the 1956 Post Office article:  
  https://www.britishtelephones.com/cto/documents/poeej_vol49_oct1956_telegraphy.pdf

- Western Union, *Telegraph History*, bulletin 13-1:  
  https://mail.navy-radio.com/manuals/tty/wutr/13-1.pdf

- Historical analysis of printing-telegraph codes, Circuitous Root:  
  https://circuitousroot.com/artifice/telegraphy/tty/codes/

- Circuitous Root, Morkrum/Teletype and ITA2 chronology:  
  https://nadcomm.com/index153d.php?p=106

- NADCOMM, five-unit and start-stop code discussion:  
  https://nadcomm.com/index5eda.php?p=95

- RTTY historical five-unit code tables:  
  https://rtty.com/England/fiveunits.htm

## Equipment manuals and archives

- Teletype Corporation manual archive:  
  https://www.navy-radio.com/manuals-ttycorp.htm

- Teletype Corporation specifications archive:  
  https://www.navy-radio.com/tty/ttycorp-specs.htm

- AT&T and Bell System Teletype publication archive:  
  https://circuitousroot.com/artifice/telegraphy/tty-biblio/att/index.html

- *Teleprinters Made Easy*, Teletypewriters for the Deaf, 1974:  
  https://www.smecc.org/teletypewriters_made_easy.htm

- Model 28 reference material:  
  https://specsigs.com/mod28

- British GPO telegraph perforators:  
  https://www.britishtelephones.com/cto/perforator.htm

## Current and specialist use

- ARRL, digital data modes and RTTY:  
  https://www.arrl.org/digital-data-modes

- German teleprinter museum, telex history:  
  https://www.teleprinter.net/english/inhalt/telex.shtml

- Japanese Computer Museum, SC-4 kanji teleprinter:  
  https://museum.ipsj.or.jp/en/computer/device/printer/0080.html

- Japanese Computer Museum, Model 55 six-unit teleprinter:  
  https://museum.ipsj.or.jp/en/heritage/Model_55_TERETAIPU.html

## Later encoding lineage and contrast

- Unicode Consortium history:  
  https://www.unicode.org/history/

- Unicode summary narrative:  
  https://www.unicode.org/history/summary.html

- Unicode Version 1 chronology:  
  https://www.unicode.org/history/versionone.html

- Unicode publication history and *Unicode 88*:  
  https://www.unicode.org/history/publicationdates.html

- Unicode/ISO merger, Ed Hart memorandum:  
  https://www.unicode.org/history/hartmemo.html

- Participant discussion of Unicode’s origins:  
  https://www.unicode.org/mail-arch/unicode-ml/y2002-m02/0110.html

- Rob Pike, *UTF-8 history*:  
  https://www.cl.cam.ac.uk/~mgk25/ucs/utf-8-history.txt

- RFC 3629, *UTF-8, a transformation format of ISO 10646*:  
  https://www.rfc-editor.org/info/rfc3629/

- Unicode Technical Report #36, historical security considerations:  
  https://www.unicode.org/reports/tr36/

- Unicode Technical Standard #39, current confusables and security mechanisms:  
  https://www.unicode.org/reports/tr39/

## Secondary indexes consulted but not used as substitutes for standards

- Baudot code overview and variant index:  
  https://en.wikipedia.org/wiki/Baudot_code

- Telegraph-code overview:  
  https://en.wikipedia.org/wiki/Telegraph_code

- Teleprinter overview:  
  https://en.wikipedia.org/wiki/Teleprinter

- Telex overview:  
  https://en.wikipedia.org/wiki/Telex

- Émile Baudot biographical index:  
  https://en.wikipedia.org/wiki/%C3%89mile_Baudot

- Chinese telegraph code index:  
  https://en.wikipedia.org/wiki/Chinese_telegraph_code

- Practical ITA2/USTTY comparison table:  
  https://madrona.ca/e/stds.html

- Unicode mailing-list recollection concerning five-level telex tape:  
  https://www.unicode.org/mail-arch/unicode-ml/y2004-m01/0133.html
