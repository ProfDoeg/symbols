# Brahmi numerals and the Indian decimal place-value system: Research Dossier

## Method and evidentiary labels

This dossier distinguishes several kinds of statement:

- **[A—artefact]** Directly attested by a surviving inscription, manuscript, coin, or other object.
- **[T—text]** Explicitly stated in a surviving historical text, though the witness may be later than its composition.
- **[R—reconstruction]** A conclusion inferred by modern scholarship from palaeography, linguistic comparison, mathematical structure, or transmission history.
- **[TR—tradition]** A traditional attribution or story in premodern sources.
- **[D—disputed]** A claim for which substantial scholarly disagreement remains.
- **[L—legend]** A story unsupported by contemporary evidence.
- **[M—modern invention]** A recent explanatory tale, reconstruction, or typographic convention sometimes mistaken for ancient fact.

“Brahmi numerals” and “the Indian decimal place-value system” must not be treated as exact synonyms. The former was initially a non-positional system with separate signs for units and tens and multiplicative constructions for hundreds and thousands. The latter used nine digit signs repeatedly by position, together with an explicit placeholder zero. The historical achievement lies partly in the transition between them, not in finding the finished modern system in third-century-BCE inscriptions.

---

## Basic identification

| Field | Identification |
|---|---|
| Name | Brahmi numerals; later Indian decimal place-value numerals; in Arabic sources, *ḥisāb al-Hind* or “Indian reckoning” |
| Base | Decimal, base 10 |
| Earliest securely dated period | Mauryan India, third century BCE |
| Early type | Ciphered-additive below 100; multiplicative-additive at 100 and 1,000; non-positional; no zero sign |
| Later type | Positional decimal with nine nonzero digits and a zero placeholder; eventually zero also treated as a number |
| Region | Indian subcontinent; transmitted to Sri Lanka and Southeast Asia, the Islamicate world, Europe, and ultimately worldwide |
| Basic early signs | Separate signs for 1–9, 10–90, 100, and 1,000, though the earliest Ashokan corpus attests only a subset |
| Later signs | Ten digits 0–9 in numerous Brahmi-derived regional forms |
| Period of transition | Roughly the first millennium CE, especially the fifth–ninth centuries |
| Modern descendants | Devanagari, Bengali, Gujarati, Gurmukhi, Tamil, Telugu, Kannada, Malayalam, Sinhala, Khmer, Thai, Lao, Tibetan and other numeral families; Arabic-Indic, Eastern Arabic-Indic, and European “Arabic” figures |

The Unicode Standard separates the two historical layers:

- **Brahmi Numbers:** 𑁒–𑁥, representing 1–9, 10–90, 100, and 1,000.
- **Brahmi Digits:** 𑁦–𑁯, representing positional 0–9.
- **Brahmi Number Joiner:** U+1107F, used electronically to encode multiplicative numeral ligatures.

