# Hindu-Arabic numerals and the zero in the West: Research Dossier

## Method and evidentiary labels

This dossier distinguishes six kinds of statement:

- **[Artefact]** A surviving object, inscription, manuscript, coin, or printed book.
- **[Documented text]** A claim explicitly present in a surviving text, although the surviving witness may be a copy or translation.
- **[Scholarly reconstruction]** A conclusion inferred from palaeography, linguistic evidence, mathematical structure, transmission routes, or comparison among sources.
- **[Tradition]** A report preserved by later writers whose historical core may be real but is not independently demonstrated.
- **[Disputed]** A claim on which specialists differ or for which the dating or interpretation is materially uncertain.
- **[Legend/modern invention]** A story unsupported by early evidence, including modern explanatory myths.

The subject is the Hindu-Arabic decimal place-value system and its western branch. Babylonian, Egyptian, Chinese, Roman, African tally, and Maya materials are included as comparanda—not as a single evolutionary chain. Similarity, especially possession of a zero-like mark, does not by itself establish borrowing.

---

## Basic identification

| Field | Identification |
|---|---|
| Name | Hindu-Arabic numeral system; Indian decimal place-value notation; in medieval Arabic, *ḥisāb al-Hind* or *al-ḥisāb al-hindī*, “Indian reckoning”; its western Arabic form is often called *ghubār* numeration |
| Base | 10 |
| Type | Ciphered, positional, multiplicative by place; ordinary multi-digit notation is neither additive nor subtractive |
| Fundamental signs | `0 1 2 3 4 5 6 7 8 9` |
| Arabic-script branch | `٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩` |
| Persian/extended Arabic-Indic branch | `۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹` |
| Devanagari branch | `० १ २ ३ ४ ५ ६ ७ ८ ९` |
| Period | Precursors by the third century BCE; decimal positional notation demonstrable in the first millennium CE; transmitted through Arabic scholarship from the eighth–ninth centuries; present in Latin Europe from the tenth century; globally dominant in modern science, commerce, and computing |
| Region | Origin and early development in South Asia; elaboration and transmission through the Islamic world; adaptation in al-Andalus, Latin Europe, and subsequently most of the world |
| Direction | Digits are ordered from highest place at the left to units at the right. This order remains internally left-to-right even when embedded in right-to-left Arabic-script text |
| Capacity | In principle unlimited: a finite alphabet of ten digits represents every non-negative integer; signs and conventions extend it to negatives, rational and real numbers, scientific notation, and complex numbers |

