# Binary numerals: Leibniz, the I Ching and the machine: Research Dossier

## Method and evidentiary labels

This dossier distinguishes six kinds of statement:

- **[Documented text]** — stated in a surviving manuscript, printed work, standard, patent, or correspondence.
- **[Documented artefact]** — embodied in a surviving or securely recorded object.
- **[Scholarly reconstruction]** — a historian’s interpretation of texts, diagrams, or technical practice.
- **[Tradition]** — an attribution transmitted within a culture but not independently verified.
- **[Disputed]** — a claim for which serious alternatives remain.
- **[Legend/modern invention]** — a retrospective story unsupported by the chronology or the surviving evidence.

Dates before the Common Era are BCE. Binary numerals carry the subscript ₂ where ambiguity is possible; decimal comparanda carry ₁₀.

---

## Basic identification

| Field | Identification |
|---|---|
| **Name** | Binary numeral system; base-two notation; historically Leibniz also used terms translated as *binary* or *dyadic progression* |
| **Base** | **2** |
| **Type** | **Ciphered positional**: two digit-signs occupy places whose weights are powers of two |
| **Signs** | `0` and `1`; Unicode U+0030 DIGIT ZERO and U+0031 DIGIT ONE |
| **Place values** | …, 2⁵, 2⁴, 2³, 2², 2¹, 2⁰; after the radix point, 2⁻¹, 2⁻², 2⁻³, … |
| **Zero** | A genuine digit and number in mathematical notation; in fixed-width machine words it also fills unused positions. Its electrical meaning is conventional, not intrinsically “off.” |
| **Direction** | Conventionally most-significant digit at left, least-significant at right |
| **Period** | Abstract base-two procedures occur in several independent traditions. Explicit European positional binary survives in Harriot’s early-seventeenth-century manuscripts, was printed by Caramuel in 1670, developed independently and influentially by Leibniz from 1679, and became central to switching and computing in the twentieth century. |
| **Regions** | Precursors or analogues in India, China, Egypt, Polynesia, and early-modern Europe; modern use is worldwide |
| **Range** | Mathematically unlimited: an \(n\)-digit unsigned numeral represents 0 through \(2^n-1\). Physical machines have finite word sizes. |
| **Classification caveat** | The two-valued patterns of Sanskrit metre and the *Yijing* are not automatically positional numerals. “Binary alphabet,” “binary enumeration,” “binary arithmetic,” “binary logic,” and “binary machine” are related but historically distinct. |

