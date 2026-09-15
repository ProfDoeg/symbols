# Morse code and the telegraph codes: Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| Name | International Morse code; historically preceded by Morse–Vail or American Morse, and Gerke’s Hamburg alphabet |
| Current standard | **Recommendation ITU-R M.1677-1, “International Morse code”** |
| First standardized international form | **1865**, Regulations annexed to the International Telegraph Convention, Paris |
| Current edition | **2009**, approved 3 October 2009 |
| Bit width | **None.** Morse is a variable-length, timed signal code, not a fixed-width binary character code |
| Signal alphabet | Mark and space, interpreted through five significant durations: 1-unit dot, 3-unit dash, 1-unit intra-character space, 3-unit inter-character space, 7-unit inter-word space |
| Repertoire | 26 unaccented Latin letters, É, digits 0–9, selected punctuation, arithmetic signs and procedural signals |
| Case | No distinction between uppercase and lowercase |
| Direction | Sequential in transmission; adaptations may be transcribed left-to-right or right-to-left according to local writing practice |
| Current status | **In force**, but specialized: amateur radio, navigation-aid identifiers, accessibility, signaling, training and ceremonial/emergency uses |
| Immediate ancestors | Morse’s numerical dictionary scheme; Morse–Vail alphabetic landline code; Gerke’s 1848 Hamburg revision |
| Important successors and neighbors | Cooke–Wheatstone needle alphabets; Baudot ITA1; Murray code; CCITT International Telegraph Alphabet No. 2; teleprinters, ASCII and later computer encodings |

### Evidence labels used below

- **[STD]** documented standard, convention, patent, regulation or contemporary official text.
- **[CONT]** contemporary publication or artifact not itself a standard.
- **[REC]** participant recollection or retrospective oral/personal account.
- **[SCH]** scholarly historical reconstruction based on documentary evidence.
- **[DISPUTED]** significant disagreement over fact, attribution or interpretation.
- **[FOLKLORE]** widely repeated story with weak or absent contemporary evidence.
- **[MODERN]** later analogy or interpretation, useful but anachronistic if projected backward.

---

## The code in detail

### It is not a bit code

**[STD]** ITU-R M.1677-1 defines Morse through signal duration:

1. A dot lasts one time unit.
2. A dash lasts three units.
3. The silence between elements of one character lasts one unit.
4. The silence between characters lasts three units.
5. The silence between words lasts seven units.

Thus Morse does not have a meaningful fixed “bit width.” A character occupies between one and six mark elements in the normal written repertoire, or eight dots for the error signal, plus spaces necessary to delimit it.

A computer may store `.` and `-` as bits, characters, tree paths or packed integers, but none of those representations is the Morse standard. For example, a program can encode dot as `0` and dash as `1`, yet it must separately store the element count or a terminator; otherwise `.` could mean E, the beginning of A, I, S, H, and many longer sequences.

The transmitted channel is more accurately described as binary-valued but duration-coded:

- key down, carrier on, lamp on or current flowing: **mark**;
- key up, carrier off, lamp off or no current: **space**.

Time supplies the framing.

### International Morse table

The following is the repertoire printed in ITU-R M.1677-1. The typography here uses `.` for a dot and `-` for a dash.

#### Letters

| Character | Morse | Character | Morse | Character | Morse |
|---|---:|---|---:|---|---:|
| A | `.-` | J | `.---` | S | `...` |
| B | `-...` | K | `-.-` | T | `-` |
| C | `-.-.` | L | `.-..` | U | `..-` |
| D | `-..` | M | `--` | V | `...-` |
| E | `.` | N | `-.` | W | `.--` |
| F | `..-.` | O | `---` | X | `-..-` |
| G | `--.` | P | `.--.` | Y | `-.--` |
| H | `....` | Q | `--.-` | Z | `--..` |
| I | `..` | R | `.-.` | É | `..-..` |

**[STD]** There is no separate lowercase. `A` and `a` are the same signal. É is the sole accented alphabetic character in the current international table.

#### Figures

| Figure | Morse | Figure | Morse |
|---|---:|---|---:|
| 1 | `.----` | 6 | `-....` |
| 2 | `..---` | 7 | `--...` |
| 3 | `...--` | 8 | `---..` |
| 4 | `....-` | 9 | `----.` |
| 5 | `.....` | 0 | `-----` |

The digit series has a deliberately regular structure: starting at 1, dots replace leading dashes until 5; from 6 through 0, dashes replace dots.

#### Punctuation and signs

| Meaning | Printed symbol | Morse |
|---|---:|---:|
| Full stop / period | `.` | `.-.-.-` |
| Comma | `,` | `--..--` |
| Colon or division sign | `:` | `---...` |
| Question mark; request for repetition | `?` | `..--..` |
| Apostrophe | `'` | `.----.` |
| Hyphen, dash or subtraction | `-` | `-....-` |
| Fraction bar or division sign | `/` | `-..-.` |
| Left parenthesis | `(` | `-.--.` |
| Right parenthesis | `)` | `-.--.-` |
| Quotation marks | `"` | `.-..-.` |
| Double hyphen | conventionally `=` | `-...-` |
| Cross or addition sign | `+` | `.-.-.` |
| Multiplication sign | `×` | `-..-` |
| Commercial at | `@` | `.--.-.` |

**[STD]** The multiplication sign deliberately shares X’s signal. Percentage and per-mille signs have no independent code: the recommendation prescribes sequences such as `0/0` and `0/00`.

**[STD]** The present table does **not** standardize the commonly published Morse codes for `!`, `;`, `_`, `&` or `$`. Those are national, amateur or software extensions. Modern internet charts often silently merge them with the ITU repertoire.

#### Procedural signals

| Function | Continuous signal | Conventional letters often used to name it |
|---|---:|---|
| Understood | `...-.` | SN or VE |
| Error | `........` | eight dots |
| Invitation to transmit | `-.-` | K |
| Wait | `.-...` | AS |
| End of work | `...-.-` | SK or VA |
| Starting signal | `-.-.-` | KA or CT |
| End of telegram / cross | `.-.-.` | AR |
| Section separator / double hyphen | `-...-` | BT |

A prosign is normally sent **without ordinary letter spacing**. Thus `<AR>` is not A followed by R; it is the uninterrupted sequence `.-.-.`. The letter names are mnemonics for the joined patterns.

