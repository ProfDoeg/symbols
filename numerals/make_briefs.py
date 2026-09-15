#!/usr/bin/env python3
"""Write one brief per numeral system into numerals/briefs/, roughly in order of first attestation."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "briefs")

SYSTEMS = [
 ("tally_marks", "Tally marks and counting bones", "the oldest counting: the Lebombo bone (c. 42,000 BP, 29 notches) and the Ishango bone (c. 20,000 BP, the prime-number and lunar readings and their critics), tally sticks from the Exchequer (burned in 1834 and the fire that destroyed Parliament), the notched sticks of shepherds, the five-bar gate and the Chinese 正 tally, body-counting systems of New Guinea, the base-of-all-bases"),
 ("mesopotamian_tokens_and_cuneiform", "Sumerian and Babylonian numerals (the tokens and the sexagesimal system)", "Schmandt-Besserat's clay tokens (8000-3000 BCE) and the bullae, the Uruk proto-cuneiform numerals (c. 3300 BCE) and the several metrological systems, the Sumerian sexagesimal place-value system of Ur III (c. 2100 BCE), the Old Babylonian tablets (Plimpton 322, YBC 7289 the square root of two), the absent then present zero (the Seleucid placeholder), Robson's and Høyrup's readings, the 60 that survives in our minutes, seconds and degrees"),
 ("egyptian_numerals", "Egyptian numerals (hieroglyphic and hieratic)", "the additive decimal hieroglyphs (stroke, hobble, coil, lotus, finger, tadpole, the god Heh for a million) on the Narmer macehead (c. 3000 BCE) and the tomb of Hesy-Ra; the hieratic ciphered numerals of the papyri; the Rhind Papyrus (Ahmes, c. 1550 BCE, British Museum) and the Moscow papyrus; the unit fractions and the Eye of Horus fractions (and the modern doubt about that reading); multiplication by doubling; the demotic numerals"),
 ("chinese_numerals", "Chinese numerals, counting rods and the abacus", "the oracle-bone numerals (c. 1200 BCE), the standard characters 一二三 and the financial 壹貳參, the rod numerals (suanchou) as a decimal place-value system with zero as a blank then as 〇 (the Song dynasty), the Nine Chapters on the Mathematical Art, Liu Hui, negative numbers in red and black rods, the suan pan abacus and its Japanese soroban, the priority disputes with India over place value and zero (Needham, Martzloff, Lam Lay Yong), the numerals in Japan, Korea and Vietnam today"),
 ("greek_numerals", "Greek numerals (acrophonic and alphabetic)", "the Attic acrophonic system (Ι Π Δ Η Χ Μ, from the initial letters of the number words, on the Athenian tribute lists and the Salamis counting board), the Ionic alphabetic system (alpha to theta for 1-9, iota to koppa for the tens, rho to sampi for the hundreds, the three archaic letters digamma, koppa, sampi, the keraia, the myriad and Archimedes's Sand Reckoner), isopsephy (Jesus 888 in Irenaeus, the Pompeii graffiti, Revelation 13:18), Diophantus's notation, Ptolemy's sexagesimal fractions with the Greek letters, the survival in Greek ordinals today"),
 ("roman_numerals", "Roman numerals", "the Etruscan origins (the tally strokes, V as half X, the Etruscan numerals in the Tuscania dice), I V X L C D M and the theories of their shapes (Mommsen's letters, the tally-mark theory, the chi-theta ciphers for 1000 and 500), the additive rule and the late subtractive convention (IV vs IIII, the clockface), the apostrophus and vinculum for large numbers, the Roman hand-abacus (the Louvre and British Museum bronze abaci), calculi and the calculator, the fractions in twelfths (uncia), Roman numerals in medieval Europe and the counter-casting (Recorde's Ground of Artes), their persistence: regnal numbers, popes, clocks, chapters, film dates, Super Bowls, the Roman-numeral dates on buildings and the errors in them"),
 ("hebrew_numerals", "Hebrew numerals and gematria", "the alphabetic numerals (aleph to tet 1-9, yod to tsade 10-90, qof to tav 100-400, the final letters for 500-900 in later usage), the avoidance of 15 and 16 (yod-heh and yod-vav as divine names, written tet-vav and tet-zayin), the geresh and gershayim marks, dates in the Hebrew calendar (the thousands omitted), gematria in the Talmud and the Kabbalah (the Sefer Yetzirah, the notarikon and temurah), chronograms on tombstones and title pages, the numerals on the pages of the Talmud, the Samaritan and Aramaic parallels"),
 ("maya_numerals", "Maya numerals and the vigesimal Long Count", "the bar-and-dot vigesimal system with the shell zero, the head-variant numerals, the Long Count (baktun, katun, tun, uinal, kin) and its base-18 exception in the second place, the earliest Long Count dates (Chiapa de Corzo 36 BCE, Tres Zapotes Stela C), the Dresden Codex Venus tables and eclipse tables, the 2012 completion of the thirteenth baktun and the myth around it, the Olmec and Zapotec precursors, the decipherment (Förstemann, Goodman, Thompson, the Knorozov controversy), the survival of the count among the Maya daykeepers"),
 ("brahmi_and_indian_numerals", "Brahmi numerals and the Indian decimal place-value system", "the Brahmi ciphered numerals in the Ashokan edicts, at Nana Ghat (c. 100 BCE) and Nasik; the transition to place value: the Bakhshali manuscript (radiocarbon dates 224-383, 680-779, 885-993 CE and the dispute), the Gwalior Chaturbhuj inscription of 876 with the zero, Aryabhata's word-numerals (499), Brahmagupta's rules for zero and negatives (628), the shunya and the bindu, the Jain and Buddhist large numbers, the Bakhshali dot; Plofker, Datta and Singh; the Cambodian zero of 683 (the Sambor inscription, Coedès, Aczel's Finding Zero)"),
 ("hindu_arabic_numerals", "Hindu-Arabic numerals and the zero in the West", "the digits' journey: the Indian numerals to Baghdad (al-Khwarizmi's On the Calculation with Hindu Numerals c. 825, surviving in Latin as Algoritmi de numero Indorum; al-Kindi), the Eastern and Western Arabic (ghubar) forms, Gerbert of Aurillac's apices and the abacus of the 990s, the Codex Vigilanus of 976 as the first Western appearance, Leonardo Fibonacci's Liber Abaci (1202, Pisa and Bugia), Sacrobosco's Algorismus, the Florentine ban of 1299 and the abacists vs algorists (Gregor Reisch's Margarita Philosophica woodcut of 1503), the words zero (sifr, zephirum, cifra, chiffre, cipher), the printed digits and their typography, the digits' shapes and the angle-counting legend, Ifrah's and Chrisomalis's accounts, the decimal point (Pellos, Stevin, Napier) and the comma"),
 ("khipu_numerals", "The khipu: knotted decimal numerals of the Andes", "the Inca knotted cords: the decimal place value by position on the cord, the three knot types (single, long, figure-eight) and their values, the absence of a knot as zero, the summation cords, the khipukamayuq, Locke's decipherment of 1912, the Aschers' Code of the Quipu (1981), Urton's binary reading (2003) and the Khipu Database Project (Harvard), the Puruchuco accounting hierarchy (2005), the Santa Valley khipus matched to a Spanish census (2018), the narrative-khipu question, Garcilaso and Guaman Poma as witnesses; and the Colegio Invisible's own quipu inscriptions on Dogecoin as the namesake (a line, not a section)"),
 ("counting_boards_and_abacus", "Counting boards and the abacus (Salamis, Rome, China, Japan, Russia)", "the Salamis tablet (c. 300 BCE), the Roman bronze hand-abacus, the medieval counter-casting on lines and the jetons (Recorde, the Exchequer's chequered cloth), the Chinese suan pan (2/5 beads), the Japanese soroban (1/4 beads) and its schools, the Russian schoty, the Aztec nepohualtzintzin (and the doubts), the abacus vs the algorism debate in Europe, the 1946 contest between a soroban and an electric calculator, the mental abacus (anzan)"),
 ("binary_and_leibniz", "Binary numerals: Leibniz, the I Ching and the machine", "Leibniz's Explication de l'Arithmétique Binaire (1703) and his reading of the sixty-four hexagrams via Bouvet's letter (1701) and Shao Yong's arrangement, the theological reading (creation from 0 and 1), Pingala's binary meters in the Chandahsutra (c. 200 BCE) as the Indian precedent, Francis Bacon's biliteral cipher (1605), Boole (1854), Shannon's thesis (1937), Zuse's Z3 (1941) and Atanasoff, the ASCII and Unicode encodings of all the other numerals in this set, the bit and the byte, octal and hexadecimal as binary's shorthands"),
 ("cistercian_and_other_ciphered_numerals", "Cistercian numerals and other ciphered systems", "the Cistercian numerals of the thirteenth century (a single glyph for 1-9999 from four quadrants of a stem; John of Basingstoke and the Greek origin claim; King's The Ciphers of the Monks, 2001; their revival by Agrippa and the Freemasons and by the internet), the Aegean and Cypriot numerals, the Ethiopic (Ge'ez) numerals from the Greek, the Armenian and Georgian letter-numerals, the Glagolitic and Cyrillic letter-numerals with the titlo, the Burmese and Thai digits, the Sinhala lith illakkam, the Kaktovik Inupiaq numerals (1994) as the newest system"),
]

SIGNS = {}
for i, (slug, name, pointers) in enumerate(SYSTEMS, start=1):
    SIGNS[f"{i:02d}_{slug}"] = (name, f"numeral system {i} of {len(SYSTEMS)} in this set", pointers)

ORDER = list(SIGNS.keys())

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for slug, (name, status, pointers) in SIGNS.items():
        text = f"""# {name}: research brief

Numeral-systems research, Anthony 2026-09-15, separate from the atlas. Appended to
PROMPT_TEMPLATE_NUMERALS.md by tools/codex_dossier_set.py.

---

SYSTEM. {name}: {status}. Give at the top the base, the type (additive, ciphered, positional),
the signs, the period and the region.

THREADS TO PULL, each to be verified against the sources and dated: {pointers}.

STANCE. Legend as fully as fact. Every claim labeled: documented artefact or text, scholarly
reconstruction, tradition, disputed, legend, modern invention. Where a thread above names a
dispute, present both sides with their evidence. Give the worked tables (1 to 20, the powers of
ten, famous numbers) in the system's own signs. Absence of evidence is a finding.
"""
        open(os.path.join(OUT, f"{slug}.brief.md"), "w").write(text)
    print("wrote", len(SIGNS), "briefs")
