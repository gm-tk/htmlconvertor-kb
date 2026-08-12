> **Last updated:** Thursday, 13th August, 2026
> **Granular part D (4 of 4) of `07_MTK_DOCX_CONVERSION.md`** — MTK: embedded HTML skeletons (SS19).
> All sibling parts live in `07_MTK_DOCX_CONVERSION/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 19. EMBEDDED HTML SKELETONS

These are the complete, self-contained HTML skeletons for MTK module pages. Use these directly — no reference HTML files are required. Replace placeholder tokens with actual values:

- `{MODULE_CODE}` — e.g., `TRR108`
- `{MAORI_TITLE}` — e.g., `Ngā Orokati Tuarua`
- `{ENGLISH_TITLE}` — e.g., `Final Consonants`
- `{PAGE_NUMBER}` — e.g., `0.0`, `1.0`, `2.0`
- `{LESSON_NUMBER}` — e.g., `1.0`, `2.0` (used in `#module-code` on lesson pages)

### 19.1 Overview Page Skeleton (5-Tab Variant)

```html
<!doctype html>
<html lang="en" level="" template="1-3" class="notranslate" translate="no">
<head>
    <meta charset="utf-8" />
    <meta content="IE=edge" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <title>{MODULE_CODE} 0.0</title>
    <script type="text/javascript" src="https://tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js"></script>
</head>

<body class="container-fluid reoTranslate" language="reo" translation="eng">
    <div id="header">
        <div id="module-code">
            <h1>{MODULE_CODE}</h1>
        </div>
        <h1><span>{MAORI_TITLE}</span></h1>
        <h1><span>{ENGLISH_TITLE}</span></h1>
        <div id="module-head-buttons">
            <div id="module-menu-button" class="circle-button btn1"></div>
        </div>
        <div id="module-menu-content" class="moduleMenu">
            <div class="row">
                <div class="tabs col-12">
                    <ul class="nav nav-tabs">
                        <li><a><span reo>Tirohanga whānui</span><span eng>Overview</span></a></li>
                        <li><a><span reo>Whenu</span><span eng>Strand</span></a></li>
                        <li><a><span reo>Toi mokopuna</span><span eng>Dispositions</span></a></li>
                        <li><a><span reo>Ngā whāinga matua</span><span eng>Key objectives</span></a></li>
                        <li><a><span reo>Kia mataara</span><span eng>Information</span></a></li>
                    </ul>
                    <div class="tab-content">

                        <!-- ======= Tab 1: Tirohanga whānui / Overview ======= -->
                        <div class="tab-pane">
                            <div class="row">
                                <div class="col-md-8 col-12">
                                    <!-- {OVERVIEW_TAB_CONTENT} -->
                                </div>
                            </div>
                        </div>

                        <!-- ======= Tab 2: Whenu / Strand ======= -->
                        <div class="tab-pane">
                            <div class="row">
                                <div class="col-md-8 col-12">
                                    <!-- {STRAND_TAB_CONTENT} -->
                                </div>
                            </div>
                        </div>

                        <!-- ======= Tab 3: Toi mokopuna / Dispositions ======= -->
                        <div class="tab-pane">
                            <div class="row">
                                <div class="col-md-8 col-12">
                                    <!-- {DISPOSITIONS_TAB_CONTENT} -->
                                </div>
                            </div>
                        </div>

                        <!-- ======= Tab 4: Ngā whāinga matua / Key objectives ======= -->
                        <div class="tab-pane">
                            <div class="row">
                                <div class="col-md-8 col-12">
                                    <!-- {KEY_OBJECTIVES_TAB_CONTENT} -->
                                    <!-- In 5-tab modules, this tab also contains Critical Point content -->
                                </div>
                            </div>
                        </div>

                        <!-- ======= Tab 5: Kia mataara / Information (Learning Intentions two-column) ======= -->
                        <div class="tab-pane">
                            <div class="row">
                                <div class="col-md-6 offset-md-0 col-12 paddingR">
                                    <h4 reo><span>Ngā Whainga Ako</span></h4>
                                    <h4 eng><span>Learning Intentions</span></h4>
                                    <h5 reo>Ka taea e au te:</h5>
                                    <h5 eng>I can:</h5>
                                    <ul reo>
                                        <!-- {LEARNING_INTENTIONS_ITEMS_REO} -->
                                    </ul>
                                    <ul eng>
                                        <!-- {LEARNING_INTENTIONS_ITEMS_ENG} -->
                                    </ul>

                                    <h4 reo><span>Paeru Angitu:</span></h4>
                                    <h4 eng><span>Success Criteria</span></h4>
                                    <h5 reo>Ka taea e au te:</h5>
                                    <h5 eng>I can:</h5>
                                    <ul reo>
                                        <!-- {SUCCESS_CRITERIA_ITEMS_REO} -->
                                    </ul>
                                    <ul eng>
                                        <!-- {SUCCESS_CRITERIA_ITEMS_ENG} -->
                                    </ul>
                                </div>
                                <div class="col-md-6 offset-md-0 col-12 paddingL">
                                    <h5 reo>Whakamaheretia tō wā:</h5>
                                    <h5 eng>Planning your time</h5>
                                    <!-- {PLANNING_TIME_CONTENT} -->

                                    <h5 reo>He aha tāku hei tīmata?</h5>
                                    <h5 eng>What do I need to get started?</h5>
                                    <ul reo>
                                        <!-- {CHECKLIST_ITEMS_REO} -->
                                    </ul>
                                    <ul eng>
                                        <!-- {CHECKLIST_ITEMS_ENG} -->
                                    </ul>

                                    <h5 reo>Ngā hononga</h5>
                                    <h5 eng>Connections</h5>
                                    <!-- {CONNECTIONS_CONTENT} -->
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="body">
        <!-- {OVERVIEW_BODY_CONTENT} -->
        <!-- Typically: course code h1, Module Introduction h2, paragraphs, whakatauki, karakia -->
    </div>

    <div id="footer">
        <ul class="footer-nav">
            <li><a href="" id="next-lesson" target="_self"></a></li>
            <li><a href="" class="home-nav" target="_parent"></a></li>
        </ul>
    </div>

    <!-- Acknowledgements — AFTER the footer, at the bottom of the OVERVIEW page (0.0) -->
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
                            <!-- {ACKS_PAGE_0} -->
                        </div>
                        <div class="acksLesson"><!-- Lesson 1.0 -->
                            <!-- {ACKS_PAGE_1} -->
                        </div>
                        <!-- One acksLesson div per page in the module -->
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
</body>
</html>
```

