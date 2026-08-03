> **Last updated:** Sunday, 3rd August, 2026
> **Granular part A (1 of 5) of `01_PIPELINE_EXTRACTION_TAGS.md`** — Template levels: structural reference workflow, levels, head/heading/title patterns.
> All sibling parts live in `01_PIPELINE_EXTRACTION_TAGS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
> **Last updated:** Thursday, 16th July, 2026 9:30 PM

# 01 — Template Levels Reference

> **When to load:** At the start of every conversion. This file defines the structural skeleton.

---

## CRITICAL WORKFLOW — Structural Reference Approach

Every conversion begins with TWO inputs (plus one optional input):
1. A **content source** — one of three accepted formats:
   - A **PageForge text file** (`.txt`) containing the pre-parsed module content *(preferred/standard)*, OR
   - A **raw Writers Template Word document** (`.docx`) — the original unprocessed template *(standard-docx pathway)*, OR
   - An **MTK Writers Template Word document** (`.docx`) — bilingual Te Reo Rangatira template *(MTK pathway — see `07_MTK_DOCX_CONVERSION.md`)*
2. A **structural reference** — either:
   - **Mode A:** A dedicated **template HTML file** (e.g., `refresh_template_0.0_3_template_4-6.html`), OR
   - **Mode B:** Multiple **completed HTML files from a closely related module** (same or similar curriculum subject + year level)
3. *(Optional)* A **Media List Word document** (`.docx`) — a companion document cataloguing all external media, used to verify media links and source acknowledgement titles/descriptions.

**If the user does not provide a content source, ask for one. If they do not provide either a template file or reference module files, ask for one before proceeding** (exception: MTK conversions are self-contained — no structural reference required).

**Content source format detection:** If the content source is a `.txt`, it is PageForge. If it is a `.docx`, first check whether it is an **MTK** template (look for an "MTK WRITERS TEMPLATE" heading, a `TRR`-series module code, course code `TRR900`, and a bilingual English/Māori table format). If MTK → follow `07_MTK_DOCX_CONVERSION.md`. If the `.docx` is NOT MTK → treat it as a **standard Writers Template `.docx`** and follow the Raw Writers Template Docx rules in Section 02 below. If both a `.txt` and a `.docx` of the same module are supplied, prefer the `.txt`.

### Mode A — Dedicated Template File (Preferred)

The template file is your structural blueprint. Extract from it:
- Exact `<html>` tag attributes
- Exact `<head>` section (script URLs differ between templates — critical for offline functionality)
- Document structure pattern (header, body, footer, acknowledgements)
- Heading patterns (`<span>` wrappers only in `<h1>` header titles, never in body headings)
- Module menu structure (number of tabs, column layouts, heading levels)

### Mode B — Reference Module Files (Alternative)

When no dedicated template file exists, the user provides completed HTML files from a closely related module. These files serve as the structural reference from which you derive the template skeleton.

**⚠️ CRITICAL — Before proceeding with skeleton derivation, consult `06_TEMPLATE_RECOGNITION.md` to:**
- **Confirm the reference files are Refresh (not Legacy)** — Legacy and Refresh templates are structurally incompatible. If the reference files are Legacy, flag to the user immediately (Section 1).
- **Identify the specific Refresh sub-type** — Standard, Bilingual, Fundamentals, Inquiry, or Combo — which determines navigation systems, footer classes, and body layout (Section 2).
- **Check for known quirks that should NOT be carried into the new module** — missing `<body>` tags, dev-domain URLs, non-standard heading levels, malformed paths (Section 4).
- **Run the Mode B validation checklist** to systematically verify structural integrity before starting the conversion (Section 5).

**⚠️ CRITICAL — Reference Module Derivation Rules:**

1. **Identify page types in the reference files.** Look at the filenames and content to determine which is the overview page (-00) and which are lesson pages (-01, -02, etc.). The overview page will have the full module code in `#module-code` and typically has a `tooltip="Overview"` module menu. Lesson pages will have lesson numbers in `#module-code`.

