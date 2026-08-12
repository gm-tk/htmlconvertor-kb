> **Last updated:** Thursday, 13th August, 2026
> **Granular part C (3 of 4) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — The complete Languages Audiovisual Package asset registry, absorbed verbatim from the final `20260511_Language_HTML` (5 August 2026) so the supplied HTML file no longer needs to be consulted or kept in project knowledge.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->

# 14C — Languages Audiovisual Package: the complete asset registry

> **When to load:** With `14A` §14.1, whenever a Languages-cohort module (CHFUN / JPNFUN / any future language prefix) carries an `[Audiovisual package …]` tag, a language icon tag, or a set-character reference. **The rules live in `14A` §14.1** (finalised-package rule, tag family, reference points, central-image rule); this part holds the **data**: every finalised asset with its tag, item number, delivery form, full markup source and filename. Component mechanics stay with their owners (`04A` carousel, `04B` audio image/trigger, `04C` speech bubbles, `05A` video/audio embeds, `05C` acknowledgements) — this registry only supplies the Languages-specific values.

**Provenance.** Absorbed from the design team's final `20260511_Language_HTML` ("All packages have been finalised for each of the languages"; every language panel marked *finalised and will be in use in upcoming modules*), supplied by the designer (Chris) on 5 August 2026 with the covering note naming **CHFUN** the structural reference point for all language fundamentals and **JPNFUN05** for all language 05 fundamentals. Ledger: CL-0070.

**Tag matching.** The writer's tag form is `[Audiovisual package <asset name> item N]` with variants in nested brackets (`[full body]`, `[headshot]`, `[neutral]`, `[certificate]`, `[holding books]`, `[ice cream]`, `[expression]`). Match on the **folded asset name** (case-insensitive, typo-tolerant — the reference itself contains `memebers`, `portait`, `Da wei`/`Da Wei`, `yuka headshot`, `[head shot]`, and stray spaces like `item 7 ]`); the item number is the **cross-check**, not the key. Item numbers are per-language and Japanese legitimately starts at item 0. A tagged Audiovisual asset **not** in this registry keeps the visible `Designer/Developer To Do:` note + the constraint-64 pending-ID Vimeo scaffold (`14A` §14.1).

---

## 1. Delivery forms (the supplied markup shapes)

Emit each registry asset in the form recorded for it below, using these supplied shapes exactly. (Mechanics and general rules: video `05A`, audioImage/trigger `04B`, speech bubbles `04C`, carousel `04A`.)

**Vimeo avatar/conversation video** — the full URL including the `h=` hash is required (it cannot be derived from the video id):

```html
<div class="videoSection ratio ratio-16x9">
	<iframe
		src="https://player.vimeo.com/video/1193069699?h=80d6eeee69&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
		frameborder="0"
		allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share;"
		referrerpolicy="strict-origin-when-cross-origin"
		title="German - Daniel Hoffmann (father)_1080p"
	></iframe>
</div>
```

> Three reference iframes (Wang Laoshi and two Japanese conversation videos) additionally carry an inline `style="position: absolute; …"` attribute. **Not codified** — constraint 2 (no inline CSS) is preserved with no new exception, the CL-0063 precedent; the base form above is the canonical one for every Vimeo asset.

**audioImage** (click the image to hear the voice — `04B` Audio Image):

```html
<div class="audioImage">
	<div id="German VA ONLY- Lina Hoffmann_1080p_01" class="audioImageOption">
		<img class="img-fluid imageCentral" src="German assets/Lina.jpg" />
	</div>
</div>
```

**audioButton** (voice only, named audio file — `04B`):

```html
<div class="audioButton" audioName="Chinese-Da wei"></div>
```

**audioPlayer** (voice-only narrator — `05A` Audio Player):

```html
<audio preload="none" src="audio/German_Female narrator.mp3" class="audioPlayer icon" title="German female narrator"></audio>
```

**Character headshot + speech bubble** (`04C` — text bubble, or an `audioButton` inside the bubble):

