> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part B (2 of 5) of `01_PIPELINE_EXTRACTION_TAGS.md`** — Module menu structures; footer and acknowledgements.
> All sibling parts live in `01_PIPELINE_EXTRACTION_TAGS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## Module Menu Structures

### STANDARD LEVELS (Years 1–3 through 9–10)

#### Module Overview Pages (`-00`) — Canonical Tabbed Menu (constraint 67)

> **⚠️ THIS SECTION OVERRIDES the former "mimic the reference module's overview menu" behaviour and the former "TWO tabs: Overview and Information" description.** The overview (`-00`) module menu is built from the **fixed canonical tab set below**, populating only the tabs for which the Writers Template actually supplies content and omitting every tab whose content is absent. The reference module's *particular* tab selection is never the template — the canonical set is, and the module's own content decides which tabs appear. Source of truth: the canonical overview template `refresh_NCEA_overview 3.html`, reconciled against the finalized-module corpus. (This governs the **tabbed** overview-menu archetype; a series whose overview menu is legitimately **simplified or absent** per its corpus/series precedent — see `10_CORPUS_VALIDATED_SCAFFOLDING.md` §2/§4 — keeps that archetype. Lesson-page simplified menus are unchanged.)

**The canonical shell.** Every tabbed overview (`-00`) module menu is emitted into this shell — note `tooltip="Overview"` sits on `#module-menu-button` (not on `#module-menu-content`; this supersedes the earlier tooltip-on-content rule):

```html
<div id="module-menu-button" class="circle-button btn1" tooltip="Overview"></div>
<div id="module-menu-content" class="moduleMenu">
    <div class="row">
        <div class="tabs col-12">
            <ul class="nav nav-tabs">
                <li><a>Overview</a></li>
                <li><a>Knowledge</a></li>
                <li><a>Practices</a></li>
                <li><a>Information</a></li>
                <li><a>Standards</a></li>
            </ul>
            <div class="tab-content">
                <!-- one .tab-pane per included tab, in this same order -->
            </div>
        </div>
    </div>
</div>
```

- The `<li>` order is fixed: **Overview → Knowledge → Practices → Information → Standards/Assessment.** Included tabs keep this relative order; omitted tabs simply disappear (no gap).
- Each `<li>` has a matching `.tab-pane` in `.tab-content`, in the same order — the N-th `<li>` binds positionally to the N-th `.tab-pane`. **Never emit an `<li>` without its pane, or a pane without its `<li>`.**
- The nav-tab label text is the **canonical word**, never the writer's own phrasing (see Writer Naming below). For the last tab, use **Standards** (the dominant corpus label) unless the uploaded reference clearly uses **Assessment**; the internal heading is **"Assessment for Learning"** either way.

**THE OMISSION RULE (core behaviour).** If a tab's content is not present in the Writers Template, omit that tab entirely — remove BOTH its `<li>` and its `.tab-pane`. Do NOT synthesise placeholder content to fill an optional tab (an absent optional tab is correct, not an error).

| Tab | Include when the WT supplies… | If absent |
|---|---|---|
| **Overview** | Learning Intentions and/or "How will I know…" content | Omit (rare — usually present) |
| **Knowledge** | a Knowledge list / "Knowledge" section | Omit tab + pane |
| **Practices** | a Practices list / "Practices" section | Omit tab + pane |
| **Information** | any of Planning your time / What do I need to get started / Want to know where to start | Omit tab + pane |
| **Standards/Assessment** | Assessment-for-learning text and/or NCEA standard(s) | Omit tab + pane |

Consequences: a module with only LI + Information becomes a two-tab menu (Overview + Information); an NCEA module missing Knowledge/Practices becomes Overview + Information + Standards; the full five-tab menu appears only when the module genuinely carries all five.

**THE FIVE CANONICAL PANELS.**

*Overview tab (almost always present)* — holds **Learning Intentions** and **How will I know I have learned it?** Titles are `<h4><span>…</span></h4>`; under each title is a `<h5>` label — `We are learning:` (under Learning Intentions) and `I can:` (under How will I know I have learned it?) — each followed by a `<ul>`. **PICK EXACTLY ONE VARIATION** (never both; any `Designer note:` lines and the `<hr class="my-4">` divider between variation examples in the raw template are authoring annotations — never emitted):

