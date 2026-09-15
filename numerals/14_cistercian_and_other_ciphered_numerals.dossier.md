# Cistercian numerals and other ciphered systems: Research Dossier

## Method and evidentiary labels

This dossier distinguishes six kinds of claim:

- **[A — artefact]**: supported directly by a surviving manuscript, inscription, instrument, coin, or other object.
- **[T — documented text]**: stated in a historical text, whether or not the statement is independently true.
- **[R — scholarly reconstruction]**: an inference accepted or proposed by modern specialists.
- **[D — disputed]**: materially contested in the scholarly literature.
- **[L — legend/tradition]**: transmitted as a story without adequate corroborating evidence.
- **[M — modern invention/revival]**: a recent construction, extension, encoding, font, or popular reinterpretation.

The central authority is David A. King’s *The Ciphers of the Monks* (2001), checked against Stephen Chrisomalis’s comparative typology and Unicode’s technical documentation. Online summaries have been used only where their claims can be tied back to those sources.

---

## Basic identification

### Cistercian numerals

| Property | Identification |
|---|---|
| Name | Cistercian numerals; medieval “monastic ciphers”; sometimes Basingstoke numerals |
| Base | Decimal: four decimal orders, units through thousands |
| Type | **Ciphered positional-additive ligature**: each quadrant has nine digit-shapes; quadrant supplies place value; occupied quadrants are added |
| Signs | A central staff plus strokes in four quadrants. Canonically: upper right = units; upper left = tens; lower right = hundreds; lower left = thousands |
| Range | Normally 1–9,999 in one compound sign |
| Zero | No independently attested zero digit; an omitted quadrant means a zero coefficient. The bare staff is not demonstrably a medieval numeral zero |
| Period | Early thirteenth century onward; principal Cistercian use, thirteenth–fifteenth centuries; scattered non-Cistercian continuation and later revivals |
| Region | First securely documented in northwestern Europe, especially Cistercian houses in Hainaut; subsequently England, Normandy, northern France, Italy, Sweden, and the Low Countries |
| Arithmetic use | Essentially none securely documented: employed principally as labels, indices, dates, tabular arguments, musical references, and instrument inscriptions |
| Unicode | **Not encoded as characters in Unicode 17.0.** A 2020 background paper explored encoding; current internet displays generally use images, SVG, canvas, or custom fonts |

A concise typological formula is:

\[
N=1000a+100b+10c+d,\qquad a,b,c,d\in\{0,\ldots ,9\},
\]

with each nonzero coefficient drawn as a stroke-pattern in its assigned quadrant around one staff.

The system is therefore “positional” in a spatial sense, but not a linear place-value notation like `4387`. It is also additive because the four quadrant-values are summed. “Ciphered” means that 1–9 in each order have distinctive conventional shapes rather than being made by repeating one tally mark.

---

# The system in detail

## 1. Geometry and ordering

In the common modern vertical presentation:

```text
 thousands | tens
-----------│-----------
 hundreds  | units
```

More exactly:

```text
 upper left: tens       upper right: units
                       │
                       │  central staff
 lower left: thousands  lower right: hundreds
```

Thus:

- a units stroke in the upper right has value \(1\)–\(9\);
- reflection across the vertical staff gives \(10\)–\(90\);
- reflection across the horizontal midpoint gives \(100\)–\(900\);
- reflection across both axes gives \(1,000\)–\(9,000\).

**[A/R] Variation matters.** King’s manuscript survey shows that medieval practice was not governed by one timeless printed chart. Horizontal staffs were common in Cistercian manuscripts because they fitted the line of writing. Vertical forms occur particularly in northern French material of the fourteenth and fifteenth centuries and dominate later revivals. Some traditions interchange forms conventionally assigned to 3/4 and 7/8; 5 and 9 are especially variable.

A horizontal Cistercian numeral is normally understood as the corresponding vertical sign rotated 90 degrees counter-clockwise. It is not a different numerical system.

## 2. The component shapes

For a canonical modernized chart, describe the unit-shapes in the upper-right quadrant as follows. Let the top and middle attachment points lie on the staff and let the outer endpoint lie to the right.

| Digit | Verbal construction in the units quadrant |
|---:|---|
| 1 | short horizontal stroke from the top of the staff to the right |
| 2 | short horizontal stroke from a lower attachment point to the right |
| 3 | diagonal from the top of the staff down and outward |
| 4 | diagonal from an outer upper point down to the lower staff attachment |
| 5 | the strokes of 1 and 4 joined, often triangular or angular |
| 6 | top horizontal plus an outer vertical descending stroke |
| 7 | compound conventionally formed from the 1/6 family |
| 8 | compound conventionally formed from the 2/6 family |
| 9 | closed or nearly closed angular/curved form; manuscript variants include a loop or triangle |

This verbal table is necessarily schematic. **[A]** Medieval hands differ enough that a single normalized font should not be mistaken for palaeographic reality. The most reliable full historical charts are King’s plates and the manuscript reproductions summarized in the Unicode background paper.

## 3. A text-safe notation for this dossier

Because Unicode has no Cistercian characters, I use:

```text
⟦thousands | tens ; hundreds | units⟧
```

A zero means “leave that quadrant empty,” not “write a zero sign.”

Thus:

- 7 = `⟦0|0;0|7⟧`
- 40 = `⟦0|4;0|0⟧`
- 305 = `⟦0|0;3|5⟧`
- 1,234 = `⟦1|3;2|4⟧`
- 9,999 = `⟦9|9;9|9⟧`

Each bracketed expression denotes **one ligatured glyph**, not four written numerals.

## 4. Worked table, 1–20

| Value | Cistercian compound |
|---:|---|
| 1 | `⟦0|0;0|1⟧` |
| 2 | `⟦0|0;0|2⟧` |
| 3 | `⟦0|0;0|3⟧` |
| 4 | `⟦0|0;0|4⟧` |
| 5 | `⟦0|0;0|5⟧` |
| 6 | `⟦0|0;0|6⟧` |
| 7 | `⟦0|0;0|7⟧` |
| 8 | `⟦0|0;0|8⟧` |
| 9 | `⟦0|0;0|9⟧` |
| 10 | `⟦0|1;0|0⟧` |
| 11 | `⟦0|1;0|1⟧` |
| 12 | `⟦0|1;0|2⟧` |
| 13 | `⟦0|1;0|3⟧` |
| 14 | `⟦0|1;0|4⟧` |
| 15 | `⟦0|1;0|5⟧` |
| 16 | `⟦0|1;0|6⟧` |
| 17 | `⟦0|1;0|7⟧` |
| 18 | `⟦0|1;0|8⟧` |
| 19 | `⟦0|1;0|9⟧` |
| 20 | `⟦0|2;0|0⟧` |

## 5. Tens, hundreds, and thousands

| Value | Compound | Value | Compound | Value | Compound |
|---:|---|---:|---|---:|---|
| 10 | `⟦0|1;0|0⟧` | 100 | `⟦0|0;1|0⟧` | 1,000 | `⟦1|0;0|0⟧` |
| 20 | `⟦0|2;0|0⟧` | 200 | `⟦0|0;2|0⟧` | 2,000 | `⟦2|0;0|0⟧` |
| 30 | `⟦0|3;0|0⟧` | 300 | `⟦0|0;3|0⟧` | 3,000 | `⟦3|0;0|0⟧` |
| 40 | `⟦0|4;0|0⟧` | 400 | `⟦0|0;4|0⟧` | 4,000 | `⟦4|0;0|0⟧` |
| 50 | `⟦0|5;0|0⟧` | 500 | `⟦0|0;5|0⟧` | 5,000 | `⟦5|0;0|0⟧` |
| 60 | `⟦0|6;0|0⟧` | 600 | `⟦0|0;6|0⟧` | 6,000 | `⟦6|0;0|0⟧` |
| 70 | `⟦0|7;0|0⟧` | 700 | `⟦0|0;7|0⟧` | 7,000 | `⟦7|0;0|0⟧` |
| 80 | `⟦0|8;0|0⟧` | 800 | `⟦0|0;8|0⟧` | 8,000 | `⟦8|0;0|0⟧` |
| 90 | `⟦0|9;0|0⟧` | 900 | `⟦0|0;9|0⟧` | 9,000 | `⟦9|0;0|0⟧` |

