# The Arabic alphabet: Research Dossier

## Method and evidentiary labels

This dossier distinguishes six kinds of claim:

- **[Artefact]**: supported by a surviving inscription, manuscript, coin, papyrus, or other object.
- **[Documented text]**: stated in a named premodern textual source.
- **[Scholarly reconstruction]**: the prevailing inference from comparative palaeography, linguistics, or historical context.
- **[Disputed]**: materially contested in current scholarship.
- **[Tradition]**: transmitted by historical communities but not independently demonstrated.
- **[Legend]**: supernatural, heroic, or etiological narrative.
- **[Modern invention]**: a recent convention, reform, revival, or retrospective interpretation.

Dates are CE unless otherwise stated. “Arabic alphabet” here means the 28-letter system used for Arabic; “Arabic script” includes its enlarged Persian, Urdu, Ottoman, African, and Southeast Asian descendants.

---

## Basic identification

| Field | Identification |
|---|---|
| Name | Arabic alphabet; Arabic **الأَبْجَدِيَّة العَرَبِيَّة** *al-abjadiyya al-ʿarabiyya* or **الحُرُوف العَرَبِيَّة** *al-ḥurūf al-ʿarabiyya* |
| Type | Principally an **abjad**: consonants have independent letters; long vowels generally use consonant letters as *matres lectionis*; short vowels are normally omitted but can be supplied with combining marks. Fully vocalized Arabic functions more nearly as an alphabet. |
| Core inventory | 28 consonant letters; hamza is an additional consonantal sign with special orthographic behavior. Tāʾ marbūṭa, alif maqṣūra, and alif waṣla are contextual or orthographic characters rather than additional basic alphabet letters. |
| Direction | Right to left. Numbers embedded in Arabic text conventionally display their highest place value on the left, producing mixed directional behavior governed digitally by the Unicode Bidirectional Algorithm. |
| Letter forms | Contextual joining: most letters have isolated, initial, medial, and final glyphs; six core letters—ا د ذ ر ز و—do not join to a following letter on their left. |
| Case | No capitals or lowercase. Emphasis is achieved through scale, spacing, color, ornament, calligraphic style, or modern typographic weight. |
| Earliest developmental period | Nabataean-to-Arabic transition, approximately the second–fifth centuries; recognizably Arabic monumental writing by the fifth–sixth centuries. |
| Securely dated pre-Islamic milestones | Namāra, 328, in late Nabataean; Zabad, 512, with Paleo-Arabic names; Jabal Usays, 528/529; Ḥarrān, 568. |
| Primary region | Northern Arabia, the southern Levant, and adjoining Syrian desert during formation; after the seventh-century conquests, from Iberia and West Africa to Central, South, and Southeast Asia. |
| Parent | **[Scholarly reconstruction]** Imperial Aramaic → Nabataean Aramaic → late Nabataean/Nabataeo-Arabic → Arabic. Nabataean descent is the dominant modern conclusion; Syriac contact or subsidiary influence remains possible, but direct Syriac descent is a minority position. |
| More remote ancestry | Aramaic ultimately belongs to the Northwest Semitic alphabetic line conventionally traced through Phoenician/Canaanite to the early consonantal alphabet. |
| Daughters and major adaptations | Persian, Urdu, Ottoman Turkish, Kurdish Sorani, Pashto, Sindhi, Kashmiri, Punjabi Shahmukhi, Uyghur, Jawi Malay, Pegon, Swahili and West African *ʿAjamī*, among many others. |
| Present status | Official or dominant for Arabic and several non-Arabic languages; liturgical worldwide through the Qurʾān. Unicode and complex-text shaping permit digital composition, though high calligraphic fidelity remains technically demanding. |

---

# The script in detail

## 1. Structural character

**[Scholarly classification]** Peter T. Daniels coined “abjad” as a technical category for systems in which consonants are primary and vowels secondary or optional. Arabic is the exemplary mature abjad. Calling it simply an “alphabet” is nevertheless normal outside that narrow typological usage.

The consonantal skeleton is called **rasm**. Three devices supplement it:

1. **Matres lectionis**: ا *alif*, و *wāw*, and ي *yāʾ* can indicate long /ā/, /ū/, and /ī/, besides their consonantal or other functions.
2. **Iʿjām**: dots that distinguish consonants sharing a skeleton, such as ب ت ث, ج ح خ, and د ذ.
3. **Tashkīl** or **ḥarakāt**: optional vowel and recitational marks.

Unlike Greek, Arabic did not systematically convert otherwise unnecessary consonant letters into mandatory independent vowels. The Greek innovation—repurposing Phoenician consonants such as ʾālep and hē for vowels—therefore has no equivalent borrowing event in Arabic. Arabic instead continued the Semitic strategy of consonantal writing plus matres and later vocalization.

## 2. The 28 letters

Pronunciations below give Classical Arabic/Modern Standard Arabic values. Regional vernacular values can differ substantially: ج may be /g/ in Egypt or /ʒ/ in parts of the Levant and North Africa; ق may be /q/, /g/, /ʔ/, or another realization.

The numerical column uses the common eastern **abjad al-kabīr** order. Persian additions ordinarily lack classical abjad values. Unicode code points refer to abstract characters, not contextual glyph forms.

| Hijāʾī no. | Letter | Name | Unicode | Standard value | Abjad value | Remote Semitic name/meaning |
|---:|:---:|---|---|---|---:|---|
| 1 | ا | *alif* | U+0627 | /ā/; carrier; historical /ʔ/ represented with hamza | 1 | ʾalp, “ox” |
| 2 | ب | *bāʾ* | U+0628 | /b/ | 2 | bayt, “house” |
| 3 | ت | *tāʾ* | U+062A | /t/ | 400 | taw, probably “mark/sign” |
| 4 | ث | *thāʾ* | U+062B | /θ/ | 500 | Arabic secondary differentiation; name formed from the sound, not an inherited pictorial meaning |
| 5 | ج | *jīm* | U+062C | Classical /d͡ʒ/ | 3 | gaml, “camel” |
| 6 | ح | *ḥāʾ* | U+062D | /ħ/ | 8 | ḥēt; remote meaning uncertain, often “fence” |
| 7 | خ | *khāʾ* | U+062E | /x/ | 600 | Arabic secondary differentiation |
| 8 | د | *dāl* | U+062F | /d/ | 4 | dalt, “door” |
| 9 | ذ | *dhāl* | U+0630 | /ð/ | 700 | Arabic secondary differentiation |
| 10 | ر | *rāʾ* | U+0631 | /r/ | 200 | rōʾš, “head” |
| 11 | ز | *zāy* | U+0632 | /z/ | 7 | zayn; meaning disputed, often “weapon” |
| 12 | س | *sīn* | U+0633 | /s/ | 60 | šinn, “tooth,” after Semitic sound/order changes |
| 13 | ش | *shīn* | U+0634 | /ʃ/ | 300 | šinn, “tooth” |
| 14 | ص | *ṣād* | U+0635 | /sˤ/ | 90 | ṣādē; meaning uncertain |
| 15 | ض | *ḍād* | U+0636 | Classical emphatic lateral/fricative, conventionally /dˤ/ in MSA | 800 | Arabic secondary differentiation |
| 16 | ط | *ṭāʾ* | U+0637 | /tˤ/ | 9 | ṭēt; meaning uncertain |
| 17 | ظ | *ẓāʾ* | U+0638 | /ðˤ/, often /zˤ/ | 900 | Arabic secondary differentiation |
| 18 | ع | *ʿayn* | U+0639 | /ʕ/ | 70 | ʿayn, “eye” |
| 19 | غ | *ghayn* | U+063A | /ɣ/ | 1000 | Arabic differentiation; name related to a Semitic root involving cloud/darkness is sometimes proposed |
| 20 | ف | *fāʾ* | U+0641 | /f/ | 80 | pē, “mouth” |
| 21 | ق | *qāf* | U+0642 | /q/ | 100 | qōp; meaning disputed, proposals include “monkey” or “needle eye” |
| 22 | ك | *kāf* | U+0643 | /k/ | 20 | kap, “palm of hand” |
| 23 | ل | *lām* | U+0644 | /l/ | 30 | lāmed, “goad” |
| 24 | م | *mīm* | U+0645 | /m/ | 40 | maym, “water” |
| 25 | ن | *nūn* | U+0646 | /n/ | 50 | nūn, probably “fish” |
| 26 | ه | *hāʾ* | U+0647 | /h/ | 5 | hē; reconstructed meaning uncertain, sometimes “window” or “jubilation” |
| 27 | و | *wāw* | U+0648 | /w/; long /ū/ | 6 | waw, “hook/peg” |
| 28 | ي | *yāʾ* | U+064A | /j/; long /ī/ | 10 | yad, “hand” |

### Qualifications concerning the “meanings”

**[Scholarly reconstruction]** “Ox, house, door, hand,” and similar glosses belong to reconstructed Northwest Semitic letter names and the acrophonic history of the early alphabet, not to a demonstrated Arabic pictorial stage. Arabic speakers did not invent ب by drawing a house.

