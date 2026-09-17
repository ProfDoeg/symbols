# slavic: interaction matrix

12 gods, 42 distinct relations (13 kinship, 29 meetings, myths and identifications), 88 mentions of beings without a dossier here. Built by tools/build_matrix.py from relations/*.json (Codex extraction of each dossier's genealogy and interaction sections). Matrix of counts in _matrix.csv; full records with sources in _relations.json.

## Most connected

| god | relations with | distinct gods |
|---|---|---|
| jarilo | 10 | 5 |
| morana | 11 | 5 |
| perun | 17 | 5 |
| dazhbog | 7 | 4 |
| mokosh | 13 | 4 |
| veles | 15 | 4 |
| baba_yaga | 4 | 2 |
| koschei | 3 | 1 |
| svarog | 3 | 1 |
| svetovid | 1 | 1 |
| leshy | 0 | 0 |
| rusalki | 0 | 0 |

## Each god

### baba_yaga  (2 gods)
- **koschei**: gift, served_by, shared_myth; Marya Morevna
- **morana**: identified_with

### dazhbog  (4 gods)
- **svarog**: child_of, other; Dazhbog as Sun, son of Svarog; Dazhbog succeeds Svarog as ruler; Succession of Svarog
- **mokosh**: shared_myth; Vladimir installs the Kievan pantheon; Vladimir’s Kyiv pantheon
- **jarilo**: identified_with
- **perun**: shared_myth; Vladimir’s Kyiv pantheon

### jarilo  (5 gods)
- **morana**: consort_of, killed_by, shared_myth, sibling_of; Annual fertility, betrayal, death, and regeneration; Jarilo–Morana seasonal cycle; Jarilo–Morana seasonal wedding; Morana’s revenge
- **dazhbog**: identified_with
- **perun**: child_of
- **svetovid**: identified_with
- **veles**: other; Child taken into Veles’s otherworld

### koschei  (1 gods)
- **baba_yaga**: gift, served, shared_myth; Marya Morevna

### leshy  (0 gods)

### mokosh  (4 gods)
- **perun**: consort_of, punished_by, shared_myth; Reconstructed Perun–Veles conflict; Reconstructed punishment of the adulteress; Vladimir installs the Kievan pantheon; Vladimir’s Kyiv pantheon
- **veles**: consort_of, identified_with, theft; Mokosh as Veles’s wife or lover; Reconstructed Perun–Veles conflict; Veles abducts the thunderer’s woman
- **dazhbog**: shared_myth; Vladimir installs the Kievan pantheon; Vladimir’s Kyiv pantheon
- **morana**: identified_with, parent_of

### morana  (5 gods)
- **jarilo**: consort_of, killed, shared_myth, sibling_of; Annual fertility, betrayal, death, and regeneration; Jarilo–Morana seasonal cycle; Jarilo–Morana seasonal wedding; Morana’s revenge
- **mokosh**: child_of, identified_with
- **baba_yaga**: identified_with
- **perun**: punished_by
- **veles**: consort_of; Underworld partnership

### perun  (5 gods)
- **veles**: fought, shared_myth, theft; Condemned pagan gods listed together; Oleg’s men swear by Perun and Volos; Oleg’s purported oath; Perun pursues Veles with thunderbolts
- **mokosh**: consort_of, punished, shared_myth; Reconstructed Perun–Veles conflict; Reconstructed punishment of the adulteress; Vladimir installs the Kievan pantheon; Vladimir’s Kyiv pantheon
- **dazhbog**: shared_myth; Vladimir’s Kyiv pantheon
- **jarilo**: parent_of
- **morana**: punished

### rusalki  (0 gods)

### svarog  (1 gods)
- **dazhbog**: other, parent_of; Dazhbog as Sun, son of Svarog; Dazhbog succeeds Svarog as ruler; Succession of Svarog

### svetovid  (1 gods)
- **jarilo**: identified_with

### veles  (4 gods)
- **perun**: fought, shared_myth, theft; Condemned pagan gods listed together; Oleg’s men swear by Perun and Volos; Oleg’s purported oath; Perun pursues Veles with thunderbolts
- **mokosh**: consort_of, identified_with, theft; Mokosh as Veles’s wife or lover; Reconstructed Perun–Veles conflict; Veles abducts the thunderer’s woman
- **jarilo**: other; Child taken into Veles’s otherworld
- **morana**: consort_of; Underworld partnership

## Named but without a dossier here

- Khors (6): dazhbog, jarilo, mokosh, perun, veles
- Ivan Tsarevich (4): koschei
- Stribog (3): dazhbog, mokosh, perun
- Simargl (3): dazhbog, mokosh, perun
- St George (2): jarilo, leshy
- Kostroma (2): jarilo, morana
- Kupala (2): jarilo, morana
- Marya Morevna (2): koschei
- Marya-Tsarevna (2): koschei
- Kashcheyevna (2): koschei
- Christ (2): leshy, perun
- neighboring Leshies (2): leshy
- Lada (2): morana, svarog
- Chernobog (2): morana
- Svarozhich (2): svarog
- Bright Day (1): baba_yaga
- Red Sun (1): baba_yaga
- Dark Night (1): baba_yaga
- Sea Tsar (1): baba_yaga
- Serpent/Dragon (1): baba_yaga
- Baba Yaga sisters (1): baba_yaga
- crocodile (1): baba_yaga
- Jarovit (1): jarilo
- Kostrub (1): jarilo
- Ivan Godinovich (1): koschei
- Nastasya (1): koschei
- Mikhailo Potyk (1): koschei
- Falcon husband (1): koschei
- Eagle husband (1): koschei
- Raven husband (1): koschei
- Nenaslyadnaya Krasota (1): koschei
- Vasilisa Kirbitevna (1): koschei
- Bulat (1): koschei
- Vasilisa the Wise (1): koschei
- Firebird (1): koschei
- Prince Ivan (1): koschei
- Princess of Unearthly Beauty (1): koschei
- leshachikha (1): leshy
- leshata (1): leshy
- the Virgin (1): leshy
- St Nicholas (1): leshy
- Polevik (1): leshy
- Domovoi (1): leshy
- Bannik (1): leshy
- Forest Tsar (1): leshy
- vily (1): mokosh
- Rod (1): mokosh
- the Rozhanitsy (1): mokosh
- vampires (1): mokosh
- beregyni (1): mokosh
- Matʹ Syra Zemlia (1): mokosh
- Paraskeva Pyatnitsa (1): mokosh
- the Moirai (1): mokosh
- Vesna (1): morana
- Dziewanna (1): morana
- Elijah (1): perun
- Ježibaba (1): rusalki
- Vodník (1): rusalki
- Three wood nymphs (1): rusalki
- Radegast (1): svarog
