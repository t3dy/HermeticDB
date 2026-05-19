"""Write definition_short for concepts missing index card text."""
import sqlite3

DB_PATH = r"C:\Dev\EmeraldTablet\db\emerald_tablet.db"

shorts = {
    "alchemy": (
        "The art and philosophy of material and spiritual transformation, rooted in the belief that base "
        "substances can be purified and perfected through laboratory operations guided by cosmological "
        "principles. In the Hermetic tradition, alchemy operated on two levels simultaneously: the external "
        "transmutation of metals and the internal regeneration of the practitioner, whose soul was refined "
        "alongside the matter in the vessel."
    ),
    "anthropos": (
        "The primordial divine Human, a cosmic figure whose image is reflected in material creation in the "
        "Hermetic Poimandres. The Anthropos descends through the planetary spheres, taking on their qualities, "
        "and becomes the progenitor of earthly humanity. The concept grounds the Hermetic understanding that "
        "human beings carry a divine spark and are structurally related to the cosmos as microcosm to macrocosm."
    ),
    "deification": (
        "The process by which a human soul achieves union with or assimilation to the divine, attaining a "
        "god-like state through gnosis, purification, and ascent through the celestial spheres. In the Hermetic "
        "Corpus, deification (apotheosis or theosis) is the ultimate soteriological goal, accomplished not by "
        "ritual alone but by intellective transformation — the mind becoming identified with the divine Nous."
    ),
    "egypt": (
        "The geographical and cultural matrix of the Hermetic literary tradition. The Hermetic texts present "
        "their wisdom as Egyptian in origin, attributed to Hermes Trismegistus as a Hellenised Thoth. Modern "
        "scholarship locates the actual composition of the Philosophical Hermetica in Greco-Roman Egypt, likely "
        "Alexandria, where Egyptian priestly traditions, Platonism, and Stoic philosophy converged in the "
        "first to third centuries CE."
    ),
    "emanations": (
        "The process by which divine reality unfolds from a single primordial source into progressively "
        "differentiated levels of being. Derived from Neoplatonic metaphysics, emanation describes the "
        "overflow of the One into Nous, then Soul, then Matter, without diminishing the source. In Hermetic "
        "texts the Demiurge and the created world proceed from the Father-God through a similar emanative "
        "logic, making the cosmos an expression of divine excess rather than a deliberate act of creation."
    ),
    "god_making": (
        "The production of animate divine statues — material objects infused with the living presence of a "
        "deity through ritual procedures. Described in the Asclepius, god-making (theopoiia) represents the "
        "capacity of human craft to attract and house divine pneuma within sculptural form. Garth Fowden and "
        "Wouter Hanegraaff link this practice to Egyptian priestly tradition and to later theurgical statue "
        "animation in Iamblichus and the Chaldean Oracles."
    ),
    "ochema": (
        "The luminous subtle body or vehicle of the soul, conceived as the intermediary between the immaterial "
        "intellect and the dense physical body. In Neoplatonic and Hermetic thought, the ochema (vehicle) is "
        "the soul's chariot during its celestial descent and ascent, accumulating and shedding planetary "
        "qualities at each sphere. The concept is closely related to pneuma and to the Paracelsian notion "
        "of the astral body."
    ),
    "palingenesia": (
        "Rebirth or regeneration — the transformation of the soul into a new condition through initiation, "
        "gnosis, or ritual renewal. In the Hermetic Corpus, particularly Corpus Hermeticum XIII, palingenesia "
        "denotes a spiritual rebirth that occurs when the soul sheds the vices acquired during its descent "
        "through the planetary spheres and receives divine virtues in their place, emerging as a new being "
        "capable of ascending to God."
    ),
    "prophecy": (
        "Divinely inspired speech or vision through which hidden or future truths are made known to a human "
        "intermediary. In the Hermetic tradition, prophecy is associated with the activity of the divine Nous "
        "in the soul, which grants access to truths beyond ordinary sense perception. The Hermetic texts "
        "present their own revelations as prophetic in character, delivered by Hermes Trismegistus as an "
        "inspired sage who has received direct disclosure from the divine mind."
    ),
    "regeneration": (
        "The renewal or transformation of the soul from its degraded material condition to a purified, "
        "god-like state. Closely related to palingenesia, regeneration in the Hermetic Corpus (especially "
        "CH XIII) describes an inward event: the expulsion of the twelve vices associated with the zodiacal "
        "powers and their replacement by ten divine powers transmitted by Nous. The regenerated person "
        "becomes a son of God capable of true gnosis."
    ),
    "talismans": (
        "Material objects — typically inscribed stones, metals, or figurines — charged with astral power "
        "through ritual procedures performed at astrologically propitious moments. In the Hermetic-influenced "
        "traditions of astral magic, talismans serve as condensed receptors of planetary and decanic "
        "influences, operating through the principle of sympatheia. The Picatrix is the most systematic "
        "medieval account of talisman construction within a Hermetic-Neoplatonic theoretical framework."
    ),
    "virtus_loci": (
        "The power or virtue inherent in a particular place, arising from its position relative to celestial "
        "bodies, its geological or hydrological character, or its historical associations with divine "
        "presence. A key concept in medieval natural magic and Hermetic cosmology, virtus loci explains why "
        "certain sites are efficacious for ritual, healing, or oracular activity. The concept grounds the "
        "Hermetic understanding of the earth as a living body saturated with astral influences."
    ),
    "anima_mundi": (
        "The World Soul — the animating principle that pervades and governs the material cosmos, conceived "
        "as an intermediary between the divine intellect and inert matter. Derived from Plato's Timaeus and "
        "developed by the Neoplatonists, the anima mundi became central to Hermetic cosmology, Renaissance "
        "magic, and natural philosophy. For Ficino, it was the vehicle through which celestial influences "
        "flow into terrestrial reality, making the world itself a living, ensouled organism."
    ),
    "okhema": (
        "Variant spelling of ochema — the subtle vehicle or luminous body of the soul in late Platonic and "
        "Hermetic cosmology. The okhema is the soul's intermediary body: descended from the stars, clothed "
        "in planetary qualities during its downward journey, and gradually purified during the ascent back "
        "toward the divine source. The term appears in Proclus and Iamblichus and is closely associated "
        "with the pneumatic soul-body and with theurgical practices for purifying the vehicle."
    ),
    "theurgy": (
        "Divine work — ritual practices aimed at uniting the practitioner with the divine by employing "
        "material objects, prayers, and symbolic actions that participate in higher realities. Derived from "
        "the Chaldean Oracles and systematized by Iamblichus, theurgy provided the practical counterpart to "
        "the theoretical ascent of Neoplatonic contemplation. In Hermetic circles, theurgical procedures — "
        "including suffumigation, statue animation, and astral invocation — were understood to operate "
        "through the principle of sympatheia binding the cosmos."
    ),
    "tria_prima": (
        "The three primary principles of Paracelsian alchemy: Sulphur (the principle of combustibility and "
        "soul), Mercury (the principle of fluidity and spirit), and Salt (the principle of fixity and body). "
        "Introduced by Paracelsus in the sixteenth century as a replacement for the Aristotelian four "
        "elements, the Tria Prima provided the theoretical foundation for spagyrics and became a defining "
        "concept of early modern chymical philosophy, widely adopted in Rosicrucian and Hermetic "
        "reform movements."
    ),
    "gnosis": (
        "Salvific knowledge — direct, experiential apprehension of divine reality that transforms the "
        "knower. Distinct from rational discursive knowledge (episteme) or mere belief (pistis), gnosis in "
        "the Hermetic texts is an intellective vision in which the purified mind (nous) directly perceives "
        "the divine Nous or Father-God. The acquisition of gnosis is both the means and the measure of the "
        "soul's liberation from the material world and its ascent to the divine source."
    ),
}

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

for slug, text in shorts.items():
    cur.execute(
        "UPDATE concepts SET definition_short=? WHERE slug=?",
        (text, slug),
    )
    status = "updated" if cur.rowcount else "NOT FOUND"
    print(f"{slug}: {status} ({len(text.split())} words)")

conn.commit()
conn.close()
print("Done.")
