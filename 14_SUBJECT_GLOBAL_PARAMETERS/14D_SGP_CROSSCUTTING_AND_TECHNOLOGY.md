> **Last updated:** Thursday, 13th August, 2026
> **Granular part D (4 of 4) of `14_SUBJECT_GLOBAL_PARAMETERS.md`** — Cross-cutting notes (14.11) and the Technology family (14.12). Split from `14B` on 13 August 2026 when it passed the 30 KB soft limit (`CLAUDE.md` §4); content moved verbatim.
> All sibling parts live in `14_SUBJECT_GLOBAL_PARAMETERS/`; see `INDEX.md` at the repo root. Body below is verbatim source-of-truth content.

<!-- KB-PART-BODY-START -->
## 14.11 Cross-cutting notes

- **"Upload to Dropbox" series label (BLL / LS / HPE).** These three families label the dropbox submission button **"Upload to Dropbox"** (also seen as *Upload to dropbox*). This is a **series-scoped label** that sits **alongside** — and does **not** overturn — the universal **"Go to dropbox" / "Go to portfolio"** default (constraint 55 / `05` → Buttons). For any module outside these three families, the universal "Go to …" label still applies. (The HPE celebration page also carries a **"Go to your journal"** button next to its "Upload to dropbox" button.)
- **Central `imageCentral` assets recur across families.** Languages (per-language `… assets/` folders — §14.1), Taonga (`tui_characters/` — §14.3), HPE (`health & PE characters/` + the celebration `.gif` — §14.8), BLLR (`bookworms/` — §14.9), MiW (`kea_characters/` + the NZ map — §14.10), and Technology (`Technology/strand/` + the shared `congradulations/` celebration gif — §14.12) all use centralised template assets carrying `class="img-fluid imageCentral"`. These are design-team central-store assets — the `imageCentral` reservation in `01` (never on writer-specified images) is unchanged.
- **BLL dropbox-wrapper carve-out.** BLL is the **one** series that does **not** append the `dropbox` modifier to the `.activity` wrapper (§14.7). This carve-out is **scoped to BLL only** — it does **not** extend to the separate **BLLR** series (§14.9). Every other series follows constraint 43 unchanged.
- **`stickyNav` in the `<head>`.** The sticky-nav script recurs across Languages Phase 1–4 (every page), CED Phase 5 (dictionary links), and HPE (Fundamentals + Help page). Each is documented in its section above. (Split Mode base files are the exception — they carry **no** `stickyNav`; see `13_SPLIT_MODE.md`.)
- **Deferred-item convention.** Every "TO DO / TBC / placeholder / under development" item across these families is emitted as a **visible `Designer/Developer To Do:` red-note placeholder** (red + bold), never a hidden comment and never silently dropped — the pattern is built and the pending asset/URL/setup is flagged for production. See `02_DATA_CONTENT_VERIFICATION.md` → Source-Specific Red-Note Prefixes; `00` constraint 59.

---

## 14.12 Technology — strand icons + the celebration gif
**Scope — Cohort:** all **Technology** modules. *(The module-code prefix was not stated in the source; identify these modules by subject until a prefix is recorded here. Do not guess one.)*

- **Strand icons — five, one per Technology strand.** Delivered assets, held centrally in **`Technology/strand/`** and carrying `class="img-fluid imageCentral"` like every other central-store asset. Supplied markup (Spatial and Design shown — the `alt` is the strand's own name):
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="Technology/strand/active-Spacial-and-Design.svg" alt="Spacial and Design" >
  ```

  | Strand | Filename (exact case — use verbatim) |
  |---|---|
  | Spatial and Design | `active-Spacial-and-Design.svg` |
  | Materials Processing | `active-Materials-processing.svg` |
  | Electronics | `active-Electronics.svg` |
  | Digital Technology | `active-Digital-Technology.svg` |
  | Computer Science | `active-Computer-Science.svg` |

  > **⚠️ Copy the filenames character-for-character — do not "correct" them.** `active-Spacial-and-Design.svg` carries the design team's own spelling of *Spacial*, and the capitalisation is inconsistent between files (`Materials-processing` vs `Digital-Technology`). These are the real filenames on the server; a tidied path is a broken path. The **`alt` text** is the readable strand name and is not bound to the filename's spelling.

- **End-of-module celebration gif — DELIVERED.** The animated celebration graphic now exists and is emitted as a **real asset reference**, not a placeholder:
  ```html
  <img class="img-fluid imageCentral" loading="lazy" src="congradulations/Congradulations animation.gif" alt="Congradulations animation" >
  ```
  > **⚠️ THE MISSPELLING IS DELIBERATE AND STAYS — folder, filename and `alt` alike.** *Congradulations* is misspelt in the delivered asset path. Modules carrying it are already **built and live**, and the string is **never visible to a learner** (it is a path and an `alt` on a decorative graphic), so the design decision — Chris, August 2026 — is to **leave it exactly as it is**. Never silently correct it, never flag it as a typo, and never emit a "corrected" variant: `congradulations/Congradulations animation.gif` is the path that resolves. This is the **same central asset** the HPE family uses (§14.8), whose "still under development" deferral this delivery **lifts** — the standing `Designer/Developer To Do:` note about the final `.gif` being pending is retired for both families.

- **Celebration layout — text beside the graphic.** The suggested layout pairs the congratulation copy with the graphic in one row: **`col-8` = the text, `col-4` = the celebration gif.** This is the design team's stated suggestion for Technology, not a hard rule — where the content genuinely does not fit, adjust and say so. **Precedence is by family, and there is no ambiguity:** §14.8 describes the same shared gif as 1×1 and too large for a `col-8` and asks for the layout to be redesigned around it — that is **HPE's own page composition**, and this is **Technology's**. Follow the layout of the family you are converting; neither overrides the other, and neither is a property of the asset. *(If a single house rule is ever wanted for the shared graphic, that is a designer decision to state.)*
