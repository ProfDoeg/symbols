#!/usr/bin/env python3
"""Write one brief per spirit of the Ars Goetia into working/goetia/briefs/, in the Goetia's
order of 72, each paired with the Shem HaMephorash angel of the same number (Rudd's scheme, a
lead for the researcher to verify)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "briefs")

# (name, rank, extra leads); the Goetia's order; ranks as in Mathers-Crowley 1904
SPIRITS = [
 ("Bael", "King", "the first spirit; Baal/Ba'al Hadad behind the name; three heads (cat, toad, man); invisibility; de Plancy's spider-legged portrait"),
 ("Agares", "Duke", "the old man on a crocodile with a hawk; languages and earthquakes; Agreas in Weyer"),
 ("Vassago", "Prince", "not in Weyer; the finder of lost things; his 'good nature'; added to the 72"),
 ("Samigina", "Marquis", "Gamigin/Gamygyn; the little horse; the souls of the drowned; liberal sciences"),
 ("Marbas", "President", "Barbas in Weyer; the great lion; diseases and their cure; mechanical arts; shape-changing"),
 ("Valefor", "Duke", "Valefar/Malaphar; the lion with an ass's head; familiar to thieves"),
 ("Amon", "Marquis", "Aamon; the wolf with a serpent's tail vomiting flame; Amun of Egypt behind the name (disputed); reconciles friends and foes"),
 ("Barbatos", "Duke", "the archer with four kings and their companies; the voices of birds and dogs; hidden treasures; the Latin barbatus"),
 ("Paimon", "King", "the crowned man on a dromedary with trumpets, most obedient to Lucifer; Paimon in Abramelin; the 2018 film Hereditary and the name's revival; the two kings Bebal and Abalam"),
 ("Buer", "President", "the Sagittarius-timed teacher of philosophy and herbs; de Plancy's lion-headed wheel of five goat legs; the meme afterlife"),
 ("Gusion", "Duke", "Gusoin/Gusayn; Xenophilus in Weyer; the discerner of past and future; honour and dignity"),
 ("Sitri", "Prince", "Bitru in Weyer; leopard's head, gryphon's wings; inflames love, makes women show themselves naked"),
 ("Beleth", "King", "Bileth/Byleth; the terrible king on a pale horse with trumpets, treated with a hazel wand and the triangle; Ham son of Noah as the first to call him (Weyer's note); love"),
 ("Leraje", "Marquis", "Leraie/Loray/Oray; the archer in green; putrefying arrow wounds; battles"),
 ("Eligos", "Duke", "Abigor in de Plancy; the goodly knight with lance, ensign and serpent; wars and the love of lords"),
 ("Zepar", "Duke", "the soldier in red; love of women; barrenness"),
 ("Botis", "Earl and President", "Otis; the viper then the man with teeth and horns and a sword; reconciles friends and foes"),
 ("Bathin", "Duke", "Bathym/Marthim; the strong man with a serpent's tail on a pale horse; herbs and stones; transports men across countries"),
 ("Sallos", "Duke", "Saleos/Zaleos; the gallant soldier on a crocodile with a ducal crown; love"),
 ("Purson", "King", "Curson/Pursan; the lion-faced man on a bear with a viper and trumpets; hidden things, treasures, past and future; good familiars"),
 ("Marax", "Earl and President", "Morax/Foraii/Narax; the bull with a man's face; astronomy, liberal sciences, herbs and stones"),
 ("Ipos", "Earl and Prince", "Ipes/Ayperos; the angel with a lion's head, goose feet and a hare's tail; wit and boldness"),
 ("Aim", "Duke", "Aym/Haborym; three heads (serpent, man with two stars, calf), on a viper, a firebrand; sets cities on fire; wit; private matters"),
 ("Naberius", "Marquis", "Cerberus/Naberus; the black crane with a hoarse voice; rhetoric and logic; lost dignities; the Cerberus conflation"),
 ("Glasya-Labolas", "President and Earl", "Caacrinolaas/Caassimolar; the dog with gryphon wings; manslaughter and bloodshed; invisibility; sciences"),
 ("Buné", "Duke", "Bime/Bune; the three-headed dragon (dog, gryphon, man); changes the places of the dead; riches and eloquence; the 'demons upon sepulchres'"),
 ("Ronové", "Marquis and Earl", "Ronwe/Roneve; the monster; rhetoric and languages; good servants"),
 ("Berith", "Duke", "Beal/Bofry/Bolfry; the soldier in red on a red horse with a golden crown; turns metals into gold; the liar; the Ba'al Berith of Shechem behind the name; the alchemists' Berith"),
 ("Astaroth", "Duke", "Astarte/Ashtoreth behind the name; the hurtful angel on an infernal dragon with a viper, the stinking breath and the magic ring; all secrets past, present and future; how the spirits fell; de Plancy's naked rider; Astaroth in Marlowe's Faustus? and in the Grand Grimoire"),
 ("Forneus", "Marquis", "the sea monster; rhetoric, languages, a good name; loved by foes"),
 ("Foras", "President", "Forcas; the strong man; herbs and stones, logic and ethics, invisibility, long life, eloquence; lost things and treasures"),
 ("Asmoday", "King", "Asmodeus/Ashmedai/Sydonay; the three heads (bull, man, ram), serpent's tail, goose feet, on a dragon with lance and banner; the ring of virtues; geometry and handicrafts; invincibility; treasures; the Asmodeus of Tobit and the Talmud (Solomon and the shamir); Le Diable boiteux; Weyer's note on his 'unlawful' seat"),
 ("Gäap", "President and Prince", "Tap/Goap; the guide of the four kings in the manner of Amaymon; philosophy and liberal sciences; love and hatred; transports men; the 'Noah' note in Weyer (Cham); the Salomon's 'Gaap' with Beleth"),
 ("Furfur", "Earl", "the hart with a fiery tail; the liar unless in the triangle; love between man and wife; lightning and thunder"),
 ("Marchosias", "Marquis", "the she-wolf with gryphon's wings and a serpent's tail, vomiting fire; the strong fighter; hopes to return to the Seventh Throne after 1,200 years (Weyer's note); of the Order of Dominations"),
 ("Stolas", "Prince", "Stolos/Solas; the raven, then a man; astronomy, herbs and precious stones; the owl of de Plancy and the Helluva Boss character"),
 ("Phenex", "Marquis", "Pheynix/Phoenix; the phoenix with a child's voice; sweet singing; the poet; hopes to return to the Seventh Throne after 1,200 years"),
 ("Halphas", "Earl", "Malthus/Malthas; the stock-dove with a hoarse voice; builds towers and furnishes them with ammunition; sends men to war"),
 ("Malphas", "President", "the crow, then a man with a hoarse voice; builds houses and high towers; the enemies' thoughts; deceives with sacrifice"),
 ("Räum", "Earl", "Raum/Raym; the crow, then a man; steals treasure from kings' houses; destroys cities and dignities; love"),
 ("Focalor", "Duke", "Forcalor/Furcalor; the man with gryphon wings; drowns men, overthrows warships; hopes to return to the Seventh Throne after 1,000 years"),
 ("Vepar", "Duke", "Separ; the mermaid; guides waters and ships laden with arms; makes the sea rough; kills by putrefying wounds in three days"),
 ("Sabnock", "Marquis", "Sabnach/Savnok; the armed soldier with a lion's head on a pale horse; builds castles and towers; wounds and worms; good familiars"),
 ("Shax", "Marquis", "Chax/Scox; the stock-dove with a hoarse voice; takes away sight, hearing and understanding; steals money; must be commanded into the triangle for truth"),
 ("Viné", "King and Earl", "Vine; the lion on a black horse with a viper; discovers hidden things, witches and wizards; builds towers, overthrows walls, makes waters rough"),
 ("Bifrons", "Earl", "Bifrous/Bifrovs; the monster then a man; astrology, geometry, herbs, stones and woods; changes dead bodies and lights candles on graves; the two-faced Janus behind the name"),
 ("Uvall", "Duke", "Vual/Voval; the mighty dromedary who speaks Egyptian; love of women; friendship of foes; past, present and future"),
 ("Haagenti", "President", "Hagenti; the bull with gryphon wings; makes men wise; turns metals to gold, water to wine"),
 ("Crocell", "Duke", "Crokel/Procell; the angel who speaks darkly of hidden things; geometry and liberal sciences; the sound of rushing waters; warms waters and baths; of the Order of Potestates"),
 ("Furcas", "Knight", "the only knight; the cruel old man with a long beard on a pale horse with a sharp weapon; philosophy, astrology, rhetoric, logic, chiromancy and pyromancy"),
 ("Balam", "King", "Balaam; three heads (bull, man, ram), serpent's tail, flaming eyes, on a bear with a goshawk; past, present and future; invisibility and wit; the Balaam of Numbers behind the name?"),
 ("Alloces", "Duke", "Allocer/Alocer; the soldier with a lion's red face and flaming eyes on a great horse; astronomy and liberal sciences; good familiars"),
 ("Camio", "President", "Caim/Caym; the thrush, then a man with a sword, answering in burning ashes; the understanding of birds, oxen, dogs and waters; disputes; the Cain behind the name?"),
 ("Murmur", "Duke and Earl", "Murmus; the warrior with a ducal crown on a gryphon, with trumpets; philosophy; constrains the souls of the dead to answer; of the Order of Thrones and Angels"),
 ("Orobas", "Prince", "the horse, then a man; past, present and future; dignities and prelacies; faithful, and defends from temptation"),
 ("Gremory", "Duke", "Gomory/Gamori; the beautiful woman with a duchess's crown on a camel; hidden treasures; the love of women old and young"),
 ("Ose", "President", "Oso/Voso; the leopard, then a man; liberal sciences; transforms men into any shape so that they believe it; the hour"),
 ("Amy", "President", "Avnas; the flaming fire, then a man; astrology and liberal sciences; good familiars; treasures kept by spirits; hopes to return to the Seventh Throne after 1,200 years"),
 ("Oriax", "Marquis", "Orias/Orobas confusion?; the lion with a serpent's tail on a horse, holding two hissing serpents; the virtues of the stars and planets; transformations; dignities"),
 ("Vapula", "Duke", "Naphula; the lion with gryphon wings; handicrafts, professions, philosophy and sciences"),
 ("Zagan", "King and President", "the bull with gryphon wings, then a man; makes men witty; turns wine into water, blood into wine, water into wine, metals into coin; makes fools wise"),
 ("Valac", "President", "Volac/Ualac/Valu; the child with angel's wings on a two-headed dragon; hidden treasures; serpents; the Valak of The Conjuring 2 and the name's revival"),
 ("Andras", "Marquis", "the angel with a raven's head on a black wolf with a sword; sows discord; kills the master and his fellows if not careful"),
 ("Flauros", "Duke", "Haures/Hauras/Havres; the leopard, then a man with flaming eyes; past, present and future; burns the exorcist's enemies; the fall of the angels; the triangle"),
 ("Andrealphus", "Marquis", "the noisy peacock, then a man; geometry, mensuration, astronomy; transforms men into birds"),
 ("Kimaris", "Marquis", "Cimeies/Cimejes/Cimeries; the valiant soldier on a black horse; rules the spirits of Africa; grammar, logic, rhetoric; lost things and treasures; Cimeries in Crowley's? and the Cimmerians"),
 ("Amdusias", "Duke", "Amduscias/Ambduscias; the unicorn, then a man; trumpets and musical instruments heard but not seen; trees bend; good familiars"),
 ("Belial", "King", "Beliya'al of the Hebrew Bible and Qumran; the two beautiful angels in a chariot of fire; created next after Lucifer; dignities, favours of friends and foes, familiars; demands sacrifices; Belial in Milton, in the Testament of Solomon, in the Dead Sea Scrolls; the Ars Goetia's note that Solomon shut him in a vessel found by the Babylonians"),
 ("Decarabia", "Marquis", "Carabia; the star in a pentacle, then a man; the virtues of birds and stones; birds as familiars"),
 ("Seere", "Prince", "Sear/Seir; the beautiful man on a winged horse; brings things to pass in an instant, carries anything anywhere; thefts and hidden treasures; of a good nature; not in Weyer"),
 ("Dantalion", "Duke", "the man with many faces of men and women, holding a book; arts and sciences; the thoughts of all; changes minds; love; shows the likeness of anyone; not in Weyer"),
 ("Andromalius", "Earl", "the man holding a great serpent; brings back thieves and stolen goods; discovers wickedness, hidden treasures; punishes thieves; not in Weyer"),
]

ANGELS = ["Vehuiah", "Jeliel", "Sitael", "Elemiah", "Mahasiah", "Lelahel", "Achaiah", "Cahetel", "Haziel",
          "Aladiah", "Lauviah", "Hahaiah", "Iezalel", "Mebahel", "Hariel", "Hakamiah", "Lauviah (Leuviah)", "Caliel",
          "Leuviah", "Pahaliah", "Nelchael", "Yeiayel", "Melahel", "Haheuiah", "Nith-Haiah", "Haaiah", "Yerathel",
          "Seheiah", "Reiyel", "Omael", "Lecabel", "Vasariah", "Yehuiah", "Lehahiah", "Chavakiah", "Menadel",
          "Aniel", "Haamiah", "Rehael", "Ieiazel", "Hahahel", "Mikael", "Veuliah", "Yelahiah", "Sealiah", "Ariel",
          "Asaliah", "Mihael", "Vehuel", "Daniel", "Hahasiah", "Imamiah", "Nanael", "Nithael", "Mebahiah", "Poyel",
          "Nemamiah", "Yeialel", "Harahel", "Mitzrael", "Umabel", "Iah-hel", "Anauel", "Mehiel", "Damabiah",
          "Manakel", "Eyael", "Habuhiah", "Rochel", "Jabamiah", "Haiaiel", "Mumiah"]
assert len(SPIRITS) == 72 and len(ANGELS) == 72

SIGNS = {}
for i, (name, rank, extra) in enumerate(SPIRITS, start=1):
    slug = f"{i:02d}_{name.lower().replace('ä', 'a').replace('é', 'e').replace('-', '_').replace(' ', '_')}"
    SIGNS[slug] = (name, f"spirit {i} of 72 in the Ars Goetia, {rank}; paired in Rudd's scheme with the Shem HaMephorash angel {ANGELS[i-1]} (angel {i} of 72; verify the pairing and the angel's five degrees, psalm verse and meaning)",
                   f"{extra}; the metal and planet of the rank {rank}; the legions; the seal and its variants; Weyer's Latin and Scot's English verbatim; Crowley's 777 quinance and tarot pip for spirit {i}; de Plancy's portrait if any; the later fiction and game appearances, attested")

ORDER = list(SIGNS.keys())

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for slug, (name, status, pointers) in SIGNS.items():
        text = f"""# {name}: research brief

Goetia research, Anthony 2026-09-14, separate from the atlas. Appended to
PROMPT_TEMPLATE_GOETIA.md by atlas_tools/codex_dossier_set.py.

---

SPIRIT. {name}: {status}. Give at the top the name and variants, the number, the rank, the
legions, the seal in words, the angel, the quinance and the tarot pip.

THREADS TO PULL, each to be verified against the sources and dated: {pointers}.

STANCE. Legend as fully as fact. Every claim labeled: documented text, scholarly reconstruction,
tradition, esoteric correspondence, disputed, legend, modern invention. Where a thread above
carries a question mark, treat it as a lead to check and report what you found. Quote Weyer, Scot
and the Goetia in their own words with edition and page. Absence of evidence is a finding: if the
name has no pre-1577 attestation, say so.
"""
        open(os.path.join(OUT, f"{slug}.brief.md"), "w").write(text)
    print("wrote", len(SIGNS), "briefs")