```html
<div class="row speechBubble" layout="speech">
	<div class="col-md-4 offset-md-0 col-12">
		<img class="img-fluid imageCentral" loading="lazy" src="Chinese assets/Da wei_headshot.jpg" alt="Da Wei headshot" />
	</div>
	<div class="col-md-8 col-12">
		<div class="bubble-right no-hover"><p>…</p></div>
	</div>
</div>
```

**Carousels** (`04A`): image scenes use `<div class="row carousel">` → `<div class="col-md-12 col-12 viewer">` → `<div class="item image">` with the `<img>` then a `<div class="carousel-caption"><p>…</p></div>`; the French avatar set uses the bordered variant `<div class="row carousel carouselBorder">` with `item video` (videoSection then caption). The Japanese conversation carousel nests the videoSection *inside* `carousel-caption` — an observed reference variant; either placement is acceptable for video items.

---

## 2. Language icons

Tag: `[Audiovisual package Icon <Name>]`. Files: `images/Icons/black icons/<filename>`. **The icons are identical throughout the phases and automatically match the module's phase colour** (phase-coloured files exist under `images/Icons/phase colour/`) — the writer never specifies a colour and the conversion never asks for one. Emit the black-icons file; the phase colouring is a template/production concern.

| Icon | Filename (exact case) |
|---|---|
| Reading | `Language icons_Reading.jpg` |
| Listening | `Language icons_Listening.jpg` |
| Speaking | `Language icons_Speaking.jpg` |
| Writing | `Language icons_Writing.jpg` |
| Interact | `Language icons_Interact.jpg` |
| Think | `Language icons_Think.jpg` |
| Idea | `Language icons_idea.jpg` |
| Linguist | `Language icons_linguist.jpg` |

Supplied form: `<img class="img-fluid" loading="lazy" src="images/Icons/black icons/Language icons_Reading.jpg" alt="reading" />`.

---

## 3. German — the Hoffmann family + friends (central folder `German assets/`)

| Asset (tag name) | Item | Form | Source / details |
|---|---|---|---|
| Claudia Hoffmann (mother) | 1 | Vimeo | `player.vimeo.com/video/1193069697?h=ac5760a77d&…` · title `_Claudia Hoffmann (Mum)_1080p` · voice + avatar from Heygen |
| Daniel Hoffmann (father) | 2 | Vimeo | `player.vimeo.com/video/1193069699?h=80d6eeee69&…` · title `German - Daniel Hoffmann (father)_1080p` · voice + avatar from Heygen |
| Lina Hoffmann (sister) | 3 | audioImage | id `German VA ONLY- Lina Hoffmann_1080p_01` · img `German assets/Lina.jpg` · voice Heygen, avatar Co-pilot ("Click on the image to hear their voice.") |
| Felix Hoffmann (brother) | 4 | Vimeo | `player.vimeo.com/video/1200277175?h=074b578675&…` · title `German - Felix Hoffmann` · avatar + voice from Heygen |
| Der Lehrer (teacher) | 5 | Vimeo | `player.vimeo.com/video/1193069825?h=58aa168f6d&…` · title `German - Der Lehrer_1080p` · voice + avatar from Heygen |
| Arihi | 6 | audioImage | id `German-Arihi_voice` · img `German assets/Ahirihi.jpg` · voice Heygen, picture/avatar Co-pilot |
| Narrator voice (VOICE ONLY) | 7 | audioPlayer | `audio/German_Female narrator.mp3` · title `German female narrator` · voice from Heygen |
| Salzi the pretzel (mascot) | 8 | audioImage + image variants | neutral = audioImage id `German_Salzi`, img `German assets/Salsi_neutral.jpg`; `[certificate]` → `Salsi_certificate.jpg`; `[holding books]` → `Salsi_books.jpg`; `[ice cream]` → `Salsi_ice cream.jpg` (all `imageCentral`; note the **Salsi** filename spelling vs the **Salzi** character/tag name). All variant tags are item 8, e.g. `[Audiovisual package Salzi [certificate] item 8]` |

