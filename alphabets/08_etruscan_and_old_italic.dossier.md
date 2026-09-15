# The Etruscan and Old Italic alphabets: Research Dossier

## Evidentiary key

- **[A — documented artefact]** Surviving object, inscription, excavation record, or scientific analysis.
- **[T — documented ancient text]** Statement preserved in an ancient literary source.
- **[R — scholarly reconstruction]** Mainstream inference from palaeography, linguistics, archaeology, or historical context.
- **[D — disputed]** Competing scholarly interpretations remain viable or the evidence is materially incomplete.
- **[Tr — tradition]** Premodern account transmitted as history or cultural memory but not independently demonstrated.
- **[L — legend]** Mythic narrative.
- **[M — modern invention/reception]** Modern typography, occultism, revival, pseudohistory, or popular adaptation.

Dates are BCE/CE. “Etruscan” below names both a language and the alphabets used to write it; “Old Italic” is a modern collective label for related but distinct scripts.

---

## 1. Basic identification

| Field | Identification |
|---|---|
| **Name** | Etruscan alphabet; collectively, the Old Italic alphabets. “Old Italic” is a scholarly and Unicode umbrella, not an ancient self-name. |
| **Type** | **Alphabet**: vowels and consonants are written as independent letters. It is neither an abjad nor a syllabary. |
| **Core inventory** | Archaic model alphabet: 26 signs on the Marsiliana tablet. Functional Etruscan inventories were smaller: approximately 22 signs in early practical writing and about 20 in the classical northern/southern standards, with regional variation. Unicode’s unified Old Italic repertoire presently contains 39 letters and four numerals, not one historical alphabet of 39 letters. |
| **Direction** | Predominantly **right-to-left** in mature Etruscan and many epichoric descendants. Early material also includes left-to-right, boustrophedon, spiral, circular, and vertical arrangements. Late left-to-right writing reflects, in some cases, Latin influence. |
| **Period** | Earliest Etruscan writing about 700 BCE; regional Old Italic traditions continue into the first century BCE and, exceptionally, approximately the first century CE. Etruscan itself appears to have ceased as a normal written vernacular under Romanization, though Roman authors still knew Etruscan religious learning. |
| **Region** | Etruria—chiefly Tuscany, western Umbria, and northern Lazio—plus Etruscan Campania and the Po valley. Related alphabets extended through central and southern Italy, Picenum, the Veneto, Lombardy, Liguria, Trentino–Alto Adige/Südtirol, Slovenia, and the Alpine zone. |
| **Immediate parent** | **[R]** A western, Euboean Greek alphabet used by colonists at Pithekoussai/Ischia and Cumae in the Bay of Naples, adopted in an Etruscan-speaking environment during the late eighth or early seventh century BCE. |
| **Ultimate ancestry** | Greek alphabet ← Phoenician consonantal alphabet; Greek innovators reassigned redundant Phoenician consonants to vowels. Etruscan inherited the already “full” Greek alphabetic treatment of vowels. |
| **Daughters and relatives** | **[R]** Latin, Faliscan, Oscan, Umbrian, South Picene, Venetic, Lepontic/Lugano, Raetic, Camunic, and several poorly attested local alphabets. Messapic is often grouped typologically with Old Italic but more probably derives independently from a Greek model. **[D]** One or more North Italic alphabets may have contributed to the creation of runes. |
| **Languages represented** | Non-Indo-European Etruscan and Raetic; probably non-Indo-European North Picene; Indo-European Latin-Faliscan, Oscan-Umbrian and other Sabellic languages, South Picene, Venetic, Lepontic/Cisalpine Celtic, and uncertain Camunic. |
| **Modern encoding** | Unicode block **Old Italic, U+10300–U+1032F**, introduced in Unicode 3.1 (2001) and subsequently expanded. ISO 15924 code: **Ital (210)**. |

