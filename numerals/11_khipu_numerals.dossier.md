# The khipu: knotted decimal numerals of the Andes: Research Dossier

> **Evidence labels used throughout**
>
> - **[Artefact]** surviving object or archaeological context.
> - **[Documented text]** historical testimony, manuscript, legal record, or early printed source.
> - **[Secure reading]** interpretation independently checkable against repeated structures or arithmetic relations.
> - **[Scholarly reconstruction]** inference accepted or seriously entertained in specialist scholarship.
> - **[Disputed]** claim with material scholarly objections or insufficient independent confirmation.
> - **[Tradition]** Indigenous or colonial testimony whose historical meaning cannot be checked directly.
> - **[Legend]** story repeated without adequate documentary or archaeological support.
> - **[Modern invention]** modern notation, reconstruction, revival, artwork, software, or analogy—not an ancient practice.

## Basic identification

| Field | Identification |
|---|---|
| **Name** | **Khipu** in modern Andeanist spelling; **quipu**, **quipo**, and other forms in colonial and older European spelling. Quechua *khipu* means “knot” and, contextually, a knotted record/account. |
| **Base** | **Ten** in the canonical Inka numerical system. |
| **Type** | **Decimal positional notation on each numerical cord**, but with **additive repetition inside each place**: three single hundred-knots mean 300. It is therefore best described as **positional-additive decimal**, not “ciphered” in the sense of possessing ten independent digit glyphs. |
| **Signs** | Empty decimal position = 0; figure-eight knot = 1 in the units position; long knots with 2–9 turns = units 2–9; clusters of 1–9 single overhand knots = tens, hundreds, thousands, and higher places. No khipu numerals are encoded in Unicode. |
| **Carrier** | A primary cord bearing pendant cords; pendants may bear subsidiary cords, which may bear further subsidiaries. Color, fiber, spin, ply, attachment direction, spacing, grouping, and knot direction could also distinguish categories or records. |
| **Period** | Possible precursor at Caral, c. 2600–2000 BCE, **disputed**; well-substantiated cord records associated with Wari, c. 600–1000 CE; canonical decimal Inka khipus principally c. 1400–1532 CE; extensive colonial continuation through the sixteenth and seventeenth centuries, with later local survivals and transformations into the nineteenth, twentieth, and twenty-first centuries. |
| **Region** | Central Andes: principally modern Peru, but within the Inka sphere also parts of Bolivia, Ecuador, northern Chile, north-western Argentina, and southern Colombia. |
| **Users** | Inka and local officials commonly called *khipukamayuq*—“one responsible for/expert in khipu”—plus colonial community authorities, witnesses, tribute administrators, and religious users. |
| **Status today** | The decimal knot notation is deciphered. Much categorical and nonnumerical information remains unread. Living communities preserve some historical khipus ritually, but no continuous community is known to retain a complete, generally readable version of the imperial code. |

