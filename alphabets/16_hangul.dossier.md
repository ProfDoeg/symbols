# Hangul: Research Dossier

## Method and evidentiary labels

This dossier uses the following labels throughout:

- **[Documented text]**: stated in a contemporary or near-contemporary written source.
- **[Documented artefact]**: supported by a surviving physical object, manuscript, or printing.
- **[Scholarly reconstruction]**: an inference accepted or proposed in modern scholarship.
- **[Disputed]**: a claim for which substantial competing interpretations exist.
- **[Tradition]**: a received historical account whose factual basis is incomplete.
- **[Legend]**: a story not supported by contemporary evidence.
- **[Modern invention]**: a recent symbolic, nationalist, artistic, or technical development.
- **[Absence of evidence]**: no securely documented example was found in the sources consulted.

Transcriptions use Revised Romanization where practical, with older McCune–Reischauer forms retained in bibliographical titles. IPA values are approximate because both Middle Korean and modern Korean values depend on position, dialect, and phonological analysis.

---

## Basic identification

| Field | Identification |
|---|---|
| Name | **Hangul** or **Hangeul** 한글 in South Korea; **Chosŏn’gŭl** 조선글 in North Korea; originally **Hunminjeongeum** 訓民正音, “The Correct/Proper Sounds for Instructing the People” |
| Script type | A **featural alphabet** whose alphabetic letters (*jamo*) are assembled into **syllable blocks**. Unicode consequently calls it a “featural syllabic script,” but its signs represent phonemes rather than whole syllables. |
| Original inventory | **28 basic letters** in 1443/1446: 17 consonants and 11 vowels |
| Modern basic inventory | South Korean analysis: **24 basic letters**, 14 consonants and 10 vowels. Five doubled consonants and eleven compound vowels produce the familiar practical inventory of 40. North Korean rules count those composites and therefore speak of **40 letters**. |
| Direction | Originally vertical columns, read top-to-bottom, with columns ordered right-to-left, following Sinographic book practice. Modern writing is predominantly horizontal left-to-right. Vertical writing remains possible. No documented boustrophedon. |
| Period | Devised by late 1443 or early 1444; explanatory book published in the ninth lunar month of 1446; continuously used to the present |
| Region | Created in Joseon Korea; now the principal script of both Koreas and Korean communities worldwide; experimentally adapted to Cia-Cia in Indonesia |
| Parent | **No securely demonstrated parent in the ordinary genealogical sense.** The official 1446 explanation derives basic consonants from articulatory diagrams and vowels from Heaven–Earth–Human. Gari Ledyard proposed a limited formal stimulus from Mongol imperial ʼPhags-pa for part of the consonant design; this remains disputed. |
| Daughters | No major genealogical daughter script. The 2009 Cia-Cia orthography is an adaptation of Hangul, not a new independent script. Numerous modern constructed Hangul orthographies exist for other languages. |
| Numerical values | None inherent. Hangul was never an alphabetic numeral system comparable to Greek, Hebrew, or Arabic abjad numerals. Korean texts used Chinese-derived number words and numerals, counting-rod forms, and later Hindu-Arabic digits. |
| Capital/minuscule distinction | None. Hangul has no historical uppercase/lowercase opposition. Size, weight, spacing, color, or Hanja could instead distinguish headings and names. |
| Unicode | Hangul Jamo U+1100–U+11FF; Compatibility Jamo U+3130–U+318F; Jamo Extended-A U+A960–U+A97F; precomposed modern syllables U+AC00–U+D7A3; Jamo Extended-B U+D7B0–U+D7FF; halfwidth compatibility forms in U+FFA0–U+FFDC |

The Unicode Standard contains both alphabetic jamo and all 11,172 possible modern precomposed syllables. Its own classification—“featural syllabic script”—captures Hangul’s dual structure: alphabetic phonemes below the syllable level, square syllable cells at the graphic level. [Unicode, Chapter 18](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/)

---

# The script in detail

## 1. Structural principle

A Hangul word is not written as an uninterrupted linear row of letters. Its jamo are grouped into syllable blocks:

- 한 *han* = ㅎ *h* + ㅏ *a* + ㄴ *n*
- 글 *geul* = ㄱ *g/k* + ㅡ *eu* + ㄹ *l/r*

The vowel’s shape controls layout:

- Vertical vowels such as ㅏ, ㅓ, ㅣ are placed to the right of the initial: 나 *na*.
- Horizontal vowels such as ㅗ, ㅜ, ㅡ are placed below it: 노 *no*.
- A final consonant, *batchim* 받침, occupies the bottom: 난 *nan*.
- Compound vowels and consonant clusters subdivide the same square.

**[Documented text]** The *Hunminjeongeum Haerye* explicitly distinguishes initial, medial, and final positions and describes combining the letters into syllables. It also states that an initial consonant may be reused as a final consonant.

**[Scholarly reconstruction]** The square block was almost certainly compatible with the visual and material ecology of Chinese-character writing: the new phonemic signs could be written alongside Hanja without disrupting vertical columns or the square em. This does not make the blocks logograms.

## 2. Featural consonant design

The 1446 *Haerye* identifies five basic consonant forms:

| Basic jamo | Traditional class | Approximate original value | Stated design |
|---|---|---:|---|
| ㄱ | molar/velar 牙音 | /k/ | Outline of the tongue root blocking the throat |
| ㄴ | lingual 舌音 | /n/ | Outline of the tongue touching the upper gums |
| ㅁ | labial 脣音 | /m/ | Shape of the mouth |
| ㅅ | dental 齒音 | /s/ | Shape of a tooth or teeth |
| ㅇ | throat 喉音 | zero or laryngeal class | Shape of the throat |

**[Documented text]** These explanations occur in the *Chejahae*, “Explanation of the Making of the Letters,” in the 1446 *Haerye*.

Additional strokes differentiate related consonants:

- ㄱ → ㅋ
- ㄴ → ㄷ → ㅌ
- ㅁ → ㅂ → ㅍ
- ㅅ → ㅈ → ㅊ
- ㅇ → ㆆ → ㅎ

This is **featural** because related graphic shapes encode related articulatory categories. The exact phonetic interpretation of every added stroke is not simply “more aspiration”: the system was framed through fifteenth-century Chinese phonological classes, degrees of force, and Korean phonetics.

ㄹ and ㅿ were treated as exceptional or “half” members of their respective classes rather than straightforward stroke-derived series.

## 3. Vowel design: Heaven, Earth, and Human

The three elementary vowel signs were:

| Original sign | Unicode/modern form | Cosmological value | Graphic explanation |
|---|---|---|---|
| ㆍ | U+318D HANGUL LETTER ARAEA | Heaven 天 | A round point |
| ㅡ | U+3161 | Earth 地 | A horizontal line |
| ㅣ | U+3163 | Human 人 | An upright person |

The *Haerye* says:

> 形之圓 象乎天也  
> “Its round shape symbolizes Heaven.”

> 形之平 象乎地也  
> “Its level shape symbolizes Earth.”

> 形之立 象乎人也  
> “Its upright shape symbolizes humanity.”

