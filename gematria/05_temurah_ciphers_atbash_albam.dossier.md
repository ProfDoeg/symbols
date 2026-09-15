# Temurah: Atbash, Albam, Avgad and the letter-substitution ciphers: Research Dossier

## Basic identification

| Field | Identification |
|---|---|
| Primary name | **Temurah**, Hebrew תְּמוּרָה / תמורה, “exchange,” “substitution,” or “permutation” |
| Principal script | Hebrew square script; historically also paleo-Hebrew and cryptic scripts in related Second Temple practices |
| Core period | Biblical Atbash: textually attested in Jeremiah, substantially sixth century BCE in origin though transmitted in later manuscripts; systematic Jewish letter-combination: late antique and medieval; mature kabbalistic temurah: twelfth–thirteenth centuries onward |
| Principal regions | Judah/Babylonia; Roman Palestine; medieval Germany, Provence, Iberia and Italy; subsequently Christian Europe and modern occultism |
| Type | Rule-governed substitution or permutation of letters; related to, but not identical with, numerical gematria |
| Sister methods | **Gematria** גימטריא, numerical interpretation; **notarikon** נוטריקון, expansion or contraction through initials/finals; **tzeruf** צירוף, combination; **ḥillufei otiyyot** חילופי אותיות, exchanges of letters |
| Important warning | Temurah normally changes letters into letters. It has no intrinsic “table of numerical values.” Numbers enter when the substituted result is subsequently evaluated by gematria, or in systems such as **Aiq Bekar** whose classes are based on decimal values. |

### Standard Hebrew alphabet and numerical values

These are the values normally used if a temurah result is then calculated by standard gematria, *mispar hekhreḥi* (“necessary/absolute number”):

| Letter | Name | Value | Letter | Name | Value | Letter | Name | Value |
|---|---:|---:|---|---:|---:|---|---:|---:|
| א | alef | 1 | י | yod | 10 | ק | qof | 100 |
| ב | bet | 2 | כ / ך | kaf/final kaf | 20 | ר | resh | 200 |
| ג | gimel | 3 | ל | lamed | 30 | ש | shin | 300 |
| ד | dalet | 4 | מ / ם | mem/final mem | 40 | ת | tav | 400 |
| ה | he | 5 | נ / ן | nun/final nun | 50 |  |  |  |
| ו | vav | 6 | ס | samekh | 60 |  |  |  |
| ז | zayin | 7 | ע | ayin | 70 |  |  |  |
| ח | ḥet | 8 | פ / ף | pe/final pe | 80 |  |  |  |
| ט | tet | 9 | צ / ץ | tsadi/final tsadi | 90 |  |  |  |

In ordinary gematria the five finals ך ם ן ף ץ retain 20, 40, 50, 80 and 90. In *mispar gadol* they may instead be 500, 600, 700, 800 and 900. That second convention is especially important for **Aiq Bekar**, which needs twenty-seven forms—twenty-two ordinary letters plus five finals—to fill nine groups of three.

Hebrew is principally consonantal. Masoretic vowel-points, cantillation marks, punctuation, spaces and word dividers do not ordinarily enter either temurah or gematria. Matres lectionis—א ה ו י used as vowel letters—do count because they are written consonantal letters. Orthography therefore matters: plene and defective spellings can give different totals or different substitutions.

---

## The system in detail

### 1. What “temurah” covers

**Documented medieval and Renaissance classification.** In the standard artificial or practical Kabbalah, temurah is one member of a triad:

1. **Gematria**: interpret letters as numbers and compare totals.
2. **Notarikon**: expand letters as initials, or contract a phrase into initials or finals.
3. **Temurah**: replace, reorder or permute letters according to a declared rule.

The triad is prominently transmitted in Christian Kabbalah by Johannes Reuchlin and Cornelius Agrippa. It should not be projected unchanged onto Jeremiah. Jeremiah supplies ancient examples of a reverse-alphabet cipher, but does not call the device *temurah*.

A useful formal description is:

\[
f:\mathcal A\rightarrow\mathcal A
\]

where \(\mathcal A\) is the twenty-two-letter Hebrew alphabet. Each written letter is replaced by \(f(\text{letter})\). Some systems are involutions—applying them twice restores the original—while others are cycles or one-way shifts.

Spaces and word boundaries are normally retained for readability but are not part of the transformation. Final forms are generally normalized to כ מ נ פ צ before substitution; the output receives a final form if the resulting letter stands at the end of a word. A text using Aiq Bekar’s twenty-seven-character array may instead distinguish finals as independent members.

### 2. Atbash — אתב״ש

The name is a mnemonic made from its first two pairs:

- א ↔ ת: **AT**
- ב ↔ ש: **BSh**

It reverses the alphabet:

| Plain | א | ב | ג | ד | ה | ו | ז | ח | ט | י | כ | ל |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Substitute | ת | ש | ר | ק | צ | פ | ע | ס | נ | מ | ל | כ |

The remaining pairs repeat reciprocally:

| Pair | Pair | Pair | Pair | Pair | Pair |
|---|---|---|---|---|---|
| א ↔ ת | ב ↔ ש | ג ↔ ר | ד ↔ ק | ה ↔ צ | ו ↔ פ |
| ז ↔ ע | ח ↔ ס | ט ↔ נ | י ↔ מ | כ ↔ ל |  |

It is self-reciprocal:

\[
f(f(x))=x.
\]

In zero-based modern cryptographic notation for an alphabet of size 22,

\[
f(x)=21-x.
\]

#### Biblical examples

**Documented text, cipher identification traditional and philologically secure.**

Jeremiah 25:26 and 51:41 use שֵׁשַׁךְ, *Sheshach*. Atbash gives:

- ש → ב
- ש → ב
- כ → ל

Thus:

\[
ששך \rightarrow בבל
\]

