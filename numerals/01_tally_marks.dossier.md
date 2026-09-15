# Tally marks and counting bones: Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| **Name** | Tally marks; tally notation; notched tallies; counting or marked bones |
| **Base** | Strictly **unary**, not “base 1” in the ordinary positional sense. Regrouped tallies commonly use bundles of 5, 10, 20, or locally defined units. |
| **Type** | In its elementary form, **cumulative-additive and non-positional**: each stroke contributes one. Grouped tallies remain additive. Systems in which differently shaped or sized notches represent £1, £20, £100, and so forth are **mixed sign-value/additive systems**. |
| **Signs** | A stroke, scratch, nick, notch, bead, pebble, knot, or designated body point for one counted item. Western fence tally: `||||` followed by a crossing fifth stroke, Unicode `𝍷` (one) and `𝍸` (five). East Asian five-stroke tally: progressive strokes forming `正`, Unicode `𝍲 𝍳 𝍴 𝍵 𝍶`. |
| **Zero** | Normally represented by **no mark** or an empty tallying area, not by a written zero sign. In tabulation, a blank may be ambiguous between zero, “not counted,” and missing data; a later numeral or explicit word may therefore be supplied. |
| **Fractions** | No inherent general notation. Fractions can be represented by specially defined notches, subdivisions, half-notches, or units such as halfpennies and farthings. The English Exchequer used conventional cuts for denominations and could halve certain large-value cuts. |
| **Period** | Possible prehistoric examples from more than 40,000 years ago; securely interpretable historical examples from antiquity onward; still used in the present. |
| **Region** | Potentially worldwide and independently reinvented. Tallying is a procedure, not a single genealogical script tradition. |
| **Capacity** | Formally unbounded if material and time are unlimited; practically restricted by the available surface, the reader’s ability to distinguish marks, and the grouping convention. |
| **Language** | Language-independent at the elementary level. Spoken number words, labels, and contextual inscriptions may identify what is counted. |

### Evidentiary labels used below

- **[ARTEFACT]**: an extant object whose material features can be inspected.
- **[DOCUMENTED TEXT]**: a statement in a surviving historical text, law, account, or manuscript.
- **[OBSERVED PRACTICE]**: ethnographically or administratively recorded use.
- **[SCHOLARLY RECONSTRUCTION]**: a reasoned interpretation extending beyond what the object or text states.
- **[DISPUTED]**: a claim for which specialists have offered materially different readings.
- **[TRADITION]**: a community or later historical account not independently demonstrated by contemporary evidence.
- **[LEGEND]**: a narrative circulated as history without adequate supporting evidence.
- **[MODERN INVENTION]**: a recent convention, encoding, graphic, or retrospective reconstruction.

## The system in detail

### 1. The elementary principle

A tally establishes one-to-one correspondence:

> one encountered object or event → one deliberately added mark

If thirteen sheep pass through a gate, the recorder makes thirteen strokes. The notation need not name “thirteen”; its meaning lies in the correspondence between strokes and sheep.

**[SCHOLARLY RECONSTRUCTION]** Cognitive and historical accounts often call tallying an elementary bridge between recognizing a collection and assigning it an abstract number. It externalizes memory: the final array persists after the sheep, days, votes, debts, or blows have passed. That does not establish that every prehistoric line series was numerical. Chrisomalis treats unstructured tallies as an evident precursor to several cumulative-additive notations, while carefully separating numeral notation from spoken number systems and full writing. His comparative framework is preferable to a universal evolutionary ladder in which every civilization must pass through identical stages. [Chrisomalis, *Numerical Notation*, introduction](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/90BCD7A80F84CBEF195F02D36511F4E7/9780511676062c1_p1-33_CBO.pdf/introduction.pdf)

A plain tally has:

- one sign-value: `| = 1`;
- addition by concatenation;
- no place value;
- no multiplication sign;
- no obligatory direction;
- no separate negative numbers;
- no inherent radix point or fraction bar;
- no intrinsic vocabulary;
- no largest representable integer.

Calling it “base 1” is useful in computer science, where unary encoding represents \(n\) by \(n\) identical symbols, but mathematically it is not a positional radix system: ordinary base-\(b\) place values are \(b^0,b^1,b^2,\ldots\), whereas \(1^k\) never distinguishes places. **“Unary cumulative notation” is therefore the less misleading description.**

### 2. Western or fence tally

The common modern Western convention writes four more-or-less parallel strokes, then crosses them with a fifth:

```text
1  |
2  ||
3  |||
4  ||||
5  ||||̸
```

In words, five resembles a four-bar fence crossed by a diagonal gate. In Unicode, the encoded atomic characters are:

- `𝍷` — U+1D377 TALLY MARK ONE
- `𝍸` — U+1D378 TALLY MARK FIVE