Variation 1 — two side-by-side columns (default when both lists are present and of comparable length):
```html
<div class="tab-pane">
    <div class="row">
        <div class="col-md-6 col-12 paddingR">
            <h4><span>Learning Intentions</span></h4>
            <h5>We are learning:</h5>
            <ul>
                <li>…</li>
            </ul>
        </div>
        <div class="col-md-6 col-12 paddingL">
            <h4><span>How will I know I have learned it?</span></h4>
            <h5>I can:</h5>
            <ul>
                <li>…</li>
            </ul>
        </div>
    </div>
</div>
```

Variation 2 — single stacked `col-md-8` column (use when only one of the two lists is present, or the lists are long enough that side-by-side would be cramped):
```html
<div class="tab-pane">
    <div class="row">
        <div class="col-md-8 col-12 paddingR">
            <h4><span>Learning Intentions</span></h4>
            <h5>We are learning:</h5>
            <ul>
                <li>…</li>
            </ul>
            <h4><span>How will I know I have learned it?</span></h4>
            <h5>I can:</h5>
            <ul>
                <li>…</li>
            </ul>
        </div>
    </div>
</div>
```

*Knowledge tab (optional)* — single `col-md-8 col-12` column, title `<h4><span>Knowledge</span></h4>`, then a `<ul>` of knowledge statements. The most common scroll-rule candidate — the canonical template wraps it in `overflowYScroll`:
```html
<div class="tab-pane overflowYScroll" scroll="500">
    <div class="row">
        <div class="col-md-8 col-12">
            <h4><span>Knowledge</span></h4>
            <ul>
                <li>…</li>
            </ul>
        </div>
    </div>
</div>
```

*Practices tab (optional)* — same shape as Knowledge, title `<h4><span>Practices</span></h4>` (no scroll wrapper by default).

*Information tab (optional)* — holds **Planning your time**, **What do I need to get started?**, and **Want to know where to start?** — the three sub-sections are themselves individually optional (include only those supplied; if NONE are supplied, omit the whole tab). **All headings here are `<h5>` with NO span. No te reo translation of titles in this tab.** One `col-md-8` column:
```html
<div class="tab-pane">
    <div class="row">
        <div class="col-md-8 col-12">
            <h5>Planning your time</h5>
            <ul>
                <li>…</li>
            </ul>
            <h5>What do I need to get started?</h5>
            <ul>
                <li>…</li>
            </ul>
            <h5>Want to know where to start?</h5>
            <p>…</p>
            <a href="…" target="_blank"><div class="button">Year planner</div></a>
        </div>
    </div>
</div>
```

*Standards/Assessment tab (optional)* — holds **Assessment for Learning** and the standard(s) the module works toward. **All headings `<h5>` no span. No te reo translation of titles in this tab.** **PICK ONE VARIATION by counting the standards:**

Variation A — 3 or fewer standards → single `col-md-8` column, prose form:
```html
<div class="tab-pane">
    <div class="row">
        <div class="col-md-8 col-12">
            <h5>Assessment for Learning</h5>
            <p>{intro paragraph describing the assessment / project}</p>
            <p>You will work towards the following standard:</p>
            <p><b>{Standard code + title}</b><br>
               <a href="{standard url}" target="_blank">{standard description}</a><br>
               {Level, Internal/External}<br>{N credits}</p>
        </div>
    </div>
</div>
```

Variation B — MORE than 3 standards → intro in a `col-md-8`, standards split across `col-md-6 paddingR` (left) and `col-md-6 paddingL` (right), subsequent entries in a column carrying `style="padding-top: 1rem;"`:
```html
<div class="tab-pane">
    <div class="row">
        <div class="col-md-8 col-12">
            <h5>Assessment for Learning</h5>
            <p>{intro paragraph}</p>
            <p>You will work towards the following standards:</p>
        </div>
        <div class="col-md-6 col-12 paddingR">
            <p><b>{Standard 1}</b><br><a href="…" target="_blank">…</a><br>Level 1, Internal<br>6 credits</p>
            <p style="padding-top: 1rem;"><b>{Standard 2}</b><br><a href="…" target="_blank">…</a><br>…</p>
        </div>
        <div class="col-md-6 col-12 paddingL">
            <p><b>{Standard 3}</b><br><a href="…" target="_blank">…</a><br>…</p>
            <p style="padding-top: 1rem;"><b>{Standard 4}</b><br><a href="…" target="_blank">…</a><br>…</p>
        </div>
    </div>
</div>
```