Unicode itself summarizes the historical model: the ultimate source was Euboean Greek at Ischia and Cumae; the indigenous alphabets of much of Italy derive through Etruscan; and Latin probably arose from a south-Etruscan model, perhaps Caere or Veii, around the middle of the seventh century BCE. [Unicode 16, §8.6.1](https://www.unicode.org/versions/Unicode16.0.0/UnicodeStandard-16.0.pdf)

---

## 2. The script in detail

### 2.1 What kind of alphabet was it?

**[A/R]** Etruscan writing represents segmental vowels and consonants. Its four ordinary vowel letters were:

- 𐌀 **a**
- 𐌄 **e**
- 𐌉 **i**
- 𐌖 **u**

The Greek **o** sign occurs in archaic model alphabets, but Etruscan had no phonemic /o/ distinct from /u/ and therefore normally discarded it in practical Etruscan orthography. Faliscan, Latin, Venetic, and Lepontic retained or revived O because their languages needed it.

This is not a case of *matres lectionis* or later vowel pointing. The vowel principle had already been built into Greek writing: Phoenician signs for consonants absent from Greek were reassigned to Greek vowel phonemes. Etruscan borrowed those vowel letters as letters.

### 2.2 Archaic “model alphabet” and practical alphabet

The Marsiliana abecedarium reproduces an inherited theoretical row of 26 characters, conventionally transliterated:

> a b c d e v z h θ i k l m n ξ o p ś q r s t u x φ χ

That row was written right-to-left, so the actual signs face in their retrograde orientation.

**[A]** B, D, O, and a samekh/xi-like sign could be copied in abecedaria even though ordinary Etruscan did not require their Greek sound values.

**[R]** This distinction between a memorized teaching row and a functional orthography explains why “unused letters” occur on alphabet tablets but disappear from running texts.

**[R]** Etruscan lacked a phonemic contrast between voiced and voiceless stops comparable to Greek /b~p/, /d~t/, and /g~k/. Thus inherited B and D were superfluous, while gamma-shaped 𐌂, kappa 𐌊, and qoppa 𐌒 were assigned contextually to variants of /k/:

- C before **e, i**
- K before **a**
- Q before **u**

This convention was never perfectly mechanical and simplified over time. Southern Etruscan increasingly generalized C; northern traditions favored K in some periods.

### 2.3 Unicode table

The Unicode names are modern technical names, usually based on conventional transliteration; they are **not documented ancient Etruscan letter names**. Glyphs are displayed left-to-right by modern fonts even when the ancient inscription ran right-to-left.

| Order / code | Sign | Unicode name | Approximate historical value and use |
|---:|:---:|---|---|
| U+10300 | 𐌀 | OLD ITALIC LETTER A | /a/ |
| U+10301 | 𐌁 | LETTER BE | /b/ in donor alphabet and languages needing it; normally unused in Etruscan |
| U+10302 | 𐌂 | LETTER KE | Etruscan /k/, especially before front vowels; Oscan could employ it for /g/ |
| U+10303 | 𐌃 | LETTER DE | /d/ in other Italic languages; normally unused in Etruscan |
| U+10304 | 𐌄 | LETTER E | /e/ |
| U+10305 | 𐌅 | LETTER VE | /w/; conventionally *v* |
| U+10306 | 𐌆 | LETTER ZE | Etruscan affricate, conventionally /ts/ |
| U+10307 | 𐌇 | LETTER HE | /h/ |
| U+10308 | 𐌈 | LETTER THE | aspirated dental /tʰ/ or a related voiceless dental |
| U+10309 | 𐌉 | LETTER I | /i/, sometimes glide /j/ |
| U+1030A | 𐌊 | LETTER KA | /k/, especially before /a/ in archaic Etruscan |
| U+1030B | 𐌋 | LETTER EL | /l/ |
| U+1030C | 𐌌 | LETTER EM | /m/ |
| U+1030D | 𐌍 | LETTER EN | /n/ |
| U+1030E | 𐌎 | LETTER ESH | Samekh/xi-line sign; not normally part of mature Etruscan; values vary in descendants |
| U+1030F | 𐌏 | LETTER O | /o/ in Faliscan and other languages; normally unused for Etruscan |
| U+10310 | 𐌐 | LETTER PE | /p/ |
| U+10311 | 𐌑 | LETTER SHE | San/ś; Etruscan sibilant conventionally transliterated ś |
| U+10312 | 𐌒 | LETTER KU | Archaic Etruscan /k/ before /u/; /kʷ/ or related uses elsewhere |
| U+10313 | 𐌓 | LETTER ER | /r/ |
| U+10314 | 𐌔 | LETTER ES | /s/ |
| U+10315 | 𐌕 | LETTER TE | /t/ |
| U+10316 | 𐌖 | LETTER U | /u/ and possibly /w/ in some systems |
| U+10317 | 𐌗 | LETTER EKS | /ks/; especially Faliscan/other local use |
| U+10318 | 𐌘 | LETTER PHE | /pʰ/ |
| U+10319 | 𐌙 | LETTER KHE | /kʰ/; its position/value reflects western Greek, where X and Ψ differed from eastern/Ionic assignments |
| U+1031A | 𐌚 | LETTER EF | Etruscan /f/; developed after earlier VH/HV spellings |
| U+1031B | 𐌛 | LETTER ERS | Special Umbrian letter, commonly transliterated ř/rs; probably a rhotic or fricative development |
| U+1031C | 𐌜 | LETTER CHE | Special Umbrian sign; conventional transliteration ç; precise phonetic value debated |
| U+1031D | 𐌝 | LETTER II | Oscan í, representing a vowel distinct from ordinary I |
| U+1031E | 𐌞 | LETTER UU | Oscan ú, representing a vowel distinct from ordinary U |
| U+1031F | 𐌟 | LETTER ESS | Special South Picene sibilant |
| U+10320 | 𐌠 | NUMERAL ONE | 1 |
| U+10321 | 𐌡 | NUMERAL FIVE | 5 |
| U+10322 | 𐌢 | NUMERAL TEN | 10 |
| U+10323 | 𐌣 | NUMERAL FIFTY | 50 |
| U+1032D | 𐌭 | LETTER YE | Additional North Italic letter |
| U+1032E | 𐌮 | LETTER NORTHERN TSE | North Italic affricate sign |
| U+1032F | 𐌯 | LETTER SOUTHERN TSE | South/North Italic regional affricate sign |

Code points U+10324–U+1032C are unassigned in the current chart. The authoritative repertoire and character names are in the [Unicode Old Italic names list](https://www.unicode.org/charts/nameslist/n_10300.html).

### 2.4 Sound values and uncertainty

**[R]** Values are reconstructed by:

1. correspondence with the Greek donor alphabet;
2. spelling variation inside Etruscan;
3. Etruscan transcriptions of Greek names;
4. Greek and Latin transcriptions of Etruscan names;
5. bilingual inscriptions;
6. related Raetic and Lemnian material;
7. internal morphology.

**[D]** Exact phonetic realizations remain uncertain. Conventional /tʰ/, /pʰ/, and /kʰ/ are historically and graphically useful labels; whether every period maintained aspiration exactly as Greek did is less secure.

**[D]** The two Etruscan sibilants written S and Ś had dialect-dependent distributions. Northern and southern orthographic traditions could reverse which graph represented which sibilant category.

### 2.5 The letter F

**[A/R]** Etruscan /f/ was at first represented with a digraph, normally **VH** or **HV**. During the sixth century BCE, a new sign shaped approximately like 8, Unicode 𐌚, became the regular single-letter notation for /f/. Its invention is anonymous.

This was a genuine local graphic innovation, not a diacritic. Latin instead assigned the inherited digamma-shaped F to /f/, after an early FH spelling.

### 2.6 Direction and boustrophedon

- **[A]** The Marsiliana alphabet is right-to-left.
- **[A]** Most mature Etruscan inscriptions are right-to-left.
- **[A]** Archaic inscriptions may run left-to-right or boustrophedon.
- **[A]** Texts on pottery can follow rims, handles, circular fields, or the shape of the object.
- **[A/R]** Late left-to-right examples occur under growing Latin graphic influence.

Unicode assigns the Old Italic script strong right-to-left behavior even though some historical varieties were bidirectional. Modern scholarly transliteration is normally left-to-right.

### 2.7 Word division and punctuation

Early writing may be *scriptio continua*. Later conventions include:

- one, two, three, or four vertically arranged dots;
- short strokes;
- spaces;
- punctuation used irregularly as word division;
- line dividers or object-imposed divisions.

No universal punctuation standard existed.

#### Syllabic punctuation

**[A/R]** A special dotting system occurs in southern Etruscan teaching traditions and becomes characteristic of Venetic. It does not merely divide words. It marks graphs that stand outside the assumed open CV syllable pattern—for example a consonant not followed by a vowel, or a vowel following another vowel. Prosdocimi and Wachter independently connected the system with instruction by syllabic spelling. The practice is explained with examples in the [Mnamon Venetic writing dossier](https://mnamon.sns.it/index.php?id=31&lang=en&page=Scrittura).

### 2.8 Ligatures and diacritics

- **Ligatures:** **[A]** Occasional joined letters and compact monograms occur, especially where space is restricted, but Etruscan did not develop a canonical ligature system comparable to medieval Latin.
- **Diacritics:** **[A]** There was no productive accent or vowel-pointing system. Oscan Í and Ú and distinctive Umbrian signs are independent alphabetic characters, not optional accents in the modern sense.
- **Gemination:** Double consonants may be written, but practice varies by period and locality.
- **Abbreviation:** Personal names, offices, and formulaic expressions could be shortened, particularly on coins and labels; the conventions were not one pan-Italic standard.

### 2.9 Capitals, minuscules, handwriting, and typography

**[A]** Ancient Old Italic scripts did not possess a capital/minuscule opposition. Monumental, scratched, painted, stamped, and ink-written hands differ, but they are not paired cases like modern Latin A/a.

**[A]** The *Liber Linteus* proves that an Etruscan ink book-hand existed. Its letters remain fundamentally majuscule and separate.

**[R]** There was no independent Old Italic path to uncial or medieval minuscule. Those are developments of Greek and Latin book hands after the regional Old Italic traditions had disappeared.

**[M]** Modern fonts generally normalize signs into geometric capitals and provide mirrored glyph handling for right-to-left text. Typeface forms are scholarly reconstructions based on epigraphic exemplars, not continuations of an Etruscan scribal school.

### 2.10 Letter names and acrophony

**Absence of evidence:** no ancient source preserves a complete set of Etruscan letter names.

Unicode’s *A, Be, Ke, De,* and so forth are technical labels. Calling 𐌀 “alpha” or 𐌁 “beta” is convenient comparison, not proof that an Etruscan teacher used those words.

**[R/D]** Latin’s short letter names—*a, be, ce, de; el, em, en, er, es; ka; qu*—may reflect Etruscan pedagogical mediation. Particularly suggestive are *ka* and *qu*, which correspond to the Etruscan distribution of K before A and Q before U. B. L. Ullman argued this case in 1927, but the lack of directly attested Etruscan names prevents certainty. [Ullman, “The Etruscan Origin of the Roman Alphabet and the Names of the Letters”](https://www.journals.uchicago.edu/doi/10.1086/360949)

**[A/D]** A vase base, conventionally Pe 9.1 and dated about 550–500 BCE, carries an abbreviated alphabet and the sequence *abat…*. Michel Lejeune proposed that this was an Etruscan name for “alphabet,” assembled from initial letter names. The reading is suggestive, not a recovered naming list.

The Semitic meanings “ox” (*ʾalp*), “house” (*bēt*), and the acrophonic naming principle belong far upstream in the alphabet’s ancestry. Greek preserved altered forms *alpha, beta*, but their original lexical meanings were no longer Greek. Etruscan inherited sign order and values through Greek; it did not inherit pictorial ox- and house-symbolism as an active feature demonstrable in Etruscan practice.

---

## 3. Origins: dated and placed

### 3.1 Before Etruscan: the Euboean bridge

**[A/R]** Euboean settlers established Pithekoussai on Ischia in the eighth century BCE and Cumae on the Campanian mainland. Their western Greek alphabet retained digamma for /w/ and had the “western” supplementary assignments X = /ks/ and Ψ = /kʰ/.

No Greek abecedarium from Cumae itself survives. The identification of the donor as Euboean rests on:

- the alphabetic inventory;
- western assignments of the supplementary signs;
- letter forms;
- the location and chronology of Greek–Etruscan contact;
- Euboean inscriptions from the Bay of Naples.

The earliest Euboean writing at Pithekoussai includes the so-called Nestor’s Cup, conventionally about 725 BCE. It demonstrates that extended metrical alphabetic writing existed in the precise colonial contact zone shortly before the first Etruscan records. Richard Janko’s synthesis emphasizes the relevance of Pithekoussai, Methone, Eretria, Gabii, and Gordion to the early Greek chronology. [Janko, “From Gabii and Gordion to Eretria and Methone”](https://websites.umich.edu/~rjanko/Methone_final%20proofs.pdf)

### 3.2 The borrowing event

**[R]** The standard reconstruction is not that one named inventor designed “the Etruscan alphabet.” Etruscan elites, craftspeople, merchants, or bilingual intermediaries learned a Euboean alphabet in the late eighth century and adapted it to Etruscan.

Possible immediate settings include:

- Pithekoussai;
- Cumae;
- an Etruscan port or aristocratic center receiving Euboean teachers and goods;
- multiple connected contact points.

**[D]** Cumae is the conventional shorthand, but the actual place, agent, and whether transmission happened once or repeatedly are unknown.

### 3.3 The Marsiliana d’Albegna tablet

**[A]**

- **Object:** small ivory writing tablet whose recessed surface once held wax.
- **Findspot:** Circolo degli Avori, Banditella necropolis, Marsiliana d’Albegna near Manciano, Tuscany.
- **Discovery:** 1908.
- **Date:** conventionally about 700 BCE; sometimes placed in the first decades of the seventh century.
- **Present location:** Museo Archeologico Nazionale, Florence.
- **Text:** a 26-sign abecedarium incised around the frame, right-to-left.
- **Importance:** earliest securely contextualized complete Etruscan alphabet row and evidence for elite writing instruction.

A stable public museum inventory number could not be verified in the accessible official catalogue searched for this dossier; secondary web pages sometimes circulate numbers without a traceable collection record. That absence should not be filled by repetition.

The tablet’s signs include letters not needed for Etruscan. It therefore records a learned model close to its Greek exemplar, not the mature practical alphabet.

### 3.4 Other early abecedaria and inscriptions

**[A]** Seventh-century alphabet rows occur at Formello, Caere/Cerveteri, and on inscribed vessels. A bucchero cockerel-shaped alphabet vessel, approximately 650–600 BCE, is an especially famous teaching or display object.

**[A/R]** Early inscriptions are frequently possession, gift, maker, or speaking-object formulas: “I am [the object] of X,” “X gave/made me,” or a personal name. Such formulae permit interpretation by comparison with Greek, Latin, and other Italic texts even where individual words remain uncertain.

### 3.5 From model row to classical Etruscan alphabet

A simplified chronology:

| Period | Principal developments |
|---|---|
| c. 700–650 BCE | Full inherited model alphabet copied; variable direction; B, D, O and other redundant signs appear in abecedaria. |
| 7th–6th centuries | Practical inventories regionalize; B and D disappear from Etruscan text; C/K/Q distribution develops; VH/HV writes /f/. |
| 6th–5th centuries | 8-shaped 𐌚 replaces the /f/ digraph; southern and northern sibilant conventions diverge; right-to-left becomes dominant. |
| 5th–3rd centuries | Regional “neo-Etruscan” alphabets are more stable and reduced; punctuation and orthographic localism continue. |
| 3rd–1st centuries | Etruscan coexists increasingly with Latin; some late inscriptions turn left-to-right; the epichoric tradition contracts. |
| 1st century BCE–early imperial age | Vernacular inscription declines sharply. Etruscan ritual specialists and books remain known to Romans, but no continuing manuscript tradition survives. |

### 3.6 Decipherment: script versus language

The Etruscan alphabet was not deciphered by a single Rosetta-Stone event.

- **[R]** Renaissance antiquarians compared its signs with Greek and Latin, often mixing sound observations with fanciful etymology.
- **[M/forgery]** Annius of Viterbo’s 1498 *Antiquitates* linked Etruscan with the language of Noah and fabricated ancient authorities and inscriptions to glorify Viterbo. His constructions were influential despite early criticism.
- **[R]** Luigi Lanzi’s *Saggio di lingua etrusca* (1789) rejected much speculative “Oriental” comparison and correctly identified nearly all common letter values by systematic Greek/Latin comparison. This is the decisive modern milestone. [Lanzi, 1789 edition](https://books.google.com/books?id=RBNKAAAAcAAJ)
- **[A/R]** Jakob Krall recognized in 1891–92 that the writing on the Zagreb mummy wrappings was Etruscan and published it as a columnar linen book.
- **[A/R]** The Pyrgi tablets, excavated by Massimo Pallottino’s team in 1964, aided linguistic interpretation but did not decipher the already readable alphabet.

Thus:

> **The script is deciphered; the language is incompletely understood.**

Enrico Benelli notes that Lanzi understood all but one of the most common letters by 1789, while modern talk of “deciphering Etruscan” often confuses reading the graph system with translating the language. [INSCRIBE/University of Bologna](https://site.unibo.it/inscribe/en/conference-abstracts/enrico-benelli)

---

## 4. The major texts and objects

### 4.1 Pyrgi gold tablets

**[A]**

- **Findspot:** sanctuary of Pyrgi, port of Caere/Cerveteri, at modern Santa Severa.
- **Excavation:** 1964.
- **Date:** about 510 BCE.
- **Object:** three gold sheets pierced for attachment to a temple doorway.
- **Languages:** two Etruscan inscriptions and one Phoenician.
- **Named ruler:** Thefarie Velianas of Caere.
- **Cult:** dedication involving Uni and Phoenician Astarte.
- **Present collection:** Museo Nazionale Etrusco di Villa Giulia, Rome.
- **Corpus references:** commonly Etruscan Texts Cr 4.4–4.5 / TLE 874–875.

The museum describes the tablets as having been attached to Temple B and dates the complex to about 510 BCE. [Museo Nazionale Etrusco di Villa Giulia](https://www.museoetru.it/works/lamine-doro-da-pyrgi)

**[R]** The Phoenician and Etruscan texts overlap in event and cultic context but are not line-for-line translations. Therefore “bilingual” is correct in the broad epigraphic sense, while “Etruscan Rosetta Stone” is misleading.

### 4.2 Tabula Capuana

**[A]**

- **Object:** terracotta tile or tablet.
- **Findspot:** Santa Maria Capua Vetere, ancient Capua.
- **Date:** about 500–450 BCE.
- **Content:** long ritual/calendar text, incompletely understood.
- **Collection:** Antikensammlung, Staatliche Museen zu Berlin, **inv. 30892**.

It is one of the longest Etruscan texts. The Berlin record explicitly connects it with Etruscan calendrical and religious writing. [Staatliche Museen record](https://artsandculture.google.com/asset/tabula-capuana-unknown/kAHMSLRI1HBeiw?hl=en)

### 4.3 Liber Linteus Zagrabiensis

**[A]**

- **Object:** a linen book cut into strips and reused as wrappings for an Egyptian mummy.
- **Probable production:** inland northern or northeastern Etruria, perhaps around the Trasimene–Perugia–Cortona region.
- **Date:** palaeographically often c. third century BCE; the linen has a calibrated radiocarbon date centered about 390 BCE, which dates the textile rather than necessarily the writing.
- **Layout:** twelve columns written in ink; approximately 1,200 readable words, with repetition.
- **Content:** ritual prescriptions or a liturgical calendar; many details remain untranslated.
- **Modern history:** Mihajlo Barić acquired the mummy in Egypt in 1848/49; it entered the Zagreb museum in the 1860s.
- **Recognition:** museum curator Mijat Sabljar noticed the writing; Richard Francis Burton published it in 1879 while misidentifying it as runic; Jakob Krall recognized and published it as Etruscan in 1891–92.
- **Collection:** Archaeological Museum in Zagreb.

The Croatian national encyclopedia records the sequence of observation, Burton’s mistaken runic classification, Krall’s recognition, infrared photography in 1932, and modern conservation. [Hrvatska enciklopedija](https://enciklopedija.hr/clanak/liber-linteus-zagrabiensis) The museum identifies the mummy and Linen Book as central holdings. [Archaeological Museum Zagreb](https://amz.hr/en/museum/about-the-museum/)

**Absence of evidence:** why an Etruscan book reached Egypt and became embalming material is unknown. Trade, migration, recycling, or the possessions of an expatriate are possibilities, not established histories.

### 4.4 Cippus Perusinus

**[A]** A large stone boundary/legal text from near Perugia, generally dated to the third or second century BCE. Its forty-plus lines regulate land or boundary relations between the Velthina and Afuna families. It is one of the principal sources for Etruscan legal vocabulary.

### 4.5 Tabula Cortonensis

**[A/D]**

- **Object:** bronze tablet, originally eight pieces; seven survive.
- **Dimensions:** reconstructed at about 28.5 × 45.8 cm.
- **Date:** third–second century BCE.
- **Content:** legal transaction involving land and the Cusu family.
- **Collection:** MAEC, Cortona.

The discovery lacked a controlled archaeological excavation and was initially concealed, which produced understandable suspicion. The metal, writing, linguistic structure, and ancient breakage have nevertheless led specialists and the museum to accept it. Its find context remains irrecoverable. [MAEC Cortona](https://cortonamaec.org/en/museum-masterpieces/tabula-cortonensis/)

### 4.6 Piacenza liver

**[A]**

- **Found:** 1877 near Gossolengo.
- **Date:** second–first century BCE.
- **Object:** bronze model of a sheep’s liver.
- **Writing:** approximately forty divine names/labels divided across sectors.
- **Collection:** Museo Civico di Palazzo Farnese, Piacenza.

It is a technical-religious diagram for *haruspicy*, not an alphabet oracle. The city museum account records its discovery and donation in 1894. [Visit Piacenza / civic museum](https://visitpiacenza.it/en/art-and-culture/etruscan-liver/)

### 4.7 Vicchio/Poggio Colla stele

**[A]** Found in a sanctuary context in 2015, this sixth-century BCE sandstone stele bears multiple Etruscan texts and is among the longest early religious documents. Its secure excavation context makes it especially important even though much of the language remains difficult. [Fondazione Luigi Rovati](https://www.fondazioneluigirovati.org/en/events-exhibitions/exhibits/the-vicchio-stele/)

---

## 5. Spread and change

### 5.1 South into Latin and Faliscan

**[R]** Latin most probably borrowed a south-Etruscan alphabet, commonly localized to Caere or Veii, about the middle of the seventh century BCE.

Evidence includes:

- C used for both /k/ and /g/ in early Latin, reflecting Etruscan non-distinction;
- survival of K and Q in restricted environments;
- F descended from digamma but reassigned through the Italic handling of /f/;
- letter order inherited through the Etruscan model;
- Latin letter-name patterns plausibly mediated through Etruscan instruction.

Latin retained B, D, and O because Latin needed /b d o/. It eventually created G by adding a stroke to C, conventionally associated in Roman grammatical tradition with Spurius Carvilius Ruga in the third century BCE.

**[D]** “Borrowed from Etruscan” does not preclude continuing direct contact with Greek writing. Early central Italy was multilingual, and individual signs or practices could be refreshed from Greek models.

### 5.2 Umbrian

Umbrian used a native alphabet derived from Etruscan and, later, Latin script.

The **Iguvine Tables** are seven bronze tablets containing priestly ritual regulations:

- found at Gubbio by the fifteenth century;
- acquired by the city in 1456;
- written partly in native Umbrian script and partly in Latin letters;
- conventionally dated from the third to first centuries BCE.

Their two-script sections are crucial for checking sound values and the history of Umbrian. They remain at the Museo Civico, Palazzo dei Consoli, Gubbio. [MeTU museum record](https://www.umbriametu.it/museums/museo-civico-palazzo-dei-consoli-gubbio/the-iguvine-tables/?lang=en)

### 5.3 Oscan

The national or central Oscan alphabet was adapted from Etruscan, probably by the fifth century BCE. It added signs conventionally transcribed Í and Ú to distinguish vowels not covered adequately by the inherited inventory.

Major documents include:

- **Cippus Abellanus**, a treaty or boundary agreement between Abella and Nola concerning a sanctuary of Hercules, late third or second century BCE;
- **Tabula Bantina**, a bronze law text with Oscan and Latin faces, second or first century BCE;
- the **Tabula Osca/Agnone Tablet**, a religious dedication/list of cult places;
- coin legends and public inscriptions from Samnite and Campanian communities.

Oscan was also written in Greek script in the south and Latin script under Roman influence. “Oscan alphabet” therefore names one important regional medium, not every written form of the language.

### 5.4 South Picene and other Sabellic traditions

South Picene inscriptions, chiefly sixth–fourth centuries BCE, use a distinctive alphabet ultimately connected with the Etruscan-derived central Italic family. The language is Indo-European and broadly Sabellic. A special sibilant sign is encoded at U+1031F.

North Picene, represented especially by the Novilara stele, is not demonstrably the same language and remains poorly understood. Similar geography and names must not be turned into a false linguistic unity.

### 5.5 Venetic

Venetic writing is attested mainly from the sixth century BCE to the early Roman period around Este, Padua, the Piave and Cadore regions, and neighboring Slovenia.

**[R/D]** An early northern-derived phase was followed by a second phase whose alphabets reflect renewed south-Etruscan influence, perhaps from Caere or Veii.

Distinctive features include:

- multiple local alphabet varieties;
- inverted forms of lambda and upsilon;
- special dental-letter solutions;
- extensive syllabic punctuation;
- numerous votive writing tablets and styli dedicated to the goddess Reitia;
- coexistence with Latin script during Romanization.

The University of Florence project notes that syllabic punctuation was transferred with an Etruscan model and that Venetic and Latin scripts overlapped in the Roman period. [PRIN Italia Antica](https://www.prin-italia-antica.unifi.it/index.php?func=viewpage&module=CMpro&newlang=eng&pageid=219)

### 5.6 Lepontic/Lugano and Cisalpine Celtic

The Lepontic alphabet was used in the lakes district of northern Italy and southern Switzerland from approximately the sixth/fifth centuries BCE, with possible earlier examples. It wrote Lepontic, an early Celtic language, and later Cisalpine Gaulish.

The modern [Lexicon Leponticum](https://lexlep.univie.ac.at/wiki/North_Italic_Script) stresses that “North Italic” is a continuum of local alphabets rather than an easily bounded single system.

### 5.7 Raetic

Raetic inscriptions occur principally in Trentino, South Tyrol/Alto Adige, North Tyrol, and adjoining Alpine regions, approximately the sixth to first centuries BCE.

Two major traditions are:

- **Sanzeno**
- **Magrè**

**[R]** Linguistic comparison places Raetic with Etruscan and Lemnian in a Tyrsenian family, though the limited corpus leaves many words and grammatical details unclear.

The open [Thesaurus Inscriptionum Raeticarum](https://tir.univie.ac.at/wiki/Script) provides object-by-object records and emphasizes variation among northern scripts.

### 5.8 Camunic

Camunic writing is known largely from rock inscriptions in Valcamonica.

**[A]** The graph system is alphabetic and related to the North Italic environment.

**[D]** The language has not been convincingly identified or deciphered. Readings as Etruscan, Raetic, Celtic, or a separate local language have all been proposed for individual records. The corpus’s archaeological dating is often broad because rock surfaces are difficult to stratify.

### 5.9 Replacement by Latin

Roman political conquest did not instantly terminate local writing. Instead:

1. epichoric alphabets continued for religion, law, burial, coinage, and civic identity;
2. bilingual and biscriptal practice increased;
3. Latin script became useful for dealings with Roman institutions;
4. local languages shifted to Latin letters;
5. Latin replaced both language and script.

The timing differed by region. Umbrian, Oscan, Venetic, and Etruscan were still written during the last centuries BCE; scattered later evidence does not demonstrate an uninterrupted living tradition beyond antiquity.

---

## 6. The letters as numbers and signs

### 6.1 Graphic numerals

Old Italic Unicode encodes:

| Sign | Value | Comment |
|:---:|---:|---|
| 𐌠 | 1 | tally-like stroke |
| 𐌡 | 5 | additive/subtractive use varies |
| 𐌢 | 10 | cross or angle-derived forms occur |
| 𐌣 | 50 | later forms overlap the ancestry of Roman L |

**[R/D]** Etruscan numerical notation is structurally related to Roman additive and subtractive numerals, but the exact direction of every borrowing and the derivation of individual shapes remain debated. Unicode warns that the numerical corpus is poorly attested and that additional proposed signs remain unencoded.

These were not Greek-style alphabetic numerals in which each letter had a place value. No Etruscan isopsephy or gematria system is documented.

### 6.2 Number words

Secure or widely accepted values include:

| Value | Etruscan word | Status |
|---:|---|---|
| 1 | θu | broadly accepted |
| 2 | zal | broadly accepted |
| 3 | ci | broadly accepted |
| 4 | śa | supported by recent dice analysis, formerly disputed |
| 5 | maχ | broadly accepted |
| 6 | huθ | supported by recent dice analysis, formerly disputed |
| 10 | śar | broadly accepted |
| 20 | zaθrum | broadly accepted |
| 30 | cealχ | broadly accepted |

The famous word-dice from Tuscania, now in the Cabinet des Médailles in Paris, carry *maχ, θu, zal, huθ, ci,* and *śa*. For generations scholars disagreed over whether *huθ* and *śa* meant four or six.

**[R/D]** Artioli, Nociti, and Angelini compared the word-dice with the changing arrangement of pip dice and concluded that **śa = 4** and **huθ = 6**. Their statistical/archaeometric case is strong but should be distinguished from direct bilingual proof. [“Gambling with Etruscan Dice,” *Archaeometry* 53.5 (2011)](https://onlinelibrary.wiley.com/doi/10.1111/j.1475-4754.2011.00596.x)

### 6.3 Religious signs and divination

Etruscan writing is deeply represented in religious contexts:

- calendrical ritual in the *Liber Linteus* and *Tabula Capuana*;
- divine names on the Piacenza liver;
- dedicatory texts in sanctuaries;
- labels on mirrors showing mythological figures;
- boundary and funerary formulae with religious implications.

**Absence of evidence:** there is no surviving Etruscan equivalent of Hebrew gematria, Greek isopsephy, *Sefer Yetzirah*, Arabic *ʿilm al-ḥurūf*, rune poems, or a letter-by-letter mystical treatise.

Ancient Roman authors describe an extensive **Etrusca disciplina**—books on lightning, entrails, ritual, and fate. That is evidence for written divinatory learning, not for alphabet mysticism.

### 6.4 Individual signs used nonphonographically

**[A/R]** Isolated letters on pottery, building elements, lots, and workshops can be:

- ownership or maker marks;
- assembly marks;
- counting marks;
- abbreviations;
- alphabet exercises;
- possibly lots or ritual labels.

Context must decide. Calling every isolated character “magical” is not warranted.

---

## 7. People

### Ancient transmitters and writers

- **Unknown Euboean and Etruscan teachers, c. 750–700 BCE — [R]:** actual agents of borrowing; no names survive.
- **Thefarie Velianas, c. 510 BCE — [A]:** ruler of Caere named on the Pyrgi tablets.
- **Etruscan scribes and ritual specialists — [A/T]:** anonymous makers of the *Liber Linteus*, Piacenza liver, calendars, tomb texts, dedications, and legal tablets.
- **Spurinna family and other Etruscan aristocrats — [A/T]:** known from inscriptions and later Roman tradition; not alphabet inventors.
- **Spurius Carvilius Ruga, third century BCE — [Tr/D]:** Roman grammatical tradition associates him with introducing G into Latin; the attribution is late and not proven by a contemporary object.

### Ancient traditions and legends

- **Cadmus — [L]:** Greek tradition credited the Phoenician prince with bringing letters to Greece. Herodotus 5.58–61 calls archaic letters “Phoenician” and associates them with Cadmeans. This is relevant to the alphabet’s Greek self-understanding, not evidence that Cadmus visited Etruria.
- **Palamedes and Simonides — [Tr/L]:** Greek sources assign additions to the alphabet to culture heroes or poets. These stories rationalize regional letter inventories.
- **Thoth/Hermes — [L]:** Egyptian/Greco-Roman inventor-of-writing traditions; no demonstrated role in the historical Etruscan borrowing.
- **Tages — [L/Tr]:** childlike prophetic figure said to have sprung from a ploughed furrow and taught Etruscan divination.
- **Tarchon — [Tr/L]:** culture founder and transmitter of Etruscan sacred learning.
- **Odin’s acquisition of runes — [L]:** *Hávamál* 138–39 describes Odin hanging wounded on the wind-swept tree and taking up runes. It is a Norse myth of sacred knowledge, not historical evidence for where the runic letter forms originated.

### Modern scholars

- **Annius of Viterbo (Giovanni Nanni), c. 1432–1502 — [M/forgery]:** promoted a Noahic/Etruscan antiquity through forged authorities and artefacts.
- **Luigi Antonio Lanzi, 1732–1810 — [R]:** placed Etruscan epigraphy on a comparative footing; *Saggio di lingua etrusca* (1789).
- **Wilhelm Deecke, 1831–1897 — [R]:** major nineteenth-century comparative work on Etruscan and Italic inscriptions.
- **Carl Pauli, 1839–1901 — [R]:** Etruscan and North Italic epigraphy.
- **Jakob Krall, 1857–1905 — [R]:** identified and published the *Liber Linteus* as Etruscan.
- **Massimo Pallottino, 1909–1995 — [R]:** established modern Etruscology as an archaeological-historical discipline; directed the Pyrgi excavation.
- **Giulio and Larissa Bonfante — [R]:** influential synthesis of Etruscan language and alphabet.
- **Helmut Rix, 1926–2004 — [R]:** Etruscan grammar, Tyrsenian comparison, and *Etruskische Texte*.
- **Michel Lejeune, 1907–2000 — [R]:** Italic, Venetic, and alphabetic transmission.
- **Aldo Luigi Prosdocimi, 1941–2016 — [R]:** Venetic, Umbrian, writing instruction, and syllabic punctuation.
- **Rex Wallace — [R]:** modern grammatical and epigraphic synthesis.
- **L. Bouke van der Meer — [R]:** extended analysis of the *Liber Linteus*.
- **Corinna Salomon — [R]:** digital corpora and palaeography of Lepontic, Raetic, and North Italic writing.
- **Michael Everson and John Jenkins — [M/technical]:** principal figures in the Unicode encoding work for Old Italic.

No historical Etruscan calligrapher or alphabet inventor is named in surviving evidence.

---

## 8. Culture and social use

### 8.1 Education and abecedaria

The Marsiliana wax tablet, alphabet vessels, model rows, pseudo-writing, and Venetic votive tablets establish formal or semi-formal teaching.

**[R]** Alphabet rows served several possible functions:

- memorization;
- scribal practice;
- elite display;
- dedication of literacy to a deity;
- apotropaic use.

An abecedarium is evidence that someone represented alphabetic order; it does not by itself prove a school building or a professional scribal class.

### 8.2 Law and public administration

Surviving examples include:

- *Tabula Cortonensis*: land transaction;
- *Cippus Perusinus*: boundary/legal settlement;
- *Cippus Abellanus*: sanctuary boundary/treaty;
- *Tabula Bantina*: Oscan public law;
- civic magistracies and ethnic names on inscriptions and coins.

Writing authenticated claims, memorialized agreements, fixed sacred boundaries, and displayed public authority.

### 8.3 Religion

The richest extended Etruscan texts are religious:

- *Liber Linteus*: ritual calendar or liturgy;
- *Tabula Capuana*: ritual calendar;
- Piacenza liver: divine map for extispicy;
- Pyrgi tablets: royal temple dedication;
- Reitia tablets: Venetic votive literacy;
- Iguvine Tables: Umbrian priestly ritual.

This distribution reflects both ancient practice and preservation bias. Linen and wooden secular books rarely survive.

### 8.4 Tombs

Most Etruscan inscriptions are funerary. They record:

- personal name;
- parents and descent;
- clan;
- age;
- offices;
- ownership of tomb or sarcophagus;
- construction or dedication.

Because names and kinship formulae recur, funerary epigraphy is the firmest part of the lexicon but gives a narrow sample of the spoken language.

### 8.5 Pottery, tools, and trade

Inscribed ceramics carry:

- owners’ names;
- makers’ names;
- gifts;
- dedications;
- alphabet exercises;
- capacity or commercial marks.

Greek loan-names and Etruscan inscriptions on imported shapes reveal intense intercultural exchange rather than two isolated literate worlds.

### 8.6 Coins and seals

Etruscan and other Italic coinages employ abbreviated city names, ethnic designations, magistrates, and denominations. Restricted space encouraged letter variants and abbreviations. Seals and gems similarly combine image, name, and ownership.

### 8.7 Myth in visual art

Engraved mirrors label Greek heroes and gods in adapted Etruscan names. The Vatican mirror of Calchas labels the winged haruspex **Kalkhas**, joining Greek myth with an Etruscan divinatory image. [Vatican Museums](https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/museo-gregoriano-etrusco/sala-iii--bronzi/specchio-inciso-con-calcante.html)

### 8.8 Literature and lost books

**[T]** Roman authors refer to:

- *libri haruspicini*;
- *libri fulgurales*;
- *libri rituales*;
- Etruscan histories;
- ritual and prophetic books.

Emperor Claudius reportedly wrote a twenty-book history of the Etruscans in Greek; it is lost.

**Absence of evidence:** no Etruscan epic, lyric poem, drama, alphabet poem, or complete secular prose work survives. That is not evidence that none existed. The *Liber Linteus* shows that books on perishable material did exist.

---

## 9. Digital encoding

### 9.1 Unicode history

Old Italic entered Unicode in version 3.1 in 2001. The block occupies U+10300–U+1032F in Plane 1.

Early proposals debated whether Etruscan, Oscan, Umbrian, and related scripts should be:

- separately encoded;
- unified as one script on the basis of shared historical identity and character correspondence;
- unified with archaic Greek;
- represented as font variants.

The adopted solution was a distinct **Old Italic** block with regional glyph variation handled substantially by fonts.

An archived 1997 proposal even considered Greek/Etruscan/Gothic unification, illustrating how unsettled the character/glyph boundary was. [Unicode mailing-list archive](https://www.unicode.org/mail-arch/unicode-ml/Archives-Old/UML011/0025.html)

### 9.2 Advantages and problems of unification

**Advantages**

- straightforward transliteration;
- shared code points for historically corresponding letters;
- easier cross-corpus searching;
- avoidance of many near-duplicate blocks.

**Problems**

- local scripts had genuinely different inventories and values;
- one abstract character may need markedly different regional shapes;
- scholars may need palaeographic distinctions that plain text cannot encode;
- Unicode names can look more phonologically certain than the evidence permits;
- direction varied historically.

Later additions supplied special Umbrian, Oscan, South Picene, and North Italic signs. A substantial technical survey is preserved in the [2011 Old Italic proposal](https://unicode.org/L2/L2011/11146-old-italic.pdf) and its [2012 revision](https://www.unicode.org/L2/L2012/12386-old-italic.pdf).

### 9.3 Present-day use

**[M]** Old Italic is used today in:

- digital scholarly editions;
- museum labels;
- teaching;
- Unicode demonstrations;
- historical fonts;
- tattoos, games, fantasy, and modern “Etruscan” designs.

There is no continuous native scribal community. Modern neo-Etruscan language projects, magical alphabets, and decorative fonts are revivals or inventions and should not be cited as ancient practice.

---

## 10. Controversies and disputes

### 10.1 Exactly when and where was the alphabet borrowed?

**Consensus reconstruction:** late eighth/early seventh century BCE through the Euboean colonial world of Pithekoussai and Cumae.

**Evidence:**

- Euboean letter inventory and supplementary values;
- Greek settlement chronology;
- Bay of Naples inscriptions around 725 BCE;
- Etruscan abecedaria around 700 BCE;
- archaeological exchange.

**Competing refinements:**

- Pithekoussai rather than Cumae;
- direct adoption in an Etruscan port;
- more than one transfer;
- participation by Phoenician intermediaries;
- a model already circulating among mixed communities.

**Finding:** the Euboean relationship is very strong; the named teacher, exact workshop, and single-place narrative are unreconstructable.

### 10.2 Were Romans taught directly by Greeks or through Etruscans?

**Etruscan-intermediary case:**

- early Latin C for /k/ and /g/ resembles an alphabet transmitted through a language lacking the contrast;
- K/Q distributions;
- geographical relations with Caere and Veii;
- likely Etruscan structure of Latin letter names.

**Direct-Greek or mixed-contact case:**

- Greek writing was present in Latium;
- Romans retained signs Etruscan did not use;
- no surviving document records the borrowing event;
- alphabet transmission can involve repeated contact.

**Assessment:** mediation through a south-Etruscan model is the prevailing reconstruction, but continued Greek input is probable and “pure descent” is too rigid.

### 10.3 Why copy B, D, and O if Etruscan did not use them?

The Marsiliana and related abecedaria preserve a pedagogical alphabet older than its functional reduction.

This is positive evidence that alphabet order was learned as a cultural object. It is not proof that the signs had secret values, nor that Etruscan possessed /b d o/ at that date.

### 10.4 Is Etruscan “undeciphered”?

Two usages collide:

- **Strict epigraphic usage:** the script is deciphered; values are known.
- **Popular usage:** the language is not fully translated, so it is called undeciphered.

Known elements include names, kinship terms, case suffixes, numerals, offices, verbs, ritual expressions, and substantial grammar. Unknown vocabulary and difficult long passages remain abundant.

The Pyrgi documents are parallel rather than exact translations. No long Etruscan–Greek or Etruscan–Latin bilingual has supplied a comprehensive lexicon.

### 10.5 Is Etruscan an isolate?

Older descriptions call it an isolate.

**[R]** Most recent specialists recognize a **Tyrsenian** family containing Etruscan, Raetic, and Lemnian, on the basis of shared morphological and lexical features.

**[D]** The family’s deeper affiliations remain uncertain. Proposed connections with Indo-European, Anatolian, Semitic, Kartvelian, Hungarian, Turkic, Basque, and numerous other languages range from serious but minority hypotheses to pseudolinguistic comparison.

Superficial look-alikes without regular sound correspondences, morphology, and chronology do not demonstrate kinship.

### 10.6 Etruscan ethnic origins versus script origins

Ancient accounts disagree:

- **[T/Tr] Herodotus 1.94:** migration from Lydia under Tyrrhenus.
- **[T/Tr] Dionysius of Halicarnassus 1.25–30:** indigenous people unlike the Lydians.
- **[T/Tr] Hellanicus tradition:** association with Pelasgians.

These concern the people, not directly the alphabet. Even an indigenous population could adopt Greek writing; even a migrated population would not thereby make the alphabet Lydian.

Modern archaeology generally sees Etruscan civilization developing from the preceding Villanovan culture in Italy, while ancient-DNA studies address population history rather than letter transmission. The written evidence still points to Euboean Greek regardless of the ethnic-origin debate.

### 10.7 Did North Italic writing create the runes?

#### North Italic/Raetic case

- several rune shapes resemble Raetic, Venetic, Lepontic, or Camunic forms;
- those alphabets were available near trans-Alpine routes;
- the Negau B helmet may preserve a Germanic name in a North Italic alphabet;
- straight strokes suit carving in both traditions;
- Unicode once summarized an Alpine source more confidently than current scholarship does.

#### Latin case

- intensive Roman–Germanic contact around the first centuries BCE/CE;
- early runes appear in a Roman Iron Age material world;
- most rune forms have plausible Latin capital antecedents;
- no single North Italic alphabet supplies the full rune row;
- the futhark order is radically different.

#### Greek and mixed models

Greek, especially northern/Black Sea or cursive forms, has also been proposed. Eclectic models derive different runes from different neighboring scripts.

#### Negative evidence

- no transitional alphabet survives;
- the earliest securely runic inscriptions are centuries later than most North Italic corpora;
- similarity between angular signs is not by itself genealogy;
- runic order and rune names are independent innovations;
- the Negau inscription is North Italic, not itself runic.

**Conclusion:** Mediterranean alphabetic ancestry is nearly certain; whether the immediate model was Latin, a North Italic alphabet, or a mixed contact repertoire remains disputed. The University of Vienna thesis project explicitly re-examines the Raetic case from the complete corpus. [“Raetic and runes”](https://utheses.univie.ac.at/detail/48069)

### 10.8 Negau Helmet B

**[A]** One helmet from the Negau/Negova hoard carries a right-to-left North Italic inscription commonly segmented *harigasti teiva…*.

**[D]**

- the script is variously classified as Venetic, Raetic, or another North Italic variety;
- *Harigastiz* may be a Germanic personal name;
- *teiva* has been interpreted as “god,” a personal element, or something else;
- the date of manufacture, inscription, and deposition need not be identical.

It is evidence for Alpine cultural contact. It is not a securely dated “first rune.”

### 10.9 The Praeneste fibula

This is Latin rather than Etruscan but central to the Old Italic chronology.

**Claimed artefact:** gold fibula with *MANIOS MED FHEFHAKED NVMASIOI*, “Manius made me for Numerius,” conventionally seventh century BCE.

**Forgery case:**

- Wolfgang Helbig’s find story was indirect;
- no controlled provenance;
- Margherita Guarducci argued that the handwriting and manufacture indicated a nineteenth-century fabrication.

**Authenticity case:**

- later finds confirmed linguistic forms once thought suspicious;
- technical examinations found ancient manufacture and plausible inscription processes;
- the name *Numasiana* appears on another archaic object;
- Markus Hartmann and others restored it to the early Latin corpus.

**Finding:** modern scholarship has shifted substantially toward authenticity, but its provenance remains defective. A useful historiographic review is [“The Consequences of Truth”](https://archaeologybulletin.org/articles/10.5334/bha.22113).

### 10.10 Tabula Cortonensis provenance

The tablet’s delayed disclosure and missing eighth fragment encouraged forgery rumors. No controlled excavation record can now be produced. However, the accepted linguistic, palaeographic, metallurgical, and physical evidence favors antiquity.

The correct label is:

- artefact accepted as ancient;
- original find circumstances uncertain;
- historical reconstruction of its precise depositional context impossible.

### 10.11 Renaissance and modern forgeries

#### Annius of Viterbo

**[M/forgery]** His 1498 pseudo-ancient texts made Noah, Janus, and Etruscan civilization part of a universal sacred history centered on Viterbo. Jean Lemaire de Belges and other sixteenth-century writers spread portions of this constructed past. [Rothstein, “Reception of Annius’s Forgeries”](https://www.journals.uchicago.edu/doi/10.1086/698141)

#### Inghirami’s *Scarith*

**[M/forgery]** Curzio Inghirami announced wax capsules containing purported Etruscan prophetic records in the seventeenth century. Anachronistic materials, language, and circumstances exposed them as fabrications.

#### British Museum “Cerveteri sarcophagus”

**[M/forgery]** Withdrawn after stylistic and technical examination; the inscription had reportedly been copied from a genuine gold brooch. Contemporary discussion appears in [Nature, “Etruscan Forgery in the British Museum”](https://www.nature.com/articles/136752b0) and a conservation summary from [ICCROM](https://www.iccrom.org/resources/resources-of-the-month/united-kingdom-etruscan-fake).

#### Modern “complete translations”

Claims that Etruscan is wholly Turkish, Hungarian, Albanian, Hebrew, Slavic, Tamil, or another favored modern language commonly:

- assign new values to already deciphered letters;
- compare isolated similar-looking words;
- ignore inflection and chronology;
- produce translations that cannot predict unread texts.

They are modern reception history, not an alternative decipherment with comparable evidentiary support.

### 10.12 Numerical controversy: four and six

Older scholarship divided between:

- *huθ* = 4, *śa* = 6;
- *śa* = 4, *huθ* = 6.

The 2011 dice study strongly supports the second arrangement through combinatorial comparison and dating. Because this is inference from dice conventions rather than a bilingual equation, “resolved by strong converging evidence” is preferable to “directly attested.”

### 10.13 Unicode “unification”

Some users object that Etruscan, Oscan, Umbrian, Venetic, and the Alpine scripts are too different to share code points. Others regard their differences as palaeographic/font-level variants within a historical script family.

The dispute is partly conceptual:

- epigraphy needs exact glyph shape;
- plain-text encoding seeks abstract characters;
- Unicode does not attempt to encode every palaeographic allograph.

High-fidelity editions therefore need photographs, drawings, or specialized markup in addition to Unicode text.

---

## 11. Open questions

1. Where precisely did the first Etruscan acquisition of the Euboean alphabet occur?
2. Was there one borrowing event or several overlapping teaching traditions?
3. Who taught the alphabet—Greek settlers, mixed families, merchants, craftspeople, or Etruscan specialists?
4. How early are the first non-abecedarial Etruscan texts when archaeological dating margins are fully accounted for?
5. What exact phonetic values did the two sibilants have in each region?
6. How did aspiration and stop articulation change between archaic and late Etruscan?
7. What were the native letter names?
8. Does *abat…* genuinely preserve an Etruscan word for “alphabet”?
9. How standardized were schools at Caere, Veii, Tarquinia, Vulci, and northern centers?
10. Which unattested intermediary traditions connect central Etruscan with the earliest northern alphabets?
11. Is every proposed “North Italic” inscription assigned to the correct language?
12. What language or languages underlie the Camunic corpus?
13. How much of the *Liber Linteus* can be securely translated rather than structurally parsed?
14. Where was the linen book written, and how did it reach Egypt?
15. How closely do the three Pyrgi texts correspond at the clause level?
16. Can further dice or accounting finds confirm the values of Etruscan number words?
17. What was the full repertoire of Etruscan graphic numerals?
18. Did Latin numeral notation descend directly from Etruscan forms, or from a wider central-Italic tally tradition?
19. Which script was the immediate model for the Elder Futhark?
20. Can new imaging recover erased or illegible texts on stone, bronze, pottery, or linen?
21. How representative is a corpus dominated by graves and dedications of the spoken language?
22. How much Etruscan secular literature was lost because its normal media were wood, wax, and linen?
23. When and where was Etruscan last used as a community language rather than antiquarian or priestly knowledge?
24. Can Unicode’s unified model adequately support rigorous regional palaeography, or will variation selectors, markup, or separate scholarly fonts remain necessary?

---

## 12. Sources and editions consulted

### Foundational books and corpora

- Peter T. Daniels and William Bright, eds., *The World’s Writing Systems*. New York/Oxford: Oxford University Press, 1996.
- David Diringer, *The Alphabet: A Key to the History of Mankind*, 3rd ed. London: Hutchinson, 1968.
- Lilian H. Jeffery, *The Local Scripts of Archaic Greece*, rev. ed. with supplement by A. W. Johnston. Oxford: Clarendon Press, 1990.
- Joseph Naveh, *Early History of the Alphabet: An Introduction to West Semitic Epigraphy and Palaeography*, 2nd ed. Jerusalem: Magnes, 1987.
- Benjamin Sass, *The Genesis of the Alphabet and Its Development in the Second Millennium B.C.* Wiesbaden: Harrassowitz, 1988.
- Barry B. Powell, *Homer and the Origin of the Greek Alphabet*. Cambridge: Cambridge University Press, 1991.
- Giuliano Bonfante and Larissa Bonfante, *The Etruscan Language: An Introduction*, 2nd ed. Manchester: Manchester University Press, 2002.
- Rex E. Wallace, *Zikh Rasna: A Manual of the Etruscan Language and Inscriptions*. Ann Arbor/New York: Beech Stave Press, 2008.
- Helmut Rix et al., *Etruskische Texte*, 2 vols. Tübingen: Gunter Narr, 1991.
- Massimo Pallottino, *Testimonia Linguae Etruscae*, 2nd ed. Florence: La Nuova Italia, 1968.
- *Corpus Inscriptionum Etruscarum*. Leipzig/Rome, 1893–present.
- L. Bouke van der Meer, *Liber Linteus Zagrabiensis: The Linen Book of Zagreb*. Louvain: Peeters, 2007.
- R. I. Page, *An Introduction to English Runes*, 2nd ed. Woodbridge: Boydell, 1999.
- Tineke Looijenga, *Texts and Contexts of the Oldest Runic Inscriptions*. Leiden: Brill, 2003.

### Digital standards and proposals

- Unicode Standard 16.0, §8.6, Old Italic:  
  https://www.unicode.org/versions/Unicode16.0.0/UnicodeStandard-16.0.pdf
- Unicode Old Italic names list:  
  https://www.unicode.org/charts/nameslist/n_10300.html
- Unicode Old Italic block chart/index:  
  https://www.unicode.org/charts/nameslist/c_10300.html
- Unicode 3.1 additions, UAX #27:  
  https://unicode.org/reports/tr27/tr27-4.html
- Unicode exploratory proposals, UTR #3:  
  https://www.unicode.org/reports/tr3-2/
- Old Italic proposal, L2/11-146:  
  https://unicode.org/L2/L2011/11146-old-italic.pdf
- Revised Old Italic proposal, L2/12-386:  
  https://www.unicode.org/L2/L2012/12386-old-italic.pdf
- Archived Greek/Etruscan/Gothic unification discussion:  
  https://www.unicode.org/mail-arch/unicode-ml/Archives-Old/UML011/0025.html

### Museums, objects, and institutional records

- Museo Nazionale Etrusco di Villa Giulia, Pyrgi tablets:  
  https://www.museoetru.it/works/lamine-doro-da-pyrgi
- Archaeological Museum in Zagreb, museum and collection:  
  https://amz.hr/en/museum/about-the-museum/
- Archaeological Museum in Zagreb, Etruscan Room:  
  https://amz.hr/hr/virtualni-muzej/vodici-kroz-stalni-postav/vodic-kroz-stalni-postav-egipatske-zbirke-arheoloskog-muzeja-u-zagrebu/etruscanska-soba/
- Archaeological Museum in Zagreb, *Liber i Mumija*:  
  https://amz.hr/hr/muzej/nakladnistvo/opera-varia/liber-i-mumija/
- Croatian Encyclopedia, *Liber Linteus Zagrabiensis*:  
  https://enciklopedija.hr/clanak/liber-linteus-zagrabiensis
- Italian Ministry of Culture, *Liber Linteus*:  
  https://cultura.gov.it/evento/iorestoacasa-etru-per-la-giornata-mondiale-del-libro-il-liber-linteus
- Staatliche Museen zu Berlin, *Tabula Capuana*, inv. 30892:  
  https://artsandculture.google.com/asset/tabula-capuana-unknown/kAHMSLRI1HBeiw?hl=en
- Staatliche Museen zu Berlin, representation of a *liber linteus*:  
  https://visit.smb.museum/object/obj-728078
- MAEC Cortona, *Tabula Cortonensis*:  
  https://cortonamaec.org/en/museum-masterpieces/tabula-cortonensis/
- Museo Civico di Palazzo Farnese/Visit Piacenza, bronze liver:  
  https://visitpiacenza.it/en/art-and-culture/etruscan-liver/
- Fondazione Luigi Rovati, Vicchio/Poggio Colla stele:  
  https://www.fondazioneluigirovati.org/en/events-exhibitions/exhibits/the-vicchio-stele/
- MeTU, Iguvine Tables:  
  https://www.umbriametu.it/museums/museo-civico-palazzo-dei-consoli-gubbio/the-iguvine-tables/?lang=en
- Vatican Museums, mirror of Calchas:  
  https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/museo-gregoriano-etrusco/sala-iii--bronzi/specchio-inciso-con-calcante.html
- Metropolitan Museum, *Etruscan Art in the Metropolitan Museum*:  
  https://resources.metmuseum.org/resources/metpublications/pdf/Etruscan_Art_in_The_Metropolitan_Museum.pdf

### Specialist digital corpora and writing-system resources

- Lexicon Leponticum, North Italic script:  
  https://lexlep.univie.ac.at/wiki/North_Italic_Script
- Thesaurus Inscriptionum Raeticarum, script:  
  https://tir.univie.ac.at/wiki/Script
- Thesaurus Inscriptionum Raeticarum, alphabet classifications:  
  https://tir.univie.ac.at/wiki/Property%3Aalphabet
- Mnamon, Venetic writing and syllabic punctuation:  
  https://mnamon.sns.it/index.php?id=31&lang=en&page=Scrittura
- University of Florence PRIN, Venetic alphabet:  
  https://www.prin-italia-antica.unifi.it/index.php?func=viewpage&module=CMpro&newlang=eng&pageid=219
- TITUS, Osco-Umbrian corpus:  
  https://titus.uni-frankfurt.de/texte/etcs/ital/oskumb/oskumt.htm
- Corinna Salomon, North Italic sign–phoneme configuration:  
  https://lexlep.univie.ac.at/images/7/7e/Salomon_2021c.pdf
- Palaeohispanica, “The writing systems of Pre-Roman Italy”:  
  https://www.ifc-ojs.es/index.php/palaeohispanica/en/article/view/386

### Decipherment, language, and transmission

- Luigi Lanzi, *Saggio di lingua etrusca e di altre antiche d’Italia* (1789):  
  https://books.google.com/books?id=RBNKAAAAcAAJ
- Enrico Benelli, “The decipherment of the Etruscan alphabet,” INSCRIBE:  
  https://site.unibo.it/inscribe/en/conference-abstracts/enrico-benelli
- Silvia Ferrara, Barbara Montecchi, and Miguel Valério, “Writing from Invention to Decipherment”:  
  https://flore.unifi.it/retrieve/81004007-8df7-4755-b33f-86622e603a2d/Ferrara-Montecchi-Val%C3%A9rio_OUP_2024.pdf
- Treccani, history of Etruscology:  
  https://www.treccani.it/enciclopedia/l-etruscologia_%28Il-Mondo-dell%27Archeologia%29/
- B. L. Ullman, “The Etruscan Origin of the Roman Alphabet and the Names of the Letters,” *Classical Philology* 22.4 (1927):  
  https://www.journals.uchicago.edu/doi/10.1086/360949
- Richard Janko, “From Gabii and Gordion to Eretria and Methone”:  
  https://websites.umich.edu/~rjanko/Methone_final%20proofs.pdf
- “Italic Alphabets,” *Handbook of Comparative and Historical Indo-European Linguistics*:  
  https://ebrary.net/106824/economics/italic_alphabets
- M. I. Finley, “Etruscan Things,” *New York Review of Books* (1964):  
  https://www.nybooks.com/articles/1964/11/05/etruscan-things/
- Paolo Agostini and Adolfo Zavaroni, Pyrgi bilingual study:  
  https://hrcak.srce.hr/en/165455

### Numerals

- Gilberto Artioli, Valentina Nociti, and Ivana Angelini, “Gambling with Etruscan Dice: A Tale of Numbers and Letters,” *Archaeometry* 53.5 (2011):  
  https://onlinelibrary.wiley.com/doi/10.1111/j.1475-4754.2011.00596.x
- Jennifer Alvino, “La questione della resa grafica dei numerali etruschi”:  
  https://riviste.unimi.it/index.php/aristonothos/article/view/13725
- Ryuichi Hirata, “Parecchi problemi sui numerali etruschi”:  
  https://tohoku-gakuin.repo.nii.ac.jp/record/24510/files/20210326_hirataryuichi.pdf
- “The Origin of the Latin Numerals 1 to 1000,” *American Journal of Archaeology* 92.4:  
  https://www.journals.uchicago.edu/doi/pdfplus/10.2307/505248

### Runes and the North Italic question

- University of Vienna, “Raetic and runes—on the North Italic theory of the origin of the runic script”:  
  https://utheses.univie.ac.at/detail/48069
- University of Vienna, “Die Inschrift auf dem Helm B von Negau”:  
  https://ucrisportal.univie.ac.at/de/publications/die-inschrift-auf-dem-helm-b-von-negau-m%C3%B6glichkeiten-und-grenzen-/
- Gustav Must, “The Problem of the Inscription on Helmet B of Negau”:  
  https://www.jstor.org/stable/310966
- Tübingen dissertation, *Runic and Latin Written Culture*:  
  https://publikationen.uni-tuebingen.de/xmlui/bitstream/handle/10900/47095/pdf/SEBaur_Runic_and_Latin_Written_Culture_Co_Existence_and_Interaction_of_Two_Script_Cultures_in_the_Norwegian_Middle_Ages.pdf?isAllowed=y&sequence=1
- Oxford Academic, *Runes: A Concise History*:  
  https://academic.oup.com/book/61598

### Contested authenticity, forgery, and reception

- “The Consequences of Truth: The Praeneste Fibula,” *Bulletin of the History of Archaeology*:  
  https://archaeologybulletin.org/articles/10.5334/bha.22113
- Archaeology Magazine archive, “Who Made the Praeneste Fibula?”:  
  https://archive.archaeology.org/online/features/hoaxes/praeneste_fibula.html
- Federico Frasson et al., “I falsi epigrafici dell’Etruria”:  
  https://www.sco-pisa.it/index.php/sco/article/view/491
- Marian Rothstein, “The Reception of Annius of Viterbo’s Forgeries”:  
  https://www.journals.uchicago.edu/doi/abs/10.1086/698141
- “Renaissance Epigraphy and Its Legitimating Potential: Annius of Viterbo”:  
  https://onlinelibrary.wiley.com/doi/10.1111/j.2041-5370.2000.tb01965.x
- *Nature*, “Etruscan Forgery in the British Museum”:  
  https://www.nature.com/articles/136752b0
- ICCROM, “United Kingdom: An Etruscan fake”:  
  https://www.iccrom.org/resources/resources-of-the-month/united-kingdom-etruscan-fake
- George Dennis, *Cities and Cemeteries of Etruria*, discussion of Annius:  
  https://penelope.uchicago.edu/Thayer/E/Gazetteer/Places/Europe/Italy/_Periods/Roman/Archaic/Etruscan/_Texts/DENETR%2A/12.html
- “Etruscan history gets a rewrite,” *Times Higher Education*, on the Tabula Cortonensis controversy:  
  https://www.timeshighereducation.com/books/etruscan-history-gets-a-rewrite/156223.article

### Orientation-only index

- Omniglot, Etruscan alphabet and language—consulted only as a starting index, not as authority:  
  https://www.omniglot.com/writing/etruscan.htm