## 6. Famous numbers

| Number | Name/context | One Cistercian glyph |
|---:|---|---|
| 666 | “number of the beast” in later Christian reception | `⟦0|6;6|6⟧` |
| 1066 | Norman Conquest date | `⟦1|6;0|6⟧` |
| 1215 | Magna Carta | `⟦1|1;2|5⟧` |
| 1729 | Hardy–Ramanujan number | `⟦1|2;7|9⟧` |
| 1984 | Orwell’s title/year | `⟦1|8;9|4⟧` |
| 2026 | present-era example | `⟦2|2;0|6⟧` |
| 9999 | normal one-sign maximum | `⟦9|9;9|9⟧` |

## 7. Zero

**[A]** A vacant quadrant performs the structural work of zero: in 1,005, the tens and hundreds quadrants are empty.

**[R]** This makes Cistercian notation place-sensitive without giving it a written zero digit.

**[D/M]** Modern diagrams sometimes call a bare staff “0.” No known medieval Cistercian table securely defines the bare staff that way. A bare staff can be invented as zero in a modern extension, but it should be labelled accordingly.

This is comparable to saying that an empty column on a counting board can represent no counters without claiming that the culture possessed a written zero numeral.

## 8. Fractions

**[A: negative finding]** King found no established Cistercian fractional notation and no evidence that the cipher was used as an operational fraction system.

Fractions could of course be written beside Cistercian integers in ordinary medieval Latin forms, Roman fractions, words, or Indo-Arabic notation, but those are not intrinsic Cistercian fraction signs.

## 9. Arithmetic

The notation is ill suited to written carrying and long multiplication because four decimal places are superimposed. Nothing prevents a modern user from decoding two glyphs, calculating, and re-encoding the answer, but that is not evidence for a medieval algorithm.

**[A]** The surviving uses catalogued by King are overwhelmingly:

- years and calendar arguments;
- foliation and textual divisions;
- numbered propositions, notes, and concordances;
- musical staff-lines and organizational markers;
- astronomical or geometrical scales;
- wine-gauging and other labelling contexts.

**[A: negative finding]** No securely identified medieval Cistercian abacus, calculating board, arithmetic textbook, multiplication table, or worked commercial account uses these signs as its operative numerals.

## 10. Higher numbers

The normal Cistercian system has 36 nonzero place-signs—nine in each of four quadrants—and a one-glyph ceiling of 9,999.

**[A]** Later, mainly non-Cistercian adaptations experimented with further multiplication, including treating an entire sign as thousands or adding marks. These are not uniform.

**[M]** Writing successive Cistercian glyphs as base-10,000 “superdigits” gives unlimited range, but this is a modern extension, not the documented medieval system.

## 11. Words for the powers

Cistercian notation did not create a new spoken number-language. A Latin reader used ordinary Latin words:

- 1: *unus*
- 10: *decem*
- 100: *centum*
- 1,000: *mille*
- 10,000: *decem milia*

Vernacular users pronounced the same signs in their own languages. The numeral is a written cipher, not a lexical system.

---

# Origins: dated and placed

## Before the Cistercians: what is and is not an ancestor

The very early objects named in the general series brief—the Lebombo and Ishango bones, Uruk accounting tokens, Narmer macehead, Bakhshali manuscript, Gwalior inscription, Brahmi numerals, and Dresden Codex—are essential to a global history of notation but are **not demonstrated ancestors of Cistercian numerals**.

### Lebombo and Ishango bones

- **[A]** The Lebombo bone, from Border Cave in southern Africa, bears a sequence of notches and has been assigned a Late Stone Age date, often around 35,000–40,000 years ago.
- **[A]** The Ishango bone, found at Ishango near Lake Edward and held by the Royal Belgian Institute of Natural Sciences, bears grouped notches and is commonly dated to roughly 20,000 years ago.
- **[R/D]** Their interpretation as calendars, prime-number tables, lunar records, or deliberate arithmetic exceeds what the notches alone prove.
- **Finding:** no transmission chain connects either object with the medieval monastic cipher.

### Uruk tokens and clay accounting

- **[A]** Fourth-millennium BCE Mesopotamian tokens, bullae, numerical tablets, and proto-cuneiform administrative records document increasingly abstract accounting.
- **[R/D]** Denise Schmandt-Besserat argued that tokens were direct precursors of written signs. Her broad model was influential; Assyriologists have qualified its linearity and noted that tokens and writing coexisted.
- **Finding:** spatially compounded Cistercian signs did not demonstrably descend from Uruk notation.

### Narmer macehead

- **[A]** The ceremonial macehead from Hierakonpolis, conventionally associated with King Narmer, contains animal and numerical signs interpreted as enormous counts of captives or booty.
- **[R/D]** Exact readings depend on Egyptian numerical and iconographic interpretation.
- **Finding:** no genetic relationship to the Cistercian cipher.

### Bakhshali manuscript and Gwalior zero

- **[A]** The Bakhshali manuscript, Bodleian MS. Sansk. d. 14, uses a dot as a place marker.
- **[D]** Oxford radiocarbon tests on separate birch-bark leaves produced dates in several periods, including the third–fourth, eighth–ninth, and tenth centuries CE. Treating the earliest bark date as the date of one unitary mathematical text is disputed because the manuscript is composite and palaeographic/contextual dating differs.
- **[A]** The Gwalior inscription dated 876 CE contains a circular zero in decimal numbers, including a garden dimension normally read as 270.
- **Finding:** these belong to the history of Indian positional numerals, not the direct origin of the monastic cipher.

### Brahmi numerals at Naneghat and Nasik

- **[A]** Early Indian inscriptions at Naneghat/Nanaghat and later at Nasik/Nashik preserve non-positional Brahmi number signs.
- **[R]** These form part of the long prehistory of Indian decimal notation, but direct graphic descent from individual Brahmi forms to every modern digit cannot always be followed continuously.
- **Finding:** no specific Brahmi-to-Cistercian transmission is documented.

### Dresden Codex

- **[A]** The Dresden Maya Codex contains calendrical and astronomical tables using bars, dots, and zero signs in vigesimal notation.
- **[A]** It is a pre-Columbian Maya manuscript, probably a late copy of older material.
- **Finding:** independent of medieval European Cistercian signs.

These comparisons are salutary: visual similarity, use of place, or possession of zero is not itself evidence of descent.

---

## Immediate background: shorthand and ciphered-additive notation

### Twelfth-century English *ars notaria*

**[A/R]** King identifies close forms in an English shorthand tradition around 1175. These could express numbers to 99 through signs placed around a line. This provides a plausible local formal ancestor for the signs later associated with John of Basingstoke.

It explains two important facts better than a remote exotic derivation:

1. signs resembling the Basingstoke forms existed in England before John’s reported Greek studies;
2. the earliest stage appears to have covered 1–99, with the four-quadrant 1–9,999 arrangement arising later.

### John of Basingstoke

John of Basingstoke, or Johannes de Basing, was an English scholar and Archdeacon of Leicester, dead in 1252. He had returned to England by 1235.

