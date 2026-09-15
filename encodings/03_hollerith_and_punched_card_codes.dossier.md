# Hollerith and the punched-card codes: Research Dossier

> **Encoding 3 of 17**
>
> **Standard:** ANSI X3.26-1980, *Hollerith Punched Card Code*; earlier ANSI X3.26-1970 / FIPS PUB 14; revised federal adoption FIPS PUB 14-1  
> **Year:** Conventional IBM 80-column form introduced in 1928, expanded to twelve rows by 1930; first national code standard approved in 1970 and revised in 1980  
> **Bit width:** Physically 12 binary punch positions per column; conventional character repertoire used a restricted, variable-weight subset, commonly 48 or 64 characters; ANSI X3.26 assigned 256 selected hole patterns corresponding to eight-bit code positions  
> **Repertoire:** Originally decimal or application-defined statistical fields; later blank, ten digits, 26 uppercase Latin letters and machine-dependent punctuation; ANSI X3.26 represented all 128 ASCII characters plus 128 additional positions  
> **Current status:** The historic character-code standard is withdrawn. Punched cards remain a preservation, museum and specialist-legacy medium. ISO 1681:1973, specifying unpunched paper cards rather than the character code, was still listed by ISO as current and confirmed in 2020.

## Method and evidence labels

“Hollerith code” is not the name of one immutable encoding. It can mean:

1. Hollerith’s application-specific census index-point systems of the 1880s;
2. early tabulating-machine numeric card layouts;
3. IBM’s conventional alphanumeric card code;
4. one of several IBM 026 or 029 keypunch repertoires;
5. ANSI X3.26’s later 256-pattern interchange standard;
6. loosely, any data punched on an IBM-format card.

Conflating these produces most incorrect “Hollerith tables” found online.

Every substantive historical statement below is marked:

- **[D] Documented text/standard:** contemporary patent, manual, standard, government record or institutional collection.
- **[S] Scholarly reconstruction:** conclusion in a later historical study.
- **[P] Participant recollection:** statement by a participant or contemporary witness.
- **[Q] Disputed:** competing accounts or insufficient evidence.
- **[F] Folklore:** widely repeated story whose evidentiary chain is weak.
- **[M] Modern invention:** a later simplification, analogy or retroactively imposed terminology.

“Absence finding” means that the searched primary record did not establish the claim; it does not prove the opposite.

---

## Basic identification

### Names