Stephen Chrisomalis classifies positional systems by how signs and place values combine. On that terminology, modern binary is a ciphered-positional notation, not additive. His comparative survey also notes that binary, octal, and hexadecimal are unusual precisely because they became widely used technical systems without replacing decimal as society’s ordinary notation ([Chrisomalis 2010](https://www.cambridge.org/core/books/numerical-notation/4C3107573159D539D04DD7307423FA36); accessible text [here](https://glossographia.files.wordpress.com/2010/01/chrisomalis-numerical-notation.pdf)).

---

# The system in detail

## 1. The two signs

### Modern numerical signs

- `0` — zero; U+0030.
- `1` — one; U+0031.
- `₂` — subscript two, U+2082, often appended to declare the radix: `101101₂`.
- A point ordinarily separates integer and fractional places: `101.01₂`.

The shapes are inherited from the Hindu-Arabic typographic digits, not designed especially for binary. There are no traditional binary ligatures. Separating spaces or underscores—`1101 0110`, `1101_0110`—are modern readability conventions, not numeral-signs.

### Physical two-state signs

A bit can be realized by any reliably distinguishable pair:

- low/high voltage;
- switch open/closed;
- relay released/energized;
- magnetic orientation A/B;
- pit/land or dark/light mark;
- punched/unpunched;
- false/true;
- yin/yang line, if a modern mapping is deliberately imposed.

**[Technical fact]** Neither 0 nor 1 inherently means “off,” “false,” or “yin.” Encoding polarity is chosen by a system designer. Active-low electronics regularly reverses the popular equation “0 = off, 1 = on.”

### *Yijing* line signs

Unicode provides:

- `⚊` U+268A — MONOGRAM FOR YANG: one unbroken horizontal line.
- `⚋` U+268B — MONOGRAM FOR YIN: a horizontal line broken in the middle.
- Eight trigram characters `☰`–`☷`, U+2630–U+2637.
- Sixty-four hexagram characters `䷀`–`䷿`, U+4DC0–U+4DFF.

The Unicode hexagrams occur in the traditional received, usually called King Wen, order—not Shao Yong’s binary-like order. Unicode describes them as semantically distinct signs with traditional names, not as the integers 0–63 ([Unicode 17, Yijing block](https://www.unicode.org/charts/PDF/U4DC0.pdf); [Unicode Core Specification §22.9.11](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-22/)).

In words:

- yang: “a solid, unbroken horizontal stroke”;
- yin: “a horizontal stroke divided by a central gap”;
- trigram: three such lines stacked vertically;
- hexagram: six such lines stacked vertically, traditionally read and generated from the bottom upward.

**[Documented text plus retrospective mapping]** Leibniz mapped solid line to 1 and broken line to 0 in his 1703 explanation. This mapping is mathematically possible and visually exact; it does not establish that ancient diviners treated the figures as positional numbers.

---

## 2. Positional value

For digits \(b_i\in\{0,1\}\),

\[
b_nb_{n-1}\ldots b_1b_0{}_2
=\sum_{i=0}^{n}b_i2^i.
\]

Thus:

\[
110101_2
=1(32)+1(16)+0(8)+1(4)+0(2)+1(1)
=53_{10}.
\]

Zeroes are operationally indispensable: in `100000₂`, the five zeroes say that the coefficients of 16, 8, 4, 2, and 1 are absent, leaving \(2^5=32\).

Leading zeroes do not alter a mathematical integer:

\[
101_2=0101_2=00000101_2.
\]

They do matter in fixed-width encodings: `00000101` explicitly occupies eight bits.

---

## 3. Table: decimal 0–20

| Decimal | Binary | Expansion |
|---:|---:|---|
| 0 | `0₂` | 0 |
| 1 | `1₂` | 1 |
| 2 | `10₂` | 2 |
| 3 | `11₂` | 2 + 1 |
| 4 | `100₂` | 4 |
| 5 | `101₂` | 4 + 1 |
| 6 | `110₂` | 4 + 2 |
| 7 | `111₂` | 4 + 2 + 1 |
| 8 | `1000₂` | 8 |
| 9 | `1001₂` | 8 + 1 |
| 10 | `1010₂` | 8 + 2 |
| 11 | `1011₂` | 8 + 2 + 1 |
| 12 | `1100₂` | 8 + 4 |
| 13 | `1101₂` | 8 + 4 + 1 |
| 14 | `1110₂` | 8 + 4 + 2 |
| 15 | `1111₂` | 8 + 4 + 2 + 1 |
| 16 | `10000₂` | 16 |
| 17 | `10001₂` | 16 + 1 |
| 18 | `10010₂` | 16 + 2 |
| 19 | `10011₂` | 16 + 2 + 1 |
| 20 | `10100₂` | 16 + 4 |

Counting follows the positional carry rule:

```text
   0
   1
  10
  11
 100
 101
 110
 111
1000
```

A carry occurs because `1 + 1 = 10₂`.

---

## 4. Tens, hundreds, thousands, and powers of ten

The request for “tens, hundreds, thousands” is naturally interpreted as decimal round numbers expressed in binary:

| Decimal | Binary |
|---:|---:|
| 10 | `1010₂` |
| 20 | `10100₂` |
| 30 | `11110₂` |
| 40 | `101000₂` |
| 50 | `110010₂` |
| 60 | `111100₂` |
| 70 | `1000110₂` |
| 80 | `1010000₂` |
| 90 | `1011010₂` |
| 100 | `1100100₂` |
| 200 | `11001000₂` |
| 300 | `100101100₂` |
| 400 | `110010000₂` |
| 500 | `111110100₂` |
| 600 | `1001011000₂` |
| 700 | `1010111100₂` |
| 800 | `1100100000₂` |
| 900 | `1110000100₂` |
| 1,000 | `1111101000₂` |
| 10,000 | `10011100010000₂` |
| 100,000 | `11000011010100000₂` |
| 1,000,000 | `11110100001001000000₂` |
| 1,000,000,000 | `111011100110101100101000000000₂` |

The “round” numbers native to binary are powers of two:

| Power | Decimal | Binary | Common machine association |
|---:|---:|---:|---|
| \(2^0\) | 1 | `1₂` | one state-weight |
| \(2^1\) | 2 | `10₂` | |
| \(2^2\) | 4 | `100₂` | nibble size in bits |
| \(2^3\) | 8 | `1000₂` | modern byte size in bits |
| \(2^4\) | 16 | `10000₂` | hexadecimal alphabet size |
| \(2^8\) | 256 | `1 0000 0000₂` | number of patterns in a byte |
| \(2^{10}\) | 1,024 | `100 0000 0000₂` | one kibibyte’s bytes |
| \(2^{16}\) | 65,536 | `1` followed by 16 zeroes | 16-bit address/value boundary |
| \(2^{32}\) | 4,294,967,296 | `1` followed by 32 zeroes | |
| \(2^{64}\) | 18,446,744,073,709,551,616 | `1` followed by 64 zeroes | |

The IEC approved binary prefixes in 1998: kibi- \(=2^{10}\), mebi- \(=2^{20}\), gibi- \(=2^{30}\), and so forth. Thus 1 KiB is exactly 1,024 bytes, unlike 1 kB, conventionally 1,000 bytes ([NIST binary-prefix table](https://physics.nist.gov/cuu/Units/binary.html)).

---

## 5. Famous numbers

| Number | Binary form | Reason for fame |
|---:|---:|---|
| 42 | `101010₂` | Douglas Adams’s “Answer to the Ultimate Question” |
| 64 | `1000000₂` | \(2^6\); number of possible six-line two-state figures |
| 255 | `11111111₂` | largest unsigned 8-bit integer |
| 1,024 | `10000000000₂` | \(2^{10}\), traditional computing “K” boundary |
| 1,703 | `11010100111₂` | year of Leibniz’s published *Explication* |
| 1,945 | `11110011001₂` | year of von Neumann’s EDVAC draft |
| 65,535 | `1111111111111111₂` | largest unsigned 16-bit integer |
| 4,294,967,295 | 32 consecutive ones | largest unsigned 32-bit integer |

There is no largest mathematical binary numeral. For any numeral \(N\), appending an additional leading `1` can make a larger one. An unsigned \(n\)-bit storage unit has maximum \(2^n-1\), but that is a property of the container, not the numeral system.

Binary has no special native words for large numbers. Speakers ordinarily use the number words of their language: “one thousand twenty-four,” “a million,” and so forth. “K,” “meg,” “gig,” *kibibyte*, and *gibibyte* belong to technical metrology, not to the grammar of binary numerals.

---

## 6. Fractions

Places to the right of the binary point have weights \(1/2,1/4,1/8,\ldots\):

| Fraction | Binary |
|---:|---:|
| \(1/2\) | `0.1₂` |
| \(1/4\) | `0.01₂` |
| \(3/4\) | `0.11₂` |
| \(1/8\) | `0.001₂` |
| \(3/8\) | `0.011₂` |
| \(5/8\) | `0.101₂` |
| \(7/8\) | `0.111₂` |
| \(1/3\) | `0.010101…₂` |
| \(1/5\) | `0.001100110011…₂` |
| \(1/10\) | `0.0001100110011…₂` |

A rational number has a terminating binary expansion exactly when its reduced denominator is a power of two. Consequently decimal `0.1` cannot be represented as a finite ordinary binary fraction. This—not an arithmetic malfunction—is the source of familiar floating-point surprises.

Modern computers use:

- **fixed point**, where the binary point has an agreed location;
- **floating point**, where significand and exponent are stored separately;
- rational, decimal, or arbitrary-precision software when exact non-dyadic fractions are required.

IEEE 754-1985 standardized widely compatible binary floating-point formats; the current IEEE 754-2019 standard covers binary and decimal formats, arithmetic, rounding, infinities, signed zero, NaNs, and exceptions ([IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/)).

---

## 7. Negative numbers and non-integers

A bare binary numeral denotes a nonnegative magnitude. Signed representation requires an added convention:

- sign-and-magnitude;
- ones’ complement;
- two’s complement;
- biased integers;
- floating-point sign, exponent, and significand.

In an \(n\)-bit two’s-complement word, values range from \(-2^{n-1}\) through \(2^{n-1}-1\). For eight bits:

- `00000001` = +1;
- `01111111` = +127;
- `11111111` = −1;
- `10000000` = −128.

**[Documented text]** John von Neumann’s 1945 *First Draft of a Report on the EDVAC* proposed complement representation. EDSAC subsequently used two’s complement. Earlier and contemporary machines also used ones’ complement and sign-and-magnitude; therefore “computers represent negatives in two’s complement” is a useful modern generalization, not a universal historical truth.

---

## 8. Arithmetic

The elementary tables contain only four cases.

### Addition

```text
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10₂
```

Example:

```text
   101101
 + 011011
 --------
  1001000
```

That is \(45+27=72\).

### Multiplication

```text
0 × 0 = 0
0 × 1 = 0
1 × 0 = 0
1 × 1 = 1
```

Example:

```text
      1101       13
    × 1011     × 11
    ------
      1101
     11010
    000000
+ 1101000
---------
 10001111      143
```

Multiplication by \(2^k\) shifts an unsigned integer left \(k\) places, provided no finite machine word overflows. Division by two corresponds to a right shift for nonnegative integers, with the discarded low bit giving the remainder.

### Boolean operations on bit strings

Modern machines also apply logical operations position by position:

```text
  1100
AND 1010 = 1000
 OR 1010 = 1110
XOR 1010 = 0110
NOT 1100 = 0011    (within four bits)
```

These are not ordinary numerical addition and multiplication, although Boolean AND resembles multiplication on individual 0/1 values.

---

## 9. Octal and hexadecimal

Binary strings become long for human readers. Two exact grouping systems developed as shorthand:

- one octal digit represents three bits;
- one hexadecimal digit represents four bits.

Example:

```text
Binary       1101 1110 1010 1101
Hexadecimal     D    E    A    D   = DEAD₁₆

Binary       011 011 110 101
Octal          3   3   6   5       = 3365₈
```

Octal suited machines with 6-, 12-, 18-, 24-, or 36-bit units. Hexadecimal fits 8-, 16-, 32-, and 64-bit architectures because two hex digits make one eight-bit byte. IBM documentation explicitly presents hexadecimal as a shorthand for binary ([IBM data-processing manual](https://bitsavers.org/pdf/ibm/generalInfo/GC20-1684-4_IBMdpIntroJul78.pdf); [IBM conversion table](https://www.ibm.com/docs/en/aix/7.1.0?topic=adapters-ascii-decimal-hexadecimal-octal-binary-conversion-table)).

---

# Origins: the dated record

## 1. Deep prehistory: tallies are not binary numerals

Marked bones such as Lebombo and Ishango are frequently placed in general histories of number. They show intentional notching and perhaps grouped counting. They do not show two positional digits, place values \(1,2,4,8,\ldots\), or base-two arithmetic.

- **[Documented artefact]** The Lebombo bone is a notched baboon fibula from Border Cave in southern Africa, often dated broadly to about 44,000–35,000 years ago.
- **[Documented artefact, disputed interpretation]** The Ishango bone, from the Lake Edward region of today’s Democratic Republic of the Congo, is normally dated to the Later Stone Age, often around 20,000 years ago. Proposed readings include arithmetic grouping, lunar counting, and simple tallying.
- **Finding:** neither is an attestation of binary notation. Calling grouped notches “binary” would be a modern projection.

Similarly, Mesopotamian tokens, Uruk numerical tablets, the Narmer macehead, Brahmi numerals, Bakhshali zero, Gwalior zero, Maya numerals, and the Dresden Codex are crucial to other numeral-system histories but are not stages in a demonstrable genealogy of binary. No source establishes a route from them to Harriot, Caramuel, Leibniz, or electronic computing.

This negative finding matters: a comprehensive binary history should not confuse “very old number artefact” with “ancestor of base two.”

---

## 2. Egyptian doubling

**[Documented text]** Egyptian mathematical documents, especially the Rhind Mathematical Papyrus copied by the scribe Ahmes around 1650 BCE from an older exemplar, perform multiplication and division by successive doubling and selective addition.

A modern reconstruction of \(13\times11\) looks like:

```text
1     11   ✓
2     22
4     44   ✓
8     88   ✓
           ---
           143
```

Because \(13=8+4+1\), the selected doubled values sum to 143.

**[Scholarly reconstruction]** This algorithm decomposes the multiplier into powers of two and is mathematically equivalent to binary “double-and-add.” It does not follow that Egyptian scribes wrote positional binary numerals or conceptualized the procedure as base-two notation. The Rhind text belongs under binary algorithms, not under attestations of the signs `0,1` ([Rhind edition](https://en.wikisource.org/wiki/Page:The_Rhind_Mathematical_Papyrus,_Volume_I.pdf/21)).

The same distinction applies to later “Russian peasant multiplication”: halving and doubling implement a binary decomposition without requiring the user to write the factors in binary.

---

## 3. The *Yijing*: two forms, sixty-four figures

### Earliest secure textual evidence

The *Zhouyi*, the oldest textual stratum of what became the *Yijing* or *Book of Changes*, is conventionally associated with early Zhou China. Traditional dates reach back to Fu Xi and remote antiquity.

- **[Tradition]** Fu Xi invented or revealed the trigrams; King Wen ordered or interpreted the hexagrams; the Duke of Zhou supplied line texts; Confucius supplied commentaries.
- **[Documented absence]** The *Zhouyi* does not narrate this composite authorship.
- **[Modern scholarship]** The received work is stratified and developed over centuries.
- **[Documented artefact]** The earliest substantial excavated *Zhouyi* manuscript, in the Shanghai Museum bamboo corpus, dates to about 300 BCE. Other excavated witnesses include Mawangdui Tomb 3, sealed in 168 BCE, and Fuyang material associated with a tomb occupant who died in 165 BCE. Their arrangements and wording vary. Edward Shaughnessy emphasizes that no excavated version can simply be declared the single original text ([Unearthing the Changes](https://www.jstor.org/stable/10.7312/shau16184); [Oxford survey](https://academic.oup.com/book/8934/chapter-abstract/155240726)).

Each of the six positions has two forms, yielding \(2^6=64\) possible hexagrams. That combinatorial fact is indisputable.

### Are the hexagrams numerals?

**[Disputed terminology]**

Case for calling them binary:

- they are ordered strings over a two-sign alphabet;
- the six positions are distinguishable;
- mapping the two line types to 0 and 1 produces six-bit words;
- certain arrangements associated with Shao Yong can be traversed so that these words correspond regularly to 0–63.

Case against calling the ancient system binary numeration:

- the figures’ documented function is divinatory, cosmological, and classificatory;
- their traditional line values are commonly 6, 7, 8, and 9 in divination, not zero and one;
- no early Chinese text performs base-two positional arithmetic with them;
- the received King Wen sequence is not numerical binary order;
- equivalence to six-bit words can be imposed on any ordered collection of two-state sequences.

The careful conclusion is: **the hexagrams constitute an ancient two-state combinatorial notation; their interpretation as positional binary numerals is a seventeenth-century European reading prompted by an eleventh-century Chinese arrangement.**

---

## 4. Pingala and Sanskrit prosody

### The text

**[Documented textual tradition, uncertain date]** The *Chandaḥsūtra* attributed to Piṅgala is the earliest surviving Sanskrit treatise devoted to prosody. Estimates vary widely, commonly within roughly the fifth to second centuries BCE; “c. 200 BCE” is a conventional shorthand, not a manuscript colophon date.

Sanskrit metres classify syllables as:

- *laghu* — light/short;
- *guru* — heavy/long.

For \(n\) positions there are \(2^n\) possible light-heavy patterns. The procedures called *prastāra* (systematic expansion), *naṣṭa* (recovering a missing pattern from its index), and *uddiṣṭa* (finding a pattern’s index) form an algorithmic combinatorics of two-valued strings. Later commentators, especially Halāyudha, explain the terse sūtras.

A convenient modern illustration for three positions is:

```text
LLL
LLG
LGL
LGG
GLL
GLG
GGL
GGG
```

The exact traditional ordering and which of L/G corresponds to the modern 0/1 depend on the reconstruction. Pingala’s procedure is often read from a direction opposite to modern most-significant-bit-first notation and may produce reversed or complemented values.

### What may responsibly be claimed

- **[Documented/reconstructed]** Pingala’s school systematically enumerated all two-state metrical patterns and used recursive parity procedures.
- **[Scholarly reconstruction]** These algorithms are isomorphic to binary enumeration.
- **[Disputed popular claim]** “Pingala invented binary numbers” overstates the evidence if it means positional numerals `0,1` with ordinary arithmetic.
- **[Legend/modern inflation]** “Pingala invented computer code” is anachronistic.
- **[Incorrect conflation]** The prosodic use of *śūnya* in later exposition does not by itself make Pingala the inventor of the mathematical zero digit.

Kim Plofker treats this material within the specialised setting of Indian prosody and combinatorics, not as a direct ancestor of European binary computing (*Mathematics in India*, Princeton, 2009; [publisher/review information](https://old.maa.org/press/maa-reviews/mathematics-in-india)). A source-based study with translations of the prosodic algorithms is available from the University of Hyderabad ([Sanskrit Prosody and Binary Arithmetic](https://www.ms.uky.edu/~sohum/ma330/files/chennai_talks/Emch_Sridharan_Srinivas%20-%20Contributions%20ot%20the%20History%20of%20Indian%20Mathematics%20%282005%29.pdf)).

No documentary chain joins Pingala to Harriot, Caramuel, Leibniz, or Shao Yong. Independent development is the evidentially conservative position.

---

## 5. Shao Yong’s arrangement

Shao Yong (1011–1077), a Song dynasty philosopher associated with “images and numbers” learning, arranged the trigrams and hexagrams in diagrams later called “Earlier Heaven,” “Prior Heaven,” or “Fu Xi” arrangements.

**[Documented historical association]** These arrangements systematically divide configurations according to their lines. With appropriate choices of reading direction and polarity, the sequence corresponds to binary integers.

**[Dispute]** Some historians call the diagram genuinely binary because it recursively orders two symbols. Others object that:

- it was not used for positional arithmetic;
- Bouvet and Leibniz read the diagram in a direction foreign to its Chinese use;
- “binary” can mean two-element combinatorics or specifically base-two numeration.

Marie-Julie Maitre’s recent analysis argues that the diagram is structurally binary even though its construction and use differ from Leibnizian arithmetic; the controversy is therefore largely about what “binary” is allowed to denote ([Science in Context article record](https://openurl.ebsco.com/contentitem/doi%3A10.1017/s0269889725100665?id=ebsco%3Adoi%3A10.1017%2Fs0269889725100665&sid=ebsco%3Aplink%3Acrawler)).

There is no evidence that Shao Yong intended the lines as zero and one or calculated sums and products in base two.

---

## 6. Francis Bacon’s biliteral cipher, 1605/1623

**[Documented text]** In *The Advancement of Learning* (1605), Francis Bacon announced a cipher in which letters could be reduced to combinations of two forms. He presented a fuller Latin account and alphabet in *De augmentis scientiarum* (1623).

Using five positions, each in state `a` or `b`, gives \(2^5=32\) possible groups—enough for Bacon’s reduced Latin alphabet. A typical modern transcription begins:

```text
A  aaaaa
B  aaaab
C  aaaba
D  aaabb
...
```

Bacon proposed concealing the two forms through differences in typeface or other perceptible paired features. His striking principle was that the method works through anything capable of two differences—*omnia per omnia*, conventionally glossed “anything by anything.”

- **[Documented]** This is a two-symbol, fixed-length code.
- **[Classification]** It is binary encoding, not positional numerical arithmetic: `ababa` denotes a letter by table lookup, not normally a number to be added.
- **[Disputed/legend]** Elizabeth Wells Gallup’s late-nineteenth-century claim that Bacon’s cipher concealed vast secret autobiographical and Shakespearean texts in early printing is rejected by mainstream textual scholarship. Irregular Renaissance typography does not supply the controlled two-font distinction her readings require.

Primary text: [Bacon, *Advancement of Learning*](https://oll-resources.s3.us-east-2.amazonaws.com/oll3/store/titles/1433/Bacon_AdvancementLearning0414.pdf). Gallup’s claims can be read in her own words in [*The Biliteral Cypher of Francis Bacon*](https://www.gutenberg.org/cache/epub/70119/pg70119-images.html).

---

## 7. Thomas Harriot, about 1600–1605

Thomas Harriot (1560–1621) left unpublished manuscript calculations in several bases.

**[Documented manuscript]** One sheet converts `1101101₂` to 109 by listing 64, 32, 8, 4, and 1. Another gives binary addition, subtraction, and multiplication. For example, it records:

```text
10110010₂ − 111011₂ = 1110111₂
```

or \(178-59=119\).

J. W. Shirley first brought this material prominently into the history of binary in “Binary Numeration before Leibniz,” *American Journal of Physics* 19 (1951), 452–454. MacTutor reproduces and explains the surviving calculations ([MacTutor: Harriot and binary numbers](https://mathshistory.st-andrews.ac.uk/Extras/Harriot_binary_numbers/)).

- **[Documented]** Harriot understood conversion and arithmetic in positional base two.
- **[Disputed dating detail]** The sheets are assigned approximately to the early seventeenth century, not dated by Harriot in a way equivalent to a printed title page.
- **[Documented reception]** They remained unpublished and exerted no demonstrated influence on Leibniz or twentieth-century engineering.
- **[Important distinction]** Harriot has priority in surviving European manuscript evidence but not in effective publication or transmission.

---

## 8. John Napier’s “location arithmetic,” 1617

**[Documented printed text]** In the final section of *Rabdologiae* (Edinburgh, 1617), John Napier described *arithmetica localis* performed with counters on a chessboard-like grid. Columns represent successive powers of two. Counters are placed, combined, and moved to perform addition, subtraction, multiplication, division, and root extraction.

Napier explicitly acknowledged the inconvenience of converting ordinary numbers into the new form and back. His binary-like representation was chiefly a working-board method rather than a standard two-digit written notation.

- **[Documented]** It is a published computational use of powers-of-two representation.
- **[Scholarly classification]** Robin Rider calls it a pioneering explanation of binary arithmetic as a computational aid.
- **[Reception]** It remained a curiosity and did not found a continuous school.

See the digitized [1617 *Rabdologiae*](https://library.si.edu/digital-library/book/rabdologiaseunu00napi) and the detailed Mathematical Association of America reconstruction ([Napier’s Binary Chessboard Calculator](https://old.maa.org/press/periodicals/convergence/john-napiers-binary-chessboard-calculator-napiers-rabdologiae)).

---

## 9. Juan Caramuel y Lobkowitz, 1670

Juan Caramuel y Lobkowitz (1606–1682), Cistercian cleric and later bishop, printed *Mathesis biceps vetus et nova* in 1670.

**[Documented printed text]** Pages 45–48 discuss representation in bases 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, and 60. Historians commonly call this the first printed European discussion of the positional binary system. Caramuel gave little nondecimal arithmetic beyond elementary succession/addition.

- **[Priority claim]** First known printed general presentation of base two in Europe.
- **[Reception]** The discussion was brief and apparently little noticed.
- **[Disputed]** A modern accusation that Leibniz plagiarized Caramuel argues that Leibniz knew Caramuel’s work directly or indirectly. Other manuscript scholarship reports no evidence that Leibniz saw *Mathesis biceps* and reconstructs his development from different mathematical problems. Earlier publication proves priority, not transmission or plagiarism.

Sources: [digitized bibliographic record](https://books.google.com/books/about/Ioannis_Caramuelis_Mathesis_biceps_Vetus.html?id=fieU6ZZRQ_UC); [MacTutor biography and quotation](https://mathshistory.st-andrews.ac.uk/Biographies/Caramuel/); the accusatory case in García et al., [“Who Discovered the Binary System and Arithmetic?”](https://pubmed.ncbi.nlm.nih.gov/28281152/); countervailing manuscript-based discussion in [Strickland, “The Development of Binary”](https://philpapers.org/archive/STRLON.pdf).

---

## 10. Leibniz before China: 1679–1701

Gottfried Wilhelm Leibniz (1646–1716) developed base-two arithmetic before receiving Bouvet’s hexagram diagram.

### The manuscripts

**[Documented manuscript]** *De progressione dyadica* survives under the shelf reference LH XXXV, 3, B 2, fols. 1–4 in the Leibniz papers. The date 15/25 March 1679—Old Style/New Style—is treated in current scholarship as the earliest securely dated Leibnizian binary document. Companion papers treat:

- conversion between decimal and binary;
- positional geometric progressions;
- addition, subtraction, multiplication, and division;
- binary fractions and periodic expansions;
- a proposed binary calculating mechanism;
- base sixteen, which Leibniz called “sedecimal” or “sedenary,” as a more practical notation.

The recent critical translation sequence is Richard Strickland and Harry Lewis, *Leibniz on Binary: The Invention of Computer Arithmetic* (MIT Press, 2022), whose contents and manuscript dates are listed by [MIT Press](https://direct.mit.edu/books/monograph/5492/Leibniz-on-BinaryThe-Invention-of-Computer).

### The machine sketch

**[Documented design, not constructed machine]** Leibniz imagined a device using holes or openings and falling marbles to embody 0/1 states and automate binary reckoning. It was a conceptual design, not a surviving operating digital computer.

This matters because “Leibniz built the first binary computer” is false. He analysed how simple repeated mechanisms could embody base-two arithmetic; no completed machine is documented.

### The creation medallion

In 1697 Leibniz sent Duke Rudolph August of Brunswick a design for a medallion pairing decimal and binary numbers. The proposed inscriptions treated unity as God and zero as nothing.

- **[Documented theological interpretation]** Leibniz explicitly used the generation of all numbers from 1 and 0 as an emblem of divine creation.
- **[Not a mathematical proof]** It is theological symbolism, not empirical cosmology.
- **[Later retelling]** Laplace famously summarized the episode by saying unity represented God and zero the void, and that Leibniz hoped the emblem might assist Christian conversion in China. MacTutor preserves this later account ([Harriot and binary numbers](https://mathshistory.st-andrews.ac.uk/Extras/Harriot_binary_numbers/)).
- **[Caution]** Laplace’s elegant formulation should not be silently substituted for Leibniz’s own correspondence.

---

## 11. Bouvet’s letter and the *Yijing*, 1701–1703

Joachim Bouvet (1656–1730) was one of the French Jesuits sent to the Qing court under Louis XIV’s missionary-scientific programme. He became a “Figurist,” seeking anticipations of Christian revelation in ancient Chinese texts.

Chronology:

1. **Before 1701:** Leibniz had already developed binary arithmetic.
2. **Early 1701:** Leibniz communicated his binary table to Bouvet.
3. **4 November 1701, Beijing:** Bouvet replied with a diagram of the sixty-four hexagrams derived from the arrangement associated with Shao Yong.
4. **1 April 1703:** according to manuscript reconstruction, Bouvet’s letter finally reached Leibniz.
5. **7 April 1703:** Leibniz wrote to Jean-Paul Bignon and prepared the binary memoir for the Paris Academy.
6. **1703/1705 bibliographic issue:** the memoir belongs to the Academy’s 1703 proceedings, although volumes or copies bear later printing dates.

Leibniz’s title was:

> *Explication de l’Arithmétique Binaire, qui se sert des seuls caractères 0 & 1; avec des remarques sur son utilité, & sur ce qu’elle donne le sens des anciennes figures chinoises de Fohy.*

“Explanation of binary arithmetic, which uses only the characters 0 and 1; with remarks on its usefulness and on the meaning it gives to the ancient Chinese figures of Fu Xi.”

**[Documented text]** Leibniz explains place-value binary, gives a table, and identifies the unbroken line with 1 and broken line with 0. He states that the Shao/Bouvet ordering runs through all six-place combinations.

**[Historically false traditional attribution]** Leibniz and Bouvet assigned the diagram to the legendary Fu Xi and treated it as extremely ancient. The particular systematic arrangement was associated with Shao Yong’s eleventh-century intellectual world, even though its figures drew on much older *Changes* traditions.

**[Legend overturned by chronology]** The *I Ching* did not inspire Leibniz to invent binary arithmetic. He sent binary to Bouvet; Bouvet recognized the formal parallel and sent the diagram back.

**[Scholarly judgment]** Gorai Kinzō called the relationship “only a purely formal correspondence.” Modern scholarship is divided over whether “formal” diminishes it too much: the combinatorial isomorphism is real, but ancient positional arithmetic is unattested ([Gorai article abstract](https://www.tandfonline.com/doi/abs/10.1080/00033798100200121); [Oxford, “The Yijing’s Journey to the West”](https://academic.oup.com/book/8934/chapter-abstract/155251802)).

Primary/near-primary translations: [Leibniz’s *Explanation*](https://www.leibniz-translations.com/binary), [Leibniz to Bignon, 7 April 1703](https://www.leibniz-translations.com/bignon1703), and [Bouvet to Leibniz, 4 November 1701](https://scicenter.online/filosofi-scicenter/joachim-bouvet-leibniz1-peking-novembre-52035.html).

---

# Arithmetic and instruments

## 1. Mental and finger reckoning

Binary finger counting assigns successive powers of two to fingers. A lowered and raised finger form the two states. Five fingers yield 32 configurations, representing 0–31; ten fingers yield 1,024 configurations, representing 0–1,023.

**[Modern technique]** There is no evidence that this was Leibniz’s normal method or that it represents an ancient continuous tradition. It is a modern pedagogical application of positional binary.

Its advantages are capacity and direct physicality. Its disadvantages are awkward finger independence, orientation ambiguity, and some culturally rude intermediate gestures.

---

## 2. Boards and counters

Napier’s *arithmetica localis* is the clearest early binary counting-board system. A counter’s location determines its power-of-two value. Two counters in one place are exchanged for one in the next, precisely the binary carry rule.

This belongs to the much wider history of reckoning boards, abaci, Chinese counting rods, Japanese soroban, Roman *calculi*, and medieval counter-casting. But no evidence makes the suanpan, soroban, Roman abacus, quipu, or ordinary rod numerals ancestors of modern binary:

- suanpan and soroban are normally decimal or bi-quinary instruments;
- Chinese counting-rod numerals are decimal positional signs;
- Roman boards commonly organize decimal subdivisions;
- quipu employ positional decimal knot registers;
- their two-state physical features do not convert them into base-two systems.

The maxim “anything with two states is binary” is too weak for historical classification. Every written text has ink and blank paper; that does not make every script a binary numeral system.

---

## 3. Textbook problems genuinely relevant to binary

Most canonical ancient arithmetic texts in the broad template—Plimpton 322, the *Nine Chapters*, Āryabhaṭa, Brahmagupta, al-Khwārizmī, Fibonacci, Sacrobosco, Pacioli, and Recorde—are not textual stages in binary’s transmission.

Their relevance is comparative:

- Egyptian doubling demonstrates a power-of-two algorithm.
- Indian prosody demonstrates recursive enumeration of paired states.
- Bacon demonstrates fixed-length two-form encoding.
- Napier demonstrates board calculation by powers of two.
- Harriot demonstrates written positional arithmetic.
- Caramuel prints general radix theory.
- Leibniz gives a systematic arithmetic and philosophical programme.
- Boole supplies algebraic logic.
- Shannon connects Boolean algebra to switching circuits.

There is no “binary Liber Abaci” or medieval contest between binary algorists and abacists. Medieval algorist–abacist conflict concerned Hindu-Arabic written decimal algorithms versus counters and boards.

---

## 4. John Napier’s worked operations

Napier’s board used transformation rules resembling:

- replace two counters in column \(2^n\) with one in \(2^{n+1}\);
- reverse that replacement to borrow;
- shift patterns for multiplication;
- convert to and from ordinary notation.

The method performed addition, subtraction, multiplication, division, and square-root extraction. The primary text calls the movement of counters almost a recreation rather than labour, but also admits conversion as its “small difficulty.” The method’s lack of adoption is itself evidence: human convenience did not favour long base-two expressions before automatic machinery.

---

## 5. Leibnizian arithmetic

Leibniz stressed the tiny operation tables: multiplication reduces to choosing zero or a shifted copy of the multiplicand; addition requires only the binary carry. He saw theoretical simplicity but also recognized long strings as a practical disadvantage. His consideration of hexadecimal for practice anticipates the modern programmer’s use of grouped binary.

He also investigated repeating fractional patterns. This is significant because it shows that his project was not merely a list of integers or a theological diagram but a general positional arithmetic.

---

# Transmission and replacement

Binary did not travel along one continuous “India → China → Europe → computer” road. The documented history is a convergence of independent strands.

```text
Sanskrit prosody ── two-state combinatorics ── no documented route to Europe
                                                      
Zhouyi figures ── Shao Yong ordering ── Bouvet ── Leibniz’s interpretation
                                                ↑
Harriot manuscripts ── no known transmission    │
Caramuel print ── disputed influence             │
Napier board ── limited reception                │
                                                │
Leibniz’s independent work from 1679 ───────────┘
                         │
                         ├── mathematical radix theory
                         ├── theological symbolism
                         └── later historical prestige
                         
Boole’s algebra of logic ── Shannon’s switching algebra
                                      │
relays / tubes / transistors ── electronic digital machines
```

## 1. From Leibniz to radix theory

Leibniz’s 1703 paper circulated through the learned institutions of Europe and secured his name to binary. Later mathematicians examined nondecimal bases as number theory, recreation, and pedagogy. Binary did not displace decimal commercial arithmetic because its strings are long and conversion costs are high.

Leibniz’s direct influence on every later computer designer should not be assumed. His historical prestige made binary intellectually familiar, but twentieth-century engineers also arrived at two-state logic from relays, telegraphy, Boolean algebra, and circuit economy.

---

## 2. George Boole, 1847 and 1854

George Boole (1815–1864) published *The Mathematical Analysis of Logic* in 1847 and *An Investigation of the Laws of Thought* in 1854.

**[Documented text]** Boole represented classes through algebraic symbols satisfying the “index law” \(x^2=x\). The special values 0 and 1 represented, respectively, the empty and universal classes in relevant interpretations.

**[Correction]** Boole did not simply turn Leibniz’s binary numerals into computer logic. His algebra had operations and interpretations broader than ordinary arithmetic on base-two numerals. `1 + 1 = 10₂` in binary arithmetic, while Boolean OR gives \(1\lor1=1\). Confusing the two erases the crucial difference between radix arithmetic and logic.

Primary edition: [Boole, *Laws of Thought* (1854)](https://openlibrary.org/books/OL33179161M/An_investigation_of_the_laws_of_thought).

---

## 3. Telegraphy and paired signals

Nineteenth-century telegraph codes turned sequences of distinguishable signal conditions into letters. Morse code is often called binary because it has dots and dashes, but actual transmission also requires gaps at several levels. Baudot-style fixed-length codes are closer to Bacon’s paired-state alphabet.

These systems established that language could be transmitted as combinations of discrete states, yet they were codes rather than necessarily binary numerical arithmetic.

---

## 4. Claude Shannon, 1937–1938

Claude Elwood Shannon submitted “A Symbolic Analysis of Relay and Switching Circuits” at MIT on 10 August 1937; it became his master’s thesis and was published in 1938.

**[Documented text]** Shannon showed that Boolean algebra could analyse and synthesize relay switching networks. Series connections model conjunction; parallel alternatives model disjunction; open and closed circuit conditions can be represented algebraically.

This was the decisive bridge between nineteenth-century symbolic logic and practical digital circuit design. It did not “invent binary,” but it made systematic two-state circuit engineering possible.

Primary source: [MIT digitization of Shannon’s thesis](https://dspace.mit.edu/bitstream/handle/1721.1/11173/34541425-MIT.pdf). Museum interpretation: [Computer History Museum, “How Do Digital Computers Think?”](https://www.computerhistory.org/revolution/digital-logic/12/269).

---

## 5. George Stibitz, 1937–1940

At Bell Laboratories in 1937, George Stibitz built the “Model K” adder on his kitchen table from relays and other components. It demonstrated binary addition. The later Model I Complex Number Calculator, completed in 1939–1940, used relay logic and supported remote operation.

- **[Documented artefact/history]** Model K is a proof-of-concept binary relay adder.
- **[Qualification]** The larger Bell calculator used binary-coded representations internally while presenting convenient decimal input/output; “binary machine” does not imply that operators typed naked strings of zeroes and ones.

See the [Computer History Museum timeline](https://www.computerhistory.org/timeline/computers/) and the [IEEE Computer Society biography](https://history.computer.org/stibitz.html).

---

## 6. Konrad Zuse and the Z3, 1941

Konrad Zuse’s Z1, built in Berlin in 1936–1938, used mechanical binary elements and binary floating-point concepts but was unreliable. His electromechanical Z3 became operational in 1941.

**[Documented machine]** The Z3 used roughly 2,300 relays, a 22-bit floating-point word, binary arithmetic, and punched film for programs. The original was destroyed in wartime bombing; Zuse constructed a replica in the 1960s, now at the Deutsches Museum.

**[Priority formulation]** The Deutsches Museum calls it the world’s first programmable binary computer and the first freely programmable, fully automatic calculating machine ([Deutsches Museum](https://www.deutsches-museum.de/en/museumsinsel/ausstellung/computers)).

**[Dispute]** “First computer” depends on criteria:

- programmable or fixed-function;
- automatic;
- general-purpose;
- electronic or electromechanical;
- stored-program or externally programmed;
- operational reliability;
- conditional branching;
- binary internal representation.

The Z3 is an excellent claimant for first working programmable automatic binary digital computer, but not for first electronic stored-program computer.

---

## 7. Atanasoff and Berry, 1939–1942

John Vincent Atanasoff and Clifford Berry built the Atanasoff–Berry Computer at Iowa State College to solve systems of linear equations.

Its innovations included:

- electronic vacuum-tube arithmetic;
- binary numbers;
- capacitive regenerative storage on rotating drums;
- separation of memory and arithmetic;
- special-purpose rather than general programmable operation.

**[Documented artefact/history]** It was a binary electronic special-purpose calculator, not a stored-program general-purpose computer.

**[Legal finding]** In *Honeywell v. Sperry Rand* (1973), Judge Earl R. Larson invalidated the ENIAC patent and found that subject matter claimed for ENIAC had been derived from Atanasoff after John Mauchly’s visit. The decision did not create a universally accepted philosophical definition of “the first computer”; it resolved patent claims on an extensive evidentiary record.

Primary legal record: [Iowa State digital collection](https://digitalcollections.lib.iastate.edu/atanasoff/items/atanasoff2655.html) and [judgment PDF](https://isuu00001library102stg.blob.core.windows.net/digital-objects/atanasoff/pdf/atanasoff2655.pdf).

---

## 8. Colossus, ENIAC, EDVAC, and stored programs

- **Colossus, 1943–1944:** electronic, digital, programmable through switches and plugboards, built for cryptanalysis; its logical processing was binary-like but it was not a general numerical stored-program computer.
- **ENIAC, completed 1945–1946:** electronic, general-purpose, programmable, but its numerical accumulators were decimal ring counters. Calling every electronic computer binary is therefore wrong.
- **EDVAC design, 1945:** binary and intended to store instructions and data in memory.
- **Manchester Baby, 21 June 1948:** first operational electronic stored-program computer in the strong sense of executing a program held in writable electronic memory.
- **EDSAC, 1949:** an early practical stored-program service computer.

**[Contested first]** Each machine can be “first” under a carefully specified property. Unqualified superlatives are advertising, not historical analysis. The Computer History Museum explicitly warns that quests for “the first computer” depend on definitions ([CHM, “The Neverending Quest for Firsts”](https://computerhistory.org/blog/the-neverending-quest-for-firsts/)).

---

## 9. Transistors and integrated electronics

Bell Labs’ John Bardeen and Walter Brattain demonstrated the point-contact transistor in December 1947; William Shockley developed the junction-transistor theory and design. Bell Labs announced the device publicly in 1948.

Transistors supplied reliable, compact two-state switching and amplification. Integrated circuits later placed many such devices on one substrate; microprocessors put complete processing units on chips. Binary’s engineering dominance arose because circuits can maintain, restore, and discriminate two separated state ranges robustly—not because electrical reality has only two values.

Official histories: [Bell Labs](https://www.nokia.com/bell-labs/about/history/) and [Computer History Museum transistor history](https://www.computerhistory.org/siliconengine/invention-of-the-point-contact-transistor/).

---

## 10. The bit and byte

### Bit

**[Documented etymology]** *Bit* abbreviates *binary digit*. John W. Tukey used and defined the term in a Bell Laboratories memorandum in January 1947. Claude Shannon’s 1948 “A Mathematical Theory of Communication” credited Tukey and gave the term its foundational information-theory role. An historical study reproduces the memorandum trail ([Annals account](https://cse.buffalo.edu/~rapaport/Papers/Papers.by.Others/bit.pdf)).

A bit is an information unit or binary position, not necessarily a literal printed `0` or `1`.

### Byte

**[Documented etymology]** Werner Buchholz coined *byte* during IBM Stretch design in June 1956. The spelling deliberately differed from *bite* so that it would not be confused with *bit*. A byte initially meant a variable-sized group used for character or field processing; eight bits later became dominant.

Today NIST defines a byte in its computing standards as eight bits, while noting the historical variability ([NIST byte glossary](https://csrc.nist.gov/glossary/term/byte); [NIST IR 8289](https://nvlpubs.nist.gov/nistpubs/ir/2020/NIST.IR.8289.pdf)).

Related terms:

- **nibble/nybble:** four bits, half an eight-bit byte;
- **word:** architecture-dependent processing unit;
- **octet:** explicitly eight bits;
- **bitmap:** array of bit-valued picture elements or flags;
- **bitwise:** operation applied separately to corresponding bits.

---

## 11. ASCII and Unicode

### ASCII

The American Standard Code for Information Interchange was first standardized as ASA X3.4-1963 and substantially revised in 1967. It is a seven-bit code with 128 positions.

ASCII encodes the decimal digit characters as:

| Character | Decimal code | Hex | Seven-bit binary |
|---:|---:|---:|---:|
| `0` | 48 | 30 | `0110000` |
| `1` | 49 | 31 | `0110001` |
| `2` | 50 | 32 | `0110010` |
| `3` | 51 | 33 | `0110011` |
| `4` | 52 | 34 | `0110100` |
| `5` | 53 | 35 | `0110101` |
| `6` | 54 | 36 | `0110110` |
| `7` | 55 | 37 | `0110111` |
| `8` | 56 | 38 | `0111000` |
| `9` | 57 | 39 | `0111001` |

A crucial distinction:

- the number five in binary is `101₂`;
- the ASCII character `5` is code 53, `0110101₂`.

The binary code represents a glyph identifier, not the glyph’s numerical value.

Sources: [Computer History Museum ASCII history](https://www.computerhistory.org/internethistory/1960s/) and [NBS/NIST history](https://www.govinfo.gov/content/pkg/GOVPUB-C13-310bc7b3121ed82b8f13fc15a5c9e639/pdf/GOVPUB-C13-310bc7b3121ed82b8f13fc15a5c9e639.pdf).

### Unicode

Unicode assigns every encoded character an abstract integer code point. UTF-8, UTF-16, and UTF-32 then represent those code points as sequences of code units.

Examples:

| Character | Identity | Code point | Code point in binary |
|---|---|---:|---:|
| `0` | DIGIT ZERO | U+0030 | `110000₂` |
| `1` | DIGIT ONE | U+0031 | `110001₂` |
| `Ⅻ` | ROMAN NUMERAL TWELVE | U+216B | `10000101101011₂` |
| `零` | CJK ideograph “zero” | U+96F6 | `1001011011110110₂` |
| `٠` | ARABIC-INDIC DIGIT ZERO | U+0660 | `11001100000₂` |
| `०` | DEVANAGARI DIGIT ZERO | U+0966 | `100101100110₂` |
| `𝋠` | MAYAN NUMERAL ZERO | U+1D2E0 | `11101001011100000₂` |
| `⚊` | MONOGRAM FOR YANG | U+268A | `10011010001010₂` |
| `⚋` | MONOGRAM FOR YIN | U+268B | `10011010001011₂` |
| `䷀` | HEXAGRAM FOR THE CREATIVE HEAVEN | U+4DC0 | `100110111000000₂` |

The “other numerals in this set” were not enumerated in the prompt, so a claim to list all fourteen systems’ characters would be unreconstructable. Unicode’s current chart index includes Roman, Greek, Brahmi, Cuneiform, Counting Rod, Mayan, Kaktovik, Ottoman Siyaq, Rumi, and many script-specific decimal digits ([Unicode chart index](https://www.unicode.org/charts/?level=1)). Binary encodes all of them as code points; it does not erase their historical numeral structures.

---

# People

## Piṅgala

Dates uncertain, conventionally placed in the last centuries BCE. The attributed *Chandaḥsūtra* systematizes Sanskrit metre. The named author is historically elusive; biography is mainly traditional.

## Fu Xi

A culture hero traditionally placed in remote antiquity and credited with trigrams, writing, hunting, and civilizational arts. **[Tradition/legend]** There is no contemporary inscription or securely dated artefact establishing him as a historical inventor of binary signs.

## Shao Yong (1011–1077)

Song philosopher and cosmologist whose recursively organized hexagram diagrams allowed Bouvet’s and Leibniz’s binary correspondence. His aim was cosmological ordering, not documented base-two calculation.

## Francis Bacon (1561–1626)

Statesman and philosopher who proposed the biliteral cipher. His genuine cipher later became attached to the Bacon–Shakespeare authorship industry, where demonstrable cryptography and speculative decipherment must be separated.

## Thomas Harriot (1560–1621)

Mathematician, astronomer, algebraist, and Virginia traveller. His binary work remained among private papers, helping explain its lack of historical influence.

## John Napier (1550–1617)

Scottish mathematician, inventor of logarithms and reckoning devices. His location arithmetic constitutes a published, instrument-based power-of-two calculus.

## Juan Caramuel y Lobkowitz (1606–1682)

Polymath and bishop. His radix survey has printed priority over Leibniz but limited known reception.

## Gottfried Wilhelm Leibniz (1646–1716)

Philosopher, mathematician, librarian, diplomat, calculator designer, and correspondent. His importance is not an uncontested “first” but the breadth of his synthesis: positional arithmetic, algorithms, fractions, mechanization, combinatorics, metaphysics, China, and publication.

## Joachim Bouvet (1656–1730)

French Jesuit at the Kangxi court. He made the decisive historical comparison between Leibniz’s table and Shao Yong’s hexagram diagram. He did not transmit ancient Chinese arithmetic to an uninformed Leibniz; he recognized an analogy after receiving Leibniz’s system.

## George Boole (1815–1864)

Created an algebraic treatment of logic and classes. His special 0/1 interpretations later became technologically actionable through Shannon.

## Claude Shannon (1916–2001)

Connected Boolean algebra to switching circuits in 1937 and founded mathematical information theory in 1948. He did not invent the word *bit*, but credited Tukey for it.

## George Stibitz (1904–1995)

Built relay binary arithmetic demonstrations and Bell Labs calculators.

## Konrad Zuse (1910–1995)

Designed mechanical and relay binary floating-point machines. The Z3’s reconstruction survives; the wartime original does not.

## John Vincent Atanasoff (1903–1995) and Clifford Berry (1918–1963)

Built a special-purpose electronic binary calculator. Their priority became central to the ENIAC patent litigation.

## John von Neumann (1903–1957)

His 1945 EDVAC draft publicized a binary stored-program architecture. The architecture was collaborative; naming it solely after von Neumann obscures Eckert, Mauchly, Goldstine, Burks, and the Moore School group.

## Werner Buchholz (1922–2019)

IBM engineer who coined *byte* during Stretch development.

---

# Culture

## 1. Divination and cosmology

The *Yijing* is binary in its repertoire of line forms but culturally far more than a numeral table. Hexagrams carry names, judgments, line texts, commentarial traditions, correlative associations, and divinatory transformations. Changing lines produce another hexagram; the significance lies in interpretation, not numerical addition.

Leibniz’s reading is an episode in early-modern intercultural hermeneutics:

- Bouvet sought Christian prefiguration in Chinese antiquity.
- Leibniz sought universal rational structures.
- Shao Yong’s diagram supplied a remarkable formal bridge.
- The result illuminated European conceptions as much as ancient Chinese intentions.

## 2. Theology

Leibniz’s 1/0 symbolism equated:

- 1 with God or unity;
- 0 with nothing;
- all numbers emerging from their combinations with creation from nothing through divine unity.

This symbolism belongs to a wider early-modern culture of emblems, medals, universal languages, and missionary apologetic. It was sincere but never a required interpretation of binary arithmetic.

## 3. Cryptography and steganography

Bacon’s biliteral cipher established a powerful cultural proposition: any carrier capable of two controlled forms can conceal writing. Later binary codes implemented this idea mechanically and electronically.

The Baconian authorship legends demonstrate the danger: if typography is allowed to vary arbitrarily and the decoding rules are adjusted after inspection, almost any text can be made to disclose a secret. A genuine cipher requires a stable alphabet, reproducible distinctions, and results not selected ad hoc.

## 4. Literature

Binary and two-state combinatorics became symbols for:

- mechanical reason;
- the opposition of being and nothing;
- the possibility of universal language;
- permutation and exhaustive libraries;
- human life reduced to machine-readable choices.

Jorge Luis Borges’s “The Library of Babel” is not written as binary arithmetic, but its universe of all possible books belongs to the same combinatorial imagination. Umberto Eco’s *The Name of the Rose* and writing about labyrinthine libraries extend that cultural line. An Oxford study explicitly connects the *Book of Changes*, Leibniz, Borges, and Eco ([*Celestial Tapestry*, “The Book of Changes”](https://academic.oup.com/book/33813/chapter-abstract/288596942)).

Douglas Adams’s 42 became a programming joke because `101010₂` is visually alternating. The joke is retrospective: Adams’s narrative does not require base two.

## 5. Visual culture

Binary strings appear in:

- digital-themed typography;
- clocks displaying hours, minutes, and seconds as bit columns;
- hacker and cyberpunk imagery;
- barcodes and machine-readable patterns;
- conceptual art contrasting on/off or presence/absence.

**[Modern myth]** The green “digital rain” in *The Matrix* is often described casually as binary. Its visible glyphs are not merely `0` and `1`; the association is atmospheric rather than literal.

## 6. Law and administration

Binary itself rarely appears on coins, monumental dates, papal regnal numbers, or Super Bowls; Roman and decimal conventions dominate those settings. Binary’s legal importance lies instead in:

- patent disputes over electronic computation;
- statutory and contractual definitions of data units;
- encoding standards;
- computer evidence and digital signatures;
- software and communications regulation.

The 1973 ENIAC judgment is therefore binary culture’s closest counterpart to the “numerals in law” tradition.

## 7. Typography

Binary uses ordinary lining or old-style forms of `0` and `1` according to typeface. Ambiguity with capital `O`, lowercase `l`, and capital `I` encouraged:

- slashed or dotted zeroes;
- serifed ones;
- monospaced fonts;
- grouped bits;
- prefixes such as `0b1010`;
- suffixes such as `1010b`.

These are practical disambiguations, not new numeral systems.

---

# Controversies and disputes

## 1. Who invented binary?

There is no single answer until “binary” is defined.

| Candidate | Secure achievement | What is not secure |
|---|---|---|
| Egyptian scribes | Double-and-add computation using powers of two | Positional two-digit notation |
| *Yijing* tradition | Complete repertoire of six-position two-state figures | Arithmetic interpretation in early China |
| Piṅgala school | Algorithmic enumeration of light/heavy metrical patterns | Modern `0,1` arithmetic or computer code |
| Shao Yong | Recursive hexagram arrangement formally equivalent to a binary order | Use for base-two calculation |
| Bacon | Published two-form fixed-length alphabetic code | Binary numerical arithmetic |
| Harriot | Surviving positional base-two conversion and arithmetic | Publication or influence |
| Napier | Published location arithmetic with powers of two | Standard `0,1` positional notation and uptake |
| Caramuel | First known printed European radix-two exposition | Extensive binary algorithms or demonstrated influence on Leibniz |
| Leibniz | Independent systematic development, fractions, mechanization, philosophical interpretation, influential publication | Absolute first conception |
| Shannon | Boolean switching-circuit synthesis | Invention of binary numbers or Boolean algebra |

The historically useful formulation is:

> Harriot has early surviving manuscript priority for positional binary arithmetic in Europe; Caramuel has early printed priority for a radix-two exposition; Leibniz independently developed the fullest and historically influential early-modern binary arithmetic; older Indian and Chinese traditions exhibit profound binary-like combinatorics without a documented transmission chain to him.

## 2. Did Leibniz plagiarize Caramuel?

**For the accusation:** Caramuel’s publication predates Leibniz; Leibniz moved in overlapping learned networks; modern authors argue he had opportunities to know Caramuel.

**Against:** manuscript chronology shows Leibniz working through his own mathematical problems in 1679; no citation, copy, borrowing trace, or matching developmental sequence proves that he saw the relevant pages; Caramuel’s brief survey differs from Leibniz’s extensive algorithms and motivations.

Verdict: **[Disputed, unproven]** priority is certain; plagiarism is not.

## 3. Did the *I Ching* inspire binary?

No, if “inspire” means cause Leibniz’s invention. His dated binary manuscripts precede the 1701 Bouvet letter by twenty-two years.

Yes, in the limited later sense that the diagram:

- inspired Leibniz’s published comparison;
- strengthened his conviction that binary expressed a universal order;
- fed his theological and intercultural programme;
- helped shape the cultural afterlife of his arithmetic.

The popular statement “Leibniz read the *I Ching* and then invented binary” is a **modern chronological inversion**.

## 4. Were the ancient Chinese doing binary arithmetic?

Evidence for:

- two possible lines at each position;
- all \(2^6\) combinations;
- Shao Yong’s recursive ordering;
- exact convertibility to six-bit words.

Evidence against:

- no surviving addition, subtraction, multiplication, or conversion tables using the lines as positional digits;
- traditional functions are divinatory and cosmological;
- traditional line-number terminology uses 6–9;
- binary ordering requires choices of direction and polarity.

Verdict: **binary structure, yes; demonstrated positional binary arithmetic, no.**

## 5. Did Pingala invent zero and binary?

The strongest claim justified by the texts is two-state combinatorial enumeration with recursive procedures. Dating is approximate, the sūtras are terse, and detailed explanations come through later commentary.

Claims that Pingala invented the zero digit, modern binary numerals, Pascal’s triangle, Fibonacci numbers, recursion, and computer science all at once combine achievements from different texts, commentators, and concepts. Some analogies are mathematically illuminating; the bundled priority story is historically unsound.

## 6. Was Leibniz’s binary the direct ancestor of computers?

**[Qualified reconstruction]** Leibniz supplied a celebrated general account and imagined mechanization. But the practical twentieth-century line runs through Boolean algebra, relay engineering, telegraph codes, vacuum-tube circuits, and independent machine projects. Shannon’s explicit Boolean-switching synthesis is a much firmer technical bridge.

No evidence shows Zuse, Atanasoff, or every other pioneer simply constructing Leibniz’s machine proposal.

## 7. Which was the first binary computer?

Different answers correspond to different predicates:

- Z1: early mechanical binary programmable design, unreliable.
- Model K: working relay binary adder, not a general computer.
- ABC: electronic binary special-purpose calculator.
- Z3: working automatic programmable electromechanical binary computer.
- Colossus: electronic programmable special-purpose logical machine.
- EDVAC: early binary stored-program design, completed later.
- Manchester Baby: first operating electronic stored-program machine.

“The first computer” without qualifiers has no stable technical meaning.

## 8. Atanasoff versus ENIAC

The 1973 court found derivation and invalidated the ENIAC patent. That is documented law. Historians nevertheless distinguish legal patent findings from broader categories such as general-purpose programmability and practical influence. ABC’s electronic binary design was earlier; ENIAC was general-purpose and decimal; neither fact cancels the other.

## 9. Does a computer contain literal zeroes and ones?

Usually not as tiny printed characters. `0` and `1` are human notation for equivalence classes of physical states. Voltage ranges, charge, magnetization, optical reflectance, or transistor configurations implement bits. Their continuous physical behaviour is engineered so that two state regions can be treated discretely.

“The machine thinks only in zeroes and ones” is a serviceable metaphor, not a neurological or philosophical finding.

## 10. Does quantum computing abolish binary?

No. A qubit has a two-dimensional quantum state space and may occupy a superposition before measurement. Quantum computation differs radically from a classical bit, but measurement still yields one of two basis outcomes in the standard model. Quantum hardware also depends on extensive classical binary control and error processing.

## 11. Is binary inherently superior?

It is robust for two-state components and has extremely simple elementary arithmetic, but it is verbose for humans. Decimal machines have existed; balanced ternary machines have existed; multilevel cells store more than one bit per physical element. Binary dominance is an engineering and historical equilibrium, not a theorem that all computation must use radix two.

## 12. “There are 10 kinds of people…”

The joke reads `10` as two in binary: “those who understand binary and those who do not.” Variants adding a third category usually switch the joke to ternary. This is modern folklore, not an old Leibnizian aphorism.

## 13. “Binary is hidden in nature”

Day/night, male/female, life/death, yin/yang, open/closed, and being/nothing are frequently recruited as validations of binary. These are cultural classifications. Many have ambiguous, continuous, overlapping, or socially constructed intermediate cases. They show the cognitive power of opposition, not that nature is literally encoded in base two.

---

# Open questions

1. **Harriot’s chronology.** Can further paper, ink, watermark, or contextual analysis narrow the dates and internal sequence of his radix manuscripts?

2. **Caramuel’s reception.** Did any identifiable reader transmit the relevant pages of *Mathesis biceps* before Leibniz’s 1679 work? The current plagiarism dispute needs documentary linkage, not merely opportunity.

3. **Napier’s uptake.** Are there annotations, copied boards, or inventories showing actual seventeenth-century use of location arithmetic beyond the printed book?

4. **Shao Yong’s sources.** Which parts of the “Earlier Heaven” arrangement are securely attributable to Shao himself, his school, or later transmission?

5. **Early Chinese numerical intention.** Can excavated diagrammatic materials demonstrate arithmetic use of paired line structures, rather than only divinatory or cosmological classification?

6. **Pingala’s textual strata.** Which combinatorial procedures belong to the oldest recoverable *Chandaḥsūtra*, and which depend on Halāyudha and other commentators?

7. **Leibniz’s influences.** Recent scholarship proposes divisibility, perfect numbers, and geometric progressions as the immediate problems that generated his binary work. A definitive account depends on the ordering and dating of many manuscript leaves.

8. **Leibniz’s technological influence.** Which twentieth-century engineers demonstrably read his binary writings, rather than merely sharing the same general tradition?

9. **Global independent systems.** The Mangarevan mixed system, documented from nineteenth-century linguistic evidence, superposed binary steps on a decimal structure: special words represented 10, 20, 40, and 80. Andrea Bender and Sieghard Beller argue that it facilitated calculation and was locally invented before sustained European influence ([PNAS study](https://math.hawaii.edu/~tom/ethnomathematics/PNAS-2013.pdf)). Further ethnographic comparison may reveal other systems that fail conventional “pure-base” classifications.

10. **Terminology.** Historians still need clearer vocabulary separating “two signs,” “two classes,” “powers-of-two algorithm,” “binary enumeration,” “positional base-two numeral,” “Boolean value,” and “binary physical device.”

---

# Assessment

Binary’s history is not a straight road from an ancient oracle to a laptop. It is a history of repeated recognition that two distinguishable states can generate large structured spaces.

The oldest relevant records contribute different pieces:

- Egyptian scribes exploited doubling.
- Indian prosodists enumerated light/heavy sequences.
- Chinese diviners and cosmologists organized broken/unbroken lines.
- Bacon encoded letters through two forms.
- Harriot calculated in positional base two.
- Napier moved counters through power-of-two locations.
- Caramuel printed radix theory.
- Leibniz joined notation, arithmetic, mechanism, metaphysics, and the *Yijing*.
- Boole algebraized logic.
- Shannon made that algebra a design language for switches.
- Zuse, Stibitz, Atanasoff, Berry, Flowers, the Moore School team, and others embodied discrete operations in machinery.
- ASCII, Unicode, networks, memory standards, and semiconductor engineering made binary the substrate through which the world’s other scripts and numeral systems now circulate.

The strongest conclusion is therefore neither “Leibniz invented everything” nor “the *I Ching* was already a computer.” Leibniz’s achievement was a historically consequential synthesis. The *Yijing* comparison was genuine, mathematically exact at the level of two-state configurations, philosophically fertile, and historically retrospective. The machine emerged only when this arithmetic met switching logic, materials, standards, and engineering institutions.

---

# Sources

## Primary and near-primary texts

1. Gottfried Wilhelm Leibniz, “Explication de l’Arithmétique Binaire” (1703), transcription/translation:  
   https://www.leibniz-translations.com/binary

2. Leibniz to Jean-Paul Bignon, 7 April 1703:  
   https://www.leibniz-translations.com/bignon1703

3. Leibniz, “Binary and the Hexagrams of Fuxi,” translated materials:  
   https://www.leibniz-translations.com/fuxi

4. French/German presentation of Leibniz’s 1703 text:  
   https://www.gheinz.de/news/leibniz/leibniz_1703_de.htm

5. Richard T. W. Arthur, translation of Leibniz’s *Explanation*:  
   https://kastalia.medienhaus.udk-berlin.de/odl/Leibniz.pdf

6. Joachim Bouvet to Leibniz, Beijing, 4 November 1701:  
   https://scicenter.online/filosofi-scicenter/joachim-bouvet-leibniz1-peking-novembre-52035.html

7. Francis Bacon, *The Advancement of Learning*:  
   https://oll-resources.s3.us-east-2.amazonaws.com/oll3/store/titles/1433/Bacon_AdvancementLearning0414.pdf

8. John Napier, *Rabdologiae* (Edinburgh, 1617), Smithsonian Libraries:  
   https://library.si.edu/digital-library/book/rabdologiaseunu00napi

9. Juan Caramuel y Lobkowitz, *Mathesis biceps vetus et nova* (1670), bibliographic/digitized record:  
   https://books.google.com/books/about/Ioannis_Caramuelis_Mathesis_biceps_Vetus.html?id=fieU6ZZRQ_UC

10. George Boole, *An Investigation of the Laws of Thought* (1854):  
    https://openlibrary.org/books/OL33179161M/An_investigation_of_the_laws_of_thought

11. Claude E. Shannon, “A Symbolic Analysis of Relay and Switching Circuits,” MIT thesis, 1937:  
    https://dspace.mit.edu/bitstream/handle/1721.1/11173/34541425-MIT.pdf

12. *Honeywell Inc. v. Sperry Rand Corp.*, findings, conclusions, and judgment, 1973:  
    https://isuu00001library102stg.blob.core.windows.net/digital-objects/atanasoff/pdf/atanasoff2655.pdf

13. Iowa State University, Atanasoff legal-decision collection record:  
    https://digitalcollections.lib.iastate.edu/atanasoff/items/atanasoff2655.html

14. Rhind Mathematical Papyrus historical edition:  
    https://en.wikisource.org/wiki/Page:The_Rhind_Mathematical_Papyrus,_Volume_I.pdf/21

## Standard historical surveys and books

15. Stephen Chrisomalis, *Numerical Notation: A Comparative History*, Cambridge University Press, 2010:  
    https://www.cambridge.org/core/books/numerical-notation/4C3107573159D539D04DD7307423FA36

16. Accessible copy of Chrisomalis, *Numerical Notation*:  
    https://glossographia.files.wordpress.com/2010/01/chrisomalis-numerical-notation.pdf

17. Ernest Davis, review and synopsis of Chrisomalis:  
    https://www.siam.org/publications/siam-news/articles/numerical-notation-systems-as-cultural-artifacts

18. Karl Menninger, *Number Words and Number Symbols: A Cultural History of Numbers*, trans. Paul Broneer, MIT Press, 1969:  
    https://books.google.com/books/about/Number_words_and_number_symbols.html?id=89tLAAAAMAAJ

19. Menninger, Open Library record:  
    https://openlibrary.org/books/OL5612154M/Number_words_and_number_symbols

20. Georges Ifrah, *The Universal History of Numbers*, bibliographic review:  
    https://www.kirkusreviews.com/book-reviews/georges-ifrah/a-universal-history-of-numbers/

21. Joseph Dauben’s critical review of Ifrah, accessible copy:  
    https://es.scribd.com/document/204079257/Critique-de-Georges-Ifrah

22. Kim Plofker, *Mathematics in India*, Princeton University Press, 2009, MAA review:  
    https://old.maa.org/press/maa-reviews/mathematics-in-india

23. Joseph Needham, *Science and Civilisation in China*, Cambridge series record:  
    https://www.cambridge.org/core/series/science-and-civilisation-in-china/8D2C5F13F76CA8576578F1ECEEFAF072

24. Richard Strickland and Harry Lewis, *Leibniz on Binary: The Invention of Computer Arithmetic*, MIT Press, 2022:  
    https://direct.mit.edu/books/monograph/5492/Leibniz-on-BinaryThe-Invention-of-Computer

25. Richard Strickland, “The Development of Binary”:  
    https://philpapers.org/archive/STRLON.pdf

26. “Leibniz, Weigel and the Birth of Binary Arithmetic”:  
    https://lexicon.cnr.it/ojs/index.php/LP/article/view/478

27. “The Development of Binary Arithmetic by Leibniz”:  
    https://site-zmxaj2y2.wsecdn1.websitecdn.com/uploads/28ce969316734246868446e4a7878573.pdf/Maitre17-37?v=242009030214

## India and China

28. “Sanskrit Prosody, Piṅgala Sūtras and Binary Arithmetic”:  
    https://www.ms.uky.edu/~sohum/ma330/files/chennai_talks/Emch_Sridharan_Srinivas%20-%20Contributions%20ot%20the%20History%20of%20Indian%20Mathematics%20%282005%29.pdf

29. University of Hyderabad, *Pingala* materials:  
    https://sanskrit.uohyd.ac.in/Algorithms_in_Ancient_India/Material/Pingala.pdf

30. Edward Shaughnessy, *Unearthing the Changes*:  
    https://www.jstor.org/stable/10.7312/shau16184

31. Oxford Academic, “Recently Excavated Manuscripts”:  
    https://academic.oup.com/book/8934/chapter-abstract/155240726

32. Oxford Academic, “The Yijing’s Journey to the West”:  
    https://academic.oup.com/book/8934/chapter-abstract/155251802

33. Gorai Kinzō study of Leibniz and the hexagrams:  
    https://www.tandfonline.com/doi/abs/10.1080/00033798100200121

34. Marie-Julie Maitre, Shao Yong diagram and binary interpretation:  
    https://openurl.ebsco.com/contentitem/doi%3A10.1017/s0269889725100665?id=ebsco%3Adoi%3A10.1017%2Fs0269889725100665&sid=ebsco%3Aplink%3Acrawler

35. Brill, study of early *Zhou Changes* manuscripts and sequences:  
    https://doi.org/10.1163/9789004513945_003

36. Andrea Bender and Sieghard Beller, “Mangarevan invention of binary steps for easier calculation,” *PNAS* 111 (2014):  
    https://math.hawaii.edu/~tom/ethnomathematics/PNAS-2013.pdf

## Harriot, Napier, Caramuel, and contested priority

37. MacTutor, “Harriot and Binary Numbers”:  
    https://mathshistory.st-andrews.ac.uk/Extras/Harriot_binary_numbers/

38. J. W. Shirley, “Binary Numeration before Leibniz,” citation and reconstruction through MacTutor:  
    https://mathshistory.st-andrews.ac.uk/Extras/Harriot_binary_numbers/

39. MacTutor, Juan Caramuel biography:  
    https://mathshistory.st-andrews.ac.uk/Biographies/Caramuel/

40. García et al., “Who Discovered the Binary System and Arithmetic? Did Leibniz Plagiarize Caramuel?”:  
    https://pubmed.ncbi.nlm.nih.gov/28281152/

41. Sidney J. Kolpas and Erwin Tomash, “John Napier’s Binary Chessboard Calculator”:  
    https://old.maa.org/press/periodicals/convergence/john-napiers-binary-chessboard-calculator-napiers-rabdologiae

42. MacTutor, Napier’s rods:  
    https://mathshistory.st-andrews.ac.uk/Extras/Napier_rods/

43. MAA, “Russian Multiplication, Microprocessors, and Leibniz”:  
    https://old.maa.org/press/periodicals/convergence/russian-multiplication-microprocessors-and-leibniz

44. French scholarly history, *Le binaire au bout des doigts*:  
    https://doi.org/10.4000/12cux

## Computing history

45. Stanford Encyclopedia of Philosophy, “The Modern History of Computing”:  
    https://plato.stanford.edu/entries/computing-history/

46. Computer History Museum, Computing Timeline:  
    https://www.computerhistory.org/timeline/computers/

47. Computer History Museum, “How Do Digital Computers Think?”:  
    https://www.computerhistory.org/revolution/digital-logic/12/269

48. Computer History Museum, “The Neverending Quest for Firsts”:  
    https://computerhistory.org/blog/the-neverending-quest-for-firsts/

49. Deutsches Museum, Computers exhibition and Z3:  
    https://www.deutsches-museum.de/en/museumsinsel/ausstellung/computers

50. Deutsches Museum, Konrad Zuse research project:  
    https://www.deutsches-museum.de/forschung/forschungsinstitut/projekte/detailseite/konrad-zuse

51. IEEE Computer Society, George Stibitz:  
    https://history.computer.org/stibitz.html

52. Bell Labs computing history archive:  
    https://archive.computerhistory.org/resources/access/text/2022/08/102804421-05-01-acc.pdf

53. Bell Labs history, transistor:  
    https://www.nokia.com/bell-labs/about/history/

54. Computer History Museum, invention of the point-contact transistor:  
    https://www.computerhistory.org/siliconengine/invention-of-the-point-contact-transistor/

55. U.S. Army history of EDVAC:  
    https://ftp.arl.mil/mike/comphist/61ordnance/chap3.html

56. U.S. government history, ENIAC and later binary machines:  
    https://www.govinfo.gov/content/pkg/GOVPUB-D105-PURL-LPS58495/pdf/GOVPUB-D105-PURL-LPS58495.pdf

57. University of Pennsylvania, ENIAC trial exhibits finding aid:  
    https://archives.upenn.edu/collections/finding-aid/upd8_12/

## Standards, encoding, and terminology

58. Unicode 17.0, Yijing Hexagram Symbols:  
    https://www.unicode.org/charts/PDF/U4DC0.pdf

59. Unicode Yijing names list:  
    https://www.unicode.org/charts/nameslist/c_4DC0.html

60. Unicode Core Specification, Yijing:  
    https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-22/

61. Unicode character-chart index:  
    https://www.unicode.org/charts/?level=1

62. Unicode architecture and code points:  
    https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-2/

63. Unicode UTF FAQ:  
    https://www.unicode.org/faq/utf_bom.html

64. Computer History Museum, ASCII in 1963:  
    https://www.computerhistory.org/timeline/1963/

65. Computer History Museum, Internet/ASCII history:  
    https://www.computerhistory.org/internethistory/1960s/

66. U.S. government/NBS history of ASCII:  
    https://www.govinfo.gov/content/pkg/GOVPUB-C13-310bc7b3121ed82b8f13fc15a5c9e639/pdf/GOVPUB-C13-310bc7b3121ed82b8f13fc15a5c9e639.pdf

67. IBM ASCII, decimal, hexadecimal, octal, and binary table:  
    https://www.ibm.com/docs/en/aix/7.1.0?topic=adapters-ascii-decimal-hexadecimal-octal-binary-conversion-table

68. IBM, *Introduction to Data Processing Systems*:  
    https://bitsavers.org/pdf/ibm/generalInfo/GC20-1684-4_IBMdpIntroJul78.pdf

69. NIST byte glossary:  
    https://csrc.nist.gov/glossary/term/byte

70. NIST IR 8289, software measurement units:  
    https://nvlpubs.nist.gov/nistpubs/ir/2020/NIST.IR.8289.pdf

71. NIST binary prefixes:  
    https://physics.nist.gov/cuu/Units/binary.html

72. IEEE 754-2019 floating-point standard record:  
    https://standards.ieee.org/ieee/754/6210/

73. Historical study of the word *bit* and Tukey’s memorandum:  
    https://cse.buffalo.edu/~rapaport/Papers/Papers.by.Others/bit.pdf

74. Werner Buchholz/IBM Stretch “byte” documentary antedating:  
    https://listserv.linguistlist.org/pipermail/ads-l/2014-August/133656.html
