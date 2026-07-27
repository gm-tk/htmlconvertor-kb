> **Last updated:** Thursday, 16th July, 2026 9:30 PM
> **Granular part C (3 of 4) of `07_MTK_DOCX_CONVERSION.md`** — MTK: header, footer, acks, word/image, Kiwi Kaiarahi, checklist, pitfalls (SS12-18).
> All sibling parts live in `07_MTK_DOCX_CONVERSION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 12. HEADER CONSTRUCTION

### Overview Page (0.0)

```html
<div id="header">
    <div id="module-code">
        <h1>{MODULE_CODE}</h1>
    </div>
    <h1><span>{MAORI_TITLE}</span></h1>
    <h1><span>{ENGLISH_TITLE}</span></h1>
    <div id="module-head-buttons">
        <div id="module-menu-button" class="circle-button btn1"></div>
    </div>
    <!-- Module menu content here -->
</div>
```

### Lesson Pages (1.0, 2.0, etc.)

```html
<div id="header">
    <div id="module-code">
        <h1>{LESSON_NUMBER}</h1>
    </div>
    <h1><span>{MAORI_TITLE}</span></h1>
    <h1><span>{ENGLISH_TITLE}</span></h1>
</div>
```

**No menu button or menu content on lesson pages.**

### Title Extraction from Metadata

The module code line in the metadata table follows patterns such as:
```
TRR108: Ngā Orokati Tuarua – Final Consonants
```

Extract the module code before the colon/dash, then split the title portion. The Māori title typically comes first, followed by a dash or separator, then the English title.

---

## 13. FOOTER CONSTRUCTION

### Overview Page
```html
<div id="footer">
    <ul class="footer-nav">
        <li><a href="" id="next-lesson" target="_self"></a></li>
        <li><a href="" class="home-nav" target="_parent"></a></li>
    </ul>
</div>
```

### Middle Lesson Pages
```html
<div id="footer">
    <ul class="footer-nav">
        <li><a href="" id="prev-lesson" target="_self"></a></li>
        <li><a href="" id="next-lesson" target="_self"></a></li>
        <li><a href="" class="home-nav" target="_parent"></a></li>
    </ul>
</div>
```

### Final Lesson Page
```html
<div id="footer">
    <ul class="footer-nav">
        <li><a href="" id="prev-lesson" target="_self"></a></li>
        <li><a href="" class="home-nav" target="_parent"></a></li>
    </ul>
</div>
```

The acknowledgements accordion goes AFTER the footer **on the overview page (page 0.0)** — never on the last lesson page.

---

## 14. ACKNOWLEDGEMENTS STRUCTURE

> ⚠️ **PLACEMENT:** The acknowledgements accordion is placed at the bottom of the **overview page (page 0.0)**, AFTER the `#footer` `<div>`. It is NEVER placed on the last lesson page. The block covers the whole module (one `acksLesson` div per page), but it only ever appears once — on page 0.0.
>
> **Sourcing:** If a Media List `.docx` was supplied, build the entries from it (descriptions, sources, URLs, and the `WTPg No.` column to assign items to the correct page). Otherwise derive entries from the `[image]`/`[video]` references in the writer template.

```html
<div class="row">
    <div class="col-md-8 col-12">
        <div class="acks">
            <div class="accordion">
                <div class="accHead">
                    <h4>Acknowledgements</h4>
                </div>
                <div class="accContent">
                    <div class="acksLesson">
                        <p><i>Every effort has been made to acknowledge and contact copyright holders. Te Aho o Te Kura Pounamu apologises for any omissions and welcomes more accurate information.</i></p>
                    </div>
                    <div class="acksLesson"><!-- Lesson 0.0 -->
                        <p>Attribution text...</p>
                    </div>
                    <div class="acksLesson"><!-- Lesson 1.0 -->
                        <p>Attribution text...</p>
                    </div>
                    <!-- One acksLesson div per page -->
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

---

## 15. WORD/IMAGE DISPLAY PATTERN

A recurring pattern in these modules shows words with associated images in a grid. The writer specifies bold words with image references:

```
**ikarangi** [Item 3] [Image] [galaxy](URL)
**putiputi** [Item 4] [Image] [flower](URL)
```

This maps to a table-in-grid layout:
```html
<div class="row">
    <div class="col-md-6 col-12 paddingLR">
        <div class="table-responsive">
            <table class="table table-bordered align-middle">
                <tr>
                    <td><img class="img-fluid" src="images/..." alt="..." /></td>
                </tr>
                <tr>
                    <td class="rowSolid">
                        <p reo style="text-align: center; margin-bottom:0em; color:white;">ikarangi</p>
                        <p eng style="text-align: center; margin-bottom:0em; color:white;">ikarangi</p>
                    </td>
                </tr>
            </table>
        </div>
    </div>
    <!-- Repeat for each word/image pair -->