### Space, newline, deletion and case

- **Space:** **[STD]** no character code. A seven-dot-duration silence separates words.
- **Newline:** no general textual newline code exists in M.1677-1. Operational practice uses separators such as `<BT>` between sections or paragraphs. Some national and amateur conventions use other prosigns, but these are not a universal Morse equivalent of ASCII LF.
- **Deletion/backspace:** no random-access deletion character exists. **[STD]** the error signal—eight dots—is sent after a sending mistake, followed by retransmission according to operating procedure.
- **Case:** absent. Capitalization is irrecoverably lost unless spelled or signaled by an agreed convention.
- **Blank line:** not inherently representable. A long silence has operational meaning but does not count blank text lines.
- **Tabulation, font, emphasis and layout:** outside the code.
- **Combining marks and arbitrary Unicode characters:** not expressible without spelling, transliteration, a codebook or a separately agreed extension.

### Collating order

Morse defines no collating or sorting order. Alphabetical order comes from the source language, not from signal values.

A binary-tree presentation is pedagogically useful—dot to one side, dash to the other—but the standard does not say that E sorts before T, or that a traversal of the tree is a collation sequence. Treating dot as zero and dash as one creates a modern implementation order, not a historical Morse order.

### Variable length and compression

**[MODERN]** Morse is frequently described as an early form of lossless compression because frequent English letters such as E and T receive short signals while rarer letters often receive longer ones. This is a legitimate information-theoretic comparison.

It requires three qualifications:

1. **[CONT/SCH]** The early code’s assignments were shaped by estimated letter frequency and operating cost, but its designers did not possess Shannon’s twentieth-century theory.
2. Morse is not a prefix code if the spaces are removed: E (`.`) is a prefix of I (`..`), S (`...`) and H (`....`).
3. Its cost is not merely the number of dots and dashes. Dashes take three times as long, and character separators also consume time. A formally optimized code under that cost model would not necessarily be the historical Morse table.

**[DISPUTED]** Calling it “the first compression code” is too strong. Abbreviations, shorthand, numerical dictionary codes, commercial codebooks and earlier variable-length telegraph schemes predate or overlap it. A defensible formulation is: Morse is one of the earliest widely deployed variable-length character codes whose lengths broadly reflect symbol frequency.

### Error and synchronization behavior

Morse is not self-correcting and has no checksum.

- A wrong-length mark can turn one valid letter into another.
- A missing intra-character gap can join marks.
- A gap stretched from one to three units can split a character.
- A gap stretched from three to seven units can create a false word boundary.
- Noise can insert a dot or subdivide a dash.

Recovery is nevertheless often local:

- A valid three-unit character gap gives the next character a fresh boundary.
- A seven-unit gap gives an even stronger word resynchronization point.
- The eight-dot error signal and requests for repetition provide procedural recovery.
- Natural-language redundancy, call signs, repeated groups and experienced rhythmic listening let humans correct errors that the code itself cannot.

A reader entering midstream must wait for a recognizable character or word gap. There is no byte boundary, start bit or length prefix. If timing is badly distorted, formal recovery may be impossible.

### Worked example: `MORSE`

#### International Morse

| Character | Morse | Mark-time units | With internal spaces |
|---|---:|---:|---|
| M | `--` | 6 mark units | `---·---` in a unit-grid notation |
| O | `---` | 9 | `---·---·---` |
| R | `.-.` | 5 | `=·===·=` |
| S | `...` | 3 | `=·=·=` |
| E | `.` | 1 | `=` |

Using `=` for one unit of signal and `·` for one unit of silence:

```text
M       letter gap   O           letter gap   R       letter gap   S       letter gap   E
===·=== ···          ===·===·=== ···          =·===·= ···          =·=·=   ···          =
```

The conventional written form is:

```text
-- --- .-. ... .
```

#### ASCII and UTF-8 comparison

Because the word contains only ASCII characters, UTF-8 uses the same bytes.

| Character | ASCII/UTF-8 hexadecimal | Binary |
|---|---:|---:|
| M | `4D` | `01001101` |
| O | `4F` | `01001111` |
| R | `52` | `01010010` |
| S | `53` | `01010011` |
| E | `45` | `01000101` |

ASCII is fixed at seven significant bits; commonly stored in eight-bit octets. UTF-8 is byte-oriented and self-synchronizing. Morse has neither byte values nor a fixed field width.

#### ITA2 comparison

In the commonly tabulated CCITT International Telegraph Alphabet No. 2 bit-number convention:

| Character | ITA2 value | Five-bit group |
|---|---:|---:|
| M | 28 | `11100` |
| O | 24 | `11000` |
| R | 10 | `01010` |
| S | 5 | `00101` |
| E | 1 | `00001` |

ITA2 depends on the current **letters** or **figures** shift state. Bit transmission and printed bit order differ among documentation conventions, so a raw group must always be accompanied by its bit-numbering and transmission-order convention.

### Worked example: `SOS @ 2026`

```text
SOS         ... --- ...
word gap    seven units of silence
@           .--.-.
word gap
2           ..---
0           -----
2           ..---
6           -....
```

ASCII/UTF-8 bytes:

```text
53 4F 53 20 40 20 32 30 32 36
```

The contrast is fundamental: ASCII encodes spaces as byte `20`; Morse encodes them as duration. The Morse `@` character was added in 2004 as `.--.-.`, conventionally understood as A and C run together.

---

## Origins

### Before electrical telegraph character codes

**[SCH]** Long-distance signaling systems already separated a message into a repertoire of conventional states. Chappe’s optical semaphore, naval flag systems and numbered codebooks were conceptual predecessors, although their physical channels and symbol organizations differed from Morse.

Numerical codebooks were especially important. A sender transmitted a number; the receiver looked it up to recover a word or phrase. This reduced the repertoire that the apparatus had to signal but imposed dictionary lookup and prevented free spelling of unknown words.

### 1832–1837: Morse’s concept

**[REC/SCH]** Samuel Finley Breese Morse later associated his conception of an electromagnetic recording telegraph with discussions aboard the packet ship *Sully* while returning from Europe in 1832. The story rests substantially on later recollection and corroborating statements gathered during patent disputes; it is not a contemporary engineering notebook proving a single instant of invention.