**[T]** Matthew Paris’s *Chronica Majora* reports that John knew Greek learning, brought books and “Greek numerals” from Athens, and credited an exceptionally learned daughter of the archbishop of Athens with teaching him.

**[D]** The phrase “Greek numerals” does not prove that the four-quadrant Cistercian system existed in Greece. No matching Byzantine Greek corpus has been found.

**[R]** King considered a Greek or ancient shorthand relationship possible and pointed to distant formal analogues, including a fourth-century BCE Greek inscription and the larger history of tachygraphy.

**[R/D]** The stronger palaeographic alternative is that the operative numeral forms were derived from, or at least mediated by, English *ars notaria*. The pre-John English parallels make literal importation of the full system from Athens doubtful.

**[L]** The learned Athenian girl is preserved by Matthew Paris as John’s own reported story, but she is not independently attested in local Athenian evidence.

### Earliest Cistercian stage

**[A/R]** The earliest surviving Cistercian attestations are early-thirteenth-century manuscript material associated with monasteries in Hainaut, the historical county spanning parts of present-day Belgium and France.

At first the notation appears principally in a two-place 1–99 form. It was subsequently expanded by reflecting the signs into four positions around a staff, producing 1–9,999.

**[A]** King catalogued approximately two dozen medieval Cistercian manuscripts, thirteenth through fifteenth centuries, distributed from England to Italy and from Normandy to Sweden.

A limitation must be stated plainly: widely accessible summaries of King’s catalogue do not supply a dependable shelfmark-and-folio list for every earliest witness. Consequently it would be unsafe to invent one definitive “first tablet,” museum number, or exact year. The system survives principally in codices, not on an eponymous excavated tablet.

### Physical objects

**[A]** The best-known non-codex witness is the astrolabe associated with “Berselius,” made in the Picardy/northern French milieu, usually dated to the later fourteenth or early sixteenth century depending on which object or reconstruction is meant in secondary retellings. Its scales include the ciphers.

**Caution:** popular accounts often collapse multiple astrolabe discussions or give an unqualified date. King’s instrument catalogue and technical description must control identification; no safe Louvre inventory number emerged from the consulted catalogue material.

---

# Chronological account

## c. 1175: English shorthand parallels

**[A/R]** Numerical shorthand signs resembling the later Basingstoke family are documented in England. They support indigenous shorthand development but do not yet constitute the fully expanded Cistercian system.

## Before 1235–1252: John of Basingstoke

**[T]** John says, through Matthew Paris’s report, that he acquired Greek learning at Athens.  
**[D]** Whether his numerical cipher was Greek, English, or a synthesis remains unresolved.

## Early thirteenth century: adoption in Cistercian circles

**[A/R]** Houses in Hainaut furnish the earliest Cistercian witnesses. The initial 1–99 system was expanded to four decimal orders.

## Late thirteenth century

**[A]** Use spread through monastic manuscript networks. The Beaupré Antiphonary complex, Walters W.759 and related volumes, illustrates the rich Cistercian book culture of Hainaut around 1280–1290, though its catalogue description should not itself be taken as proof that every volume contains numeral ciphers.

## Fourteenth–fifteenth centuries

**[A]** This is the principal period of attested use:

- horizontal forms in flowing manuscript text;
- vertical forms in northern France;
- indices, lists, foliation, Easter tables, musical references;
- astronomical and geometrical instrument work;
- variant digit shapes and quadrant conventions.

A fourteenth-century Norman manuscript reproduced in modern surveys contains long passages in the numeral system; later hands supplied Hindu-Arabic equivalents in the margins, including readings such as 4,484, 715, and 5,199.

## Late fifteenth century

**[A]** A Norman arithmetic text uses Cistercian and Indo-Arabic numerals together. This coexistence is important: the monastic signs were not simply an isolated opponent vanquished at one moment by “Arabic” numerals.

## 1533: Heinrich Cornelius Agrippa

**[T/A]** Book II, chapter 19 of Agrippa’s *De occulta philosophia libri tres* prints the signs and calls them *quadam elegantissima numerorum nota*—approximately “a certain most elegant notation of numbers.”

Agrippa’s occult framing helped detach the notation from mundane monastic indexing and associate it with secret, ancient, or learned writing.

## Sixteenth–eighteenth centuries: practical afterlife

**[A]** The signs continued sporadically outside the Cistercian order. King documented wine-gauging in the Bruges/Damme region into the early eighteenth century.

## Late eighteenth century: Rosicrucian and Masonic settings

**[A/T]** Parisian Chevaliers de la Rose-Croix used the numerals for a short period. Some Freemasons encountered them through Agrippa and antiquarian cipher literature.

**[D]** This does not show an unbroken medieval Cistercian-to-Masonic transmission.

**[Common confusion]** Agrippa’s numeral signs, his cabalistic alphabets, and the later pigpen or “Masonic” alphabet are related through early-modern interests in cipher and occult writing, but they are not one identical system.

## Nineteenth century: antiquarian rediscovery

The numerals were gathered into histories of shorthand, secret writing, Masonry, and number symbols. They were sometimes labelled “Chaldean,” “Cabalistic,” or impossibly ancient.

**[L]** Such labels reflect early-modern and antiquarian prestige genealogies, not demonstrated Near Eastern descent.

## Early twentieth century

**[A/T]** German nationalist and racial-occult writers considered or appropriated the forms as allegedly “Aryan” signs.

**[L]** The Aryan antiquity claim lacks evidence. The secure record is medieval Christian and European.

## 2001: King’s reconstruction

David A. King published the first exhaustive monographic catalogue and historical reconstruction:

> *The Ciphers of the Monks: A Forgotten Number-Notation of the Middle Ages.*

King assembled manuscripts, astronomical instruments, wine-gauging evidence, occult revivals, and modern appropriations, replacing a diffuse antiquarian story with an object-based corpus.

## 2020 onward: internet and encoding revival

**[M]** Social media diagrams, clocks, tattoos, puzzle ciphers, online converters, fonts, and programming packages popularized the vertical four-quadrant form.

**[M]** Some add:

- a bare-staff zero;
- base-10,000 positional chaining;
- decimal points or fractions;
- negative signs;
- standardized geometric grids;
- “secret monk code” narratives.

These can be elegant extensions but are not medieval evidence.

A 2020 Unicode background paper discussed the system. It did not result in encoded Cistercian characters through Unicode 17.0.

---

# Arithmetic and instruments

## How Cistercian users probably calculated

**[R]** Their calculations were likely carried out in the same media as those of their contemporaries—counters, boards, finger reckoning, Roman numerals, words, and increasingly Hindu-Arabic figures—then results or identifiers could be copied into Cistercian form.

That reconstruction follows from:

- the absence of Cistercian computational textbooks;
- the notation’s use as compact labelling;
- the coexistence of several numeral repertoires in medieval manuscripts.

It does not follow that the monks were mathematically unsophisticated. It only means that this particular notation was not their principal calculating algorithm.

## Finger reckoning

Medieval Latin writers inherited elaborate finger-number systems, especially through Bede’s *De temporum ratione*. Finger signs could represent units, tens, hundreds, and thousands through hand and finger positions.

The resemblance to assigning decimal orders to spatial zones is suggestive, but no source says the Cistercian quadrants were copied from Bedean finger reckoning.

## Counting boards and abaci

The Roman *calculus* was a pebble used in reckoning; hence Latin *calculare* and English “calculate” and “calculus.” Medieval European reckoning tables placed counters on lines or spaces representing orders of magnitude.

The famous portable Roman hand abaci—including examples traditionally illustrated from the Bibliothèque nationale and museums such as the Louvre—use slotted beads or buttons and Roman fractional subdivisions. They are not Cistercian devices.

## Abacists and algorists

From the twelfth century onward:

- **abacists** calculated with counters and reckoning boards;
- **algorists** promoted written Hindu-Arabic place-value procedures.

The contrast was real but not absolute. Merchants and teachers could use both. Cistercian ciphers formed a third, specialized notational option, principally for recording and organization rather than computation.

## Textbooks in the wider environment

The requested canonical mathematical works belong to different numeral traditions:

- Rhind Mathematical Papyrus: Egyptian unit-fraction computation.
- Plimpton 322: Old Babylonian sexagesimal table.
- *Nine Chapters*: Chinese counting-rod algorithms.
- Aryabhata: Indian verse mathematics and place-sensitive letter notation.
- Brahmagupta: arithmetic rules involving debts, fortunes, and zero.
- al-Khwarizmi: Arabic exposition of Indian calculation; the Latinized name supplied “algorithm.”
- Fibonacci, *Liber Abaci* (1202; revised 1228): dissemination of Indian numerals and commercial arithmetic in Latin Europe.
- Sacrobosco, *Algorismus vulgaris*: university exposition of decimal algorism.
- Pacioli, *Summa de arithmetica* (1494): commercial mathematical synthesis.
- Robert Recorde: sixteenth-century English arithmetic and algebra.

**[A: negative finding]** None is a textbook of Cistercian-cipher arithmetic.

## Word histories

| Word | Documentary descent |
|---|---|
| calculus | Latin *calculus*, “small pebble,” hence a counter and calculation |
| digit | Latin *digitus*, “finger”; finger counting underlies the mathematical sense |
| abacus | Latin *abacus*, from Greek *abax/abakion*; deeper borrowing is debated |
| algorithm | Medieval Latin forms of al-Khwarizmi’s name, later generalized from decimal calculation to any specified procedure |
| cipher | Medieval Latin *cifra/ciphra*, from Arabic *ṣifr*, “empty/zero”; later “numeral” and then secret writing |
| zero | Italian *zero/zefiro*, through medieval Latin/Italian forms of Arabic *ṣifr* |
| score | Germanic cutting/notching vocabulary; later twenty, probably through counting tallies |

Calling the monastic signs “ciphers” is historically intelligible because *cipher* once meant a numeral or numerical notation, not only encrypted writing.

---

# Transmission and replacement

## Cistercian route

A cautious route is:

```text
English shorthand environment, c. 1175
        ↓
John of Basingstoke tradition, early 13th century
        ↓
Cistercian houses in Hainaut
        ↓
monastic manuscript networks across western and northern Europe
        ↓
limited lay/instrumental use
        ↓
Agrippa’s printed occult-philosophical presentation, 1533
        ↓
wine-gauging, antiquarian, Rosicrucian and Masonic afterlives
        ↓
King’s scholarly reconstruction, 2001
        ↓
internet diagrams, fonts and digital art
```

The Athens-to-England arrow remains disputed; the Hainaut manuscript diffusion is much better supported.

## Why it was replaced

No decree abolished Cistercian numerals. Their decline is best explained by competition:

- Hindu-Arabic notation supported written algorithms and arbitrary-length numbers;
- Roman numerals remained institutionally familiar;
- printing rewarded small standardized character repertoires;
- the Cistercian system had many handwritten variants;
- a superimposed four-place glyph is harder to sort, proofread, and calculate with than a linear digit string.

The Florentine statute of 1299 restricting merchant-account entries in “figures” and requiring letters or Roman numerals belongs to the history of distrust of Hindu-Arabic digits, especially their alterability. It is not evidence that Florence preferred Cistercian signs.

---

# Comparative ciphered systems

## What “ciphered” means here

Chrisomalis calls a notation **ciphered-additive** when it supplies a distinct sign for each unit multiple in successive decimal orders—1–9, 10–90, 100–900—then adds those values. Greek alphabetic, Armenian, Georgian, Glagolitic, Cyrillic, and Ethiopic numerals largely fit this family.

Cistercian numerals are unusual because the order is encoded by quadrant and all components are ligatured into one graph.

---

## Aegean and Cypriot numerals

### Identification

| Property | Aegean numerals |
|---|---|
| Period | Bronze Age Crete and Mycenaean Greece; inherited in Cypriot writing |
| Base/type | Decimal, additive, with separate signs for powers of ten |
| Core Unicode signs | 𐄇 1; 𐄐 10; 𐄙 100; 𐄢 1,000; 𐄫 10,000 |
| Zero | None required in additive notation |
| Region | Crete, Greek mainland, Aegean islands, Cyprus |
| Direction/order | Normally higher values before lower ones; signs repeated |

**[A]** Linear A and Linear B administrative tablets contain numeral and commodity signs. The Aegean number-sign repertoire derives from Linear A and was retained in Linear B; related forms persisted in Cypriot syllabic documents.

**[A/R]** Linear B was deciphered as Mycenaean Greek by Michael Ventris, with crucial philological collaboration from John Chadwick, in 1952–1953. Linear A remains undeciphered linguistically, but its numerical signs can often be understood through accounting context and continuity with Linear B.

### Examples

Using repeated signs:

| Value | Aegean |
|---:|---|
| 1 | 𐄇 |
| 2 | 𐄈 |
| 3 | 𐄉 |
| 4 | 𐄊 |
| 5 | 𐄋 |
| 10 | 𐄐 |
| 20 | 𐄑 |
| 100 | 𐄙 |
| 1,000 | 𐄢 |
| 10,000 | 𐄫 |

Unicode encodes consolidated number characters as well as unit signs; these are scholarly digital encodings of attested ancient forms, not evidence that Bronze Age scribes possessed a character standard.

### Fractions

Linear A has signs interpreted as fractional quantities, but exact phonetic values and the full system remain debated. Linear B ration systems combine numerals with commodity and metrological signs. They should not be forced into a modern universal fraction chart.

### Relation to Cistercian notation

**Finding:** typological only. Both are decimal and compact relative to tallying, but Aegean notation is additive-linear and more than two millennia earlier. No transmission is documented.

---

## Ethiopic or Geʽez numerals

### Identification

| Property | Ethiopic |
|---|---|
| Period | Aksumite/late antique development, conventionally around the fourth century CE; continuing liturgical and traditional use |
| Type | Ciphered-additive with multiplicative powers of 100 |
| Zero | None |
| Direction | Left to right |
| Origin | Numeral glyphs derived from Greek alphabetic numerals, perhaps through Coptic forms |
| Basic signs | ፩–፱, ፲–፺, ፻ 100, ፼ 10,000 |

### Signs

| Value | Sign | Value | Sign |
|---:|---|---:|---|
| 1 | ፩ | 10 | ፲ |
| 2 | ፪ | 20 | ፳ |
| 3 | ፫ | 30 | ፴ |
| 4 | ፬ | 40 | ፵ |
| 5 | ፭ | 50 | ፶ |
| 6 | ፮ | 60 | ፷ |
| 7 | ፯ | 70 | ፸ |
| 8 | ፰ | 80 | ፹ |
| 9 | ፱ | 90 | ፺ |
| 100 | ፻ | 10,000 | ፼ |

### 1–20

`፩ ፪ ፫ ፬ ፭ ፮ ፯ ፰ ፱ ፲ ፲፩ ፲፪ ፲፫ ፲፬ ፲፭ ፲፮ ፲፯ ፲፰ ፲፱ ፳`

### Structure

Unicode gives:

\[
2345=(20+3)\times100+(40+5)=\text{፳፫፻፵፭}.
\]

A coefficient of one before ፻ or ፼ is often omitted. Repeated hundred signs can indicate successive powers of 100.

**[R]** Derivation from the Greek alphabetic system is strongly supported by sign order and shapes, possibly mediated by Coptic. Ethiopic is exceptional because the numeral signs are no longer simply the ordinary letters of the Geʽez script.

