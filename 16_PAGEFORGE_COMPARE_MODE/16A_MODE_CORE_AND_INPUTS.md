> **Last updated:** Thursday, 6th August, 2026 12:02 PM
> **Granular part A (1 of 3) of `16_PAGEFORGE_COMPARE_MODE.md`** — Mode purpose, trigger + precedence, where it sits in the tester workflow, the four inputs, the two PageForge upload formats and how to tell them apart, the workflow.
> All sibling parts live in `16_PAGEFORGE_COMPARE_MODE/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
# 16 — PageForge Compare Mode (Mode 7)

> **PURPOSE.** **PageForge** (the standalone HTML Generator, PageForge V2) converts a Writers
> Template + Media List into a module's HTML automatically. It is not yet at go-live quality, so
> while it is being refined the human developers keep building modules the normal way — through
> **this project** — and, as a test, ALSO run the same module through PageForge and keep those
> files aside.
>
> **PageForge Compare Mode is the feedback loop back to PageForge's own code.** It compares the
> **PageForge-generated HTML** against the **human-developed, go-live-quality HTML** for the same
> module, and produces **one downloadable report for Gavin** naming, with evidence, the places
> where PageForge read a writer's tag less accurately than the human developer did.
>
> **The measure is the writer's template, not the human's taste.** PageForge's job is to turn the
> writer's tags into the correct elements. A human developer routinely makes extra decisions —
> often after talking to the writer directly — that are nowhere in the Writers Template. Those are
> **not PageForge faults and are never reported.** See `16B` §5.

**This mode changes nothing about Modes 1–6.** It converts nothing, builds nothing, edits nothing.
It reads three artefacts and writes one report.

---

## 1. THE TRIGGER

The mode runs when **both** of the following are true in one message:

1. The message contains the phrase **`PAGEFORGE COMPARE MODE`** (case-insensitive). The
   variants **`PAGEFORGE COMPARISON MODE`** and **`PAGEFORGE COMPARE`** mean the same thing and
   are accepted.
2. The **PageForge-generated HTML files** for the module are uploaded with it.

If the phrase appears with no PageForge files uploaded, do not start — ask the tester to upload
the HTML files PageForge produced (the set they saved aside, clearly marked as PageForge output).

### 1.1 Same chat only — this is a hard requirement

**PageForge Compare Mode runs ONLY in the original conversion chat** — the same chat that
converted this module in Mode 1 and then ran `COMPARISON MODE` on the developer's refined files.
That chat already holds the writer's template and the developer's finished HTML, and those must be
the genuine originals.

If the chat does **not** contain the original conversion turn (and `conversation_search` /
`recent_chats` cannot surface it), **stop and say so plainly**: ask the tester to run the mode in
the chat where the module was converted. Do **not** offer to proceed in the wrong chat on
re-uploaded substitutes — a report built on files whose provenance cannot be trusted is worse than
no report, because Gavin would spend a PageForge round chasing a difference that never existed.

**This bans the wrong chat, not a re-upload.** Where this **is** the conversion chat but an
artefact has scrolled out of context or was never attached, asking the tester to re-supply that
one artefact is correct and expected (§4.1, §4.2) — the provenance is the chat, not the
attachment.

### 1.2 Precedence — and the one collision to watch

| Signal in the message | Mode |
|---|---|
| `COMPARISON MODE` **without** the word PageForge in front of it | **Mode 3** — Comparison (the project's own feedback loop) |
| `PAGEFORGE COMPARE MODE` / `PAGEFORGE COMPARISON MODE` / `PAGEFORGE COMPARE` | **Mode 7** — this file |
| `UPDATE MODE` | **Mode 4** — always takes precedence |

**The word `PAGEFORGE` immediately before COMPARE/COMPARISON MODE is the discriminator.** A
message reading `PAGEFORGE COMPARISON MODE` contains the substring `COMPARISON MODE`; it is
**Mode 7, not Mode 3**. Check for the PageForge prefix first.

`UPDATE MODE` still outranks everything. A PageForge Compare request arriving inside an Update
Mode run is not actioned — say so and ask which the designer wants first.

An uploaded `{CODE}_interactives.txt` worklist normally triggers **Mode 6**. Inside a PageForge
Compare run it does **not** — here the worklist is *evidence*, not a work order (§4.3). If a
worklist arrives with the `PAGEFORGE COMPARE MODE` phrase, read it as evidence and say so; never
silently start building interactives.

---

## 2. WHERE THIS SITS IN THE TESTER WORKFLOW

The tester follows five steps. This mode is step 5.

1. **PageForge run.** The tester converts the module's Writers Template + Media List in
   PageForge's HTML Generator and downloads the results — the HTML pages, and the companion
   `{CODE}_interactives.txt` worklist. These are stored in a folder **clearly marked as
   PageForge-generated** and are not edited.
2. **Normal build.** In a fresh chat with **this** project, the tester uploads the same Writers
   Template + Media List and converts the module the normal way (Mode 1).
3. **Refinement.** The developer takes that output away and refines it by hand until it is good
   enough to go live. This is where writer liaison, editorial judgement and design decisions
   happen.
4. **`COMPARISON MODE`** (Mode 3), in that same chat, on the refined files — the existing feedback
   loop that improves **this project's** knowledge files.
5. **`PAGEFORGE COMPARE MODE`** (this mode), in that same chat, with the **PageForge** files from
   step 1 uploaded — the feedback loop that improves **PageForge's code**. The report goes to
   Gavin.

Steps 4 and 5 are independent: neither needs the other to have run, and their outputs go to
different people for different purposes. Running step 4 first is the norm simply because the
developer is already in that chat.

---

## 3. WHAT THE REPORT IS FOR (and who reads it)

The reader is **Gavin**, who maintains PageForge's converter code. He works in disciplined rounds:
he measures a class of problem across the whole module corpus, fixes the general rule behind a
reversible flag, and proves it. So the report is most useful when it gives him, for each finding:

- **the writer's own tags** that PageForge had to interpret (his input),
- **what PageForge produced** (his current output),
- **what the human produced** (the target),
- and a plain statement of **what appears to have been mis-read**.

He does not need a fix, a patch, or a rewrite of PageForge's HTML — he needs the evidence. Never
propose code changes to PageForge in the report; describe the behaviour, not the remedy.

---

## 4. THE THREE REQUIRED INPUTS (plus one optional)

| Input | What it is | Where it comes from |
|---|---|---|
| **W — the writer's template** | The Writers Template (`.docx` or PageForge `.txt`), plus the Media List if one was supplied | Already in **this chat**, from the original conversion turn |
| **H — the human-developed HTML** | The developer's finished, go-live-quality files | Already in **this chat** — the files uploaded for `COMPARISON MODE` in step 4 |
| **P — the PageForge-generated HTML** | The pages PageForge produced from the same inputs | **Uploaded now**, with the trigger |
| **X — the interactives worklist** *(optional but important)* | `{CODE}_interactives.txt`, downloaded from PageForge alongside the pages | Uploaded now, if the tester has it (§4.3) |

**W is the referee.** Every finding must be traceable to something the writer actually wrote. A
difference between H and P that cannot be traced back to a writer tag or writer content is either
a human decision (out of scope — `16B` §5) or an uncertain item (`16B` §6, which prints in the
report's own Section 2 — `16C` §3). Never report a difference on the strength of the H-vs-P diff
alone.

### 4.1 If H is missing

If the developer's refined files are not in the chat (e.g. the tester skipped step 4), ask for
them. Without H there is nothing to compare PageForge against — the project's **own** Mode 1
output is **not** a substitute, because it has not been through the human refinement that makes it
the go-live target.

### 4.2 If W is missing

Try `conversation_search` / `recent_chats` first. If the writer's template genuinely cannot be
recovered, ask the tester to re-upload it. Do not proceed without it — see §1.1.

### 4.3 Why the worklist (X) matters

PageForge's `{CODE}_interactives.txt` lists **only the interactives PageForge did NOT build**.
That single fact answers the question this mode otherwise cannot: when a widget is present in the
PageForge files as finished markup, did **PageForge** build it, or did **Claude** build it in Mode
6 and the Page Stitcher splice it in?

- **Worklist supplied** → the answer is definitive for every interactive in the module.
- **Worklist not supplied, interactive still in its reference box** → still answerable: a box on
  the page means PageForge did not build that one.
- **Worklist not supplied, interactive present as finished markup** → **not answerable for that
  interactive.** Ask the tester for the `.txt` (they downloaded it in step 1). If they cannot
  supply it, run the comparison anyway, mark those interactives `state unknown` in the inventory
  and **make no class C finding about them** — never guess which side built a widget. The class is
  suppressed only for the interactives whose state is genuinely unknown, never for the module as a
  whole: any interactive still wearing a reference box is still judged normally.

**Matching a worklist entry to a place on the page.** The worklist lists un-built interactives
only, and a **stitched** widget carries no code at all — the stitcher removes both anchors — so a
finished widget can never be matched to a worklist entry *by code*. Match by **position**: the
entry's `File:` line gives the page, its `Activity:` line gives the owning activity (or `(none —
inline component)`), and its `Content:` block gives the writer content the widget was built from.
An entry whose content matches a finished widget on that page = that widget was **stitched**; a
finished widget that matches **no** entry = **PageForge built it**. Where the position is genuinely
ambiguous (two same-type entries in one activity), record `state unknown` rather than guessing.

---

## 5. THE TWO PAGEFORGE UPLOAD FORMATS — AND HOW TO TELL THEM APART

The tester may upload PageForge files in either of two states, and must not have to say which.
**Detect it, per interactive, from the markup.**

### 5.1 Format 1 — HAND-OFF (PageForge's default output)

PageForge leaves every interactive it cannot build as a **reference box** on the page, with the
raw captured writer content present but collapsed inside it:

```html
<div class="cv2-interactive cv2-int-ref" data-cv2-index="57" data-cv2-ref="XDLS901-04-01" style="…">
    …label row + arrow…
    <div class="cv2-int-raw">…the raw captured content, verbatim…</div>