**[STD/CONT]** Morse’s earliest practical scheme used numbered signals interpreted through a dictionary. His apparatus recorded current interruptions on moving paper. Leonard Gale contributed electrical knowledge, drawing on Joseph Henry’s work with electromagnets and long circuits.

**[DISPUTED]** Morse was not the sole inventor of electrical telegraphy. Pavel Schilling, Gauss and Weber, Carl August von Steinheil, Cooke and Wheatstone, and others constructed distinct systems. Priority depends on whether “telegraph” means conceptual proposal, experimental line, practical railway installation, recording apparatus, single-wire circuit or commercially scalable network.

### Cooke–Wheatstone needle code, 1837

**[STD/CONT]** William Fothergill Cooke and Charles Wheatstone patented their joint needle telegraph in 1837. In the five-needle display, two needles deflected toward a printed letter on a diamond-shaped board.

The common five-needle face displayed only twenty letters; museum examples omit C, J, Q, U, X and Z or supply them through conventions. Numerals required additional arrangements. The system’s advantages were direct visual reading and little code memorization. Its disadvantages were multiple wires, cost and limited repertoire.

The London and Birmingham Railway demonstration between Euston and Camden in 1837 is well documented. Later one- and two-needle instruments reduced wire count but required memorized sequences.

### Morse and Vail, 1837–1838

**[STD/CONT]** Alfred Vail joined Morse and Leonard Gale in 1837, bringing finance, skilled mechanical work and access to the Speedwell Iron Works. Library of Congress materials show that the dot-and-dash letter system appeared after this collaboration began. By January 1838, the project had moved from dictionary-indexed words toward directly coding letters.

### Who invented the alphabet?

This is the central credit dispute.

- **[CONT]** Vail’s 1845 *The American Electro Magnetic Telegraph* publicly attributed the alphabet to Morse.
- **[STD/CONT]** Morse’s name stood on the principal patents and became the commercial system’s name.
- **[SCH]** Vail unquestionably redesigned and improved the register, keying and mechanical apparatus, and he participated directly in developing the alphabetic system.
- **[REC/DISPUTED]** Late nineteenth-century advocates, especially Franklin Leonard Pope and members of the Vail family, argued that Alfred Vail devised the practical alphabet and was denied credit.
- **[SCH/DISPUTED]** The Smithsonian has sometimes stated the strong Vail attribution directly; the Library of Congress uses more cautious collaborative wording.
- **Finding:** surviving evidence supports joint development and a major Vail role, but does not securely allocate every letter assignment to a single individual. Vail’s own contemporary attribution to Morse is evidence against an uncomplicated “Vail alone” claim, though it may also reflect contractual and patent politics.

### The printer’s type-case story

**[FOLKLORE/DISPUTED]** A famous story says Vail visited a Morristown newspaper office, counted the pieces of movable type in its cases and assigned shorter signals to letters with more sorts.

The story is plausible because type founders and printers stocked letters according to expected frequency, and the resulting code does favor common letters. But the evidentiary chain is weak:

- no contemporary Vail notebook yet located in the consulted archives states that this experiment determined the code;
- modern accounts often repeat one another without identifying an early primary source;
- assignments are only approximately frequency-ordered when actual timing cost is considered.

Accordingly, the type-case episode should be reported as durable folklore, not established fact. The broader claim that frequency influenced the code is better supported than this particular anecdote.

### 24 May 1844

**[CONT]** Morse sent “WHAT HATH GOD WROUGHT” from Washington to Alfred Vail in Baltimore over the federally financed demonstration line. Annie Ellsworth selected the biblical phrase from Numbers 23:23. The surviving message artifact and correspondence establish the event.

The code in use was what later became **American Morse**, **railroad Morse** or the **Morse landline code**, not the final International Morse table.

### American Morse structure

American Morse was more rhythmically complicated than International Morse. Besides ordinary dots and dashes it used:

- internal long spaces within certain letters;
- more than one dash length;
- sequences whose identity depended strongly on landline timing.

This suited embossed paper tape and, later, operators listening to a sounder’s paired clicks. It was less suitable for international interoperability and noisy radio.

The two systems agree on some letters but differ on many others. Printed transcriptions of American Morse require typography for long gaps and long dashes; tables that reduce everything to ordinary `.` and `-` can erase essential distinctions. This is why the current International table above should not be retroactively called the exact code of the 1844 message.

### Operators abandon the paper record

**[CONT/SCH]** Morse’s register was designed to emboss or mark moving paper. Operators learned to recognize the armature’s clicks and transcribe directly by ear. This human reinterpretation made the apparatus faster and simpler: the meaningful output ceased to be the paper trace and became rhythm heard at the sounder.

This was not merely a cultural flourish. It changed the effective channel from visual record to trained auditory performance.

### Gerke’s Hamburg alphabet, 1848

**[CONT/SCH]** Friedrich Clemens Gerke, associated with the Hamburg–Cuxhaven telegraph, revised the American alphabet for European operation. His system eliminated internal character spaces and multiple dash lengths, leaving ordinary dots and dashes with regular spacing.

Gerke’s line began operation in 1848; his manual *Der praktische Telegraphist* appeared in 1851. Dates such as 1848, 1849 and 1851 in modern accounts sometimes refer respectively to practical preparation, publication/display and institutional adoption rather than three incompatible invention dates.

Gerke added or accommodated German characters and substantially reassigned the alphabet. International Morse is therefore not simply the 1844 American table with a new name.

### 1851: German-Austrian adoption

**[CONT/SCH]** The Deutsch-Österreichischer Telegraphenverein adopted a revised Morse alphabet in 1851. This is the meaningful origin of the often-used phrase “International Morse of 1851,” although the worldwide intergovernmental adoption came later.

Some International assignments were further altered after Gerke; accounts identify Steinheil-derived patterns among the changes. Only a small subset of modern letter codes is identical through every early stage.

### 1865: international adoption

**[STD]** Twenty states met in Paris and signed the first International Telegraph Convention on 17 May 1865, establishing the International Telegraph Union. Regulations annexed to the convention prescribed Morse code and Morse apparatus for international service.

The exact 1865 table was a standardized European/continental descendant of Gerke’s revision. It was not the American landline code still used in North America.

**[STD]** This is one of the earliest examples of an international organization standardizing not only service rules and tariffs but a particular communications alphabet and apparatus family.

### Rival systems

Morse’s success was not technically inevitable.