**[A]** Traditional manuscripts may include the conjunction ወ “and” when spelling the expression in a speech-like sequence.

### Fractions and maximum

There is no intrinsic modern-style decimal fraction notation. Fractional expressions use words or specialized manuscript conventions. The system is theoretically extensible by multiplication and repeated powers; unlike one-glyph Cistercian notation, it has no comparable 9,999 ceiling.

---

## Armenian letter-numerals

### Identification

| Property | Armenian |
|---|---|
| Period | After creation of Armenian script, conventionally 405–406 CE |
| Type | Decimal ciphered-additive alphabetic |
| Signs | First nine letters = 1–9; next nine = 10–90; next = 100–900; next = 1,000–9,000 |
| Zero | None in the original alphabetic system |
| Maximum ordinary alphabetic series | 9,999 |
| Region | Armenia and Armenian manuscript diaspora |

### Core table

| 1–9 | 10–90 | 100–900 | 1,000–9,000 |
|---|---|---|---|
| Ա–Թ | Ժ–Ղ | Ճ–Ջ | Ռ–Ք |

Examples:

- 1 = Ա
- 9 = Թ
- 10 = Ժ
- 20 = Ի
- 100 = Ճ
- 1,000 = Ռ
- 1,999 = ՌՋՂԹ

Values are added, normally largest first.

**[R]** The numerical organization was probably modelled on Greek alphabetic notation.  
**[T/L/D]** Medieval Armenian tradition attributes the alphabet to Mesrop Mashtots and also credits him with Georgian and Caucasian Albanian writing. Armenian script creation is well supported; the extension of sole authorship to Georgian remains contested.

**[T/A]** Anania Shirakatsi in the seventh century devised a distinctive compact numerical scheme using twelve Armenian letters. It is a learned secondary notation, not the basic alphabetic system.

Overbars and other multiplier conventions were later used for high values, but they were not perfectly uniform.

---

## Georgian letter-numerals

Traditional Georgian alphabetic numerals likewise assign:

- nine letters to 1–9;
- nine to 10–90;
- nine to 100–900;
- further letters to thousands and 10,000.

They are additive and have no original zero.

**[A]** They appear in manuscripts, inscriptions, ecclesiastical numbering, dates, chapters, and lists.

**[R]** Their organization belongs to the Greek-influenced family of eastern Christian alphabetic numerations.

**[D]** Origin narratives for the Georgian script are entangled with Armenian and Georgian national historiographies. Armenian historical tradition credits Mashtots; Georgian tradition generally rejects Armenian authorship. Structural resemblance shows contact or shared models more securely than it identifies one individual inventor.

Arabic/European figures replaced the letter-numerals in most calculation, while Georgian letters remain possible for enumerative or ceremonial purposes.

---

## Glagolitic numerals

Glagolitic was devised in or around 862–863 for the Slavonic mission of Constantine-Cyril and Methodius.

### Structure

- letters receive values in native Glagolitic alphabetic order;
- 1–9, 10–90, and 100–900 are additive;
- numbers are written left to right, usually greatest first;
- a line or tilde above, or medial dots around letters, may mark numerical use.

The 1483 *Missale Romanum Glagolitice* and the Vinodol Statute preserve numerical marking conventions.

**[A]** Because letters served double duty, numeral marks disambiguated them.  
**[R]** The structural model is Greek alphabetic notation, but the values follow Glagolitic order rather than mechanically copying every Greek letter-value.

---

## Cyrillic numerals

Old Cyrillic numerical notation more closely follows Greek numerical values than Glagolitic does.

Examples in normalized Church Slavonic typography:

- а҃ = 1
- в҃ = 2
- г҃ = 3
- і҃ = 10
- к҃ = 20
- р҃ = 100

The combining titlo is Unicode U+0483: ◌҃. A thousands sign, ҂, placed before a unit letter multiplies it by 1,000:

- ҂а = 1,000
- ҂в = 2,000

**[A]** In manuscripts and early print, a titlo may span all or part of a multi-letter number; Unicode’s single combining character is a digital representation of variable scribal practice.

**[A]** Cyrillic numerals survived in Church Slavonic printing, inscriptions, coins, and ecclesiastical books after Hindu-Arabic digits had entered secular calculation.

**[Common error]** Cyrillic letters do not always take values in modern Russian alphabet order. The system follows the old ecclesiastical alphabet and its Greek model.

---

## Burmese digits

### Signs

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| ၀ | ၁ | ၂ | ၃ | ၄ | ၅ | ၆ | ၇ | ၈ | ၉ |

Burmese notation is decimal and positional, with zero, and belongs to the Indian-derived numeral family.

**[R]** The Myanmar script derives through Brahmi-related South Indian scripts, with Mon mediation conventionally important from about the eighth century.

**[A/M]** Unicode distinguishes Myanmar digit zero ၀ from visually similar Myanmar letter wa ဝ. Visual identity in some fonts does not make them the same encoded character.

### 1–20

`၁ ၂ ၃ ၄ ၅ ၆ ၇ ၈ ၉ ၁၀ ၁၁ ၁၂ ၁၃ ၁၄ ၁၅ ၁၆ ၁၇ ၁၈ ၁၉ ၂၀`

Powers: `၁၀, ၁၀၀, ၁၀၀၀, ၁၀၀၀၀`.

Unlike Cistercian notation, this is a fully linear place-value system suitable for standard written arithmetic.

---

## Thai digits

### Signs

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| ๐ | ๑ | ๒ | ๓ | ๔ | ๕ | ๖ | ๗ | ๘ | ๙ |

### 1–20

`๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙ ๑๐ ๑๑ ๑๒ ๑๓ ๑๔ ๑๕ ๑๖ ๑๗ ๑๘ ๑๙ ๒๐`

Powers: `๑๐, ๑๐๐, ๑๐๐๐, ๑๐๐๐๐`.

Thai is decimal positional and contains zero. Its signs belong to the Brahmi-derived Southeast Asian tradition.

**[A]** Thai numerals continue in official documents, religious or traditional contexts, clocks, prices, and stylistic uses, while European digits predominate in many everyday and technical settings.

**[R]** Similarities between Thai number words and Chinese varieties involve contact and borrowing, especially in higher constructions; they should not be confused with the graphic ancestry of the digits.

---

## Sinhala Illakkam and Lith Illakkam

Two systems must not be conflated.

### Sinhala archaic numerals or Sinhala Illakkam

- non-positional;
- separate signs for 1–9, tens, 100, and 1,000;
- no zero;
- used before the end of the Kandyan kingdom in 1815;
- encoded at U+111E0–U+111FF.

### Sinhala Lith Illakkam

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| ෦ | ෧ | ෨ | ෩ | ෪ | ෫ | ෬ | ෭ | ෮ | ෯ |

Lith Illakkam is decimal positional and includes a zero. It was used especially in astrological calculation, ephemerides, horoscopes, and numbering palm-leaf pages.

**[A/T]** Abraham Mendis Gunasekera’s 1891 grammar and related writing distinguish older Sinhala numeral practices. Later catalogue and encoding work identified multiple Lith variants, especially for 2, 3, and 9.

**[D]** Sources have repeatedly confused the zero-less archaic Sinhala Illakkam with zero-bearing Lith Illakkam. Statements such as “Sinhala numerals had no zero” are true of the former and false of the latter.

Unicode explicitly distinguishes them.

---

## Kaktovik Iñupiaq numerals

### Basic identification

