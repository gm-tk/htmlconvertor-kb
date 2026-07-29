> **Last updated:** Wednesday, 29th July, 2026 6:41 PM
> **Granular part B (2 of 3) of `09_COMPARISON_MODE.md`** — Comparison Mode: the exclusions list (Section 4.1) and the inclusion gate (SS4.1-5).
> All sibling parts live in `09_COMPARISON_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.
> *Split from `09A_COMPARISON_CORE.md` on 29 July 2026 (soft-limit split per `CLAUDE.md` §2/§4) — content moved verbatim, nothing reworded or re-ordered.*

<!-- KB-PART-BODY-START -->
## 4.1 DIFFERENCES NOT TO CAPTURE (EXCLUSIONS)
 
Some categories of difference are **never reported**, even though they would otherwise look like meaningful changes. These are not "noise" in the whitespace sense — they are substantive edits that the designer has explicitly directed should be excluded from difference reports, because they do not indicate a rule fault or a conversion error. Do NOT create a comparison bundle for any difference that falls into these categories.
 
> These exclusions are applied **in addition to** the inclusion gate in Section 5. A difference must clear *both* — it must be knowledge-derived (Section 5) *and* not fall into an exclusion below — to be reported.
 
### Exclusion 1 — Red flags & designer notes (ALL templates, ALL modules)
 
Never report a difference that consists of a **red flag or designer note** being added, removed, reworded, or reformatted. This includes any change of prefix among the source-specific designer-note prefixes (`Note from {author}:`, `Writers Note:`, `Red Flag:`, `Designer/Developer To Do:`), the **substitution of any of them for a non-standard label the designer prefers** (e.g. `RED FLAG:` → `Designer note:`), the dropping of any such prefix, a change in font weight or styling of the note (including the presence or absence of the trailing semicolon in `style="color: red;"` / `style="color: red"`, and the addition or removal of `font-weight: bold`), the removal of a restated writer instruction or source link, and any change to the wording or formatting of an in-progress `<p style="color: red; font-weight: bold;">…</p>` message.
 
Rationale: red flags and designer notes are developer scaffolding, **not module content**. They are expected to change — each initial red flag is resolved and removed as the designer actions it; some are rewritten to convey a different task to be actioned later; some are added in this style specifically to generate a front-end message aimed at the original course writer (asking them to clarify something to the human developer). Because their presence and wording are inherently transient and developer-facing, comparing them tells us nothing about whether a project file needs refining. Ignore them entirely.
 
> **Scope of this exclusion (confirmed 9 July 2026).** This covers **every** red-flag / designer-note difference without exception — prefix, label, wording, inline style, font weight, and presence/absence alike. Nothing in this category is ever reported by Comparison Mode. It therefore already subsumes designer relabelling of a Convertor red flag (e.g. `RED FLAG:` / `style="color: red;"` → `Designer note:` / `style="color: red"`); no separate exclusion is needed for it.
 
### Exclusion 2 — Overview module-menu heading styling (currently suspended)
 
Do NOT report `<span>`-wrapper additions/removals or heading-level styling differences on **overview-page module-menu headings** (the `<h4>`/`<h5>` headings inside `#header` / `#module-menu-content`, e.g. the Overview / Knowledge / Practices / Learning Intentions / Success Criteria labels).
 