</div>
```

**Note:** The word label row uses `rowSolid` class (dark background) with white text. When the word is the same in both languages (as with Māori vocabulary), both `reo` and `eng` paragraphs contain the same text.

---

## 16. KIWI KAIĀRAHI (LEARNING GUIDE) PATTERN

Multiple modules include a break activity referencing "Te rōpū ako o te kiwi" (The kiwi group's learning guide). This uses a standard activity wrapper with an image + button link to a PDF:

```html
<div class="activity" number="N.N">
    <div class="row">
        <div class="col-12">
            <h3 reo>Te rōpū ako o te kiwi</h3>
            <h3 eng>The kiwi group's learning guide</h3>
            <p reo>Break text in Māori...</p>
            <p eng>Break text in English...</p>
            <img class="img-fluid" loading="lazy" src="images/.../Nga_Kiwi_Kaiarahi_Front.jpg" alt="Ngā Kiwi Kaiārahi" />
            <a eng href="QUICKLINK_URL" target="_blank"><div class="button">Go to Ngā Kiwi kaiārahi</div></a>
            <a reo href="QUICKLINK_URL" target="_blank"><div class="button">Haere ki Ngā Kiwi kaiārahi</div></a>
        </div>
    </div>
</div>
```

---

## 17. CONVERSION CHECKLIST (MTK Docx-to-HTML)

Before starting:
- [ ] Confirm module code (TRR1XX) from metadata table
- [ ] Extract Māori and English module titles from metadata
- [ ] Identify page count from `[End Page]` markers and lesson headers
- [ ] Determine tab count (5 or 6) from menu section structure
- [ ] Identify all interactive components from activity descriptions
- [ ] Catalogue all `[Item N]` media references
- [ ] Image output mode (Mode P or Mode D) confirmed with user before generating HTML
- [ ] Select the appropriate skeleton from Section 19

For each page:
- [ ] Correct `<title>` element (module code + page number)
- [ ] Correct `#module-code` content
- [ ] Correct `<h1><span>` titles (Māori then English)
- [ ] All bilingual content uses `reo`/`eng` attributes
- [ ] All paragraphs split into proper `<p reo>` / `<p eng>` pairs
- [ ] No `<span>` wrappers on body headings (h2–h5)
- [ ] Activity numbers use decimal format (1.1, not 1A)
- [ ] Interactive components follow documented patterns (COMP files)
- [ ] Buttons have both `reo` and `eng` variants
- [ ] Image output mode applied consistently to all images in the file
- [ ] Media placeholders have CS comments with item numbers
- [ ] Audio filenames have no spaces
- [ ] Div tags are balanced

Final verification:
- [ ] Overview menu has correct tab count with all content
- [ ] All student-facing content is visible HTML (no content hidden in comments only)
- [ ] Footer navigation is correct for page position
- [ ] Acknowledgements accordion is at the bottom of the OVERVIEW page (0.0), after the footer — NOT on the last lesson page
- [ ] No stale module codes left from copy-paste (e.g., TRR102, TRR104)
- [ ] `template="1-3"` confirmed on `<html>` tag

---

## 18. COMMON PITFALLS

1. **Mixing up English and Māori columns** — Column 1 in the writer's table is ALWAYS English, Column 2 is ALWAYS Māori. But in the HTML, Māori (`reo`) comes FIRST for most elements.

2. **Treating writer CS instructions as student content** — Text in square brackets like `[Please created 5 Accordions]` or `[Creative team- can we have this as a side tab.]` are instructions for Creative Services, not student content. Surface them as VISIBLE red flags (`<p style="color: red; font-weight: bold;">Writers Note: ...</p>`), never as hidden HTML comments and never as student-facing content. (A bracketed CS instruction is the writer's own note, so it takes the `Writers Note:` prefix — see `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes. The MTK `<!-- CS: Item N -->` media-catalogue annotation is the one retained comment exception — see Section 10.)

3. **Forgetting the Māori-first order** — In the `.docx`, English is column 1. But in the HTML output, Māori content (`reo`) typically appears FIRST in the source order (the template CSS handles display based on language toggle).

4. **Applying `sassoonI-text` universally** — The `sassoonI-text` class is specific to the letter "I" modules. Other letter modules may use `sassoon-text` (general) or no special font class at all (e.g., TRR107, TRR108 consonants modules).

5. **Carrying over stale module codes** — When building from skeletons or copy-pasting, ensure ALL `<title>`, `<h1>`, and `#module-code` elements are updated to the new module's values. TRR108's finalized HTML had stale `TRR102` references in `<title>` elements — this is a known human error to avoid.

6. **Treating `[H2]` in menu sections as body headings** — Inside the overview menu tabs, `[H2]` from the writer maps to `<h5>` (not `<h3>`). The `[H2]` → `<h3>` mapping only applies in body content.

7. **Inconsistent activity number formats** — The writer uses letters (1A, 1B, 1C); the preferred HTML format uses decimals (1.1, 1.2, 1.3). Be consistent within a module.

8. **Missing bilingual button variants** — All interactive component buttons should have both `reo` and `eng` variants. TRR108's finalized HTML was missing bilingual buttons on some D&D components — this is an error to avoid.

---