**[Reconstruction]** In the acrophonic principle, a picture or sign named by a word supplied its initial consonant: a sign called *bayt*, “house,” represented /b/. By the time of Aramaic, Nabataean, and Arabic, the signs were highly abstract and most names functioned simply as letter names.

**[Disputed details]** Several ancient meanings—especially zayin, ṭēt, ṣādē, qōp, and hē—remain uncertain. Popular charts that present every gloss as settled history overstate the evidence.

## 3. Two orders

### Abjad order

The inherited Semitic sequence survives in the mnemonic:

**أبجد هوز حطي كلمن سعفص قرشت ثخذ ضظغ**

Eastern order:

**ʾ b j d h w z ḥ ṭ y k l m n s ʿ f ṣ q r sh t th kh dh ḍ ẓ gh**

This preserves the old 22-letter order through *tāʾ*, followed by the six specifically Arabic phonemic differentiations. A western Maghribi numerical ordering places the final letters differently and consequently assigns different high values.

### Hijāʾī order

**[Historical reform, exact date uncertain]** The modern teaching/dictionary order groups letters by graphic skeleton and dot pattern:

**ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي**

It could only arise after differentiated dotted letter identities had become established. Medieval sources associate orthographic work with Naṣr ibn ʿĀṣim and Yaḥyā ibn Yaʿmar under al-Ḥajjāj, but surviving manuscripts show development rather than a single decree.

## 4. Joining and contextual forms

Arabic is cursive in both handwriting and ordinary print. Unicode assigns one principal character code to each letter; shaping software selects its glyph:

| Joining class | Core examples | Available forms |
|---|---|---|
| Dual joining | ب ت ث ج ح خ س ش ص ض ط ظ ع غ ف ق ك ل م ن ه ي | isolated, initial, medial, final |
| Right joining only | ا د ذ ر ز و | isolated and final; breaks the connection to the next letter |
| Nonjoining/sign behavior | ء and most vowel marks | does not form the ordinary cursive connection |

This is not a capital/minuscule distinction. “Kufic” and “naskh” are script styles, not uppercase and lowercase.

## 5. Hamza and alif

Hamza **ء** (U+0621) records the glottal stop /ʔ/. Depending on phonology and orthographic rules it may stand alone or sit on/under a “seat”:

- أ, إ: hamza with alif;
- ؤ: with wāw;
- ئ: with yāʾ-shaped seat;
- ء: on the line.

Alif often records long /ā/, but word-initial vowels require an alif carrier and, in fully marked writing, hamza or **ٱ** *alif waṣla*. Thus alif is not a simple one-sound/one-letter equivalent.

Other special forms include:

- **ى** *alif maqṣūra*: word-final /ā/, shaped like dotless yāʾ.
- **ة** *tāʾ marbūṭa*: commonly /a/ or /ah/ in pause and /at/ in construct pronunciation.
- **ـ** *taṭwīl/kashīda*: an elongation character used for joining or justification, not a letter.
- **ﻻ / لا** *lām–alif*: the mandatory conventional ligature of lām followed by alif.

## 6. Vowels and recitation signs

| Sign | Name | Unicode | Function |
|:---:|---|---|---|
| َ | *fatḥa* | U+064E | short /a/ |
| ِ | *kasra* | U+0650 | short /i/ |
| ُ | *ḍamma* | U+064F | short /u/ |
| ْ | *sukūn* | U+0652 | absence of a vowel |
| ّ | *shadda* | U+0651 | consonant gemination |
| ً | *fatḥatān* | U+064B | /an/ |
| ٍ | *kasratān* | U+064D | /in/ |
| ٌ | *ḍammatān* | U+064C | /un/ |
| ٰ | superscript alif | U+0670 | historical/orthographic long /ā/ |
| ٓ | *madda* | U+0653 | lengthening/hamza-related orthography |
| ٔ / ٕ | combining hamza | U+0654/U+0655 | hamza above/below |

Ordinary Arabic prose is normally unvocalized. Children’s books, dictionaries, primers, poetry when ambiguity matters, and Qurʾānic editions use more extensive marking. Qurʾānic writing also employs pause, elongation, and recitational signs beyond everyday *tashkīl*.

**[Artefact]** Early Qurʾānic manuscripts can have sparse consonantal dots; some later manuscripts use colored dots for vowels and separate strokes or dots for consonantal distinction.

**[Tradition]** Abū al-Aswad al-Duʾalī (d. c. 688) is credited with red-dot vocalization, supposedly at the request of Ziyād ibn Abīhi after hearing erroneous Arabic.

**[Tradition]** Naṣr ibn ʿĀṣim and Yaḥyā ibn Yaʿmar are credited with systematic consonantal differentiation under al-Ḥajjāj ibn Yūsuf (governor 694–714).

**[Documented later attribution]** The earliest surviving author known to credit Abū al-Aswad with founding grammar is Ibn Sallām al-Jumaḥī (d. 845), substantially later than Abū al-Aswad himself.

**[Scholarly conclusion]** These reports probably preserve memories of standardization, not literal invention from nothing: pre-Islamic and first-century AH objects already contain occasional dots.

**[Documented text/tradition]** Al-Khalīl ibn Aḥmad al-Farāhīdī (d. c. 786/791) is credited with the mature stroke-shaped vowel signs, shadda, and hamza conventions that replaced ambiguous colored-dot systems.

## 7. Punctuation

Classical manuscripts used spacing, verse dividers, rosettes, colored dots, marginal signs, and chapter headings rather than a single modern punctuation system. Modern punctuation was substantially regularized under the influence of European printing and translation:

- **،** Arabic comma, U+060C;
- **؛** semicolon, U+061B;
- **؟** question mark, U+061F;
- full stop, colon, parentheses, quotation marks, and Arabic-script-specific signs.

The orientation of comma and question mark reflects right-to-left typography. Punctuation practice still varies across Arabic, Persian, Urdu, and other traditions.

---

# Origins: dated and placed

## 1. Remote ancestry

**[Scholarly reconstruction]**

A defensible stemma is:

**Early Northwest Semitic consonantal alphabet → Phoenician/Canaanite → Aramaic → Nabataean Aramaic → transitional Nabataeo-Arabic → Arabic**

This is not a single recorded “borrowing event.” It was a long transformation of scribal practice. Nabataean was a 22-letter Aramaic script used from the late first millennium BCE in Petra, the Ḥawrān, Sinai, the Negev, and northwestern Arabia. Its cursive ligaturing created letter shapes increasingly close to Arabic.

Arabic possessed more consonantal phonemes than the inherited Aramaic inventory could unambiguously represent. Several sounds therefore shared the same base form. Iʿjām eventually differentiated them, allowing 28 functional consonant letters to arise from fewer skeletons.

## 2. Why Nabataean rather than Syriac?

**[Prevailing reconstruction]** Letter-by-letter palaeographic development through dated Nabataean inscriptions is sufficiently continuous that John Healey characterized Nabataean ancestry as almost universally accepted. Beatrice Gruendler’s comparative study systematically traces the transition.

**[Minority/disputed reconstruction]** Earlier scholars and some Arabic traditions connected Arabic script with Syriac centers such as al-Ḥīra. Syriac and Arabic share general Aramaic features and inhabited overlapping scribal environments.

**Evidence assessment:** Syriac contact is historically plausible, but the shapes and intermediate inscriptions favor Nabataean as the principal graphic ancestor. A once-common theory dividing “Kufic from Syriac” and “naskh from Nabataean” is not accepted as a literal bifurcated ancestry by most current palaeographers.

## 3. Key inscriptions

### Namāra inscription, 7 December 328

- **Object:** basalt funerary inscription of Imruʾ al-Qays ibn ʿAmr.
- **Findspot:** al-Namāra in the basalt desert south of Damascus, now Syria.
- **Present location:** Louvre, Paris.
- **Inventory:** commonly cited as **AO 4083**.
- **Discovery/publication:** found by René Dussaud and Frédéric Macler in 1901; Dussaud published the first major reading in 1905.
- **Date:** 7 Kislev, year 223 of the Bostra/Nabataean era = 7 December 328.
- **Language/script:** Arabic-dominant language in a late Nabataean script.
- **Status:** **[Artefact]** secure date; **[Scholarly classification]** pivotal Nabataeo-Arabic rather than a fully developed dotted Arabic alphabet.
- **Dispute:** James Bellamy proposed a substantially revised reading in 1985; individual words and the king’s titles remain debated. Its importance does not depend on accepting every reconstruction.

The inscription is often called “the oldest Arabic inscription.” That is imprecise: older Arabic-language material occurs in other scripts, while Namāra is not yet ordinary Islamic-period Arabic script.

### Raqush inscription, 267

**[Artefact]** A funerary text from Madāʾin Ṣāliḥ/Hegra, written in Nabataean and displaying Arabic linguistic features. It is sometimes advertised as the “first Arabic inscription,” but that label conflates language, script, and developmental stage. It is better evidence for the transition’s depth than a fixed birthday for Arabic writing.

### ʿEn ʿAvdat, approximately 88–150

**[Artefact; disputed interpretation]** A Nabataean inscription containing lines interpreted as Arabic verse. Its identification as poetic Old Arabic is influential but not identical with evidence for a separate Arabic alphabet.

