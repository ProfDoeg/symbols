# etruscan: interaction matrix

12 gods, 57 distinct relations (4 kinship, 53 meetings, myths and identifications), 134 mentions of beings without a dossier here. Built by tools/build_matrix.py from relations/*.json (Codex extraction of each dossier's genealogy and interaction sections). Matrix of counts in _matrix.csv; full records with sources in _relations.json.

## Most connected

| god | relations with | distinct gods |
|---|---|---|
| tinia | 17 | 8 |
| menrva | 22 | 6 |
| turms | 17 | 6 |
| uni | 16 | 5 |
| fufluns | 4 | 4 |
| sethlans | 6 | 4 |
| turan | 13 | 4 |
| aita | 4 | 2 |
| tages | 2 | 2 |
| vanth | 6 | 2 |
| voltumna | 2 | 2 |
| charun | 5 | 1 |

## Each god

### aita  (2 gods)
- **turms**: served_by, shared_myth; Abduction or return of Phersipnai; Turms escorts Teiresias before Odysseus
- **vanth**: served_by; Abduction of Phersipnai

### charun  (1 gods)
- **vanth**: allied, shared_myth; Achilles sacrifices Trojan prisoners; Funerary journey of the deceased; Guardians at the tomb doorway; Guardians at the tomb entrance

### fufluns  (4 gods)
- **menrva**: shared_myth; Artamis carries Esia before Fuflunus
- **sethlans**: allied; Return to the divine assembly
- **tinia**: child_of
- **turms**: other; Infant Fufluns

### menrva  (6 gods)
- **turan**: contest, shared_myth; Divine colloquy before an architectural setting; Hercle and Epiur presentation; Judgment of Paris; Menrva and the Maris children
- **turms**: other, shared_myth; Judgment of Paris; Menrva and the Maris children; Oracular-head scene; Perseus and Medusa
- **uni**: contest, fought, shared_myth; Birth of Menrva; Birth of Menrva from Tinia’s head; Judgment of Elcsntre; Judgment of Paris
- **tinia**: child_of, shared_myth; Assisted head-birth at Palestrina; Birth of Menrva from Tinia’s head; Hercle’s adoption into the divine family
- **sethlans**: other; Birth of Menrva; Birth of Menrva from Tinia’s head
- **fufluns**: shared_myth; Artamis carries Esia before Fuflunus

### sethlans  (4 gods)
- **menrva**: other; Birth of Menrva; Birth of Menrva from Tinia’s head
- **tinia**: other, shared_myth; Birth of Menrva
- **fufluns**: allied; Return to the divine assembly
- **uni**: rescued; Binding and liberation of Uni

### tages  (2 gods)
- **tinia**: descendant_of
- **voltumna**: shared_myth; Revelation of the Etruscan discipline

### tinia  (8 gods)
- **uni**: allied, consort_of, shared_myth; Birth of Menrva; Hercle’s adoption by Uni; Hercle’s adoption through Uni’s nursing; Uni confronts Hercle
- **menrva**: parent_of, shared_myth; Assisted head-birth at Palestrina; Birth of Menrva from Tinia’s head; Hercle’s adoption into the divine family
- **turms**: served_by, shared_myth; Reconciliation of Hercle and Apulu; Turms before the seated Tinia; Unidentified divine consultation
- **sethlans**: other, shared_myth; Birth of Menrva
- **fufluns**: parent_of
- **tages**: ancestor_of
- **turan**: shared_myth; Hercle’s adoption into the divine family
- **voltumna**: identified_with

### turan  (4 gods)
- **menrva**: contest, shared_myth; Divine colloquy before an architectural setting; Hercle and Epiur presentation; Judgment of Paris; Menrva and the Maris children
- **turms**: other, shared_myth; Judgment of Paris; Presentation of the Mariś infants; The Maris infants
- **uni**: contest, shared_myth; Aftermath of Elcsntre’s judgment; Judgment of Elcsntre; Judgment of Paris
- **tinia**: shared_myth; Hercle’s adoption into the divine family

### turms  (6 gods)
- **menrva**: other, shared_myth; Judgment of Paris; Menrva and the Maris children; Oracular-head scene; Perseus and Medusa
- **aita**: served, shared_myth; Abduction or return of Phersipnai; Turms escorts Teiresias before Odysseus
- **tinia**: served, shared_myth; Reconciliation of Hercle and Apulu; Turms before the seated Tinia; Unidentified divine consultation
- **turan**: other, shared_myth; Judgment of Paris; Presentation of the Mariś infants; The Maris infants
- **uni**: other, shared_myth; Judgment of Elcsntre; Judgment of Paris
- **fufluns**: other; Infant Fufluns

### uni  (5 gods)
- **menrva**: contest, fought, shared_myth; Birth of Menrva; Birth of Menrva from Tinia’s head; Judgment of Elcsntre; Judgment of Paris
- **tinia**: allied, consort_of, shared_myth; Birth of Menrva; Hercle’s adoption by Uni; Hercle’s adoption through Uni’s nursing; Uni confronts Hercle
- **turan**: contest, shared_myth; Aftermath of Elcsntre’s judgment; Judgment of Elcsntre; Judgment of Paris
- **turms**: other, shared_myth; Judgment of Elcsntre; Judgment of Paris
- **sethlans**: rescued_by; Binding and liberation of Uni

### vanth  (2 gods)
- **charun**: allied, shared_myth; Achilles sacrifices Trojan prisoners; Funerary journey of the deceased; Guardians at the tomb doorway; Guardians at the tomb entrance
- **aita**: served; Abduction of Phersipnai

### voltumna  (2 gods)
- **tages**: shared_myth; Revelation of the Etruscan discipline
- **tinia**: identified_with

## Named but without a dossier here

- Laran (6): fufluns, tinia, turan, turms
- Thalna (5): menrva, tinia, turan, uni
- Hercle (4): fufluns, tinia, turms
- Mean (4): menrva, tinia, turan, uni
- Semla (3): fufluns, sethlans
- Apulu (3): fufluns, sethlans, turms
- Amamtunia (3): menrva, turan, turms
- Odysseus (2): aita, vanth
- Calu (2): aita, turms
- Achilles (2): charun, vanth
- Castur (2): fufluns, tinia
- Thanr (2): menrva, tinia
- Ethausva (2): menrva, tinia
- Maris Husrnana (2): menrva, turms
- Epiur (2): menrva, tinia
- Elcsntre (2): menrva, uni
- Tarchon (2): tages
- Thesan (2): tages, tinia
- Maris (2): tinia, turms
- Paris (2): turan
- Turnu (2): turan
- Rath (2): turms, voltumna
- Teiresias (1): aita
- Hydra (1): aita
- Theseus (1): aita
- Peirithoos (1): aita
- Śuri (1): aita
- Mantus (1): aita
- Soranus (1): aita
- Tuchulcha (1): charun
- Acheron (1): charun
- Patroclus (1): charun
- Ajax (1): charun
- Penthesilea (1): charun
- Alcestis (1): charun
- Admetus (1): charun
- Sime (1): fufluns
- Esia (1): fufluns
- Vesuna (1): fufluns
- Svutaf (1): fufluns
- Eiasun (1): fufluns
- Aminth (1): fufluns
- Śeθlans (1): fufluns
- Catha (1): fufluns
- Selvans (1): fufluns
- Liber (1): fufluns
- Maris Tiusta (1): menrva
- Maris Halna (1): menrva
- Pherse (1): menrva
- Umalee (1): menrva
- Thevrumines (1): menrva
- Mine (1): menrva
- Vile (1): menrva
- Cilen (1): menrva
- Hephaistos (1): sethlans
- Veltune (1): tages
- Raθlθ (1): tages
- Vegoia (1): tages
- Bacitis (1): tages
- Pultuce (1): tinia
