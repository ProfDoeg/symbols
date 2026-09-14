#!/usr/bin/env python3
"""Write one brief per tarot card into working/tarot/briefs/: 22 trumps in Marseille order,
then the 56 minors by suit, ace to ten and the four courts. The minors' Golden Dawn decan
titles and attributions are given as leads for the researcher to verify against Book T."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "briefs")

MAJORS = [
 ("00_the_fool", "The Fool", "trump 0 (unnumbered in Marseille), Il Matto, Le Mat", "Aleph, Air, the Golden Dawn's path 11; the Visconti-Sforza beggar with feathers in his hair; the Marseille wanderer with the animal at his heels; Waite's youth at the cliff with the dog and the white rose; Crowley's green man; the Fool's role in play (the Excuse, l'Excuse); Crowley on the Fool as the Holy Ghost, the Green Man, the April fool; the Fool in Calvino and in Eliot? (no: check); the 'zero' question and where Lévi and Papus put him (between XX and XXI)"),
 ("01_the_magician", "The Magician", "trump I, Il Bagatto/Bagatello, Le Bateleur", "Beth, Mercury; the mountebank at his table in the fifteenth century (a conjurer, a craftsman?); the Marseille Bateleur's hat as a lemniscate; Waite's Magus with the four suit-signs and 'as above so below'; Crowley's three Magi paintings; Lévi's Magus with the wand; the Mercury/Hermes reading; the cups-and-balls game"),
 ("02_the_high_priestess", "The High Priestess", "trump II, La Papessa, La Papesse, Juno in Besançon", "Gimel, the Moon; the Visconti-Sforza Papess as Sister Manfreda Visconti of the Guglielmites (Moakley's thesis) and its critics; the Pope Joan legend; Juno with the peacock in the Besançon pattern; Waite's priestess between Boaz and Jachin with the Torah and the pomegranate veil; Crowley's Isis with the camel; Lévi's Isis"),
 ("03_the_empress", "The Empress", "trump III, L'Imperatrice", "Daleth, Venus; the Visconti empress with the eagle shield; the Marseille sceptre and shield; Waite's Venus in the wheat field; Crowley's Empress with the pelican and the shield of the double eagle; the alchemical Salt reading"),
 ("04_the_emperor", "The Emperor", "trump IV, L'Imperatore, L'Empereur", "Heh (or Tzaddi in Crowley's swap), Aries; the Visconti emperor, Sigismund?; the Marseille profile emperor with the eagle shield and crossed legs; Waite's rams; Crowley's Emperor with the Lamb and the Bees of Napoleon; the Tzaddi/Heh question in full (Liber AL I:57, Crowley's Book of Thoth)"),
 ("05_the_hierophant", "The Hierophant", "trump V, Il Papa, Le Pape, Jupiter in Besançon, Bacchus in some Belgian decks", "Vav, Taurus; the Pope with two acolytes in the fifteenth century; the renamings in Protestant and Josephine lands; Waite's Hierophant with the crossed keys; Crowley's Hierophant with the bull, the elephants and the Scarlet Woman; Lévi's Grand Hierophant; the Taurus attribution"),
 ("06_the_lovers", "The Lovers", "trump VI, L'Amore, L'Amoureux", "Zayin, Gemini; the fifteenth-century blindfolded Cupid over a couple (a wedding card?); the Marseille man between two women (the Choice of Hercules, mother and bride) with Cupid above; Waite's Eden with the angel Raphael; Crowley's alchemical wedding with the Hermit officiating, Cain and Abel, the Orphic egg; Lévi's Vice and Virtue"),
 ("07_the_chariot", "The Chariot", "trump VII, Il Carro, Le Chariot", "Cheth, Cancer; the Visconti-Sforza lady in a chariot drawn by winged horses; the Marseille prince under a canopy with two horses and the SM shoulder-masks; Waite's sphinxes and the star canopy; Crowley's charioteer in amber armour with the four sphinxes and the Grail; Petrarch's Trionfi as a source for the whole series"),
 ("08_strength", "Strength", "trump VIII in Waite, XI in Marseille; La Fortezza, La Force, Lust in Crowley", "Teth, Leo; the Visconti Hercules with the club and the lion; the Marseille woman opening the lion's jaws with the lemniscate hat; the Golden Dawn's swap of Strength and Justice and why; Waite's VIII; Crowley's Lust: the Scarlet Woman on the Beast with the Grail; the cardinal virtue Fortitude"),
 ("09_the_hermit", "The Hermit", "trump IX, Il Gobbo/Il Vecchio/Il Tempo, L'Hermite", "Yod, Virgo; the fifteenth-century old man with an hourglass (Time) becoming a lantern (the hermit); the Marseille Hermite with lantern and staff; Waite's mountain hermit with the six-pointed star in the lantern; Crowley's Hermit with Cerberus, the serpent and the Orphic egg; Diogenes; Saturn/Chronos; the Virgo attribution"),
 ("10_the_wheel_of_fortune", "The Wheel of Fortune", "trump X, La Ruota, La Roue de Fortune", "Kaph, Jupiter; the medieval Rota Fortunae with regnabo-regno-regnavi-sum sine regno; the Visconti wheel with the blindfolded Fortuna; the Marseille three animals on the wheel with a crank; Waite's wheel with TARO/ROTA and the four living creatures, the sphinx, Typhon, Anubis; Crowley's wheel with Sphinx, Hermanubis and Typhon and the ten spokes; Boethius"),
 ("11_justice", "Justice", "trump XI in Waite, VIII in Marseille; La Giustizia, La Justice, Adjustment in Crowley", "Lamed, Libra; the fifteenth-century Justice with sword and scales (and a knight above in Visconti-Sforza); the cardinal virtue; the Golden Dawn swap; Waite's XI between pillars; Crowley's Adjustment, the dancer with the sword and the balances, Maat, the Alpha and Omega"),
 ("12_the_hanged_man", "The Hanged Man", "trump XII, L'Appeso/Il Traditore, Le Pendu", "Mem, Water; the pittura infamante (shame paintings of traitors hung by one foot) as the source; the Visconti-Sforza hanged man with money bags in some readings; the Marseille figure with the crossed leg; Waite's halo and the T-cross; Crowley's Hanged Man nailed on the ankh over the water, the serpent; Judas readings; Odin readings; the reversed-card printing error theory"),
 ("13_death", "Death", "trump XIII, La Morte, unnamed in Marseille (L'Arcane sans nom)", "Nun, Scorpio; the skeleton with the scythe in the fifteenth century, on horseback in some; the Marseille skeleton reaping heads and hands with the card unnamed; Waite's black knight with the white rose banner, the bishop, the rising sun; Crowley's dancing skeleton with the scythe, the fish, the scorpion, the eagle; the danse macabre; superstitions about the card"),
 ("14_temperance", "Temperance", "trump XIV, La Temperanza, Tempérance, Art in Crowley", "Samekh, Sagittarius; the cardinal virtue pouring between two vessels; the Visconti angel? and the Marseille winged woman; Waite's angel with the sun on the brow, one foot in the water, the iris; Crowley's Art: the alchemical androgyne, VITRIOL, the lion and eagle; the alchemical reading"),
 ("15_the_devil", "The Devil", "trump XV, Il Diavolo, Le Diable", "Ayin, Capricorn; no fifteenth-century Devil survives (the missing Visconti cards); the Marseille devil on a pedestal with two chained imps; Lévi's Baphomet of Mendes (1856) and its adoption by Waite (1909) with the inverted pentagram and the chained couple; Crowley's Devil as the goat of Mendes with the third eye, the testicles as the root, Pan; the Capricorn attribution; the Templar Baphomet"),
 ("16_the_tower", "The Tower", "trump XVI, La Torre/La Casa del Diavolo/La Saetta, La Maison Dieu", "Peh, Mars; no fifteenth-century Tower survives except the Sforza Castle sheet?; the Marseille Maison Dieu with the crown blown off and two falling figures; the Tower of Babel, the house of God (hospital?) readings, the lightning; Waite's tower with 22 Yods; Crowley's Tower with the eye of Shiva, the dove and the serpent, the mouth of Dis; the Mars attribution"),
 ("17_the_star", "The Star", "trump XVII, La Stella, L'Étoile", "Tzaddi (Heh in Crowley's swap), Aquarius; the Visconti-Sforza woman holding a star; the Marseille naked woman pouring two vessels under eight stars with the bird in the tree; Waite's ibis; Crowley's Nuit with the seven-pointed star of Babalon; the 'Tzaddi is not the Star' verse (Liber AL I:57) and the Emperor exchange"),
 ("18_the_moon", "The Moon", "trump XVIII, La Luna, La Lune", "Qoph, Pisces; the Visconti-Sforza woman with the crescent (Diana?); the Marseille two towers, two dogs, the crayfish in the pool, the drops; Waite's path between the towers; Crowley's Anubis twins and the beetle Khephra carrying the sun; the Pisces attribution; the 'dark night' readings"),
 ("19_the_sun", "The Sun", "trump XIX, Il Sole, Le Soleil", "Resh, the Sun; the Visconti-Sforza putto with the sun's head on a cloud; the Marseille two children (twins, Gemini? the Dioscuri?) under the sun with the wall; Waite's child on the horse with the banner and the sunflowers; Crowley's Sun with the two children on the green mound and the twelve signs, the rose cross; the Gemini reading of the Marseille twins"),
 ("20_judgement", "Judgement", "trump XX, Il Giudizio/L'Angelo, Le Jugement, The Aeon in Crowley", "Shin, Fire (Spirit); the angel with the trumpet and the rising dead in the fifteenth century; the Marseille three figures; Waite's cross banner and the sea; Crowley's Aeon: Nuit, Hadit and Ra-Hoor-Khuit, the Aeon of Horus (1904); the Last Judgement iconography; the placement above the World in some orders"),
 ("21_the_world", "The World", "trump XXI, Il Mondo, Le Monde, The Universe in Crowley", "Tav, Saturn (and Earth); the Visconti-Sforza putti holding up a globe with a city (the New Jerusalem?); the Marseille dancer in the mandorla with the four living creatures; Waite's dancer with two wands; Crowley's Universe with the serpent, the eye of Shiva, the four kerubim and the house of matter; the anima mundi; the Tetramorph"),
]

SUITS = [
 ("wands", "Wands", "Bastoni, Bâtons; Fire; Golden Dawn Wands, Thoth Wands; the club/baton of the Italian and Spanish packs; Yod of the Tetragrammaton"),
 ("cups", "Cups", "Coppe, Coupes; Water; the Grail readings; Heh"),
 ("swords", "Swords", "Spade, Épées; Air; the curved scimitars of the Marseille pattern; Vav"),
 ("pentacles", "Pentacles", "Denari, Deniers, Coins; Earth; Disks in Crowley; the pentacle introduced by the Golden Dawn and Waite; final Heh"),
]

# Golden Dawn Book T decan titles and planet-in-sign for the pips two to ten (leads to verify),
# with the Thoth title where Crowley renamed.
PIPS = {
 "wands": {2: ("Dominion", "Mars in Aries"), 3: ("Established Strength; Thoth: Virtue", "Sun in Aries"),
           4: ("Perfected Work; Thoth: Completion", "Venus in Aries"), 5: ("Strife", "Saturn in Leo"),
           6: ("Victory", "Jupiter in Leo"), 7: ("Valour", "Mars in Leo"),
           8: ("Swiftness", "Mercury in Sagittarius"), 9: ("Great Strength; Thoth: Strength", "Moon in Sagittarius"),
           10: ("Oppression", "Saturn in Sagittarius")},
 "cups": {2: ("Love", "Venus in Cancer"), 3: ("Abundance", "Mercury in Cancer"),
          4: ("Blended Pleasure; Thoth: Luxury", "Moon in Cancer"), 5: ("Loss in Pleasure; Thoth: Disappointment", "Mars in Scorpio"),
          6: ("Pleasure", "Sun in Scorpio"), 7: ("Illusionary Success; Thoth: Debauch", "Venus in Scorpio"),
          8: ("Abandoned Success; Thoth: Indolence", "Saturn in Pisces"), 9: ("Material Happiness; Thoth: Happiness", "Jupiter in Pisces"),
          10: ("Perfected Success; Thoth: Satiety", "Mars in Pisces")},
 "swords": {2: ("Peace Restored; Thoth: Peace", "Moon in Libra"), 3: ("Sorrow", "Saturn in Libra"),
            4: ("Rest from Strife; Thoth: Truce", "Jupiter in Libra"), 5: ("Defeat", "Venus in Aquarius"),
            6: ("Earned Success; Thoth: Science", "Mercury in Aquarius"), 7: ("Unstable Effort; Thoth: Futility", "Moon in Aquarius"),
            8: ("Shortened Force; Thoth: Interference", "Jupiter in Gemini"), 9: ("Despair and Cruelty; Thoth: Cruelty", "Mars in Gemini"),
            10: ("Ruin", "Sun in Gemini")},
 "pentacles": {2: ("Harmonious Change; Thoth: Change", "Jupiter in Capricorn"), 3: ("Material Works; Thoth: Works", "Mars in Capricorn"),
               4: ("Earthly Power; Thoth: Power", "Sun in Capricorn"), 5: ("Material Trouble; Thoth: Worry", "Mercury in Taurus"),
               6: ("Material Success; Thoth: Success", "Moon in Taurus"), 7: ("Success Unfulfilled; Thoth: Failure", "Saturn in Taurus"),
               8: ("Prudence", "Sun in Virgo"), 9: ("Material Gain; Thoth: Gain", "Venus in Virgo"),
               10: ("Wealth", "Mercury in Virgo")},
}
NUMS = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
COURTS = [
 ("page", "Page", "Fante/Valet; Golden Dawn and Thoth Princess; the Earth (final Heh) of the suit; the Marseille valet; Waite's page; the throne of the Aces; the four quadrants of the world in Book T"),
 ("knight", "Knight", "Cavallo/Cavalier; Golden Dawn King (on horseback), Thoth Knight; the Fire (Yod) of the suit; the zodiacal span 20° of one sign to 20° of the next in Book T (verify which); Waite's knight; the confusion of Waite's Knight with the Golden Dawn's Prince"),
 ("queen", "Queen", "Regina/Reine; the Water (Heh) of the suit; the zodiacal span in Book T; the queens absent from the Italian and Spanish regular packs and present in tarot from the start"),
 ("king", "King", "Re/Roi; Golden Dawn and Thoth Prince (in a chariot); the Air (Vav) of the suit; the zodiacal span in Book T; the seated Marseille king; Waite's king"),
]

SUIT_POINTERS = {
 "wands": "the Mamluk polo-stick suit (jawkān) becoming the Italian bastoni and the French bâtons; the clubs of the Spanish pack; the suit's element (Fire) and Tetragrammaton letter (Yod) in the Golden Dawn; Book T's ten decans of the fire signs across the pips; the Waite-Smith wands as living branches with leaves; Crowley's wands as different ritual weapons per card (the phoenix wand, the lotus wand, the Ace as the flaming club); the suit in tarocchi play and its rank order; the Grail-legend reading of the suit as the lance; the suit's court as a family; the suit's Marseille pattern (crossed batons with the floral ornament); the four suits as the four estates (peasantry? or merchants?) in Court de Gébelin and later; the four suits as the four elements from Lévi on; Etteilla's meanings for the suit; the suit's colour and season in the various systems",
 "cups": "the Mamluk cups (tūmān) and the Italian coppe, the French coupes, the hearts of the French pack; Water and Heh; Book T's decans of the water signs; the Waite-Smith cups as scenes of feeling; Crowley's cups as lotus-cups with the Ace as the Holy Grail; the Grail reading; the Ace of Cups as a fountain or a church in the early decks; the Marseille cups; the suit as the clergy in Gébelin's estates; Etteilla; colour and season",
 "swords": "the Mamluk scimitars (suyūf) and the Italian spade, the French épées, the spades of the French pack and the etymology of 'spade'; Air and Vav; Book T's decans of the air signs; the Waite-Smith swords as the suit of grief; Crowley's swords as the suit of the mind, with the Ace as the sword of the Magus; the Marseille curved swords in an almond; the suit as the nobility; Etteilla; colour and season",
 "pentacles": "the Mamluk coins (darāhim) and the Italian denari, the French deniers, the diamonds of the French pack; the pentacle (pentagram-on-a-disk) introduced by the Golden Dawn and Waite, Crowley's 'disks'; Earth and final Heh; Book T's decans of the earth signs; the Ace of Coins as the card-maker's signature card with name, city and tax stamp; the Waite-Smith pentacles as the suit of work and money; Crowley's disks with the Ace as the disk of the Aeon of Horus; the suit as the merchants; Etteilla; colour and season",
}

SIGNS = {}
for slug, name, ident, pointers in MAJORS:
    SIGNS[slug] = (name, f"{ident}; a trump of the tarot, Marseille numbering unless noted", pointers)
for si, (skey, sname, sdesc) in enumerate(SUITS):
    SIGNS[f"suit_{skey}"] = (f"The Suit of {sname}",
        f"not one card but the whole suit of {sname} ({sdesc}) as a set of fourteen: this dossier describes the suit as a whole, its history, its element and its logic, and the fourteen cards as a system; the individual cards have their own dossiers",
        SUIT_POINTERS[skey])
    for n in range(1, 11):
        slug = f"{30 + si * 14 + n - 1:02d}_{NUMS[n].lower()}_of_{skey}"
        name = f"{NUMS[n]} of {sname}"
        if n == 1:
            pointers = (f"the Ace as the Root of the Powers of {['Fire','Water','Air','Earth'][si]} in Book T; the suit itself: {sdesc}; "
                        f"the Sola Busca and Marseille aces (the ace of coins as the maker's card with the printer's name and tax stamp, the ace of cups as a fountain/church); "
                        f"Waite's hand from the cloud; Crowley's ace; the Mamluk ancestor of the suit; the Ace's rank in play (high in tarocchi trumps? no: check)")
        else:
            title, decan = PIPS[skey][n]
            pointers = (f"Golden Dawn Book T title '{title}' with the decan {decan} (verify against Book T and the Thoth deck); the Sola Busca pip (1491) as the source of Pamela Colman Smith's scene; "
                        f"the Marseille pip with its floral ornament; Waite's scene and its reading in the Pictorial Key; Crowley's geometric design with Harris; Etteilla's meanings; the suit: {sdesc}; "
                        f"the number's meaning on the Tree of Life (Sephira {n}); the card in tarocchi play")
        SIGNS[slug] = (name, f"pip card of the suit of {sname}", pointers)
    for ci, (ckey, cname, cdesc) in enumerate(COURTS):
        slug = f"{30 + si * 14 + 10 + ci:02d}_{ckey}_of_{skey}"
        name = f"{cname} of {sname}"
        pointers = (f"{cdesc}; the suit: {sdesc}; the Visconti-Sforza court figure (which family member, if any, per Moakley and Kaplan); the Marseille figure; Waite's figure and the Pictorial Key description; "
                    f"Crowley's figure and the Book of Thoth description; the Golden Dawn's sub-elemental attribution and its zodiacal decans; the court's rank and value in play; the Mamluk na'ib ancestor")
        SIGNS[slug] = (name, f"court card of the suit of {sname}", pointers)

ORDER = list(SIGNS.keys())


def out_path(slug):
    """where the dossier lives, relative to working/tarot: major/, or minor/<suit>/; a suit's own
    dossier is minor/<suit>/<suit>.md"""
    if slug.startswith("suit_"):
        s = slug[5:]
        return f"minor/{s}/{s}.md"
    if slug[:2].isdigit() and int(slug[:2]) < 30:
        return f"major/{slug}.dossier.md"
    s = slug.rsplit("_of_", 1)[1]
    return f"minor/{s}/{slug}.dossier.md"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for slug, (name, status, pointers) in SIGNS.items():
        text = f"""# {name}: research brief

Tarot research, Anthony 2026-09-14, separate from the atlas. Appended to
PROMPT_TEMPLATE_TAROT.md by atlas_tools/codex_dossier_tarot.py.

---

CARD. {name}: {status}. Give at the top the names across decks, the number, the earliest
surviving example, and the Golden Dawn attribution.

THREADS TO PULL, each to be verified against the sources and dated: {pointers}.

STANCE. Myth as fully as fact. Every claim labeled: documented fact, scholarly reconstruction,
tradition, esoteric attribution, disputed, legend, modern invention. Where a thread above carries
a question mark or '(verify)', treat it as a lead to check and report what you found. Quote the
occultists (Lévi, Papus, Waite, Crowley) in their own words with edition and page. Absence of
evidence is a finding: say what could not be traced.
"""
        open(os.path.join(OUT, f"{slug}.brief.md"), "w").write(text)
    print("wrote", len(SIGNS), "briefs")