### Zabad, 512

- **Object:** dark basalt lintel in three pieces, approximately 3.05 m long, from the martyrion of St Sergius.
- **Findspot:** Zabad/Zebed, southeast of Aleppo, Syria.
- **Present location:** Royal Museums of Art and History, Brussels.
- **Inventory:** **A 1308**.
- **Discovery/history:** reported by Johann Gottfried Wetzstein; copied/published by Eduard Sachau after work at the site in 1879; moved to Brussels through Henri Lammens in the early twentieth century.
- **Date:** Greek and Syriac sections give Seleucid year 823 = 512.
- **Languages:** Greek, Syriac, and a short Arabic sequence of personal names.
- **Status:** **[Artefact]** major securely associated early Paleo-Arabic example.
- **Dispute:** It is not strictly a translation repeated in three languages. Earlier scholars argued that the Arabic names could be a later graffito. Current opinion generally considers all parts contemporary, but Michael C. A. Macdonald cautions that the Arabic portion’s sharing of the 512 date is probable, not absolutely demonstrable.

### Jabal Usays, 528/529

**[Artefact]** An Arabic graffito in southern Syria dated year 423 of the Bostra era, naming Ruqaym son of Maʿarrif al-Awsī and referring to being sent by “al-Ḥārith the king.” It was discovered and published by Muḥammad Abū al-Faraj al-ʿUsh in 1964.

Because its Arabic text carries its own date and is in recognizably Arabic script, Pierre Larcher has described it as the oldest perfectly dated inscription that is simultaneously Arabic in language and script. This is a more precise claim than assigning that title to Zabad.

### Ḥarrān/Umm al-Jimāl area, 568

**[Artefact]** A Greek-Arabic Christian dedicatory inscription conventionally dated 568. It is another securely dated waypoint toward the early Islamic hand.

### Dūmat al-Jandal and other sixth-century material

Recent surveys of Paleo-Arabic inscriptions in northwestern Arabia and the northern Ḥijāz have weakened the old picture of an alphabet imported suddenly from Syrian cities just before Islam. They instead suggest sustained local use and multiple scribal networks.

**[Open archaeological finding]** The corpus remains small and discoveries continue; statements such as “the first Arabic inscription” are therefore unusually vulnerable to revision.

---

# The rise of Islamic Arabic writing

## 1. Muḥammad’s lifetime and the first caliphates

**[Documented text]** The Qurʾān itself refers repeatedly to writing, pens, sheets, contracts, and written scripture. Early Islamic narrative sources name secretaries and describe written revelations and treaties.

**[Historical caution]** Most detailed biographies and collection narratives survive in sources compiled generations later. They demonstrate an early Muslim memory of writing but cannot, alone, reconstruct each manuscript act.

**[Artefact]** Seventh-century papyri, inscriptions, and coins show Arabic entering government, taxation, commemoration, and religious proclamation.

Important dated landmarks include:

- **22 AH/643:** Greek-Arabic papyrus PERF 558, a bilingual receipt, among the earliest dated Arabic documentary papyri.
- **24 AH/644–645:** Zuhayr inscription, an early dated Islamic rock inscription mentioning the death of Caliph ʿUmar.
- **72 AH/691–692:** Arabic inscriptions of the Dome of the Rock, Jerusalem—monumental Qurʾānic and confessional statements under ʿAbd al-Malik.
- **Late seventh century:** Arabization of imperial administration and coinage under ʿAbd al-Malik, making Arabic script a principal medium of state.

## 2. The Qurʾānic manuscripts

### Birmingham folios

- **Repository:** University of Birmingham, Cadbury Research Library.
- **Shelfmark:** Mingana Islamic Arabic **1572a**.
- **Contents:** parts of suras 18–20.
- **Script:** early Ḥijāzī.
- **Radiocarbon result:** parchment dated **568–645 at 95.4% probability**.
- **Status:** **[Artefact/scientific measurement]** the animal died within that modeled interval.
- **Caution:** radiocarbon dates parchment, not the ink or act of writing. Palaeography and codicology are needed to date inscription. The leaves belong with BnF Arabe 328c in the larger codex commonly called the *Codex Parisino-petropolitanus*.

### Ṣanʿāʾ manuscript cache and palimpsest

- **Discovery:** manuscript material found during restoration of the Great Mosque of Ṣanʿāʾ in 1972.
- **Object:** thousands of Qurʾānic fragments; the best-known palimpsest has an erased lower Qurʾānic text and a later upper text.
- **Repository designation:** portions include Dār al-Makhṭūṭāt DAM 01-27.1.
- **Status:** **[Artefact]** evidence of early Qurʾānic copying, correction, reuse, orthographic variation, and a lower text with readings not identical to the standard consonantal text.
- **Dispute:** It is evidence of early textual plurality, but claims that it single-handedly proves a radically late creation of the Qurʾān go beyond the manuscript evidence. Dating depends on multiple leaves, radiocarbon ranges, script, and textual analysis.

### What early manuscripts show about dots

**[Artefact]** First-century AH Ḥijāzī manuscripts contain some consonantal dots, but not enough to eliminate every ambiguity. This contradicts the simple popular assertion that “the Qurʾān originally had no dots at all.”

**[Scholarly reconstruction]** Dotting and vocalization were techniques already available in regional scribal cultures and became more systematic as Arabic acquired imperial, educational, and liturgical functions.

**[Tradition versus artefact]** Reports assigning invention to one grammarian should therefore be understood as founder traditions or memories of reform.

---

# Spread and change

## 1. Early book hands: Ḥijāzī and “Kufic”

**Ḥijāzī** is a modern palaeographic umbrella for sloping, relatively informal early Qurʾānic hands. It should not be imagined as one standardized font.

“Kufic” traditionally connects angular Qurʾānic scripts with Kufa. Modern manuscript scholarship uses more specific categories because many so-called Kufic codices cannot be proven to have been copied there.

**[Tradition]** Medieval sources associate monumental angular scripts with Kufa.

**[Scholarly qualification]** “Kufic” is useful as a broad art-historical label but can conceal numerous regional and chronological hands.

Angular scripts dominated many early Qurʾāns and monuments. They encouraged horizontal extension, controlled geometry, and ornamental treatment. Floral, foliated, plaited, and “eastern Kufic” forms later appeared in architecture, ceramics, textiles, coins, and manuscripts.

## 2. Cursive book and chancery scripts

Cursive writing existed from the beginning; naskh did not suddenly replace a purely angular original alphabet. What changed was the prestige and codification of cursive book hands.

### Ibn Muqla

Abū ʿAlī Muḥammad ibn ʿAlī Ibn Muqla (886–940), Abbasid vizier and calligrapher, is credited with establishing **al-khaṭṭ al-mansūb**, proportioned writing.

His system related letters to:

- the rhomboid dot made by the cut reed pen;
- alif height;
- a proportional circle.

**[Tradition with textual support]** Later calligraphic histories attribute the canon of six pens to him. The extent to which he personally “invented” each style cannot be verified from securely autographic manuscripts.

The six canonical pens were:

- naskh;
- thuluth;
- muḥaqqaq;
- rayḥān;
- tawqīʿ;
- riqāʿ.

### Ibn al-Bawwāb

ʿAlī ibn Hilāl Ibn al-Bawwāb (d. 1022) refined the proportional system and is associated particularly with elegant naskh and rayḥān.

**[Artefact/attribution caution]** A Qurʾān dated 391 AH/1000–1001 in the Chester Beatty Library is conventionally accepted as the only surviving Qurʾān signed by him, though attribution practices always require codicological scrutiny.

### Yāqūt al-Mustaʿṣimī

Yāqūt (d. c. 1298), secretary and calligrapher at late Abbasid Baghdad, became the third member of the canonical lineage Ibn Muqla → Ibn al-Bawwāb → Yāqūt. Tradition credits him with refining the pen’s oblique cut and the six scripts.

### Major styles

- **Naskh:** rounded, readable book hand; eventually central to Qurʾān and ordinary Arabic printing.
- **Thuluth:** large, sweeping, complex, often architectural and titular.
- **Muḥaqqaq:** stately, broad script favored in large Qurʾāns.
- **Rayḥān:** finer counterpart to muḥaqqaq.
- **Tawqīʿ and riqāʿ:** chancery and smaller documentary hands.
- **Maghribī:** family of western Islamic scripts used from North Africa to al-Andalus, with distinct letter and dot conventions.
- **Nastaʿlīq:** developed in Persianate contexts by the fourteenth–fifteenth centuries, conventionally explained as combining naskh and taʿlīq. It became the pre-eminent Persian and Urdu literary hand.
- **Shikasta nastaʿlīq:** more rapid Persian chancery/epistolary form.
- **Dīwānī:** Ottoman court script, elaborated in the imperial chancery.
- **Ruqʿa:** compact modern handwriting, especially associated with Ottoman reforms and everyday writing.

**[Popular legend]** Nastaʿlīq’s strokes are sometimes said to reproduce trees, hills, meadows, music, human bodies, or birds in flight. Iranica records this as a popular aesthetic belief, not a historical account of invention.

## 3. Persian