Module-local scene example (not `imageCentral`): `images/German/Family playing board game.png` — "a couple of the characters within a scene".

---

## 4. French — three Vimeo avatars in a bordered carousel (no central image folder)

Presentation: `row carousel carouselBorder`, `item video`, caption below each video. The characters ARE the videos — French has no central image folder; the podcast scene screenshot is module-local `images/French/Sophie and Luc podcast.png`.

| Asset (tag name) | Item | Form | Source / details |
|---|---|---|---|
| Luc | 1 | Vimeo | `player.vimeo.com/video/1190998681?h=b086b19880&…` · title `Luc - French speaker_1080p` · French speaker from France |
| Sophie | 2 | Vimeo | `player.vimeo.com/video/1190998668?h=ac5494a544&…` · title `Sophie - French speaker_1080p` · French speaker from France |
| Malia | 3 | Vimeo | `player.vimeo.com/video/1190998650?h=b027907f6a&…` · title `Malia - NZ speaker_1080p` · NZ + French speaker from New Zealand |

---

## 5. Chinese (central folder `Chinese assets/`)

Voices (audioButton `audioName` values): **Da Wei** → `Chinese-Da wei` · **Xiao Mei** → `Chinese-Xiao mei` · **Female narrator** → `Chinese_Female narrator`.

| Asset (tag name) | Item | Form | Source / details |
|---|---|---|---|
| Da wei | 1 | image (`[full body]` / `[headshot]`) | `Chinese assets/Da wei.jpg` (full body) · `Chinese assets/Da wei_headshot.jpg` |
| Xiao Mei | 2 | image (`[full body]` / `[headshot]`) | `Chinese assets/Xiao Mei_full body.jpg` · `Chinese assets/Xiao Mei_headshot.jpg` |
| Wang Laoshi (teacher) | 3 | Vimeo | `player.vimeo.com/video/1196193454?h=2c32d71555&…` · title `Wang Laoshi - avatar and voice_1080p` · avatar and voice |
| Panda (mascot) | 4 | image | `Chinese assets/iStock-2193695860.jpg` — derived from iStock **2193695860**; the writer **still puts an i-Stock link in the WT for the allocated designer**; acks per §9 |

Speech-bubble pairings observed: Da Wei headshot + text bubble; Xiao Mei headshot + a bubble containing her `audioButton`.

---

## 6. Japanese (central folder `japanese assets/` — also seen as `Japanese assets/`; one folder)

Voices (audioButton `audioName` values): **Kauri** → `Japanese_Kauri` · **Yuka** → `Japanese_Yuka` · **Sakura** → `Japanese_Sakura`.

| Asset (tag name) | Item | Form | Source / details |
|---|---|---|---|
| Sakura | 0 | image (`[full body]` / `[headshot]`) | `japanese assets/Sakura.jpg` · `japanese assets/Sakura_headshot.jpg` |
| Yuka | 3 | image (`[full body]` / `[headshot]`) | `japanese assets/Yuka.jpg` · `japanese assets/Yuka_HEADSHOT.jpg` |
| Kauri | 4 | image (`[full body]` / `[headshot]`) | `Japanese assets/Kauri.jpg` · `japanese assets/Kauri_headshot.jpg` |
| morning / afternoon / evening / night greeting | 1 | image (scene-stills carousel) | `japanese assets/Yuka_Kauri_greeting_morning.jpg` / `_noon.jpg` / `_evening.jpg` / `_night.jpg` — captions "School in the morning/afternoon/evening", "station at night" |
| Snow festival | 7 | image (scene still) | `japanese assets/Yuka_Kauri_snowfestival.jpg` |
| Ainu village | 10 | image (scene still) | `japanese assets/Yuka_Kauri_Ainu village.jpg` |
| Introductions | 5 | Vimeo (in carousel) | `player.vimeo.com/video/1200640618?h=44d39bf1d8&…` · title `Sakura and Kauri in gym` — "still images and audio in conversation" |
| Meeting someone for the first time asking their name | 2 | Vimeo (in carousel) | `player.vimeo.com/video/1203682044?h=d08cbdf0c5&…` · title `Meeting someone for the first time` |
| Showing family members | 6 | Vimeo (in carousel) | `player.vimeo.com/video/1203681543?h=f359402236&…` · title `Showing family members` (reference tag reads `memebers` — match tolerantly) |

