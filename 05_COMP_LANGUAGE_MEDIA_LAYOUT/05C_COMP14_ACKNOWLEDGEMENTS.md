> **Last updated:** Thursday, 13th August, 2026
> **Granular part C (3 of 4) of `05_COMP_LANGUAGE_MEDIA_LAYOUT.md`** — COMP_14 acknowledgements.
> All sibling parts live in `05_COMP_LANGUAGE_MEDIA_LAYOUT/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## Acknowledgements

> ⚠️ **PLACEMENT — READ FIRST:** The acknowledgements block is **ALWAYS placed at the bottom of the FIRST page of the module — the overview page (`-00`, i.e. lesson 0.0).** It sits **after (outside) the `#footer` `<div>`**, at the very end of the page, using the accordion structure shown below.
>
> Acknowledgements are **NEVER** placed on the last page or on any other lesson page. This is a firm rule for **every** conversion — PageForge, raw Writers Template `.docx`, and MTK alike. If a Mode B reference module carries its acknowledgements on its last page (an older convention), do **not** copy that placement: take the accordion *structure* from the reference but position the populated block at the bottom of the new module's overview page.

### Basic block (wrapper)

The acknowledgements wrapper is **`<div class="acks acksTemplate">`** — the `acksTemplate` modifier is now the standard. When the module uses **AI-generated media** (e.g. CoPilot/DALL·E images), add the `acksAI` modifier as well → **`<div class="acks acksTemplate acksAI">`**.

```html
<div class="acks acksTemplate">
    <div class="accordion">
        <div class="accHead"><h4>Acknowledgements</h4></div>
        <div class="accContent">
            <!-- acksLesson blocks -->
        </div>
    </div>
</div>
```

**With AI-generated media:** add the `acksAI` modifier in addition to `acksTemplate` → `<div class="acks acksTemplate acksAI">`. Use `acksAI` whenever the module includes any AI-generated image or asset (e.g. CoPilot/DALL·E); otherwise the wrapper is simply `<div class="acks acksTemplate">`.

**⚠️ CRITICAL — A REQUESTED AI asset counts, even though it does not exist yet (constraint 72).** The `acksAI` test is about what the **finished module will contain**, not what exists at conversion time. A conversion can never see an asset that a later CS request will produce, so the condition is read **forward**: where the writer has **requested** an AI-generated asset — typically a red-text CS instruction such as *"CS: could you create an image for this please?"* — apply `acksAI` **in anticipation**:

```html
<div class="acks acksTemplate acksAI">
```

and pair it with a visible note recording that the asset is pending:

```html
<p style="color: red; font-weight: bold;">Designer/Developer To Do: create the requested AI image and add its acknowledgement entry. The acks wrapper already carries acksAI in anticipation.</p>
```

The prefix is **`Designer/Developer To Do:`** — the pattern is correctly built and only the asset is pending (constraint 59), which is exactly this prefix's remit; it is not a `Red Flag:`.

**Which requests count:** any writer request for an asset that will be **AI-generated** (CoPilot / DALL·E / equivalent). A request for a *non*-AI asset (a photograph to source, a CS-drawn diagram, an Audiovisual video) does **not** trigger `acksAI` — it gets its own `Designer/Developer To Do:` note without the modifier. Where the writer's request does not make the production method clear, **apply `acksAI` and say so in the note** — the modifier is trivially removable by the designer if the asset turns out to be hand-made, whereas a missing `acksAI` on a shipped AI asset is a compliance miss. If the designer ultimately creates the asset by other means, they drop the modifier.

### Accordion structure — at the bottom of the overview page (lesson 0.0)

This is the form to generate. Place it after the `#footer` `<div>` on the overview (`-00`) page, inside a standard `row` → `col-md-8 col-12`:

