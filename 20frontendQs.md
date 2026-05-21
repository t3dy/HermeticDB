# 20 Frontend Improvement Questions — HermeticDB

*Audit date: 2026-05-20. Current state: static HTML, dark academic aesthetic, Leaflet map,
force-directed graph (D3), client-side filter bars. No hover previews, no global search,
graph nodes not clickable, timeline has no era filter, map popup names are plain text.*

---

## 1. Should internal links in encyclopedia prose show hover-preview cards?

**Current state:** Dictionary entries mention persons ("Garth Fowden") and concepts
("*gnosis*") as plain text or bare `<a>` links. No preview on hover.

**Suggested answer: Yes — implement tooltip preview cards.**

When a reader hovers over an internal link (e.g., `<a href="../concepts/gnosis.html">gnosis</a>`),
a small floating card (max 300px wide) should appear showing:
- The term's label in gold
- Its `definition_short` or `description` (the 60–120 word index card)
- A faint "click to read full entry →" hint

**Why:** This is the single highest-leverage UX improvement for a scholarly reference portal.
It lets readers check a term without losing their place. The data already exists
(`definition_short` / `description` fields). Implementation is pure JS + CSS: a single
`mouseover` event listener on `<a href>` links, a fetch of a pre-built JSON lookup, and a
positioned `<div>`. No server required.

---

## 2. Should map marker popups link to biography/scholar pages?

**Current state:** Map popups show person names as plain text (e.g., "Zosimos of Panopolis
(born)"). The `person_locations` table now contains 45 associations, but the popup renders
them as strings, not hyperlinks.

**Suggested answer: Yes — link person names to their pages.**

Each name in the "Key Figures" section of the map popup should be an `<a>` tag pointing to
`/HermeticDB/biographies/{person_id}.html` or `/scholars/{person_id}.html`.

**Why:** The map is currently a dead end. A reader curious about Zosimos cannot navigate from
the Akhmim marker to his biography — they have to close the popup and hunt through the
biographies index. Adding these links closes the most obvious navigation gap and makes the
map a genuine entry point into the relational system. The `person_locations` table already
stores `person_id`; the deploy script just needs to use it when building the popup HTML.

---

## 3. Should dictionary/concept pages show which persons worked with that concept?

**Current state:** Dictionary pages have "Related Concepts" and "In the Literature" (texts)
sections. They do **not** show which historical figures used or theorized the concept.
The `person_text_roles` table exists but is unused on these pages.

**Suggested answer: Yes — add a "Key Figures" section.**

Query `person_text_roles` (and, where available, direct concept-person associations) to show
up to 8 linked names with a one-phrase role description: e.g., "Marsilio Ficino — principal
theorist in *De vita*."

**Why:** For a scholarly reference portal, knowing *who* used a concept is as important as
knowing what it means. This section transforms a static encyclopedia entry into a relational
hub. It is also the natural home for the Actor/Analyst distinction made visible: show
historical actors separately from modern analysts.

---

## 4. Should graph nodes navigate to the relevant page on click?

**Current state:** The force-directed graph on `graph.html` renders concept and person nodes.
Clicking a node does nothing — it only selects it visually.

**Suggested answer: Yes — single-click navigates; double-click opens in new tab.**

`node.on("click", d => { window.location.href = d.url; })`

Each node's data object should include a `url` field (`/HermeticDB/dictionary/{slug}.html`
for concepts, `/biographies/{id}.html` for persons). A subtle cursor change (`cursor: pointer`)
on hover signals clickability.

**Why:** The graph is currently decorative. Making nodes clickable turns it into the most
powerful navigation tool on the site — a reader can visually explore the semantic network
and jump directly to any node's full entry. This is one click to implement and transforms
the page's utility entirely.

---

## 5. Should graph edges show their relationship type on hover?

**Current state:** Edges between concept nodes are rendered as plain lines. The `concept_links`
table stores relationship types (`DERIVED_FROM`, `EXPLAINS`, `SUBSET_OF`, `OPPOSED_TO`,
`RELATED`) but this information is not visible in the graph.

**Suggested answer: Yes — show a tooltip label on edge hover.**

On `mouseover` of an edge, display a small label (e.g., "gnosis EXPLAINS nous") in a fixed
position near the cursor or at the edge's midpoint.

**Why:** The relationship type is the most intellectually valuable piece of information the
graph can convey. Without it, all edges look equivalent. A reader who sees that "alchemy
OPPOSED_TO pneumatic_philosophy" or "solve_et_coagula DERIVED_FROM chrysopoeia" has learned
something about the structure of the tradition — not just that two concepts are connected.
This requires no new data; only new rendering logic.

---

## 6. Should the timeline have era-based filter buttons?