Speech-bubble pairing observed: Yuka headshot + a bubble containing her `audioButton`.

---

## 7. Spanish (central folder `Spanish assets/`)

**Accents:** a Spanish voice audio runs through **all** the accents in one file — the order is **Spain, Latin America, Mexico**; keep the writer's "please listen to the full audio" framing wherever the voices are introduced.

**Expressions:** Pablo and María have multiple expressions; the writer puts the number in correlation to the expression — e.g. `[Audiovisual package Pablo [expression] item 1]`.

| Asset (tag name) | Item | Form | Source / details |
|---|---|---|---|
| Pablo | 1 | audioButton + expression carousel | `audioName="Spanish_Pablo"` · iStock **2214853643** · expressions `Spanish assets/Spanish assets_Pablo_<neutral|angry|happy|scared>.jpg` |
| María | 1 | audioButton + expression carousel | `audioName="Spanish_Maria"` · iStock **2214816016** · expressions `Spanish assets/Spanish assets_Maria_<neutral|happy|sad|scared|smile>.jpg` |
| family tree | 3 | image | `Spanish assets/Spanish_Family tree.jpg` · iStock **1675300511** (people) + **2207512167** (pets) |
| family portait | 4 | image | `Spanish assets/Spanish_Portait.jpg` (the reference's own `portait` spelling in both tag and filename — match tolerantly, keep the filename as supplied) |

---

## 8. Samoan (central folder `Samoan character assets/`)

| Asset (tag name) | Item | Form | Source / details |
|---|---|---|---|
| Fa'auiga | 1 | image (`[full body]` / `[headshot]`) | `Samoan character assets/Fa'auiga.jpg` · `Samoan character assets/Fa'auiga_headshot.jpg` |
| Si'iolo | 2 | image (`[full body]` / `[head shot]`) | `Samoan character assets/Si'iolo.jpg` · `Samoan character assets/Si'iolo_headshot.jpg` |
| NZ to Samoa | 3 | image (animated gif) | `Samoan character assets/Adobe Express - nz to samoa.gif` · iStock **926176050** (NZ map) + **2215778947** (Samoa map) |

---

## 9. Acknowledgements for the iStock-derived registry assets

Per `05C`; the reference ships these exact lines ("Adapted. Used with permission." — the assets are derived/adapted, not reproduced):

- Chinese Panda: `Photo: Print, iStock 2193695860, Getty Images. Adapted. Used with permission.`
- Samoan maps: `Photo: Map of New Zealand, iStock 926176050, Getty Images. Adapted. Used with permission.` · `Photo: Samoa - Detailed map with regions, cities and country flag, iStock 2215778947, Getty Images. Adapted. Used with permission.`
- Spanish: `Photo: Cool Young Man Portrait- Facial Expressions, iStock 2214853643, Getty Images. Adapted. Used with permission.` · `Photo: Young Woman With Long Dark Hair Portrait- Facial Expressions, iStock 2214816016, Getty Images. Adapted. Used with permission.` · `Photo: Cartoon family. Couples of parents with happy kids and grandparents, full family portrait vector illustration, iStock 1675300511, Getty Images. Adapted. Used with permission.` · `Photo: Cute pet set: cat, dog, rabbit, guinea pig, hamster, rat, parrot, fish, snake, turtle, lizard and snail. Cartoon domestic animals collection. Vector flat illustration isolated on white background, iStock 2207512167, Getty Images. Adapted. Used with permission.`

All other registry assets (Heygen/Co-pilot characters, icons, scenes) fall under the standing `All other images © Te Aho o Te Kura Pounamu, Wellington, New Zealand.` line.