```html
    </div><!-- #footer -->

    <!-- Acknowledgements — bottom of the overview page (lesson 0.0), after the footer -->
    <div class="row">
        <div class="col-md-8 col-12">
            <div class="acks acksTemplate">
                <div class="accordion">
                    <div class="accHead"><h4>Acknowledgements</h4></div>
                    <div class="accContent">
                        <div class="acksLesson">
                            <p><i>Every effort has been made to acknowledge and contact copyright holders. Te Aho o Te Kura Pounamu apologises for any omissions and welcomes more accurate information.</i></p>
                        </div>
                        <div class="acksLesson"><!-- Lesson 0.0 -->
                            <p>Image: Cover image from <i>We Belong</i>, illustrations by Stevie Mahardhika, from <i>Ready to Read Phonics Plus</i>, Ministry of Education © Crown copyright, <a href="https://newzealandcurriculum.tahurangi.education.govt.nz/we-belong---r-kau/5637164991.p" target="_blank">https://newzealandcurriculum.tahurangi.education.govt.nz/we-belong---r-kau/5637164991.p</a>. Adapted. Creative Commons Attribution-NonCommercial 4.0 Licence.</p>
                            <p>Story: <i>We Belong</i>, words by Maggie Boston and Jennifer Smith, illustrations by Stevie Mahardhika, <i>Ready to Read Phonics Plus</i>, Ministry of Education © Crown copyright, <a href="https://newzealandcurriculum.tahurangi.education.govt.nz/we-belong---r-kau/5637164991.p" target="_blank">https://newzealandcurriculum.tahurangi.education.govt.nz/we-belong---r-kau/5637164991.p</a>. Creative Commons Attribution-NonCommercial 4.0 Licence.</p>
                        </div>
                        <div class="acksLesson"><!-- Lesson 1.0 (example: a page of stock photos) -->
                            <p>Photo: The historic stone bridge over the Karaisalı Kapıkaya Canyon, iStock 2241375863, Getty Images. Used with permission.</p>
                            <p>Photo: Parade float in Nice, France, Shutterstock 2581191123, Shutterstock Images LLC, USA. Used with permission.</p>
                            <p>Illustration: 3D two Party popper, iStock 1461683255, Getty Images. Used with permission.</p>
                        </div>
                        <!-- one acksLesson div per page in the module, in order: Lesson 0.0, Lesson 1.0, Lesson 2.0, … -->
                        <div class="acksLesson">
                            <p>All other images © Te Aho o Te Kura Pounamu, Wellington, New Zealand.</p>
                        </div>
                        <div class="acksLesson">
                            <p><i>Copyright © <span class="currentYear"></span> Board of Trustees of Te Aho o Te Kura Pounamu, Private Bag 39992, Wellington Mail Centre, Lower Hutt 5045, New Zealand. All rights reserved. No part of this publication may be reproduced or transmitted in any form or by any means without the written permission of Te Aho o Te Kura Pounamu.</i></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
```

**Structure notes:**
- Wrapper is `<div class="acks acksTemplate">` (the `acksTemplate` modifier is standard); add `acksAI` as well — `<div class="acks acksTemplate acksAI">` — when the module uses AI-generated media.
- The whole module's acknowledgements live in this single block on page 0.0 — one `acksLesson` div per page of the module (0.0, 1.0, 2.0, …), in order, so every lesson's media is credited even though the block itself only appears on the first page.
- **The page-label annotation reads `Lesson N.N`, never `Page N.N` (constraint 73).** Each media-carrying `acksLesson` div opens with a comment naming the page it covers, worded **`<!-- Lesson 0.0 -->`, `<!-- Lesson 1.0 -->`, `<!-- Lesson 2.0 -->`, …** — matching the `acksLesson` class name and the way the team refers to the pages. Do **not** write `<!-- Page N.N -->`. This annotation is a **permitted comment exception** (see `02_DATA_CONTENT_VERIFICATION.md` → Comment & Red Flag Policy → The permitted comment exceptions, and `00` constraint 37): it is a structural grouping label for the developer and carries **no** student content, designer-action note, ambiguity, or interactive answer — anything of that kind still goes in a visible red note. The three standard boilerplate divs (the opening apology, the "All other images ©…" line, and the closing Te Kura copyright) carry **no** label comment, since they belong to no single page.
- The opening apology line, the "All other images © Te Aho o Te Kura Pounamu, Wellington, New Zealand." line, and the closing Te Kura copyright line (with `<span class="currentYear"></span>`) are standard — include all three.

### Entry format

Each entry is a `<p>` that begins with the asset **type prefix**, then the asset's **published title**, then the source/credit, then the licence or permission string. Match these patterns:

| Asset kind | Entry pattern |
|---|---|
| Stock photo (iStock / Getty) | `Photo: [published title], iStock [ID], Getty Images. Used with permission.` |
| Stock photo (Shutterstock) | `Photo: [published title], Shutterstock [ID], Shutterstock Images LLC, USA. Used with permission.` |
| Vector / cartoon illustration | `Illustration: [published title], iStock [ID], Getty Images. Used with permission.` |
| Book / journal cover image | `Image: Cover image from <i>[Title]</i>, illustrations by [illustrator], from <i>[Series]</i>, Ministry of Education © Crown copyright, [wrapped URL]. Adapted. Creative Commons Attribution-NonCommercial 4.0 Licence.` |
| Story / journal text | `Story: <i>[Title]</i>, words by [author], illustrations by [illustrator], <i>[Series]</i>, Ministry of Education © Crown copyright, [wrapped URL]. Creative Commons Attribution-NonCommercial 4.0 Licence.` |
| Video (YouTube) | `Video: [title], [author], <a href="[URL]" target="_blank">[URL]</a>, retrieved d/m/y. Used in online learning within the exception for education.` |

- **Italics:** story, journal, and book-series titles are italicised (`<i>…</i>`). Photo and illustration published titles are not italicised.
- **Published title verbatim — including a trailing ". stock photo" (constraint 66).** The entry title is the asset's **official published title exactly as it appears on the platform** — sentence casing, internal punctuation, and any trailing **". stock photo"** suffix included when it is part of the official iStock title (e.g. iStock 1137701281's official title is *"Tourist visiting lake Wanaka, New Zealand. stock photo"* — the acks entry keeps the suffix: `Photo: Tourist visiting lake Wanaka, New Zealand. stock photo, iStock 1137701281, Getty Images. Used with permission.`). **Never strip, re-case, re-punctuate, or title-case the published title**, and never drop the suffix because of the alt-text rule — the "no *stock photo*" prohibition applies to **alt text only** (constraint 52), where a brief description for screen readers rightly drops platform-title suffixes; the acknowledgements cite the title as published.
- **iStock ID consistency (constraint 61).** The `iStock [ID]` cited in a Photo / Illustration entry is the **`gm`-leading number** from the asset URL — the platform's **"Stock photo ID"** — and is **identical** to the number used in the `images/iStock-{ID}.jpg` filename for that asset. For a dual-ID URL (`gm{A}-{B}`, e.g. `gm2194652495-612793002`) the cited ID is **`A`** (`2194652495`); the trailing `B` is never cited. Filename and acks citation must always carry the **same** ID. See `01_PIPELINE_EXTRACTION_TAGS.md` → Images (filename construction).
- **Story bylines** (`words by …`, `illustrations by …`) and the series/journal name are part of every story and cover entry. These names are **not** in the media list — they come from the cited source page's metadata. If a byline cannot be confirmed from the supplied materials, raise a VISIBLE red flag (`<p style="color: red; font-weight: bold;">Red Flag: …</p>`) for the developer to supply it — never invent an author/illustrator name and never emit a thin entry that omits the byline. (An unconfirmed byline is a Convertor-detected gap, so it takes the `Red Flag:` prefix; see `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes.)
- **Video entries (YouTube).** Use the full layout: `Video: [title], [author], <a href="[URL]" target="_blank">[URL]</a>, retrieved d/m/y. Used in online learning within the exception for education.`
  - **`[title]` and `[author]`** — the video's real title and the channel/author. **The title is ALWAYS the video's full published title** (the title as it appears on the video itself). The **Media List `Description` column is NOT authoritative for video titles** — writers routinely abbreviate it, get it wrong, or invent a label from their own description of what the video is about. Where the Media List label and the published title differ, the **published title wins**; the Media List is a locating aid (it tells you *which* video), not a source of title text. If the full published title cannot be confirmed from the supplied materials, raise a VISIBLE red flag — do not fall back to the Media List label and do not invent one. Likewise, if the author cannot be confirmed, raise a VISIBLE red flag — do not invent it.
  - **Wrapped link** — the watch URL is a **live anchor** (`<a href="…" target="_blank">…</a>`), consistent with the URL-wrapping rule below; the trailing comma sits outside the closing `</a>`.
  - **`retrieved d/m/y`** — the **date the conversion is processed** (i.e. today's date when the HTML is generated), written `d/m/y` (e.g. `18/6/2026`). It is *not* the video's upload date.
  - **Permission string** — always `Used in online learning within the exception for education.` for YouTube videos.
  - Example: `<p>Video: How volcanoes work, GNS Science, <a href="https://www.youtube.com/watch?v=XXXXXXXXXXX" target="_blank">https://www.youtube.com/watch?v=XXXXXXXXXXX</a>, retrieved 18/6/2026. Used in online learning within the exception for education.</p>`

### URL wrapping — every acks URL is a link (Template rule)

**Every URL that appears in an acknowledgement entry must be wrapped in `<a href="URL" target="_blank">URL</a>` — not just video URLs.** Designers often wrap only video links for speed; that is a shortcut, not the standard. The supplied human-built reference pages (`BLL246_0_0.html`, `BLL246-Correct-Acks.html`) show acks URLs as plain text — that reflects the common designer shortcut and is the exact behaviour this rule corrects, so do **not** copy the plain-text URLs from those references. The anchor text is the URL itself (so the link stays visible), and any sentence punctuation (the trailing full stop) sits **outside** the closing `</a>`. Entries cited by ID alone (iStock / Shutterstock photos) carry no URL and need no anchor.

### Sourcing the acknowledgement entries

Build the entries from the module's external media:

- **Media List as the inventory.** When a Media List is supplied (see `01_PIPELINE_EXTRACTION_TAGS.md` → Media List Companion Document), use it to confirm you have captured **every** external item, to assign each item to the correct page via its `WTPg No.` column, and to read each item's provider, ID, and URL. The Media List's `Description` column is a writer-descriptive label (e.g. *"Stock photo of a car driving across a narrow bridge"*) — it is **not** the acks title. **This holds for videos too:** a video's acks title is its **full published title**, never the Media List label (see the Video entries bullet under Entry format).
- **iStock acknowledgements file is authoritative (verbatim).** When a developer supplies an **iStock acknowledgements file** (a list of acks lines pulled directly from the iStock/Getty API — see `01_PIPELINE_EXTRACTION_TAGS.md` → iStock Acknowledgements File), those lines are **perfectly accurate and used exactly as written.** When the lesson-ordered acks build reaches an iStock image, **insert the matching line from that list verbatim** — match by iStock ID (and/or the descriptive name), do **not** re-derive the title from the URL slug, do **not** reword or reformat, and place it under the `acksLesson` div for the page on which the image is used. This takes precedence over the URL-slug derivation below for the items it covers. (Non-iStock items, and any iStock image with no matching line, still follow the normal routes — for a missing line, red-flag for the developer rather than inventing an entry.)
- **Use the asset's published title, not the media-list description — and use it exactly as published (constraint 66).** For iStock / Shutterstock photos and illustrations the published title is normally recoverable from the asset URL slug (e.g. `…/photo/the-historic-stone-bridge-over-the-karaisalı-kapıkaya-canyon.jpg` → *The historic stone bridge over the Karaisalı Kapıkaya Canyon*). A slug is an **approximation** — it loses the official title's casing, punctuation, and any trailing ". stock photo" suffix — so wherever the official published title is available (the iStock acknowledgements file, or the asset page itself), that exact form wins verbatim, suffix included; do not title-case a slug-derived title beyond its natural sentence form, and never "correct" the official title. Use the media-list description only as a fallback hint when no published title is available. *(When an iStock acknowledgements file is supplied, prefer its verbatim line over slug derivation — see the bullet above.)*
- **Shutterstock items with an iStock replacement.** When the Media List's *Shutterstock replacement image* column gives an iStock alternative, credit the licensed / replacement asset — its published title, iStock ID, and Getty Images — per the designer convention. Otherwise credit the listed source (`Shutterstock [ID], Shutterstock Images LLC, USA`).
- **If no Media List was supplied:** derive entries from the `[image]` / `[video]` references in the content source itself. Where a title or byline is unavailable, raise a VISIBLE red flag for the developer to complete — not a hidden HTML comment.
- **Group** entries under the `acksLesson` div for the page on which they appear, in page order.

**Acknowledgement requirement (cultural alerts):** When the module uses cultural alerts, the acknowledgements block on page 0.0 MUST include the required cultural-alert credit line (see the Cultural Alerts section earlier in this file).