New Persian adopted Arabic script after the Islamic conquest and the decline of Middle Persian administrative scripts. Persian added:

| Letter | Value |
|:---:|---|
| پ | /p/ |
| چ | /t͡ʃ/ |
| ژ | /ʒ/ |
| گ | /g/ |

These additions generally have no classical abjad numerical values. Persian also reshaped usage: ك/ک and ي/ی have distinct Arabic/Persian Unicode characters and conventions, a continuing source of search, sorting, and normalization problems.

## 4. Urdu and South Asia

Urdu writing developed through Persianate literary and administrative culture in South Asia. Its enlarged inventory represents aspirates, retroflexes, and other Indo-Aryan contrasts. Nastaʿlīq became culturally normative.

The diagonally cascading, context-sensitive nature of nastaʿlīq made metal type and early digital typography especially difficult. Lithography flourished partly because it could reproduce a calligrapher’s page directly.

Arabic-derived scripts also remain important for Sindhi, Pashto, Kashmiri, Balochi, and Shahmukhi Punjabi, each adding or reallocating dots and marks.

## 5. Ottoman Turkish and the 1928 reform

Ottoman Turkish used an Arabic-derived alphabet with Persian additions. It represented Arabic and Persian loan vocabulary effectively but mapped Turkish vowels and some consonants ambiguously.

**[Documented law]** Turkey’s Law No. 1353, adopted 1 November and published/entered into force 3 November 1928, replaced the Arabic letters used for Turkish with a Latin-based “Turkish alphabet.” State implementation proceeded rapidly into 1929.

Mustafa Kemal Atatürk publicly championed the reform; a language commission prepared the alphabet and primers.

**[Disputed interpretation]**

- Reformist accounts emphasize literacy, phonological fit, printing, modernization, and integration with Europe.
- Critical accounts emphasize rupture with Ottoman documentary memory, coercive state nation-building, secularization, and a sudden generational barrier.
- The law itself documents replacement and deadlines; it does not resolve competing judgments about motive or social effect.

Arabic script continues in Ottoman studies, religious contexts, archives, and some private or revivalist use, but not as the ordinary official script of Turkish.

## 6. Malay and Southeast Asia

Arabic-derived **Jawi** spread with Islam, trade, sultanates, and manuscript culture. Its earliest securely dated history is debated because inscriptions may mix Arabic, Malay, Sanskritic vocabulary, and uncertain calendrical readings. The Terengganu Inscription Stone is generally dated to the early fourteenth century and is a major early Malay-Jawi legal/religious monument.

Jawi added letters for Malay sounds, including forms for /p/, /g/, /ŋ/, /t͡ʃ/, and /ɲ/. It served law codes, chronicles, letters, religious teaching, seals, and court literature.

Latin Rumi script became dominant under colonial administration and postcolonial schooling, but Jawi remains co-official or institutionally protected in Brunei and has religious and cultural roles in Malaysia, southern Thailand, Indonesia, and Singapore.

Pegon and related traditions adapted Arabic script to Javanese, Sundanese, and other languages.

## 7. Swahili and African ʿAjamī

Arabic script reached the Swahili coast with Indian Ocean Islam and commerce. Early Swahili poetry and religious literature circulated in Arabic-derived spelling.

**[Scholarly finding]** There was no single ancient standardized “Swahili alphabet.” Scribes used Arabic conventions and gradually experimented with Swahili-specific consonants and vowel representation. Mwalimu Sikujua of Mombasa is associated with a systematic nineteenth-century adaptation.

Across West Africa, **ʿAjamī** traditions wrote Hausa, Fulfulde, Wolof, Mandinka, Kanuri, and other languages. Manuscripts include theology, law, healing, history, poetry, commercial records, and correspondence. Colonial scholarship often underestimated them because it equated literacy with European-language or Latin-script literacy.

## 8. Central Asia and other replacements

Arabic-derived scripts were historically used for Chagatai, Uzbek, Kazakh, Kyrgyz, Turkmen, Azerbaijani, Crimean Tatar, and other languages. Soviet policies shifted many first to Latin and then Cyrillic. Iran and Afghanistan retained Arabic-derived systems for several languages; the People’s Republic of China maintains an Arabic-derived official Uyghur script, while diaspora practices vary.

Script replacement was seldom a purely technical matter. It commonly accompanied changes in religion, empire, nationalism, schooling, printing infrastructure, or geopolitical alignment.

---

# Calligraphy and sacred art

## 1. Religious status

**[Documented religious culture]** Qurʾānic copying gave writing exceptional prestige. Calligraphy adorned mosques, Qurʾāns, textiles, ceramics, metalwork, weapons, seals, and architecture.

The phrase “calligraphy is the sacred art of Islam” is a useful art-historical description but not a universal theological doctrine. It should not be reduced to the old claim that Islam simply “forbade images”: figural art existed extensively in secular, courtly, scientific, and even some religious contexts.

Respect for divine names affects placement. Metropolitan Museum scholarship notes that inscriptions were generally avoided on surfaces liable to be trodden or sat upon when they might contain God’s name.

## 2. Tools and transmission

The traditional instrument is the cut reed pen, **qalam**, with carbon or gall ink on papyrus, parchment, paper, ceramic, plaster, stone, wood, glass, metal, or textile. Training relies on copying a master’s models and receiving an **ijāza**, a certificate of competence in a specific hand.

Paper technology spreading westward through the Islamic world from the eighth century greatly expanded bureaucratic and book production. Baghdad, Cairo, Damascus, Shiraz, Herat, Samarqand, Istanbul, Fez, and other centers developed distinct traditions.

## 3. Ottoman masters

Şeyh Hamdullah (1436–1520) reshaped Ottoman naskh and thuluth. Hâfız Osman (1642–1698) further refined them and became a foundational model for Qurʾān copying. Mustafa Râkım (1757–1826) transformed celî thuluth and the imperial tughra. Their practice demonstrates that the canon was continuously reinterpreted rather than frozen in Ibn Muqla’s age.

---

# Printing and typography

## 1. Early European Arabic type

Arabic presented severe problems for movable type: contextual joining, many potential ligatures, stacked dots and vowels, baseline variation, and calligraphic expectations.

- **1514:** Gregorio de Gregorii printed the Arabic *Kitāb Ṣalāt al-Sawāʿī*, a Christian Book of Hours—generally treated as the first book printed entirely with Arabic movable type.
- **Sixteenth century:** Guillaume Le Bé and Robert Granjon designed Arabic types in Europe.
- **1580s:** Granjon cut types for the Medici Oriental Press established under Cardinal Ferdinando de’ Medici; its books aimed at eastern Christian and scholarly markets.

**[Documented correction to a common myth]** Napoleon’s Egyptian expedition did not introduce Arabic printing itself. It brought presses in 1798 and used them for occupation publications, but Arabic books had been printed centuries earlier.

## 2. Printing in Muslim polities

Printing’s slower adoption had technological, economic, scribal, political, and religious causes; blanket claims that Islam “banned printing” are inadequate.

Ibrahim Müteferrika, a Hungarian-born Ottoman convert, received authorization and operated an Ottoman Turkish press from 1727. Restrictions and manuscript competition persisted, particularly around Qurʾānic reproduction.

## 3. Būlāq

Muḥammad ʿAlī founded Egypt’s Būlāq/Amiri Press in 1820; it became operational in 1821–1822. Niqūlā al-Masābikī trained in Milan in printing and type founding. The press issued military, scientific, administrative, linguistic, and literary works and became central to the nineteenth-century Arabic print sphere.

Mirzā Sanglākh designed or supervised improved naskh and nastaʿlīq types. Būlāq’s typographic standards influenced Arabic book design far beyond Egypt.

Lithography remained especially successful for Persian and Urdu because it reproduced flowing nastaʿlīq without decomposing it into rigid metal sorts.

## 4. Modern designers and systems

Twentieth-century mechanization produced simplified forms for linotype, monotype, and typewriters. Nasri Khattar advocated “Unified Arabic” disconnected forms; Kamel Mrowa and others worked on simplified newspaper types. Such systems improved mechanical economy but could sacrifice calligraphic richness.

Contemporary Arabic type design includes figures such as Smitshuijzen AbiFarès, Mamoun Sakkal, Nadine Chahine, Mourad Boutros, and Titus Nemeth. OpenType shaping now enables contextual alternates, ligatures, mark positioning, and stylistic variation beyond what metal type or early bitmap fonts allowed.

---

# Digital encoding

## 1. Unicode model

The Unicode Standard encodes abstract characters rather than separate initial, medial, final, and isolated letters. Rendering engines apply joining properties and font rules.

Principal blocks include:

- Arabic: U+0600–U+06FF;
- Arabic Supplement: U+0750–U+077F;
- Arabic Extended-B: U+0870–U+089F;
- Arabic Extended-A: U+08A0–U+08FF;
- Arabic Extended-C: U+10EC0–U+10EFF;
- Arabic Presentation Forms-A: U+FB50–U+FDFF;
- Arabic Presentation Forms-B: U+FE70–U+FEFF;
- Arabic Mathematical Alphabetic Symbols: U+1EE00–U+1EEFF.

The last ranges and exact allocations should always be checked against the current charts.

