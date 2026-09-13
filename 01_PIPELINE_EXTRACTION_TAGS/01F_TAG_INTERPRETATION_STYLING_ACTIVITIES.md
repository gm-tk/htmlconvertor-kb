> **Last updated:** Monday, 14th September, 2026 10:51 AM
> **Granular part F (6 of 6) of `01_PIPELINE_EXTRACTION_TAGS.md`** — Tag interpretation, second half: content styling, activities, links & buttons, interactive components. Opened 14 September 2026 when `01E` passed the 30 KB soft limit; the content below was **moved verbatim** from `01E_TAG_INTERPRETATION.md` (`CLAUDE.md` §4) — nothing reworded, nothing re-ordered.
> All sibling parts live in `01_PIPELINE_EXTRACTION_TAGS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## Content Styling

| Normalised | HTML |
|---|---|
| `alert` | `<div class="alert"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `important` | `<div class="alert solid"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `alert_cultural_wananga` | `<div class="alert cultural" layout="wananga"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `alert_cultural_talanoa` | `<div class="alert cultural" layout="talanoa"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `alert_cultural_combined` | `<div class="alert cultural" layout="combined"><div class="row"><div class="col-12"><p>content</p></div></div></div>` |
| `whakatauki` | `<div class="whakatauki"><p>Māori text</p><p>English text</p></div>` |
| `quote` | `<p class="quoteText">"Quote"</p><p class="quoteAck">Attribution</p>` |
| `rhetorical_question` | `<div class="rhetoricalQuestion"><p>Question text</p></div>` |
| `reo_translate` | Body class `reoTranslate` + `language`/`translation` attributes. See COMP_12 in `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` |

---

## Activities

| Normalised | HTML |
|---|---|
| `activity` + ID (interactive) | `<div class="activity interactive" number="ID">` |
| `activity` + ID (text/workbook) | `<div class="activity alertPadding" number="ID">` |
| `activity` + ID (dropbox) | `<div class="activity alertPadding dropbox" number="ID">` |
| `activity_heading` | `<h3>Activity heading text</h3>` within activity |
| `end_activity` | Closing `</div>` for activity container |

**Dropbox trigger — BLL series:** *for BLL-series modules,* append the `dropbox` modifier to any activity that ends in an **Upload to dropbox** button (or carries `[trigger engagement]` on it) — e.g. `activity dropbox` (no interactive) or `activity interactive dropbox` (with an interactive). Applies to BLL modules only; see `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Activities for the full condition.

Activity sidebar:
```html
<div class="col-md-4 offset-md-0 col-12">
    <div class="alertActivity"><h4>Note</h4><p>Text</p></div>
</div>
```

---

## Links & Buttons

| Normalised | HTML |
|---|---|
| `button` | `<a href="URL" target="_blank"><div class="button">Text</div></a>` |
| `external_link_button` | `<a href="URL" target="_blank"><div class="externalButton">Text</div></a>` |
| `external_link` — **standalone** (own line/paragraph) | `<a href="URL" target="_blank"><div class="externalButton">Text</div></a>` (constraint 75) |
| `external_link` — **inline** (inside prose, a list item, or a table cell) | `<a href="URL" target="_blank">Text</a>` |
| `engagement_quiz_button` | External quiz link button |
| `mtk_quiz` | **A numbered `activity` box (next consecutive number, even where the writer assigned none) holding ONLY these children, in order:** `<h3>` quiz title (default `Quiz`, or the writer's own title verbatim) → the writer's quiz instructions as normal `<p>` text (**omitted where the writer supplied none**) → a visible `Designer/Developer To Do:` note (create the quiz in MTK DEV and orgunit link it to the module) → `<a href="#" target="_blank"><div class="button">Go to quiz</div></a>`. **NEVER the quiz's own questions, options or answers** — silently omitted, no `Red Flag:` (constraint 65 / CL-0082). **NEVER a dropbox button.** See `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Buttons → MTK Quiz |
| `supervisor_button` | The **`super-content-button` family** (Shape A activity-integrated / Shape B section standalone / Shape C section paired — outer `<div class="row supervisor">`); the legacy `supervisorContainer`/`supervisorButton`/`supervisorContent` trio is **RETIRED — never emit it** (constraint 68). See `05_COMP_LANGUAGE_MEDIA_LAYOUT.md` → Supervisor Button for the full decision tree and templates |
| `modal_button` | `<div class="button TKmodalButton">Text</div>` + `<div class="TKmodal" size="S"><p>Content</p></div>` |
| `audio_button` | `<div class="audioButton" audioName="">` |

---

## Interactive Components

**For every interactive, consult the relevant component section from `03_COMP_CORE_INTERACTIVES.md`, `04_COMP_SEGMENTS_OVERLAYS.md`, or `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`.**

The normalised tag tells you which component; the data pattern (see section 06 in `02_DATA_CONTENT_VERIFICATION.md`) tells you how to extract the data; the component section gives you the exact HTML structure.

### Info Trigger Image

| Normalised | HTML |
|---|---|
| `info_trigger_image` | `infoImage` container with positioned `infoTrigger` elements. See COMP_08 in `04_COMP_SEGMENTS_OVERLAYS.md` for full structure. |

**⚠️ CRITICAL:** This is a DOCUMENTED component. Do NOT fall back to flip cards, accordions, or other alternatives. Use the `infoImage` pattern with `infoTrigger` elements positioned over the image using percentage-based `top` and `left` inline styles. See Pattern 12 in section 06 of `02_DATA_CONTENT_VERIFICATION.md` for data extraction and COMP_08 in `04_COMP_SEGMENTS_OVERLAYS.md` for the HTML structure.