This separation is historically useful, although Unicode glyphs are normalized representative forms, not facsimiles of every inscription. [Unicode Names List](https://www.unicode.org/charts/nameslist/n_11000.html), [Unicode Core Specification, chapter 14](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-14/).

---

# The system in detail

## 1. The early Brahmi numeral inventory

### Units

| Value | Unicode | Verbal description |
|---:|:---:|---|
| 1 | 𑁒 | A short stroke; early forms may be vertical, later often horizontal |
| 2 | 𑁓 | Two strokes, subsequently joined or cursivized |
| 3 | 𑁔 | Three strokes, subsequently cursivized |
| 4 | 𑁕 | A distinct hooked or crossed sign, varying strongly by period |
| 5 | 𑁖 | A distinct angular/looping sign |
| 6 | 𑁗 | A curved or hooked sign |
| 7 | 𑁘 | A distinct angular sign |
| 8 | 𑁙 | A compound or looping sign |
| 9 | 𑁚 | A curved/hooked sign |

**[A/R]** One, two, and three plausibly began as one, two, and three strokes. The origins of 4–9 are uncertain. The historical shapes vary too much for a single modern font to reproduce the Ashokan, Nana Ghat, Nasik, Gupta, and later regional forms faithfully.

### Tens and higher powers

| Value | Unicode |
|---:|:---:|
| 10 | 𑁛 |
| 20 | 𑁜 |
| 30 | 𑁝 |
| 40 | 𑁞 |
| 50 | 𑁟 |
| 60 | 𑁠 |
| 70 | 𑁡 |
| 80 | 𑁢 |
| 90 | 𑁣 |
| 100 | 𑁤 |
| 1,000 | 𑁥 |

**[A]** The mature early system has twenty basic values: nine units, nine tens, 100, and 1,000. It therefore resembles other “ciphered” systems—such as Greek alphabetic numerals—in having special signs for decimal ranks, but its signs were not simply the ordinary letters of the Brahmi alphabet.

**[A/R]** Its normal structural description is:

- 1–99: ciphered-additive.
- Multiples of 100 and 1,000: multiplicative or ligatured.
- Complex numbers: multiplicative-additive.
- No place-value zero.

Chrisomalis characterizes the system as consistently ciphered-additive below 100 and multiplicative-additive at 100 and 1,000. The Ashokan signs are too sparse to establish every later detail, but the architecture is already substantially visible. [Chrisomalis, *Numerical Notation*](https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20%28CUP%2C%202010%29%28ISBN%200521878187%29%28O%29%28498s%29_MPop_.pdf).

## 2. One to twenty

The table below gives normalized Unicode representations. Actual inscriptions may reverse, stack, fuse, or reshape components.

| Number | Early Brahmi form | Structure | Later positional digits |
|---:|:---:|---|:---:|
| 1 | 𑁒 | one | 𑁧 |
| 2 | 𑁓 | two | 𑁨 |
| 3 | 𑁔 | three | 𑁩 |
| 4 | 𑁕 | four | 𑁪 |
| 5 | 𑁖 | five | 𑁫 |
| 6 | 𑁗 | six | 𑁬 |
| 7 | 𑁘 | seven | 𑁭 |
| 8 | 𑁙 | eight | 𑁮 |
| 9 | 𑁚 | nine | 𑁯 |
| 10 | 𑁛 | ten | 𑁧𑁦 |
| 11 | 𑁛𑁒 | ten + one | 𑁧𑁧 |
| 12 | 𑁛𑁓 | ten + two | 𑁧𑁨 |
| 13 | 𑁛𑁔 | ten + three | 𑁧𑁩 |
| 14 | 𑁛𑁕 | ten + four | 𑁧𑁪 |
| 15 | 𑁛𑁖 | ten + five | 𑁧𑁫 |
| 16 | 𑁛𑁗 | ten + six | 𑁧𑁬 |
| 17 | 𑁛𑁘 | ten + seven | 𑁧𑁭 |
| 18 | 𑁛𑁙 | ten + eight | 𑁧𑁮 |
| 19 | 𑁛𑁚 | ten + nine | 𑁧𑁯 |
| 20 | 𑁜 | special sign for twenty | 𑁨𑁦 |

The positional column is an explanatory normalization using Unicode’s Brahmi digit block. It should not be read as claiming that an Ashokan scribe would have written those forms.

## 3. Tens, hundreds, and thousands

### Tens

The system has separate signs 𑁛–𑁣 for 10, 20, … 90. Thus 37 is structurally “30 + 7,” not three tens and seven units and not the positional sequence “3, 7.”

### Hundreds

A sign for 100 was modified or ligatured with a unit multiplier:

- 100: 𑁤
- 200: “2 × 100,” often a ligature rather than the two freely juxtaposed characters 𑁓𑁤
- 300: “3 × 100”
- …
- 900: “9 × 100”

The exact ordering and fusion vary by inscription. Unicode’s Brahmi Number Joiner was added because plain juxtaposition can mean addition whereas a ligature may express multiplication.

### Thousands

Likewise:

- 1,000: 𑁥
- 2,000: “2 × 1,000”
- 3,000: “3 × 1,000”
- …
- Larger values could combine multiple thousands and lower terms.

Nana Ghat’s 24,400 is analyzed as:

> 1,000 × 20 + 1,000 × 4 + 100 × 4.

This is a particularly clear demonstration that the system is not positional. It decomposes the number into explicitly valued components. Chrisomalis notes that no separate 10,000 sign was required: 10,000 could be expressed as 1,000 × 10. [Chrisomalis](https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20%28CUP%2C%202010%29%28ISBN%200521878187%29%28O%29%28498s%29_MPop_.pdf).

## 4. Ordering

**[A/R]** Higher-valued components normally precede lower-valued ones in the developed epigraphic system. Multipliers could be written beside or incorporated into 100 and 1,000 signs. Because the notation changed across centuries and regions, “left-to-right” is an insufficient universal rule: one must inspect the particular inscription and determine whether adjacency is additive or ligatured-multiplicative.

In Indian spoken and verse numeration, numbers could also be expressed in ascending order—units first—which explains constructions whose verbal order differs from their written order. This later became especially important in word-numeral systems.

## 5. Zero and absence

### Early Brahmi

**[A]** The early ciphered system needs no zero placeholder. A number such as 205 can be written “200 + 5”; no tens position exists that must be filled.

It is therefore misleading to say simply that early Brahmi “lacked the concept of nothing.” What it demonstrably lacked was a zero digit within that notation.

### Positional transition

Once the same nine digits were reused by position, an empty place became ambiguous:

- 25
- 205
- 2,005

A blank could work on a ruled board or in a carefully spaced manuscript, but blanks are fragile in continuous writing. Indian scribes came to use a dot or small circle, called among other things *bindu* (“dot”) and associated with *śūnya* (“empty, void”).

### Bakhshali dot

**[A]** The Bakhshali manuscript uses a dot in decimal place-value numbers.

**[D]** The dot’s conceptual status is debated. The Bodleian publicity described it chiefly as a placeholder ancestral to zero. Plofker, Keller, Hayashi, Montelle, and Wujastyk argued that some occurrences function arithmetically, not merely typographically. The distinction cannot be resolved by glyph shape alone; it depends on the mathematical syntax of individual passages. [Plofker et al., 2017](https://journals.library.ualberta.ca/hssa/index.php/hssa/article/view/22).

### Brahmagupta

In 628 CE Brahmagupta’s *Brāhmasphuṭasiddhānta* gives explicit rules involving *śūnya* and signed quantities:

- zero plus a positive is positive;
- zero plus a negative is negative;
- zero plus zero is zero;
- subtracting zero leaves a number unchanged;
- a positive times zero is zero;
- a negative times zero is zero.

**[T]** This is the earliest surviving systematic rule-set normally credited with treating zero as an arithmetic operand.

His treatment of division by zero was not the modern one. He did not formulate the modern prohibition or the extended-real notion of infinity consistently. Celebrating his achievement does not require silently correcting his rule. See Colebrooke’s 1817 translation of chapters 12 and 18. [Colebrooke edition](https://www.hist-math.fr/textes/Colebrooke1817_BrahmeguptaBhaskaracharya.pdf).

## 6. Fractions

The early epigraphic numeral system has no securely demonstrated general fractional notation comparable to its integer signs.

Later Indian mathematical manuscripts used:

- numerator above denominator;
- no horizontal fraction bar;
- stacked mixed numbers;
- abbreviations such as *bha* from *bhāga*, “part,” for division;
- *yu* from *yuta*, “added,” in Bakhshali notation;
- a mark after a quantity to indicate a negative value.

**[A]** Bakhshali fractions resemble modern vertical fractions but lack the bar. Compound fractions may occupy three lines. [MacTutor, Bakhshali manuscript](https://mathshistory.st-andrews.ac.uk/HistTopics/Bakhshali_manuscript/).

A horizontal vinculum became standard through later Arabic and European practice; it should not be retrojected into classical Indian manuscripts.

## 7. Largest numbers

There was no inherent largest integer in the positional system: any integer can be extended by adding places.

Indian languages and cosmological, Jain, and Buddhist texts developed elaborate names for powers of ten. The sequences are not uniform across texts, and identical words sometimes have different magnitudes.

A common Sanskrit series includes:

| Power | Name, with variation cautions |
|---:|---|
| 10¹ | *daśa* |
| 10² | *śata* |
| 10³ | *sahasra* |
| 10⁴ | *ayuta* |
| 10⁵ | *lakṣa* |
| 10⁷ | *koṭi* |
| Higher powers | *niyuta*, *prayuta*, *arbuda*, *nyarbuda*, *samudra*, *madhya*, *anta*, *parārdha*—values vary by source |

The modern Indian grouping convention uses lakh = 100,000 and crore = 10,000,000, as in 1,23,45,678.

### Jain and Buddhist expansions

**[T]** Jain canonical and mathematical literature cultivates extremely large finite numbers and classifications of enumerable, innumerable, and infinite quantities.

**[T/TR]** The *Lalitavistara* narrates the young Bodhisattva’s mastery of an enormous sequence of number names during a contest with the mathematician Arjuna. The episode is a Buddhist literary celebration, not an independently dated classroom transcript. Different recensions produce different terminal powers, often summarized as reaching approximately 10^53 or far beyond depending on how the recursive rules are interpreted.

## 8. Famous numbers

The following use normalized positional Brahmi digits, not claims about the handwriting of a particular manuscript.

| Number | Brahmi positional form | Significance |
|---:|:---:|---|
| 270 | 𑁨𑁭𑁦 | One of the quantities in the 876 Gwalior inscription |
| 50 | 𑁫𑁦 | The inscription’s daily garland endowment |
| 62,832 | 𑁬𑁨𑁮𑁩𑁨 | Aryabhata’s circumference value for a diameter of 20,000 |
| 4,320,000,000 | 𑁪𑁩𑁨𑁦𑁦𑁦𑁦𑁦𑁦 | Number of years conventionally assigned to a *kalpa* in one influential cosmological scheme |

Aryabhata’s celebrated rule says, in effect, that adding four to one hundred, multiplying by eight, and adding sixty-two thousand gives approximately the circumference of a circle whose diameter is twenty thousand:

\[
((100+4)\times8)+62,000=62,832,
\]

hence

\[
\pi\approx \frac{62,832}{20,000}=3.1416.
\]

**[T]** The Sanskrit qualifies the result as *āsanna*, “approximate.”

---

# Origins

## 1. What counts as an origin?

At least four separable innovations are often collapsed into “the invention of our numerals”:

1. decimal number words;
2. written signs for decimal values;
3. positional reuse of a small digit inventory;
4. a zero sign and arithmetic with zero.

These need not have arisen simultaneously or from a single inventor.

## 2. Earlier Indian number language

**[T/R]** Vedic texts attest decimal number words and extensive power-of-ten vocabularies well before the surviving Brahmi inscriptions. Ritual geometry in the *Śulbasūtras* required measurement, transformations of areas, and approximations.

This establishes an old Indian decimal linguistic and computational environment. It does not supply a palaeographic ancestor for each Brahmi digit.

## 3. Ashokan numerals: third century BCE

**[A]** Numeral signs occur in some inscriptions of Emperor Ashoka, conventionally dated approximately 260–232 BCE. The attested set is sparse—signs read as 1, 2, 4, 6, 50, and 200 have been reported—rather than a monumental presentation of all twenty signs.

The edicts were first systematically deciphered in the nineteenth century. James Prinsep’s 1830s work established the Brahmi alphabet and identified “Devanampiya Piyadasi” as the ruler known through the inscriptions. Georg Bühler, Émile Senart, Bhagvanlal Indraji, Alexander Cunningham, and later epigraphists refined the numeral readings.

**[D]** A 1911 critique questioned whether certain supposed Ashokan numerals had been interpreted too confidently. The objection matters because isolated damaged marks can be hard to distinguish from letters or punctuation. It does not erase the broader early epigraphic sequence, which is supported by later, fuller inscriptions. [*Indian Antiquary* discussion](https://jainqq.org/booktext/Indian_Antiquary_Vol_40_Romanized/032532).

**Absence finding:** No securely dated pre-300-BCE Indian artefact carries a complete recognizable Brahmi numeral series.

## 4. Nana Ghat

**[A]** The Nana Ghat/Naneghat cave inscription in Maharashtra was commissioned by Queen Nāganikā of the early Satavahana dynasty, probably in the late second or first century BCE; “about 100 BCE” is a serviceable rounded date, not an exact internal date.

It records royal genealogy, Vedic sacrifices, fees, coins, cattle, horses, and other donations. Its numerous values include thousands and tens of thousands, making it crucial for reconstructing the mature ciphered/multiplicative system. The celebrated 24,400 expression is non-positional.

William Henry Sykes brought the site to scholarly notice in 1828. Later readings by Bhagvanlal Indraji, Bühler and other epigraphists established its historical and numerical importance.

The inscription remains in situ rather than having a conventional museum accession number. Claims assigning one should be treated cautiously. A modern presentation of the text includes values such as 14,000, 20,000, 10,000, and 1,100. [Naneghat inscription text](https://en.wikipedia.org/wiki/Naneghat), [Satavahana inscription corpus](https://sahitya.marathi.gov.in/scans/The%20History%20and%20Inscriptions%20of%20The%20Satavahanas%20and%20The%20Western%20Kshatrapas.pdf).

## 5. Nasik

**[A]** The Buddhist cave inscriptions at Nasik—modern Nashik, Maharashtra—span the first and second centuries CE. A particularly important numeral-rich record is dated Śaka 42, or 120 CE. It displays a developed range of Brahmi numerals and multiplicative constructions.

Émile Senart published the Nasik inscriptions in *Epigraphia Indica* 8 (1905–06), pp. 59–96. The records are carved in the caves and therefore generally lack portable-object museum accession numbers. [Senart publication record](https://graph.architexturez.net/doc/az-cf-208560), [digital epigraphic record](https://dharmalekha.info/texts/INSSIIv06p0i0461-0466).

## 6. Possible ancestors and neighbours

### Kharosthi

Kharosthi was used in northwest South Asia and written right-to-left. It ultimately derives from Aramaic. Its numeral system used additive and multiplicative principles and is the closest geographically documented comparator.

**[R/D]** Similarities between Brahmi and Kharosthi multiplication may indicate interaction, but neither a simple one-way borrowing nor a complete derivation of Brahmi numerals from Kharosthi is demonstrable.

### Aramaic, Phoenician, Egyptian, Greek

Numerous nineteenth- and early-twentieth-century proposals derived Brahmi numeral forms from:

- Semitic letter-numerals;
- Phoenician or Aramaic signs;
- Egyptian hieratic/demotic numerals;
- Greek alphabetic numerals;
- invented abbreviations of Indian number words.

**[D]** None explains the whole inventory through an unbroken, securely dated chain.

The separate question of whether the Brahmi writing system had a Semitic stimulus must not be assumed to settle the origin of its numerals.

### Chinese numerals and counting rods

Chinese decimal number words and decimal-multiplicative written numerals are old. Counting-rod configurations later constitute a place-sensitive decimal working notation.

**[D]** Joseph Needham and especially Lam Lay Yong entertained strong Chinese-priority or transmission models. Jean-Claude Martzloff and other historians objected that reconstructions of early rod layouts can depend on later diagrams, texts of uncertain date, and modern redrawing. Similarity between two decimal positional practices does not itself demonstrate transmission.

A cautious conclusion is:

- Chinese rod calculation and Indian written place value are both major decimal traditions.
- Trade and Buddhist travel created possible contact routes.
- No surviving document records the transfer of the positional principle from China to India.
- Indian glyph ancestry from Brahmi is independently traceable.
- The provenance of the abstract positional idea remains less palaeographically visible than the history of the signs.

## 7. Aryabhata, 499 CE

**[T]** Aryabhata composed the *Āryabhaṭīya* in 499 CE. Its mathematical chapter presupposes decimal place-value thinking. A famous verse says “place to place, each is ten times the preceding.”

Aryabhata also devised an alphasyllabic encoding:

- consonants carry numerical values;
- vowels locate them at powers of 100;
- syllables can encode enormous astronomical constants in metrical verse.

This is positional in a broad structural sense but is not ordinary written decimal notation and contains no zero digit. Empty places can be skipped because the vowel marks specify magnitude.

## 8. Bakhshali manuscript

### Object and discovery

**[A]** The Bakhshali manuscript consists of approximately seventy surviving birch-bark leaves or fragments. It was found in 1881 near Bakhshali village, close to Mardan and Peshawar in present-day Pakistan.

A. F. R. Hoernle described it to the Asiatic Society of Bengal in 1882 and published an account in 1883. He gave it to the Bodleian Library in 1902. Its shelfmark is **MS. Sansk. d. 14**.

It contains rules, examples, solutions, and demonstrations dealing with arithmetic, fractions, progressions, square roots, rule-of-three problems, equations, wages, journeys, trade, and animal-price puzzles.

### The radiocarbon results

Three sampled folios produced calibrated ranges:

- 224–383 CE;
- 680–779 CE;
- 885–993 CE.

**[A]** These are measurements of bark samples, not direct dates of ink or composition. [Oxford radiocarbon report](https://ora.ox.ac.uk/objects/uuid%3A5a6d1dd7-f20c-4209-adb6-33849f5b08f4/files/snp193c210).

### The dispute

The Bodleian’s 2017 announcement treated the manuscript as composite and promoted the earliest folio as evidence for the earliest known written zero.

Plofker, Keller, Hayashi, Montelle, and Wujastyk objected:

- The manuscript is codicologically and scribally much more coherent than a six-century spread suggests.
- Birch bark may have been old when inscribed or affected by conservation and contamination.
- The Śāradā palaeography, language, terminology, and mathematical culture appear medieval.
- A date for one bark leaf is not automatically a date for the mathematical text or the act of writing.
- If one insists on the radiocarbon sequence, the latest sampled folio supplies a safer terminus for the assembled manuscript than the earliest.
- The dot sometimes functions mathematically, complicating the placeholder-versus-number publicity.

Takao Hayashi’s critical edition had favoured approximately the seventh century for the underlying work and eighth–twelfth centuries for the surviving copy, with room for uncertainty.

**Finding:** The three carbon ranges are documented. “The Bakhshali manuscript was written in 224 CE” is not documented and should not be repeated. The manuscript’s date remains disputed. [Scholarly response](https://journals.library.ualberta.ca/hssa/index.php/hssa/article/view/22), [MacTutor](https://mathshistory.st-andrews.ac.uk/HistTopics/Bakhshali_manuscript/).

## 9. Brahmagupta, 628 CE

Brahmagupta was born in 598 and worked at Bhillamāla, in present Rajasthan. His *Brāhmasphuṭasiddhānta*, composed in 628, connects astronomy, arithmetic, algebra, geometry, and indeterminate analysis.

**[T]** It is the first surviving work to present a substantial, explicit arithmetic of zero and negative quantities, phrased through “fortunes” and “debts.” It defines zero as the result of subtracting a number from itself.

**[D]** “Brahmagupta invented zero” is too strong. His text proves that he systematized a concept and rules already embedded in a computational tradition. It does not identify the first person to use a zero placeholder or the first person ever to conceive nothing numerically.

## 10. The Sambor inscription K.127

**[A]** The Old Khmer inscription K.127 was found at Trapeang Prei near Sambor on the Mekong in Cambodia. It records the date Śaka 605, equivalent to 683 CE, using a dot between positional digits.

Adhémard Leclère found or reported the stone in 1891. George Cœdès published and interpreted it in 1931. It later disappeared from public view, was located again through Amir Aczel’s investigation in 2013, and was returned to the National Museum of Cambodia in 2015.

**[D]** Aczel called it the earliest zero “within the system that evolved into ours.” That is defensible as an early securely dated epigraphic positional zero in a Brahmi-derived tradition, but not as the invention of zero itself. It postdates Brahmagupta’s text by fifty-five years and cannot outrank an earlier manuscript merely because it is stone; its special strength is its explicit date. [Aczel’s account](https://time.com/3845786/my-quest-to-find-the-first-zero/).

Its catalogue identifier is the epigraphic number **K.127**, not necessarily a museum accession number in the ordinary collections-management sense.

## 11. Gwalior, 876 CE

**[A]** The Chaturbhuj temple inscription at Gwalior Fort is dated Vikrama year 933, corresponding to 876 CE. It records, among other endowments:

- a garden 270 *hastas* long and 187 *hastas* wide;
- provision of fifty garlands daily.

The zeros in 270 and 50 are small circles recognizable as positional zero signs.

E. Hultzsch published the two temple inscriptions in *Epigraphia Indica* 1 (1892), using mechanical copies made in 1885; an earlier rough version of the second was published by Rajendralala Mitra. The inscription remains architectural and has no normal portable-object museum number. [Hultzsch’s original publication](https://upload.wikimedia.org/wikipedia/commons/d/dc/Epigraphia_Indica_Vol_1_%281892%29.pdf).

**[D]** It is often called “the first zero.” More precisely, it is among the earliest indisputable, dated Indian stone inscriptions using a circular zero in ordinary decimal-place notation. K.127 is earlier outside India; texts and manuscripts attest related ideas earlier still.

---

# Arithmetic and instruments

## 1. Oral and written computation in India

Indian mathematical works were commonly composed as compact metrical rules, learned orally, and unpacked by teachers and prose commentators. A written verse might preserve an algorithm while worked numbers were written on a dust board, palm leaf, birch bark, or other erasable surface.

This helps explain a central evidentiary imbalance:

- polished rules survive because they were repeatedly copied;
- scratch calculations and boards usually do not;
- our earliest surviving manuscript can be far later than the computational practice it describes.

Terms such as *pāṭīgaṇita*—“board arithmetic”—point to written or dust-board calculation. Place value is especially natural on a ruled or spatial surface where empty columns remain visible.

## 2. Finger reckoning

**[R/T]** Finger counting was almost certainly widespread, as it was across Eurasia, and Sanskrit vocabulary connects number and digit in ways comparable to other languages. But no surviving Ashokan-era manual describes a uniquely Brahmi finger algorithm. Detailed reconstructions should therefore be labeled comparative rather than directly attested.

## 3. Counting boards and abaci

India’s positional written arithmetic should not be collapsed into a single “Indian abacus.” Literary references suggest boards and counters, but no standard ancient Indian device survives comparable to the Chinese *suanpan* or Japanese *soroban*.

A plausible developmental model is:

1. named decimal places in speech;
2. columns or spatial positions on a board;
3. digits recording the contents of those places;
4. a dot or circle replacing an empty column on portable writing.

This is a scholarly reconstruction, not a documented inventor’s account.

## 4. Comparative calculating instruments

### Roman calculus

Roman calculation used pebbles or counters—Latin *calculi*—on tables or grooved abaci. Hence *calculus*, literally a small stone, came to mean calculation and eventually a branch of mathematics.

Roman numerals were record signs, while much arithmetic could be done on a board independently of how the answer was written. Thus “Roman numerals cannot calculate” is an oversimplification.

The so-called Roman hand abacus in the Bibliothèque nationale de France and comparable museum pieces use grooved decimal and fractional columns. Frequently repeated claims about “the Roman abacus in the Louvre” are inadequately sourced unless accompanied by a Louvre inventory number; no secure Louvre catalogue identification was found in the sources consulted.

### Chinese rods, suanpan, and Japanese soroban

Chinese counting rods represent units by position, alternating orientation to prevent adjacent ranks merging visually. They allowed algorithms with positive and negative numbers.

The framed *suanpan* is later than the earliest rod texts. The Japanese *soroban* was adapted from Chinese forms and simplified over time. Neither instrument is an ancestor of the Brahmi digit shapes, although rod calculation is central to debates over positional priority.

### Medieval European counters

European counting tables and exchequer boards arranged counters by decimal or monetary columns. “Casting accounts” meant placing or throwing counters. Jettons survive in large numbers.

This allowed Roman numerals to persist as documentary notation while calculations occurred spatially.

### Quipu

Andean *khipu* record numbers through knot type, position, and decimal rank. It is a genuine decimal positional recording technology, independently developed in the Americas. No evidence connects it to India.

## 5. Textbook lineages

### Mesopotamia

- **Plimpton 322**, Old Babylonian, approximately 1800 BCE, Columbia University Cuneiform Collection **CULC 460**, records a structured list of sexagesimal numbers associated with right-triangle computations.
- Babylonian school tablets teach multiplication tables, reciprocals, areas, volumes, and equation procedures.
- The system is sexagesimal positional, initially using spacing and later a placeholder sign, but normally no terminal zero and no zero as an independently operated number.

These are comparative precedents, not ancestors established for Brahmi numerals. Høyrup emphasizes the rhetorical and procedural nature of Old Babylonian algebra; Robson warns against reading modern trigonometry too directly into Plimpton 322.

### Egypt

- **Rhind Mathematical Papyrus**, copied by Ahmose around 1650 BCE from an older exemplar, British Museum **EA10057 and EA10058**, uses hieratic decimal-additive numerals and mostly unit fractions.
- Its worked problems concern distribution, bread and beer, geometry, and false position.

No line of descent connects its digit forms to Brahmi.

### China

- The received *Nine Chapters on the Mathematical Art*, compiled through the late first millennium BCE and early centuries CE, with Liu Hui’s commentary of 263 CE, presents algorithms for fractions, areas, elimination, taxation, surveying, and signed counting rods.
- Its rectangular-array elimination is structurally comparable to modern linear algebra, but the historical procedure is a rod-board algorithm.

### India

- Aryabhata, *Āryabhaṭīya* (499): place-value principle, algorithms, astronomy, alphabetic number coding.
- Brahmagupta, *Brāhmasphuṭasiddhānta* (628): zero, debts and fortunes, quadratic and indeterminate equations.
- Bakhshali manuscript: commercial arithmetic, fractions, approximate square roots, linear and quadratic problems.
- Mahāvīra, *Gaṇitasārasaṅgraha* (c. 850): systematic arithmetic including fractions and combinatorial problems.
- Bhāskara II, *Līlāvatī* and *Bījagaṇita* (1150): verse problems and refined arithmetic/algebra.

### Islamicate world

- Muḥammad ibn Mūsā al-Khwarizmi, *Kitāb al-jamʿ wa-l-tafrīq bi-ḥisāb al-Hind*, approximately 825: “Book of addition and subtraction according to Indian calculation.” The Arabic original is lost; Latin adaptations preserve portions of the tradition.
- Al-Kindi, approximately 830: reportedly wrote a four-part work on Indian numerals.
- Al-Uqlidisi, *Kitāb al-Fuṣūl fī al-ḥisāb al-Hindī* (952–53): adapted Indian arithmetic to pen and paper and used decimal fractions.
- Al-Biruni, early eleventh century: described Indian mathematical and calendrical learning while noting that numeral forms differed regionally.

### Latin Europe

- Gerbert of Aurillac, later Pope Sylvester II, c. 946–1003: promoted an abacus using numbered counters or *apices*. The forms and exact route of acquisition remain debated.
- Leonardo of Pisa, Fibonacci, *Liber Abaci* (1202; revised 1228): opened with the “nine figures of the Indians” and the sign 0, called *zephirum*.
- Sacrobosco, *Algorismus vulgaris*, thirteenth century: a highly influential university exposition.
- Pacioli, *Summa de arithmetica* (1494): synthesized commercial arithmetic in print.
- Robert Recorde, *The Ground of Artes* (1543): taught arithmetic in English.
- John Napier, *Rabdologiae* (1617): calculating rods or “Napier’s bones”; his logarithms transformed multiplication into addition.

## 6. Algorists and abacists

**[Documented social tendency; partly stylized opposition]**

- *Abacists* calculated with counters on a board.
- *Algorists* used written Hindu-Arabic figures and algorithms.
- Manuscript and printed images stage contests between the two methods.

The distinction was real but not absolute. Merchants and clerks could use counters for one task and written figures for another.

---

# Transmission and replacement

## 1. India to Southeast Asia

Brahmi-derived scripts accompanied Sanskrit and Buddhist/Hindu textual cultures into Sri Lanka and Southeast Asia. Numeral forms diversified locally.

The Cambodian K.127 zero of 683 and a roughly contemporary Sumatran inscription show that positional decimal notation was not confined to the political boundaries of India. Whether particular innovations arose in India and travelled east, or developed within a connected South/Southeast Asian scholarly zone, cannot always be determined object by object.

## 2. India to Baghdad

A traditional account reports that an Indian astronomical work reached the Abbasid court of Caliph al-Manṣur in 773. It was translated into Arabic and associated with the *Sindhind* tradition, often connected to Brahmagupta’s *Brāhmasphuṭasiddhānta* or *Khaṇḍakhādyaka*.

**[T/R]** The episode is reported in later Arabic bibliographical and scientific sources; details of the Indian visitor’s name and the precise Sanskrit exemplar vary.

Baghdad’s translation movement supplied the institutional setting in which Greek, Persian, and Indian materials were combined. Al-Khwarizmi did not invent the numerals; his title explicitly labels the arithmetic Indian.

## 3. Baghdad to al-Andalus and North Africa

Indian numerals developed distinct eastern and western Arabic shapes:

- Eastern Arabic-Indic: ٠١٢٣٤٥٦٧٨٩
- Persian: ۰۱۲۳۴۵۶۷۸۹
- Western European descendants: 0123456789

The European figures descend chiefly from western Arabic or *ghubār* forms circulating in the Maghreb and al-Andalus, not directly from modern Eastern Arabic-Indic typography.

## 4. Gerbert’s apices

Gerbert probably encountered Iberian mathematical learning while studying in Catalonia during the 960s. Medieval manuscripts associate him with a decimal abacus whose counters bore numeral signs.

**[D]** The surviving “Boethian” geometrical manuscripts containing apices are late and interpolated. They do not prove that Boethius, around 500, knew Hindu-Arabic numerals.

**[L]** Later writers surrounded Gerbert with tales of sorcery, a talking bronze head, and a demonic compact. These reflect his reputation for unfamiliar science, not evidence about numeral transmission.

## 5. Fibonacci in Bugia

Fibonacci says that his father served Pisan merchants at Bugia—modern Béjaïa, Algeria—and arranged for him to learn calculation there. In *Liber Abaci* he praises the nine Indian figures and zero and explains arithmetic, exchange, barter, interest, alloying, and commercial problems.

**[T]** The autobiographical core comes from Fibonacci’s prologue.

**[R]** Calling him the man who single-handedly introduced Arabic numerals to Europe is exaggerated. Latin translators, Gerbertian abaci, Mediterranean merchants, and earlier manuscripts preceded him. His work was nevertheless an exceptionally powerful exposition.

## 6. The Florentine prohibition of 1299

A Florentine guild regulation of 1299 is frequently said to have banned Arabic numerals and required numbers to be written in words or Roman numerals.

**[D]** The rule is better understood as a restriction in certain account books, motivated by alteration and ambiguity, not a citywide ban on learning or using the numerals. Early handwritten 0, 6, and 9 could be altered; a sequence of figures was easier to tamper with than words. The famous slogan “Florence banned Arabic numerals” overstates the legal scope.

## 7. Printing, commerce, and science

From the fifteenth century onward:

- printed arithmetic books regularized digit forms;
- bookkeeping and commercial schools made written algorithms ordinary;
- decimal fractions spread;
- logarithms, navigation, astronomy, and scientific tables rewarded compact positional notation;
- state bureaucracies and industrial accounting completed the replacement.

Roman numerals remained for restricted cultural purposes rather than general computation.

## 8. Persistence and coexistence

Roman numerals survive on:

- clock faces, often with **IIII** rather than IV;
- monarchs and popes;
- monuments and cornerstones;
- book preliminaries;
- outlines and copyright dates;
- Super Bowl numbering, except the specially branded “Super Bowl 50.”

This is functional specialization, not mathematical survival as the dominant calculating notation.

Chinese characters such as 一, 二, 三, 十, 百 and financial forms coexist with Arabic digits in China, Japan, and Korea. Japanese and Korean documents use Arabic numerals heavily while retaining Chinese-derived numerals in formal, linguistic, calendrical, and cultural settings.

---

# People

| Person | Dates | Connection |
|---|---:|---|
| Ashoka | r. c. 268–232 BCE | Earliest securely dated imperial Brahmi inscriptions containing numeral signs |
| Nāganikā | c. first century BCE | Satavahana queen who commissioned the numeral-rich Nana Ghat inscription |
| James Prinsep | 1799–1840 | Deciphered Brahmi inscriptions in the 1830s |
| Alexander Cunningham | 1814–1893 | Surveyed inscriptions and monuments; foundational Archaeological Survey work |
| Bhagvanlal Indraji | 1839–1888 | Early Indian epigraphist who studied Brahmi and Nana Ghat |
| Georg Bühler | 1837–1898 | Major palaeographer; proposed theories of Brahmi script and numeral origins |
| Émile Senart | 1847–1928 | Edited Nasik inscriptions |
| Aryabhata | b. 476 | Composed *Āryabhaṭīya* in 499 |
| Brahmagupta | 598–c. 668 | Systematic rules for zero and signed quantities, 628 |
| Bhāskara I | c. 600–680 | Commentator on Aryabhata |
| Mahāvīra | c. ninth century | *Gaṇitasārasaṅgraha* |
| Bhāskara II | 1114–c. 1185 | *Līlāvatī*, *Bījagaṇita* |
| A. F. R. Hoernle | 1841–1918 | First scholarly description and partial study of Bakhshali |
| G. R. Kaye | 1866–1929 | Edited Bakhshali; advanced sceptical and now largely rejected foreign-origin theories |
| Takao Hayashi | modern | Produced the standard critical Bakhshali study |
| George Cœdès | 1886–1969 | Published and interpreted K.127 in 1931 |
| Amir Aczel | 1950–2015 | Searched for and publicized the rediscovered K.127 stone |
| Al-Khwarizmi | c. 780–c. 850 | Wrote on Indian calculation; source of “algorithm” |
| Al-Kindi | c. 801–873 | Authored a work on Indian numerals |
| Al-Uqlidisi | tenth century | Adapted Indian arithmetic to written calculation |
| Al-Biruni | 973–after 1050 | Described Indian numerals, astronomy, calendars, and regional variation |
| Gerbert of Aurillac | c. 946–1003 | Associated with the apex abacus; later Pope Sylvester II |
| Fibonacci | c. 1170–after 1240 | *Liber Abaci*, learned Mediterranean commercial arithmetic at Bugia |
| Sacrobosco | d. c. 1256 | Influential Latin *Algorismus* |
| Luca Pacioli | c. 1447–1517 | Printed commercial arithmetic and bookkeeping |
| Robert Recorde | c. 1512–1558 | Popularized arithmetic in English |
| John Napier | 1550–1617 | Logarithms and calculating rods |
| Bibhutibhusan Datta | 1888–1958 | Co-author with A. N. Singh of *History of Hindu Mathematics* |
| A. N. Singh | 1901–1954 | Historian of Indian mathematics |
| Kim Plofker | contemporary | Standard modern synthesis of Indian mathematics |
| Stephen Chrisomalis | contemporary | Comparative standard account of numeral systems |

---

# Culture

## 1. Inscriptions, endowments, and law

Brahmi numerals appear in records of:

- regnal years;
- donations;
- cave construction;
- land dimensions;
- quantities of cattle, coins, and garlands;
- monastic endowments;
- taxes and commercial values.

Nana Ghat’s sacrificial fees and Gwalior’s garden and garlands show that numeral history is inseparable from institutions, property, ritual, and administration.

## 2. Coins

Coins provide abundant but sometimes difficult evidence:

- numeral signs may state regnal years, eras, or denominations;
- dies can reverse or distort forms;
- attribution and chronology may depend on disputed dynastic sequences;
- Greek, Kharosthi, Brahmi, Persian, Arabic, and regional numeral traditions can coexist on currencies.

A coin’s numeral is therefore only as securely dated as the coin’s archaeological context or accepted ruler chronology.

## 3. Calendars

Indian dates combine:

- regnal years or named eras;
- lunar months;
- bright and dark fortnights;
- lunar days;
- weekdays and astronomical details.

The Gwalior date uses an era year whose conversion to 876 CE depends on identifying the Vikrama era correctly.

Chronograms later encoded dates through words assigned numerical values. In the *bhūtasaṃkhyā* system, objects conventionally stand for numbers:

- moon = 1;
- eyes = 2;
- Vedas = 4;
- seasons = 6;
- sages = 7;
- elephants of the directions = 8;
- planets = 9;
- sky or void = 0.

Values are often read in reverse order under the maxim *aṅkānāṃ vāmato gatiḥ*, “digits move to the left.”

## 4. Liturgy and sacred number

Numbers such as 3, 7, 8, 9, 18, 27, 54, and 108 acquire religious importance in Hindu, Buddhist, and Jain contexts. Mala bead counts, ritual repetitions, cosmological cycles, textual divisions, and temple measurements employ numbers symbolically.

These meanings belong to cultural numerology and ritual convention; they are not evidence for how a digit glyph was invented.

## 5. Gematria and isopsephy

Hebrew gematria and Greek isopsephy assign numerical values to alphabetic letters. Comparable Indian systems include:

- Aryabhata’s phonetic numeration;
- *kaṭapayādi*, mapping consonants to digits;
- *bhūtasaṃkhyā*, using semantic number words.

There is no evidence that Hebrew or Greek mysticism generated Indian decimal place value. The comparison demonstrates a widespread human practice of encoding numbers in language.

## 6. Literature and mnemonic numbers

Indian authors embedded numerical constants in verse so that they could be memorized and transmitted orally. A word could carry:

- a normal semantic meaning;
- a numerical value;
- a metrical function;
- an astronomical constant.

This makes Indian numeral culture broader than the graphic history of 0–9.

## 7. Typography

European digits varied dramatically in manuscripts and early print. Modern typography distinguishes:

- lining figures: 0123456789, usually equal cap height;
- old-style or text figures: digits with ascenders and descenders;
- proportional figures: varying widths;
- tabular figures: fixed widths for columns.

Old-style figures are not an ancient Indian invention. They are a European typographic accommodation of numerals to lowercase Latin text. [“Thinking on Paper”](https://journals.uc.edu/index.php/vl/article/view/5759).

---

# Comparative world chronology: what is and is not ancestral

The requested objects span independent traditions. They should be placed alongside the Indian development without constructing a fictitious universal chain.

## Lebombo bone

**[A/D]** A notched baboon fibula from Border Cave in southern Africa, often dated to approximately 35,000–44,000 years ago, is called the Lebombo bone.

**[R]** The notches may record counting or repeated activity.

**[D/L]** Identifying it as a lunar calendar, menstrual calendar, or “the first mathematical object” exceeds the evidence. It has no demonstrated relation to Brahmi.

## Ishango bone

**[A]** Found in the 1950s by Jean de Heinzelin near Ishango in the Democratic Republic of Congo; held by the Royal Belgian Institute of Natural Sciences. Usually dated to the Late Stone Age, often around 20,000 years ago, though published dates vary.

**[D]** Interpretations include arithmetic groupings, doubling, prime numbers, lunar notation, or patterned tallying. None is securely established.

## Uruk tokens and bullae

**[A/R]** Clay tokens and sealed bullae from ancient Southwest Asia preceded and accompanied proto-cuneiform accounting.

Denise Schmandt-Besserat argued that token shapes were direct precursors of impressed numerical and commodity signs. Her work made the objects central to histories of writing.

**[D]** Specialists accept the importance of accounting devices but dispute a simple, universal token-to-writing evolutionary sequence. This tradition is not a demonstrated ancestor of Indian digits.

## Narmer macehead

**[A]** The ceremonial macehead of Narmer, excavated at Hierakonpolis by James Quibell and Frederick Green and now in the Ashmolean Museum, **E.3631**, contains Egyptian numerical signs interpreted as immense counts of captives, cattle, or booty.

**[D]** Whether every figure is a literal administrative total or royal hyperbole is uncertain. Egyptian numerals are decimal-additive, not positional.

## Plimpton 322

**[A]** Old Babylonian tablet, Columbia **CULC 460**, c. 1800 BCE.

**[D]** Interpretations range from a scribal exercise in reciprocal mathematics and right triangles to a “trigonometric table.” The latter description can be mathematically suggestive but historically anachronistic.

## Rhind Mathematical Papyrus

**[A]** British Museum **EA10057–58**, copied by Ahmose c. 1650 BCE.

It demonstrates sophisticated Egyptian arithmetic without positional notation or an Indian-style zero.

## Maya numerals and Dresden Codex

**[A]** The Maya used dots for ones, bars for fives, and a shell-like zero in a mainly vigesimal positional system. Long Count calendrical places modify the pure base-20 sequence by using 18×20 for the third place.

The Dresden Codex is held by the Saxon State and University Library Dresden as **Mscr.Dresd.R.310**. It is a pre-Columbian Maya screenfold, probably copied in the Postclassic period, containing calendrical and astronomical tables.

**[A/R]** Maya zero arose independently of Old World zero.

**[D]** The earliest exact Maya zero attestation depends on contested readings and conversions of monuments and calendrical notations.

**[L]** Maya mathematics did not simply “die with the codices.” Spanish colonial destruction was catastrophic, but Maya calendrical knowledge, languages, communities, and numerical practices survived in altered forms. The Long Count itself has been revived and studied through inscriptions and living Maya cultural work.

---

# Words descended from the tradition

## Digit

Latin *digitus*, “finger.” It came to mean a finger-width, then one of the numerals 0–9. This etymology reflects finger reckoning generally, not a specifically Indian coinage.

## Calculus

Latin *calculus*, “small pebble,” from counters used in reckoning. Later meanings include a method of calculation and, from the seventeenth century, differential and integral calculus.

## Abacus

Latin *abacus*, from Greek *abax/abakion*, probably a counting board or slab. A proposed ultimate Semitic source is often mentioned but remains etymologically uncertain.

## Algorithm

From the Latinized name of al-Khwarizmi:

> *Algoritmi* / *Algorismi* → algorism → algorithm.

Originally it referred especially to calculation with Indian numerals; its meaning broadened to any defined computational procedure.

## Cipher

Arabic *ṣifr*, “empty, zero,” through Medieval Latin *cifra* and French/Italian forms. It acquired meanings including zero, numeral, secret writing, and an insignificant person.

## Zero

Sanskrit *śūnya*, “empty,” was translated conceptually into Arabic *ṣifr*. Through Italian *zefiro/zero*, the word became English *zero*. The exact phonological path belongs to Arabic-to-Romance transmission; “zero comes directly from Sanskrit” is an oversimplification.

---

# Controversies and disputes

## 1. Who invented zero?

The question lacks a single answer because “zero” can mean:

- an unmarked empty position;
- a written placeholder;
- a calendrical ordinal;
- a number equal to \(a-a\);
- an operand with arithmetic rules;
- a modern algebraic identity element.

### Babylonian claim

**[A]** Mesopotamian scribes used positional sexagesimal notation. By the first millennium BCE they employed a placeholder sign internally.

**Limitation:** It was not normally a terminal zero, not a general numeral standing alone, and not accompanied by a surviving arithmetic theory of zero.

### Maya claim

**[A]** Maya calendrical and numerical inscriptions use explicit zero glyphs in a positional framework independently of Eurasia.

**Limitation:** Dating the first instance and distinguishing calendrical completion signs from cardinal zero require case-by-case analysis.

### Indian claim

**[A/T]** India supplies the historically connected package leading to the modern worldwide system:

- decimal place value;
- Brahmi-derived digits;
- an explicit zero mark;
- arithmetic rules for zero;
- a documented route through Arabic mathematical literature into Europe.

**Conclusion:** India did not invent every historical use of absence or placeholder. It did develop the zero-bearing decimal tradition ancestral to modern global notation.

## 2. Is Bakhshali the oldest zero?

**[D]**

For:

- one radiocarbon sample dates to 224–383 CE;
- the folio carries dot placeholders;
- that range precedes Brahmagupta and K.127.

Against:

- the sample dates bark, not writing;
- the other two samples are centuries later;
- script and language appear medieval;
- the manuscript may be a single copying event;
- conservation or old stock can distort inference;
- “oldest zero” equivocates between placeholder and number.

Responsible formulation:

> Bakhshali contains an early dot zero in positional notation. One sampled bark leaf returned a third–fourth-century range, but the manuscript’s writing and compilation date remain disputed.

## 3. Gwalior versus Sambor

- Gwalior: 876 CE, India, circular zeros, securely dated architectural inscription.
- Sambor K.127: 683 CE, Cambodia, dot zero, securely dated inscription in a Brahmi-derived cultural sphere.
- Bakhshali: potentially earlier material but disputed manuscript date.
- Brahmagupta: 628 CE text with explicit arithmetic rules, preserved in later manuscripts.

Each can be “first” only under a carefully specified category.

## 4. Did Aryabhata use zero?

Aryabhata’s numerical system can encode absent places by omission and vowel position. His decimal-place statement presupposes place value.

**[D]** This does not prove that he wrote a zero glyph. Saying that he “used zero” is defensible only if one means the structural idea of an empty place, not a surviving written 0.

## 5. Were Brahmi numerals derived from letters?

Nineteenth-century writers proposed that each numeral abbreviated a corresponding Sanskrit number word.

**[D]** No systematic phonetic/palaeographic derivation has won acceptance. One through three are readily explained as stroke tallies; higher signs have obscure histories.

## 6. The “angles count the value” story

A popular diagram claims that:

- 1 has one angle;
- 2 has two;
- …
- 9 has nine;
- 0 has none.

**[M/L]** This is a modern invention. Early Brahmi, Arabic, and European digit forms do not display the required angle counts. The diagrams redraw the digits to manufacture the result. No Indian or medieval Arabic text gives this construction.

## 7. “Arabic numerals are really Indian”

This slogan corrects one misconception while risking another.

Accurate formulation:

- the decimal-place system and ultimate ancestry of the principal digit shapes are Indian;
- Arabic-speaking and Persian scholars adopted, analyzed, modified, and transmitted them;
- western Arabic forms underwent further transformation in North Africa, Iberia, and Europe;
- “Hindu-Arabic numerals” acknowledges this layered history.

## 8. “Roman numerals have no zero”

True narrowly: the standard Roman numeral inventory has no positional zero.

Misleading broadly:

- Latin writers had words such as *nihil* for nothing;
- medieval computists could mark empty places;
- Roman and medieval calculators used boards whose empty columns functioned operationally;
- later manuscripts sometimes employed N or other marks.

The absence concerns the canonical numeral notation, not an inability to understand absence.

## 9. Chinese counting-rod priority

**[D]** Counting rods supply very early decimal, place-sensitive computation; surviving Chinese texts and later diagrams document powerful positional algorithms.

The strongest China-to-India thesis argues that contact transmitted this method westward. Objections are:

- uncertain dates of some texts and diagrams;
- absence of a transfer document;
- differences in signs and zero practice;
- independent Indian verbal place-value traditions;
- risk of reconstructing ancient boards from later printed conventions.

The evidence permits contact but does not prove dependence.

## 10. Ifrah’s synthesis

Georges Ifrah’s *Universal History of Numbers* is extraordinarily wide-ranging and visually useful, but it should not be the sole authority.

Joseph Dauben’s detailed review identified:

- chronological errors;
- reliance on obsolete secondary sources;
- reconstructions presented too confidently;
- inaccurate treatment of Chinese rod diagrams;
- failure to correct errors noted in earlier reviews.

Chrisomalis likewise favors typologically explicit, artefact-based analysis and is more cautious about diffusion. Ifrah is best used as a source of hypotheses, examples, and historiographical influence, followed by verification in specialist literature. [Dauben review in *Notices of the AMS*](https://www.ams.org/notices/200201/200201FullIssue.pdf).

## 11. Nationalist and diffusionist extremes

Two recurring modern narratives are unsupported:

- “Every element of mathematics, including all zeros and all numeral signs, originated in India.”
- “Indian numerals were merely imported wholesale from Babylonia, Greece, China, or Arabia.”

The surviving record instead shows:

- independent inventions of positional devices;
- extensive cross-cultural contact;
- a securely Indian genealogy for the numeral tradition transmitted under the name “Indian reckoning” by Arabic authors;
- unresolved questions about earlier conceptual stimuli.

---

# Open questions

1. What calculations lay behind the earliest Ashokan numeral forms, given that working boards have not survived?
2. Were Brahmi signs 4–9 indigenous inventions, abbreviations, or transformations of foreign signs?
3. How much structural influence passed between Kharosthi and Brahmi notation?
4. When was a written zero first used in India itself, as distinct from surviving later copies of earlier texts?
5. How should the contradictory Bakhshali radiocarbon results be reconciled with its apparently coherent script and codicology?
6. Can ink analysis, multispectral imaging, or additional minimally destructive sampling refine Bakhshali’s date?
7. When did *śūnya* shift from philosophical and linguistic “emptiness” to a technical arithmetical term?
8. Did the written positional system develop directly from a counting board, from verbal place-value expressions, or from their interaction?
9. How much contact existed between Indian decimal practice and Chinese counting rods before 600 CE?
10. Were the early Southeast Asian zeros direct imports, innovations by mobile Indian scribes, or products of local scholarly communities?
11. What was the precise Sanskrit work translated at al-Manṣur’s court?
12. How closely did al-Khwarizmi’s lost Arabic text resemble the surviving Latin *Algoritmi* adaptations?
13. Which merchant communities were most responsible for transmission through the Indian Ocean and Mediterranean?
14. How representative are monumental inscriptions, which preserve formal notation, of everyday commercial handwriting?
15. How many supposedly early numerical marks in damaged inscriptions would survive modern epigraphic re-examination?

---

# Conclusions

The fullest defensible reconstruction is not a tale of one instantaneous invention.

The earliest Brahmi numerals, securely visible under Ashoka in the third century BCE, formed a decimal but non-positional notation. By Nana Ghat and Nasik, scribes possessed distinct unit and decade signs and multiplicative devices for hundreds and thousands. This system could express large numbers efficiently without zero because it did not depend on empty written positions.

Indian number words, calculation practices, astronomical tables, and mnemonic systems increasingly organized quantities by decimal place. Aryabhata’s work of 499 explicitly articulates place progression and offers a different, alphabetic positional encoding. At some uncertain point, probably through interaction between spoken place names, boards, and written numerals, the nine unit signs became reusable digits. A dot or circle marked an empty position.

Bakhshali preserves this developed practice but cannot presently be assigned wholesale to its earliest radiocarbon interval. Brahmagupta’s text of 628 provides the decisive surviving conceptual evidence: zero appears within rules of arithmetic alongside positive and negative numbers. The Cambodian K.127 inscription of 683 and Gwalior inscription of 876 provide secure epigraphic anchors.

Arabic and Persian scholars accurately called the technique Indian. Al-Khwarizmi and his successors converted it into a major written computational tradition; western Arabic forms reached Latin Europe through Iberia, North Africa, translation, trade, Gerbertian abaci, and Fibonacci. Printing, commercial schooling, decimal fractions, logarithms, bookkeeping, and science ultimately made it global.

Babylonian placeholders, Chinese rods, and Maya zero are essential comparisons and in some categories earlier. None, however, supplies the documented historical line leading to the particular decimal zero-bearing system now used worldwide. That line is Indian in formation, Islamicate in a crucial stage of elaboration and transmission, and globally plural in its later scripts and uses.

---

# Sources: editions and URLs consulted

## Primary texts and inscriptions

- Hultzsch, E. “The Two Inscriptions of the Vāillabhaṭṭasvāmin Temple at Gwalior.” *Epigraphia Indica* 1 (1892), pp. 154–162.  
  https://upload.wikimedia.org/wikipedia/commons/d/dc/Epigraphia_Indica_Vol_1_%281892%29.pdf

- Senart, Émile. “The Inscriptions in the Caves at Nasik.” *Epigraphia Indica* 8 (1905–06), pp. 59–96.  
  https://graph.architexturez.net/doc/az-cf-208560  
  https://whatisindia.com/inscriptions/epigraphica_indica/vol8_1905-1906/senart.html

- Digital Corpus of Sanskrit and Prakrit Inscriptions, Nasik records and bibliographical history.  
  https://dharmalekha.info/texts/INSSIIv06p0i0461-0466

- Mirashi, V. V., ed. *The History and Inscriptions of the Sātavāhanas and the Western Kshatrapas*.  
  https://sahitya.marathi.gov.in/scans/The%20History%20and%20Inscriptions%20of%20The%20Satavahanas%20and%20The%20Western%20Kshatrapas.pdf

- Colebrooke, Henry Thomas, trans. *Algebra, with Arithmetic and Mensuration, from the Sanscrit of Brahmegupta and Bháscara*. London, 1817.  
  https://www.hist-math.fr/textes/Colebrooke1817_BrahmeguptaBhaskaracharya.pdf  
  https://zenodo.org/records/7882650

- Bakhshali manuscript radiocarbon report, University of Oxford.  
  https://ora.ox.ac.uk/objects/uuid%3A5a6d1dd7-f20c-4209-adb6-33849f5b08f4/files/snp193c210

## Standard modern studies

- Chrisomalis, Stephen. *Numerical Notation: A Comparative History*. Cambridge University Press, 2010.  
  https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20%28CUP%2C%202010%29%28ISBN%200521878187%29%28O%29%28498s%29_MPop_.pdf

- Plofker, Kim. *Mathematics in India*. Princeton University Press, 2009.  
  https://sanskrit.uohyd.ac.in/Algorithms_in_Ancient_India/Material/Kim_Plofkar_Maths_in_India.pdf

- Datta, Bibhutibhusan, and Avadhesh Narayan Singh. *History of Hindu Mathematics*, 1935–38; reprints.  
  https://www.dbraulibrary.org.in/RareBooks/History%20of%20Hindu%20Mathematics.pdf

- Hayashi, Takao. *The Bakhshālī Manuscript: An Ancient Indian Mathematical Treatise*. Groningen, 1995; revised Brill edition, 2025.  
  https://books.google.com/books/about/The_Bakhsh%C4%81l%C4%AB_Manuscript.html?id=JDZEEQAAQBAJ

- Plofker, Kim; Agathe Keller; Takao Hayashi; Clemency Montelle; Dominik Wujastyk. “The Bakhshālī Manuscript: A Response to the Bodleian Library’s Radiocarbon Dating.” *History of Science in South Asia* 5.1 (2017): 134–150.  
  https://journals.library.ualberta.ca/hssa/index.php/hssa/article/view/22  
  https://doi.org/10.18732/H2XT07

- Plofker et al., downloadable copy of the Bakhshali response.  
  https://www.wisdomlib.org/uploads/journals/hssa/5_2_27.pdf

- Bhāvanā, “The Bakhshali Manuscript and the Indian Zero.”  
  https://bhavana.org.in/the-bakhshali-manuscript/

- Bhāvanā, “Mathematics in India,” discussion of fractions.  
  https://bhavana.org.in/mathematics-in-india-4/

- Smith, David Eugene, and Louis Charles Karpinski. *The Hindu-Arabic Numerals*. Boston, 1911.  
  https://preview.wellcomecollection.org/works/kerkrdtr  
  https://in.okfn.org/files/2013/07/The-Hindu-Arabic-Numerals.pdf  
  https://mathshistory.st-andrews.ac.uk/Extras/Karpinski_Smith/

- Menninger, Karl. *Number Words and Number Symbols: A Cultural History of Numbers*. Translated by Paul Broneer. MIT Press, 1969; Dover reprint, 1992.

- Ifrah, Georges. *The Universal History of Numbers: From Prehistory to the Invention of the Computer*. Translated by David Bellos et al. Wiley/Harvill, 1998–2000.

- Dauben, Joseph W. Review of Ifrah’s *Universal History of Numbers* and *Universal History of Computing*. *Notices of the American Mathematical Society* 49 (2002).  
  https://www.ams.org/notices/200201/200201FullIssue.pdf

- Salomon, Richard. *Indian Epigraphy: A Guide to the Study of Inscriptions in Sanskrit, Prakrit, and the Other Indo-Aryan Languages*. Oxford University Press, 1998.

## MacTutor History of Mathematics

- “Indian Numerals.”  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_numerals/

- “Arabic Numerals.”  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Arabic_numerals/

- “The Bakhshali Manuscript.”  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Bakhshali_manuscript/

- “Indian Mathematics—Redressing the Balance,” Bakhshali chapter.  
  https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-7/

## Unicode and digital encoding

- Unicode Brahmi names list.  
  https://www.unicode.org/charts/nameslist/n_11000.html

- Unicode Brahmi chart.  
  https://www.unicode.org/charts/PDF/U11000.pdf

- Unicode Standard, chapter 14.  
  https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-14/

- Proposal to encode the Brahmi Number Joiner.  
  https://www.unicode.org/wg2/docs/n4166.pdf

## Cambodia and zero

- Aczel, Amir. “My Quest to Find the First Zero.” *Time*, 2015.  
  https://time.com/3845786/my-quest-to-find-the-first-zero/

- Spanish account of Aczel and Cœdès’s reading.  
  https://elpais.com/elpais/2016/09/09/ciencia/1473436052_073929.html

## Comparative histories

- Robson, Eleanor. *Mathematics in Ancient Iraq: A Social History*. Princeton University Press, 2008.

- Høyrup, Jens. *Lengths, Widths, Surfaces: A Portrait of Old Babylonian Algebra and Its Kin*. Springer, 2002.

- Needham, Joseph. *Science and Civilisation in China*, vol. 3: *Mathematics and the Sciences of the Heavens and the Earth*. Cambridge University Press, 1959.

- Martzloff, Jean-Claude. *A History of Chinese Mathematics*. Springer, 1997.

- Non-power positional systems and Maya zero.  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC8022160/  
  https://arxiv.org/abs/2005.10207

- Maya zero survey.  
  https://www.mayaexploration.org/pdf/ZeroInPreColumbianAmericas_CatepillanMendez_Sept2017.pdf

## Typography

- “Thinking on Paper: Hindu-Arabic Numerals in European Typography.” *Visible Language*.  
  https://journals.uc.edu/index.php/vl/article/view/5759  
  https://journals.uc.edu/index.php/vl/article/download/5759/4623

- Butterick, “Alternate Figures.”  
  https://practicaltypography.com/alternate-figures.html

## Useful collection identifiers

- Bakhshali manuscript: Bodleian Library, **MS. Sansk. d. 14**.
- Narmer macehead: Ashmolean Museum, **E.3631**.
- Rhind Mathematical Papyrus: British Museum, **EA10057 and EA10058**.
- Plimpton 322: Columbia University, **CULC 460**.
- Dresden Maya Codex: SLUB Dresden, **Mscr.Dresd.R.310**.
- Sambor inscription: Cambodian epigraphic catalogue **K.127**.
- Nana Ghat, Nasik, and Gwalior inscriptions: architectural inscriptions primarily preserved in situ; no verified portable-object museum accession numbers were found.
