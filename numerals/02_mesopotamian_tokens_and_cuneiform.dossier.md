# Sumerian and Babylonian numerals (the tokens and the sexagesimal system): Research Dossier

## Editorial method and evidentiary labels

This dossier concerns Mesopotamian numerical notation, especially:

1. prehistoric clay objects conventionally called *tokens*;
2. Late Uruk proto-cuneiform metrological numerations;
3. Sumerian written number systems;
4. the sexagesimal place-value notation used in Ur III and Babylonian mathematics;
5. its continuation in Babylonian astronomy and, indirectly, modern angular and time notation.

It does **not** treat the Ishango and Lebombo bones, Egyptian numerals, Brahmi and Hindu-Arabic numerals, Chinese counting rods, Maya numerals, Roman numerals, or medieval European arithmetic as though they belonged to this lineage. Those items in the general template concern other dossiers in the proposed fourteen-system series. They appear below only when there is a demonstrable comparison or transmission relevant to Mesopotamia.

Claims are marked as follows:

- **[Artefact]**: directly attested object, inscription, excavation record, or museum collection.
- **[Text]**: statement or procedure preserved in an ancient written source.
- **[Reconstruction]**: modern scholarly interpretation derived from artefacts or texts.
- **[Disputed]**: a claim for which substantial alternatives exist.
- **[Tradition]**: an old or recurrent report not independently established as fact.
- **[Legend]**: narrative without adequate historical evidence.
- **[Modern invention]**: recent pedagogical, typographical, popular, or digital convention.
- **[Absence of evidence]**: a commonly imagined practice for which direct evidence is lacking.

Modern transliteration separates sexagesimal positions with commas and the fractional part with a semicolon:

\[
a,b,c;d,e
=
a60^2+b60+c+\frac d{60}+\frac e{60^2}.
\]

This punctuation is **modern**, not Babylonian.

---

## 1. Basic identification

| Field | Identification |
|---|---|
| Name | Sumerian and Babylonian numerals; more exactly, a family of Mesopotamian numerical and metrological notations |
| Best-known form | Sexagesimal place-value notation |
| Principal base | 60 |
| Internal digit construction | Decimal-additive: units 1–9 plus tens 10–50 |
| Structural type | Additive within each place; positional between powers of 60; therefore mixed additive-positional |
| Earlier forms | Commodity- and metrology-dependent additive systems, including sexagesimal, bisexagesimal, capacity, area, ration, and calendrical systems |
| Zero | Initially blank space or contextual absence; later a medial placeholder; never consistently a terminal zero and not an independently operated number |
| Fractions | Sexagesimal fractional places, usually without a written radix point; also special metrological fraction signs |
| Earliest relevant objects | Neolithic clay objects interpreted as counters, from approximately the ninth millennium BCE |
| Earliest writing | Proto-cuneiform accounting tablets, Late Uruk, approximately 3400–3000 BCE |
| Place-value innovation | Late third millennium BCE, with contested exact dating; securely established by the Ur III/early second-millennium transition |
| Classic mathematical use | Old Babylonian period, especially approximately 1900–1600 BCE |
| Astronomical use | Especially first millennium BCE, continuing through Seleucid and Parthian scholarly cuneiform |
| Region | Southern Mesopotamia—principally modern Iraq—with related evidence from Syria, Iran, Turkey, and the broader ancient Near East |
| Languages | Sumerian and Akkadian, including Babylonian and Assyrian dialects; numeral signs were not tied to a single spoken language |
| Modern residue | Sexagesimal subdivision of angular degrees and of hours/minutes, mediated through later astronomy rather than preserved as ordinary Babylonian notation |