| Property | Kaktovik |
|---|---|
| Date | 1994 |
| Place | Harold Kaveolook School, Kaktovik, Barter Island, Alaska |
| Creators | A class of Iñupiaq middle-school students, guided by teacher William Clark Bartley |
| Base | 20, with visible sub-base 5 |
| Type | Positional, iconic/tally-structured |
| Digits | Twenty atomic digits, 0–19 |
| Unicode | U+1D2C0–U+1D2D3, added in Unicode 15.0 |
| Status | Deliberate modern community invention, subsequently adopted and taught regionally |

### Signs, 0–19

| Value | Sign | Value | Sign |
|---:|---|---:|---|
| 0 | 𝋀 | 10 | 𝋊 |
| 1 | 𝋁 | 11 | 𝋋 |
| 2 | 𝋂 | 12 | 𝋌 |
| 3 | 𝋃 | 13 | 𝋍 |
| 4 | 𝋄 | 14 | 𝋎 |
| 5 | 𝋅 | 15 | 𝋏 |
| 6 | 𝋆 | 16 | 𝋐 |
| 7 | 𝋇 | 17 | 𝋑 |
| 8 | 𝋈 | 18 | 𝋒 |
| 9 | 𝋉 | 19 | 𝋓 |

Twenty decimal is written `𝋁𝋀`: one score plus zero units.

### Construction

- vertical strokes encode units within a group of five;
- horizontal strokes encode groups of five;
- 18, for example, is three horizontal strokes plus three vertical strokes: \(3\times5+3\).

The zero resembles crossed arms or an X. **[T]** Bartley recalls that a student demonstrated “nothing” by crossing her arms above her head and that this inspired the sign.

### Positional values

Because the radix is 20:

- 𝋁 = 1
- 𝋁𝋀 = 20
- 𝋁𝋀𝋀 = 400
- 𝋁𝋀𝋀𝋀 = 8,000

There is no fixed maximum.

### Arithmetic

The iconic construction permits visual operations:

- addition by combining strokes;
- subtraction by erasing corresponding strokes;
- regrouping five verticals as one horizontal;
- carrying four groups of five into the next base-20 position.

**[A/T]** Reports connect classroom use with improved engagement and test performance. Strong causal claims require caution because the evidence does not come from a controlled experiment.

### Priority claim

**[M/A]** Kaktovik is securely dated and documented as a 1994 creation. Calling it “the newest numeral system” is defensible only with qualifications: people continually invent private and constructed systems. It is one of the newest community-created systems to achieve educational adoption and Unicode encoding.

---

# People

## John of Basingstoke (d. 1252)

Scholar of Greek, Archdeacon of Leicester, and reported carrier of “Greek numerals.” His role in the immediate precursor tradition is documented through Matthew Paris; his personal invention of the final four-quadrant form is not.

## Matthew Paris (c. 1200–1259)

Benedictine chronicler of St Albans. His *Chronica Majora* is the principal textual source for John’s Greek learning and Athens narrative.

## Cistercian scribes

Mostly anonymous. They transformed a learned or shorthand cipher into a flexible monastic information technology: foliation, concordance, tabular reference, music, calendrical work, and instrument labelling.

## Heinrich Cornelius Agrippa (1486–1535)

Printed the signs in *De occulta philosophia* and helped give them an occult afterlife.

## David A. King (b. 1941)

Historian of astronomy and scientific instruments. His 2001 monograph reconstructed the corpus and remains indispensable.

## Stephen Chrisomalis

Anthropologist and historian of numerical notation. His 2010 comparative study supplies the standard structural vocabulary—additive, multiplicative, positional, ciphered—and situates Cistercian numerals among world systems.

## Mesrop Mashtots (c. 362–440)

Traditionally and historically connected with the Armenian alphabet. Claims regarding Georgian authorship remain contested.

## Anania Shirakatsi (seventh century)

Armenian mathematician who created a compact secondary alphabetic notation and wrote mathematical tables and problems.

## Constantine-Cyril (826/827–869) and Methodius (c. 815–885)

Missionaries associated with the creation and dissemination of Glagolitic literacy and Slavonic liturgy.

## Michael Ventris (1922–1956) and John Chadwick (1920–1998)

Central to the decipherment and philological validation of Linear B as Mycenaean Greek.

## Abraham Mendis Gunasekera (1849–1918)

Recorded Sinhala grammatical and numerical traditions at the end of the nineteenth century, including distinctions later important to Unicode encoding.

## Kaktovik students and William Clark Bartley

The student group collectively designed the Kaktovik numeral forms in 1994. Bartley facilitated and later documented the project. Accounts that substitute a different teacher or call the pupils high-school students conflict with the Unicode proposal and Bartley-based reporting.

---

# Culture

## Monastic information design

Cistercian numerals belong less to theoretical mathematics than to the history of indexing. A single complex sign could function as a compact visual label, much like a modern barcode interpreted by a trained reader.

Uses included:

- dividing sermons and theological works;
- numbering marginal notes;
- calendrical and Easter-table arguments;
- concordance references;
- identifying musical staff lines;
- marking dates or quantities on scientific instruments.

## Liturgy

Cistercian manuscripts were liturgical and devotional objects, but the signs themselves were not inherently sacramental. Later occult readings should not be projected backward into every monastic use.

Glagolitic, Cyrillic, Armenian, Georgian, and Ethiopic numerals remained strongly associated with church books because the scripts themselves were maintained through liturgy.

## Gematria and isopsephy

Greek isopsephy, Hebrew gematria, Arabic *abjad* calculation, and related systems exploit the fact that letters carry number-values.

Cistercian numerals are not an alphabet and therefore do not naturally yield word-sums. Agrippa’s juxtaposition of numeral ciphers with occult alphabets encouraged later confusion.

## Chronograms

A chronogram embeds numeral-letters—especially Roman `M D C L X V I`—inside a phrase; their sum gives a date. This flourished particularly in early-modern Europe.

Cistercian signs can write dates compactly but do not make conventional alphabetic chronograms because their strokes are not simultaneously letters.

## Law, coins, and official documents

Alphabetic numerals appear in:

- Armenian and Georgian manuscript divisions;
- Cyrillic-dated Russian and ecclesiastical coins;
- Thai legal and governmental numbering;
- Sinhala royal or astrological documents;
- Ethiopic chronicles and church texts.

Cistercian numerals had much less official political reach.

## Typography

Hindu-Arabic typography developed:

- lining figures of equal height;
- old-style or text figures with ascenders and descenders;
- tabular figures of equal width;
- proportional figures.

Cistercian notation never passed through a comparable mass-print typographic standardization. Agrippa’s printed table and modern fonts freeze one selection from a variable manuscript repertoire.

## Modern art and internet culture

Since the 2010s, Cistercian numerals have become popular for:

- clocks;
- tattoos and jewellery;
- puzzles and escape rooms;
- programming demonstrations;
- generative graphics;
- science-fiction and constructed scripts;
- year logos.

This revival often favors visual symmetry over historical variants.

---

# Controversies and disputes

## 1. Were Cistercian numerals invented by John of Basingstoke?

- **For:** Matthew Paris associates John with unusual “Greek numerals”; later signs belong to the Basingstoke family.
- **Against:** comparable English shorthand signs occur around 1175; the earliest Cistercian witnesses are institutional and anonymous; the four-order expansion may postdate John.
- **Assessment:** John is a plausible transmitter or namesake, not a securely documented sole inventor.

## 2. Did the signs come from Greece?

- **For:** Matthew Paris’s explicit report; King’s comparison with an ancient Greek inscription and broader shorthand traditions.
- **Against:** no Byzantine Greek corpus contains the full Cistercian system; English *ars notaria* supplies closer immediate parallels.
- **Assessment:** a Greek-learning tradition is documented; Greek origin of the exact system is disputed.

## 3. Are they genuinely Cistercian?

