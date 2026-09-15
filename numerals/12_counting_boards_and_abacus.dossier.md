# Counting boards and the abacus (Salamis, Rome, China, Japan, Russia): Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| Name | Counting board; Greek ἄβαξ (*abax*); Latin *abacus*; Chinese 算盤/算盘 (*suànpán*, “calculating tray”); Japanese 算盤/そろばん (*soroban*); Russian счёты (*schëty/schoty*, “accounts, reckoning”) |
| Base | Normally decimal positional; Roman instruments add duodecimal fractional registers; medieval fiscal boards may be mixed-radix; purported Aztec devices are described as vigesimal, but their pre-Columbian existence is disputed |
| Type | Instrumental positional notation. Individual beads/counters are additive within a place; places are multiplicative powers of a base. A 1:4 or 2:5 frame is bi-quinary-coded decimal, not a written numeral script |
| Signs | No alphabet of written digits is intrinsic. The “signs” are occupied places: counters on lines/spaces, or beads touching a reckoning beam. In compact notation this dossier uses `H:a | E:b`, where `H` is the number of five-beads engaged and `E` the number of one-beads engaged |
| Zero | An empty place. It is operationally indispensable but normally has no bead or counter of its own |
| Period | Pre-Classical antecedents uncertain; Salamis board, fourth–third century BCE; Roman hand abaci, Imperial period; medieval European boards, at least the early Middle Ages through the seventeenth century; Chinese framed abacus securely widespread in the Ming period; Japanese soroban from the late sixteenth century; Russian schoty in recognizable modern form by the eighteenth century; all survive in education or specialist practice |
| Core regions | Mediterranean; Roman Empire; medieval and early-modern Europe; China; Japan; Korea; Russia and neighboring regions |
| Classification | A family of material calculating notations, not one genealogically demonstrated invention |

### Evidentiary labels used

- **[A: documented artefact]** A surviving object with catalogue or archaeological documentation.
- **[T: documented text/image]** A surviving text, illustration, inscription, or contemporary report.
- **[R: scholarly reconstruction]** A conclusion inferred from arrangement, later descriptions, experimental operation, or comparative evidence.
- **[Tradition]** A historical claim maintained by practitioners or later national histories but incompletely documented.
- **[D: disputed]** Serious alternatives exist or the evidence is insufficient.
- **[L: legend]** A story repeated without adequate primary evidence.
- **[M: modern invention/reconstruction]** A recent device, representation, or interpretation presented as old, or a pedagogical reconstruction of an old one.

The labels concern the status of a claim, not its cultural worth.

---

## 1. The system in detail

### 1.1 What kind of “numeral system” is an abacus?

An abacus is a temporary, material positional notation. A bead has no fixed numerical value apart from its location and state. The same lower bead may mean 1, 10, 100, 0.1, a coin, or a measure, depending on which rod is declared the unit rod.

The essential grammar is:

\[
N=\sum_i d_i b^i
\]

where \(b\) is normally 10 and each \(d_i\) is represented by counters or beads. On a bi-quinary frame:

\[
d_i=5h_i+e_i,
\]

with \(h_i\) engaged five-beads and \(e_i\) engaged one-beads.

Thus the instrument is:

- positional between rods, lines, or spaces;
- additive within each place;
- multiplicative because moving one place changes value by the base;
- sometimes mixed-radix where money, weights, or fractions require it.

Calling this merely “additive” misses its positional structure. Calling the beads “digits” is convenient but potentially misleading: a digit is the entire state of a column, not one bead.

### 1.2 Direction and ordering

On the Chinese and Japanese frames, conventionally:

- units are assigned to a chosen rod;
- tens, hundreds, and higher powers run leftward;
- tenths, hundredths, and lower powers run rightward;
- beads count only when moved toward the central beam.

The unit rod is conventional rather than physically necessary. Modern soroban usually mark every third rod with a dot to assist grouping and decimal placement.

On the Russian schoty:

- the wires are horizontal;
- beads are moved from the operator’s right toward the left to be counted;
- place values rise upward;
- the middle two beads are often colored differently as visual separators, not as five-valued beads.

On a European lined board:

- one convention gives lines the values 1, 10, 100, 1,000…;
- spaces between lines then carry five times the lower line: 5, 50, 500…;
- five counters on a line are exchanged for one in the space above; two in a space are exchanged for one on the next line.

Different boards reverse or rotate the physical orientation. The numerical principle, not “left” or “up,” is fundamental.

### 1.3 No intrinsic written glyphs

There are no Unicode “abacus digits.” Unicode contains:

- Chinese number words such as 一, 二, 三, 十, 百, 千, 萬/万;
- Japanese uses the same characters, alongside Hindu-Arabic digits;
- Roman numerals such as Ⅰ–Ⅻ and ordinary letters `I V X L C D M`;
- rod-numeral characters `𝍠`–`𝍨` and `𝍩`–`𝍱` in the Counting Rod Numerals block.

These belong to written notations associated with, or parallel to, calculation. They are not the bead states themselves.

For clarity, this dossier uses:

- `H` = an upper or heaven bead of value five;
- `E` = a lower or earth bead of value one;
- `●` = an engaged bead/counter;
- `○` = disengaged or empty;
- `|` = the reckoning beam;
- a blank column = zero.

For example, decimal 7 on a 1:4 soroban is `H:1 | E:2`.

### 1.4 Worked table, 1–20

This table describes the modern 1:4 soroban. “Tens; units” are separate rods.

| Number | Soroban state | Chinese/Japanese written forms |
|---:|---|---|
| 1 | `0:1` | 一 |
| 2 | `0:2` | 二 |
| 3 | `0:3` | 三 |
| 4 | `0:4` | 四 |
| 5 | `1:0` | 五 |
| 6 | `1:1` | 六 |
| 7 | `1:2` | 七 |
| 8 | `1:3` | 八 |
| 9 | `1:4` | 九 |
| 10 | `1 ; 0` | 十 |
| 11 | `1 ; 0:1` | 十一 |
| 12 | `1 ; 0:2` | 十二 |
| 13 | `1 ; 0:3` | 十三 |
| 14 | `1 ; 0:4` | 十四 |
| 15 | `1 ; 1:0` | 十五 |
| 16 | `1 ; 1:1` | 十六 |
| 17 | `1 ; 1:2` | 十七 |
| 18 | `1 ; 1:3` | 十八 |
| 19 | `1 ; 1:4` | 十九 |
| 20 | `2 ; 0` | 二十 |

Here `0:4` means no five-bead and four one-beads engaged. A bare `1`, in a place to the left of the semicolon, means digit 1 on the tens rod.

The older Chinese 2:5 suanpan has redundant states:

- canonical 0–9 can be represented exactly as on a 1:4 instrument;
- the extra lower bead permits 5 as `0:5`;
- a second upper bead permits 10 as `2:0`;
- certain historical multiplication and division routines retain intermediate values above nine before carrying.

This redundancy is functional, not evidence that ordinary suanpan notation has base 16.

### 1.5 Tens, hundreds, thousands, and powers

| Value | Bead-state by rods | Chinese | Japanese reading |
|---:|---|---|---|
| 10 | `1 0` | 十 | 十, *jū* |
| 20 | `2 0` | 二十 | 二十, *nijū* |
| 30 | `3 0` | 三十 | 三十 |
| 40 | `4 0` | 四十 | 四十 |
| 50 | `5 0` | 五十 | 五十 |
| 60 | `6 0` | 六十 | 六十 |
| 70 | `7 0` | 七十 | 七十 |
| 80 | `8 0` | 八十 | 八十 |
| 90 | `9 0` | 九十 | 九十 |
| 100 | `1 0 0` | 百 | 百, *hyaku* |
| 1,000 | `1 0 0 0` | 千 | 千, *sen* |
| 10,000 | `1 0 0 0 0` | 萬/万 | 万, *man* |
| 100,000,000 | nine rods, 1 followed by eight empty places | 億/亿 | 億, *oku* |
| \(10^{12}\) | thirteen rods | 兆 | 兆, *chō* |

A frame has no mathematically fixed maximum. An \(r\)-rod decimal abacus represents \(0\) through \(10^r-1\) canonically. A 23-rod soroban can therefore represent up to:

`99,999,999,999,999,999,999,999`

if all rods are used as integer places. Larger values can be obtained by declaring a scaled unit, joining frames, or recording partial results. The limit is physical bookkeeping, not a terminus in the numeral language.

Chinese large-number vocabulary has changed historically, and successive terms have not always represented the same powers in every period. Modern common assignments include 萬 \(10^4\), 億 \(10^8\), 兆 \(10^{12}\), 京 \(10^{16}\), 垓 \(10^{20}\), and further named powers. Those names belong to language and writing, not to a special limit imposed by the suanpan.

### 1.6 Famous numbers

| Number | Canonical rod sequence | Written parallel |
|---:|---|---|
| 365 | `3 | 6 | 5` = `0:3 ; 1:1 ; 1:0` | 三百六十五 |
| 876 | `8 | 7 | 6` = `1:3 ; 1:2 ; 1:1` | 八百七十六 |
| 1,202 | `1 | 2 | blank | 2` | 千二百二 / 一千二百零二 |
| 1,946 | `1 | 9 | 4 | 6` | 千九百四十六 |
| 46,802 | `4 | 6 | 8 | blank | 2` | 四万六千八百二 / 四萬六千八百零二 |
| 2026 | `2 | blank | 2 | 6` | 二千二十六 |
| 3.1416 | choosing the first rod as units: `3 | 1 | 4 | 1 | 6` | 3.1416; 三点一四一六 |