**WRITER NAMING IS UNRELIABLE — match by MEANING, label by CANON.** Writers do not use consistent tab titles or section headings. Do NOT match the writer's exact words to decide a tab — match by semantic role using a tolerant vocabulary, and do NOT copy the writer's heading text into the output as the label. Normalise to the canonical labels: nav tabs = Overview / Knowledge / Practices / Information / Standards(|Assessment); Overview-tab titles = "Learning Intentions" and "How will I know I have learned it?"; labels = "We are learning:" / "I can:"; Standards heading = "Assessment for Learning". The writer's phrasing is a **structural marker that identifies the section, not literal output** (the same principle the lesson-page menus already apply); only the list items / body text under each heading are content and carried through. Suggested mapping cues (non-exhaustive):

| Canonical tab / section | Writer phrasings seen |
|---|---|
| Learning Intentions | "Learning Intentions", "We are learning", "We are learning to…", "Ākonga will learn", "WALT", "Learning goals" |
| How will I know I have learned it? | "How will I know I've learned it?", "I can…", "Success Criteria", "You will show your understanding by", "WILF" |
| Knowledge | "Knowledge", "Know", "Knowledge (from the curriculum)" |
| Practices | "Practices", "Do", "Skills and practices" |
| Planning your time | "Planning your time", "How long will this take", "Time" |
| What do I need to get started? | "What do I need to get started?", "What you need", "Getting started", "Resources needed" |
| Want to know where to start? | "Want to know where to start?", "Where to start", "Year plan(ner)" |
| Assessment for Learning | "Assessment for Learning", "Assessment", "Standards", "NCEA standards", "You will work towards…" |

