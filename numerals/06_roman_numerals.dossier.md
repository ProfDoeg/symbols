# Roman numerals: Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| Name | Roman numerals; Latin *notae numerorum*, *numeri*, later “Roman figures” |
| Base | Decimal, with a quinary sub-base: powers of ten are paired with “half-power” signs: 1/5, 10/50, 100/500 |
| Type | Originally cumulative-additive; later mixed additive–subtractive; multiplicative devices were added for large numbers. Non-positional in its ordinary form and not ciphered |
| Classical/modern signs | I = 1; V = 5; X = 10; L = 50; C = 100; D = 500; M = 1,000 |
| Older large-number signs | ↀ or CIↃ = 1,000; ↁ or IↃↃ = 5,000; ↂ or CCIↃↃ = 10,000; ↇ = 50,000; ↈ = 100,000 |
| Fractional signs | A dot or pellet for an *uncia* (1/12); S for *semis* (1/2); combinations of S and pellets for other twelfths; additional metrological signs existed |
| Period | Etruscan antecedents securely by the late sixth century BCE; Roman forms by the fifth century BCE and common from the third century BCE; continuous specialized use to the present |
| Region | Origin in central Italy; spread throughout the Roman Mediterranean and western provinces; dominant in Latin-literate medieval western Europe; now internationally recognizable |
| Writing direction | Roman normally left-to-right; the Etruscan ancestor was usually right-to-left |
| Zero | No place-holding zero is needed in ordinary non-positional notation. Classical Roman notation has no regular numeral-sign for zero; late antique and medieval computists used words such as *nulla* and sometimes N |
| Evidentiary classification | The structural and chronological summary follows Stephen Chrisomalis’s comparative synthesis and Paul Keyser’s study of the epigraphic and numismatic evidence. The exact prehistoric derivation of individual signs remains reconstructed rather than directly documented. [Chrisomalis, *Numerical Notation*, ch. 4](https://doi.org/10.1017/CBO9780511676062.004); [Keyser 1988](https://doi.org/10.2307/505248) |

### Evidence labels used below

- **[Artefact]**: a surviving object or inscription.
- **[Documented text]**: a surviving literary, legal, administrative, or instructional text.
- **[Scholarly reconstruction]**: an inference from comparative, chronological, palaeographic, linguistic, or archaeological evidence.
- **[Tradition]**: a long-established practice whose initial author or occasion is not securely known.
- **[Disputed]**: specialists have offered materially different readings.
- **[Legend]**: a story transmitted as explanation or anecdote but unsupported by contemporary evidence.
- **[Modern invention]**: a recent convention projected backward or newly formalized.

---

## The system in detail

### 1. The signs

#### The familiar alphabetized system

| Value | Ordinary form | Dedicated Unicode form | Description in words | Latin number-word |
|---:|---|---|---|---|
| 1 | I | Ⅰ U+2160 | one vertical stroke | *unus* |
| 5 | V | Ⅴ U+2164 | two oblique strokes meeting below | *quinque* |
| 10 | X | Ⅹ U+2169 | two crossed oblique strokes | *decem* |
| 50 | L | Ⅼ U+216C | upright with a short horizontal foot | *quinquaginta* |
| 100 | C | Ⅽ U+216D | open semicircular letter-form | *centum* |
| 500 | D | Ⅾ U+216E | vertical stem and right-hand bowl | *quingenti* |
| 1,000 | M | Ⅿ U+216F | alphabetic M | *mille*; plural *milia* |

**[Documented standard]** Unicode encodes Ⅰ–Ⅻ, Ⅼ, Ⅽ, Ⅾ, Ⅿ and lowercase counterparts as compatibility characters. In ordinary digital text, sequences of Latin letters—`VIII`, not necessarily the single character `Ⅷ`—are normally preferable. Unicode also encodes archaic signs ↀ–ↈ. [Unicode Number Forms chart](https://www.unicode.org/charts/PDF/U2150.pdf); [Unicode names list](https://www.unicode.org/charts/nameslist/n_2150.html)

**[Historical qualification]** These seven letters are not the unchanged original Roman inventory. I and X are stable; V developed from an earlier orientation resembling an inverted V; L passed through several “arrow” and inverted-T forms; C supplanted an older crossed or divided form; D developed from the right half of the thousand-sign; and M became the ordinary 1,000-sign mainly in the Middle Ages. In classical inscriptions M could instead abbreviate the word *mille* or *milia*. [Chrisomalis, pp. 109–15](https://doi.org/10.1017/CBO9780511676062.004)

#### Apostrophus notation

The apostrophus family enclosed I between ordinary and reversed C-like curves:

| Form | Unicode | Value | Verbal construction |
|---|---:|---:|---|
| CIↃ or ↀ | U+2180 | 1,000 | I enclosed by C and reversed C |
| IↃ | — | 500 | right half of CIↃ |
| CCIↃↃ or ↂ | U+2182 | 10,000 | one additional C and reversed C |
| IↃↃ or ↁ | U+2181 | 5,000 | half of CCIↃↃ |
| CCCIↃↃↃ | — | 100,000 | another enclosing pair |
| IↃↃↃ | — | 50,000 | its right half |

**[Artefact/text]** Large apostrophic signs are attested in Republican and Imperial epigraphy. The successive enclosing arcs raise the value by a factor of ten; taking the right half produces the five-value.

**[Scholarly reconstruction]** D is best understood palaeographically as the alphabetized right half of the older 1,000-sign, not as an original acrophonic abbreviation for *quingenti*. M likewise grew out of older 1,000-forms under pressure from the word *mille*. The resemblance of the completed forms to letters subsequently made them easier to normalize as letters.

#### Vinculum and framing

A horizontal bar above a numeral—the *vinculum*, *virgula*, or medieval *titulus*—could multiply what lay beneath it by 1,000:

- V̅ = 5,000
- X̅ = 10,000
- C̅ = 100,000
- M̅ = 1,000,000
- M̅CM̅ = 1,900,000 under one modern interpretation, though ancient grouping must be read from the actual bar’s extent.

**[Artefact]** Chrisomalis identifies the *Lex de Gallia Cisalpina*, 49–42 BCE, as the earliest known use of the thousand-bar. The bar continued into medieval usage. [Chrisomalis, pp. 112–14](https://doi.org/10.1017/CBO9780511676062.004)

Three strokes enclosing a numeral across its top and sides could multiply it by 100,000. **[Artefact]** This is attested from the late first century BCE and more often in the second century CE, but disappeared with the Empire.

**[Modern convention]** Online converters frequently present the overline as an unlimited, perfectly standardized recursive rule. Ancient practice was neither perfectly uniform nor infinitely recursive. Fonts also make combining overlines unreliable.

### 2. Structural principles

#### Additive notation

The older and statistically dominant ancient principle was cumulative addition:

- VIII = 5 + 1 + 1 + 1 = 8
- XII = 10 + 1 + 1 = 12
- XXVIII = 10 + 10 + 5 + 1 + 1 + 1 = 28
- MDCCCCXV = 1,000 + 500 + 400 + 15 = 1915

Signs normally descend from greater to lesser value. A power-of-ten sign could commonly repeat up to four times; a half-power sign normally appeared once.

**[Artefact]** At Vindolanda, about 85–130 CE, surviving ink tablets use `IIII` consistently rather than `IV`; `VIIII` is usual, though `IX` occurs. One text contains both `XLVI` and `XXXXV`, showing that writers could mix conventions. [Roman Inscriptions of Britain, Vindolanda introduction](https://romaninscriptionsofbritain.org/tabvindol/vol-II/introduction)

#### Subtractive notation

A lower power of ten before a higher sign can be subtracted:

- IV = 5 − 1 = 4
- IX = 10 − 1 = 9
- XL = 50 − 10 = 40
- XC = 100 − 10 = 90
- CD = 500 − 100 = 400
- CM = 1,000 − 100 = 900

The modern school standard normally permits only those six pairs, discourages more than three repeated I/X/C/M signs, and rejects forms such as IL = 49, IC = 99, XD = 490, and IM = 999.

**[Historical qualification]** That standard is a useful modern normalization, not a law enforced by Romans. Ancient forms include XIIX = 18, XXIIX = 28, IIX = 8, XXC = 80 and end-subtraction such as XXCIII for 83. Subtraction began occasionally in the late Republic; additive forms remained more common in formal inscriptions. [Chrisomalis, pp. 111–12](https://doi.org/10.1017/CBO9780511676062.004); [Sandys, *Latin Epigraphy*](https://archive.org/details/introductiontost00sand)

**[Scholarly reconstruction]** Subtractive spellings may partly mirror Latin speech—*duodeviginti*, “two from twenty,” and *undeviginti*, “one from twenty”—and partly save space, especially at line endings. Neither explanation accounts for every use.

#### Multiplication

Roman numeration became mixed rather than purely additive when bars and frames multiplied enclosed values. Medieval scribes also wrote constructions such as:

- `Mijc lviii` = 1,258, with *ij c* meaning two hundreds;
- `IIIIxx et huit` = 88, literally “four twenties and eight,” reflecting French vigesimal wording;
- `viM viiC xiii` = 6,713.

These are **[Documented medieval variants]**, not canonical modern Roman numerals. They combine Latin abbreviations, Roman signs, superscripts and vernacular number grammar.

#### Position

Ordinary Roman notation is non-positional: X means ten in X, XII and CX. Its value does not become 100 merely because it moves one column left.

**[Documented exception]** Around 1130, H. Ocreatus’s *Helcep Sarracenicum* used Roman phrases I–IX as positional digits and O or another *cifra* sign for an empty place, separating positions with dots: `I.O.VIII.IX` = 1089. It survives in a thirteenth-century witness, Cashel, Bolton Library, Medieval MS 1. It was a Roman–Arabic hybrid and did not become general practice. [Chrisomalis, pp. 120–21](https://doi.org/10.1017/CBO9780511676062.004)

### 3. Worked table, 1–20

Modern normalized forms are given first; common additive ancient/medieval alternatives follow.

| Number | Normalized Roman | Historically common alternative |
|---:|---|---|
| 1 | I | I |
| 2 | II | II |
| 3 | III | III |
| 4 | IV | IIII |
| 5 | V | V |
| 6 | VI | VI; late ligature ↅ |
| 7 | VII | VII |
| 8 | VIII | VIII; occasionally IIX |
| 9 | IX | VIIII |
| 10 | X | X |
| 11 | XI | XI |
| 12 | XII | XII |
| 13 | XIII | XIII; IIIX is attested with a different subtractive grouping |
| 14 | XIV | XIIII |
| 15 | XV | XV |
| 16 | XVI | XVI |
| 17 | XVII | XVII |
| 18 | XVIII | XVIII; XIIX |
| 19 | XIX | XVIIII; IXX |
| 20 | XX | XX |

### 4. Tens, hundreds and thousands

| Number | Normalized form | Additive or archaic alternative |
|---:|---|---|
| 10 | X | X |
| 20 | XX | XX |
| 30 | XXX | XXX |
| 40 | XL | XXXX |
| 50 | L | early arrow/inverted-T forms; Unicode ↆ represents an early 50 |
| 60 | LX | LXXXX? No: ordinary additive form is LX; in some North African inscriptions XXXXXX |
| 70 | LXX | LXX |
| 80 | LXXX | LXXX; XXC attested |
| 90 | XC | LXXXX |
| 100 | C | earlier crossed forms |
| 200 | CC | CC |
| 300 | CCC | CCC |
| 400 | CD | CCCC |
| 500 | D | IↃ; older half-thousand signs |
| 600 | DC | DC |
| 700 | DCC | DCC |
| 800 | DCCC | DCCC |
| 900 | CM | DCCCC |
| 1,000 | M | CIↃ; ↀ |
| 5,000 | V̅ | IↃↃ; ↁ |
| 10,000 | X̅ | CCIↃↃ; ↂ |
| 50,000 | L̅ | IↃↃↃ; ↇ |
| 100,000 | C̅ | CCCIↃↃↃ; ↈ |
| 1,000,000 | M̅ | *decies centena milia*, “ten times one hundred thousand” |

### 5. Famous and diagnostic numerals

| Number | Roman form | Why notable |
|---:|---|---|
| 49 | XLIX | Demonstrates two separately applied subtractive pairs; `IL` is a modern nonstandard shortcut |
| 944 | CMXLIV | Three subtractive groups |
| 1,666 | MDCLXVI | Every familiar sign appears once in descending order |
| 1,776 | MDCCLXXVI | Conventional date of the American Declaration of Independence |
| 1,984 | MCMLXXXIV | Title year of Orwell’s *Nineteen Eighty-Four* |
| 1,999 | MCMXCIX | Three subtractive groups following M |
| 2,024 | MMXXIV | Modern date |
| 3,888 | MMMDCCCLXXXVIII | Longest conventional numeral from 1 to 3,999: fifteen letters |
| 3,999 | MMMCMXCIX | Often called the largest “standard” modern numeral only because many teaching rules stop at 3,999 |
| 4,000 | IV̅ or MMMM | Requires an overline under one convention, but additive MMMM is historically possible |
| 100,000 | C̅ or ↈ | Attested large-number category |
| 100,000,000 | framed M | Apparently attested at Ostia in an inscription dated 36 CE |

### 6. Zero and absence

**[Documented structural fact]** A non-positional cumulative numeral does not require a placeholder. `XI` is eleven; there is no vacant tens or units column to mark.

**[Classical absence]** No regular classical Roman sign belonged to the I–V–X system with the value zero. This does not mean Romans were unable to say “none,” record an empty account category, or understand the result of exhaustion.

**[Documented text]** Dionysius Exiguus’s Easter table of 525 uses *nulla*, “none,” alongside Roman numerals where a computed epact is zero. Around 725 a table attributed to Bede or his circle uses N, probably from *nulla* or *nihil*. These are genuine written representations of zero in a Roman-numeral environment, but not a classical place-value digit.

**[Disputed formulation]** Thus both slogans—“Roman numerals have no zero” and “N is the Roman numeral for zero”—mislead. The precise finding is: classical Roman notation had no standard zero sign; medieval Latin computists sometimes represented a zero result lexically or by abbreviation.

### 7. Fractions

Roman fractional notation was predominantly duodecimal because the *as*—a unit of weight and coinage—was divided into twelve *unciae*.

| Fraction | Sign | Latin name | Literal or practical sense |
|---:|---|---|---|
| 1/12 | · | *uncia* | one twelfth; source of “ounce,” and indirectly “inch” |
| 2/12 = 1/6 | ·· or : | *sextans* | sixth |
| 3/12 = 1/4 | ··· or triangular dots | *quadrans* | quarter |
| 4/12 = 1/3 | ···· or :: | *triens* | third |
| 5/12 | five dots | *quincunx* | five unciae; source of “quincunx” |
| 6/12 = 1/2 | S | *semis* | half |
| 7/12 | S· | *septunx* | seven unciae |
| 8/12 = 2/3 | S·· | *bes* | two-thirds |
| 9/12 = 3/4 | S··· | *dodrans* | one quarter short |
| 10/12 = 5/6 | S···· | *dextans* or *decunx* | one sixth short/ten unciae |
| 11/12 | S····· | *deunx* | one uncia short |
| 1/24 | special mark or half-*uncia* form | *semuncia* | half an uncia |
| 1/48 | special mark | *sicilicus* | quarter uncia |
| 1/72 | special mark | *sextula* | sixth uncia |
| 1/288 | special mark | *scrupulum* | scruple |

**[Artefact]** Republican bronze coins carry pellets marking uncia-values; an *uncia* could bear one pellet and a *semis* an S. A Roman metrological alphabet has also been identified on Ibero-Roman pottery from Tossal de Manises/Lucentum. [Unicode proposal documenting coin evidence](https://www.unicode.org/L2/L2006/06173-roman-coinage.pdf); [University of Alicante record](https://doi.org/10.14201/zephyrus202494123142)

**[Correction to a secondary source]** MacTutor says Romans “did not use numerals to indicate fractions, but instead used words.” The word-system is real, but coins, inscriptions and surviving abaci also show fractional signs. Its table is useful for the names, not a complete description of notation. [MacTutor fraction history](https://mathshistory.st-andrews.ac.uk/Miller/mathsym/fractions/)

### 8. Largest expressible numbers

There is no inherent largest number if signs may repeat or multiplier marks may be iterated. Three different questions must be separated:

1. **Largest number under the modern seven-letter convention:** teaching manuals often stop at 3,999, `MMMCMXCIX`. This is a **[Modern convention]**, not an ancient limit.
2. **Largest ordinary ancient sign:** 100,000 had a special sign; Pliny says, *Non erat apud antiquos numerus ultra centum milia*—“among the ancients there was no numeral beyond one hundred thousand” (*Natural History* 33.47.133). Pliny was describing an older stage, not denying later multiplicative expressions.
3. **Largest surviving ancient use:** Gordon reported 35,863,120 as the largest known hybrid expression; Menninger cited an Ostian inscription of 36 CE apparently expressing 100,000,000. The reading and the corpus may change with discoveries. [Chrisomalis, pp. 112–14](https://doi.org/10.1017/CBO9780511676062.004)

Latin could name indefinitely larger quantities by multiplication and plural *milia*: *centum milia* = 100,000; *decies centena milia* = 1,000,000. The modern noun *million* is medieval Italian, not a classical Roman numeral-word.

### 9. Ligatures, marks and abbreviations

- **[Artefact]** A cursive ligature of VI became a special late-antique six-sign, now Unicode ↅ. It occurs in inscriptions and on sixth-century Byzantine coins and probably disappeared by the eighth century.
- **[Documented scribal practice]** Medieval `iiij` used a final j to prevent fraudulent extension: another i could not easily be appended.
- **[Documented scribal practice]** A stroke through the final numeral could mean subtract one-half.
- **[Artefact]** Bars, dots, or hooked bars distinguished numerals from identical letters. Vindolanda cohort numbers are often overlined for this reason; that bar does not multiply them.
- **[Documented medieval practice]** Ordinal endings appeared as superscripts: `IVto`, *quarto*, and `Mmo`, *millesimo*.
- **[Documented medieval variants]** Visigothic manuscripts developed special ligatures for 40 and other values.
- **[Modern typography]** Lowercase Roman numerals—i, ii, iii, iv—are now used for preliminary pages and outline levels. They descend from actual medieval minuscule practice, not merely modern case conversion.
- **[Modern typography]** Dedicated Unicode glyphs are compatibility forms. Roman numerals are normally set from alphabetic capitals, often with old-style or inscriptional proportions. “Old-style figures” properly means Hindu-Arabic digits with ascenders and descenders—such as 3, 4, 5, 7, 9 in a text face—not Roman numerals.

---

## Origins: dated and placed

### 1. What is—and is not—ancestral

The Ishango and Lebombo bones, Uruk tokens, Narmer macehead, Babylonian tablets, Brahmi numerals, Bakhshali manuscript, Gwalior zero and Dresden Codex are important to global numeral history, but none is evidence for the descent of Roman numerals.

- **[Artefact, unrelated genealogy]** Lebombo and Ishango are notched bones, their numerical interpretation and calendrical significance disputed.
- **[Scholarly reconstruction, unrelated genealogy]** Denise Schmandt-Besserat interpreted Near Eastern clay tokens as precursors to proto-cuneiform accounting. This is a separate Mesopotamian lineage.
- **[Artefact, unrelated genealogy]** The Narmer macehead carries very large Egyptian numerical quantities.
- **[Artefact, unrelated genealogy]** Brahmi numerals at Nāṇā Ghāṭ and Nasik belong to the Indian lineage that eventually produced positional Hindu-Arabic numerals.
- **[Disputed dating, unrelated genealogy]** Oxford’s radiocarbon tests placed different leaves of the Bakhshali manuscript between the third–fourth, eighth–ninth and tenth centuries CE; palaeographers dispute whether the sampled leaves establish the date of the mathematical text as a whole.
- **[Artefact, unrelated genealogy]** The Gwalior inscription dated 876 CE contains circular zeroes in a positional decimal context.
- **[Artefact, independent lineage]** The Dresden Codex uses Maya vigesimal notation and zero signs. Maya zero arose independently.
  
Their inclusion as alleged Roman ancestors would be a **[Modern conflation]**. Roman numerals belong to an Italic/Etruscan network.

### 2. Mediterranean setting, circa 700–500 BCE

**[Artefact]** Etruscan writing is attested from about 700 BCE. The alphabet was adapted from archaic Euboean Greek and normally written right-to-left.

**[Artefact]** Numeral signs recognizable as an Etruscan cumulative decimal/quinary system occur from the late sixth century BCE. The earliest material includes inscriptions on pottery and other marked objects; preservation is sparse because hypothetical tally-sticks would have been wood.

**[Scholarly reconstruction]** Chrisomalis judges that the Etruscan system may have arisen relatively independently while participating in a Mediterranean environment full of decimal additive systems: Egyptian, Phoenician, Aramaic, Cypriot, Anatolian and residual Aegean traditions. Etruscan and early Greek acrophonic systems are structurally so close that a shared late-sixth-century ancestral milieu is possible, but chronological priority cannot presently be assigned. [Chrisomalis, pp. 94–97](https://doi.org/10.1017/CBO9780511676062.004)

### 3. The Tuscania dice

**[Artefact]** A pair of ivory dice found in clandestine excavations near Tuscania/Toscanella in 1848 carries the Etruscan words:

- *θu*
- *zal*
- *ci*
- *śa*
- *maχ*
- *huθ*

The dice are catalogued as TLE 197 and are held in Paris at the Bibliothèque nationale de France, Cabinet des Médailles.

**[History of reading]** Nineteenth- and twentieth-century scholars agreed that these were the six number-words but disagreed especially over four and six. Massimo Pallottino and Giuliano and Larissa Bonfante transmitted influential assignments.

**[Reassessment]** In 2011 Gilberto Artioli and collaborators compared the written dice with 91 southern Etrurian pip-dice dated from the eighth to third centuries BCE. Their combinatorial analysis assigned *huθ* = 6 and *śa* = 4. This is stronger than guessing from one modern “opposite sides sum to seven” convention, because ancient dice used several opposition patterns. [Artioli et al., “Gambling with Etruscan Dice”](https://doi.org/10.1111/j.1475-4754.2011.00596.x); [Treccani, “Dadi”](https://www.treccani.it/enciclopedia/dadi_%28Enciclopedia-Italiana%29/)

The dice document Etruscan number-words, not by themselves the graphic ancestors of I, V and X.

### 4. From tally structures to Etruscan signs

Paul Keyser’s 1988 reconstruction is now the most influential account:

1. I began as one tally stroke.
2. A fifth stroke was differentiated to make groups legible.
3. X represented a crossed tenth mark.
4. The five-sign was graphically one half of the ten-sign.
5. The fifty-sign was similarly half of the hundred-sign.
6. Higher signs were made by additional crossing, circling or enclosing.

**[Scholarly reconstruction]** The strong evidence is the systematic form/value relation and the continuity between Etruscan and early Roman signs. The weak point is direct archaeology: no Etruscan wooden tally survives showing the proposed transformation. Chrisomalis therefore calls tally practice probable but not directly attested.

### 5. Earliest Roman attestations

**[Artefact]** Roman numeral signs appear “well into the fifth century BCE” and become frequent only in the third century BCE. They occur on coins, pottery and stone.

**[Artefact]** Large signs up to 100,000 are attested by the third century BCE. A securely dated C = 100 occurs in 186 BCE; Keyser reconstructs its emergence around 250–200 BCE from an older Etruscan hundred-sign.

**[Artefact with complex transmission]** The *Columna rostrata* commemorated consul Gaius Duilius’s naval victory in 260 BCE. Its surviving inscription was recut, probably under Augustus, but retained an older expression containing at least 22 and perhaps 32 signs for 100,000 to describe booty exceeding two million asses. It is therefore evidence for an old numeral structure, but not an untouched third-century carving.

**Absence of evidence:** no single excavated object can presently be named “the invention tablet” of Roman numerals. The system emerges across fragmentary Italic coin and inscription corpora.

---

## Competing theories of the signs’ shapes

### Tally-mark/Etruscan theory

**Status: [Scholarly reconstruction; strongest current synthesis].**

Keyser rejected the formerly standard mixed theory in favor of direct diffusion of Etruscan tally-derived signs into Latin. Supporting evidence:

- Etruscan forms are earlier.
- The Roman and Etruscan inventories have the same decimal/quinary structure.
- Several early signs are nearly identical.
- The writing direction changes with the host script: Etruscan right-to-left, Latin left-to-right.
- Five- and fifty-signs behave graphically as halves of ten- and hundred-signs.
- Alphabetic-looking C, D and M appear relatively late.

### Mommsen’s theory

**Status: [Historic scholarly theory; now generally rejected].**

Theodor Mommsen’s 1850 account treated I, V and X pictographically but derived the older 50, 100 and 1,000 signs from unused Chalcidian Greek aspirate letters—often described as chi, theta and phi.

Objections developed by Keyser and Chrisomalis:

- the proposed hundred-sign does not match the relevant theta closely;
- the supposedly “unused” letters were not wholly unavailable;
- the sequence does not naturally explain the early 500-sign;
- the Etruscan chronological and structural parallels provide a more economical account.

### Acrophonic letter theory

**Status: [Ancient/early scholarly explanation; rejected as an origin story].**

C looks like the first letter of *centum* and M of *mille*, so generations of writers inferred that the signs were abbreviations. But C replaces an older nonalphabetic form; D derives from half an apostrophic thousand; M becomes regular late. Alphabetic association influenced their final shapes but does not explain the origin of the system.

The late Roman grammarian Priscian offered an elaborate alphabetic explanation. It is valuable as a **[Documented late-antique belief]**, not eyewitness evidence for events a millennium earlier.

### Fingers and hands

**Status: [Early-modern pictographic theory/legend].**

In this story I is one finger, V is an open hand or the angle between thumb and forefinger, and X is two hands or two V’s. It was spread by early-modern antiquarians and repeated in popular books.

The ease of drawing I and the half-X relation make parts intuitively plausible, but there is no ancient explanatory text or developmental artifact demonstrating “V = hand.” Keyser’s tally sequence accounts for more signs with fewer assumptions.

### “Angles count the value”

**Status: [Modern invention].**

Internet diagrams redraw modern 1, 2, 3 and other Hindu-Arabic digits as angular polygons whose numbers of corners allegedly equal their values. This has no relevance to Roman numerals and no ancient manuscript lineage. It fails against the documented historical forms of the Hindu-Arabic digits.

---

## Arithmetic and instruments

## 1. Notation was usually output, not workspace

**[Scholarly consensus]** Roman numerals recorded quantities and results efficiently enough for administration but were poorly suited to column algorithms. The principal evidence indicates that calculation occurred with fingers, counters, boards and abaci; the result could then be written in Roman numerals.

This distinction prevents a common mistake: an empire need not multiply `CCXLVII × XVIII` by manipulating those written strings. It can set the quantities on a board, calculate physically, and record `MMMMCDXLVI`.

### Worked counter addition

For `CCVIII + DCXVII`:

1. Put down two hundred-counters, no tens, one five-counter and three units.
2. Add six hundreds, one ten, one five and two units.
3. Five unit counters exchange for one five-counter.
4. Two five-counters exchange for one ten-counter.
5. Ten hundred-counters would exchange for a thousand if necessary.
6. The remaining counters read DCCCXXV = 825.

The operation uses place-value columns without requiring a written positional numeral. The Roman signs correspond naturally to “one-counter” and “five-counter” levels.

### Worked counter multiplication

To calculate XXIII × XII:

- Double XXIII to obtain XLVI.
- Multiply by ten on the board by shifting the counter pattern one decimal column: CCXXX.
- Add the doubled amount: CCXXX + XLVI = CCLXXVI.

This reconstructed procedure is consistent with board calculation, but no surviving Roman worksheet records precisely these steps.

## 2. Fingers

**[Documented text and art]** Finger reckoning was widespread in Greco-Roman and medieval society. Different bends and placements represented units, tens and higher orders. Bede’s eighth-century *De temporum ratione* opens with a detailed system capable of representing thousands with both hands and larger values by bodily placement.

Finger numbers were useful for bargaining, dates and mental calculation and could communicate across languages. They were not Roman numerals written in the air; they were a parallel embodied notation.

The English word **digit** descends from Latin *digitus*, “finger/toe,” reflecting the body’s role in counting.

## 3. Calculi, boards and abaci

Latin *calculus* is a small pebble, especially a reckoning counter; *calculare* is to reckon with such stones.

**[Artefact]** The Museo Nazionale Romano owns an Imperial bronze portable abacus, inventory 65054, 11.5 × 7.2 cm. Its slots represent decimal orders and five-unit subdivisions; fractional slots support twelfths. [Museo Galileo catalogue](https://exhibits.museogalileo.it/archimedes/object/PortableCounterAbacus.html)

**[Artefact with provenance caution]** The Bibliothèque nationale de France holds a bronze button-abacus, inventory bronze.1925, formerly in the abbey of Sainte-Geneviève and Nicolas-Claude Fabri de Peiresc’s collection; it entered the national collection in 1797. The BnF notes that the six known abaci of this type all surfaced only from the seventeenth century onward. That late provenance does not prove forgery, but it makes secure archaeological context unavailable. [BnF catalogue, bronze.1925](https://medaillesetantiques.bnf.fr/ws/catalogue/app/collection/record/ark:/12148/c33gb18n6s)

**[Artefact/provenance caution]** The British Museum example is OA.2419. It is another of this very small family, not independent proof of a securely excavated “Roman abacus from the Louvre.”

**[Correction of requested anecdote]** The famous object sometimes called “the Roman abacus in the Louvre” is more accurately associated in accessible catalogues with the former Sainte-Geneviève collection and today’s BnF, while secure Roman collections include the Museo Nazionale Romano object. The Louvre’s online catalogue does not presently provide a matching portable abacus record. Conflating the Louvre, BnF and Parisian historical collections is a modern catalogue error.

## 4. What the Roman abacus shows

A portable abacus generally had:

- long lower slots with four movable beads for 1–4 of a denomination;
- short upper slots with one bead worth five of that denomination;
- successively valued decimal columns;
- special fractional slots for portions of an *uncia*.

It is structurally base ten with a five-sub-base, just like the written numeral system. This is why no column needs more than four “one” beads.

**[Disputed causal direction]** Taisbak argued that Roman numeral forms arose from abacus reckoning. Chrisomalis reverses the likely direction: Etruscan numeral/tally structure is earlier, so the abacus probably conformed to the notation. The instruments and numerals certainly complemented each other; priority is reconstructed.

## 5. Literary arithmetic

Roman authors preserve sophisticated fractional reasoning in surveying, law, architecture, commerce and inheritance.

**[Documented text]** Roman law divided estates into shares of an *as*: heirs could receive a *semis*, *quadrans*, *sextans* and so forth.

**[Documented text]** Vitruvius discusses proportions and measures; Frontinus and the *Corpus Agrimensorum* attest practical geometry; Pliny preserves large-number terminology.

**[Controversy]** Maher and Makowski showed that Latin texts require genuine multistep calculation with fractions. They argued that written Roman notation may have been used operationally. Chrisomalis accepts the arithmetic competence but judges direct written-symbol manipulation unproved. The absence of scratch-work matters: possible modern algorithms for Roman strings are not evidence Romans used them.

## 6. The Lamasba table

**[Artefact]** An irrigation regulation from Lamasba in Roman North Africa, in the reign of Elagabalus, 218–222 CE, includes a multiplication table for allocating water. It is evidence that tables could compensate for cumbersome repeated calculation.

## 7. Medieval counter-casting

The Roman board tradition continued in medieval Europe. Lines represented monetary or decimal denominations; counters placed on lines or spaces carried different values.

**[Documented text]** Richard FitzNigel’s *Dialogus de Scaccario*, composed about 1179, describes the English Exchequer table as roughly ten feet by five, edged to prevent counters falling, covered with a checkered cloth, and operated by officials under prescribed rules. [*Dialogue concerning the Exchequer*](https://www.medievalhistory.net/excheq1.htm)

The words *Exchequer* and *chequer* refer to the checkered board. Tallies and written Roman numerals preserved the result after the counters were removed.

**[Documented text]** Robert Recorde’s *The Ground of Artes* (1543) taught both written arithmetic and “counter casting.” It became one of the most reprinted English arithmetic books, with roughly forty-five editions before 1700. The longevity of the counter sections shows that written Hindu-Arabic methods did not instantly eliminate board reckoning.

**[Documented administrative evidence]** Exchequer records and surviving descriptions show counter patterns being copied into accounts alongside Roman or Arabic totals. [Jenkinson, “Arithmetic of the Exchequer”](https://repository.londonmet.ac.uk/7523/1/328938.pdf)

## 8. Algorists and abacists

These labels oversimplify a gradual technical and social change.

- **Abacists** calculated with boards/counters, often recording Roman numerals.
- **Algorists** calculated in writing with Hindu-Arabic positional digits.
- Many practitioners used both.
- Italian *abbaco* schools often taught Hindu-Arabic commercial arithmetic despite their name.

**[Documented text]** John Palsgrave’s 1530 dictionary supplied the sentence: “I shall reken it syxe tymes by aulgorisme or you can caste it ones by counters.” It is evidence that both techniques were culturally recognizable, although it is a sample sentence, not a measured speed test.

### Relevant textbooks and their relationship to Roman numerals

The following works do not descend from Roman notation, but they explain the computational traditions that displaced or coexisted with it:

- **Rhind Mathematical Papyrus**, c. 1650 BCE, copied by Ahmes from an older Egyptian source: unit fractions and worked administrative problems. Separate Egyptian notation.
- **Plimpton 322**, Old Babylonian, c. 1800 BCE: sexagesimal table whose interpretation as trigonometric, pedagogical or problem-generating remains debated. Separate Mesopotamian lineage.
- **Nine Chapters on the Mathematical Art**, compiled in China by the first century CE with Liu Hui’s commentary of 263: counting-rod algorithms. Separate decimal positional instrument tradition.
- **Aryabhata**, *Āryabhaṭīya*, 499: Indian astronomical computation and alphabetic number encoding.
- **Brahmagupta**, *Brāhmasphuṭasiddhānta*, 628: explicit arithmetic rules for zero and negative quantities, although his rule for zero divided by zero is not modern.
- **al-Khwārizmī**, early ninth century: Arabic work on calculation with Indian numerals, known in Latin through adaptations beginning *Dixit Algoritmi*.
- **Fibonacci**, *Liber Abaci*, 1202, revised 1228: commercial and recreational problems using the “nine Indian figures” and the sign 0.
- **Sacrobosco**, *Algorismus vulgaris*, early thirteenth century: numeration, addition, subtraction, halving, doubling, multiplication, division, progressions and root extraction with positional digits; an exceptionally successful university text. [Ptolemaeus Arabus et Latinus manuscript record](https://ptolemaeus.badw.de/jordanus/ms/4076)
- **Luca Pacioli**, *Summa de arithmetica*, 1494: consolidated commercial arithmetic and bookkeeping; interestingly recommended Roman letters for year dates “for beauty” while using positional figures for calculation.
- **Recorde**, *Ground of Artes*, 1543: taught English readers both methods.
- **John Napier**, *Mirifici Logarithmorum Canonis Descriptio*, 1614: logarithms accelerated calculation in Hindu-Arabic notation. Roman numerals remained for headings and dates, not logarithmic work.

### Fibonacci and Bugia

**[Documented autobiography]** In the prologue to *Liber Abaci*, Leonardo of Pisa says his father was a Pisan customs official at Bugia/Béjaïa in North Africa and arranged his instruction there. Leonardo learned the *modus Indorum*, traveled around the Mediterranean comparing methods, and chose the Indian system. This is not a tale invented by later biographers, though picturesque details about a single Muslim “master” may go beyond Leonardo’s words. [Sigler-related text and Chapter XII transcription](https://www.math.stonybrook.edu/~tony/archive/118s13/fibonacci.html)

### Gerbert’s apices

Gerbert of Aurillac, later Pope Sylvester II (pope 999–1003), taught an abacus employing counters marked with digit-like signs traditionally called *apices*.

**[Documented scholarly tradition]** Gerbert’s association with the abacus and apices is well founded in manuscripts and reports by pupils.

**[Disputed detail]** Whether his digit forms came directly from Islamic Spain, through Catalonia, or through another channel remains debated. His system seems not to have employed zero as an ordinary counter; an empty column did its work.

**[Legend]** Later hostile stories made Gerbert a magician who learned forbidden arts from Muslims, possessed a talking brazen head, or obtained the papacy through a pact with the Devil. These belong to medieval polemic and wonder literature, not evidence about his mathematics.

## 9. Comparative instruments explicitly not Roman

- Chinese **suanpan**, Japanese **soroban**, counting rods and rod numerals are independent East Asian technologies. They should not be described as descendants of the Roman hand-abacus.
- The Andean **quipu/khipu** records decimal positional information in knot placement and type; it is neither Roman nor a simple tally.
- Finger reckoning is near-universal and cannot be assigned a single Roman origin.
- Modern “Roman-numeral long division” methods demonstrate mathematical possibility, not historical use.

---

## Transmission and replacement

### 1. Italy and the Empire

From roughly the fifth century BCE, the Latin system differentiated itself from its Etruscan parent by left-to-right ordering and extensive large-number notation. Roman state expansion carried it through Italy, western Europe, North Africa and much of the Mediterranean.

**[Artefact]** Coins, milestones, military inscriptions, building accounts, amphorae, calendars and funerary monuments attest numbers for:

- money and weights;
- troop units;
- ages;
- regnal and tribunician years;
- distances;
- quantities;
- consular dates;
- production batches and ownership.

Greek alphabetic numerals continued beside Roman ones in the eastern Mediterranean. Roman political rule did not imply uniform numeral replacement.

### 2. Late antiquity

Cursive inscriptions and papyri produced ligatures and regional forms. The sign ↅ for six appears widely; L and C could be written in deliberately numeral-like cursive forms to avoid confusion with letters.

Roman numerals survived the western imperial collapse because Latin literacy survived in the Church, law, monastic education and successor administrations. Indeed, their geographic cultural range became greater in medieval Latin Christendom.

### 3. Medieval Europe

From the fifth through twelfth centuries Roman numerals were the usual written number notation in western Europe. Greek and Arabic alternatives were known in border regions and to specialists.

Uses expanded into:

- computus and Easter tables;
- manuscript quire, folio and chapter numbering;
- legal documents;
- charters and accounts;
- astronomy;
- regnal and pontifical ordinals;
- liturgical calendars;
- chronograms.

Minuscule forms, final-j spellings and superscript grammatical endings flourished. There was never one medieval standard.

### 4. India → Baghdad → al-Andalus → Latin Europe

This is the principal replacement route, not a route by which Roman numerals themselves traveled.

1. **[Documented intellectual transmission]** Indian decimal positional numeration reached Abbasid scholarly circles by the late eighth century.
2. **[Documented text]** Al-Khwārizmī wrote on calculation with Indian numerals in the early ninth century.
3. Arabic mathematical astronomy carried positional and alphabetic systems across North Africa and into al-Andalus.
4. Tenth- and eleventh-century Iberian Latin scholars encountered Arabic science; some modified Roman notation rather than immediately adopting the digits.
5. Gerbert’s abacus introduced apices into an elite Latin setting around the late tenth century.
6. Twelfth-century translators produced Latin algorisms associated with al-Khwārizmī and Indian reckoning.
7. Fibonacci’s 1202 *Liber Abaci* addressed merchants and practical calculators from an Italian–Mediterranean perspective.
8. University algorisms such as Sacrobosco’s and commercial *abbaco* schools normalized pen calculation.
9. Printing, expanding literacy and increasingly calculation-intensive commerce favored the compact positional system.
10. Roman numerals retreated to ordinal, ceremonial and paratextual functions rather than becoming extinct.

Calling modern digits simply “Arabic” is therefore incomplete but not wholly false: their remote structural and graphic ancestry is Indian; Arabic-speaking scholars transmitted, reshaped and taught them to Latin Europe.

### 5. The Florentine prohibition of 1299

**[Documented regulation]** The Florentine moneychangers’ guild, the Arte del Cambio, prohibited the “figures” in its registers in 1299, requiring Roman numerals or written forms. The restriction remained in force for at least twenty years.

The rule’s stated concern was fraud: a positional digit could be altered or have a zero appended.

**[Scholarly interpretation]** Dirk Struik and later historians add guild politics, mistrust of unfamiliar notation and social conflict between established and innovating groups.

**[Legendary inflation]** It was not a Europe-wide ban on mathematics, proof that the Church declared zero satanic, or evidence that bankers maintained universally documented secret double books. Charles Burnett’s study of “satanic ciphers” traces the Devil/zero story as a modern historical canard. [Oxford HSMT, “Medieval Europe’s satanic ciphers”](https://www.hsmt.ox.ac.uk/publication/1074391/ora-hyrax)

In 1348 Padua required booksellers to list prices *non per cifras, sed per literas clara*—“not by ciphers, but by clear letters.” Frankfurt still restricted reckoners’ use of positional figures in 1494.

### 6. The long replacement

Roman numerals did not vanish in 1202:

- Italian city-states adopted positional figures relatively early, around 1300 in many mercantile settings.
- Portugal’s broad shift occurred around 1500.
- England and Germany retained Roman notation heavily into the late fifteenth and sixteenth centuries.
- William Cecil, Lord Burghley, reportedly converted financial figures back into Roman numerals late in the sixteenth century.
- Some English state-account restrictions involving Roman forms survived into the nineteenth century.
- By the seventeenth century, positional numerals had won ordinary calculation and most quantitative recordkeeping.

The printing press helped, but early printing was not instantly “Arabic”: many incunables contain no positional digits. Social recruitment of new literate merchants and officials was at least as important as abstract efficiency.

### 7. Present survivals

#### Monarchs and popes

Elizabeth II, Louis XIV, Benedict XVI and John Paul II use Roman ordinals. In speech these are ordinals—“the Second,” “the Fourteenth”—not cardinal readings.

**[Tradition]** Numbering rulers systematically is often retrospective. Medieval contemporaries did not always use the same ordinals later historians assigned, so apparent “errors” can reflect later historiography.

#### Clocks

Many dials use IIII at four and IX at nine.

- **[Documented continuity]** IIII was ordinary ancient and medieval notation, so it needs no special royal decree.
- **[Scholarly suggestion]** IIII may balance VIII visually and divide a dial into groups using I, V and X.
- **[Tradition]** It simplified casting sets or preserved sundial usage.
- **[Legend]** Charles V, Louis XIV, or another ruler supposedly ordered IIII after correcting a clockmaker; versions contradict one another and lack contemporary evidence.
- **[Legend]** IV was avoided because it begins Jupiter’s Latin name, IVPPITER. Ancient inscriptions freely used IV in other contexts, and medieval clockmakers were not operating under a documented taboo.

The late-fourteenth-century Wells Cathedral dial is frequently cited for IIII, but no single dial can prove why the convention spread. [Fondation de la Haute Horlogerie](https://www.hautehorlogerie.org/en/watches-and-culture/watchmaking-knowledge/encyclopedia/roman-numeral-iiii-on-dials); [Seiko Museum](https://museum.seiko.co.jp/en/knowledge/trivia02/)

#### Books and outlines

Roman numerals distinguish prefaces from the Arabic-numbered main text, identify volumes, chapters, acts, scenes and nested list levels. This supplies a useful second enumeration series rather than simulating antiquity alone.

#### Buildings and monuments

Dates in Roman capitals signal permanence, Latinity, state authority or antiquity. Additive dates such as MDCCCC are historically legitimate even when a modern style guide prefers MCM.

**[Documented modern dispute]** Arlington Memorial Amphitheater’s 1915 cornerstone reads MDCCCCXV; critics immediately called it inaccurate and preferred MCMXV, used on the finished pediment. An archival memo suggested the architects chose the longer form for visual balance. Both evaluate to 1915 under historical additive practice. [Washington Post investigation](https://www.washingtonpost.com/local/arlington-national-cemetery-roman-numerals/2021/12/04/7f5f33bc-5471-11ec-9267-17ae3bde2f26_story.html)

#### Film and television dates

Roman copyright years became a familiar screen convention.

- **[Documented practice]** The dates occur extensively in surviving credits.
- **[Scholarly inference/trade tradition]** Roman capitals were visually robust on degraded film and harmonized with title typography.
- **[Anecdote]** The difficult-to-read date supposedly disguised a production’s age from viewers.
- **Absence of evidence:** no identified industry decree or originating studio memorandum establishes either explanation universally. The “hide the age” claim should remain folklore.

#### Super Bowls

The NFL adopted Roman numbering from Super Bowl V, played in 1971, to distinguish the game-number from the season’s calendar year.

**[Documented modern exception]** In 2014 the NFL announced that the fiftieth game would be branded “Super Bowl 50,” not “Super Bowl L”; Roman numerals resumed with LI. The organization said its designers found the solitary L visually unsatisfactory after testing numerous logos. [NFL announcement](https://www.nfl.com/news/nfl-won-t-use-roman-numerals-for-super-bowl-50-0ap2000000355943)

#### East Asia

Chinese-character numerals remain culturally and legally active in China, Japan and Korea beside Hindu-Arabic figures, especially in formal documents, calendars, addresses and ceremonial writing. They are not Roman survivals. Roman numerals occur there through global typography—clocks, outlines, product names and monarchic or event labels.

---

## People

| Person | Dates | Connection | Evidence status |
|---|---|---|---|
| Gaius Duilius | consul 260 BCE | Victory column carried enormous additive numeral phrase | Artefact, later recut |
| Cicero | 106–43 BCE | Textual evidence for Roman accounting, fractions and number language | Documented text |
| Vitruvius | fl. first century BCE | Proportional and metrological calculation | Documented text |
| Augustus | 63 BCE–14 CE | Period in which older inscriptions were restored and numeral styles shifted | Artefact/history |
| Pliny the Elder | 23/24–79 CE | Discussed old large-number limits and Roman measures | Documented text |
| Suetonius | c. 69–after 122 | Reports Tiberius exploiting an ambiguously framed will-numeral to reduce Livia’s legacy | Documented anecdote, motives uncertain |
| Priscian | fl. c. 500 | Proposed an alphabetic theory of Roman numeral origins | Documented ancient theory, historically late |
| Dionysius Exiguus | fl. early sixth century | Used *nulla* in an Easter table, 525 | Documented text |
| Bede | 672/3–735 | Described finger reckoning and computus; N-zero appears in his milieu | Documented, attribution of table uncertain |
| Gerbert of Aurillac/Sylvester II | c. 946–1003 | Taught apices and abacus reckoning | Documented core; magical tales legendary |
| al-Khwārizmī | fl. c. 820 | His name produced *algorism/algorithm*; Indian arithmetic contributed to Roman replacement | Documented transmission |
| Adelard of Bath | c. 1080–c. 1152 | Translator and teacher in Arabic–Latin scientific exchange | Documented |
| H. Ocreatus | fl. c. 1130 | Constructed positional Roman–cifra hybrid | Documented manuscript; identity obscure |
| Richard FitzNigel | c. 1130–1198 | Described Exchequer counter reckoning | Documented text |
| Fibonacci | c. 1170–after 1240 | Learned in Bugia; wrote *Liber Abaci* in 1202/1228 | Documented autobiography and text |
| Sacrobosco | died c. 1236 | Wrote influential *Algorismus vulgaris* | Documented manuscripts |
| Luca Pacioli | c. 1447–1517 | Commercial arithmetic; preferred Roman date letters aesthetically | Documented text |
| Jacob Köbel | 1460/70–1533 | Printed a 1514 counting-board arithmetic using Roman numerals | Documented book |
| Robert Recorde | c. 1512–1558 | Taught counter-casting and written arithmetic in English | Documented book |
| Petrus Bungus | died 1601 | Catalogued numeral variants in a number-mysticism work, 1583–84 | Documented book |
| John Napier | 1550–1617 | Logarithms mark the new calculation regime | Documented text |
| Theodor Mommsen | 1817–1903 | Established the influential Greek-letter/mixed origin theory in 1850 | Historic scholarship |
| Karl Menninger | 1898–1963 | Synthesized numeral forms, words and instruments | Secondary synthesis |
| Georges Ifrah | 1947–2019 | Popular global synthesis with rich illustrations but unreliable leaps | Secondary synthesis requiring checking |
| Paul Keyser | modern scholar | Reconstructed Etruscan tally ancestry in 1988 | Major scholarly argument |
| Stephen Chrisomalis | contemporary | Produced the standard cross-cultural structural survey in 2010 | Modern scholarly synthesis |

### Tiberius and Livia’s will

Suetonius, *Galba* 5, reports that Tiberius manipulated the reading of a framed or barred numeral in Livia’s will, reducing Galba’s intended legacy by a factor of 500.

**Status:** **[Documented ancient anecdote]**, but Suetonius wrote biography rich in moralizing stories. The episode proves that multiplier marks could create consequential ambiguity; it does not prove the precise psychology attributed to Tiberius.

---

## Culture

### Law and administration

Roman legal and fiscal documents used numerals for shares, sums, penalties, office repetitions and dates. On imperial inscriptions:

- `COS III` means consul for the third time;
- `TR P XII` means holder of tribunician power for a twelfth term/year;
- legion numbers distinguish units;
- ages commonly follow `ANN`, *annorum*.

These ordinal uses can date monuments even where no calendar year is stated.

Medieval charters often surrounded numerals with words or marks to prevent alteration. Final-j forms and written-out sums served the same anti-fraud goal that later motivated restrictions on positional digits.

### Liturgy and computus

Roman numerals organized:

- Easter cycles;
- Golden Numbers;
- indictions;
- Kalends, Nones and Ides;
- biblical chapters and liturgical lessons;
- manuscript canons and tables.

Dionysius’s *nulla* demonstrates that computus could require a zero result even within Roman notation. There is no year zero in the traditional BCE/CE chronology because ordinal year-counting moves from 1 BCE to 1 CE; this is related to the chronology’s construction, not mechanically caused by the absence of a Roman zero glyph.

### Chronograms

In a chronogram, letters that are also Roman numeral signs are extracted and summed to produce a date. They may be enlarged or capitalized.

Example principle:

`M + D + C + L + X + V + I = 1666`

The descending phrase `MDCLXVI` famously uses every standard sign once.

**[Documented tradition]** Confirmed chronograms appear from the mid-fourteenth century and became popular on Renaissance and Baroque tombs, church inscriptions, medals and commemorative texts. Retrospective chronograms purporting to encode earlier dates do not establish earlier invention.

### Gematria and isopsephy

Hebrew gematria and Greek isopsephy assign numerical values across their alphabets. Roman numerals are different:

- Greek and Hebrew systems are ciphered-additive alphabetic systems.
- Almost every relevant letter has a conventional numerical value.
- Roman notation uses a small selected inventory with a five/ten structure.

Chronograms became possible precisely because I, V, X, L, C, D and M were simultaneously letters and numeral signs after alphabetization. Calling all three practices “gematria” conceals their structural differences.

### Coins

Roman Republican bronzes often marked denomination fractionally:

- one pellet: one *uncia*;
- two pellets: *sextans*;
- three: *quadrans*;
- four: *triens*;
- S: *semis*.

Coin evidence is especially important because it anchors fractional signs in dated material rather than later manuscript tables.

### Calendars

Roman calendar dates were relational: “the third day before the Nones,” counted inclusively. Numerals modified calendar words rather than supplying a modern day/month/year string.

Medieval calendar numerals developed specialized northern European variants, sometimes misleadingly called “runic numerals.” They are modified Roman notation, not automatically inherited pagan runes.

### Typography

Roman capitals derive prestige from monumental inscriptional models. Renaissance printers revived classical-looking proportions while medieval scribes continued lowercase `i, v, x, l, c, d, m`.

Modern typographic uses include:

- small-cap Roman numerals;
- lowercase preliminary pagination;
- tabular alignment in outlines;
- dedicated Unicode compatibility characters;
- serif inscriptional numerals in monuments;
- intentionally additive forms for visual width.

A malformed modern inscription is not automatically historically “wrong.” The proper questions are whether it is interpretable, internally consistent, appropriate to its chosen convention, and intentional.

### Literature and art

Roman numerals structure plays into acts and scenes, poems into books, symphonies into movements, sequels into numbered titles and paintings or buildings into dated objects. They connote antiquity, succession, ceremony, hierarchy and monumentality.

Examples include:

- Shakespeare editions: Act III, Scene ii;
- papal and royal portrait captions;
- sporting events and film sequels;
- copyright dates;
- monumental foundation stones;
- chapter numerals in novels;
- chemical oxidation states such as iron(III), a modern scientific extension;
- chord analysis, where I, IV and V identify scale degrees—another modern specialized use.

---

## Words descending from the reckoning traditions

| Word | Derivation | Qualification |
|---|---|---|
| calculus, calculate | Latin *calculus*, small pebble/counter | Directly connected with physical reckoning stones |
| digit | Latin *digitus*, finger/toe | Reflects finger counting; later a numeral character |
| abacus | Latin *abacus*, Greek *abax/abak-* “board/slab” | A Semitic origin related to “dust” is commonly proposed but not certain |
| algorithm | Medieval Latin *algorismus/algoritmi*, from al-Khwārizmī’s name | Later reshaped under influence of Greek *arithmos* |
| algorism | The older form for positional written arithmetic | Historically distinct from today’s broad “algorithm” |
| cipher | Arabic *ṣifr*, empty/zero, through Medieval Latin *cifra* and French | Acquired the senses “digit,” “zero,” “nonentity,” and encoded writing |
| zero | Arabic *ṣifr* through Latin/Italian *zephirum, zefiro, zero* | Fibonacci used *zephirum* |
| ounce | Latin *uncia*, one twelfth | Passed through Romance weight terminology |
| inch | Latin *uncia* through Old English/Romance contact | Originally a twelfth part |
| quincunx | Latin *quincunx*, five twelfths/five-uncia arrangement | Now also the five-dot pattern |
| calculator | Latin *calculator*, a reckoner | Originally a person; later a machine |
| counter | Medieval Latin/French counting object | Became both a reckoning token and, by semantic branching, a shop surface |

[MacTutor mathematical word histories](https://mathshistory.st-andrews.ac.uk/Miller/mathword/); [Oxford Learner’s Dictionaries, “abacus”](https://www.oxfordlearnersdictionaries.com/definition/english/abacus)

---

## Controversies and disputes

### 1. “Who invented Roman numerals?”

No named inventor is documented.

- **Fact:** related Etruscan signs are earlier.
- **Reconstruction:** Roman notation diffused from Etruscan tally-derived notation.
- **Unknown:** the individuals, precise town and exact decade.
- **Legend:** a Roman king, shepherd, merchant or soldier devised I–V–X in a single act.

### 2. Did V arise as half of X?

**[Scholarly reconstruction]** Yes, in the leading tally theory: an early five-sign resembles half of the ten-sign, and fifty similarly half of one hundred. This repeated graphic rule is strong comparative evidence.

**Caution:** It is not witnessed by an ancient caption saying “cut X in half.” The claim is palaeographic inference.

### 3. Are I, V and X pictures of fingers?

**[Disputed historic theory; popular legend]** Finger counting is ancient, but resemblance alone does not establish sign ancestry. The tally account better incorporates the whole sequence.

### 4. Are C and M initials of *centum* and *mille*?

**[Myth if presented as original invention.]** Their eventual alphabetic match aided normalization. C developed from an older hundred-sign; M emerged from transformations of the apostrophic thousand-sign and from abbreviation of *mille*. Alphabetization is historical, but original acrophony is not.

### 5. Did Roman numerals prohibit subtraction?

No.

- Additive construction is older and more frequent.
- Subtractive construction is genuinely ancient.
- Modern restrictions on permitted pairs are later norms.
- `IIII`, `VIIII` and `DCCCC` are not automatically errors.
- A form can still be a stonecutter’s mistake, but deviation from a school rule does not prove it.

### 6. Why IIII on clocks?

The survival of older additive notation is documented; the causal story is not.

- visual balance: plausible inference;
- fewer molds or repeated casting: craft tradition without general proof;
- avoidance of IV/Jupiter: legend;
- royal command after a clockmaker’s error: legend in mutually incompatible versions.

### 7. Did Roman numerals have zero?

This requires four distinctions:

1. empty quantity as a concept;
2. word meaning “none”;
3. sign for a zero result;
4. positional placeholder/digit.

Classical Roman notation lacks (4) and a standard member-sign for (3). Latin always possessed words for absence. Late antique/medieval computists used *nulla* and N for (3). Therefore “Romans could not conceive nothing” is false; “classical Roman numerals were not a zero-based positional system” is true.

### 8. Could Romans calculate with their numerals?

**[Disputed.]**

- Modern authors can devise correct symbolic algorithms.
- Literary evidence proves sophisticated arithmetic.
- Abaci and finger reckoning are historically attested.
- No surviving ancient evidence shows ordinary long arithmetic performed by rewriting Roman-numeral strings.

The responsible conclusion is not “impossible,” but “not demonstrated as their normal method.”

### 9. Did bad numerals prevent Roman mathematics?

**[Rejected technological determinism.]** Roman notation is cumbersome for written algorithms, but Romans administered extensive fiscal, military, engineering and metrological systems using complementary tools. Greek-speaking subjects used other notations; educated Romans could use Greek mathematics. Notation mattered, but cannot alone explain the history of Roman theoretical mathematics.

### 10. Was the Roman abacus in the Louvre?

**[Catalogue confusion.]** A famous Paris bronze is in the BnF, inventory bronze.1925, from Sainte-Geneviève/Peiresc. Comparable pieces include British Museum OA.2419 and Museo Nazionale Romano 65054. The BnF itself emphasizes that this class lacks ancient excavation provenance because every known specimen surfaced in early-modern collections.

### 11. Did Fibonacci single-handedly abolish Roman numerals?

**[Heroic simplification.]** *Liber Abaci* was pivotal, especially for Italian commerce, but earlier Latin translations, Iberian contacts and Gerbert preceded it; Sacrobosco, *abbaco* teachers, printers and merchants followed it. Replacement took centuries.

### 12. Did Florence ban zero because the Church feared it?

**[Modern legend.]** The surviving guild rationale concerns fraud and legibility. Broader social resistance is plausible. A Church-wide theological ban and satanic-zero campaign are not documented.

### 13. Is 3,999 the maximum?

**[Modern classroom convention.]** Ancient special signs and multiplier marks reached far higher. Repetition also has no mathematical upper bound.

### 14. Film dates conceal age

**[Industry folklore.]** Some viewers and practitioners repeat it; visual durability and typography are alternative explanations. No originating directive has been identified.

### 15. Ifrah’s reliability

Georges Ifrah’s *Universal History of Numbers* is exceptionally broad and visually useful, but Joseph Dauben’s detailed review documents errors, unsupported transitions and excessive confidence, especially when Ifrah connects separated cultures or supplies exact chronologies from ambiguous evidence. It should be mined for leads and illustrations, then checked against corpora and specialist studies—not treated as the source of record. [Dauben review, AMS](https://www.ams.org/notices/200202/rev-dauben.pdf)

### 16. What the global “first zero” debates do not prove about Rome

Babylonian placeholders, Maya zeroes, Indian zero and Chinese empty rod positions concern distinct functions and lineages.

- A Babylonian placeholder need not be a number operated on like Brahmagupta’s zero.
- Maya zero is independent and calendrically attested early.
- Bakhshali’s dot is a positional placeholder; its manuscript leaves have multiple radiocarbon ranges.
- Brahmagupta’s 628 rules explicitly treat zero arithmetically.
- Chinese counting boards used vacant positions before a written circular zero became common.
- None supplied the original Roman system.

Statements such as “X invented zero first” are ill-posed unless “zero” is defined as word, empty position, placeholder sign, cardinal number or arithmetic operand.

---

## Open questions

1. Which exact late-sixth- or fifth-century BCE object should count as the earliest unambiguous Roman rather than Etruscan numeral inscription?
2. Can new stratified excavations close the provenance gap for portable bronze hand-abaci?
3. Did perishable wooden Italic tallies really display the hypothesized stages from strokes to crossed five/ten signs?
4. How frequently were subtractive forms used by date, region, medium and social context? Large machine-readable epigraphic corpora could replace impressionistic examples.
5. Were Roman numeral strings ever systematically manipulated during calculation, or only written before and after operations performed physically or mentally?
6. How should the Ostian 100,000,000 inscription be read and contextualized against the complete large-number corpus?
7. At what dates and through which workshops did D and M become dominant rather than merely alphabetic abbreviations?
8. How far did Visigothic Roman-numeral ligatures affect the palaeography of western Hindu-Arabic figures?
9. Who first established the stable IIII/IX clock-dial combination, and do workshop records support visual-balance or casting explanations?
10. When did film studios begin Romanizing copyright dates, and do production manuals explain why?
11. Which apparently “incorrect” modern monumental dates are errors, and which are deliberate additive, medievalizing or spatially balanced forms?
12. Can the BnF, British Museum and Roman abaci be authenticated more securely through alloy, tool-mark and collection-history analysis?
13. Was the Etruscan/Greek decimal-quinary structure independently invented, mutually borrowed, or derived from a shared contact-zone practice?
14. How should the Tuscania dice assignments be revised if larger statistically controlled corpora of Etruscan dice become available?

Absence of a final answer to these questions is itself an evidentiary result. The history is reconstructable in outline, but it is not a continuous chain of named inventors and securely proven motives.

---

## Sources

### Core modern scholarship

1. Stephen Chrisomalis, *Numerical Notation: A Comparative History*. Cambridge University Press, 2010, especially chapter 4, “Italic Systems,” pp. 93–132 in the printed pagination.  
   https://doi.org/10.1017/CBO9780511676062.004  
   Accessible book scan consulted:  
   https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20(CUP,%202010)(ISBN%200521878187)(O)(498s)_MPop_.pdf

2. Paul Keyser, “The Origin of the Latin Numerals 1 to 1000,” *American Journal of Archaeology* 92.4, 1988, pp. 529–546.  
   https://doi.org/10.2307/505248  
   https://www.journals.uchicago.edu/doi/abs/10.2307/505248

3. Karl Menninger, *Number Words and Number Symbols: A Cultural History of Numbers*, translated by Paul Broneer. MIT Press, 1969; revised reprint.  
   https://openlibrary.org/books/OL5612154M/Number_words_and_number_symbols  
   https://archive.org/details/numberwordsnumbe00menn

4. Florian Cajori, *A History of Mathematical Notations*, vol. 1. Open Court, 1928.  
   https://en.wikisource.org/wiki/A_History_Of_Mathematical_Notations/Volume_1/Romans  
   https://www.maths.ed.ac.uk/~v1ranick/papers/cajorinot.pdf

5. Stephen Chrisomalis, *Reckonings: Numerals, Cognition, and History*. MIT Press, 2020.  
   https://glossographia.com/reckonings/

6. Stephen Chrisomalis, “Juvenile Ethnopaleography,” including discussion of Roman–positional hybrids.  
   https://glossographia.com/2010/02/06/juvenile-ethnopaleography/

7. Oxford Classical Dictionary, “numbers, Roman.”  
   https://academic.oup.com/edited-volume/61673/chapter-abstract/548071223

8. Charles Burnett, “The Palaeography of Numerals,” in *The Oxford Handbook of Latin Palaeography*, 2020.  
   https://doi.org/10.1093/oxfordhb/9780195336948.013.96

9. Gilberto Artioli et al., “Gambling with Etruscan Dice: A Tale of Numbers and Letters,” *Archaeometry* 53, 2011.  
   https://doi.org/10.1111/j.1475-4754.2011.00596.x

10. Frederik Christiaan Woudhuizen, “Etruscan Numerals in Indo-European,” *Talanta* 20–21. Consulted for the history of assignments, not accepted as establishing Indo-European descent.  
    https://www.talanta.nl/wp-content/uploads/2014/10/Woudhuizen-109-124.pdf

11. “La questione della resa grafica dei numerali etruschi: appunti e considerazioni,” *Aristonothos*.  
    https://riviste.unimi.it/index.php/aristonothos/article/view/13725

### Epigraphy, inscriptions and artifacts

12. Roman Inscriptions of Britain, Vindolanda Tablets II, Introduction: script, abbreviations and numerals.  
    https://romaninscriptionsofbritain.org/tabvindol/vol-II/introduction

13. Bibliothèque nationale de France, “Abaque à boutons mobiles,” inventory bronze.1925.  
    https://medaillesetantiques.bnf.fr/ws/catalogue/app/collection/record/ark:/12148/c33gb18n6s

14. British Museum, portable abacus, OA.2419.  
    https://www.britishmuseum.org/collection/object/H_OA-2419

15. Museo Galileo exhibition catalogue, Roman portable counter abacus, Museo Nazionale Romano inventory 65054.  
    https://exhibits.museogalileo.it/archimedes/object/PortableCounterAbacus.html

16. Treccani, “Dadi,” including the Tuscania dice and history of their reading.  
    https://www.treccani.it/enciclopedia/dadi_%28Enciclopedia-Italiana%29/

17. Unicode Consortium, Number Forms names list.  
    https://www.unicode.org/charts/nameslist/n_2150.html

18. Unicode Standard, Number Forms chart, U+2150–U+218F.  
    https://www.unicode.org/charts/PDF/U2150.pdf

19. David Perry and Michael Everson, proposal on ancient Roman weights and monetary signs, with coin examples.  
    https://www.unicode.org/L2/L2006/06173-roman-coinage.pdf

20. “Un abecedario metrológico latino pintado sobre cerámica iberorromana del Tossal de Manises,” *Zephyrus* 94.  
    https://doi.org/10.14201/zephyrus202494123142

21. John Edwin Sandys, *Latin Epigraphy: An Introduction to the Study of Latin Inscriptions*.  
    https://archive.org/details/introductiontost00sand

22. Washington Post, archival investigation of the MDCCCCXV/MCMXV inscriptions at Arlington Memorial Amphitheater.  
    https://www.washingtonpost.com/local/arlington-national-cemetery-roman-numerals/2021/12/04/7f5f33bc-5471-11ec-9267-17ae3bde2f26_story.html

### Arithmetic, medieval transmission and textbooks

23. Richard FitzNigel, *Dialogus de Scaccario* / *Dialogue concerning the Exchequer*.  
    https://www.medievalhistory.net/excheq1.htm

24. Hilary Jenkinson, “The Arithmetic of the Exchequer.”  
    https://repository.londonmet.ac.uk/7523/1/328938.pdf

25. Barbara E. Reynolds, “The Algorists vs. the Abacists,” in *Sherlock Holmes in Babylon*. Mathematical Association of America, 2003.  
    https://doi.org/10.5948/UPO9781614445036.021

26. Ptolemaeus Arabus et Latinus, manuscript description of Sacrobosco’s *Algorismus*.  
    https://ptolemaeus.badw.de/jordanus/ms/4076

27. Anianus and Sacrobosco, 1488 printed *Computus* and *Algorismus*, Freiburg digital copy.  
    https://dl.ub.uni-freiburg.de/diglit/anianus1488

28. Vatican Pal. lat. 1452, digital manuscript including Sacrobosco’s *Algorismus*.  
    https://digi.ub.uni-heidelberg.de/diglit/bav_pal_lat_1452

29. Sacrobosco, *Algorismus vulgaris*, English selection translated from Maximilian Curtze’s 1897 edition.  
    https://www.originalsources.com/Document.aspx?DocID=3LEK1GQB2EZFQD6

30. Leonardo Fibonacci, *Liber Abaci*, 1202/revised 1228; Chapter XII Latin and English transcription keyed to Laurence Sigler’s translation.  
    https://www.math.stonybrook.edu/~tony/archive/118s13/fibonacci.html

31. Laurence E. Sigler, trans., *Fibonacci’s Liber Abaci*. Springer, 2002. Bibliographic record and relevant text referenced through the preceding source.

32. Robert Recorde, *The Ground of Artes*, first edition 1543; bibliographic overview.  
    https://en.wikipedia.org/wiki/The_Ground_of_Arts

33. Gareth Roberts, ed., *Robert Recorde: The Life and Times of a Tudor Mathematician*. University of Wales Press.  
    https://api.pageplace.de/preview/DT0400.9780708325278_A23706914/preview-9780708325278_A23706914.pdf

34. “From Abacus to Algorism: Theory and Practice in Medieval Arithmetic,” *British Journal for the History of Science*.  
    https://www.cambridge.org/core/journals/british-journal-for-the-history-of-science/article/abs/from-abacus-to-algorism-theory-and-practice-in-medieval-arithmetic/7DFF144C90C127E715CA40083254E601

35. Charles Burnett, “Medieval Europe’s Satanic Ciphers: On the Genesis of a Modern Myth.”  
    https://www.hsmt.ox.ac.uk/publication/1074391/ora-hyrax

36. MacTutor History of Mathematics, “A History of Zero.”  
    https://mathshistory.st-andrews.ac.uk/HistTopics/Zero/

37. MacTutor, “Earliest Uses of Symbols for Fractions.”  
    https://mathshistory.st-andrews.ac.uk/Miller/mathsym/fractions/

38. MacTutor, “Earliest Known Uses of Some of the Words of Mathematics.”  
    https://mathshistory.st-andrews.ac.uk/Miller/mathword/

39. Oxford English-language history of *abacus*.  
    https://www.oxfordlearnersdictionaries.com/definition/english/abacus

40. *Liber Abaci* square-root procedures, modern textual study.  
    https://arxiv.org/abs/2401.12016

### Modern persistence

41. Fondation de la Haute Horlogerie, “Understanding Roman Numeral IIII on Dials.”  
    https://www.hautehorlogerie.org/en/watches-and-culture/watchmaking-knowledge/encyclopedia/roman-numeral-iiii-on-dials

42. Seiko Museum Ginza, “The Mystery of Numerical Notation on the Dial Plate.”  
    https://museum.seiko.co.jp/en/knowledge/trivia02/

43. National Archives, UK, guide to Roman numerals in historical documents.  
    https://www.nationalarchives.gov.uk/help-with-your-research/reading-old-documents/roman-numerals/

44. NFL, announcement that Super Bowl 50 would not be styled Super Bowl L.  
    https://www.nfl.com/news/nfl-won-t-use-roman-numerals-for-super-bowl-50-0ap2000000355943

### Historiography and source criticism

45. Georges Ifrah, *The Universal History of Numbers: From Prehistory to the Invention of the Computer*, English trans., Wiley, 1999/2000.

46. Joseph W. Dauben, “The Universal History of Numbers and The Universal History of Computing,” *Notices of the American Mathematical Society* 49, 2002.  
    https://www.ams.org/notices/200202/rev-dauben.pdf

47. Ernest Davis, review of Chrisomalis, *Numerical Notation*, *SIAM News*.  
    https://cs.nyu.edu/~davise/papers/OldReviews/Chrisomalis.pdf

48. Open Library bibliographic record for Menninger’s 1969 edition.  
    https://openlibrary.org/books/OL5612154M/Number_words_and_number_symbols

49. Stephen Chrisomalis, *Glossographia*, author and research description.  
    https://glossographia.com/about/

50. MacTutor History of Mathematics Archive, main index.  
    https://mathshistory.st-andrews.ac.uk/