- **Cooke–Wheatstone:** easily read display, but expensive multiwire construction.
- **Breguet and Foy–Breguet:** reused visual conventions familiar from French optical telegraphy.
- **Hughes printing telegraph:** direct printed output and keyboard operation.
- **Wheatstone automatic system:** punched tape and high-speed transmission.
- **House, Bain and other printing/recording systems:** competed commercially and in patent litigation.
- **Baudot:** fixed five-unit combinations and multiplex operation.
- **Murray:** keyboard-to-tape workflow and assignments designed to reduce punching/mechanical wear.
- **Teleprinter systems:** eventually removed the need for a skilled listener to translate rhythm.

Morse won where low line cost, simple apparatus, manual flexibility and trained operators mattered. Printing codes won where automatic preparation, switching, storage and unattended reproduction mattered.

---

## From Morse to fixed-unit telegraph codes

### Baudot’s five-unit code

**[STD/CONT]** Émile Baudot patented his rapid printing telegraph in France in 1874, patent no. 103,898. Each character used five equal signal units, permitting 32 combinations. His five-key “piano” keyboard was scanned by a synchronous distributor, and several operators could be time-multiplexed on one line.

Baudot’s original assignment later became known as **International Telegraph Alphabet No. 1**, or ITA1. It should not be confused with the later five-bit code casually called “Baudot” in computing and radio-teletype literature.

### Donald Murray

**[CONT/REC]** Donald Murray developed a keyboard perforator, paper-tape transmitter and printing system around 1899–1901. His code was also five units but substantially rearranged.

Because a typist first punched tape, Murray did not need Baudot’s hand-chording mnemonic arrangement. He gave common letters combinations requiring fewer holes, reducing mechanical punching and tape wear. Murray introduced or consolidated format controls such as carriage return and line feed and used shift states for larger repertoires.

**[REC/DISPUTED]** Murray maintained that he arrived at the five-unit principle independently through logic, especially W. Stanley Jevons, while acknowledging Baudot’s earlier achievement. The physical and assignment differences lend some support, but later “Baudot–Murray” terminology obscures which contribution is being described.

### ITA2

**[STD]** In 1932 the CCITT standardized International Telegraph Alphabet No. 2, derived primarily from Murray and Western Union practice. Its 32 five-bit combinations included:

- 26 letters in the letters state;
- a figures shift and letters shift;
- digits and punctuation in the alternate state;
- carriage return;
- line feed;
- space;
- null/blank and national-use positions, depending on edition.

ITA2 introduced a vulnerability absent from stateless International Morse: a corrupted shift character could garble every following character until the next shift restored state. Conversely, its start/stop teleprinter framing and fixed character width suited automation far better than Morse.

The historical path is therefore not simply “Morse became ASCII.” It is:

```text
manual variable-duration codes
        ↓
fixed-unit printing codes with shift states
        ↓
teleprinter controls and paper-tape conventions
        ↓
six-, seven- and eight-bit computer character codes
```

ASCII’s separate CR and LF controls inherit teleprinter mechanics much more directly from Murray/ITA2 practice than from Morse.

---

## Prosigns, abbreviations and operating language

Morse working developed a layer above the character alphabet:

- call signs;
- Q codes such as QTH and QRM;
- `DE` for “from”;
- `R` for received;
- procedural signals such as `<AS>`, `<BT>`, `<AR>` and `<SK>`;
- commercial code words representing entire phrases;
- abbreviated amateur-radio conversational forms such as `TNX`, `73` and `CUL`.

These are not all “characters.” They mix code points, uninterrupted prosigns, abbreviations and higher-level protocols. A transcription that prints `<SK>` as two ordinary letters loses the fact that it was keyed continuously.

---

## SOS

### Adoption

**[STD]** The 1906 International Radiotelegraph Conference in Berlin selected the continuous distress signal:

```text
...---...
```

The implementing convention took effect in 1908. It was transmitted as one uninterrupted sequence, not three conventionally spaced letters.

The signal was chosen for distinctiveness and simplicity. Its symmetrical succession of three short, three long and three short marks was recognizable even without language.

### What it does not mean

**[FOLKLORE]** “Save Our Souls,” “Save Our Ship” and similar expansions are backronyms. The 1906 convention specifies the signal, not an English phrase. The fact that an international conference selected it also weighs against an English-only origin.

### CQD

Marconi operators previously used `CQD`, developed from the general call `CQ` plus D for distress. “Come Quick, Danger” is itself a mnemonic/backronym rather than the formal derivation.

### Titanic

**[CONT/REC]** Titanic’s operators sent both CQD and SOS in April 1912. Survivor Harold Bride’s contemporary newspaper account supplies the famous recollection that he suggested trying the “new call” because it might be their last chance.

**[FOLKLORE]** Titanic was not the first ship to send SOS. Ships including *Arapahoe* used it earlier. Claims of a surviving audio recording of Titanic’s transmission are also false: radio operators made written logs, but no contemporary audio recording is known.

---

## Adoption and decline

### Landline telegraphy

American Morse became the working language of United States and Canadian commercial and railroad telegraphy. Operators formed occupational communities with distinctive rhythm, abbreviations, fists—individual sending styles—and oral lore.

International Morse dominated cross-border European traffic and later radio. American Morse survived on North American wires well into the twentieth century because installed practice and trained labor can preserve a code after a technically simpler rival exists.

### Radio

Spark transmitters naturally produced on-off radio-frequency energy and made Morse an easy migration from wire to wireless. Radiotelegraphy added the need for standardized call signs, distress procedures, frequency discipline and watches.

Morse was central to:

- maritime communications;
- early military and diplomatic radio;
- aviation;
- news and commercial wireless;
- amateur radio;
- clandestine and resistance communication;
- navigation beacons.

### Maritime watch and 1999

**[STD]** The Global Maritime Distress and Safety System became fully effective on **1 February 1999**. Satellite and automated terrestrial alerting replaced the mandatory global regime centered on manual radiotelegraph watches.

A careful formulation is required:

- correct: 1999 ended the historic mandatory Morse radiotelegraph watch for SOLAS shipping under the replaced regime;
- incorrect: “Morse ceased to be used anywhere at sea in 1999”;
- misleading: “radio at sea ended in 1999.”

Ships, navies, amateurs, historical stations and specialized services could and did continue Morse operation.

### Amateur radio

Morse survived unusually well because it works with:

- very narrow bandwidth;
- low transmitter power;
- simple equipment;
- signals too weak for comfortable voice reception;
- operators who value its rhythm and traditions.

Many administrations once required Morse proficiency for access to amateur frequencies below 30 MHz. After changes to international regulations, national requirements disappeared. **[STD]** The United States ended its remaining amateur Morse examination requirement on 23 February 2007. This ended compulsory testing, not amateur CW operation.

### Aviation

**[STD]** VOR, ILS, NDB and related navigation aids identify themselves with two- or three-letter International Morse groups. ICAO documentation still specifies Morse identifiers, although voice or automatic cockpit decoding may accompany them and satellite navigation has reduced reliance on some terrestrial aids.

### The 2004 `@`

**[STD]** ITU-R M.1677-0, approved in May 2004, included the commercial-at sign `@` as:

```text
.--.-.
```

The sequence resembles A (`.-`) and C (`-.-.`) run together. The addition responded to the practical need to send e-mail addresses. M.1677-1 retained it in 2009.

**Finding:** this is widely described as Morse’s first new character in many decades, but claims specifying an exact number of years vary because standards had revised punctuation and operational tables at different dates.

### Present status

International Morse remains an in-force recommendation but is no longer a general-purpose text interchange encoding. Its surviving strengths are physical simplicity, human recognizability, low bandwidth and the ability to cross media: electric current, carrier, tone, whistle, light, touch or movement.

---

## The other scripts

International Morse’s repertoire is Eurocentric and extremely small. It cannot directly represent most human writing.

### Latin extensions

National tables added codes for characters such as Ä, Å, Á, Ç, CH, Ñ, Ö, Ü and others. These extensions were not perfectly uniform. Some reused a prosign or punctuation pattern, making interpretation depend on language and context.

The current ITU table’s inclusion of É alone does not make it adequate for French, German, Polish, Czech, Turkish, Vietnamese or most other Latin-script orthographies.

### Greek

Greek Morse generally assigns International patterns by phonetic or transliteration correspondence and supplies mappings for letters without simple Latin equivalents. It is a separate repertoire agreement, not something intrinsically discoverable from International Morse.

Case and polytonic accent distinctions are normally lost unless separately spelled or encoded.

### Cyrillic

Russian and related Morse alphabets map many Cyrillic letters to corresponding or transliterated International signals and add patterns for the remaining letters. Language-specific Cyrillic letters require national extensions.

The method works because Morse patterns are abstract rhythmic groups, but an identical signal can mean different written characters depending on the declared alphabet.

### Hebrew

Hebrew Morse maps its consonantal letters onto Morse groups. Ordinary Hebrew directionality affects transcription and display, not the temporal direction of the signal stream. Vowel points, cantillation and full typographic distinctions are generally not represented.

### Arabic and Persian

Arabic Morse systems assign patterns to letters rather than encoding contextual glyph forms. That avoids having separate codes for isolated, initial, medial and final shapes: shaping is reconstructed when written.

However:

- short vowels commonly omitted in ordinary Arabic remain absent;
- extended Persian/Urdu letters need additional assignments;
- bidirectional layout and numeral handling are outside the Morse signal layer;
- no international Morse mechanism specifies Arabic shaping or bidirectional ordering.

### Indic scripts

Morse extensions can encode transliterated letters or locally agreed alphabetic/syllabic units, but International Morse itself has no model for:

- independent versus dependent vowels;
- combining vowel signs;
- virama/halant;
- conjunct consonants;
- canonical equivalence;
- reordering and shaping.

Those are precisely the kinds of representation issues later computer encodings and rendering systems had to address.

### Japanese: Wabun

Wabun code represents Japanese kana with Morse-like sequences. It is not merely International Morse applied to romanization: most groups have kana values independent of their International Latin meanings.

Procedural signals mark transitions between Wabun and International/Latin working. Kanji are not directly represented by ordinary Wabun groups; messages may use kana readings or another codebook.

### Korean: SKATS

The Standard Korean Alphabet Transliteration System assigns Morse-compatible Latin-letter signals to Hangul jamo. Its mappings are operational rather than straightforward phonetic Romanization. Hangul syllable-block composition must be reconstructed at the writing stage.

### Chinese

Morse cannot assign short rhythmic groups to tens of thousands of Han characters without an enormous, impractical repertoire. Chinese telegraphy therefore used numeric codebooks.

**[CONT/SCH]** After the Great Northern Telegraph Company linked Shanghai and Hong Kong in 1871, Hans Schjellerup, Septime Auguste Viguier and Chinese collaborators developed codebooks assigning four-digit numbers to thousands of characters. Viguier’s *電報新書* (*Diànbào xīnshū*, “New Book for the Telegraph”) appeared in the early 1870s.

A clerk converted Chinese characters to four-digit groups; the digits traveled through Morse or another telegraph channel; a receiving clerk looked them up. The system:

- enabled Han-character messages over digit-capable networks;
- imposed clerical labor and codebook dependence;
- limited the repertoire;
- charged a high signaling cost because each character became four transmitted digits;
- created opportunities for additive numerical encryption;
- later diverged between mainland and Taiwan codebooks.

This was a layered encoding: Chinese character → four-digit code → telegraph signals.

### Emoji

International Morse has no emoji repertoire and no general escape mechanism. An emoji can only be:

- named in words;
- transliterated descriptively;
- assigned an ad hoc code;
- sent through a higher-level numeric scheme such as its Unicode code point.

Claims that patterns such as `...---...` are an “SOS emoji” conflate a signal with pictographic encoding.

---

## People and institutions

### Samuel F. B. Morse (1791–1872)

Painter, promoter and principal patent holder of the American recording telegraph. He proposed the early numerical/dictionary method, organized collaborators and political support, and became the system’s public name.

### Alfred Vail (1807–1859)

Mechanical collaborator, financier and operator. He made major improvements to the apparatus and participated centrally in the creation of the practical alphabetic code. The degree to which he alone designed the table remains disputed.

### Leonard Gale (1800–1883)

New York University chemist who helped Morse understand electrical circuits and apply existing electromagnetic research over distance.

### Joseph Henry (1797–1878)

Experimental physicist whose electromagnetic work materially enabled long-distance telegraph circuits. Later patent testimony and Morse–Vail efforts to minimize Henry’s published credit produced a documented controversy.