## 2. Presentation-form controversy

**[Documented standards history]** Unicode retained large sets of contextual glyph forms and ligatures as compatibility characters because legacy encodings and systems already depended on them.

**[Current Unicode policy]** Normal text should use base Arabic characters; layout software should select contextual glyphs. Presentation Forms-A/B are not recommended as ordinary interchange text.

This compromise is sometimes described as a “fight,” but it was chiefly a standards tension:

- compatibility with existing Arabic systems;
- versus Unicode’s character/glyph separation;
- versus communities’ need to encode genuinely distinct regional letters rather than merely stylistic shapes.

## 3. Persistent technical problems

- Bidirectional interaction among Arabic, Latin text, numbers, punctuation, and brackets.
- Canonically equivalent but differently ordered stacks of combining marks.
- Arabic ي versus Persian ی and Arabic ك versus Persian ک.
- Searching unvocalized and vocalized text.
- Qurʾānic signs and specialized orthographies.
- Mark collisions and poor vowel placement.
- Nastaʿlīq’s vertical and diagonal composition.
- Fonts that support basic Arabic but omit regional letters.
- Line justification using kashīda without distorting word shapes.
- Legacy visual-order encodings and presentation characters.
- Security risks from visually confusable characters.

Unicode 17’s Arabic Mark Rendering annex notes that ordinary NFC or NFD normalization alone may not produce the visual mark order Arabic readers expect. This illustrates why character encoding and typography are separate but interdependent.

---

# The letters as numbers and signs

## 1. Abjad numerals

The 28 letters represent 1–1000:

| Range | Letters and values |
|---|---|
| Units | ا 1, ب 2, ج 3, د 4, ه 5, و 6, ز 7, ح 8, ط 9 |
| Tens | ي 10, ك 20, ل 30, م 40, ن 50, س 60, ع 70, ف 80, ص 90 |
| Hundreds | ق 100, ر 200, ش 300, ت 400, ث 500, خ 600, ذ 700, ض 800, ظ 900 |
| Thousand | غ 1000 |

Uses included:

- numbering lists, sections, manuscript quires, astronomical tables, and calendars;
- **ḥisāb al-jummal**, numerical calculation by letters;
- chronograms whose textual total gives a year;
- talismans and magic squares;
- numerological exegesis.

The positional “Arabic numerals” 0–9 are a different system, derived through Indian mathematics. Conflating abjad numerals with Hindu-Arabic positional numerals is an error.

## 2. Isolated Qurʾānic letters

Twenty-nine Qurʾānic suras begin with combinations such as **الم**, **كهيعص**, and **ق**, traditionally called **al-ḥurūf al-muqaṭṭaʿāt**.

- **[Artefact/text]** Their presence in the Qurʾān is certain.
- **[Documented tradition]** Exegetes proposed divine secrets, abbreviations, oaths, names, numerical signs, or challenges assembled from the same letters as human speech.
- **[Scholarly conclusion]** No interpretation commands consensus.
- **[Absence of evidence]** There is no surviving contemporary key explaining them.

## 3. ʿIlm al-ḥurūf

The “science of letters” developed through late antique inheritances, Qurʾānic reflection, number symbolism, cosmology, astrology, and ritual practice.

### Al-Kindī and early letter sciences

Al-Kindī (d. c. 873) and other ninth–tenth-century authors investigated relations among letters, numbers, sounds, medicines, and cosmic qualities. The boundaries between linguistics, philosophy, cryptanalysis, natural science, and occult science were not identical to modern disciplinary boundaries.

### Al-Būnī

Aḥmad al-Būnī (d. 1225) is associated with letter correspondences, divine names, magic squares, invocations, planets, and talismanic techniques.

**[Textual history warning]** The famous *Shams al-maʿārif* exists in multiple recensions; the large printed version cannot automatically be treated as the exact book written by the historical al-Būnī. Noah Gardiner’s manuscript research shows extensive later selection, compilation, and reshaping of “Būnian” material.

### Ibn ʿArabī

Muḥyī al-Dīn Ibn ʿArabī (1165–1240), especially in the *al-Futūḥāt al-Makkiyya*, treated letters as ontological and cosmological realities. Alif could signify unity, uprightness, or the primordial principle; breath and articulation linked cosmic creation with language.

**[Interpretive caution]** Ibn ʿArabī’s letter science is not identical with later Ḥurūfism, despite frequent popular conflation.

### The bāʾ and its dot

Sufi and esoteric interpretations locate creation or differentiated existence in the dot beneath **ب** of the basmala.

- **[Documented mystical interpretation]** Works associated with Ibn ʿArabī’s school and later exegetes connect bāʾ and its dot with First Intellect, manifestation, or the relation between worshipper and worshipped.
- **[Popular attribution/uncertain transmission]** “All knowledge is in the Fātiḥa, the Fātiḥa in the basmala, the basmala in the bāʾ, and I am the dot beneath the bāʾ” is widely attributed to ʿAlī. Its exact early documentary chain is insecure; it should not be presented as a verified saying of the historical ʿAlī.

## 4. Ḥurūfism

Fażlallāh Astarābādī (c. 1340–1394) founded the Ḥurūfī movement. His *Jāvīdān-nāma* interprets revelation, the human face, sounds, and divine manifestation through the letters.

The 28 Arabic and 32 Perso-Arabic letters became cosmological structures. His movement spread in Timurid Iran and influenced Bektashi environments in Anatolia.

**[Documented historical judgment]** Authorities executed Fażlallāh in 1394. Sources differ over political and doctrinal circumstances.

## 5. Magic, divination, and protection

Letter grids, Qurʾānic verses, divine names, numerical totals, seals, and magic squares appear on manuscripts, bowls, scrolls, shirts, amulets, and architecture.

The same object might be understood by different users as prayer, medicine, protection, astrology, “licit magic,” illicit sorcery, or art. A modern binary between religion and magic can obscure historical categories.

---

# People

## Formation and grammatical tradition

- **René Dussaud (1868–1958):** co-discoverer and first major publisher/reader of Namāra.
- **Frédéric Macler (1869–1938):** participated in the Namāra expedition.
- **Eduard Sachau (1845–1930):** published important Syrian and Arabic inscriptions, including Zabad.
- **James A. Bellamy (1925–2015):** proposed the influential 1985 rereading of Namāra.
- **Nabia Abbott (1897–1981):** foundational studies of early Arabic scripts and papyri.
- **Beatrice Gruendler:** systematic palaeographic study of Nabataean-to-Arabic development.
- **John F. Healey:** scholarship on Nabataean and early alphabets.
- **Michael C. A. Macdonald:** Ancient North Arabian and Paleo-Arabic epigraphy.
- **François Déroche:** Qurʾānic palaeography and codicology.
- **Ahmad Al-Jallad:** Old Arabic, Ancient North Arabian inscriptions, and Paleo-Arabic.
- **Abū al-Aswad al-Duʾalī:** traditional founder of Arabic grammar and vowel dotting.
- **Naṣr ibn ʿĀṣim and Yaḥyā ibn Yaʿmar:** traditional consonantal-dotting reformers.
- **Al-Khalīl ibn Aḥmad (d. c. 786/791):** grammarian and lexicographer credited with mature vowel notation and author of *Kitāb al-ʿAyn*.
- **Sībawayh (c. 760–796):** author of the foundational Arabic grammatical *Kitāb*.

## Calligraphers

- Ibn Muqla (886–940).
- Ibn al-Bawwāb (d. 1022).
- Yāqūt al-Mustaʿṣimī (d. c. 1298).
- Mīr ʿAlī Tabrīzī (fl. late fourteenth century), traditionally credited with nastaʿlīq’s formulation.
- Sultan ʿAlī Mashhadī (1430s–1520).
- Şeyh Hamdullah (1436–1520).
- Mīr ʿImād al-Ḥasanī (1554–1615), great Persian nastaʿlīq master.
- Hâfız Osman (1642–1698).
- Mustafa Râkım (1757–1826).
- Hāmid al-Āmidī (1891–1982), major modern Ottoman/Turkish master.
- Muhammad Zakariya (b. 1942), prominent contemporary American calligrapher in the Ottoman lineage.

## Printers and type designers

- Gregorio de Gregorii: printer of the 1514 Arabic Book of Hours.
- Guillaume Le Bé (1525–1598): early European Arabic punches.
- Robert Granjon (1513–1590): influential Medici Press Arabic types.
- Ibrahim Müteferrika (c. 1674–1745): Ottoman printer.
- Niqūlā al-Masābikī (d. 1830): Būlāq type founder and director.
- Mirzā Sanglākh (d. 1877): calligrapher and type designer associated with Būlāq.
- Nasri Khattar (1911–1998): proposed Unified Arabic.
- Kamel Mrowa (1915–1966): newspaper lettering and simplified Arabic-type development.
- Contemporary designers named above continue the negotiation between calligraphic inheritance and screen typography.

## Legends of invention

Arabic-origin legends are less standardized than the stories of Cadmus or Odin but are abundant:

- **[Qurʾānic/religious tradition]** Adam was sometimes called the first writer.
- **[Legend]** Idrīs—identified in some traditions with Enoch—was said to be the first to write with a pen.
- **[Tradition]** Ishmael was credited with the first Arabic writing or the first eloquent Arabic.
- **[Documented medieval tradition]** Ibn al-Nadīm’s *Fihrist* records competing accounts: script learned from al-Anbār and al-Ḥīra; invented at a settlement in Midian; or borrowed from earlier peoples.
- **[Tradition]** The chain al-Anbār → al-Ḥīra → Mecca is found in Islamic historical reports.
- **[Scholarly assessment]** These accounts preserve memories of scribal centers and cultural transmission but cannot override the palaeographic Nabataean sequence. Recent epigraphy also makes a single east-to-west transmission route too simple.

---

# Culture

## 1. Law and government

Arabic script became an instrument of empire through:

- taxation receipts and papyri;
- chancery documents;
- treaties;
- legal manuals;
- court registers;
- land deeds;
- waqf endowments;
- seals, signatures, and the Ottoman **ṭughrā**;
- public decrees and monumental inscriptions.

The Qurʾānic injunction to record deferred debts (Q 2:282) gave writing a conspicuous place in legal ethics.

## 2. Scripture

The Qurʾān was decisive for preservation, teaching, and prestige. Arabic script was also used by Arabic-speaking Christians and Jews:

- Christian Arabic Bibles and liturgy;
- **Judaeo-Arabic**, normally written in Hebrew letters but also interacting with Arabic scribal culture;
- **Garshuni**, Arabic written in Syriac script, demonstrating that Arabic language and Arabic alphabet were never absolutely inseparable.

Qurʾānic calligraphy ranges from portable codices to the Dome of the Rock and monumental mosque inscriptions. Script, recitation, illumination, geometry, and architecture jointly organized sacred experience.

## 3. Coins

Umayyad coin reform replaced or transformed Byzantine and Sasanian images and inscriptions. From the 690s, epigraphic gold dinars and silver dirhams proclaimed Islamic formulas and Qurʾānic text in Arabic. Their broad circulation made script a portable statement of sovereignty.

## 4. Seals and signatures

Personal seals commonly carry names, pious formulas, or Qurʾānic phrases. Ottoman sultans’ tughras fused name, title, genealogy, and emblem into a highly formal calligraphic sign.

## 5. Calendars and astronomy

Abjad notation served astronomical tables, manuscript organization, and chronograms. Arabic-script scientific manuscripts transmitted Greek, Persian, Indian, and original Islamic astronomy, medicine, mathematics, and geography.

## 6. Alphabet poems, acrostics, and literature

Arabic literary culture uses:

- alphabetical dictionaries;
- abecedarian didactic poems;
- acrostics;
- *muʿammā* riddles and chronograms;
- letter-by-letter mystical treatises;
- visual poetry and calligrams.

Al-Khalīl’s *Kitāb al-ʿAyn* famously orders roots not by modern hijāʾī sequence but by a phonetic scheme beginning with ʿayn, believed to arise deepest in the throat.

Modern artists turned the script into painting, sculpture, and concrete poetry. The twentieth-century **ḥurūfiyya** art movement appropriated letter forms as modern visual material.

**[Modern invention distinguished from medieval Ḥurūfism]** Modern *ḥurūfiyya* is not simply the survival of Fażlallāh’s religion. Artists variously invoked heritage, abstraction, nationalism, spirituality, and postcolonial identity.

---

# Controversies and disputes

## 1. What is the “earliest Arabic inscription”?

The phrase can mean at least four things:

1. earliest Arabic language in any script;
2. earliest Arabic linguistic features in Nabataean;
3. earliest recognizably Arabic alphabet;
4. earliest independently dated Arabic-language Arabic-script inscription.

Namāra, Raqush, ʿEn ʿAvdat, Zabad, and Jabal Usays can each be called “earliest” only under different definitions. Failure to specify the criterion creates manufactured controversy.

## 2. Nabataean versus Syriac origin

- **Nabataean case:** continuous letter-shape transitions; geography; dated inscriptions; cursive joining.
- **Syriac case:** cultural contact, eastern origin traditions, and certain broad formal parallels.
- **Current balance:** principal Nabataean descent, possible Syriac contact. A direct South Arabian *musnad* ancestry lacks a convincing sequence of graphic intermediates.

## 3. Southern Arabian origin tradition

Ibn Jinnī, Ibn Khaldūn, and other authors transmitted views connecting Arabic letters with Yemenite or *musnad* writing.

- **[Documented tradition]** Important for medieval historical consciousness.
- **[Scholarly assessment]** The monumental South Arabian alphabet belongs to a different graphic branch and order. No continuous chain leads from its forms to Arabic.
- **[Possible contact]** South Arabian minuscule writing and Arabian multilingualism remain relevant to the region’s overall scribal ecology.

## 4. Who invented the dots?

- **Traditional narrative:** Abū al-Aswad invented vowel dots; Naṣr and Yaḥyā introduced consonantal dots under al-Ḥajjāj; al-Khalīl perfected the signs.
- **Artefactual objection:** sporadic dots occur before or during these figures’ lifetimes.
- **Current reconstruction:** dotting was inherited and experimented with, then standardized through multiple administrative and grammatical interventions.
- **Unresolved:** exactly what al-Ḥajjāj ordered and how uniformly it was implemented.

Adam Bursi’s study, “The Emergence of Arabic Diacritics in Myth and History,” specifically argues that later narratives should not be read as transparent contemporary reports.

## 5. Did al-Ḥajjāj alter the Qurʾān?

**[Documented polemic/tradition]** Later reports attribute orthographic measures, distribution of codices, or a set of word changes to al-Ḥajjāj.

**[Artefact]** Manuscripts show evolving orthography and dotting, but not a sudden universally imposed fully dotted text matching the strongest later claims.

**[Scholarly dispute]** Al-Ḥajjāj and ʿAbd al-Malik plausibly affected administrative standardization and Qurʾānic transmission. Evidence does not support treating every later accusation—or every apologetic denial—as a direct record of an early-seventh-century event.

## 6. Dating early Qurʾāns

Radiocarbon ranges can begin before Muḥammad’s lifetime because they date animal skin. Parchment might be stored before use, and a codex can combine leaves of different dates. Palaeography is comparative rather than mechanically exact.

The sound method combines:

- radiocarbon;
- script;
- orthography;
- codicology;
- art history;
- textual relations;
- documentary provenance.

Calling Birmingham “a Qurʾān written in 568” mistakes the lower boundary of a probability range for a writing date.

## 7. “Kufic” as a historical category

The medieval association with Kufa is real as tradition; the modern practice of labeling nearly every angular early hand “Kufic” is overly broad. François Déroche’s typology favors descriptions grounded in actual graphic features.

## 8. Calligraphy and the alleged image prohibition

The thesis that Arabic calligraphy became supreme solely because Islam prohibited all images is disputed. Aniconism matters in particular religious contexts, but figural art flourished in palaces, manuscripts, ceramics, metalwork, and scientific illustration. Qurʾānic centrality, state patronage, architecture, portability, and the aesthetic potential of Arabic writing are all independently important.

## 9. Printing “ban”

Ottoman juristic and governmental restrictions existed in particular periods and domains, but scribal economics, specialized labor, technical shortcomings, readership, and manuscript prestige also mattered. The phrase “Muslims rejected printing for religious reasons” is too general to explain the differing histories of Christian Arabic, Jewish Ottoman printing, Persian lithography, Müteferrika’s press, and Būlāq.

## 10. Modern alphabet-reform claims

Arguments that Arabic script is intrinsically “unfit” for science or modernity are ideological generalizations. Real orthographic difficulties exist: vowel omission, spelling conventions, keyboarding, regional letters, and typography. Yet the system has supported immense scientific, legal, and literary corpora.

Conversely, claims that the script is divinely perfect in all graphic details belong to theology or symbolism, not historical palaeography. Arabic letter shapes demonstrably changed over time.

## 11. Forgeries and misreadings

No single notorious forgery defines Arabic-script origins in the way the Praeneste Fibula once affected Latin debates. The more persistent hazards are:

- undated graffiti assigned dates from letter style alone;
- modern recutting or enhancement;
- photographs with missing context;
- circular readings based on expected religious formulas;
- equating any Arabic-language text with Arabic script;
- assigning a whole multilingual monument’s date automatically to a possibly secondary Arabic addition;
- internet “ancient alphabet” charts that project reconstructed pictograms directly onto Arabic letters.

Namāra’s successive readings and Zabad’s disputed contemporaneity exemplify legitimate revision rather than fraud.

## 12. Modern pseudo-history

**[Modern invention]** Claims that letter shapes encode modern anatomy, electromagnetic principles, or universal sacred geometry generally lack ancient textual or artefactual evidence. They may be meaningful contemporary spiritual or artistic systems but must not be retrojected as the alphabet’s historical design specification.

---

# Open questions