**[Documented text]** These are the text’s own explanations, not retrospective folklore. They belong to a Neo-Confucian cosmological account in which yin and yang, the Three Powers, directions, seasons, and vowel harmony are coordinated. [English text and Classical Chinese transcription](https://en.wikisource.org/wiki/Translation:Hunminjeongeum)

Dots were combined with the horizontal or vertical stroke:

- ㆍ + ㅡ → ㅗ or ㅜ
- ㆍ + ㅣ → ㅏ or ㅓ
- doubling the dot supplied the y-glides: ㅛ, ㅠ, ㅑ, ㅕ

In handwriting and type, the dot lengthened into a short stroke. The original ㆍ, now called *arae-a* “lower a,” disappeared from standard Korean spelling but survives in historical transcription and limited Jeju-related use.

## 4. Original 1446 inventory

The promulgation presents the consonants in a phonological order rather than modern dictionary order:

ㄱ ㅋ ㆁ ㄷ ㅌ ㄴ ㅂ ㅍ ㅁ ㅈ ㅊ ㅅ ㆆ ㅎ ㅇ ㄹ ㅿ

and the vowels:

ㆍ ㅡ ㅣ ㅗ ㅏ ㅜ ㅓ ㅛ ㅑ ㅠ ㅕ

### Original consonants

| No. | Letter | Unicode representation | Conventional historical name | Approximate Middle Korean value/function | Modern status |
|---:|---|---:|---|---|---|
| 1 | ㄱ | U+3131; choseong ᄀ U+1100 | *kiyeok* later | /k~g/ | Modern |
| 2 | ㅋ | U+314B; ᄏ U+110F | *khieukh* | aspirated /kʰ/ | Modern |
| 3 | ㆁ | U+3181; initial ᅌ U+114C, final ᆼ U+11BC | *yes-ieung*, “old ieung” | /ŋ/, including initial /ŋ/ | Obsolete as a distinct initial; merged graphically/functionally with ㅇ in modern practice |
| 4 | ㄷ | U+3137; ᄃ U+1103 | *tikeut/digeut* | /t~d/ | Modern |
| 5 | ㅌ | U+314C; ᄐ U+1110 | *thieuth* | /tʰ/ | Modern |
| 6 | ㄴ | U+3134; ᄂ U+1102 | *nieun* | /n/ | Modern |
| 7 | ㅂ | U+3142; ᄇ U+1107 | *pieup/bieup* | /p~b/ | Modern |
| 8 | ㅍ | U+314D; ᄑ U+1111 | *phieuph* | /pʰ/ | Modern |
| 9 | ㅁ | U+3141; ᄆ U+1106 | *mieum* | /m/ | Modern |
| 10 | ㅈ | U+3148; ᄌ U+110C | *cieuc/jieut* | affricate /ts~dz/ | Modern; later palatalized |
| 11 | ㅊ | U+314A; ᄎ U+110E | *chieuch* | /tsʰ/ | Modern; later palatalized |
| 12 | ㅅ | U+3145; ᄉ U+1109 | *sios* | /s/ with conditioned variants | Modern |
| 13 | ㆆ | U+3186; ᅙ U+1159 | *yeorin-hieuh*, “light hieuh” | glottal/laryngeal sign, often reconstructed /ʔ/ | Obsolete |
| 14 | ㅎ | U+314E; ᄒ U+1112 | *hieuh* | /h/, laryngeal/aspirating functions | Modern |
| 15 | ㅇ | U+3147; ᄋ U+110B | *ieung* later | initial zero; associated with throat class | Modern; final form represents /ŋ/ |
| 16 | ㄹ | U+3139; ᄅ U+1105 | *rieul* | liquid /r~l/ | Modern |
| 17 | ㅿ | U+317F; ᅀ U+1140 | *bansiot*, “half-siot” | lenited sibilant, commonly reconstructed /z/ | Obsolete by the early modern period |

The later names are not given as a complete modern-style nomenclature in the 1446 promulgation. Choe Sejin’s *Hunmong jahoe* 訓蒙字會 of 1527 furnished the basis of the familiar names by using Chinese characters to show initial and final values. **[Documented text]** [Academy of Korean Studies entry](https://encykorea.aks.ac.kr/Article/E0065801)

### Original vowels

| No. | Letter | Unicode | Approximate Middle Korean value | Construction/status |
|---:|---|---:|---|---|
| 1 | ㆍ | U+318D | conventionally /ʌ/ or a low/back central vowel; exact quality disputed | Heaven-dot; obsolete in standard Korean |
| 2 | ㅡ | U+3161; ᅳ U+1173 | /ɯ/ | Earth |
| 3 | ㅣ | U+3163; ᅵ U+1175 | /i/ | Human |
| 4 | ㅗ | U+3157; ᅩ U+1169 | /o/ | Dot above ㅡ |
| 5 | ㅏ | U+314F; ᅡ U+1161 | /a/ | Dot right of ㅣ |
| 6 | ㅜ | U+315C; ᅮ U+116E | /u/ | Dot below ㅡ |
| 7 | ㅓ | U+3153; ᅥ U+1165 | /ə/ | Dot left of ㅣ |
| 8 | ㅛ | U+315B; ᅭ U+116D | /jo/ | Doubled dot above |
| 9 | ㅑ | U+3151; ᅣ U+1163 | /ja/ | Doubled dot right |
| 10 | ㅠ | U+3160; ᅲ U+1172 | /ju/ | Doubled dot below |
| 11 | ㅕ | U+3155; ᅧ U+1167 | /jə/ | Doubled dot left |

Compound vowels such as ㅐ, ㅔ, ㅘ, ㅝ, ㅢ were constructed from these elements. Some represented diphthongs in Middle Korean but became monophthongs or merged in later speech.

## 5. Modern basic inventory and order

### Modern consonants

| South Korean order | Letter | South Korean name | North Korean name where different | Initial value, approximate | Final value, approximate | Number value |
|---:|---|---|---|---|---|---|
| 1 | ㄱ | 기역 *giyeok* | 기윽 *kiŭk* | /k~ɡ/ | /k̚/ | None |
| 2 | ㄲ | 쌍기역 *ssanggiyeok* | 된기윽 *toen-kiŭk* | tense /k͈/ | /k̚/ | None |
| 3 | ㄴ | 니은 *nieun* | same | /n/ | /n/ | None |
| 4 | ㄷ | 디귿 *digeut* | 디읃 *tiŭt* | /t~d/ | /t̚/ | None |
| 5 | ㄸ | 쌍디귿 *ssangdigeut* | 된디읃 | tense /t͈/ | normally not final | None |
| 6 | ㄹ | 리을 *rieul* | same | /ɾ~l/ | /l/ | None |
| 7 | ㅁ | 미음 *mieum* | same | /m/ | /m/ | None |
| 8 | ㅂ | 비읍 *bieup* | same, conventionally *piŭp* | /p~b/ | /p̚/ | None |
| 9 | ㅃ | 쌍비읍 *ssangbieup* | 된비읍 | tense /p͈/ | normally not final | None |
| 10 | ㅅ | 시옷 *siot* | 시읏 *siŭt* | /s/, [ɕ] before /i, j/ | /t̚/ | None |
| 11 | ㅆ | 쌍시옷 *ssangsiot* | 된시읏 | tense /s͈/ | /t̚/ | None |
| 12 | ㅇ | 이응 *ieung* | same | silent onset | /ŋ/ | None |
| 13 | ㅈ | 지읒 *jieut* | same | /tɕ~dʑ/ | /t̚/ | None |
| 14 | ㅉ | 쌍지읒 *ssangjieut* | 된지읒 | tense /tɕ͈/ | normally not final | None |
| 15 | ㅊ | 치읓 *chieut* | same | /tɕʰ/ | /t̚/ | None |
| 16 | ㅋ | 키읔 *kieuk* | same | /kʰ/ | /k̚/ | None |
| 17 | ㅌ | 티읕 *tieut* | same | /tʰ/ | /t̚/ | None |
| 18 | ㅍ | 피읖 *pieup* | same | /pʰ/ | /p̚/ | None |
| 19 | ㅎ | 히읗 *hieut* | same | /h/ | /t̚/ or conditioning aspiration | None |

North Korea ordinarily places the simple consonants first and the tense composites later; its dictionary treatment of onset ㅇ also differs because it has no onset sound. South Korean collation interleaves ㄲ after ㄱ, ㄸ after ㄷ, and so forth. [National Hangeul Museum comparison](https://www.hangeul.go.kr/webzine/201806/sub1_1.html)

### Modern vowels

| South Korean order | Letter | Name | Approximate contemporary value | Origin |
|---:|---|---|---|---|
| 1 | ㅏ | 아 *a* | /a/ | Basic |
| 2 | ㅐ | 애 *ae* | /ɛ~e/ | ㅏ + ㅣ |
| 3 | ㅑ | 야 *ya* | /ja/ | Basic y-vowel |
| 4 | ㅒ | 얘 *yae* | /jɛ~je/ | ㅑ + ㅣ |
| 5 | ㅓ | 어 *eo* | /ʌ/ | Basic |
| 6 | ㅔ | 에 *e* | /e/ | ㅓ + ㅣ |
| 7 | ㅕ | 여 *yeo* | /jʌ/ | Basic y-vowel |
| 8 | ㅖ | 예 *ye* | /je/ | ㅕ + ㅣ |
| 9 | ㅗ | 오 *o* | /o/ | Basic |
| 10 | ㅘ | 와 *wa* | /wa/ | ㅗ + ㅏ |
| 11 | ㅙ | 왜 *wae* | /wɛ~we/ | ㅗ + ㅐ |
| 12 | ㅚ | 외 *oe* | /we/ or [ø] conservatively | ㅗ + ㅣ |
| 13 | ㅛ | 요 *yo* | /jo/ | Basic y-vowel |
| 14 | ㅜ | 우 *u* | /u/ | Basic |
| 15 | ㅝ | 워 *wo* | /wʌ/ | ㅜ + ㅓ |
| 16 | ㅞ | 웨 *we* | /we/ | ㅜ + ㅔ |
| 17 | ㅟ | 위 *wi* | /wi/ or [y] conservatively | ㅜ + ㅣ |
| 18 | ㅠ | 유 *yu* | /ju/ | Basic y-vowel |
| 19 | ㅡ | 으 *eu* | /ɯ/ | Basic |
| 20 | ㅢ | 의 *ui* | /ɰi/, with positional reductions | ㅡ + ㅣ |
| 21 | ㅣ | 이 *i* | /i/ | Basic |

The merger of ㅐ and ㅔ in much contemporary Seoul speech is phonological, not orthographic: they remain distinct letters and spellings.

## 6. Letter names and the acrophonic question

Hangul’s consonant names are not inherited picture-names like Semitic *ʾālep* “ox” or *bēt* “house.” They are pedagogical frames designed to pronounce a consonant both initially and finally:

- ㄴ: 니은 *ni-eun*, initial /n/ and final /n/
- ㅁ: 미음 *mi-eum*
- ㅂ: 비읍 *bi-eup*

The irregular South Korean names 기역, 디귿, 시옷 preserve Choe Sejin’s 1527 Chinese-character mnemonics and the limited inventory of Chinese syllables he could use. North Korea regularized these as 기윽, 디읃, 시읏.

Thus:

- **Acrophony in the Semitic historical sense:** absent.
- **Pedagogical initial/final framing:** present.
- **Pictorial meanings attached to individual consonants:** articulatory, not lexical.
- **Numerical ordering:** absent.

## 7. Vowels: not an abjad problem

Hangul is a fully vocalic alphabet. Every ordinary syllable block contains a medial vowel letter. A vowel-initial syllable uses silent ㅇ as a graphic onset:

- 아 = ㅇ + ㅏ
- 우 = ㅇ + ㅜ

There are no *matres lectionis*, optional vowel points, or a Greek-style historical conversion of consonant letters into vowels. The vowels were designed as a distinct subsystem from the outset.

**[Documented text]** The 1446 work explicitly calls them “medial sounds” and gives eleven signs.

## 8. Ligatures and complex jamo

Hangul has structures resembling ligatures, but several distinctions matter:

1. **Syllable blocks** are normal graphic compositions, not lexical ligatures.
2. **Double consonants** ㄲ, ㄸ, ㅃ, ㅆ, ㅉ express tense consonants in modern Korean.
3. **Final clusters** such as ㄳ, ㄵ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, and ㅄ combine two consonant letters in a single final slot.
4. **Compound vowels** such as ㅘ and ㅢ are conventional combinations.
5. Early texts also used now-obsolete compounds for Korean and for transcribing Chinese, Japanese, Mongolian, Jurchen, and Manchu sounds.
6. The “light labials,” including ㅸ, were made by placing ㅇ beneath a labial consonant. Their exact phonetics and design history are specialized questions.

Unicode treats many historical leading, medial, and trailing compounds as separate conjoining jamo because their positional behavior must be encoded.

## 9. Tone marks and diacritics

Middle Korean texts used *bangjeom* 傍點, “side dots,” placed to the left of a syllable:

| Mark | Traditional category | Modern interpretation |
|---|---|---|
| none | level tone 平聲 | commonly reconstructed low pitch |
| 〮 | departing tone 去聲 | commonly reconstructed high pitch |
| 〯 | rising tone 上聲 | commonly reconstructed low-high contour |
| no independent dot rule | entering tone 入聲 | associated with checked syllable structure rather than a separate pitch sign |

**[Documented artefact/text]** These dots occur in early printed Hangul.

**[Disputed analysis]** The creators mapped Korean onto Chinese tone terminology. Modern specialists debate whether Middle Korean had lexical tone, pitch accent, or a system best analyzed through moraic pitch. The marks are evidence of contrast; the precise phonological analysis is reconstructed.

The marks declined during the sixteenth century as the relevant prosodic system changed. Unicode encodes:

- U+302E HANGUL SINGLE DOT TONE MARK
- U+302F HANGUL DOUBLE DOT TONE MARK

Their digital classification and spacing behavior required later correction because they appear to the left of a syllable in both horizontal and vertical presentation. [Unicode proposal L2/11-402](https://www.unicode.org/L2/L2011/11402-bangjeom.pdf)

## 10. Punctuation and spacing

Early Hangul followed East Asian manuscript and printing practice:

- text commonly ran continuously without Western word spacing;
- small circles or dots marked syntactic or textual divisions;
- punctuation interacted with vertical columns and with Hanja annotation;
- tone dots were distinct from punctuation even when visually similar.

Modern punctuation largely follows international print conventions: comma, full stop, colon, semicolon, quotation marks, parentheses, question mark, and exclamation mark. Vertical typesetting rotates or repositions appropriate marks.

Word spacing was systematized under modern print influence. Seo Jae-pil’s *Dongnip sinmun* / *The Independent* from 1896 is particularly associated with Hangul prose, simplified syntax, and spacing. The Korean Language Society’s 1933 orthography regularized spacing, though it remains one of the most complex parts of Korean orthography.

## 11. Capitals and minuscules

**[Absence of evidence]** Hangul never developed a historical bicameral system. There is no indigenous equivalent of Greek/Latin majuscule versus minuscule.

Modern designers sometimes create display forms that imitate capitalization, linearize blocks, or enlarge initials. These are **[modern inventions]**, not standard orthography.

## 12. Direction

- Fifteenth-century books: vertical, top-to-bottom, columns right-to-left.
- Nineteenth- and early twentieth-century print: vertical remained dominant, often in Hangul–Hanja mixed script.
- Twentieth century: horizontal left-to-right progressively became normal.
- Contemporary Korean: overwhelmingly horizontal left-to-right in digital and everyday print.
- Vertical writing survives in signs, book design, calligraphy, and ceremonial typography.
- **Boustrophedon:** no documented period of use.

---

# Origins

## 1. Before Hangul: writing Korean with Chinese graphs

Before the fifteenth century, Korean speakers used:

- Literary Chinese for government, scholarship, diplomacy, and historiography.
- **Idu** 吏讀, adapting Chinese graphs to Korean words and grammatical endings.
- **Hyangchal**, especially associated with vernacular poetry.
- **Gugyeol**, glossing and parsing Literary Chinese for Korean reading.
- Phonographic use of Hanja in names and transcriptions.

These systems could represent Korean, but they required mastery of Chinese characters and offered no compact, purpose-built alphabet for Korean phonology.

**[Scholarly reconstruction]** “Hangul was invented because Chinese cannot write Korean at all” is an overstatement. Chinese-derived systems did write Korean, but at considerable educational and structural cost. Sejong’s preface says Korean speech “does not accord with Chinese letters,” not that no representation had ever existed.

## 2. 1443: first secure attestation

The *Sejong sillok*, 25th regnal year, twelfth month, records:

> 是月上親制諺文二十八字  
> “This month the king personally devised twenty-eight vernacular letters.”

It adds that the letters are divided into initial, medial, and final sounds and can be combined to write words.

**Status:** **[Documented text]**, the earliest secure surviving attestation.

**Date:** The twelfth lunar month of Sejong 25 overlaps late December 1443 and January 1444 in the proleptic Gregorian calendar. Consequently, “invented in 1443” is conventional but “completed on a particular day in 1443” is not documented.

**Place:** The Joseon royal court at Hanseong, modern Seoul.

**Object:** The annal is a transmitted official historiographical record, not Sejong’s autograph notebook. The Joseon annals are preserved in multiple historical repositories and are registered by UNESCO.

## 3. 1444: Ch’oe Malli’s memorial

On 5 March 1444 in a commonly used Gregorian conversion, Ch’oe Malli and other Hall of Worthies officials submitted a memorial criticizing the new *ŏnmun*, “vernacular script.”

Their objections included:

- departure from the civilization centered on Chinese writing;
- fear that Korea would resemble peoples using non-Chinese scripts;
- concern that a simpler script might weaken Chinese learning;
- objection to rapid implementation and to associated phonological work;
- criticism that the crown prince was being burdened with the project;
- doubt that legal clerks would become morally or intellectually better merely by learning an easy script.

They nevertheless called the invention extraordinary—“divine creation unparalleled in history”—before arguing against its policy implications.

**Status:** **[Documented text]**. [Translation from the *Sejong sillok*](https://afe.easia.columbia.edu/main_pop/ps/ps_korea-alphabet-dissent.htm)

### What the memorial proves

It proves that:

- the script existed and was known at court by early 1444;
- Sejong was publicly treated as its creator;
- elite resistance was real;
- Chinese cultural allegiance and policy concerns were central;
- work on Chinese pronunciation and the *Yunhui* rhyme-book tradition was entangled with the project.

It does **not** prove that all yangban opposed Hangul, that elites universally wanted commoners permanently illiterate, or that the Hall of Worthies as an institution had secretly invented it for Sejong.

## 4. 1444–1446: testing and application

Sejong directed work using the new letters for Korean and Sino-Korean phonology. Scholars associated with the later commentary included:

- Jeong Inji 鄭麟趾 (1396–1478)
- Choe Hang 崔恒 (1409–1474)
- Pak Paengnyeon 朴彭年 (1417–1456)
- Sin Sukju 申叔舟 (1417–1475)
- Seong Sammun 成三問 (1418–1456)
- Kang Huian 姜希顔 (1417–1464)
- Yi Gae 李塏 (1417–1456)
- Yi Seonro 李善老

**[Documented text]** Jeong Inji’s postface names the explanatory enterprise. Contemporary sources attribute the core creation to Sejong and the explanation and applications to scholars.

## 5. 1446: promulgation and the *Haerye*

The *Hunminjeongeum* was published in the ninth lunar month of 1446. It includes:

1. Sejong’s short promulgation text and examples.
2. The *Haerye* 解例, “Explanations and Examples.”
3. Jeong Inji’s postface.

Sejong’s famous preface begins:

> 國之語音異乎中國 與文字不相流通  
> “The speech of this country differs from that of China and does not accord with Chinese writing.”

It concludes that he has made twenty-eight letters so that people may learn and use them conveniently.

The *Haerye* adds a pedagogical claim:

> “A wise person may acquaint himself with them before the morning is over; a dull person can learn them in ten days.”

**Status:** **[Documented text]**. The manuscript is not merely a later story about the invention: it contains the creators’ own contemporary rationale.

### Date caution

The annals say that the work was completed “in this month.” Jeong Inji’s postface is dated to the first ten days of the ninth month, but no surviving statement identifies the Gregorian 9 October as the exact promulgation day.

Therefore:

- “Published in the ninth lunar month of 1446”: documented.
- “Promulgated exactly on 9 October 1446”: **[tradition/commemorative reconstruction]**.
- South Korea’s Hangul Day date is historically reasoned, not an exact anniversary securely stated by the primary source.

## 6. The surviving *Haerye* manuscript

### Kansong copy

| Field | Record |
|---|---|
| Conventional name | Kansong copy of the *Hunminjeongeum Haerye* |
| Date | Text published 1446; surviving copy generally treated as a fifteenth-century witness, though whether every surviving leaf is original has been questioned |
| Rediscovery | 1940, from Andong |
| Collector | Jeon Hyeong-pil 全鎣弼 (1906–1962), pen name Kansong |
| Present repository | Kansong Art Museum, Seoul |
| Korean designation | National Treasure No. 70, designated 1962 |
| UNESCO | Memory of the World, registered 1997 |
| Format | One volume, 33 leaves; two opening leaves are restorations/replacements rather than original leaves |

UNESCO describes the manuscript as containing the promulgation, *Haerye*, and Jeong Inji’s postface. [UNESCO object record](https://www.unesco.org/en/memory-world/hunminjeongum-manuscript)

**[Documented artefact]** The manuscript survives.

**[Disputed detail]** Some scholars, including Pang Chonghyeon as reported by Ledyard, considered the witness authentic but possibly a later pre-Imjin-War copy rather than the actual 1446 impression. The underlying 1446 text is independently corroborated by the *Sejong sillok* and later editions.

### Sangju copy

In 2008 Bae Ik-gi announced another copy at Sangju and released limited photographs. Litigation concluded that it had been unlawfully obtained and that ownership belonged to the state through the prior owner’s donation; Bae has not surrendered it.

**Status:** **[Documented modern claim with partially documented artefact]**. Photographs support the existence of material, but lack of full scholarly access prevents complete codicological and textual verification. Claims about its condition, completeness, market value, or destruction should remain provisional. [Korea Times account of the litigation](https://www.koreatimes.co.kr/southkorea/society/20190717/court-ruling-re-sparks-tug-of-war-over-priceless-hangeul-handbook)

## 7. Was there a “decipherment”?

No Champollion- or Ventris-like decipherment was required. Hangul was introduced with explicit phonetic explanations and examples, remained in use, and was transmitted through later spelling books and vernacular editions.

The rediscovery of the full *Haerye* in 1940 was nevertheless interpretively transformative: it replaced speculative external-origin theories with a contemporary explanation of the design.

**[Absence of evidence]** There was no lost-script decipherment event or single “decipherer.”

---

# The parent-script and borrowing question

## 1. The official account

The *Haerye* says the basic consonants imitate speech organs and that related letters are made by adding strokes. It derives the vowels from the Three Powers, Heaven, Earth, and Human.

This is **[documented contemporary theory]**. It is direct evidence of how the promulgators wanted the construction understood. It does not exclude every external visual or conceptual stimulus, but any competing theory must explain why the contemporary description is so systematic.

The promulgation also says the letters were made “in imitation of the forms of the old seal script” (*guzhuan* 古篆). Interpretations include:

- a general claim that the characters belong within respectable East Asian graph-making;
- reference to the graphic principle of pictorial derivation;
- a more specific allusion to another script called or perceived as “old seal.”

The phrase is genuine; its exact referent is disputed.

## 2. Gari Ledyard’s ʼPhags-pa hypothesis

Gari Ledyard’s 1966 dissertation, revised and published in 1998 as *The Korean Language Reform of 1446*, argued that:

- Sejong’s project was situated in a Eurasian environment where Mongol imperial writing and ʼPhags-pa were known;
- a small core of consonant shapes—the “five letters” he isolated—may have been transformed from ʼPhags-pa models;
- Sejong then reorganized them through articulatory principles and generated the rest featurally;
- ʼPhags-pa was therefore a stimulus, not a full parent that explains the entire Korean system.

Evidence advanced includes selected shape/sound correspondences, historical Korean access to Yuan linguistic materials, and the ambiguous “old seal” phrase.

### Evidence against or limiting the hypothesis

Critics argue:

- the *Haerye* supplies an internally coherent articulatory derivation;
- visual resemblance among simple geometric signs is weak evidence;
- proposed correspondences require rotation, simplification, or selective matching;
- no workshop draft, order, colophon, or contemporary statement names ʼPhags-pa;
- the vowels, syllable arrangement, derivative strokes, and system-wide phonological design are not explained by ordinary descent from ʼPhags-pa.

**Assessment:** **[Disputed scholarly reconstruction]**. A limited ʼPhags-pa stimulus is plausible to some specialists; direct genealogical descent of Hangul as a whole is not demonstrated. Calling ʼPhags-pa simply “the parent of Hangul” overstates Ledyard’s own nuanced proposal.

## 3. Other proposed parents

Older writers proposed relationships to:

- Tibetan
- Sanskrit/Indic scripts
- Uighur-Mongolian
- Hebrew
- Chinese seal forms
- Japanese kana
- ancient Korean scripts

Most rested on superficial graphic comparison and were seriously weakened by the 1940 recovery of the *Haerye*.

### Garimto and “ancient Hangul”

Claims that Hangul reproduces an ancient Korean alphabet called *Garimto* depend on the *Hwandan gogi*, first made public in the twentieth century and widely regarded by historians as a modern compilation or forgery.

**Status:** **[Modern nationalist claim/disputed forgery tradition]**. There is no securely excavated pre-fifteenth-century Garimto inscription, no contemporaneous manuscript chain, and no accepted palaeographic sequence connecting it to Hangul.

### Japanese *jindai moji*

Some Japanese “Age of the Gods characters” resemble Hangul. Mainstream scholarship dates relevant examples after Hangul’s creation and treats many as early-modern or modern fabrications.

**Status:** resemblance is documented; priority over Hangul is unsupported.

---

# Spread and change

## 1. 1446–1450: royal deployment

The script’s earliest uses were state-sponsored and intellectually ambitious, not merely elementary literacy exercises.

### Principal early works

- **Hunminjeongeum** (1446): promulgation and technical account.
- **Yongbieocheonga** 龍飛御天歌, *Songs of the Dragons Flying to Heaven* (1447): dynastic praise and the first major extended work in the new script.
- **Dongguk jeongun** 東國正韻 (1447–1448): a rhyme dictionary prescribing Sino-Korean pronunciation.
- **Seokbo sangjeol** 釋譜詳節 (1447): Buddhist biography and translation associated with Prince Suyang.
- **Worin cheongang jigok** 月印千江之曲 (c. 1447–1449): Sejong’s Buddhist songs.
- Later Buddhist translations and vernacular glosses extended its practical domain.

**[Documented artefacts/texts]** Surviving early printed witnesses show Hangul being used for Korean prose, verse, Chinese phonology, and Buddhist teaching.

This complicates the modern slogan that the script was created only so peasants could write complaints. Sejong’s preface emphasizes ordinary people, but royal language planning, legal clarity, pronunciation reform, translation, and state pedagogy were also involved.

## 2. Fifteenth- and sixteenth-century sound change

The script was designed for Middle Korean and initially recorded contrasts later lost:

- ㅿ disappeared as its sound merged or was lost.
- ㆆ disappeared.
- initial ㆁ ceased to be distinct.
- ㆍ gradually merged with other vowels; its loss proceeded differently by dialect.
- the original pitch system changed, and *bangjeom* fell out of use.
- vowel combinations changed phonetically.
- consonant clusters and tense consonants were reanalyzed.

The script therefore did not remain a phonetic snapshot. Orthography accumulated historical and morphophonemic conventions.

## 3. Yeonsangun’s restrictions, 1504

After Hangul placards criticizing King Yeonsangun appeared, the king ordered restrictions involving vernacular-script materials and informants.

**[Documented text]** Annal entries support a punitive episode.

**Qualification:** “Hangul was totally banned for centuries” is false. Restrictions were episodic; royal, religious, domestic, and literary Hangul use continued. The episode may help explain stories that owners concealed Hangul books, but it does not establish the particular provenance legend attached to every damaged copy.

## 4. Choe Sejin and standard pedagogical order, 1527

Choe Sejin’s *Hunmong jahoe*, a primer for Chinese characters, placed Hangul letters in a pedagogically useful order and provided letter-name mnemonics. The familiar *ganada* order ultimately descends from this tradition.

The irony is instructive: Hangul spread partly through tools intended to teach Hanja. The two scripts were usually complementary rather than immediately antagonistic.

## 5. Vernacular letters and everyday writing

From the sixteenth century onward, surviving *eongan* 諺簡—vernacular letters—document use by:

- royal family members;
- aristocratic men and women;
- court women;
- husbands and wives;
- officials and household members;
- eventually lower-status writers.

The corpus is uneven because preservation favored elite households. It nonetheless disproves the idea that Hangul was exclusively female.

## 6. “Women’s script”

Names applied to Hangul included:

- *jeongeum* 正音, “correct sounds”
- *eonmun* 諺文, “vernacular writing”
- *banjeol*
- *gukmun* 國文, “national writing”
- *amgeul/amkeul*, “women’s writing”
- *Hangul*, from the early twentieth century

**[Documented social history]** Women, especially in elite households and the palace, became major readers, copyists, correspondents, and authors in Hangul. Court women developed *gungche*, “palace hand,” and copied long vernacular novels. Women wrote practical texts including household and culinary books.

**[Disputed characterization]** “Women’s script” can report an actual social association, but it is misleading as a formal name or exclusive function. Men wrote Hangul from its first decades, including the king, princes, monks, translators, husbands, scholars, printers, and officials.

**[Scholarly reconstruction]** Gender segregation in education helped create a division: elite men were trained in Literary Chinese, while women excluded from that curriculum could use vernacular writing. The lower prestige of women’s literacy could both marginalize Hangul and give it a durable domestic domain. [Study of women’s contribution to Joseon Hangul](https://www.kci.go.kr/kciportal/ci/sereArticleSearch.pib?arti_id=ART002278069)

## 7. Literature

Hangul enabled or expanded:

- translations of Buddhist and Confucian texts;
- *sijo* and *gasa* verse;
- vernacular fiction;
- court memoirs;
- family letters;
- women’s instructional literature;
- cookbooks and household encyclopedias;
- popular printed tales.

Major examples include:

- Queen Sohye’s *Naehun* 內訓 (1475), instruction for women in mixed and translated form;
- *Hong Gildong jeon*, traditionally associated with Heo Gyun, though authorship and textual history are disputed;
- *Inhyeon wanghu jeon*, an anonymous court narrative;
- Lady Hyegyeong’s *Hanjungnok* memoirs (1795–1805);
- long family novels copied and consumed in palace women’s communities.

**[Documented artefact]** Manuscripts and woodblock editions survive.

**[Disputed attribution]** Many vernacular novels circulated anonymously; later claims assigning them to famous men or court women often exceed the evidence.

## 8. Calligraphy

Three broad modern museum categories are commonly used:

1. **Panbonche / 판본체**, “woodblock-edition style”: square, balanced, geometrical forms associated with early printing.
2. **Gungche / 궁체**, “palace style”: developed through court women’s manuscript practice; includes formal and cursive varieties.
3. **Minche / 민체**, “folk or popular hand”: a broad category for less formally standardized vernacular hands.

These are classificatory umbrellas, not three immutable scripts created simultaneously in 1446. Individual manuscripts show extensive variation.

Hangul calligraphy interacted with brush technique inherited from Chinese calligraphy, but its block structure required distinctive spacing, stroke proportion, and internal balance.

## 9. Printing

Korea possessed woodblock printing and movable metal type before Hangul; *Jikji* was printed with metal type in 1377. Hangul therefore entered an advanced print culture.

Early Hangul printing faced a paradox:

- only 28 basic letters were conceptually needed;
- but block typography could require many positional forms or whole syllable sorts;
- mixed Hangul–Hanja books required coordination between two typographic systems.

Woodblocks allowed precise custom blocks. Metal type required systems for variant jamo positions, precomposed syllables, or both.

Surviving Korean collections contain hundreds of thousands of metal sorts, including Hangul types from later dynastic series. [Study of National Museum of Korea Hangul metal type](https://www.ijkaa.org/v.4/0/116/93?view=pubreader)

## 10. Nineteenth-century reform and 1894 official status

Missionaries, reformers, newspapers, and educators expanded vernacular print. Mixed Hangul–Hanja became an important modern public style.

During the Gabo reforms, Royal Ordinance No. 1 on official document forms, dated 21 November 1894, prescribed that laws and ordinances take *gukmun* as their base, with Chinese translation added or mixed script used where appropriate.

**Status:** **[Documented legal text]**. This is the basis for the statement that Hangul acquired official national standing in 1894. [Academy of Korean Studies](https://encykorea.aks.ac.kr/Article/E0061508)

Qualification: it did not instantly eliminate Literary Chinese or Hanja. Administrative habit, educational prestige, and mixed-script publishing continued.

## 11. *The Independent* and modern public prose

Seo Jae-pil’s *Dongnip sinmun*, founded in 1896, used Hangul prominently and promoted accessible public prose. It helped normalize:

- vernacular journalism;
- word spacing;
- modern punctuation;
- a broad reading public;
- the concept of Hangul as a national civic medium.

## 12. Ju Sigyeong and the name “Hangul”

Ju Sigyeong 周時經 (1876–1914) was central to modern Korean linguistic analysis and script reform.

**[Disputed attribution]** He is often said to have coined *Hangul*, but the precise author and first occurrence are uncertain. The name is securely visible in records from the early 1910s; an important attestation is associated with the 23 March 1913 renaming of a language society to *Hangulmo*. The National Hangeul Museum accordingly says that the term began to be used in the early 1910s rather than identifying an uncontested single coinage. [Museum account](https://m.hangeul.go.kr/lang/en/html/education/Hangeul.do)

Possible meanings include “great script,” “Korean script,” or “one/unified script,” but confident etymological slogans are partly retrospective.

## 13. Japanese colonial rule, 1910–1945

The colonial history must be divided into phases.

### Early and “cultural rule” phases

Japanese was the language of colonial authority, but Korean-language education and print did not disappear immediately. Korean newspapers, textbooks, religious publications, and scholarship continued under censorship and unequal conditions.

### Intensification after 1937–1938

With wartime mobilization and assimilation policy:

- Korean instruction was progressively reduced;
- under the 1938 educational regime Korean ceased to be compulsory and was then eliminated from significant school contexts;
- Japanese-language use was aggressively promoted;
- Korean publications faced closure and restriction;
- public and private pressure favored Japanese names and Japanese linguistic identity.

### Korean Language Society Incident, 1942

Colonial police arrested members of the Korean Language Society, disrupted dictionary compilation, and prosecuted scholars under security law. Yi Yunjae (1888–1943) and Han Jing (1886–1944) died in prison.

**Status:** **[Documented historical event]**. [Korean Language Society history](https://eng.hangeul.or.kr/homepage/custom/Colonial)

### Necessary qualification

“Japan banned Hangul for all thirty-five colonial years” is inaccurate. Policy varied and Korean publishing continued for much of the period. “The late colonial state systematically suppressed Korean-language education and scholarship” is well documented.

## 14. Orthographic reform, 1933

The Korean Language Society’s *Unified Hangul Orthography* of 1933 established a strongly morphophonemic framework:

- morphemes should retain recognizable spelling despite phonetic alternation;
- spacing and grammatical conventions were regularized;
- letter order and names were standardized;
- the spelling system became the main ancestor of both present-day Korean orthographies.

It was not pure phonetic writing. For example, underlying morphological structure may be preserved even when surface pronunciation assimilates.

## 15. Hangul Day

- 1926: the Korean Language Research Society celebrated *Gagyanal* on lunar 29 September, believing it the 480th anniversary of promulgation.
- 1928: the name changed to *Hangulnal*, Hangul Day.
- After liberation: South Korea fixed 9 October in the solar calendar.
- 1949: designated a public holiday.
- 1991: removed from the public-holiday calendar.
- 2006: elevated to national-holiday status.
- 2013: restored as a day off.
- North Korea observes *Chosŏn’gŭl Day* on 15 January, commemorating creation rather than the southern promulgation date.

**[Documented institutional history]** [National Institute of Korean Language history](https://www.korean.go.kr/nkview/news/10/102.htm)

## 16. Liberation, division, and the North–South split

Both emerging states inherited the 1933 reform but developed different policies.

### Shared structure

Both use essentially the same modern phonemic jamo and syllable-block mechanism. Ordinary northern and southern Hangul remain mutually legible.

### South Korea

- Retained historical names such as 기역, 디귿, 시옷.
- Counts 24 basic letters.
- Interleaves tense consonants and compound vowels in collation.
- Applies the *du-eum* rule, changing certain word-initial Sino-Korean ㄴ and ㄹ: southern 여자 *yeoja*, northern 녀자 *nyŏja*; southern 이, northern 리 in relevant surnames/words.
- Revised official orthography in 1988 and subsequently amended it.
- Hanja persisted in mixed script longer and remains available in limited domains, though Hangul-only writing dominates.

### North Korea

- Calls the script *Chosŏn’gŭl*.
- Counts 40 when doubled consonants and compound vowels are included.
- Regularized names: 기윽, 디읃, 시읏; uses *doen-* rather than Sino-Korean *ssang-* for tense letters.
- Orders simple signs before composites in many official lists.
- Uses more morphologically conservative initial ㄴ/ㄹ spellings.
- Eliminated routine Hanja use much earlier and more completely.
- Generally uses fewer word spaces by grouping compounds differently.

### The 1948 “New Korean Orthography”

North Korean linguists proposed six new morphophonemic jamo—five consonants and one vowel—to represent alternations more abstractly. It was officially associated with reform from 1948 but met practical opposition and was abandoned by 1954.

**Status:** **[Documented modern reform]**, not evidence that ordinary North Korean Hangul today contains six extra spoken phonemes. [Unicode proposal documenting the six letters](http://www.unicode.org/L2/L2019/19230-six-hangul-letters.pdf)

## 17. Mechanization and the keyboard

### Typewriters

Hangul’s two-dimensional blocks challenged mechanical typewriters. Early machines used multiple positional sets of jamo. Wonic/Lee Won-ik and Horace Underwood are connected with early twentieth-century designs; exact priority among early machines depends on whether one counts patents, prototypes, or usable production.

Gong Byeong-u 孔炳禹 (1907–1995), an ophthalmologist, introduced an influential three-set typewriter in 1949. Separate keys for initial consonants, vowels, and finals enabled rapid professional composition and generated distinctive type forms.

### Standardization

South Korea’s 1969 state program imposed a four-set mechanical standard amid debate among inventors and users. With electronic systems, the government selected a two-set computer layout in 1982; it became KS X 5002.

On modern *dubeolsik*:

- consonants occupy the left;
- vowels occupy the right;
- software automatically determines initial, medial, and final position;
- Shift produces tense consonants and selected vowels;
- an IME composes keystrokes into precomposed syllables or jamo sequences.

Three-set layouts remain in use among enthusiasts and specialists. The victory of two-set was political, institutional, and path-dependent, not proof of universally superior ergonomics. [Korean National Archives history](https://theme.archives.go.kr/next/hangeulPolicy/mechanization.do)

## 18. Cia-Cia in Indonesia

In July 2009, educators connected with the Hunminjeongeum Society introduced a Hangul-based orthography for Cia-Cia in Baubau, Southeast Sulawesi. Textbooks and local instruction followed; signs in Sorawolio displayed Cia-Cia in Hangul.

**[Documented modern adaptation]** The program began in 2009. [Cho Tae-young’s 2012 study](https://journal.ugm.ac.id/jurnal-humaniora/article/view/1374)

### What “adoption” means

Reports often said that an Indonesian “tribe” or city had made Hangul its official alphabet. Evidence supports a local educational and preservation project, not national Indonesian replacement of Latin orthography. Indonesia’s language policy and local-government authority limited what could become legally official.

Funding, teacher supply, institutional disagreements, and diplomatic misunderstandings produced interruptions. Later reports and recent Indonesian scholarship show continued or revived cultural use in some locations.

**Assessment:** “Cia-Cia adopted Hangul in 2009” is true in the limited sense of an organized local orthographic program. “Hangul became the exclusive or nationally official script of Cia-Cia” is unsupported.

---

# Digital encoding

## 1. The fundamental encoding problem

A modern Hangul syllable can be represented either as:

- a sequence of conjoining jamo, e.g. ᄒ + ᅡ + ᆫ; or
- one precomposed character, 한.

There are:

- 19 modern leading consonants;
- 21 modern vowels;
- 27 possible final consonants plus no final.

Thus:

19 × 21 × 28 = **11,172** possible modern syllable blocks.

Unicode encodes all of them from U+AC00 가 through U+D7A3 힣. [Unicode Hangul Syllables chart](https://www.unicode.org/charts/nameslist/c_AC00.html)

## 2. Blocks

| Block | Range | Purpose |
|---|---|---|
| Hangul Jamo | U+1100–U+11FF | Conjoining leading, medial, and trailing jamo, including historical forms |
| Hangul Compatibility Jamo | U+3130–U+318F | Spacing forms inherited from Korean standards |
| Hangul Jamo Extended-A | U+A960–U+A97F | Additional historical leading consonants |
| Hangul Syllables | U+AC00–U+D7A3 | 11,172 precomposed modern blocks |
| Hangul Jamo Extended-B | U+D7B0–U+D7FF | Additional historical vowels and final consonants |
| Halfwidth Hangul | U+FFA0–U+FFDC | Compatibility forms for East Asian legacy encoding |

## 3. The “Korean mess” and code-point relocation

Unicode 1.0 encoded 2,350 common syllables based on KS C 5601. Unicode 1.1 expanded the repertoire to 6,646 syllables at U+3400–U+4DFF. This remained incomplete and involved problematic mappings.

For Unicode 2.0, Unicode and ISO/IEC 10646 replaced those blocks with the complete, algorithmically ordered 11,172-syllable Johab set at U+AC00–U+D7A3.

This violated what became Unicode’s cardinal stability principle: assigned characters should never be moved. The old code points were later reassigned, including to CJK Extension A and Yijing symbols. Conversion tables were necessary.

**[Documented standards history]** Unicode acknowledges the old and new inventories; mailing-list archives record 6,646 in version 1.1 and 11,172 from version 2.0. [Unicode archive](https://www.unicode.org/mail-arch/unicode-ml/y2015-m06/0189.html)

**Significance:** the disruption became a major lesson behind Unicode’s subsequent absolute encoding-stability policy.

## 4. Wansung versus Johab

- **Wansung**, “completed,” stores selected precomposed syllables.
- **Johab**, “combined,” represents or systematically generates syllables from components.

The conflict was technical and ideological. Component encoding matched Hangul’s design elegance, but legacy fonts, terminals, and government standards used selected precomposed repertoires. Unicode’s current solution supports both precomposed modern syllables and decomposed jamo.

Old Hangul still depends heavily on correct conjoining-jamo shaping. A string can be valid Unicode while displaying badly in a font without archaic Hangul support.

## 5. Normalization and searching

Modern precomposed Hangul has algorithmic canonical decomposition. Software should treat 한 and its canonically equivalent L–V–T sequence consistently under Unicode normalization.

Compatibility jamo are not interchangeable with conjoining jamo in every context. Their normalization and visual spacing can change behavior. This remains a common source of broken search, cursor movement, fonts, and text processing.

---

# The letters as numbers and signs

## 1. Numerical values

Hangul letters have no traditional fixed numerical values.

- There is no Hangul equivalent of Greek alphabetic numerals.
- No historical Hangul gematria or isopsephy system is securely documented.
- Korean numbers were written through Chinese characters, Korean number words, counting systems, and later Arabic digits.
- Alphabetical list labels such as 가, 나, 다 can function like English A, B, C, but that is ordinal labeling, not numerical value inherent in the letters.

**[Absence of evidence]** No premodern canonical table assigning ㄱ = 1, ㄴ = 2, etc., was found.

Modern numerological schemes that assign values by 가나다 order are **[modern inventions]** unless a specific documented community and date are supplied.

## 2. Cosmological symbolism

Hangul does possess explicit symbolic design, but it is cosmological and phonological rather than numerological:

- Heaven, Earth, Human;
- yin and yang;
- directions and seasons;
- the Five Phases;
- articulatory organs;
- consonantal strength and derivation;
- vowel harmony.

These associations are in the *Haerye* and therefore **[documented text]**, although their exact relationship to the practical design process is open to interpretation.

## 3. Magic and divination

Unlike Hebrew, Greek, Arabic, runes, or Ogham, Hangul did not develop a comparably ancient corpus of letter magic.

**[Absence of evidence]** The sources consulted yielded no premodern Hangul analogue of:

- *Sefer Yetzirah*;
- Greek magical-vowel sequences;
- Arabic *ʿilm al-ḥurūf*;
- alphabetic rune divination;
- letter-number talismans based on inherited numerical values.

Korean talismans and divination historically relied more heavily on Chinese characters, diagrams, calendrical signs, trigrams, stems and branches, Buddhist dhāraṇī, and Daoist graphic traditions.

Hangul can occur on modern charms, souvenirs, occult art, and online numerology, but that is normally **[modern adaptation]** rather than an inherited letter-mystical system.

## 4. Political and sacred symbolism

The opening of the *Hunminjeongeum* has become a quasi-iconic national text. Its archaic orthography appears on:

- monuments;
- museum façades;
- public art;
- typography;
- souvenirs;
- currency-related designs and commemorative material;
- Hangul Day imagery.

King Sejong and the script function as symbols of literacy, national independence, technical ingenuity, and cultural survival.

This symbolism intensified under colonialism and after 1945. It should not be projected unchanged into 1446: the original work was a royal Joseon language project framed through Chinese phonology, Confucian cosmology, and dynastic governance.

---

# People

## Sejong the Great

**Yi Do 李祹, 1397–1450; reigned 1418–1450**

- **[Documented text]** The *Sejong sillok* says the king personally devised the 28 letters.
- He wrote or authorized the promulgation preface.
- He directed phonological, lexicographical, translation, and publishing projects.
- Contemporary opponents addressed him as inventor.
- The degree of private assistance before the announcement remains uncertain.

## Hall of Worthies scholars

Jeong Inji, Choe Hang, Pak Paengnyeon, Sin Sukju, Seong Sammun, Kang Huian, Yi Gae, and Yi Seonro are associated with the *Haerye* and early applications.

**Correction to popular retelling:** “Sejong and the Hall of Worthies jointly invented Hangul” is possible as a loose statement about the broader project but is not what the strongest contemporary evidence says. The records distinguish Sejong’s prior invention from later scholarly explanation and implementation.

## Ch’oe Malli

**died 1445**

Led the 1444 memorial criticizing the project. He was not simply a cartoon villain opposed to peasant literacy. His text combines cultural conservatism, administrative criticism, concerns about Chinese learning, and opposition to connected pronunciation reforms.

## Choe Sejin

**1465–1542**

Linguist and author of *Hunmong jahoe* (1527). His letter order and name mnemonics strongly shaped later teaching.

## Queen Sohye / Queen Insu

**1437–1504**

Compiled *Naehun* in 1475, drawing on Chinese didactic sources but making instruction available through Hangul translation. She exemplifies royal women’s role in vernacular literacy.

## Court women and anonymous scribes

The identities of many palace copyists are lost. Their manuscript labor shaped *gungche*, preserved vernacular fiction, and transmitted royal and household correspondence.

**[Absence of evidence]** A history limited to named male officials systematically erases much of the actual scribal population.

## Seo Jae-pil

**1864–1951**

Reformer and founder of *The Independent* in 1896. Important in modern Hangul journalism, spacing, and accessible public prose.

## Ju Sigyeong

**1876–1914**

Grammarian, teacher, and language reformer. Central to modern analysis of Korean and Hangul. Often credited with the name *Hangul*, though exact coinage is disputed.

## Members of the Korean Language Society

Standardized orthography, compiled dictionaries, and made the script a focus of cultural nationalism. Yi Yunjae and Han Jing died after imprisonment during the 1942 persecution.

## Jeon Hyeong-pil, Kansong

**1906–1962**

Acquired the rediscovered *Haerye* in 1940 and preserved it in the collection now associated with the Kansong Art Museum. Stories about the extraordinary purchase price are institutionally transmitted; the acquisition itself and present object are documented.

## Gong Byeong-u

**1907–1995**

Inventor and advocate of influential three-set typewriters and keyboards. His work helped make rapid Hangul typing practical and generated new typographic aesthetics.

## Choe Jeong-ho

**1916–1988**

A foundational twentieth-century type designer whose drawings shaped newspaper, textbook, metal-type, and phototypesetting faces. Later digital fonts inherit his proportions. [ATypI overview](https://atypi.org/presentation/a-history-of-hangul-typefaces-in-the-20th-century/)

## Ahn Sang-soo

**born 1952**

Designer of the experimental Ahn Sang-soo typeface and a major figure in treating individual jamo and block geometry as a field for modern graphic experimentation. His work challenged conventional square-body proportions without creating a new official orthography.

---

# Legends of invention

## Sejong’s solitary revelation

**[Tradition]** Sejong is sometimes portrayed as creating the entire alphabet alone in a sudden flash of genius.

The evidence does identify him as principal inventor, but it does not preserve drafts, laboratory notes, or every consultation. A complex phonological system probably required sustained research.

## The Hall of Worthies secretly did everything

**[Modern popular counter-legend]** This reverses the royal myth by claiming court scholars invented the system and Sejong took credit.

Contemporary evidence cuts against it:

- the annals call it the king’s personal creation;
- Ch’oe Malli’s faction was surprised and opposed it;
- Jeong Inji’s postface distinguishes the king’s creation from scholarly explanation.

Assistance is plausible; wholesale concealed authorship is undocumented.

## Princess Jeongui solved the blocks

**[Tradition/disputed modern claim]** Stories give Sejong’s daughter Princess Jeongui a decisive role in solving the design or syllable combination. No contemporary record securely establishes this. Modern scholarly defenses rely on later family traditions or inference.

## Window-lattice and door-shape stories

**[Legend/modern folklore]** Popular accounts say Sejong derived letters from lattice windows, palace doors, or patterns glimpsed while confined by illness. These stories are not in the *Haerye* and lack contemporary support.

## Ancient Korean prototype

**[Modern nationalist legend/disputed forgery claim]** Garimto and similar scripts are said to prove that Sejong merely restored a primordial Korean alphabet. No securely dated pre-1443 artefact supports this.

---

# Culture

## 1. Law and administration

- Early Hangul could clarify legal readings and vernacular statements.
- The 1894 ordinance formally elevated *gukmun* in laws and commands.
- Modern constitutions and statutes of both Koreas are published in Hangul.
- Hanja may still disambiguate legal terminology in South Korean historical or specialist contexts.

## 2. Scripture and religion

Early royal patronage strongly favored Buddhist translation:

- *Seokbo sangjeol*
- *Worin cheongang jigok*
- later vernacular sutras and dhāraṇī explanations

Confucian didactic works were likewise translated to disseminate state ethics. Christian missionaries later used Hangul extensively for scripture, hymnals, tracts, and literacy work, helping expand mass readership in the nineteenth and twentieth centuries.

The script itself was not created as a sacred revelation, although later national rhetoric can treat it reverentially.

## 3. Monuments and public inscriptions

Hangul was initially less common than Hanja on formal stone monuments, seals, and elite epitaphs. Its growing state prestige after 1894 and especially after 1945 transformed the public landscape:

- road and station signs;
- monuments and memorials;
- government seals and logos;
- building inscriptions;
- military and civic signage;
- commemorative sculpture.

## 4. Coins, notes, and stamps

Premodern coin legends were overwhelmingly Chinese-character based. Modern Korean currency, postage, and state emblems employ Hangul, often beside Arabic numerals, Hanja, or Latin transliteration.

**Absence finding:** there is no historical Hangul letter-numeral coinage comparable to Greek alphabetic denominations.

## 5. Calendars

Traditional calendars used Chinese characters, sexagenary stems and branches, and numerical systems inherited from East Asia. Modern calendars use Hangul weekday/month labels and Arabic digits. Hangul letters themselves are not calendrical numerals.

## 6. Literature and alphabet play

Hangul supports:

- acrostic poems, especially *samhaengsi*, where successive lines begin with syllables from a name or phrase;
- children’s 가나다 poems and alphabet songs;
- typographic and concrete poetry;
- calligrams assembled from jamo;
- visual puns exploiting syllable-block geometry;
- experimental decomposition of words into consonant/vowel components.

These practices are analogous to alphabet poems but are organized around Korean syllables and jamo rather than inherited Semitic letter names.

## 7. Art and design

Modern artists have used:

- isolated jamo as abstract geometry;
- the *Hunminjeongeum* preface as patterned texture;
- block decomposition in kinetic typography;
- calligraphic *gungche*;
- modular fonts;
- “linear Hangul,” freeing jamo from square blocks;
- three-dimensional and architectural forms.

Ahn Sang-soo’s work is especially important in modern graphic reinterpretation. MoMA describes Hangul type design as a modular field in which phonemic elements and block structure interact. [MoMA essay](https://www.moma.org/explore/inside_out/2015/02/05/korean-hangul-typeface-design-a-unique-game-of-modular-design/)

---

# Controversies and disputes

## 1. Who invented Hangul?

### Position A: Sejong personally invented the core script

Evidence:

- explicit *Sejong sillok* attribution;
- opponents address the innovation as his;
- Jeong Inji’s postface credits the king;
- the Hall of Worthies opposition makes secret institutional authorship unlikely;
- later named scholars are securely associated with explanation and application.

### Position B: Sejong led a collaborative project

Evidence:

- complexity of phonological research;
- named scholarly collaborators;
- royal projects normally depended on offices, translators, printers, and specialists;
- consultation may not have been separately entered in the annals.

### Position C: the Hall or royal children did the real work

Evidence offered is mostly later tradition and inference. It lacks contemporary attribution.

**Best-supported conclusion:** Sejong was the principal inventor; collaborators helped test, explain, apply, and publish the system. The exact private division of labor is irrecoverable.

## 2. ʼPhags-pa influence

### For

- Joseon scholars had access to Mongol/Yuan phonological knowledge.
- Some consonant forms and sound correspondences can be aligned.
- The “old seal” phrase may conceal or euphemize a connection.
- Ledyard’s version is limited and historically contextualized.

### Against

- no contemporary source names ʼPhags-pa;
- simple shapes invite accidental resemblance;
- the articulatory derivation is comprehensive for the foundational series;
- vowels and syllable blocks are not derived from ʼPhags-pa;
- transformations needed for some matches are selective.

**Finding:** possible limited stimulus, unproven parentage.

## 3. Was the *Haerye* itself forged or altered?

The 1446 text is corroborated by the annals and transmitted excerpts. The Kansong physical copy has replacement opening leaves, and scholars debate whether it is the original 1446 printing or a somewhat later reproduction.

That is different from claiming the entire *Haerye* is a twentieth-century forgery. Its language, textual relationships, provenance before academic publication, and agreement with earlier witnesses make wholesale modern fabrication implausible.

The Sangju copy remains inaccessible enough that full authentication is unresolved.

## 4. Was Hangul suppressed by the yangban?

**For a strong-resistance account:**

- the 1444 memorial is explicit;
- Literary Chinese remained the route to office and prestige;
- dismissive terms such as *eonmun* and *amgeul* circulated;
- official adoption remained limited for centuries.

**Against a total-suppression account:**

- state-sponsored books appeared immediately;
- princes, kings, monks, translators, male officials, and elite households used it;
- royal women and men corresponded in it;
- vernacular fiction and practical literature flourished;
- several governments printed Hangul translations.

**Finding:** institutional and status resistance was real, but there was no continuous universal yangban ban.

## 5. Was it literally “women’s script”?

The term and association were real. Exclusivity was not.

The label may be:

- descriptive of women’s strong use;
- dismissive when voiced by elite men;
- empowering in modern recovery of women’s authorship;
- misleading when it hides male and state usage.

Every occurrence must be interpreted in its particular source rather than assigned one timeless meaning.

## 6. Did Japanese rule ban Hangul?

### Strong claim

“Hangul was banned from 1910 to 1945.”

This is false as stated: Korean books, newspapers, schools, and scholarship existed during significant portions of colonial rule.

### Narrower claim

“Late colonial assimilation policy suppressed Korean-language education, publishing, and scholarship, culminating in the 1942 Korean Language Society arrests.”

This is documented.

The difference matters because exaggerating the chronology is unnecessary and obscures how policy radicalized after 1937–1938.

## 7. Is Hangul “the most scientific script”?

This is a modern evaluative slogan, not a falsifiable historical classification.

Documentable features include:

- explicit articulatory design;
- systematic derivation;
- distinctive vowel construction;
- economical alphabet;
- regular block composition;
- a surviving contemporary design treatise.

Limitations include:

- modern spelling is morphophonemic, not a direct phonetic transcript;
- letter-to-sound values depend on context;
- block typography and computing can be complex;
- obsolete contrasts and sound change separate modern pronunciation from original design;
- ease of literacy also depends on language, education, vocabulary, and social conditions.

“Scientific” can reasonably describe the conscious phonological analysis; “best alphabet in the world” is an aesthetic or political judgment.

## 8. Were all 28 letters designed from speech organs?

The *Haerye* explicitly derives the five basic consonants from articulators and the three basic vowels from cosmic/graphic principles. It derives other consonants and vowels from those forms.

A popular simplification says all 28 directly picture the mouth. That is inaccurate. Most are derivatives; the vowels receive a cosmological explanation, though their orientation is also correlated with articulation.

## 9. Is Hangul an alphabet or syllabary?

### Alphabet argument

- jamo represent consonant and vowel phonemes;
- the same jamo recur across syllables;
- unfamiliar syllables can be composed productively;
- 11,172 blocks need not be memorized as independent signs.

### Syllabic argument

- the visible unit is a syllable block;
- reading, cursor movement, sorting, typography, and encoding often operate at block level;
- initial and final forms can be position-specific.

**Finding:** “featural alphabet written in syllable blocks” is most precise. “Alphabetic syllabary” or Unicode’s “featural syllabic script” describes presentation but should not imply that each syllable is an indivisible sign.

## 10. Cia-Cia: triumph, failure, or publicity event?

- Organized teaching and textbook production: documented.
- Local signage and continuing symbolic use: documented.
- Permanent universal community adoption: not demonstrated.
- Complete abandonment: also too strong; later activity is documented.
- Official replacement of Latin throughout Baubau or Indonesia: false.

The case is best understood as a fragile transnational revitalization project shaped by local agency, Korean cultural diplomacy, institutional discontinuity, and media exaggeration.

## 11. Unicode completeness

“All Hangul is encoded as 11,172 syllables” is true only for modern combinations. Historical Hangul contains thousands of possible blocks represented through conjoining jamo. Fonts and rendering engines may fail even when the underlying characters are encoded.

## 12. Garimto and other ancient-origin claims

No accepted archaeological object establishes a pre-fifteenth-century alphabet graphically identical to Hangul. Sources claiming one are late, textually unstable, or associated with modern pseudo-history.

**Finding:** absence of early material evidence is decisive unless a securely excavated, independently dated inscription is produced.

---

# Open questions

1. **The invention workshop:** No drafts or personal design notes survive. How Sejong moved from phonological analysis to exact graphic forms cannot be reconstructed step by step.

2. **Extent of consultation:** The records identify Sejong as inventor but do not reveal every conversation with princes, interpreters, physicians, Buddhist scholars, or phonologists.

3. **Meaning of “old seal script”:** Whether 古篆 is rhetorical, generic, Chinese-palaeographic, or an oblique reference to another alphabet remains unsettled.

4. **ʼPhags-pa stimulus:** The hypothesis is historically possible but lacks a documentary bridge. Comparative shape analysis alone cannot settle it.

5. **Exact Middle Korean phonetics:** Values conventionally assigned to ㅿ, ㆆ, ㆁ, ㆍ, light labials, and consonant clusters remain reconstructions.

6. **Middle Korean prosody:** The *bangjeom* contrasts are certain; whether they should be modeled as tone, pitch accent, or moraic pitch remains debated.

7. **Early readership:** Surviving books and letters are biased toward court, temple, and elite archives. Actual fifteenth- and sixteenth-century popular literacy rates remain poorly recoverable.

8. **Women’s authorship:** Anonymous palace and household manuscripts may conceal extensive female composition and copying that cannot now be attributed.

9. **Kansong copy production date:** The text is authentic, but more material study may refine whether the surviving impression is exactly contemporary with 1446.

10. **Sangju copy:** Full access is required before its text, paper, printing, and relationship to the Kansong witness can be assessed.

11. **Cia-Cia vitality:** Reports conflict because “use” can mean a school course, public signs, literacy, cultural display, or community-wide daily writing. Longitudinal fieldwork is needed.

12. **Digital Old Hangul:** Encoding is substantially available, but typography, normalization, input, searching, and preservation remain uneven.

13. **North–South standardization:** Technical committees have proposed joint orders and keyboards, but orthography is tied to state identity; a neutral unified standard remains politically difficult.

---

# Sources

## Primary and institutional sources

1. *Hunminjeongeum*, English translation with Classical Chinese text, Wikisource:  
   https://en.wikisource.org/wiki/Translation:Hunminjeongeum

2. UNESCO, “Hunminjeongum Manuscript,” Memory of the World:  
   https://www.unesco.org/en/memory-world/hunminjeongum-manuscript

3. UNESCO nomination dossier for National Treasure No. 70:  
   https://media.unesco.org/sites/default/files/webform/mow001/republic_of_korea_hunmin_chongum.pdf

4. Columbia University, Asia for Educators, “Excerpts from the Sejong Sillok: Ch’oe Malli’s Opposition to the Korean Alphabet”:  
   https://afe.easia.columbia.edu/main_pop/ps/ps_korea-alphabet-dissent.htm

5. PDF edition of the same primary-source selection:  
   https://afe.easia.columbia.edu/ps/korea/alphabet_dissent.pdf

6. National Hangeul Museum, permanent exhibition:  
   https://www.hangeul.go.kr/en/exhi/dailyExhibition.do

7. National Hangeul Museum, “About Hangeul”:  
   https://m.hangeul.go.kr/lang/en/html/education/Hangeul.do

8. National Institute of Korean Language, “About Hangeul—Origin”:  
   https://www.korean.go.kr/eng_hangeul/origin/001.html

9. National Institute of Korean Language, “Principle of Hangeul”:  
   https://www.korean.go.kr/eng_hangeul/principle/001.html

10. National Institute of Korean Language, history of Hangul Day:  
    https://www.korean.go.kr/nkview/news/10/102.htm

11. National Institute of Korean Language, Revised Romanization:  
    https://www.korean.go.kr/front_eng/roman/roman_01.do

12. Academy of Korean Studies, Encyclopedia of Korean Culture, “한글”:  
    https://encykorea.aks.ac.kr/Article/E0061508

13. Academy of Korean Studies, “훈민정음 28자모”:  
    https://encykorea.aks.ac.kr/Article/E0074518

14. Academy of Korean Studies, “훈몽자회”:  
    https://encykorea.aks.ac.kr/Article/E0065801

15. Academy of Korean Studies, “조선어학회 사건”:  
    https://encykorea.aks.ac.kr/Article/E0052129

16. Korean Language Society, colonial-period history:  
    https://eng.hangeul.or.kr/homepage/custom/Colonial

17. Korean National Archives, history of Hangul policy:  
    https://theme.archives.go.kr/next/hangeulPolicy/outline.do

18. Korean National Archives, keyboard mechanization and standardization:  
    https://theme.archives.go.kr/next/hangeulPolicy/mechanization.do

19. Presidential Archives of Korea, Hangul Day:  
    https://www.pa.go.kr/portal/online_contents/instant_record/instantRecordDetail.do?seq=81

20. National Folk Museum of Korea, Hangul Day:  
    https://www.nfm.go.kr/user/month12Bbs/english/81/977/Month12BbsEngList.do?bbsCategoryIdxs=&bbsDataIdx=20607

21. Kansong Art and Culture Foundation, acquisition history:  
    https://kansong.org/eng/index.do?menu_id=00005124

22. National Hangeul Museum, North–South letter names and order:  
    https://www.hangeul.go.kr/webzine/201806/sub1_1.html

23. North Korean *Chosŏnmal Kyubŏmchip* 2010 facsimile information:  
    https://commons.wikimedia.org/wiki/File:%EC%A1%B0%EC%84%A0%EB%A7%90%EA%B7%9C%EB%B2%94%EC%A7%91%282010%29.pdf

## Unicode and computing sources

24. Unicode Standard 17.0, Chapter 18, East Asia—Hangul:  
    https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-18/

25. Unicode Standard, Chapter 3, Hangul composition algorithm:  
    https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/

26. Unicode Hangul Jamo names list:  
    https://www.unicode.org/charts/nameslist/n_1100.html

27. Unicode Hangul Jamo chart:  
    https://unicode.org/charts/PDF/U1100.pdf

28. Unicode Hangul Syllables names list:  
    https://www.unicode.org/charts/nameslist/c_AC00.html

29. Unicode Hangul Jamo Extended-B:  
    https://www.unicode.org/charts/nameslist/c_D7B0.html

30. Unicode Korean FAQ:  
    https://www.unicode.org/faq/korean.html

31. Unicode Normalization Annex:  
    https://unicode.org/reports/tr15/

32. Unicode Collation Algorithm:  
    https://unicode-org.github.io/unicode-reports/tr10/tr10.html

33. Unicode proposal on *bangjeom*:  
    https://www.unicode.org/L2/L2011/11402-bangjeom.pdf

34. Unicode mailing-list history of 1.1 and 2.0 Hangul repertoires:  
    https://www.unicode.org/mail-arch/unicode-ml/y2015-m06/0189.html

35. Unicode document on early Hangul mappings:  
    https://www.unicode.org/L2/L2017/17080-three-hangul-syl.pdf

36. Unicode comments explaining the 11,172-syllable repertoire:  
    https://www.unicode.org/L2/L2017/17248-hangul-cmts.pdf

37. Proposal documenting North Korea’s six reform letters:  
    http://www.unicode.org/L2/L2019/19230-six-hangul-letters.pdf

38. Microsoft, Developing OpenType Fonts for Korean Hangul:  
    https://learn.microsoft.com/en-us/typography/script-development/hangul

39. Young Back Choi, “Path Dependence and the Korean Keyboard”:  
    https://www.wiwiss.fu-berlin.de/forschung/pfadkolleg/Archiv/_NEU_Veranstaltungen/konferenzen/download_center_2011/papers/Choi__Young_Back.pdf

## Major scholarly works and reference editions

40. Peter T. Daniels and William Bright, eds., *The World’s Writing Systems*. New York/Oxford: Oxford University Press, 1996. WorldCat record/search:  
    https://search.worldcat.org/search?q=ti%3AThe+World%27s+Writing+Systems+au%3ADaniels+Bright

41. Young-Key Kim-Renaud, ed., *The Korean Alphabet: Its History and Structure*. Honolulu: University of Hawai‘i Press, 1997. Publisher/search record:  
    https://uhpress.hawaii.edu/title/the-korean-alphabet-its-history-and-structure/

42. Gari K. Ledyard, *The Korean Language Reform of 1446: The Origin, Background, and Early History of the Korean Alphabet*. PhD diss., University of California, Berkeley, 1966; revised Seoul: Singu munhwasa, 1998. Google Books record:  
    https://books.google.com/books/about/The_Korean_Language_Reform_of_1446.html?id=1bELAQAAMAAJ

43. Gari Ledyard, “The International Linguistic Background of the Correct Sounds for the Instruction of the People,” in Kim-Renaud, *The Korean Alphabet*, 1997.

44. Ki-Moon Lee and S. Robert Ramsey, *A History of the Korean Language*. Cambridge: Cambridge University Press, 2011. Publisher page:  
    https://www.cambridge.org/core/books/history-of-the-korean-language/18711F0A619D30F97A70D6C9CC1F3C88

45. Ho-min Sohn, *The Korean Language*. Cambridge: Cambridge University Press, 1999. Accessible bibliographical PDF:  
    https://altaica.ru/LIBRARY/KOREAN/Jae%20Jung%20Song_The%20Korean%20Language.pdf

46. Jae Jung Song, *The Korean Language: Structure, Use and Context*. London: Routledge, 2005.

47. Florian Coulmas, *The Blackwell Encyclopedia of Writing Systems*. Oxford: Blackwell, 1996.

48. Geoffrey Sampson, *Writing Systems: A Linguistic Introduction*. Stanford: Stanford University Press, 1985; second edition, Equinox, 2015.

49. Iksop Lee and S. Robert Ramsey, *The Korean Language*. Albany: SUNY Press, 2000.

50. Sohn, Ho-min, “Orthographic Divergence in South and North Korea: Toward a Unified Spelling System,” in Kim-Renaud, 1997.

51. Cambridge sample discussing North–South divergence:  
    https://assets.cambridge.org/97805218/28581/sample/9780521828581ws.pdf

52. Academy of Korean Studies, *The Korean Alphabet: Hangeul*:  
    https://www.korean.go.kr/common/download.do%3Bfront%3D1DCADDF6F42CC605F6C85228AC3A5959?c_file_name=89c36d8f-0c82-401b-b293-9394b66a058e_0.pdf&file_path=reportData&o_file_name=The+Korean+Alphabet_Hangeul.pdf

53. Academy of Korean Studies, discussion of the 28 letters:  
    https://www.aks.ac.kr/ikorea/upload/intl/korean/UserFiles/UKS1_Hangeul_eng.pdf

54. Gari Ledyard, “Sejong the Great,” Korea Society monograph:  
    https://www.koreasociety.org/images/pdf/KoreanStudies/Monographs_GeneralReading/GettingtoKnowKorea/GTKK%202%20Ledyard%20Sejong%20The%20Great.pdf

55. Thorsten Traulsen, “Han’gŭl Reform Movement in the Twentieth Century”:  
    https://brill.com/previewpdf/book/edcoll/9789004217003/B9789004217003_007.xml

## Specialized scholarship

56. Cho Tae-young, “Cia-Cia Language: From the Era of Oral to the Era of Writing,” *Humaniora* 24.3 (2012):  
    https://journal.ugm.ac.id/jurnal-humaniora/article/view/1374

57. Recent Indonesian discussion of Cia-Cia revitalization:  
    https://www.ejournal.unma.ac.id/index.php/diglosia/article/view/18439

58. Tae-Ho Kim, “State-led Modernization of Language: Standardization of Korean Typewriter Keyboard in 1969”:  
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch.kci?sereArticleSearchBean.artiId=ART002053954

59. “A Study of the Hangeul Metal Printing Types from the Collection of the National Museum of Korea”:  
    https://www.ijkaa.org/v.4/0/116/93?view=pubreader

60. “The Birth of Hangeul Punctuation Marks (1446–1876)”:  
    https://koreantypography.org/wp-content/uploads/thesis/kst_j8_1.pdf

61. “The Development of the Hangul Writing System and Women in the Joseon Dynasty”:  
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch.pib?arti_id=ART002278069

62. UCLA Korean History and Culture Digital Museum, “How Women in Chosŏn Korea Legitimized Han’gul”:  
    https://koreanhistory.humspace.ucla.edu/items/show/14

63. Study of North–South *saisori* rules:  
    https://www.kci.go.kr/kciportal/ci/sereArticleSearch.kci?sereArticleSearchBean.artiId=ART002178466

64. National Institute of Korean Language, comparative North–South policy study:  
    https://www.korean.go.kr/common/download.do?c_file_name=7758f2cb-dee9-4512-a13b-1ac1cf08b1db.pdf&file_path=reportData&o_file_name=KR201201031.pdf

65. Reassessment of Ch’oe Malli’s memorial:  
    https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11219308

66. Study arguing for Sejong’s sole core inventorship:  
    https://kiss.kstudy.com/Detail/Ar?key=3871316

67. Study of Sejong and collaborators:  
    https://kiss.kstudy.com/Detail/Ar?key=2403948

68. Choi Jeong-ho typeface history, ATypI:  
    https://atypi.org/presentation/a-history-of-hangul-typefaces-in-the-20th-century/

69. Choi Jeong-ho type-design lineage:  
    https://resources.morisawa.co.jp/uploads/tmg_block_page_image/file/2457/Morisawa_Choi_Jeong-ho_Font.pdf

70. Letterform Archive, Ahn Sang-soo and AG Typography Institute:  
    https://letterformarchive.org/news/from-the-collection-ahn-sang-soo/

71. MoMA, “Korean Hangul Typeface Design: A Unique Game of Modular Design”:  
    https://www.moma.org/explore/inside_out/2015/02/05/korean-hangul-typeface-design-a-unique-game-of-modular-design/

72. Korean Typography Society, punctuation and historical typography resources:  
    https://koreantypography.org/

73. Open Korean Historical Corpus, diachronic textual evidence:  
    https://arxiv.org/abs/2510.24541

## Manuscript controversy and repository reporting

74. Korea JoongAng Daily, Kansong and Sangju copies:  
    https://www.koreajoongangdaily.com/lifestyle/struggle-to-retrieve-treasured-manuscript-continues-supreme-courts-ruling-that-huminjeongeum-belongs-to-cha-creates-new-options/10309640

75. Korea JoongAng Daily, digital and material value of the manuscript:  
    https://www.koreajoongangdaily.com/lifestyle/is-a-national-treasure-still-valuable-in-digital-form/10115278

76. Korea Times, 2019 Supreme Court dispute:  
    https://www.koreatimes.co.kr/southkorea/society/20190717/court-ruling-re-sparks-tug-of-war-over-priceless-hangeul-handbook

77. ANU repository discussion of the Kansong copy, dimensions, and design:  
    https://openresearch-repository.anu.edu.au/server/api/core/bitstreams/1a24fe66-1359-498a-85af-1ba4e2481a04/content

## Starting indexes consulted cautiously

78. Omniglot, Korean alphabet index:  
    https://www.omniglot.com/writing/korean.htm

79. Unicode overview and current block list:  
    https://www.unicode.org/charts/

80. National Hangeul Museum English portal:  
    https://www.hangeul.go.kr/en/