### Cooke and Wheatstone

William Fothergill Cooke (1806–1879) supplied entrepreneurial and practical railway impetus; Charles Wheatstone (1802–1875) supplied substantial scientific and instrument-design work. Their 1837 joint patent covered a practical needle system.

### Friedrich Clemens Gerke (1801–1888)

Hamburg telegraphist, writer and systematizer. His removal of American Morse’s irregular internal spaces and dash lengths created the foundation of International Morse.

### Émile Baudot (1845–1903)

French telegraph engineer who patented a five-unit printing and multiplex system. The unit “baud” later commemorated him, though modern ITA2 is not his original code table.

### Donald Murray (1865–1945)

New Zealand-born journalist and telegraph engineer. Developed automatic punched-tape and printing arrangements whose code assignments became the major ancestor of ITA2.

### Institutions

- **United States Congress:** financed the Washington–Baltimore experimental line.
- **Railroad and telegraph companies:** created the operational labor culture that sustained American Morse.
- **Deutsch-Österreichischer Telegraphenverein:** adopted the Gerke-derived continental alphabet in 1851.
- **International Telegraph Union / ITU:** standardized international telegraph and radio procedure from 1865 onward.
- **CCITT:** standardized ITA1/ITA2 and later international telecommunication alphabets.
- **Marconi companies:** developed early commercial wireless practice, including CQD.
- **IMO:** administered the transition to GMDSS.
- **ICAO:** preserves Morse identifiers in navigation standards.
- **National amateur-radio administrations and organizations:** preserved CW practice after commercial decline.

---

## Culture

### “Plain text” before electronic text

Morse represents an early ideal of abstracting language from its visible form. A letter could survive a change from paper indentation to click, tone or flash because its identity lay in a temporal pattern.

But it was never culturally neutral plain text:

- its default repertoire privileged a small Latin alphabet;
- capitalization and typography disappeared;
- trained operators supplied segmentation and error correction;
- non-Latin writers bore the cost of transliteration or codebooks;
- commercial brevity was shaped by per-word tariffs.

### The operator’s “fist”

Operators recognized one another by timing, pressure and rhythm. A “fist” was analogous to handwriting or an accent. This complicates the claim that Morse is a purely discrete code: the standardized pattern carried a continuous human performance layer.

### Acoustic icon

SOS escaped its technical origin to become an almost universal sound emblem for distress. It appears in music, film, lighting, jewelry and graphic design. Its cultural meaning often survives when the audience cannot decode any other Morse character.

### Literature and popular stories

The 1844 biblical message has repeatedly been treated as a prophetic announcement of instant global communication. Titanic narratives made SOS synonymous with technological disaster, even though Titanic neither originated the signal nor left an audio recording.

Edgar Allan Poe-style cryptographic culture, scouting manuals, wartime adventure fiction and prison-escape narratives commonly use tapped Morse. Many fictional examples ignore timing, produce invalid groups or assume any tapping system is Morse.

### Tapping and accessibility

Morse can be adapted to a switch, blink, breath, touch or other binary gesture. This made it useful in disability interfaces and emergency communication. Such adaptations may alter timing or group delimiters; they are Morse-derived protocols rather than necessarily literal ITU radio procedure.

### ASCII art and the demoscene

ASCII art and the demoscene belong to later fixed-width computer character culture, not Morse history proper. The family resemblance is cultural:

- making expressive artifacts from a tiny repertoire;
- treating technical constraints as aesthetic material;
- valuing compactness and operator skill.

Calling Morse “ASCII art in sound” would be a modern metaphor, not a historical connection.

---

## Controversies and disputes

### “Morse invented Morse code”

**Assessment:** oversimplified.

Morse originated and promoted the system, but the alphabet emerged during collaboration with Vail and was later transformed by Gerke. “Morse code” is a conventional eponym for a lineage, not proof of sole authorship.

### “Vail invented the whole code and Morse stole it”

**Assessment:** possible elements of under-credit, but not established in that absolute form.

Late Vail advocacy, mechanical evidence and institutional reconstructions support a much larger Vail contribution than popular histories once allowed. Against sole authorship stand Vail’s own 1845 attribution and the collaborative documentary chronology. Contractual dependence and patent strategy complicate both sides.

### The newspaper type-case anecdote

**Assessment:** folklore not securely documented.

It provides an elegant explanation of frequency assignment, which may explain its persistence. The consulted primary catalogues and early text did not produce a contemporary statement proving it.

### “First data compression”

**Assessment:** useful modern analogy, disputed as priority.

Morse economizes expected duration, but earlier shorthand and codebooks compressed information; the table is not strictly optimized; and its separators are essential. It is safer to call it an early mass-deployed variable-length code.

### “Morse is binary”

**Assessment:** true only at the physical-state level.

The line can be on or off, but duration distinguishes dot, dash and three kinds of spacing. A dot/dash transcription already suppresses important timing. As an abstract symbol code it is at least a two-mark alphabet plus structured separators; as a waveform it is binary-valued and time-coded.

### “International Morse was invented in 1851”

**Assessment:** date compression.

1851 marks German-Austrian adoption of the Gerke-derived alphabet. 1865 marks formal international adoption in Paris. Gerke’s operational revision began around 1848.

### “SOS means Save Our Souls”

**Assessment:** folklore/backronym.

The convention specifies a distinctive signal. The English phrases appear as later mnemonic explanations.

### “Titanic sent the first SOS”

**Assessment:** false.

Earlier documented uses exist. Titanic sent CQD and SOS.

### “Commercial Morse ended in 1999”

**Assessment:** misleading.

The GMDSS transition ended the mandatory global maritime radiotelegraph-watch regime. It did not prohibit Morse, erase amateur activity or end every commercial, military and navigation use.

### International versus national alphabets

Morse standardization improved interoperability but never settled a universal repertoire. National extensions frequently collided with prosigns or one another. A group may mean a letter, punctuation mark or procedure depending on context.

This is a miniature version of later encoding politics: which distinctions are treated as characters, which are relegated to higher-level protocol, and whose writing receives direct representation.

### Security

Morse itself offers no cryptographic secrecy and very limited integrity protection.

- Anyone who can receive the signal can decode it.
- Operator style can identify a sender.
- Traffic analysis exposes call signs, timing and message volume.
- A jammer can obliterate or falsify marks.
- Spoofed navigation-aid identifiers can mislead if not cross-checked.
- Homographs arise when the same pattern is assigned differently in national alphabets or when prosigns collide with punctuation.