Unicode deliberately distinguishes terminology: “Arabic digits” is ambiguous. It calls `0–9` European digits, `٠–٩` Arabic-Indic digits, `۰–۹` Eastern Arabic-Indic digits, and `०–९` Devanagari digits. It also emphasizes that digit shapes and preferred local usage are separate matters. **[Modern standard]** [Unicode digit terminology](https://www.unicode.org/terminology/digits.html); [Unicode, Chapter 9](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-9/).

---

# The system in detail

## 1. The ten signs

| Value | Western | Arabic-Indic | Eastern Arabic-Indic | Devanagari | Verbal description of common Western form |
|---:|:---:|:---:|:---:|:---:|---|
| 0 | 0 | ٠ | ۰ | ० | Oval or circular loop |
| 1 | 1 | ١ | ۱ | १ | Upright stroke, often with head and foot |
| 2 | 2 | ٢ | ۲ | Curved upper stroke descending to a horizontal base |
| 3 | 3 | ٣ | ۳ | Two open right-facing bowls |
| 4 | 4 | ٤ | ۴ | Open or closed triangular/diagonal construction with vertical |
| 5 | 5 | ٥ | ۵ | Top bar and lower bowl |
| 6 | 6 | ٦ | Loop below with rising stem |
| 7 | 7 | ٧ | Top bar and diagonal descending stroke |
| 8 | 8 | ٨ | Two vertically joined loops |
| 9 | 9 | ٩ | Upper loop with descending stem |

These are values, not immutable drawings. Manuscripts display large regional and scribal variation. In particular, Arabic-script 4, 5, 6, and 7 have locale-sensitive forms. Unicode encodes characters, while typefaces and language-specific shaping determine many glyph differences. **[Modern standard]** [Unicode Arabic-script digit tables](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-9/).

The familiar western shapes are the end of a branching palaeographic history, not ten diagrams designed at one sitting. **[Scholarly reconstruction]** Brahmi-derived forms developed through regional Indian scripts; Islamic scribes produced eastern and western families; medieval European handwriting and printing regularized the western family. Chrisomalis’s comparative survey remains the best single structural treatment. [Chrisomalis, *Numerical Notation*](https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20%28CUP%2C%202010%29%28ISBN%200521878187%29%28O%29%28498s%29_MPop_.pdf).

## 2. Place value

For a numeral \(d_nd_{n-1}\dots d_1d_0\),

\[
d_n10^n+d_{n-1}10^{n-1}+\cdots+d_1 10+d_0
\]

is its value.

Thus:

\[
5072 = 5\times1000 + 0\times100 + 7\times10 + 2.
\]

The written numeral is:

- **ciphered** because each unit value 0–9 has its own sign;
- **positional** because the same `5` means five, fifty, five hundred, and so forth according to place;
- **multiplicative by position** because the digit implicitly multiplies a power of ten;
- not normally **additive in form**, although its expanded interpretation is a sum.

Zero performs two distinguishable functions:

1. **Placeholder:** the `0` in `5072` marks an empty hundreds place.
2. **Number:** `0` can itself be an operand, the additive identity, and the boundary between positive and negative numbers.

Those functions have separate histories. A blank place, dot, or separator can serve the first without a culture possessing modern arithmetic on zero.

## 3. Worked table: zero through twenty

| Value | Western | Arabic-Indic | Eastern Arabic-Indic | Devanagari | English |
|---:|---:|---:|---:|---:|---|
| 0 | 0 | ٠ | ۰ | ० | zero |
| 1 | 1 | ١ | ۱ | १ | one |
| 2 | 2 | ٢ | ۲ | २ | two |
| 3 | 3 | ٣ | ۳ | ३ | three |
| 4 | 4 | ٤ | ۴ | ४ | four |
| 5 | 5 | ٥ | ۵ | ५ | five |
| 6 | 6 | ٦ | ۶ | ६ | six |
| 7 | 7 | ٧ | ۷ | ७ | seven |
| 8 | 8 | ٨ | ۸ | ८ | eight |
| 9 | 9 | ٩ | ۹ | ९ | nine |
| 10 | 10 | ١٠ | ۱۰ | १० | ten |
| 11 | 11 | ١١ | ۱۱ | ११ | eleven |
| 12 | 12 | ١٢ | ۱۲ | १२ | twelve |
| 13 | 13 | ١٣ | ۱۳ | १३ | thirteen |
| 14 | 14 | ١٤ | ۱۴ | १४ | fourteen |
| 15 | 15 | ١٥ | ۱۵ | १५ | fifteen |
| 16 | 16 | ١٦ | ۱۶ | १६ | sixteen |
| 17 | 17 | ١٧ | ۱۷ | १७ | seventeen |
| 18 | 18 | ١٨ | ۱۸ | १८ | eighteen |
| 19 | 19 | ١٩ | ۱۹ | १९ | nineteen |
| 20 | 20 | ٢٠ | ۲۰ | २० | twenty |

The digit order does not reverse in Arabic: `١٢٣` has hundreds, tens, and units in the same visual order as `123`, although Arabic prose surrounds it in right-to-left order.

## 4. Tens, hundreds, and thousands

| Value | Western | Arabic-Indic | Devanagari | Name |
|---:|---:|---:|---:|---|
| 10 | 10 | ١٠ | १० | ten |
| 20 | 20 | ٢٠ | २० | twenty |
| 30 | 30 | ٣٠ | ३० | thirty |
| 40 | 40 | ٤٠ | ४० | forty |
| 50 | 50 | ٥٠ | ५० | fifty |
| 60 | 60 | ٦٠ | ६० | sixty |
| 70 | 70 | ٧٠ | ७० | seventy |
| 80 | 80 | ٨٠ | ८० | eighty |
| 90 | 90 | ٩٠ | ९० | ninety |
| 100 | 100 | ١٠٠ | १०० | hundred |
| 200 | 200 | ٢٠٠ | २०० | two hundred |
| 500 | 500 | ٥٠٠ | ५०० | five hundred |
| 1,000 | 1000 | ١٠٠٠ | १००० | thousand |
| 10,000 | 10000 | ١٠٠٠٠ | १०००० | ten thousand; Indian *das hazār* |
| 100,000 | 100000 | ١٠٠٠٠٠ | १००००० | hundred thousand; Indian lakh/lac |
| 1,000,000 | 1000000 | ١٠٠٠٠٠٠ | १०००००० | million; ten lakh |
| 10,000,000 | 10000000 | ١٠٠٠٠٠٠٠ | १००००००० | ten million; one crore |

Indian grouping normally writes `1,00,000` and `1,00,00,000`; international three-place grouping writes `100,000` and `10,000,000`. Grouping is a display convention, not part of positional value. Unicode CLDR records the default, native, and traditional numbering systems and grouping conventions of individual locales. **[Modern standard]** [CLDR numbering systems](https://cldr.unicode.org/translation/core-data/numbering-systems).

## 5. Powers of ten and number words

| Power | International short-scale English | Traditional Indian English |
|---:|---|---|
| \(10^0\) | one | one |
| \(10^1\) | ten | ten |
| \(10^2\) | hundred | hundred |
| \(10^3\) | thousand | thousand |
| \(10^4\) | ten thousand | ten thousand |
| \(10^5\) | hundred thousand | lakh |
| \(10^6\) | million | ten lakh |
| \(10^7\) | ten million | crore |
| \(10^9\) | billion | hundred crore / arab in some Indo-Aryan naming traditions |
| \(10^{12}\) | trillion | lakh crore; names vary by language and historical scheme |
| \(10^{100}\) | googol | no structural limit imposed by notation |

Ancient and medieval Sanskrit texts contain very long series of named powers, but the lists and values vary by genre and period. These names do not limit the written notation: one may append as many places as required.

## 6. Famous numbers

| Number | Western | Arabic-Indic | Devanagari | Note |
|---|---:|---:|---:|---|
| \(108\) | 108 | ١٠٨ | १०८ | Ritually prominent in Hindu, Buddhist, and Jain traditions |
| \(1729\) | 1729 | ١٧٢٩ | १७२९ | Hardy–Ramanujan taxicab number |
| \(3.14159265\ldots\) | 3.14159265… | ٣٫١٤١٥٩٢٦٥… | ३.१४१५९२६५… | Approximation of \(\pi\) |
| \(6.02214076\times10^{23}\) | 6.02214076×10²³ | ٦٫٠٢٢١٤٠٧٦×١٠²³ | ६.०२२१४०७६×१०²³ | Avogadro constant’s fixed SI numerical value |
| \(2^{82,589,933}-1\) | 2^82589933−1 | — | — | A compact expression illustrating that algebraic notation can name integers impractical to print digit by digit |

## 7. Fractions

The positional principle extends naturally to fractional places:

\[
0.375 = 3\times10^{-1}+7\times10^{-2}+5\times10^{-3}=\frac{3}{8}.
\]

Modern forms include:

- common fraction: `3/8`, \(\frac38\);
- decimal fraction: `0.375`;
- mixed number: \(2\frac38\);
- scientific notation: \(3.75\times10^{-1}\);
- repeating decimal: \(0.\overline{3}\), `0.333…`.

Indian manuscript fractions were often written with numerator above denominator without the modern horizontal fraction bar. Islamic and European practitioners employed several layouts before the horizontal bar became standard. Fibonacci devoted extensive attention to unit-fraction decompositions inherited partly through Mediterranean commercial and Arabic mathematical practice.

### Decimal separator

There was no single moment at which “the decimal point” was invented.

- **[Artefact/printed text]** Francesco Pellos’s 1492 commercial arithmetic used a point in a decimal context, but historians disagree over whether he understood it as a general separator.
- **[Documented text]** Christoff Rudolff used a vertical separator in 1530.
- **[Documented text]** Simon Stevin’s *De Thiende/La Disme* (1585) systematically advocated decimal fractions but marked each place with circled indices instead of our point.
- **[Documented/disputed priority]** Magini (1592), Bürgi’s manuscript work, and Clavius (1593) used point- or comma-like separators.
- **[Documented text]** Edward Wright’s 1616 English translation of Napier’s logarithms printed a point-like separator; Napier’s *Rabdologia* (1617) used both point and comma.
- **[Modern convention]** English-language practice generally uses a point for decimals and comma for thousands; much of continental Europe reverses them. International technical practice also uses spaces for grouping.

The detailed priority evidence is collected by [MacTutor’s history of fraction symbols](https://mathshistory.st-andrews.ac.uk/Miller/mathsym/fractions/).

## 8. Signs, ligatures, and abbreviations

The system itself requires no numeral ligatures: `37` is simply `3` followed by `7`. Nevertheless scribal and typographic practice produced:

- joined handwritten digits in rapid account scripts;
- superior and inferior figures;
- vulgar-fraction characters such as `½`, `⅓`, `¾`;
- ordinal abbreviations such as `1st`, French `1er`, Italian `1º`;
- commercial abbreviations and overlines;
- exponent notation, as in `10³`;
- scientific `E` notation, as in `1.5E6`;
- signs for percent `%`, per mille `‰`, currency, plus/minus, and accounting parentheses.

These are extensions surrounding the ten-digit system, not additional digits.

---

# Origins: dated and placed

## 1. Before numerals: tally-like artefacts

### Lebombo bone

- **[Artefact]** A notched bone from Border Cave in the Lebombo Mountains of southern Africa, generally assigned to the Later Stone Age; modern estimates often place it roughly 44,000–42,000 years before present.
- It preserves 29 incisions and is broken at one end.
- **[Scholarly reconstruction]** It may be a tally.
- **[Disputed]** Interpretation as a lunar or menstrual calendar rests mainly on the number of surviving marks. No inscription identifies its function, and the broken end means 29 need not be the original total.
- **Finding:** it is not evidence for decimal place-value notation and is not an ancestor demonstrably connected to Hindu-Arabic numerals.

### Ishango bone

- **[Artefact]** Found in 1950 by Jean de Heinzelin near Ishango, then Belgian Congo, now Democratic Republic of Congo; commonly dated around 20,000 years before present. It is held by the Royal Belgian Institute of Natural Sciences.
- Three columns of grouped incisions appear on a bone bearing a quartz point.
- **[Scholarly reconstruction]** Jean de Heinzelin saw arithmetical patterns; Alexander Marshack later proposed lunar calendrical use.
- **[Disputed]** Interpretations include tally, doubling, primes, base 12, base 10, or a lunar record. The groupings are real; their intended semantics are not recoverable.
- **[Modern cultural tradition]** It is frequently called the oldest mathematical instrument. That phrase is interpretive, not an archaeological reading.

The general methodological problem is decisive: parallel notches can count, decorate, schedule, record ownership, or serve another purpose, and there is no universally reliable way to identify their intended meaning from shape alone.

## 2. Near Eastern tokens and Uruk numerical tablets

- **[Artefact]** Small clay tokens occur at many Southwest Asian sites from approximately 7500 BCE; sealed clay envelopes and impressed numerical tablets appear in the fourth millennium BCE.
- **[Artefact]** Late Uruk tablets, approximately 3200–3000 BCE, contain numerical and metrological signs used in accounting.
- **[Scholarly reconstruction]** Denise Schmandt-Besserat argued from the 1970s onward that plain and complex tokens encoded commodities and quantities, that impressions of tokens on envelopes led to numerical signs, and that this accounting technology helped generate writing.
- **[Qualified consensus/dispute]** Correspondence between some plain tokens and later impressions is widely accepted. Her stronger continuous-evolution theory, universal functional assignments, and claims about abstract-number cognition have been criticized as exceeding the evidence.

Schmandt-Besserat’s mature account draws on about 8,000 tokens from Turkey to Iran. [Her summary](https://www.cambridge.org/core/books/abs/archaeology-of-measurement/token-system-of-the-ancient-near-east-its-role-in-counting-writing-the-economy-and-cognition/0AB9E89E74F94FE95F53B145F59CCA59); [constructive reassessment of early numeracy](https://doi.org/10.1016/j.hm.2020.08.002).

Mesopotamian numeration later used base-60 place-value notation. Old Babylonian scribes could leave an internal blank; much later texts used paired wedges as a placeholder. They did not normally write a terminal zero and did not treat that sign as the number zero. **[Artefact plus reconstruction]** This is an independent predecessor of positional technique, not a demonstrated direct ancestor of Indian decimal notation.

## 3. Egyptian numeration and the Narmer macehead

- **[Artefact]** The ceremonial Narmer macehead was excavated by James Quibell and Frederick Green at Hierakonpolis in 1897–98 and dates to the late fourth millennium BCE, conventionally around 3100 BCE. It is in the Ashmolean Museum, Oxford, inventory **AN1896–1908 E.3915**.
- Its lower register contains Egyptian numerical signs conventionally read as enormous totals, often 400,000 cattle, 1,422,000 smaller livestock, and 120,000 captives.
- **[Disputed interpretation]** Whether these are literal booty totals, idealized royal abundance, or numbers attached differently to the pictorial elements is debated. Their scale makes literal readings doubtful.
- Egyptian hieroglyphic numerals were decimal but primarily additive, using repeated power-of-ten signs. They are not positional and are not a direct structural source for Hindu-Arabic notation.

The museum-associated discussion is available in [Ashmolean, “Object in Focus: The Narmer Mace-Head”](https://www.hierakonpolis-online.org/files/hk_nn/nn-31-2019.pdf); object data and bibliography appear in the [Narmer Catalog](https://narmer.org/inscription/0080.pdf).

## 4. Babylonian mathematical texts

### Plimpton 322

- **[Artefact]** Old Babylonian clay tablet, usually dated about 1800 BCE, probably from southern Iraq; Columbia University Rare Book and Manuscript Library, **Plimpton 322**.
- It contains a sexagesimal table associated with right-triangle relations.
- **[Disputed]** Competing interpretations call it a table of Pythagorean triples, a reciprocal-table exercise, a teacher’s table, or trigonometric in some broader sense. Calling it a modern trigonometry table can overstate the evidence.
- The tablet shows the power of place-value computation without a full zero digit.

### Høyrup and Robson

Jens Høyrup reconstructs Babylonian problem traditions through philology and procedural vocabulary; Eleanor Robson emphasizes scribal schooling, tablet archaeology, and the danger of translating Old Babylonian procedures directly into timeless modern algebra. Their work is methodologically important here: identical-looking calculations do not prove direct transmission of signs.

## 5. Egyptian fraction arithmetic: the Rhind Papyrus

- **[Artefact]** British Museum **EA10057**, with other fragments in Brooklyn; copied by the scribe Ahmose around 1550 BCE from an older exemplar.
- **[Documented text]** It contains 84 problems concerning arithmetic, unit fractions, distribution, geometry, and administration.
- Egyptian scribes normally decomposed fractions into sums of distinct unit fractions, with special notation for some common values.
- The papyrus was purchased at Luxor by Alexander Henry Rhind in 1858; its modern name therefore records ownership, not authorship.
- It is not ancestral evidence for Indian positional digits, but it demonstrates how sophisticated arithmetic can flourish in a non-positional notation.

[British Museum catalogue, EA10057](https://www.britishmuseum.org/collection/object/Y_EA10057).

## 6. Brahmi numerals: the graphic ancestry

### Aśokan inscriptions

- **[Artefact]** Third-century BCE inscriptions associated with Aśoka contain early Brahmi numeral signs, especially forms for 1, 4, and 6.
- These numerals were not yet a ten-digit positional system. Brahmi possessed separate signs for units, tens, hundreds, and larger values and combined them additively or multiplicatively-additively.
- **[Scholarly reconstruction]** Modern western digits descend graphically, through many intermediate hands, from Brahmi-family signs. The remote origin of the earliest Brahmi signs remains less certain than that later descent.

### Naneghat/Nāṇāghāṭ

- **[Artefact]** Satavahana-period Prakrit inscriptions in the Naneghat pass, Maharashtra, usually dated to the late second or first century BCE.
- Numeral signs record large sacrificial gifts.
- Chrisomalis gives `24,400` as a compound expression equivalent to \(1000\times20+1000\times4+100\times4\): a mixed multiplicative-additive notation, not positional writing.
- The inscriptions were reported in the nineteenth century and studied through the Bombay Archaeological Survey and *Epigraphia Indica*.

### Nasik/Nashik caves

- **[Artefact]** Inscriptions from approximately the first–second centuries CE include numerous Brahmi numbers; one important rubbing is dated about 120 CE.
- Some numbers are written both in words and figures, which helped James Prinsep, Bhagwanlal Indraji, Georg Bühler, Émile Senart, and later epigraphists establish their readings.
- **Finding:** The forms provide palaeographic ancestors for several digits, but neither Naneghat nor early Nasik demonstrates the complete zero-bearing positional system.

See Chrisomalis, pp. 190 onward, and Richard Salomon’s account of decipherment and numeral methodology in [*Indian Epigraphy*](https://rapeutation.com/salomonindianepigraphy.pdf).

## 7. Place-value in Sanskrit language

Long before all surviving manuscripts can be securely dated, Sanskrit astronomical and mathematical texts used:

- power-of-ten number words;
- word numerals (*bhūtasaṃkhyā*), where objects conventionally signify values—moon = 1, eyes = 2, Vedas = 4, and so forth;
- alphabetic schemes such as Āryabhaṭa’s syllabic number notation;
- place-value order, often with numbers spoken or versified from units upward.

### Āryabhaṭa

- **[Documented text]** Āryabhaṭa composed the *Āryabhaṭīya* in 499 CE.
- It employs an alphabetic numerical scheme useful for versified astronomical constants.
- **Finding:** Āryabhaṭa demonstrates decimal place-value thought, but not the ordinary ten written digits in the modern fashion. His system should not be presented as simply `0–9` in disguise.

## 8. The Bakhshali manuscript

- **[Artefact]** A birch-bark mathematical manuscript discovered in 1881 near Bakhshali, now in Pakistan; Bodleian Library, Oxford, **MS. Sansk. d. 14**.
- It contains prose rules, examples, arithmetic, algebraic problems, square-root approximations, and a dot used in empty positions and sometimes in other notational roles.
- **[Documented palaeographic fact]** The manuscript is physically composite, written on separate pieces of bark, and likely copied from older mathematical material.
- **[Radiocarbon result]** Tests announced by the Bodleian in 2017 produced strikingly different ranges for three leaves: roughly the third–fourth, eighth–ninth, and tenth centuries CE.
- **[Disputed inference]** The Bodleian publicity treated the earliest bark range as evidence for a very early zero dot. Kim Plofker, Agathe Keller, Takao Hayashi, Clemency Montelle, and Dominik Wujastyk objected that dating three bark samples does not date the composition, ink, scribal act, or whole composite manuscript; palaeography and textual unity also require consideration.
- **Finding:** The radiocarbon measurements are evidence about the bark samples. They do not by themselves prove that the complete surviving mathematical text, or even every visible dot, was written in the earliest range.
- **Further caution:** The Bakhshali dot is a place marker in written calculation. Calling it the first fully developed number zero collapses the distinction between placeholder and arithmetic object.

The specialist response is open access: [Plofker et al., “The Bakhshālī Manuscript: A Response to the Bodleian Library’s Radiocarbon Dating”](https://journals.library.ualberta.ca/hssa/index.php/hssa/article/view/22).

## 9. Brahmagupta and zero as an operand

- **[Documented text]** Brahmagupta composed the *Brāhmasphuṭasiddhānta* at Bhillamāla in 628 CE.
- Chapter 18 sets out arithmetic rules for positive quantities, debts/negative quantities, and *śūnya*, zero.
- In modernized paraphrase:
  - a number plus zero is unchanged;
  - a number minus zero is unchanged;
  - zero minus a positive number is negative;
  - zero minus a negative number is positive;
  - zero times a number is zero.
- **[Historical limitation]** Brahmagupta did not give the modern rule that division by zero is undefined. His statements about a number divided by zero and zero divided by zero are obscure or mathematically unacceptable by modern field arithmetic.
- **[Significance]** This is the earliest surviving systematic set of arithmetic rules treating zero together with positive and negative quantities.
- **Not a claim of creation ex nihilo:** The text proves Brahmagupta’s formulation in 628, not the personal identity of the first human ever to conceptualize zero.

Sanskrit text and verse concordance: [TITUS edition](https://titus.fkidg1.uni-frankfurt.de/texte/etcs/ind/aind/klskt/mathemat/brsphsd/brspht.htm). The foundational English translation is H. T. Colebrooke, *Algebra, with Arithmetic and Mensuration, from the Sanscrit of Brahmegupta and Bháscara* (London, 1817).

## 10. The Gwalior inscription

- **[Artefact]** Two Sanskrit inscriptions are cut on the Chaturbhuj/Chatur-bhuja temple at Gwalior Fort, Madhya Pradesh.
- The relevant inscription is dated Vikrama year 933, conventionally **876 CE**, under Bhojadeva.
- It records land dimensions including `270` and provision for `50` garlands; circular zero signs occur within positional numerals.
- **[Publication history]** The inscriptions were described by Alexander Cunningham and edited in *Epigraphia Indica*, vol. 1.
- **[Status]** It is the earliest widely accepted, securely dated Indian inscription containing a circular zero in ordinary decimal place-value numerals.
- **Dating caution:** Some secondary pages say 875 or 870. The inscriptional date is Vikrama 933; conversion and regnal/calendar conventions explain some variation, but 876 CE is standard.
- It has no museum inventory because it remains in situ.

Primary epigraphic publication: [*Epigraphia Indica*, vol. 1, “The Two Inscriptions of the Vaillabhaṭṭasvāmin Temple at Gwalior”](https://upload.wikimedia.org/wikipedia/commons/d/dc/Epigraphia_Indica_Vol_1_%281892%29.pdf).

## 11. Independent Maya zero and the Dresden Codex

- **[Artefact/system]** Classic Maya scribes used a vigesimal positional notation, with dots for ones, bars for fives, and a shell-like zero.
- The calendrical Long Count modifies strict base 20 at one position: 18 *uinals* make a *tun*, approximating the solar year.
- Early Maya zero signs occur centuries before the Dresden Codex; exact “first” claims depend upon whether an inscription is securely dated and whether the shell sign is calendrical or numerical.
- **[Independent invention]** No credible transmission route connects the Maya zero with India, Babylonia, or the Islamic world.
- **[Artefact]** The Dresden Codex, SLUB Dresden **Mscr. Dresd. R. 310**, is a pre-Columbian Maya screenfold, generally dated to the Postclassic period. It contains ritual almanacs, eclipse and Venus tables, and large calendrical numbers.
- **[Documented modern decipherment]** Ernst Wilhelm Förstemann, librarian at Dresden, recognized key calendrical and numerical structures in the late nineteenth century.
- **[Colonial destruction]** Diego de Landa reported the burning of Maya books at Maní in 1562. Only four generally accepted pre-Columbian Maya codices survive.
- **Qualification:** Maya communities and calendrical knowledge did not simply “die.” The elite written tradition was catastrophically disrupted; the Long Count and Maya calendar have since been subjects of epigraphic recovery and Indigenous cultural renewal.

[SLUB Dresden, codex contents](https://www.slub-dresden.de/en/explore/manuscripts/the-dresden-maya-codex/content).

---

# Arithmetic and instruments

## 1. Finger reckoning

Finger counting is nearly universal but not uniform:

- fingers may represent single units;
- thumb joints and finger segments permit counting in twelves;
- one hand can mark units while the other records groups of five or ten;
- medieval European finger-reckoning traditions assigned gestures to values far beyond ten.

The English word **digit**, from Latin *digitus*, “finger/toe,” records the body-number association. The bodily origin of base ten is plausible and widely reconstructed, but no single prehistoric event can be documented.

## 2. Counting boards, counters, and abaci

A written numeral system and a calculating technique are distinct. Greeks, Romans, medieval Europeans, Chinese practitioners, and merchants often recorded results in one notation while calculating materially in another.

### Roman *calculus*

- Latin *calculus* means a small pebble.
- Pebbles or counters placed on ruled boards represented values by column.
- From this comes *calculation* and, much later, mathematical *calculus*.
- Roman numeral inscriptions’ lack of a standard zero did not prevent an empty column on a board from representing no counters in that place.

Thus “Romans had no zero” is tolerable only if narrowed to “standard Roman inscriptional numerals had no ordinary zero digit.” Roman reckoners certainly handled absence, null results, and empty columns.

### Roman hand abacus

Surviving Roman portable abaci use grooves and sliding beads for decimal places, plus special fractional positions. One much-reproduced example is in the Bibliothèque nationale de France; alleged references to “the Roman abacus in the Louvre” require care because catalogues, replicas, and nineteenth-century drawings have often been conflated. **Absence-of-evidence finding:** no securely identified Louvre inventory number was established in the consulted catalogue material, so the anecdote should not be repeated without a specific collection record.

A useful museum-style description of Roman *abacus* and *calculi* is provided in the Fribourg exhibition catalogue [*Des chiffres ou des lettres*](https://fri-memoria.bcu-fribourg.ch/uploads/r/bcu-fribourg/b/e/7/be71634cb35b1bda72f1ba4a8e8b45d95b4765213c846c4ac31b13d5f19da631/Des_chiffres_ou_des_lettres__compter__calculer__mesurer____l___poque_romaine.pdf).

## 3. Medieval counter-casting

Medieval European counting tables or cloths were divided into monetary and place-value lines. A counter on a line had one value; between lines it could have five times that value. Treasury, mint, market, and household officials could calculate rapidly without writing intermediate Hindu-Arabic numerals.

English *Exchequer* derives from the chequered calculating cloth used in royal accounting.

## 4. Chinese counting rods

- Rod numerals used vertical and horizontal configurations for 1–9, alternating orientation by decimal place so adjacent columns remained distinguishable.
- A blank space served for zero; later written traditions adopted a zero circle.
- Negative quantities could be distinguished by rod color or other convention.
- **[Documented textual practice]** Procedures preserved in the *Nine Chapters on the Mathematical Art*, compiled over centuries and canonically edited with Liu Hui’s commentary of 263 CE, presuppose calculations performed on a counting surface.
- **[Disputed transmission]** Chinese rod notation and Indian decimal positional notation are structurally comparable. Some historians proposed Chinese priority or influence through Central Asia; others stress the lack of a documented transmission chain and the significant differences in written practice.
- The earliest surviving rods rarely remain in their original arrangement, so texts and diagrams supply much of the reconstruction.

Li Chunfeng and colleagues canonized the *Ten Mathematical Classics* in 656. A current study of the connection between textual algorithms and material rods is [Karine Chemla, “The interplay between textual procedures and material operations”](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7E654BC8863452F26F2E0C43892699F4/S0269889725100860a.pdf/div-class-title-the-interplay-between-textual-procedures-and-material-operations-from-the-viewpoint-of-chinese-mathematical-texts-div.pdf).

## 5. Suanpan and soroban

- The Chinese **suanpan** normally has two upper beads worth five each and five lower unit beads per rod in its widely known late form.
- A 1337 Chinese text depicts an instrument generally accepted as an abacus; surviving physical examples are later, chiefly from the sixteenth century onward.
- The Japanese **soroban** evolved toward one five-bead and four unit-beads per rod, well suited to decimal calculation.
- These instruments implement place value materially. They do not require the user to inscribe zero: a cleared rod is an empty place.
- Written Arabic numerals today coexist with suanpan/soroban education; the instruments did not generate the shapes `0–9`.

Chrisomalis notes the 1337 depiction and sixteenth-century surviving suanpans in [*Numerical Notation*](https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20%28CUP%2C%202010%29%28ISBN%200521878187%29%28O%29%28498s%29_MPop_.pdf).

## 6. Quipu/khipu

Andean khipus encode numerical information through knots, position, cord hierarchy, color, and direction:

- long knots commonly encode units;
- clusters of single knots encode higher decimal places;
- absence in a position functions like zero;
- subsidiary cords create hierarchical records.

**[Artefact and ethnohistorical evidence]** Many khipus are accounting records, and Spanish colonial texts describe specialists called *khipukamayuq*.  
**[Disputed/open]** Whether some encode narrative or phonetic information remains debated.  
**Finding:** Decimal positional structure can exist in a non-written, tactile medium; there is no historical connection to Indian numeral glyphs.

## 7. Paper algorithms

The decisive practical advantage of the Hindu-Arabic system is not that Roman numeral users were incapable of arithmetic. It is that place-value digits let one preserve all intermediate states of an algorithm on paper.

### Addition

```text
  5072
+  958
------
  6030
```

Columns directly align equal powers of ten. Carrying converts ten units into one ten, ten tens into one hundred, and so forth.

### Multiplication

```text
     237
×     46
--------
    1422     (237 × 6)
+  9480      (237 × 40)
--------
   10902
```

### Division

Long division repeatedly estimates a place-value digit, multiplies, subtracts, and brings down the next digit. Zero must sometimes be inserted in the quotient to preserve place.

Islamic arithmetic texts describe several arrangements—dust-board calculation, finger arithmetic, sexagesimal astronomical calculation, and ink-on-paper methods. The history is therefore not a simple replacement of “abacus” by “written digits.”

## 8. Al-Uqlidisi

- **[Documented text]** Abū al-Ḥasan al-Uqlīdisī composed *Kitāb al-Fuṣūl fī al-ḥisāb al-hindī* at Damascus in 952–953 CE.
- He adapted Hindu arithmetic to pen and paper, explicitly avoiding dependence on a dust board and erasure.
- His work is crucial evidence that calculation media affected algorithms and notation.

## 9. Algorists and abacists

“Abacist versus algorist” compresses a long coexistence into a memorable opposition:

- **abacist:** calculates with counters on a board or cloth;
- **algorist:** uses written Hindu-Arabic digits and procedures descended from Arabic arithmetic.

They were not necessarily hostile professional castes, and many practitioners knew both methods.

### Reisch’s *Typus arithmeticae*

- **[Artefact/printed image]** Gregor Reisch’s *Margarita philosophica*, Freiburg, 1503, contains the famous *Typus arithmeticae* woodcut.
- Lady Arithmetic stands between a figure labeled Boethius using written digits and Pythagoras using counters.
- The written calculator’s side appears favored, and Arithmetic’s garment bears numeral signs.
- **[Later interpretation]** It is routinely presented as a literal contest between algorists and abacists. It is more securely an allegory of two methods and their authorities.

[Library of Congress catalogue and image](https://www.loc.gov/pictures/item/92518152/).

---

# Surviving textbooks and worked traditions

## 1. Rhind Papyrus

As above: unit-fraction decomposition, false position, distribution, bread and beer measures, areas, and volumes. It demonstrates algorithmic thought within hieratic Egyptian notation.

## 2. Plimpton 322

A table rather than an explanatory textbook. Reconstructions of its generating algorithm depend on regularities in sexagesimal entries and knowledge from parallel tablets.

## 3. *Nine Chapters*

The text contains 246 problems in its received form, ranging across land measurement, grain exchange, distribution, taxation, linear equations, and right triangles. Liu Hui’s 263 commentary explains and justifies many procedures. Computation was performed with rods, and the text’s imperative algorithms were read alongside those material actions.

## 4. Āryabhaṭa

The *Āryabhaṭīya* gives condensed verse rules in astronomy and mathematics: place-value language, roots, progressions, geometry, trigonometric tables, and the *kuṭṭaka* pulverizer for indeterminate equations. Commentators such as Bhāskara I expanded terse verses into worked practice.

## 5. Brahmagupta

The *Brāhmasphuṭasiddhānta* includes arithmetic, geometry, algebra, astronomical computation, equations, surds, interpolation, and rules for debts, fortunes, and zero. Its zero rules are historically fundamental but not identical to modern axioms.

## 6. Al-Khwarizmi

- Muḥammad ibn Mūsā al-Khwārizmī worked in Abbasid Baghdad in the early ninth century, associated with al-Maʾmūn’s learned milieu.
- **[Lost original]** His Arabic *Kitāb al-ḥisāb al-hindī*, usually dated approximately 825, does not survive.
- **[Surviving mediated text]** A twelfth-century Latin adaptation/translation survives, beginning *Dixit Algorizmi* and conventionally published as *Algoritmi de numero Indorum*.
- It teaches decimal digits, addition, subtraction, doubling, halving, multiplication, division, and fractions.
- Because the Arabic original is lost, exact statements about its title, diagrams, zero glyph, and wording must be attributed to reconstruction through Latin witnesses.
- The principal Latin witness used by Crossley and Henry is Cambridge University Library **MS Ii.vi.5**.

[Max Planck Institute ISMI record and facsimile](https://ismi.mpiwg-berlin.mpg.de/text/336395); [Crossley and Henry, “Thus spake al-Khwārizmī”](https://www.sciencedirect.com/science/article/pii/031508609090048I).

### Al-Kindi

Yaʿqūb ibn Isḥāq al-Kindī, c. 801–873, reportedly wrote a four-part work *On the Use of the Indian Numerals*. **[Documented bibliographic tradition, lost text]** Its existence is known from medieval bibliographical testimony, but the work does not survive, preventing detailed comparison with al-Khwarizmi.

## 7. Fibonacci’s *Liber Abaci*

- Leonardo of Pisa, later nicknamed Fibonacci, was born around 1170.
- **[Documented autobiographical text]** In his prologue he says his father was posted with Pisan merchants at Bugia/Bougie, now Béjaïa in Algeria, and had him instructed in calculation there.
- He encountered Indian arithmetic through the Arabic-speaking commercial Mediterranean and traveled to other trading centers.
- The first *Liber Abaci* was completed in Pisa in 1202; the surviving revised version dates from 1228.
- Its opening presents nine Indian figures and the sign `0`, called *zephirum*: *cum his itaque novem figuris, et cum hoc signo 0, quod arabice zephirum appellatur…*
- It covers whole-number operations, fractions, currency and measure conversions, barter, partnerships, alloying, interest-like commercial problems, algebra, and recreational problems.
- The rabbit problem that generated the later-named Fibonacci sequence is a very small part of the book.
- **Qualification:** Fibonacci did not introduce the digits to a Europe that had never seen them—the Codex Vigilanus predates him by more than two centuries. His achievement was a large, practical Latin synthesis and powerful commercial exposition.

Latin chapter list: [*Liber abbaci*](https://la.wikisource.org/wiki/Liber_abbaci/Capitula). Modern edition: Laurence E. Sigler, trans., *Fibonacci’s Liber Abaci* (Springer, 2002).

## 8. Sacrobosco

- Johannes de Sacrobosco, active in the early thirteenth century, wrote the widely copied *Algorismus vulgaris* or *Tractatus de arte numerandi*.
- It organized arithmetic into operations such as numeration, addition, subtraction, mediation, doubling, multiplication, division, extraction of roots, and related procedures.
- Its pedagogical brevity made it a university standard, supplemented by commentaries.
- Vatican **Pal. lat. 1420**, fols. 37r–40v, preserves one witness. [Digital manuscript](https://digi.ub.uni-heidelberg.de/diglit/bav_pal_lat_1420/0181/scroll); [IRHT work record](https://fama.irht.cnrs.fr/oeuvre/268660).

## 9. Pacioli

Luca Pacioli’s *Summa de arithmetica, geometria, proportioni et proportionalità*, Venice, 1494:

- synthesized commercial arithmetic, algebra, bookkeeping, measurement, and mathematical vocabulary;
- used printed Hindu-Arabic numerals;
- became famous for its exposition of Venetian double-entry bookkeeping, though it did not invent the practice;
- belongs to a growing incunable tradition of printed commercial arithmetics.

## 10. Robert Recorde

Robert Recorde’s English *The Ground of Artes* first appeared in 1543 and repeatedly expanded thereafter. It taught numeration and arithmetic in the vernacular, helping normalize Hindu-Arabic written computation in England. Recorde later introduced the equals sign in *The Whetstone of Witte* (1557), explaining his parallel lines as things that “can be no more equal.”

## 11. Napier

John Napier’s logarithms reduced multiplication to addition of logarithms; his *Rabdologiae* (1617) presented “Napier’s bones,” rods carrying multiplication tables. The rods combined physical manipulation with printed Hindu-Arabic numerals. Napier’s publications also helped popularize point/comma decimal separation, though he was not the unique inventor of decimal fractions or their separator.

---

# Transmission and replacement

## 1. India to the Islamic world

### Early notice

- **[Documented text]** Severus Sebokht, a Syriac bishop writing in 662 CE, praised the “subtle discoveries” of Indians and their calculation “by means of nine signs.”
- This is an important external witness to Indian digit reckoning.
- It mentions nine signs, not an explicit tenth zero sign.

### Abbasid translation

- Under the caliph al-Manṣūr, an Indian astronomical work was reportedly brought to Baghdad around 770 and translated by al-Fazārī and Yaʿqūb ibn Ṭāriq; Arabic writers called the resulting tradition *Sindhind*, from Sanskrit *siddhānta*.
- **[Tradition supported by Arabic historiography]** Details vary among later bibliographical accounts.
- Brahmagupta’s astronomical tradition influenced this material, but a simple line “Brahmagupta → one literal Arabic translation → al-Khwarizmi” is too neat for the surviving evidence.

### Al-Khwarizmi, c. 825

His lost work gave the Indian techniques a durable Arabic and Latin career. Islamic mathematicians did not merely courier the system: they compared numeral forms, adapted algorithms to dust boards and paper, integrated decimal and sexagesimal practice, and wrote extensive teaching traditions.

## 2. Eastern and western Arabic forms

Two broad graphic families developed:

- **Eastern Arabic-Indic:** `٠١٢٣٤٥٦٧٨٩`, with Persian and Urdu variants `۰۱۲۳۴۵۶۷۸۹`.
- **Western Arabic or Maghribi/ghubār ancestors:** forms that contributed more directly to medieval European digits.

*Ghubār* means “dust,” conventionally associated with reckoning on a dust board, but the nomenclature and exact relation among “ghubār,” western forms, and individual manuscript traditions are more complicated than popular family-tree diagrams imply.

Al-Biruni, writing about India around 1030, explicitly observed that Indian numeral signs varied regionally just as letters did. **[Documented text]** This undercuts the myth of one canonical original set.

## 3. The Codex Vigilanus, 976

- **[Artefact]** The Codex Vigilanus or Albeldensis was compiled by the monks Vigila, Sarracino, and García at San Martín de Albelda in Rioja and completed in 976. It is held at the Real Biblioteca del Monasterio de El Escorial, **MS d.I.2**.
- It displays nine western Arabic/Indian-derived signs, ordered `9 8 7 6 5 4 3 2 1`, without zero.
- The Latin text says, in part:

> *Scire debemus Indos subtilissimum ingenium habere… Et hoc manifestum est in novem figuris…*

“We ought to know that the Indians possess a most subtle intelligence … and this is manifest in the nine figures…”

- **Status:** earliest securely dated Latin Christian manuscript to display the nine numerals.
- **Qualification:** it proves knowledge of their forms and attribution to India, not widespread practical use in tenth-century western bookkeeping.

[Image and transcription](https://commons.wikimedia.org/wiki/File%3ACodex_Vigilanus_Primeros_Numeros_Arabigos.jpg).

## 4. Gerbert of Aurillac and the apices

Gerbert, c. 946–1003, studied in Catalonia in the 960s, taught at Reims, became archbishop of Reims and Ravenna, and in 999 became Pope Sylvester II.

- **[Documented reconstruction]** Gerbert and his circle used a calculating board with marked counters called *apices*. The labels corresponded to nine numeral signs; an empty column supplied place vacancy.
- **[Disputed details]** No authenticated complete Gerbertian set survives, and descriptions come substantially from pupils and later manuscripts. Whether Gerbert personally learned the forms directly from Muslim teachers, Mozarabic intermediaries, or Latin Catalan sources cannot be shown.
- **[Important limitation]** His apparatus did not require a zero counter, so it transmitted digit-labeled positional board computation without necessarily transmitting written zero-based algorithms.
- **[Tradition/legend]** Later hostile stories made his scientific learning magical: a stolen book, Muslim sorcerer, talking brazen head, or pact with the devil. These stories are evidence for medieval attitudes toward learned technology, not for Gerbert’s actual instruction.

## 5. Twelfth-century translations

Translation centers in Iberia and elsewhere rendered Arabic mathematical works into Latin. Named translators include Adelard of Bath, John of Seville, Robert of Chester, and Gerard of Cremona, but attribution of the surviving *Algoritmi de numero Indorum* is uncertain. **[Disputed attribution]** It should not automatically be assigned to Adelard or John without a particular manuscript argument.

## 6. Fibonacci, 1202 and 1228

Fibonacci’s *modus Indorum* joined written numerals to problems of merchants moving among Pisa, Bugia, Egypt, Syria, Provence, Sicily, and Byzantium. His book’s readership was initially specialist; broad replacement came through many abacus-school manuals, merchants, notaries, printers, astronomers, and teachers rather than a single publication.

## 7. The alleged Florentine ban of 1299

The usual story says Florence “banned Arabic numerals” in 1299 because `0` could be altered into `6` or `9` and digits were easier to falsify than written Roman numerals.

The evidence requires narrower wording:

- **[Documented statutory tradition]** Statutes associated with the Florentine money-changers’ guild required entries to be made in letters rather than *figures*.
- **[Scholarly interpretation]** Fraud resistance is a reasonable explanation: abbreviated digits are easier to alter, interpolate, or erase than fully written sums.
- **[Overstatement/modern retelling]** This was not a general municipal prohibition on possessing, teaching, printing, or calculating with Arabic numerals. “Florence banned zero” is still less defensible.
- **[Open bibliographical problem]** Popular accounts repeatedly cite 1299 without reproducing the exact archival statute, folio, recension, and original Italian/Latin. Until those are supplied, the precise scope and wording should remain qualified.
- The rule illustrates coexisting media: merchants could calculate with digits but enter legally sensitive totals in words.

## 8. Abacus schools and merchant arithmetic

From the thirteenth through sixteenth centuries, Italian *maestri d’abaco* taught:

- decimal written arithmetic;
- complex currencies and measures;
- partnership, barter, interest, exchange, and alloy problems;
- algebra in vernacular settings.

Here *abaco* often meant the commercial mathematical discipline, not necessarily a bead frame. This linguistic fact complicates any sharp “abacists versus algorists” narrative.

## 9. Printing

- European movable-type printing stabilized digit repertoires but did not immediately standardize shapes.
- Early printers cut forms suited to local manuscript hands.
- Commercial arithmetics, calendars, astronomical tables, bookkeeping texts, and page numbers spread the digits.
- By the sixteenth century, the western set was recognizable, though `4`, `5`, and `7` remained especially variable.
- Tabular composition encouraged equal-width figures; logarithmic and astronomical tables made exact alignment economically important.

## 10. Replacement was functional, not absolute

Hindu-Arabic numerals progressively displaced Roman numerals in:

- arithmetic;
- accounts;
- science;
- page numbering;
- dates;
- statistics;
- mechanical and electronic computation.

Roman numerals survived where their non-positional form signaled rank, sequence, ceremony, antiquity, or display:

- monarchs and popes: Charles III, Benedict XVI;
- book volumes, chapters, prefaces, and clock faces;
- monumental inscriptions and foundation dates;
- film copyright dates;
- Super Bowls.

The NFL used Roman numerals from Super Bowl V, temporarily wrote **Super Bowl 50** rather than **L**, and returned to Roman numerals afterward. **[Documented modern branding]** [Contemporary report](https://time.com/2822841/nfl-super-bowl-50-l/).

Clock dials often use `IIII` rather than `IV`. Explanations include visual balance against `VIII`, manufacturing economy in cast sets, deference to Jupiter’s Latin name `IVPPITER`, and royal preference. **[Tradition/disputed]** No single universal cause is documented; different makers and periods may have had different reasons.

## 11. East Asia today

Arabic numerals coexist with Chinese-character numerals:

- China: `0–9` dominate much horizontal technical, financial, and digital writing; `一二三四五六七八九十` remain normal in words and formal contexts, with financial anti-fraud forms such as `壹贰叁`.
- Japan: Arabic digits are common in horizontal writing, measurements, addresses, prices, and technology; kanji numerals remain common in vertical text, traditional dates, idioms, legal and ceremonial forms.
- Korea: Arabic digits are ubiquitous, alongside Sino-Korean number words and occasional Chinese characters in formal or historical contexts.

This is functional coexistence, not incomplete replacement.

## 12. Global computing

Modern computing gives the western digits a second, technical universality:

- ASCII assigns `0–9` contiguous code points U+0030–U+0039.
- Unicode encodes numerous script-specific decimal sets, each with decimal digit values.
- Locale software selects glyph set, decimal separator, grouping, currency pattern, and directionality.
- Credit cards, scientific datasets, identifiers, and programming languages often privilege ASCII digits even where local typography uses another set.

Unicode explicitly says encoding a script-specific digit set does not mean it is the preferred set in every locale. [Unicode digit terminology](https://www.unicode.org/terminology/digits.html); [CLDR numbers specification](https://unicode.org/reports/tr35/tr35-numbers.html).

---

# People

## South Asia

- **Aśokan officials and stonecutters**, third century BCE: earliest securely contextualized Brahmi digit forms.
- **Nāganikā and Satavahana patrons**, late second/first century BCE: Naneghat sacrificial donation inscriptions.
- **Āryabhaṭa** (born 476; *Āryabhaṭīya*, 499): decimal place-value verbal and alphabetic computation.
- **Bhāskara I**, seventh century: commentator who made Āryabhaṭa’s compressed rules operational.
- **Brahmagupta** (598–after 665): rules for zero, debts, fortunes, and algebra in 628.
- **Mahāvīra**, ninth century: extensive arithmetic in the *Gaṇitasārasaṅgraha*, including zero-related rules but difficulties with division by zero.
- **Bhāskara II** (1114–c. 1185): *Līlāvatī* and *Bījagaṇita*; refined arithmetic and algebra, while sometimes treating division by zero through an “infinite” quantity in ways unlike modern analysis.
- **Bakhshali scribes**, names unknown: copied and worked a practical mathematical tradition on birch bark.
- **Alla, son of Vaillabhaṭṭa**, ninth century: named patron associated with the Gwalior temple inscription.

## Islamic world

- **Severus Sebokht**, died 666/667: Syriac witness to Indian computation with nine signs.
- **Al-Manṣūr**, Abbasid caliph 754–775: patronal setting for early Indian astronomical transmission.
- **Muḥammad al-Fazārī**, eighth century: associated with the Arabic *Sindhind* translation tradition.
- **Al-Khwarizmi**, active c. 820–850: author of the lost Arabic Hindu arithmetic; Latinized name generated *algorism* and *algorithm*.
- **Al-Kindi**, c. 801–873: author of a lost multi-part work on Indian numerals.
- **Al-Uqlidisi**, tenth century: adapted Indian calculation to ink and paper.
- **Al-Biruni**, 973–after 1050: described Indian sciences, languages, and regional numeral variation.
- **Kushyar ibn Labban**, c. 971–1029, and **al-Nasawi**, eleventh century: important expositors of Hindu arithmetic.

## Latin Europe

- **Vigila, Sarracino, and García**, tenth-century monks: compilers/scribes of the Codex Vigilanus.
- **Gerbert of Aurillac/Pope Sylvester II**, c. 946–1003: apex-board computation.
- **Bernelinus and Richer of Reims**, Gerbert’s circle: transmitters of descriptions and methods.
- **Twelfth-century translators**, including John of Seville and Adelard of Bath: Arabic-to-Latin mathematical transfer, although attribution of individual arithmetic translations remains disputed.
- **Leonardo of Pisa/Fibonacci**, c. 1170–after 1240: *Liber Abaci*, 1202/1228.
- **Guglielmo Bonacci**, Fibonacci’s father: Pisan commercial official in Bugia; central to Leonardo’s autobiographical transmission story.
- **Johannes de Sacrobosco**, active early thirteenth century: university algorism.
- **Abacus masters and merchant pupils**, thirteenth–sixteenth centuries: largely anonymous agents of practical diffusion.
- **Luca Pacioli**, c. 1447–1517: printed synthesis of commercial mathematics.
- **Gregor Reisch**, c. 1467–1525: printed the famous arithmetic allegory in 1503.
- **Francesco Pellos**, active 1492: early printed decimal point-like usage.
- **Christoff Rudolff**, 1499–1545: operated with decimal fractions and a separator.
- **Simon Stevin**, 1548–1620: systematic public campaign for decimal fractions.
- **Robert Recorde**, c. 1512–1558: English arithmetic pedagogy.
- **John Napier**, 1550–1617: logarithms, calculating rods, and decimal separator practice.
- **Christopher Clavius**, 1538–1612; **Giovanni Antonio Magini**, 1555–1617; **Jost Bürgi**, 1552–1632: rival early decimal-separator claims.

## Modern historians and decipherers

- **James Prinsep** (1799–1840), **Bhagwanlal Indraji** (1839–1888), **Georg Bühler** (1837–1898), and **Émile Senart** (1847–1928): Brahmi and Indian epigraphic work.
- **Augustus Hoernle** (1841–1918): first major editor of the Bakhshali manuscript.
- **David Eugene Smith** and **Louis Charles Karpinski**: *The Hindu-Arabic Numerals* (1911), foundational but now dated.
- **Karl Menninger** (1898–1963): comparative history emphasizing number words, hand signs, and written symbols.
- **Joseph Needham** (1900–1995): monumental history of Chinese science; influential, sometimes diffusionist.
- **Jean-Claude Martzloff**: specialist history of Chinese mathematics.
- **Takao Hayashi**, **Kim Plofker**, **Agathe Keller**, **Clemency Montelle**, and **Dominik Wujastyk**: modern South Asian mathematical-text scholarship and Bakhshali dating critique.
- **Jens Høyrup** and **Eleanor Robson**: contextual histories of Babylonian mathematics.
- **Georges Ifrah** (1947–2019): extraordinarily wide popular comparative synthesis, rich in illustrations but unreliable in some chronology and diffusion claims.
- **Stephen Chrisomalis**: comparative classification and standard modern survey of numerical notation.

---

# Words descended from the history

| Word | Route and evidentiary note |
|---|---|
| digit | Latin *digitus*, finger or toe; later a numeral sign, reflecting finger reckoning |
| calculus | Latin *calculus*, small stone/pebble used as a counter; later calculation and the mathematical calculus |
| abacus | Latin *abacus*, from Greek *abax/abakion*, a board or counting table; ultimate source is uncertain and may be Semitic |
| algorithm | Medieval Latin forms of al-Khwarizmi’s name—*Algoritmi/Algorismi*—first denoted arithmetic with Indian numerals; later generalized to a finite procedure |
| algorism | Older English/Latin-derived term specifically for written numerical reckoning |
| zero | Arabic *ṣifr*, “empty, zero,” represented in medieval Latin as *zephirum*; Italian forms contracted toward *zero* |
| cipher | Arabic *ṣifr* → medieval Latin *cifra* → Old French *cifre*; originally zero, then numeral/digit, then coded writing |
| chiffre | French descendant of the same *ṣifr* line; now “digit/number,” while *zéro* names zero |
| zephyr | The wind-word comes through Greek *Zephyros* and is etymologically unrelated to numerical *zephirum*, despite superficial resemblance |

The often-repeated statement that Arabic *ṣifr* is a “translation” of Sanskrit *śūnya* is semantically plausible—both express emptiness—but exact lexical causation is harder to demonstrate than conceptual transmission. Arabic *ṣifr* already belonged to an Arabic root meaning emptiness. It could be an indigenous word selected to translate the Indian concept, rather than a word descended from Sanskrit sounds.

---

# Culture

## 1. Law and administration

Written number forms matter legally because they differ in alterability:

- `100` can become `1000` by adding a zero;
- an open `0` may be modified;
- `1` may receive a leading or trailing digit;
- words are longer but harder to alter invisibly.

Consequently contracts, cheques, statutes, and prescriptions often require both figures and words. Anti-fraud Chinese financial numerals serve the same function. The Florentine rule belongs to this larger documentary ecology.

## 2. Coins and dates

Coins are conservative objects:

- Islamic coins used Arabic legends and several systems of dating, including words, abjad letter-numerals, and eventually digit forms.
- European coins retained Roman numerals in regnal names and dates long after Hindu-Arabic numerals became ordinary in accounts.
- Mixed inscriptions are common: a Roman numeral for a ruler, Arabic figures for the year, alphabetic abbreviations for denomination.

A coin’s date can be evidence for a digit shape only after authenticity, mint, calendar, and reading are established.

## 3. Calendars and clocks

Hindu-Arabic numerals dominate modern calendar grids because positional notation efficiently distinguishes day, month, and year. Roman numerals survive on clock dials and ceremonial calendars. Arabic-script digits appear in many Islamic calendars, while year numbering can follow Hijri, Gregorian, Persian, Hebrew, Buddhist, Japanese era, or other systems. A numeral system and a calendar era are independent.

## 4. Liturgy

Roman numerals remain common for:

- numbered popes;
- psalms and canticles;
- lectionary divisions;
- book and chapter numbering;
- inscriptions.

Hindu-Arabic digits dominate modern page references and dates. This coexistence lets typography signal sacred continuity versus practical lookup.

## 5. Gematria and isopsephy

Hebrew and Greek letter-numerals are ciphered-additive systems:

- Greek **isopsephy** assigns numerical values to alphabetic letters.
- Hebrew **gematria** does likewise.
- Words can therefore be read as sums.

These systems coexist with Hindu-Arabic notation but do not descend from it. Their cultural function differs: they bind number to language, allowing exegetical, mnemonic, cryptographic, and poetic associations.

## 6. Chronograms

A chronogram is a phrase in which selected numeral letters sum to a date:

- Roman-letter chronograms emphasize `I V X L C D M`;
- Hebrew and Arabic traditions can use alphabetic numerical values;
- typography may enlarge or capitalize the operative letters.

Chronograms deliberately resist the compact transparency of decimal positional notation: the date is encoded as literary wit.

## 7. Literature and art

Numbers function as:

- structural counts—books, cantos, chapters, stanzas;
- mystical quantities such as 3, 7, 12, 40, 108, 1001;
- emblems of modernity, bureaucracy, anonymity, and calculation;
- visual forms in concrete poetry, Futurism, Dada, conceptual art, and digital art.

The arrival of printed digits made numerical typography available as a graphic vocabulary separate from spelled number words.

## 8. Old-style figures

Old-style, text, or non-lining figures have varied heights:

- some sit at x-height;
- some ascend;
- `3`, `4`, `5`, `7`, or `9` may descend, depending on typeface.

Lining figures share a common baseline and cap-like height. Either style may be:

- **proportional**, with widths fitted to each digit;
- **tabular**, with equal advance widths for aligned columns.

Old-style figures harmonize with lowercase prose; tabular lining figures suit financial and scientific tables. Unicode normally does not encode them as different characters; OpenType features such as `onum`, `lnum`, `pnum`, and `tnum` choose glyphs. [Type Network’s figure-style explanation](https://typenetwork.com/articles/opentype-at-work-figure-styles).

---

# Controversies and disputes

## 1. Who invented zero?

There is no single satisfactory answer unless “zero” is defined.

| Meaning of zero | Earliest relevant evidence | Proper conclusion |
|---|---|---|
| Absence of objects | Prehistoric and universal | Not a datable invention |
| Empty place on a calculating surface | Attested or reconstructable in several cultures | May leave no written sign |
| Written placeholder in positional notation | Babylonian internal placeholder; Chinese blank; Indian dot; Maya shell | Independently developed more than once |
| Explicit zero digit usable at all places | Indian decimal notation, first millennium CE | Central Indian achievement, exact first unknown |
| Zero as arithmetic operand | Brahmagupta, 628, earliest surviving systematic rules | Secure textual milestone, not proof he originated every concept |
| Modern algebraic zero | Product of later Indian, Islamic, and European formalization | No single inventor |

Thus “India invented zero” is defensible when it means the integration of a zero sign with an unrestricted decimal positional system and arithmetic treatment, but misleading if it erases Babylonian placeholder use, independent Maya zero, Chinese empty-place computation, or the difference between a placeholder and a number.

## 2. Babylonian placeholder

- **[Artefact]** Late Babylonian scribes used a sign resembling two oblique wedges to disambiguate an internal empty sexagesimal place.
- It generally did not occur at the end of a numeral.
- There was no fixed absolute magnitude without context—`1` could mean 1, 60, \(1/60\), and so on.
- **Conclusion:** It is a zero-like placeholder but not the same notation or arithmetic object as modern `0`.

## 3. Maya priority

Maya inscriptions may provide earlier securely dated zero glyphs than India’s Gwalior inscription. That does not make Maya zero the ancestor of modern zero.

- If “first” means earliest surviving dated zero sign in any positional culture, Maya evidence is a contender.
- If it means source of the globally transmitted decimal zero, South Asia is the relevant origin.
- If it means earliest arithmetic rules, Brahmagupta is the critical surviving author.

These are different questions, frequently collapsed in popular argument.

## 4. Bakhshali dating

The 2017 radiocarbon results do not have to be rejected; their interpretation must be limited.

Evidence for an early date:

- one sampled bark folio returned a third–fourth-century range;
- the dot appears as an empty-place marker in the manuscript tradition.

Evidence against dating the whole mathematical text that early:

- other sampled folios returned much later ranges;
- bark may have been stored before writing;
- carbon dating dated substrate, not ink;
- the manuscript is composite;
- palaeography and textual analysis do not support treating one bark date as the date of the entire witness.

The appropriate wording is: “A Bakhshali folio’s bark produced an early radiocarbon range; the date of the writing and unified manuscript remains disputed.”

## 5. Gwalior “first zero”

Gwalior’s strength is secure inscriptional context and date. Its weakness as an absolute-first claim is survival bias: earlier zero-bearing texts may be lost, undated, copied later, or disputed. It is safest to call Gwalior the earliest generally accepted, securely dated Indian inscription with a circular positional zero—not the first human use of zero.

## 6. Chinese counting-rod priority

Arguments for Chinese influence on India cite:

- decimal place structure;
- nine nonzero rod-digit values;
- blanks for empty positions;
- Central Asian communication routes.

Arguments against a demonstrated borrowing cite:

- no surviving transmission document;
- major graphic differences;
- rod orientation alternation unlike Brahmi-derived digits;
- independent plausibility of decimal place value;
- uncertain chronology of written rod configurations.

Needham entertained substantial east-to-west influence. Martzloff and later specialists more often distinguish structural comparison from proven descent. Chrisomalis treats the link as possible but not established.

## 7. Were the numerals “Arabic” or “Indian”?

Both names encode part of the history:

- Indian scholars developed the decimal place-value complex from Brahmi-derived signs.
- Arabic and Persian scholars called the arithmetic Indian, preserved, expanded, and transmitted it.
- Europeans encountered the signs chiefly through Arabic-language mathematics and Mediterranean practice.
- The western shapes were transformed in Maghribi and European hands.

Therefore “Hindu-Arabic” is historically fuller than either “Hindu” or “Arabic” alone. “Hindu” here is an old geographical-cultural label for India, not a claim that the notation belongs only to the Hindu religion.

## 8. The angles-count-the-value story

The story redraws each digit so that:

- `1` has one angle,
- `2` has two,
- …
- `9` has nine,
- `0` has none.

**[Legend/modern invention]**

Evidence against it:

- no early Indian, Arabic, or Latin source explains the digits this way;
- historical digit forms vary radically;
- curves and angles depend upon script and redrawer;
- the scheme works only by selectively counting corners and inventing artificial glyphs;
- palaeographic series link the forms to Brahmi-derived handwriting.

The legend appears to be a modern pedagogical graphic, spread widely by posters and social media. The date and individual originator remain unestablished. Its popularity is evidence about modern desire for rational-looking symbol origins, not ancient design.

## 9. Ghubār-from-Arabic-letters theories

Modern authors have proposed that western digits derive from Arabic alphabet letters selected by abjad values. Their evidence is visual resemblance after rotating or stylizing glyphs.

**[Minority/disputed claim]**

Against it:

- Indian numeral forms predate the relevant Arabic examples;
- Arabic medieval authors themselves called the arithmetic Indian;
- al-Biruni explicitly described Indian numeral variation;
- resemblance generated by selective rotation is weak evidence;
- palaeographic descent must explain intermediate dated forms, not merely endpoints.

The mainstream reconstruction remains Brahmi-derived signs transformed through Indian and Islamic scribal traditions.

## 10. “Roman numerals have no zero”

True in a narrow sense:

- the ordinary monumental system `I V X L C D M` lacks a regular positional zero digit.

Misleading in broader senses:

- Latin had words such as *nihil* and *nulla*;
- Roman counting boards represented empty positions;
- medieval scribes sometimes used `N` for *nulla* in particular tables;
- later users could mix Roman and Hindu-Arabic practices.

A missing written digit does not imply inability to conceive or calculate a null quantity.

## 11. Florence “banned Arabic numerals”

The strongest defensible version is that a Florentine guild regulation required account entries in words rather than numerical figures. The broad version—“Florence outlawed Arabic numerals in 1299”—turns a documentary-security rule into a citywide cultural ban. The still broader “Europe rejected zero as satanic” lacks adequate documentary support.

## 12. Gerbert the magician

Gerbert’s mathematical interests are documented. The devil-pact, stolen magical book, and brazen head belong to later legend. His unusual learning, Iberian associations, and rise to the papacy helped produce the tales. They reveal cultural anxiety but cannot reconstruct his actual lessons.

## 13. Fibonacci “introduced Arabic numerals to Europe”

- **False if “first appearance” is intended:** the Codex Vigilanus dates to 976, and Gerbertian apices belong to about the same broad period.
- **Reasonable if “major influential exposition” is intended:** *Liber Abaci* offered a comprehensive commercial and mathematical treatment with zero.
- **Still incomplete:** numerous translators, teachers, merchants, notaries, and printers produced actual diffusion.

## 14. Ifrah: use with caution

Georges Ifrah’s *Histoire universelle des chiffres* is valuable for:

- comparative ambition;
- extensive illustrations;
- attention to bodily and material calculation;
- bringing non-European systems to a mass readership.

Criticisms include:

- speculative diffusion chains;
- insufficient source citation for some illustrations;
- chronological mistakes;
- reproducing obsolete readings;
- blurring inference and fact;
- treating attractive structural parallels as historical connections.

Joseph Dauben’s AMS review documents examples of incorrect dates and bibliographic claims. [Dauben review](https://www.ams.org/notices/200202/rev-dauben.pdf). Chrisomalis should supersede Ifrah for typology and genealogical claims, while Ifrah remains a useful guide to questions and images that must be independently checked.

## 15. “The best system inevitably won”

The Hindu-Arabic system is exceptionally efficient for written algorithms, but adoption was not automatic:

- users already possessed reliable counter-based methods;
- currencies and measures were non-decimal;
- manuscripts and schooling were expensive;
- unfamiliar figures increased fraud risk;
- institutions valued traditional notation;
- tables, instruments, and spoken arithmetic could compensate for awkward written forms.

Its eventual dominance followed printing, commercial education, state administration, decimalization, scientific tables, mechanization, and global imperial-economic networks—not abstract efficiency alone.

---

# Open questions

1. **When and where did the first complete Indian ten-sign positional repertoire arise?** Surviving inscriptions are sparse, manuscripts are copies, and early writing materials decayed.

2. **How should the Bakhshali layers be dated?** More non-destructive ink analysis, full codicological reconstruction, and integrated palaeographic study are needed.

3. **What exact relation links Brahmi signs to their more remote predecessors?** Later Brahmi-to-Indic descent is much firmer than claims about Semitic, Egyptian, or other ultimate origins.

4. **Was Chinese rod computation historically influential in India?** The structural case is suggestive; the documentary transmission chain is absent.

5. **How much of al-Khwarizmi’s original Hindu arithmetic survives in each Latin recension?** The Arabic source is lost, and Latin witnesses are adaptations as well as translations.

6. **What exactly did al-Kindi’s four-part work contain?** Bibliographical notices survive, the work does not.

7. **How did eastern and western Arabic digit families diversify?** More dated manuscript evidence is needed, particularly for early Maghribi forms.

8. **What is the exact archival text behind the Florentine 1299 claim?** A modern critical citation should give guild, statute recension, folio, original wording, and scope.

9. **Where and when did the angles legend originate?** It is demonstrably non-ancient, but its first poster, textbook, or designer remains unidentified.

10. **Which alleged Roman abacus is meant by “the Louvre abacus”?** A museum inventory number is necessary before the anecdote can be treated as an artefact claim.

11. **How widespread was practical digit use before surviving manuscripts display it?** Perishable dust boards, palm leaves, birch bark, wax tablets, and merchant scraps bias the record toward stone and prestige codices.

12. **What exactly constituted “replacement”?** Roman, alphabetic, rod, counter, verbal, and positional systems often coexisted, each occupying a different social or material niche.

---

# Sources

## Primary objects, manuscripts, catalogues, and texts

- British Museum. “Papyrus: Rhind Mathematical Papyrus,” EA10057.  
  https://www.britishmuseum.org/collection/object/Y_EA10057

- Ashmolean Museum / Hierakonpolis Expedition. “Object in Focus: The Narmer Mace-Head.”  
  https://www.hierakonpolis-online.org/files/hk_nn/nn-31-2019.pdf

- Narmer Catalog. “Narmer Macehead,” Ashmolean AN1896–1908 E.3915.  
  https://narmer.org/inscription/0080.pdf

- *Epigraphia Indica*, vol. 1. “The Two Inscriptions of the Vaillabhaṭṭasvāmin Temple at Gwalior.”  
  https://upload.wikimedia.org/wikipedia/commons/d/dc/Epigraphia_Indica_Vol_1_%281892%29.pdf

- Bodleian Library, MS. Sansk. d. 14, Bakhshali Manuscript; critical dating discussion accessed through Plofker et al.  
  https://journals.library.ualberta.ca/hssa/index.php/hssa/article/view/22

- TITUS. Brahmagupta, *Brāhmasphuṭasiddhānta*, electronic Sanskrit text.  
  https://titus.fkidg1.uni-frankfurt.de/texte/etcs/ind/aind/klskt/mathemat/brsphsd/brspht.htm

- Colebrooke, Henry Thomas. *Algebra, with Arithmetic and Mensuration, from the Sanscrit of Brahmegupta and Bhascara*. London, 1817.

- Codex Vigilanus/Albeldensis, El Escorial MS d.I.2, numeral folio image and transcription.  
  https://commons.wikimedia.org/wiki/File%3ACodex_Vigilanus_Primeros_Numeros_Arabigos.jpg

- Max Planck Institute for the History of Science, ISMI. “Algoritmi de numero Indorum,” record and facsimile.  
  https://ismi.mpiwg-berlin.mpg.de/text/336395

- Al-Khwarizmi. *Algoritmi de numero Indorum*, ed. Baldassarre Boncompagni, Rome, 1857.  
  https://books.google.com/books/about/Algoritmi_de_numero_Indorum.html?id=6DbCUdJ4fYoC

- Crossley, John N., and Alan S. Henry. “Thus spake al-Khwārizmī: A translation of Cambridge University Library Ms. Ii.vi.5.” *Historia Mathematica* 17.2 (1990): 103–131.  
  https://www.sciencedirect.com/science/article/pii/031508609090048I

- Fibonacci, Leonardo. *Liber Abbaci*, Latin chapter list.  
  https://la.wikisource.org/wiki/Liber_abbaci/Capitula

- Fibonacci, Leonardo. *Fibonacci’s Liber Abaci*, trans. Laurence E. Sigler. New York: Springer, 2002.

- Vatican Library, Pal. lat. 1420, Sacrobosco, *Algorismus*, fols. 37r–40v.  
  https://digi.ub.uni-heidelberg.de/diglit/bav_pal_lat_1420/0181/scroll

- IRHT-CNRS FAMA. “Johannes de Sacrobosco, Algorismus vulgaris.”  
  https://fama.irht.cnrs.fr/oeuvre/268660

- Library of Congress. Gregor Reisch, *Margarita philosophica*, 1503.  
  https://www.loc.gov/resource/rbctos.2017rosen0595/

- Library of Congress. “Typus arithmeticae,” 1503 woodcut catalogue.  
  https://www.loc.gov/pictures/item/92518152/

- SLUB Dresden. “The Dresden Maya Codex: Content,” Mscr. Dresd. R. 310.  
  https://www.slub-dresden.de/en/explore/manuscripts/the-dresden-maya-codex/content

## Standard modern surveys

- Chrisomalis, Stephen. *Numerical Notation: A Comparative History*. Cambridge: Cambridge University Press, 2010.  
  https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20%28CUP%2C%202010%29%28ISBN%200521878187%29%28O%29%28498s%29_MPop_.pdf

- Chrisomalis, Stephen. “Re-evaluating Merit: Multiple Overlapping Factors Explain the Evolution of Numerical Notations.” *Writing Systems Research* 9.1.  
  https://www.tandfonline.com/doi/abs/10.1080/17586801.2016.1227688

- Chrisomalis, Stephen. “The Cognitive and Cultural Foundations of Numbers.” In *Oxford Handbook of the History of Mathematics*.  
  https://academic.oup.com/book/53073/chapter-abstract/421974901

- Menninger, Karl. *Number Words and Number Symbols: A Cultural History of Numbers*. Trans. Paul Broneer. Cambridge, MA: MIT Press, 1969.

- Plofker, Kim. *Mathematics in India*. Princeton: Princeton University Press, 2009.

- Salomon, Richard. *Indian Epigraphy: A Guide to the Study of Inscriptions in Sanskrit, Prakrit, and the Other Indo-Aryan Languages*. Oxford University Press, 1998.  
  https://rapeutation.com/salomonindianepigraphy.pdf

- Smith, David Eugene, and Louis Charles Karpinski. *The Hindu-Arabic Numerals*. Boston: Ginn, 1911.  
  https://in.okfn.org/files/2013/07/The-Hindu-Arabic-Numerals.pdf

- Ifrah, Georges. *The Universal History of Numbers: From Prehistory to the Invention of the Computer*. Trans. David Bellos et al. London: Harvill; New York: Wiley, 1998–2000.

- Dauben, Joseph W. Review of Ifrah, *The Universal History of Numbers* and *The Universal History of Computing*. *Notices of the AMS* 49 (2002).  
  https://www.ams.org/notices/200202/rev-dauben.pdf

## Indian numerals and zero

- Plofker, Kim; Agathe Keller; Takao Hayashi; Clemency Montelle; Dominik Wujastyk. “The Bakhshālī Manuscript: A Response to the Bodleian Library’s Radiocarbon Dating.” *History of Science in South Asia* 5.1 (2017): 134–150.  
  https://journals.library.ualberta.ca/hssa/index.php/hssa/article/view/22

- MacTutor History of Mathematics. “Indian Numerals.”  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Indian_numerals/

- MacTutor History of Mathematics. “A History of Zero.”  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Zero/

- MacTutor History of Mathematics. “Arabic Numerals.”  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Arabic_numerals/

- MacTutor History of Mathematics. “Decimal Numeration and the Place-Value System.”  
  https://mathshistory.st-andrews.ac.uk/Projects/Pearce/chapter-8/

- MacTutor History of Mathematics. “Earliest Uses of Symbols for Constants.”  
  https://mathshistory.st-andrews.ac.uk/Miller/mathsym/constants/

## Babylonian and early accounting

- Høyrup, Jens. *Lengths, Widths, Surfaces: A Portrait of Old Babylonian Algebra and Its Kin*. New York: Springer, 2002.

- Høyrup, Jens. *In Measure, Number, and Weight: Studies in Mathematics and Culture*. Albany: SUNY Press, 1994.

- Robson, Eleanor. *Mathematics in Ancient Iraq: A Social History*. Princeton University Press, 2008.

- Schmandt-Besserat, Denise. *Before Writing*, 2 vols. Austin: University of Texas Press, 1992.

- Schmandt-Besserat, Denise. “The Token System of the Ancient Near East.”  
  https://www.cambridge.org/core/books/abs/archaeology-of-measurement/token-system-of-the-ancient-near-east-its-role-in-counting-writing-the-economy-and-cognition/0AB9E89E74F94FE95F53B145F59CCA59

- “Numeracy at the Dawn of Writing: Mesopotamia and Beyond.” *Historia Mathematica*.  
  https://doi.org/10.1016/j.hm.2020.08.002

- Schmandt-Besserat, Denise. “An Archaic Recording System in the Uruk-Jemdet Nasr Period.” *American Journal of Archaeology* 83.1.  
  https://www.journals.uchicago.edu/doi/10.2307/504234

## China and East Asia

- Needham, Joseph, with Wang Ling. *Science and Civilisation in China*, vol. 3: *Mathematics and the Sciences of the Heavens and the Earth*. Cambridge University Press, 1959.

- Martzloff, Jean-Claude. *A History of Chinese Mathematics*. Berlin: Springer, 1997.

- Chemla, Karine, and Guo Shuchun. *The Nine Chapters on the Mathematical Art: Companion and Commentary*. Springer, 2004.

- Chemla, Karine. “The Interplay between Textual Procedures and Material Operations from the Viewpoint of Chinese Mathematical Texts.”  
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7E654BC8863452F26F2E0C43892699F4/S0269889725100860a.pdf/div-class-title-the-interplay-between-textual-procedures-and-material-operations-from-the-viewpoint-of-chinese-mathematical-texts-div.pdf

## Numeral typography, decimals, and modern standards

- MacTutor History of Mathematics. “Earliest Uses of Symbols for Fractions.”  
  https://mathshistory.st-andrews.ac.uk/Miller/mathsym/fractions/

- Unicode Consortium. “Digit Terminology.”  
  https://www.unicode.org/terminology/digits.html

- Unicode Consortium. *The Unicode Standard*, Chapter 9, “Middle Eastern Scripts.”  
  https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-9/

- Unicode Consortium. *The Unicode Standard*, Chapter 22, “Numerals.”  
  https://unicode.org/versions/Unicode16.0.0/core-spec/chapter-22/

- Unicode CLDR. “Numbering Systems.”  
  https://cldr.unicode.org/translation/core-data/numbering-systems

- Unicode. *Locale Data Markup Language*, Part 3: Numbers.  
  https://unicode.org/reports/tr35/tr35-numbers.html

- Type Network. “OpenType at Work: Figure Styles.”  
  https://typenetwork.com/articles/opentype-at-work-figure-styles

- Monotype. “How to Use Figure Styles.”  
  https://www.monotype.com/resources/expertise/how-use-figure-styles-illustrator

## Roman calculation and continuing cultural use

- Bibliothèque cantonale et universitaire de Fribourg. *Des chiffres ou des lettres: compter, calculer, mesurer à l’époque romaine*.  
  https://fri-memoria.bcu-fribourg.ch/uploads/r/bcu-fribourg/b/e/7/be71634cb35b1bda72f1ba4a8e8b45d95b4765213c846c4ac31b13d5f19da631/Des_chiffres_ou_des_lettres__compter__calculer__mesurer____l___poque_romaine.pdf

- “NFL: It’s ‘Super Bowl 50,’ Not ‘Super Bowl L.’”  
  https://time.com/2822841/nfl-super-bowl-50-l/

## Additional research and source criticism

- MacTutor History of Mathematics. Smith and Karpinski resource page.  
  https://mathshistory.st-andrews.ac.uk/Extras/Karpinski_Smith/

- SIAM News. “Numerical Notation Systems as Cultural Artifacts.”  
  https://www.siam.org/publications/siam-news/articles/numerical-notation-systems-as-cultural-artifacts

- MIT Press Reader. “Re-counting the Cognitive History of Numerals.”  
  https://thereader.mitpress.mit.edu/recounting-cognitive-history-of-numerals/

- Unicode CLDR numbering-system source data.  
  https://github.com/unicode-org/cldr/blob/main/common/supplemental/numberingSystems.xml
