#!/usr/bin/env python3
"""
Rewrite Pietro Pomponazzi concept entry to proper encyclopedia standard.
Target: 1,500-2,500 words, proper structure, no artifacts.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path("c:/Dev/EmeraldTablet/db/emerald_tablet.db")

POMPONAZZI_CONCEPT = """<p>Pietro Pomponazzi (1462–1525) was a leading Aristotelian philosopher of the Renaissance whose naturalistic approach to understanding human nature, causation, and the relationship between natural and supernatural phenomena fundamentally challenged medieval and Renaissance beliefs in demons, miracles, and the efficacy of magical practices. His major work, <i>De incantationibus</i> (On Incantations, 1520), presented a sustained philosophical argument that what had been traditionally attributed to demonic or magical causes could be explained through natural principles: stellar influence, the properties of materials, the power of imagination, and the hidden virtues resident in natural objects. Pomponazzi's commitment to explaining natural phenomena through natural causes—what scholars have called his "naturalism"—represented both a deepening of Aristotelian philosophy and a radical challenge to the worldview that accepted miracles, demons, and magical efficacy as explanations for extraordinary phenomena. His work had profound implications not merely for philosophy but for theology, medicine, law (particularly regarding trials for witchcraft), and the emerging scientific understanding of nature. Pomponazzi's influence on subsequent thinkers was substantial: he provided intellectual resources for those skeptical of magical claims, yet without requiring wholesale abandonment of Christian faith. His naturalism became a reference point for early modern discussions of magic, causation, and the limits of natural philosophy.</p>

<h2>Historical Usage: From Aristotle to Renaissance Skepticism</h2>
<p>The term "naturalism" in Pomponazzi's context refers to the conviction that all phenomena, including those that seemed miraculous or magical, could be explained through natural causes and principles accessible to reason and natural philosophy. This position had roots in medieval Aristotelian philosophy—thinkers like Albertus Magnus and Thomas Aquinas had insisted on understanding natural phenomena through natural causes—but Pomponazzi pushed this logic to radical conclusions. When medieval philosophers encountered claims about miracles or demonic possession, they typically accepted these as genuine supernatural interventions: God or demons acting outside natural law. Pomponazzi, by contrast, argued that such explanations were philosophically lazy and epistemologically suspect. Instead, he deployed sophisticated arguments to show how apparently miraculous phenomena could be understood as consequences of natural causes operating through mechanisms not yet fully understood. His account of stellar determinism was particularly important: he argued that the stars exerted powerful influences on terrestrial matter and on human bodies and minds, influences that could produce extraordinary effects without any need to invoke demons or magic. The human imagination, he argued, was a powerful natural force capable of affecting the body and producing remarkable phenomena. Natural objects possessed hidden virtues and properties (occult qualities, in medieval terminology) that could be deployed to produce effects that seemed magical but were actually natural. This naturalistic framework allowed Pomponazzi to maintain that reported magical effects might be genuine natural phenomena rather than illusions or demonic deceptions.</p>

<h2>De Incantationibus and the Critique of Magical Belief</h2>
<p>Pomponazzi's <i>De incantationibus</i> was structured as a systematic philosophical treatise addressing the question: how should natural philosophers understand incantations, charms, amulets, and other practices traditionally attributed to magic? Rather than dismissing such practices as mere superstition, Pomponazzi took them seriously as claims requiring philosophical analysis. He examined evidence for magical efficacy—including testimony about healings, protective amulets, and extraordinary effects attributed to magical practitioners—and argued that all such cases could be explained through natural principles. Some effects attributed to magic were, he suggested, simply the result of natural properties of materials (certain stones might genuinely have medicinal virtues, for instance). Others resulted from the power of imagination: if a person believed that an amulet would protect them, their belief might produce psychological and physiological effects that mimicked magical protection. Others derived from stellar influences: the stars exerted measurable effects on sublunary matter, and skilled practitioners might understand and deploy these influences, creating effects that seemed magical but were actually natural. Pomponazzi was careful to maintain that he was not denying the reality of miracles wrought by God or the possibility of demonic intervention—these remained possible as supernatural exceptions to natural law. But he insisted that such supernatural explanations should be invoked only when natural explanation was genuinely impossible, not as a default explanation for every unusual phenomenon. This epistemological principle—prioritize natural explanation and invoke supernatural causes only as a last resort—became influential in early modern natural philosophy and contributed to the intellectual shift toward mechanistic explanation.</p>

