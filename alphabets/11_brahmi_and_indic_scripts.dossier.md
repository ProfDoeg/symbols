# Brahmi and the Indic scripts (Devanagari and its sisters): Research Dossier

## Method and evidentiary labels

This dossier distinguishes:

- **[Artefact]** surviving, physically documented inscription, coin, seal, manuscript, or printed object.
- **[Text]** claim made in a surviving historical text; this proves that the claim circulated, not necessarily that it is historically true.
- **[Reconstruction]** modern scholarly inference from palaeography, linguistics, archaeology, or comparative history.
- **[Tradition]** community attribution or inherited account not independently established by contemporary evidence.
- **[Disputed]** claim seriously contested in specialist literature.
- **[Legend]** supernatural, etiological, or heroic narrative.
- **[Modern invention]** recent standardization, revival, identity claim, character encoding, or popular reinterpretation.

“Brahmi” below refers either narrowly to the early historical script conventionally called Brāhmī or, where specified, to the enormous Brahmic/Indic family descended from it.

---

## Basic identification

| Field | Identification |
|---|---|
| Name | **Brāhmī**; Sanskrit feminine *brāhmī*, conventionally “belonging to Brahmā/Brahman.” The name is ancient but is not known from Aśoka’s inscriptions themselves. |
| Type | **Abugida** or alphasyllabary: each consonant letter conventionally carries an inherent vowel, normally /a/; other vowels are supplied by dependent signs, and vowel absence is indicated contextually, by conjunct formation, or in later orthographies by virāma. |
| Basic inventory | Early Brahmi varies by place and period. Its reconstructed/classificatory Sanskritic inventory comprises independent vowels, corresponding dependent vowel signs, approximately 33 basic consonants, several regional consonants, nasal/aspiration signs, punctuation, and numerals. Unicode presently assigns **Brahmi U+11000–U+1107F**. |
| Direction | Predominantly **left-to-right**. A few early specimens run right-to-left or irregularly; the Yerragudi/Erragudi Minor Rock Edict includes reversed or alternating passages sometimes called boustrophedon. These exceptions do not establish a normal right-to-left stage. |
| Period | Secure monumental corpus: reign of Aśoka, third century BCE, especially c. 260–232 BCE. Earlier archaeological candidates may reach the fourth or fifth century BCE but remain disputed. “Brahmi” continued through changing regional forms into the early medieval period; its descendants remain in extensive daily use. |
| Region | Initially attested from Afghanistan/Pakistan and the Gangetic basin to Gujarat, Odisha, Karnataka, Andhra, Tamil Nadu, and Sri Lanka; descendants spread across South, Central, Southeast, and parts of East Asia. |
| Parent | **Uncertain.** A modified Semitic, especially Aramaic, stimulus is the leading comparative reconstruction in much Western scholarship; deliberate local invention informed by Indian phonetics is often incorporated into that model. Independent indigenous invention and Indus-script continuity have also been argued but are unproved. |
| Closest early neighbour | **Kharoṣṭhī**, used chiefly in the northwest, written right-to-left and much more transparently derived from Aramaic. It is not securely demonstrated to be Brahmi’s parent. |
| Principal daughters | Northern: Gupta, Siddham/Siddhamātṛkā, Śāradā, Nāgarī, Devanagari, Bengali-Assamese, Odia, Gujarati, Gurmukhi and related scripts, Newa, Tibetan. Southern: Tamil-Brahmi, Bhattiprolu and southern Brahmi traditions, Tamil, Grantha, Telugu, Kannada, Malayalam, Sinhala. Southeast Asian: Pyu, Mon-Burmese/Myanmar, Khmer, Cham, Kawi/Old Javanese, Javanese, Balinese, Thai, Lao and related scripts. The exact intermediate genealogy differs by scholar and region. |

The Unicode Standard calls Brahmi and the modern Indic systems abugidas and describes the canonical orthographic syllable as `(((C)C)C)V`. It also cautions that related scripts cannot be assumed to render identically merely because their character repertoires are homologous. [Unicode, Chapter 12](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-12/)

---

# The script in detail

## 1. Structural principle

**[Artefact + reconstruction]** Early Brahmi represents consonants as syllabic bases. Thus 𑀓 is conventionally transliterated *ka*, not bare *k*. A dependent sign changes the vowel:

- 𑀓 *ka*
- 𑀓𑀸 *kā*
- 𑀓𑀺 *ki*
- 𑀓𑀻 *kī*
- 𑀓𑀼 *ku*
- 𑀓𑀽 *kū*
- 𑀓𑁆 *k* in the modern Unicode representation using virāma

At the beginning of a syllable, or where no consonantal base is present, a vowel receives an independent letter: 𑀅 *a*, 𑀆 *ā*, 𑀇 *i*.

This is not an abjad: vowels are structurally represented. Nor is it a syllabary with an unrelated sign for every possible syllable. Its vowel signs systematically modify consonants, making “abugida” the most useful modern category. Peter T. Daniels coined that comparative term; Sanskrit grammatical terminology instead speaks of *akṣaras*, “imperishable units” and, contextually, letters or syllabic units.

### The “vowel question”

Brahmi does not reproduce the Greek innovation of treating consonant-letter forms as an autonomous set of full vowel letters. Its solution is different:

1. a consonant has a default/inherent vowel;
2. an independent vowel is used initially;
3. a *mātrā* replaces or modifies the inherent vowel;
4. consonant clusters suppress internal vowels;
5. later systems employ an explicit vowel-canceller, normally called *virāma*, *halant*, *hasant*, or—in Tamil—*puḷḷi*.

The system could have been inspired by Semitic consonantal writing while being radically redesigned through Indian phonological analysis. That redesign, rather than simple graphic copying, is central to the origin debate.

## 2. Core Brahmi sign table

The following is the normalized Unicode inventory, not a claim that every listed sign occurred in every Aśokan province or that Unicode’s glyphs reproduce one single historical hand. Sound values are conventional Sanskrit transliterations; Aśokan Prakrit lacked or merged several Sanskrit contrasts in particular dialects.

### Signs and independent vowels

| Unicode | Sign | Unicode name | Conventional value/function |
|---|---:|---|---|
| U+11000 | 𑀀 | Brahmi sign candrabindu | nasalization |
| U+11001 | 𑀁 | Brahmi sign anusvara | homorganic/final nasal |
| U+11002 | 𑀂 | Brahmi sign visarga | postvocalic aspiration /ḥ/ |
| U+11003 | 𑀃 | Brahmi sign jihvamuliya | special prevelar visarga |
| U+11004 | 𑀄 | Brahmi sign upadhmaniya | special prelabial visarga |
| U+11005 | 𑀅 | letter A | /a/ |
| U+11006 | 𑀆 | letter AA | /aː/ |
| U+11007 | 𑀇 | letter I | /i/ |
| U+11008 | 𑀈 | letter II | /iː/ |
| U+11009 | 𑀉 | letter U | /u/ |
| U+1100A | 𑀊 | letter UU | /uː/ |
| U+1100B | 𑀋 | vocalic R | /r̩/ |
| U+1100C | 𑀌 | vocalic RR | /r̩ː/ |
| U+1100D | 𑀍 | vocalic L | /l̩/ |
| U+1100E | 𑀎 | vocalic LL | /l̩ː/ |
| U+1100F | 𑀏 | letter E | /e/ |
| U+11010 | 𑀐 | letter AI | /ai/ |
| U+11011 | 𑀑 | letter O | /o/ |
| U+11012 | 𑀒 | letter AU | /au/ |

### Consonants in traditional *varṇamālā* order

| Class | Unicode signs | Names | Conventional values |
|---|---|---|---|
| Velars | 𑀓 𑀔 𑀕 𑀖 𑀗 | ka kha ga gha ṅa | /k kʰ g gʱ ŋ/ |
| Palatals | 𑀘 𑀙 𑀚 𑀛 𑀜 | ca cha ja jha ña | /t͡ɕ~c, aspirate, voiced series, ɲ/ |
| Retroflexes | 𑀝 𑀞 𑀟 𑀠 𑀡 | ṭa ṭha ḍa ḍha ṇa | /ʈ ʈʰ ɖ ɖʱ ɳ/ |
| Dentals | 𑀢 𑀣 𑀤 𑀥 𑀦 | ta tha da dha na | /t̪ t̪ʰ d̪ d̪ʱ n̪/ |
| Labials | 𑀧 𑀨 𑀩 𑀪 𑀫 | pa pha ba bha ma | /p pʰ b bʱ m/ |
| Semivowels/liquids | 𑀬 𑀭 𑀮 𑀯 | ya ra la va | /j r l ʋ~v/ |
| Sibilants | 𑀰 𑀱 𑀲 | śa ṣa sa | /ɕ~ʃ ʂ s/ |
| Laryngeal | 𑀳 | ha | /ɦ~h/ |
| Regional additions | 𑀴 𑀵 𑀶 | ḷa, Old Tamil ḻa, Old Tamil ṟa | retroflex/lateral and Tamil sounds |