**Current state:** The timeline lists 41 events in chronological order as flat cards. There
is no filtering. A reader wanting only Renaissance events must scroll through everything.

**Suggested answer: Yes — add era filter buttons above the timeline.**

Five buttons: ANTIQUITY · MEDIEVAL · RENAISSANCE · EARLY MODERN · MODERN. Each event card
already has a date range; the deploy script can add a `data-era` attribute. The existing
`FILTER_JS` already handles this pattern — it just needs to be wired to the timeline page.

**Why:** The timeline spans 3,000 years. Without filtering, it is overwhelming and
underutilized. Era buttons are the minimum viable navigation improvement. A bonus enhancement
would be a century-range slider, but era buttons alone are simple and already supported by
the existing filter infrastructure.

---

## 7. Should timeline event cards link to the persons and texts they mention?

**Current state:** Timeline event descriptions mention figures ("Marsilio Ficino," "Isaac
Casaubon") and texts ("*Corpus Hermeticum*") by name, as plain text within paragraphs.

**Suggested answer: Yes — auto-link named entities during deploy.**

During deploy, run a pass over each `timeline_events.description` field that matches known
`person.name` and `text.title` values and wraps them in `<a>` tags. A simple dictionary
lookup (name → page URL) built at deploy time would catch the most frequent names.

**Why:** This is the defining feature of a relational database portal vs. a flat encyclopedia.
Every mention of Ficino on the timeline should be a link to Ficino's page. The alternative —
manually tagging timeline entries — is impractical at scale. Automated entity linking at
deploy time is the correct architectural choice.

---

## 8. Should there be a global search bar in the navigation?

**Current state:** Each section (dictionary, biographies, texts) has its own search input
inside the filter bar. There is no cross-section search. A reader who types "Zosimos"
on the dictionary page gets no results because Zosimos is a person, not a concept.

**Suggested answer: Yes — add a global search overlay triggered by a nav icon.**

A magnifying-glass icon in the top nav opens a full-width overlay. As the reader types,
results appear grouped by section (Concepts, Persons, Texts, Timeline Events) — all sourced
from a pre-built `search_index.json` generated at deploy time.

**Why:** Cross-section search is the most common user need. A reader who arrives knowing
only a name or term cannot reliably find it without knowing which section to look in.
The `search_index.json` approach requires no server: the deploy script generates a flat JSON
array of `{label, url, section, description}` objects, and the JS filters client-side.
Total payload is under 150KB for this corpus.

---

## 9. Should person detail pages list the concepts they are associated with?

**Current state:** Person pages show biography text and (as of today) a "Key Locations"
section. They do not show which concepts the person theorized, used, or is cited in
connection with.

**Suggested answer: Yes — add a "Key Concepts" section.**

Query `concept_text_refs` joined through `person_text_roles` (or a direct person-concept
association if one is built) to surface up to 10 linked concept chips below the biography.

**Why:** A biography of Ficino that does not link to *prisca theologia*, *anima mundi*, or
*magia naturalis* is an island. These concept links complete the relational loop. The reader
who arrives at Ficino's page from the map or graph should be able to navigate directly to
the concepts he worked with, not hunt through the dictionary separately.

---

## 10. Should the dictionary index page show Actor Term / Analyst Term as a visual badge?

**Current state:** The dictionary index cards show label and definition_short. The
`category_type` field (`ACTOR_TERM` / `ANALYST_TERM` / `HYBRID`) is stored but rendered
only as plain metadata text below the card.

**Suggested answer: Yes — render a small colour-coded badge.**

ACTOR_TERM → gold badge; ANALYST_TERM → teal/grey badge; HYBRID → neutral. The badge
appears in the top-right corner of each index card, 2–3 lines of label, and is explained by
a legend above the filter bar.

**Why:** The Actor/Analyst distinction is the methodological core of the entire portal
(Hanegraaffian methodology). Making it instantly visible at the index level ensures that
every reader immediately registers it, rather than discovering it buried in prose. It also
makes the filter buttons (which already exist for this attribute) more legible — readers
will understand what they are filtering before they click.

---

## 11. Should the map have a side-panel list of all locations that stays visible?

**Current state:** The map has a click-to-reveal info panel at the top, but no persistent
list. To find a specific location, a reader must zoom and click each marker or know where
to look.

**Suggested answer: Yes — add a collapsible sidebar list of all 28 locations.**

A left sidebar (collapsible on mobile) lists location names alphabetically. Clicking a name
pans and zooms the map to that marker and opens its info panel, equivalent to clicking the
marker directly.

**Why:** Leaflet maps are discoverable by browsing for casual users but opaque for readers
with a specific location in mind. The sidebar converts the map from a "browse and discover"
experience into one that supports both browsing and directed lookup. It also solves the
problem of overlapping markers (e.g., Akhmim and Panopolis) which cannot both be selected
easily when zoomed out.

---

## 12. Should concept pages cross-link to their dictionary entry, and vice versa?

**Current state:** The portal has two complementary sections for concepts:
`/concepts/{slug}.html` (relational browsing) and `/dictionary/{slug}.html` (full
encyclopedia entry). The CLAUDE.md specifies they should cross-link, but this is currently
not implemented — there is no "Read the full dictionary entry →" link on concept pages
or "← Relational browsing" on dictionary pages.

**Suggested answer: Yes — add a persistent cross-link banner.**

On each `/concepts/` page: a gold banner at the top reading "Read the full encyclopedia
entry →" linking to `/dictionary/{slug}.html`. On each `/dictionary/` page: "← Browse
relational connections" linking to `/concepts/{slug}.html`.

**Why:** This is explicitly mandated in CLAUDE.md and currently missing entirely. Without it,
a reader who arrives at a concept page via the graph or filter has no way to reach the full
scholarly entry, and vice versa. This is a one-line change per page in the deploy script.

---

## 13. Should there be a back-to-top button on long encyclopedia entries?

**Current state:** Dictionary entries can run 1,500–2,500 words. There is no scroll-to-top
mechanism. After reading a long entry, the reader must scroll manually to the nav.

**Suggested answer: Yes — a fixed-position circular button, visible after 400px scroll.**

A small button (↑) fixed at bottom-right, appearing only when `window.scrollY > 400`,
scrolls to the top on click. Standard implementation, ~10 lines of JS/CSS.

**Why:** Long pages without a back-to-top button feel unfinished. For a scholarly reference
portal where entries regularly exceed 2,000 words, this is a basic usability expectation.
The implementation cost is negligible and the quality-of-life improvement for readers
navigating long entries is immediate.

---

## 14. Should the biographies index show era as a color-coded visual indicator on cards?

**Current state:** Person cards on the biographies index show the era in plain text as part
of the card metadata (`ANTIQUITY · PHILOSOPHER`). The era filter buttons exist but the
cards themselves give no visual era cue.

**Suggested answer: Yes — add a left-border colour stripe per era.**

A 4px left border: ANTIQUITY = deep ochre; MEDIEVAL = forest green; RENAISSANCE = burgundy;
EARLY_MODERN = slate blue; MODERN = charcoal silver. This is set via a `data-era` attribute
and a CSS rule in the deploy script.

**Why:** Visual era coding lets readers scan the biographies index at a glance without
reading the metadata text. It complements (not replaces) the text filter — readers can see
the era distribution of the corpus immediately, before filtering. The five-color system is
simple enough to be learnable without a legend.

---

## 15. Should the graph page have a text search to highlight specific nodes?

**Current state:** The graph renders all nodes simultaneously. With 90+ persons and 77
concepts, the graph is dense. There is no way to locate a specific node by name other than
visually scanning.

**Suggested answer: Yes — add a search input above the graph.**

As the reader types, matching nodes are highlighted (enlarged, accent-coloured) and
non-matching nodes fade to low opacity. Clearing the search restores all nodes.

**Why:** A dense force-directed graph without search is difficult for directed lookup.
A new researcher who wants to see how "gnosis" relates to other concepts cannot easily
locate the gnosis node among 150+ nodes. Text highlight search is the standard solution
for this problem in network visualizations and is straightforward to implement with D3's
existing selection pattern.

---

## 16. Should the map markers cluster when zoomed out?

**Current state:** At the default zoom level (4), markers for nearby locations — e.g.,
Alexandria and Cairo; Akhmim and Panopolis — can overlap. The duplicate
`akhmim` / `akhmim_expanded` / `panopolis` slugs for the same geographic region
make this worse.

**Suggested answer: Yes — use Leaflet.markercluster for the map.**

When multiple markers are within a pixel threshold at the current zoom, they collapse into
a numbered cluster circle. Clicking a cluster zooms to the cluster's bounds. This is the
standard Leaflet clustering plugin, already battle-tested and lightweight (18KB min+gzip).

**Why:** Overlapping markers are currently confusing and unclickable without precision. As
the map grows, clustering becomes more important. It also implicitly solves the
`akhmim`/`panopolis` duplication problem. As a parallel improvement, the duplicate slugs
for the same location should be consolidated in the database.

---

## 17. Should the texts index clearly distinguish primary sources from scholarship visually?

**Current state:** The texts index groups entries into "PRIMARY SOURCES" and "MODERN
SCHOLARSHIP" sections, but the visual treatment of cards is identical. A card for the
*Corpus Hermeticum* and a card for Hanegraaff's *Dictionary of GWE* look the same.

**Suggested answer: Yes — use a visual icon/badge and distinct card treatment.**

Primary sources: a small scroll icon (Unicode: 📜, or an SVG) and a warmer card border.
Scholarship: a book icon and a cooler card border. This can be done with a `data-type`
attribute and CSS `::before` content.

**Why:** The primary-source / secondary-scholarship distinction is architecturally central
to the portal (it is in the CLAUDE.md, ONTOLOGY.md, and the STYLEGUIDE). Making it
visually obvious at the index level reinforces the methodological principle for every
reader. A student arriving for the first time should immediately understand which entries
are original texts and which are modern analysis.

---

## 18. Should era pages (`/eras/`) be built and linked from the nav?

**Current state:** The nav bar has links to `/eras/late-antiquity.html`, `/eras/medieval.html`,
and `/eras/renaissance.html`, but these pages are referenced and never generated by the
deploy script. The `eras/` directory is created but remains empty.

**Suggested answer: Yes — generate era hub pages, or remove the nav links.**

Either: (a) generate three era pages, each showing the persons, texts, and timeline events
from that period with the existing filter infrastructure; or (b) remove the nav links to
avoid 404s. Option (a) is preferred — era hub pages are a natural entry point for
readers approaching the tradition chronologically.

**Why:** Broken nav links undermine trust in the entire portal. This is the most urgent
navigation defect currently present. If era pages are not built this session, the nav links
must be removed. If they are built, they become one of the most useful entry points for
teaching and introductory research use.

---

## 19. Should long definition_short cards on the dictionary index be truncatable?

**Current state:** Dictionary index cards show the full `definition_short` text (60–120
words). After recent updates, all definition_short fields meet the 60-word minimum, so
cards are now noticeably longer than before the update session.

**Suggested answer: Yes — clamp to 3 lines with a "show more" toggle.**

CSS `display: -webkit-box; -webkit-line-clamp: 3; overflow: hidden;` with a small
"Read more" link that removes the clamp on click. This keeps the index scannable while
preserving the full text for interested readers.

**Why:** A grid of 77 cards, each showing 100+ words, is overwhelming to scan. Clamping
to 3 lines creates a consistent card height, makes the grid more navigable, and encourages
readers to click through to the full dictionary entry — which is the intended user journey.

---

## 20. Should the graph distinguish between concept-concept edges and person-concept edges visually?

**Current state:** The graph renders concept-concept edges (from `concept_links`) and
person-text-person relationships, but it is not clear whether person nodes and concept nodes
use meaningfully different edge styles to distinguish the types of relationship.

**Suggested answer: Yes — use distinct edge colours and widths by relationship type.**

- Concept-concept RELATED: thin grey line
- Concept-concept DERIVED_FROM / EXPLAINS: medium gold line with directional arrow
- Concept-concept OPPOSED_TO: red dashed line
- Person-concept (worked with): thin teal line, lower opacity

**Why:** Edge visual encoding is the primary way a graph communicates more than a list.
A reader who can immediately see "these two concepts are opposed" vs. "this concept explains
that one" vs. "this person worked with that concept" gets scholarly value from the graph
that a plain network diagram cannot convey. The D3 selection pattern for this is identical
to the existing rendering; only the CSS properties differ by edge type.

---

## Priority Order (Recommended Implementation Sequence)

| Priority | Question | Effort | Scholarly Impact |
|---|---|---|---|
| 1 | Q18 — Fix broken era nav links (build pages or remove) | Low | High (trust) |
| 2 | Q12 — Cross-link /concepts/ ↔ /dictionary/ | Low | High (navigation) |
| 3 | Q4 — Graph nodes clickable | Low | High |
| 4 | Q2 — Map popup person links | Low-Medium | High |
| 5 | Q8 — Global search overlay | Medium | Very High |
| 6 | Q1 — Hover preview cards on internal links | Medium | Very High |
| 7 | Q6 — Timeline era filter | Low | Medium |
| 8 | Q7 — Timeline entity auto-linking | Medium | High |
| 9 | Q3 — Concept pages show key figures | Low-Medium | High |
| 10 | Q9 — Person pages show key concepts | Low-Medium | High |
| 11 | Q10 — Actor/Analyst badge on dictionary index | Low | Medium |
| 12 | Q14 — Era colour stripe on biography cards | Low | Medium |
| 13 | Q5 — Graph edge labels on hover | Medium | High |
| 14 | Q15 — Graph text search / node highlight | Medium | Medium |
| 15 | Q20 — Graph edge visual encoding by type | Medium | High |
| 16 | Q19 — Clamp definition_short cards | Low | Medium |
| 17 | Q11 — Map sidebar location list | Medium | Medium |
| 18 | Q16 — Map marker clustering | Low | Medium |
| 19 | Q13 — Back-to-top button | Very Low | Low |
| 20 | Q17 — Primary source vs. scholarship visual badge | Low | Medium |