**Central qualification.** **[Artefact + Reconstruction]** There was no single unchanged “Sumerian numeral system.” Proto-cuneiform scribes selected different signs and conversion sequences according to what was counted or measured. The familiar abstract sexagesimal place-value notation was a later mathematical development. Jöran Friberg describes its creation as a sequence of innovations rather than the uninterrupted survival of one prehistoric code. [Friberg, “Three Thousand Years of Sexagesimal Numbers”](https://doi.org/10.1007/s00407-019-00221-3)

---

# 2. The system in detail

## 2.1 The two elementary wedges

In mature Babylonian place-value notation, every sexagesimal digit from 1 through 59 was assembled from two elementary sign-types.

| Value | Conventional name | Unicode | Shape in words |
|---:|---|---|---|
| 1 | DIŠ, “one” wedge | 𒁹 U+12079 | A short vertical wedge, made by pressing the stylus point into clay |
| 10 | U, “ten” wedge | 𒌋 U+1230B | A sideways or corner wedge, often described typographically as a left-pointing chevron |

**[Artefact]** The exact shape varies greatly by period, city, scribal hand, stylus angle, and modern font. Unicode characters are encoded sign identities, not photographic replicas of Old Babylonian handwriting.

**[Modern invention]** Textbooks commonly render the unit wedge as `|` and the ten wedge as `<`. This is useful but should not be mistaken for ancient typography.

Within one sexagesimal place:

\[
\text{digit}=10t+u,\qquad 0\le t\le5,\quad 0\le u\le9.
\]

Tens normally precede units. Thus 23 is “two tens, three units.”

This is:

- additive inside the digit: \(20+3\);
- positional between digit groups: for example \(23,4=23\times60+4\).

It is not a true alternating-base 6/10 positional notation. The decimal grouping is a graphic economy used to construct 59 possible nonzero digits; place values themselves advance by powers of 60.

## 2.2 Unicode ligatures and numeric characters

Unicode contains both ordinary cuneiform signs and a special “Cuneiform Numbers and Punctuation” block. Examples include:

- 𒐀 TWO AŠ, U+12400
- 𒐁 THREE AŠ, U+12401
- 𒐇 NINE AŠ, U+12407
- 𒐈 THREE DIŠ, U+12408
- 𒐎 NINE DIŠ, U+1240E
- 𒐏 FOUR U, U+1240F
- 𒐐 FIVE U, U+12410
- 𒐕 ONE GEŠ₂, U+12415
- 𒐞 ONE GEŠU, U+1241E
- 𒐬 ONE ŠARU, U+1242C
- 𒑚 ONE-THIRD DIŠ, U+1245A
- 𒑛 TWO-THIRDS DIŠ, U+1245B
- 𒑜 FIVE-SIXTHS DIŠ, U+1245C.

The official chart warns through its organization that many apparently similar forms belong to different metrological systems. It also includes stacking variants, slanted numerals, capacity signs, area signs, and punctuation. [Unicode names list](https://unicode.org/charts/nameslist/n_12400.html), [Unicode chart PDF](https://www.unicode.org/charts/PDF/U12400.pdf)

**[Modern invention]** Unicode’s names such as “TWO AŠ” or “ONE GEŠU” are modern standardization labels compiled from Assyriological sign lists. They are not a Babylonian catalogue of fonts.

**[Reconstruction]** A single Unicode glyph cannot reproduce the historical distinction among archaic round impressions, Ur III wedge formations, Old Babylonian cursive forms, Neo-Assyrian forms, and Late Babylonian handwriting.

## 2.3 Worked table: 1–20

The “expanded wedges” column makes the additive construction explicit. The “compact Unicode” column uses an encoded ligature where one is convenient. Font support varies.

| Decimal | Sexagesimal digit | Expanded wedges | Compact Unicode |
|---:|---:|---|---|
| 1 | 1 | 𒁹 | 𒁹 |
| 2 | 2 | 𒁹𒁹 | 𒈫 |
| 3 | 3 | 𒁹𒁹𒁹 | 𒐈 |
| 4 | 4 | 𒁹𒁹𒁹𒁹 | 𒐉 |
| 5 | 5 | five vertical wedges | 𒐊 |
| 6 | 6 | six vertical wedges | 𒐋 |
| 7 | 7 | seven vertical wedges | 𒐌 |
| 8 | 8 | eight vertical wedges | 𒐍 |
| 9 | 9 | nine vertical wedges | 𒐎 |
| 10 | 10 | 𒌋 | 𒌋 |
| 11 | 11 | 𒌋𒁹 | 𒌋𒁹 |
| 12 | 12 | 𒌋𒁹𒁹 | 𒌋𒈫 |
| 13 | 13 | 𒌋 + three units | 𒌋𒐈 |
| 14 | 14 | 𒌋 + four units | 𒌋𒐉 |
| 15 | 15 | 𒌋 + five units | 𒌋𒐊 |
| 16 | 16 | 𒌋 + six units | 𒌋𒐋 |
| 17 | 17 | 𒌋 + seven units | 𒌋𒐌 |
| 18 | 18 | 𒌋 + eight units | 𒌋𒐍 |
| 19 | 19 | 𒌋 + nine units | 𒌋𒐎 |
| 20 | 20 | 𒌋𒌋 | 𒎙 |

On actual tablets, the repeated wedges are grouped into compact arrangements. Five through nine are not necessarily long horizontal strings; scribes stack them in recognizable clusters.

## 2.4 Tens

| Decimal | Sexagesimal digit | Expanded | Compact Unicode |
|---:|---:|---|---|
| 10 | 10 | 𒌋 | 𒌋 |
| 20 | 20 | 𒌋𒌋 | 𒎙 |
| 30 | 30 | 𒌋𒌋𒌋 | 𒌍 |
| 40 | 40 | four ten-wedges | 𒐏 |
| 50 | 50 | five ten-wedges | 𒐐 |
| 60 | 1,0 | one unit-wedge in the next position | 𒁹, followed by an empty units position |

The last line exposes the central ambiguity: in early place notation, the written sign for 1, 60, \(60^2\), \(1/60\), and so forth could be identical. The scale came from context.

## 2.5 Powers of ten, hundreds, and thousands

The following are modern conversions into sexagesimal. A colon separates place groups for clarity; the Babylonians did not use these colons.

| Decimal | Sexagesimal | Value analysis | Cuneiform-style rendering |
|---:|---:|---|---|
| 1 | 1 | \(1\) | 𒁹 |
| 10 | 10 | \(10\) | 𒌋 |
| 100 | 1,40 | \(1\times60+40\) | 𒁹 𒐏 |
| 1,000 | 16,40 | \(16\times60+40\) | 𒌋𒐋 𒐏 |
| 10,000 | 2,46,40 | \(2\times3600+46\times60+40\) | 𒈫 𒐏𒐋 𒐏 |
| 100,000 | 27,46,40 | \(27\times3600+46\times60+40\) | 𒎙𒐌 𒐏𒐋 𒐏 |
| 1,000,000 | 4,37,46,40 | \(4\times60^3+37\times60^2+46\times60+40\) | 𒐉 𒌍𒐌 𒐏𒐋 𒐏 |

**[Important qualification]** This table demonstrates place-value mathematics, not necessarily how an administrative scribe would phrase or notate every such quantity. Metrological texts could use named high units or non-place-value forms.

## 2.6 Named large units

Sumerian written-number vocabulary included, with variation by period and scholarly normalization:

| Unit | Approximate numerical role | Conventional reading |
|---|---:|---|
| 1 | 1 | diš |
| 10 | 10 | u |
| 60 | 60 | geš₂ |
| 600 | \(10\times60\) | gešu |
| 3,600 | \(60^2\) | šar₂ |
| 36,000 | \(10\times60^2\) | šaru |
| 216,000 | \(60^3\) | šar-gal, “great šar,” in some lexical traditions |

Akkadian had a largely decimal spoken numeral vocabulary but borrowed or employed high-unit terms including:

- *šūšu/šūši*, 60;
- *nēru*, conventionally 600;
- *šāru*, 3,600.

**[Text + Reconstruction]** The relationship between spoken number words, logographic spellings, metrological units, and mathematical place-value signs changes by corpus. It is unsafe to infer the spoken reading merely from the written numeral.

**[Reconstruction]** The high unit *šar* also acquired senses such as totality or an immense multitude. Modern claims that it always meant exactly 3,600 in every literary occurrence are too rigid.

## 2.7 Ordering of signs

Within a normal place-value digit:

1. tens appear before units;
2. higher sexagesimal positions appear before lower ones;
3. a sufficiently wide gap may mark an empty position;
4. in later texts a placeholder may replace that gap;
5. neither the absolute scale nor the integer/fraction boundary is normally explicit.

Thus:

\[
1,24,51,10
\]

means, depending on scale:

- \(1+\frac{24}{60}+\frac{51}{60^2}+\frac{10}{60^3}\);
- or 60 times that;
- or \(60^2\) times that;
- and so on.

Scholars call this **floating** or **relative** place value.

## 2.8 Zero: four distinct questions

“Did Babylonians have zero?” is too imprecise. Four propositions must be separated.

### No independently operated zero-number

**[Textual absence]** No surviving Babylonian mathematical text gives arithmetic rules for zero comparable to Brahmagupta’s seventh-century CE rules. There is no word functioning throughout Babylonian arithmetic as the number zero, no zero in standard reciprocal tables, and no consistent terminal zero digit.

### Empty places were conceptually necessary

**[Artefact]** Once place notation existed, a number could contain an empty internal position. Scribes sometimes left space. A sequence corresponding to modern \(1,0,1\) could be written as a one-wedge, an enlarged gap, and another one-wedge.

### A medial placeholder appeared later

**[Artefact]** First-millennium and especially Late Babylonian astronomical and mathematical manuscripts employ a sign made from two small oblique wedges as a placeholder in an internal empty place.

**[Disputed terminology]** Calling this sign “zero” is defensible if “zero” means a placeholder digit. It is misleading if “zero” means a number subject to arithmetic.

### Terminal emptiness remained ambiguous

The placeholder was generally not written at the right edge. Hence a written `1` could still mean:

\[
\ldots,\frac1{60},1,60,3600,\ldots
\]

Context, dimensions, expected magnitude, and metrological labels supplied the scale.

**[Modern myth]** “The Babylonians invented zero” conflates placeholder, digit, and number.

**[Opposite modern myth]** “They had no zero at all” erases the later medial placeholder and the deliberate use of blank positions.

## 2.9 Fractions

### Sexagesimal fractions

The same digit sequence extended indefinitely to fractional powers:

\[
0;30=\frac{30}{60}=\frac12
\]

\[
0;20=\frac13
\]

\[
0;15=\frac14
\]

\[
0;12=\frac15
\]

\[
0;10=\frac16.
\]

There was normally no written semicolon and no leading zero. `30` could therefore mean 30, \(1/2\), 1,800, or another scale-equivalent number.

### Regular and irregular reciprocals

A number is sexagesimally **regular** when its prime factors are only 2, 3, and 5. Its reciprocal terminates:

\[
1/8=0;7,30
\]

because:

\[
\frac7{60}+\frac{30}{3600}=\frac18.
\]

Likewise:

\[
1/9=0;6,40.
\]

But:

\[
1/7=0;8,34,17,8,34,17,\ldots
\]

repeats. Babylonian reciprocal tables emphasize regular numbers precisely because division could then be replaced by multiplication by a finite reciprocal.

### Special fraction signs

Metrological notation also possessed special signs for fractions such as:

- 𒑚, one third;
- 𒑛, two thirds;
- 𒑜, five sixths;
- 𒈦, used in a context corresponding to one-half DIŠ;
- distinct signs for fractions of area and capacity units.

These belong to specific notational and metrological environments, not to a universal set of “Babylonian fraction digits.” [Unicode names list](https://unicode.org/charts/nameslist/n_12400.html)

## 2.10 Range and largest expressible numbers

### Theoretical range

**[Reconstruction]** Place-value notation has no intrinsic maximum. More positions produce higher powers of 60. Its written range is limited only by tablet space and legibility.

### Practical lexical range

Named units such as 60, 600, 3,600, 36,000, and 216,000 supplied ways to express large administrative and literary quantities.

### Largest known extended computation

**[Artefact + Reconstruction]** Friberg identified Late Babylonian factorization tables whose initial numbers occupy 25 and 30 sexagesimal places. One 30-place number is interpreted as:

\[
9^{11}\times12^{39}.
\]

Friberg calls it probably the longest number attested from antiquity. “Probably” matters: the corpus is incomplete, and “longest” can mean most written places rather than greatest mathematical magnitude. [Friberg, “Powers of 9”](https://arxiv.org/abs/1306.5989)

## 2.11 Ligatures and abbreviations

- Repeated unit and ten wedges were stacked or ligatured into compact clusters.
- Certain values had separately encoded sign forms, but scribal practice was not a typewriter-like substitution of one character per number.
- Older metrological systems used distinct rounded, impressed, incised, or rotated forms.
- Slanted number signs could serve specialized functions, including calendrical or subtractive notations.
- Unit names could disambiguate the scale.
- Mathematical tables frequently omitted prose and used extremely terse numerical layouts.
- Sexagesimal places were separated principally by visual grouping and spacing, not commas.

**[Modern invention]** Writing every digit with a neat Unicode ligature produces a readable scholarly facsimile, not an exact Old Babylonian autograph.

---

# 3. Famous numbers worked out

## 3.1 The approximation to \(\sqrt2\) on YBC 7289

YBC 7289 gives:

\[
1;24,51,10.
\]

In decimal notation:

\[
1+\frac{24}{60}+\frac{51}{3600}+\frac{10}{216000}
=1.41421296296\ldots
\]

while:

\[
\sqrt2=1.41421356237\ldots
\]

Cuneiform-style digit groups:

- 1: 𒁹
- 24: 𒎙𒐉
- 51: 𒐐𒁹
- 10: 𒌋

Hence:

> 𒁹  𒎙𒐉  𒐐𒁹  𒌋

**[Modern punctuation transliteration]** `1;24,51,10`.

The tablet also shows a square with side `30` and the result:

\[
42;25,35 = 30\times1;24,51,10.
\]

Rendered by groups:

> 𒐏𒈫  𒎙𒐊  𒌍𒐊

The tablet is a small round Old Babylonian school tablet of unknown exact provenance, now in the Yale Babylonian Collection. Its usual date is approximately 1800–1600 BCE. [YBC 7289 teaching and catalogue page](https://myslu.stlawu.edu/~dmel/mesomath/tablets/YBC7289)

**[Reconstruction]** The scale may equivalently be read as a side of \(0;30\) and diagonal \(0;42,25,35\), because the notation floats. The geometric relationship remains the same.

**[Absence of evidence]** The tablet does not prove that its writer knew \(\sqrt2\) was irrational.

## 3.2 The reciprocal pair \(2;24\) and \(0;25\)

A standard school reciprocal pair is:

\[
2;24\times0;25=1.
\]

Verification:

\[
2;24=2+\frac{24}{60}=\frac{12}{5};
\qquad
0;25=\frac{5}{12}.
\]

This pair is central to several reconstructions of Plimpton 322. Old Babylonian multiplication-table curricula began with reciprocal pairs and proceeded through a conventional series of multiplication tables. [Robson, Ashmolean mathematical tablets](https://www.sciamvs.org/files/SCIAMVS_05_003-065_Robson.pdf)

## 3.3 A Plimpton 322 triple

One famous first-row triple in modern integer scaling is:

\[
119^2+120^2=169^2.
\]

Sexagesimally:

- \(119=1,59\)
- \(120=2,0\)
- \(169=2,49\).

Cuneiform-style:

- 119: 𒁹 𒐐𒐎
- 120: 𒈫 with a following empty zero place
- 169: 𒈫 𒐏𒐎.

**[Artefact]** Plimpton 322 preserves fifteen rows of related numerical entries.

**[Reconstruction]** Calling it a list of “Pythagorean triples” accurately describes a modern arithmetical relationship among its entries.

**[Disputed]** Whether its purpose was number theory, reciprocal-pair computation, problem generation, surveying, or “trigonometry” remains debated.

## 3.4 \(1,0,0\): the same inscription, many scales

A one-wedge followed by two empty places can represent:

\[
1,0,0=3600.
\]

But with no explicit boundary it could also be:

\[
1;0,0=1,\qquad
0;1,0=\frac1{60},
\]

or another scale-equivalent value.

This is not scribal incompetence. Babylonian mathematical problems normally supplied dimensions and expected magnitude, just as algebraists may work with a proportional value without specifying units until the end.

---

# 4. Origins: chronological reconstruction

## 4.1 Before clay tokens

### Tally bones

The Lebombo and Ishango bones are sometimes placed at the start of universal histories of numeration.

- **[Artefact]** Both bear sets of incisions and are prehistoric.
- **[Disputed]** Whether every incision series records numerical counting, lunar observation, games, decoration, or something else is uncertain.
- **[Absence of evidence]** No archaeological or historical chain connects either bone to Mesopotamian clay tokens, Sumerian metrology, or sexagesimal notation.

They are therefore comparative evidence for early marking, not ancestors of the Babylonian system.

## 4.2 Neolithic clay objects, approximately 9000–3500 BCE

Small clay cones, spheres, disks, cylinders, tetrahedra, and other objects occur across the Near East.

### Schmandt-Besserat’s thesis

Beginning in publications of the 1970s and culminating in *Before Writing* (1992) and *How Writing Came About* (1996), Denise Schmandt-Besserat argued that:

1. plain tokens represented quantities;
2. complex tokens represented particular commodities;
3. the system began with Neolithic agriculture;
4. tokens were placed in clay envelopes or *bullae*;
5. impressions of tokens on the envelope’s outside made opening unnecessary;
6. two-dimensional impressions and drawn signs eventually replaced the tokens;
7. proto-cuneiform writing therefore grew from token accounting.

**[Artefact]** Tokens and bullae are real, widely distributed objects. Some sealed bullae contain small clay pieces.

**[Reconstruction]** Their identification as a coherent, stable accounting code lasting several millennia is Schmandt-Besserat’s interpretation.

**[Disputed]** Critics including Paul Zimansky, Jöran Friberg, Robert Englund, and later historiographical surveys have raised several objections:

- excavation reports often did not systematically collect or describe tiny clay objects;
- some may be toys, gaming pieces, spindle-related objects, amulets, debris, or objects with changing functions;
- shape alone does not securely establish meaning;
- the geographic and chronological variation is greater than a single code implies;
- proposed commodity identifications sometimes conflict with distribution—for example, an alleged sheep token is scarce where sheep accounting should be common;
- many proposed token-to-sign resemblances are selective;
- a gap remains between possible counting aids and the complex syntax of writing.

A modern survey concludes that token meaning must be reconstructed from archaeological context, not shape resemblance alone. [Overmann et al., “Numeracy at the Dawn of Writing”](https://doi.org/10.1016/j.hm.2020.08.002)

### What can safely be said

- **[Artefact]** Clay objects conventionally called tokens existed long before writing.
- **[Artefact]** Late-fourth-millennium bullae sometimes enclosed such objects and bore external marks.
- **[Strong reconstruction]** At least some late tokens and bullae participated in administration or accounting.
- **[Plausible reconstruction]** Some external impressions represented the contents.
- **[Disputed]** All or most Neolithic geometric pieces formed a uniform numerical code.
- **[Disputed]** Proto-cuneiform signs are straightforward two-dimensional copies of token shapes.
- **[Legend/modern simplification]** “Writing was invented when one Sumerian accountant flattened a token envelope.”

## 4.3 Bullae at Uruk and Susa, approximately 3500–3200 BCE

**[Artefact]** Hollow clay envelopes containing tokens are known from Uruk and Susa.

A particularly important object is:

### Sb 1927, Louvre/Susa collection

- Site: Susa, modern Iran.
- Collection number: Sb 1927.
- Date: late fourth millennium BCE, proto-Elamite horizon.
- Object: inscribed bulla containing tokens.
- Present collection: Musée du Louvre.

Friberg describes one large conical token, smaller cones, round pieces, and lenses. Marks on the outside appear to correspond numerically to the contents.

**[Reconstruction]** Friberg proposes that the token classes represent units such as 10, 60, and \(10\times60\), related to the sexagesimal S system.

**[Disputed]** The numerical identifications are not equivalent to a deciphered verbal inscription. Friberg appropriately calls the correspondence conjectural. [Friberg full text](https://research.chalmers.se/publication/508683/file/508683_Fulltext.pdf)

## 4.4 Proto-cuneiform Uruk, approximately 3400–3000 BCE

Thousands of tablets and fragments from Uruk IV and Uruk III administrative contexts constitute the earliest large written corpus.

### Date and place

- Uruk, southern Mesopotamia, especially the Eanna precinct.
- Uruk IV: conventionally approximately 3400/3350–3200 BCE.
- Uruk III/Jemdet Nasr: approximately 3200–3000 BCE.
- Exact absolute dates vary with archaeological chronology.

### Earliest numeral-bearing tablets

**[Artefact]** Administrative tablets include impressed and incised numerical signs alongside commodity and official signs. A representative published example is Uruk tablet W 20044, from an Uruk IV context, showing more than one numerical/metrological system.

**[Reconstruction]** The tablets are usually called proto-cuneiform because many signs remain undeciphered and their relationship to later cuneiform is developmental rather than identical.

### Several systems, not one

Robert Englund, Peter Damerow, Hans Nissen, Jöran Friberg, and collaborators reconstructed multiple systems, conventionally labeled:

- sexagesimal S;
- sexagesimal S′;
- bisexagesimal B;
- bisexagesimal B*;
- grain-capacity ŠE and variants;
- area GAN₂/G;
- time or calendrical U₄;
- EN;
- vessel-capacity systems DUG.

Counts in modern literature vary—twelve, thirteen, or more—because scholars group variants differently.

Typical associations include:

- S for discrete objects such as people, animals, tools, and containers;
- B for rationed grain products;
- ŠE for grain capacity;
- GAN₂ for land area;
- specialized variants for malt, groats, beer, or particular rations.

**[Artefact + Reconstruction]** The same graphic impression could represent different numerical magnitudes depending on the governing system. Quantity was therefore not wholly abstracted from the kind or measure of the thing counted.

**[Disputed formulation]** Some writers say “abstract number did not yet exist.” The evidence proves that notational systems remained semantically tied to commodities and measures; it cannot prove what every Uruk accountant was cognitively capable of conceiving.

## 4.5 Why 60?

No Mesopotamian text says, “We selected 60 because…”.

### Divisor-efficiency theory

Sixty factors as:

\[
60=2^2\times3\times5
\]

and has divisors:

\[
1,2,3,4,5,6,10,12,15,20,30,60.
\]

**[Reconstruction]** This makes common fractions terminate conveniently and helps explain the system’s longevity.

**[Absence of evidence]** It does not establish why the system first arose. Utility after adoption is not proof of original motivation.

### Fusion of decimal and seximal counting

The numeral graph uses groups of ten within a cycle of sixty.

**[Reconstruction]** Some scholars have proposed interaction between a decimal system and a system based on six.

**[Disputed]** Older ethnic versions of this theory imagined two peoples, one counting by tens and the other by sixes, merging their systems. Evidence for such population-specific bases is lacking.

### Finger-joint theory

A popular demonstration counts twelve finger segments with the thumb of one hand and records five twelves on the other:

\[
12\times5=60.
\]

**[Modern pedagogical tradition]** This is a physically workable technique.

**[Absence of evidence]** No surviving Sumerian or Babylonian text or image explains sexagesimal origins in this way. Statements that “the Sumerians counted this way” often present possibility as fact.

### The 360-day year theory

Six sixties make 360, near the number of days in a solar year.

**[Tradition/Reconstruction]** Astronomy and schematic 360-day calendars made 360 culturally important.

**[Chronological problem]** Sexagesimal counting appears in accounting contexts earlier than the mathematical astronomy usually invoked to explain it. The calendar may have reinforced 60 and 360 without originating them.

### Language-and-writing theory

Thorkild Jacobsen and later analysts explored the interaction between Sumerian numeral words and written numerical sequences.

**[Reconstruction]** The sudden maturation of place-value notation around 2100–2000 BCE may reflect a conscious scribal invention built from older linguistic and graphic structures. [“Origin of the Sexagesimal System”](https://journals.uc.edu/index.php/vl/article/view/5115)

### Best conclusion

The divisor structure explains mathematical attractiveness; metrological convergence and scribal practice explain institutional survival. The original selection of 60 remains open.

## 4.6 Early Dynastic and Akkadian developments, approximately 2900–2150 BCE

**[Artefact]** Numerical and metrological records proliferated through the Early Dynastic city-states and Akkadian imperial administration.

Developments included:

- replacement of many rounded impressions with sharper wedge forms;
- regularization of capacity, weight, length, area, and labor accounting;
- co-existence of decimal counting, sexagesimal high units, and metrological conversion chains;
- use of large round-number units such as 3,600;
- numerical rhetoric in royal inscriptions.

**[Reconstruction]** Administrative standardization encouraged conversion tables and numerical abstraction, but development was neither uniform nor irreversible.

## 4.7 Ur III and the place-value breakthrough, approximately 2112–2004 BCE

### Traditional account

The Third Dynasty of Ur created a highly bureaucratic state. Tens of thousands of administrative tablets record workers, animals, fields, grain, silver, textiles, and time.

**[Artefact]** Ur III tablets exhibit mature numerical and metrological expertise.

### Dating place-value notation

Friberg places the invention of extended sexagesimal place-value numbers in the Neo-Sumerian period around 2000 BCE. A significant text is:

- **YOS 4, 293**
- Ur III or the Ur III/early second-millennium transition
- contains sexagesimal numbers interpreted positionally.

**[Disputed]** Damerow and Englund have favored a later or more cautious dating, emphasizing that unambiguous place value requires proof that identical digit forms occupy systematically different powers without attached metrological units.

**[Scholarly issue]** A sign sequence can be read positionally by a modern editor even when the scribe may have conceptualized it through named units or quasi-integers. The transition was therefore probably gradual.

### Innovations attributed to this transition

Friberg reconstructs:

1. extension to indefinitely high places;
2. extension downward to fractional places;
3. abandonment of older quasi-integer devices in mathematical calculation;
4. creation of reciprocal tables;
5. separation between calculation numbers and metrological statements.

By the Old Babylonian period, the system is unmistakably established. [Friberg](https://doi.org/10.1007/s00407-019-00221-3)

## 4.8 Old Babylonian florescence, approximately 1900–1600 BCE

This is the best-attested period for elementary and advanced cuneiform mathematics.

Important centers include:

- Nippur;
- Sippar;
- Ur;
- Larsa;
- Babylon;
- Eshnunna;
- Susa;
- Mari and other neighboring traditions.

Texts include:

- multiplication tables;
- reciprocal tables;
- square and square-root tables;
- metrological lists;
- coefficient lists;
- geometric problems;
- linear and quadratic problems;
- excavation and brick problems;
- canal and field calculations;
- inheritance, interest, and commercial calculations;
- problem collections apparently used by advanced scribes.

The questions and answers often employ concrete units, while intermediate work uses floating place-value numbers.

---

# 5. Arithmetic and instruments

## 5.1 Scribal education

### House F at Nippur

**[Artefact]** An eighteenth-century BCE domestic building at Nippur, called House F by archaeologists, yielded more than 1,400 school tablets and fragments.

**[Reconstruction]** Correlations between tablet format, handwriting, copying errors, and content permit a reconstruction of elementary training.

The curriculum included:

1. individual wedge forms;
2. syllabic exercises;
3. personal names;
4. thematic lexical lists;
5. metrological tables;
6. multiplication and reciprocal tables;
7. model contracts and proverbs;
8. advanced Sumerian compositions.

Mathematical and metrological tablets made up approximately 10 percent of the House F assemblage. [Robson, “Tablet House”](https://shs.cairn.info/journal-revue-d-assyriologie-2001-1-page-39?lang=en)

Tablet formats included:

- teacher-and-student copies;
- small extracts memorized by pupils;
- round “lentil” exercises;
- large multicolumn compilations;
- prisms containing longer series.

**[Reconstruction]** School was not necessarily a separate state institution called an *edubba*. Domestic instruction by literate specialists better fits several excavated contexts.

## 5.2 Addition and subtraction

Addition could be performed by combining corresponding sexagesimal places and carrying at 60.

Example:

\[
25,48+17,35.
\]

Lower place:

\[
48+35=83=1\times60+23.
\]

Carry 1:

\[
25+17+1=43.
\]

Answer:

\[
43,23.
\]

Subtraction used complementary reasoning and borrowing from a higher place as 60.

**[Textual caution]** Surviving tablets usually record problems, tables, and results rather than every transient hand movement. Modern long-column reconstructions may reproduce the arithmetic but not the physical procedure.

## 5.3 Multiplication

Multiplication was heavily table-based.

Robson’s reconstruction of the standard Old Babylonian series begins with reciprocal pairs, then multiplication tables arranged in a conventional descending sequence—50, 48, 45, 44;26,40, 40, and so on, ending around 1;15. Individual tables ordinarily list multiples 1–20, then 30, 40, and 50. [Robson, Ashmolean corpus](https://www.sciamvs.org/files/SCIAMVS_05_003-065_Robson.pdf)

A typical entry has the form:

> “\(n\) times \(m\) is \(nm\).”

Some tablets use a full verbal expression; revision tablets use terse numerical entries.

Large products could be decomposed into known table factors and added. A rare Late Babylonian tablet, BM 34601, has been reconstructed as using a slanting arrangement of partial products.

## 5.4 Division as multiplication by a reciprocal

The core technique was:

\[
a\div b=a\times\frac1b.
\]

For regular \(b\), the reciprocal terminates in base 60.

Example:

\[
10\div8.
\]

Because:

\[
1/8=0;7,30,
\]

then:

\[
10\times0;7,30=1;15.
\]

The Akkadian term *igi* and its Sumerian-written forms are conventionally translated “reciprocal,” literally involving the “front” or “face” of a number.

**[Reconstruction]** “Division” is a convenient modern label; scribes may have conceptualized operations as finding the reciprocal and “raising” or multiplying.

## 5.5 Squares, roots, and approximation

Tables supplied squares and square roots. For a nonsquare quantity, scribes could use iterative approximations.

A method attested in the wider cuneiform corpus is equivalent to:

\[
x_{n+1}=\frac12\left(x_n+\frac{S}{x_n}\right),
\]

now often called the Babylonian method or Heron’s method.

**[Text + Reconstruction]** Related procedures occur on BM 96957 + VAT 6598. YBC 7289 itself gives the constant for \(\sqrt2\), but does not show the steps used to produce it.

**[Modern myth]** Calling every later use of this recurrence a direct, continuous borrowing from Babylon is unwarranted unless transmission is documented.

## 5.6 “Algebra”

Old Babylonian problems determine unknown lengths, widths, areas, volumes, and quantities through prescribed operations.

A familiar type asks for the sides of a rectangle given:

- their area;
- their sum or difference.

A modern rendering yields a quadratic equation, but Jens Høyrup argues that the operative vocabulary distinguishes geometrically meaningful actions:

- “join”;
- “hold”;
- “make square”;
- “break off”;
- “raise”;
- “tear out” or extract.

His “conformal translations” preserve those distinctions rather than translating everything into symbolic algebra. [Høyrup, *Lengths, Widths, Surfaces*](https://books.google.com/books/about/Lengths_Widths_Surfaces.html?id=GavTBwAAQBAJ)

**[Disputed terminology]**

- “Babylonian algebra” is acceptable as a comparative description of problem structure.
- It becomes anachronistic if it implies equations written with variables, coefficients, and equality signs.
- Høyrup reconstructs cut-and-paste geometry from language and numerical structure; literal physical cutting is not directly depicted in most manuscripts.

## 5.7 Writing surfaces and calculating instruments

### Clay tablets and stylus

**[Artefact]** The primary surviving instrument is the clay tablet. A reed stylus produced wedges; errors could be smoothed away while the clay remained moist. Tablets could be dried, recycled, accidentally fired, or deliberately preserved.

### Dust boards or temporary surfaces

**[Reconstruction]** Some calculations were probably carried out on perishable or erasable surfaces before results were copied.

### Counting boards and abaci

**[Disputed]** Older histories sometimes state that Babylonians invented or used an abacus.

Possible evidence includes:

- lexical references interpreted as boards;
- the convenience of manipulating place-value counters;
- layouts that may reflect intermediate columns;
- the likelihood that not every calculation was performed directly in permanent clay.

Against a confident claim:

- no securely identified Babylonian counting board with an intact set of counters and explicit operating instructions survives;
- no image unambiguously shows a Babylonian abacus in use;
- place-value notation does not logically require a physical abacus.

Therefore:

- **[Possible reconstruction]** Counters or boards may have been used.
- **[Absence of evidence]** Their precise form and rules are unknown.
- **[Modern myth]** The Chinese *suanpan*, Japanese *soroban*, Roman hand abacus, and medieval European counting table cannot be projected backward onto Babylonia.

### Finger reckoning

Finger counting is anthropologically plausible, but no source demonstrates a standard Babylonian 12-joint-times-five procedure.

## 5.8 Metrology as practical arithmetic

Mesopotamian calculation was inseparable from measurement.

Important structures included:

- 60 shekels to a mina in important weight traditions;
- 60 minas to a talent;
- grain-capacity systems with sexagesimal and non-sexagesimal subdivisions;
- length units used for fields, canals, and construction;
- area units such as the *iku* and *bùr*;
- labor accounting in days and work rates;
- schematic years and months.

**[Qualification]** Unit systems varied by place and time. A clean modern chart can conceal reforms, local variants, and the difference between normative tables and actual accounts.

## 5.9 Surviving “textbooks”

There is no Babylonian book with a title and continuous exposition exactly equivalent to Euclid or the *Nine Chapters*. The textbook tradition consisted chiefly of:

- tables;
- model problems;
- problem collections;
- teacher copies;
- student exercises;
- metrological sequences;
- lexical and coefficient lists.

### Important corpora and editions

- François Thureau-Dangin, *Textes mathématiques babyloniens* (1938).
- Otto Neugebauer, *Mathematische Keilschrift-Texte*, 3 volumes (1935–1937).
- Otto Neugebauer and Abraham Sachs, *Mathematical Cuneiform Texts* (1945).
- E. M. Bruins and M. Rutten, *Textes mathématiques de Suse* (1961).
- Eleanor Robson, *Mesopotamian Mathematics, 2100–1600 BC* (1999).
- Jens Høyrup, *Lengths, Widths, Surfaces* (2002).
- Jöran Friberg, *A Remarkable Collection of Babylonian Mathematical Texts* (2007).
- Eleanor Robson, *Mathematics in Ancient Iraq* (2008).

The Rhind Papyrus, *Nine Chapters*, Āryabhaṭa, Brahmagupta, al-Khwārizmī, Fibonacci, Sacrobosco, Pacioli, and Recorde belong to other textual traditions. None is a Babylonian arithmetic textbook, although Greek, Indian, and Islamic astronomy eventually inherited sexagesimal techniques.

---

# 6. Principal artefacts

## 6.1 W 20044

- **Site:** Uruk.
- **Date:** Uruk IV, approximately 3350–3200 BCE.
- **Type:** proto-cuneiform administrative tablet.
- **Importance:** illustrates simultaneous use of distinct metrological systems rather than one abstract numeral code.
- **Reading:** developed through work by Englund, Damerow, Nissen, Friberg, and CDLI collaborators.
- **Status:** **[Artefact]** signs and layout; **[Reconstruction]** exact system assignments and commodity relations.

## 6.2 Sb 1927

- **Site:** Susa.
- **Museum:** Musée du Louvre.
- **Number:** Sb 1927.
- **Date:** late fourth millennium BCE.
- **Type:** bulla with tokens and external impressions.
- **Importance:** unusually direct evidence connecting enclosed objects and surface markings.
- **Status:** **[Artefact]** object and contents; **[Reconstruction]** precise sexagesimal values.

## 6.3 YOS 4, 293

- **Period:** Ur III or transition around 2000 BCE.
- **Importance:** cited in the debate over the first sexagesimal place-value notation.
- **Status:** **[Artefact]** written number sequence; **[Disputed reconstruction]** degree to which it proves fully abstract place value.

## 6.4 Plimpton 322

- **Date:** Old Babylonian, commonly approximately 1800 BCE.
- **Likely origin:** southern Iraq; sometimes associated through the antiquities trade with Larsa/Senkereh, but archaeological provenance is not secure.
- **Collection:** Columbia University Rare Book and Manuscript Library.
- **Number:** Plimpton 322.
- **Acquisition history:** bought by George Arthur Plimpton from the dealer Edgar J. Banks in the 1920s; later donated to Columbia.
- **Publication:** Otto Neugebauer and Abraham Sachs gave the canonical mathematical publication in 1945.
- **Contents:** fifteen preserved rows, three main numerical columns plus row numbers, with the left edge broken.
- **Importance:** numbers related to right triangles and reciprocal pairs.

### Interpretive history

- Neugebauer and Sachs: Pythagorean-number interpretation.
- Evert Bruins: reciprocal pairs.
- Jöran Friberg: systematic generation of triples.
- Eleanor Robson, 2001: culturally contextual reassessment; probably a teacher’s aid for constructing reciprocal-pair and quadratic problems, not trigonometry or Greek-style number theory.
- Daniel Mansfield and Norman Wildberger, 2017: argued for an exact sexagesimal trigonometric table, possibly useful in surveying.

**[Consensus-level fact]** The surviving numbers satisfy right-triangle relations under suitable scaling.

**[Disputed]** The purpose of the table.

**[Weakly supported modern publicity]** “The world’s oldest and most accurate trigonometric table.” Critics note:

- no angles appear;
- no sine, cosine, tangent, or chord function appears;
- the columns are not labeled as angular functions;
- the table fits an Old Babylonian reciprocal-and-quadratic curriculum;
- “more accurate” compares unlike systems because finite sexagesimal ratios are exact by construction.

Robson’s article remains a central corrective. [Robson, “Neither Sherlock Holmes nor Babylon”](https://ora.ox.ac.uk/objects/uuid%3Ae3d8eedb-e745-45b3-8612-71f8951599aa)

## 6.5 YBC 7289

- **Collection:** Yale Babylonian Collection.
- **Number:** YBC 7289.
- **Date:** approximately 1800–1600 BCE.
- **Provenance:** unknown; likely southern Mesopotamia.
- **Form:** small round school or “hand” tablet.
- **Contents:** square and diagonals; 30 on one side; `1;24,51,10`; product `42;25,35`.
- **Importance:** very accurate approximation to \(\sqrt2\).
- **Acquisition context:** part of the early Yale Babylonian collection associated with J. P. Morgan’s acquisitions/bequest.
- **Status:** **[Artefact]** diagram and numbers; **[Reconstruction]** classroom use and whether the constant was copied from a list.

## 6.6 BM 13901

- **Collection:** British Museum.
- **Number:** BM 13901.
- **Date:** Old Babylonian.
- **Contents:** a collection of quadratic or “square” problems.
- **Importance:** central to Høyrup’s contextual interpretation of Babylonian algebra.
- **Status:** **[Text]** algorithms framed as lengths, widths, and surfaces; modern symbolic equations are translations.

## 6.7 VAT 8389 and related legal-economic mathematics

Old Babylonian tablets combine mathematical reasoning with interest, partnership, inheritance, and surveying.

**[Text]** Problems may be stylized school exercises rather than records of actual lawsuits or transactions.

## 6.8 BM 34601

- **Date:** Late Babylonian/Seleucid.
- **Collection:** British Museum.
- **Importance:** exceptionally elaborate computation, reconstructed as squaring a thirteen-place sexagesimal number through partial products.
- **Status:** **[Artefact + Reconstruction]** evidence for written large-number calculation; exact procedural reconstruction remains scholarly.

## 6.9 Late Babylonian astronomical tablets

Ephemerides and procedure texts from Babylon and Uruk use many-place sexagesimal numbers to predict:

- lunar and planetary positions;
- lunar velocity;
- syzygies;
- eclipses;
- calendar phenomena.

The ACT corpus was published by Otto Neugebauer in *Astronomical Cuneiform Texts* (1955). Abraham Sachs classified and edited many related texts.

**[Artefact]** These tablets prove systematic numerical predictive astronomy.

**[Reconstruction]** Modern algebraic functions called “System A” and “System B” summarize procedures that Babylonian texts express tabularly rather than with modern functions.

---

# 7. Transmission and replacement

## 7.1 Within Mesopotamia

The notation moved across:

- Sumerian-speaking administrations;
- Akkadian imperial and local traditions;
- Old Babylonian schools;
- Kassite, Middle Babylonian, Assyrian, Neo-Babylonian, Seleucid, and Parthian scholarly communities.

Cuneiform numerals survived language shift because scribes continued to learn Sumerian logograms, metrology, lexical lists, and mathematical tables.

Ordinary administration increasingly used Aramaic and alphabetic media during the first millennium BCE, while specialist cuneiform endured in temples and scholarly families.

## 7.2 Mesopotamia and Elam

Proto-Elamite accounting shares several numerical systems or structural correspondences with Late Uruk notation.

**[Reconstruction]** Englund and Damerow have argued for dependence or strong stimulus from Uruk accounting during the “Uruk expansion.”

**[Disputed]** Shared numerical devices do not imply that proto-Elamite language or its entire script derived from Sumerian.

## 7.3 Babylonian astronomy and Greek science

From the Hellenistic period, Greek astronomers acquired substantial Babylonian observational and computational material.

Documented or strongly reconstructed areas include:

- eclipse periods;
- lunar and planetary observations;
- zodiacal division;
- sexagesimal fractions;
- astronomical period relations.

Hipparchus, second century BCE, used Babylonian-derived astronomical data or parameters. Ptolemy, second century CE, used sexagesimal fractions extensively in the *Almagest*.

Greek notation used alphabetic numerals rather than cuneiform wedges, but positional sexagesimal fraction technique could be retained. Ptolemaic manuscripts use a small circle-like sign in some empty positions.

**[Disputed]** The Greek sign is sometimes called a zero. It functioned as a placeholder, but its exact graphic and conceptual relationship to Babylonian placeholder signs is not a simple case of copying one glyph.

## 7.4 Degrees

The claim “Babylonians invented the 360-degree circle” requires division.

- **[Text/Artefact]** Mesopotamian astronomy used 360-day schematic years and divided the ecliptic into twelve zodiacal signs.
- **[Artefact]** Late Babylonian texts used degrees or degree-like units within the zodiac.
- **[Reconstruction]** A 360-part circle harmonized with sexagesimal computation and the zodiac.
- **[Transmission]** Greek astronomy adopted and formalized sexagesimal angular measurement.
- **[Overstatement]** The exact modern geometric degree, with all its present uses, was not created in one datable Babylonian act.

## 7.5 Hours, minutes, and seconds

The modern statement “Babylonians gave us 60 minutes in an hour” compresses several histories.

- Dividing day and night into twelve hours has important Egyptian antecedents.
- Mesopotamian astronomy used sexagesimal fractions of temporal units.
- Hellenistic astronomy combined traditions.
- Greek sexagesimal subdivisions passed into Latin, Arabic, and medieval European astronomy.
- Latin *pars minuta prima*, “first diminished part,” produced *minute*.
- *Pars minuta secunda*, “second diminished part,” produced *second*.

Thus:

- **[Transmission]** Sexagesimal subdivision is substantially Mesopotamian in mathematical ancestry.
- **[Etymology]** The English words *minute* and *second* are Latin, not Sumerian or Akkadian.
- **[Modern simplification]** The modern clock was not directly handed down unchanged from Babylon.

## 7.6 India and the Islamic world

Indian astronomers used sexagesimal subdivisions and astronomical parameters transmitted through combinations of Greek and other sources. Islamic astronomers inherited Greek, Indian, and directly or indirectly Near Eastern practices, producing extensive sexagesimal tables.

This is not the same route as the decimal place-value numerals:

> India → Baghdad → al-Andalus/Italy.

That route concerns Hindu-Arabic decimal digits. Sexagesimal astronomical calculation had a partially overlapping but older and more complex Mediterranean and Near Eastern history.

## 7.7 Medieval and early modern Europe

Astronomers continued to calculate in sexagesimal fractions. Tables frequently used degrees, minutes, and seconds.

By the sixteenth and seventeenth centuries, decimal fractions increasingly competed with sexagesimal fractions outside astronomy.

### Napier

John Napier’s logarithms were developed in an astronomical environment where sexagesimal tables were normal.

**[Historical connection]** Logarithms reduced multiplication and division in astronomical work.

**[Overstatement]** Napier did not revive Babylonian cuneiform arithmetic or directly borrow from Babylonian tablets, which had not yet been deciphered.

## 7.8 Modern survival

Sexagesimal structure survives in:

- 60 seconds per minute;
- 60 minutes per hour;
- 60 arcseconds per arcminute;
- 60 arcminutes per degree;
- geographic latitude and longitude;
- right ascension in astronomy;
- some traditional astronomical tables and computer data formats.

**[Modern systems]** Contemporary notation normally supplies explicit separators and zeros:

- `12:05:09`;
- \(23^\circ 14' 08''\).

This removes ambiguities tolerated in cuneiform.

**[No direct survival]** Ordinary modern users do not use the Babylonian two-wedge digit inventory or floating scale.

---

# 8. People

## 8.1 Ancient people

### Anonymous accountants of Uruk

The creators of proto-cuneiform numerical records are unnamed.

**[Artefact]** Their administrative work is visible.

**[Absence of evidence]** No known individual can securely be called “the inventor of sexagesimal.”

### Ur III administrators

Named scribes appear in administrative colophons and sealings, but the invention of place value cannot be assigned to one of them.

### Old Babylonian teachers and pupils

School tablets preserve personal names and occasional colophons.

**[Reconstruction]** Errors, erasures, teacher copies, and repeated exercises identify learning stages.

### Kidinnu and Naburimannu

These names are associated in later Greco-Roman tradition and cuneiform colophons with Babylonian astronomy.

**[Disputed]** Older histories assigned entire astronomical “systems” to individual geniuses. Modern scholarship is more cautious: System A and System B likely arose through cumulative scholarly traditions, and the attribution of specific inventions to Kidinnu or Naburimannu is uncertain.

## 8.2 Modern decipherers

### Georg Friedrich Grotefend, 1775–1853

His work on Old Persian royal names helped open the multilingual path to cuneiform decipherment.

### Henry Creswicke Rawlinson, 1810–1895

Copied and studied the Behistun inscription. His Old Persian work was crucial, though his early Babylonian readings contained major errors.

### Edward Hincks, 1792–1866

Recognized essential features of Akkadian cuneiform:

- syllabic values;
- logograms;
- polyphony;
- the non-alphabetic character of the script.

### Jules Oppert, 1825–1905

Contributed to decipherment and promoted recognition of Sumerian as the language behind the older non-Semitic layer.

### William Henry Fox Talbot, 1800–1877

One of the four participants in the Royal Asiatic Society’s 1857 test in which independent translations of an Assyrian inscription were compared.

**[Documented history]** Decipherment was cumulative and competitive.

**[Legend]** Rawlinson single-handedly “cracked cuneiform” on a cliff.

## 8.3 Historians of Mesopotamian mathematics

### François Thureau-Dangin, 1872–1944

Published foundational editions and translations of mathematical tablets.

### Otto Neugebauer, 1899–1990

Systematized the mathematical reading of cuneiform texts and published *Mathematische Keilschrift-Texte* and *Astronomical Cuneiform Texts*.

### Abraham Sachs, 1914–1983

Collaborated on *Mathematical Cuneiform Texts* and transformed the study of Late Babylonian astronomy.

### Bartel van der Waerden, 1903–1996

Popularized a strongly achievement-centered account of Babylonian mathematics in *Science Awakening*.

### Denise Schmandt-Besserat, born 1933

Catalogued thousands of possible tokens and formulated the influential token-to-writing hypothesis.

### Peter Damerow, 1939–2011

Worked on the cognition, notation, and historical development of early numerical systems.

### Robert K. Englund, 1952–2020

A leading scholar of proto-cuneiform administration and co-founder of the Cuneiform Digital Library Initiative.

### Jöran Friberg, 1934–2024

Reconstructed archaic numerical systems and numerous Babylonian table-making procedures.

### Jens Høyrup, born 1943

Developed philologically sensitive interpretations of Old Babylonian problem procedures.

### Eleanor Robson, born 1969

Situated mathematical texts in their archaeological, political, and pedagogical settings; reassessed Plimpton 322 and reconstructed Nippur school practice.

### Christine Proust

Reconstructed mathematical education and calculation at Nippur and emphasized distinctions between metrological notation and floating calculation.

---

# 9. Culture and social use

## 9.1 Administration and law

Numerals recorded:

- grain deliveries;
- livestock;
- rations;
- labor days;
- land;
- canal dimensions;
- silver;
- loans and interest;
- rents;
- taxes and obligations;
- temple and palace inventories.

Contracts could be enclosed in clay envelopes carrying duplicate text. In a dispute, the envelope could be broken and the inner tablet consulted.

This resembles earlier bullae only at a broad technological level. A second-millennium legal envelope is not a direct survival of a Neolithic token bulla.

## 9.2 Royal numbers

Kings used large quantities to describe:

- troops;
- captives;
- booty;
- building materials;
- offerings;
- regnal achievements.

**[Text]** Such numbers are documented rhetorical claims.

**[Reconstruction]** Administrative plausibility may sometimes be assessed.

**[Caution]** A numerically exact inscription need not be statistically reliable.

## 9.3 The Sumerian King List

The King List assigns fantastically long reigns to antediluvian and early rulers, often built from sexagesimally round quantities.

- **[Text]** The manuscript tradition contains these figures.
- **[Reconstruction]** Sexagesimal patterning supports deliberate literary or numerological construction.
- **[Tradition]** The list presents kingship as descending from heaven and moving between cities.
- **[Legend]** Treating every reign as literal solar chronology and using it to calculate prehistoric human longevity.
- **[Modern invention]** Claims that the figures encode extraterrestrial orbital cycles or hidden modern science lack textual support.

## 9.4 Divine numbers

Mesopotamian scholarly traditions assigned numbers to major deities, for example:

- Anu: 60;
- Enlil: 50;
- Ea/Enki: 40;
- Sîn: 30;
- Šamaš: 20;
- Ištar: 15;
- Adad: 10.

**[Textual tradition]** These occur in first-millennium learned lists and divine-name writings.

**[Interpretation]** The descending values reflect divine hierarchy and numerical theology.

**[Modern myth]** Modern charts that map these values onto Kabbalah, chakras, planets, or invented “Sumerian sacred geometry” generally combine unrelated traditions.

## 9.5 Calendars

Mesopotamian calendars were lunar, with months beginning by lunar observation and intercalation maintaining seasonal alignment.

Sexagesimal arithmetic assisted:

- month lengths;
- schematic 30-day months;
- 360-day administrative years;
- astronomical periods;
- eclipse cycles.

**[Simplification]** The actual Babylonian year was not permanently fixed at 360 days. Intercalary months were essential.

## 9.6 Astronomy and astrology

Numbers governed:

- lunar visibility;
- planetary synodic phenomena;
- eclipse possibilities;
- zodiacal longitude;
- calendar regulation;
- omen series.

**[Modern distinction]** Astronomy and astrology were not institutionally separated in the modern way. Nonetheless, numerical predictive schemes and omen interpretation were distinct genres with different procedures.

## 9.7 Literature

Sexagesimal round numbers could signal:

- completeness;
- magnitude;
- divine order;
- conventional exaggeration.

The word *šar* could evoke both a numerical unit and totality.

**[Caution]** Numerological interpretations should begin with attested lexical lists and scribal conventions, not search texts for arbitrary modern patterns.

## 9.8 Coins and monumental dates

Mesopotamian numerals occur extensively on tablets, bricks, seals, weights, and inscriptions. Coinage entered Mesopotamia comparatively late and usually bore Greek, Aramaic, or later scripts rather than classic Old Babylonian place-value notation.

**[Absence of evidence]** The system did not develop a Roman-style monumental numeral tradition continuing visibly on modern buildings.

## 9.9 Typography and digital culture

Modern Assyriological typography has passed through:

1. hand copies;
2. engraved or lithographed sign forms;
3. specialist cuneiform fonts;
4. ASCII transliteration;
5. Unicode.

Old-style and lining decimal figures are unrelated typographic developments.

Modern converters that produce “Babylonian numerals” typically:

- use a single standardized glyph style;
- insert modern spacing;
- assume an explicit integer boundary;
- suppress metrological variation.

They are educational tools, not universal transliterators of ancient accounting.

---

# 10. Controversies and disputes

## 10.1 Did tokens create writing?

### Strong thesis

Schmandt-Besserat argues for a continuous progression:

> token → bulla → impressed bulla → tablet → writing.

Evidence:

- long-lived clay geometric objects;
- bullae containing counters;
- exterior impressions corresponding in some cases to contents;
- formal similarities between some tokens and early signs;
- accounting as a dominant function of early tablets.

### Critical position

Critics argue:

- not all “tokens” are demonstrably counters;
- meanings change through time and place;
- excavation collection is biased;
- resemblance is not descent;
- commodity interpretations are often unverifiable;
- early writing includes complex administrative structures not explained by simple one-token/one-sign substitution.

### Assessment

- Late token/bulla accounting is strongly supported.
- A role in the emergence of numerical notation is plausible.
- A single 6,000-year, pan–Near Eastern code is not demonstrated.
- The origin of writing cannot be reduced to copying token shapes.

## 10.2 When was place value invented?

### Ur III/Neo-Sumerian dating

Friberg and others identify fully significant developments around 2100–2000 BCE, including YOS 4, 293.

### Later cautious dating

Damerow, Englund, and related scholarship stress that unambiguous abstract place value becomes much more secure in Old Babylonian mathematical texts.

### Why the dispute exists

A sequence may behave mathematically like place value while remaining embedded in metrological conversion. Scholars disagree about the threshold for calling it:

- positional notation;
- abstract number;
- floating calculation;
- a conversion shorthand.

### Firm finding

By approximately 1800 BCE, Old Babylonian school mathematics unmistakably uses sexagesimal place-value calculation.

## 10.3 Did the Babylonians invent zero?

Three answers correspond to three definitions:

| Meaning of zero | Answer |
|---|---|
| Empty place recognized contextually | Yes |
| Written medial placeholder | Yes, in later first-millennium practice |
| Number with general arithmetic rules | No surviving evidence |

The placeholder was not routinely terminal, so it did not fully fix magnitude.

**[Disputed first]** Dating the earliest placeholder depends on distinguishing:

- an intentional separator;
- a blank;
- punctuation;
- a sign meaning “nothing here.”

A cautious description is “Late Babylonian medial placeholder,” not “the first zero.”

## 10.4 Was Plimpton 322 trigonometry?

### For a trigonometric reading

- values correspond to exact right-triangle ratios;
- rows are ordered systematically;
- a broken portion may have contained additional parameters;
- exact ratio tables could theoretically assist surveying.

### Against

- no angles;
- no trigonometric functions;
- no independent evidence for angle-based Old Babylonian geometry;
- reciprocal pairs and quadratic exercises are abundantly attested in school curricula;
- tablet headings use square and diagonal terminology;
- “trigonometry” imports a later conceptual category.

### Present responsible formulation

Plimpton 322 is an Old Babylonian table of numbers generated from reciprocal relations and connected to right triangles. Its exact pedagogical or practical purpose remains disputed. Calling it “trigonometric” requires a broad structural definition, not the ordinary historical meaning of a table of functions of angle.

## 10.5 Did Babylonians know the Pythagorean theorem?

**[Artefact]** Several tablets contain exact integer or rational right-triangle relationships.

**[Text/Reconstruction]** Survey and diagonal problems use the relation equivalent to:

\[
a^2+b^2=c^2.
\]

**[Absence of evidence]** No Babylonian deductive proof comparable to Euclid’s survives.

Therefore:

- they knew and used the numerical relationship;
- “theorem” may describe the mathematical content;
- calling it a proved general proposition in the Greek sense goes beyond the evidence.

## 10.6 Did they know irrational numbers?

YBC 7289 gives an excellent finite approximation to \(\sqrt2\).

**[Artefact]** Accurate approximation is certain.

**[Absence of evidence]** There is no Old Babylonian proof that \(\sqrt2\) cannot be expressed as a ratio of integers.

“Discovered irrationality” is therefore unsupported.

## 10.7 Did they invent the abacus?

- No intact, unambiguous Babylonian abacus survives.
- Counters and boards are possible.
- Some computational errors and arrangements may reflect unrecorded intermediate work.
- A place-value writing system can be operated without a bead-frame.

The claim should remain **[Disputed reconstruction]**, not fact.

## 10.8 Why base 60?

All major explanations remain reconstructions:

- high divisibility;
- merger of ten and six;
- hand/finger-joint counting;
- twelve months times five;
- 360-day calendar;
- metrological convergence;
- interaction between Sumerian language and numerical signs.

There is no decisive origin text.

## 10.9 Did the Babylonians give us minutes and seconds?

The genealogical claim is broadly right at the level of sexagesimal mathematical structure but misleading if understood as direct institutional continuity.

A more accurate chain is:

> Mesopotamian sexagesimal computation and astronomy  
> → Hellenistic Greek astronomy  
> → Greek and late-antique astronomical tables  
> → Arabic and Latin astronomy  
> → medieval and early modern clocks, navigation, and mathematical notation.

The terms *minute* and *second* are Latin. Mechanical clock displays are medieval and early modern.

## 10.10 Were Uruk numerals already “abstract”?

### Strong non-abstraction view

A number sign’s value depended on the object or measure; therefore there was no independent written number.

### Cautious view

Notation can be domain-dependent while users still possess abstract concepts. Archaeology exposes marks and practices, not private mental categories.

The artefactual finding is contextual numeration. The cognitive conclusion remains theoretical.

## 10.11 Was Sumerian mathematics superior because 60 has many divisors?

**[Documented mathematical property]** Base 60 handles halves, thirds, quarters, fifths, sixths, and many other fractions efficiently.

**[Value judgment]** “Superior” depends on task:

- better for many common fractions;
- requires up to 59 digit-values;
- ambiguous without a zero and radix point;
- cumbersome in ordinary literacy;
- excellent for table-based specialist computation.

## 10.12 The “angles determine digit shapes” legend

This popular legend claims that modern Hindu-Arabic digits have as many angles as their values.

- It concerns modern decimal digits, not cuneiform.
- The proposed diagrams use artificial straight-line redrawings.
- Historical digit forms evolved from Indian scripts.
- The legend is a modern invention.

No analogous theory explains Babylonian wedge counts: Babylonian digits genuinely are additive arrangements of one- and ten-wedges.

## 10.13 Extraterrestrials, the “Sumerian 12th planet,” and 3,600

Modern ancient-astronaut literature has associated *šar* = 3,600 with planetary orbital periods and the alleged planet Nibiru.

- **[Text]** *Nibiru* is an astronomical/divine term with context-dependent identifications.
- **[Text]** *šar* is a numerical and literary term.
- **[Modern invention]** Treating *šar* as an extraterrestrial year and Nibiru as a hidden planet on a regular 3,600-year orbit is not supported by cuneiform astronomy.
- **[Cultural fact]** These claims have had substantial popular influence and belong to the modern reception of Sumerian numbers.

## 10.14 Ifrah, Menninger, and synthetic universal histories

Karl Menninger’s *Number Words and Number Symbols* remains valuable for comparative examples and the materiality of counting, but parts predate major advances in proto-cuneiform study.

Georges Ifrah assembled an exceptionally broad visual and narrative history. Specialists have criticized:

- incomplete citations;
- repeated errors from older secondary works;
- speculative diffusion presented confidently;
- unsupported “firsts”;
- reconstructions or anecdotes treated as established.

Joseph Dauben’s two-part review records serious objections by specialists and notes examples of misreading and fabrication. [Dauben review record/search copy](https://es.scribd.com/document/204079257/Critique-de-Georges-Ifrah)

Stephen Chrisomalis’s *Numerical Notation* (2010) is the standard comparative survey because it distinguishes notation structure, transmission, and independent development more systematically. Its Mesopotamian chapter should nevertheless be supplemented by Englund, Damerow, Friberg, Proust, Høyrup, and Robson. [Cambridge contents](https://www.cambridge.org/core/books/abs/numerical-notation/cognitive-and-structural-analysis/13A760A1E6258DCC74FC0F129E805899)

---

# 11. Historiography: how the readings developed

## Before decipherment

European travelers copied wedge inscriptions but could not read them. Biblical and Classical traditions supplied names such as Babylon, Assyria, and Chaldaea, encouraging both serious study and speculative identification.

## 1800s: decipherment

Old Persian royal inscriptions provided an entry point. Behistun’s multilingual text enabled comparisons among Old Persian, Elamite, and Babylonian versions.

By the 1850s:

- Hincks had recognized syllabic and logographic structure;
- Rawlinson had advanced readings through Behistun;
- Oppert and Talbot contributed independent translations;
- the 1857 Royal Asiatic Society comparison helped persuade skeptics.

Numerical passages were often easier to isolate than ordinary language because repetition, royal counts, and metrological patterns exposed regularities.

## Late nineteenth and early twentieth centuries

Excavations and antiquities-market collections brought mathematical tablets to:

- Berlin;
- London;
- Paris;
- Istanbul;
- Jena;
- Yale;
- Columbia;
- Philadelphia.

Scholars including Hilprecht, Thureau-Dangin, Neugebauer, and Sachs established numerical readings through:

- repeated tables;
- bilingual lexical lists;
- known unit conversions;
- internal verification of products and reciprocals.

## Mid-twentieth century

Neugebauer’s publications emphasized the high mathematical level of Babylonian texts. Van der Waerden and popular histories framed them as precursors of Greek algebra and number theory.

## 1970s–1990s

Research shifted toward:

- archaic numeration;
- cognitive development;
- tokens;
- school practice;
- non-symbolic geometry;
- philologically exact operation words.

Schmandt-Besserat, Damerow, Englund, Friberg, Høyrup, and Powell were central.

## 2000s to present

Robson, Proust, and others have emphasized:

- archaeological provenance;
- social institutions;
- teacher-pupil relationships;
- local variation;
- political history;
- the danger of reverse-engineering tablets from modern mathematics.

Digital projects such as CDLI and ORACC allow tablet images, transliterations, metadata, and sign lists to be compared at corpus scale.

---

# 12. Open questions

1. Which prehistoric clay objects were actually numerical tokens?

2. How stable were token meanings across millennia and regions?

3. Did late token/bulla accounting directly generate proto-cuneiform signs, or was it one component in a broader administrative transformation?

4. How many Uruk numerical systems should be distinguished? Published counts depend on whether variants are grouped or separated.

5. What language or languages underlay the earliest proto-cuneiform accounts?

6. At what point should context-bound numerical sequences be called “abstract numbers”?

7. Is YOS 4, 293 sufficient to establish fully developed place value in Ur III, or only a transitional procedure?

8. Was sexagesimal place value invented once in a particular scribal milieu, or did several practices converge?

9. Why was 60 originally privileged?

10. What temporary calculating media—dust boards, waxed surfaces, counters, mental algorithms—have vanished?

11. What was Plimpton 322 made for?

12. How was the approximation on YBC 7289 obtained: copied from a coefficient table, generated by iteration, or learned through another routine?

13. How early is the first unambiguous medial placeholder?

14. Did the placeholder emerge from punctuation, spacing conventions, or deliberate numerical analysis?

15. How directly did Greek astronomers learn from Babylonian practitioners, and through what bilingual intermediaries?

16. Which portions of Greek sexagesimal practice were transmitted from Babylon and which were independently reformulated?

17. When precisely did hours acquire routinely displayed minutes and seconds outside astronomical tables?

18. How representative are surviving mathematical tablets, given that durable clay preserves school debris but most everyday reckoning may have occurred on perishable media?

19. How much has the antiquities market distorted provenances and therefore historical reconstruction?

20. Will digital joins, multispectral imaging, and automated sign comparison identify missing fragments of major mathematical tablets?

---

# 13. Findings by evidentiary strength

## Secure

- Late-fourth-millennium Uruk tablets contain several numerical/metrological notations.
- Old Babylonian mathematics uses sexagesimal place value.
- Digits 1–59 are constructed principally from unit and ten wedges.
- The system is additive within positions and positional between powers of 60.
- The place-value scale normally floats.
- Reciprocal and multiplication tables were fundamental to scribal training.
- YBC 7289 contains `1;24,51,10`, an excellent approximation to \(\sqrt2\).
- Plimpton 322 contains systematic numbers related to right triangles.
- Later Babylonian texts use a medial placeholder.
- Babylonian astronomy employed many-place sexagesimal computation.
- Greek astronomy adopted substantial Babylonian data and sexagesimal techniques.
- Modern angular and temporal subdivisions preserve sexagesimal structure.

## Strong reconstruction

- Some late prehistoric tokens and bullae were accounting devices.
- Ur III scribes participated in the transition to fully abstract place-value calculation.
- Plimpton 322 belongs to a reciprocal/quadratic educational environment.
- Sexagesimal divisibility was a major reason for the system’s mathematical persistence.

## Genuinely disputed

- The extent of the token-to-writing sequence.
- The exact first place-value text.
- Plimpton 322’s intended function.
- The physical instruments used for intermediate computation.
- The first occurrence properly called a zero placeholder.
- The mechanism and personnel of Babylonian-to-Greek transmission.

## Unsupported or legendary

- One named Sumerian invented base 60.
- Sumerians are documented counting twelve finger joints and five dozens.
- Astronomy alone created sexagesimal notation.
- YBC 7289 proves knowledge of irrational numbers.
- Plimpton 322 is unambiguously a trigonometric table.
- Babylonians had a zero-number equivalent to modern 0.
- Babylonian astronomers designed the modern mechanical clock.
- *Šar* proves a 3,600-year extraterrestrial orbit.
- Neolithic tally bones in Africa are demonstrable ancestors of Sumerian notation.

---

# 14. Sources consulted and recommended editions

## Primary corpora, catalogues, and digital resources

- Cuneiform Digital Library Initiative, tablet catalogue and images:  
  https://cdli.mpiwg-berlin.mpg.de/

- ORACC, Open Richly Annotated Cuneiform Corpus:  
  http://oracc.museum.upenn.edu/

- ORACC/ePSD2, Electronic Pennsylvania Sumerian Dictionary:  
  http://oracc.museum.upenn.edu/epsd2/

- ORACC Digital Corpus of Cuneiform Lexical Texts, Jena school tablets:  
  https://oracc2.museum.upenn.edu/dcclt/jena/Highlights/OBSchoolTexts/index.html

- Yale Babylonian Collection:  
  https://babylonian-collection.yale.edu/

- Duncan Melville, YBC 7289:  
  https://myslu.stlawu.edu/~dmel/mesomath/tablets/YBC7289

- Columbia University Libraries, Plimpton collection portal:  
  https://library.columbia.edu/

- British Museum Collection Online:  
  https://www.britishmuseum.org/collection

- Musée du Louvre collections database:  
  https://collections.louvre.fr/

- Institute for the Study of Ancient Cultures, University of Chicago:  
  https://isac.uchicago.edu/

- Unicode, Cuneiform Numbers and Punctuation names list:  
  https://unicode.org/charts/nameslist/n_12400.html

- Unicode, Cuneiform Numbers and Punctuation chart:  
  https://www.unicode.org/charts/PDF/U12400.pdf

- Unicode Standard, Cuneiform chapter:  
  https://www.unicode.org/versions/Unicode12.1.0/ch11.pdf

## Editions of mathematical texts

- Neugebauer, Otto. *Mathematische Keilschrift-Texte*. 3 vols. Berlin: Springer, 1935–1937.

- Neugebauer, Otto, and Abraham J. Sachs. *Mathematical Cuneiform Texts*. American Oriental Series 29. New Haven: American Oriental Society, 1945.  
  https://archive.org/search?query=%22Mathematical+Cuneiform+Texts%22

- Neugebauer, Otto. *Astronomical Cuneiform Texts*. 3 vols. London: Lund Humphries, 1955.  
  https://archive.org/search?query=%22Astronomical+Cuneiform+Texts%22

- Thureau-Dangin, François. *Textes mathématiques babyloniens*. Leiden: Brill, 1938.  
  https://archive.org/search?query=%22Textes+math%C3%A9matiques+babyloniens%22

- Bruins, E. M., and M. Rutten. *Textes mathématiques de Suse*. Mémoires de la Mission Archéologique en Iran 34. Paris: Geuthner, 1961.

## Proto-cuneiform, tokens, and early numeracy

- Schmandt-Besserat, Denise. “An Archaic Recording System and the Origin of Writing.” *Syro-Mesopotamian Studies* 1.1, 1977.

- Schmandt-Besserat, Denise. “An Archaic Recording System in the Uruk-Jemdet Nasr Period.” *American Journal of Archaeology* 83.1, 1979, 19–48.  
  https://www.journals.uchicago.edu/doi/10.2307/504234

- Schmandt-Besserat, Denise. “The Earliest Precursor of Writing.” *Scientific American* 238.6, 1978.

- Schmandt-Besserat, Denise. “Decipherment of the Earliest Tablets.” *Science* 211, 1981.  
  https://pubmed.ncbi.nlm.nih.gov/17748027/

- Schmandt-Besserat, Denise. “Tokens: Facts and Interpretations.” *Visible Language* 20.3, 1986.  
  https://journals.uc.edu/index.php/vl/article/view/5441

- Schmandt-Besserat, Denise. *Before Writing*. 2 vols. Austin: University of Texas Press, 1992.

- Schmandt-Besserat, Denise. *How Writing Came About*. Austin: University of Texas Press, 1996.

- Schmandt-Besserat, Denise. “The Invention of Tokens.” In *Tokens: Culture, Connections, Communities*. Royal Numismatic Society, 2019.  
  https://sites.utexas.edu/dsb/tokens/the-invention-of-tokens/

- Zimansky, Paul. Review of Schmandt-Besserat, *Before Writing*. *Journal of Field Archaeology* 20, 1993.  
  https://urkesh.org/attach/Zimansky1993.pdf

- Nissen, Hans J.; Peter Damerow; and Robert K. Englund. *Archaic Bookkeeping: Early Writing and Techniques of Economic Administration in the Ancient Near East*. Chicago: University of Chicago Press, 1993.

- Englund, Robert K. “Proto-Cuneiform Account-Books and Journals.”  
  https://cdli.mpiwg-berlin.mpg.de/files-up/publications/englund2004a.pdf

- Englund, Robert K. “Late Uruk Period Cattle and Dairy Products.”  
  https://cdli.mpiwg-berlin.mpg.de/files-up/publications/englund1995b.pdf

- Overmann, Karenleigh A., et al. “Numeracy at the Dawn of Writing: Mesopotamia and Beyond.” *Historia Mathematica* 52, 2020.  
  https://doi.org/10.1016/j.hm.2020.08.002

- “The Cultural Origins of Symbolic Number.”  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC8678391/

## Sexagesimal notation

- Friberg, Jöran. “Three Thousand Years of Sexagesimal Numbers in Mesopotamian Mathematical Texts.” *Archive for History of Exact Sciences* 73, 2019, 183–216.  
  https://doi.org/10.1007/s00407-019-00221-3

- Open full text of Friberg’s article:  
  https://research.chalmers.se/publication/508683/file/508683_Fulltext.pdf

- Friberg, Jöran. “The Powers of 9 and Related Mathematical Tables from Babylon.”  
  https://arxiv.org/abs/1306.5989

- Powell, Marvin A. “The Origin of the Sexagesimal System: The Interaction of Language and Writing.” *Visible Language*.  
  https://journals.uc.edu/index.php/vl/article/view/5115

- Powell, Marvin A. “The Antecedents of Old Babylonian Place Notation and the Early History of Babylonian Mathematics.” *Historia Mathematica* 3, 1976.  
  https://peachv.org/images/MuslimGeo/BabyMathPlaceNotationPowell.pdf

- MacTutor History of Mathematics, “Babylonian Numerals”:  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/

- Friberg-related overview of Uruk and Susa metrology:  
  https://mathscitech.org/articles/mathematics-uruk-susa

## Babylonian mathematics and education

- Robson, Eleanor. *Mesopotamian Mathematics, 2100–1600 BC: Technical Constants in Bureaucracy and Education*. Oxford: Clarendon Press, 1999.

- Robson, Eleanor. “The Tablet House: A Scribal School in Old Babylonian Nippur.” *Revue d’Assyriologie* 93/95, 2001.  
  https://shs.cairn.info/journal-revue-d-assyriologie-2001-1-page-39?lang=en

- Robson, Eleanor. “Mathematical Cuneiform Tablets in the Ashmolean Museum.” *SCIAMVS* 5, 2004.  
  https://www.sciamvs.org/files/SCIAMVS_05_003-065_Robson.pdf

- Robson, Eleanor. *Mathematics in Ancient Iraq: A Social History*. Princeton: Princeton University Press, 2008.  
  https://www.jstor.org/stable/j.ctv10qqzk0

- Robson, sample chapter, *Mathematics in Ancient Iraq*:  
  https://sidoli.w.waseda.jp/Robson_1.pdf

- Proust, Christine. “Mathematics in Mesopotamia: From Elementary Education to Erudition.” Institute for Advanced Study, 2010.  
  https://www.ias.edu/ideas/2010/proust-mesopotamian-mathematics

- Proust, Christine. “Quantifier et calculer: usages des nombres à Nippur.”  
  https://eudml.org/doc/274971

- Høyrup, Jens. *Lengths, Widths, Surfaces: A Portrait of Old Babylonian Algebra and Its Kin*. New York: Springer, 2002.  
  https://books.google.com/books/about/Lengths_Widths_Surfaces.html?id=GavTBwAAQBAJ

- Friberg, Jöran. *A Remarkable Collection of Babylonian Mathematical Texts*. New York: Springer, 2007.

- “Bases, Positions and Computations,” historical analysis of cuneiform place value:  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12536272/

## Plimpton 322

- Robson, Eleanor. “Neither Sherlock Holmes nor Babylon: A Reassessment of Plimpton 322.” *Historia Mathematica* 28.3, 2001, 167–206.  
  https://ora.ox.ac.uk/objects/uuid%3Ae3d8eedb-e745-45b3-8612-71f8951599aa

- Accessible copy of Robson’s article:  
  https://mathcs.holycross.edu/~little/Mont201617/RobsonNeither.pdf

- Friberg, Jöran. “Methods and Traditions of Babylonian Mathematics: Plimpton 322, Pythagorean Triples, and the Babylonian Triangle Parameter Equations.” *Historia Mathematica* 8.3, 1981, 277–318.  
  https://doi.org/10.1016/0315-0860(81)90069-0

- AMS discussion of Plimpton 322 interpretations:  
  https://www.ams.org/journals/notices/200405/200405FullIssue.pdf

- AMS Feature Column, “Completing the Square”:  
  https://mathvoices.ams.org/featurecolumn/2020/11/01/fc-2020-10-2/

## Decipherment

- Encyclopaedia Iranica, “Rawlinson: Contributions to Assyriology”:  
  https://www.iranicaonline.org/articles/rawlinson-ii/

- Smithsonian, account of the competing cuneiform decipherers:  
  https://www.smithsonianmag.com/history/mystery-worlds-oldest-writing-system-remained-unsolved-until-four-competitive-scholars-raced-to-decipher-it-180985954/

## Comparative histories

- Chrisomalis, Stephen. *Numerical Notation: A Comparative History*. Cambridge: Cambridge University Press, 2010.  
  https://www.cambridge.org/core/books/numerical-notation/6E243BD17A4BCA1F43672B3FD29D698A

- Chrisomalis, chapter and contents record:  
  https://www.cambridge.org/core/books/abs/numerical-notation/cognitive-and-structural-analysis/13A760A1E6258DCC74FC0F129E805899

- Review of Chrisomalis:  
  https://cs.nyu.edu/faculty/davise/papers/Chrisomalis.pdf

- Menninger, Karl. *Zahlwort und Ziffer: Eine Kulturgeschichte der Zahl*. 2nd ed. Göttingen: Vandenhoeck & Ruprecht, 1957–1958.

- Menninger, Karl. *Number Words and Number Symbols: A Cultural History of Numbers*. Translated by Paul Broneer. Cambridge, MA: MIT Press, 1969.  
  https://archive.org/search?query=%22Number+Words+and+Number+Symbols%22

- Ifrah, Georges. *Histoire universelle des chiffres*. Paris: Seghers/Bouquins, revised 1994.

- Ifrah, Georges. *The Universal History of Numbers: From Prehistory to the Invention of the Computer*. Translated by David Bellos et al. London/New York: Harvill/Wiley, 1998–2000.

- Dauben, Joseph W. “The Universal History of Numbers and the Universal History of Computing.” *Notices of the American Mathematical Society* 49, 2002, two parts.  
  https://www.ams.org/notices/200201/rev-dauben.pdf  
  https://www.ams.org/notices/200202/rev-dauben.pdf

- Kirkus review of Ifrah:  
  https://www.kirkusreviews.com/book-reviews/georges-ifrah/a-universal-history-of-numbers/

## General accessible reference

- MacTutor, “Babylonian Numerals”:  
  https://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_numerals/

- Institute for the Study of Ancient Cultures, *They Wrote on Clay*:  
  https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/they_wrote_on-clay.pdf

- Unicode proposal and updated numeric-sign documentation:  
  https://www.unicode.org/L2/L2024/24239-xsux-numeric.pdf
