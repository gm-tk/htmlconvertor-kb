> **Last updated:** Thursday, 13th August, 2026
> **Granular part B (2 of 3) of `16_PAGEFORGE_COMPARE_MODE.md`** — The five finding classes, the boundary check (reading PageForge's captured content from the reference box on the page), the complex/non-complex interactive rule, the exclusions (incl. the total notes-and-comments exclusion), and the uncertainty rule.
> All sibling parts live in `16_PAGEFORGE_COMPARE_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 16B — What to report, and what to ignore

Everything in this part answers one question: **did PageForge read the writer's template less
accurately than the human developer did?** If a difference does not answer that question, it does
not belong in the report.

---

## 1. THE FIVE FINDING CLASSES

Every reported finding carries exactly one class. The report is ordered by class (A first), then
by page. The classes are ordered by how directly they serve PageForge's job.

| Class | Name | What it captures |
|---|---|---|
| **A** | **Tag → element interpretation** | A writer tag PageForge turned into the wrong thing: wrong element, wrong component type, wrong variant/layout, wrong class or attribute, wrong nesting, wrong heading level. |
| **B** | **Activity & interactive boundaries** | The right elements, but the wrong content assigned to them — an activity or interactive that ends too early (content spills out) or too late (content is swallowed). §3. |
| **C** | **Non-complex interactive not built** | An interactive of a type PageForge *can* build was left as a hand-off placeholder. §4. |
| **D** | **Content fidelity & placement** | Writer content dropped, duplicated, altered, leaking as a visible `[tag]`, or landing on the wrong page — including a wrong number of pages. |
| **E** | **Page scaffold & module furniture** | Header titles, module menu, footer, acknowledgements, page-level attributes — **reported only where the writer's template or media list supplied the source material** for them. |

Class **B** is the one Chris singled out and the one most likely to be under-detected, because a
boundary error produces two innocent-looking pieces of correct markup in the wrong relationship to
each other. Give §3 its own deliberate pass — do not expect boundary errors to fall out of the
element-by-element comparison.

---

## 2. NOTES ON EACH CLASS

### 2.1 Class A — tag → element interpretation

The core class. For each finding, name **the writer tag** PageForge had to interpret. Typical
shapes:

- The writer's `[tabs]` became an accordion (or a placeholder) where the human built tabs.
- `[alert]` / `[side alert]` / `[whakataukī]` rendered as the wrong callout, or as plain body text.
- A heading tag rendered at the wrong level, or a `[H2]` swallowed into a widget.
- A `[button]` / `[external link]` rendered as a bare anchor where the human built the button form
  (or the reverse).
- A layout table rendered as a `<table>` where the human built the `row`/`col` grid — or the
  reverse, a genuine data table flattened into a grid.
- A writer tag rendered as **visible bracketed text** on the page. (This is always a finding —
  cross-listed under D if content was also lost.)
- An `[image]` / `[video]` / `[audio]` reference resolved to the wrong element or the wrong media
  form. **The asset itself is out of scope** — see §5.5.

Class A is where a difference in *which documented component* was chosen belongs. Whether the
component's internal markup is perfect is only in scope when PageForge built it (§4).

### 2.2 Class C — see §4 in full

### 2.3 Class D — content fidelity

Report content the writer wrote that PageForge lost, doubled, moved, or corrupted. Also report the
opposite: content in the PageForge output that is in neither the writer's template nor the human's
file.

**Page count and page split belong here.** If the writer's `[LESSON]` / `[End page]` boundaries
produce 10 pages in the human's build and 13 in PageForge's, that is one finding, stated once at
module level, naming the boundary tags PageForge appears to have mis-read — not thirteen findings.
Pair the pages by content order before concluding a page is missing (`16A` §6 step 2).

### 2.4 Class E — scaffold, and the limit on it

PageForge generates the whole page scaffold — `<html>` attributes, body class, header titles,
module menu, footer, acknowledgements — so scaffold differences **are** actionable for Gavin.
But most of the human's scaffold comes from a structural reference file rather than from the
writer's template, and the report must not fill up with it.

**Report a class E finding only when the writer's template or the media list is the source.**
Examples that qualify: the module or lesson title the writer supplied rendered wrongly or missing;
a menu built from the writer's `[Lesson Overview]` / learning-intentions block; an acknowledgement
whose media-list row PageForge mis-read. Examples that do **not**: a stylesheet link, a script URL,
a body class, or a footer shape that the human took from their structural reference.

Where a scaffold difference is real but you cannot tell whether the writer supplied its source,
put it in the "For Gavin to judge" section (§6) rather than the main body.

---

## 3. THE BOUNDARY CHECK (class B) — do this deliberately, for every activity and interactive

A boundary error means the content is all present but assigned to the wrong container. It is
**not** visible in an element-by-element diff, and it matters more than almost anything else in the
report: PageForge's activity and interactive boundaries are decided by rules in its own code, and
an over- or under-running boundary breaks the module's structure even when every individual element
is right.

### 3.1 The two failure directions

- **SPILL (ends too early).** The writer put content inside an activity or interactive; PageForge
  closed the container before it, so the content lands **outside** — usually in a plain content
  row with no activity wrapper and no widget markup at all. In the human's file the same content
  sits **inside** the box.
- **SWALLOW (ends too late).** The reverse: PageForge kept the container open past the writer's
  own end point, so content that belongs to the *next* section — a following heading, a body
  paragraph, a table, the next activity — is **inside** the box. In the human's file it sits
  outside.

Both are reportable. Both are equally common.

### 3.2 The procedure

For **every** activity box and **every** interactive in the module, in page order:

1. **Read the writer's intent from W.** Find the opener (`[Activity …]`, or the interactive's
   invocation tag) and work out, from the template alone, where that region ends: the next
   activity opener, an explicit closer tag (`[end …]`), the next section heading, the next page
   boundary, or the point at which the content is plainly no longer part of the task.
2. **List H's membership.** In the human's file, find the corresponding
   `<div class="activity" …>` / widget wrapper and list the content it contains, in order.
3. **List P's membership.** Same, in the PageForge file. **In hand-off format the reference box's
   collapsed `cv2-int-raw` content counts as captured** — that raw block *is* the interactive's
   boundary, and comparing it to the human's widget contents is exactly how an un-built
   interactive's boundary is judged.

   **Check the owning ACTIVITY on its own account.** The reference box sits inside whatever
   activity wrapper PageForge put it in — that wrapper is PageForge's ownership decision. Compare it
   with the activity the *writer* placed the interactive in. A box inside Activity 1B where the
   writer's tag sits inside Activity 1A, or a box sitting loose outside any activity where the writer
   plainly tagged an owning one, is a class B finding in its own right — a boundary fault even when
   the widget's own content looks perfectly ordinary.

   **Where the widget has been STITCHED, the page no longer carries this evidence.** The stitcher
   replaced PageForge's reference box with Claude's finished widget and removed both anchors, so
   neither the captured content nor the ownership decision survives on the page. This is why the mode
   asks for PageForge's **original** output (`16A` §4.3, §5.2). If only a stitched upload exists, judge
   the boundary from what is visible on the page against the writer's template and mark the interactive
   `state unknown` — and if the tester happened to attach a `{CODE}_interactives.txt`, its `Activity:`
   and `Content:` lines restate PageForge's assignment and may be read as corroborating evidence.
4. **Compare the two membership lists**, and report:
   - content in H's box but outside P's → **SPILL**;
   - content outside H's box but inside P's → **SWALLOW**;
   - same members, different order or nesting → a class A finding, not B.
5. **Name the tags.** State which writer tag opened the region and which one PageForge appears to
   have treated (or failed to treat) as its end. That sentence is what makes the finding
   actionable.

### 3.3 Boundaries are checked for EVERY interactive — no exceptions

This is the rule to hold on to when the complexity and built-state rules start pulling the other
way:

> **Build quality** is judged only for interactives PageForge built, and only for non-complex
> types. **Boundaries** are judged for **every** interactive in the module — complex or
> non-complex, built, un-built, or stitched.

A complex interactive that PageForge correctly left un-built, but whose reference box swallowed the
following section's heading and three paragraphs, is a **class B finding** and must be reported.
Its internals are not — see §5.2.

### 3.4 Activity boxes the human invented

Human developers sometimes wrap a standalone task widget in an activity box the writer never
tagged. Where the human has an activity box with **no** writer `[Activity …]` opener behind it,
that is a human structural decision — record it in "For Gavin to judge" (§6) rather than as a
class B finding, and say plainly that no writer tag backs it. (PageForge has its own rules about
inventing these boxes; whether they should fire here is Gavin's call, not this report's.)

---

## 4. COMPLEX vs NON-COMPLEX INTERACTIVES (class C)

### 4.1 The rule

- **Non-complex** = a type **PageForge already has a builder for**. If PageForge left one of these
  as a hand-off placeholder, that is a **class C finding** — PageForge should have built it, and
  Gavin needs to know why it declined. Report it with the writer's raw content, because the
  content is precisely what tells him which authoring dialect his builder failed to recognise.
- **Complex** = every other type. PageForge is not expected to build these yet, so an un-built
  complex interactive is **not a finding** — it is the design. Ignore it for build purposes,
  **but still check its boundary** (§3.3).

### 4.2 The non-complex list

These are the types PageForge's builder handles, as at **6 August 2026** (PageForge build
`260618.44`):

`accordion` · `carousel` (including the rotating-banner variant) · `clickDrop` · `dragAndDrop` ·
`flipCard` · `glossary` · `hint` · `hintSlider` · `modal` · `selfCheck` · `shapeHover` ·
`speechBubble` · `tabs`

Any other type — quizzes, crossword, word find, memory game, reorder, word select, slider,
timeline, sketcher, `unclassified`, and so on — is **complex** for this mode's purposes.

**Judge by PageForge's own classification of the writer's tag**, carried in the reference box's
visible label — the full code `{CODE}-INT-{NN}-{SS}-{type}`, whose last segment is the type. (A
volunteered worklist's `Type:` line carries the same value.)

Where a volunteered worklist entry lists several types joined by ` + ` (`clickDrop + speechBubble +
carousel`) — the box's own label carries only the first — **judge on the FIRST type only**. That is
the bundle's primary type, the one PageForge's builder actually dispatched on and the one carried in
the reference code. The remaining types were never attempted as builds, so they cannot be "not
built". Name them in the finding as context where they are knowable, never as separate findings.

**Reading the type off the page.** The reference box's visible label text is the full code — read
the type from its last segment. (The box's `data-cv2-ref` attribute carries only the bare
`{CODE}-{NN}-{SS}` and no type.) If the label is unreadable and no worklist was volunteered, infer
the type from the captured content and the writer's tag, mark it in the inventory as inferred, and
make a class C finding only where the writer's own tag names a non-complex type unambiguously.

### 4.3 Why the list is written this way

The list mirrors PageForge's builder set rather than a designer's opinion of difficulty, because
that makes the finding mechanical and honest: *PageForge can build this shape, and here it did
not.* It also means the list is self-correcting — if a type drops off PageForge's builder set, its
placeholders stop being findings, and if Gavin adds a builder, the list should gain that type at
the next update. **If a type turns up that is not on this list, treat it as complex** and do not
improvise.

A volunteered worklist's own `Tier 1 / Tier 2` header lines are a **different, older classification**
(`accordion, flipCard, speechBubble, tabs`) kept for PageForge's internal routing. **Do not use the
tier lines for this decision** — use the list above.

### 4.4 What a class C finding contains

1. The reference code and type, read from the box's visible label.
2. The writer's raw content for that interactive — the collapsed `cv2-int-raw` content from the
   page. **Quote it as it stands**, red-text sentinels,
   `[tags]`, ASCII table borders and all: the exact authoring shape is the evidence.
3. What the human built from that same content (the finished widget markup).
4. One sentence on what about the authoring shape PageForge's builder may have declined on — the
   table layout, a missing marker, an extra column, a writer instruction mixed into the data, and
   so on. Say "unclear" if it is unclear; never invent a cause.

### 4.5 When PageForge DID build a non-complex interactive

Then it is PageForge's own output and is compared normally: wrong type chosen, wrong variant,
missing panels, mangled data → **class A**. Content the widget lost → **class D**. Content it
should or should not have absorbed → **class B**.

---

## 5. THE EXCLUSIONS — never report these

Each of these is dropped silently from the main report (counted in the report's exclusion summary,
`16C` §5 — so nothing disappears without trace).

### 5.1 Human decisions that are not in the writer's template

**The most important exclusion.** A human developer talks to the writer, applies design judgement,
and makes calls the template does not contain. If the human's version differs from PageForge's and
the difference cannot be traced to something the writer wrote, it is **not a PageForge fault**.
This covers: rewritten or re-ordered prose, content the human added or removed, a component
swapped for a nicer one where the writer's tag genuinely named the one PageForge used, an
editorial heading, a bespoke layout, extra explanatory text, a design flourish.

**The test:** *point at the writer's tag or the writer's words that PageForge got wrong.* If you
cannot point at one, it is not a class A–E finding.

**Excluded here, or held for §6? Use this discriminator, in this order:**

1. **Is there a writer tag or writer content that BOTH outputs are renderings of?**
   **No** — the human's version has no counterpart in the template at all (added content, an
   invented heading, a restructure of material the writer left unstructured) → **exclude here,
   silently, and count it.**
2. **Yes, and PageForge plainly departed from what that tag says** (the taxonomy in `01` maps the
   tag to what the human produced, or the writer's content plainly says otherwise) →
   **a class A–E finding.**
3. **Yes, but which reading is right cannot be settled from the template** (the tag is ambiguous,
   the taxonomy admits both, or the human's version is better for a reason the template does not
   state) → **hold for §6.**

Step 1 is the one that keeps the report honest: no writer source, no report.

### 5.2 Complex interactives — their build and their internals

Not built by PageForge by design (§4.1). Never report their absence, their placeholder, their
internals, their answer keys, or their styling. **Their boundaries are still checked** (§3.3).

### 5.3 Anything a stitched build produced

In format 2, a stitched widget's markup came from **Claude** (Mode 6), not from PageForge.
Comparing it to the human's widget measures the wrong thing. Ignore the internals; check the
boundary of the region it occupies as far as the page allows (§3.2 step 3). This is the state the
mode asks testers to avoid by uploading PageForge's **original** output, where the reference box
still carries PageForge's own assignment (`16A` §4.3).

### 5.4 Comments, developer notes and restated writer instructions — IGNORE THEM ENTIRELY

**This exclusion works exactly the same way it does in the ordinary `COMPARISON MODE`** (Mode 3,
`09B` Exclusion 1), and it is total. Notes and comments are **developer scaffolding, not module
content**: they are added, reworded, actioned and deleted continually as the writer and developer
pass information back and forth during a build, so they are guaranteed to differ between the two
outputs and that difference says nothing whatever about how PageForge read the writer's template.

**Never report — in either output, in either direction, added or removed:**

- PageForge's own visible red notes — `Writers Note:`, `Red Flag:`,
  `Designer/Developer To Do:`, `Note from {author}:` — and their absence from the human's file
  (the developer strips each one once actioned; that is the intended lifecycle);
- a note the **human developer added** that has no counterpart in PageForge's output — including
  one aimed at the course writer asking them to clarify something, one recording work still to
  do, and one left for another developer;
- a note the human **reworded, relabelled, restyled or re-prefixed** (`RED FLAG:` →
  `Designer note:`, a changed colour or `font-weight`, a dropped prefix, a trailing semicolon);
- HTML **comments** (`<!-- … -->`) present in one file and not the other, or reworded between
  them, whatever they say;
- a **restated writer instruction** or source link carried into the HTML as a visible note;
- the **presence, absence, position or ordering** of any of the above.

**The one thing that is NOT excluded:** a writer's `[tag]` or the writer's actual content
**leaking onto the page as visible bracketed text** is module content gone wrong, not a note —
that stays a class A finding (and class D if content was lost with it). The test is whether the
text is *addressed to a developer* (excluded) or is *the writer's material rendered badly*
(reported).

A corollary worth applying: where a PageForge `Designer/Developer To Do:` note already discloses
that something is pending (an asset to source, a URL to wire, a journal document to create), the
thing it names is **correct-but-pending, not a fault** — do not report it.

**Boundary work is unaffected.** Ignoring a note means ignoring it *as a difference*; it does not
mean ignoring where it sits. Where a note is the thing that appears to have closed an activity
early (`16A`'s own `[Supervisor note]` example, §6.1 of `16C`), the **boundary** is still the
finding — described in terms of the content that landed in the wrong container, never in terms of
the note's own wording.

### 5.5 Assets, URLs and publish-time wiring

PageForge ships image placeholders, unresolved media references and empty navigation hrefs by
design; the human sources the real assets and the D2L quicklinks. Exclude: image filenames and
`src` values, iStock ids and acknowledgement titles the human hand-verified, video/audio URLs,
footer and menu `href` values, quiz quicklinks. **Exception:** if the writer's template or the
media list plainly supplied the reference and PageForge attached it to the *wrong element*, that is
a class A finding about the element, not about the asset.

### 5.6 Cosmetic noise

Whitespace, indentation, line breaks, attribute order, quoting style, comment formatting, and any
re-ordering with no structural effect.

### 5.7 Content the human corrected because the writer was wrong

Typos, factual corrections, and content fixes the human made to the *writer's* material. PageForge
is required to reproduce the writer's content faithfully; reproducing it faithfully is not a fault.

---

## 6. WHEN THE ORIGIN IS UNCLEAR — the "For Gavin to judge" section

Some differences genuinely cannot be resolved from the artefacts: the human's version is better,
and it is impossible to tell from the template whether they were reading a tag PageForge misread or
exercising judgement after a conversation with the writer.

**Do not drop these, and do not pad the main body with them.** Collect them in the report's second
section, "For Gavin to judge — origin uncertain" (`16C` §3), each with:

- the writer's template extract (including "the template says nothing about this", where true),
- PageForge's output, the human's output,
- and one sentence naming **why** it is uncertain — the specific question Gavin would have to
  answer.

Keeping the main body strictly to traceable findings is what makes the main body trustworthy. A
report whose findings are all defensible, plus a short honest list of maybes, is far more use than
a long list of everything that differed.

---

## 7. WHAT THIS MODE NEVER DOES

- It never converts the module, rebuilds a page, or builds an interactive.
- It never edits, corrects or "tidies" any of the three inputs — not the writer's content, not the
  human's HTML, not PageForge's HTML.
- It never proposes code changes to PageForge, or writes PageForge configuration.
- It never updates this project's knowledge files. (That is Mode 3 → Mode 4. If a difference in
  this run reveals something about **this project's** conversion rules, mention it in one line in
  the chat reply so the tester can raise it in `COMPARISON MODE` — do not put it in the report,
  which is Gavin's.)
- It never judges whether the human developer was right. The human's file is the target by
  definition.