**[Secure reading]** The numerical interpretation rests on surviving cords whose “summation” or top cords equal the sums of associated pendant cords. Locke demonstrated this with AMNH Bandelier specimen **B/87.13**, from Huando north of Lima, in 1912. The agreement supplies an internal check rather than depending only on colonial testimony. [Locke’s original article](https://en.wikisource.org/wiki/The_Ancient_Quipu,_a_Peruvian_Knot_Record); [JSTOR record](https://www.jstor.org/stable/659935); [Smithsonian history of Locke’s work](https://www.si.edu/object/book-ancient-quipu-or-peruvian-knot-record%3Anmah_1590977).

---

## The system in detail

### 1. The physical document

A canonical Inka khipu is not one “number written in string.” It is a structured textile document:

```text
PRIMARY CORD ──────────────────────────────────────
                 │         │            │
              pendant   pendant      pendant
                 │         └── subsidiary
                 │                 └── sub-subsidiary
                 └── knot groups arranged by decimal height
```

**[Artefact]** Surviving examples commonly have:

- a thicker **primary cord**;
- pendant cords attached by a looped hitch;
- occasional **top cords**, projecting in the opposite direction;
- **subsidiary cords** attached to pendants or other subsidiaries;
- groups separated by gaps or repeated color sequences;
- cotton and camelid fiber, natural or dyed;
- S- or Z-spun components, S- or Z-ply, recto or verso attachment, and differently directed knots.

Locke described primary cords from a few centimetres to a metre or more, pendants usually under half a metre, and extant khipus with anything from a few to more than one hundred pendants. Larger and more complicated examples are now known. [Locke, lines 131–158](https://en.wikisource.org/wiki/The_Ancient_Quipu,_a_Peruvian_Knot_Record).

**[Scholarly reconstruction]** The cord hierarchy could express relationships such as category → subcategory → item, household → subgroup → community, or component → subtotal → total. It should not be assumed that “one cord always means one person” or that every subsidiary is a decimal fraction of its parent.

### 2. The signs

There is no Indigenous graphic font for khipu knots, and Unicode contains no canonical khipu numeral characters. The following dossier notation is therefore explicitly a **modern transcription**:

| Modern transcription | Physical form | Canonical value |
|---|---|---:|
| `∅` | no knot in an expected decimal zone | 0 in that place |
| `E` | one figure-eight knot | 1 in the units place |
| `L2` … `L9` | one long knot with 2–9 turns | 2–9 in the units place |
| `S` | one single overhand knot | one unit of a non-units place |
| `SSS` | cluster of three single knots | digit 3 in that place |

“Drawn in words”:

- **Single knot:** make an ordinary overhand loop and pull the end through once.
- **Long knot:** begin an overhand knot, pass the free end repeatedly through the loop, then tighten; the resulting knot is an elongated coil. Its turns carry the value.
- **Figure-eight knot:** the cord crosses itself in the familiar shape of the numeral 8 before tightening.
- **Zero:** leave the relevant position unknotted.

**[Secure reading]** The canonical rule is:

- units 1 → `E`;
- units 2–9 → `L2` through `L9`;
- tens and higher digits → that many separate single knots;
- zero → no knot at the relevant height.

Chrisomalis explains an important design advantage: a long or figure-eight knot marks the bottom units position, reducing ambiguity over whether a final group of ordinary single knots means units, tens, or hundreds. [Chrisomalis, *Numerical Notation*, pp. 311–13](https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20(CUP,%202010)(ISBN%200521878187)(O)(498s)_MPop_.pdf).

**[Qualification]** This is the “Lockean” or canonical decimal typology. Real khipus contain anomalies: long or figure-eight knots sometimes occur outside their expected position, extra “nether” knots may occur below normal units, and some cords are damaged or structurally noncanonical. Such exceptions do not overturn the internally verified decimal corpus, but they warn against treating every knot on every Andean cord as an ordinary digit.

### 3. Place value and reading direction

On a pendant cord:

```text
attachment to primary cord
        │
        SSSS       4 thousands
        SS         2 hundreds
        ∅          0 tens
        L7         7 units
free end
```

This reads **4,207**.

Higher powers normally lie nearer the primary cord and units nearer the free end. On a top cord, because the cord projects in the opposite direction, the physical reading direction reverses.

A digit is additive within its zone:

\[
SSS_{\text{hundreds}}=1\cdot100+1\cdot100+1\cdot100=300.
\]

The whole cord is positional:

\[
SSS_{\text{hundreds}}+SSSS_{\text{tens}}+L5
=3\cdot100+4\cdot10+5=345.
\]

Thus the best typological formula is:

> **decimal place value × additive knot count within each place.**

It is not multiplicative in the manner of a written sign “3” followed by a separate sign “100,” and it is not a ciphered decimal notation with a unique glyph for every digit.

### 4. Zero and absence

**[Secure reading]** A missing knot in an expected decimal zone gives a **place-value zero**. Thus 102 has one hundred-knot, an empty tens zone, and a two-turn long units knot.

**[Important distinction]** An empty zone is not the same as an absent cord:

- a present cord with a recognized category/color but no knot may record a quantity of zero;
- the absence of the category’s cord may mean that the category itself was not included.

Marcia Ascher used the illustrative distinction “zero potatoes consumed by children” versus “no children/category represented.” The first can use a present but unknotted category cord; the second lacks the cord. [Ascher discussion reproduced here](https://www.slideshare.net/slideshow/marcia-ascher-ethnomathematicsbrooks-cole-publishing-1991-1/51838853).

**[Controversy]** Calling this “the invention of zero” overstates the evidence. Khipu have a zero-place convention and could record a zero count. That does not prove an abstract zero with all the algebraic properties formulated in Indian mathematics. Conversely, saying “the Inka had no zero because they had no zero glyph” is also false: a blank place functions as zero.

### 5. Table: 1 to 20

The diagrams show one pendant cord, from high place at left/top to units at right/bottom. `S₁₀` means a single knot in the tens zone; `E₁` and `Lx₁` are units knots.

| Number | Decimal-zone transcription | Knots in words |
|---:|---|---|
| 1 | `E₁` | one figure-eight unit knot |
| 2 | `L2₁` | one two-turn long unit knot |
| 3 | `L3₁` | one three-turn long unit knot |
| 4 | `L4₁` | one four-turn long unit knot |
| 5 | `L5₁` | one five-turn long unit knot |
| 6 | `L6₁` | one six-turn long unit knot |
| 7 | `L7₁` | one seven-turn long unit knot |
| 8 | `L8₁` | one eight-turn long unit knot |
| 9 | `L9₁` | one nine-turn long unit knot |
| 10 | `S₁₀ · ∅₁` | one single tens knot; empty units |
| 11 | `S₁₀ · E₁` | one tens knot; figure-eight unit knot |
| 12 | `S₁₀ · L2₁` | one tens knot; two-turn unit knot |
| 13 | `S₁₀ · L3₁` | one tens knot; three-turn unit knot |
| 14 | `S₁₀ · L4₁` | one tens knot; four-turn unit knot |
| 15 | `S₁₀ · L5₁` | one tens knot; five-turn unit knot |
| 16 | `S₁₀ · L6₁` | one tens knot; six-turn unit knot |
| 17 | `S₁₀ · L7₁` | one tens knot; seven-turn unit knot |
| 18 | `S₁₀ · L8₁` | one tens knot; eight-turn unit knot |
| 19 | `S₁₀ · L9₁` | one tens knot; nine-turn unit knot |
| 20 | `SS₁₀ · ∅₁` | two single tens knots; empty units |

Quechua forms vary by language and modern orthography. In Southern Quechua a representative sequence is:

`huk, iskay, kimsa, tawa, pichqa, suqta, qanchis, pusaq, isqun, chunka, chunka hukniyuq … iskay chunka`.

**[Documented linguistic structure]** The spoken numeral system combines decimal multiplication and addition: “two ten” = 20, “ten having one” = 11. [INALCO survey](https://www.inalco.fr/en/quechua-oral-numeration-and-its-writing-quipus).

### 6. Tens, hundreds, thousands, and higher powers

| Number | Khipu transcription | Representative Quechua term |
|---:|---|---|
| 10 | `S₁₀ · ∅₁` | *chunka* |
| 20 | `SS₁₀ · ∅₁` | *iskay chunka* |
| 30 | `SSS₁₀ · ∅₁` | *kimsa chunka* |
| 40 | `SSSS₁₀ · ∅₁` | *tawa chunka* |
| 50 | `SSSSS₁₀ · ∅₁` | *pichqa chunka* |
| 60 | `SSSSSS₁₀ · ∅₁` | *suqta chunka* |
| 70 | `SSSSSSS₁₀ · ∅₁` | *qanchis chunka* |
| 80 | `SSSSSSSS₁₀ · ∅₁` | *pusaq chunka* |
| 90 | `SSSSSSSSS₁₀ · ∅₁` | *isqun chunka* |
| 100 | `S₁₀₀ · ∅₁₀ · ∅₁` | *pachak* |
| 1,000 | `S₁₀₀₀ · ∅₁₀₀ · ∅₁₀ · ∅₁` | *waranqa* |
| 10,000 | `S₁₀₀₀₀ · … · ∅₁` | often *chunka waranqa* |
| 100,000 | `S₁₀₀₀₀₀ · … · ∅₁` | *pachak waranqa* |
| 1,000,000 | `S₁₀⁶ · … · ∅₁` | commonly *hunu* in later Quechua sources |

**[Disputed terminology]** Early sources do not give a perfectly consistent magnitude for *hunu*: it may mean ten thousand in some contexts and one million in others. Dialect, period, and administrative usage must be specified. It is unsafe to project one modern standardized vocabulary unchanged into the imperial past. [INALCO discussion](https://www.inalco.fr/la-numeration-orale-quechua-et-son-ecriture-dans-les-quipus).

### 7. Famous and diagnostic numbers

#### 135: Locke’s demonstrative pendant

```text
primary
  │
  S          hundreds = 100
  SSS        tens     =  30
  L5         units    =   5
  │
 free end
TOTAL = 135
```

**[Artefact / secure reading]** Locke’s plate includes a pendant encoding 135 and uses it while explaining the knot types. [American Mathematical Society exposition](https://www.ams.org/publicoutreach/feature-column/fc-2014-05).

#### 102: internal zero

```text
S₁₀₀ · ∅₁₀ · L2₁ = 102
```

It proves why “no knot” must be read positionally rather than as “nothing was written.”

#### 620: terminal-zero diagnostic

```text
SSSSSS₁₀₀ · SS₁₀ · ∅₁ = 620
```

Six single knots followed by two single knots cannot canonically mean 62, because the units digit 2 would have to be a two-turn long knot. The single-knot ending therefore signals that the final cluster belongs above the units place and that a terminal zero follows. [Chrisomalis, pp. 311–13](https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20(CUP,%202010)(ISBN%200521878187)(O)(498s)_MPop_.pdf).

#### 776 = 360 + 23 + 102 + 291

Chrisomalis’s diagram is explicitly **unattested but plausible**, synthesized to show documented relationships:

```text
P1 = 360
P2 =  23
P3 = 102
P4 = 291
          ───
top cord = 776
```

Its subsidiary relation is likewise:

```text
20 + 6 = 26
```

**[Modern scholarly diagram, not an artefact]** It faithfully illustrates structures found on actual khipus but must not be called a surviving famous Inka document. [Chrisomalis, figure 10.2](https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20(CUP,%202010)(ISBN%200521878187)(O)(498s)_MPop_.pdf).

#### The Santa Valley count: 132 people in 133 groups

**[Document-and-object match, probable but not uniquely proved]** A Spanish *revisita* of 1670 lists 132 tributaries in six *pachacas*, naming 130 and noting two absences. Six Santa Valley khipus contain 133 color-coded six-cord groups. Values on the first cords total the tribute assessed by the written record. Medrano and Urton therefore proposed that the two media came from the same administrative procedure. [Article and abstract](https://www.researchgate.net/publication/322809850_Toward_the_Decipherment_of_a_Set_of_Mid-Colonial_Khipus_from_the_Santa_Valley_Coastal_Peru).

### 8. Fractions

**[Negative finding]** No securely identified canonical knot sign means “½,” “⅓,” a decimal point, numerator, denominator, or fraction bar.

**[Scholarly reconstruction]** The Aschers found numerical relations consistent with:

- division into equal portions;
- unequal proportional partition;
- multiplication of integers by integers;
- multiplication by fractional proportions.

Those relations exist between recorded integers. They show proportional arithmetic, but not a written fractional notation. A useful summary explicitly concludes that fractional values were handled through partition and ratio although “fractions cannot be encoded on the quipus” in any securely deciphered direct notation. [History and Science of Knots summary](https://online.flipbuilder.com/juwl/yomg/files/basic-html/page92.html).

### 9. Largest expressible number

**[Structural conclusion]** There is no known fixed maximum. In principle, another decimal zone can be placed nearer the attachment, so capacity is limited physically by cord length, distinguishable spacing, and practical use—not by a highest sign.

**[Documented language, qualified]** Quechua possessed terms for large decimal groupings, including *waranqa* and *hunu*, but historical values of *hunu* vary. Modern lists extending the vocabulary to extremely large powers should not be treated automatically as imperial evidence.

**[Artefact]** Surviving khipus record numbers into at least the tens of thousands. Claims of a single definitive “largest Inka khipu number” are not well founded because:

- many objects lack provenance;
- some cords are damaged;
- the highest unknotted places cannot be recovered;
- an apparent number may instead be a label;
- the corpus continues to change.

### 10. Ligatures and abbreviations

The written-numeral categories “ligature” and “abbreviation” fit poorly.

- A long knot compresses two to nine unit knots into one multi-turn knot; functionally it is a compact digit sign.
- Color series can repeat rather than restating a category in words.
- Subsidiaries spatially nest information instead of repeating a heading.
- Top or summation cords compress many entries into totals.
- Some number sequences may be **labels**, identifiers, or place names rather than quantities.

**[Disputed]** Brezine proposed that a recurring three-number sequence on Puruchuco khipus may identify Puruchuco, popularly compared to a ZIP code. It is a contextual identification, not a universally accepted phonetic reading.

---

## Origins: dated and placed

### Before khipu: knots, textiles, and accounting

**[Scholarly reconstruction]** Knotted cords occur in many societies and need not descend from one invention. Locke himself warned that reckoning by knots could arise wherever spinning and weaving existed. Chinese traditions of knotted records therefore do not establish trans-Pacific ancestry. No evidence links khipu genetically to Mesopotamian tokens, Egyptian numerals, Indian zero, Chinese rods, Maya numerals, the Ishango bone, or the Lebombo tally.

The broad comparative items named in the general template—Uruk tokens, Narmer, Bakhshali, Gwalior, Brahmi numerals, Dresden Codex—belong to other numeral histories. **Absence of evidence is the relevant result here:** none is an ancestor or demonstrable donor to the Andean khipu system.

### c. 2600–2000 BCE: Caral

**[Artefact, disputed identification]** Excavators at the Late Preceramic complex of Caral in Peru’s Supe Valley reported twelve cotton strings twisted around sticks and called them an early khipu. The site itself has strong radiocarbon chronology: monumental occupation falls broadly in the later third millennium BCE. [Caral radiocarbon study](https://pubmed.ncbi.nlm.nih.gov/11326098/).

**[Disputed]** The identification is not established because the object’s full data and detailed publication were unavailable when Chrisomalis assessed it; a bundle of strings is not by itself proof of a numerical cord record. Chrisomalis calls the claim “unsubstantiated.” [Chrisomalis, p. 312](https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20(CUP,%202010)(ISBN%200521878187)(O)(498s)_MPop_.pdf).

**Conclusion:** Caral is the earliest claimed ancestor, not the earliest securely readable khipu.

### c. 200–600 CE: possible Moche imagery

**[Scholarly suggestion]** Wendell Bennett noted marks on Moche vessels that resemble khipu. Resemblance in ceramic imagery cannot establish that the depicted strings used decimal place value. This remains an antecedent hypothesis rather than a deciphered attestation.

### c. 600–1000 CE: Wari cord records

**[Artefact]** The first well-substantiated khipu-like records come from Middle Horizon contexts associated with Wari. They share the basic cord-record architecture but differ from canonical Inka khipus in wrapping, coloring, and knot patterning.

Urton reported a group of eight late Middle Horizon khipus and AMS dates for four. Their knots cluster notably in fives, leading him to suggest a **base-five Wari system**. [Urton, *Antiquity*](https://www.cambridge.org/core/journals/antiquity/article/abs/from-middle-horizon-cordkeeping-to-the-rise-of-inka-khipus-in-the-central-andes/04964C31803194A5EA0F1565617F00C9).

**[Disputed reconstruction]** “Wari used base five” is plausible from clustering but not a decipherment comparable to the Inka decimal reading. The specimens are deteriorated, and no Wari bilingual or total cord fixes the values.

One AMNH Wari object is catalogued as **41.2/7678**. [AMNH digital collection](https://digitalcollections.amnh.org/C.aspx?IID=2URM1THGVJ3M&PN=18&VBID=&VF=DamViewDetailPopup&VP3=CMS3).

### c. 1000–1400 CE: transition

**[Open archaeological interval]** The developmental route from Wari cord-keeping to the Inka canonical khipu is not documented by a continuous, well-provenanced series. The Inka may have inherited and standardized older Andean practices, but “the Inka copied Wari decimal notation” is not demonstrated—especially because Wari objects may have operated differently.

No securely demonstrated foreign donor is known. The safest origin model is **indigenous Andean development within textile, tribute, and administrative traditions**.

### c. 1400–1532: imperial standardization

**[Artefact and reconstruction]** Most canonical decimal specimens belong stylistically to the Inka Late Horizon. They show considerable standardization in decimal knot placement while varying in material organization.

**[Documented administrative context]** The empire organized labor, populations, storage, military obligations, and officials through nested decimal categories described by colonial witnesses: groups nominally associated with 10, 100, 1,000, and 10,000 households. These social groupings were not necessarily exact demographic blocks at every time and place.

### 1533: first European encounter in writing

**[Documented text]** Hernando Pizarro’s 1533 letter records an encounter in which an Andean official used knots to account for what had been brought to a storehouse. It is generally treated as the earliest surviving European eyewitness notice of khipu, only months after Cajamarca. [Historical text portal](https://faculty.chass.ncsu.edu/slatta/hi216/documents/pizarro.htm).

This testimony proves contemporary administrative use. It does not decipher individual knot forms.

---

## Arithmetic and instruments

### Record versus calculator

The khipu is best understood primarily as a **recording, organizing, checking, and transmitting medium**. It is not established that users performed every intermediate calculation by manipulating knots.

**[Documented texts]** Colonial observers describe calculations with stones or maize kernels:

- José de Acosta, *Historia natural y moral de las Indias* (1590), reports experts putting one grain here, three there, moving grains, and emerging from difficult accounts without error.
- Garcilaso says accounts were made with small stones and obtained with striking exactness.
- Guaman Poma says they counted on boards from hundred-thousands and ten-thousands down to one.

The passages are conveniently assembled in a modern history of yupana studies. [Scielo article](https://www.scielo.org.pe/scielo.php?pid=S2219-71682023000100086&script=sci_arttext); [Acosta’s 1590 text](https://www.gutenberg.org/cache/epub/70219/pg70219-images.html).

### The yupana

*Yupana* derives from Quechua *yupay*, “to count/reckon.” The term is now applied to compartmented Andean boards and to the checkerboard drawn beside Guaman Poma’s chief accountant.

**[Documented image]** Guaman Poma’s autograph *Nueva corónica y buen gobierno*, c. 1615/16, depicts the **“contador mayor y tesorero”** holding a khipu beside a 5×4 spotted checkerboard. The manuscript is Copenhagen, Royal Danish Library **GKS 2232 4°**. [Royal Library facsimile portal](https://poma.kb.dk/).

**[Artefact]** Compartmented stone and wooden boards survive, including examples conventionally called yupanas. Their exact function is not demonstrated merely by their shape. [Museo de Arte de Lima object page](https://artsandculture.google.com/asset/yupana-inca-style/qgHcj1oAkruUHg?hl=en).

**[Scholarly reconstruction, disputed]** Numerous modern algorithms assign different weights to the compartments—decimal, mixed-base, Fibonacci-like, or other patterns. Several can perform arithmetic, but showing that an algorithm works on the board does not prove that an Inka accountant used it. No colonial manual gives the moves.

The most defensible reconstruction is:

1. arrange counters by place or category;
2. move and regroup kernels or stones to calculate;
3. transfer the result to a khipu;
4. use summation cords and duplicate accounts for checking.

### Operations recoverable from khipus

**[Secure reading]**

- **Addition:** many total cords equal sums of associated pendants.
- **Hierarchical summation:** local totals can become entries in a higher-level khipu.
- **Duplicate checking:** khipus at the same administrative level sometimes repeat the same values and color patterns.

**[Scholarly reconstruction]**

- subtraction from declining inventory;
- multiplication as repeated groups;
- equal and unequal division;
- proportional allocation;
- fractions handled as relations between whole-number entries.

There are no surviving Inka arithmetic textbooks comparable to the Rhind Mathematical Papyrus, *Nine Chapters*, Brahmagupta, al-Khwarizmi, or Fibonacci. **[Negative finding]** No worked khipu manual, named Inka theorem, or step-by-step yupana algorithm survives.

### Puruchuco: arithmetic through a bureaucracy

**[Artefact]** Twenty-one khipus were discovered in 1956 in an urn beneath the floor of a building adjoining the Inka palace at Puruchuco, about 11.5 km north-east of central Lima. Carol Mackey proposed that the building was a khipu keeper’s residence.

**[Secure numerical relationship / reconstructed administration]** Urton and Carrie Brezine’s 2005 analysis linked seven khipus in three levels:

- Level I: UR63 and UR73;
- Level II: UR64, UR68, and museum specimen no. 9;
- Level III: UR66 and UR67.

Accounts at one level substantially sum into those above; same-level examples match or nearly match, while groupings become increasingly aggregated. UR66 and UR67 were bundled together and carry identical numerical values with coordinated colors.

This strongly supports upward aggregation, downward partition, and redundant checking. Whether the flow represented labor tribute, goods, or another account remains inferential. [Original *Science* record](https://pubmed.ncbi.nlm.nih.gov/16099983/); [detailed exposition](https://repositoriodigital.bnp.gob.pe/bnp/recursos/2/html/el-imperio-inka/296/).

### Inkawasi storehouse archive

**[Artefact]** Excavation of an Inka storage installation at Inkawasi produced 34 khipus in archaeological association with stored agricultural products. This is especially important because most museum khipus were collected without precise context. [Urton and Chu, *Latin American Antiquity*](https://www.cambridge.org/core/journals/latin-american-antiquity/article/accounting-in-the-kings-storehouse-the-inkawasi-khipu-archive/417CED6AB7ED0F6D37DC7A3E84F698D5).

**[Scholarly reconstruction]** Numerical regularities may reflect commodity batches, standardized accounting units, deductions, seed retention, or tribute. The archaeological association supports storehouse accounting, but it does not identify every colored cord with a particular crop.

### Finger reckoning

**[Negative finding]** Quechua *ruki* and related bodily counting terminology merit linguistic study, but there is no comparably detailed early description of a standardized imperial finger-reckoning method. Claims assigning fixed values to every finger joint should be treated as modern reconstruction unless tied to a specific ethnographic source.

---

## Transmission and replacement

### Inside Tawantinsuyu

**[Documented and reconstructed]** Khipus circulated through an empire connected by roads, storehouses, provincial centers, and messenger relays. Local khipukamayuq compiled figures; higher officials received aggregates. Puruchuco supplies material confirmation of tiered accounting, though it does not prove a single empire-wide route for every record.

Khipus were not necessarily “read aloud directly” without context. Color, cord order, administrative category, accompanying messenger, and trained memory could cooperate.

### Early Spanish rule, 1530s–1560s

**[Documented text]** Spaniards initially depended on Indigenous accountants for censuses, tribute, labor, supplies, and historical testimony. Courts accepted khipu-based statements when a khipukamayuq interpreted them orally.

A major 1561 proceeding heard khipukamayuq testimony over many days and cross-examined Indigenous elites, conquistadors, and officials. [French demographic study](https://www.persee.fr/doc/pop_0032-4663_1998_num_53_1_6849).

**[Legal fact]** Khipus could function as evidence in practice even though the Council of the Indies did not issue a general authorization making them equivalent to Castilian written instruments. [Cambridge history of colonial law](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6D953D4F0BEFC1A7C213F45216EC06E1/9781316518045c4_141-249.pdf/how_to_approach_colonial_law.pdf).

### Translation into paper

**[Documented practice]** Khipu readings were dictated into Spanish documents. Such “paper khipus” preserve the categories and verbal formulas of performances but usually not a one-to-one map from cord to phrase.

This process both preserved information and displaced authority:

```text
cord archive → oral interpretation → notarial Spanish text
```

At each transition, information could be reordered, translated, omitted, or adapted to colonial fiscal concepts.

### Church use and suppression

The history is contradictory, not a simple story of immediate destruction.

**[Documented use]** Missionaries encouraged converts to make personal khipus to remember sins before confession and used khipu boards to track Easter confession and communion obligations. [Hyland, “Unreliable Confessions”](https://www.cambridge.org/core/journals/americas/article/abs/unreliable-confessions-khipus-in-the-colonial-parish/FC2D07D0803C674C1DEAF65D95AC1C14); [khipu boards study](https://doi.org/10.25222/larr.1032).

**[Documented suppression]** The Third Council of Lima, 1582–83, ordered the destruction of khipus containing records of non-Christian rites, ceremonies, and laws regarded as “ancient superstition.” This was targeted religious suppression; it did not mean every numerical tax khipu was burned everywhere.

**[Myth corrected]** “The Spaniards burned all khipus on arrival” is false. Colonial officials used them, courts admitted their interpreted contents, priests adapted them, and communities continued producing them. Destruction was nevertheless real and materially damaging, particularly where records were classified as idolatrous.

### Seventeenth century

Khipu production and courtroom visibility declined from the late sixteenth century and markedly after the mid-seventeenth, while alphabetic records increasingly dominated. Yet the 1670 Santa Valley case proves sophisticated Inka-style accounting well into colonial rule.

### Eighteenth and nineteenth centuries

**[Documented colonial survivals]** Cord messages and community records continued in some regions. Hybrid khipu/alphabetic boards joined cords to written personal names or parish registers. Rebellion-era khipu “letters” reported in central Peru are central to the modern phonetic debate.

### Twentieth century to the present

**[Ethnographic documentation]** Communities retained several transformed cord traditions:

- herding and livestock counts;
- labor and office records;
- ritual or patrimonial khipus;
- khipu boards recording communal or religious obligations.

At San Andrés de Tupicocha, Huarochirí, historical *quipocamayos* are displayed and wrapped around authorities during annual ceremonies. Paper now carries active accounts, while the old cords serve as authoritative prototypes and symbols of ayllu continuity. [Salomon’s study](https://www.degruyterbrill.com/document/doi/10.7560/769038-014/html).

In 2019 Peru declared the ritual and social use of Tupicocha’s khipus part of the nation’s cultural heritage. [Peruvian Ministry of Culture resolution](https://www.gob.pe/institucion/cultura/normas-legales/391137-rvm-n-236-2019-vmpcic-mc).

**[Qualification]** This is genuine cultural survival, but not proof that Tupicocha residents can read every imperial Inka khipu.

---

## People

### Khipukamayuq

**[Documented institution]** The word combines *khipu* with *kamayuq*, a person possessing a particular charge, expertise, or responsibility. “Knot keeper,” “cord keeper,” “accountant,” and “khipu specialist” are better contextual translations than the narrower “scribe.”

Colonial witnesses describe multiple keepers checking one another’s accounts, specialists attached to provinces and storehouses, and historical informants consulting khipus.

### Hernando Pizarro, c. 1502–1578

Spanish conquistador and author of the 1533 letter containing the earliest surviving European eyewitness description of an Andean official accounting by knots.

### Pedro Cieza de León, c. 1520–1554

**[Documented text]** His chronicles describe provincial accounting and people charged with keeping accounts. His evidence is near-contemporary but filtered through Spanish concepts of history, writing, and government.

### Juan Polo de Ondegardo, died 1575

Colonial official who investigated Inka institutions and used khipukamayuq testimony in reconstructing tribute, religion, and law. His reports are indispensable but were produced within a colonial project of governance.

### José de Acosta, 1540–1600

Jesuit author of the 1590 *Historia natural y moral de las Indias*. He admired the accuracy of Indigenous calculations performed with grains while interpreting the practice through European missionary categories.

### Inca Garcilaso de la Vega, 1539–1616

Born in Cusco to a Spanish father and Inka noble mother; left Peru at about twenty. His *Comentarios reales* (1609) gives the clearest colonial verbal account of decimal place order: higher numbers nearer the top, descending through decimal ranks.

**[Documented testimony, not neutral eyewitness record]** Garcilaso grew up near living Inka traditions and claimed Indigenous knowledge, but wrote decades later in Spain, within Renaissance historiography. Locke treated him as the most reliable colonial interpreter; modern historians use him critically rather than literally. [Spanish text](https://biblioteca.clacso.edu.ar/clacso/se/20190904032639/Comentarios_reales_2_Inca_Garcilaso_de_la_Vega.pdf).

### Felipe Guaman Poma de Ayala, c. 1535–after 1616

Indigenous Andean author and artist of *El primer nueva corónica y buen gobierno*. His drawing of the chief accountant, khipu, and spotted board is the most famous image connecting record and calculation. [Royal Danish Library manuscript](https://poma.kb.dk/).

### Leland L. Locke, 1875–1943

A mathematics teacher and historian of calculating instruments. In 1912 he decoded the decimal numerical structure of AMNH khipus; in 1923 he expanded the work into *The Ancient Quipu or Peruvian Knot Record*, cataloguing 45 supposed specimens and rejecting five as modern or spurious.

**[Historiography]** Locke concluded too strongly that authentic khipus were purely numerical, but his decimal reading survives because the internal sums test it. [Smithsonian biography and book record](https://www.si.edu/object/book-ancient-quipu-or-peruvian-knot-record%3Anmah_1590977).

### Carlos Radicati di Primeglio, 1914–1990

Developed twentieth-century analysis of khipu structure, numerical classes, and yupana. His work helped reopen questions that Locke’s exclusively numerical conclusion had closed.

### Marcia Ascher, 1935–2013, and Robert Ascher, 1931–2014

Mathematician and anthropologist. Their 1969 *Nature* paper argued that khipu coding was richer than simple digit storage. Their databooks described 191 objects, and *Code of the Quipu* (1981; revised as *Mathematics of the Incas*, 1997) analyzed spatial hierarchy, arithmetic relations, labels, and cultural logic. [1969 paper](https://www.nature.com/articles/222529a0); [Cornell databook portal referenced here](https://www.gresham.ac.uk/sites/default/files/transcript/2021-10-20-1600_MEDRANO_BSHM-T.pdf).

### William J. Conklin

Analyzed Wari cord records and their thread-wrapped construction, providing the foundation for treating them as genuine pre-Inka antecedents.

### Frank Salomon, born 1946

Ethnohistorian and ethnographer of modern and colonial Andean cord-keeping, especially Tupicocha. He emphasizes khipu as socially performed authority rather than merely a storage technology.

### Gary Urton, born 1946

Proposed systematic binary dimensions in khipu construction in *Signs of the Inka Khipu* (2003), founded the Harvard Khipu Database Project, and coauthored the Puruchuco and Santa Valley studies.

**[Disputed theory]** His binary model remains influential as a cataloguing and hypothesis-generating framework, but the proposed combinations have not yielded a generally readable lexicon.

### Carrie J. Brezine

Mathematician, textile specialist, and database designer. She built the computational infrastructure of the Harvard Khipu Database and coauthored the 2005 Puruchuco hierarchy study. The present Open Khipu Repository retains her in its advisory structure.

### Sabine Hyland

Anthropologist working with colonial and community khipus. Her work on hybrid alphabetic/khipu boards found a statistically meaningful relation between knot direction and social moiety. Her later Collata interpretation proposes phonetic or logosyllabic readings of cord combinations.

### Manuel Medrano

Historian and khipu researcher, coauthor of the 2018 Santa Valley census match and analyst of colonial “paper khipus.” His work stresses correspondence between cords and alphabetic administrative records.

### Museums and collections

Important holdings include the American Museum of Natural History, Museo Nacional de Arqueología, Antropología e Historia del Perú, Museo de Sitio Arturo Jiménez Borja–Puruchuco, Museo de Arte de Lima, Museo Larco, Ethnologisches Museum Berlin, Peabody Museum, Musée du quai Branly, and numerous regional or community collections.

**[Caution]** Most old museum specimens lack secure excavation context. Catalogue number is evidence of present custody, not proof of date or provenance.

---

## Culture

### Government and labor

Khipus recorded or supported the administration of:

- tribute;
- labor service;
- censuses;
- storehouse inventories;
- herds;
- military levies;
- land and community divisions;
- calendrical or ritual obligations.

**[Secure versus reconstructed]** Numerical accounting is secure. Assigning a particular object to “tax,” “army,” or “potatoes” without archaeological or documentary linkage is reconstruction.

### Law

Khipus entered colonial litigation through expert performance. A khipukamayuq presented the cords, explained their categories, and testified to their contents; Spanish notaries converted the testimony into alphabetic records.

The khipu was therefore simultaneously:

- an archive;
- a prompt for oral evidence;
- a claim to Indigenous expertise;
- an object whose credibility colonial judges negotiated.

### Religion and liturgy

Christian authorities used cords for confession preparation and parish compliance while destroying cords associated with pre-Christian ritual. This ambivalence shows that the medium itself was not always prohibited; its authorized or unauthorized content mattered.

### Calendars

**[Documented tradition]** Colonial writers associate khipu specialists with calendrical reckoning.

**[Disputed]** Individual extant “calendar khipus” are rarely demonstrable. The so-called Pachaquipu in the Miccinelli documents claims to reproduce the conquest-year calendar, but the Miccinelli manuscripts’ provenance and authenticity have been heavily disputed. It cannot serve as a secure decipherment key. [Pachaquipu proposal](https://arxiv.org/abs/0801.1577).

### Literature, histories, and songs

Garcilaso, Cieza, Guaman Poma, Bernabé Cobo, and other colonial writers say khipus aided the preservation of royal genealogies, historical events, laws, poems, or songs.

That testimony permits at least three models:

1. **Mnemonic model:** knots cue a memorized oral performance.
2. **Semasiographic model:** cords encode concepts and categories without mapping systematically to spoken words.
3. **Writing model:** some configurations encode language, perhaps including sounds or syllables.

No model has yet been proved for the entire corpus. Khipus could also have had different genres using different degrees of linguistic encoding.

### Textile aesthetics and authority

A khipu communicates by more than knots. Color alternation, tactile fiber, cord thickness, spin and ply, branching, and display create a document that is:

- visible;
- touch-readable;
- three-dimensional;
- rearrangeable in the hands;
- worn or ceremonially displayed.

Its textile nature tied information to highly developed Andean weaving traditions. Calling it merely a “string abacus” conceals this material sophistication.

### Number words and descendants

Unlike Hindu-Arabic numerals, khipu did not transmit international words such as *zero*, *cipher*, or *algorithm*. Its important lexical descendants are Quechua and Andean Spanish:

- *khipu/quipu* — knot, record;
- *khipukamayuq/quipucamayoc* — responsible expert or keeper;
- *yupay* — count, reckon;
- *yupana* — modern scholarly name for an Andean counting board.

### Modern art, computing, and metaphor

**[Modern invention]** Artists and digital-humanities projects use khipu as a model for relational data, memory, decolonial archives, and tactile writing. These works continue the cultural life of the object but are not deciphered Inka texts.

The Harvard Khipu Database developed into a major comparative corpus. The present **Open Khipu Repository** is administered by the Open Khipu Research Laboratory and overseen by an advisory board including Brezine, FitzPatrick, Ghezzi, Hyland, Medrano, and Splitstoser. [Open Khipu Repository data release](https://doi.org/10.5281/zenodo.18025748).

**[Requested namesake note; absence of verification]** Extensive searches found no reliable primary source documenting “the Colegio Invisible’s own quipu inscriptions on Dogecoin.” It should therefore be recorded only as an **unverified modern claim**, not as part of khipu history, unless an inscription ID, transaction hash, or issuer’s source is supplied.

---

## Controversies and disputes

### 1. Was Caral’s string bundle a khipu?

**For:** the object comes from an exceptionally early complex society where administration is plausible; its excavators identify it as a khipu precursor.

**Against:** full technical publication and a readable knot structure were lacking; strings wound around sticks need not be a numerical document.

**Finding:** earliest claimed example, c. third millennium BCE; not the earliest secure numerical khipu.

### 2. Wari base five or precursor decimal?

**For base five:** repeated five-knot clustering in dated Middle Horizon objects.

**Against a firm decipherment:** deterioration, limited sample, and absence of checking totals or a bilingual key.

**Finding:** Wari cord-keeping is archaeologically real; its exact numeration remains reconstructed.

### 3. Did the Inka “invent zero”?

**For:** empty decimal positions behave exactly as zero placeholders, including internal and terminal zeros.

**Against the broad claim:** there is no separate zero glyph and no surviving Inka algebraic text treating zero as a number with explicit operational rules.

**Finding:** secure place-value zero; abstract numerical zero not directly documented.

### 4. Are khipus writing?

**Numerical minimum:** some unquestionably encode decimal numbers.

**Mnemonic position:** colonial “histories” may have been memorized speeches prompted by numbers, colors, and categories.

**Semasiographic position:** structural signs may encode persons, classes, moieties, commodities, or actions without representing Quechua sounds.

**Linguistic position:** some colonial khipus may use rebus, logosyllabic, or phonetic strategies.

**Finding:** “khipu is writing” and “khipu is not writing” are both too categorical. The corpus may include several genres and historical stages.

### 5. Urton’s binary code

In 2003 Urton proposed paired choices in material construction: cotton/camelid fiber, S/Z spin or ply, attachment direction, knot direction, and other marked/unmarked alternatives. Combined with color, he estimated a large sign capacity, often popularized as **1,536 possible signs**.

**Evidence for:**

- the material distinctions are real;
- some occur nonrandomly;
- later work links attachment or knot direction to moiety categories;
- imperial administration would benefit from shared conventions.

**Evidence against a completed decipherment:**

- not every proposed binary variable is present or reliably recorded;
- the variables may have different meanings by genre;
- theoretical capacity is not proof that all combinations were signs;
- no vocabulary of 1,536 meanings has been read;
- “seven-bit Inka computer code” is a modern analogy, not an Indigenous description.

**Finding:** productive structural hypothesis, not a decoded binary language. [Urton book record](https://www.jstor.org/stable/10.7560/785397); [contemporary account](https://www.abc.net.au/science/articles/2003/07/03/893964.htm?site=sci&topic=latest).

### 6. Puruchuco’s hierarchy

**For:** matching colors and numerical sequences; systematic sums between levels; duplicate high-level accounts; common archaeological cache.

**Qualification:** some totals differ slightly and may involve rounding, averaging, correction, damage, or different accounting moments.

**Finding:** strong evidence for hierarchical accounting, weaker evidence for the particular commodity or direction of information flow.

### 7. The Santa Valley “Rosetta khipus”

**For:**

- six *pachacas* in the 1670 census and six khipus;
- 132 tributaries, while the cords form 133 six-cord groups;
- first-cord totals agree with assessed tribute;
- attachment differences correspond plausibly to upper/lower social moieties.

**Against certainty:**

- the khipus were reportedly recovered from a burial rather than excavated under modern controls;
- 133 groups do not exactly equal 132 tributaries;
- numerical coincidence does not establish every name-to-cord mapping;
- later work proposes a different optimal moiety alignment;
- colors proposed as personal-name signs remain undeciphered.

**Finding:** among the strongest document-object correlations, but not a word-for-word bilingual. [2018 article](https://www.researchgate.net/publication/322809850_Toward_the_Decipherment_of_a_Set_of_Mid-Colonial_Khipus_from_the_Santa_Valley_Coastal_Peru).

### 8. Hyland’s Collata phonetic interpretation

Two eighteenth-century epistolary khipus preserved at San Juan de Collata were locally said to be letters connected with rebellion. Hyland proposed that combinations of colored animal fiber, ply, and other features represented ayllu names through phonetic or logosyllabic rebus principles.

**Supporting evidence:**

- community testimony identifies them as letters;
- their structure is unlike a normal decimal ledger;
- cord endings plausibly behave as sender “signatures”;
- hybrid alphabetic/khipu documents independently prove that cord features could correspond to named social units;
- knot direction has been statistically linked to Hanan/Urin moieties in a hybrid text. [Hyland, Ware, and Clark](https://www.cambridge.org/core/journals/latin-american-antiquity/article/abs/knot-direction-in-a-khipualphabetic-text-from-the-central-andes/C7898F2731F82777C595F599909745B5).

**Objections:**

- the proposed sound values are derived from very few correspondences;
- the epistolary khipus are colonial, not securely imperial;
- community explanations were recorded long after manufacture;
- no independent complete reading predicts a previously unknown passage;
- the system could be locally innovative or influenced by alphabetic literacy.

**Finding:** serious, testable evidence for linguistic content in some colonial khipus; not yet a general decipherment of Inka khipu.

### 9. Color dictionaries

Colonial sources and later summaries sometimes state “red = war,” “yellow = gold,” “white = peace,” and so forth.

**Evidence:** suggestive color associations are reported historically, and repeated color series visibly organize records.

**Problem:** meanings change with context; a color could classify material, origin, status, gender, moiety, commodity, or document genre. No surviving universal imperial color dictionary exists.

**Finding:** colors carried information, but popular one-color/one-word charts are oversimplifications.

### 10. “Every village had four khipu keepers”

Garcilaso says multiple accountants kept parallel records so their results could be compared.

**Status:** documented colonial testimony, plausible in a system emphasizing redundancy, but not an archaeological census of staffing. “Exactly four in every village” should not be repeated as a statistically universal imperial regulation.

### 11. “The khipu was an abacus”

**For the analogy:** it records place-value numbers and belongs in histories of calculating instruments.

**Against literal identity:** knots are comparatively slow to tie and preserve results; colonial witnesses describe calculations with movable counters on boards.

**Finding:** ledger/archive plus verification device; probably paired with a counting board. “Textile abacus” is metaphorical.

### 12. “The Spaniards destroyed the code”

**Fact:** ecclesiastical authorities ordered destruction of idolatrous cords, and conquest disrupted trained institutions and archival continuity.

**Correction:** Spaniards also used khipukamayuq data, accepted it in court, transcribed it, and adapted khipus for Christian practice. Colonial Indigenous communities continued making them.

**Finding:** violent suppression and gradual replacement, not a single universal bonfire.

### 13. Miccinelli documents and Blas Valera

The manuscripts attributed to the Jesuit Blas Valera contain extraordinary claims about syllabic khipu and a calendar record.

**For:** internal sophistication and claimed early-seventeenth-century authorship.

**Against:** problematic provenance, late discovery, anomalous materials and contents, and longstanding allegations of modern fabrication.

**Finding:** disputed documents cannot establish the imperial code unless authenticity and provenance are independently resolved.

### 14. Etymology and spelling

*Khipu* reflects modern Quechua orthographies distinguishing an aspirated /kh/ in varieties where applicable; *quipu* is entrenched through Spanish colonial spelling.

**Myth:** spelling *khipu* is not a newly invented object distinct from *quipu*. They are orthographic forms of the same historical word.

### 15. “No writing in the Inka Empire”

This formula depends on the definition of writing.

- If writing must graphically represent language, the imperial khipu case remains unproved.
- If writing includes conventional durable notation of numbers and categories, khipu clearly qualifies as inscription.
- If writing includes semasiographic administrative records readable by trained specialists, many khipus probably qualify.

The safe statement is: **the Inka had no known paper, tablet, or monumental script comparable to Maya glyphs, but they possessed a sophisticated textile recording system whose numerical component is deciphered and whose linguistic reach remains disputed.**

### 16. The “angles equal digit value” myth

That familiar legend concerns Hindu-Arabic digit shapes and has no historical relevance to khipu. Khipu values derive from knot count, knot type, position, and document structure—not angles.

### 17. Comparisons with other numeral traditions

There is no evidence that:

- Ishango or Lebombo tally bones led to khipu;
- Uruk tokens traveled to the Andes;
- Brahmi or Hindu-Arabic zero influenced the Inka;
- Chinese counting rods or the suanpan supplied its decimal arrangement;
- Maya vigesimal numerals were its source.

Such comparisons illuminate independent solutions to recording quantity but are not transmission histories.

---

## Chronological conspectus

| Date | Event | Status |
|---|---|---|
| c. 2600–2000 BCE | Caral string bundle called a khipu precursor | **Disputed artefact identification** |
| c. 200–600 CE | Moche images or marks compared with cords | **Suggestion** |
| c. 600–1000 | Wari cord records; some AMS-dated | **Secure artefacts; values disputed** |
| c. 1400–1532 | Canonical Inka decimal khipu | **Secure artefact tradition** |
| 1533 | Hernando Pizarro describes knot accounting | **Documented eyewitness text** |
| mid-1500s | Khipukamayuq testimony used in tribute, census, and litigation | **Documented practice** |
| 1561 | Extended legal proceeding tests khipu-derived testimony | **Documented text** |
| 1582–83 | Third Council of Lima orders destruction of idolatrous khipus | **Documented ecclesiastical rule** |
| 1590 | Acosta describes calculation with grains | **Documented text** |
| 1609 | Garcilaso describes decimal place order and khipu uses | **Documented retrospective text** |
| c. 1615/16 | Guaman Poma draws accountant with khipu and counting board | **Autograph manuscript** |
| 1670 | Santa Valley census later correlated with six khipus | **Documented text; disputed object match** |
| 18th century | Collata epistolary khipus and rebellion traditions | **Objects and community tradition; reading disputed** |
| 1897 | Max Uhle and other early museum scholarship | **Documented scholarship** |
| 1908 | Guaman Poma manuscript brought to wider scholarly attention | **Modern rediscovery** |
| 1912 | Locke publishes decimal decipherment | **Secure reading** |
| 1923 | Locke expands catalogue and analysis | **Documented scholarship** |
| 1969 | Aschers publish richer structural analysis in *Nature* | **Documented scholarship** |
| 1981 | *Code of the Quipu* | **Major synthesis** |
| 1994 onward | Salomon investigates Tupicocha | **Ethnography** |
| 1997 | Revised Ascher volume, *Mathematics of the Incas* | **Major synthesis** |
| 2003 | Urton’s binary-code model | **Influential disputed hypothesis** |
| 2005 | Puruchuco accounting hierarchy published | **Strong numerical reconstruction** |
| 2014–15 | AMS chronology and Wari-to-Inka studies | **Artefact dating and reconstruction** |
| 2014/2017 | Hybrid khipu/alphabetic study links knot direction and moiety | **Statistical decipherment claim** |
| 2018 | Santa Valley census match published | **Strong but disputed correlation** |
| 2019 | Tupicocha ritual khipu use declared Peruvian heritage | **Modern legal recognition** |
| 2020s | Open Khipu Repository succeeds and expands the Harvard database | **Digital corpus** |
| present | Numerical system readable; narrative and phonetic dimensions unresolved | **Scholarly consensus boundary** |

---

## Open questions

1. What exactly was the Caral object, and can it be fully published and directly dated?
2. Did Wari cords encode base five, decimal values, categories, or several systems?
3. How did Wari material practices become canonical Inka decimal khipu?
4. Which surviving museum khipus are certainly pre-conquest rather than colonial?
5. How many document genres existed—census, storehouse, calendar, history, letter, genealogy, ritual?
6. Were color and fiber meanings empire-wide, provincial, occupational, or genre-specific?
7. Are apparent anomalies damage, scribal correction, nondecimal information, or alternative knot grammars?
8. Did numbers sometimes act as labels, rebuses, or names?
9. Can the Santa Valley groups be aligned uniquely with named tributaries?
10. Can Collata sound values predict a reading in an independent khipu?
11. Did imperial khipus encode Quechua, Aymara, several languages, or mainly language-independent categories?
12. What were the exact moves and place weights on a yupana?
13. Were knots revised during calculation, or were finished khipus archival copies?
14. How did readers hold, rotate, touch, and vocalize the cords?
15. What knowledge survives in community custody but remains absent from museum databases?
16. How should databases represent uncertainty, repairs, color fading, and conflicting catalogues?
17. What proportion of the surviving corpus is numerical, nonnumerical, hybrid, fragmentary, or modern?
18. Can microscopy, proteomics, dye analysis, stable isotopes, and improved radiocarbon calibration distinguish regional workshops and pre-/post-conquest production?
19. Did the state impose a standard, or did related local codes coexist?
20. Is “decipherment” the right goal for a medium whose meaning may have depended on performance, office, and social memory?

---

## Assessment

The fullest reconstructable account yields a firm center and uncertain edges.

**Firmly established:** canonical Inka khipus encode decimal integers by positional knot zones. Three knot forms distinguish units from higher positions; missing knots supply zero places; total cords, duplicate records, Puruchuco aggregation, and colonial descriptions independently reinforce the reading. Khipus served a vast bureaucracy and survived well into colonial rule.

**Probable:** color, grouping, attachment, fiber, and branching recorded categories and social relations; calculating boards and loose counters supplied arithmetic whose results were transferred to cords; several document genres existed.

**Unresolved:** a universal color dictionary, an imperial phonetic script, the detailed yupana algorithm, a direct fraction notation, and the precise Wari system.

**Unsupported as stated:** descent from Old World numerals, universal Spanish destruction at conquest, a fully deciphered Inka binary language, a fixed highest number, or the claim that every surviving khipu can be read by applying Locke’s three knots alone.

The essential historical point is not that the Andes possessed an exotic substitute for “real” notation. It is that an imperial society built durable decimal records out of textile structure—using position, repetition, absence, hierarchy, color, touch, and trained performance as parts of one information technology.

---

## Sources

### Primary and early sources

- Leland L. Locke, “The Ancient Quipu, a Peruvian Knot Record,” *American Anthropologist* 14.2 (1912), 325–332:  
  https://en.wikisource.org/wiki/The_Ancient_Quipu,_a_Peruvian_Knot_Record  
  https://www.jstor.org/stable/659935  
  https://anthrosource.onlinelibrary.wiley.com/doi/abs/10.1525/aa.1912.14.2.02a00070

- Leland L. Locke, *The Ancient Quipu or Peruvian Knot Record* (New York: American Museum of Natural History, 1923), Smithsonian catalogue and historical description:  
  https://www.si.edu/object/book-ancient-quipu-or-peruvian-knot-record%3Anmah_1590977

- Inca Garcilaso de la Vega, *Comentarios reales de los Incas* (Lisbon, 1609), Books VI.8–9:  
  https://biblioteca.clacso.edu.ar/clacso/se/20190904032639/Comentarios_reales_2_Inca_Garcilaso_de_la_Vega.pdf

- Felipe Guaman Poma de Ayala, *El primer nueva corónica y buen gobierno*, c. 1615/16, Royal Danish Library, GKS 2232 4°:  
  https://poma.kb.dk/

- José de Acosta, *Historia natural y moral de las Indias* (Seville, 1590):  
  https://www.gutenberg.org/cache/epub/70219/pg70219-images.html  
  https://www.memoriapoliticademexico.org/Textos/1Independencia/1590HNM.html

- Hernando Pizarro, letter/account of Peru, 1533:  
  https://faculty.chass.ncsu.edu/slatta/hi216/documents/pizarro.htm

### Standard surveys and major monographs

- Stephen Chrisomalis, *Numerical Notation: A Comparative History* (Cambridge University Press, 2010), chapter 10, pp. 310–15:  
  https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20(CUP,%202010)(ISBN%200521878187)(O)(498s)_MPop_.pdf

- Marcia Ascher and Robert Ascher, *Code of the Quipu: A Study in Media, Mathematics, and Culture* (University of Michigan Press, 1981); revised as *Mathematics of the Incas: Code of the Quipu* (Dover, 1997):  
  https://books.google.com.ec/books?id=1Zsu5XFAI_oC  
  https://dokumen.pub/code-of-the-quipu-a-study-in-media-mathematics-and-culture-9780472093250-9780472063253.html

- Marcia Ascher and Robert Ascher, “Code of Ancient Peruvian Knotted Cords (Quipus),” *Nature* 222 (1969), 529–533:  
  https://www.nature.com/articles/222529a0

- Gary Urton, *Signs of the Inka Khipu: Binary Coding in the Andean Knotted-String Records* (University of Texas Press, 2003):  
  https://www.jstor.org/stable/10.7560/785397  
  https://revista.drclas.harvard.edu/signs-of-the-inka-khipu/

- Galen Brokaw, *A History of the Khipu* (Cambridge University Press, 2010), publisher excerpt:  
  https://assets.cambridge.org/97805211/97793/excerpt/9780521197793_excerpt.pdf

- Jeffrey Quilter and Gary Urton, eds., *Narrative Threads: Accounting and Recounting in Andean Khipu* (University of Texas Press, 2002), including Frank Salomon’s Tupicocha chapter:  
  https://www.degruyterbrill.com/document/doi/10.7560/769038-014/html

### Archaeology and chronology

- Ruth Shady Solís, Jonathan Haas, and Winifred Creamer, “Dating Caral, a Preceramic Site in the Supe Valley on the Central Coast of Peru,” *Science* 292 (2001):  
  https://pubmed.ncbi.nlm.nih.gov/11326098/

- Gary Urton, “From Middle Horizon Cord-Keeping to the Rise of Inka Khipus in the Central Andes,” *Antiquity* 88/89 (online 2015):  
  https://www.cambridge.org/core/journals/antiquity/article/abs/from-middle-horizon-cordkeeping-to-the-rise-of-inka-khipus-in-the-central-andes/04964C31803194A5EA0F1565617F00C9

- Gary Urton et al., “Radiocarbon Chronology of Andean Khipus”:  
  https://journals.pagepress.net/arc/article/view/arc.2014.5260  
  https://dash.harvard.edu/bitstreams/7312037d-8665-6bd4-e053-0100007fdf3b/download

- American Museum of Natural History, Wari khipu, catalogue 41.2/7678:  
  https://digitalcollections.amnh.org/C.aspx?IID=2URM1THGVJ3M&PN=18&VBID=&VF=DamViewDetailPopup&VP3=CMS3

- Gary Urton and Alejandro Chu, “Accounting in the King’s Storehouse: The Inkawasi Khipu Archive,” *Latin American Antiquity*:  
  https://www.cambridge.org/core/journals/latin-american-antiquity/article/accounting-in-the-kings-storehouse-the-inkawasi-khipu-archive/417CED6AB7ED0F6D37DC7A3E84F698D5

- Museo Nacional de Arqueología, Antropología e Historia del Perú, permanent Inka exhibition:  
  https://mnaahp.cultura.pe/node/514

### Numerical structure and arithmetic

- American Mathematical Society, “The Knots in the Quipu, and in the Friar’s Belt”:  
  https://www.ams.org/publicoutreach/feature-column/fc-2014-05

- Manuel Medrano, “Knot Just Numbers: Andean Khipu Strings,” Gresham College lecture and transcript:  
  https://www.gresham.ac.uk/watch-now/knot-just-numbers  
  https://www.gresham.ac.uk/sites/default/files/transcript/2021-10-20-1600_MEDRANO_BSHM-T.pdf

- Khipu Field Guide, decipherment and statistical analyses:  
  https://www.khipufieldguide.com/guidebook/KhipuDecipherment.html  
  https://www.khipufieldguide.com/notebook/analyses/ascher_sums_overview.html

- INALCO, “Quechua Oral Numeration and Its Writing in Quipus”:  
  https://www.inalco.fr/en/quechua-oral-numeration-and-its-writing-quipus  
  https://www.inalco.fr/la-numeration-orale-quechua-et-son-ecriture-dans-les-quipus

- “Inka Numerical Systems: Khipu and Yupana Analysis,” *Journal of Cognition and Culture* 25 (2025):  
  https://brill.com/view/journals/jocc/25/1-2/article-p128_8.pdf

- “Yupana or Inca Abacus, at 100 Years,” historical survey:  
  https://www.scielo.org.pe/scielo.php?pid=S2219-71682023000100086&script=sci_arttext

- Museo de Arte de Lima, Inka-style yupana:  
  https://artsandculture.google.com/asset/yupana-inca-style/qgHcj1oAkruUHg?hl=en

### Administrative decipherment

- Gary Urton and Carrie J. Brezine, “Khipu Accounting in Ancient Peru,” *Science* 309 (2005), 1065–67:  
  https://pubmed.ncbi.nlm.nih.gov/16099983/

- Detailed Spanish exposition of the Puruchuco hierarchy:  
  https://repositoriodigital.bnp.gob.pe/bnp/recursos/2/html/el-imperio-inka/296/

- Contemporary *Nature* report on Puruchuco:  
  https://www.nature.com/news/2005/050808/full/news050808-11.html

- Manuel Medrano and Gary Urton, “Toward the Decipherment of a Set of Mid-Colonial Khipus from the Santa Valley, Coastal Peru,” *Ethnohistory* 65.1 (2018), 1–23:  
  https://www.researchgate.net/publication/322809850_Toward_the_Decipherment_of_a_Set_of_Mid-Colonial_Khipus_from_the_Santa_Valley_Coastal_Peru  
  https://doi.org/10.1215/00141801-4260638

### Narrative, phonetic, and structural research

- Sabine Hyland, Gene A. Ware, and Madison Clark, “Knot Direction in a Khipu/Alphabetic Text from the Central Andes,” *Latin American Antiquity* 25.2:  
  https://www.cambridge.org/core/journals/latin-american-antiquity/article/abs/knot-direction-in-a-khipualphabetic-text-from-the-central-andes/C7898F2731F82777C595F599909745B5  
  https://doi.org/10.7183/1045-6635.25.2.189

- University of St Andrews, “Discovering the Chanka”:  
  https://news.st-andrews.ac.uk/long-reads/discovering-the-chanka/

- Gary Urton, “Writing the History of an Ancient Civilization without Writing”:  
  https://www.journals.uchicago.edu/doi/10.1086/690611

- Indigenous scripts and the problem of categorizing khipu:  
  https://online.ucpress.edu/jmw/article/1/3/105/50997/Indigenous-Scripts-in-Mesoamerica-and-the-Andes

### Colonial law, religion, and survival

- *Cambridge History of Latin American Law in Global Perspective*, chapter on colonial law and khipu evidence:  
  https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6D953D4F0BEFC1A7C213F45216EC06E1/9781316518045c4_141-249.pdf/how_to_approach_colonial_law.pdf

- José Carlos de la Puente Luna, work on khipu and Indigenous legal activism, discussed in:  
  https://www.cambridge.org/core/journals/americas/article/abs/unreliable-confessions-khipus-in-the-colonial-parish/FC2D07D0803C674C1DEAF65D95AC1C14

- “Du bon usage des quipus face à l’administration coloniale espagnole”:  
  https://www.persee.fr/doc/pop_0032-4663_1998_num_53_1_6849

- Sabine Hyland, “Khipus, Khipu Boards, and Sacred Texts”:  
  https://doi.org/10.25222/larr.1032

- Frank Salomon, “The Twisting Paths of Recall”:  
  https://socialsci.libretexts.org/Bookshelves/Anthropology/Archaeology/Book%3A_Writing_as_Material_Practice_-_Substance_Surface_and_Medium_%28Piquette_et_al.%29/02%3A_The_Twisting_Paths_of_Recall_-_Khipu_%28Andean_Cord_Notation%29_as_Artifact_%28Frank_Salomon%29/2.05%3A_After_the_Inka_Canon_-_The_Khipu_%28Paper_Interface_and_Its_Modern_Successors%29

- Peruvian Ministry of Culture, Tupicocha heritage declaration, 2019:  
  https://www.gob.pe/institucion/cultura/normas-legales/391137-rvm-n-236-2019-vmpcic-mc

### Databases and current corpus work

- Open Khipu Repository, data release:  
  https://doi.org/10.5281/zenodo.18025748

- Cornell Ascher khipu databooks:  
  https://courses.cit.cornell.edu/quipu/

- Khipu Database Project legacy address:  
  http://khipukamayuq.fas.harvard.edu

- “Structural Pattern Mining in Inka Khipus” (2026 preprint; provisional, not peer-reviewed evidence):  
  https://arxiv.org/abs/2607.00185

### Additional contextual sources consulted

- Smithsonian, history of calculating instruments and Locke:  
  https://www.si.edu/object/book-ancient-quipu-or-peruvian-knot-record%3Anmah_1590977

- Smarthistory, “The Inka Khipu”:  
  https://smarthistory.org/inka-khipu/

- Wolfram MathWorld, “Quipu”:  
  https://mathworld.wolfram.com/Quipu.html

- Spanish review of Salomon’s *The Cord Keepers*:  
  https://www.scielo.cl/scielo.php?pid=S0717-73562007000200008&script=sci_arttext

- Miccinelli/Pachaquipu calendar proposal, used only as a disputed source:  
  https://arxiv.org/abs/0801.1577