Unicode calls these “Western tally marks” or “fence tally marks.” Two, three, and four are sequences of U+1D377 rather than separate characters. The characters were approved after proposals in 2015–2017 and entered Unicode 11.0 in 2018; they are **modern digital encodings**, not evidence that historical talliers treated a group of five as an indivisible written glyph. [Unicode names list](https://www.unicode.org/charts/nameslist/n_1D360.html), [Unicode chart](https://www.unicode.org/charts/PDF/U1D360.pdf), [UTC recommendation](https://www.unicode.org/L2/L2016/16156-script-recs.pdf)

**[OPEN QUESTION]** No reliable early attestation for the exact four-verticals-plus-diagonal “five-barred gate” convention emerged from the consulted scholarship. Modern accounts frequently illustrate it without tracing its first manuscript or dated object. Its practical value is evident—groups of five can be recognized rapidly—but an ancient or prehistoric origin is unproved.

### 3. East Asian `正` tally

In China and other parts of the Sinographic cultural sphere, a five-count is made by adding the five conventional strokes of `正` (“correct,” “upright,” “main”):

```text
1  𝍲
2  𝍳
3  𝍴
4  𝍵
5  𝍶   → completed form 正
```

Unicode assigns:

- `𝍲` U+1D372 IDEOGRAPHIC TALLY MARK ONE
- `𝍳` U+1D373 IDEOGRAPHIC TALLY MARK TWO
- `𝍴` U+1D374 IDEOGRAPHIC TALLY MARK THREE
- `𝍵` U+1D375 IDEOGRAPHIC TALLY MARK FOUR
- `𝍶` U+1D376 IDEOGRAPHIC TALLY MARK FIVE

**[OBSERVED PRACTICE]** The convention is used in Chinese-speaking settings and is familiar in Japan and Korea. The character’s lexical meaning is not “five”; its usefulness comes from having five clear strokes in a fixed order. Unicode explicitly cross-references the completed tally to U+6B63 `正`. [Unicode names list](https://www.unicode.org/charts/nameslist/n_1D360.html)

**[DISPUTED/UNVERIFIED ORIGIN]** Online stories derive the practice from five-person seating groups in old Shanghai theatres, or say that Japan formerly used `玉`. The searches located repetition of these stories but no dated theatre register, manual, or contemporaneous source. They should be retained as folklore, not presented as established origin history.

### 4. Worked table: 1–20

Because font support for the Unicode tally symbols is uneven, both literal strokes and Unicode notation are supplied.

| Number | Western strokes | Unicode composition | Grouped reading |
|---:|---|---|---|
| 1 | `|` | `𝍷` | one |
| 2 | `||` | `𝍷𝍷` | two |
| 3 | `|||` | `𝍷𝍷𝍷` | three |
| 4 | `||||` | `𝍷𝍷𝍷𝍷` | four |
| 5 | `||||̸` | `𝍸` | one five |
| 6 | `||||̸ |` | `𝍸𝍷` | five plus one |
| 7 | `||||̸ ||` | `𝍸𝍷𝍷` | five plus two |
| 8 | `||||̸ |||` | `𝍸𝍷𝍷𝍷` | five plus three |
| 9 | `||||̸ ||||` | `𝍸𝍷𝍷𝍷𝍷` | five plus four |
| 10 | `||||̸ ||||̸` | `𝍸𝍸` | two fives |
| 11 | `||||̸ ||||̸ |` | `𝍸𝍸𝍷` | ten plus one |
| 12 | `||||̸ ||||̸ ||` | `𝍸𝍸𝍷𝍷` | ten plus two |
| 13 | `||||̸ ||||̸ |||` | `𝍸𝍸𝍷𝍷𝍷` | ten plus three |
| 14 | `||||̸ ||||̸ ||||` | `𝍸𝍸𝍷𝍷𝍷𝍷` | ten plus four |
| 15 | `||||̸ ||||̸ ||||̸` | `𝍸𝍸𝍸` | three fives |
| 16 | `||||̸ ||||̸ ||||̸ |` | `𝍸𝍸𝍸𝍷` | fifteen plus one |
| 17 | `||||̸ ||||̸ ||||̸ ||` | `𝍸𝍸𝍸𝍷𝍷` | fifteen plus two |
| 18 | `||||̸ ||||̸ ||||̸ |||` | `𝍸𝍸𝍸𝍷𝍷𝍷` | fifteen plus three |
| 19 | `||||̸ ||||̸ ||||̸ ||||` | `𝍸𝍸𝍸𝍷𝍷𝍷𝍷` | fifteen plus four |
| 20 | `||||̸ ||||̸ ||||̸ ||||̸` | `𝍸𝍸𝍸𝍸` | four fives; one score |

The line crossing in the plain-text column is only an approximation. `𝍸` is the standardized character.

### 5. Tens, hundreds, and thousands

In an uncompacted unary tally, every unit is still written:

| Value | Exact tally principle | Compact display used here |
|---:|---|---|
| 10 | ten strokes | `𝍸𝍸` |
| 20 | twenty strokes | `𝍸𝍸𝍸𝍸` |
| 30 | thirty strokes | `𝍸 × 6` |
| 40 | forty strokes | `𝍸 × 8` |
| 50 | fifty strokes | `𝍸 × 10` |
| 60 | sixty strokes | `𝍸 × 12` |
| 70 | seventy strokes | `𝍸 × 14` |
| 80 | eighty strokes | `𝍸 × 16` |
| 90 | ninety strokes | `𝍸 × 18` |
| 100 | one hundred strokes | `𝍸 × 20` |
| 1,000 | one thousand strokes | `𝍸 × 200` |
| 10,000 | ten thousand strokes | `𝍸 × 2,000` |

`× 20`, commas, and the Arabic numerals in the compact column are editorial abbreviations, **not tally signs**. A literal tally for 1,000 contains 1,000 unit strokes or 200 drawn five-groups.

This illustrates why talliers introduce:

- visible spacing after a group;
- a crossing fifth stroke;
- a longer fifth, tenth, twentieth, or hundredth notch;
- counters or pebbles for completed groups;
- separate columns;
- notches of different shapes or widths;
- labels written in another numeral system.

Those devices improve readability but can transform a pure unary tally into a mixed notation.

### 6. Ordering, ligatures, and abbreviations

A tally’s numerical value normally does not depend on left-to-right versus right-to-left order. Sequence can nevertheless matter for its use: successive days, deliveries, debts, or kills may be appended in chronological order.

The crossed fifth stroke is best described as **group punctuation or bundling**. Unicode’s U+1D378 treats the complete five-group as a character for interchange, but historically it need not be a ligature in the paleographic sense.

Common abbreviations include:

- crossing each fourth stroke to make five;
- a longer stroke for 5, 10, 20, or 100;
- a pebble for each completed score;
- notches of different widths for different denominations;
- moving completed groups to a separate register;
- writing a conventional numeral beside the tally total.

The Pitt Rivers Museum records a South Downs sheep tally in which ordinary sheep were notched on bark, a pebble stored inside represented each completed score of twenty, and each fifth score—100 sheep—received a specially extended notch. That is a documented mixed material grouping system, not merely a classroom reconstruction. [Pitt Rivers/Edward Lovett collection](https://england.prm.ox.ac.uk/englishness-Edward-Lovett.html)

### 7. Zero, fractions, and negative quantities

#### Zero

A pristine tally begins blank. That blank may be read as zero only if the tallying frame is known to exist and the counting procedure has begun. There is no elementary “zero mark.”

**[IMPORTANT QUALIFICATION]** “Tallies have no zero” is true only of the elementary sign inventory. A tally user can:

- say or write a word meaning “none”;
- enter `0` from another notation;
- reserve an empty labeled row for zero;
- use a cancellation mark;
- compare additions and removals on opposite sides.

Thus tallying does not imply ignorance of zero as a quantity. It lacks a native zero *glyph* and has no positional empty place requiring a placeholder.

#### Fractions

Pure unit tallies work most naturally for discrete items. Fractions require a defined unit or a new convention. A half loaf might be tallied as one half-unit rather than as “½” internally.

The late-twelfth-century *Dialogus de Scaccario* describes half-value variants of large Exchequer cuts: a half-thousand could be made with a cut of the thousand’s length but removing only half the wood, and analogous treatment applied when the relevant higher denomination was absent. It also distinguished pounds, shillings, pence, gold, and silver by size, placement, and shape. This is a **documented specialist fraction/denomination notation**, not a universal property of tallies. [Church and Harvey edition preview](https://dokumen.pub/dialogus-de-scaccario-and-constitutio-domus-regis-the-dialogue-of-the-exchequer-and-the-disposition-of-the-kings-household-0199258619-9780199258611.html)

#### Negative numbers

There is no inherent negative sign. A counter-tally, crossed-out mark, removed counter, separate debit column, or verbal designation can distinguish debts from payments. The physical system records magnitudes whose economic sign is provided by context.

### 8. Famous numbers written as tallies

#### Lebombo: 29 surviving incisions

```text
𝍸𝍸𝍸𝍸𝍸 𝍷𝍷𝍷𝍷
```

This is a modern normalized transcription of “29,” not a facsimile of the bone. The original incisions differ in form and the bone is broken, so 29 is the surviving count, not necessarily the original total.

#### Ishango left/G column: 11, 13, 17, 19

```text
11  𝍸𝍸𝍷
13  𝍸𝍸𝍷𝍷𝍷
17  𝍸𝍸𝍸𝍷𝍷
19  𝍸𝍸𝍸𝍷𝍷𝍷𝍷
```

These equal the primes between 10 and 20, but whether the maker selected them *because they were prime* is disputed.

#### Ishango totals: 60, 48, 60

```text
60 = 𝍸 × 12
48 = 𝍸 × 9 + 𝍷𝍷𝍷
60 = 𝍸 × 12
```

Again these are normalized computations from counted incision groups, not original glyph strings.

#### The Parliament fire: 1,834

A literal Western tally would contain 366 five-groups plus four strokes:

```text
1834 = (𝍸 × 366) + 𝍷𝍷𝍷𝍷
```

The number is famous in tally history because obsolete Exchequer tallies burned on 16 October 1834 ignited the Palace of Westminster.

## Origins: what survives, what it proves, and what it does not

### 1. Before recognizable tallies

Humans made incisions, perforations, repeated strokes, ochre cross-hatching, and patterned marks long before writing. Determining which were numerical is exceptionally difficult.

**[ARTEFACT]** Engraved ochres from Blombos Cave in South Africa are far older than the usual tally bones and contain deliberate geometric patterns.  
**[DISPUTED]** They have sometimes been called “tallies,” but specialist analyses emphasize that individual signs cannot presently be assigned stable numerical values. The marks may be symbolic, decorative, procedural, or products of repeated gestures. Calling them the earliest recorded counting is unsupported by contextual evidence. [Henshilwood et al. discussion](https://www.researchgate.net/publication/26257796_Engraved_Ochres_from_the_Middle_Stone_Age_Levels_at_Blombos_Cave_South_Africa), [Malafouris on mark-making](https://pmc.ncbi.nlm.nih.gov/articles/PMC7889684/)

**Finding:** the earliest intentional marks are not automatically the earliest numbers.

### 2. The “Lebombo bone”

#### Object and context

**[ARTEFACT]** The object commonly called the Lebombo bone is a short fragment of baboon fibula bearing 29 incisions. Peter Beaumont’s excavations recovered it in 1970–71 from Border Cave, on the present South Africa–Eswatini border in the Lebombo Mountains.

It is not, despite frequent wording, from a separate “Lebombo Cave.” “Lebombo” names the mountain region; the archaeological locality is Border Cave.

The artefact’s precise museum accession number was not located in a publicly searchable collection catalogue during this research. That absence matters: many popular accounts repeat its description without linking to a custodial record.

#### Date

**[SCHOLARLY RECONSTRUCTION]** Popular dates range from roughly 35,000 to 44,000 BP; the item-specific brief’s “c. 42,000 BP” reflects the commonly cited modern age assigned through its archaeological layer. The bone itself has not yielded a direct radiocarbon date in the sources consulted. The date is contextual and depends on the stratigraphic attribution and chronology of Border Cave.

Peter Beaumont’s 1980 study documents the 1970–75 excavations and the site’s dating problems. A later Beaumont and Robert Bednarik paper describes a 3.8 cm marked baboon fibula found in 1970–71. [Beaumont, “On the Age and Context of the Border Cave Skeletons”](https://files01.core.ac.uk/download/pdf/39674913.pdf), [Beaumont and Bednarik 2013](https://www.ifrao.com/wp-content/uploads/2014/08/30-1-BeaumontBed.pdf)

#### Reading

- **[ARTEFACT]** Twenty-nine surviving incisions are visible.
- **[SCHOLARLY RECONSTRUCTION]** The marks were deliberately accumulated over time and functioned as a tally.
- **[DISPUTED]** Twenty-nine represents days in a lunar synodic month.
- **[TRADITION/MODERN CULTURAL CLAIM]** A woman made it to track menstruation and women were therefore the first mathematicians.
- **[UNSUPPORTED]** It demonstrates arithmetic, a calendar science, or a defined base.

The lunar reading is numerically attractive because a lunation lasts about 29.5 days. Against it:

1. the object is broken, so 29 may not be the complete intended series;
2. no marks securely identify lunar phases;
3. there is no repeated month or independent key;
4. any count of 29 items can be retrospectively mapped to a lunar month.

A recent archaeological discussion states explicitly that there are no physical signs establishing calendar use. [Cambridge Archaeological Journal, “The Beginning of Time”](https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/beginning-of-time/B7DDE9AC9E3BEC0027FF453046846D31)

The strongest defensible formulation is:

> **A deliberately notched bone fragment survives from a very early Border Cave context; it may be a count, but neither what was counted nor whether 29 was the finished total is known.**

### 3. The Dolní Věstonice “wolf bone”

**[ARTEFACT]** A wolf bone with roughly 55–57 incisions was found in 1937 by the excavation team of Karel Absolon at Dolní Věstonice, Moravia, in the present Czech Republic. It belongs to the Upper Palaeolithic/Gravettian archaeological complex, approximately 30,000 years ago.

**[DISPUTED]** It is regularly called a tally or counting stick. The intentional marks are real; a numerical interpretation is plausible but not demonstrated by an accompanying label or repeated operational context. Published popular totals vary between 55 and 57, another warning that diagrams and damage histories must be checked against the original object. [Australian Museum on Dolní Věstonice](https://australian.museum/learn/cultures/international-collection/dolni-vstonice-archaeological-site/), [Smithsonian incised bone record](https://humanorigins.si.edu/evidence/behavior/art-music/other-decorated-objects/geometric-incised-bone-rectangle)

It cannot simply be placed “after” the Lebombo bone with single-year precision because both ages are archaeological ranges and the functional reading of each is uncertain.

### 4. The Ishango bone

#### Discovery and custody

**[ARTEFACT]** In 1950 Belgian geologist Jean de Heinzelin de Braucourt, working for the Royal Belgian Institute of Natural Sciences, directed excavations at Ishango on the Congolese shore of Lake Edward, near the Semliki River in the present Democratic Republic of the Congo. A small, dark, mineralized bone handle—often described as bearing a quartz point at one end—carries 168 incisions arranged in three longitudinal columns.

The object is held by the Institute of Natural Sciences in Brussels. Its public institutional pages identify the excavation and custody, but the searched public record did not supply a normal accession or inventory number. [Institute exhibition record](https://www.naturalsciences.be/en/museum/exhibitions-activities/exhibitions/250-years-of-natural-sciences/the-ishango-bone), [Institute dossier](https://www.naturalsciences.be/file/cc73d96153bbd5448a56f19d925d05b1379c7f21/369895724a871d793f603e27d8e31fae74fdbf13/inst-202403-brochure-ishango-en-fv.pdf?name=inst_202403_brochure_ishango_en_fv.pdf&type=application%2Fpdf)

De Heinzelin published the excavation in *Les fouilles d’Ishango* in 1957 and presented the mathematical interpretation to a broad audience in “Ishango,” *Scientific American* 206.6 (June 1962), pp. 105–116. These are the first influential readings, not oral explanations preserved from the makers. [Bibliographic record for the 1957 report](https://books.google.com/books/about/Les_fouilles_d_Ishango.html?id=o35DqYKR440C)

#### Date

De Heinzelin initially assigned the site to approximately 8,500–11,000 BP through its archaeological industry. Later work substantially changed that estimate.

**[SCHOLARLY RECONSTRUCTION]** Modern dating places the principal occupation deposits broadly around 20,000–26,000 calibrated years BP. Five mollusc-shell dates fall between 19,540 and 24,145 BP, but lake and volcanic “old carbon” complicate shell dates. An ostrich-eggshell fragment, whose carbon derived from terrestrial diet, produced approximately 25,570 ± 350 cal BP and supported a Late Pleistocene attribution. The carved bone itself is mineralized and lacks organic matter suitable for a simple direct radiocarbon result. [Crévecoeur et al., 2016](https://www.sciencedirect.com/science/article/abs/pii/S0047248416300057), [Institute stratigraphy page](https://ishango.naturalsciences.be/en/en-ishango-13.html)

Thus “c. 20,000 BP” is a useful rounded description, not a direct date stamped on the artefact.

#### The marks

De Heinzelin labeled the columns G (*gauche*, left), M (*milieu*, middle), and D (*droite*, right). Normalized group counts are:

| Column | Groups | Sum |
|---|---|---:|
| G | 11, 13, 17, 19 | 60 |
| M | 3, 6, 4, 8, 9 or 10, 5, 5, 7 | approximately 48 |
| D | 11, 21, 19, 9 | 60 |

Damage makes at least one group count uncertain. The Institute’s reconstruction gives a total of 168 lines. [Institute brochure](https://www.naturalsciences.be/file/cc73d96153bbd5448a56f19d925d05b1379c7f21/369895724a871d793f603e27d8e31fae74fdbf13/inst-202403-brochure-ishango-en-fv.pdf?name=inst_202403_brochure_ishango_en_fv.pdf&type=application%2Fpdf)

#### Competing readings

1. **Arithmetic or “prime-number table” — [DISPUTED].**  
   De Heinzelin observed that 11, 13, 17, and 19 are precisely the primes between 10 and 20; that 11, 21, 19, and 9 can be read as \(10+1, 20+1, 20-1, 10-1\); and that early middle groups appear paired as 3/6 and 4/8. This reading first appears in his work of the 1950s and was popularized in 1962.

   Evidence for it is the pattern itself. Evidence against treating it as proof is the absence of an explanatory text, repeated table, operations, divisibility sign, or independent example. Four retrospectively selected numbers provide a small statistical sample.

2. **Lunar calendar — [DISPUTED].**  
   Alexander Marshack, especially in *The Roots of Civilization* (1972), used microscopic study of incision sequences to argue for accumulated lunar notation rather than a static arithmetic table.

   Francesco d’Errico criticized many Palaeolithic lunar-calendar readings as insufficiently testable pattern matching. His 1989 title, “Palaeolithic Lunar Calendars: A Case of Wishful Thinking?”, captures the methodological objection. [d’Errico 1989](https://www.journals.uchicago.edu/doi/pdf/10.1086/203721)

3. **Base 12, sub-bases 3 and 4, or calculation aid — [DISPUTED].**  
   Vladimir Pletser and Dirk Huylebrouck stress that the outer columns total 60 and the middle one 48, all multiples of 12, and propose a duodecimal manipulation device or “slide-rule” interpretation. They concede that the bone is insufficient to demonstrate prime-number theory. [Pletser and Huylebrouck](https://arxiv.org/abs/1204.1019)

4. **Menstrual record made by a woman — [TRADITION/ADVOCACY; UNPROVED].**  
   Claudia Zaslavsky linked lunar recording with women’s menstrual observation and popularized the idea of women as the first mathematicians. It is historically important as an intervention against narratives that erase African and female intellectual agency. There is, however, no evidence identifying the carver’s sex or the counted phenomenon.

5. **Decorated handle, mnemonic object, or other notation — [OPEN].**  
   The artefact’s patterned arrangement is compatible with deliberate information storage, but the information may not map to modern categories such as “multiplication table” or “calendar.” The Institute itself notes that notched prehistoric objects are not rare and may have served various purposes. [Institute object-context page](https://ishango.naturalsciences.be/en/en-ishango-19.html)

The correct source-critical conclusion is not “the bone means nothing.” It is that deliberate grouping is documented while its semantic key is lost.

### 5. From notches to written numeral systems?

**[SCHOLARLY RECONSTRUCTION]** Repeated unit signs provide an obvious model for cumulative-additive numerals: Egyptian `||||`, early Chinese horizontal lines, and Roman `I` all resemble tallying. Chrisomalis notes that independently invented notations frequently begin cumulatively, which is compatible with—but does not prove—descent from physical tallies.

There is no evidence for one primordial tally script spreading from Border Cave or Ishango to Egypt, Mesopotamia, China, India, or Rome. Similar marks can arise independently because a line is easy to incise and one mark per item is cognitively transparent.

#### Mesopotamian tokens

Denise Schmandt-Besserat argued that Near Eastern clay tokens used to account for goods developed into impressed numerical signs and ultimately writing. These tokens are materially different from bone tallies: they use differentiated shapes and commodity-specific conventions, and early Mesopotamian metrology combines several bases. They are relevant as a parallel route from correspondence accounting to notation, not demonstrated descendants of African counting bones.

Some details of Schmandt-Besserat’s universal developmental sequence have been challenged by later Assyriologists and archaeologists. Tallies, tokens, sealings, and written numerals should not be collapsed into a single invention.

#### Roman numerals

**[SCHOLARLY RECONSTRUCTION]** Menninger and many later histories compare Roman `I`, `V`, and `X` with shepherds’ notches: unit cuts, a special fifth cut, and a crossed tenth. Roman numerals, however, are historically related to Etruscan numeral signs. The transformation from notched sticks into the precise Etruscan/Roman inventory is reconstructed rather than directly documented.

**[LEGEND]** The familiar classroom tale that `V` is a hand with five fingers and `X` is two hands is an explanatory mnemonic, not a securely documented ancient derivation.

### 6. Antiquity: textual witnesses

Pliny the Elder’s *Natural History* (c. CE 77) discusses woods suitable for tallying, frequently cited as an early Roman textual witness. **[DOCUMENTED TEXT, INTERPRETIVE CONTEXT]** Pliny attests practical marked-stick technology, not a universal Roman numeral origin. [Computer History Museum synopsis and references](https://www.computerhistory.org/storageengine/roman-philosopher-pliny-describes-tally-sticks/)

Herodotus describes Darius I giving Ionians a knotted cord and instructing them to untie one knot per day. That is a countdown device rather than a written numeral system, but it uses the same one-to-one external-memory principle.

## Arithmetic and instruments

### 1. What arithmetic tallies support

Tallies make four operations physically transparent:

- **Addition:** concatenate two arrays.
- **Subtraction:** strike out, erase, break off, or pair and cancel marks.
- **Comparison:** align two arrays one-to-one; whichever has unmatched marks is larger.
- **Grouping/division:** partition marks into equal batches and inspect the remainder.
- **Multiplication:** repeat a group a fixed number of times.
- **Ratios:** compare group lengths, although no intrinsic fraction notation results.

A tally is especially effective for an **accumulating count**. It is poor for repeatedly copying, multiplying, or comparing very large numbers: the representation grows in direct proportion to the value.

### 2. Fingers and body reckoning

Fingers are transient tallies. Each raised or touched finger can represent one item; completed hands naturally encourage grouping by five or ten. This does not prove that every decimal spoken system originated from finger counting, though the anatomical motivation is strong.

#### New Guinea body-counting

**[OBSERVED PRACTICE]** Numerous New Guinea Highlands communities use ordered body points as a count list. The best-studied example is Oksapmin:

- counting begins at a thumb;
- proceeds along fingers, wrist, forearm, elbow, upper arm, shoulder, and head;
- reaches the opposite side;
- a normal pass contains 27 named positions;
- additional passes can extend the count.

Geoffrey Saxe’s fieldwork in 1980 and later work with Indigo Esmonde showed that traditional body counting was adapted to cash, shop transactions, and school arithmetic. A body-point system is not simply “base 27” in the strict positional sense: 27 is the length of the cycle, and repeated passes require contextual gestures or words. [Saxe project](https://culturecognition.com/new-page-3), [Saxe, *Cultural Development of Mathematical Ideas* excerpt](https://assets.cambridge.org/97805217/61666/excerpt/9780521761666_excerpt.pdf), [PNG overview](https://www.thenational.com.pg/number-systems-in-societies/)

This is a strong caution against the phrase “the base of all bases.” Elementary one-to-one correspondence underlies counting, but culturally elaborated tally systems do not all become decimal positional systems.

### 3. Counting boards and counters

A tally records successive events; a counting board allows counters to be moved between valued zones. The English Exchequer used a chequered cloth or table from which its name derives. Columns represented denominations—pence, shillings, pounds, scores of pounds, hundreds, and thousands.

**[DOCUMENTED TEXT]** The *Dialogus de Scaccario*, composed in the late twelfth century by Richard FitzNeal, explains the Exchequer’s personnel, board, accounting, and tally conventions. The checkerboard calculation and the wooden receipt were complementary:

```text
spoken/received amount
        ↓
counters arranged on the Exchequer board
        ↓
amount entered in rolls
        ↓
value cut into tally
        ↓
stock and foil used at audit
```

This is not positional written arithmetic in the Hindu-Arabic sense. Place-like valued columns exist on the board, while the permanent wooden record uses shaped sign-values. [Baxter, “Early Accounting: The Tally and Checkerboard”](https://egrove.olemiss.edu/aah_journal/vol16/iss2/2/)

### 4. The split tally as calculation and authentication

A split tally was cut across a stick and then cleaved lengthwise so that both halves carried the same notches and a unique grain and fracture boundary. Matching the halves verified that neither party had enlarged the record independently.

The terminology varied, but in the English Exchequer the longer creditor’s part was normally the **stock** and the retained counterpart the **foil** or counter-stock. Writing identifying the payer and transaction supplemented the cuts.

**[QUALIFICATION]** “Fraud-proof” is too absolute. A matching fracture strongly resists unilateral alteration, but it does not prevent collusion, substitution before splitting, destruction, dishonest witnessing, or abuse by the institution controlling enforcement.

### 5. English Exchequer notch values

The *Dialogus* gives the following hierarchy:

| Amount | Cut described in the medieval text |
|---:|---|
| £1,000 | incision about the width of a palm |
| £100 | about the width of a thumb |
| £20 | about the width of a little finger |
| £1 | about the width of a swollen barleycorn |
| 1 shilling | narrower notch made by two cuts removing wood |
| 1 penny | a cut removing no wood |
| smaller denominations | still smaller marks or points in later descriptions |
| gold | distinguished from silver by placement or a straight rather than slanting cut |

Large units occupied privileged parts or edges; lesser units went on another side. The result was additive but not unary: a palm-width cut represented £1,000, not one unspecified object. [Church and Harvey translation](https://dokumen.pub/dialogus-de-scaccario-and-constitutio-domus-regis-the-dialogue-of-the-exchequer-and-the-disposition-of-the-kings-household-0199258619-9780199258611.html), [Hampshire Museums example](https://collections.hampshireculture.org.uk/object/inscribed-wooden-tally-stick-13th-14th-century-preston-candover-hampshire)

The Science Museum preserves sixteen stocks dated approximately 1440 as object **1952-431**. [Science Museum Group catalogue](https://collection.sciencemuseumgroup.org.uk/objects/co60506/medieval-exchequer-tally-sticks)

The British Museum holds a woodcutter’s tally from Brandon, Suffolk, **1936,1213.1**, a baton-shaped wooden object with notches around its sides. It is occupational rather than an Exchequer tally. [British Museum catalogue](https://www.britishmuseum.org/collection/object/H_1936-1213-1)

A box of Exchequer tallies from 1296, found in the Chapel of the Pyx in Westminster Abbey in 1808, includes a tally naming William de Costello, sheriff of London. [MAA object study](https://old.maa.org/press/periodicals/convergence/mathematical-treasures-english-tally-sticks)

### 6. Shepherds’ tallies

**[OBSERVED PRACTICE]** Shepherds and rural producers used notched wood into the twentieth century. Edward Lovett recorded South Downs sheep tallies in which:

- each ordinary notch represented a sheep;
- a pebble inside a hollow container represented a completed score;
- the fifth score was distinguished to make a hundred;
- the shepherd could “tot up” a flock rapidly.

The Pitt Rivers object **1909.60.4** is a model of this system. [Pitt Rivers Museum](https://england.prm.ox.ac.uk/englishness-Edward-Lovett.html)

The Horniman Museum’s maple milk tally, **1957.225**, from Salva and dated 1944, has sixteen notches and was used in cheesemaking to calibrate rennet and salt against the milk in a vat. It was also decorated, demonstrating that utilitarian notation and art are not mutually exclusive. [Horniman catalogue](https://www.horniman.ac.uk/object/1957.225/)

### 7. Other instruments: similarities without identity

- **Abacus, suanpan, soroban:** movable counters in positional or valued columns. They embody grouping and exchange, but their state is not normally a permanent tally.
- **Chinese counting rods:** decimal positional calculating signs whose orientation distinguishes adjacent places. Repetition of rods resembles tallying, but the mature system is much more expressive.
- **Roman calculus:** pebbles or counters on a board; Latin *calculus* means a small pebble and gives English “calculation.”
- **Quipu/khipu:** Andean knotted cords encode decimal place values, categories, and sometimes more complex information. Knots can record counts but are not merely unary scratches.
- **Medieval counter-casting:** placing counters on lined tables for arithmetic; represented in manuals and imagery of merchants and Exchequer officials.
- **Algorists versus abacists:** in later medieval Europe, written Hindu-Arabic algorithms increasingly competed with counter-board calculation. The famous visual opposition is real as a pedagogical and iconographic theme, but practitioners could use both.
- **Double-entry books and printed arithmetic:** did not instantly eliminate tallies. Durable, matched wooden receipts solved authentication problems that a naked written number did not.

### 8. Relation to famous mathematical textbooks

The Rhind Mathematical Papyrus, Plimpton 322, *Nine Chapters*, Aryabhata, Brahmagupta, al-Khwarizmi, Fibonacci, Sacrobosco, Pacioli, and Recorde belong to histories of Egyptian fractions, Mesopotamian sexagesimal calculation, Chinese rods, Indian place value, and written European arithmetic. None is a textbook of prehistoric counting-bone notation.

Their relevance is comparative:

- tally arithmetic is concrete and cumulative;
- counting-board arithmetic is place-structured but ephemeral;
- written algorithms preserve both operands and procedures compactly;
- positional numerals make large-number arithmetic far more economical.

There is therefore no tally equivalent of the Rhind Papyrus with worked textual problems, no Lebombo multiplication manual, and no Ishango scribal school archive. **That absence is one of the sharpest limits on reconstruction.**

## Transmission, replacement, and survival

### 1. No single transmission route

Tallying requires only a markable material and a one-to-one procedure. Its worldwide distribution need not result from diffusion. Bone, antler, wood, clay, stone, string, fingers, and body points independently afford countable marks.

The often-implied sequence—

```text
Lebombo → Ishango → Egypt → Rome → modern tally marks
```

—is **[MODERN MYTH/UNSUPPORTED]**. Chronology and visual simplicity do not establish descent.

### 2. Medieval England

English royal administration used Exchequer tallies from at least the twelfth century. A claim that Henry I personally “invented” or introduced them around 1100 is widely repeated but too strong; notched and split records long predate him, and the administrative development is not documented as a single royal invention.

By the fourteenth century, Exchequer stocks could circulate as orders or claims against revenue. They resembled transferable financial instruments in function, although equating them without qualification to modern banknotes or cryptocurrency is anachronistic.

**[DOCUMENTED LAW]** The Ipswich custumal’s “law merchant” provisions explain how an unsealed tally offered in a debt action could be supported by sworn witnesses and condemned if testimony was inconsistent. Physical matching helped authenticate amount; legal institutions established obligation. [Ipswich custumal](https://www.arlima.net/the-orb/encyclop/culture/towns/ipswich5.html)

### 3. Marco Polo’s report

**[DOCUMENTED TEXT, SECOND-HAND ETHNOGRAPHY]** Marco Polo reported that people of Zardandan in Yunnan recorded transactions by splitting a stick, each party keeping a half until settlement. The report shows that medieval Europeans knew of a Chinese-region parallel, not that England borrowed split tallies from Yunnan. [Computer History Museum](https://www.computerhistory.org/storageengine/roman-philosopher-pliny-describes-tally-sticks/)

### 4. Abolition and the 1834 fire

English Exchequer tally procedures were abolished in 1826, but stored sticks remained.

On 16 October 1834 workers burned two cartloads of obsolete tallies in underfloor furnaces beneath the House of Lords. The furnaces and flues overheated; fire spread through the Palace of Westminster, destroying the Lords and Commons chambers while Westminster Hall narrowly survived.

This causal chain is **[DOCUMENTED ADMINISTRATIVE EVENT]**, not legend. Parliament’s own history states that the tally fire ignited panelling in the Lords Chamber. [UK Parliament: Great Fire](https://www.parliament.uk/about/living-heritage/building/palace/architecture/palacestructure/great-fire/), [UK Parliament: reconstruction](https://www.parliament.uk/about/living-heritage/building/palace/westminsterhall/architecture/reconstruction-fire-of-1834/)

Important corrections to popular versions:

- the tallies were deliberately being destroyed because the system was obsolete;
- Parliament was not burned to erase a secret national debt;
- the fire was accidental but associated with ignored heat and smoke warnings;
- not every historical tally was lost; museum collections preserve numerous examples.

### 5. Persistence into modern life

**[OBSERVED PRACTICE]** Tallies remain useful where events arrive sequentially:

- sports scores;
- inventory and forestry counts;
- attendance;
- bar and shop counts;
- laboratory observations;
- prisoner or castaway day-counts;
- game rounds;
- industrial production;
- election audits.

California’s current manual-vote-count regulation expressly instructs tally keepers to place a horizontal hash through four vertical marks for every fifth vote. This provides a dated, legally documented contemporary survival of the five-bar gate. [California manual tally standards](https://www.sos.ca.gov/administration/regulations/current-regulations/elections/manual-tally-standards)

Computers use unary strings in teaching, complexity theory, and specialized encodings, but ordinary digital arithmetic is binary positional. Unicode’s tally characters preserve the appearance for interchange; they do not turn modern computers into unary calculating machines.

## People

### Anonymous makers

The most important people are unknowable:

- the person or persons who incised the Border Cave bone;
- the Ishango craftsperson who prepared the bone handle and its columns;
- shepherds, dairy workers, tally cutters, merchants, debtors, and creditors whose names were rarely recorded.

Sex, occupation, language, intentions, and number vocabulary cannot be recovered merely from the marks.

### Peter Beaumont (1935–2016)

South African archaeologist who excavated Border Cave in the 1970s and reported the marked baboon fibula. His attribution of changing cut profiles to different edges or episodes is material observation; later claims of a lunar or menstrual calendar go beyond what he could directly establish.

### Karel Absolon (1877–1960)

Czech archaeologist and palaeontologist whose team excavated at Dolní Věstonice, including the marked “wolf bone” found in 1937.

### Jean de Heinzelin de Braucourt (1920–1998)

Belgian geologist and archaeologist who excavated at Ishango in 1950 and 1959, published *Les fouilles d’Ishango* in 1957, and publicly developed the arithmetic reading in 1962. He deserves credit both for recovering the object and for originating the famous mathematical interpretation; the two achievements must not be conflated.

### Alexander Marshack (1918–2004)

American journalist and researcher associated with Harvard’s Peabody Museum. Through microscopic analysis and *The Roots of Civilization* (1972), he argued that many Palaeolithic marks were accumulated lunar notation. His work made prehistoric notation a major research question but attracted criticism for interpretive flexibility.

### Francesco d’Errico

Archaeologist who subjected proposed Palaeolithic notations to technological and microscopic analysis. His 1989 critique argued that calendrical interpretations required tests capable of excluding alternatives, not merely patterns compatible with lunar counts.

### Claudia Zaslavsky (1917–2006)

Mathematics educator and ethnomathematics writer. *Africa Counts* and later essays spread the view that women tracking menstrual and lunar cycles may have been humanity’s earliest mathematicians. The claim has cultural and historiographical importance but cannot be proven from the makerless bones.

### Vladimir Pletser and Dirk Huylebrouck

Modern advocates of a base-12 and calculation-device interpretation of Ishango. Their reconstructions exploit the 48/60/60 totals and internal groupings while acknowledging that prime-number knowledge is not established.

### Richard FitzNeal (c. 1130–1198)

Royal treasurer and bishop of London, author traditionally identified with the *Dialogus de Scaccario*. His account is the central textual source for the medieval English Exchequer’s tally and counting-board procedure.

### Tally cutters and scribes

The Exchequer’s *talliator* cut standardized notches; the *scriptor talliarum* supplied identifying writing. Their divided labor shows that numerical cuts and alphabetic text were complementary technologies.

### William de Costello

Sheriff of London named on a surviving 1296 Exchequer tally from the Chapel of the Pyx group. His presence anchors a physical tally in a named administrative transaction.

### Geoffrey B. Saxe and Indigo Esmonde

Researchers who documented Oksapmin body counting and its transformation under schooling, shops, currency, and changing social practice. Their work is evidence against treating “traditional numeral systems” as frozen survivals.

## Culture

### 1. Law and obligation

A tally could function simultaneously as:

- number record;
- receipt;
- contract evidence;
- identity-bearing object;
- instrument payable from revenue;
- audit token.

Its effectiveness came from combining quantity with a difficult-to-reproduce physical match. Medieval courts did not regard the wood as magically self-proving: witnesses, seals, custom, and institutional records still mattered.

The Napoleonic legal tradition preserved rules concerning matching tally sticks much later than their everyday economic heyday. Claims that such articles “remain valid everywhere today” require jurisdiction-by-jurisdiction checking; the French Civil Code was extensively renumbered and revised in 2016.

### 2. Taxation and public finance

Exchequer tallies materialized royal claims in wood. The very term “Exchequer” recalls the checkered calculating surface. Their history complicates the claim that sophisticated finance requires paper literacy: accounts could be distributed across speech, counters, rolls, seals, and split wood.

### 3. Labor and coercion

Tallies are morally neutral only as marks; their uses are not.

**[DOCUMENTED HISTORY]** Caribbean plantation authorities used wooden tallies to measure work performed by enslaved field laborers, and shortfalls could bring violent punishment. Enslaved drivers could be forced to maintain the records through which labor was disciplined. [Randy Browne, *The Driver’s Story*](https://www.jstor.org/stable/jj.5186787)

Nineteenth-century American plantation and government labor records likewise used tally marks and tabular accounts to quantify work by enslaved people. [US National Park Service/NARA study](https://www.govinfo.gov/content/pkg/GOVPUB-I29-PURL-gpo235523/pdf/GOVPUB-I29-PURL-gpo235523.pdf)

This is a necessary counterweight to romantic accounts of tally sticks as quaint pastoral technology.

### 4. Literature

In Daniel Defoe’s *Robinson Crusoe* (1719), Crusoe erects a post or cross and cuts a notch for each day, with longer periodic marks organizing weeks and months. **[DOCUMENTED LITERARY USE]** It dramatizes tallying as civilization reduced to durable memory: an isolated person reconstructs calendar order from repeated cuts.

Later prison, castaway, and captivity imagery conventionally shows groups of five scratched on a wall. **[MODERN CULTURAL TROPE]** It is visually economical, but not every depicted cell-wall tally documents an actual prison practice.

### 5. Art and design

Tally marks are used in contemporary art to signify:

- duration;
- repetition;
- incarceration;
- mortality;
- anonymous mass;
- labor;
- obsession;
- survival.

The mark’s apparent neutrality can be exploited: every person becomes the same stroke. Memorial art may use that equality solemnly; bureaucratic or violent imagery may use it to expose dehumanization.

### 6. Language descended from tally practice

#### Tally

**[DOCUMENTED ETYMOLOGY]** English *tally* comes through Anglo-French *tallie* and medieval Latin *tallia* from Latin *talea*, a cutting, rod, or twig. The English noun is recorded in the fifteenth century, while Anglo-Latin administrative forms are older. The later verb “to tally,” meaning to agree or correspond, derives from the matching halves. [Online Etymology Dictionary](https://www.etymonline.com/word/tally)

#### Score

Old English/Old Norse forms connect *score* with a cut or notch and with twenty. **[SCHOLARLY ETYMOLOGICAL RECONSTRUCTION]** A common explanation is that a special notch marked each completed group of twenty animals or items. The connection between “notch” and “twenty” is genuine; the precise prehistoric counting scenario is reconstructed rather than witnessed. [Dictionary.com etymology](https://www.dictionary.com/browse/score)

#### Stock

Museum and accounting literature frequently says financial *stock* descends from the creditor’s long half of an Exchequer tally. The association is historically attractive and widely repeated.

**[ETYMOLOGICAL CAUTION]** English *stock* already had broad Germanic senses involving a trunk, block, stored supply, or fund. The wooden tally reinforced financial usage, but “the stock market is named solely after tally sticks” is too simple.

#### Foil

The shorter counterpart was called the foil or counter-tally. The word participates in a broader history of leaves, sheets, and counterparts; it should not be assumed that every modern sense of *foil* derives from split tallies.

#### “Short end of the stick”

**[LEGEND]** A common story derives this phrase from the debtor receiving the shorter foil and thereby being disadvantaged. The two halves had different evidentiary roles, but no adequate historical citation was found connecting the idiom’s origin to Exchequer tallies. Treat it as folk etymology.

#### “To keep tabs,” “chalk it up,” and related expressions

These belong to a broad cultural family of material accounting, but direct derivation from tally sticks must be demonstrated individually. Visual similarity is not etymology.

### 7. Liturgy, gematria, isopsephy, coins, clocks, and typography

For this item, absence of evidence is decisive:

- tally notation did not generate a known liturgical numeral canon;
- it has no native gematria or isopsephy because its strokes are not letters;
- it was not a normal system for inscribing coin denominations or regnal dates;
- it did not furnish a clock-face numeral series;
- it has no old-style versus lining figure typography comparable to Hindu-Arabic digits;
- no tally chronograms exist in the strict sense, since chronograms depend on selected numeral-valued letters.

Tallies can coexist with all those practices and may underlie some cumulative habits, but importing the cultural institutions of Roman, Greek, Hebrew, Chinese, or Hindu-Arabic numerals would create a false dossier.

## Controversies and disputes

### 1. “The oldest mathematical artefact”

Candidates change according to the definition:

- oldest deliberate repeated marks;
- oldest marks plausibly used to count;
- oldest securely contextualized number;
- oldest calculation;
- oldest written numeral;
- oldest mathematical table.

The Lebombo bone may be among the oldest objects *interpreted* as a tally. It is not securely the oldest mathematical artefact if “mathematical” requires demonstrated numerical meaning. Ishango has more structured grouping but is younger. Mesopotamian numerical documents are far later but much less semantically ambiguous.

### 2. Was the Lebombo bone a lunar calendar?

**For:**

- 29 approximates the days of a lunation;
- repeated incisions are compatible with daily accumulation;
- lunar observation is ethnographically widespread.

**Against:**

- the object is broken;
- the marks lack phase symbols;
- one sequence supplies no repeated periodic test;
- 29 may count anything;
- no direct contextual association with astronomy or menstruation exists.

**Assessment:** possible, memorable, unproved.

### 3. Did the Ishango makers know prime numbers?

**For:**

- 11, 13, 17, and 19 are exactly the primes between 10 and 20;
- the marks are deliberately grouped rather than uniformly spaced;
- other columns also show conspicuous numerical relationships.

**Against:**

- four numbers form a small sample;
- “prime” requires evidence of a divisibility concept, not just an odd-number sequence;
- alternative decompositions can be generated after inspection;
- there is no second prime list or explanatory operation.

**Assessment:** an ingenious reading originated by de Heinzelin; not proof of prime-number theory.

### 4. Decimal, duodecimal, or sexagesimal Ishango?

The sequences around 10 and 20 support a decimal reading; totals 48 and 60 support attention to 12; 60 invites comparison with sexagesimal organization.

But a base is not merely a number that divides a total. A numeral base should organize representation or recurrence systematically. The bone does not clearly encode place values, powers, or a complete digit inventory.

**Assessment:** numerical structuring is plausible; assignment of a formal base is disputed.

### 5. Calendar notation and Marshack’s microscopy

Marshack’s strongest contribution was to ask whether differences in tool, direction, and superposition reveal marks accumulated at different times. Critics objected that he could explain too many configurations after the fact and did not sufficiently test non-calendrical alternatives.

The dispute is methodological:

```text
compatible pattern ≠ uniquely identified function
```

D’Errico’s critique does not demonstrate that the marks were meaningless; it lowers confidence in calendrical specificity.

### 6. “Women invented mathematics”

This story was spread particularly through Zaslavsky and later educational and Afrocentric literature.

- **As possibility:** women could certainly have made and used early notations.
- **As corrective tradition:** it challenges unsupported default assumptions that prehistoric innovators were male.
- **As artefactual conclusion:** neither Lebombo nor Ishango identifies its maker or subject.
- **As universal first:** untestable with present evidence.

Presenting it as a labeled tradition preserves its intellectual and political history without converting it into archaeological fact.

### 7. “Tally marks are the base of all bases”

This phrase contains a useful metaphor and an overclaim.

- **Useful:** one-to-one correspondence is foundational to exact counting; cumulative unit marks can precede grouped numeral systems.
- **Overclaim:** numeral systems can arise through tokens, fingers, body points, knots, measures, counters, and language; no universal historical chain is documented.
- **Mathematical problem:** unary is not an ordinary positional base.

Better: **tallying is one of the simplest and most repeatedly invented external representations of discrete quantity.**

### 8. The origin of the five-bar gate

Its perceptual efficiency is obvious, but the dossier found no securely dated ancient origin. The claim that it descends directly from Roman `V` or a medieval gate is unsupported. The name describes the modern appearance.

### 9. The origin of `正` tallying

The practice is real and modern Unicode encoding is documented. Its first adoption remains obscure in the consulted sources. Theatre-seat and gambling-house stories currently belong under tradition or legend unless tied to dated documents.

### 10. “Roman numerals came from shepherds’ tallies”

Roman and Etruscan unit strokes fit a tally origin well. The development of `V`, `X`, `L`, `C`, `D`, and `M` is more complicated. A generic tally ancestry is plausible; the tidy story of a shepherd making every fifth notch a V and every tenth an X is reconstruction.

### 11. “Tallies were used because people were illiterate”

This is reductive.

Tallies were used by highly literate royal administrations because they were:

- durable;
- quick to cut;
- readable across languages;
- hard to alter after splitting;
- suited to audit;
- compatible with written rolls.

Literacy and tallying were complementary, not mutually exclusive.

### 12. “Split tallies were impossible to forge”

Matching wood grain and fracture provided excellent tamper evidence. It did not solve coercion, collusion, institutional dishonesty, lost halves, false witnesses, or fraudulent creation of the original agreement.

### 13. “Exchequer tallies were money”

They sometimes circulated as claims on revenue and could perform money-like credit functions. They were not a homogeneous legal tender identical to coins or modern notes. “Wooden money” is a useful analogy only when the transaction type, period, and legal framework are specified.

### 14. The 1834 fire myths

**Documented:** obsolete tally sticks were burned; overheated furnaces caused the Palace fire.

**Legend or exaggeration:**

- six centuries of every English financial record were destroyed;
- the government deliberately erased its debts;
- the fire abolished the tally system—it had already been abolished in 1826;
- no tallies survived.

### 15. Ifrah and universal histories

Georges Ifrah’s *Histoire universelle des chiffres* popularized an enormous range of counting devices and numeral traditions. It remains valuable for comparison and illustration.

Joseph Dauben’s review records specialists’ objections to errors in Ifrah’s Mesopotamian, Chinese, Mayan, and Indian chronologies and interpretations. Ifrah should therefore be used as a guide to claims and examples, not as sole authority for disputed firsts. [Dauben review](https://www.ams.org/notices/200202/rev-dauben.pdf)

Chrisomalis’s 2010 comparative study is methodologically stronger for classifying notations and tracing historically demonstrable relations. Menninger remains valuable for older European scholarship, material devices, and etymological-cultural comparisons, but some evolutionary narratives and artefact readings require updating.

## Open questions

1. What exactly was counted on the Lebombo fragment?
2. Is its association with the dated Border Cave layer secure enough to support the often-repeated c. 42,000 BP figure?
3. How many incisions were lost at the broken end?
4. Can microscopic refitting establish the sequence and number of engraving episodes?
5. What species and exact anatomical element is the Ishango handle, and can improved non-destructive analysis refine that identification?
6. Can the Ishango object itself ever be directly dated, rather than dated by its deposit?
7. Which middle-column incision count—especially the damaged group—is correct?
8. Do statistical tests distinguish the proposed Ishango arithmetic structures from patterns obtainable in other plausible groupings?
9. Are there additional marked objects from the same Ishango level that form a coherent notational tradition?
10. What are the accession numbers and complete curatorial histories of the Lebombo and Ishango objects?
11. What is the earliest dated example of the Western five-bar gate?
12. What is the earliest dated Chinese use of progressive `正` as a tally?
13. Which routes, if any, connect occupational notching traditions with formal numeral scripts?
14. How often did medieval Exchequer stocks circulate beyond their original payees?
15. Which surviving legal cases tested altered or mismatched split tallies?
16. How did tally systems function in societies where spoken number words had low conventional limits?
17. Which prehistoric mark series can be shown experimentally to have accumulated one event at a time?
18. How should historians recognize Indigenous and African intellectual agency without assigning unsupported modern operations to anonymous artefacts?

## Sources

### Primary artefacts, catalogues, and institutional records

1. Institute of Natural Sciences, Brussels, “The Ishango Bone.”  
   https://www.naturalsciences.be/en/museum/exhibitions-activities/exhibitions/250-years-of-natural-sciences/the-ishango-bone

2. Institute of Natural Sciences, *The Carved Ishango Bone* exhibition brochure.  
   https://www.naturalsciences.be/file/cc73d96153bbd5448a56f19d925d05b1379c7f21/369895724a871d793f603e27d8e31fae74fdbf13/inst-202403-brochure-ishango-en-fv.pdf?name=inst_202403_brochure_ishango_en_fv.pdf&type=application%2Fpdf

3. Institute of Natural Sciences, Ishango stratigraphy and dating.  
   https://ishango.naturalsciences.be/en/en-ishango-13.html

4. Institute of Natural Sciences, Ishango notched-object context.  
   https://ishango.naturalsciences.be/en/en-ishango-19.html

5. Science Museum Group, “Medieval Exchequer Tally Sticks,” object 1952-431.  
   https://collection.sciencemuseumgroup.org.uk/objects/co60506/medieval-exchequer-tally-sticks

6. British Museum, “Woodcutter’s tally stick,” museum number 1936,1213.1.  
   https://www.britishmuseum.org/collection/object/H_1936-1213-1

7. Horniman Museum and Gardens, “Milk tally stick,” museum number 1957.225.  
   https://www.horniman.ac.uk/object/1957.225/

8. Pitt Rivers Museum/England: The Other Within, Edward Lovett sheep tallies, including 1909.60.4.  
   https://england.prm.ox.ac.uk/englishness-Edward-Lovett.html

9. Hampshire Cultural Trust, “Inscribed wooden tally stick,” thirteenth–fourteenth century.  
   https://collections.hampshireculture.org.uk/object/inscribed-wooden-tally-stick-13th-14th-century-preston-candover-hampshire

10. London Museum, “Tallystick.”  
    https://www.londonmuseum.org.uk/collections/v/object-372215/tallystick/

11. London Museum, “Tally stick.”  
    https://www.londonmuseum.org.uk/collections/v/object-37216/tally-stick/

12. Mathematical Association of America, Swetz and Katz, “Mathematical Treasures—English Tally Sticks.”  
    https://old.maa.org/press/periodicals/convergence/mathematical-treasures-english-tally-sticks

13. Smithsonian Human Origins Program, “Geometric Incised Bone, Dolní Věstonice.”  
    https://humanorigins.si.edu/evidence/behavior/art-music/other-decorated-objects/geometric-incised-bone-rectangle

14. Australian Museum, “Dolní Věstonice Archaeological Site.”  
    https://australian.museum/learn/cultures/international-collection/dolni-vstonice-archaeological-site/

15. UK Parliament, “The Great Fire of 1834.”  
    https://www.parliament.uk/about/living-heritage/building/palace/architecture/palacestructure/great-fire/

16. UK Parliament, “Reconstruction and the Fire of 1834.”  
    https://www.parliament.uk/about/living-heritage/building/palace/westminsterhall/architecture/reconstruction-fire-of-1834/

17. Wellcome Collection, “A tally stick used to record a financial transaction between the British Exchequer and Barbados,” 1835 lithograph.  
    https://wellcomecollection.org/works/szsfztr9

18. University of London Digital Galleries, “Tally sticks.”  
    https://exhibitions.london.ac.uk/s/digital-galleries/item/2795

### Archaeological and historical studies

19. Peter B. Beaumont, “On the Age and Context of the Border Cave Skeletons,” *Palaeontologia Africana* 23 (1980), 21–33.  
    https://files01.core.ac.uk/download/pdf/39674913.pdf

20. Peter B. Beaumont and Robert G. Bednarik, Border Cave marked-object study, *Rock Art Research* 30.1 (2013).  
    https://www.ifrao.com/wp-content/uploads/2014/08/30-1-BeaumontBed.pdf

21. Jean de Heinzelin, *Les fouilles d’Ishango* (Brussels: Institut des parcs nationaux du Congo belge, 1957).  
    https://books.google.com/books/about/Les_fouilles_d_Ishango.html?id=o35DqYKR440C

22. Institute library bibliography for Jean de Heinzelin.  
    https://library.naturalsciences.be/selection-of-the-month/jean-de-heinzelin-de-braucourt-1920-1998

23. Isabelle Crévecoeur et al., “Late Stone Age Human Remains from Ishango,” *Journal of Human Evolution* 96 (2016).  
    https://www.sciencedirect.com/science/article/abs/pii/S0047248416300057

24. Alison S. Brooks and Catherine C. Smith, “Ishango Revisited: New Age Determinations and Cultural Interpretations,” *African Archaeological Review* 5 (1987), 65–78.  
    https://link.springer.com/article/10.1007/BF01117460

25. Francesco d’Errico, “Palaeolithic Lunar Calendars: A Case of Wishful Thinking?”, *Current Anthropology* 30.1 (1989), 117–118.  
    https://www.journals.uchicago.edu/doi/pdf/10.1086/203721

26. Karenleigh A. Overmann, “The Beginning of Time,” *Cambridge Archaeological Journal* (2024).  
    https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/beginning-of-time/B7DDE9AC9E3BEC0027FF453046846D31

27. Karenleigh A. Overmann, “Keeping Count: On Interpreting Record Keeping in Prehistory,” *Journal of Anthropological Archaeology* 63 (2021).  
    https://www.sciencedirect.com/science/article/abs/pii/S0278416521000374

28. Vladimir Pletser and Dirk Huylebrouck, “Does the Ishango Bone Indicate Knowledge of the Base 12?”  
    https://arxiv.org/abs/1204.1019

29. Dirk Huylebrouck, *Africa and Mathematics: From Colonial Findings Back to the Ishango Rods* (Springer, 2019).  
    https://link.springer.com/book/10.1007/978-3-030-04037-6

30. Olivier Keller, “Les fables d’Ishango, ou l’irrésistible tentation de la mathématique-fiction.”  
    https://www.bibnum.education.fr/sites/default/files/ishango-analysis_v2.pdf

31. Dirk Huylebrouck, response to “Les fables d’Ishango.”  
    https://www.bibnum.education.fr/sites/default/files/64-ishango-answer.pdf

32. UNESCO/ICOMOS, *Heritage Sites of Astronomy and Archaeoastronomy: A Thematic Study*.  
    https://whc.unesco.org/document/104639

33. Lambros Malafouris, “Mark Making and Human Becoming,” 2021.  
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7889684/

34. Henshilwood et al., “Engraved Ochres from the Middle Stone Age Levels at Blombos Cave.”  
    https://www.researchgate.net/publication/26257796_Engraved_Ochres_from_the_Middle_Stone_Age_Levels_at_Blombos_Cave_South_Africa

### Tally accounting, law, and social history

35. William T. Baxter, “Early Accounting: The Tally and Checkerboard,” *Accounting Historians Journal* 16.2 (1989).  
    https://egrove.olemiss.edu/aah_journal/vol16/iss2/2/

36. Richard FitzNeal, *Dialogus de Scaccario*, in Emilie Amt and S. D. Church, eds., *Dialogus de Scaccario and Constitutio Domus Regis* (Oxford, 2007), searchable preview.  
    https://dokumen.pub/dialogus-de-scaccario-and-constitutio-domus-regis-the-dialogue-of-the-exchequer-and-the-disposition-of-the-kings-household-0199258619-9780199258611.html

37. Older English translation of Richard FitzNeal, *Dialogus de Scaccario*.  
    https://www.heritech.com/yamaguchy/library/duncan/dialogus.html

38. Ipswich Borough Custumal, chapter 40, “Proof of Tally.”  
    https://www.arlima.net/the-orb/encyclop/culture/towns/ipswich5.html

39. Computer History Museum, “Roman Philosopher Pliny Describes Tally Sticks.”  
    https://www.computerhistory.org/storageengine/roman-philosopher-pliny-describes-tally-sticks/

40. Randy M. Browne, *The Driver’s Story: Labor and Power in the World of Atlantic Slavery* (University of Pennsylvania Press, 2024), chapter 2.  
    https://www.jstor.org/stable/jj.5186787

41. US National Park Service, *The Enslaved African American Experience, 1847–1863*, using NARA time books and paybooks.  
    https://www.govinfo.gov/content/pkg/GOVPUB-I29-PURL-gpo235523/pdf/GOVPUB-I29-PURL-gpo235523.pdf

42. California Secretary of State, “Manual Tally Standards.”  
    https://www.sos.ca.gov/administration/regulations/current-regulations/elections/manual-tally-standards

### Anthropology and cognition

43. Geoffrey B. Saxe, Oksapmin Counting Project.  
    https://culturecognition.com/new-page-3

44. Geoffrey B. Saxe, *Cultural Development of Mathematical Ideas: Papua New Guinea Studies* (Cambridge University Press, 2012), excerpt.  
    https://assets.cambridge.org/97805217/61666/excerpt/9780521761666_excerpt.pdf

45. Geoffrey Saxe and Indigo Esmonde, “Making Change in Oksapmin Tradestores” and related work, bibliographic context.  
    https://culturecognition.com/new-page-3

46. “Number Systems in Societies,” *The National* (Papua New Guinea).  
    https://www.thenational.com.pg/number-systems-in-societies/

47. Russell Gray et al., “The Cultural Origins of Symbolic Number.”  
    https://pmc.ncbi.nlm.nih.gov/articles/PMC8678391/

48. Glendon Lean, *Counting Systems of Papua New Guinea and Oceania*, overview PDF.  
    https://uscngp.com/s/17-02-TallySystems.pdf

### Comparative histories and historiography

49. Stephen Chrisomalis, *Numerical Notation: A Comparative History* (Cambridge University Press, 2010), front matter.  
    https://assets.cambridge.org/97805218/78180/frontmatter/9780521878180_frontmatter.pdf

50. Stephen Chrisomalis, *Numerical Notation*, introduction.  
    https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/90BCD7A80F84CBEF195F02D36511F4E7/9780511676062c1_p1-33_CBO.pdf/introduction.pdf

51. Stephen Chrisomalis, *Numerical Notation: A Comparative History*, searchable copy consulted for the treatment of cumulative systems and tallies.  
    https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20%28CUP%2C%2C2010%29%28ISBN%200521878187%29%28O%29%28498s%29_MPop_.pdf

52. Karl Menninger, *Number Words and Number Symbols: A Cultural History of Numbers*, trans. Paul Broneer (Cambridge, MA: MIT Press, 1969; Dover reprint, 1992), bibliographic and lending record.  
    https://openlibrary.org/books/OL5612154M/Number_words_and_number_symbols

53. Georges Ifrah, *The Universal History of Numbers: From Prehistory to the Invention of the Computer*, trans. David Bellos et al. (London: Harvill Press, 1998; Wiley edition, 2000).

54. Joseph W. Dauben, review of Ifrah’s *Universal History of Numbers* and *Universal History of Computing*, *Notices of the AMS* 49.1 (2002), 32–38.  
    https://www.ams.org/notices/200202/rev-dauben.pdf

55. George Gheverghese Joseph, *The Crest of the Peacock: Non-European Roots of Mathematics*, consulted digital edition.  
    https://www.ms.uky.edu/~sohum/ma330/files/crest_of_the_peacock.pdf

56. Alexander Marshack, *The Roots of Civilization: The Cognitive Beginnings of Man’s First Art, Symbol and Notation* (New York: McGraw-Hill, 1972; later revised editions).

### Unicode and modern signs

57. Unicode Consortium, “Counting Rod Numerals: Names List,” including ideographic and Western tally marks.  
    https://www.unicode.org/charts/nameslist/n_1D360.html

58. Unicode Consortium, *The Unicode Standard*, Counting Rod Numerals chart.  
    https://www.unicode.org/charts/PDF/U1D360.pdf

59. Ken Lunde and Daisuke Miura, Unicode tally-mark proposal and Script Ad Hoc recommendations, 2016.  
    https://www.unicode.org/L2/L2016/16156-script-recs.pdf

60. Unicode tally-mark naming clarification, 2017.  
    https://www.unicode.org/L2/L2017/17188-tally-mark-name-change.pdf

### Lexicography

61. Online Etymology Dictionary, “tally.”  
    https://www.etymonline.com/word/tally

62. CNRTL, French *taille*, historical etymology.  
    https://www.cnrtl.fr/etymologie/taille//1

63. *Encyclopédie*, first edition, “TAILLE,” on wooden payment tallies.  
    https://fr.wikisource.org/wiki/L%E2%80%99Encyclop%C3%A9die/1re_%C3%A9dition/TAILLE

64. Dictionary.com, “score,” including Old Norse *skor*, “notch.”  
    https://www.dictionary.com/browse/score

65. World English Historical Dictionary, “Tally.”  
    https://wehd.com/93/Tally_sb1.html
