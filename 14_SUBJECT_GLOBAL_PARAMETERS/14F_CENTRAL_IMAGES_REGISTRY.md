> **Last updated:** Tuesday, 3rd November, 2026 5:48 PM
> **Granular part F (7 of 7) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — §14.16, the central-images registry: every image on the design team's Centralised Images page (`refresh_imageCentral.html`, refreshed 3 November 2026) with the writer tag that asks for it and the exact path it builds. Opened 3 November 2026 (CL-0141) as a new part rather than growing `14E`.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 14.16 The central-images registry — one writer tag per centralised image
**Scope — (c) Universal:** any module whose Writers Template asks for a centralised image by its tag. The family facts that decide *which* image a module uses (the BLLR code ranges, the Tūī phase folder, the HPE phase) stay in each family's section and are restated below only where the tag needs them. Source: the design team's Centralised Images page, `Z:\Development\Online\Templates\Refresh Template - modules\refresh_template_HTML\tools snippets\refresh_imageCentral.html`, refreshed and supplied by Gavin on 3 November 2026 (ADMIN MODE, CL-0141). This registry absorbs the page — it no longer needs to be consulted.

### The rule
- **The tag.** The page's own form is `[Centralised image: <image name>]` (its header: *"[Centralised image: + image name]"*); the other centralised-image wordings in `01` → Tag Taxonomy (`[Central image: …]`, `[Image centralised …]`) are the same request. For almost every image the **name is the image's file name without its extension** (`[Centralised image: HP_Sura_1_phase_1]`, `[Centralised image: kea_3]`, `[Centralised image: bookworm_1a]`); the exceptions — the Technology, disposition and AI-icon names — are listed in their tables below.
- **Matching.** Case is ignored, and a space, an underscore and a hyphen count as the same separator, so `[Centralised image: HP Sura 1 phase 1]` and `[Central image: Aroha 1]` are the same requests as the page's forms. Where two images differ **only** by that separator (the Phase 5 `be_a_communicator` image and the Phase 1–4 `be-a-communicator` disposition), the writer's exact spelling decides; failing that, the module's phase does.
- **Output.** `<img class="img-fluid imageCentral" loading="lazy" src="<path>" alt="<alt>">` with the path **copied character-for-character from the tables** — folder casing, spaces, `&`, the design team's spellings (`congradulations`, `Spacial`, `think_like_a_innovator`) and all. Two families are not `<img>`: the Technology **hats** are `<object>` elements, and the **Phase 1–4 dispositions** are the template's `beAKiwi` div (tables below).
- **Never guessed.** A name the registry does not hold is an ordinary image request (CL-0117's rule, unchanged). A known name asking for a pose or number the store does not hold is a visible `Red Flag:` naming the request — never a constructed filename. Where the tag cannot pick one image on its own (a Tūī with no pose, a default avatar or weather icon described in words, a Technology character with no *head* / *full*), the build follows the row's own instruction and raises a visible `Designer/Developer To Do:` naming what the writer asked for.
- **`alt`.** As listed. Where a family section already sets the `alt` (Tūī *Tui character*, bookworm *Bookworm*, Kea *Kea character*, Science / Maths the character's name) that wins over the page's empty `alt`.
- **Not on the page, unchanged elsewhere.** The page's *Phase 1-4 Languages* panel reads *"Designer note: Content in development"* — the Languages central assets stay those of §14.1 and `14C`. The ENWJ New Zealand map has no tag; §14.10's rule is unchanged.

### Congratulations
| Tag name | Path | `alt` |
|---|---|---|
| `Congradulations animation` | `congradulations/Congradulations animation.gif` | `Congradulations animation` |

The misspelling is the delivered asset's (§14.12) — a writer's correctly spelt *Congratulations animation* asks for the same file; the path is never corrected.

### Default avatars — `Character_assets/`
Tag `[Centralised image: default avatar <description>]`. Ten avatars, `alt=""`: `buns`, `babyface`, `bobgal`, `sweatergal`, `shirtboy`, `hoodieboy`, `froboy`, `jacketgal`, `ladsladslads`, `harrypotter` → `Character_assets/<name>.png`. The page defines no descriptions, so the avatar is built when the description **is** one of the ten names (`[Centralised image: default avatar bobgal]`); any other description raises a `Designer/Developer To Do:` naming it and builds nothing.

### Dispositions
**Phase 5 (NCEA)** — images in `beA-NCEA/`; the tag name is the file name:

| Tag name | Path | `alt` |
|---|---|---|
| `be_a_communicator` | `beA-NCEA/be_a_communicator.png` | `Be a communicator` |
| `be_a_learner` | `beA-NCEA/be_a_learner.png` | `Be a learner` |
| `be_a_thinker` | `beA-NCEA/be_a_thinker.png` | `Be a thinker` |
| `think_like_a_innovator` | `beA-NCEA/think_like_a_innovator.png` | `Think like an innovator` |
| `think_like_a_mathematician` | `beA-NCEA/think_like_a_mathematician.png` | `Think like a mathematician` |
| `think_like_a_scientist` | `beA-NCEA/think_like_a_scientist.png` | `Think like a scientist` |
| `think_like_a_social_scientist` | `beA-NCEA/think_like_a_social_scientist.png` | `Think like a social scientist` |

(The file is `think_like_a_innovator.png` — copy it; *think like an innovator* in a tag asks for the same image.)

**Phases 1–4 (and Combo / FUNdamental)** — not an image: the tag builds the template's disposition div, the same div in every phase (the page shows it under each phase's colour level):

| Tag name | Builds |
|---|---|
| `be-a-communicator` | `<div class="beAKiwi disposition-be-a-communicator"></div>` |
| `be-a-learner` | `<div class="beAKiwi disposition-be-a-learner"></div>` |
| `be-an-innovator` | `<div class="beAKiwi disposition-be-an-innovator"></div>` |
| `be-a-mathematician` | `<div class="beAKiwi disposition-be-a-mathematician"></div>` |
| `be-a-scientist` | `<div class="beAKiwi disposition-be-a-scientist"></div>` |
| `be-a-social-scientist` | `<div class="beAKiwi disposition-be-a-social-scientist"></div>` |

### Technology (Phase 1–4) — folder `technology/` (lower-case)
- **TENZ Design Thinking Process** — eighteen images `technology/TENZ/DTP <Stage> <Colour>.png`, tag `[Centralised image: DTP <Stage> <Colour>]`, `<Stage>` = `Model`, `Notice`, `Empathise`, `Define`, `Ideate`, `Analyse`, `Develop`, `Create`, `Evaluate`; `<Colour>` = `White` or `Blue`. `alt` = `TENZ Design Thinking Process <Stage>` (e.g. `technology/TENZ/DTP Ideate Blue.png`, `alt="TENZ Design Thinking Process Ideate"`).
- **Mātauranga Māori connection** — `[Centralised image: Matauranga maori connection]` → `technology/Matauranga maori connection iStock-2243541508.svg`, `alt="Matauranga maori connection"`. Acknowledgement line (supplied): `Illustration: Curled Fern Frond in Minimalist Vector Style, iStock 2243541508, Getty Images. Used with permission.` The page's example places it in an `alert` headed *Mātauranga Māori connection*, the picture in a `col-md-4 offset-md-4 col-12 paddingL` column under the text.
- **Technology characters** — Jo, Tina, Charlie, each a head and a full-body image:

  | Tag name | Head | Full body | Acknowledgement (supplied) |
  |---|---|---|---|
  | `Technology character Jo` | `technology/Jo character/Jo_head 2192287171.svg` (`alt="Jo head"`) | `technology/Jo character/Jo_full 2192287171.svg` (`alt="Jo full"`) | `Illustration: Handsome business man set, iStock 2192287171, Getty Images. Used with permission.` |
  | `Technology character Tina` | `technology/Tina character/Tina_head 2235638824.svg` | `technology/Tina character/Tina_full 2235638824.svg` | `Illustration: Young beautiful student woman set, iStock 2235638824, Getty Images. Used with permission.` |
  | `Technology character Charlie` | `technology/Charlie character/Charlie_head 2241025538.svg` | `technology/Charlie character/Charlie_full 2241025538.svg` | `Illustration: Set of young student man set different poses, iStock 2241025538, Getty Images. Used with permission.` |

  `alt` = `<Name> head` / `<Name> full` for all three. The tag followed by *head* or *full* builds that image; the bare tag builds the **full-body** image and a `Designer/Developer To Do:` to confirm head or full. The page lists further iStock poses as *"Images to be added to centralised files as needed"* — they are not on the store, so a request for one is an ordinary image request.
- **Hats** — six `<object>` elements: `[Centralised image: Technology <Colour> hat]`, `<Colour>` = `Blue`, `Black`, `Yellow`, `White`, `Green`, `Red`:
  ```html
  <object class="imageCentral" data="technology/Hats/Blue hat.svg" type="image/svg+xml">Blue hat</object>
  ```
  The page's note beside them: text must stay web-standard size — the same size as `.captionText` or larger.

### Technology strand icons — folder `Technology/strand/` (capital T)
The five icons of §14.12 now have tags. Each strand also has an **inactive** twin (`inactive-…svg`, same name otherwise) with no tag of its own:

| Tag name | Active icon | `alt` | Caption shown on the page |
|---|---|---|---|
| `Tech SPD` | `Technology/strand/active-Spacial-and-Design.svg` | `Spacial and Design` | Spatial and Product Design |
| `Tech MPT` | `Technology/strand/active-Materials-processing.svg` | `Materials processing` | Materials and Processing Technology |
| `Tech EM` | `Technology/strand/active-Electronics.svg` | `Electronics` | Electronics and Mechatronics |
| `Tech DT` | `Technology/strand/active-Digital-Technology.svg` | `Digital Technology` | Digital Technologies |
| `Tech CS` | `Technology/strand/active-Computer-Science.svg` | `Computer Science` | Computer Science |

(The page writes the last tag without its closing bracket, `[Centralised image: Tech CS` — read as `[Centralised image: Tech CS]`.) **The strand strip** (the page's *Example*): all five icons in one `div.row.gap-3`, one `div.col` each, the module's own strands **active** with a `<p class="captionText center-text">` caption under them, the rest **inactive** with no caption.

### English — Kea characters (Writing Journals) — `kea_characters/`
Six images, **numbered by pose, not by phase** — the same six serve every phase: `kea_1` default right · `kea_4` default left · `kea_2` walking right · `kea_5` walking left · `kea_3` pointing right · `kea_6` pointing left. Path `kea_characters/kea_<n>.jpg` — **`kea_5.jpg` lower-case** — `alt="Kea character"`. The page's three phase examples all use `kea_3` and differ only in the bubble's colour (§14.10).

### BLLR bookworms — `bookworms/`
| Tag name | Worm | Year / module codes |
|---|---|---|
| `bookworm_1` | Yellow worm (*book & quill*) | Year 4 — BLLR201–BLLR210 |
| `bookworm_3` | Red worm | **Year 5 — BLLR211–BLLR220** |
| `bookworm_2` | Green worm | **Year 6 — BLLR221–BLLR230** |

Extra poses of the yellow worm: `bookworm_1a` writing on note pad · `bookworm_1b` magnifying glass · `bookworm_1c` holding a sign · `bookworm_1d` checklist clipboard · `bookworm_1e` lantern. Path `bookworms/<name>.jpg`, `alt="Bookworm"`.

### The Arts — Tūī — `tui_characters/phase <N>/` (a space, not an underscore)
Tag `[Centralised image: tui_<pose>]`; the **folder's phase is the module's phase** (template band `1-3` → 1, `4-6` → 2, `7-8` → 3, `9-10` → 4): `tui_characters/phase 2/tui_5.jpg`. Poses 1–6 in phases 1–3, poses 1–4 in phase 4; `alt="Tui character"`.

| Pose | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|---|---|---|---|---|
| 1 | flight — facing right | default — facing left | perched singing — facing left | perched singing — facing left |
| 2 | flight — facing left | default — facing left | perched singing — facing right | perched singing — facing right |
| 3 | perched — facing left | perched — facing left | default — facing left | default — facing left |
| 4 | perched — facing right | perched — facing right | default — facing right | default — facing right |
| 5 | perched — facing left | perched singing — facing left | flight — facing left | — |
| 6 | perched — facing right | perched singing — facing right | flight — facing right | — |

### Health and PE characters — `health & PE characters/`
Tag = the file name: `[Centralised image: HP_<Name>_<pose>_phase_<N>]`. **Every one of the five characters has all four poses in all four phases:** poses 1–2 full body in `health & PE characters/phase <N>/`, poses 3–4 head only in `health & PE characters/phase <N>/head_only/` — e.g. `health & PE characters/phase 4/head_only/HP_Sura_3_phase_4.png`. Pairs (phase 1 only): `[Centralised image: Kai and Afi phase 1]` → `health & PE characters/phase 1/combination/Kai and Afi phase 1.png`, `[Centralised image: Sura and Leila phase 1]` → `…/combination/Sura and Leila phase 1.png`. `alt=""` throughout. The full-body poses as the page describes them:

| Character | Phase 1 (pose 1 · 2) | Phase 2 | Phase 3 | Phase 4 |
|---|---|---|---|---|
| Sura | hydration · netball | gymnastics · standing | standing · gardening | playing soccer · standing |
| Alex | standing · dribbling basketball | standing · kicking ball | hockey · standing | skateboarding · standing |
| Afi | holding apple · sitting | playing cricket · haka | badmintin · holding volleyball | thumbs-up · surfing |
| Leila | standing · running | reading · rollerskating | feating lunch · playing tennis | taking scores · biking |
| Kai | tying shoes · standing | swimming · typing | holding soccer ball · playing rugby | holding clipboard · playing basketball |

### Science characters
Tag = the file name, `[Centralised image: <Name>-<n>]` (`Aroha-1`), and the scenes `[Centralised image: clubhouse_1]` / `[Centralised image: kowhai_reserve_1]`. The page writes the folder `science characters/`; **the path built is §14.13's server spelling, `Science Characters/` (CL-0119)**. Poses as the page describes them: **Aroha** 1 welcoming · 2 inspecting with magnifying glass · 3 pointing · 4–5 headshots; **Lani** 1 welcoming · 2 talking · 3 pointing · 4–5 headshots; **Max** 1 talking · 2 thinking · 3 writing · 4–5 headshots; **Quinn** 1 holding prototype · 2 pointing · 3 idea · 4–5 headshots, safety goggles down · 6–7 headshots, safety goggles up.

### Maths characters
Tag = the file name, `[Centralised image: maths_characters_<name>]` → `Maths Characters/maths_characters_<name>.jpg` (Ada, Omar, Hypi, Erni, Lara — §14.14, whose numbered-pose rule is unchanged).

### Weather — `weatherIcons/`
Twenty icons `weatherIcons/weather-1.svg` … `weather-20.svg`, `alt=""`. The page's tag is `[Centralised image: weather <type>]` but it names no types, so the icon is built when the writer gives its **number** (`[Centralised image: weather 7]`); a type in words raises a `Designer/Developer To Do:` naming it and builds nothing. Acknowledgement line (supplied): `Illustration: Weather Icons, Metservice, https://about.metservice.com/our-company/learning-centre/weather-icons-explained/. Used with permission.`

### AI guidelines icons — `AI guidelines icons/`
| Tag name | Path | Meaning (the page's caption) |
|---|---|---|
| `AI traffic light - red` | `AI guidelines icons/AI guidelines icon 1.svg` | No AI use allowed |
| `AI traffic light - orange` | `AI guidelines icons/AI guidelines icon 2.svg` | Using AI in tasks |
| `AI traffic light - green` | `AI guidelines icons/AI guidelines icon 3.svg` | Task can be completed using AI |

`alt=""` as supplied. These are icons, not the eight AI Guidelines PDFs of constraint 84.

### Acknowledgements
The three iStock-derived Technology assets and the weather icons carry the supplied lines above in the module's acknowledgements, like any other credited image. The NZ map keeps its §14.10 line.