### 19.2 Overview Page Skeleton (6-Tab Variant)

Identical to the 5-tab skeleton above (including the acknowledgements accordion after the footer) except the `<ul class="nav nav-tabs">` has 6 tabs and the tab-content has 6 `<div class="tab-pane">` sections:

```html
<!-- Replace the nav-tabs section with: -->
<ul class="nav nav-tabs">
    <li><a><span reo>Tirohanga whānui</span><span eng>Overview</span></a></li>
    <li><a><span reo>Whenu</span><span eng>Strand</span></a></li>
    <li><a><span reo>Toi mokopuna</span><span eng>Dispositions</span></a></li>
    <li><a><span reo>Ngā Whāinga Matua</span><span eng>Key objectives</span></a></li>
    <li><a><span reo>Kia Mataara</span><span eng>Critical Point of Learning</span></a></li>
    <li><a><span reo>Ngā Whainga Ako</span><span eng>Learning Intentions</span></a></li>
</ul>
```

In the 6-tab variant:
- Tab 4 contains ONLY Key Objectives content (no Critical Point)
- Tab 5 contains ONLY Critical Point content
- Tab 6 contains the Learning Intentions two-column layout (same structure as Tab 5 in the 5-tab variant)

### 19.3 Lesson Page Skeleton (Middle Page)