The 46,802 example is used in the MacTutor description of the Chinese abacus. Its zero tens-place is not represented by a zero bead: that rod remains empty. [MacTutor’s illustrated explanation](https://mathshistory.st-andrews.ac.uk/HistTopics/Chinese_numerals/)

### 1.7 Zero

**[Documented operation / reconstruction]** An empty column functions as zero and distinguishes 12 from 102. This is a genuine positional zero-function.

**[Important qualification]** It is still correct that the classical Greek or Roman hand abacus has no dedicated zero token. It is incorrect to infer that its operators lacked the concept of “none,” could not preserve an empty place, or could not calculate through a zero result.

**[Comparative finding]** The operational empty place of a board is not automatically the historical ancestor of the written zero symbol. The transition from an unmarked spatial vacancy to a durable written mark requires separate evidence.

### 1.8 Fractions and mixed units

Any decimal frame can represent fixed-point fractions by declaring a unit rod. The rods to its right become tenths, hundredths, and so forth. No decimal point need be inscribed on the frame.

The Roman bronze hand abacus is more specialized:

- seven principal columns represent powers from units through one million;
- each has four lower buttons worth one unit of its place and one upper button worth five;
- an additional column represents *unciae*, twelfths of an *as*;
- the surviving instruments include small fractional slots probably representing subdivisions of an *uncia*.

The traditional interpretation gives:

- *uncia*: \(1/12\);
- *semuncia*: \(1/24\);
- *sicilicus*: \(1/48\);
- *sextula*: \(1/72\);
- *dimidia sextula*: \(1/144\);
- *scriptulum*: \(1/288\).

**[D]** The main ounce column is secure from the layout and marks; the exact values and readings of every tiny right-hand slot have generated disagreement. Claims that every mark is unambiguously decoded overstate the evidence.

Medieval fiscal boards were often mixed-radix. English money required:

- 12 pence = 1 shilling;
- 20 shillings = £1;
- 20 pounds = one score of pounds in the Exchequer arrangement.

Robert Recorde’s counter arithmetic also handles pounds, shillings, and pence by allocating separate compartments rather than pretending that the units are decimal.

### 1.9 Ligatures and abbreviations

Bead systems have no ligatures in the typographic sense. They have:

- compression by exchange, such as five lower counters becoming one five-counter;
- carrying, such as ten units becoming one ten;
- empty positions;
- place labels or abbreviated unit signs.

The Salamis slab bears acrophonic Greek monetary signs at its edges. Roman pocket abaci engrave shortened or archaic-looking value marks between grooves. These labels identify columns; they are not the movable numeral itself.

---

## 2. Origins: dated and placed

### 2.1 Prehistory: what is and is not an abacus antecedent

#### Tally bones

The Lebombo bone and Ishango bone are important in the history of marking quantities, but neither is a counting board or bead frame.

- **Lebombo bone:** **[A, interpretation disputed]** A notched baboon fibula from Border Cave in southern Africa, often dated to roughly 42,000 years ago and interpreted as a tally. Whether its notches record counting, calendrical activity, ornament, or repeated manufacture is not demonstrable from the object alone.
- **Ishango bone:** **[A, interpretations disputed]** A notched bone from Ishango in the Democratic Republic of Congo, generally placed around the Late Stone Age, often approximately 20,000 years ago. Arithmetic, prime-number, lunar-calendar, and doubling interpretations are modern hypotheses.

**Finding:** Neither artefact supplies evidence for positional counter calculation, place-value columns, or transmission to the Mediterranean abacus.

#### Mesopotamian tokens and tablets

- **[A]** Clay tokens, envelopes, numerical tablets, and proto-cuneiform records from Uruk document material accounting and evolving written metrology.
- **[R/D]** Denise Schmandt-Besserat argued that tokens enclosed in clay envelopes were direct precursors of impressed signs and writing. Her work made the model famous from the 1970s onward.
- **[D]** Later specialists accept the relevance of token accounting but dispute a simple one-to-one evolutionary chain for all signs and all writing.
- **[Absence of evidence]** Claims of a Mesopotamian dust abacus thousands of years before Salamis are plausible analogies, not supported by a securely identified surviving board.

Babylonian scribes used sophisticated sexagesimal place-value written notation. That is a distinct system and should not be casually treated as the notation of the later Mediterranean board.

### 2.2 Egypt

Herodotus, writing in the fifth century BCE, contrasts Greek and Egyptian directionality in calculation, saying Egyptians move their counters in the opposite direction to Greeks.

- **[T]** This is evidence that movable-counter calculation was familiar in the Classical period.
- **[D]** Herodotus does not describe the board’s exact layout.
- **Narmer macehead:** **[A]** Its large numerical records, conventionally dated around 3100 BCE, are evidence for Egyptian written enumeration. They are not evidence for an abacus.
- **Rhind Mathematical Papyrus:** **[T]** Copied by Ahmes around 1650 BCE from older material, it documents Egyptian arithmetic and unit-fraction methods. It does not establish the use of a bead frame.

### 2.3 The Salamis tablet

**[A]** The Salamis tablet is the earliest securely surviving object generally interpreted as a counting board.

- Find: Salamis, Greece, in 1846.
- Date: commonly circa 300 BCE; the Computer History Museum catalogue gives approximately the fourth century BCE.
- Material: white marble.
- Size: approximately 149–150 × 75 × 4.5 cm.
- Present location: Epigraphical Museum, Athens.
- Inventory: **EM 11515**.
- Layout: parallel lines, a transverse division, and Greek acrophonic numeral or monetary inscriptions around three edges.
- Initial interpretation: game board.
- Later interpretation: calculation/accounting board, with loose pebbles placed on and between lines.
- Modern publication history: early drawings and nineteenth-century descriptions preceded the standard comparison with Greek and Roman counter reckoning.

The official-credit catalogue entry identifies it as Epigraphical Museum EM 11515 and dates it to the fourth century BCE. [Computer History Museum object record](https://www.computerhistory.org/revolution/artifact/1/128)

**[R]** The operational reading assigns powers or money units to lines and five-times values to intervening spaces. No counters were found fixed to the slab, so demonstrations are reconstructions.

**[D]** “Oldest abacus” is safe only if *abacus* includes counting boards. It is not a framed bead abacus. Its commercial ownership is a reasonable inference, not an inscribed fact.

### 2.4 Greek representations and vocabulary

Greek *psēphoi* were pebbles or counters; *psēphizein* could mean to count or calculate. An engraved gem, painted vessels, and literary references show people reckoning with counters.

The Darius Painter’s large Apulian vase, conventionally called the Darius Vase and dated to the late fourth century BCE, depicts a seated figure with a board or tablet associated with tribute accounting.

- **[T]** It supports the cultural presence of visible financial calculation.
- **[D]** The exact mechanics represented cannot be reconstructed from the image alone.

### 2.5 Rome: board, *calculi*, and hand abacus

Roman calculation used loose *calculi*, literally small stones, on a board, as well as portable grooved instruments.

#### Surviving hand abaci

**[A] BnF bronze.1925**

- Institution: Bibliothèque nationale de France, Département des Monnaies, médailles et antiques.
- Inventory: **bronze.1925**.
- Material: bronze.
- Size: 12.5 × 8 cm.
- Reported findspot: Autun, according to Nicolas-Claude Fabri de Peiresc.
- Layout: nine long parallel grooves and eight shorter ones, with riveted sliding buttons and engraved column signs.
- Documentary history: drawn in Peiresc’s collection, BnF Estampes, Rés. AA.53/54, fol. 102; mentioned in two letters of 1634.
- Provenance: Peiresc; cabinet of the Abbey of Sainte-Geneviève; seized for the national collection on 27 February 1797.

The catalogue notes five other known objects of this general type, including Rome, London, and Aosta, while two seventeenth-century published examples are lost. [BnF catalogue record](https://medaillesetantiques.bnf.fr/ws/catalogue/app/collection/record/3184)

**[A] Museo Nazionale Romano inv. 65054**

- Imperial Roman period.
- Bronze.
- 11.5 × 7.2 cm.
- Rome, Museo Nazionale Romano.
- Inventory **65054**.
- Museum interpretation: a portable instrument used by traders and *nummularii*, money professionals. [Museo Galileo object page](https://exhibits.museogalileo.it/archimedes/object/PortableCounterAbacus.html)

**[A] Aosta example**

A bronze hand abacus was excavated from a late first-century CE grave at Aosta. It is especially valuable because its archaeological context is better than that of pieces that first entered antiquarian collections in the seventeenth century.

**[A but incomplete catalogue access] British Museum OA.2419**

The BnF catalogue cross-references a similar British Museum piece as **OA.2419**. The museum link was not consistently retrievable during this research, so no unsupported dimensions or findspot are supplied here.

#### The “Roman abacus in the Louvre”

**[L/misidentification]** Popular histories sometimes place the famous bronze Roman hand abacus “in the Louvre.”

The catalogued object most commonly reproduced is at the **BnF Cabinet des Médailles**, not the Louvre. Searches of the Louvre collection identify architectural *abaci*—the slabs atop capitals—but not this calculating instrument. The confusion probably arose because:

- both institutions are in Paris;
- *abacus* also names an architectural part;
- older English captions loosely said “Paris museum” or “Cabinet des Médailles.”

This is a useful example of a museum-location anecdote propagated by repetition rather than an ancient tradition.

#### Authenticity and dating caution

**[D]** The BnF catalogue makes an unusually important observation: all the classically styled loose-provenance “Roman” bronze abaci became known in the seventeenth century. The contextual Aosta find strengthens the ancient attribution of the type, but it does not automatically authenticate every antiquarian specimen. The surviving corpus is tiny—approximately three or four originals under conservative counts, or six if lost and contested records are included.

### 2.6 Late antiquity and early medieval Europe

After the western Roman state fragmented, calculation on boards did not simply vanish. Written Roman numerals, finger reckoning, memorized tables, loose counters, and boards coexisted.

Boethius (c. 480–524/525) transmitted Greek arithmetic theory in Latin. Later sources made him an emblem of arithmetic, but the famous printed image of “Boethius the algorist” is anachronistic.

Finger reckoning remained important. Bede’s *De temporum ratione* (725) opens with a system of finger numbers used in calendrical computation. The word *digit* descends from Latin *digitus*, “finger,” preserving the bodily origin of elementary enumeration.

### 2.7 Gerbert’s apices

Gerbert of Aurillac, later Pope Sylvester II (c. 946–1003), is associated with a columnar abacus employing counters marked with nine numeral signs, the *apices*.

- **[T]** Gerbertian and post-Gerbertian abacus texts exist, including work associated with Bernelinus.
- **[R]** The counters allowed a single marked token to replace several identical loose counters in a column.
- **[D]** How directly Gerbert obtained the numeral forms from al-Andalus, Catalonia, or Arabic teaching is debated.
- **[L]** Later legend turned Gerbert’s mathematical and astronomical learning into sorcery and dealings with a demon. These stories are evidence of his posthumous reputation, not of his methods.
- **[Important distinction]** His system used digits 1–9 on counters but no necessary zero counter: an empty column supplied the zero-place.

This is neither yet ordinary written Hindu-Arabic algorism nor merely the classical unmarked-counter board. It is a hybrid material notation.

### 2.8 China: counting rods before the framed abacus

Chinese calculation with rods is much earlier and far better documented than the framed suanpan.

- **[A/T]** Archaeological rods and textual references exist from the Han era and later.
- **[T/R]** The *Nine Chapters on the Mathematical Art*, compiled from material conventionally dated around the first century BCE–first century CE, gives procedures widely reconstructed as operations with counting rods.
- **[R]** Rods represented decimal place-value numbers; alternating horizontal and vertical forms reduced ambiguity between adjacent places.
- **[R]** An empty position served as zero in manipulation.
- **[T]** Thirteenth-century mathematical printing supplies explicit diagrams resembling operational rod arrays.

A recent study emphasizes that the evidence consists chiefly of procedural texts and later rod diagrams: the *Nine Chapters* rarely says exactly how rods were physically arranged. [Karine Chemla and related scholarship summarized in *Science in Context*](https://www.cambridge.org/core/journals/science-in-context/article/interplay-between-textual-procedures-and-material-operations-from-the-viewpoint-of-chinese-mathematical-texts/7E654BC8863452F26F2E0C43892699F4)

#### Was there a rigid Chinese “counting board”?

**[D]** Needham and others reconstructed a gridded board on which rods were manipulated. Martzloff stresses that ancient and medieval Chinese sources do not securely describe such a physical board, and no ancient wooden example has been identified. Texts instead mention rods spread on tables, beds, mats, paper, or the ground.

The defensible formulation is “rod-calculation surface,” not necessarily a purpose-built checkerboard. The Italian *Storia della Scienza* discussion expressly notes that the board commonly reconstructed by Libbrecht lacks direct original-text evidence. [Treccani discussion](https://www.treccani.it/enciclopedia/la-scienza-in-cina-dai-qin-han-ai-tang-la-matematica_%28Storia-della-Scienza%29/)

#### From rods to suanpan

**[R/D]** Operational continuity makes the rod calculus a strong indigenous predecessor of the suanpan: both use decimal places, empty zero-positions, carrying, and table-based algorithms. But no text documents a single inventor or a precise act of conversion from loose rods into beads on rods.

Claims that the “Chinese abacus is documented in the second century BCE” often conflate:

- generic calculation;
- the term *suan*;
- rods;
- a bead instrument mentioned in Xu Yue’s *Shushu jiyi*;
- the later 2:5 framed suanpan.

Xu Yue (c. 160–c. 220) is associated with the *Shushu jiyi* (“Notes on Traditions of Arithmetic Methods”), which mentions several devices. **[D]** The received text’s history and the device’s exact form do not justify identifying it straightforwardly with the Ming suanpan.

MacTutor gives a cautious popular chronology: rods dominate first; the abacus appears around the fourteenth century. [MacTutor](https://mathshistory.st-andrews.ac.uk/HistTopics/Chinese_numerals/)

Martzloff’s more conservative conclusion is that the framed abacus entered common Chinese use only in the second half of the sixteenth century. [Martzloff, *A History of Chinese Mathematics*](https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Martzloff%20-%20A%20history%20of%20chinese%20mathematics.pdf)

### 2.9 Secure Ming evidence

By the late Ming, the evidence becomes abundant.

- **[T]** Cheng Dawei (程大位, 1533–1606), *Suanfa tongzong* (算法統宗, “General Source of Computational Methods”), 1592: a comprehensive commercial-arithmetic and abacus manual containing hundreds of problems.
- **[T]** Cheng published the abridged *Suanfa zuanyao* in 1598.
- **[T]** Abacus rhymes encode carry, borrow, multiplication, and division routines.
- **[T]** Ming images and surviving objects establish framed bead instruments beyond reasonable doubt.

The familiar 2-heaven/5-earth structure offers enough temporary capacity to hold 0–15 in a column, useful in older algorithms. MacTutor explains that this does not change the final decimal normalization. [MacTutor](https://mathshistory.st-andrews.ac.uk/HistTopics/Chinese_numerals/)

### 2.10 Japan

Chinese-style framed abaci reached Japan by the late Muromachi or Momoyama period, probably through trade and contact with Ming China.

- **[Tradition with material support]** Transmission is generally assigned to the sixteenth century.
- **[A]** The Shibei Shigekatsu Hairyo soroban, with a provenance dated 1591, is reported as the oldest extant Japanese example.
- **[T]** Mōri Shigeyoshi’s *Warizan-sho* (割算書, 1622) is regarded by the Japanese abacus federation as the oldest surviving Japanese printed book centered on abacus division.
- **[T]** Yoshida Mitsuyoshi’s enormously influential *Jinkōki* (塵劫記, 1627) spread practical arithmetic through many editions.
- **[T]** Edo-period *terakoya* schools taught commercial arithmetic.
- **[T]** Seki Takakazu (c. 1642–1708) represents higher *wasan*, though not every part of his mathematics depended on the bead abacus.

Evolution of the frame:

1. imported or early Japanese 2:5 pattern;
2. 1:5 pattern increasingly common in the nineteenth century;
3. 1:4 soroban becomes standard in the twentieth century;
4. the Education Ministry prescribed the four-earth-bead school standard in 1938.

The Japan Chamber of Commerce and Industry’s federation confirms that the 1:4 instrument is now standard and that formal proficiency testing began in 1928. [Japan Abacus Association](https://www.shuzan.jp/english/history/) The national federation gives a more detailed institutional chronology. [National Federation history, Japanese](https://www.soroban.or.jp/howto/arekore/history/)

### 2.11 Russia

The modern Russian schoty differs structurally from the East Asian abacus.

- horizontal wires rather than vertical rods;
- ordinarily ten beads on a wire;
- no transverse five-bead deck;
- middle beads may be differently colored to aid visual grouping;
- decimal place value rises vertically;
- one exceptional four-bead wire historically accommodated quarters of a monetary unit.

**[T/R]** Sokolov, Karelskaia, and Zuga connect its emergence with sixteenth-century Russian decimal monetary development and date its familiar form to the eighteenth century. [Their 2023 *Accounting History* article](https://journals.sagepub.com/doi/10.1177/10323732221132005)

**[D]** Russian historiography often calls it an indigenous invention, while comparative historians have proposed transmission or influence from China. The seventeenth-century Russian “board account” described in manuscripts differed considerably from the later schoty. A definitive continuous material genealogy has not been established.

Recent scholarship has reopened the possibility of Chinese influence rather than treating either national-origin claim as settled. [Aleksey Volkov seminar abstract](https://www.mathnet.ru/php/seminars.phtml?option_lang=eng&presentid=48907)

### 2.12 The alleged Aztec *nepohualtzintzin*

Modern teaching devices called *nepohualtzintzin* usually have 13 rows and seven beads, sometimes divided 3+4, and are explained through a base-20 cosmological scheme.

- **[M]** The familiar bead-frame reconstruction was popularized in the twentieth century, particularly by Mexican engineer David Esparza Hidalgo and his *Cómputo azteca*.
- **[D]** No securely excavated pre-Columbian example of this frame is known.
- **[D]** No unambiguous pre-Conquest codex illustration establishes its construction.
- **[T, but different device]** Early colonial accounts mention indigenous reckoning, kernels, stones, cords, colors, and knots. Diego de Valadés in 1579 described cord-and-knot devices by comparison with quipus.
- **[R]** Such testimony may preserve knowledge of indigenous calculating aids, but it does not validate the specific modern 13×7 frame.
- **[L/M]** Claims that the exact modern device was used unchanged by Olmec, Maya, Mexica, and Inca peoples collapse distinct cultures and lack an archaeological chain.

The responsible conclusion is not “the Aztecs could not calculate.” Their tribute records and land surveys show substantial arithmetic. It is that the modern bead-frame’s claimed antiquity remains unproved.

---

## 3. Arithmetic and instruments

### 3.1 Finger reckoning

Hands precede all surviving boards. Finger counting supplies:

- the obvious decimal grouping;
- five as a sub-base;
- terms such as *digit*;
- portable signaling systems capable of representing much larger numbers than ten.

Classical and medieval finger-reckoning schemes assigned hundreds and thousands through finger positions and choice of hand. Bede’s 725 description is a documented example, not evidence that every earlier society used the same scheme.

### 3.2 Pebble-board arithmetic

Consider 278 + 156 on a decimal lined board.

1. Set 278: two counters in hundreds, seven in tens, eight in units.
2. Add six units: the units now total fourteen.
3. Exchange ten unit counters for one tens counter, leaving four.
4. Add five tens to the existing eight tens: thirteen tens.
5. Exchange ten tens for one hundred, leaving three tens.
6. Add one hundred to the existing three hundreds.
7. Read 434.

On a bi-quinary board the exchanges are smaller and faster:

- five one-counters become one five-counter;
- five plus five becomes one counter in the next decimal place.

A counter-board calculation is an algorithm, but the temporary intermediate states normally vanish when the board is cleared. Written accounts usually record inputs and result, not every manipulation.

### 3.3 Roman *calculus*

Latin *calculus* is a diminutive of *calx*, a small stone or pebble. From “reckoning pebble” it came to mean a calculation or account, and eventually the mathematical “calculus.”

Roman operators probably combined:

- memorized multiplication;
- finger reckoning;
- loose counters;
- written Roman numerals for durable records;
- boards or portable bronze abaci.

**[R]** The bronze frame’s design permits addition and subtraction directly and multiplication or division by repeated partial operations. No surviving Roman user manual explains the exact hand choreography. Demonstrations necessarily adapt later counter algorithms.

### 3.4 Chinese rod calculus

Rod calculation could support:

- addition and subtraction;
- multiplication and division;
- extraction of square and cube roots;
- fractions;
- simultaneous linear equations;
- positive and negative quantities, often distinguished by rod color;
- polynomial procedures in Song–Yuan mathematics.

The *Nine Chapters* contains practical problems in fields, grain exchange, taxation, surveying, proportions, and linear systems. Liu Hui’s commentary of 263 CE explains and justifies many algorithms.

The *fangcheng* procedure arranges coefficients in a rectangular array and eliminates them in a manner recognizably related to modern Gaussian elimination. That similarity does not mean ancient Chinese authors possessed modern matrix symbolism; it shows that movable positional counters enabled column operations.

### 3.5 Suanpan technique

Typical operations include:

- direct addition and subtraction using complement rules;
- multiplication with memorized tables;
- division with quotient-placement rules;
- square- and cube-root algorithms;
- commercial conversion of money, weights, and measures.

A traditional rhyme embodies a bead operation. For example, adding three when insufficient lower beads are available may be expressed by the complement instruction “add five, remove two.” The spoken rule synchronizes memory and hand.

The extra beads of the 2:5 frame permit “suspended bead” or temporary over-capacity techniques. A normalized answer still has one decimal digit per rod.

### 3.6 Soroban technique and schools

Japanese practice reduced physical redundancy and optimized motion:

- 1:4 beads exactly encode digits 0–9;
- the thumb normally raises lower beads;
- the index finger lowers them and moves the heaven bead;
- complement operations avoid slow bead-by-bead counting;
- multiplication and division are laid out across several rods.

Edo-period *terakoya*, merchant houses, printed manuals, and private masters transmitted practical skill. In the modern period:

- national school curricula formalized technique;
- commercial and educational associations created ranks and examinations;
- 1928 marks the beginning of the major formal proficiency-testing system;
- the four-bead form entered national school texts in 1938;
- private *soroban juku* remain active.

### 3.7 Schoty technique

Each ordinary wire represents a power of ten and contains ten equal beads. At zero, beads rest to the right; counted beads move left. Ten beads carried on one wire are cleared and replaced by one bead on the next wire above.

Because five is not embodied by a separate heaven bead, the differently colored fifth and sixth beads act as visual landmarks. The schoty is therefore decimal positional with perceptual five-grouping, not bi-quinary coding.

Its commercial advantages included:

- rapid totaling;
- robustness;
- visibility to clerk and customer;
- compatibility with Russian monetary accounts;
- no need for paper during intermediate work.

It remained emblematic of Russian shops and accountancy into the Soviet period and, according to recent scholarship, survived in limited use much later than simplistic “calculator replaced it instantly” narratives suggest.

### 3.8 Medieval counter-casting and jetons

European reckoning counters were called:

- counters;
- jetons or jettons;
- French *jetons*, associated with *jeter*, “to throw/place”;
- German *Rechenpfennige*, “reckoning pennies.”

The oldest securely identified medieval jetons are often assigned to the late thirteenth century, including issues connected with John II of Hainault and Holland (1280–1304). Nuremberg later became a major production center.

Jetons resemble coins but ordinarily were not currency. Their imagery could advertise rulers, cities, guilds, reckoning masters, or makers. Some were plated or misleadingly imitative; inscriptions sometimes explicitly denied that the brass counter was a gold coin.

### 3.9 The English Exchequer

Richard fitzNigel’s *Dialogus de Scaccario*, composed around 1178–1189, gives the classic first-person institutional description.

- **[T]** The table was about ten feet by five, with a raised rim.
- **[T]** It carried a black cloth ruled with lines a foot or hand-span apart.
- **[T]** Counters were placed in its spaces according to rank.
- **[T]** The accountant had to coordinate spoken declaration with placement so that witnesses could detect error.
- **[T]** Columns handled pence, shillings, pounds, scores, hundreds, thousands, and rarely tens of thousands.

The Latin begins: *Superponitur scaccario pannus non quilibet, sed niger virgis distinctus… In spatiis autem calculi…*—“Over the exchequer is spread not an ordinary cloth but a black one marked with lines… In the spaces the counters…” [Harvard Ames Foundation text](https://amesfoundation.law.harvard.edu/lhsemelh/materials/Exchequer.pdf)

**[D]** “Chequered cloth” is often imagined as alternating black-and-white chessboard squares. FitzNigel actually describes a black cloth marked with lines. Nineteenth- and twentieth-century scholars disputed whether it really looked like the modern checkerboard suggested by the institution’s name. [Cambridge discussion](https://www.cambridge.org/core/books/abs/english-and-their-legacy-9001200/exchequer-cloth-c-11761832-the-calculator-the-game-of-chess-and-the-process-of-photozincography/3B6D88DC7879B1BD80A712B8D5CF2342)

The board served audit and legal theater as much as raw arithmetic: sheriff, treasurer, clerks, and witnesses could see debts and credits enacted materially.

### 3.10 Robert Recorde

Robert Recorde (c. 1512–1558), Welsh physician and mathematician, published *The Grounde of Artes* in 1543; some catalogues give 1542 for the first issue. It became one of the most influential English arithmetic books.

Recorde explains both:

- counter reckoning;
- written arithmetic with numerals.

His dialogic master-and-scholar format preserves practical “casting” of accounts. A documented worked layout represents £198 19s. 11d. in separate compartments for pence, shillings, pounds, and scores of pounds. This is direct evidence that written algorism did not instantly displace the board.

Recorde also introduced the equality sign `=` in *The Whetstone of Witte* (1557), choosing parallel lines because “noe 2 thynges can be moare equalle.” That typographic invention belongs to written algebra, not to the counter board, but it shows the same author standing across material and written calculation.

### 3.11 Algorists and abacists

The standard narrative presents a contest:

- abacists: counters and Roman numerals;
- algorists: written Hindu-Arabic digits and zero.

There was real competition between practices, but “two ideological parties fighting for centuries” is partly a textbook dramatization.

**Documented coexistence:**

- Gerbertian digit-counters;
- thirteenth- to sixteenth-century written algorisms;
- merchant arithmetic schools;
- account books mixing Roman and Hindu-Arabic forms;
- books such as Recorde teaching both;
- continued production of jetons after written numerals were common.

**Famous image:** Gregor Reisch’s *Margarita philosophica* editions, especially the 1503/1504 tradition and the 1512 *Margarita philosophica nova*, show Arithmetic presiding over Boethius using written figures and Pythagoras using a counter board.

- **[T]** The woodcut is real.
- **[R]** It visualizes contemporary ideas about old and new techniques.
- **[L if read literally]** Boethius did not historically use the mature late-medieval Hindu-Arabic notation shown, and Pythagoras is not documented using that exact medieval board. ETH correctly calls it anachronistic. [ETH Library](https://library.ethz.ch/en/sammlungen-und-archive/platforms/virtual-exhibitions/fibonacci-un-ponte-sul-mediterraneo/fibonaccis-significance-for-the-present-day/dispute-between-abacists-and-algorists.html)

### 3.12 Related textbooks: what belongs and what does not

The following works illuminate arithmetic history, but only some directly document abacus practice.

| Work | Date | Relationship to boards |
|---|---:|---|
| Rhind Mathematical Papyrus | c. 1650 BCE | Egyptian arithmetic text; no framed abacus established |
| Plimpton 322 | Old Babylonian, c. 1800 BCE | Sexagesimal table; not an abacus manual |
| *Nine Chapters* | compiled around 1st c. BCE/CE | Procedures reconstructed as counting-rod operations |
| Aryabhata, *Aryabhatiya* | 499 | Indian mathematical astronomy; not a bead-abacus manual |
| Brahmagupta, *Brahmasphutasiddhanta* | 628 | Written rules for arithmetic with zero and negatives; not evidence for invention of the abacus |
| al-Khwarizmi, arithmetic treatise | early 9th c. | Disseminated Indian positional calculation in Arabic; Latin descendants gave “algorithm” |
| Fibonacci, *Liber abaci* | 1202; revised 1228 | Despite its title, promotes Indian digits and written arithmetic, not a bead frame |
| Sacrobosco, *Algorismus vulgaris* | 13th c. | Written place-value arithmetic |
| Pacioli, *Summa de arithmetica* | 1494 | Commercial arithmetic in the Italian abacus-school tradition; “abacus” here can mean practical arithmetic broadly |
| Recorde, *Grounde of Artes* | 1543 | Directly teaches counters and written arithmetic |
| Cheng Dawei, *Suanfa tongzong* | 1592 | Major suanpan manual |

The title *Liber abaci* is therefore frequently mistranslated in spirit. In medieval Italy, *abbaco* could mean calculation or practical arithmetic, not necessarily the framed device now pictured by the English word *abacus*.

### 3.13 The 1946 soroban–calculator contest

**[T, with a one-day dating discrepancy in secondary accounts]**

In November 1946 at Tokyo’s Ernie Pyle Theater:

- Japanese operator: Kiyoshi/Yoshiyoshi Matsuzaki (松崎喜義), champion employee of the postal Savings Bureau;
- American operator: Private Thomas Nathan Wood, U.S. Army finance section;
- instruments: modern 1:4 soroban versus a Monroe electric mechanical calculator;
- tests: addition, subtraction, multiplication, division, and a mixed problem;
- result: soroban won four events to one; the calculator won multiplication.

The Japanese Abacus Museum gives **11 November** and cites the later book *Gakkō shuzan meikai*. Other reports and reproductions give **12 November**. The contemporary *Time* item appeared on 25 November. The safest conclusion is that the contest and 4–1 result are well attested, while secondary sources disagree by one day. [Japanese Abacus Museum account](https://soroban-museum.note.jp/n/n0ab5b78d8796) [Contemporary-source-based English account](https://www.ee.torontomu.ca/~elf/abacus/abacus-contest.html)

**[Legendary framing]** Headlines saying civilization “tottered” or that the machine age “took a step backward” are journalistic drama. The contest compared an expert soroban operator with one contemporary calculator and one operator under a chosen problem set. It did not show that all abaci outperform all electronic calculation.

### 3.14 Mental abacus, *anzan*

*Anzan* (暗算) means mental calculation. In abacus pedagogy it often means visualizing and manipulating an imagined soroban; “flash anzan” presents numbers rapidly for mental summation.

**[T/scientific evidence]** James Stigler’s 1984 experiments found qualitative and quantitative evidence that trained children used a mental-abacus representation. [Cognitive Psychology article](https://www.sciencedirect.com/science/article/pii/0010028584900069)

Later neuroimaging studies found that expert abacus calculation recruits visuospatial neural resources differently from ordinary verbally mediated arithmetic. [Hanakawa et al.](https://www.sciencedirect.com/science/article/pii/S1053811903000508)

**[Qualification]** Evidence supports domain-specific calculation skill and altered strategies. Broad advertising claims that abacus lessons automatically increase intelligence, cure cognitive conditions, or improve every academic domain go beyond the cited evidence.

---

## 4. Transmission and replacement

### 4.1 Mediterranean transmission

No continuous document traces “Mesopotamia → Egypt → Greece → Rome” as a single technological lineage.

What can be said:

1. **[A/T]** Several ancient Mediterranean cultures used counters and accounting surfaces.
2. **[R]** Greek and Roman boards share a family resemblance and probable historical continuity.
3. **[D]** The exact direction and dates of every borrowing are unknown.
4. **[L]** A single named inventor of the abacus is not preserved.
5. **[L]** “Invented in Mesopotamia in 2700 BCE” is frequently repeated without a surviving identified board or contemporary description.

### 4.2 Rome to medieval Europe

Loose-counter practice fits continuity better than a story of disappearance and rediscovery. Portable bronze hand abaci vanish from the material record, but boards, counters, finger arithmetic, and Roman written numerals continued.

Gerbert’s apex-board around 1000 shows transformation: positional columns combined with marked digit counters. Later medieval fiscal and merchant boards usually reverted to or retained unmarked jetons.

### 4.3 India, Baghdad, al-Andalus, and Italy

This route belongs chiefly to written positional numerals and algorism:

- Indian place-value arithmetic, including zero notation;
- adoption and exposition in Arabic;
- al-Khwarizmi in Abbasid Baghdad, early ninth century;
- Latin translations from the twelfth century;
- contact zones in al-Andalus, Sicily, and Mediterranean trade;
- Fibonacci, raised partly in Bugia/Béjaïa in North Africa, publishing *Liber abaci* in 1202.

This transmission did not carry “the abacus” as a simple object from India to Europe. It introduced a competing and eventually dominant written calculation technology.

### 4.4 The Florentine ban of 1299

A celebrated claim says Florence banned Arabic numerals in 1299 because merchants could alter them or because zero enabled fraud.

- **[Documented core]** The statute of the Florentine money-changers’ guild required account entries to be written openly in letters and forbade certain ciphered forms.
- **[R]** Legibility, auditability, and resistance to alteration are plausible motives.
- **[D]** Popular paraphrases differ about whether all Hindu-Arabic numerals were prohibited, whether only account books were covered, and whether the statute specifically targeted zero.
- **[L unless the statute is quoted]** “Florence banned zero” is an overstatement.
- **[L]** Claims that bankers therefore kept a secret second set of Arabic-numeral books require case-specific evidence.

The real episode shows institutional resistance to easily altered symbols in legal accounts, not irrational fear of mathematics.

### 4.5 China to Japan and Korea

The framed Chinese abacus reached Japan by the late sixteenth century and was adapted into the soroban. Korean *jupan* forms similarly belong to a wider East Asian sphere of commercial and pedagogical exchange.

Chinese-character numerals still coexist with Hindu-Arabic digits in China, Japan, and Korea:

- financial documents may use formal anti-fraud characters such as 壹, 貳/贰, 參/叁;
- calendars, legal texts, addresses, ceremonial dates, and vertical typography retain character numerals;
- Arabic digits dominate much scientific and everyday numerical writing.

This coexistence is not survival of “abacus numerals”: written character numerals and bead calculation are related but distinct systems.

### 4.6 China: rods replaced by beads

The transition was gradual:

- rods retained advantages for advanced algebraic arrays;
- beads were captive and portable;
- commercial arithmetic favored fast addition, subtraction, multiplication, and division;
- printed rhyme manuals supported standardized instruction;
- by late Ming times the suanpan was culturally conspicuous.

**[D]** It remains unclear why replacement occurred when it did. Printing, commercialization, pedagogy, portability, and changing mathematical priorities are all plausible contributors.

### 4.7 Japan: adaptation rather than simple copying

Japan did not merely preserve the imported 2:5 device:

- it reduced the heaven deck to one bead;
- then reduced earth beads from five to four;
- standardized fingering;
- developed graded school and commercial systems;
- integrated physical calculation with mental visualization.

The 1:4 form became an optimized decimal digit-machine.

### 4.8 Russia and electronic replacement

Schoty persisted in retail, bookkeeping, and schools through much of the twentieth century. Mechanical calculators and then electronic calculators reduced its commercial role, but replacement was uneven.

**[Documented present]** Soroban and suanpan practice survive in education, competition, cultural heritage, shops, museums, and mental arithmetic. Chinese *zhusuan* was inscribed by UNESCO in 2013 on the Representative List of the Intangible Cultural Heritage of Humanity—not, as some Japanese summaries loosely say, “the abacus became a World Heritage site.”

---

## 5. People

### Greek and Roman world

- **Herodotus** (c. 484–c. 425 BCE): provides the textual comparison of Greek and Egyptian counter direction.
- **Nicolas-Claude Fabri de Peiresc** (1580–1637): documented the Autun-attributed bronze abacus in drawings and letters dated 1634.
- **Marcus Welser** (1558–1614): published a now-lost Roman-style hand abacus.
- **Lorenzo Pignoria** (1571–1631): published another early antiquarian representation.
- **Rudolf Fellmann**: published the Aosta bronze and Roman calculating tablets in modern archaeological scholarship.

### Medieval and Renaissance Europe

- **Boethius** (c. 480–524/525): Latin authority on arithmetic; later cast anachronistically as the victorious algorist.
- **Bede** (672/673–735): documented medieval finger reckoning and calendrical computation.
- **Gerbert of Aurillac/Sylvester II** (c. 946–1003): associated with apex-counters and mathematical teaching; later demonized in legend.
- **Bernelinus** (early eleventh century): preserves Gerbertian abacus material and fraction procedures.
- **Richard fitzNigel** (c. 1130–1198): author of *Dialogus de Scaccario* and witness to the English fiscal counting table.
- **al-Khwarizmi** (fl. c. 820): his name yielded Latin *algorismus* and ultimately “algorithm.”
- **Leonardo Fibonacci** (c. 1170–after 1240): learned commercial mathematics in Bugia and advocated Indian numerals in *Liber abaci*.
- **Johannes de Sacrobosco** (d. c. 1256): *Algorismus vulgaris* helped standardize written calculation.
- **Gregor Reisch** (c. 1467–1525): author of *Margarita philosophica*, source of the celebrated Boethius–Pythagoras image.
- **Luca Pacioli** (c. 1447–1517): codified commercial arithmetic and bookkeeping culture in the 1494 *Summa*.
- **Robert Recorde** (c. 1512–1558): taught counter-casting and written arithmetic in English.
- **John Napier** (1550–1617): logarithms and “Napier’s bones” belong to the next wave of calculating aids; neither derived simply from the abacus, although both reduced repeated arithmetic operations.

### China

- **Xu Yue** (c. 160–c. 220): linked to an early textual notice of calculation devices; identification with the later suanpan is disputed.
- **Liu Hui** (fl. 263): commentator on the *Nine Chapters*; crucial for reconstructing rod algorithms.
- **Qin Jiushao** (c. 1202–1261) and **Zhu Shijie** (fl. 1280–1303): represent the sophistication of pre-suanpan rod mathematics.
- **Cheng Dawei** (1533–1606): merchant-mathematician and author of the 1592 *Suanfa tongzong*.
- **Zhu Zaiyu** (1536–1611): prince, mathematician, and music theorist; associated with high-precision calculations for equal temperament.
- **Joseph Needham** (1900–1995): made Chinese scientific history widely accessible but sometimes accepted stronger reconstruction than later textual critics.
- **Jean-Claude Martzloff** (1943–2018): produced a critical history attentive to gaps between textual evidence and modern reconstructions.

### Japan

- **Mōri Shigeyoshi** (fl. early seventeenth century): *Warizan-sho*, 1622.
- **Yoshida Mitsuyoshi** (1598–1672): *Jinkōki*, 1627.
- **Seki Takakazu** (c. 1642–1708): major *wasan* mathematician.
- **Kiyoshi/Yoshiyoshi Matsuzaki**: soroban operator in the 1946 contest.
- **Thomas Nathan Wood**: U.S. Army calculator operator in that contest.
- **James W. Stigler**: supplied experimental evidence for mental-abacus cognition in 1984.

### Russia

- Russian merchants, cashiers, and bookkeepers—not one securely documented inventor—created and transmitted schoty practice.
- **I. A. Apokin and L. E. Maistrov** surveyed Russian calculating technology.
- **Viatcheslav Sokolov, Svetlana Karelskaia, and Ekaterina Zuga** produced the recent accounting-history reassessment.
- **Aleksey Volkov** has reopened the case for Chinese influence.

### The purported Aztec device

- **David Esparza Hidalgo**: twentieth-century engineer who popularized the modern *nepohualtzintzin*. He is the documented disseminator of the present bead-frame form, not a witness to a surviving pre-Columbian specimen.

---

## 6. Culture

### 6.1 Law and public audit

Counting boards made arithmetic visible. At the English Exchequer, counters embodied claims and credits in front of officials and witnesses. The tool was consequently part of law, fiscal procedure, and ritualized accountability.

The very word *Exchequer* descends from the table/cloth and its comparison to a chessboard. Modern “check,” “chequer,” and “chess” have intertwined etymological histories, but the popular claim that every sense of “check” derives directly from counter arithmetic is too simple.

### 6.2 Coins and jetons

Jetons occupy a border between instrument and image:

- they were calculation tools;
- they carried portraits, coats of arms, religious mottoes, guild marks, or political propaganda;
- worn or pierced examples were reused as gaming pieces, charms, or ornaments;
- their coin-like form invited counterfeiting or confusion.

Roman hand abaci were calibrated for currency and weight fractions. Their duodecimal registers materialize the relationship among *libra*, *as*, and *uncia*.

### 6.3 Liturgy and calendars

Computus—the calculation of Easter and the ecclesiastical calendar—used finger reckoning, tables, written numbers, and occasionally boards. Bede’s work integrates number, fingers, time, and liturgy.

The abacus itself has no liturgical numeral script. Roman numerals persisted in church inscriptions, regnal designations, chapter numbering, and calendars alongside material calculation.

### 6.4 Gematria, isopsephy, and chronograms

Hebrew gematria and Greek isopsephy assign values to letters; Latin chronograms select numeral-letters from a phrase to yield a date.

These are not abacus systems. Their relevance is cultural contrast:

- letter-numerals preserve values in a durable text;
- board values arise from place;
- a chronogram invites reading and interpretation;
- a counter arrangement invites manipulation.

No evidence shows that gematria or isopsephy generated the bead abacus.

### 6.5 Literature and art

Abaci and counting tables signify:

- commerce and thrift;
- accountancy and official scrutiny;
- practical intelligence;
- old technology confronted by modern machinery.

Examples include:

- the Darius Vase’s tribute/accounting scene;
- medieval and Renaissance images of merchants at counting tables;
- Reisch’s personified Arithmetic judging Boethius and Pythagoras;
- Nuremberg jetons depicting reckoning masters;
- Russian paintings and literature using schoty as attributes of the merchant or cashier;
- postwar reporting that made the 1946 contest a parable of tradition defeating mechanization.

### 6.6 Typography and old-style figures

Old-style or text figures—`1 2 3 4 5 6 7 8 9 0` with varying ascenders and descenders—belong to European printing with Hindu-Arabic digits. They are not derived from bead shapes.

The supposed “number of angles” origin of the modern digits is a modern diagrammatic legend. Historical digit forms evolved through Indian and Arabic manuscript traditions; their changing curves do not preserve a designed angle-count code.

### 6.7 Modern identity and heritage

Chinese *zhusuan* is a recognized intangible cultural practice. Japanese soroban organizations maintain museums, examinations, teacher networks, competitions, and school materials. Russian schoty remain a recognizable national cultural object.

National identification can preserve expertise, but it also encourages overly clean origin stories. Cultural ownership in the present is documented; sole prehistoric invention is a separate historical question.

---

## 7. Controversies and disputes

### 7.1 Who invented the abacus?

**Verdict: open.**

- **Fact:** Salamis is the earliest surviving generally accepted counting board.
- **Reconstruction:** loose-counter arithmetic is older than the surviving slab.
- **Dispute:** Mesopotamia, Egypt, and other regions are proposed as places of origin.
- **Legend:** a single inventor or an exact date such as “Babylonia, 2700 BCE.”
- **Evidence absent:** a securely identified Mesopotamian or Egyptian physical board with contemporary operating instructions.

Independent invention is entirely plausible because grouping objects by place is technically simple.

### 7.2 Does the abacus have zero?

Both “yes” and “no” can be misleading.

- It has a zero-state: an empty place.
- Most historical frames lack a dedicated zero bead.
- An empty operational place is not identical to a written zero glyph.
- Roman operators could represent 101 through an empty tens column.
- There is no evidence that the Roman abacus independently produced the later written European `0`.

Thus “Roman numerals have no zero” says something about the ordinary written numeral inventory, not the full computational capacities of Roman people.

### 7.3 Is the suanpan ancient Han technology?

**Evidence for an early date:**

- Han-era texts discuss calculation and devices;
- Xu Yue’s received work mentions bead-related calculation;
- rods supplied an indigenous decimal positional substrate.

**Evidence for a later date:**

- early passages do not clearly describe the standard framed 2:5 instrument;
- pictorial evidence before the late medieval period is ambiguous;
- the *Qingming shanghe tu* object sometimes identified as an abacus is contested;
- unambiguous printed manuals and images become abundant only in the Ming;
- Martzloff dates common use to the later sixteenth century.

**Conclusion:** Chinese positional material calculation is ancient; the standard suanpan’s secure history is much later.

### 7.4 Did China have a counting board?

Needham and other historians pictured rods on a marked grid. Martzloff and later textual scholarship note:

- no securely identified ancient rigid board;
- no clear ancient description requiring one;
- texts allow a table, mat, floor, bed, or paper;
- later images may depict an abacus, not a rod board.

“Counting board” is therefore often a functional translation for the work surface, not necessarily an excavated gridded object.

### 7.5 Did Rome borrow its hand abacus from China?

The resemblance—decimal columns divided into one-valued and five-valued sections—is real.

Against a confident transmission claim:

- Roman and Chinese secure dates do not provide a clear donor–recipient sequence;
- bi-quinary organization follows naturally from fingers and decimal grouping;
- direct documentary transmission evidence is absent;
- the mature suanpan is securely attested much later than Imperial Roman bronze frames.

Similarity alone cannot establish direction. Independent optimization is at least as plausible as Silk Road transfer.

### 7.6 Is the Russian schoty indigenous or Chinese-derived?

**Indigenous-development case:**

- form differs markedly from suanpan and soroban;
- Russian manuscript predecessors and monetary reforms supply local context;
- recognizable form emerges with Russian decimal accounting.

**Chinese-influence case:**

- Eurasian commercial routes existed;
- bead-frame principles could travel and be radically adapted;
- recent comparative work finds the question insufficiently closed.

No named inventor or decisive transitional object settles it.

### 7.7 Is the *nepohualtzintzin* pre-Columbian?

**Claim:** a 13×7 Aztec abacus embodies sacred counts—13 heavens or days, 20-based arithmetic, and a 260-day calendar.

**Supporting material cited by advocates:**

- indigenous vigesimal numeration;
- colonial reports of stones, maize kernels, knots, or cords;
- later oral testimony;
- modern operational elegance.

**Objections:**

- no securely excavated example;
- no unambiguous pre-Conquest depiction;
- the precise modern form becomes visible through Esparza Hidalgo;
- symbolic explanations may be retrospective;
- cord/knotted records are not the same object as a bead frame.

**Conclusion:** pre-Columbian Mesoamerican calculating aids are credible; this exact bead device is a modern reconstruction unless new archaeological evidence appears.

### 7.8 The 1946 contest

The event is factual. The mythology lies in what is inferred:

- speed depended on task mix;
- the Monroe device was electromechanical, not an electronic general-purpose computer in the modern sense;
- expert selection mattered;
- one contest does not rank technologies universally.

The one-day date discrepancy—11 versus 12 November—should remain visible rather than silently harmonized.

### 7.9 The “abacists versus algorists” war

There was competition, but the polarized image exaggerates:

- users frequently knew both methods;
- counters and written digits were complementary;
- resistance often concerned auditability and training costs rather than theology;
- the Reisch woodcut is allegory, not reportage;
- claims that “the Church banned Arabic numerals” require a particular decree and should not be generalized from municipal or guild regulations.

### 7.10 The Florentine ban

The 1299 rule is real in its guild-account context. Later retellings add:

- a universal city ban;
- a special ban on zero;
- church hostility;
- secret double bookkeeping.

Those additions require evidence not supplied by the usual citation.

### 7.11 Salamis as gaming board or calculator

Its discovery as a “game board” interpretation reflects formal resemblance. The acrophonic monetary signs and place-like line system support calculation. Nevertheless:

- no contemporary instruction survives;
- multipurpose use cannot be excluded;
- exact counter motions remain reconstructed.

### 7.12 Authenticity of Roman bronze examples

The Aosta archaeological context supports the ancient class. Antiquarian pieces appearing in seventeenth-century collections must still be evaluated individually. The BnF catalogue’s candor about discovery history is more reliable than captions that simply call every specimen “first-century Roman.”

### 7.13 Etymology of *abacus*

Secure chain:

- English *abacus*;
- Latin *abacus*;
- Greek ἄβαξ, genitive ἄβακος, “board/table.”

**[D]** A further derivation from a Semitic word cognate with Hebrew אָבָק, “dust,” is widely repeated but semantically and phonologically debated. Robert Beekes and others regard it as weak. Therefore “abacus literally means dust board” should be labeled a hypothesis, not a fact. [Etymonline](https://www.etymonline.com/word/abacus) [American Heritage Dictionary](https://www.ahdictionary.com/word/search.html?q=abacus)

### 7.14 Word descendants

- **calculus:** Latin “small pebble,” then reckoning/account, later the branch of mathematics.
- **calculate:** from Latin *calculare*, to reckon with pebbles.
- **digit:** Latin *digitus*, finger or toe.
- **cipher:** Old French/medieval Latin from Arabic *ṣifr*, “empty, zero”; later “numeral,” secret writing, or code.
- **zero:** Italian *zero*, via medieval Latin forms, from Arabic *ṣifr*; ultimately connected to Sanskrit *śūnya*, “empty.”
- **algorithm:** medieval Latin *algorismus*, from the Latinized name of al-Khwarizmi; later reshaped under influence of Greek *arithmos*.
- **abacus:** Latin from Greek; deeper Semitic origin uncertain.
- **counter:** an object used in counting; not every sense derives from the calculating object.
- **jeton:** French, conventionally connected with *jeter*, because counters were placed or cast.

### 7.15 Other template “firsts” that do not establish abacus origins

The Bakhshali manuscript, Gwalior inscription of 876, Brahmi numerals at Nana Ghat and Nasik, and Dresden Codex are central to histories of written numerals and zero, not direct evidence for counting boards.

- **Bakhshali:** birch-bark manuscript with dot placeholders; radiocarbon tests produced widely separated date ranges for different leaves. Dating the physical bark does not automatically date one act of composition.
- **Gwalior, 876 CE:** a secure inscriptional zero in a place-value number; important for written Indian zero.
- **Nana Ghat and Nasik:** early Brahmi numeral evidence; non-positional and not bead notation.
- **Dresden Codex:** securely demonstrates Maya bar-and-dot numerals and zero signs in calendrical computation; it does not document the modern *nepohualtzintzin*.
- **Maya zero:** independently developed in Mesoamerica, but particular “earliest” dates depend on whether one requires a full positional function, a calendrical completion sign, or a glyph recognizable as zero.
- **Babylonian placeholder:** late Babylonian scribes used separation signs internally, but not initially as a number usable in all positions.
- **Chinese rod empty place:** operational zero without an obligatory physical token.
- **Roman empty groove:** likewise an empty-state zero.

These histories show that “zero” is not one indivisible invention. Empty place, placeholder mark, number word, arithmetic operand, and metaphysical concept have different documentary histories.

### 7.16 Ifrah, Menninger, and modern grand narratives

Karl Menninger’s *Number Words and Number Symbols* remains valuable for comparative examples and images, but its diffusionist and developmental narratives must be checked against newer archaeology and philology.

Georges Ifrah’s *Universal History of Numbers* made the subject accessible and assembled a huge range of examples.

- **Strength:** encyclopedic comparative ambition.
- **Problem:** reviewers including Joseph Dauben and later specialists identify unsupported reconstructions, misdatings, and overly confident diffusion stories.
- **Methodological rule:** use Ifrah to locate a claim, not as the final authority for a contested artefact.

Stephen Chrisomalis’s *Numerical Notation* (2010) is the standard comparative typological survey for written notations. Its strength is separating structural classification from myths of linear progress. Because the abacus is an instrumental rather than written notation, Chrisomalis supplies classification discipline more than a complete artefact catalogue.

---

## 8. Open questions

1. What material or textual evidence preceded Salamis but failed to survive?
2. Was the Salamis slab a dedicated commercial calculator, a public-account board, a teaching tool, or multipurpose equipment?
3. What are the individual authenticity histories of every Roman bronze hand abacus first recorded in seventeenth-century cabinets?
4. Can the smallest Roman fractional grooves be decoded from an independent contemporary text?
5. How common were portable hand abaci compared with loose-counter boards?
6. What exact device did Xu Yue or the received *Shushu jiyi* describe?
7. When did the term *suanpan* shift from a general calculating surface to the familiar framed abacus?
8. Did a rigid gridded Chinese rod board ever exist as standard equipment?
9. Which economic or pedagogical changes explain the rapid Ming adoption of bead arithmetic?
10. Was the first Japanese transmission direct from coastal China, through Korea, through returning soldiers or merchants, or through several channels?
11. Can a continuous object sequence connect seventeenth-century Russian board accounts to eighteenth-century schoty?
12. Did Chinese bead frames influence Russia, or do the similarities arise independently?
13. Is there any pre-twentieth-century source for the precise 13-row, seven-bead *nepohualtzintzin*?
14. Can archival copies of the 1299 Florentine guild statute establish the exact scope of its numeral rule and strip away later paraphrase?
15. Was the 1946 contest held on 11 or 12 November, and can a same-day program or newspaper resolve the discrepancy?
16. How durable are mental-abacus gains outside trained calculation tasks?
17. How should museums distinguish ancient originals, early-modern antiquarian restorations, and modern operational replicas?

---

## 9. Chronological synopsis

| Date | Event | Status |
|---|---|---|
| c. 42,000 BP | Lebombo notches | Artefact; counting interpretation disputed |
| c. 20,000 BP | Ishango bone | Artefact; mathematical readings disputed |
| 4th millennium BCE | Mesopotamian tokens and proto-writing | Documented accounting; no secure abacus |
| c. 3100 BCE | Narmer macehead numbers | Written enumeration, not an abacus |
| c. 1800 BCE | Plimpton 322 | Babylonian numerical table |
| c. 1650 BCE | Rhind Papyrus copied | Egyptian arithmetic |
| 5th c. BCE | Herodotus on Greek/Egyptian counter direction | Documented text |
| late 4th c. BCE | Darius Vase accounting scene | Documented image; mechanics uncertain |
| 4th–3rd c. BCE | Salamis tablet, EM 11515 | Earliest surviving accepted counting board |
| c. 1st c. BCE–1st c. CE | *Nine Chapters* compilation | Rod procedures reconstructed |
| late 1st c. CE | Aosta Roman bronze abacus | Archaeologically contextualized artefact |
| 263 CE | Liu Hui’s commentary | Major rod-calculation text |
| 499 | Aryabhata | Indian positional mathematical tradition |
| 628 | Brahmagupta’s zero rules | Written arithmetic, not bead-frame origin |
| 725 | Bede’s finger reckoning | Documented text |
| early 9th c. | al-Khwarizmi’s arithmetic | Indian numerals in Arabic scholarship |
| c. 980–1000 | Gerbert’s apex-abacus tradition | Textually documented hybrid |
| c. 1178–1189 | *Dialogus de Scaccario* | Detailed fiscal counting-table account |
| 1202/1228 | Fibonacci’s *Liber abaci* | Written algorism and merchant arithmetic |
| 13th c. | Sacrobosco’s *Algorismus* | Written decimal arithmetic |
| 1299 | Florentine guild restriction | Documented core; scope often exaggerated |
| c. 14th–16th c. | Suanpan emerges and spreads | Early date disputed; Ming evidence secure |
| 1494 | Pacioli’s *Summa* | Abacus-school commercial arithmetic |
| 1503–1512 | Reisch’s abacist/algorist image | Documented but deliberately anachronistic |
| 1543 | Recorde’s *Grounde of Artes* | Counter and written methods |
| 1591 | Oldest provenance-dated Japanese soroban | Reported extant artefact |
| 1592 | Cheng Dawei’s *Suanfa tongzong* | Secure major suanpan manual |
| 1622 | Mōri’s *Warizan-sho* | Oldest surviving Japanese abacus book |
| 1627 | Yoshida’s *Jinkōki* | Mass diffusion in Japan |
| 1634 | Peiresc records Autun-attributed bronze | Secure modern documentary provenance |
| 18th c. | Familiar schoty form | Scholarly reconstruction from Russian evidence |
| late 19th c. | 1:4 soroban appears | Documented Japanese development |
| 1928 | Major Japanese proficiency tests begin | Institutional record |
| 1938 | Four-bead soroban prescribed for schools | Institutional record |
| Nov. 1946 | Matsuzaki defeats Wood’s calculator 4–1 | Documented; day disputed |
| 1984 | Stigler’s mental-abacus study | Experimental evidence |
| 2013 | Chinese zhusuan inscribed by UNESCO | Documented heritage action |
| Present | Educational, competitive, mental, museum, and limited practical use | Documented continuation |

---

## 10. Sources and editions consulted

### Standard surveys

- Stephen Chrisomalis, *Numerical Notation: A Comparative History* (Cambridge University Press, 2010):  
  https://doi.org/10.1017/CBO9780511676062
- Karl Menninger, *Number Words and Number Symbols: A Cultural History of Numbers*, trans. Paul Broneer (MIT Press, 1969):  
  https://archive.org/details/numberwordsnumbe00menn  
  https://openlibrary.org/books/OL5612154M/Number_words_and_number_symbols
- Jean-Claude Martzloff, *A History of Chinese Mathematics*, trans. Stephen S. Wilson, 2nd ed. (Springer, 2006):  
  https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Martzloff%20-%20A%20history%20of%20chinese%20mathematics.pdf  
  https://books.google.fr/books/about/A_History_of_Chinese_Mathematics.html?id=ACK1jreKgCoC
- Joseph Needham, with Wang Ling, *Science and Civilisation in China*, vol. 3, *Mathematics and the Sciences of the Heavens and the Earth* (Cambridge University Press, 1959).
- Georges Ifrah, *The Universal History of Numbers*, trans. David Bellos et al. (Wiley, 2000).
- Serafina Cuomo, *Ancient Mathematics* (Routledge, 2001):  
  https://www.nzdr.ru/data/media/biblio/kolxoz/M/Cuomo%20S.%20Ancient%20mathematics%20%28Routledge%2C%202001%29%28ISBN%20041516494X%29%28O%29%28303s%29_M_.pdf
- MacTutor, “Chinese Numerals”:  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Chinese_numerals/

### Salamis and the ancient Mediterranean

- Computer History Museum, Salamis tablet, Epigraphical Museum EM 11515:  
  https://www.computerhistory.org/revolution/artifact/1/128
- *Encyclopaedia of Greek Education* paper containing dimensions and historiography:  
  https://www.pee.gr/wp-content/uploads/eRA8_1-481.pdf
- William Smith, *A Dictionary of Greek and Roman Antiquities*, “Abacus”:  
  https://en.wikisource.org/wiki/A_Dictionary_of_Greek_and_Roman_Antiquities/Abacus
- Daremberg and Saglio, *Dictionnaire des antiquités grecques et romaines*, “Abacus”:  
  https://fr.wikisource.org/wiki/Dictionnaire_des_antiquit%C3%A9s_grecques_et_romaines/ABACUS
- Schreiber and Anderson, *Atlas of Classical Antiquities* (1895):  
  https://digi.ub.uni-heidelberg.de/diglit/schreiber1895/0188?ui_lang=eng
- Museo Galileo, “Portable Counter Abacus,” Museo Nazionale Romano inv. 65054:  
  https://exhibits.museogalileo.it/archimedes/object/PortableCounterAbacus.html
- BnF, “Abaque à boutons mobiles,” bronze.1925:  
  https://medaillesetantiques.bnf.fr/ws/catalogue/app/collection/record/3184
- Babelon and Blanchet, *Catalogue des Bronzes Antiques de la Bibliothèque nationale* (1895):  
  https://upload.wikimedia.org/wikipedia/commons/9/9e/Catalogue_des_bronzes_antiques_de_la_Biblioth%C3%A8que_nationale_%28IA_cataloguedesbron00bibl_0%29.pdf
- Science Museum Group, modern Roman-abacus replicas, object 1974-487:  
  https://collection.sciencemuseumgroup.org.uk/objects/co59965
- Peeters, study of Roman financial calculation and decimal/duodecimal fractions:  
  https://poj.peeters-leuven.be/content.php?id=3285199&url=article
- German *Realencyclopädie* entry, “Abacus”:  
  https://de.wikisource.org/wiki/RE%3AAbacus_9
- Louvre Collections search result illustrating the architectural, not calculating, sense of *abacus*:  
  https://collections.louvre.fr/en/ark:/53355/cl010253799

### Medieval and Renaissance Europe

- Richard fitzNigel, *Dialogus de Scaccario*, text/translation:  
  https://amesfoundation.law.harvard.edu/lhsemelh/materials/Exchequer.pdf
- Emilie Amt and S. D. Church, eds., *Dialogus de Scaccario and Constitutio Domus Regis* (Oxford Medieval Texts, 2007), publisher preview:  
  https://api.pageplace.de/preview/DT0400.9780191569036_A37045331/preview-9780191569036_A37045331.pdf
- “The Exchequer Cloth, c. 1176–1832,” Cambridge/Boydell entry:  
  https://www.cambridge.org/core/books/abs/english-and-their-legacy-9001200/exchequer-cloth-c-11761832-the-calculator-the-game-of-chess-and-the-process-of-photozincography/3B6D88DC7879B1BD80A712B8D5CF2342
- American Numismatic Society Digital Library, “Computing Jetons”:  
  https://numismatics.org/digitallibrary/ark%3A/53695/nnan19038
- Proceedings of the Society of Antiquaries of Scotland, study discussing Recorde and counting boards:  
  https://journals.socantscot.org/index.php/psas/article/download/9477/9444/9429
- “Jetons: Their Use and History”:  
  https://www.chicagocoinclub.org/projects/PiN/juh.html
- ETH Library, “Dispute between abacists and algorists”:  
  https://library.ethz.ch/en/sammlungen-und-archive/platforms/virtual-exhibitions/fibonacci-un-ponte-sul-mediterraneo/fibonaccis-significance-for-the-present-day/dispute-between-abacists-and-algorists.html
- ETH Library, German version:  
  https://library.ethz.ch/sammlungen-und-archive/online-zugaenge/virtuelle-ausstellungen/fibonacci-un-ponte-sul-mediterraneo/bedeutung-fibonaccis-fuer-die-gegenwart/streit-zwischen-abakisten-und-algoristen.html

### China and counting rods

- Martzloff, *A History of Chinese Mathematics*:  
  https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Martzloff%20-%20A%20history%20of%20chinese%20mathematics.pdf
- “The Interplay between Textual Procedures and Material Operations,” *Science in Context*:  
  https://www.cambridge.org/core/journals/science-in-context/article/interplay-between-textual-procedures-and-material-operations-from-the-viewpoint-of-chinese-mathematical-texts/7E654BC8863452F26F2E0C43892699F4
- Treccani, Chinese mathematics from Qin–Han to Tang, including the counting-board dispute:  
  https://www.treccani.it/enciclopedia/la-scienza-in-cina-dai-qin-han-ai-tang-la-matematica_%28Storia-della-Scienza%29/
- MacTutor, Chinese numerals and abacus:  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Chinese_numerals/
- Tsinghua University Science Museum, Chinese abacus:  
  https://tsm.tsinghua.edu.cn/?p=2769
- University of Queensland Physics Museum, Chinese 2:5 abacus:  
  https://physicsmuseum.uq.edu.au/chinese-abacus
- Study discussing Wylie, rods, and Martzloff’s late dating:  
  https://hub.hku.hk/bitstream/10722/177469/1/Content.pdf
- Study of later written zero and rod notation:  
  https://doi.org/10.1163/22105018-02602003

### Japan and soroban

- Japan Chamber of Commerce and Industry/Japan Abacus Association, “History of the Soroban”:  
  https://www.shuzan.jp/english/history/
- Japan Abacus Association, instrument description:  
  https://www.shuzan.jp/english/
- National Federation of Abacus Education, historical chronology:  
  https://www.soroban.or.jp/howto/arekore/history/
- National Federation, Japanese Abacus Museum:  
  https://www.soroban.or.jp/howto/arekore/museum/
- Japanese Abacus Museum, evolution of bead counts and 1938 standard:  
  https://soroban-museum.note.jp/n/n11be82a513a4
- MAA, “Soroban Arithmetic in Edo Period Japan”:  
  https://old.maa.org/sites/default/files/images/upload_library/46/Hosking-abacus/Convergence_TaiseiSankei.pdf
- Japanese Abacus Museum, 1946 contest:  
  https://soroban-museum.note.jp/n/n0ab5b78d8796
- Takashi Kojima, *The Japanese Abacus: Its Use and Theory*; contest excerpt:  
  https://www.ee.torontomu.ca/~elf/abacus/abacus-contest.html
- Computer History Museum, 1946 contest summary:  
  https://computerhistory.org/wp-content/uploads/2019/08/2011_Core.pdf

### Russia

- Viatcheslav Sokolov, Svetlana Karelskaia, and Ekaterina Zuga, “The schoty (abacus) as the phenomenon of Russian accounting,” *Accounting History* 28.1 (2023):  
  https://journals.sagepub.com/doi/10.1177/10323732221132005
- EBSCO bibliographical abstract of the same article:  
  https://www.ebsco.com/articles/mathematics/a271598f-9fc7-5e9a-bf85-427e5b83ece2/the-schoty-abacus-as-the-phenomenon-of-russian-accounting/
- “Pedagogical value of the Russian abacus,” noting the discontinuity between seventeenth- and eighteenth-century forms:  
  https://opinvisindi.is/bitstreams/410fd28a-1cf1-45fe-a2ee-c39745374749/download
- Aleksey Volkov, “On the Chinese origin of the Russian computing device ‘schyoty’”:  
  https://www.mathnet.ru/php/seminars.phtml?option_lang=eng&presentid=48907
- Mark A. Tsayger-related material, “Arithmetic in Sixteenth-Century Muscovy”:  
  https://ircps.org/wp-content/uploads/2021/04/2012-21_Weiss.pdf

### Mental abacus

- James W. Stigler, “‘Mental abacus’: The effect of abacus training on Chinese children’s mental calculation,” *Cognitive Psychology* 16.2 (1984), 145–176:  
  https://doi.org/10.1016/0010-0285(84)90006-9  
  https://www.sciencedirect.com/science/article/pii/0010028584900069
- Takashi Hanakawa et al., “Neural correlates underlying mental calculation in abacus experts,” *NeuroImage* (2003):  
  https://doi.org/10.1016/S1053-8119(03)00050-8  
  https://www.sciencedirect.com/science/article/pii/S1053811903000508

### Mesoamerica and contested *nepohualtzintzin*

- David Esparza Hidalgo, *Cómputo azteca* (the principal modern popularizing source; bibliographic availability varies).
- Barbara J. Williams and María del Carmen Jorge y Jorge, “Aztec arithmetic revisited: land-area algorithms and Acolhua congruence arithmetic,” *Science* 320 (2008):  
  https://doi.org/10.1126/science.1153976  
  https://pubmed.ncbi.nlm.nih.gov/18388287/
- Smithsonian/Bureau of American Ethnology, *Numeral Systems of Mexico and Central America*:  
  https://repository.si.edu/bitstream/handle/10088/91700/Numeral%20Systems%20of%20Mexico%20and%20Central%20America.pdf
- Critical German discussion of the modern reconstruction:  
  https://www.telepolis.de/article/Ethnomathematik-Die-Farce-um-den-aztekischen-Abakus-10443879.html?seite=all

### Etymology

- Online Etymology Dictionary, “abacus”:  
  https://www.etymonline.com/word/abacus
- Online Etymology Dictionary, “calculator”:  
  https://www.etymonline.com/word/calculator
- American Heritage Dictionary, “abacus”:  
  https://www.ahdictionary.com/word/search.html?q=abacus
- Académie française, “abaque”:  
  https://dictionnaire-academie.fr/article/B0A0016
- CNRTL, “abax”:  
  https://www.cnrtl.fr/etymologie/abax

### Collection records

- BnF bronze.1925:  
  https://medaillesetantiques.bnf.fr/ws/catalogue/app/collection/record/3184
- Museo Nazionale Romano inv. 65054 via Museo Galileo:  
  https://exhibits.museogalileo.it/archimedes/object/PortableCounterAbacus.html
- British Museum Chinese wooden abacus As.3593:  
  https://www.britishmuseum.org/collection/object/A_As-3593
- Science Museum replica Roman abaci, 1974-487:  
  https://collection.sciencemuseumgroup.org.uk/objects/co59965
- Epigraphical Museum EM 11515 via Computer History Museum:  
  https://www.computerhistory.org/revolution/artifact/1/128