or **Sheshach → Babel/Babylon**. Sefaria’s modern JPS note explicitly identifies Sheshach as a cipher for Babel. [Jeremiah 25](https://www.sefaria.org/Jeremiah.25-29) and [Jeremiah 51](https://www.sefaria.org/Jeremiah.51).

Jeremiah 51:1 has לֵב קָמָי, *Leb-kamai*. Applying Atbash:

- ל → כ
- ב → ש
- ק → ד
- מ → י
- י → מ

Therefore:

\[
לב\ קמי \rightarrow כשדים
\]

**Leb-kamai → Kasdim**, “Chaldeans/Chaldea.” The spelling works because the two words, after substitution, yield כשדים. The JPS annotation likewise calls it a cipher for Chaldea. [Jeremiah 51:1](https://www.sefaria.org/Jeremiah.51).

These are the earliest clear Hebrew specimens of the precise substitution later named Atbash. Whether their purpose was secrecy, literary indirection, political wordplay or all three remains debated. A cipher immediately decipherable to a literate reader is better understood here as an allusive pseudonym than secure encryption.

#### Dating

Jeremiah’s Babylon oracles belong to a complex textual history. The historical setting is the late seventh or early sixth century BCE; the book’s final Hebrew form is later, and the shorter Greek Jeremiah reflects a different edition. Accordingly:

- **Documented:** the Masoretic Hebrew text contains the transformations.
- **Scholarly reconstruction:** they probably originated in exilic or anti-Babylonian prophetic composition.
- **Not demonstrated:** that a fully named, generalized “Atbash system” already existed in Jeremiah’s lifetime.

### 3. Albam — אלב״ם

The name records the opening correspondences א–ל and ב–מ. Divide the twenty-two-letter alphabet into two halves of eleven and exchange corresponding positions:

| First half | א | ב | ג | ד | ה | ו | ז | ח | ט | י | כ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Second half | ל | מ | נ | ס | ע | פ | צ | ק | ר | ש | ת |

Thus:

\[
א↔ל,\ ב↔מ,\ ג↔נ,\ ד↔ס,\ ה↔ע,\ ו↔פ,\ ז↔צ,\ ח↔ק,\ ט↔ר,\ י↔ש,\ כ↔ת.
\]

Albam is also self-reciprocal. In a one-based positional alphabet it sends position \(i\) to \(i+11\) modulo 22.

Example, שלום:

- ש → י
- ל → א
- ו → פ
- ם, normalized מ → ב

so:

\[
שלום \rightarrow יאפב
\]

and, if evaluated numerically:

\[
10+1+80+2=93.
\]

**Historical status:** Albam is a traditional Jewish substitution alphabet, well established in medieval compilations and then in Christian Kabbalah. An ancient biblical use comparable in certainty to Sheshach/Babel is not known. Claims that Albam itself is “biblical” usually confuse the antiquity of alphabetic play in general with evidence for this particular table.

### 4. Avgad — אבג״ד

Avgad, sometimes written Abgad, is the forward shift:

\[
א→ב,\ ב→ג,\ ג→ד,\ldots,\ ש→ת,\ ת→א.
\]

Full table:

| Plain | א | ב | ג | ד | ה | ו | ז | ח | ט | י | כ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Shift | ב | ג | ד | ה | ו | ז | ח | ט | י | כ | ל |

| Plain | ל | מ | נ | ס | ע | פ | צ | ק | ר | ש | ת |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Shift | מ | נ | ס | ע | פ | צ | ק | ר | ש | ת | א |

This is not self-reciprocal. To decrypt, shift one position backward.

The best-known traditional application is **Kuzu** כוזו, written on the reverse of some mezuzah parchments:

\[
יהוה \rightarrow כוזו
\]

because י→כ, ה→ו, ו→ז, ה→ו.

The longer formula is:

\[
יהוה\ אלהינו\ יהוה
\rightarrow
כוזו\ במוכסז\ כוזו.
\]

**Documented tradition:** medieval Ashkenazi mezuzah practice and later scribal manuals.  
**Disputed theological inference:** that Kuzu is an independent “divine name.” In context it is a transformed form of the words adjacent to the Shema, functioning as protective and symbolic writing.

### 5. Achbi — אכב״י / אחב״י

Achbi mirrors letters **within each half** of the alphabet. With the first half א–כ and second half ל–ת:

\[
א↔כ,\ ב↔י,\ ג↔ט,\ ד↔ח,\ ה↔ז,\ ו↔ו
\]

and

\[
ל↔ת,\ מ↔ש,\ נ↔ר,\ ס↔ק,\ ע↔צ,\ פ↔פ.
\]

The two middle letters, ו and פ, remain fixed.

Example, שלום:

- ש → מ
- ל → ת
- ו → ו
- ם/מ → ש

Thus:

\[
שלום \rightarrow מתוש
\]

and:

\[
40+400+6+300=746.
\]

**Evidence label:** medieval/traditional cipher; its precise first attestation needs manuscript-level investigation. Modern websites frequently call it ancient without naming a manuscript. No evidence establishes its use by biblical authors.

### 6. Atbaḥ — אטב״ח

This system pairs letters within numerical decades so that their values complete 10, 100 or 1,000:

- units: א↔ט (1+9), ב↔ח (2+8), ג↔ז (3+7), ד↔ו (4+6); ה, value 5, is self-paired;
- tens: י↔צ (10+90), כ↔פ (20+80), ל↔ע (30+70), מ↔ס (40+60); נ, value 50, is self-paired;
- hundreds, using finals: ק↔ץ (100+900), ר↔ף (200+800), ש↔ן (300+700), ת↔ם (400+600); ך, value 500, is self-paired.

This illustrates the intimate relation between substitution and numerical classification: the cipher’s structure presupposes decimal letter-values.

### 7. Aiq Bekar / Ayak Bakar — אי״ק בכ״ר

Also spelled Aiq Beker, Aiq Bekar or Ayak Bakar. Its mnemonic begins with its first two groups:

\[
א\,י\,ק\quad ב\,כ\,ר.
\]

It groups letters by the same reduced decimal value:

| Reduced value | Chamber |
|---:|---|
| 1 | א י ק |
| 2 | ב כ ר |
| 3 | ג ל ש |
| 4 | ד מ ת |
| 5 | ה נ ך |
| 6 | ו ס ם |
| 7 | ז ע ן |
| 8 | ח פ ף |
| 9 | ט צ ץ |

The five finals supply 500–900 and complete the twenty-seven positions.

Two distinct operations must be separated:

1. **Jewish letter exchange:** cycle or substitute among members of a group, e.g. א→י→ק.
2. **Western “Qabalah of the Nine Chambers”:** draw nine boxes and mark which chamber and which member of it represents a letter. The Golden Dawn used this as a graphic reduction for constructing sigils.

The grouping is based on decimal reduction:

\[
ק=100\rightarrow1,\quad ר=200\rightarrow2,\quad ש=300\rightarrow3,
\]

and similarly for finals. It is therefore closer to a structured family of substitutions than to an ordinary monoalphabetic cipher.

**Traditional Jewish status:** documented as a kabbalistic cipher family.  
**Renaissance and occult reception:** Agrippa describes related “commutations” and character construction; nineteenth- and twentieth-century ceremonial magicians made “Nine Chambers” a standard sigil technique. Israel Regardie’s presentation explicitly reduces letters through Aiq Bekar before placing strokes on magical squares. [Regardie, *Complete Golden Dawn*](https://s3.us-west-1.wasabisys.com/luminist/EB/R/Regardie%20-%20The%20Complete%20Golden%20Dawn.pdf).

### 8. Akhas Beta — אח״ס בט״ע

This divides most of the alphabet into seven three-letter cycles:

\[
א→ח→ס→א
\]
\[
ב→ט→ע→ב
\]
\[
ג→י→פ→ג
\]
\[
ד→כ→צ→ד
\]
\[
ה→ל→ק→ה
\]
\[
ו→מ→ר→ו
\]
\[
ז→נ→ש→ז
\]

with ת left over or handled according to the particular table.

This is a reminder that “temurah” is not one cipher. Sources differ over direction, whether exchanges are reciprocal or cyclic, and how an unmatched letter is treated. A result is not reproducible unless the exact table and direction are stated.

### 9. Tzeruf in *Sefer Yetzirah*

*Sefer Yetzirah* does not simply prescribe Atbash. Its foundational operation is **ṣeruf/tzeruf**, combination or joining.

Its twenty-two “foundation letters” are:

- engraved,
- hewn,
- weighed,
- permuted or exchanged,
- and combined.

The “231 gates” are the unordered pairs of twenty-two different letters:

\[
\binom{22}{2}
=
\frac{22\times21}{2}
=
231.
\]

The text describes alef with every letter, bet with every letter, and so forth, and says the wheel turns “forward and backward.” [A historical translation and discussion](https://hermetic.com/heidrick/yetzirah); [David Blumenthal’s technical analysis](https://davidblumenthal.org/CreatorandComputer.html).

**Documented:** the received recensions contain letter-combination and 231-gate language.  
**Dating:** the work is difficult to date; proposals range from the first centuries CE into the early Islamic period. Its major recensions and commentaries are medieval.  
**Tradition:** attribution to Abraham.  
**Legend:** that it directly supplies an operational recipe by which Abraham, Rabbi Ḥanina, Rabbi Oshaia or the Maharal created a golem. The text’s combinatorial cosmology encouraged later golem manuals, but the familiar Prague golem story is much later folklore.

### 10. Abulafia’s ecstatic combination

Abraham Abulafia (1240–after 1291) made letter combination central to prophetic or ecstatic Kabbalah. His **ḥokhmat ha-tzeruf**, “science of combination,” involved:

- writing and permuting divine-name letters;
- vocalizing them with changing vowels;
- controlled breathing;
- head movements corresponding to vowel signs;
- visualization;
- gematria, notarikon and regular substitutions;
- dissolution of ordinary semantic language into a field of divine names.

Scholem described this as a “music of pure thought.” More exactly, in Abulafia’s theory language unfolds from the divine name, and substitutions can in principle continue indefinitely. Scholem’s essay specifically notes “Gematria, the acrostic, [and] substitution of letters in accordance with certain rules.” [Scholem, “The Name of God and the Linguistic Theory of the Kabbala”](https://journals.sagepub.com/doi/10.1177/039219217202008008).

Moshe Idel corrected older portrayals of Abulafia as marginal or merely eccentric, emphasizing his philosophical psychology, performance and prophetic aims. “Temurah” here is consequently broader than decoding: it is a disciplined means of altering consciousness.

### 11. Notarikon, the sister method

Notarikon derives an interpretation from initials or finals.

#### Expansion

Each letter becomes the initial of a word. The classic Christian-kabbalistic example is:

\[
אדם = א\text{דם},\ ד\text{וד},\ מ\text{שיח}
\]

or:

- א = אדם, Adam
- ד = דוד, David
- מ = משיח, Messiah

Thus **ADaM = Adam, David, Messiah**. This is documented in Renaissance Christian Kabbalah; presenting it as the original lexical meaning of אדם would be false.

#### Contraction

A phrase may be reduced to initials, as in:

\[
פרד״ס =
פשט,\ רמז,\ דרש,\ סוד
\]

*PaRDeS*: plain sense, hint, exposition and secret.

“First-letter” and “last-letter” notarikon are both attested categories. Modern occult sources sometimes call almost every acrostic “notarikon”; historically the method overlaps ordinary mnemonic abbreviation, scribal sigla and exegetical wordplay.

---

## Worked numerical examples and comparative systems

These are not all temurah. They are included to define the larger letter-number environment and prevent category errors.

### Hebrew standard gematria

#### Eliezer = 318

\[
אליעזר
=
א(1)+ל(30)+י(10)+ע(70)+ז(7)+ר(200)
=318.
\]

Genesis 14:14 says Abraham mustered 318 retainers. Nedarim 32a and midrashic tradition identify them homiletically with Abraham’s servant Eliezer. Rashi adopts the interpretation: Abraham went with Eliezer alone, whose name equals 318. [Nedarim 32a](https://www.sefaria.org/Nedarim.32a); [Rashi on Genesis 14:14](https://www.sefaria.org/Rashi_on_Genesis.14.14.3); [Baraita’s rule and example](https://www.posenlibrary.com/entry/midrash-thirty-two-attributes).

Ibn Ezra objects:

- **Documented dissent:** this is midrash, not the verse’s plain sense;
- he remarks in effect that Scripture does not speak through gematria and that such freedom can make a name mean almost anything. [Ibn Ezra on Genesis 14:14](https://www.sefaria.org/Genesis.14.14-16?lang2=en&with=Ibn+Ezra).

The example is therefore also an early statement of the coincidence and overfitting objection.

#### Ahavah = echad = 13

\[
אהבה
=
א(1)+ה(5)+ב(2)+ה(5)
=13
\]

\[
אחד
=
א(1)+ח(8)+ד(4)
=13.
\]

Traditional and Renaissance interpreters connect “love” and “one.” Reuchlin helped circulate this example in Christian Kabbalah. The arithmetic is exact; the theological implication belongs to interpretation, not arithmetic.

#### Naḥash = Mashiaḥ = 358

\[
נחש
=
נ(50)+ח(8)+ש(300)
=358
\]

\[
משיח
=
מ(40)+ש(300)+י(10)+ח(8)
=358.
\]

The serpent and Messiah equivalence became famous in kabbalistic and Christian-occult literature. The common sum is documented arithmetic; claims that it proves an identity, cosmic polarity or secret Christian prophecy vary by interpreter and are not entailed by the words themselves.

#### The Tetragrammaton = 26

\[
יהוה
=
י(10)+ה(5)+ו(6)+ה(5)
=26.
\]

This is one of the most consequential kabbalistic numbers. Neither vowel points nor proposed vocalization is counted. Its double, 52, and spelling-out expansions of the four letters produce further divine-name systems.

### Greek isopsephy

Greek alphabetic numerals use units, tens and hundreds:

- α–θ = 1–9,
- ι–ϟ = 10–90,
- ρ–ϡ = 100–900,

including the numeral signs stigma/digamma ϛ = 6, koppa ϟ = 90 and sampi ϡ = 900.

#### Jesus = 888

\[
ΙΗΣΟΥΣ
=
Ι(10)+Η(8)+Σ(200)+Ο(70)+Υ(400)+Σ(200)
=888.
\]

The Marcosian arithmetic reported and criticized by Irenaeus is exact. Irenaeus, writing about 180 CE, objects that the heretics reduce the Lord to 888 and manipulate alphabets, syllables and aeons. [Irenaeus, *Against Heresies* I.14–16](https://www.earlychristianwritings.com/text/irenaeus-book1.html); [standard Roberts–Donaldson text, I.14](https://www.logoslibrary.org/irenaeus/heresies/114.html).

#### Dove = 801

Greek περιστερά, *peristera*:

\[
Π(80)+Ε(5)+Ρ(100)+Ι(10)+Σ(200)+Τ(300)+Ε(5)+Ρ(100)+Α(1)
=801.
\]

The Marcosian interpretation joins 801 to alpha and omega:

\[
Α(1)+Ω(800)=801.
\]

This belongs to a Gnostic symbolic system in which letter counts, numerical values, aeons and the baptismal dove mutually interpret one another. It is preserved through an opponent, Irenaeus, and must therefore be read as hostile evidence, albeit unusually detailed hostile evidence.

#### Pompeii: “I love her whose number is 545”

The graffito, CIL IV 4861, reads:

> Φιλῶ ἧς ἀριθμός ΦΜΕ

“**I love [the woman] whose number is 545**.”

The numeral is:

\[
Φ(500)+Μ(40)+Ε(5)=545.
\]

The woman’s name is concealed behind its sum. It was found at Pompeii and therefore predates the eruption of 79 CE. This is firm epigraphic evidence that name-number riddles were popular practice rather than solely elite philosophy. [Ancient Graffiti Project, EDR165177](https://ancientgraffiti.org/Graffiti/graffito/AGP-EDR165177).

### Revelation’s beast

Revelation 13:18 asks the reader to “calculate” the beast’s number, usually transmitted as 666, with an ancient variant 616.

The influential modern solution transliterates Greek *Nerōn Kaisar* into Hebrew:

\[
נרון\ קסר
\]

\[
נ(50)+ר(200)+ו(6)+ן(50)+ק(100)+ס(60)+ר(200)
=666.
\]

Dropping the final nun to represent Latin *Nero*:

\[
נרו\ קסר
=
50+200+6+100+60+200
=616.
\]

**Documented:** 666 and 616 are ancient textual readings.  
**Scholarly reconstruction:** Nero is widely regarded as a strong candidate because both spellings explain the two numbers.  
**Important qualification:** the Nero solution itself first appears in modern scholarship in 1831; no surviving ancient commentator states it. A recent reassessment stresses that this absence weakens claims of certainty and explores Claudian alternatives. [Oxford, “Concealed Claudian”](https://academic.oup.com/jts/article/76/1/109/8043235); [survey of papyri, graffiti and inscriptions](https://www.tandfonline.com/doi/abs/10.1080/2222582X.2016.1218996).

Irenaeus knew 666 and warned that many names could be made to fit it. That is among antiquity’s clearest formulations of the multiple-solution problem.

### Arabic abjad

The common eastern abjad sequence and values are:

| Value | Letter | Value | Letter | Value | Letter | Value | Letter |
|---:|---|---:|---|---:|---|---:|---|
| 1 | ا | 10 | ي | 100 | ق | 1000 | غ |
| 2 | ب | 20 | ك | 200 | ر |  |  |
| 3 | ج | 30 | ل | 300 | ش |  |  |
| 4 | د | 40 | م | 400 | ت |  |  |
| 5 | ه | 50 | ن | 500 | ث |  |  |
| 6 | و | 60 | س | 600 | خ |  |  |
| 7 | ز | 70 | ع | 700 | ذ |  |  |
| 8 | ح | 80 | ف | 800 | ض |  |  |
| 9 | ط | 90 | ص | 900 | ظ |  |  |

Regional Maghribi arrangements differ in the later letters, so a chronogram must be calculated using the convention of its place and period.

#### Bismillah = 786

The commonly counted spelling is:

\[
بسم\ الله\ الرحمن\ الرحيم
\]

- بسم: ب(2)+س(60)+م(40)=102
- الله: ا(1)+ل(30)+ل(30)+ه(5)=66
- الرحمن: ا(1)+ل(30)+ر(200)+ح(8)+م(40)+ن(50)=329
- الرحيم: ا(1)+ل(30)+ر(200)+ح(8)+ي(10)+م(40)=289

Therefore:

\[
102+66+329+289=786.
\]

This conventional total depends on written orthography: the omitted alif in بسم and orthographic conventions in divine names matter. “786” is particularly popular in South Asian Muslim usage as a respectful numerical substitute or emblem. It is tradition, not a Qur’anic declaration that 786 is divinely mandated.

Arabic script descends paleographically from Nabataean Aramaic, but it does **not** follow automatically that the complete Islamic abjad-value system is a mechanically inherited Nabataean numeral notation. Script ancestry, alphabet order and numerical practice are separate historical questions. [Daniel Birnstiel Suchard on Nabataean Aramaic](https://onlinelibrary.wiley.com/doi/10.1111/aae.12234).

#### Abjad chronograms

In a **tārīkh** or chronogram, a meaningful word or line totals the year of an event. A Persian example cited in *Encyclopaedia Iranica* is *lawd*, “refuge,” recording 736 AH/1335 CE, the death-year of the Ilkhan Abū Saʿīd. Persian poets elaborated:

- *tārīkh-e maʿnawī*, meaningful chronogram;
- riddling *tārīkh-e taʿmiya*;
- additions or subtractions signaled by verbal clues;
- lines in which selected, dotted or undotted letters supply the date.

[Encyclopaedia Iranica, “Chronograms”](https://www.iranicaonline.org/articles/chronograms-pers/).

Ottoman Turkish poets called the genre **tarih düşürmek**, “to cast/drop a date.” Court poets composed chronograms for accessions, victories, mosques, fountains, births and deaths. The abjad total could be announced by an imperative such as “say its date,” leaving the final hemistich to encode the year.

The earliest securely identified **poetic** chronograms are medieval, with the genre becoming conspicuous around the fourteenth century; claims of an unbroken pre-Islamic poetic chronogram tradition lack evidence. [UAEU study of abjad dating](https://research.uaeu.ac.ae/en/publications/abjad-numerals-as-an-absolute-dating-method-forts-from-al-ain-uae/).

### Agrippa’s Latin table

In *De occulta philosophia* II.19–20, substantially composed earlier but printed in definitive form at Cologne in 1533, Agrippa adapts the units–tens–hundreds pattern to Latin:

| A | B | C | D | E | F | G | H | I |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

| K | L | M | N | O | P | Q | R | S |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |

| T | V/U | X | Y | Z | I/J variants |
|---:|---:|---:|---:|---:|---:|
| 100 | 200 | 300 | 400 | 500 | later tables may extend 600–900 |

The exact treatment of I/J, U/V and W varies because they were not yet three stable, independent modern alphabetic letters. Consequently, the online table commonly called “Jewish gematria” is often a modern normalization of an Agrippan Latin scheme, not a Jewish cipher.

Agrippa’s primary discussion says that Greek and Hebrew letters are divided into units, tens and hundreds and that other languages imitate them. [Agrippa, Book II](https://www.esotericarchives.com/agrippa/op2.htm); [1533 facsimile of the letter table](https://commons.wikimedia.org/wiki/File%3AAgrippa_lettertable.png).

---

## Origins: dated and placed

### Before alphabetic numerals: Sargon II

A Khorsabad inscription of Sargon II, king of Assyria 721–705 BCE, says that he made the circuit of Dūr-Šarrukīn’s wall **16,280 cubits**, “corresponding to the reading/numeral of my name.” Some copies or editions give 16,283, and the reconstruction of how the cuneiform name generated the number is disputed. [Israel Museum publication of Sargon’s cylinder](https://museum.imj.org.il/journal/archive/2018-2019/pdf/cylinder.pdf).

Status:

- **Documented:** the royal text associates a monumental measurement with the numerical reading of the king’s name.
- **Disputed reconstruction:** the precise sign arithmetic and whether 16,280 or 16,283 is primary.
- **Category caution:** cuneiform signs are not Hebrew-style alphabetic numerals. This is an early name-number analogue, not an Atbash specimen and not proof of direct transmission to Israel or Greece.

### Alphabetic numerals

Temurah’s substitution alphabets require a stable alphabetic order. Gematria and isopsephy additionally depend on letters functioning as numerals.

Greek alphabetic numeral notation developed through the addition of archaic numeral signs to form a 27-sign series. Hebrew numerical letters follow the same units–tens–hundreds architecture, but the date and route of borrowing are debated. Most scholars resist reading full alphabetic gematria into early biblical compositions before there is evidence that Hebrew letters were routinely used as numerals.

The priority questions must therefore be divided:

1. earliest name-number symbolism of any kind;
2. earliest alphabetic numeral notation;
3. earliest word-summing;
4. earliest Hebrew substitution;
5. earliest named kabbalistic taxonomy.

One culture can be earliest in one category without being the source of all the others.

### Jeremiah: sixth century BCE setting

As shown above, Sheshach/Babel and Leb-kamai/Kasdim are exact Atbash transformations. These are earlier than surviving rabbinic discussions and constitute the earliest secure Hebrew substitution evidence.

### Hellenistic Greek isopsephy

Alphabetic numerals were widely established by the Hellenistic period. Apollonius of Perga in the third century BCE presents sophisticated letter-number riddling, while inscriptions and later Pompeian graffiti demonstrate popular isopsephy.

**Scholarly reconstruction:** Jewish gematria probably developed in a multilingual Hellenistic and Roman environment where Greek alphabetic numerals and isopsephy were familiar.  
**Disputed stronger thesis:** Kieren Barry argues for Greek priority and influence on what he calls “Greek Qabalah.” His evidence for earlier Greek isopsephy is substantial; the further conclusion that Hebrew Kabbalah as a whole is Greek in origin is much broader and is not scholarly consensus. [Barry, *The Greek Qabalah*](https://books.google.com/books/about/The_Greek_Qabalah.html?id=w70rWN_-ANAC).

Franz Dornseiff’s *Das Alphabet in Mystik und Magie* (1922; expanded second edition 1925) remains a foundational comparative dossier on alphabet magic, vowels, acrostics, isopsephy, Gnosticism, magical papyri and Jewish materials. Its diffusionist judgments reflect the scholarship of its time and must be checked against later discoveries. [Google Books record](https://books.google.com/books/about/Das_Alphabet_in_Mystik_und_Magie.html?id=aAovAAAAYAAJ).

### Second Temple cryptic writing

The Dead Sea Scrolls contain several cryptic scripts, conventionally called Cryptic A, B and C, as well as occasional paleo-Hebrew and Greek characters. Texts including 4Q186 combine scripts and unusual writing directions.

**Documented:** Qumran scribes used substitutional or special alphabets to restrict or mark esoteric material.  
**Not established:** that all of these scripts are Atbash. “The Dead Sea Scrolls used Atbash” is too broad. Some Qumran cryptography uses special signs or mixed scripts rather than the twenty-two-letter reverse alphabet.  
**Interpretation:** secrecy, scribal training, prestige and marking restricted knowledge are all proposed.

### Rabbinic gematria and the Thirty-Two Rules

Gematria appears as rule 29 in a received form of the **Baraita of the Thirty-Two Rules attributed to R. Eliezer b. Yose ha-Gelili**, a second-century tanna. Some enumerations make it rule 28 or divide the rule differently. [Jewish Encyclopedia, “Rules of Eliezer”](https://www.jewishencyclopedia.com/articles/12935-rules-of-eliezer-b-jose-ha-gelili-the-thirty-two).

Critical qualification:

- **Tradition:** the rules belong to R. Eliezer in the second century.
- **Documentary history:** the full Baraita survives in medieval witnesses and was incorporated into *Midrash ha-Gadol*.
- **Modern dispute:** some scholars date the extant compilation considerably later, even to the tenth century.
- Thus it is unsafe to call the extant Baraita a manuscript “written in 200 CE.”

The Babylonian Talmud, redacted approximately fifth–sixth centuries CE, contains gematria arguments independently of the later Baraita’s manuscript date. Nedarim 32a preserves the Eliezer/318 exposition.

### Marcosians and Irenaeus, about 180 CE

Irenaeus’ *Against Heresies* I.14–16 is one of the richest early descriptions of letter-number cosmology. Marcus’ school analyzed:

- the twenty-four Greek letters;
- vowels and consonants;
- syllables of divine names;
- 888 for Jesus;
- 801 for the dove/alpha-omega;
- aeons grouped into numerical structures.

It is direct documentation that second-century Gnostic Christians used Greek isopsephy and alphabet symbolism. Because Irenaeus aims to refute them, his rhetoric must be separated from the practices he reports.

### Magical papyri

Greek and Demotic magical papyri, particularly Roman Egypt from roughly the first century BCE through the fourth century CE, employ:

- vowel strings;
- palindromes;
- divine names;
- charaktêres;
- alphabet sequences;
- numerical arrangements;
- voces magicae.

Some formulae are interpretable by isopsephy; others deliberately resist lexical interpretation. The papyri show a shared Mediterranean technology of letters, sounds, names and numbers, but not a single unified “gematria religion.”

### *Pistis Sophia*

The Coptic *Pistis Sophia*, usually dated to the third or fourth century CE, contains elaborate mystery names, repeated letters, seals and interpretations. Its sequences—such as repeated alpha, mu, omega, psi and phi—belong to late antique Gnostic letter mysticism. [G. R. S. Mead translation](https://sacred-texts.com/chr/ps/ps067.htm).

Calling every such passage “gematria” is reductive: pronunciation, graphic form, repetition and ritual transmission are as important as numerical value.

### *Sefer Yetzirah*

Its date remains one of the major open questions. The work is late antique or early medieval in surviving form, with Saadia Gaon’s tenth-century commentary providing a firm terminus for reception. Its creation through thirty-two paths, ten sefirot and twenty-two letters gave later Kabbalists a scriptural-cosmological grammar for tzeruf.

### Medieval Kabbalah

#### Ashkenazi Ḥasidim, twelfth–thirteenth centuries

The German Pietists used exact counting, divine names, prayer structures, gematria and letter combinations. Eleazar of Worms (c. 1165–c. 1230) is central, and *Sefer Razi’el ha-Malakh*, a composite work associated with this milieu, transmitted alphabets, names, seals, angelology and magical procedures.

#### Abulafia, thirteenth century

Abulafia transformed combination into a repeatable contemplative discipline, discussed above.

#### Zohar, late thirteenth-century Castile

The Zohar repeatedly treats Torah’s letters as living, creative and symbolic realities. It uses gematria, acronyms, changes of order and mythic narratives about letters. Tradition attributes it to the second-century Simeon bar Yoḥai; historical scholarship, beginning well before Scholem and consolidated by him, locates its principal composition around Moses de León’s late-thirteenth-century Castilian circle.

Both claims must be reported:

- **Traditional attribution:** revelation by Simeon bar Yoḥai and companions.
- **Scholarly reconstruction:** medieval composition drawing on earlier rabbinic and mystical traditions.

### Islamicate letter sciences

Arabic **ḥisāb al-jummal** calculates letter values; **ʿilm al-ḥurūf** studies occult properties of letters; **awfāq** are concordant or magic squares.

Aḥmad al-Būnī, active around 1225, became the most famous authority for letter magic, divine names and magic squares. Yet the printed *Shams al-maʿārif* attributed to him is a layered corpus, not a transparent authorial edition. Scholarship warns against treating it as a single summa preserving every earlier practice. [Noah Gardiner/Hallum-related study of early awfāq literature](https://wrap.warwick.ac.uk/id/eprint/117867/1/WRAP-new-light-early-arabic-literature-Hallum-2020.pdf).

The Arabic *Ghāyat al-Ḥakīm*, composed in al-Andalus in the tenth or eleventh century and translated into Latin as *Picatrix* in the thirteenth, joins astrology, talismans, names and numerical correspondences. Later readers sometimes project mature Būnian abjad-square practice into every part of the *Picatrix*; textual layers should be distinguished.

### Renaissance Christian Cabala and cryptography

#### Pico and Reuchlin

Giovanni Pico della Mirandola (1463–1494) claimed Kabbalah confirmed Christianity. Johannes Reuchlin’s *De verbo mirifico* (1494) and *De arte cabalistica* (1517) systematized Christian Cabala for Latin readers, including gematria, notarikon and temurah. His dialogue presents Jewish, Muslim and Pythagorean speakers, creating an imagined genealogy from ancient wisdom to Christianity. [Reuchlin edition information](https://www.frommann-holzboog.de/editionen/1706/170600211?lang=de).

The genealogy is theological-humanist construction, not documentary proof that Pythagoras learned a complete Kabbalah.

#### Trithemius

Johannes Trithemius (1462–1516) wrote *Steganographia* around 1499–1500 and printed *Polygraphia* in 1518. *Polygraphia* contains hundreds of substitution alphabets and wheels. *Steganographia* mixes angelic language with operational cryptography; the third book’s numerical-astrological ciphers were only conclusively demonstrated in modern scholarship. [Thomas Ernst’s decipherment](https://gwern.net/doc/cs/cryptography/steganography/1998-ernst.pdf).

#### Agrippa

Agrippa, Trithemius’ pupil, drafted *De occulta philosophia* around 1510 and published the full three-book form in 1533. Book III supplies tables of **ziruph**—tzeruf—and “commutations of letters and numbers,” including extraction of angel names. [Agrippa, Book III](https://www.esotericarchives.com/agrippa/agripp3b.htm).

#### Kircher

Athanasius Kircher (1602–1680) incorporated Cabala, combinatorial wheels, universal-language projects and hieroglyphic speculation into encyclopedic works. Much of his Egyptology is now obsolete, but his diagrams powerfully transmitted the visual idea that finite alphabets could generate universal knowledge.

#### Bacon and Vigenère: alleged “debt”

Francis Bacon’s biliteral cipher encodes letters through groups of two typefaces; Blaise de Vigenère’s *Traicté des chiffres* (1586/87) systematizes polyalphabetic ciphering. Both belong to the Renaissance expansion of combinatorial alphabets.

- **Documented intellectual environment:** Trithemius, Porta, Vigenère, Bacon and others knew a European tradition of alphabet tables and substitution.
- **Plausible influence:** Trithemius’ printed polyalphabets affected later cryptography.
- **Unproved stronger claim:** that Bacon’s or Vigenère’s central cipher was directly “borrowed from Atbash” or Jewish temurah. Alphabetic substitution is the shared structural principle, but Vigenère’s keyed polyalphabetic system and Bacon’s binary steganography are materially different inventions.

### Eighteenth- to twentieth-century numerology

Modern name numerology should not be retrojected onto Pythagoras.

L. Dow Balliett’s *The Philosophy of Numbers* (early twentieth century) and related books helped popularize English letter-to-digit reduction. “Cheiro” (William John Warner, 1866–1936) marketed a “Chaldean” name-number system through *Cheiro’s Book of Numbers*.

- **Documented modern system:** English names are assigned digits and reduced to personal numbers.
- **Traditional/marketing claim:** the tables descend from ancient Chaldea or Pythagoras.
- **Finding:** no ancient Babylonian or Pythagorean document contains the modern English A–Z grids. Their alphabet, spelling assumptions and reduction rules require a modern English orthographic setting.
- **Conclusion:** “Pythagorean numerology” and “Chaldean numerology” are modern systems bearing ancient prestige names.

### Golden Dawn and Crowley

The Hermetic Order of the Golden Dawn, founded in Britain in 1888, synthesized Hebrew Kabbalah, Renaissance magic, Rosicrucianism, tarot, astrology and Egyptianizing ritual. It taught:

- Hebrew letter values;
- notarikon and temurah;
- Aiq Bekar/Nine Chambers;
- planetary kameas;
- construction of spirit sigils by tracing letter-number positions.

Aleister Crowley (1875–1947), a former Golden Dawn member, and Allan Bennett compiled *Sepher Sephiroth*, published in *The Equinox* I.8 (1912). It is a numerical lexicon of Hebrew words arranged by value. *Liber 777* correlates columns of gods, colors, planets, tarot, Hebrew letters and other symbolic systems. [Crowley, *777 and Other Qabalistic Writings*](https://hermetic.com/crowley/777/index); [*Sepher Sephiroth*](https://hermetic.com/crowley/libers/lib500).

Crowley used traditional Hebrew arithmetic but placed it in a distinct Thelemic interpretive system. Equalities in *Sepher Sephiroth* are source material for occult meditation, not historical proofs about biblical authors.

### New Aeon English Qabalah

Crowley’s *Book of the Law* II.55 promises an “order & value of the English Alphabet.” James Lees developed the system now called English Qaballa or the ALW cipher in November 1976; Ray Sherwin publicly reported it in 1979, and materials appeared in *The New Equinox* in the early 1980s. [Hadean Press history](https://hadean.press/products/the-new-equinox).

Its order begins:

\[
A,L,W,H,S,D,O,Z,K,V,G,R,C,N,Y,J,U,F,Q,B,M,X,I,T,E,P.
\]

Values 1–26 are assigned in that order.

- **Documented:** twentieth-century invention by Lees and collaborators.
- **Practitioner claim:** discovered or revealed from Crowley’s manuscript.
- **Not ancient:** it is not Hebrew temurah, historical Jewish Kabbalah or Pythagorean mathematics.

---

## Uses

### Exegesis

Rabbinic authors used gematria and, less commonly, substitution to reinforce homilies. Early examples usually support an interpretation rather than independently establish law. Nazir’s conventional thirty-day term is related to:

\[
יהיה=י(10)+ה(5)+י(10)+ה(5)=30.
\]

The status of such deductions was contested. Ibn Ezra’s objection to Eliezer/318 shows that medieval Jewish interpreters did not uniformly grant numerical readings equal authority.

Kabbalists expanded the practice because Torah was understood as a divine arrangement in which no letter is accidental. Under that premise, reordered or exchanged letters could disclose latent names and structures.

### Meditation and prophecy

For Abulafia, permutation suspends ordinary meaning and redirects the intellect toward prophecy. Letter writing, breath and vocalization are bodily techniques, not merely paper puzzles.

The Baal Shem tradition—both the title “master of the Name” and later Hasidic stories about Israel ben Eliezer, the Baal Shem Tov (c. 1700–1760)—connects holy names, letter concentration and miraculous power. Stories must be stratified:

- manuals and amulets document techniques;
- later hagiography attributes healings, exorcisms and supernatural knowledge;
- the tales are evidence of reception, not automatically eyewitness biography.

### Amulets and magic

Jewish amulets employ:

- divine and angelic names;
- Psalm verses;
- permutations;
- magic squares;
- seals;
- letter substitutions intended to conceal or intensify names.

*Sefer Razi’el* is a major transmission vehicle, but its attribution to the angel Raziel’s revelation to Adam is legendary. The extant work is a medieval compilation.

Islamicate awfāq arrange numbers or their letter equivalents so that rows, columns and diagonals agree. Divine-name totals may determine the entries. Al-Būnī’s corpus became especially influential, though manuscripts differ greatly.

Greek magical papyri use alphabetic and vocalic sequences in ritual. Similarity of technique does not prove a single secret organization spanning Jewish, Christian, Greek and Arabic magic.

### Chronograms

Hebrew chronograms appear on:

- tombstones;
- synagogue inscriptions;
- title pages;
- approbations;
- colophons.

Often only letters marked by dots, enlarged type or a biblical quotation’s selected words count. The Hebrew year may omit the thousands, requiring contextual restoration.

Persian and Ottoman chronograms became prestigious poetic genres. Arabic chronograms also appear in buildings and manuscripts. Latin chronograms use Roman-numeral letters embedded in a phrase—IVXLCDM—with enlarged or capitalized letters indicating the date. Latin chronograms are consequently not Agrippan gematria unless an author explicitly uses Agrippa’s whole alphabet.

### Prophecy and polemic

Revelation’s 666 generated centuries of identification:

- Irenaeus proposed several Greek candidates but cautioned against certainty;
- medieval writers applied it to enemies and heretics;
- Reformation polemic manufactured papal totals, especially from forms such as *Vicarius Filii Dei*;
- Catholic controversialists reciprocated with Protestant names;
- modern interpreters have proposed Napoleon, Hitler, computers, barcodes and political leaders.

The standard polemical method chooses:

1. a convenient spelling or title;
2. a favorable alphabet;
3. inclusion or exclusion rules;
4. sometimes a multiplier or reduction.

These are historically real uses but weak identification procedures.

### Literature

Borges explicitly engaged Kabbalah in “A Vindication of the Kabbalah” (1932), “On the Cult of Books” (1951), the poem “The Golem,” and his 1980 lecture “La cábala.” His infinite libraries, aleph, divine names and exhaustive permutations are meaningfully comparable to Abulafian tzeruf. He acknowledged limited Hebrew; his Kabbalah is literary and philosophical reception, not rabbinic practice. [Poveda, “Abulafia in the Library”](https://www.ktavet.uw.edu.pl/files/Oriol_Poveda_art.pdf).

Georges Perec and Oulipo used mathematical constraints, lipograms and combinatorial structures. Perec’s *La Disparition* excludes the letter *e*. Scholarship fruitfully compares this attention to material letters with Kabbalah, but:

- **documented:** Oulipian constraint and arithmetic architecture;
- **interpretive comparison:** calling Perec’s constraints “temurah”;
- **not demonstrated:** that his principal procedures were derived from Atbash.

James Joyce’s works contain conspicuous number-play, multilingual puns and calendrical structures. Claims of particular hidden gematria require case-by-case evidence; there is no single canonical “Joycean gematria table.”

### Internet gematria and conspiracy culture

Modern calculators can apply dozens or hundreds of ciphers instantly. This changes the evidentiary situation: a user can search many spellings, phrases and transformations until a desired number appears.

Gematrinator formerly labeled an Agrippa-derived English table “Jewish” and now calls it “Latin.” Its own FAQ documents the renaming. [Gematrinator FAQ](https://gematrinator.com/faq).

Common modern inventions include:

- “English ordinal”: A=1 … Z=26;
- reverse ordinal;
- digit-reduced or “full reduction” systems;
- English extended units–tens–hundreds;
- Agrippa-derived “Jewish gematria”;
- “Satanic” offsets constructed to make SATAN equal 666;
- prime, triangular and square-number ciphers.

These systems are legitimate as declared modern games or occult practices. They become historically misleading when described as the cipher of the Hebrew Bible.

---

## People and key texts

| Date | Person/group | Role and text |
|---|---|---|
| 721–705 BCE | Sargon II and royal scribes | Khorsabad inscription equating wall circuit with numerical reading of royal name |
| Sixth century BCE setting | Jeremiah tradition | Sheshach/Babel and Leb-kamai/Kasdim Atbash |
| Third century BCE | Apollonius of Perga | Sophisticated Greek alphabet-number riddles |
| Before 79 CE | Anonymous Pompeian writer | “I love her whose number is 545” |
| Late first century CE | John of Patmos | Revelation 13:18, 666/616 |
| c. 180 CE | Marcus and Marcosians | Letter-number cosmology recorded by Irenaeus |
| c. 180 CE | Irenaeus of Lyons | *Against Heresies* I.14–16 and V.30; critic of numerical speculation |
| Second century by tradition; extant later | R. Eliezer b. Yose ha-Gelili | Thirty-Two Rules; gematria rule |
| Fifth–sixth centuries redaction | Babylonian rabbis | Nedarim 32a, Eliezer = 318; Berakhot 55a, Bezalel joining creation’s letters |
| Late antique/early medieval | Anonymous *Sefer Yetzirah* author(s) | Twenty-two letters, permutations, 231 gates |
| Tenth century | Saadia Gaon | Commentary on *Sefer Yetzirah* |
| c. 1165–c. 1230 | Eleazar of Worms | Ashkenazi pietist gematria, names and prayer mysticism |
| Thirteenth century | *Sefer Razi’el* compilers | Angelic names, alphabets, amulets and seals |
| 1240–after 1291 | Abraham Abulafia | Ecstatic Kabbalah and *ḥokhmat ha-tzeruf* |
| late thirteenth century | Moses de León/Zoharic circle | Zoharic letter symbolism, gematria and permutation |
| fl. c. 1225 | Aḥmad al-Būnī | Islamicate science of letters and awfāq |
| 1463–1494 | Pico della Mirandola | Christian Cabala theses |
| 1455–1522 | Johannes Reuchlin | *De verbo mirifico*; *De arte cabalistica* |
| 1462–1516 | Johannes Trithemius | *Steganographia*; *Polygraphia* |
| 1486–1535 | Cornelius Agrippa | *De occulta philosophia*, Latin values and Hebrew commutation tables |
| 1523–1596 | Blaise de Vigenère | *Traicté des chiffres* |
| 1561–1626 | Francis Bacon | Biliteral cipher |
| 1602–1680 | Athanasius Kircher | Combinatorial and universal-language syntheses |
| nineteenth century | Éliphas Lévi, Mathers, Golden Dawn founders | Integration of Kabbalah into ceremonial magic |
| 1866–1936 | Cheiro | Popular “Chaldean” name numerology |
| 1875–1947 | Aleister Crowley | *777*, *Sepher Sephiroth*, Thelemic gematria |
| 1897–1982 | Gershom Scholem | Historical study of Kabbalah and Abulafia |
| 1922 | Franz Dornseiff | *Das Alphabet in Mystik und Magie* |
| b. 1947 | Moshe Idel | Revisionist study of Abulafia, experience and technique |
| 1976 onward | James Lees and collaborators | English Qaballa/ALW |
| 1999 | Kieren Barry | *The Greek Qabalah* |
| twenty-first century | Calculator makers and online communities | Mass search across heterogeneous ciphers |

---

## Controversies and disputes

### 1. Mesopotamia, Greece or Israel?

There is no single priority answer.

- **Mesopotamia:** earliest cited monumental name-number statement, Sargon II; not alphabetic gematria.
- **Israel/Judah:** earliest secure Hebrew reverse-alphabet wordplay, Jeremiah.
- **Greece:** earliest abundant alphabetic numeral and word-sum evidence.
- **Rabbinic Judaism:** distinctive exegetical gematria developed in Greek-speaking and Aramaic-speaking environments.
- **Medieval Kabbalah:** systematic metaphysics and contemplative practice of permutation.

A linear claim—“Sargon invented gematria, which passed to the Hebrews, then Greeks”—exceeds the evidence. So does “Pythagoras invented Kabbalah.” Parallel invention and multiple transmissions are entirely possible.

### 2. The Pythagorean claim

Ancient Pythagoreans unquestionably cultivated number symbolism. What is not demonstrated is that Pythagoras used the modern repeating A=1–I=9 English-name table or taught Hebrew temurah.

Reuchlin’s Pythagorean speaker and later occult histories merge:

- Greek number philosophy;
- Hebrew Kabbalah;
- Christian revelation;
- prisca theologia, an alleged primordial wisdom.

That genealogy is documented Renaissance ideology, not modern historical proof.

### 3. “Chaldean” numerology

The modern Chaldean table assigns English letters to digits by claimed vibration or sound, often omitting 9. No cuneiform tablet contains this English grid. Cheiro and related occult authors popularized it under an ancient ethnic name. Its antiquity is unsupported.

### 4. The coincidence problem

Suppose a lexicon contains many thousands of words but ordinary gematria values occupy a much smaller range. Collisions are inevitable by the pigeonhole principle. They are especially frequent because:

- common letters cluster in value;
- word lengths occupy a narrow range;
- spelling variants multiply possibilities;
- prefixes and suffixes can be added;
- multiple ciphers may be tried;
- translations and transliterations add choices.

If a researcher searches \(C\) ciphers, \(S\) spellings and \(P\) phrases, the effective opportunity for a match grows roughly with \(C\times S\times P\). A post hoc equality is therefore much less probative than a prediction made in advance under fixed rules.

Historically, practitioners did not necessarily regard equal sums as proof of lexical identity. A strong traditional reading normally also uses semantic, scriptural or ritual context.

Ibn Ezra’s criticism of Eliezer/318 and Irenaeus’ warning that 666 fits many names show that the objection is not a modern secular novelty.

### 5. Barry, Dornseiff, Scholem, Idel, Weinreb and Kaplan

- **Dornseiff:** indispensable comparative collection; sometimes accepts broad lines of influence that later work must refine.
- **Barry:** effectively restores Greek evidence neglected in popular Kabbalah histories; his “Greek origin of Hebrew Qabalah” thesis is more controversial than his documentation of Greek isopsephy.
- **Scholem:** separated historical Kabbalah from timeless occult genealogy, dated the Zohar largely to medieval Castile and recovered Abulafia as a major phenomenon.
- **Idel:** criticized Scholem’s tendency to organize Kabbalah through a few dominant types and gave greater attention to technique, experience, performance and multiple centers.
- **Aryeh Kaplan:** valuable interpreter and translator of *Sefer Yetzirah*, especially for practical and combinatorial explanation; his proposed datings and lines of secret transmission are not universally accepted by academic historians.
- **Friedrich Weinreb:** developed an expansive twentieth-century symbolic reading of Hebrew numbers. His work has devotees but is not a substitute for philological dating or manuscript evidence.

### 6. Forgeries, pseudepigrapha and invented antiquity

Several different things are routinely conflated:

- **Pseudepigraphy:** a medieval text attributed to Adam, Abraham, Raziel or an ancient sage. This can be a conventional literary mode rather than modern fraud.
- **Composite transmission:** works such as *Sefer Razi’el* and the Būnian corpus accrete layers.
- **Renaissance prisca theologia:** historical authors sincerely claimed primordial transmission without modern source standards.
- **Modern invention with honest disclosure:** James Lees’s English Qaballa.
- **Modern invention presented as ancient:** English “Pythagorean” and “Chaldean” tables advertised as unchanged ancient science.
- **Modern relabeling:** Agrippa-derived Latin values called “Jewish gematria.”
- **Fabricated prediction:** choosing spellings and ciphers after an event, then claiming the match predicted it.

No well-documented ancient source supports the vast majority of internet “English gematria” ciphers.

### 7. Temurah and real cryptography

Atbash and Albam are monoalphabetic substitutions. Against frequency analysis they offer negligible security. Their historical functions include:

- euphemism;
- elite recognition;
- sacred transformation;
- mnemonic display;
- restricted scribal knowledge;
- allegory.

Trithemius and Vigenère belong to a later history in which variable alphabets and keys increase cryptographic security. Calling every substitution “Kabbalah” erases those innovations; denying any relation ignores the shared European fascination with tables, alphabets and permutations.

---

## Open questions

1. What is the earliest manuscript explicitly using *temurah* as the technical umbrella term for Atbash, Albam and related alphabets?
2. Which specific medieval Jewish manuscripts first display complete Albam, Achbi, Atbaḥ and Aiq Bekar tables?
3. Were Jeremiah’s Atbash forms intended as concealment, mockery, scribal demonstration or literary allusion?
4. How should the shorter Greek Jeremiah and differing Hebrew textual strata affect their dating?
5. Which Qumran cryptic scripts, if any, represent transformations of older named substitution systems?
6. What is the earliest securely dated use of Aiq Bekar as a nine-chamber graphic device rather than simply a letter class?
7. How much of Agrippa’s commutation material derives directly from Jewish informants, Reuchlin, converted Jewish authors or Latin compilations?
8. Did the Golden Dawn obtain its precise Nine Chambers sigil method directly from Agrippa, later grimoires, Mathers’ Hebrew studies or several channels?
9. Can manuscript stemmatics disentangle the historical al-Būnī from the expanding *Shams al-maʿārif* corpus?
10. What are the earliest securely dated Arabic, Persian and Ottoman poetic chronograms in each regional value order?
11. Can controlled corpus studies measure how often classical Hebrew words collide under each method while correcting for morphology and orthographic variation?
12. When did the Internet label “Jewish gematria” first become attached to Agrippa-derived English values?
13. Which literary claims about Joyce and Perec are based on explicit notebooks or authorial statements, and which are later analogies?
14. Was 666 originally designed for Nero, another ruler, a title, the word “beast,” Solomon imagery or a polyvalent set of references? The arithmetic alone cannot decide.
15. How should historians describe “invention” where a practitioner believes a new table was discovered through revelation rather than consciously devised?

---

## Sources: editions and URLs consulted

- Hebrew Bible, Jeremiah 25, Sefaria/JPS: https://www.sefaria.org/Jeremiah.25-29
- Hebrew Bible, Jeremiah 51, Sefaria/JPS: https://www.sefaria.org/Jeremiah.51
- Babylonian Talmud, Nedarim 32a, Sefaria: https://www.sefaria.org/Nedarim.32a
- Babylonian Talmud, Berakhot 55a:13, Sefaria: https://www.sefaria.org/Berakhot.55a.13
- Rashi on Genesis 14:14, Sefaria: https://www.sefaria.org/Rashi_on_Genesis.14.14.3
- Ibn Ezra on Genesis 14:14, Sefaria: https://www.sefaria.org/Genesis.14.14-16?lang2=en&with=Ibn+Ezra
- *Baraita of the Thirty-Two Rules*, Posen Library: https://www.posenlibrary.com/entry/midrash-thirty-two-attributes
- Jewish Encyclopedia, “Gematria”: https://sefaria.jewishencyclopedia.com/articles/6571-gematria
- Jewish Encyclopedia, “Atbash”: https://www.jewishencyclopedia.com/articles/2075-atbash
- Jewish Encyclopedia, “Rules of Eliezer b. Jose ha-Gelili, the Thirty-Two”: https://www.jewishencyclopedia.com/articles/12935-rules-of-eliezer-b-jose-ha-gelili-the-thirty-two
- Jewish Encyclopedia, “Baraita of the Thirty-Two Rules”: https://www.jewishencyclopedia.com/articles/2500-baraita-of-the-thirty-two-rules
- Jewish Encyclopedia, “Eliezer”: https://jewishencyclopediadev.sefaria.org/articles/5597-eliezer
- Encyclopaedia Judaica, 2nd ed., vol. 1: https://www.jevzajcg.me/enciklopedia/Encyclopaedia%20Judaica%2C%20v.%2001%20%28Aa-Alp%29.pdf
- *Sefer Yetzirah*, historical translation at Hermetic Library: https://hermetic.com/heidrick/yetzirah
- David R. Blumenthal, “The Creator and the Computer: Sefer Yetsira”: https://davidblumenthal.org/CreatorandComputer.html
- Aryeh Kaplan, *Sefer Yetzirah: The Book of Creation in Theory and Practice*: https://leonbahrmanministries.org/wp-content/uploads/2018/01/Aryeh-Kaplan-Sefer-Yetzirah2.pdf
- Gershom Scholem, *Kabbalah*: https://www.betemunah.org/kabbalah-gershom-scholem.pdf
- Gershom Scholem, “The Name of God and the Linguistic Theory of the Kabbala”: https://journals.sagepub.com/doi/10.1177/039219217202008008
- Moshe Idel, *Abraham Abulafia’s Esotericism: Secrets and Doubt*: https://www.ssoar.info/ssoar/bitstream/handle/document/70561/ssoar-2020-idel-Abraham_Abulafias_Esotericism_Secrets_and.pdf
- Moshe Idel, “Abraham Abulafia on the Messiah and the Pope”: https://www.mdpi.com/2077-1444/16/3/273
- Oriol Poveda, “Abulafia in the Library: Comparing Tzeruf ha-Otiyyot and Borgesian Letter Combinations”: https://www.ktavet.uw.edu.pl/files/Oriol_Poveda_art.pdf
- Irenaeus, *Against Heresies*, Book I, Roberts–Donaldson translation: https://www.earlychristianwritings.com/text/irenaeus-book1.html
- Irenaeus, *Against Heresies* I.14, Logos Library: https://www.logoslibrary.org/irenaeus/heresies/114.html
- Irenaeus, *Against Heresies* I.15, New Advent: https://www.newadvent.org/fathers/0103115.htm
- *Pistis Sophia*, G. R. S. Mead translation: https://sacred-texts.com/chr/ps/ps067.htm
- Ancient Graffiti Project, CIL IV 4861/EDR165177: https://ancientgraffiti.org/Graffiti/graffito/AGP-EDR165177
- Israel Museum, “The Cylinder Inscription of Sargon II”: https://museum.imj.org.il/journal/archive/2018-2019/pdf/cylinder.pdf
- Royal Inscriptions of the Neo-Assyrian Period, ORACC: https://oracc.museum.upenn.edu/rinap/rinap2/Q006603
- Franz Dornseiff, *Das Alphabet in Mystik und Magie*, bibliographic/scan record: https://books.google.com/books/about/Das_Alphabet_in_Mystik_und_Magie.html?id=aAovAAAAYAAJ
- Kieren Barry, *The Greek Qabalah: Alphabetic Mysticism and Numerology in the Ancient World*, 1999: https://books.google.com/books/about/The_Greek_Qabalah.html?id=w70rWN_-ANAC
- “Counting on God’s Name: The Numerology of Nomina Sacra,” *Harvard Theological Review*: https://doi.org/10.1017/s001781602510076x
- “Concealed Claudian: The Meaning of 666 in Revelation,” *Journal of Theological Studies*: https://academic.oup.com/jts/article/76/1/109/8043235
- “The Number of the Beast in Revelation 13 in Light of Papyri, Graffiti, and Inscriptions”: https://www.tandfonline.com/doi/abs/10.1080/2222582X.2016.1218996
- Encyclopaedia Iranica, “Chronograms”: https://www.iranicaonline.org/articles/chronograms-pers/
- “Abjad Numerals as an Absolute Dating Method: Forts from Al-Ain, UAE”: https://research.uaeu.ac.ae/en/publications/abjad-numerals-as-an-absolute-dating-method-forts-from-al-ain-uae/
- Daniel Birnstiel Suchard, “What Can Nabataean Aramaic Tell Us about Pre-Islamic Arabic?”: https://onlinelibrary.wiley.com/doi/10.1111/aae.12234
- Noah D. Gardiner/related awfāq study, “New Light on Early Arabic Awfāq Literature”: https://wrap.warwick.ac.uk/id/eprint/117867/1/WRAP-new-light-early-arabic-literature-Hallum-2020.pdf
- Princeton Islamic Manuscripts, *Kitāb al-Nūr al-sāṭiʿ wa-al-sirr al-qāṭiʿ fī ʿilm al-awfāq*: https://digital-collections.princeton.edu/i/%D9%83%D8%AA%D8%A7%D8%A8-%D8%A7%D9%84%D9%86%D9%88%D8%B1-%D8%A7%D9%84%D8%B3%D8%A7%D8%B7%D8%B9-%D9%88%D8%A7%D9%84%D8%B3%D8%B1-%D8%A7%D9%84%D9%82%D8%A7%D8%B7%D8%B9-%D9%81%D9%8A-%D8%B9%D9%84%D9%85-%D8%A7%D9%84%D8%A7%D9%88%D9%81%D8%A7%D9%82./item/a10564a7-607f-465b-bca5-0fc5433cb2fa
- Johannes Reuchlin, *De arte cabalistica*, edition record: https://www.frommann-holzboog.de/editionen/1706/170600211?lang=de
- Johannes Reuchlin, *De arte cabalistica*, digitization: https://sammlungen.ub.uni-frankfurt.de/freimann/content/titleinfo/404942
- Thomas Ernst, “The Numerical-Astrological Ciphers in the Third Book of Trithemius’s Steganographia”: https://gwern.net/doc/cs/cryptography/steganography/1998-ernst.pdf
- Cornelius Agrippa, *De occulta philosophia*, Book II: https://www.esotericarchives.com/agrippa/op2.htm
- Cornelius Agrippa, Book III, “Tables of Ziruph and the Commutations of Letters”: https://www.esotericarchives.com/agrippa/agripp3b.htm
- Agrippa’s 1533 letter table, facsimile: https://commons.wikimedia.org/wiki/File%3AAgrippa_lettertable.png
- Bibliothèques Virtuelles Humanistes, 1533 *De occulta philosophia*: https://www.bvh.univ-tours.fr/consult/index.asp?numfiche=785
- Israel Regardie, *The Complete Golden Dawn System of Magic*: https://s3.us-west-1.wasabisys.com/luminist/EB/R/Regardie%20-%20The%20Complete%20Golden%20Dawn.pdf
- Aleister Crowley, *777 and Other Qabalistic Writings*: https://hermetic.com/crowley/777/index
- Aleister Crowley and Allan Bennett, *Sepher Sephiroth*: https://hermetic.com/crowley/libers/lib500
- Hadean Press, *The New Equinox: The British Journal of Magick*: https://hadean.press/products/the-new-equinox
- Ancient/medieval cipher comparison table, Targum Molcho: https://targum.shaulmolcho.com/letters
- Gematrinator FAQ and cipher-name history: https://gematrinator.com/faq
- “In the Mirror of the Dream: Borges and the Poetics of Kabbalah”: https://www.jstor.org/stable/43298720
- “Metamorphoses of the Letter in Paul Celan, Georges Perec…”: https://ecommons.cornell.edu/bitstreams/6e3b52be-0c0d-40e2-b962-6a803458438d/download

