> **Last updated:** Thursday, 13th August, 2026
> **Granular part C (3 of 3) of `16_PAGEFORGE_COMPARE_MODE.md`** — The report file: structure, the finding bundle, the interactive inventory, the exclusion summary (incl. the notes-and-comments counter), worked examples, and how the run closes in chat.
> All sibling parts live in `16_PAGEFORGE_COMPARE_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 16C — The report

**One downloadable file per run**, produced in a single pass. There is no scope-assignment round
trip: this report goes to **Gavin**, who decides what PageForge does about each finding, so the
tester is not asked to classify anything.

- **Filename:** `{CODE}_pageforge_compare_report.md` (Markdown by default; another format on
  request).
- Save it to the outputs location and present it with `present_files`.
- **Always produce the file**, even when there are no findings — a clean result is a result. Write
  the header and a single line: *"No PageForge conversion faults detected for this module."*
- It must be **self-contained and emailable**: Gavin will read it away from this chat, so it
  carries its own preamble, its own scope statement, and enough of each artefact to be understood
  on its own.

---

## 1. REPORT HEADER

```
# PageForge Compare Report — [MODULE_CODE] [Module Title]
Generated: [date]                     Module series: [PREFIX]        Template level: [LEVEL]
Writer's template: [filename]         Media list: [filename | none]
Human-developed files: [N files]      PageForge files: [N files]
PageForge upload format: [original (un-stitched) | stitched | mixed | provenance unconfirmed]
PageForge build: [version if the files state one | not stated]

Findings: [N]   (A tag interpretation [n] · B boundaries [n] · C non-complex not built [n] ·
                 D content fidelity [n] · E scaffold [n])
For Gavin to judge — origin uncertain: [N]

WHAT THIS REPORT IS
This compares the HTML PageForge generated for this module against the HTML a human
developer built and refined to go-live quality from the same Writers Template and Media
List. It reports only differences that trace back to something the writer actually wrote —
places where PageForge appears to have interpreted the writer's tags or content less
accurately than the developer did.

WHAT IT DELIBERATELY LEAVES OUT
- Decisions the developer made that are not in the writer's template (including anything
  agreed with the writer directly) — PageForge cannot be expected to reproduce those.
- Complex interactives PageForge is not yet expected to build, and any interactive built by
  Claude and stitched in. Their internals are out of scope — but their BOUNDARIES are in
  scope and are checked in full.
- ALL comments, developer notes and restated writer instructions, in both files and in both
  directions — PageForge's own red notes (Writers Note: / Red Flag: / Designer/Developer To
  Do: / Note from …), notes the developer added, reworded or deleted, and HTML comments.
  These change constantly as the writer and developer exchange information during a build and
  are never module content, so they are ignored entirely.
- Real assets, media URLs and publish-time links (PageForge ships placeholders by design),
  and cosmetic formatting.