- **[D]** Hollerith himself called his method an “Art of Compiling Statistics.” His patents describe cards, strips or tablets carrying “circuit-controlling index-points,” not an alphabet named “Hollerith code.” U.S. patents 395,781, 395,782 and 395,783 were granted on 8 January 1889 from applications beginning in 1884. [Patent 395,782](https://patents.google.com/patent/US395782A/en); [USPTO historical account](https://www.uspto.gov/learning-and-resources/journeys-innovation/historical-stories/count-me).

- **[D]** “Hollerith punched card code” became the formal title of ANSI X3.26-1970. That standard explicitly called the pre-existing practice a *de facto* standard and retained commonly used Hollerith patterns for numerals and single-case letters. [ANSI X3.26-1970 / FIPS PUB 14](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

- **[D]** ANSI X3.26-1980 revised the 1970 edition. Its federal adoption was FIPS PUB 14-1. [FIPS PUB 14-1 / ANSI X3.26-1980](https://www.govinfo.gov/content/pkg/GOVPUB-C13-ae993250946603686b40e5d15bda75a8/pdf/GOVPUB-C13-ae993250946603686b40e5d15bda75a8.pdf).

- **[D]** The final ANSI/INCITS listing describes 256 patterns, covering the 128 ASCII characters and 128 additional eight-bit positions, and records the standard as withdrawn in 2013. [ANSI/INCITS catalogue entry](https://shop.standards.ie/en-ie/standards/ansi-incits-26-80-r1991--614614_saig_iti_iti_1414020/).

### Medium and capacity

- **[D]** The familiar IBM card measured 7⅜ by 3¼ inches, had 80 vertical character columns and twelve horizontal punching rows, ordered from top to bottom as 12, 11, 0, 1, 2, …, 9. Each column could therefore be regarded physically as a 12-bit bitmap. [IBM history](https://www.ibm.com/history/punched-card); [ANSI X3.26-1970](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

- **[D]** “Twelve-bit” does **not** imply a 4,096-character repertoire. Traditional equipment recognized only selected one-, two- and three-punch combinations. ANSI X3.26 selected 256 combinations, while common commercial machines generally provided 48 or 64 characters. [ANSI X3.26-1970, §§1–2 and Appendix A](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf); [IBM 029 manual](https://www.masswerk.at/keypunch/manuals/IBM029-GA24-3332-6_Reference_Manual_Model_29_Card_Punch_Jun70.pdf).

- **[D]** In an ordinary text deck, one card column represented one character and one card held at most 80 characters. In binary or multi-column schemes the same stock could be interpreted differently. [IBM history](https://www.ibm.com/history/punched-card); [IBM System/360 Model 20 Functional Characteristics](https://www.bitsavers.org/pdf/ibm/360/functional_characteristics/A26-5847-3_360-20_funChar_Apr67.pdf).

- **[M]** Calling a card “80 bytes” is a convenient modern analogy, correct only after a reader translates each column into one stored character. The card itself contains holes, not bytes.

---

## The code in detail

## 1. Physical organization

An IBM-format card column is:

```text
row:   12  11   0   1   2   3   4   5   6   7   8   9
bit:    •   •   •   •   •   •   •   •   •   •   •   •
```

A hole is 1/present; unpunched stock is 0/absent.

- **[D]** Rows 12, 11 and 0 became the three *zone* positions. Rows 1–9 supplied digit punches. The 0 row had a double role: it represented decimal zero alone and acted as a zone when combined with another digit punch. [IBM 024/026 manual](https://bitsavers.org/pdf/ibm/punchedCard/Keypunch/024-026/A24-0520-3_24_26_Card_Punch_Reference_Manual_Oct1965.pdf); [IBM 1401 restoration technical notes](https://ibm1401.computerhistory.org/IBM-1401-Theory-of-Operation-GF.pdf).

- **[D]** Ordinary digits used one hole:

| Character | Punch |
|---|---:|
| `0` | `0` |
| `1` | `1` |
| `2` | `2` |
| `3` | `3` |
| `4` | `4` |
| `5` | `5` |
| `6` | `6` |
| `7` | `7` |
| `8` | `8` |
| `9` | `9` |

- **[D]** Uppercase letters used one zone plus one digit:

| 12-zone | Punch | 11-zone | Punch | 0-zone | Punch |
|---|---:|---|---:|---|---:|
| A | 12-1 | J | 11-1 | S | 0-2 |
| B | 12-2 | K | 11-2 | T | 0-3 |
| C | 12-3 | L | 11-3 | U | 0-4 |
| D | 12-4 | M | 11-4 | V | 0-5 |
| E | 12-5 | N | 11-5 | W | 0-6 |
| F | 12-6 | O | 11-6 | X | 0-7 |
| G | 12-7 | P | 11-7 | Y | 0-8 |
| H | 12-8 | Q | 11-8 | Z | 0-9 |
| I | 12-9 | R | 11-9 | — | — |

The missing `0-1` alphabetic position was conventionally assigned to slash `/` in major IBM repertoires. [IBM 024/026 manual](https://bitsavers.org/pdf/ibm/punchedCard/Keypunch/024-026/A24-0520-3_24_26_Card_Punch_Reference_Manual_Oct1965.pdf).

### Why S starts at 2

- **[S]** The offset is best understood as inheritance from decimal-card machinery and available punch combinations, not as a linguistic partition of the alphabet. It produced groups of 9, 9 and 8 letters.

- **[M]** Claims that the unusual S–Z placement was deliberately invented for EBCDIC are chronologically wrong: the card grouping predates EBCDIC by decades. EBCDIC inherited the discontinuities.

## 2. Blank, space and punctuation

- **[D]** In the common card code, an entirely unpunched column represented blank or space. ANSI’s historical appendix says the widespread 48-character repertoire consisted of blank, ten digits, 26 letters and eleven special characters. [ANSI X3.26-1970, Appendix A2](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

- **[D]** The invariant core was only the blank, digits and uppercase alphabet—37 characters. ANSI found “almost complete uniformity” for those patterns but substantial disagreement over the remaining special-character assignments. [ANSI X3.26-1970, Appendix A2](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

Typical IBM 026 assignments included:

| Character | Common punch |
|---|---:|
| space | no holes |
| `&` | `12` |
| `-` | `11` |
| `/` | `0-1` |
| `.` | `12-8-3` in a common commercial arrangement |
| `$` | `11-8-3` |
| `*` | `11-8-4` |
| `,` | machine/repertoire dependent |
| `(` | commonly `12-8-5` |
| `)` | commonly `11-8-5` |
| `+` | commonly `12-8-6` |
| `=` | commonly `11-8-6` |

- **[D]** This list cannot safely be called *the* Hollerith punctuation table. IBM supplied different 026 “commercial” and “FORTRAN” arrangements, and ANSI recorded two widespread 48-character groupings plus divergent extensions up to 64 characters. The correct decoder must identify the punch, reader and application convention. [IBM 024/026 manual](https://bitsavers.org/pdf/ibm/punchedCard/Keypunch/024-026/A24-0520-3_24_26_Card_Punch_Reference_Manual_Oct1965.pdf); [ANSI X3.26-1970, Fig. A1](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

- **[D]** The IBM 029 offered 48- or 64-character keyboards. The expanded set was broadly EBCDIC-oriented, lacked lowercase, and included such programming symbols as the logical-not sign `¬`. [IBM 029 manual](https://www.masswerk.at/keypunch/manuals/IBM029-GA24-3332-6_Reference_Manual_Model_29_Card_Punch_Jun70.pdf); [Columbia 029 exhibit](https://www.columbia.edu/cu/computinghistory/029.html).

## 3. ANSI X3.26’s extended code

- **[D]** ANSI X3.26-1970 specified 256 selected hole patterns. Positions 0–127 represented the characters of ANSI X3.4-1968 ASCII; positions 128–255 were intended for eight-bit systems. One selected pattern—examples include `12-2`, `11-8-6` and `11-9-8-6`—occupied one card column. [ANSI X3.26-1970, §§1–2](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

- **[D]** It was not simply “punch the eight bits of ASCII into eight rows.” Its goal was to preserve established punches for digits and uppercase letters while allocating more complicated patterns to the rest of ASCII. [ANSI X3.26-1970, Appendix A](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

- **[D]** Lowercase letters therefore existed in the ANSI standard, but ordinary 026/029 installations normally could not key them. Standards repertoire and deployed keyboard repertoire must not be equated.

- **[D]** ANSI encoded ASCII controls including NUL, LF, CR, ESC and DEL as selected column patterns. They were data values, not movements mechanically performed by the card reader merely because such a pattern was encountered.

## 4. Case

- **[D]** Conventional Hollerith/IBM card code was single-case. It represented `A`–`Z`, not distinct `a`–`z`.

- **[D]** Keypunch keyboard shift was generally a keyboard-selection mechanism—for example, selecting numeric or special functions—not a persistent in-band letter-shift code comparable to Baudot’s FIGS/LTRS.

- **[D]** ANSI X3.26 assigned separate column patterns to ASCII lowercase. It did not turn traditional decks into a stateful shifted encoding.

- **[S]** Uppercase-only programming languages, job-control syntax and identifiers were partly accommodated to the installed card/keypunch ecology. It would overstate causation to say cards alone “caused” uppercase computing.

## 5. Newline, space, deletion and editing

- **[D] Space:** An unpunched column normally represented space.

- **[D] Newline:** Traditional Hollerith code had no in-column newline. The end of the physical card was the record boundary. “One card equals one input record” later became a software abstraction.

- **[D] CR/LF:** ANSI X3.26 could represent ASCII CR and LF patterns, but their interpretation belonged to the receiving system.

- **[D] Deletion:** A punched hole could not be restored on the original card. An erroneous card was normally replaced or duplicated with a correction. Keypunches could backspace before release, but could only add holes; once an incorrect hole existed, re-punching could not erase it.

- **[D] Verification:** Separate verifier machines reread a card while a second operator rekeyed the source. A mismatch could be notched or otherwise signalled. The IBM 059 used optical sensing; earlier equipment used mechanical sensing. [Columbia 029 exhibit](https://www.columbia.edu/cu/computinghistory/029.html).

- **[F] “Punch every hole to delete”:** This analogy comes from paper tape, where an all-holes character could overwrite an earlier character and became ASCII DEL. On a punched card, an all-punched “lace card” was mechanically troublesome and did not provide a general semantic deletion operation.

## 6. Error detection and synchronization

- **[D]** The ordinary code has no checksum, parity bit or guaranteed minimum Hamming distance. A missing or added punch can turn one valid character into another.

- **[S]** Some illegal combinations could be rejected because only a subset of 4,096 possible column patterns belonged to the reader’s repertoire. This is incidental validity checking, not systematic error correction.

- **[D]** Columns are fixed physical positions, so a reader does not suffer bit-stream character-boundary loss. Each new column and each new card supplies physical resynchronization.

- **[D]** Card-feed orientation was protected by stock geometry and handling conventions, including a clipped corner on many cards. Reversed, upside-down, skewed, bent or torn cards could still be misread or jam.

- **[D]** Losing a card from a deck or shuffling a deck was a record-level error that the character code could not detect. Programs frequently reserved columns 73–80 for sequence numbers so a sorter or listing could restore order.

- **[F/P]** Stories about dropping a thousand-card program deck and spending hours re-sorting it are abundant in programmer recollections. The risk is real, but many retellings omit sequence-number columns, diagonal marker stripes and deck trays that mitigated it.

## 7. Collating order

There is no single universal “numeric value of a Hollerith character” comparable to ASCII code-point order.

- **[D]** Numeric sorting was mechanical: sorters selected cards by sensing a given row in a chosen column.

- **[D]** Alphabetic sorting commonly took two passes per character column: one for digit rows and another for zones 12, 11 and 0. [Description of card-sorter operation](https://en.wikipedia.org/wiki/Punched_card_sorter).

- **[S]** The alphabet’s 12/11/0 grouping made alphabetic collation feasible but tied order to machine wiring, pass order and stacker handling. Punctuation order was especially repertoire- and equipment-dependent.

- **[D]** When the card-derived scheme became six-bit BCD and later EBCDIC, the alphabet remained broken into three blocks. Consequently binary EBCDIC order is not ASCII order; in common EBCDIC pages lowercase letters, uppercase letters and digits occupy separated high-valued ranges. [IBM EBCDIC collating sequence](https://www.ibm.com/docs/en/ssw_ibm_i_74/db2/rbafzsortsequence.htm).

## 8. Worked example: `HOLLERITH`

### Conventional card columns

| Column | Character | Punch pattern |
|---:|:---:|---:|
| 1 | H | `12-8` |
| 2 | O | `11-6` |
| 3 | L | `11-3` |
| 4 | L | `11-3` |
| 5 | E | `12-5` |
| 6 | R | `11-9` |
| 7 | I | `12-9` |
| 8 | T | `0-3` |
| 9 | H | `12-8` |

A card image, treating rows as bits in order `12,11,0,1,2,3,4,5,6,7,8,9`, would be:

| Character | 12-bit physical bitmap |
|---|---|
| H | `100000000010` |
| O | `010000001000` |
| L | `010001000000` |
| L | `010001000000` |
| E | `100000010000` |
| R | `010000000001` |
| I | `100000000001` |
| T | `001001000000` |
| H | `100000000010` |

- **[M]** These bit strings are a modern visualization. Historic manuals normally wrote row names such as `12-8`, not twelve-bit binary numbers.

### ASCII comparison

| Character | ASCII hex | Binary |
|---|---:|---:|
| H | `48` | `01001000` |
| O | `4F` | `01001111` |
| L | `4C` | `01001100` |
| L | `4C` | `01001100` |
| E | `45` | `01000101` |
| R | `52` | `01010010` |
| I | `49` | `01001001` |
| T | `54` | `01010100` |
| H | `48` | `01001000` |

### EBCDIC code page 037 comparison

| Character | EBCDIC hex |
|---|---:|
| H | `C8` |
| O | `D6` |
| L | `D3` |
| L | `D3` |
| E | `C5` |
| R | `D9` |
| I | `C9` |
| T | `E3` |
| H | `C8` |

- **[S]** The visible three-block inheritance is clear: `A–I` occupy `C1–C9`, `J–R` occupy `D1–D9`, and `S–Z` occupy `E2–E9`, echoing the 12-, 11- and 0-zone card groups.

### Example with a space

`HI IBM`

```text
H      I      space  I      B      M
12-8   12-9   none   12-9   12-2   11-4
```

No terminator need be punched. The end of the card, a programmed field boundary, or the application’s record layout supplies the boundary.

---

## Origins

## 1. Precursors: looms, paper media and railway tickets

- **[D]** Punched control media predate Hollerith. Eighteenth- and early-nineteenth-century textile mechanisms culminated in Joseph-Marie Jacquard’s linked punched-card loom control. These cards controlled operations; they were not census character records. [Smithsonian punched-card collection](https://americanhistory.si.edu/collections/object-groups/punch-cards/punch-cards-data-processing); [IBM history](https://www.ibm.com/history/punched-card).

- **[D/P]** Census physician John Shaw Billings suggested to Hollerith that census tabulation might be mechanized on a principle like the Jacquard loom. The Census Bureau preserves that institutional account. [Census biography](https://www.census.gov/library/photos/1880/herman-hollerith.html).

- **[P/S]** Hollerith’s more specific inspiration for placing personal characteristics at positions on a card is generally traced to railway conductors’ “punch photographs”: tickets punched at positions describing a passenger. IBM and Smithsonian histories repeat this account. [IBM history](https://www.ibm.com/history/punched-card); [Smithsonian](https://americanhistory.si.edu/collections/object-groups/punch-cards/punch-cards-data-processing).

- **[Q]** “Jacquard inspired Hollerith” and “railway tickets inspired Hollerith” are not mutually exclusive. Billings’ suggestion concerns mechanized tabulation; the railway-ticket story concerns the choice of a separate card and positional personal attributes. Modern summaries often collapse them into a single eureka moment.

- **[D]** Hollerith initially experimented with continuous strips or paper tape. His patent deliberately covers a “strip or tablet,” while his mature system used a separate record card for each individual. [Patent 395,782](https://patents.google.com/patent/US395782A/en); [Columbia history](https://columbia.edu/cu/computinghistory/hollerith.html).

## 2. The 1880 census problem

- **[D]** Hollerith, born in 1860 and trained at Columbia’s School of Mines, worked briefly for the Census Office around the 1880 census. That census’s final tabulations were not completed until 1887. [Census biography](https://www.census.gov/library/photos/1880/herman-hollerith.html); [Census tabulation history](https://www.census.gov/about/history/bureau-history/census-innovations/technology/tabulation-and-processing.html).

- **[D]** The immediate technical problem was not merely addition. Officials wanted cross-tabulations—age by sex, race, birthplace, occupation and other characteristics—without repeatedly hand-counting schedules.

- **[D]** Hollerith’s decisive abstraction was the *unit record*: a separate machine-readable record for each person. A template fixed the meaning of each possible punch position; electrical contacts detected holes and advanced counters. [Patent 395,782](https://patents.google.com/patent/US395782A/en).

- **[D]** The 1890 census report says that information about each person was transferred to a separate card and that the card then took the place of the schedule for detailed tabulation. [1890 census report](https://www2.census.gov/prod2/decennial/documents/1890a_v1-05.pdf).

## 3. Competition and the 1890 census

- **[D]** In an 1888 Census Office trial using 1880 data from four St Louis districts, three systems were compared. The Census Bureau’s retrospective gives data-capture times of 144.5, 100.5 and 72.5 hours; Hollerith’s system then prepared the data for tabulation in 5.5 hours against 44.5 and 55.5 hours for the others. [Census competition account](https://www.census.gov/about/history/bureau-history/census-innovations/technology/hollerith-machine.html).

- **[D]** Hollerith won the 1890 contract. Operators transferred schedule facts through a pantograph punch; a press brought spring-loaded pins through holes into mercury cups, completing circuits; counters accumulated totals; sorting boxes separated cards for subsequent passes. [Census machine description](https://www.census.gov/about/history/bureau-history/census-innovations/technology/hollerith-machine.html).

- **[D]** Hollerith described the system in “An Electric Tabulating System,” *The Quarterly*, Columbia School of Mines, April 1889, and in the work accepted for his Columbia PhD in 1890. He later described it to the Royal Statistical Society in 1894. [Columbia bibliography](https://columbia.edu/cu/computinghistory/hollerith.html).

- **[Q]** The familiar claim that Hollerith reduced census processing “from eight years to one” is misleading. Different accounts measure preliminary population totals, particular tabulations or completion of all publications. The 1890 census itself still generated work for years. The well-supported conclusion is that mechanization greatly accelerated and enlarged tabulation, not that the entire census was finished in a few months.

- **[Q]** Monetary savings figures vary according to which counterfactual and which phase is counted. “Saved $5 million” is repeated in later accounts, but should not be presented without its calculation and contemporary budget basis.

## 4. Were the 1890 cards a character code?

- **[D]** No, not principally. The card was a positional questionnaire. A hole might mean “male,” a particular age group, marital status or birthplace, depending on the template. Multiple positions together represented a person’s attributes.

- **[S]** Calling the 1890 layout a “text encoding” is therefore anachronistic. It was a machine-readable categorical data schema. The later letter code grew inside a card ecosystem descended from Hollerith’s machinery.

- **[M]** Online diagrams that place `A–Z` on “Hollerith’s 1890 census card” usually project the later IBM alphabetic code backward.

## 5. Company formation and rivals

- **[D]** Hollerith formed the Tabulating Machine Company in 1896. It became one of the businesses combined by Charles R. Flint into the Computing-Tabulating-Recording Company in 1911; CTR adopted the name International Business Machines in 1924. [Census biography](https://www.census.gov/library/photos/1880/herman-hollerith.html).

- **[D]** Hollerith’s prices and rental terms produced conflict with the new permanent Census Bureau after 1900. The Bureau established a machine shop and developed alternatives. [Census tabulation history](https://www.census.gov/about/history/bureau-history/census-innovations/technology/tabulation-and-processing.html).

- **[D]** James Legrand Powers, working for the Bureau, developed faster feeding, punching and sorting machinery. He left in 1911 to establish the Powers Accounting Machine Company, which became IBM’s principal punched-card competitor and ultimately part of the Remington Rand lineage. [Smithsonian Powers history](https://www.si.edu/spotlight/tabulating-equipment/the-bureau-of-the-census-to-remington-rand).

- **[S]** Hollerith did not “beat all rivals.” He won the pivotal 1890 census contest, later lost much Census Bureau work to in-house/Powers equipment, and his corporate successors ultimately won the larger commercial platform contest.

- **[D]** Powers-Samas developed commercially important alphabetic equipment. Consequently “Hollerith invented the punched-card alphabet” is too broad; alphabetic card processing was a competitive, incremental development.

## 6. From 45 to 80 columns

- **[D]** IBM’s predecessor cards evolved through several incompatible layouts: approximately 22 columns by eight positions, 24 columns by ten positions, and 45 columns by twelve positions with round holes. [IBM history](https://www.ibm.com/history/punched-card).

- **[D]** In 1928 Thomas J. Watson Sr. commissioned competing higher-capacity designs from Clair D. Lake and J. Royden Pierce. James W. Bryce selected Lake’s design: smaller rectangular holes allowed 80 columns on essentially the established card stock. [IBM history](https://www.ibm.com/history/punched-card).

- **[D]** IBM introduced the 80-column card in 1928 with ten numeric rows; the twelve-row form appeared in 1930. [IBM history](https://www.ibm.com/history/punched-card).

- **[D/S]** IBM’s own history explicitly notes a commercial advantage: the new card was compatible only with IBM machines. Technical capacity and platform control coincided.

### The dollar-bill story

- **[F]** A persistent story says Hollerith chose card dimensions to match a U.S. dollar bill so existing currency drawers or boxes could be used.

- **[Q]** The familiar 7⅜-by-3¼-inch IBM card was introduced decades after Hollerith’s original census cards. Modern U.S. notes were reduced to 6.14 by 2.61 inches in 1929, whereas earlier large-size currency was approximately 7.42 by 3.125 inches—close but not identical.

- **Absence finding:** Neither Hollerith’s cited patents nor IBM’s detailed 1928 Lake/Pierce account, among the sources consulted here, documents a decision to copy a banknote or reuse currency storage. The story should remain folklore unless a contemporary IBM engineering memorandum, drawing or testimony is produced.

---

## The BCD and BCDIC descendants

## 1. Six-bit machine codes

- **[D]** When IBM moved card data into electronic calculators and computers, the card’s zone-plus-digit structure was translated into six bits: two zone bits and four numeric bits. Six bits provided 64 combinations, enough for the installed uppercase repertoire.

- **[D]** Machines in the 1950s used related but not always identical six-bit schemes, including the IBM 702/704 families and the IBM 1401. “BCD,” “BCD interchange code,” “BCDIC,” tape BCD and card BCD are not interchangeable names for one table. [Charles Mackenzie, *Coded Character Sets*](https://archive.org/details/codedcharacterse00unse); [IBM 1401 documentation index](https://www.bitsavers.org/1401/1401-docs.html).

- **[D]** The IBM 1401 stored characters in six data bits—commonly described as `B`, `A`, `8`, `4`, `2`, `1`—plus a separate word-mark facility. The names `B` and `A` for the zone bits and `8-4-2-1` for numeric bits directly reflect card practice. [IBM 1401 restoration documentation](https://ibm1401.computerhistory.org/IBM-1401-Theory-of-Operation-GF.pdf).

- **[D]** Translation was not perfectly one-to-one. Zero and several zone/numeric combinations required special cases; some memory characters could not be read from an ordinary card in the same form, and printer-chain choice could alter the printed graphic. [IBM 1401 restoration technical notes](https://ibm1401.computerhistory.org/IBM-1401-Theory-of-Operation-GF.pdf).

- **[S]** It is therefore more precise to describe BCDIC as a family of card-derived six-bit encodings than as a universal standard.

## 2. EBCDIC

- **[D]** IBM designed the eight-bit Extended Binary Coded Decimal Interchange Code for System/360, announced in 1964. Its name and layout identify it as an extension of the earlier BCD-interchange family.

- **[D]** EBCDIC retained card-derived alphabet blocks and many punch-code relationships. ANSI X3.26 included an informative appendix mapping EBCDIC card code. [ANSI X3.26-1970, Appendix B](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

- **[S]** Cards did not mechanically force every EBCDIC assignment. Rather, compatibility with a large installed base of punches, readers, tapes, programs and business data made discontinuous inheritance economically compelling.

### “IBM chose EBCDIC because ASCII was not ready”

- **[S/Q]** The standard reconstruction is that IBM participated strongly in ASCII development but froze System/360’s peripheral and compatibility designs before a sufficiently stable, commercially usable ASCII ecosystem was ready. EBCDIC allowed reuse of card-derived machinery and translation practice.

- **[Q]** The simplified story “IBM rejected ASCII to lock in customers” overstates the surviving evidence. Lock-in was a consequence and compatibility was commercially advantageous, but timing, peripheral engineering and installed-base preservation were also real constraints.

### The “unused ASCII bit” defense

- **[F/P]** A recurring System/360 story says IBM expected an eighth-bit ASCII or reserved an unused bit, then was forced at the last moment to fill it with EBCDIC.

- **[Q]** Versions differ over which engineer made the decision and whether a particular bit in System/360 peripherals was “for ASCII.” The architecture did support an ASCII mode in some contexts, and some card-image formats placed six row bits in eight-bit bytes with two unused positions. That does not establish the sweeping claim that System/360 was secretly designed as an ASCII machine.

- **Absence finding:** No single contemporary IBM memorandum located in this research pass proves the popular last-minute narrative. It should be cited as participant-era lore unless tied to a named witness and document.

---

## Adoption and use

## 1. Government and business

- **[D]** Hollerith systems were used after the U.S. census in Canada, Norway and Austria and in railway accounting. [Census biography](https://www.census.gov/library/photos/1880/herman-hollerith.html).

- **[D]** The U.S. Social Security program became an enormous punched-card application after 1935, requiring millions of cards and tabulating machines for records and checks. [IBM history](https://www.ibm.com/history/punched-card).

- **[D]** Cards supported payroll, inventory, billing, banking, insurance, library circulation, police records, scientific calculation and government statistics. Some bills and checks were themselves returnable punched cards. [IBM history](https://www.ibm.com/history/punched-card); [Smithsonian collections](https://americanhistory.si.edu/collections/object-groups/punch-cards/punch-cards-data-processing).

- **[D]** By 1937 IBM’s Endicott operation had 32 presses producing approximately five to ten million cards daily. In the mid-1950s card sales supplied roughly 20 percent of IBM revenue and 30 percent of profit, according to IBM’s corporate history. [IBM history](https://www.ibm.com/history/punched-card).

- **[S]** Because IBM is the source of those financial figures, they should be understood as corporate historical reporting, though they are specific and internally plausible.

## 2. Science and war

- **[D]** Punched-card accounting machines performed extensive numerical work at wartime laboratories, including Los Alamos during the Manhattan Project. [Los Alamos computing study](https://arxiv.org/abs/2103.05705).

- **[S]** Cards blurred the boundary between “business machine” and “computer”: plugboard-controlled tabulators and calculators could execute long numerical workflows before stored-program machines absorbed those tasks.

## 3. Computing practice

- **[D]** Card readers and punches were standard peripherals on IBM 650, 704/709 families, 1401, System/360 and many non-IBM systems.

- **[D]** A program commonly used one card per source line. Language formats consequently allocated fixed columns. FORTRAN conventionally used columns 1–5 for labels, 6 for continuation, 7–72 for statements and 73–80 for identification or sequence data.

- **[D]** COBOL similarly inherited fixed-column divisions. IBM Job Control Language and batch operating systems treated card images as records even after terminals and disk files replaced the physical card.

- **[S]** The continuing 80-column terminal and text-editor tradition has several causes, but card width is a major documented ancestor. It is not the sole cause of every later 80-character style guideline.

- **[P]** Programmers recall submitting decks to operators, waiting for a batch run and receiving line-printer output; keypunching was often performed by specialist operators from handwritten coding sheets.

- **[P/Q]** Accounts differ sharply by institution. Some programmers personally punched cards; others never touched a keypunch. Turnaround might be minutes at a lightly loaded university or a day at a large batch installation. There was no single “punched-card programming experience.”

## 4. Standardization

- **[D]** X3.26 was sponsored by the Business Equipment Manufacturers Association and approved by ANSI on 19 January 1970. The Office of Management and Budget approved it for federal use on 16 June 1971 as FIPS PUB 14. [ANSI X3.26-1970](https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf).

- **[D]** The standard was developed by ANSI Committee X3 on Computers and Information Processing, chaired at approval by C. A. Phillips, with Alexander C. Grove as secretary. The published roster records representatives of manufacturers, government agencies and user organizations.

- **[D]** ANSI X3.26-1980 revised the standard and was federally adopted as FIPS PUB 14-1. [FIPS PUB 14-1](https://www.govinfo.gov/content/pkg/GOVPUB-C13-ae993250946603686b40e5d15bda75a8/pdf/GOVPUB-C13-ae993250946603686b40e5d15bda75a8.pdf).

- **[D]** ISO 1681:1973 standardized physical characteristics of general-purpose unpunched paper cards. ISO 6586:1980 specified implementation of ISO seven- and eight-bit character sets on punched cards. These are distinct from ANSI X3.26. [ISO 1681 catalogue](https://www.iso.org/standard/6296.html).

- **[S]** X3.26 arrived after the medium’s practical conventions were mature and after ASCII and EBCDIC had divided the electronic-character market. It regularized interchange more than it created ordinary Hollerith practice.

## 5. Decline

- **[D]** Magnetic tape offered higher speed and far greater density, while disks and interactive terminals removed the need to transport and sequence physical decks. [IBM history](https://www.ibm.com/history/punched-card).

- **[D]** IBM consciously began leaving card data processing in the late 1960s and closed its last U.S. punched-card manufacturing plant, in Washington, D.C., at the end of 1984. [Washington Post, 2 July 1984](https://www.washingtonpost.com/archive/business/1984/07/02/ibm-punch-card-plant-will-close/ec29daaf-2c2a-496b-90d0-e6569340fd2d/).

- **[D]** The IBM 129, announced in 1971, was IBM’s last keypunch design. It added a small buffer permitting correction before the holes were committed. The 029 was withdrawn in the 1980s. [Columbia 029 exhibit](https://www.columbia.edu/cu/computinghistory/029.html).

- **[Q]** “Punched cards ended in 1980” is only a broad periodization. Use disappeared at different times. Some university and mainframe sites retained cards into the 1980s; specialist installations survived much longer. IBM employees reportedly continued using old cards as note cards into the early 1990s. [IBM history](https://www.ibm.com/history/punched-card).

- **[S]** A better chronology is: punched cards became central to data processing from the 1930s through the 1960s; terminal, tape and disk workflows displaced them rapidly in the 1970s; institutional remnants persisted through the 1980s and isolated legacy use later.

---

## The other scripts

## 1. The fundamental limitation

- **[D]** The conventional repertoire was designed around uppercase English, Western digits and a small set of business/programming symbols.

- **[D]** It could not directly represent lowercase, accents, Greek, Cyrillic, Hebrew, Arabic, Indic scripts, CJK ideographs or emoji.

- **[S]** Twelve physical positions offered plenty of theoretical combinations, but installed punches, readers, printers and tabulators recognized only selected patterns. Reassigning unused patterns was easier than creating interoperable keyboards, fonts, printers and sorting rules.

## 2. European Latin alphabets

- **[D/S]** National installations substituted accented letters, currency signs or punctuation for less-needed U.S. symbols. The result resembled later national ASCII variants: locally useful but not reliably interchangeable.

- **[D]** IBM machine manuals must be consulted with their country, keyboard arrangement and printer chain. A punch pattern alone may not identify the intended glyph.

## 3. Cyrillic and Greek

- **[D]** Cyrillic scientific and machine-translation projects created local card conventions. A 1958 *Mechanical Translation* paper describes assigning Cyrillic letters to IBM card punch combinations. [Edmundson, 1958](https://www.mt-archive.net/50/MT-1958-Edmundson.pdf).

- **[S]** Techniques included direct reassignment, transliteration, multiple columns or shift conventions. None became a universal Hollerith standard.

- **[D/S]** Greek faced the same repertoire and printing problems. Mathematical work often used Roman transliterations or application-specific symbol codes.

## 4. Hebrew and Arabic

- **[D/S]** Hebrew projects investigated punched cards for lexicography and text processing by the 1950s, but required custom character assignments and output machinery. [History of Hebrew computer codes](https://www.persee.fr/doc/rjuiv_0484-8616_2002_num_161_1_2758).

- **[S]** Card columns have a physical left-to-right order but no inherent display direction. Hebrew and Arabic implementations had to decide logical versus visual order at the application level.

- **[S]** Arabic added contextual shaping and joining. A card code could assign abstract letters or printed forms, but the ordinary Hollerith repertoire and line printers provided no general shaping engine.

## 5. Indic scripts

- **[S]** Indic writing requires consonants, vowel signs, combining behavior and conjunct formation far beyond the normal 48/64-character environment. Practical projects relied on transliteration, custom multi-column encodings or specialized phototypesetting/output systems.

- **Absence finding:** No evidence was found for a broadly adopted “Hollerith Indic code.” Local schemas should not be mistaken for a standard.

## 6. Chinese, Japanese and Korean

- **[D]** Thousands of ideographs made a one-column single-byte repertoire impossible. Early systems used numerical character identifiers or multi-column codes.

- **[D/Q]** IBM demonstrated a Kanji processing prototype at Expo ’70 and announced the IBM Kanji System in 1971. Its IBM 5924 keypunch was derived from the 029 and encoded a selected Kanji repertoire using two card columns. Sources disagree in secondary retellings over 12 versus 15 shift keys and approximately 2,592 versus 2,950 directly selectable characters. [IBM Kanji System overview](https://en.wikipedia.org/wiki/IBM_Kanji_System); [IBM 5924 discussion and discrepancy](https://deskthority.net/viewtopic.php?t=15556).

- **[D/S]** Japanese Katakana could be supported in smaller single-byte repertoires. Full Kanji demanded double-byte processing, custom keyboards and the IBM 2245 Kanji printer.

- **[S]** CJK card systems foreshadowed DBCS architecture: one visible character occupied more than one machine byte or card column.

## 7. Emoji

- **[M]** Emoji have no historical Hollerith encoding. Modern punch-card generators sometimes approximate emoji with multiple columns, ASCII art or arbitrary Unicode-to-hole mappings; these are artistic encodings, not compatible historical codes.

---

## People and institutions

### Herman Hollerith, 1860–1929

- **[D]** Columbia-trained engineer; Census Office employee; inventor named on the 1889 patents; founder of the Tabulating Machine Company; consultant to its successor until retirement in 1921. [Census biography](https://www.census.gov/library/photos/1880/herman-hollerith.html).

- **[S]** His strongest claim is not “inventor of the first punched card,” but creator of the first successful large-scale punched-card statistical unit-record system combining punching, electrical sensing, counting and sorting.

### John Shaw Billings, 1838–1913

- **[P/S]** Census physician credited with suggesting Jacquard-like mechanization. The exact wording survives through historical recollection rather than a design specification.

### James Legrand Powers, 1871–1927

- **[D]** Census Bureau engineer whose alternative equipment challenged Hollerith and seeded the Powers Accounting Machine Company.

### Thomas J. Watson Sr., 1874–1956

- **[D]** Joined CTR in 1914, led its commercial expansion, and presided over the 1924 renaming to IBM and the 1928 card redesign.

### Clair D. Lake, J. Royden Pierce and James W. Bryce

- **[D]** IBM engineers central to the 80-column-card decision: Lake and Pierce developed competing proposals; Bryce selected Lake’s rectangular-hole solution. [IBM history](https://www.ibm.com/history/punched-card).

### Charles A. Phillips

- **[Q]** Frequently credited with coining “Do not fold, spindle or mutilate” and later chaired ANSI X3 during X3.26’s approval. The phrase certainly appeared on returnable cards, but the precise first use and Phillips’s authorship need a contemporary company record.

### Charles E. Mackenzie

- **[D/S]** IBM engineer and author of *Coded Character Sets: History and Development* (1980), the most detailed single reconstruction of card codes, BCD, EBCDIC and ASCII standardization. Mackenzie was close to the standards work, but the book is a retrospective technical history rather than a neutral contemporary transcript. [Internet Archive edition](https://archive.org/details/codedcharacterse00unse).

### Institutions

- **[D]** The U.S. Census Office/Bureau supplied the initial problem, procurement contest, operational laboratory and later rival development shop.

- **[D]** Hollerith’s Tabulating Machine Company, CTR and IBM supplied the dominant commercial lineage.

- **[D]** Powers, Powers-Samas and Remington Rand supplied the principal alternative lineage.

- **[D]** ANSI Committee X3, the Business Equipment Manufacturers Association, the National Bureau of Standards and OMB standardized the late interchange code.

- **[D]** ISO standardized card stock and international character-set implementation.

### People not directly responsible

- **[S]** Baudot and Murray belong to the parallel history of telegraph codes, not the design lineage of the Hollerith alphabet. Bemer, Davis, Mackenzie and others belong to ASCII-era standardization; Thompson, Pike, Becker, Collins, Whistler and the Unicode founders belong to later universal-character work. Their codes eventually absorbed card data, but they did not design the original Hollerith code.

---

## Culture

## 1. “Do not fold, spindle or mutilate”

- **[D]** Returnable cards often carried warnings against damage because folds, staples, spindle holes or extra punches could jam equipment or change data. The Smithsonian preserves examples. [Smithsonian library card](https://www.si.edu/object/ibm-z27004-library-card%3Anmah_1214020).

- **[D/S]** By the 1960s the phrase had become a metaphor for bureaucratic treatment of people. Berkeley students wore slogans such as “Do not fold, spindle or mutilate—I am a student.” A 1965 student-newspaper editorial treated the IBM card as a symbol of depersonalizing administration. [Cultural-history text](https://www.landley.net/history/mirror/pre/fsm.html).

- **[D]** The phrase supplied titles for a 1967 Canadian film, Doris Miles Disney’s 1970 novel and a 1971 television adaptation.

- **[Q]** Charles A. Phillips is often named as the phrase’s author, but the first printed card and dated corporate attribution remain insufficiently established in the accessible sources.

## 2. The card deck as labor discipline

- **[P/S]** Card systems divided intellectual and clerical work: analyst or programmer, coding-sheet writer, keypunch operator, verifier, computer operator and output clerk could be different people.

- **[S]** Fixed fields made institutional schemas physically visible. A person became a unit record; a program became a deck; sequence and validity were properties of paper objects managed by queues and operators.

- **[P]** Veteran accounts emphasize noise, card dust or “chad,” heavy boxes, diagonal deck markings, rubber bands, job windows and anxiety about one bad punch.

## 3. Lace cards

- **[P/F]** A card with every possible hole punched was called a “lace card,” “doily” or similar names. It was extremely weak and could jam or shed material in a reader.

- **[F]** Tales of deliberately feeding lace cards to sabotage a machine are widespread. They describe a physically plausible nuisance, but individual dramatic incidents are rarely documented.

## 4. Programming’s visible inheritance

- **[S]** Eighty-column source formats, sequence fields, “card image” records, job “decks,” batch queues and card-oriented command syntax survived after physical cards disappeared.

- **[S]** EBCDIC’s non-contiguous alphabet and modern mainframe translation problems are direct coding residues of the card’s zone layout.

- **[M]** ASCII art and the demoscene belong primarily to terminal and display encodings, not Hollerith. Punched cards did produce graphic images through patterns of holes, but calling all such work “ASCII art” is retroactive.

## 5. The “plain text” ideal

- **[S]** Hollerith demonstrates that text is never wholly plain: meaning depends on card stock, orientation, row assignments, keyboard repertoire, printer chain and record layout.

- **[S]** Its history anticipates mojibake. Reading an IBM 026 FORTRAN punch with a commercial or EBCDIC table can yield plausible but wrong punctuation—the physical holes survive while the code agreement is lost.

---

## Controversies and disputes

## 1. Who invented punched cards?

- **[D]** Punched media existed in textile control before Hollerith.

- **[D]** Hollerith patented a statistical recording and electrical tabulating system, not the abstract idea of making holes in cards.

- **[S]** “Inventor of punched-card data processing” is defensible; “inventor of punched cards” is not.

## 2. Jacquard versus railway-ticket inspiration

- **[Q]** Both stories appear in reputable institutional histories. The most economical reconstruction assigns Billings/Jacquard to the general mechanization concept and the conductor’s punch photograph to positional personal data on a portable record. There is no evidence that one must displace the other.

## 3. Was the 1890 census completed in record time?

- **[Q]** Yes in important tabulation stages; no if the claim means that every 1890 census publication was complete almost immediately. Comparisons often mix data capture, preliminary population counts and final publication.

## 4. IBM, monopoly and compatibility

- **[D]** IBM’s 80-column format increased capacity and required IBM-compatible machinery. Card sales were extraordinarily profitable.

- **[S]** Compatibility and lock-in are both supported interpretations. Treating the design as either purely technical progress or purely anticompetitive intent ignores half the record.

- **[D]** U.S. antitrust action addressed IBM’s practice of tying machine leases to IBM card purchases; a 1936 consent decree helped create an independent card-supply market.

## 5. IBM and Nazi Germany

- **[D]** Dehomag, IBM’s German subsidiary, supplied Hollerith machines used for German censuses and administrative work under the Nazi regime.

- **[D]** The 1933 and 1939 censuses included information from which aggregate Jewish populations could be tabulated. The United States Holocaust Memorial Museum cautions that identifying and locating victims did not depend exclusively—or in most occupied territories primarily—on punched-card technology. [USHMM, “Locating the Victims”](https://encyclopedia.ushmm.org/content/en/article/locating-the-victims).

- **[Q]** Edwin Black’s *IBM and the Holocaust* (2001) argues that IBM’s technology and corporate involvement were central to multiple stages of persecution and extermination. The book established extensive commercial involvement but its claims about indispensability, knowledge and direct operational control are disputed.

- **[D/Q]** Auschwitz-Birkenau Museum historian Franciszek Piper stated in 2001 that no Hollerith machines operated at Auschwitz itself; stamped records may have been processed elsewhere. Piper added evidence for a Hollerith department at Stutthof in 1944. [Auschwitz-Birkenau Museum statement](https://www.auschwitz.org/en/museum/news/ibm-i-n-auschwitz-concentration-camp-no-hollerith-machines-at-auschwitz-concentration-camp%2C259.html).

- **[S]** The evidence supports neither denial of Nazi use nor the simple claim that “Hollerith cards caused the Holocaust.” The historically defensible position is that tabulating machinery increased administrative capacity; the extent of IBM headquarters’ knowledge and its operational indispensability remain contested.

## 6. The status of X3.26

- **[D]** X3.26 was a real approved standard, not merely a proposal.

- **[Q]** Its actual deployment for full 128- or 256-character interchange appears much narrower than the installed use of traditional 48/64-character IBM and EBCDIC card codes. Adoption as a federal standard proves administrative status, not ubiquity.

- **Absence finding:** No evidence located here supports the claim that most card decks ever used the full X3.26 repertoire.

## 7. “Hollerith code became EBCDIC”

- **[S]** This is substantially true as a lineage claim but false as an identity. Card patterns influenced six-bit BCD forms; IBM then extended and rearranged that family into eight-bit EBCDIC. Translation steps, special cases and code-page variants intervene.

## 8. The first alphabetic punched card

- **[Q]** Popular IBM histories often make the IBM alphabet appear inevitable. Powers-Samas had commercially important alphabetic machinery by the early 1920s, before IBM’s 1930s alphabetic expansion. Priority depends on whether “first” means experimental representation, working machine, commercial installation or the later dominant pattern.

## 9. Privacy and the unit record

- **[S]** Hollerith’s system made population characteristics cheaply sortable and cross-tabulated. That supported beneficial administration and science but also classification, surveillance and discriminatory policy.

- **[S]** The political risk is not encoded in a particular hole pattern. It arises from institutional collection, categories, identifiers, linkage and power. The same distinction matters in evaluating both census modernization and Nazi use.

## 10. Relation to later Unicode controversies

- **[S]** Han unification, bidirectional text, emoji selection, homoglyphs, byte-order marks and UTF-8 security are not controversies of Hollerith code. They arise in universal and networked character standards decades later.

- **[S]** Hollerith is nevertheless an instructive predecessor: repertoire decisions privileged particular users; vendor equipment defined practical interoperability; one physical pattern could receive different glyphs; and unencoded communities depended on transliteration or bespoke systems.

- **Absence finding:** Searches combining Hollerith with “Han unification,” “mojibake,” “homoglyph security” and similar terms produced no evidence of a historical design dispute connecting those subjects. Treating them as Hollerith-era debates would be a modern invention.

---

## Adoption timeline

| Date | Event | Evidence |
|---:|---|---|
| 1720s–1800s | Punched media developed for textile control; Jacquard’s linked cards became the famous precursor | **[D/S]** Institutional histories |
| 1880 | Hollerith worked around the U.S. census problem | **[D]** Census records |
| 1884 | Earliest Hollerith patent applications filed | **[D]** Patent record |
| 1887 | Baltimore-area trial and development work | **[D]** Census history |
| 1888 | Census competition | **[D]** Census retrospective |
| 8 Jan. 1889 | U.S. patents 395,781–395,783 granted | **[D]** Patent record |
| Apr. 1889 | “An Electric Tabulating System” published | **[D]** Columbia bibliography |
| 1890 | Hollerith system used in U.S. census; Columbia doctorate | **[D]** Census and university records |
| 1894 | Paper presented to Royal Statistical Society | **[D]** Bibliographic record |
| 1896 | Tabulating Machine Company founded | **[D]** Corporate/government history |
| 1900 | Hollerith equipment again used for U.S. census | **[D]** Census history |
| 1910 | Census Bureau alternatives, including Powers machinery, compete | **[D]** Census/Smithsonian |
| 1911 | Powers company founded; Hollerith firm merged into CTR | **[D]** Institutional histories |
| 1924 | CTR renamed IBM | **[D]** IBM/Census history |
| 1928 | IBM introduces 80-column rectangular-hole card | **[D]** IBM history |
| 1930 | Twelve-row version appears | **[D]** IBM history |
| Early 1930s | IBM expands alphabetic processing | **[D/S]** IBM/manual history |
| 1935 | Social Security creates massive card workload | **[D]** IBM history |
| 1936 | U.S. consent decree addresses card-supply tying | **[D/S]** Antitrust history |
| 1940s | Cards central in business, government and scientific computation | **[D]** Manuals and archives |
| 1949 | IBM 024/026 keypunch generation introduced | **[D]** IBM manuals |
| Early 1950s | Six-bit card-derived BCD codes used in electronic IBM systems | **[D]** Machine manuals |
| 1952–59 | IBM 701/702/704/650/1401 generation expands card computing | **[D]** IBM manuals |
| 1959 | IBM 1401 announced with six-bit BCD character storage | **[D]** IBM documentation |
| 1964 | System/360 and EBCDIC; IBM 029 keypunch | **[D]** IBM documentation |
| 1960s | U.S. card consumption and institutional use near peak | **[S]** Industry histories |
| 19 Jan. 1970 | ANSI X3.26-1970 approved | **[D]** Standard |
| 1971 | FIPS PUB 14 federal adoption; IBM 129 and Kanji system era | **[D]** Standards/manuals |
| 1973 | ISO 1681 paper-card specification | **[D]** ISO |
| 1980 | ANSI X3.26 revised; ISO 6586 published | **[D]** Standards catalogues |
| 1980s | General card use ends at most computing sites | **[S/P]** Institutional and participant evidence |
| End 1984 | IBM closes its last U.S. punch-card plant | **[D]** Contemporary press |
| 1991 | X3.26 reaffirmation reflected in later catalogue record | **[D]** Standards catalogue |
| 2013 | ANSI/INCITS 26 withdrawn | **[D]** Catalogue |
| 2020 | ISO 1681:1973 reconfirmed | **[D]** ISO catalogue |
| Present | Museums, restorations, archives, art and isolated legacy workflows preserve the medium | **[D/S]** Museum and institutional sites |

---

## What survives

- **[D]** EBCDIC code pages retain the three discontinuous alphabetic blocks inherited through card-derived BCD.

- **[D]** Mainframe files, database exports and network transfers still require EBCDIC/Unicode conversion.

- **[S]** Fixed 80-column display conventions, source-code style limits and “card image” records are cultural and software descendants.

- **[D]** FORTRAN and COBOL fixed-form layouts remain supported by modern compilers.

- **[S]** Mojibake involving `¢`, `¬`, brackets, currency signs and punctuation often reflects differences among EBCDIC code pages whose history reaches back to incompatible keypunch and printer repertoires.

- **[D]** Museums including the Computer History Museum maintain working IBM 1401 systems and keypunch demonstrations.

- **[S]** The card remains a compact emblem of bureaucratic computation: durable, legible to trained humans, physically sortable—and constrained by an institutional schema literally printed onto the medium.

---

## Open questions

1. **The first documented dollar-bill explanation.** Who first asserted that card dimensions copied U.S. currency, in what publication, and on what evidence?

2. **The first printed “fold, spindle or mutilate” warning.** A dated specimen or corporate directive is needed to establish authorship and whether Charles A. Phillips coined the exact phrase.

3. **Alphabet priority.** A comparative chronology of Powers-Samas and IBM engineering records could distinguish first experiment, first commercial alphabetic machine and first use of the later IBM punch assignments.

4. **X3.26 deployment.** Which federal or commercial installations actually exchanged full ASCII or eight-bit X3.26 cards, as opposed to using the standard’s traditional subset?

5. **System/360’s ASCII option.** Surviving IBM project memoranda and oral histories may clarify which ASCII capabilities were planned, when they were curtailed, and how much the peripheral schedule dictated EBCDIC.

6. **National repertoires.** Many non-English card codes survive only in equipment manuals, local documentation and physical decks. A complete catalogue would require country-by-country archival work.

7. **CJK IBM 5924 figures.** Secondary accounts conflict over the number of shift keys and directly selectable characters. The definitive answer requires the original Japanese IBM announcement and engineering manual.

8. **Nazi-era corporate control.** The machinery’s use is established; the degree of IBM headquarters’ knowledge and operational control across 1933–45 remains a documentary and historiographical dispute.

9. **End dates.** IBM’s 1984 plant closure is well documented, but the last continuous operational use of standard 80-column cards is inherently difficult to establish.

---

## Sources consulted

### Primary patents, standards and government records

1. Herman Hollerith, U.S. Patent 395,782, *Art of Compiling Statistics*, granted 8 January 1889:  
   https://patents.google.com/patent/US395782A/en

2. USPTO, “Count Me In,” discussion of patents 395,781–395,783:  
   https://www.uspto.gov/learning-and-resources/journeys-innovation/historical-stories/count-me

3. U.S. Census Bureau scan of Hollerith patent material:  
   https://www2.census.gov/about/history/agency-history/innovations/technology/hollerith-machine/hollerith-patent.pdf

4. U.S. Census, *Report on Population of the United States at the Eleventh Census: 1890*, discussion of card tabulation:  
   https://www2.census.gov/prod2/decennial/documents/1890a_v1-05.pdf

5. ANSI X3.26-1970 / FIPS PUB 14, *Hollerith Punched Card Code*:  
   https://www.govinfo.gov/content/pkg/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f/pdf/GOVPUB-C13-e3451a498e87e3f4269328d3ab8d278f.pdf

6. ANSI X3.26-1980 / FIPS PUB 14-1, *Hollerith Punched Card Code*:  
   https://www.govinfo.gov/content/pkg/GOVPUB-C13-ae993250946603686b40e5d15bda75a8/pdf/GOVPUB-C13-ae993250946603686b40e5d15bda75a8.pdf

7. Alternate scan, ANSI X3.26-1980:  
   https://www.bitsavers.org/pdf/ansi/X3/X3.026-1980_Hollerith_Punched_Card_Code.pdf

8. ANSI/INCITS catalogue record for INCITS 26-1980 (R1991), withdrawn:  
   https://shop.standards.ie/en-ie/standards/ansi-incits-26-80-r1991--614614_saig_iti_iti_1414020/

9. ISO 1681:1973, *Information processing—Unpunched paper cards—Specification*:  
   https://www.iso.org/standard/6296.html

### IBM manuals and institutional IBM material

10. IBM, “The punched card”:  
    https://www.ibm.com/history/punched-card

11. IBM, “The punched card tabulator”:  
    https://www.ibm.com/history/punched-card-tabulator

12. IBM 24/26 Card Punch Reference Manual, A24-0520-3, October 1965:  
    https://bitsavers.org/pdf/ibm/punchedCard/Keypunch/024-026/A24-0520-3_24_26_Card_Punch_Reference_Manual_Oct1965.pdf

13. IBM 29 Card Punch Reference Manual, GA24-3332-6, June 1970:  
    https://www.masswerk.at/keypunch/manuals/IBM029-GA24-3332-6_Reference_Manual_Model_29_Card_Punch_Jun70.pdf

14. Columbia University, “The IBM 029 Key Punch”:  
    https://www.columbia.edu/cu/computinghistory/029.html

15. IBM 1401 Restoration Project, documentation supplement:  
    https://ibm1401.computerhistory.org/i1401_doc-supplement.html

16. IBM 1401 restoration, *Theory of Operation*:  
    https://ibm1401.computerhistory.org/IBM-1401-Theory-of-Operation-GF.pdf

17. IBM 1401 document index:  
    https://www.bitsavers.org/1401/1401-docs.html

18. IBM System/360 Model 20 Functional Characteristics, A26-5847-3, April 1967:  
    https://www.bitsavers.org/pdf/ibm/360/functional_characteristics/A26-5847-3_360-20_funChar_Apr67.pdf

19. IBM EBCDIC collating-sequence documentation:  
    https://www.ibm.com/docs/en/ssw_ibm_i_74/db2/rbafzsortsequence.htm

20. IBM DBCS code-scheme documentation:  
    https://www.ibm.com/docs/en/i/7.5.0?topic=fundamentals-dbcs-code-scheme

21. IBM Japan corporate chronology:  
    https://www.ibm.com/jp-ja/about/ibm-japan-history

### Contemporary and scholarly histories

22. Charles E. Mackenzie, *Coded Character Sets: History and Development*, Addison-Wesley, 1980, Internet Archive edition:  
    https://archive.org/details/codedcharacterse00unse

23. Open Library bibliographic record for Mackenzie:  
    https://openlibrary.org/books/OL4570655M/Coded_character_sets

24. Columbia University Computing History, “Herman Hollerith”:  
    https://columbia.edu/cu/computinghistory/hollerith.html

25. U.S. Census Bureau, “Herman Hollerith”:  
    https://www.census.gov/library/photos/1880/herman-hollerith.html

26. U.S. Census Bureau, “The Hollerith Machine”:  
    https://www.census.gov/about/history/bureau-history/census-innovations/technology/hollerith-machine.html

27. U.S. Census Bureau, “Tabulation and Processing”:  
    https://www.census.gov/about/history/bureau-history/census-innovations/technology/tabulation-and-processing.html

28. Smithsonian Institution, “Punch Cards for Data Processing”:  
    https://americanhistory.si.edu/collections/object-groups/punch-cards/punch-cards-data-processing

29. Smithsonian, “The Bureau of the Census to Remington Rand”:  
    https://www.si.edu/spotlight/tabulating-equipment/the-bureau-of-the-census-to-remington-rand

30. IEEE Engineering and Technology History Wiki, “Early Punched Card Equipment, 1880–1951”:  
    https://ethw.org/Early_Punched_Card_Equipment%2C_1880_-_1951

31. William Heckbert, “‘Do Not Fold, Spindle or Mutilate’: A Cultural History of the Punch Card”:  
    https://www.ioccc.org/1987/heckbert/FoldSpindleMutilate.pdf

32. Accessible mirror of the cultural-history text:  
    https://www.landley.net/history/mirror/pre/fsm.html

33. Smithsonian IBM Z27004 punched library card:  
    https://www.si.edu/object/ibm-z27004-library-card%3Anmah_1214020

34. Nicholas Metropolis and related historical reconstruction, “The Los Alamos Computing Facility during the Manhattan Project”:  
    https://arxiv.org/abs/2103.05705

35. H. P. Edmundson, punched-card conventions for Cyrillic in *Mechanical Translation*, vol. 5, no. 1, July 1958:  
    https://www.mt-archive.net/50/MT-1958-Edmundson.pdf

36. “Hebrew alphabets, symbols and computer codes: History and preliminary tabulation”:  
    https://www.persee.fr/doc/rjuiv_0484-8616_2002_num_161_1_2758

### Decline, preservation and controversy

37. *Washington Post*, “IBM Punch-Card Plant Will Close,” 2 July 1984:  
    https://www.washingtonpost.com/archive/business/1984/07/02/ibm-punch-card-plant-will-close/ec29daaf-2c2a-496b-90d0-e6569340fd2d/

38. United States Holocaust Memorial Museum, “Locating the Victims”:  
    https://encyclopedia.ushmm.org/content/en/article/locating-the-victims

39. Auschwitz-Birkenau State Museum, “IBM in Auschwitz Concentration Camp? No Hollerith Machines at Auschwitz Concentration Camp,” 12 February 2001:  
    https://www.auschwitz.org/en/museum/news/ibm-i-n-auschwitz-concentration-camp-no-hollerith-machines-at-auschwitz-concentration-camp%2C259.html

40. *Washington Post*, review discussing the evidence and limits of Edwin Black’s claims:  
    https://www.washingtonpost.com/archive/entertainment/books/2001/03/18/big-bad-blue/e704b4e9-7733-4a35-94c5-ea3220a04773/

41. Wired, “The Undead,” on continuing punched-card manufacture and estimated U.S. consumption:  
    https://www.wired.com/1999/03/punchcards/

### Secondary indexes used cautiously

42. Punched card overview and standards index:  
    https://en.wikipedia.org/wiki/Punched_card

43. BCD character-code comparison index:  
    https://en.wikipedia.org/wiki/BCD_%28character_encoding%29

44. EBCDIC history index:  
    https://en.wikipedia.org/wiki/EBCDIC

45. IBM Kanji System index:  
    https://en.wikipedia.org/wiki/IBM_Kanji_System

46. Discussion identifying discrepancies in IBM 5924 keyboard figures:  
    https://deskthority.net/viewtopic.php?t=15556

47. Columbia’s IBM computing-history collection:  
    https://www.columbia.edu/cu/computinghistory/

48. Computer History Museum IBM 1401 Restoration Project:  
    https://ibm1401.computerhistory.org/
