# norse: interaction matrix

18 gods, 37 distinct relations (5 kinship, 32 meetings, myths and identifications), 272 mentions of beings without a dossier here. Built by tools/build_matrix.py from relations/*.json (Codex extraction of each dossier's genealogy and interaction sections). Matrix of counts in _matrix.csv; full records with sources in _relations.json.

## Most connected

| god | relations with | distinct gods |
|---|---|---|
| helgi_hundingsbane | 6 | 5 |
| dietrich_von_bern | 6 | 4 |
| gunnar | 18 | 4 |
| hagen | 8 | 3 |
| atli_etzel | 7 | 2 |
| bodvar_bjarki | 3 | 2 |
| gudrun_kriemhild | 8 | 2 |
| hrolf_kraki | 3 | 2 |
| sigmund | 7 | 2 |
| signy | 6 | 2 |
| beowulf | 1 | 1 |
| starkad | 1 | 1 |
| aslaug | 0 | 0 |
| egil | 0 | 0 |
| grettir | 0 | 0 |

Relations with the gods of the pantheon: 46 (listed under each figure as 'gods').

## Each figure

### aslaug  (0 figures, 0 gods)

### atli_etzel  (2 figures, 0 gods)
- **gunnar**: deceived, fought, killed, punished, shared_myth; Battle for the Niflung treasure; Death in the serpent enclosure; Destruction for the forbidden affair; Feast and catastrophe at Etzel's court
- **dietrich_von_bern**: allied, served_by; Campaigns and Niflung catastrophe; Dietrich’s exile at Etzel’s court

### beowulf  (1 figures, 1 gods)
- **bodvar_bjarki**: identified_with; Modern Bjarki-Beowulf comparison
- gods: folklore/grendel (fought, killed)

### bodvar_bjarki  (2 figures, 1 gods)
- **hrolf_kraki**: allied, served; Last stand at Lejre
- **beowulf**: identified_with; Modern Bjarki-Beowulf comparison
- gods: norse/urd_verdandi_skuld (fought, killed_by)

### dietrich_von_bern  (4 figures, 1 gods)
- **atli_etzel**: allied, served; Campaigns and Niflung catastrophe; Dietrich’s exile at Etzel’s court
- **gudrun_kriemhild**: fought, other; Burgundian hall battle; Guðrún’s adultery ordeal
- **gunnar**: fought; Burgundian hall battle
- **hagen**: fought; Burgundian hall battle
- gods: norse/alberich (allied, gift)

### egil  (0 figures, 1 gods)
- gods: norse/ran_and_daughters (shared_myth)

### grettir  (0 figures, 0 gods)

### gudrun_kriemhild  (2 figures, 0 gods)
- **gunnar**: gift, killed, punished, rescued, shared_myth, sibling_of; Gunnar's imprisonment after the Niflung battle; Guðrún's revenge upon Atli; Marriage of Guðrún and Sigurd; Revenge at Etzel's court
- **dietrich_von_bern**: fought, other; Burgundian hall battle; Guðrún’s adultery ordeal

### gunnar  (4 figures, 3 gods)
- **gudrun_kriemhild**: gift, killed_by, punished_by, rescued_by, shared_myth, sibling_of; Gunnar's imprisonment after the Niflung battle; Guðrún's revenge upon Atli; Marriage of Guðrún and Sigurd; Revenge at Etzel's court
- **hagen**: allied, killed_by, served_by, sibling_of; Final combat against Walter; Plot to kill Sigurd; Resistance to Atli; Siegfried's murder and Kriemhild's revenge
- **atli_etzel**: deceived_by, fought, killed_by, punished_by, shared_myth; Battle for the Niflung treasure; Death in the serpent enclosure; Destruction for the forbidden affair; Feast and catastrophe at Etzel's court
- **dietrich_von_bern**: fought; Burgundian hall battle
- gods: norse/sigurd (allied, deceived, killed, served_by); norse/brynhild (consort_of, contest, deceived, fought, punished_by); norse/alberich (other)

### hagen  (3 figures, 2 gods)
- **gunnar**: allied, killed, served, sibling_of; Final combat against Walter; Plot to kill Sigurd; Resistance to Atli; Siegfried's murder and Kriemhild's revenge
- **dietrich_von_bern**: fought; Burgundian hall battle
- **helgi_hundingsbane**: killed_by; Battle at Frekasteinn
- gods: norse/alberich (child_of, served); norse/rhinemaidens (contest)

### helgi_hundingsbane  (5 figures, 1 gods)
- **sigmund**: child_of, gift; Helgi’s naming and endowment
- **hagen**: killed; Battle at Frekasteinn
- **hrolf_kraki**: parent_of
- **signy**: other
- **starkad**: fought; Höðbroddr campaign
- gods: norse/valkyries (allied)

### hervor  (0 figures, 1 gods)
- gods: norse/vidar (killed)

### hrolf_kraki  (2 figures, 1 gods)
- **bodvar_bjarki**: allied, served_by; Last stand at Lejre
- **helgi_hundingsbane**: child_of
- gods: norse/urd_verdandi_skuld (fought, sibling_of)

### lagertha  (0 figures, 0 gods)

### ragnar_lodbrok  (0 figures, 0 gods)

### sigmund  (2 figures, 3 gods)
- **signy**: allied, rescued_by, seduced_by, sibling_of; Escape from Siggeirr’s stone prison; Sigmundr survives the she-wolf; Signý conceives Sinfjǫtli in magical disguise; Vengeance against Siggeirr
- **helgi_hundingsbane**: gift, parent_of; Helgi’s naming and endowment
- gods: norse/odin (descendant_of, fought, gift, shared_myth); norse/wagner_gods (child_of, gift, judged_by, punished_by); norse/frigg (other)

### signy  (2 figures, 0 gods)
- **sigmund**: allied, rescued, seduced, sibling_of; Escape from Siggeirr’s stone prison; Sigmundr survives the she-wolf; Signý conceives Sinfjǫtli in magical disguise; Vengeance against Siggeirr
- **helgi_hundingsbane**: other

### starkad  (1 figures, 2 gods)
- **helgi_hundingsbane**: fought; Höðbroddr campaign
- gods: norse/thor (fought, punished_by, transformed_by); norse/odin (gift, served)

## Named but without a dossier here

- Óðinn (10): bodvar_bjarki, egil, helgi_hundingsbane, hrolf_kraki, ragnar_lodbrok, signy
- The dragon (5): beowulf, sigmund
- Sigurðr Fáfnisbani (4): aslaug, helgi_hundingsbane, signy, starkad
- Grendel’s mother (4): beowulf
- Hildebrand (4): dietrich_von_bern, gunnar
- Rüdiger of Bechelaren (4): dietrich_von_bern, gunnar
- Sigrún Hǫgnadóttir (4): helgi_hundingsbane
- Heiðrekr (4): hervor
- Hvítserkr (3): aslaug, bodvar_bjarki
- Hjalti (3): bodvar_bjarki
- Widia (3): dietrich_von_bern
- Giselher (3): dietrich_von_bern, gunnar
- Heime (3): dietrich_von_bern
- Laurin (3): dietrich_von_bern
- Kárr inn gamli (3): grettir
- Glámr (3): grettir
- Vǫlsungr (3): signy
- Siggeirr (3): signy
- Ívarr inn beinlausi (2): aslaug
- Bjǫrn járnsíða (2): aslaug
- Sigurðr ormr í auga (2): aslaug
- Agnarr (2): aslaug, bodvar_bjarki
- Elg-Fróði (2): bodvar_bjarki
- Hringr (2): bodvar_bjarki, helgi_hundingsbane
- Siegfried (2): dietrich_von_bern, gunnar
- Þetleifr (2): dietrich_von_bern
- Fasolt (2): dietrich_von_bern
- Walberan (2): dietrich_von_bern
- The nameless maiden in Wunderer (2): dietrich_von_bern
- Gernot (2): gunnar
- Gothorm (2): gunnar
- Oddrún (2): gunnar
- Glaumvör (2): gunnar
- Dietrich (2): gunnar
- Osid (2): gunnar
- Dietleib (2): gunnar
- Hadburg (2): hagen
- Hundingr (2): helgi_hundingsbane
- Hámundr (2): helgi_hundingsbane, signy
- Sinfjötli (2): helgi_hundingsbane
- Hamall (2): helgi_hundingsbane
- Dagr Hǫgnason (2): helgi_hundingsbane
- Höðbroddr Granmarsson (2): helgi_hundingsbane
- Yrsa (2): helgi_hundingsbane
- Angantýr Arngrímsson (2): hervor
- Bjarmarr (2): hervor
- Hǫfundr (2): hervor
- Angantýr Heiðreksson (2): hervor
- Hlöðr (2): hervor
- Hljóð (2): sigmund, signy
- Sinfjǫtli (2): signy
- Brynhildr Buðladóttir (1): aslaug
- Heimir of Hlymdalir (1): aslaug
- Áki (1): aslaug
- Gríma (1): aslaug
- Rǫgnvaldr (1): aslaug
- Eirekr (1): aslaug
- God (1): beowulf
- Aðils (1): bodvar_bjarki
- Áli (1): bodvar_bjarki