2. **Extract the shared skeleton.** All reference files from the same module share:
   - The `<html>` tag attributes (including `template="..."` level)
   - The `<head>` section (exact script URLs — these are critical)
   - The `<body>` class
   - The basic structural pattern: `#header` → `#body` → `#footer`

3. **Use the overview page (-00) as the template for the new module's -00 page.** Extract:
   - The header structure (module-code div, `<h1><span>` title pattern, dual title if present)
   - The module menu **shell position** only — ⚠️ the overview (`-00`) module-menu **tab set is NOT copied from the reference**: the overview menu is built from the **canonical tab set** (see Module Menu Structures → Module Overview Pages (`-00`) — Canonical Tabbed Menu, constraint 67), with the new module's own content deciding which canonical tabs appear
   - The footer navigation pattern
   - The acknowledgements accordion structure (the new module's acknowledgements are ALWAYS placed at the bottom of this overview page — if the reference carries acks on its last page instead, take the structure but reposition to the overview page)

4. **Use a lesson page (-01 or -02) as the template for new lesson pages.** Extract:
   - The header structure (lesson number in `#module-code`, `<h1><span>` title pattern)
   - The module menu structure for lesson pages (simplified vs full tabs)
   - The footer navigation pattern
   - Component patterns used (activity wrappers, alert styles, grid patterns)

5. **Replace ALL reference module identifiers:**
   - Replace the reference module code (e.g., `ENGS401`) with the NEW module code (e.g., `ENGR401`) in `#module-code`, `<title>`, footer nav hrefs, and anywhere else it appears
   - Replace the reference module titles with the NEW module's titles from the content source
   - Replace the reference Te Reo title with the new module's Te Reo title (if present in the content source)

6. **Preserve ALL structural patterns from the reference:**
   - Exact script URLs from the reference `<head>` section
   - Module menu structure and heading levels as used in the reference — **for lesson-page menus only**; the overview (`-00`) module menu follows the canonical tab set (constraint 67), never the reference's particular tab selection
   - Grid patterns (`col-md-8 col-12` defaults, etc.)
   - Footer navigation pattern
   - Any class usage patterns observed in the reference

7. **Adapt intelligently when the new module differs:**
   - The new module may have more or fewer lessons than the reference — generate the correct number of output files based on the content source's page boundaries
   - The new module's overview content (Understand/Know/Do, Learning Intentions, etc.) comes from the content source — the overview (`-00`) module menu is built from the **canonical tab set** populated with this content (matching writer sections by MEANING, labelling by CANON — see Module Menu Structures), NOT by pouring content into the reference's own tab skeleton
   - If the reference module menu uses a structure that doesn't fit the new module's content (e.g., reference has full tabs but new module only needs simplified), adapt to match the content while following the documented rules in this file
   - If the reference carries acknowledgements on its last page (old convention), reposition them — the new module's acknowledgements always go at the bottom of the overview page (`-00`)

8. **Fix known structural issues identified during validation:**
   - If `06_TEMPLATE_RECOGNITION.md` flagged missing `<body>` tags, malformed script paths, or other structural defects in the reference files, correct these in the output — do NOT carry them into the new module
   - If the reference uses `tekuradev` (dev domain) for script URLs, note this in the verification summary — default to preserving the reference's domain per Rule 6, but flag it for user awareness

**Example — Deriving from ENGS401 reference files for an ENGR401 module:**
```
Reference files: ENGS401_0_0.html, ENGS401_1_0.html, ENGS401_2_0.html, ENGS401_3_0.html
New module: ENGR401 (from ENGR401_parsed.txt)

Step 0: Consult 06_TEMPLATE_RECOGNITION.md — confirm Refresh, identify as Standard Lesson
        (template="9-10"), check for known pitfalls, run validation checklist
Step 1: ENGS401_0_0.html is the overview → use as template for ENGR401-00.html
Step 2: ENGS401_1_0.html is a lesson page → use as template for ENGR401-01.html etc.
Step 3: Extract <html lang="en" level="" template="9-10" ...> from any reference file
Step 4: Extract exact <head> section (script URLs) from any reference file
Step 5: Replace "ENGS401" → "ENGR401" everywhere
Step 6: Replace "Responding to Texts" → new module title from PageForge
Step 7: Replace "Te whakautu i ngā kuputuhi" → new Te Reo title from PageForge
Step 8: Build the -00 module menu from the canonical tab set, populated with the new module's overview content (constraint 67)
Step 9: Generate correct number of lesson pages based on PageForge boundaries
```

**⚠️ CRITICAL — What NOT to carry over from reference files:**
- Do NOT carry over body content from the reference module — all body content comes from the PageForge file
- Do NOT carry over reference module-specific media (videos, images) — use the new module's media references
- Do NOT carry over reference module titles, descriptions, or Learning Intentions — use the new module's content
- Do NOT carry over the reference module's page count as a constraint — the new module defines its own page count via page boundaries
- Do NOT carry over known structural defects (missing `<body>` tags, malformed paths) — fix these silently in the output
- Do NOT carry over custom CSS `<link>` elements from reference files (e.g., `href="css/engs302.css"`) unless the new module is confirmed to have its own matching CSS file. These are module-specific and should not be replicated without confirmation.
- Do NOT automatically carry over `stickyNav.js` from reference files. This script is not universal — some modules include it and some do not. If unclear, omit it (it can be added later by the developer). Note in the verification summary: "stickyNav.js was [included/omitted] in the reference — [included/omitted] in the output."

---

## Level Identification

Module code prefix indicates year level:
- **101** = Years 1–3 (template="1-3")
- **201** = Years 4–6 (template="4-6")
- **301** = Years 7–8 (template="7-8")
- **401** = Years 9–10 (template="9-10")
- **501** / NCEA level modules (template="NCEA")

If unsure, ask the user. The module code is also available in the PageForge metadata block.

**Mode B confirmation:** When using reference module files, verify that the `template="..."` attribute in the reference matches the expected year level for the new module code. For example, if the new module is `ENGR401` (Years 9–10), the reference files should have `template="9-10"`. If there is a mismatch (e.g., reference is `template="9-10"` but new module is 301 → Years 7–8), **always set the `template` attribute to match the new module's year level, not the reference**. This is a silent correction — do not ask for confirmation. Note the correction in the verification summary.

---

## Template HTML Tag Patterns

| Level | HTML Tag |
|---|---|
| Years 1–3 | `<html lang="en" level="" template="1-3" class="notranslate" translate="no" >` |
| Years 4–6 | `<html lang="en" level="" template="4-6" class="notranslate" translate="no" >` |
| Years 7–8 | `<html lang="en" level="" template="7-8" class="notranslate" translate="no" >` |
| Years 9–10 | `<html lang="en" level="" template="9-10" class="notranslate" translate="no">` |
| NCEA | `<html lang="en" level="" template="NCEA" class="notranslate " translate="no">` |

Note: `level=""` is ALWAYS empty. Do not populate it.

---

## Template Head Sections

**CRITICAL:** The `<head>` section differs between templates. Script URLs are NOT interchangeable.

Known variations in `idoc_scripts.js` URL:
- Some: `https://tekuradev.desire2learn.com/shared/refresh_template/js/idoc_scripts.js`
- Others: `https://tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js`

Local stickyNav:
```html
<script src="js/stickyNav.js" type="text/javascript" class="stickyNav"></script>
```

**`stickyNav.js` presence:** This script is NOT universal. When operating in Mode B, note whether the reference includes it, but do NOT automatically carry it into the new module. If unclear, omit it (it can be added later by the developer). Flag in the verification summary: "stickyNav.js was [included/omitted] in the reference — [included/omitted] in the output."

**ALWAYS copy exact `idoc_scripts.js` URL from the provided structural reference (template file or reference module files).** Do NOT carry over module-specific CSS `<link>` elements from reference files.

**Void element self-closing syntax:** Use XHTML-style self-closing tags on void elements (e.g., `<meta charset="utf-8" />`, `<link ... />`, `<img ... />`). This is the convention used consistently by human developers across all Refresh template files.

**DOCTYPE casing:** Use lowercase `<!doctype html>` (not `<!DOCTYPE html>`). This matches the convention used across all human-developed Refresh template files.

**Mode B note:** See `06_TEMPLATE_RECOGNITION.md` Section 4.1 for a list of known files that use the dev domain (`tekuradev`). If the reference files use `tekuradev`, flag this to the user in the verification summary.

---

## Template Heading Patterns

**Body headings (ALL levels, including Years 1–3)** do NOT use `<span>` wrappers:
```html
<h2>Heading Text</h2>
<h3>Heading Text</h3>
<h4>Heading Text</h4>
<h5>Heading Text</h5>
```

**⚠️ CRITICAL:** `<span>` wrappers are used ONLY inside `<h1>` elements in the page header (i.e., `<h1><span>Title Text</span></h1>`). Do NOT add `<span>` to any body headings (`<h2>` through `<h5>`) at any year level.

**HEADING FORMATTING RULE:** Never wrap entire headings in italic/bold unless writer explicitly styled only part of the heading. Full-heading italic is almost always a .docx artefact — strip it.

---

## Template Title Patterns

### Page `<title>` Element

**Overview page (-00):** The `<title>` element should contain the module code followed by a space and the English module title:
```html
<title>OSAI101 AI Digital Citizenship</title>
```

**Lesson page (-01, -02, etc.):** The `<title>` element should contain ONLY the module code followed by a space and the lesson number. Do NOT include a lesson-specific title or the module English title in the `<title>` element for lesson pages:
```html
<title>ENGC401 1.0</title>
<title>ENGS301 01</title>
```

**⚠️ CRITICAL — `<title>` English only:** Do NOT include Te Reo Māori translations or subtitles in the `<title>` element. The `<title>` is English-only. Te Reo titles appear only in the visible page header `<h1>` elements.

**Mode B note:** When deriving from reference files, the `<title>` format pattern is preserved but the module code and title text are replaced with the new module's values. Follow the standard title format patterns above. Do NOT carry over the reference module's title format if it differs from the standard.

### Overview Page (-00) Header

```html
<div id="module-code"><h1>MODULE_CODE</h1></div>
<h1><span>English Title </span></h1>
```

**YEARS 9–10 and NCEA (dual title):**
```html
<div id="module-code"><h1>MODULE_CODE</h1></div>
<h1><span>English Title </span></h1>
<h1><span>Te Reo Māori Translation </span></h1>
```

### Lesson Page (-01, -02, etc.) Header

**⚠️ CRITICAL — Lesson number format:** On lesson pages, the `#module-code` `<h1>` should contain ONLY the lesson number, NOT the full module code. Use zero-padded two-digit integers: `01`, `02`, `03`, etc. Do NOT use decimal notation (e.g., `1.0`, `2.0`) even if the reference module uses this format. The full module code is only used on the overview page (-00).

```html
<div id="module-code"><h1>01</h1></div>
<h1><span>Lesson Title </span></h1>
```

**⚠️ CRITICAL — Lesson Page `<h1>` Title — the LESSON's own title (constraint 79).** On a lesson page (`-01`, `-02`, …) the `<h1><span>` title bar carries **that lesson's own title**, NOT the module title. The header of a lesson page is lesson-scoped throughout: the `#module-code` `<h1>` holds the lesson **number** and the title `<h1><span>` holds the lesson **name**. The full module code and the module title belong to the overview page (`-00`).

> **This supersedes the former "lesson `<h1>` = MODULE title" rule and retires the OSSC series exception, which described the corpus norm rather than an exception.** Verified directly against the finalized corpus: **1,105** lesson pages carry the lesson's own title against **252** that repeat the module title, and that minority is almost entirely pages where the writer supplied **no** lesson title at all, plus the BLL phonics series (whose lesson title genuinely *is* the module's letter-team list) and single-file Fundamentals modules (which have no separate lesson pages). Per subject family the lesson title is effectively universal — CEDK, CEDO, CEDT, CEDW, ENGC, ENGI, ENGR, ENGS, HES, HIS, MXDI, MXEO, MXEX, MXFU, PES, PHE, XDLS and XGF all sit at **0.94–1.00**. The `#module-code` chip agrees: **1,390** lesson pages carry a lesson number against **49** carrying the module code.