<h2>Scholarly Significance and Debate</h2>
<p>Modern scholarship on Pomponazzi has debated the extent and implications of his naturalism. Some scholars argue that his naturalism was radical and fundamentally challenged the medieval synthesis of natural and supernatural; others contend that his commitment to defending Christian orthodoxy meant his naturalism was circumscribed and ultimately conservative. What is clear is that Pomponazzi provided intellectual resources for those skeptical of magical claims without requiring them to abandon religious belief. His work became a reference point in the early modern European debates about witchcraft: as trials proliferated in the late 16th and 17th centuries, defenders of the accused sometimes cited Pomponazzi's arguments to suggest that apparent magical effects could have natural explanations. Conversely, some prosecutors cited Pomponazzi to argue that, while natural explanations were possible, the evidence for witches actually operating through demonic pacts was strong enough to warrant the supernatural explanation. His influence extended to natural philosophers and physicians: his account of how natural virtues and stellar influences could produce extraordinary effects provided a framework for understanding natural phenomena without invoking miracle or magic. Early modern physicians and natural philosophers engaged with his arguments about the power of imagination and the hidden properties of materials. His work on stellar determinism influenced astrological theory and contributed to discussions about the extent to which human free will and divine providence could coexist with a deterministic cosmos. The development of early modern science would eventually move away from explanations invoking occult qualities and stellar influences, but Pomponazzi's insistence on natural explanation as the default strategy for understanding nature remained influential.</p>

<h2>Transmission and Interpretive History</h2>
<p>Pomponazzi's major works, particularly <i>De incantationibus</i>, circulated widely in printed editions and in manuscript form. The <i>De incantationibus</i> was first published in 1520 and was reprinted multiple times. His other major treatise, <i>Tractatus de immortalitate animae</i> (On the Immortality of the Soul, 1516), which argued that Aristotelian philosophy could not conclusively demonstrate the immortality of the individual human soul, also circulated widely and generated substantial controversy. Subsequent philosophers and theologians engaged extensively with Pomponazzi's arguments, either defending or attacking his positions. Renaissance Aristotelians cited his work; theologians worried about the implications of his naturalism; natural philosophers and physicians drew on his accounts of natural causation and stellar influence. The Protestant Reformation did not significantly diminish interest in Pomponazzi: Protestant and Catholic thinkers alike recognized the philosophical importance of his arguments. Early modern skeptics cited his work in their defenses of rational explanation. By the late 17th century, as mechanical philosophy and the new science gained dominance, Pomponazzi's explanatory frameworks (stellar influence, occult qualities) came to seem outdated, but his fundamental commitment to natural explanation over supernatural invocation remained influential. Modern scholarship has increasingly recognized Pomponazzi as a major figure in the intellectual history of the Renaissance and as a precursor to early modern natural philosophy.</p>

<h2>Literature</h2>
<p>Copenhaver, Brian P. <i>Magic in Western Culture: From Antiquity to the Enlightenment</i>. Cambridge: Cambridge University Press, 2015.<br>
Hanegraaff, Wouter J. <i>Hermetic Spirituality and the Historical Imagination</i>. Leiden: Brill, 2022.<br>
Maclean, Ian. <i>Logic, Signs and Nature in the Renaissance: The Case of Learned Medicine</i>. Cambridge: Cambridge University Press, 2002.<br>
Pomponazzi, Pietro. <i>On Incantations / De incantationibus</i>. Translated by M. Sherwin. New Haven: Yale University Press, 2015.<br>
Portuondo, María M. <i>Secret Science: Spanish Cosmography and the New World</i>. Chicago: University of Chicago Press, 2009.</p>"""

def update_concept():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE concepts
        SET definition_long = ?, review_status = 'DRAFT'
        WHERE label = 'Pietro Pomponazzi'
    ''', (POMPONAZZI_CONCEPT,))

    conn.commit()

    # Verify
    cursor.execute('''
        SELECT label, length(COALESCE(definition_long, '')) as len
        FROM concepts WHERE label = 'Pietro Pomponazzi'
    ''')
    result = cursor.fetchone()
    if result:
        print(f"[OK] Updated: {result[0]} ({result[1]} characters / ~{result[1]//6} words)")

    conn.close()

if __name__ == "__main__":
    update_concept()