Code points run from U+11013 KA through U+11036 OLD TAMIL RRA. The Unicode proposal explicitly added Tamil and Bhattiprolu requirements rather than treating Aśokan northern Brahmi as the whole historical repertoire. [Unicode Brahmi chart](https://www.unicode.org/charts/PDF/U11000.pdf); [Everson, Glass and Baums proposal](https://www.unicode.org/L2/L2008/08277r-n3490r-brahmi.pdf)

### Dependent vowels and modifiers

| Function | Representative Unicode signs |
|---|---|
| ā | 𑀸 |
| i, ī | 𑀺, 𑀻 |
| u, ū | 𑀼, 𑀽 |
| vocalic r/rr/l/ll | 𑀾 𑀿 𑁀 𑁁 |
| e, ai, o, au | 𑁂 𑁃 𑁄 𑁅 |
| virāma | 𑁆 |
| anusvāra/visarga | 𑀁, 𑀂 |

**[Qualification]** Unicode character names are stable technical labels, not necessarily the names used by an Aśokan scribe. Likewise, a Unicode glyph is a normalized representative, not a facsimile of every palaeographic form.

## 3. Order and phonetic science

**[Documented intellectual tradition + reconstruction]** The *varṇamālā*, “garland of sounds,” is ordered articulatorily:

1. vowels;
2. velars at the back of the mouth;
3. palatals;
4. retroflexes;
5. dentals;
6. labials;
7. semivowels;
8. sibilants;
9. *h*.

Within each stop row come voiceless unaspirated, voiceless aspirated, voiced unaspirated, voiced aspirated, and nasal.

Pāṇini, probably fourth century BCE within a broad disputed range, did not write an alphabet textbook: his *Aṣṭādhyāyī* uses the fourteen Māheśvara/Śiva Sūtras as a compressed grammatical index. Nevertheless, Indian phonetic analysis plainly predates the mature manuscript tradition and provides the conceptual apparatus behind Brahmi’s expanded distinctions.

It is therefore safer to say:

- **[Documented]** the order corresponds to ancient Indian phonological science.
- **[Reconstruction]** grammarians or persons trained in that science designed or regularized Brahmi.
- **[Not documented]** Pāṇini personally invented Brahmi.

The letters’ ordinary Sanskrit names—*a, ā, ka, kha*, and so forth—are essentially their sound values, normally pronounced with a support vowel. Unlike Phoenician *ʾālep* “ox” and *bēt* “house,” Brahmi has no demonstrated set of pictorial, meaningful, acrophonic letter names. Proposed “picture meanings” for Brahmi letters are modern speculation.

## 4. Conjuncts, ligatures, and orthographic syllables

**[Artefact]** Consonant clusters could be represented by joined, stacked, reduced, or specially shaped components. Practices varied historically.

Modern Devanagari illustrates the mature mechanism:

- क् + त → क्त *kta*
- त् + र → त्र *tra*
- ज् + ञ → ज्ञ *jña*
- क् + ष → क्ष *kṣa*

The last two are often taught as if they were independent alphabet letters; structurally they are conjuncts. Devanagari *r* has several contextual forms: repha above a following consonant, a subjoined form, and regional/type-specific ligatures.

In Brahmic computing, encoded characters are stored in logical order. A shaping engine chooses the visible matra positions, half-forms, repha, stacking, and ligatures. Consequently a displayed “letter” may correspond to several code points, while a single code point can take multiple glyph forms.

## 5. Direction and exceptional writing

The normal direction of Aśokan Brahmi and virtually all major daughters is left-to-right.

**[Artefact]** Exceptional reversed legends occur, including on coins. The Yerragudi edict contains reversed or alternating lines/passages. Earlier writers used these anomalies to support a transition from Semitic right-to-left writing.

**[Disputed inference]** A few reversals do not necessarily preserve an ancestral direction: coin dies readily produce mirror writing, and an engraver unfamiliar with a monumental layout can reverse a model. Ahmad Hasan Dani and others warned against building a genetic theory on such irregularities.

Brahmi never developed a routine right-to-left tradition comparable to Kharoṣṭhī.

## 6. Punctuation, spacing, case, and scribal distinctions

- Early inscriptions often divide clauses by spaces, dots, vertical strokes, or decorative marks, inconsistently.
- The single **danda** `।` and double danda `॥` became characteristic terminators for verse or larger divisions.
- Word spacing varies greatly by date and medium.
- An **avagraha** marks elision in Sanskrit orthography.
- Anusvāra, candrabindu, visarga, Vedic accent marks, nukta, and script-specific signs expanded the diacritic repertory.
- Modern Hindi also freely uses comma, full stop, colon, question mark, quotation marks, and other European punctuation; the danda is now strongest in traditional, poetic, and Sanskrit contexts. [Unicode, Chapter 12](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-12/)
- There is no Indic equivalent of historically distinct Roman capitals and minuscules. Monumental versus documentary hands and formal versus cursive letterforms exist, but they are not a casing system.
- Unicode therefore assigns Brahmi and Indic letters no upper-/lower-case pairs.

The horizontal headline or *śirorekhā* characteristic of Nāgarī/Devanagari developed historically from pen forms; it is not present as a continuous line in early Brahmi. Gujarati later discarded the full headline in the mercantile and documentary styles ancestral to its modern print form.

## 7. Numerals

Brahmi letters were not ordinarily assigned numbers in alphabetic order like Greek isopsephy or Hebrew gematria.

### Early additive-multiplicative numerals

**[Artefact]** Brahmi possesses separate signs for 1–9, the tens 10–90, 100, and 1000. Values normally descend and add; a multiplier can combine with 100 or 1000.

| Sign | Value | Unicode |
|---:|---:|---|
| 𑁒 | 1 | U+11052 |
| 𑁓 | 2 | U+11053 |
| 𑁔 | 3 | U+11054 |
| 𑁕 | 4 | U+11055 |
| 𑁖 | 5 | U+11056 |
| 𑁗 | 6 | U+11057 |
| 𑁘 | 7 | U+11058 |
| 𑁙 | 8 | U+11059 |
| 𑁚 | 9 | U+1105A |
| 𑁛 | 10 | U+1105B |
| 𑁤 | 100 | U+11064 |
| 𑁥 | 1000 | U+11065 |

Unicode’s BRAHMI NUMBER JOINER U+1107F distinguishes multiplicative ligation: an unjoined “100 + 4” means 104, while joined “100 × 4” means 400. [Unicode, Chapter 14](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-14/)

### Positional digits

Later Brahmi documents contain a second repertoire, ancestral to the place-value decimal numerals:

`𑁦 𑁧 𑁨 𑁩 𑁪 𑁫 𑁬 𑁭 𑁮 𑁯` = 0–9.

**[Reconstruction]** The shapes ultimately developed into regional Indic digits and, through further transmission, the Hindu-Arabic numerals.

**[Disputed]** Claims that the earliest Brahmi numeral shapes were alphabetic, acrophonic, or merely tally-derived remain conjectural.

---

# Origins

## 1. The prehistory of writing in South Asia

### Indus signs

**[Artefact]** The Indus/Harappan corpus, approximately 2600–1900 BCE, consists of short sign sequences on seals, tablets, pottery, and other objects.

**[Open question]** Whether it encodes continuous language, and which language, remain undeciphered.

**[Disputed]** Direct descent from Indus signs to Brahmi has been repeatedly proposed. The evidentiary problems are:

- roughly a millennium or more with no secure sequence of intermediate texts;
- no agreed Indus decipherment from which sound correspondences can be tested;
- Brahmi’s systematic alphasyllabic structure differs from every major published reconstruction of the Indus corpus;
- visually similar simple strokes can arise independently.

Continuity of scribal or marking practices is conceivable; demonstrable graphic-linguistic descent is absent.

## 2. Earliest candidates

| Candidate | Date claimed | Place/object | Evidentiary status |
|---|---:|---|---|
| Anuradhapura potsherds | beginning of fourth century BCE; some reports claim still earlier levels | Citadel of Anuradhapura, Sri Lanka | **[Artefact; dating disputed]** letters occur on sherds associated with radiocarbon-dated strata. Coningham and colleagues argued for early fourth-century Brahmi. Doubts concern intrusion, residual material, calibration, and association rather than direct dating of the incisions. |
| Porunthal/Kodumanal sherds | c. 520–490 BCE in associated carbon samples | Tamil Nadu | **[Artefact; disputed identification and association]** K. Rajan and V. P. Yatheeskumar connect inscribed pottery with AMS-dated material. Harry Falk disputes that some supposed letters are Brahmi rather than megalithic graffiti and rejects direct transfer of the carbon date to the inscription. |
| Keeladi sherds | claims of sixth/fifth century BCE literacy | Tamil Nadu | **[Artefact + disputed inference]** settlement samples yield early dates and inscribed sherds exist, but the claim that a particular Brahmi inscription is directly dated to the sixth century BCE requires secure stratigraphic association and full publication. The state excavation report advocates the early interpretation. |
| Adichanallur/Sivagalai claims | variously eighth/sixth century BCE or earlier | Tamil Nadu | **[Disputed]** radiocarbon dates generally date associated organic material, not the strokes themselves; some marks may be nonlinguistic graffiti. |
| Piprahwa reliquary inscription | often placed c. third–first century BCE; sometimes claimed pre-Aśokan | Uttar Pradesh border region | **[Artefact; date/reading disputed]** discovered by W. C. Peppé in 1898, read by Georg Bühler as referring to relics of the Buddha and the Śākyas. Authenticity, syntax, depositional history, and date have all been debated. |
| Sohgaura copper plate | Mauryan or possibly pre-Mauryan | near Gorakhpur, Uttar Pradesh | **[Artefact; dating disputed]** Prakrit administrative text in early Brahmi, traditionally connected with famine relief. It does not carry an unambiguous absolute date. |
| Mahasthangarh stone | Mauryan, sometimes proposed pre-Aśokan | Bangladesh | **[Artefact; disputed date]** early Prakrit/Brahmi administrative order; palaeography supplies only a range. |
| Bhattiprolu caskets | third–first centuries BCE | Andhra Pradesh stupa | **[Artefact]** regional Brahmi orthography on relic caskets, important for southern developments but not securely earlier than Aśoka. |
| Eran coin | early date proposed; reversed legend | Madhya Pradesh | **[Artefact; interpretation disputed]** reverse direction may reflect die engraving, not an ancestral right-to-left Brahmi. |

**Finding:** No presently known pre-Aśokan candidate combines an internally dated inscription, uncontested Brahmi letter identification, secure undisturbed context, and universal specialist acceptance.

Coningham’s peer-reviewed Anuradhapura study calls the sherds the earliest archaeological examples, while Salomon accepted their possible importance cautiously. [Coningham et al., “Passage to India?”](https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/abs/passage-to-india-anuradhapura-and-the-early-use-of-the-brahmi-script/DAAA2514FB08E1DDE3FAFF2171AB097B); [Tamil Nadu Archaeology, Keeladi](https://www.tnarch.gov.in/node/1257)

## 3. The first secure great corpus: Aśoka

**[Artefact]** Aśoka’s rock and pillar edicts, composed during his reign in the third century BCE, are the first extensive and historically anchored corpus in Brahmi. They proclaim *dhamma*, administrative policy, animal and human welfare, restraint, religious concord, and royal activity.

The corpus is multilingual and multiscript:

- Brahmi for Prakrit through most of the empire;
- Kharoṣṭhī for northwestern Prakrit at Shahbazgarhi and Mansehra;
- Aramaic in Afghanistan;
- Greek and Greek-Aramaic at Kandahar.

This distribution is powerful evidence that the Mauryan chancery deliberately selected scripts for regional audiences. The edicts are not proof that Aśoka invented Brahmi: their geographic variety and competent execution imply prior development and trained scribes.

Important sites include:

- Girnar/Junagadh, Gujarat: Major Rock Edicts I–XIV;
- Kalsi, Uttarakhand: Major Rock Edicts;
- Dhauli and Jaugada, Odisha: modified Kalinga series;
- Shahbazgarhi and Mansehra, Pakistan: Kharoṣṭhī versions;
- Sanchi, Sarnath, Kosambi, Lauriya-Araraj, Lauriya-Nandangarh, Rampurva, Delhi-Topra, and Delhi-Meerut: pillar or schism texts;
- Maski and Gujarra: texts naming Aśoka rather than only “Devanampiya Piyadasi”;
- Bairat/Bhabru: a uniquely Buddhist recommendation of named teachings.

Many monuments remain in situ and therefore have no museum accession number. A firmly catalogued exception is the polished sandstone fragment of the Meerut-Delhi pillar bearing part of Major Pillar Edict VI, **British Museum 1880.21**. It was erected at Meerut, moved to Delhi under Fīrūz Shāh Tughluq, later broken, and transferred through the India Museum. [British Museum object 1880.21](https://www.britishmuseum.org/collection/object/A_1880-21)

The Bairat/Bhabru boulder is in the Asiatic Society, Kolkata. The Society identifies it as its oldest inscription but its online catalogue supplies no accession number; absence of a published number should not be repaired by invention. [Asiatic Society collection record](https://www.asiaticsociety.culture.gov.in/departments/museum/collections/inscriptions)

## 4. Competing origin hypotheses

### A. Aramaic or broader Semitic stimulus

**[Scholarly reconstruction; disputed in details]** Albrecht Weber proposed Semitic derivation in 1856. Georg Bühler’s *On the Origin of the Indian Brāhma Alphabet* developed a detailed northern-Semitic comparison in 1895.

Evidence advanced:

- Achaemenid Aramaic was an imperial administrative script in territories adjoining or including the northwest of South Asia.
- Kharoṣṭhī is demonstrably close to Aramaic.
- Some Brahmi signs can be compared with Aramaic forms after rotation, inversion, or graphic modification.
- Brahmi emerges historically after sustained West Asian contact.
- The designers may have taken a consonantal signary and expanded it to accommodate Indo-Aryan phonology.

Difficulties:

- proposed one-to-one graphic matches often require different rotations or transformations;
- Brahmi’s order and structure are thoroughly Indian;
- independent vowel letters, aspirate/voicing distinctions, retroflexes, and the inherent-vowel system require major innovation;
- no intermediate “Proto-Brahmi” document shows the borrowing in progress;
- Brahmi is much less transparently Aramaic than Kharoṣṭhī.

A defensible synthesis is “external graphic stimulus plus deliberate Indian systemic creation,” but this remains reconstruction, not an attested borrowing event.

### B. Indigenous invention

**[Scholarly reconstruction; broad and internally diverse]** An indigenous model may mean invention within South Asia without direct graphic descent from another script. Its evidence includes Brahmi’s close fit with Indian phonetics, its rational order, and the absence of a compelling complete Aramaic sign-by-sign derivation.

Its principal difficulty is historical: the earliest secure corpus appears suddenly in a period of intensive Persian, Aramaic, Greek, and northwestern contact.

### C. Indus descent

**[Disputed]** Advocates compare individual forms or propose survival through pottery graffiti. The chronological gap and undeciphered source corpus prevent testing sound correspondences. No specialist consensus accepts a demonstrated genealogical chain.

### D. Greek or hybrid models

**[Disputed reconstruction]** Greek influence has been invoked for vowel representation, left-to-right direction, or particular letter shapes. Joseph Halévy proposed a composite formation involving Aramaic, Kharoṣṭhī, and Greek. Modern hybrid proposals continue.

Greek contact in the northwest is historically real, and Greek appears in Aśokan administration, but a specific Greek-to-Brahmi derivation is not established. Brahmi’s vowel system is not simply the Greek alphabetic solution.

### E. Invention by Aśoka’s government

**[Disputed reconstruction]** Harry Falk has argued for comparatively late, deliberate creation in connection with Mauryan imperial needs.

Supporting points:

- the first unquestionably dated corpus is Aśokan;
- rapid administrative dissemination can explain broad standardization;
- the design appears systematic.

Counter-evidence:

- regional varieties within the edicts imply pre-existing scribal practice;
- Anuradhapura may predate the Mauryan corpus;
- the fully elaborated system would have required a preparatory stage;
- writing is presupposed by some earlier textual and administrative traditions, though textual dates are difficult.

The evidence permits Mauryan reform, sponsorship, or standardization more readily than it proves invention from nothing.

## 5. Traditional and legendary origins

**[Text/tradition]** Buddhist *Lalitavistara* and Jain script lists place Brāhmī and Kharoṣṭhī among numerous scripts known to an exemplary learned figure. These texts are later than the events they narrate and cannot establish a fifth-century BCE sign inventory.

**[Legend]** Brahmā created the script, or Brāhmī personifies his creative energy. The tale explains the name and sacral authority of writing; it is not corroborated by early inscriptions.

**[Text]** The Chinese Buddhist encyclopedia *Fayuan zhulin* and related transmitted traditions associate Brāhmī with left-to-right writing and Kharoṣṭhī with right-to-left writing. These preserve learned classifications rather than eyewitness evidence of invention.

---

# Decipherment

## 1. Loss and partial continuity

Brahmi did not vanish in the sense of leaving no descendants. Its ancient monumental forms became unreadable because letter shapes changed drastically, languages changed, and Aśoka’s political identity disappeared from accessible historical memory.

Medieval and early modern readers could read contemporary Nāgarī or Bengali but not automatically Mauryan inscriptions.

## 2. Prinsep and the decipherment network

**[Documented publication history]**

- Eighteenth- and early nineteenth-century surveyors copied inscriptions, often imperfectly.
- Charles Wilkins and others read later Gupta and post-Gupta scripts, establishing palaeographic bridges.
- Christian Lassen and others used bilingual Indo-Greek coin legends in the recovery of Kharoṣṭhī.
- James Prinsep, secretary of the Asiatic Society of Bengal, collated multiple facsimiles and coin legends.
- In 1837 he recognized recurrent donative formulas on Sanchi-type inscriptions, including forms corresponding to *dānaṃ*, “gift.”
- He read the royal title **Devanampiya Piyadasi**, “Beloved of the Gods, He of Gracious Appearance,” across the edicts.
- George Turnour’s work with the Sri Lankan Pali chronicles connected Piyadasi with Aśoka.
- Prinsep’s publications of 1837–38 produced an essentially successful Brahmi key, later refined for regional and phonetic details.

It is misleading to portray this as a solitary instantaneous “Eureka.” Prinsep’s synthesis was decisive, but it depended on Indian pandits, engravers, draftsmen, field officers, earlier palaeographers, coin collectors, Turnour, Lassen, and the institutional exchange of copies. The original contemporary record is in the *Journal of the Asiatic Society of Bengal*, vol. VI. [Digitized 1837 volume](https://zenodo.org/records/3361245); [Prinsep, “Further elucidation…”](https://www.biodiversitylibrary.org/part/366962)

---

# Spread and change

## 1. Third–first centuries BCE: imperial and regional Brahmi

After Aśoka, Brahmi appears in:

- Buddhist and Jain cave donations;
- reliquaries and stupas;
- royal and private records;
- coins, seals, potsherds, and merchants’ marks;
- Tamil-speaking territory and Sri Lanka.

### Tamil-Brahmi

**[Artefact + reconstruction]** Brahmi was adapted to Tamil phonology, including special letters for sounds conventionally transliterated ḻ, ṟ, and ṉ and orthographic strategies better suited to consonant-final words and the absence of the same pervasive inherent /a/ assumptions as northern Prakrit.

Early cave inscriptions frequently name donors and are associated with Jain ascetics, but it is too strong to infer that every early Tamil inscription or the entire adaptation was exclusively Jain.

### Bhattiprolu

Relic-casket inscriptions at the Buddhist stupa in Andhra Pradesh use a distinctive regional Brahmi. Their treatment of consonants and vowels has figured prominently in discussions of southern Brahmi and Tamil-Brahmi, but a simple one-way genealogy is not established.

### Kharoṣṭhī in the northwest

Kharoṣṭhī remained important in Gandhāra, the Punjab, Afghanistan, and Central Asian Buddhist networks, especially from the third century BCE into the early centuries CE. It wrote right-to-left and used an inherent-vowel system developed from Aramaic. Brahmi ultimately replaced it in most functions by roughly the fourth/fifth century CE.

## 2. First centuries CE: Sanskritization and diversification

The earliest Brahmi corpus is overwhelmingly Middle Indo-Aryan/Prakrit, not Vedic or Classical Sanskrit.

From around the first centuries BCE/CE, Sanskrit increasingly entered inscriptions. Major landmarks include the Sanskritized Ayodhya and Ghosundi materials and the polished Sanskrit prose of Rudradāman’s Junagadh inscription, c. 150 CE.

**[Reconstruction]** The use of Brahmi for Sanskrit helped expand or regularize distinctions that some Aśokan Prakrit dialects did not require.

Regional scripts become increasingly distinguishable:

- northwestern;
- Mathura;
- eastern;
- western;
- Andhra;
- Tamil and Sinhala traditions;
- Central Asian Brahmi varieties.

## 3. Gupta and post-Gupta scripts, fourth–seventh centuries

“Gupta script” is a palaeographic umbrella rather than one perfectly uniform alphabet. It denotes northern Brahmi forms characteristic of Gupta-era inscriptions and manuscripts.

From later Gupta and post-Gupta styles developed:

- **Siddham/Siddhamātṛkā**;
- **Śāradā** in Kashmir and the northwest;
- early **Nāgarī**;
- eastern forms ancestral to Gauḍī, Bengali-Assamese, Odia, and related scripts.

## 4. Siddham and Buddhist East Asia

Siddham developed around the sixth century CE and became important for Sanskrit Buddhist manuscripts and dhāraṇīs.

**[Artefact/textual transmission]** Buddhist monks carried Sanskrit texts and Indic letter knowledge into China and Japan. In Japan, especially through Shingon and Tendai esoteric Buddhism, Siddham—Japanese *shittan*—survived as a sacred calligraphic script after ordinary Indian use declined. Kūkai (774–835), who studied in Tang China, became central to Japanese esoteric transmission, though he did not invent Siddham.

Siddham letters may be contemplated individually as embodiments of Buddhas, syllables, or cosmic principles. This is a living ritual survival, not merely an antiquarian revival.

## 5. Nāgarī and Devanagari

Early Nāgarī emerged gradually from north-Indian post-Gupta hands. By approximately the eighth–eleventh centuries it is visibly ancestral to mature Devanagari; the full headline becomes increasingly characteristic.

The name *Devanāgarī* is interpreted as “divine/city script” or “script of the divine Nāgarī,” but no single etymology or founding event is securely documented.

Devanagari became a leading manuscript hand for Sanskrit, but Sanskrit remained multiscriptal: it was also written in Grantha, Telugu, Kannada, Malayalam, Bengali, Śāradā, Newa, Nandinagari, Tibetan, and other scripts. The notion that Sanskrit “belongs” intrinsically to Devanagari is largely a product of modern standardization and print.

### Hindi standard

In the nineteenth and twentieth centuries, Hindi advocates, printers, educational institutions, colonial bureaucracies, and the Nāgarī Prachāriṇī Sabhā promoted Devanagari against Persian-script Urdu and competing documentary hands.

**[Modern legal fact]** Article 343 of India’s Constitution declares Hindi in Devanagari the official language of the Union, while permitting continued English and recognizing a multilingual constitutional order. The Central Hindi Directorate issued spelling standardization in 1967, revised it in 1983 and again in 2024. [Government of India standardization record](https://www.chd.education.gov.in/devanagari-lipi-tatha-hindi-vartani-manakikaran)

Devanagari is currently used for Hindi, Marathi, Nepali, Sanskrit, Konkani and many additional languages, although usage and official status vary.

## 6. Northern and western sisters

### Bengali-Assamese

Eastern post-Gupta/Gauḍī forms developed into the modern Bengali-Assamese script. Bengali and Assamese share most of the graphic system but differ in preferred letter names, a few characters, typography, and cultural designation.

### Odia

Odia emerged from eastern scripts. Its rounded forms are frequently attributed to palm-leaf writing, where long horizontal cuts could split a leaf.

**[Qualification]** Writing material plausibly influenced ductus, but “all rounded letters arose because straight strokes tore palm leaves” is an oversimplified modern explanation.

### Gujarati

Gujarati developed from western Nāgarī documentary and mercantile hands, becoming recognizably distinct by the early modern period. Removal of the continuous headline suited rapid account-book writing, though functionality alone does not explain every form.

A manuscript of 1591–92 is often cited as an early specimen of distinct Gujarati; print appeared by the late eighteenth/early nineteenth century. Jain scribes and merchants were central to its documentary culture.

### Gurmukhi

**[Tradition]** Guru Angad (1504–1552), second Sikh Guru, created Gurmukhi.

**[Historical reconstruction]** Most letterforms have demonstrable pre-Sikh northwestern antecedents, often discussed through Śāradā, Takri, and Laṇḍā traditions. Guru Angad or the early Sikh community probably selected, regularized, taught, and authorized a regional script during the 1530s–40s rather than inventing every sign ex nihilo.

Gurmukhi became the script of Sikh scripture and eastern Punjabi. The *Ādi Granth* was compiled under Guru Arjan in 1604. Punjabi in Pakistan is principally written in Shahmukhi, a Perso-Arabic script.

## 7. Southern sisters

### Tamil

Tamil script descends through Tamil-Brahmi and later southern forms, including Vaṭṭeḻuttu-related and Pallava/Grantha interaction. Modern Tamil has fewer consonant letters than Sanskrit-oriented scripts and uses contextual values plus Grantha-derived additions for some Sanskrit sounds.

### Telugu and Kannada

They share a long common history in southern Brahmi, Kadamba/Chalukya and “Telugu-Kannada” writing. Clearly separate typographic standards crystallized gradually rather than at a single split date.

### Malayalam

Malayalam developed from southern Grantha and regional Kerala hands, alongside interaction with Vaṭṭeḻuttu and Koleḻuttu. Its large conjunct inventory reflects heavy Sanskrit use; twentieth-century reforms promoted reduced forms for printing and typewriting while traditional orthography survives.

### Sinhala

Sinhala descends from southern Brahmi in Sri Lanka, with inscriptions from the last centuries BCE onward. It developed separate sets of core “pure Sinhala” letters and an expanded repertoire for Sanskrit/Pali loans.

## 8. Tibetan

**[Tradition]** King Songtsen Gampo sent Thonmi Sambhota to India in the seventh century; Thonmi returned, created Tibetan writing from an Indic model, and composed grammars.

**[Historical difficulty]** Contemporary Old Tibetan sources do not securely identify Thonmi as inventor; clear narratives appear in later Tibetan historiography. The figure’s existence and exact role are therefore difficult to verify.

**[Palaeographic reconstruction]** Tibetan is unmistakably Brahmic, probably derived from a north-Indian Gupta/post-Gupta model, with debate over whether the closest comparison is Kashmiri, Siddham, or another regional hand. The script adapted the abugida through stacked consonants and a fixed set of vowel signs. [Sam van Schaik, “A New Look at the Tibetan Invention of Writing”](https://earlytibet.com/wp-content/uploads/2007/06/vanschaik_2011a.pdf)

## 9. Southeast Asia

Indic writing travelled with maritime and overland exchange, courts, Brahmins, Buddhist monks, Sanskrit prestige culture, and Pali textual traditions. “Indianization” should not be understood as mass Indian colonization: Southeast Asian courts actively selected and redesigned imported forms.

Early landmarks include:

- Sanskrit inscriptions in mainland and island Southeast Asia from approximately the fourth/fifth centuries CE, with the Võ Cạnh inscription sometimes placed earlier but disputed;
- Kutai yūpa inscriptions in Borneo;
- Tarumanagara inscriptions in Java;
- early Khmer inscriptions, including a dated Khmer text of 611 CE;
- Pyu and Mon inscriptions;
- Kawi/Old Javanese inscriptions from the first millennium CE.

Genealogical outline:

- southern Brahmi/Pallava-Grantha styles → early Khmer;
- Khmer and related mainland traditions → Thai and Lao, with major restructuring for tone;
- southern Indic forms → Mon and Burmese/Myanmar;
- Pallava/Kawi → Javanese, Balinese and related Indonesian scripts.

Thai is structurally innovative: consonant classes, tone marks, complex vowel placement, and reduced conjunct behavior adapt a Brahmic base to a tonal Tai language. Khmer retains extensive subscript consonants. Burmese and Sinhala developed strongly rounded manuscript hands. Javanese and Balinese retain elaborate syllabic and honorific/calligraphic traditions.

## 10. Printing and typography

Indic ligatures and repositioning made movable type unusually laborious.

- **1771:** the *Alphabetum Brammhanicum* printed in Rome included Devanagari types, with shapes reportedly based on drawings by Indian Christian assistants.
- **1778:** Nathaniel Brassey Halhed’s *A Grammar of the Bengal Language* used Bengali types cut through the collaboration of Charles Wilkins and Panchanan Karmakar.
- Mission presses at Serampore expanded Bengali, Devanagari, and other Indic fonts.
- Metal type forced decisions about which conjuncts deserved separate sorts.
- Lithography often preserved manuscript freedom more successfully than movable type.
- Typewriters and hot-metal composition encouraged reduced conjunct repertoires.
- Twentieth-century Monotype and Linotype projects regularized character widths and joining behavior, sometimes reshaping orthographic convention.
- Fiona Ross and contemporary designers have documented the “invisible hands” of Indian punchcutters, compositors, draftsmen, and consultants omitted from corporate histories. [Ross and Shaw, Linotype Devanagari study](https://centaur.reading.ac.uk/101230/); [Ross, Bengali type history](https://soas-repository.worktribe.com/output/403271/the-evolution-of-the-printed-bengali-character-from-1778-to-1978)

Gurmukhi movable type is documented from 1800; its British design and distribution history is reconstructed in Sahar Afshar’s archival study. [Afshar 2023](https://www.open-access.bcu.ac.uk/14181/)

## 11. Digital encoding and the “Unicode fights”

Unicode inherited much of its modern Indic layout from ISCII. Devanagari, Bengali, Gurmukhi, Gujarati, Odia, Tamil, Telugu, Kannada, and Malayalam were assigned parallel block structures, although their rendering behavior differs.

| Script | Principal Unicode block |
|---|---|
| Devanagari | U+0900–U+097F |
| Bengali | U+0980–U+09FF |
| Gurmukhi | U+0A00–U+0A7F |
| Gujarati | U+0A80–U+0AFF |
| Odia | U+0B00–U+0B7F |
| Tamil | U+0B80–U+0BFF |
| Telugu | U+0C00–U+0C7F |
| Kannada | U+0C80–U+0CFF |
| Malayalam | U+0D00–U+0D7F |
| Sinhala | U+0D80–U+0DFF |
| Thai | U+0E00–U+0E7F |
| Lao | U+0E80–U+0EFF |
| Tibetan | U+0F00–U+0FFF |
| Myanmar | U+1000–U+109F |
| Khmer | U+1780–U+17FF |
| Balinese | U+1B00–U+1B7F |
| Javanese | U+A980–U+A9DF |
| Brahmi | U+11000–U+1107F |
| Siddham | U+11580–U+115FF |

Important controversies were technical rather than merely graphic:

- whether historically divergent regional Brahmis should be unified;
- whether a conjunct is a character or a font-rendered sequence;
- how to encode visibly identical but semantically different marks;
- whether Vedic signs are script-specific or generic;
- how collation should treat nukta letters;
- whether inherited ISCII ordering should be retained;
- how Tamil and Bhattiprolu consonant/vowel behavior should be represented.

The 2007–08 Brahmi proposal was expressly controversial over unifying later Central Asian varieties; its authors proposed proceeding first with the mature, broadly accepted repertoire. Unicode ultimately encoded Brahmi in version 6.0 (2010). [Everson, Glass and Baums](https://www.unicode.org/L2/L2008/08277r-n3490r-brahmi.pdf)

Unicode encodes abstract characters, not every historical glyph. Fonts, OpenType shaping rules, and language tags remain necessary to produce correct regional and manuscript forms.

---

# The letters as numbers and signs

## 1. Alphabetic numeration

Early Brahmi numerals are separate number signs, not systematic letter values.

Later India did develop **alphasyllabic numeral notations**, including:

- **Āryabhaṭa’s system**, assigning place values through consonants and vowels;
- **Kaṭapayādi**, assigning digits to consonant classes so meaningful words or verses encode numbers;
- **bhūtasaṃkhyā**, using objects conventionally associated with numbers—moon = 1, eyes = 2, Vedas = 4, and so forth.

These resemble gematria functionally but are not simple Brahmi-letter ordinal values.

## 2. Oṃ

**[Text]** The syllable *oṃ* or *praṇava* is interpreted in the Upaniṣads, especially the Chāndogya, Taittirīya, Māṇḍūkya, and related traditions, as sacred sound, cosmic totality, assent, and meditative support.

**[Artefact]** Its modern graphic symbol `ॐ` is much younger than those oral and textual interpretations. Written Oṃ developed through regional ligature and calligraphic traditions in the early medieval period; Buddhists and Jains contributed to its inscriptional/iconographic history as well as Brahmanical traditions.

Script-specific symbols include Devanagari ॐ, Tamil ௐ, Grantha 𑍐, and others. Unicode also encodes U+1F549 OM SYMBOL as a generic symbol. It is incorrect to project the modern Devanagari glyph unchanged into Vedic antiquity. [University of Vienna, “Inscribing the Sacred Syllable”](https://stb.univie.ac.at/news-events/detail/news/inscribing-the-sacred-syllable-towards-a-history-of-om-as-a-written-sign-and-icon/)

## 3. Mātṛkā, bīja, and tantric letter cosmology

**[Text/tradition]** In Śaiva, Śākta, Buddhist, and Jain esoteric traditions, sounds and letters can be powers rather than neutral notational units.

- The Sanskrit phonemes are the **Mātṛkās**, “Mothers.”
- The alphabet may be installed on the practitioner’s body through *mātṛkānyāsa*.
- Lotus petals of subtle-body diagrams receive letter sets.
- A **bīja**, “seed syllable,” condenses a deity or power: *hrīṃ, śrīṃ, klīṃ, hūṃ*, and so on.
- *A* and *ha*, first and last in a traditional sequence, can signify totality; *aham* is interpreted esoterically as encompassing the alphabet.
- Kṣa, technically a conjunct, often functions ritually as the alphabet’s final member.
- Mantras may be “extracted” through coded alphabet tables and substitution vocabularies.

These are documented religious semiotics, not claims about the historical invention of Brahmi. A representative translated ritual source is the *Mahānirvāṇa Tantra*, whose goddess of speech is visualized as composed of fifty letters. [Text, chapter 5](https://sacred-texts.com/tantra/maha/maha05.htm); [Cambridge study of mantra practice](https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/abs/selecting-and-perfecting-mantras-in-hindu-tantrism/7122857D5602C55F933838D1AA6E9CF2)

## 4. Siddham letter symbolism

In East Asian esoteric Buddhism, individual Siddham syllables serve as icons. The syllable `अ` /a/, for example, can symbolize non-arising or emptiness; seed syllables identify Buddhas and ritual families. Calligraphing, visualizing, or placing such a letter in a mandala is itself religious practice.

## 5. Sikh letter symbolism

The Gurmukhi script derives sacral prestige from its embodiment of *gurbāṇī*. Acrostic compositions such as Guru Nanak’s *Paṭī* use the pedagogical alphabet as a sequence for spiritual teaching. Reverence belongs to the revealed utterance and scripture; this should not be converted into the undocumented claim that each Gurmukhi glyph was supernaturally invented.

---

# People

| Person/group | Dates | Role and status |
|---|---:|---|
| Pāṇini | commonly c. fifth/fourth century BCE; disputed | **[Textual scholar]** grammarian whose phonological system demonstrates sophisticated sound classification; not documented as Brahmi’s inventor. |
| Aśoka | reigned c. 268–232 BCE | **[Documented patron]** ordered the first great dated corpus; used Brahmi, Kharoṣṭhī, Greek, and Aramaic regionally. |
| Mauryan scribes and engravers | third century BCE | **[Artefact]** anonymous designers, translators, copyists, and stonecutters responsible for regional versions. |
| Brahmā | timeless deity | **[Legend]** creator or source of Brāhmī. |
| James Prinsep | 1799–1840 | **[Documented decipherer]** synthesized inscriptional and numismatic evidence, 1837–38. |
| George Turnour | 1799–1843 | Linked Piyadasi with Aśoka through Sri Lankan chronicles. |
| Christian Lassen | 1800–1876 | Numismatic and Kharoṣṭhī decipherment work. |
| Alexander Cunningham | 1814–1893 | Surveyor, corpus compiler, archaeological administrator, advocate of indigenous possibilities. |
| Albrecht Weber | 1825–1901 | Proposed Semitic origin in 1856. |
| Georg Bühler | 1837–1898 | Systematic palaeographer and leading Semitic-origin theorist; read the Piprahwa inscription. |
| Eugen Hultzsch | 1857–1927 | Editor of *Inscriptions of Asoka*, *Corpus Inscriptionum Indicarum* I, 1925. |
| D. C. Sircar | 1907–1985 | Major Indian epigraphist and handbook author. |
| Ahmad Hasan Dani | 1920–2009 | Historian of Indian palaeography; cautioned against genetic conclusions from reversed writing. |
| Iravatham Mahadevan | 1930–2018 | Produced foundational concordance and study of Tamil-Brahmi inscriptions. |
| Harry Falk | b. 1947 | Argued for a comparatively late, purposeful creation/adaptation of Brahmi; critic of several early Tamil datings. |
| Richard Salomon | b. 1948 | Principal modern synthesist of Indian epigraphy, Brahmi/Kharoṣṭhī, and Gandhāran manuscript culture. |
| Stefan Baums and Andrew Glass | contemporary | Specialists in early Buddhist manuscripts; co-designed the mature Brahmi Unicode proposal. |
| Michael Everson | b. 1963 | Script encoder and contributor to Brahmi’s Unicode proposal. |
| Thonmi Sambhota | traditionally seventh century | **[Tradition/disputed historicity]** credited with creating Tibetan writing. |
| Songtsen Gampo | c. 605–650 | Tibetan emperor under whom writing and translation were institutionalized. |
| Guru Angad | 1504–1552 | **[Tradition + reconstruction]** credited with inventing Gurmukhi; historically more plausibly standardized and promoted antecedent forms. |
| Charles Wilkins | 1749–1836 | Early reader of later inscriptions and pioneer of Bengali/Devanagari types. |
| Panchanan Karmakar | died c. 1804 | Indian punchcutter central to early Bengali movable type. |
| William Carey and Serampore collaborators | late eighteenth–nineteenth centuries | Expanded multilingual Indic printing. |
| Fiona Ross | contemporary | Historian and designer of Bengali and other non-Latin typography; documented Indian collaborators in type production. |

---

# Culture

## Law and government

Aśoka’s inscriptions turned exposed rocks and monolithic pillars into public royal media. Later dynasties used Brahmic scripts for:

- land grants;
- tax exemptions;
- irrigation works;
- temple endowments;
- military victories;
- genealogies;
- boundary records;
- guild and merchant donations.

Copper-plate charters became especially important. Seals authenticated grants; opening formulae and auspicious symbols carried juridical and religious authority.

## Scripture and manuscript culture

Brahmic scripts have carried:

- Buddhist sūtras, vinaya, dhāraṇī, and commentaries;
- Jain āgamas and scholastic texts;
- Vedas and Vedic accent notation;
- Sanskrit epics, Purāṇas, philosophy, grammar, mathematics, astronomy, medicine, and poetry;
- Tamil, Kannada, Telugu, Malayalam, Bengali, Marathi, Hindi, Punjabi, Sinhala, Burmese, Khmer, Thai, Javanese and Balinese literatures.

Writing materials shaped practice:

- birch bark in the northwest and Kashmir;
- palm leaf across much of southern and eastern Asia;
- paper from the medieval period onward;
- copper, stone, wood, cloth, and prepared metal;
- stylus-incised and ink-written traditions.

The survival of orally transmitted Vedic texts does not imply that writing was unknown; it reflects a deliberate ideology and technique of oral precision.

## Coins and seals

Brahmi legends occur on indigenous and Indo-Greek/Śaka/Kushan/Gupta coinages. Coins provided decipherers with short repeated royal names, titles, and bilingual correspondences. Direction can reverse because legends were cut into dies.

Seals and sealing impressions document names, offices, monasteries, merchants, and administrative control. Their brevity makes isolated readings vulnerable to circular interpretation.

## Monuments and visual art

Brahmi and its descendants appear on:

- Aśokan pillars and rocks;
- stupa railings at Sanchi and Bharhut;
- cave façades and cells;
- temple walls and foundation deposits;
- bronzes and stone icons;
- painted manuscripts;
- calligraphic mandalas and yantras.

Letters can become bodies or architecture: Sanskrit letter goddesses, Siddham seed syllables, Tibetan *lantsa* inscriptions, calligraphic Oṃ figures, and manuscript colophons all dissolve the boundary between writing and image.

## Calendars, mathematics, and science

Indic digits transformed astronomical tables, calendars, accountancy, and computation. Place-value decimal notation and zero emerged gradually in Indian mathematical culture; no single surviving object records one moment of “invention.”

Astronomers encoded numbers in words and syllables to fit verse metre. Calendrical inscriptions employ regnal years, eras, lunar months, fortnights, weekdays, and astronomical configurations, making them crucial—though sometimes treacherous—dating tools.

## Alphabet poems and pedagogy

The ordered signary generated:

- school alphabets and writing boards;
- Buddhist and Jain *lipi* lists;
- Sanskrit grammatical mnemonics;
- Sikh *paṭī* compositions;
- tantric alphabet garlands;
- South and Southeast Asian acrostic and syllabic poems.

Unlike the Semitic abecedarium, an Indic writing exercise often displays the phonetic grid: vowels followed by five stop rows.

---

# Controversies and disputes

## 1. Is Brahmi Semitic or indigenous?

No surviving ancient author describes the borrowing. The dispute is therefore inferential.

The Semitic case is strongest historically—Achaemenid Aramaic contact and the certain Aramaic descent of Kharoṣṭhī—but weakest where it claims exact visual derivation for every Brahmi letter.

The indigenous case is strongest structurally—the script embodies Indian phonology—and weakest when it treats structural redesign as proof that no foreign graphic stimulus existed.

The most economical present reconstruction is external stimulus followed by extensive local invention, but the exact prototype, place, designers, and date remain unknown.

## 2. Did writing exist in India before Aśoka?

Literary references to writing, scribes, letters, marks, and documents may preserve pre-Mauryan practice, but dating Indian texts is difficult and later passages may be interpolated.

Archaeological candidates support the possibility. None yet supplies an undisputed long pre-Aśokan text.

Therefore:

- “Aśoka invented writing in India” is unsupported.
- “Brahmi certainly existed in 600 BCE” exceeds the secure evidence.
- “There was no writing before Aśoka” mistakes absence of survival for proof of absence.

## 3. Anuradhapura

The early strata and inscribed sherds are genuine archaeological evidence. The dispute concerns whether the marked sherds belong securely to the radiocarbon-dated contexts and whether every sign is Brahmi. A fourth-century BCE date is plausible and influential but not equivalent to an internally dated monument.

## 4. Porunthal, Kodumanal, Keeladi, and “Tamili”

Tamil Nadu reports use the name *Tamili* and argue for fifth/sixth-century BCE literacy.

Critics respond that:

- dated rice or charcoal may not date a potsherd inscription;
- some supposed letters are megalithic graffiti;
- mixed or disturbed deposits weaken association;
- palaeographic expectations should be independently tested.

Political identity has intensified the argument but does not by itself invalidate either the artefacts or criticism. Full stratigraphic publication, direct residue analysis where possible, and reproducible sign readings are decisive.

## 5. Piprahwa

The reliquary inscription is physically real and Bühler’s early reading connected it with Buddha relics. Disputes concern grammar, whether the “Śākya brothers” or a donor group is intended, the date, and the integrity of the excavation. Sensational claims of either conclusive proof or obvious forgery outrun the evidence.

## 6. Brahmi and Sanskrit nationalism

**[Modern invention/identity politics]** Brahmi is sometimes described as an eternally Sanskrit or Hindu script. The earliest large corpus actually writes Prakrit and includes imperial moral policy; early expansion is deeply associated with Buddhist, Jain, mercantile, and regional use.

The contrary claim that Brahmi was exclusively Buddhist or anti-Brahmanical is equally reductive. It eventually served nearly every major South Asian religious and linguistic tradition.

## 7. “Palm leaves made every southern script round”

Writing material influenced stroke habits, especially avoidance of long cuts along the grain. But roundedness also reflects pen/stylus mechanics, inherited ductus, local aesthetics, and centuries of change. It is a contributing reconstruction, not a universal mechanical law.

## 8. Thonmi Sambhota

Tibetan tradition supplies a named inventor and royal mission. Palaeography supports derivation from India, but early Tibetan sources do not confirm the mature biography. The tradition may personify an institutional reform by multiple translators and scribes.

## 9. Guru Angad and Gurmukhi

Guru Angad’s role in teaching and standardizing Gurmukhi belongs to both Sikh memory and a plausible historical process. Pre-existing letterforms refute only the strongest “creation from nothing” version, not the Guru’s formative cultural role.

## 10. Unicode unification

Encoding a historical script requires deciding which differences are characters and which are glyph variants. Those decisions affect searchable editions and can privilege one palaeographic reconstruction.

The Brahmi proposal’s initial attempt to cover later Central Asian varieties drew criticism; the encoded repertoire was narrowed. Unicode is therefore not a neutral photograph of history but an engineered scholarly model, openly revised through proposals.

## 11. Modern pseudo-decipherments and forgeries

Brahmi itself is securely deciphered; controversy concerns particular damaged texts and datings.

Warning signs in modern claims include:

- deriving long messages from a few scratches;
- comparing glyphs without phonetic correspondences;
- dating an inscription solely from nearby charcoal;
- rotating each sign independently until it resembles a desired ancestor;
- reading modern ethnic or religious names into ambiguous fragments;
- calling an object a forgery solely because its reading is inconvenient;
- presenting a Unicode font as the exact handwriting of Aśoka.

No comprehensive, universally accepted catalogue of Brahmi forgeries exists. Absence of such a catalogue is itself a finding; individual objects must be evaluated through provenance, material analysis, excavation records, palaeography, and language.

---

# Open questions

1. What precise graphic prototype, if any, supplied the first Brahmi designer?
2. Was the design made in the northwest, Gangetic basin, Deccan, Sri Lanka, or through a network?
3. How long before Aśoka did trained Brahmi writing exist?
4. Which Anuradhapura and South Indian signs are demonstrably linguistic rather than graffiti?
5. Did the Mauryan state invent, reform, or merely monumentalize an existing script?
6. Was the inherent-vowel principle created once in Brahmi/Kharoṣṭhī interaction or independently?
7. How should “Gupta,” “Siddhamātṛkā,” and “Nāgarī” be divided when manuscripts show continua rather than clean boundaries?
8. Which specific regional Indian hand was Tibetan’s closest model?
9. How many separate transmissions carried Indic writing into Southeast Asia?
10. To what extent did palm leaf, brush, pen, and chisel independently shape regional forms?
11. How should historical glyph variants be digitally represented without multiplying characters unnecessarily?
12. Can direct dating methods for inks, accretions, or incision sequences resolve early-pottery controversies?
13. How much anonymous Indian labour underlay colonial decipherment and typography?
14. When did recognizable written Oṃ symbols first become standardized in each regional tradition?
15. Which regional Brahmi varieties remain inadequately encoded or inadequately supported by fonts?

---

# Sources

## Principal editions and specialist works

- Bühler, Georg. *On the Origin of the Indian Brāhma Alphabet*. Strassburg: Karl J. Trübner, 1898 English edition of the 1895 study.
- Bühler, Georg. *Indian Palaeography*. In *Grundriss der Indo-Arischen Philologie*, 1904. Digitized collection: https://ignca.gov.in/Asi_data/18230.pdf
- Cunningham, Alexander. *Corpus Inscriptionum Indicarum*, vol. I: *Inscriptions of Asoka*. Calcutta, 1877/1879 digitization: https://www.discoveringbuddha.org/wp-content/uploads/2026/01/1879-CII-Vol-1-Inscriptions-of-Asoka-Cunningham-1879.pdf
- Daniels, Peter T., and William Bright, eds. *The World’s Writing Systems*. Oxford University Press, 1996. Bibliographic record and preview: https://books.google.com/books/about/The_World_s_Writing_Systems.html?id=ospMAgAAQBAJ
- Falk, Harry. *Schrift im alten Indien: Ein Forschungsbericht mit Anmerkungen*. Tübingen: Gunter Narr, 1993.
- Falk, Harry. *Aśokan Sites and Artefacts: A Source-book with Bibliography*. Mainz: Philipp von Zabern, 2006.
- Hultzsch, Eugen. *Inscriptions of Asoka*. *Corpus Inscriptionum Indicarum* I, new edition. Oxford, 1925.
- Mahadevan, Iravatham. *Early Tamil Epigraphy: From the Earliest Times to the Sixth Century A.D.* Harvard Oriental Series 62. Harvard University Press, 2003.
- Prinsep, James, ed. *Journal of the Asiatic Society of Bengal*, vol. VI, 1837: https://zenodo.org/records/3361245
- Prinsep, James. “Further Elucidation of the Lát or Silasthambha Inscriptions.” 1837: https://www.biodiversitylibrary.org/part/366962
- Salomon, Richard. “Brāhmī and Kharoṣṭhī.” In Daniels and Bright, *The World’s Writing Systems*, pp. 373–383. Oxford University Press, 1996.
- Salomon, Richard. *Indian Epigraphy: A Guide to the Study of Inscriptions in Sanskrit, Prakrit, and the Other Indo-Aryan Languages*. Oxford University Press, 1998. Catalogue: https://openlibrary.org/books/OL795885M/Indian_epigraphy
- Salomon, Richard. *Indian Epigraphy*, searchable scan consulted: https://rapeutation.com/salomonindianepigraphy.pdf
- Sircar, D. C. *Indian Epigraphy*. Delhi: Motilal Banarsidass, 1965 and later editions.
- Baums, Stefan. “Writing Systems: General Historical and Analytical / Recent Script-Related Research,” 2016: https://stefanbaums.com/publications/baums_2016_1.pdf

## Archaeology, artefacts, and collections

- Asiatic Society, Kolkata, inscriptions collection and Bairat Edict: https://www.asiaticsociety.culture.gov.in/departments/museum/collections/inscriptions
- British Museum, fragment of the Meerut-Delhi Aśoka pillar, museum no. 1880.21: https://www.britishmuseum.org/collection/object/A_1880-21
- Coningham, Robin et al. “Passage to India? Anuradhapura and the Early Use of the Brahmi Script.” *Cambridge Archaeological Journal*: https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/abs/passage-to-india-anuradhapura-and-the-early-use-of-the-brahmi-script/DAAA2514FB08E1DDE3FAFF2171AB097B
- Archaeological Survey of India, historical epigraphic corpus including Girnar: https://ignca.gov.in/Asi_data/53366.pdf
- National Museum, India, Aśokan edict overview: https://www.nationalmuseumindia.gov.in/en/collections/index/21
- Sahni, D. R. *Archaeological Remains and Excavations at Bairat*: https://www.discoveringbuddha.org/wp-content/uploads/2025/02/1910-Archaeological-Remains-And-Excavations-at-Bairat-DR-Sahni-1910.pdf
- Tamil Nadu Department of Archaeology, Keeladi excavation report page: https://www.tnarch.gov.in/node/1257
- Tamil Nadu Department of Archaeology, *Keeladi: An Urban Settlement of Sangam Age on the Banks of River Vaigai*: https://www.vinavu.com/wp-content/uploads/2019/09/Keeladi-Book-English-18-09-2019.pdf
- Deraniyagala/Anuradhapura material summarized in conference proceedings: https://www.hcicolombo.gov.in/pdf/INTERNATINAL_BUDDHIST_CONFERENCE_2011_PUBLICATION.pdf

## Unicode and digital standards

- Unicode Standard 16.0, Chapter 6, writing-system classification: https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-6/
- Unicode Standard 16.0, Chapter 12, South and Central Asian scripts: https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-12/
- Unicode Standard 16.0, Chapter 14, Brahmi and numerals: https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-14/
- Unicode Standard 16.0, Chapter 15, historic South Asian scripts: https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-15/
- Unicode Standard 16.0, Chapter 16, Southeast Asian scripts: https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-16/
- Unicode 17.0 Brahmi code chart: https://www.unicode.org/charts/PDF/U11000.pdf
- Unicode 17.0 Devanagari code chart: https://www.unicode.org/charts/PDF/U0900.pdf
- Unicode Brahmi names list: https://www.unicode.org/charts/nameslist/n_11000.html
- Baums, Stefan. “Note for the UTC on the Encoding of Brahmi,” L2/02-397: https://www.unicode.org/L2/L2002/02397-baums-brahmi.pdf
- Everson, Michael, Andrew Glass, and Stefan Baums. “Progressing the Encoding of Brahmi in the SMP,” L2/08-277R: https://www.unicode.org/L2/L2008/08277r-n3490r-brahmi.pdf
- Unicode Technical Committee document register, Brahmi proposal history: https://unicode.org/L2/L2007/07344.htm

## Script history, religion, and transmission

- van Schaik, Sam. “A New Look at the Tibetan Invention of Writing”: https://earlytibet.com/wp-content/uploads/2007/06/vanschaik_2011a.pdf
- Bibliothèque nationale de France, “Languages and Scripts” in France–South Asia shared heritage: https://heritage.bnf.fr/france-southasia/en/languages-scripts-article
- *Cambodian System of Writing and Beginning Reader*, historical introduction: https://en.wikisource.org/wiki/Page%3ACambodian_system_of_writing_and_beginning_reader.pdf/9
- University of Vienna, “Inscribing the Sacred Syllable: Towards a History of OM as a Written Sign and Icon”: https://stb.univie.ac.at/news-events/detail/news/inscribing-the-sacred-syllable-towards-a-history-of-om-as-a-written-sign-and-icon/
- *Mahānirvāṇa Tantra*, chapter 5, translated ritual treatment of the alphabet goddess: https://sacred-texts.com/tantra/maha/maha05.htm
- “Selecting and Perfecting Mantras in Hindu Tantrism,” *Bulletin of the School of Oriental and African Studies*: https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/abs/selecting-and-perfecting-mantras-in-hindu-tantrism/7122857D5602C55F933838D1AA6E9CF2
- Kavaleuskaya, “Extraction of Mantras”: https://etnografia.kunstkamera.ru/en/archive/2020_issue_4_10/kavaleuskaya_a_extraction_of_mantras
- Tom Egenes, discussion of Brahmi transfer and Indian phonetic order in *Studies in the Linguistic Sciences*: https://libsysdigi.library.illinois.edu/OCA/Books2008-11/studiesinlinguis/studiesinlinguis302000univ/studiesinlinguis302000univ.pdf

## Typography and modern standardization

- Ross, Fiona, and Graham Shaw. “Invisible Hands: Tracing the Origins and Development of the Linotype Devanagari Digital Fonts”: https://centaur.reading.ac.uk/101230/
- Ross, Fiona. *The Evolution of the Printed Bengali Character from 1778 to 1978*: https://soas-repository.worktribe.com/output/403271/the-evolution-of-the-printed-bengali-character-from-1778-to-1978
- Ross, Fiona. “The Machine in the Colony: Technology, Politics, and the Typography of Devanagari”: https://centaur.reading.ac.uk/75684/
- Afshar, Sahar. *Gurmukhi Printing Types: An Historical Analysis of British Design, Development, and Distribution in the Nineteenth and Twentieth Centuries*. PhD thesis, Birmingham City University, 2023: https://www.open-access.bcu.ac.uk/14181/
- Letterform Archive, Gujarati Type Foundry 1937 specimen: https://letterformarchive.org/news/gujarati-type-foundry-specimen/
- Government of India, Official Language rules: https://www.rajbhasha.gov.in/sites/default/files/Niyam_Pustak_upto_July23.pdf
- Central Hindi Directorate, Devanagari and Hindi orthographic standardization history: https://www.chd.education.gov.in/devanagari-lipi-tatha-hindi-vartani-manakikaran

## Contested-material and comparative checks

- Witzel, Michael, discussion of the absence of demonstrated Indus-to-Brahmi continuity: https://hasp.ub.uni-heidelberg.de/journals/ejvs/article/download/830/808/1652
- Pillai, “The Hybrid Origin of Brāhmī Script from Aramaic, Phoenician and Greek Letters”: https://revistes.uab.cat/indialogs/article/view/v10-pillai
- Government excavation position on early Tamil-Brahmi/Tamili: https://www.tnarch.gov.in/node/1257
- Critical journalistic report quoting Harry Falk’s objections to the Porunthal reading and Keeladi dating inference: https://thefederal.com/the-eighth-column/keeladi-excavation-raises-more-questions-than-answers
- Marathi encyclopaedia entry preserving Indian historiography and Brahmā-origin legend, with English summary used here: https://vishwakosh.marathi.gov.in/29860/
- French overview consulted for terminology: https://fr.wikipedia.org/wiki/Brahmi
- Spanish overview consulted for bibliographic cross-checking: https://es.wikipedia.org/wiki/Brahmi