[Only if the upload was stitched or mixed, or its provenance could not be confirmed:]
- NOTE: the PageForge files supplied had been through the Page Stitcher (or could not be
  confirmed as PageForge's untouched output), and stitching removes the cv2-* markers, so
  for [N] interactive(s) already present as finished markup it could not
  be established whether PageForge or Claude built them, and PageForge's own content
  boundary for them could not be read. Those are marked "state unknown" in the inventory
  and carry no "non-complex interactive not built" finding. Every interactive still in a
  PageForge reference box was judged normally. (Uploading PageForge's original, un-stitched
  output removes this limitation entirely.)
```

Never omit the two "what this is / what it leaves out" blocks. They are what let Gavin trust the
findings without re-deriving the scope rules.

---

## 2. SECTION 1 — FINDINGS

Numbered in one continuous sequence, ordered by **class (A → E)**, then by page order. Each
finding is a five-part bundle.

```
## Finding [n] — [CLASS letter]: [short title]
**Page:** [PageForge file ↔ human file, or `module-level` for a whole-module finding such as
the page count]   **Writer tag(s):** `[tag]`, `[tag]`   **Confidence:** [high | medium]

### 1. What the writer wrote
> The relevant extract from the Writers Template — the tag(s) and the surrounding content,
> quoted as they appear. For an interactive, the raw captured content (the page's collapsed
> cv2-int-raw block), verbatim including [tags] and red-text markers.

### 2. What PageForge produced
```html
[the exact HTML from the PageForge file]
```

### 3. What the developer produced
```html
[the exact HTML from the human-developed file]
```

### 4. What appears to have been mis-read
[One or two sentences, tag-focused. Name the writer tag and what PageForge did with it.
 For a boundary finding, name the tag that opened the region and the point PageForge treated
 as its end.]

### 5. Where else this may apply
[One line, only when there is real evidence in THIS module: "the same shape appears at
 [page/location] and converted the same way" — or "single occurrence in this module".
 Never speculate about other modules; corpus-wide sizing is Gavin's own step.]
```

**Quote, never paraphrase.** The value of the report is the exact before/after. Trim long blocks
with an explicit `…` rather than rewriting them, and keep enough surrounding markup that the
nesting is visible — for a boundary finding, that means showing the container's opening tag and
the sibling the content landed in.

### 2.1 Class B findings — the extra requirement

A boundary bundle must make the *membership* difference plain. In sections 2 and 3, show the
container plus the boundary of interest, and add a short membership line beneath section 3:

```
**Membership:** developer's activity 2B contains [heading, 2 paragraphs, the click-drop table];
PageForge's activity 2B contains [heading only] — the 2 paragraphs and the table follow it as
loose `row > col-12` content with no activity wrapper.
```

State the direction explicitly in section 4 using the report's own vocabulary — **SPILL** (ended
too early) or **SWALLOW** (ended too late).

### 2.2 Confidence

- **high** — the writer's tag and content plainly account for the difference.
- **medium** — traceable to the writer's content, but another reading is possible; say what the
  other reading is in section 4.
- Anything weaker does not belong in section 1 — it goes to §3.

---

## 3. SECTION 2 — FOR GAVIN TO JUDGE (ORIGIN UNCERTAIN)

Same bundle shape, its own numbering (`U1`, `U2`, …), **without** the `Confidence:` field — an
item is here precisely because its confidence is below the §2.2 floor — plus one extra line naming
the open question:

```
**Why this is uncertain:** [the specific question — e.g. "the writer's `[hint]` could
legitimately be read as either the hint slider PageForge built or the accordion the developer
built; the tag taxonomy admits both and the surrounding content does not settle it."]
```

The uncertain items are the **step 3** cases of the `16B` §5.1 discriminator: the writer *did*
write something both outputs are rendering, but which reading is right cannot be settled from the
template. A difference with **no** writer source at all is not uncertain — it is excluded
(step 1), and counted in §5.

Keep this section short and genuinely uncertain. If it grows longer than section 1, the exclusions
in `16B` §5 are not being applied firmly enough.

---

## 4. SECTION 3 — INTERACTIVE INVENTORY

One table covering **every** interactive in the module, so Gavin can see the whole picture at a
glance — including the ones deliberately not reported.

```
| # | Reference code | Type | Complexity | PageForge state | Boundary | Reported as |
|---|---|---|---|---|---|---|
| 1 | XDLS908-INT-01-01-dragAndDrop | dragAndDrop | non-complex | hand-off (not built) | ok | Finding 7 (C) |
| 2 | XDLS908-INT-02-01-crossword  | crossword   | complex     | hand-off (not built) | SWALLOW | Finding 3 (B) |
| 3 | (no code — built by PageForge) | accordion | non-complex | built by PageForge   | ok | — |
| 4 | XDLS908-INT-04-01-mcq        | multiChoiceQuiz | complex | stitched (built in Mode 6) | ok | — (internals out of scope) |
| 5 | (none — absent from P)       | flipCard    | non-complex | absent from PageForge output | n/a | Finding 11 (D) |
```

- **Reference code** — the full `{CODE}-INT-{NN}-{SS}-{type}` form from the reference box's
  visible label. A PageForge-built or stitched widget carries no code: write
  `(no code — built by PageForge)` / `(no code — stitched)`.
- **Complexity** — per the `16B` §4.2 list, judged on the FIRST type where several are listed.
- **PageForge state** — `built by PageForge` / `hand-off (not built)` / `stitched (built in Mode
  6)` / `state unknown — provenance unconfirmed` / `absent from PageForge output` (the writer's
  interactive produced nothing at all in P — a content finding, class D or A, with boundary `n/a`).
- **Boundary** — `ok` / `SPILL` / `SWALLOW`, from the `16B` §3 pass. Every row gets a verdict;
  this column is why the table exists.

---

## 5. SECTION 4 — SCOPE AND COVERAGE

Two short blocks, so nothing looks silently missing.

```
Compared:  [N] pages · [N] activity boxes · [N] interactives · [N] media items
Pages with no findings: [list]

Differences seen and deliberately excluded (counts only):
  developer decisions not traceable to the writer's template   [n]
  complex interactives — build/internals out of scope          [n]
  interactives built by Claude and stitched in                 [n]
  comments, developer notes & restated writer instructions     [n]
  assets, media URLs and publish-time links                    [n]
  cosmetic / formatting only                                   [n]
  developer corrections to the writer's own material           [n]
```

One counter per exclusion in `16B` §5, in that order — seven lines, printed even when a count is
zero. The notes counter covers `16B` §5.4 in full: PageForge's own red notes, notes the developer
added or deleted, and HTML comments, in both files and both directions.

The exclusion counts matter: they tell Gavin the report is a filtered view and roughly how much was
filtered, which is exactly what stops him assuming a quiet report means a perfect conversion.

---

## 6. WORKED EXAMPLES

### 6.1 Class B — SPILL (an activity that ended too early)

```
## Finding 4 — B: Activity 2B closes before the writer's task content
**Page:** SCCH302_2_0.html ↔ SCCH302-02.html   **Writer tag(s):** `[Activity 2B]`, `[Supervisor note]`, `[body]`   **Confidence:** high

### 1. What the writer wrote
> [Activity 2B] Testing your solutions
> [Supervisor note] You will need safety glasses for this activity.
> [body] Work through each solution in turn and record what you observe.
> [Click drop] … (values table follows)

### 2. What PageForge produced
```html
<div class="activity" number="2B">
  <div class="row"><div class="col-12"><h3>Testing your solutions</h3></div></div>
</div>
<div class="row"><div class="col-12"><p>Work through each solution in turn…</p></div></div>
<div class="row"><div class="col-12"><div class="cv2-interactive cv2-int-ref" …>…</div></div></div>
```

### 3. What the developer produced
```html
<div class="activity" number="2B">
  <div class="row"><div class="col-12"><h3>Testing your solutions</h3>
    <p>Work through each solution in turn…</p>
    <div class="clickDrop">…</div>
  </div></div>
</div>
```

**Membership:** developer's activity 2B contains [heading, paragraph, click-drop]; PageForge's
contains [heading only] — the paragraph and the interactive follow it as loose rows.

### 4. What appears to have been mis-read
SPILL. The `[Supervisor note]` directly after the `[Activity 2B]` opener appears to have closed
the activity: everything the writer placed after it — the `[body]` paragraph and the
`[Click drop]` — landed outside the box as plain content rows. The writer's own end point is the
next activity opener on the page, `[Activity 2C]`.

### 5. Where else this may apply
The same opener-then-supervisor-note shape appears at Activity 3A on page 3 and converted the
same way.
```

### 6.2 Class C — a non-complex interactive left un-built

```
## Finding 9 — C: `[accordion]` left as a hand-off placeholder
**Page:** SCCH302_1_0.html ↔ SCCH302-01.html   **Writer tag(s):** `[accordion]`   **Confidence:** high

### 1. What the writer wrote
> [accordion] Mixtures
> [2 images next to each other]
> [image] …  [image] …
> [accordion] Solutions
> …

### 2. What PageForge produced
```html
<div class="cv2-interactive cv2-int-ref" data-cv2-ref="SCCH302-01-01">SCCH302-INT-01-01-accordion  ▾…raw content collapsed…</div>
```
Type read from the last segment of the box's visible label — `SCCH302-INT-01-01-accordion` (`16B` §4).

### 3. What the developer produced
```html
<div class="accordion">…two panels, each with a heading and a two-image row…</div>
```

### 4. What appears to have been mis-read
`accordion` is a type PageForge builds, so the placeholder is a decline rather than a gap in
coverage. The panels are un-numbered (repeated bare `[accordion] <heading>` openers) and one
panel carries the layout instruction `[2 images next to each other]`, which resolves to an
image tag with no URL — either may be what the builder declined on.

### 5. Where else this may apply
Single occurrence in this module.
```

---

## 7. HOW THE RUN CLOSES IN CHAT

Present the file, then keep the message short:

1. One line on what was compared (module, pages, upload format).
2. The finding counts by class, and the uncertain count.
3. Anything that could **not** be checked, and why (a stitched rather than original upload, an
   unpaired page, a file that would not parse). Never let a gap go unmentioned.
4. One line telling the tester the file is ready to send to Gavin.
5. **Only if applicable:** one line noting that something in this run looks like a fault in **this
   project's** conversion rules rather than PageForge's, and that it belongs in `COMPARISON MODE`.

Do not paste findings into the chat, do not offer to fix anything, and do not ask the tester to
classify or scope the findings — that is Gavin's job on the other side of the report.