Encryption historically operated above Morse: codebooks, transposition, one-time pads and machine ciphers transformed plaintext into letter or digit groups that Morse merely carried.

---

## Dedicated contested-material pass: findings

Searches combining Morse and telegraph history with *dispute*, *credit*, *controversy*, *first*, *SOS*, *compression*, *security* and related terms yielded the following material issues:

1. **Morse/Vail authorship** — genuine documentary dispute; strong evidence for collaboration, insufficient evidence for either simple sole-inventor story.
2. **Joseph Henry’s credit** — documented patent-era suppression/minimization concerns in Morse–Vail correspondence and Smithsonian scholarship.
3. **Type-case frequency story** — widely repeated but primary evidence not recovered; classify as folklore.
4. **First compression** — a modern information-theory analogy, not a documented nineteenth-century claim.
5. **Gerke’s date** — apparent discrepancies usually reflect revision, publication and adoption milestones.
6. **SOS expansion** — backronym.
7. **First SOS/Titanic** — false folklore.
8. **1999 “end of Morse”** — exaggeration of the GMDSS transition.
9. **2004 `@` as first change in X years** — basic addition is documented; exact “first in N years” formulations depend on what counts as a table revision.
10. **Chinese telegraph-code priority** — Schjellerup, Viguier, Chinese collaborators and successive editions require joint and staged credit; “Viguier alone invented Chinese telegraphy” is inadequate.
11. **Morse as ancestor of every later encoding** — defensible as broad technological genealogy, not direct table descent. ASCII descends structurally more through fixed-unit printing telegraph and teleprinter practice than through Morse assignments.
12. **Claims of authentic Titanic audio** — no contemporary recording evidence; known sound examples are recreations.

No substantive Morse-specific Han-unification, BOM, overlong UTF-8 or Unicode emoji-ballot controversy was found because those belong to later encodings. Importing them into a Morse dossier would manufacture relevance. Morse’s genuine parallel controversy is repertoire inequality and the reliance of Chinese, Japanese, Korean and other users on transliteration, local Morse alphabets or codebooks.

---

## Open questions

1. What is the earliest traceable printed source for the Morristown type-case story?
2. Can surviving Vail notebooks establish responsibility for particular alphabet assignments rather than general collaboration?
3. Which precise Gerke table was first used operationally in 1848, and how did it differ from his 1851 printed manual?
4. What exact table accompanied the 1851 Deutsch-Österreichischer Telegraphenverein decision?
5. Which changes separate that table from the 1865 Paris regulation?
6. When did “Save Our Souls” and “Save Our Ship” first appear in print as SOS explanations? The phrases are clearly later than the signal, but bibliography varies.
7. Which ship made the first operational distress use of `...---...` under the international rule? Claims for *Slavonia* and *Arapahoe* depend on definitions and contemporary log survival.
8. How consistently did operators observe nominal 1:3:7 timing rather than regional rhythm?
9. How many national Morse alphabets received formal governmental standardization, as opposed to customary operator use?
10. Which current navigation systems still require audible Morse identification, rather than transmitting it only for compatibility?
11. How should historical Morse speed be compared fairly with fixed-unit codes when operator comprehension, error rate and procedural overhead are included?
12. Can a complete critical edition align the 1838 manuscript alphabets, 1844 tape, 1845 Vail table, Gerke editions, 1851 association table and 1865 regulation without silently normalizing their typography?

---

## Sources

### Standards, conventions and official records

- ITU-R, *Recommendation M.1677-1: International Morse code*, October 2009:  
  https://www.itu.int/rec/R-REC-M.1677-1-200910-I

- ITU-R, M.1677-1 English PDF:  
  https://www.itu.int/dms_pubrec/itu-r/rec/m/r-rec-m.1677-1-200910-i%21%21pdf-e.pdf

- ITU-R, *Recommendation M.1677-0*, May 2004:  
  https://www.itu.int/rec/R-REC-M.1677-0-200405-S/en

- ITU study-group draft for the Morse recommendation, document 8/8, 21 January 2004:  
  https://www.itu.int/md/R03-SG08-C-0008

- ITU, *The 1865 International Telegraph Conference*:  
  https://www.itu.int/en/history/Pages/ITUBorn1865.aspx

- ITU, conference record and 1865 convention links:  
  https://www.itu.int/en/history/Pages/PlenipotentiaryConferences.aspx?conf=4.1

- ITU, *Pre-1865 International Telegraph Agreements*:  
  https://www.itu.int/en/history/Pages/Pre1865Agreements.aspx

- ITU, *Historical Highlights: ITU and Standardization*:  
  https://www.itu.int/en/history/Pages/FocusOnStandardization.aspx

- ITU, *Paris, 1865: The Birth of the Union*:  
  https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/12.36.72.en.100.pdf

- ITU, *International Radiotelegraph Convention of Berlin, 1906*:  
  https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.37.57.en.100.pdf

- ITU, 1906 Berlin conference history page:  
  https://www.itu.int/en/history/Pages/RadioConferences.aspx?conf=4.36

- International Maritime Organization, GMDSS history:  
  https://www.imo.org/en/ourwork/safety/pages/introduction-history.aspx

- International Maritime Organization, radiocommunications:  
  https://www.imo.org/en/ourwork/safety/pages/radiocommunications-default.aspx

- IMO, *GMDSS and SAR 1999*:  
  https://wwwcdn.imo.org/localresources/en/OurWork/Safety/Documents/GMDSSandSAR1999.pdf

- ICAO, *EUR Frequency Management Manual*, 2025 edition:  
  https://www.icao.int/sites/default/files/EURNAT/Documents/EUR%20and%20Nat%20Docs/EUR%20Documents/EUR%20Documents/011%20-%20EUR%20Frequency%20Management%20Manual/EUR-Doc-011-Edition-2025.pdf

- FAA, notice concerning ICAO phonetic alphabet/Morse tables, 2023:  
  https://www.faa.gov/AIR_TRAFFIC/FLIGHT_INFO/AERONAV/safety_alerts/media/CS_23-06_CN_ICAO_Phonetic_Alphabet_Morse_Code.pdf

- FCC, discussion of elimination of amateur Morse testing:  
  https://docs.fcc.gov/public/attachments/FCC-08-59A1.pdf