1. Which still-undiscovered inscriptions will narrow the transition from Nabataean to Arabic, especially in the northern Ḥijāz?
2. Was Arabic script’s transformation centered in one network or produced polycentrically through Petra, Ḥawrān, Syria, and northwestern Arabia?
3. How much did Syriac, Hebrew, Greek, South Arabian minuscule, and documentary Nabataean practices influence specific conventions without being the principal parent?
4. Can the earliest dots be classified regionally and chronologically from a larger corpus rather than isolated examples?
5. Which details of the Abū al-Aswad/al-Ḥajjāj narratives preserve genuine seventh-century institutional memory?
6. How precisely should Zabad’s Arabic portion be dated relative to its Greek and Syriac texts?
7. How much early Qurʾānic variation reflects scribal error, local orthography, oral readings, companion codices, or stages of textual stabilization?
8. Which works in the large printed *Shams al-maʿārif* genuinely derive from al-Būnī?
9. How should Unicode distinguish genuine orthographic characters from glyph variants in lesser-documented African and Asian Arabic-script traditions?
10. How can digital fonts reproduce mark stacking, elongation, and nastaʿlīq composition without sacrificing accessibility, text search, and interoperability?
11. How extensive are uncatalogued ʿAjamī archives in private West African, East African, and Southeast Asian collections?
12. How should scholarship preserve living non-Arabic Arabic-script traditions without forcing them into Persian or Arabic typographic assumptions?

Absence of evidence is particularly consequential in three areas: no contemporary narrative records the “invention” of Arabic script; no surviving document proves a single inventor of dotting; and no contemporary key explains the Qurʾān’s disconnected letters.

---

# Sources: editions and URLs consulted

## General histories and reference works

- Peter T. Daniels and William Bright, eds., *The World’s Writing Systems*. Oxford University Press, 1996.  
  https://global.oup.com/academic/product/the-worlds-writing-systems-9780195079937
- David Diringer, *The Alphabet: A Key to the History of Mankind*, 3rd ed. Hutchinson, 1968.  
  https://archive.org/search?query=David+Diringer+The+Alphabet
- Joseph Naveh, *Early History of the Alphabet: An Introduction to West Semitic Epigraphy and Palaeography*, 2nd ed. Magnes Press, 1987.  
  https://books.google.com/books?q=Joseph+Naveh+Early+History+of+the+Alphabet
- John F. Healey, *The Early Alphabet*. University of California Press/British Museum, 1990.  
  https://books.google.com/books?q=John+F+Healey+The+Early+Alphabet
- John F. Healey, *The Nabataean Tomb Inscriptions of Mada’in Salih*. Oxford University Press, 1993.  
  https://books.google.com/books?q=Healey+Nabataean+Tomb+Inscriptions+Mada%27in+Salih

## Arabic origins and inscriptions

- Beatrice Gruendler, *The Development of the Arabic Scripts: From the Nabatean Era to the First Islamic Century according to Dated Texts*. Scholars Press, 1993.  
  https://hmane.harvard.edu/publications/development-arabic-scriptsfrom-nabatean-era-first-islamic-century
- Laïla Nehmé, “A Glimpse of the Development of the Nabataean Script into Arabic Based on Old and New Epigraphic Material,” in *The Development of Arabic as a Written Language*. Archaeopress, 2010.  
  https://books.google.com/books?q=La%C3%AFla+Nehm%C3%A9+Glimpse+Development+Nabataean+Script+Arabic
- René Dussaud and Frédéric Macler, *Mission dans les régions désertiques de la Syrie moyenne*. Paris, 1903.  
  https://archive.org/search?query=Dussaud+Macler+Mission+r%C3%A9gions+d%C3%A9sertiques
- René Dussaud, “L’inscription de Nemāra,” *Revue archéologique*, 1905.  
  https://www.jstor.org/action/doBasicSearch?Query=Dussaud+inscription+Nemara
- James A. Bellamy, “A New Reading of the Namārah Inscription,” *Journal of the American Oriental Society* 105.1 (1985): 31–48.  
  https://www.jstor.org/stable/601538
- Michael C. A. Macdonald, “Reflections on the Linguistic Map of Pre-Islamic Arabia,” *Arabian Archaeology and Epigraphy* 11 (2000).  
  https://onlinelibrary.wiley.com/doi/10.1111/j.1600-0471.2000.aae110106.x
- Michael C. A. Macdonald, “Ancient Arabia and the Written Word,” in *The Development of Arabic as a Written Language*.  
  https://books.google.com/books?q=Michael+Macdonald+Ancient+Arabia+and+the+Written+Word
- Ahmad Al-Jallad, “A Paleo-Arabic Inscription on a Route North of Ṭāʾif,” *Arabian Archaeology and Epigraphy* 34 (2023).  
  https://onlinelibrary.wiley.com/doi/10.1111/aae.12203
- Ali ibn Ibrahim Ghabban and Robert Hoyland, “The Inscription of Zuhayr, the Oldest Islamic Inscription (24 AH/AD 644–645),” *Arabian Archaeology and Epigraphy* 19 (2008): 209–236.  
  https://onlinelibrary.wiley.com/doi/10.1111/j.1600-0471.2008.00297.x
- Fred M. Donner, “The Arabic Inscription of the Dome of the Rock,” relevant discussions in early Islamic historiography.  
  https://books.google.com/books?q=Arabic+inscription+Dome+of+the+Rock+Donner
- University of Chicago, Nabataean and North Arabic inscriptions, *Oriental Institute Publications* 50.  
  https://oi.uchicago.edu/sites/default/files/uploads/shared/docs/oip50.pdf
- Cult of Saints in Late Antiquity database, Zabad/St Sergius, Evidence E01817.  
  https://csla.history.ox.ac.uk/record.php?recid=E01817
- Royal Museums of Art and History, Brussels, Zabad inscription A 1308.  
  https://www.artandhistory.museum
- Summary and photographs of the Zabad inscription, with bibliography.  
  https://www.islamic-awareness.org/history/islam/inscriptions/zebed
- Namāra inscription overview and bibliography.  
  https://www.louvre.fr/en
- “Where Did You Learn to Write Arabic? A Critical Analysis of Some Ḥadīths on the Origins and Spread of the Arabic Script,” University of Groningen research record.  
  https://research.rug.nl/en/publications/where-did-you-learn-to-write-arabic-a-critical-analysis-of-some-%E1%B8%A5/

## Qurʾānic manuscripts, dotting, and vocalization

- University of Birmingham, Birmingham Qurʾān Manuscript.  
  https://www.birmingham.ac.uk/facilities/cadbury/TheBirminghamQuranManuscript
- University of Birmingham, “What is the Birmingham Qur’an?”  
  https://www.birmingham.ac.uk/facilities/cadbury/birmingham-quran-mingana-collection/birmingham-quran/what-is
- Corpus Coranicum, Birmingham/Parisino-petropolitanus manuscript images and records.  
  https://corpuscoranicum.de/en/manuscripts/2278/page/1r
- François Déroche, *La transmission écrite du Coran dans les débuts de l’islam: Le codex Parisino-petropolitanus*. Brill, 2009.  
  https://brill.com/display/title/16356
- François Déroche, *Qur’ans of the Umayyads: A First Overview*. Brill, 2014.  
  https://brill.com/display/title/25276
- François Déroche, *Islamic Codicology: An Introduction to the Study of Manuscripts in Arabic Script*. Al-Furqan, 2006.  
  https://www.al-furqan.com/publication/islamic-codicology-an-introduction-to-the-study-of-manuscripts-in-arabic-script-9781905122028/
- Behnam Sadeghi and Uwe Bergmann, “The Codex of a Companion of the Prophet and the Qurʾān of the Prophet,” *Arabica* 57 (2010).  
  https://brill.com/view/journals/arab/57/4/article-p343_1.xml
- Adam Bursi, “Connecting the Dots: Diacritics, Scribal Culture, and the Qurʾān in the First/Seventh Century,” *Journal of the International Qur’anic Studies Association* 3 (2018).  
  https://beta.iqsaweb.org/wp-content/uploads/2022/06/JIQSA3.5-1.pdf
- Alain George, “Coloured Dots and the Question of Regional Origins in Early Qur’ans,” Oxford Research Archive.  
  https://ora.ox.ac.uk/objects/uuid%3A509ded8b-d160-491a-b053-7248f37b7ca9
- Geoffrey Khan and collaborators, eds., *The Shared Intellectual History of Vocalisation*. Open Book Publishers, 2020s.  
  https://books.openbookpublishers.com/10.11647/obp.0271.pdf
- Marijn van Putten, Qurʾānic Arabic and early manuscript orthography research.  
  https://leidenuniv.academia.edu/MarijnvanPutten
- Nicolai Sinai, “When Did the Consonantal Skeleton of the Qurʾān Reach Closure?” *Bulletin of SOAS*.  
  https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/abs/when-did-the-consonantal-skeleton-of-the-quran-reach-closure-part-i1/D2C425AFB394D8979DE11DA4E0AAE086

## Grammar, letter order, and numerals

- Encyclopaedia Iranica, “Abjad.”  
  https://www.iranicaonline.org/articles/abjad/
- Encyclopaedia Iranica, “Mādda Tārīḵ.”  
  https://www.iranicaonline.org/articles/madda-tarik-chronogram/
