#!/usr/bin/env python3
"""Write one brief per element of the Tree of Life into working/tree/briefs/: the Tree as a
whole, the ten Sephiroth and Da'at, and the twenty-two paths (Golden Dawn numbering 11-32 on
Kircher's tree, with the Jewish trees' differences as leads)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "briefs")

SEPHIROTH = [
 ("kether", "Kether", "the first Sephira, the Crown", "Ehyeh; Metatron; the Chayot ha-Kodesh; the Primum Mobile (Rashith ha-Gilgalim); the Ancient of Days, the Vast Countenance (Arikh Anpin), the point in the circle, the three veils above it (Ain, Ain Soph, Ain Soph Aur), the crown of Isaiah 28:5; the Yetziratic 'Admirable or Hidden Intelligence'; Thaumiel the twin-headed Qliphah; the grade Ipsissimus; Fortune's chapter; Luria's Adam Kadmon and the tzimtzum"),
 ("chokmah", "Chokmah", "the second Sephira, Wisdom", "Yah / YHVH; Raziel; the Auphanim; the Zodiac (Mazloth); the Father (Abba), the Supernal Father; Proverbs 3:19 and 8; the Yetziratic 'Illuminating Intelligence'; Ghagiel; the grade Magus; the line, the phallus, the wand; Fortune's chapter"),
 ("binah", "Binah", "the third Sephira, Understanding", "YHVH Elohim; Tzaphkiel; the Aralim; Saturn (Shabbathai); the Mother (Imma), the Great Sea, the dark sterile mother and the bright fertile mother, the Supernal Mother, the Ama/Aima; the Yetziratic 'Sanctifying Intelligence'; Satariel; the grade Magister Templi and the City of the Pyramids; the cup, the yoni, the triangle; Fortune's chapter"),
 ("daat", "Da'at", "Knowledge, the hidden or eleventh Sephira on the Abyss", "the non-Sephira of the Zohar and Luria (the Sephira that is not counted, the child of Chokmah and Binah, the throat of Adam Kadmon); its absence from the Yetzirah's ten; Cordovero's and Luria's treatment; its Hasidic centrality (Chabad = Chokmah-Binah-Da'at, the Tanya); the Golden Dawn's Abyss, Choronzon and Crowley's crossing (Liber 418, the tenth Aethyr, Bou-Saada 1909); the invisible Sephira in Fortune; Kenneth Grant's Da'at as the gate to the Nightside; the 'Sephira of Knowledge' in Thelemic grades (Babe of the Abyss)"),
 ("chesed", "Chesed", "the fourth Sephira, Mercy, also Gedulah", "El; Tzadkiel; the Chashmalim; Jupiter (Tzedek); Abraham as the man of Chesed; 1 Chronicles 29:11 'the greatness'; the Yetziratic 'Cohesive or Receptacular Intelligence'; Gha'agsheblah; the grade Adeptus Exemptus; the sceptre, the orb, the tetrahedron; the day of the Omer; Fortune's chapter"),
 ("geburah", "Geburah", "the fifth Sephira, Severity, also Din and Pachad", "Elohim Gibor; Kamael; the Seraphim; Mars (Madim); Isaac; the left hand of God, the source of evil in the Zohar (the Sitra Achra born of unbalanced Din), the red pillar; the Yetziratic 'Radical Intelligence'; Golachab; the grade Adeptus Major; the sword, the spear, the scourge, the pentagon; Fortune's chapter"),
 ("tiphareth", "Tiphareth", "the sixth Sephira, Beauty", "YHVH Eloah va-Da'at; Raphael (or Michael in some lists); the Malachim; the Sun (Shemesh); Jacob, the Son (Zeir Anpin, the Lesser Countenance), the six extremities; the Christ-centre of the Christian Cabala and of the Golden Dawn (the Adeptus Minor, the Rosy Cross, the Vault); the Yetziratic 'Mediating Intelligence'; Thagirion; the Knowledge and Conversation of the Holy Guardian Angel; the lamen, the rose cross, the cube, the truncated pyramid; Fortune's chapter"),
 ("netzach", "Netzach", "the seventh Sephira, Victory, Eternity", "YHVH Tzabaoth; Haniel; the Elohim; Venus (Nogah); Moses (or Aaron); 1 Chronicles 29:11 'the victory'; the Yetziratic 'Occult Intelligence'; A'arab Zaraq the Ravens of Dispersion; the grade Philosophus; the lamp, the girdle, the rose; Fortune's chapter; the emotions and the arts"),
 ("hod", "Hod", "the eighth Sephira, Splendour, Glory", "Elohim Tzabaoth; Michael (or Raphael); the Beni Elohim; Mercury (Kokab); Aaron (or Moses); the Yetziratic 'Absolute or Perfect Intelligence'; Samael the Qliphah; the grade Practicus; the names and versicles, the apron; Fortune's chapter; the intellect and magic"),
 ("yesod", "Yesod", "the ninth Sephira, the Foundation", "Shaddai El Chai; Gabriel; the Kerubim; the Moon (Levanah); Joseph the Righteous (Tzaddik yesod olam, Proverbs 10:25); the phallus of Adam Kadmon and the covenant; the astral light, the Treasure House of Images; the Yetziratic 'Pure Intelligence'; Gamaliel the Obscene Ones and Lilith; the grade Theoricus; the perfumes and sandals; Fortune's chapter; the 'machinery of the universe'"),
 ("malkuth", "Malkuth", "the tenth Sephira, the Kingdom", "Adonai ha-Aretz, Adonai Melekh; Sandalphon; the Ashim (Ishim); the Earth, the sphere of the elements (Cholem Yesodoth); the Shekhinah, the Bride, the Daughter, the Queen, the Rachel of the partzufim, the Sabbath; the Gate, the Gate of Death, the Inferior Mother; the Yetziratic 'Resplendent Intelligence'; Lilith / Nehemoth the Qliphah; the grade Zelator (and the Neophyte's Malkuth); the four colours (citrine, olive, russet, black), the altar of the double cube, the equal-armed cross; Fortune's chapter; the exile of the Shekhinah"),
]

# Golden Dawn paths on Kircher's tree: number, letter, name, value, meaning, class, joins, attribution, trump, Yetziratic intelligence
PATHS = [
 (11, "Aleph", "ox", 1, "mother letter", "Kether-Chokmah", "Air", "the Fool", "Scintillating Intelligence"),
 (12, "Beth", "house", 2, "double letter", "Kether-Binah", "Mercury", "the Magician", "Intelligence of Transparency"),
 (13, "Gimel", "camel", 3, "double letter", "Kether-Tiphareth", "the Moon", "the High Priestess", "Uniting Intelligence"),
 (14, "Daleth", "door", 4, "double letter", "Chokmah-Binah", "Venus", "the Empress", "Illuminating Intelligence"),
 (15, "Heh", "window", 5, "simple letter", "Chokmah-Tiphareth", "Aries", "the Emperor (the Star in Crowley's swap)", "Constituting Intelligence"),
 (16, "Vav", "nail", 6, "simple letter", "Chokmah-Chesed", "Taurus", "the Hierophant", "Triumphal or Eternal Intelligence"),
 (17, "Zayin", "sword", 7, "simple letter", "Binah-Tiphareth", "Gemini", "the Lovers", "Disposing Intelligence"),
 (18, "Cheth", "fence", 8, "simple letter", "Binah-Geburah", "Cancer", "the Chariot", "Intelligence of the House of Influence"),
 (19, "Teth", "serpent", 9, "simple letter", "Chesed-Geburah", "Leo", "Strength (Lust)", "Intelligence of the Secret of all Spiritual Activities"),
 (20, "Yod", "hand", 10, "simple letter", "Chesed-Tiphareth", "Virgo", "the Hermit", "Intelligence of Will"),
 (21, "Kaph", "palm", 20, "double letter", "Chesed-Netzach", "Jupiter", "the Wheel of Fortune", "Intelligence of Conciliation"),
 (22, "Lamed", "ox-goad", 30, "simple letter", "Geburah-Tiphareth", "Libra", "Justice (Adjustment)", "Faithful Intelligence"),
 (23, "Mem", "water", 40, "mother letter", "Geburah-Hod", "Water", "the Hanged Man", "Stable Intelligence"),
 (24, "Nun", "fish", 50, "simple letter", "Tiphareth-Netzach", "Scorpio", "Death", "Imaginative Intelligence"),
 (25, "Samekh", "prop", 60, "simple letter", "Tiphareth-Yesod", "Sagittarius", "Temperance (Art)", "Intelligence of Probation"),
 (26, "Ayin", "eye", 70, "simple letter", "Tiphareth-Hod", "Capricorn", "the Devil", "Renovating Intelligence"),
 (27, "Peh", "mouth", 80, "double letter", "Netzach-Hod", "Mars", "the Tower", "Exciting Intelligence"),
 (28, "Tzaddi", "fish-hook", 90, "simple letter", "Netzach-Yesod", "Aquarius", "the Star (the Emperor in Crowley's swap)", "Natural Intelligence"),
 (29, "Qoph", "back of the head", 100, "simple letter", "Netzach-Malkuth", "Pisces", "the Moon", "Corporeal Intelligence"),
 (30, "Resh", "head", 200, "double letter", "Hod-Yesod", "the Sun", "the Sun", "Collecting Intelligence"),
 (31, "Shin", "tooth", 300, "mother letter", "Hod-Malkuth", "Fire (and Spirit)", "Judgement (the Aeon)", "Perpetual Intelligence"),
 (32, "Tav", "cross, mark", 400, "double letter", "Yesod-Malkuth", "Saturn (and Earth)", "the World (the Universe)", "Administrative Intelligence"),
]

SIGNS = {}
SIGNS["00_the_tree_of_life"] = ("The Tree of Life",
    "the whole diagram, Etz Chaim, as a system: this dossier treats the Tree entire, and the Sephiroth and paths have their own dossiers",
    "the 32 paths of the Sefer Yetzirah 1:1 and the ten Sephiroth belimah; the earliest tree diagrams (the fourteenth-century manuscripts, the Portae Lucis title page of 1516, Cordovero's, Luria's, the Gra's arrangement, Kircher's plate of 1652 and its adoption by the Golden Dawn); the three pillars (Mercy, Severity, Mildness/Equilibrium); the three triads and the pendant; the four worlds (Atziluth, Briah, Yetzirah, Assiah) and the four trees in one (Jacob's Ladder); the three veils of negative existence; the Abyss and Da'at; the lightning flash and the serpent of wisdom; the partzufim; the tzimtzum, the breaking of the vessels and tikkun; the Tree in the body (Adam Kadmon) and in the soul (nefesh, ruach, neshamah, chayah, yechidah); the Qliphoth as the inverted tree and the Sitra Achra; the colour scales; the Tree as a filing cabinet in Fortune, as the map of initiation in the Golden Dawn and A∴A∴, as Crowley's 777; the tarot on the Tree; the tribes on the twelve simple letters; the Goetic quinances on the zodiacal paths; the Tree in art (Kircher, the Golden Dawn diagrams, Grant, Lyons), in literature and in the modern imagination; the scholarship of Scholem, Idel, Wolfson, Hayman, Dan, and the Christian Cabala from Pico to Rosenroth")
for slug, name, status, pointers in SEPHIROTH:
    n = SEPHIROTH.index((slug, name, status, pointers)) + 1
    SIGNS[f"{n:02d}_{slug}"] = (name, status, pointers)
for num, letter, meaning, value, cls, joins, attr, trump, intel in PATHS:
    slug = f"{num}_path_{letter.lower()}"
    SIGNS[slug] = (f"The Path of {letter}",
        f"path {num} of the 32 on Kircher's tree, the letter {letter} ({meaning}, value {value}, a {cls}), joining {joins}; Golden Dawn attribution {attr}, tarot trump {trump}; the Yetziratic '{intel}'",
        f"the letter's form and history from proto-Sinaitic to the square script; its status as {cls} in the Sefer Yetzirah with the attribution ({attr}) and the variants between the Saadia, Gra and Ari recensions; the Yetziratic text of path {num} in Westcott's translation with the Hebrew; what the letter joins on the Ari and Gra trees versus Kircher's; the trump {trump} and the Golden Dawn's reasoning (and Crowley's where he differs); the four colour scales; the Nightside tunnel of this path in Grant's Nightside of Eden with its demon; the letter's Talmudic and Zoharic lore (the Otiyot de-Rabbi Akiva, the letters petitioning to begin the Torah); the tribe and month if a simple letter, the planet and the pair of opposites if a double, the element if a mother; the letter in gematria and in the divine names; pathworking accounts")

ORDER = list(SIGNS.keys())

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for slug, (name, status, pointers) in SIGNS.items():
        text = f"""# {name}: research brief

Tree of Life research, Anthony 2026-09-14, separate from the atlas. Appended to
PROMPT_TEMPLATE_TREE.md by atlas_tools/codex_dossier_set.py.

---

ELEMENT. {name}: {status}. Give at the top the Hebrew name, the number or letter, the position on
the Tree, the divine name, archangel, angelic order and planet (for a Sephira) or the letter class,
attribution and trump (for a path), and the Qliphah or tunnel.

THREADS TO PULL, each to be verified against the sources and dated: {pointers}.

STANCE. The Jewish tradition and the Hermetic-occult tradition side by side, each in full, never
collapsed into the other. Every claim labeled: documented text, scholarly reconstruction,
kabbalistic tradition, Hermetic-occult attribution, disputed, modern invention. Where a thread above
carries a question mark or 'or', treat it as a lead to check and report what you found. Quote the
primary texts in their own words with edition and page. Absence of evidence is a finding.
"""
        open(os.path.join(OUT, f"{slug}.brief.md"), "w").write(text)
    print("wrote", len(SIGNS), "briefs")
