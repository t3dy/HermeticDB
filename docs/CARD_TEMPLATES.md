# Card Templates — EmeraldTablet Knowledge Portal

Based on patterns from AtalantaClaudiens and HPMarginalia.

## Shared Design System

### Colors
```css
--bg: #f5f0e8;           /* parchment */
--bg-card: #fff;
--text: #2c2418;          /* dark brown */
--text-muted: #6b5d4d;
--accent: #8b4513;        /* saddle brown */
--accent-light: #d4a574;
--border: #d4c5a9;
```

### Badge System
| Badge | Color | Use |
|-------|-------|-----|
| PRIMARY | #c0392b red | Bibliography relevance |
| DIRECT | #2980b9 blue | Bibliography relevance |
| CONTEXTUAL | #7f8c8d gray | Bibliography relevance |
| HIGH confidence | #dce8d4 green | Provenance |
| MEDIUM confidence | #e8dcc8 amber | Provenance |
| LOW confidence | #e8d4d0 red | Provenance |
| DRAFT | amber | Review status |
| REVIEWED | blue | Review status |
| VERIFIED | green | Review status |

### Navigation
- Global nav bar on all pages (depth-aware relative paths)
- Back links: `← All Scholars`, `← Dictionary`
- Prev/Next on detail pages

---

## 1. Person Card (Index)

```html
<a href="persons/{slug}.html" class="card">
  <div class="card-body">
    <div class="card-sig">{name}</div>
    <div class="card-label">{era} · {role_primary badge}</div>
    <div class="card-desc">{description[:150]}...</div>
    <div class="card-meta">{text_count} texts · {role_count} roles</div>
    <div>View profile →</div>
  </div>
</a>
```

## 2. Person Detail Page

```html
<a href="../persons.html" class="back-link">← All Persons</a>
<h1>{name} <span class="badge">{role_primary}</span></h1>
<p class="meta">{era} · {birth_year}–{death_year}</p>
<p class="alt-names">Also known as: {name_alt}</p>

<div class="bio">{description / bio_html}</div>

<h2>Associated Texts</h2>
<!-- Cards with role badges: AUTHOR, TRANSLATOR, COMMENTATOR, EDITOR -->
<div class="ref-card">
  <h4><a href="../texts/{text_id}.html">{title}</a>
    <span class="badge">{role}</span></h4>
  <p>{text.description[:200]}</p>
</div>

<h2>Timeline</h2>
<!-- Events involving this person -->

<div class="provenance-section">
  Source: {source_method} · Confidence: {confidence}
</div>
```

## 3. Text Card (Index)

```html
<a href="texts/{text_id}.html" class="card">
  <div class="card-body">
    <div class="card-sig">{title}</div>
    <div class="card-label">{language badge} · {text_type badge} · {date_range}</div>
    <div class="card-desc">{description[:150]}...</div>
    <div>View details →</div>
  </div>
</a>
```

Group by: text_type (PRIMARY_SOURCE, COMMENTARY, COMPILATION, TREATISE, etc.)

## 4. Text Detail Page

```html
<a href="../texts.html" class="back-link">← All Texts</a>
<h1>{title} <span class="badge">{text_type}</span></h1>
<p class="original-title" style="font-style:italic">{title_original}</p>
<p class="meta">{language} · {date_composed_start}–{date_composed_end}</p>

<div class="description">{description}</div>

<h2>Transmission</h2>
<p>{transmission_notes}</p>

<h2>Associated Persons</h2>
<!-- Person cards with role badges -->

<h2>Related Texts</h2>
<!-- text_relationships: CONTAINS, DERIVES_FROM, TRANSLATION_OF, etc. -->
<div class="ref-card" style="border-left:4px solid {relationship_color}">
  <span class="badge">{relationship_type}</span>
  <a href="{child_text_id}.html">{child_title}</a>
  <p class="notes">{notes}</p>
</div>

<h2>Related Concepts</h2>
<!-- concept_text_refs links -->

<h2>Translations</h2>
<!-- If this is the Emerald Tablet: link to parallel viewer -->

<div class="provenance-section">...</div>
```

## 5. Concept Card (Index)

```html
<a href="concepts/{slug}.html" class="card">
  <div class="card-body">
    <div class="card-sig">{label} <span class="badge">{category}</span></div>
    <div class="card-desc">{definition_short}</div>
    <div>View definition →</div>
  </div>
</a>
```

Group by: category (COSMOLOGICAL, ALCHEMICAL, PHILOSOPHICAL, LINGUISTIC, THEOLOGICAL)

## 6. Concept Detail Page

```html
<a href="../concepts.html" class="back-link">← Concepts</a>
<h1>{label} <span class="badge">{category}</span></h1>
<p class="alt-labels">{label_alt}</p>

<div class="definition-short" style="border-left:3px solid var(--accent);padding-left:1rem;font-style:italic">
  {definition_short}
</div>

<div class="definition-long">{definition_long}</div>

<h2>Significance to the Hermetic Tradition</h2>
<p>{significance}</p>

<h2>Appears In</h2>
<!-- concept_text_refs: linked text cards -->

<h2>Related Concepts</h2>
<!-- concept_links: RELATED, SUBSET_OF, DERIVED_FROM, EXPLAINS -->
<a href="{slug}.html" class="source-link">{label} ({relationship})</a>

<div class="provenance-section">...</div>
```

## 7. Bibliography Card

```html
<div class="ref-card">
  <h4>{author} ({year})
    <span class="badge badge-{relevance}">{relevance}</span>
    {in_collection ? '<span class="badge" style="background:#d4edda">In Collection</span>' : ''}
  </h4>
  <p><em>{title}</em></p>
  <p class="meta">{journal or publisher} · {pub_type}</p>
  <p class="notes">{notes}</p>
</div>
```

Group by: relevance (PRIMARY → DIRECT → CONTEXTUAL)

## 8. Timeline Event

```html
<div class="timeline-year">{year}</div>
<div class="timeline-card" style="border-left:4px solid {event_type_color}">
  <h4><span class="badge" style="background:{color}">{event_type}</span> {title}</h4>
  <p>{description}</p>
  <p class="meta">
    {person_link} · {text_link}
  </p>
</div>
```

Event colors: COMPOSITION=#8e44ad, TRANSLATION=#2980b9, COMMENTARY=#e67e22, PUBLICATION=#27ae60, SCHOLARSHIP=#16a085

## 9. Manuscript Card

```html
<a href="manuscripts/{manuscript_id}.html" class="card">
  <div class="card-body">
    <div class="card-sig">{shelfmark}</div>
    <div class="card-label">{repository}, {city}</div>
    <div class="card-desc">{contents_summary[:150]}</div>
    <div>View details →</div>
  </div>
</a>
```

## 10. Emerald Tablet Parallel Translation Viewer (Centerpiece)

```html
<div class="parallel-viewer">
  <table class="verse-table">
    <thead>
      <tr>
        <th>Verse</th>
        <th>Arabic (Sirr al-Khaliqa)</th>
        <th>Latin Vulgate</th>
        <th>Hugo of Santalla</th>
        <th>Newton English</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="verse-num">{verse_number}</td>
        <td class="verse-text" dir="rtl">{arabic_text}</td>
        <td class="verse-text">{latin_text}</td>
        <td class="verse-text">{hugo_text}</td>
        <td class="verse-text">{newton_text}</td>
      </tr>
    </tbody>
  </table>
</div>
```

Column selection via JavaScript checkboxes. RTL support for Arabic.

## Card Grid Layout

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
}
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1.25rem;
  transition: transform 0.15s, box-shadow 0.15s;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
```