- Al-Khalīl ibn Aḥmad, *Kitāb al-ʿAyn*, Arabic editions.  
  https://archive.org/search?query=%D9%83%D8%AA%D8%A7%D8%A8+%D8%A7%D9%84%D8%B9%D9%8A%D9%86+%D8%A7%D9%84%D8%AE%D9%84%D9%8A%D9%84
- Sībawayh, *al-Kitāb*, Arabic editions.  
  https://archive.org/search?query=%D9%83%D8%AA%D8%A7%D8%A8+%D8%B3%D9%8A%D8%A8%D9%88%D9%8A%D9%87
- Ibn al-Nadīm, *Kitāb al-Fihrist*, editions and translations.  
  https://archive.org/search?query=Ibn+al-Nadim+Fihrist

## Calligraphy and art

- Metropolitan Museum of Art, *Islamic Calligraphy*, *Metropolitan Museum of Art Bulletin* 50.1 (1992).  
  https://resources.metmuseum.org/resources/metpublications/pdf/Islamic_Calligraphy_The_Metropolitan_Museum_of_Art_Bulletin_v_50_no_1_Summer_1992.pdf
- Metropolitan Museum, bifolium from a Qurʾān manuscript and script description.  
  https://www.metmuseum.org/art/collection/search/447066
- Ashmolean Museum, “The Six Pens” and Ibn Muqla tradition.  
  https://jameelcentre.ashmolean.org/collection/6980/9992/9995
- Encyclopaedia Iranica, “Calligraphy.”  
  https://www.iranicaonline.org/articles/calligraphy/
- Sheila S. Blair, *Islamic Calligraphy*. Edinburgh University Press, 2006.  
  https://edinburghuniversitypress.com/book-islamic-calligraphy.html
- Annemarie Schimmel, *Calligraphy and Islamic Culture*. New York University Press, 1984.  
  https://books.google.com/books?q=Annemarie+Schimmel+Calligraphy+and+Islamic+Culture
- Chester Beatty Library, Islamic manuscripts and Ibn al-Bawwāb Qurʾān.  
  https://chesterbeatty.ie/explore/islamic-collections/
- Khalili Collections, Abbasid Qurʾāns.  
  https://www.khalilicollections.org/portfolio/the-abbasid-tradition-qurans-of-the-8th-to-the-10th-centuries-ad/

## Persian, Urdu, Ottoman, Malay, and African adaptations

- Encyclopaedia Iranica, “Calligraphy.”  
  https://www.iranicaonline.org/articles/calligraphy/
- Encyclopaedia Iranica, “Sīāq.”  
  https://www.iranicaonline.org/articles/siaq/
- Annemarie Schimmel, *Calligraphy and Islamic Culture*.  
  https://books.google.com/books?q=Schimmel+Calligraphy+Islamic+Culture
- Richard M. Eaton, Persianate culture and South Asian Islam.  
  https://books.google.com/books?q=Richard+Eaton+Persianate+South+Asia
- M. B. Hooker, studies of Jawi law and Malay Islam.  
  https://books.google.com/books?q=M.B.+Hooker+Jawi+Malay+law
- Library of Congress, Southeast Asian manuscript collections.  
  https://www.loc.gov/collections/
- Fallou Ngom, *Muslims beyond the Arab World: The Odyssey of ʿAjamī and the Murīdiyya*. Oxford University Press, 2016.  
  https://global.oup.com/academic/product/muslims-beyond-the-arab-world-9780190279868
- Endangered Archives Programme, Arabic and ʿAjamī manuscript collections.  
  https://eap.bl.uk/
- Turkish Grand National Assembly, Law No. 1353 records.  
  https://www5.tbmm.gov.tr/develop/owa/td_v2.tutanak_sonuc
- Turkish Official Gazette history and implementation.  
  https://resmigazete.gov.tr/sayfa-tarihce
- Text of Law No. 1353.  
  https://www.lexpera.com.tr/mevzuat/kanunlar/turk-harflerinin-kabul-ve-tatbiki-hakkinda-kanun-1353

## Letter mysticism, Sufism, and magic

- Encyclopaedia Iranica, “Jafr.”  
  https://www.iranicaonline.org/articles/jafr/
- Encyclopaedia Iranica, “Horufism.”  
  https://www.iranicaonline.org/articles/horufism/
- Encyclopaedia Iranica, “Astarābādī, Fażlallāh.”  
  https://www.iranicaonline.org/articles/astarabadi-fazlallah-sehab-al-din-b/
- Encyclopaedia Iranica, “Jāvdān-nāma.”  
  https://www.iranicaonline.org/articles/javdan-nama/
- Encyclopaedia Iranica, “Besmellāh ii: In Exegesis, Jurisprudence, and Cultural Life.”  
  https://www.iranicaonline.org/articles/besmellah-islamic-formula-meaning-in-the-name-of-god-more-fully-besmellah-al-rahman-al-rahim-in-the-name-of-god-t/besmellah-ii-in-exegesis-jurisprudence-and-cultural-life/
- Hala Fouad, “The Symbolism of the Letter Alif in Ibn ʿArabi.”  
  https://fount.aucegypt.edu/faculty_journal_articles/2969/
- Alexandra Bain, *The ʿIlm al-Ḥurūf, or Science of Letters* (doctoral dissertation).  
  https://dspace.library.uvic.ca/bitstream/handle/1828/8702/Bain_Alexandra_PhD_1998.pdf
- Noah Gardiner, research on al-Būnī and the Būnian corpus, *Journal of Arabic and Islamic Studies* 12 (2012).  
  https://www.lancaster.ac.uk/jais/volume/docs/vol12/JAIS_12_%282012%29_1-263.pdf
- Ibn ʿArabī, *al-Futūḥāt al-Makkiyya*, Arabic editions.  
  https://archive.org/search?query=%D8%A7%D9%84%D9%81%D8%AA%D9%88%D8%AD%D8%A7%D8%AA+%D8%A7%D9%84%D9%85%D9%83%D9%8A%D8%A9+%D8%A7%D8%A8%D9%86+%D8%B9%D8%B1%D8%A8%D9%8A
- Fażlallāh Astarābādī manuscript and catalogue studies cited by Iranica.  
  https://www.iranicaonline.org/articles/astarabadi-fazlallah-sehab-al-din-b/

## Printing and typography

- Miroslav Krek, “The Enigma of the First Arabic Book Printed from Movable Type,” *Journal of Near Eastern Studies* 38 (1979).  
  https://www.jstor.org/stable/544727
- Geoffrey Roper, studies of early Arabic printing.  
  https://books.google.com/books?q=Geoffrey+Roper+early+Arabic+printing
- Harvard University, *The Beginnings of Arabic Printing*.  
  https://dash.harvard.edu/bitstreams/21d4f018-72b7-4729-bb6b-c184f5b4b2d7/download
- Bibliotheca Alexandrina, Būlāq Press history.  
  https://www.bibalex.org/bulaqpress/en/bulaq.htm
- Ahmed Mansour et al., “Legacy in Print: Unearthing the Documentary Heritage of the Bulaq Press.”  
  https://www.ijodh.org/0201-06/
- OpenITI, “From Handwritten to Metal Type and Back to Handwritten: The Trajectory of Nastaʿlīq Printing.”  
  https://openiti.org/2022/02/15/Handwritten-Metal-Type.html
- Titus Nemeth, *Arabic Type-Making in the Machine Age*. Brill, 2017.  
  https://brill.com/display/title/32482
- Huda Smitshuijzen AbiFarès, *Arabic Typography: A Comprehensive Sourcebook*.  
  https://books.google.com/books?q=Huda+Smitshuijzen+AbiFares+Arabic+Typography

## Unicode and digital text

- Unicode Standard 17.0, Chapter 9: Middle East-I.  
  https://unicode.org/versions/Unicode17.0.0/core-spec/chapter-9/
- Unicode Arabic chart.  
  https://www.unicode.org/charts/PDF/U0600.pdf
- Unicode Arabic Supplement chart.  
  https://www.unicode.org/charts/PDF/U0750.pdf
- Unicode Arabic Extended-A chart.  
  https://www.unicode.org/charts/PDF/U08A0.pdf
- Unicode Arabic Presentation Forms-A chart.  
  https://www.unicode.org/charts/PDF/UFB50.pdf
- Unicode Arabic Presentation Forms-B chart.  
  https://www.unicode.org/charts/PDF/UFE70.pdf
- Unicode Arabic Mathematical Alphabetic Symbols chart.  
  https://www.unicode.org/charts/PDF/U1EE00.pdf
- Unicode FAQ, “Ligatures, Digraphs and Presentation Forms.”  
  https://www.unicode.org/faq/ligature_digraph.html
- Unicode Standard Annex #9, Bidirectional Algorithm.  
  https://www.unicode.org/reports/tr9/
- Unicode Standard Annex #53, Arabic Mark Rendering.  
  https://www.unicode.org/reports/tr53/
- Unicode ArabicShaping property data.  
  https://www.unicode.org/Public/UCD/latest/ucd/ArabicShaping.txt
- W3C, *Text Layout Requirements for the Arabic Script*.  
  https://www.w3.org/TR/alreq/
- Sina Ahmadi, “Graphemic Normalization of the Perso-Arabic Script.”  
  https://arxiv.org/abs/2210.12273