- FCC public notice concerning international Morse requirements:  
  https://docs.fcc.gov/public/attachments/DA-01-2168A1.pdf

- ARRL, “Morse code requirement ends Friday, February 23,” 24 January 2007:  
  https://www.arrl.org/w1awbulletinsissue?code=ARLB005&issue=2007-01-24

### Manuscripts, patents, contemporary books and archival collections

- Library of Congress, *Samuel F. B. Morse Papers*, timeline 1791–1839:  
  https://www.loc.gov/collections/samuel-morse-papers/articles-and-essays/timeline/1791-1839/

- Library of Congress, 1835–1838 bound volume containing an early letter alphabet:  
  https://www.loc.gov/resource/mmorse.012001/?st=slideshow

- Library of Congress, *Invention of the Telegraph*:  
  https://www.loc.gov/collections/samuel-morse-papers/articles-and-essays/invention-of-the-telegraph/

- Library of Congress, Morse papers bound volume, June–October 1844:  
  https://www.loc.gov/item/mmorse000018

- Alfred Vail, *The American Electro Magnetic Telegraph*, 1845, Google Books record:  
  https://books.google.com/books/about/The_American_electro_magnetic_telegraph.html?id=LTRkAAAAcAAJ

- Alfred Vail, 1845 description, Wellcome Collection:  
  https://wellcomecollection.org/works/mqvm5sts

- Smithsonian, Vail Telegraph Collection finding aid:  
  https://www.si.edu/object/archives/sova-sia-faru7055?page=1

- New Jersey Historical Society, Alfred Vail papers guide:  
  https://jerseyhistory.org/guide-to-the-alfred-vail-1807-1859-inventor-papers1826-1918mg-50/

- U.S. Supreme Court, *O’Reilly v. Morse*, 56 U.S. 62 (1854):  
  https://tile.loc.gov/storage-services/service/ll/usrep/usrep056/usrep056062/usrep056062.pdf

- Royal Danish Library, Viguier, *電報新書 / Diànbào xīnshū*:  
  https://permalink.kb.dk/permalink/2006/manus/340/eng/

### Museum and institutional histories

- Smithsonian Institution Archives, “A Forgotten History: Alfred Vail and Samuel Morse”:  
  https://siarchives.si.edu/blog/forgotten-history-alfred-vail-and-samuel-morse

- Smithsonian Institution Archives, Morse–Vail–Henry credit controversy:  
  https://siarchives.si.edu/collections/siris_sic_12495

- Smithsonian, Western Union Telegraph Company records:  
  https://sova.si.edu/record/nmah.ac.0205

- Smithsonian, Wheatstone five-needle telegraph:  
  https://www.si.edu/object/wheatstone-5-needle-telegraph-unit%3Anmah_708625

- Science Museum Group Collection, Cooke and Wheatstone five-needle telegraph:  
  https://collection.sciencemuseumgroup.org.uk/objects/co33374/cooke-and-wheatstone-5-needle-telegraph-1837

- Science Museum Group Journal, “A tale of two telegraphs”:  
  https://journal.sciencemuseum.ac.uk/article/cooke-and-wheatstones/

- Museum Foundation Post and Telecommunication, five-needle instrument:  
  https://onlinesammlung.museumsstiftung.de/detail/collection/e5d39e03-f461-47f9-8761-68c43250eb39

- Google Arts & Culture / Museum for Communication Berlin, Gerke and German telegraphy:  
  https://artsandculture.google.com/story/qQWBl-0PURQMIw

### Scholarly and technical reconstructions

- Anton A. Huurdeman, *The Worldwide History of Telecommunications*, Wiley, 2003:  
  https://www.nzdr.ru/data/media/biblio/kolxoz/Cs/CsPop/Huurdeman%20A.A.%20The%20worldwide%20history%20of%20telecommunications%20%28Wiley%2C%202003%29%28ISBN%200471205052%29%28656s%29_CsPop_.pdf

- Eric Fischer, “The Evolution of Character Codes, 1874–1968”:  
  https://studylib.net/doc/8163638/the-evolution-of-character-codes--1874-1968

- University of Auckland, Donald Murray historical display and collected recollections:  
  https://www.cs.auckland.ac.nz/historydisplays/FifthFloor/Murray/MurraySpielLR.pdf

- David M. MacMillan, “Some Printing Telegraph Codes as Products of their Technologies”:  
  https://www.circuitousroot.com/artifice/telegraphy/tty/codes/

- Edward E. Kleinschmidt, *Printing Telegraphy… A New Era Begins*:  
  https://www.gutenberg.org/files/53481/53481-h/53481-h.htm

- Journal of Modern Chinese History, “The grammar of the telegraph in the Late Qing”:  
  https://www.tandfonline.com/doi/full/10.1080/17535654.2018.1540191

- NSA, “The Chinese Telegraph Code”:  
  https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/history-today-articles/02%202018/15FEB2018%20The%20Chinese%20Telegraph%20Code.pdf?ver=kLlbXqxl_NfOgfcP3dj3rw%3D%3D

- NSA, *Cryptologic Quarterly* material on the Viguier code:  
  https://media.defense.gov/2021/Jul/13/2002762049/-1/-1/0/CRYPTOLOGIC-QUARTERLY-2017-03.PDF

### Cultural and contested-material references

- German Federal Agency for Civic Education, “Come Quick, Danger!” and SOS cultural memory:  
  https://www.bpb.de/themen/zeit-kulturgeschichte/sound-des-jahrhunderts/209587/come-quick-danger/

- Snopes, historical review of Titanic and SOS claims:  
  https://www.snopes.com/fact-check/same-old-slip/

- Wordorigins, documented origin of SOS expansions:  
  https://www.wordorigins.org/big-list-entries/sos

- Art of Coding, demoscene and text-art heritage:  
  https://demoscene-the-art-of-coding.net/

- Norwegian inventory of intangible cultural heritage, demoscene history:  
  https://www.immateriellkulturarv.no/en/bidrag/the-demoscene-a-digital-community-across-borders-before-the-internet/

- Morse/telegraph historical article used to locate early-code references:  
  https://www.morsecode.nl/morse.pdf

- International Morse operational mirror used to cross-check accessible standard text:  
  https://www.johndcook.com/ITU_Morse_Code.pdf