Rationale: the team is currently **reinforcing the one source of truth for overview information**, so overview-page module-menu content is in flux. Overview information must not be updated or flagged at this time. This exclusion is temporal ("at this time") — revisit it once the one-source-of-truth work concludes. (The underlying rule — constraint #7, no `<span>` on body headings — is unchanged; this exclusion only suppresses *reporting* the difference.)

> *Status note (16 July 2026):* the one-source-of-truth work has now landed as the **canonical overview module-menu specification** (`01_PIPELINE_EXTRACTION_TAGS.md` → Module Menu Structures → Module Overview Pages (`-00`) — Canonical Tabbed Menu; `00` constraint 67). This exclusion is deliberately **retained as-is** until the designer explicitly asks for it to be lifted; it continues to suppress *reporting* only and never changes conversion behaviour.
 
### Exclusion 3 — Bespoke designer presentation / composition decisions (ALL templates, ALL modules)
 
Do NOT report a difference that is a **bespoke, one-off presentation or composition choice** the designer made for specific content — a choice that is not a documented rule and is not expected to become one. These are editorial/layout calls made per module; they do not indicate a rule fault. Observed examples that must NOT be captured:
 
- **Bespoke content-presentation layouts** — e.g. wrapping a sentence-parts-with-labels example in a `table` (with a `<th>` label row) instead of stacked `<p>` paragraphs.
- **Bespoke compositions of documented components for an undocumented writer request** — e.g. realising an `[embed book]` / `[embed story]` request as a cover image with a `clickDrop` that opens a page-image `carousel`.
- **Bespoke component substitutions for an undocumented writer request** — e.g. using `bingo` (with permissive `value="correct"` tiles) instead of `selectionBox` for a "click-the-tile-to-change-colour" word grid.
- **Bespoke per-row column-order / column-width refinements** — e.g. swapping or resizing the text and image columns in a particular content row to suit that specific content.
Rationale: in each case the designer is exercising judgement about how a specific piece of content should look, not correcting a systematic fault in the project's rules. Capturing these would generate churn against decisions that are expected to vary module-to-module. (If a genuinely systematic, repeating fault against an existing constraint is observed across many modules, that is a different matter — but a single bespoke styling choice for one activity is not reportable.)
 
### Exclusion 4 — Designer supplying media metadata the conversion could not confirm (ALL templates, ALL modules)

Do NOT report a difference in which the designer has **filled in acknowledgement media metadata that the conversion could not confirm from the supplied materials and therefore correctly placeholdered or red-flagged**. Observed examples that must NOT be captured:

- Resolving `[title to be confirmed]` / `[author to be confirmed]` in a video acknowledgement entry to the real published title and channel.
- Supplying an image/asset title, author, or source line that the Media List, iStock acknowledgements file, or writer's template did not carry.

Rationale: **supplying media metadata the source did not contain is expected designer production work, not a rule fault.** The conversion behaved correctly — the rules require a visible placeholder or red flag rather than an invented title (`05` → Acknowledgements → Video entries; constraint 54/66), and the designer then did exactly the production step that flag exists to request. Reporting it would generate churn against a rule that is working as designed. **This suppresses *reporting* only — the conversion behaviour is unchanged:** unconfirmable media metadata is still placeholdered/red-flagged, never invented. *(Established via the OSSC401 finalized difference report, Difference 7, scope (e), 16 July 2026.)*

### Exclusion 5 — Per-instance presentational modifier classes with no documented trigger (ALL templates, ALL modules)

Do NOT report a difference in which the designer has **added or removed a documented presentational modifier class on an otherwise correctly-built component, where that modifier has no documented trigger condition and is applied per-instance to taste**. Observed examples that must NOT be captured:

- `noBG` added to one `dragAndDrop` but not to another in the same module.
- Comparable "to taste" presentational modifiers toggled on a single component instance.

Rationale: these are **styling calls that vary activity-to-activity within a single module**, not rule faults — the very same module often shows the modifier applied to one instance and omitted from the next, so there is no consistent rule to derive. The component itself was built correctly; only its presentation was tuned. **Scope limit:** this covers modifiers that are **documented but trigger-less** (available for the designer to apply at discretion). A modifier that *does* carry a documented trigger condition (e.g. `autoCheck`'s template-based auto-application, constraint 38) is **not** covered — a wrong `autoCheck` is a genuine rule fault and stays reportable. *(Established via the OSSC401 finalized difference report, Difference 20, scope (e), 16 July 2026.)*

### Exclusion 6 — Red Flag + visible fallback for an unmapped structure, later realised by the designer with an available library component (ALL templates, ALL modules)

Do NOT report a difference in which the conversion correctly raised a `Red Flag:` + visible fallback for a writer-requested interactive/diagram structure that has NO documented tag-to-component mapping, and the designer then realised the request with an available library component. Observed examples that must NOT be captured:

- A "spider / mind-map diagram" request (per-item hover reveals) built by the designer with `shapeHover`.
- A "horizontal timeline drag-and-drop" request built by the designer with a `scatter` D&D + `imageLabel layout="labelLine"` over a purpose-made timeline image.

Rationale: the conversion behaved exactly as constraint 4 and the When-In-Doubt directive require — never guess an interactive structure; raise a visible red flag with a visible fallback. The designer's later realisation with a library component is design work the flag exists to request, not a rule fault. **This suppresses *reporting* only — the conversion behaviour is unchanged:** an unmapped structure still gets a `Red Flag:` + visible fallback, never a guessed component. *(Established via the HPRE203 finalized difference report, Differences 1–2, scope (e), 29 July 2026.)*

### Exclusion 7 — Direct-Link (Mode D) derived filename swapped for the actual asset filename (ALL templates, ALL modules)

Do NOT report a difference in which the designer replaced a Direct-Link (Mode D) filename the Convertor derived — a kebab-case descriptive name, or `shutterstock-{ID}` — with the actual supplied asset filename (spaced / sentence-style names, or `shutterstock_{ID}`).

Rationale: where the source supplies no final filename, the Convertor's derived clean `images/…` path is a correct placeholder; swapping in the real asset name is expected designer production work, not a rule fault. **Reporting suppression only — Mode D derivation behaviour is unchanged.** *(Established via the WJFUN108 finalized difference report, Difference 7, scope (e), 29 July 2026.)*

### Exclusion 8 — Designer removal of the on-page `[MTKquiz]` question set (ALL templates, ALL modules)

Do NOT report a difference in which the designer removed, from a refined `[MTKquiz]` activity, the writer-supplied question/sentence set that the conversion correctly rendered on the page per constraint 65, leaving only the "Go to quiz" quicklink button (typically with a real D2L `rcode` wired in). Observed example that must NOT be captured:

- The rendered MTKquiz question set deleted in the designer's proof, with the "Go to quiz" button retained and a live `rcode` substituted for the blank href.

Rationale: the rendered question set exists so the developer can build the quiz in MTK; its deletion while preparing the proof is the anticipated production step, not a rule fault. **Reporting suppression only — conversion behaviour is unchanged:** writer-supplied quiz content is STILL rendered on the page (constraint 65 / CL-0038 / `05` → MTK Quiz Button / the `02` checklist item — all unchanged and correct). *(Established via the WJFUN108 finalized difference report, Difference 6, re-scoped (e) by designer decision, 29 July 2026.)*

> **Note on Phase 2 option (e).** When the designer assigns scope **(e) — Ignore always** to a difference (Section 7), they are telling you that an *entire category* of change like this should never be reported again. That is the designer-driven way to *grow* this exclusions list. A difference scoped (e) is kept in the finalized report **with an explicit instruction for the future project-file-update conversation (Update Mode, `11_UPDATE_MODE.md`)** to add it here as a new standing exclusion (Section 9.3). Comparison Mode itself does not edit this list — it only records the instruction.
 
### Applying the exclusions
 
Run the exclusion check during Phase 1, Detect Differences, before applying the inclusion gate and before building any bundle: if a detected change falls into **any** of Exclusions 1–8, drop it silently — do not mention it.
 
---
 
## 5. THE INCLUSION GATE — KEEP KNOWLEDGE-DERIVED, FILTER OUT TEMPLATE-DERIVED
 
This is the defining rule of Comparison Mode. **Only differences whose project output (B) was produced by the stored project instructions are reported. Differences whose output (B) was engineered by Claude from the uploaded structural reference / example module / other templated file are filtered out entirely.**
 
The question for every difference is always: *"Where did the project get that chunk of HTML from?"* — and the answer decides whether the difference is reported at all.
 
### 5.1 Why the gate exists
 
The whole point of the report is to refine the project's **own** stored instruction files. The project owns and can change those files. It does **not** own the structural reference the designer supplied for a given conversion — that template is external input. If the designer corrected a chunk that the project merely **copied from the supplied template**, updating the project files would not prevent the same chunk recurring on the next module (because the next template still ships it). So those differences are noise for this purpose, and are dropped. Only differences the project files can actually fix are worth reporting.
 
### 5.2 What is KEPT (knowledge-derived → report it)
 
A difference is **kept and reported** when the project's output (B) was **primarily produced by following a stored rule, constraint, or component pattern from project knowledge** (`00`–`08`, COMP_*, hard constraints, tag taxonomy, autoCheck auto-application, the comment & red-flag policy, the acknowledgements placement rule, the image output mode rules, etc.):
 
- The HTML in B does **not** appear in R but **does** match a documented pattern in project knowledge.
- The HTML in B was inserted because of a hard constraint, a tag-to-component mapping, or an automatic rule (e.g. `autoCheck` auto-application, acknowledgements placement, image output mode).
- The HTML in B contradicts what R actually shows because a stored constraint overrode the template.
### 5.3 What is FILTERED OUT (template-derived → drop it silently)
 
A difference is **dropped and never reported** when the project's output (B) was **primarily produced by copying, mirroring, or referencing the supplied structural reference (R), example module, or other templated file**:
 
- The HTML in B reproduces a block from R verbatim or near-verbatim (the `<head>` block, the `#header` skeleton, the `#footer` skeleton, the acknowledgements wrapper shell, the module-menu tab skeleton, etc.).
- The HTML in B is page chrome that was lifted from R as a skeleton.
- The class names, attribute values, or markup conventions in B were taken from a pattern visible in R rather than from a documented project-knowledge rule.
Drop these silently — do not bundle them, do not mention them, do not count them.
 
### 5.4 Boundary cases — items that touch both origins
 
Some differences sit at the boundary: the template ships *something* AND a stored rule *also* affects the same element. Examples:
 
- The template ships a bare `acks` wrapper; project knowledge adds the `acksAI` modifier when the module uses AI-generated media. → The wrapper shell is template-derived (drop); the `acksAI` modifier is knowledge-derived (keep, if the designer changed it).
- The template ships a `<title>` placeholder; project knowledge dictates the actual `<title>` content per page. → The element's presence is template-derived (drop); its content is knowledge-derived (keep, if changed).
- The template ships a 3-item footer-nav skeleton; project knowledge says trim and populate. → The skeleton is template-derived (drop); the trimming/populating is knowledge-derived (keep, if changed).
**Handling rule for boundary cases:**
 
1. Identify which **portion** of the changed chunk the designer actually corrected.
2. If that portion is **knowledge-derived**, report only that portion as a normal difference and note in "What changed" that the surrounding shell is template-derived and out of scope.
3. If the corrected portion is **template-derived**, or if the difference is dominantly template-derived, **drop the whole item.**
4. When the dominant origin genuinely cannot be determined, default to **keeping** the item but tag it `ORIGIN UNCERTAIN — verify before actioning`, so the developer can confirm before refining a project file on its basis.
### 5.5 Practical inclusion checklist
 
For each surviving (post-exclusion) difference, ask in order:
 
1. **Does the changed chunk in (B) appear in the structural reference (R), copied or mirrored?**
   - Yes → **template-derived → DROP.**
   - No → continue.
2. **Did a stored project-knowledge rule produce the chunk in (B)?**
   - Yes (note which file/section — you will cite it in the Phase 2 report) → **KEEP.**
   - No → re-examine; if still unclear, KEEP and tag `ORIGIN UNCERTAIN`.
3. **Does the difference touch both origins?**
   - Yes → keep only the knowledge-derived portion; drop the template-derived portion (Section 5.4).
---
 
