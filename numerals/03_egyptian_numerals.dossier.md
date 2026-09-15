# Egyptian numerals (hieroglyphic and hieratic): Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| **Name** | Egyptian hieroglyphic numerals; hieratic numerals; later demotic numerals |
| **Base** | Decimal: signs are organized around powers of ten |
| **Hieroglyphic type** | **Cumulative-additive** or **sign-value additive**; non-positional. A sign for each power \(10^0\) through \(10^6\) is repeated as necessary |
| **Hieratic/demotic type** | **Ciphered-additive**: separate cursive signs for 1–9, 10–90, 100–900 and, in developed usage, higher multiples. Still non-positional |
| **Zero** | No positional zero was required. The word/sign *nfr* could denote a zero balance or a reference level in particular contexts, but it was not a general numeral digit |
| **Fractions** | Predominantly unit fractions \(1/n\), written by placing the “part” sign above a denominator; special conventional forms existed for \(1/2\), \(1/3\), \(2/3\), \(1/4\), and metrological fractions |
| **Period** | Numerical marks are attested in Naqada III, late fourth millennium BCE. The indigenous hieroglyphic–hieratic–demotic tradition continued into Roman Egypt; the last dated Demotic inscription is 452 CE |
| **Region** | Nile Valley and Delta; also Egyptian-controlled or Egyptian-influenced areas in Nubia, Sinai and the Levant |
| **Principal media** | Monumental stone and wood in hieroglyphic; papyrus, leather, wood and ostraca in hieratic and demotic |
| **Successors/replacements** | Greek alphabetic numerals in Ptolemaic and Roman administration; Coptic alphabetic numerals; later Arabic-language administrative notation and Hindu-Arabic digits |

### Evidentiary labels used below

- **[A] Documented artefact/text:** physically surviving object, inscription, manuscript or ancient testimony.
- **[R] Scholarly reconstruction:** inference accepted or seriously argued in specialist scholarship.
- **[D] Disputed:** competing readings or chronologies remain.
- **[T] Tradition:** an ancient or later transmitted story whose historical content cannot simply be assumed.
- **[L] Legend:** a popular story unsupported or contradicted by the evidence.
- **[M] Modern convention/invention:** terminology, diagram or reconstruction created in modern scholarship or popular culture.

A crucial boundary: Egyptian numerals are not ancestors of the Hindu-Arabic digits in any demonstrated palaeographic chain. The Ishango and Lebombo bones, Mesopotamian tokens, Plimpton 322, Bakhshali manuscript, Gwalior zero, Brahmi numerals, Chinese rods, Maya numerals and Dresden Codex belong to other histories. They are useful comparisons, but none is evidence for the origin or transmission of Egyptian notation.

---

## The system in detail

### 1. The seven familiar hieroglyphic power-signs

The following Unicode characters are the base hieroglyphs, displayed left-to-right here as a modern typographic normalization. Actual inscriptions may reverse their orientation or arrange repetitions into compact quadrats.

| Value | Unicode sign | Gardiner | Drawing in words | Conventional Egyptian reading | Status |
|---:|:---:|:---:|---|---|---|
| 1 | 𓏤 | Z1 | short vertical stroke | normally a count-stroke; “one” as a word is *wꜥ* | **[A]** |
| 10 | 𓎆 | V20 | cattle hobble or inverted U | *mḏw* “ten” | **[A/R]** identification as a hobble is conventional |
| 100 | 𓍢 | V1 | coiled rope | *šnt* or *št* | **[A]** |
| 1,000 | 𓆼 | M12 | water-lily plant, traditionally “lotus” | *ḫꜣ* | **[A]** |
| 10,000 | 𓂭 | D50 | bent or pointing finger | *ḏbꜥ* | **[A]** |
| 100,000 | 𓆐 | I8 | tadpole/frog larva | *ḥfn* | **[A]** |
| 1,000,000 | 𓁨 | C11 | kneeling god with raised arms, identified as Heh | *ḥḥ* | **[A/R]**; often “a million,” “myriad” or “countless” rather than an exact million |