```html
<!doctype html>
<html lang="en" level="" template="1-3" class="notranslate" translate="no">
<head>
    <meta charset="utf-8" />
    <meta content="IE=edge" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <title>{MODULE_CODE} {PAGE_NUMBER}</title>
    <script type="text/javascript" src="https://tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js"></script>
</head>

<body class="container-fluid reoTranslate" language="reo" translation="eng">
    <div id="header">
        <div id="module-code">
            <h1>{LESSON_NUMBER}</h1>
        </div>
        <h1><span>{MAORI_TITLE}</span></h1>
        <h1><span>{ENGLISH_TITLE}</span></h1>
    </div>

    <div id="body">
        <!-- Lesson heading -->
        <div class="row">
            <div class="col-md-8 col-12">
                <h2 reo>{MAORI_LESSON_HEADING}</h2>
                <h2 eng>{ENGLISH_LESSON_HEADING}</h2>
            </div>
        </div>

        <!-- Activities go here, each wrapped in: -->
        <!--
        <div class="row">
            <div class="col-md-8 col-12">
                <div class="activity interactive" number="N.N">
                    <div class="row">
                        <div class="col-12">
                            ... activity content ...
                        </div>
                    </div>
                </div>
            </div>
        </div>
        -->

        <!-- Alerts, "Finished!", "What have I learned?" sections between activities -->

    </div>

    <div id="footer">
        <ul class="footer-nav">
            <li><a href="" id="prev-lesson" target="_self"></a></li>
            <li><a href="" id="next-lesson" target="_self"></a></li>
            <li><a href="" class="home-nav" target="_parent"></a></li>
        </ul>
    </div>
</body>
</html>
```

### 19.4 Lesson Page Skeleton (Final Lesson Page)

The final lesson page is structurally the same as a middle lesson page; the only difference is the footer omits the `next-lesson` link. **The acknowledgements accordion is NOT placed here** — it lives at the bottom of the overview page (0.0). See skeleton 19.1.

```html
<!doctype html>
<html lang="en" level="" template="1-3" class="notranslate" translate="no">
<head>
    <meta charset="utf-8" />
    <meta content="IE=edge" http-equiv="X-UA-Compatible" />
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <title>{MODULE_CODE} {PAGE_NUMBER}</title>
    <script type="text/javascript" src="https://tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js"></script>
</head>

<body class="container-fluid reoTranslate" language="reo" translation="eng">
    <div id="header">
        <div id="module-code">
            <h1>{LESSON_NUMBER}</h1>
        </div>
        <h1><span>{MAORI_TITLE}</span></h1>
        <h1><span>{ENGLISH_TITLE}</span></h1>
    </div>

    <div id="body">
        <!-- Lesson heading -->
        <div class="row">
            <div class="col-md-8 col-12">
                <h2 reo>{MAORI_LESSON_HEADING}</h2>
                <h2 eng>{ENGLISH_LESSON_HEADING}</h2>
            </div>
        </div>

        <!-- Activities, alerts, completion sections -->

        <!-- Karakia Whakakapi (closing prayer) — if present -->
        <!--
        <div class="row">
            <div class="col-md-8 col-12">
                <h3 reo>Karakia Whakakapi</h3>
                <h3 eng>Karakia Whakakapi</h3>
                ... video/audio/text ...
            </div>
        </div>
        -->

    </div>

    <div id="footer">
        <ul class="footer-nav">
            <li><a href="" id="prev-lesson" target="_self"></a></li>
            <li><a href="" class="home-nav" target="_parent"></a></li>
        </ul>
    </div>
    <!-- NO acknowledgements here — the acknowledgements accordion is on the overview page (0.0), skeleton 19.1 -->
</body>
</html>
```

### 19.5 Key Structural Notes for All Skeletons

1. **`<!doctype html>`** — lowercase, per project convention.
2. **Self-closing void elements** — use XHTML-style: `<meta ... />`, `<br />`, `<img ... />`.
3. **Script URL is fixed** — `https://tekura.desire2learn.com/shared/refresh_template/js/idoc_scripts.js` — identical across all TRR modules.
4. **No jQuery, no stickyNav.js** — MTK modules do not use these.
5. **No custom CSS links** — MTK modules rely solely on the shared template CSS loaded by `idoc_scripts.js`.
6. **Body content grid** — all body content sits inside `<div class="row"><div class="col-md-8 col-12">...</div></div>` wrappers (unless a side alert changes the column width).
7. **Titles in `<h1><span>` — Māori first, English second.** On the **overview** page these are the **module** titles. On a **lesson** page the `<h1><span>` carries **that lesson's own title** (constraint 79 — universal, MTK included); the module title belongs to the overview, and a second `<h1><span>` appears on a lesson page only where the writer gave that lesson its own bilingual name. *(The former "module titles on both overview and lesson pages" wording is superseded by constraint 79 / `CL-0069`.)*
8. **Footer href values** — leave empty (`href=""`); the template JS resolves navigation automatically.