</div>
```

**Signature:** `class="cv2-interactive cv2-int-ref"` and/or `data-cv2-ref` on the page; usually a
`{CODE}_interactives.txt` alongside. The raw content is **there** — collapsed, not missing.

### 5.2 Format 2 — STITCHED (interactives built in Mode 6 and spliced back in)

The developer took the worklist to **Interactives Build Mode** (Mode 6), got
`{CODE}_interactives_built.html`, and ran PageForge's **Page Stitcher**. The stitcher replaces each
reference box with the finished widget and **removes both anchors**, so a stitched interactive
carries **no** `cv2-*` marker at all — it looks like ordinary finished markup.

**Signature:** no `cv2-int-ref` / `cv2-interactive` on the page where the human has a widget.

### 5.3 Mixed uploads are normal — decide per interactive, never per file

The stitcher leaves an unmatched marker in place and warns rather than failing, so a partially
stitched module is a legitimate, expected state. **Classify each interactive on its own evidence**
and record the result in the report's interactive inventory (`16C` §4):

| Evidence in P | State | How the comparison treats it |
|---|---|---|
| Reference box present (`cv2-int-ref`) | **Hand-off** — PageForge did not build it | Build ignored unless the type is non-complex (`16B` §4). **Boundary still checked** — the box's captured content IS the boundary. |
| Finished widget markup, and a worklist entry matches that position (§4.3) | **Stitched** — Claude built it | Build ignored (it is not PageForge's work). **Boundary still checked.** |
| Finished widget markup, and **no** worklist entry matches that position | **PageForge-built** | Compared normally — this IS PageForge's output. |
| Finished widget markup, no worklist supplied (or the position is ambiguous) | **Unknown** | Boundary checked; build not judged; no class C finding; recorded in the inventory as `state unknown — worklist not supplied`. |
| Present in the writer's template and in H, but **nothing at all** in P — no widget and no reference box | **Absent** | Not an interactive-state question: the content itself is missing. Report as class D (content dropped), or class A if PageForge rendered it as something else entirely. |

**The rule that survives every format:** whether or not an interactive is built, **the boundary is
always checked** — which content the writer assigned to it, and which content PageForge assigned
to it. See `16B` §3.

---

## 6. WORKFLOW

```
FUNCTION pageforge_compare(W_writers_template, H_human_html, P_pageforge_html, X_worklist?):

    # 0 — VERIFY
    CONFIRM the PAGEFORGE COMPARE MODE phrase and that P is uploaded
    CONFIRM this is the original conversion chat; LOCATE W and H in it   (§1.1, §4)
    IF H missing → ASK for the developer's refined files; STOP until supplied
    IF W missing → SEARCH the chat history; if still missing → ASK; STOP until supplied
                   (a successful recovery just continues — nothing to stop for)
    IDENTIFY module code, title, series prefix, template level
    NOTE which PageForge build produced P if the files say so

    # 1 — DETECT THE UPLOAD FORMAT (per interactive, not per file)   (§5)
    SCAN P for cv2-int-ref / cv2-interactive markers
    IF X supplied → INDEX it by reference code and type
    RECORD each interactive's state: hand-off | stitched | PageForge-built | unknown

    # 2 — PAIR THE PAGES
    MATCH each P page to its H counterpart by CONTENT ORDER first, filenames second
        (the two tools name pages differently; never pair on filename alone)
    NOTE any page present in one set and not the other — a page-count difference is
        itself a finding (class D, `16B` §2.3)

    # 3 — WALK THE WRITER'S TEMPLATE, NOT THE DIFF
    FOR EACH page:
        FOR EACH writer tag / content block in W that belongs to this page:
            LOCATE what H made of it
            LOCATE what P made of it
            IF they differ → CANDIDATE FINDING (carry the writer tag as evidence)
    THEN sweep for structures present in one output and absent in the other

    # 4 — CLASSIFY AND FILTER   (`16B`)
    FOR EACH candidate, in this order (the tests are exclusive — first match wins):
        1. IF it matches an exclusion (`16B` §5) → DROP silently, but COUNT it
           in its exclusion category for the report's coverage block (`16C` §5)
        2. ELSE IF the origin is genuinely unclear (`16B` §6 — the writer wrote
           something both outputs are renderings of, but which reading is right
           cannot be settled) → HOLD for the "For Gavin to judge" section
        3. ELSE assign a class A–E (`16B` §1) and a confidence (`16C` §2.2)

    # 5 — CHECK EVERY ACTIVITY AND INTERACTIVE BOUNDARY   (`16B` §3)
    FOR EACH activity box and each interactive in W:
        COMPARE the content assigned to it in H vs in P
        REPORT spill (P ends it too early) and swallow (P ends it too late)
        (regardless of built state, and regardless of complexity)

    # 6 — WRITE THE ONE REPORT   (`16C`)
    NUMBER the findings continuously, ordered by class then page
    BUILD the report file, SAVE it, PRESENT it
    CLOSE with a short plain-English summary for the tester
```

---

## 7. TONE + INTERACTION

The tester is a developer running a test, not a designer awaiting instructions. Keep the chat
reply short: what was compared, how many findings by class, anything that could not be checked
(and why), then the file. Do not paste the findings into the chat — they live in the report.

Ask a question only when an input is genuinely missing or the chat is the wrong one. Otherwise
compare and report.

**Never** offer to fix the PageForge files, convert the module again, or build the interactives as
part of this mode — those are Modes 1 and 6, and mixing them in destroys the report's provenance.