The lesson title is **NOT** repeated as a body heading — see the de-duplication rule in `01_PIPELINE_EXTRACTION_TAGS.md` → Headings. Since the lesson title *is* the header title, the body heading that repeats it is the one dropped.

**⚠️ WRITER VARIATION IS OVERRIDDEN — fixed source order.** Writers name a lesson in several different places and formats, and none of that variation may change where the title lands. Take the **first** source below that yields a non-empty title, then normalise it:

1. text the writer put **inside** the lesson boundary tag — `[LESSON 2: Puanga]`
2. text the writer put **immediately after** the boundary tag, on the same line — `[LESSON 1] The night sky`, `[LESSON 2] Cook's First Voyage`
3. the lesson's opening `[H2]` after `[Lesson content]` — `[H2] Lesson 1: The sky above us.` or `[H2] The night sky`
4. a `[Lesson Overview]` / lesson-menu heading that names the lesson
5. **fallback** — the module English title, with a visible note (see below)

> **Why the boundary tag outranks the opening `[H2]`:** a name the writer attached to the lesson boundary is an explicit statement of *this lesson's* name, whereas the first heading inside the body may be a content sub-heading. ANZH203 is the worked case — `[LESSON 2] Cook's First Voyage` followed by `[H2] James Cook (1728 – 1779)`; the human-built page carries **Cook's First Voyage**. Where the writer supplies both and they agree (the common case, and SCES201's), the order makes no difference. A boundary label that normalises to **nothing** — e.g. `[LESSON 2] Lesson 2` — falls through to the next source, as does an empty one.

**Normalisation** applied to whichever source wins: strip a leading `Lesson N` / `Lesson N:` / `Lesson N -` / `Lesson N.N` prefix; strip a trailing full stop; strip tag residue and `**` markers; then apply the standard title-casing rules below (sentence/title/mixed case is trusted exactly as written — see *Title casing*).

**⚠️ A DUPLICATED LESSON NAME IS NOT A CONFLICT — never fall back because of one.** Where the writer supplies the lesson name **twice** — in the boundary tag *and* again as the opening `[H2]` (`[LESSON 2: Puanga]` … `[H2] Lesson 2: Puanga`) — those are the **same** title, not two competing titles: source 1 wins, the prefix is stripped, the header takes it, and the duplicate body heading is dropped. Equally, the **presence or absence of a `Lesson N` prefix on the `[H2]` changes nothing** — the prefix is stripped either way and the title still lands in the header. A prefixed `[H2]` is *not* a signal to demote the title to the body. (This is the exact failure the rule was rewritten to close: a writer whose `[H2]`s all read `Lesson N: Name` had every lesson page fall back to the module title, while a sibling module whose `[H2]`s carried no prefix converted correctly.)

For example — writer variation, identical output:

| Writers Template | Header output |
|---|---|
| `[LESSON 1]` … `[H2] Lesson 1: The sky above us.` | `<h1>01</h1>` + `<h1><span>The sky above us</span></h1>` |
| `[LESSON 2: Puanga]` … `[H2] Lesson 2: Puanga` | `<h1>02</h1>` + `<h1><span>Puanga</span></h1>` |
| `[LESSON 3] Galaxies` … `[H2] Galaxies` | `<h1>03</h1>` + `<h1><span>Galaxies</span></h1>` |
| `[LESSON 1]` … `[H2] Lesson 1 The Evolution of Film` | `<h1>01</h1>` + `<h1><span>The Evolution of Film</span></h1>` |

**FALLBACK — no lesson title supplied anywhere (constraint 79).** Only when all four sources are genuinely empty does the header fall back to the module English title, and the fallback is **disclosed, never silent** — emit one visible note at the top of the page body:

```html
<p style="color: red; font-weight: bold;">Designer/Developer To Do: no lesson title was supplied for this lesson in the Writers Template — the module title is shown in the header as a fallback. Please confirm the intended lesson title with the writer and update the header.</p>
```

**YEARS 9–10 and NCEA lesson pages — a single title, unless the LESSON itself is bilingual.** A lesson page carries **one** `<h1><span>` holding the lesson title. The module-level Te Reo title is **not** repeated beside a lesson title — measured in the corpus, dual-title modules ship **909** lesson pages with a single lesson-title `<h1>` against **118** repeating the module pair. A **second** `<h1><span>` appears only where the writer gave *that lesson* its own bilingual name, in which case the pair is the **lesson's** English + Te Reo (70 corpus pages, e.g. ANZH104 `Ngā Whare` / `Housing`), split by the same TITLE BAR parsing rule, never the module's:

```html
<div id="module-code"><h1>02</h1></div>
<h1><span>Ngā Whare </span></h1>
<h1><span>Housing </span></h1>
```

The **overview page (`-00`) is unchanged** — it keeps the module title, dual where its year level requires it.

**Te Reo title sourcing:** The Te Reo **module** title (for the overview page) may come from the PageForge metadata, the overview page content, or the `[TITLE BAR]` section. If no Te Reo title is found in any of these sources, ask the user for it before proceeding. Do NOT omit the Te Reo title on a Years 9–10/NCEA **overview** page. A **lesson** page needs a Te Reo title only when the writer gave that lesson a bilingual name — never ask for, or invent, a Te Reo lesson title that the writer did not supply.

**TITLE BAR PARSING RULE:** English and Te Reo titles MUST be split into two separate `<h1><span>` elements. Never merge into one.

**Title casing — normalise a MULTI-WORD ALL-CAPS title (corpus-validated).** If the writer's `[TITLE BAR]` text is a **multi-word phrase in ALL CAPS**, render the header `<h1><span>` in **sentence case** (capitalise the first letter, lowercase the rest) — e.g. `ROARS AND WHISPERS` → `Roars and whispers`; the Te Reo span is normalised the same way (macrons preserved), e.g. `HARURUTANGA ME NGĀ KŌHIMUHIMU` → `Harurutanga me ngā kōhimuhimu`. Human-developed modules never ship an all-caps multi-word header title — verified directly against the finalized corpus, **0 of 105** multi-word header title spans are all-caps — so an all-caps multi-word writer title is a casing artefact to normalise, exactly like the lesson-menu label / list-item normalisation below, NOT a content edit. Titles already in sentence / title / mixed case are rendered **exactly as written** (trust them — never force casing on them).

> **Single-token exception — do NOT lowercase.** A header title that is a *single* all-caps token is almost always a proper noun, brand, or acronym, not a phrase to normalise (in the corpus the only all-caps header spans were single tokens such as `STOMP`, or a stray module code like `EXPFUN02`). Leave a single all-caps token exactly as written. If it is clearly a module code rather than a real title, raise a red flag instead — a code should not be the visible title.
>
> **Proper-noun caution.** Sentence-casing cannot restore internal capitals (e.g. `AI`, `NCEA`, `New Zealand`, `Aotearoa`). If a multi-word all-caps title likely contains a proper noun or acronym, sentence-case it AND raise a visible red flag quoting the original so the designer can confirm the intended casing.

**Title-span lowercase — BLL series (inline-style exception).** *For BLL-series modules,* the header title `<span>` retains the inline `style="text-transform: lowercase"` on EVERY page (overview and lesson):

```html
<h1><span style="text-transform: lowercase">wh, tch, dge, air, ear, ere, eer</span></h1>
```

This is a documented exception to constraint #2 (no inline CSS), scoped to the **BLL module series only** — the BLL structural references carry this style on the title span and the designer wants it kept. Do NOT apply it to other module series; for non-BLL modules the title span stays bare (`<h1><span>Title</span></h1>`).

---