An Understand/Know/Do-framed overview maps by the same cues ("Know" → Knowledge, "Do" → Practices; an "Understand" statement maps into the Overview tab only where it clearly plays the Learning-Intentions role). When the semantic role of a WT section is genuinely ambiguous (it doesn't clearly map to any canonical tab), do NOT force it into a menu tab — leave it for normal body handling and, if uncertain, surface a visible `Red Flag:` note rather than guessing.

**HEADING & COLUMN RULES (supersede the former "all `<h4>`, never `<h5>`" overview-menu rule):**

| Location | Heading | Column |
|---|---|---|
| **Overview** tab — "Learning Intentions" / "How will I know…" titles | `<h4><span>…</span></h4>` | Var 1: `col-md-6` ×2 (`paddingR`/`paddingL`) · Var 2: `col-md-8 paddingR` |
| **Overview** tab — "We are learning:" / "I can:" labels | `<h5>…</h5>` (no span) | (inside the above column) |
| **Knowledge** / **Practices** tab titles | `<h4><span>…</span></h4>` | `col-md-8 col-12` |
| **Information** tab — all headings | `<h5>…</h5>` **no span** | `col-md-8 col-12` |
| **Standards/Assessment** tab — all headings | `<h5>…</h5>` **no span** | `col-md-8` (Var A) · `col-md-8` intro + `col-md-6`×2 (Var B) |

- `<h5>` is correct for the Information and Standards tabs and for the We-are-learning:/I-can: labels; the `<h4><span>` rule holds for the Overview/Knowledge/Practices **titles**. (These are the module-menu heading exceptions to constraint 7's no-span-on-body-headings rule, which continues to govern body content.)
- Overview-tab titles MAY be bilingual (`Reo | English`) for te-reo-carrying modules; the Information and Standards tabs never take a bilingual heading.
- **SUCCESS CRITERIA HEADING (canonical):** the Overview-tab title is **"How will I know I have learned it?"** — this canonical wording supersedes the earlier "How will I know if I've learned it?" rule for tabbed `-00` menus.
- **GRID RULE (unchanged):** within each `<div class="tab-pane">`, ALL content lives inside a `col-*` column — no loose content directly under a `.tab-pane`.

**THE SCROLL RULE (long panels).** When a panel's content would exceed roughly one horizontal iPad screen (heuristic: roughly 10+ list items or ~500+ px of content), add `overflowYScroll` to that `.tab-pane` with `scroll="500"` (the corpus standard — 34 of 36 uses): `<div class="tab-pane overflowYScroll" scroll="500">`. Apply it generously to the Knowledge panel by default, and to any other panel that is clearly long.

**Worked outcomes (sanity checks):**

| Module supplies… | Emitted tabs |
|---|---|
| LI + success + Information + 1 NCEA standard | Overview (h4-span titles), Information (h5), Standards (Var A) |
| LI + success + Knowledge + Practices + Information + 5 standards | all five: Overview, Knowledge (scroll), Practices, Information, Standards (Var B, 2-col) |
| LI + success only | Overview only (one tab) |
| LI + success + Information, no standards | Overview + Information |
| Knowledge + Practices present, no Information, 2 standards | Overview + Knowledge + Practices + Standards (Var A) |

In every case: `Designer note:` lines stripped; canonical labels used regardless of the writer's wording; exactly one variation per variable panel; each `<li>` paired 1:1 with its `.tab-pane`.

#### Lesson Pages (-01, -02, etc.) — Simplified Module Menu

Lesson pages use a simplified module menu with `<h5>` headings as label text. The `<h5>` heading IS the label text — do NOT add separate section titles (e.g., "Learning intentions") above these, and do NOT add intermediate `<p>` elements between the heading and the list.

> **⚠️ SERIES EXCEPTION — OSSC (Online Safety — Scams): `[Lesson Overview]` lead-in paragraph (constraint 70).** *For OSSC-series modules at **every** year level*, where the writer's `[Lesson Overview]` section supplies a **descriptive sentence** (typically an "Ākonga will…" statement of what the lesson covers) **before** the learning/success labels, render it as a lead-in `<p>` **above the first `<h5>`**, inside the same `col-md-8 col-12`:
>
> ```html
> <div id="module-menu-content" class="moduleMenu">
>     <div class="row">
>         <div class="col-md-8 col-12">
>             <p>Ākonga will learn the difference between, mis, dis and malinformation. They will look deeper into features of fake news.</p>
>             <h5>We are learning:</h5>
>             ...
> ```
>
> This is **compatible with — not a reversal of — the prohibition above**, which bans `<p>` elements *between a heading and its list*. The lead-in sits **above the first heading**, so both rules hold: still no `<p>` between an `<h5>` and its `<ul>`. The paragraph is **writer content**, taken verbatim from `[Lesson Overview]` (constraint 1) — it is not label text and is **not** subject to the label normalisation below. Where a lesson's `[Lesson Overview]` carries no such sentence, no lead-in is emitted (the menu opens directly with `<h5>We are learning:</h5>`) — its absence is not an error. Scoped to the **OSSC series only**. See `00_MASTER_INSTRUCTIONS.md` constraint 70.

**⚠️ CRITICAL — Lesson Page Module Menu Label Patterns by Level:**

| Template Level | Learning Label | Success Label |
|----------------|---------------|---------------|
| 1-3, 4-6 | `<h5>We are learning:</h5>` | `<h5>You will show your understanding by:</h5>` |
| 7-8 | `<h5>We are learning:</h5>` | `<h5>I can:</h5>` |
| 9-10 | `<h5>We are learning:</h5>` | `<h5>I can:</h5>` |

**⚠️ CRITICAL — Label Normalisation:** Regardless of what label text the writer uses in the PageForge's `[Lesson Overview]` section (e.g., "We are learning to...", "You will show your understanding by…", "Ākonga will:", "Learning intentions", "Success criteria", etc.), ALWAYS normalise to the standard pattern for the template level shown in the table above. The writer's label text is a structural marker, not literal content. Only the list items beneath these labels are content.

**⚠️ CRITICAL — List Item Formatting for Module Menu:**
- Items under "We are learning:" should begin lowercase with "to [verb]..." form (e.g., "to understand the history...")
- Items under "I can:" should begin lowercase with base verb form (e.g., "sort cinematic advancements...", "respond to text...")
- Items under "You will show your understanding by:" should begin lowercase with gerund form (e.g., "matching book covers...")
- Do NOT capitalise the first letter of list items in the module menu
- If the PageForge source uses capitalisation or gerund forms that don't match the heading context, normalise to match
- Learning intention and success criteria list items must NOT be wrapped in `<i>` tags, even if the PageForge source text appears in italic. Full-item italic on these list items is a .docx formatting artefact and must be stripped.

**Lesson page simplified menu example (Years 7–8 / 9–10):**

```html
<div id="module-menu-button" class="circle-button btn1" tooltip="Overview"></div>
<div id="module-menu-content" class="moduleMenu">
    <div class="row">
        <div class="col-md-8 col-12">
            <h5>We are learning:</h5>
            <ul>
                <li>to use clues from a book cover to predict the story.</li>
            </ul>
            <h5>I can:</h5>
            <ul>
                <li>match book covers to their topics based on evidence.</li>
            </ul>
        </div>
    </div>
</div>
```

**Lesson page simplified menu example (Years 1–3 / 4–6):**

```html
<div id="module-menu-button" class="circle-button btn1" tooltip="Overview"></div>
<div id="module-menu-content" class="moduleMenu">
    <div class="row">
        <div class="col-md-8 col-12">
            <h5>We are learning:</h5>
            <ul>
                <li>to identify different types of stories.</li>
            </ul>
            <h5>You will show your understanding by:</h5>
            <ul>
                <li>matching story descriptions to their covers.</li>
            </ul>
        </div>
    </div>
</div>
```

**Key structural rules for lesson page simplified menus:**
- `tooltip="Overview"` goes on `#module-menu-button` (NOT on `#module-menu-content`)
- NO `<div class="tabs">` wrapper
- NO `<ul class="nav nav-tabs">` navigation
- NO `<div class="tab-content">` or `<div class="tab-pane">` wrappers
- Content goes directly inside `<div class="row"><div class="col-md-8 col-12">`
- NO `<h4><span>Tirohanga Whānui | Overview</span></h4>` heading (this is only for overview pages and full tabbed menus)
- NO intermediate `<p>` elements between `<h5>` headings and `<ul>` lists (an OSSC `[Lesson Overview]` lead-in `<p>` sits **above the first `<h5>`**, never between a heading and its list — constraint 70)
- NO `<i>` wrapping on list items

**Mode B note on heading levels:** When using reference module files, observe the heading levels actually used in the reference module menu. If the reference uses `<h3><span>` or other non-standard patterns in its module menu, do NOT replicate these. For the NEW module, always follow the documented standard rules above (`<h5>` for lesson page labels, `<h4>` for overview page sections). Note in the verification summary which heading pattern was used and why. See `06_TEMPLATE_RECOGNITION.md` Section 4.3 for a catalogue of known non-standard heading patterns and which files use them.

### Module Overview vs Lesson Pages — When to Use Which Structure

**Module overview (-00):** built from the **canonical tab set** (Overview / Knowledge / Practices / Information / Standards — see Module Overview Pages (`-00`) — Canonical Tabbed Menu above, constraint 67), including only the tabs the Writers Template supplies content for. `tooltip="Overview"` sits on `#module-menu-button`.

**Lesson pages (-01, -02, etc.):** Overview content comes from `[Lesson Overview]`. The module menu structure depends on how much content is available:

#### Lesson Page — Simplified Menu (Single Section)

**⚠️ CRITICAL:** When a lesson page has ONLY one overview section to display (e.g., just Learning Intentions and Success Criteria from `[Lesson Overview]`, with no separate Information tab content), use the SIMPLIFIED module menu structure — **NO tabs, NO nav, tooltip on button NOT on content div**:

```html
<div id="module-menu-button" class="circle-button btn1" tooltip="Overview"></div>
<div id="module-menu-content" class="moduleMenu">
    <div class="row">
        <div class="col-md-8 col-12">
            <h5>We are learning:</h5>
            <ul>
                <li>what AI is.</li>
            </ul>
            <h5>I can:</h5>
            <ul>
                <li>understand what AI is.</li>
            </ul>
        </div>
    </div>
</div>
```

**When to use simplified vs full tabs:**
- Lesson has ONLY overview content (Learning Intentions + Success Criteria) → **SIMPLIFIED** (no tabs)
- Lesson has both overview AND separate information content → **FULL TABS** (two tabs)
- Module overview page (-00) → the **canonical tabbed menu** (constraint 67): canonical tab set, content-driven omission, `tooltip="Overview"` on `#module-menu-button`

#### Lesson Page — Full Tabs (Two Sections)

When a lesson page has both overview AND information content:

```html
<div id="module-menu-button" class="circle-button btn1" tooltip="Overview"></div>
<div id="module-menu-content" class="moduleMenu" tooltip="Overview">
    <div class="row">
        <div class="tabs col-12">
            <ul class="nav nav-tabs">
                <li><a>Overview</a></li>
                <li><a>Information</a></li>
            </ul>
            <div class="tab-content">
                <div class="tab-pane">
                    <div class="row">
                        <div class="col-md-8 col-12">
                            <h4><span>Tirohanga Whānui | Overview</span></h4>
                            <h4>Learning Intentions</h4>
                            <p>Content here</p>
                        </div>
                    </div>
                </div>
                <div class="tab-pane">
                    <div class="row">
                        <div class="col-md-8 col-12">
                            <p>Information tab content</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```

### NCEA LEVEL (501)

NCEA overview (`-00`) module menus use the **same canonical tab set** as every other level (the canonical shell is itself transcribed from `refresh_NCEA_overview 3.html`, `<html template="NCEA">`). The familiar NCEA three-tab menu (Overview / Information / Standards — e.g. gold module CEDK501) is simply the omission rule at work: Knowledge and Practices were absent from that module's source, so those tabs do not appear. Where an NCEA writer supplies Understand/Know/Do framing, map it by meaning per the Writer Naming table ("Know" → Knowledge tab, "Do" → Practices tab).

**Do NOT fabricate Understand/Know/Do, Knowledge, or Practices content if not provided** — absent content means an omitted tab, never invented placeholder content.

---

## Footer and Acknowledgements

Footer nav differs by page position:
- **Overview (-00):** `next-lesson` + `home-nav` only
- **Middle pages:** all three (`prev-lesson`, `next-lesson`, `home-nav`)
- **Final page:** `prev-lesson` + `home-nav` only

**⚠️ CRITICAL — Navigation `href`s are left EMPTY (constraint 71).** Every footer navigation anchor ships with an **empty** `href=""` — `prev-lesson`, `next-lesson`, and `home-nav` alike. The links are wired up at publish time in D2L (the LMS supplies the real quicklink targets), so the conversion must **not** populate them with computed sibling filenames such as `MODULE_CODE-XX.html`:

```html
<div id="footer">
    <ul class="footer-nav">
        <li><a href="" id="prev-lesson" target="_self"></a></li>
        <li><a href="" id="next-lesson" target="_self"></a></li>
        <li><a href="" class="home-nav" target="_parent"></a></li>
    </ul>
</div>
```

The **per-position `<li>` composition rule above is unaffected** — which anchors appear on which page (overview / middle / final) is unchanged; only the `href` values are emptied. The `id`/`class` attributes (`prev-lesson`, `next-lesson`, `home-nav`) and `target` values are unchanged, since the publish-time wiring depends on them.

**Mode B note:** because the hrefs are empty, there is **nothing to re-point** when deriving from a reference file. If a reference module carries populated navigation hrefs (e.g. `ENGS401-01.html`), do **NOT** copy them and do **NOT** rewrite them to the new module code — **empty them**. This supersedes the former "replace ALL navigation hrefs to use the NEW module code" instruction, which assumed populated hrefs.

**Mode B note:** When deriving from reference files, copy the footer **structure** — but **empty every navigation `href`** (constraint 71); do NOT carry over the reference's populated hrefs and do NOT re-point them to the new module code (see the Mode B note above). Also verify the footer `<ul>` class matches the expected pattern for the detected sub-type — see `06_TEMPLATE_RECOGNITION.md` Section 2 (Quick Identifier Table) for footer class by sub-type.

**Acknowledgements:** ⚠️ **ALWAYS placed at the bottom of the FIRST page — the overview page (`-00`, i.e. lesson 0.0)** — outside (after) the footer `<div>`, using the accordion structure from the template. Acknowledgements are NEVER placed on the last page or on any lesson page. This applies to every conversion regardless of content-source format. See `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` (Acknowledgements) for the full structure and placement rules.

**Mode B note for acknowledgements:** Reference modules built under the old convention may carry the acknowledgements accordion on their LAST page. Do NOT copy that placement. When deriving a skeleton from such reference files, take the acknowledgements accordion *structure* but place the populated block at the bottom of the new module's overview page (`-00`).