Unicode encodes the underlying hieroglyphic signs and layout controls. It normally represents hieratic text through hieroglyphic transcription rather than attempting to reproduce every handwritten palaeographic form. Unicode explicitly notes that individual numeral forms are encoded because hieratic numerals can differ substantially from their hieroglyphic transcriptions. See the [Unicode Egyptian chapter](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-11/), [basic chart](https://www.unicode.org/charts/PDF/U13000.pdf), [Extended-A chart](https://www.unicode.org/charts/PDF/U13460.pdf), and [format-control names list](https://www.unicode.org/charts/nameslist/n_13430.html).

#### What the pictures originally meant

- **[A]** The graphical identifications—stroke, hobble, coil, water-lily, finger, tadpole and Heh—are based on their use elsewhere in Egyptian writing and iconography.
- **[R]** Their motivation as numeral-signs is much less certain. The stroke plausibly derives from tallying.
- **[R/D]** Following Sethe, Chrisomalis notes that 10 may have been assigned by a rebus involving the word *mḏw*, rather than because ten cattle or ten objects were literally tied with a hobble.
- **[R]** The fecund tadpole may have suggested an enormous multitude, and Heh was a divinity of indefinite extent or eternity.
- **[D]** Such semantic explanations are plausible mnemonic reconstructions, not ancient explanations preserved in a mathematical treatise. The current state of the evidence is summarized in Ferrara and colleagues’ study, [“Numeracy at the dawn of writing”](https://doi.org/10.1016/j.hm.2020.08.002).

### 2. How an integer is formed

A hieroglyphic number is the sum of its signs:

\[
N=\sum_i n_i10^i,\qquad 0\leq n_i\leq 9
\]

Thus three 100-signs, four 10-signs and two strokes mean:

> 𓍢𓍢𓍢 𓎆𓎆𓎆𓎆 𓏤𓏤 = 342.

This is decimal but not positional. Moving a stroke from the right to the left does not turn it from 1 into 1,000. Its value remains 1.

A repeated sign ordinarily appears no more than nine times before being exchanged for the next power. Repetitions were grouped aesthetically—often in rows of three—rather than mechanically printed in a straight line.

### 3. Ordering and direction

**[A]** Egyptian hieroglyphic writing could run right-to-left, left-to-right or vertically. People and animals face toward the beginning of the line. Numeral groups follow the direction and graphic organization of their host inscription.

**[A/R]** Power-signs were commonly ordered from larger to smaller values, but the order could be reversed or regrouped to fit a quadrat. Because the notation is additive, the arithmetic value normally survives such rearrangement.

**[M]** Modern textbooks nearly always normalize signs left-to-right and largest-to-smallest. That presentation should not be mistaken for a compulsory ancient “place-value” order.

### 4. Table: 1–20 in normalized hieroglyphic notation

The following uses the single-stroke sign repeatedly. Ancient scribes would usually arrange groups of strokes more compactly.

| Number | Hieroglyphic numeral | Additive reading |
|---:|---|---|
| 1 | 𓏤 | 1 |
| 2 | 𓏤𓏤 | 1 + 1 |
| 3 | 𓏤𓏤𓏤 | 3 |
| 4 | 𓏤𓏤𓏤𓏤 | 4 |
| 5 | 𓏤𓏤𓏤𓏤𓏤 | 5 |
| 6 | 𓏤𓏤𓏤𓏤𓏤𓏤 | 6 |
| 7 | 𓏤𓏤𓏤𓏤𓏤𓏤𓏤 | 7 |
| 8 | 𓏤𓏤𓏤𓏤𓏤𓏤𓏤𓏤 | 8 |
| 9 | 𓏤𓏤𓏤𓏤𓏤𓏤𓏤𓏤𓏤 | 9 |
| 10 | 𓎆 | 10 |
| 11 | 𓎆𓏤 | 10 + 1 |
| 12 | 𓎆𓏤𓏤 | 10 + 2 |
| 13 | 𓎆𓏤𓏤𓏤 | 10 + 3 |
| 14 | 𓎆𓏤𓏤𓏤𓏤 | 10 + 4 |
| 15 | 𓎆𓏤𓏤𓏤𓏤𓏤 | 10 + 5 |
| 16 | 𓎆𓏤𓏤𓏤𓏤𓏤𓏤 | 10 + 6 |
| 17 | 𓎆𓏤𓏤𓏤𓏤𓏤𓏤𓏤 | 10 + 7 |
| 18 | 𓎆𓏤𓏤𓏤𓏤𓏤𓏤𓏤𓏤 | 10 + 8 |
| 19 | 𓎆𓏤𓏤𓏤𓏤𓏤𓏤𓏤𓏤𓏤 | 10 + 9 |
| 20 | 𓎆𓎆 | 10 + 10 |

Compact hieroglyphs such as Z2 and Z3 could represent grouped strokes, but they also had non-numerical functions. The table therefore spells out the additive structure rather than claiming a single invariant manuscript glyph for each number.

### 5. Tens, hundreds and thousands

| Value | Normalized hieroglyphic form |
|---:|---|
| 10 | 𓎆 |
| 20 | 𓎆𓎆 |
| 30 | 𓎆𓎆𓎆 |
| 40 | 𓎆𓎆𓎆𓎆 |
| 50 | 𓎆𓎆𓎆𓎆𓎆 |
| 60 | 𓎆𓎆𓎆𓎆𓎆𓎆 |
| 70 | 𓎆𓎆𓎆𓎆𓎆𓎆𓎆 |
| 80 | 𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓎆 |
| 90 | 𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓎆 |
| 100 | 𓍢 |
| 200 | 𓍢𓍢 |
| 300 | 𓍢𓍢𓍢 |
| 400 | 𓍢𓍢𓍢𓍢 |
| 500 | 𓍢𓍢𓍢𓍢𓍢 |
| 600 | 𓍢𓍢𓍢𓍢𓍢𓍢 |
| 700 | 𓍢𓍢𓍢𓍢𓍢𓍢𓍢 |
| 800 | 𓍢𓍢𓍢𓍢𓍢𓍢𓍢𓍢 |
| 900 | 𓍢𓍢𓍢𓍢𓍢𓍢𓍢𓍢𓍢 |
| 1,000 | 𓆼 |
| 2,000 | 𓆼𓆼 |
| 3,000 | 𓆼𓆼𓆼 |
| 10,000 | 𓂭 |
| 100,000 | 𓆐 |
| 1,000,000 | 𓁨 |

### 6. Hieratic numerals

Hieratic was written rapidly with a reed brush. Its numerals did not remain simple cursive repetitions of the seven monumental signs.

**[A]** By the Old and Middle Kingdoms, hieratic had distinct signs for:

- 1–9;
- 10, 20, … 90;
- 100, 200, … 900;
- 1,000, 2,000, … 9,000, with changing abbreviation practices at still higher values.

Thus a hieratic scribe could write 7 with one cipher rather than seven strokes and 700 with one sign rather than seven coils. This is why Chrisomalis classifies the system as **ciphered-additive**. It resembles Greek alphabetic notation structurally—nine units, nine tens, nine hundreds—but its symbols are cursive numerical signs, not an alphabet with numerical values.

**[A]** Hieratic numeral forms changed markedly through time. Möller’s three-volume *Hieratische Paläographie* remains a fundamental palaeographic collection; a single timeless “hieratic digit font” would be misleading.

**[M]** Modern printed editions generally transcribe hieratic numerals into standardized hieroglyphs or Arabic digits. Accordingly, the hieroglyphic tables above are reliable statements of value but are not facsimiles of Ahmose’s handwriting.

**[D]** Carl Boyer emphasized “cipherization” as an Egyptian conceptual invention and suggested a relationship to later Greek alphabetic numeration. Chrisomalis’s narrower proposal is that Greek alphabetic numeration borrowed the *structure* of demotic Egyptian numerals in sixth-century BCE Ionian–Egyptian commercial contact, substituting Greek letters for Egyptian signs. This remains an argued historical transmission, not a proven palaeographic descent of the signs.

### 7. Demotic numerals

**[A]** Demotic developed from northern cursive hieratic in the seventh century BCE. It preserved the ciphered-additive principle while its signs became still more ligatured and abbreviated.

Demotic was especially important in:

- contracts and loans;
- tax receipts;
- accounts and inventories;
- land measurement;
- dates and regnal years;
- mummy labels and graffiti.

The University of Chicago holds almost 900 Demotic ostraca, dated from about 285 BCE to about 80 CE, many of them fiscal or administrative records: [ISAC Demotic Ostraca Online](https://isac.uchicago.edu/research/projects/isac-museum-demotic-ostraca-online).

### 8. Ligatures and abbreviations

**[A]** Hieratic and demotic numerals can fuse strokes and power-signs into single cursive configurations. Numerals for 2–9, multiples of ten and multiples of a hundred are themselves products of this abbreviation.

**[A/R]** In hieroglyphic texts, graphic packing can make repeated signs resemble a composite emblem, but this is not multiplication by place. A cluster of three strokes remains three.

**[A]** Date-writing sometimes uses special forms, including Gardiner V40 for 10 in dates. Ordinal, regnal and calendrical usage can differ from ordinary cardinal notation.

**[M]** Manuel de Codage and Unicode layout controls allow modern editors to specify stacking, juxtaposition, insertion and mirroring. These are digital encoding conventions for ancient layouts, not ancient operators.

### 9. Zero and absence

The statement “Egyptian numerals had no zero” requires qualification.

1. **[A] No positional digit:** The numeral system had no empty decimal place. It did not need one: 101 was simply one 100-sign plus one stroke.
2. **[A/R] Zero balances:** In administrative accounts *nfr*, “good, complete, balanced,” is attested where a remainder is nil. It is comparable to writing “balance: none” rather than introducing a reusable digit 0.
3. **[A/R] Surveying datum:** *Nfr* could mark a reference or zero level in New Kingdom architectural records.
4. **[D] Numerical status:** Some modern authors call these an “Egyptian zero.” Others reserve *zero* for an abstract number used in arithmetic or a positional placeholder. The artefacts demonstrate a concept of nothing remaining or a neutral datum, but not a general zero numeral integrated into calculation.
5. **[L]** Claims that 𓄤 *nfr* functioned just like modern 0 throughout Egyptian mathematics go beyond the surviving evidence.

### 10. Fractions

#### General rule

**[A]** Most ordinary fractions were unit fractions:

\[
\frac12,\frac13,\frac14,\frac15,\ldots
\]

The denominator was written with the “part” sign—often transliterated as an overbar—above it. In hieratic the marker is commonly a dot. Thus a marked 5 means \(1/5\), not 5.

**[A]** Proper fractions with numerator greater than one were normally decomposed into sums of distinct unit fractions:

\[
\frac25=\frac13+\frac1{15}.
\]

The Lahun fragment UC 32159 and the Rhind Papyrus give the same conventional decomposition, evidence that scribes learned standardized tables rather than choosing arbitrary modern decompositions. [UCL’s description of UC 32159](https://www.ucl.ac.uk/museums-static/digitalegypt/lahun/uc32159.html) explains the table.

Special signs or spellings existed for \(1/2\), \(1/3\), \(2/3\) and \(1/4\). The fraction \(2/3\) is the conspicuous exception to a strict “unit fractions only” formula.

#### Eye of Horus fractions

The familiar diagram assigns parts of the wedjat eye to:

\[
\frac12,\frac14,\frac18,\frac1{16},\frac1{32},\frac1{64}.
\]

These sum to \(63/64\).

- **[A]** Hieratic signs for this sequence were used in subdividing the *heqat*, a grain-capacity measure.
- **[R, 1911]** Georg Möller proposed that the signs originated as parts of the Eye of Horus.
- **[R/D, 1923]** T. Eric Peet observed that the supposed eye-part hieroglyphs are later than the hieratic fraction signs. He proposed that the old signs may have been reinterpreted as eye parts in the New Kingdom.
- **[D, 2002]** Jim Ritter traced the palaeography backward and found that the earlier forms diverge increasingly from the supposed eye components. He also argued that votive cubits do not securely prove the equation.
- **[M/L]** The ubiquitous colored eye diagram, plus the story that Thoth magically supplied the missing \(1/64\), is a modern synthesis of a genuine myth of Horus’s damaged and restored eye with Möller’s disputed mathematical reconstruction. No surviving Egyptian mathematical text tells that complete story.

See Ritter’s reference article, [“Horus-eye Fractions”](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781444338386.wbeah21178), and the concise [MathWorld survey](https://mathworld.wolfram.com/EyeofHorusFraction.html).

### 11. Expressive range

**[A]** A distinct sign existed for one million, but its semantic range included “many” or “countless.” A Heh figure could therefore be precise, rhetorical or religious depending on context.

**[R]** The basic repetitive method has no necessary mathematical ceiling: signs can be repeated, higher units described verbally, or a large unit multiplied by an accompanying numeral. Egyptian number words above 10,000 sometimes use multiplicative phrasing.

**[A]** Monumental enumerations reach into the millions. Therefore “one million was the largest number Egyptians could express” is false if taken as a hard limit. It was the largest familiar single power-sign in the canonical elementary table, not the largest possible value.

---

## Famous numbers written out

These are normalized linear renderings, not facsimile layouts.

### 1. 342

> 𓍢𓍢𓍢 𓎆𓎆𓎆𓎆 𓏤𓏤

\[
300+40+2=342.
\]

### 2. 365, the schematic civil year

> 𓍢𓍢𓍢 𓎆𓎆𓎆𓎆𓎆𓎆 𓏤𓏤𓏤𓏤𓏤

The Egyptian civil calendar contained twelve 30-day months plus five epagomenal days. This rendering illustrates the number only; actual calendrical texts employ period-specific layouts and words.

### 3. 19,607, Rhind Problem 79’s total

> 𓂭 𓆼𓆼𓆼𓆼𓆼𓆼𓆼𓆼𓆼 𓍢𓍢𓍢𓍢𓍢𓍢 𓏤𓏤𓏤𓏤𓏤𓏤𓏤

\[
10,000+9,000+600+7=19,607.
\]

The problem lists 7 houses, 49 cats, 343 mice, 2,401 ears of grain and 16,807 *heqat*, totaling 19,607. Chace’s edition is available in [facsimile and translation](https://upload.wikimedia.org/wikipedia/commons/7/7b/The_Rhind_Mathematical_Papyrus%2C_Volume_I.pdf).

### 4. The Narmer macehead’s traditional large-number readings

Modern publications commonly transcribe its bottom register as:

- cattle: 400,000  
  > 𓆐𓆐𓆐𓆐
- goats: 1,422,000  
  > 𓁨 𓆐𓆐𓆐𓆐 𓂭𓂭 𓆼𓆼
- captives: 120,000  
  > 𓆐 𓂭𓂭

**[A]** The carved signs and associated animal/captive figures exist on the macehead.

**[R/D]** The arithmetic readings are conventional Egyptological interpretations, but whether the quantities are literal administrative totals, propagandistic exaggerations, tribute or booty is not settled. The object is Ashmolean Museum **AN1896–1908.E.3631**, excavated by James Quibell and Frederick Green at Hierakonpolis in 1897–98. See the [Narmer catalogue record](https://narmer.org/inscription/0080.pdf) and Ashmolean curator Liam McNamara’s [object study](https://www.hierakonpolis-online.org/files/hk_nn/nn-31-2019.pdf).

---

## Origins: dated and placed

### Before Egyptian numerical writing

**[A]** The Lebombo and Ishango bones carry sets of incisions, but their grouping and function are disputed. They show that humans made structured marks long before Egyptian writing; they do not transmit identifiable Egyptian power-signs.

**[A/R]** Mesopotamian calculi, tokens and proto-cuneiform numerical tablets form an independent and extremely early administrative tradition. Denise Schmandt-Besserat argued that clay tokens were enclosed in bullae and then impressed or drawn on their surfaces, helping generate Mesopotamian writing. Whether every stage of her universalized token model applies is disputed. There is no demonstrated sequence “Uruk tokens → Egyptian numerals.”

### Naqada III and Tomb U-j, approximately 3300–3200 BCE

**[A]** The earliest currently recognized Egyptian numerical symbols occur on some of roughly 200 inscribed ivory and bone tags from Tomb U-j at Umm el-Qaʿab, Abydos. The tomb was discovered by Günter Dreyer’s German Archaeological Institute team in 1988 and published substantially in *Umm el-Qaab I* in 1998.

The signs include:

- vertical strokes;
- horizontal or bow-shaped strokes;
- a spiral/curled-rope form.

Groups combine these signs in limited, rule-governed quantities. Ferrara et al. call them the earliest attested Egyptian numerical symbols: [“Numeracy at the dawn of writing”](https://doi.org/10.1016/j.hm.2020.08.002).

**[R/D]** The tags probably recorded quantities, origins, institutions or deliveries attached to containers. Their exact syntax and whether all labels constitute “full writing” rather than proto-writing remain debated.

**[R]** UCL concludes that the decimal system was already developed by Naqada III, although the entire later seven-power repertoire is not equally demonstrated on every early object: [UCL, “Early numbers”](https://www.ucl.ac.uk/museums-static/digitalegypt/writing/earlynumbers.html).

### Narmer, approximately 3100 BCE

**[A]** The Narmer macehead from the Main Deposit at Hierakonpolis carries large numeral groups associated with cattle, caprids and a bound captive. It is one of the earliest spectacular demonstrations of decimal notation beyond small tallies.

**[R]** Its totals have usually been interpreted as booty or tribute presented to the king.

**[D]** The political scene has been variously understood as conquest celebration, royal jubilee, marriage or ritual presentation. The numbers cannot by themselves prove the event depicted.

### First and Second Dynasties, approximately 3000–2686 BCE

**[A]** Pottery, labels, sealings and administrative material attest routine numeracy. A First Dynasty flint from Giza bearing numerical signs is illustrated by [UCL](https://www.ucl.ac.uk/museums-static/digitalegypt/writing/earlynumbers.html).

**[R]** The growth of royal estates, taxation, redistribution and mortuary provisioning supplies a persuasive institutional context for the system. It is nevertheless a reconstruction from objects, not an Egyptian origin story.

### Hesy-Ra, early Third Dynasty, approximately 2650 BCE

**[A]** The mastaba of Hesy-Ra at Saqqara contained famous carved wooden panels and administrative/title inscriptions. Numerical and accounting practices were established by this period.

**Qualification:** the tomb is often named in popular histories as an early illustration of hieroglyphic numeration, but it is not the earliest attestation; Tomb U-j and Early Dynastic labels precede it by centuries. Claims that the complete system was “invented at the tomb of Hesy-Ra” are unsupported.

### Old Kingdom evidence

**[A]** Numerals occur in offering lists, estate accounts, construction records, calendar dates and measurements. Mathematical practice is largely reconstructed from administrative and architectural evidence because no Old Kingdom mathematical textbook comparable to Rhind survives.

**Absence of evidence:** no surviving Egyptian source identifies an inventor of the numeral signs, describes their first adoption or says that they were borrowed from a neighboring culture.

### Akhmim/Cairo wooden tablets, about 1950 BCE

**[A]** Cairo Museum **CG 25367–25368**, traditionally dated to year 38 of an unnamed king, probably Senwosret I, contain division of *heqat* quantities and checks by recombination. Georges Daressy reported them in 1901 and published them in 1906.

### Lahun mathematical papyri, approximately 1850–1800 BCE

**[A]** Fragments from Petrie’s excavations at Lahun include tables and worked problems. UCL **UC 32159** preserves part of a \(2/n\) table, with decompositions matching the later Rhind Papyrus.

This agreement is powerful evidence for a transmissible scribal curriculum rather than isolated improvisation.

### Moscow Mathematical Papyrus, approximately 1850 BCE

**[A]** Also called the Golenishchev Papyrus, now Pushkin State Museum **Papyrus Moscow 4676**. Vladimir Golenishchev bought it in Egypt in 1892 or 1893; Vasily Struve published a major edition in 1930.

Its 25 problems include:

- calculation of areas;
- divisions and ratios;
- a procedure for the volume of a square frustum.

Problem 14 uses base side 4, top side 2 and height 6, producing 56:

\[
(4^2+4\cdot2+2^2)\times \frac63=56.
\]

**[A]** The algorithm and answer are in the papyrus.

**[R/D]** The modern symbolic formula is our algebraic restatement. The papyrus provides no derivation, so claims about how Egyptians discovered or proved it are reconstructions. See the detailed history-of-mathematics discussion of [Moscow Problem 14](https://doi.org/10.1016/j.hm.2011.06.001).

### Rhind Mathematical Papyrus, approximately 1550 BCE

**[A]** British Museum **EA10057 and EA10058**, with connecting fragments formerly in the New-York Historical Society and now associated with the Brooklyn Museum collection.

- acquired at Thebes by Alexander Henry Rhind around 1858;
- probably found near the Ramesseum;
- written by the scribe Ahmose/Ahmes;
- dated to year 33 of the Hyksos king Apophis;
- described by the British Museum as containing 84 problems plus tables.

The catalogue is authoritative for the object: [British Museum EA10057](https://www.britishmuseum.org/collection/object/Y_EA10057).

**[A]** Ahmose says he copied from an older document of the time of Nymaatre, Amenemhat III.

**Qualification:** this establishes Ahmose’s claim about his exemplar. It does not prove that every problem originated under Amenemhat III, much less that the surviving roll is physically an Old Kingdom document.

### Egyptian Mathematical Leather Roll, approximately 1650 BCE

**[A]** British Museum **EA10250**, acquired with the Rhind collection. Although acquired in the nineteenth century, it was not successfully softened and unrolled until 1927. It lists equivalent unit-fraction decompositions.

**[R]** It is frequently described as a student exercise or table; that is an inference from form and repetition, not an ancient title.

### New Kingdom, approximately 1550–1070 BCE

**[A]** Mathematical and metrological knowledge appears in:

- the Rhind roll;
- ostraca used by trainee and working scribes;
- Deir el-Medina ration, payroll and work-attendance records;
- architectural plans and measurements;
- Papyrus Anastasi I;
- the Wilbour Papyrus;
- Papyrus Harris I;
- the Turin Taxation Papyrus.

The Great Wilbour Papyrus, Brooklyn Museum **34.5596**, has about 4,500 recto lines and records measurement and assessment of fields: [Brooklyn Museum catalogue](https://opencollection.brooklynmuseum.org/objects/152126).

The Turin Taxation Papyrus, Museo Egizio **Cat. 1895**, records a tax-collecting expedition in year 12 of Ramesses XI: [Museo Egizio catalogue](https://collezioni.museoegizio.it/en-GB/material/Cat_1895).

### Demotic era, seventh century BCE–fifth century CE

**[A]** Demotic became the principal Egyptian script for administration and law under the Saite rulers and continued under Persian, Ptolemaic and Roman government.

**[A]** The Rosetta Stone decree of 196 BCE demonstrates coexistence of:

- formal hieroglyphic;
- Demotic Egyptian;
- Greek.

**[A]** The last dated Demotic text is a graffito at Philae dated 11 December 452 CE. See the [Global Egyptian Museum’s Demotic chronology](https://www.globalegyptianmuseum.org/glossary.aspx?id=130).

---

## Arithmetic and instruments

### 1. Addition and subtraction

Hieroglyphic addition is conceptually concatenation followed by exchange:

- combine like signs;
- whenever ten identical signs accumulate, replace them with one sign of the next power.

Subtraction reverses the process: exchange a higher unit for ten lower units when necessary.

**[R]** Physical counters could make these operations intuitive, but the surviving mathematical papyri generally show written intermediate results. There is no securely documented standard Egyptian abacus comparable to the later Roman counting board, Chinese *suanpan* or Japanese *soroban*.

### 2. Multiplication by doubling

Egyptian multiplication used repeated doubling and addition.

To multiply \(13\times12\):

| Selected? | Multiplier | Multiplicand |
|---|---:|---:|
| ✓ | 1 | 12 |
|  | 2 | 24 |
| ✓ | 4 | 48 |
| ✓ | 8 | 96 |

Because \(13=1+4+8\):

\[
12+48+96=156.
\]

**[A]** Rhind computations explicitly use such doubling tables, often marking the chosen rows.

**Qualification:** “Egyptian multiplication” is a modern name. Doubling was prominent but not the only imaginable operation; scribes also halved, took prescribed fractions, added and used memorized tables.

### 3. Division

Division was often performed as multiplication in reverse: find which multiples of the divisor sum to the dividend. Fraction tables supplied decompositions for nonintegral results.

The Rhind \(2/n\) table gives unit-fraction representations for odd \(n\) from 3 to 101. The related \(1\)–\(9\) divided by 10 table served decimal-looking but non-positional metrological work.

### 4. Unit-fraction algorithms

The papyri show:

- halving;
- doubling unit fractions;
- transformation through common factors;
- use of auxiliary red numbers;
- checking by recomposition.

**[A]** The results are documented.

**[D]** Scholars have repeatedly proposed a single master rule governing the Rhind \(2/n\) choices. No proposal explains every entry beyond dispute. UCL warns that modern optimization criteria can impose patterns foreign to Egyptian practice.

### 5. False position

Rhind “quantity” problems use a technique now called false position. A convenient trial value is assumed, operated on according to the question, and scaled to produce the required result.

**[M]** Describing these as “linear equations” is useful translation into modern mathematics, but the manuscripts contain rhetorical instructions, not symbolic expressions such as \(x+x/7=19\).

### 6. Geometry and measurement

The papyri treat:

- rectangular and triangular fields;
- circular areas;
- granary volumes;
- pyramid slopes or *seqed*;
- cylindrical and basket-like volumes;
- the square frustum.

Rhind Problem 50 effectively computes the area of a circle of diameter 9 by taking the square of 8. This is equivalent to \(\pi\approx256/81\), but:

- **[A]** the procedure “subtract one ninth of the diameter and square the remainder” is textual;
- **[M]** attributing the explicit constant \(256/81\) or a theory of \(\pi\) to Ahmose is modern algebraic interpretation.

### 7. Instruments

#### Finger reckoning

**[R]** Finger counting is a plausible contributor to decimal organization. Human anatomy supplies an obvious model for ten, and Egyptian images show gestures with enumerative meanings.

**Absence:** no surviving Egyptian arithmetic manual gives a systematic finger-reckoning code comparable to later Greek and Roman descriptions.

#### Counting boards and counters

**[R/D]** Egyptians undoubtedly moved, grouped and measured physical commodities, but a canonical Egyptian place-value counting board has not been securely identified. Grooved boards and game boards should not automatically be called abaci.

#### Measuring instruments

Better-attested tools include:

- cubit rods;
- measuring cords;
- balances and weights;
- grain measures;
- scribal palettes;
- survey and architectural grids.

The finger sign for 10,000 also participates in words concerning precision and measurement, which may help explain its numeral use; that remains semantic reconstruction rather than a recorded origin.

#### Non-Egyptian instruments in the template

The *suanpan*, *soroban*, Roman *calculus*, European counter-casting, quipu and Chinese rod numerals did not form part of ancient Egyptian arithmetic. Likewise the medieval algorist–abacist contest belongs to the European reception of Hindu-Arabic arithmetic, not Egyptian transmission.

### 8. Textbook form

UCL characterizes the approximately 100 surviving Egyptian mathematical problems as:

- **rhetorical:** written in prose rather than symbolic algebra;
- **numerical:** using concrete values;
- **algorithmic:** presenting ordered operations.

The opening often names the problem type; red ink can mark headings; stepwise instructions lead to a checked result. See [UCL, “Problem texts”](https://www.ucl.ac.uk/museums-static/digitalegypt/lahun/mathproblems.html).

---

## Transmission and replacement

### Indigenous development versus borrowing

**[R]** The simplest reconstruction is local development within late Predynastic administration: tally-like strokes expanded into a decimal repertoire as royal institutions recorded goods and labor.

**[D]** Egypt and Mesopotamia were in contact during the late fourth millennium BCE. Some motifs and technologies travelled, but no Mesopotamian numeral series provides a direct sign-by-sign prototype for the Egyptian decimal powers.

**[D]** Egyptian influence on Aegean decimal notation has been proposed because of structural similarity and contact, but the evidence does not permit a simple family tree.

### Hieroglyphic to hieratic

This is not a foreign borrowing. Hieratic is the cursive written counterpart of Egyptian monumental script, but its numeral subsystem became increasingly ciphered.

The Greek name *hieratika*, “priestly,” reflects a later contrast. Before Demotic arose around 700 BCE, cursive Egyptian served ordinary administrative as well as religious purposes. [UCL’s hieratic overview](https://www.ucl.ac.uk/museums-static/digitalegypt/writing/hieratic.html) stresses this anachronism.

### Hieratic to Demotic

Demotic grew from northern cursive administrative writing and displaced “abnormal hieratic” in much administration. Its Egyptian designation meant “document writing”; “demotic,” Greek for “popular,” is an outsider’s label.

### Possible influence on Greek alphabetic numerals

**[R/D]** Stephen Chrisomalis argues that Ionian Greeks in Lower Egypt around the early sixth century BCE adapted the *structure* of Demotic ciphered-additive numerals—nine units, nine tens, nine hundreds—while using Greek alphabetic characters.

Evidence offered:

- close structural correspondence;
- appropriate chronology;
- Ionian mercantile activity in Egypt;
- lack of an obvious earlier Greek structural ancestor.

Limitations:

- the actual signs are not derived from Demotic;
- no bilingual manual records the act of borrowing;
- independent elaboration of alphabetic values remains possible.

### Greek, Coptic and Roman Egypt

Following Alexander’s conquest in 332 BCE and especially under the Ptolemies, Greek numerical practices coexisted with Egyptian ones. Egyptian Demotic remained vigorous in temples, law and local administration.

Coptic adopted the Greek alphabet and Greek alphabetic numeration rather than retaining Demotic numeral ciphers. The [Claremont Coptic Encyclopedia](https://ccdl.claremont.edu/digital/collection/cce/id/1471/) explicitly describes this replacement.

### Arabic administration

Greek remained an official administrative language after Rome annexed Egypt in 30 BCE and was replaced by Arabic in government during the early eighth century, traditionally dated to 706 CE. Egyptian Christians continued using Coptic much longer.

Later Egyptian accounting employed forms variously called Coptic, *ḥurūf al-zimām*, Rūmī or Fāsī numerals. These have mixed histories involving Greek/Coptic alphabetic numeration and regional administrative conventions; they are not straightforward continuations of the seven hieroglyphic signs. See Cambridge’s [Genizah numerals survey](https://genizahfragments.lib.cam.ac.uk/2021/06/02/coptic-numerals-and-genizah-studies/).

### No India-to-Baghdad-to-Egypt descent

The later Hindu-Arabic positional system reached the Islamic world from India and eventually became standard in Egypt. That process replaced indigenous and alphabetic accounting systems; it did not develop from the hieroglyphic stroke–hobble–coil series.

Consequently:

- al-Khwarizmi’s *ḥisāb al-hind*;
- Fibonacci’s *Liber Abaci*;
- the 1299 Florentine restriction on Hindu-Arabic commercial numerals;
- medieval algorists and abacists;
- Napier’s logarithms;

belong to the later history of the notation that displaced Egyptian numerals, not to its direct transmission.

---

## People

### Ancient actors

#### Narmer, approximately 3100 BCE

**[A]** King named on the ceremonial macehead bearing the best-known Early Dynastic large-number groups.

**[D]** Identification of Narmer with the Menes of later king lists is debated. The macehead does not call him “inventor of numerals.”

#### Hesy-Ra, early Third Dynasty

**[A]** High official, “chief of scribes” among other titles, buried at Saqqara.

**[L]** Calling him the inventor of mathematics or the numeral system is unsupported.

#### Amenemhat III, reigned approximately 1860–1814 BCE under one standard chronology

**[A/T]** Ahmose’s colophon associates the Rhind exemplar with the reign of Nymaatre, Amenemhat III. That makes his reign a textual point of transmission, not proof of royal authorship.

#### Ahmose/Ahmes, seventeenth–sixteenth century BCE

**[A]** Named scribe of the Rhind Papyrus. He is the earliest named copyist of a substantial surviving mathematical work.

**Qualification:** “the first named mathematician” is a modern honorific. The document identifies him as scribe and copyist, not as originator of every method.

### Discoverers, editors and decipherers

#### James Quibell and Frederick Green

Excavated the Main Deposit at Hierakonpolis in 1897–98, including the Narmer macehead.

#### Günter Dreyer, 1943–2019

Directed the excavation and publication of Tomb U-j. His 1998 report made its tags central to debates over the earliest Egyptian writing.

#### Alexander Henry Rhind, 1833–1863

Scottish antiquarian who acquired the mathematical papyrus at Thebes around 1858. The modern name honors the collector rather than its ancient scribe.

#### Vladimir Golenishchev, 1856–1947

Purchased the Moscow Mathematical Papyrus in Egypt in 1892 or 1893.

#### Thomas Young, 1773–1829

**[A]** Identified many Demotic signs and words and published an important “Egypt” article for the *Encyclopaedia Britannica* in 1819. His comparative work included numerical signs.

#### Jean-François Champollion, 1790–1832

**[A]** Announced his major phonetic breakthrough in the 1822 *Lettre à M. Dacier* and developed the system in his 1824 *Précis*.

**[D]** Priority disputes between Young and Champollion began in their lifetimes. Young made indispensable partial advances; Champollion established the broader linguistic decipherment. The [British Museum’s decipherment timeline](https://www.britishmuseum.org/exhibitions/hieroglyphs-unlocking-ancient-egypt/egyptian-hieroglyphs-decipherment-timeline) and its [Dacier-letter essay](https://www.britishmuseum.org/blog/eureka-finding-key-ancient-egypt) document the sequence.

#### August Eisenlohr, 1832–1902

Published the first major edition of the Rhind Papyrus in 1877.

#### T. Eric Peet, 1882–1934

Published a new edition of the Rhind Papyrus in 1923 and challenged a simple derivation of fraction signs from the Eye of Horus.

#### Arnold Buffum Chace, 1845–1932

Led the 1927–29 edition, translation and photographic publication of the Rhind Papyrus.

#### Georg Möller, 1876–1921

Compiled *Hieratische Paläographie* and in 1911 advanced the Eye-of-Horus origin theory for the *heqat* fraction signs.

#### Vasily Struve, 1889–1965

Published the Moscow Mathematical Papyrus in 1930.

#### Alan Gardiner, 1879–1963

His *Egyptian Grammar* systematized numeral grammar and supplied the sign-list identifiers now embedded in Unicode nomenclature.

#### Carl B. Boyer, 1906–1976

Emphasized hieratic “cipherization” in histories of mathematical notation.

#### Richard J. Gillings, 1908–1996

Published *Mathematics in the Time of the Pharaohs* (1972), an influential mathematical reading of the papyri.

#### Annette Imhausen

Her *Mathematics in Ancient Egypt: A Contextual History* (2016) is the leading recent synthesis emphasizing scribal institutions, genres and social context rather than extracting timeless modern mathematics.

#### Stephen Chrisomalis

His *Numerical Notation: A Comparative History* (2010) is the standard cross-cultural classificatory survey and the source of the influential demotic-to-Greek structural-transmission hypothesis.

---

## Culture and use

### Administration and taxation

**[A]** Numerals were ubiquitous in records of:

- cattle and grain;
- rations and wages;
- field areas and tax assessments;
- temple income;
- work attendance;
- inventories and deliveries.

This mundane use probably dwarfed surviving “pure mathematics.” Papyrus normally decays, while monumental stone survives, so the extant sample strongly distorts the original balance.

### Law

**[A]** Demotic contracts quantify prices, interest, annuities, property shares, rents and penalties. Ptolemaic law required increasingly elaborate registration and Greek abstracts. A translation of the third-century BCE Hermopolis code is available at [Attalus](https://www.attalus.org/egypt/demotic_legal_code.html).

### Calendars and dates

Egyptian dates normally state:

- regnal year;
- season;
- month;
- day.

The civil year comprised three four-month seasons of 30-day months, plus five epagomenal days. Numeral signs therefore recur in royal annals, temple rituals, labor journals and astronomical calendars.

### Metrology

Numerals were inseparable from units:

- cubit and its subdivisions;
- *heqat* for grain capacity;
- *deben* and *qedet* for weight;
- *setat* for area;
- labor-days and rations.

A bare modern conversion may conceal that Egyptian algorithms were tied to particular units and subdivisions.

### Religion and monumentality

Numbers appear in:

- offering formulas—“a thousand of bread, beer, cattle and fowl”;
- enumerations of divine beings and ritual repetitions;
- astronomical ceilings and calendars;
- king lists and regnal years;
- statements of defeated enemies and captured wealth.

**[R]** Repeated “thousands” or Heh/million signs may be numerically exact in an account but hyperbolic in royal or funerary rhetoric.

### Literature

The Rhind Papyrus’s cat-and-mouse progression has often been compared with the later “As I was going to St Ives” family of riddles.

- **[A]** Rhind Problem 79 contains the powers of seven.
- **[R]** Léon Rodet noted a similar problem in Fibonacci’s *Liber Abaci*.
- **[D]** Direct continuous transmission from pharaonic Egypt to Fibonacci and the nursery rhyme is possible in the broad sense that problems travel, but no chain of manuscripts documents it.

### Coins

Coinage was not central to most pharaonic Egyptian economic history. Regular royal coinage developed late, especially under the Ptolemies, and commonly used Greek legends and marks. Demotic numerals remained important in receipts and accounts even when the monetary unit itself was Greek or Ptolemaic.

### Gematria, isopsephy and chronograms

Egyptian script could exploit sound, image and number symbolically, but:

- **[A]** Greek isopsephy and Hebrew gematria assign numerical values to alphabetic letters.
- **[A]** Egyptian numerals are separate signs, not a general letter-number alphabet.
- **[L]** Modern “Egyptian alphanumerics” theories that assign canonical numerical values to all hieroglyphs and derive Greek, Hebrew or English letter-values from them lack acceptance in Egyptology and lack an ancient conversion table.
- **[A/R]** Greek isopsephy did exist in Greco-Roman Egypt, but that is Greek alphabetic practice conducted in an Egyptian cultural setting.

### Modern typography and art

Egyptian numeral signs entered modern type through Egyptological fonts, Gardiner codes, Manuel de Codage and Unicode.

They now appear in:

- museums and education;
- tattoos and jewelry;
- games and historical fiction;
- calculator websites;
- decorative “pharaoh fonts.”

**[M]** Horizontally aligned strings in modern sans-serif hieroglyphic fonts suppress much of the original variation in scale, orientation, color and quadrat arrangement.

Old-style Arabic figures, clock numerals and Roman numerals are unrelated typographic traditions.

### Descendant words

The requested words do not descend from Egyptian numerals:

- *calculus*: Latin “pebble”;
- *digit*: Latin *digitus*, finger;
- *cipher* and *zero*: ultimately Sanskrit *śūnya* through Arabic *ṣifr* and medieval Romance/Latin forms;
- *algorithm*: from al-Khwarizmi’s Latinized name;
- *abacus*: Greek/Latin, with deeper etymology disputed.

Possible superficial parallels—Egypt’s finger sign for 10,000 versus Latin *digitus*, for example—are not etymological descent.

---

## Controversies and disputes

### 1. Was Egyptian numeration invented independently?

**Evidence for local development**

- very early Tomb U-j numerical tags;
- integration with Egyptian administrative labels;
- distinctive decimal power-signs;
- no foreign prototype matching their forms.

**Evidence sometimes cited for influence**

- contemporary Egyptian–Mesopotamian exchange;
- broader Near Eastern movement of prestige objects and administrative ideas.

**Assessment:** independent Egyptian elaboration is the economical reconstruction, but “independent” need not mean cultural isolation. The precise stimulus is unknown.

### 2. Are the Tomb U-j marks really numbers?

**For:** limited repetition, combination rules and similarity to later numeral signs strongly support numerical interpretation.

**Against or qualifying:** some tags remain semantically obscure; numerical value does not by itself tell us what was counted; “first writing” depends on the definition of writing.

### 3. Are the Narmer totals literal?

**For:** the signs yield coherent large decimal numbers and sit beside counted categories.

**Against:** quantities such as 1,422,000 goats are extraordinarily large and occur on ceremonial royal art. They may be standardized claims, accumulated tribute or ideological magnification.

**Finding:** the numeral reading is much more secure than the historical literalness of the totals.

### 4. Did Egyptians have zero?

Three different claims are often conflated:

| Claim | Evidence | Finding |
|---|---|---|
| They understood “nothing remains” | *nfr* in accounts | **Documented contextual concept** |
| They marked a neutral/reference level | architectural or surveying usage of *nfr* | **Contextually documented/reconstructed** |
| They possessed 0 as a general number and positional digit | absent from the numeral algorithms | **Not supported** |

Thus “Egypt had no zero” is too broad, while “Egypt invented our zero” is also false.

### 5. Eye of Horus fractions

The strong claim—hieratic fractions were invented by drawing pieces of Horus’s eye—is undermined by palaeographic chronology. The weaker claim—that New Kingdom scribes or artists associated pre-existing measure signs with eye components—also lacks decisive textual proof, though it is historically more plausible.

The polished schoolroom diagram is principally a twentieth-century popular construction derived from Möller, Peet and Gardiner.

### 6. Did the six fractions intentionally omit \(1/64\) for Thoth to restore?

**[L/M]** They sum to \(63/64\), but no known Egyptian source states that Thoth supplied the missing fraction as a mathematical moral. The “missing sixty-fourth” story is a modern fusion of arithmetic observation and myth.

### 7. Was Heh exactly one million?

**[A]** It can function numerically as one million.

**[A]** It also signifies enormous, indefinite or eternal multiplicity.

Context, not the isolated sign, decides whether an exact modern integer is intended.

### 8. Was hieratic positional?

No. Its more compact signs can resemble digits, but position does not multiply their value. It is ciphered-additive.

Calling it “decimal” is correct with respect to powers and grouping; calling it a “decimal place-value system” is not.

### 9. Did hieratic numerals create the Greek alphabetic system?

Chrisomalis’s proposal is structurally and historically serious but not universally proven. It concerns the organization of values, not the graphic derivation of Greek letters from Egyptian number-signs.

### 10. Did the shapes of modern digits come from Egyptian signs?

**[L]** There is no accepted sequence from hobble, coil, lotus and tadpole to 0–9.

**[L]** The tale that each modern Arabic digit contains as many angles as its value is a modern diagram imposed on late, variable glyphs. Historical Indian, Arabic and European forms do not follow it consistently.

### 11. Were pyramids built using lost advanced algebra?

**[A]** Egyptian surveyors and scribes had effective numerical procedures.

**[R]** Modern equations can express those procedures elegantly.

**[L/D]** Claims of symbolic algebra, calculus, encoded universal constants or modern engineering theory must be demonstrated from texts, not inferred merely because monuments are impressive. The surviving sources are rhetorical and numerical, not algebraic in modern notation.

### 12. Colonial naming and ownership

“Rhind Papyrus,” “Moscow Papyrus” and “Golenishchev Papyrus” are modern collector/location names. “Ahmose Papyrus” foregrounds the ancient scribe but is less standard.

**[A]** The acquisition histories are documented.

**[D]** The ethical and legal evaluation of nineteenth-century collecting is a modern debate; the historical catalogue facts should not be confused with endorsement.

### 13. Errors in grand universal histories

Karl Menninger’s *Number Words and Number Symbols* remains rich and useful but reflects mid-twentieth-century classifications. Georges Ifrah’s works contain an extraordinary visual compilation and many stimulating comparisons, but reviewers have identified erroneous dates, unsupported diffusion stories and bibliographic weaknesses.

Joseph Dauben’s review and comments by specialists including Jim Ritter and Jean-Claude Martzloff specifically warn that apparent comprehensiveness is not a substitute for checking objects and specialist editions. Ifrah should therefore be used as a guide to claims, not as final authority.

---

## Open questions

1. What commodities and administrative categories were encoded by each Tomb U-j tag?
2. How much of the complete later decimal repertoire existed before the First Dynasty?
3. What semantic or mnemonic processes assigned the hobble, coil, lily, finger and tadpole their powers?
4. How uniform was numerical training between temples, royal administration and provincial offices?
5. How much calculation occurred mentally or with perishable counters rather than on surviving papyrus?
6. What rules, if any, governed every choice in the Rhind \(2/n\) table?
7. How was the Moscow frustum procedure discovered and justified?
8. Did New Kingdom users themselves connect *heqat* fraction signs to the wedjat eye?
9. How direct was the structural influence of Demotic numeration on Greek alphabetic numerals?
10. How were competing Greek, Demotic, Coptic and later Arabic notations selected in multilingual households and offices?
11. How often does Heh represent an exact million rather than rhetorical innumerability?
12. Can additional unpublished ostraca materially change the standard history, which is based disproportionately on a few famous school texts?

---

## Sources and editions consulted

### Primary artefacts and museum catalogues

- British Museum. “The Rhind Mathematical Papyrus,” EA10057:  
  https://www.britishmuseum.org/collection/object/Y_EA10057
- British Museum collection search, EA10057–EA10058:  
  https://www.britishmuseum.org/collection/search?title=The+Rhind+Mathematical+Papyrus
- Ashmolean/Narmer Catalogue. Narmer Macehead, AN1896–1908.E.3631:  
  https://narmer.org/inscription/0080.pdf
- McNamara, Liam. “The Narmer Mace-Head,” *Nekhen News* 31:  
  https://www.hierakonpolis-online.org/files/hk_nn/nn-31-2019.pdf
- Brooklyn Museum. Great Wilbour Papyrus, 34.5596:  
  https://opencollection.brooklynmuseum.org/objects/152126
- Museo Egizio. Turin Taxation Papyrus, Cat. 1895:  
  https://collezioni.museoegizio.it/en-GB/material/Cat_1895
- Staatliche Museen zu Berlin. Hieratic temple-land tax list, P 23251/02 + P 23252 + P 23253:  
  https://search.smb.museum/object/obj-834624
- Institute for the Study of Ancient Cultures. Demotic Ostraca Online:  
  https://isac.uchicago.edu/research/projects/isac-museum-demotic-ostraca-online
- Muhs, Brian. *Catalogue of the Early Ptolemaic Ostraca in the Nelson Collection*, OIP 126:  
  https://isac-idb-static.uchicago.edu/multimedia/532/OIP126.pdf
- Attalus. Demotic Legal Code of Hermopolis West, P. Mattha/TM 48855:  
  https://www.attalus.org/egypt/demotic_legal_code.html

### Mathematical texts and editions

- Chace, Arnold Buffum et al. *The Rhind Mathematical Papyrus*, 2 vols., 1927–29, online scan:  
  https://upload.wikimedia.org/wikipedia/commons/7/7b/The_Rhind_Mathematical_Papyrus%2C_Volume_I.pdf
- Peet, T. Eric. *The Rhind Mathematical Papyrus*, 1923; contemporary review:  
  https://www.ams.org/journals/bull/1924-30-09/S0002-9904-1924-03960-3/S0002-9904-1924-03960-3.pdf
- MacTutor History of Mathematics. “Mathematics in Egyptian Papyri”:  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Egyptian_papyri/
- UCL Digital Egypt. Lahun mathematical problem texts:  
  https://www.ucl.ac.uk/museums-static/digitalegypt/lahun/mathproblems.html
- UCL Digital Egypt. Lahun \(2/n\) table, UC 32159:  
  https://www.ucl.ac.uk/museums-static/digitalegypt/lahun/uc32159.html
- Imhausen, Annette. “Mathematical Fragments from Lahun: Introduction”:  
  https://www.ucl.ac.uk/museums-static/digitalegypt/pdf/01%20Introduction.pdf
- Imhausen, Annette. *Mathematics in Ancient Egypt: A Contextual History*. Princeton University Press, 2016. Review and bibliographic description:  
  https://old.maa.org/node/743418/  
  https://www.journals.uchicago.edu/doi/full/10.1086/693357
- Rossi, Corinna. “Did Egyptian scribes have an algorithmic means for determining the circumference of a circle?” *Historia Mathematica*; includes Moscow Problem 14 discussion:  
  https://doi.org/10.1016/j.hm.2011.06.001

### Numeral systems, palaeography and language

- Chrisomalis, Stephen. *Numerical Notation: A Comparative History*. Cambridge University Press, 2010:  
  https://books.google.com/books?id=ux--OWgWvBQC
- Chrisomalis, Stephen. Accessible publisher/prepublication PDF:  
  https://glossographia.files.wordpress.com/2010/01/chrisomalis-numerical-notation.pdf
- Davis, Ernest. Review of Chrisomalis:  
  https://cs.nyu.edu/~davise/papers/OldReviews/Chrisomalis.pdf
- Ferrara, Silvia et al. “Numeracy at the dawn of writing: Mesopotamia and beyond,” *Historia Mathematica* 2021:  
  https://doi.org/10.1016/j.hm.2020.08.002
- Gardiner, Alan H. *Egyptian Grammar*, 3rd ed., Oxford, 1957; sections 259–266 on numerals:  
  https://mjn.host.cs.st-andrews.ac.uk/egyptian/grammars/Gardiner.pdf
- Möller, Georg. *Hieratische Paläographie: Die ägyptische Buchschrift in ihrer Entwicklung von der fünften Dynastie bis zur römischen Kaiserzeit*, 3 vols., 2nd ed., Leipzig.
- UCL Digital Egypt. “Early numbers”:  
  https://www.ucl.ac.uk/museums-static/digitalegypt/writing/earlynumbers.html
- UCL Digital Egypt. “Hieratic script”:  
  https://www.ucl.ac.uk/museums-static/digitalegypt/writing/hieratic.html
- UCL Digital Egypt. “Demotic”:  
  https://www.ucl.ac.uk/museums-static/digitalegypt/writing/demotic.html
- Global Egyptian Museum. “Demotic”:  
  https://www.globalegyptianmuseum.org/glossary.aspx?id=130
- Bibliotheca Alexandrina. “Cardinal numbers”:  
  https://www.bibalex.org/learnhieroglyphs/Lesson/LessonDetails_En.aspx?l=64
- Thesaurus Linguae Aegyptiae, Berlin-Brandenburg Academy:  
  https://thesaurus-linguae-aegyptiae.de/

### Unicode and digital representation

- Unicode Standard 16.0, chapter 11, Egyptian Hieroglyphs:  
  https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-11/
- Unicode Egyptian Hieroglyphs chart:  
  https://www.unicode.org/charts/PDF/U13000.pdf
- Unicode Egyptian Hieroglyphs Extended-A chart:  
  https://www.unicode.org/charts/PDF/U13460.pdf
- Unicode Egyptian Hieroglyph Format Controls:  
  https://www.unicode.org/charts/nameslist/n_13430.html
- Unicode Technical Note 32, Manuel de Codage mapping:  
  https://www.unicode.org/notes/tn32/
- Unicode Annex 57, Unikemet database:  
  https://www.unicode.org/reports/tr57/

### Fractions and the Eye of Horus controversy

- Ritter, Jim. “Horus-eye Fractions,” *Encyclopedia of Ancient History*:  
  https://onlinelibrary.wiley.com/doi/abs/10.1002/9781444338386.wbeah21178
- MathWorld. “Eye of Horus Fraction”:  
  https://mathworld.wolfram.com/EyeofHorusFraction.html
- UCL, UC 32159 fraction table:  
  https://www.ucl.ac.uk/museums-static/digitalegypt/lahun/uc32159.html

### Origins of Egyptian writing

- Oxford Academic. “The Origins and Early Development of Writing in Egypt”:  
  https://academic.oup.com/edited-volume/43506/chapter/364131674
- Dreyer, Günter et al. *Umm el-Qaab I: Das prädynastische Königsgrab U-j und seine frühen Schriftzeugnisse*. Archäologische Veröffentlichungen 86. Mainz, 1998.
- Ferrara et al., numerical signs from U-j:  
  https://doi.org/10.1016/j.hm.2020.08.002

### Decipherment

- British Museum. “How Egyptian hieroglyphs were decoded”:  
  https://www.britishmuseum.org/exhibitions/hieroglyphs-unlocking-ancient-egypt/egyptian-hieroglyphs-decipherment-timeline
- British Museum. “Eureka! Finding the key to ancient Egypt”:  
  https://www.britishmuseum.org/blog/eureka-finding-key-ancient-egypt
- Yale Peabody Museum. Champollion’s *Précis du système hiéroglyphique*:  
  https://echoesofegypt.peabody.yale.edu/hieroglyphs/pr-cis-du-syst-me-hi-roglyphique-des-anciens
- Young, Thomas. “Egypt,” *Encyclopaedia Britannica* supplement, 1819.
- Young, Thomas. *An Account of Some Recent Discoveries in Hieroglyphical Literature and Egyptian Antiquities*. London, 1823.
- Champollion, Jean-François. *Lettre à M. Dacier*. Paris, 1822.
- Champollion, Jean-François. *Précis du système hiéroglyphique des anciens Égyptiens*. Paris, 1824.

### Comparative and historiographical works

- Menninger, Karl. *Number Words and Number Symbols: A Cultural History of Numbers*, trans. Paul Broneer. MIT Press, 1969:  
  https://openlibrary.org/books/OL5612154M/Number_words_and_number_symbols  
  https://archive.org/details/numberwordsnumbe00menn
- Ifrah, Georges. *The Universal History of Numbers*, trans. David Bellos et al. Wiley, 2000. Bibliographic review:  
  https://www.kirkusreviews.com/book-reviews/georges-ifrah/a-universal-history-of-numbers/
- Dauben, Joseph W. “The Universal History of Numbers and The Universal History of Computing,” *Notices of the AMS* 49.1 (2002), 32–38:  
  https://www.ams.org/notices/200201/rev-dauben.pdf
- Cajori, Florian. *A History of Mathematical Notations*, vol. 1, Egyptian section:  
  https://en.wikisource.org/wiki/A_History_of_Mathematical_Notations/Volume_1/Egyptians
- Boyer, Carl B. *A History of Mathematics*, Egyptian chapter:  
  https://www.hlevkin.com/hlevkin/90MathPhysBioBooks/mathHistory/Boyer-AHistoryOfMathematics.pdf
- Gillings, Richard J. *Mathematics in the Time of the Pharaohs*. MIT Press, 1972.
- Claremont Coptic Encyclopedia. “Numerical System, Coptic”:  
  https://ccdl.claremont.edu/digital/collection/cce/id/1471/
- Cambridge Genizah Research Unit. “‘Coptic’ numerals and Genizah studies”:  
  https://genizahfragments.lib.cam.ac.uk/2021/06/02/coptic-numerals-and-genizah-studies/