Yes in the limited sense that Cistercian manuscripts preserve and developed their best-known form. No if “Cistercian” is taken to mean every sign was invented from nothing inside the order or used only by Cistercians.

## 4. Is the system positional?

- **Yes:** quadrant determines decimal order.
- **Qualification:** it is not linear positional notation; each of 36 order-values has a ciphered component form, and all four are overlaid.
- **Best description:** spatially positional, ciphered-additive, decimal ligature notation.

## 5. Does it have zero?

- **Documented:** empty quadrants express zero coefficients.
- **Not documented:** an autonomous zero digit.
- **Modern invention:** assigning the bare staff the numerical value zero.
- **Conclusion:** “no zero at all” and “the staff is its zero” are both oversimplifications.

## 6. Could it perform arithmetic?

In principle, any notation can be decoded and used in calculation. The historical question is different.

- **Evidence present:** labels and recorded quantities.
- **Evidence absent:** native written algorithms, worked arithmetic, operational tables.
- **Conclusion:** claims of efficient medieval Cistercian arithmetic are modern extrapolations.

## 7. Was it a rival that nearly defeated Arabic numerals?

**[L/M]** No evidence supports a society-wide contest. Cistercian notation overlapped chronologically with the spread of Hindu-Arabic figures, but its manuscript corpus and functions were narrow.

## 8. Are the numerals “Chaldean,” Kabbalistic, or Masonic?

- “Chaldean” and “Kabbalistic” are early-modern prestige labels, not substantiated provenance.
- Freemasons and Rosicrucian groups later used or knew related diagrams.
- The pigpen alphabet is not simply Cistercian numeration converted into letters.
- There is no demonstrated ancient-to-medieval-to-Masonic chain.

## 9. Did Agrippa revive them?

Agrippa indisputably printed them in 1533. “Revive” may overstate the case because scattered practical traditions still survived. His more consequential role was reframing them within occult philosophy.

## 10. Are online charts authentic?

Usually they normalize one vertical form and suppress:

- horizontal medieval orientation;
- regional quadrant orders;
- variant 3/4/7/8 forms;
- dot, triangle, and loop variants for 5 and 9;
- ambiguous or malformed historical signs.

They are useful teaching diagrams, not diplomatic editions.

## 11. Unicode status

- **Cistercian:** discussed but not encoded through Unicode 17.0.
- **Kaktovik:** encoded in Unicode 15.0.
- **Aegean, Ethiopic, Armenian, Georgian, Glagolitic, Cyrillic, Myanmar, Thai, and Sinhala:** relevant characters are encoded.

Claims that a copied private-use Cistercian font proves official Unicode support are false.

## 12. Kaktovik “first” and “newest” claims

Kaktovik is a well-documented 1994 community invention and perhaps the most prominent recently created positional numeral system adopted for Indigenous-language education.

It is not literally humanity’s final or only new system: private, liturgical, pedagogical, and constructed numeral sets continue to be devised. Its distinctive achievement is community authorship, cultural fit, institutional teaching, and Unicode recognition.

## 13. Ethiopic origin

Greek structural and graphic derivation, possibly through Coptic, is the standard reconstruction. A direct, precisely dated act of borrowing is not documented. The Geʽez script’s South Semitic ancestry does not imply that its numeral signs must have the same origin.

## 14. Armenian and Georgian priority

The secure points are:

- Armenian writing is associated with Mashtots in the early fifth century;
- both systems use Greek-like ciphered-additive numerical organization;
- medieval Armenian tradition credits Mashtots more widely.

The disputed point is authorship of Georgian writing. National traditions cannot substitute for securely dated inscriptions and comparative palaeography.

## 15. Sinhala zero

Confusion results from two systems:

- Sinhala Illakkam: zero-less and non-positional.
- Lith Illakkam: positional and zero-bearing.

Arguments about “the Sinhala invention of zero” must also distinguish a local written zero from the much broader concept and arithmetic theory of zero.

## 16. The angles-count-the-value legend

The familiar internet diagram alleging that Hindu-Arabic digits originally contained a number of angles equal to their values is a modern fabrication. It does not explain the historical manuscript forms of Indian, Arabic, or European digits.

It is unrelated to the genuinely geometric construction of Kaktovik numerals and to the quadrant logic of Cistercian notation.

---

# Open questions

1. Can every early Cistercian witness be digitized and presented in a public manuscript census with shelfmark, folio, date, provenance, orientation, and digit variants?

2. Which exact English shorthand exemplars around 1175 provide the closest palaeographic parallels to each Basingstoke sign?

3. Does Matthew Paris’s “Greek numerals” refer to alphabetic Greek notation, a shorthand learned in Greek lands, or a system that John himself reworked?

4. Where and when was the expansion from 1–99 to 1–9,999 first made?

5. Did any practical computational worksheet using the signs disappear because ephemeral wax tablets and reckoning boards rarely survive, or was computation never attempted?

6. Can wine-gauging marks be linked continuously from medieval manuscript use to the eighteenth-century Low Countries?

7. Which Masonic and Rosicrucian archives first copied the Agrippan numeral table, and did transmission occur directly through Agrippa or through later cipher manuals?

8. Which Cistercian signs were seriously proposed in twentieth-century German nationalist literature, and which claims derive only from later descriptions?

9. Would a future Unicode encoding represent 36 component characters, complete precomposed numerals, joining controls, or a graphical notation outside ordinary character encoding? The 2020 background paper did not settle that design problem.

10. How widely are Kaktovik numerals presently taught and used outside North Slope educational and language-revitalization settings? Anecdotal spread is better documented than quantitative adoption.

---

# Sources

## Cistercian numerals: principal works and documents

- David A. King, *The Ciphers of the Monks: A Forgotten Number-Notation of the Middle Ages*, Boethius 44, Stuttgart: Franz Steiner, 2001. Bibliographic record and review:  
  https://www.persee.fr/doc/rhs_0151-4105_2005_num_58_1_2246_t1_0253_0000_2

- Review in *Suhayl* 2 (2001), including discussion of John of Basingstoke, Greek origin, *ars notaria*, and Arabic comparanda:  
  https://www.ub.edu/arab/suhayl/volums/volum2/Reviews.pdf

- Unicode, “Background for Unicode consideration of Cistercian digits,” L2/20-290, 2020:  
  https://www.unicode.org/L2/L2020/20290-cistercian-digits.pdf

- Stephen Chrisomalis, *Numerical Notation: A Comparative History*, Cambridge University Press, 2010:  
  https://doi.org/10.1017/CBO9780511676062  
  Accessible consultation copy:  
  https://nzdr.ru/data/media/biblio/kolxoz/M/MPop/Chrisomalis%20S.%20Numerical%20notation..%20A%20comparative%20history%20%28CUP%2C%202010%29%28ISBN%200521878187%29%28O%29%28498s%29_MPop_.pdf

- Stephen Chrisomalis, *Glossographia*, essays on numerical notation and Cistercian/early-modern cipher traditions:  
  https://glossographia.com/category/numerals/  
  https://glossographia.com/category/numerals/page/3/

- Matthew Paris, *Chronica Majora*, Rolls Series edition, material on John of Basingstoke:  
  https://www.deanechurch.co.uk/library/BooksDigital/ChronicaMajora/matthiparisiensi07pari.pdf

- Oxford Dictionary of National Biography-derived study, “Basingstoke, John of”:  
  https://mural.maynoothuniversity.ie/id/eprint/456/1/Basingstoke.pdf

- Walters Art Museum, W.759, Beaupré Antiphonary, Hainaut, c. 1280–1290:  
  https://thedigitalwalters.org/Data/WaltersManuscripts/html/W759/description.html

- Walters Art Museum, W.218, Cistercian Book of Hours, Hainaut, c. 1440:  
  https://www.thedigitalwalters.org/Data/WaltersManuscripts/html/W218/description.html

