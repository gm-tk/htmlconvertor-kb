# Rolling the mode skills out to the organisation

Ten skills, for nine modes: Mode 3 (`COMPARISON MODE`) is split into a **module** skill and an
**assessment** skill, because the two procedures behave differently and designers need to tell
them apart. The mode itself is not split and the typed phrase still routes itself — see
`README.md` → *The two comparison skills*.

Written for someone who is not a developer. Every step says where to go, what to click, what
you should see when it worked, and what to do if it did not.

---

## Before you start — two things to know

**1. There is no skill picker in a Claude chat.** Designers will not choose a mode from a
menu. Claude picks the skill itself, by matching what the designer typed against each skill's
short description. That is why the typed trigger phrases keep working: `COMPARISON MODE` is
written into the Comparison skill's description, so typing it is what makes the skill fire.

The place designers *can* browse the list is **Customize → Skills** (`claude.ai/customize/skills`).
There they see each skill's name and its one-line description, and clicking a skill shows its
full contents.

**2. The mode card is how a designer knows they are in the right mode.** Each skill's first
instruction is to print a short panel naming the mode, what it does, what it needs, what comes
back, and what it will not do — followed by *"Wrong mode? Tell me what you actually want to
do."* That panel appears in the chat immediately, before any work starts.

Admin Mode is the deliberate exception. Its own rules (`17_ADMIN_MODE.md` Section 10) fix
exactly what a reader sees and in what order, so adding a panel would break the mode it is
meant to help. That skill instead folds the same plain-English "this is Admin Mode, this is
what it does" into the opening line Section 10 already provides for. You will see a sentence,
not a panel — that is correct.

---

## Step 1 — Check the two organisation switches are on

Go to **Organization settings → Skills** — `claude.ai/admin-settings/skills`.

Two things must be turned on:

- **Code execution and file creation**
- **Skills**

On a **Team** plan these are usually on already. On **Enterprise** an owner has to switch them
on deliberately.

**You should see:** both toggles blue/on, and an **+ Add** button in the upper right.

**If you cannot see this page at all:** you are not an owner of the organisation. Only owners
can add organisation-wide skills. Ask whoever owns the Te Kura Claude organisation to do
Step 2, or to make you an owner.

---

## Step 2 — Upload the ten zips

The ten files are in the connected folder at:

```
00-Other-TK-Resources/htmlconvertor-kb/19_SKILLS/dist/
```

They are named after their modes: `tekura-conversion-mode.zip`,
`tekura-advisory-support-mode.zip`, `tekura-module-comparison-mode.zip`,
`tekura-assessment-comparison-mode.zip`, `tekura-update-mode.zip`,
`tekura-split-mode.zip`, `tekura-interactives-mode.zip`,
`tekura-pageforge-compare-mode.zip`, `tekura-admin-mode.zip`, `tekura-assessment-mode.zip`.

For **each** zip, one at a time:

1. On **Organization settings → Skills**, click **+ Add** in the upper right.
2. Choose **Upload a skill**.
3. Pick the `.zip` file.

**You should see:** the skill appears in the organisation's list straight away. It is
**provisioned to everyone immediately** and switched on for them by default — nobody has to
enable anything. An individual designer can switch one off for themselves, but cannot delete
it.

**If an upload fails**, it is almost always one of four things:

| What you see | What it means | What to do |
|---|---|---|
| "Folder name must match the skill name" | The zip was made by hand and has the wrong shape | Rebuild with `19_SKILLS/build_skills.sh` — it makes the right shape every time |
| "Missing required SKILL.md" | The zip has an extra wrapper folder inside it | Same fix: rebuild with the script |
| "Invalid characters in skill name or description" | Usually a description longer than 200 characters | Run `python3 tools/check_kb.py`; it reports the offending skill and the actual length |
| Nothing happens / silent failure | The zip exceeded the upload size limit | These skills are a few kilobytes each, so this should not occur; re-download the zip |

---

## Step 3 — Prove it works, in five minutes

Open a **new chat inside the HTML Convertor project** and try these.

1. **In a chat that converted a module, type `COMPARISON MODE` with your refined files attached.**
   *You should see:* the **Module** Comparison Mode card, then the mode running as it always
   has. This is the backwards-compatibility test — the old way still works, and the bare phrase
   still works out which comparison to run by itself.

2. **Type, in plain English, "I want to compare my finished HTML against what you generated".**
   *You should see:* the same card. This is the new way in, for designers who never learned the
   phrase.

3. **In that same module chat, deliberately ask for the assessment one** — "use the assessment
   comparison skill".
   *You should see:* **a warning, and nothing else.** It should say this looks like a module
   chat, name the evidence, explain that the assessment one scopes everything Universal, and
   offer *"module"* or *"continue"*. It must **not** start comparing. This is the wrong-skill
   safeguard.

4. **In an assessment chat, type `COMPARISON MODE` with a refined `{CODE}.html` attached.**
   *You should see:* the **Assessment** Comparison Mode card, and one finalized report straight
   away — no scope question, no first-pass report.

5. **Open a chat OUTSIDE the project and type `COMPARISON MODE`.**
   *You should see:* a one-line refusal saying the skill only works inside the HTML Convertor
   project. This is the guard that stops these skills misfiring in unrelated work.

**If test 1 shows no card** but the mode still runs correctly: the skill did not fire and the
project instructions handled it, which is the safety net working. Nothing is broken. Tell
whoever maintains the skills — the description may need the phrase written more prominently.

**If test 3 does not refuse:** that is the one worth fixing quickly. Switch that skill off at
the organisation level until the guard is corrected.

---

## Step 4 — Tell the designers, in one message

Something like:

> The Convertor's modes are now also skills. Nothing you already do changes — typing
> `COMPARISON MODE`, `UPDATE MODE` and the rest works exactly as before. What is new is that
> you can also just describe what you want in plain English, and that whichever mode starts,
> you now get a short panel at the top of the reply telling you what that mode does, what it
> needs from you and what it will hand back — so you can tell straight away if you have landed
> in the wrong one. If you have, just say so and it will switch. You can read what every mode
> does at Customize → Skills.
>
> One thing worth knowing: **Comparison Mode now shows up as two skills** — *Module
> Comparison* and *Assessment Comparison*. They work differently: the module one gives you a
> first report and asks you to scope each difference, the assessment one gives you the
> finalized report straight away. You do not have to pick. Typing `COMPARISON MODE` as you
> always have still works out which one you need from the chat you are in. Picking one by name
> is there if you want it, and if you pick the one that does not match the chat, it will say so
> and check with you before doing anything.

---

## Changing a mode card later

Skills do **not** sync from the GitHub repository the way the project's knowledge does. The
repo holds the source and the history; uploading is manual.

1. Edit the `SKILL.md` in `19_SKILLS/<skill-name>/`.
2. Run `python3 tools/check_kb.py` — it must pass.
3. Run `sh 19_SKILLS/build_skills.sh` to rebuild the zips.
4. Commit and push.
5. At **Organization settings → Skills**, remove the old version of that one skill and upload
   the new zip.

A change to a Convertor **rule** needs none of this. Rules live in the knowledge base; the
skills only point at them.