- Heinrich Cornelius Agrippa, *De occulta philosophia libri tres*, Book II, chapter 19; digitized editions may be located through:  
  https://archive.org/search?query=title%3A%28De+occulta+philosophia%29+AND+creator%3A%28Agrippa%29

- George Oliver/Albert Mackey traditions and nineteenth-century Masonic cipher discussion, *An Encyclopaedia of Freemasonry*:  
  https://upload.wikimedia.org/wikipedia/commons/0/02/An_encyclopaedia_of_freemasonry_and_its_kindred_sciences-_comprising_the_whole_range_of_arts%2C_sciences_and_literature_as_connected_with_the_institution%3B_%28IA_cu31924031411733%29.pdf

- Modern custom-font demonstration, useful only as a normalized reconstruction:  
  https://bobbiec.github.io/cistercian-font.html

## Unicode and comparative systems

- Unicode 17.0 Core Specification, Chapter 7: Greek, Coptic, Cyrillic, Glagolitic, Armenian:  
  https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-7/

- Unicode Technical Note 41, *Church Slavonic Typography in Unicode*:  
  https://www.unicode.org/notes/tn41/tn41-1.pdf

- Unicode 17.0 Core Specification, Chapter 13, Sinhala:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-13/

- Unicode Sinhala Archaic Numbers chart:  
  https://unicode.org/charts/PDF/U111E0.pdf

- Proposal/technical documentation for Sinhala numerals:  
  https://www.unicode.org/wg2/docs/n3888.pdf

- Unicode 17.0 Core Specification, Chapter 16, South and Southeast Asian scripts:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-16/

- Unicode 17.0 Core Specification, Chapter 19, Ethiopic:  
  https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-19/

- Unicode 17.0 Core Specification, Chapter 22, numeral systems including Kaktovik:  
  https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-22/

- Unicode Aegean script proposal, WG2 N2378:  
  https://unicode.org/wg2/docs/n2378.pdf

- Unicode Aegean proposal/background, L2/97-105:  
  https://www.unicode.org/L2/L1997/97105-Aegean.pdf

- Unicode Glagolitic proposal, N1931:  
  https://unicode.org/wg2/docs/n1931_glagolitic.pdf

## Kaktovik

- Eduardo Marín Silva and Catherine Strand, “Unicode Request for Kaktovik Numerals,” L2/21-058:  
  https://www.unicode.org/L2/L2021/21058-kaktovik-numerals.pdf

- Preliminary Unicode proposal, L2/20-070:  
  https://www.unicode.org/L2/L2020/20070-kaktovik-numerals.pdf

- Unicode names list, U+1D2C0–U+1D2D3:  
  https://unicode.org/charts/nameslist/n_1D2C0.html

- Amory Tillinghast-Raby, “A Number System Invented by Inuit Schoolchildren Will Make Its Silicon Valley Debut,” *Scientific American*, 10 April 2023:  
  https://www.scientificamerican.com/article/a-number-system-invented-by-inuit-schoolchildren-will-make-its-silicon-valley-debut1/

- KTOO, “Numerals invented by Kaktovik students can now be used digitally,” 8 November 2022:  
  https://www.ktoo.org/2022/11/08/inupiaq-number-system-kaktovik/

- NACLO 2022 problem set containing an instructional Kaktovik exercise:  
  https://naclo.org/resources/problems/2022/NACLO2022ROUND1.pdf

## General histories requested for comparison

- Karl Menninger, *Number Words and Number Symbols: A Cultural History of Numbers*, trans. Paul Broneer, MIT Press, 1969; Internet Archive search:  
  https://archive.org/search?query=Menninger+Number+Words+and+Number+Symbols

- Georges Ifrah, *The Universal History of Numbers*, trans. David Bellos et al., Wiley, 2000; catalogue/search:  
  https://archive.org/search?query=Georges+Ifrah+Universal+History+of+Numbers

- Kim Plofker, *Mathematics in India*, Princeton University Press, 2009:  
  https://press.princeton.edu/books/paperback/9780691120676/mathematics-in-india

- Eleanor Robson, *Mathematics in Ancient Iraq: A Social History*, Princeton University Press, 2008:  
  https://press.princeton.edu/books/hardcover/9780691091822/mathematics-in-ancient-iraq

- Jens Høyrup, publications and institutional bibliography:  
  https://rucforsk.ruc.dk/en/persons/jensh/

- Joseph Needham, *Science and Civilisation in China*, vol. 3, Mathematics and the Sciences of the Heavens and the Earth, Cambridge University Press:  
  https://www.cambridge.org/core/books/science-and-civilisation-in-china/43DB5686231B041AA394314A073B5F31

- Jean-Claude Martzloff, *A History of Chinese Mathematics*, Springer:  
  https://link.springer.com/book/10.1007/978-3-540-33783-6

- MacTutor History of Mathematics archive:  
  https://mathshistory.st-andrews.ac.uk/

## Indian zero and manuscripts

- Bodleian Libraries, Bakhshali manuscript project portal:  
  https://www.bodleian.ox.ac.uk/bodley/finding-resources/special-collections/rare-books/bakhshali-manuscript

- Bodleian announcement and radiocarbon interpretation:  
  https://www.ox.ac.uk/news/2017-09-14-earliest-recorded-use-zero-400-years-older-first-thought

- Encyclopaedia and manuscript search portal for Gwalior/Indian inscriptions, Archaeological Survey of India:  
  https://asi.nic.in/

## Wider mathematical texts

- Fibonacci, *Liber Abaci*, Laurence E. Sigler translation, Springer, 2002:  
  https://link.springer.com/book/10.1007/978-1-4613-0079-3

- Internet Archive holdings for *Liber Abaci*:  
  https://archive.org/search?query=Fibonacci+Liber+Abaci+Sigler

- Sacrobosco, *Algorismus* manuscript and printed-edition search:  
  https://archive.org/search?query=Sacrobosco+Algorismus

- Luca Pacioli, *Summa de arithmetica*, digitized-edition search:  
  https://archive.org/search?query=Pacioli+Summa+arithmetica

- Robert Recorde, historical editions:  
  https://archive.org/search?query=creator%3A%22Recorde%2C+Robert%22

## Sinhala documentation

- Sinhala numerals technical proposal:  
  https://www.unicode.org/wg2/docs/n3888.pdf

- “Numeration in Medieval Sri Lanka and Importance of Sinhala Zero”:  
  https://helpcentre.lk/wp-content/uploads/2023/11/Numeration-in-Anceint-Sri-Lanka-and-Importance-of-Sinhala-Zero.pdf

## Caveat on secondary summaries

For navigation and checking terminology, the following synthesis was consulted, but its unsourced claims were not treated as substitutes for King, manuscript catalogues, or Unicode documentation:

- https://en.wikipedia.org/wiki/Cistercian_numerals
- https://en.wikipedia.org/wiki/Aegean_numerals
- https://en.wikipedia.org/wiki/Armenian_numerals
- https://en.wikipedia.org/wiki/Glagolitic_numerals
- https://en.wikipedia.org/wiki/Cyrillic_numerals
- https://en.wikipedia.org/wiki/Kaktovik_numerals

The principal evidentiary conclusion is consequently narrow but firm: the four-quadrant Cistercian notation is a genuinely medieval European, principally monastic development built from an earlier 1–99 cipher tradition; John of Basingstoke’s Greek story is documented as medieval testimony but not corroborated as a literal genealogy; its computational use is unproved; its independent zero is a modern invention; and much of its alleged Chaldean, Kabbalistic, Masonic, or Aryan antiquity belongs to the history of reception rather than to the history of the system itself.
