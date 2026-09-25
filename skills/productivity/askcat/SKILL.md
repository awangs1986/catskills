---
name: askcat
description: "Build a single HTML page where a cartoon cat explains every skill installed from this repo in plain words: what each one does, when to type it, what you'll see, and which one you need right now. A guided tour of the kit, in the user's language."
disable-model-invocation: true
argument-hint: "Nothing, a language, an output path, or one skill name to start the tour on"
---

# Askcat

The user wants to understand the skills they have installed, and they want it explained the friendly way. Produce **one self-contained HTML file** in which a cat guide walks them through the whole kit: what each skill is for, when to reach for it, what a good run looks like, and a "which one do I need?" picker. This is `teach` narrowed to a single topic (this repo's skills) with a fixed guide character and a bundled page template, so the work is the writing, not the layout.

You explain; you don't run anything. Building the page is the whole job.

## 1. Gather the kit (read, don't recall)

Every sentence on the page must come from a `SKILL.md` you opened in this session. Never describe a skill from memory.

1. **Find the skills.** Look in the harness skill directories (`~/.claude/skills`, `~/.agents/skills`, `~/.pi/agent/skills`, a project-level `.claude/skills`, `.agents/skills`, `.pi/skills`) and, when the current directory is a checkout of the skills repo, in `skills/*/`. Take the **promoted** set (the `engineering/` and `productivity/` buckets, or the plugin's skill list) plus anything from `in-progress/` that is actually installed, labelled as beta. Skip `misc/` and `deprecated/`.
2. **Read each `SKILL.md`**: the frontmatter (`name`, `description`, whether `disable-model-invocation: true`, meaning the human types it) and enough of the body to say honestly what it produces and what it refuses to do. Where a skill has a docs page under `docs/<bucket>/<name>.md`, its *When to reach for it* and *It's working if* sections are the best source for the card.
3. **Read the map.** `vibe/WORKFLOW.md` (if present) gives the lanes, sizes and the order skills run in; `ask-matt/SKILL.md` gives the full map. Use them to decide chapters and to write the picker. If neither exists, group by the bucket READMEs.
4. **Note the user's language.** The page is written in the language the user is speaking to you in, unless the argument names another. Skill names, commands and file paths stay as they are.

## 2. Write the content

Fill the data object described in [DATA-FORMAT.md](DATA-FORMAT.md). One card per skill; the rules for a card:

- **Plain words.** A first-week developer who has never used an agent should follow every card. Say "a test that fails on purpose first" rather than "red-green"; if a repo term is unavoidable (spec, ticket, seam, context window, primary source), gloss it inline the first time and add it to the glossary.
- **Nothing invented.** The one-liner, the *when*, the *what you'll see*, and the *it's working if* line all come from the skill's own file. If a skill's file doesn't say what a good run looks like, say so on the card rather than guessing.
- **One realistic example prompt** per skill, in the user's language, of the kind they would actually type. For user-invoked skills, start it with the command; for model-invoked skills, show the sentence that makes the agent reach for it, and say that it is automatic.
- **The cat tip** is the one thing people get wrong with this skill, or the one habit that makes it pay off. From the docs page's *Common questions* when there is one. Not a joke; a friend's warning.
- **Working / broken tells** in one line each, so the user can tell a good run from a bad one the first time.
- **Length.** Each field one to three short sentences. The page is a tour, not the manual; the card links to the skill's own file for the rest.

Chapters follow the workflow, not the alphabet: *Start here* (the dispatcher and setup), then *Build*, *Fix*, *Review*, *Tidy*, *When the session goes wrong*, *Everything else*. Inside a chapter, order skills the way they run. Each chapter has a two-sentence blurb and a cat mood from the fixed set in DATA-FORMAT.md.

The **picker** is a short decision tree (three or four questions deep at most) that lands on one skill and one example prompt. Derive it from the workflow's lanes and signals; every leaf must be a skill that is on the page.

The **first run** list is the shortest sequence that exercises the whole loop once, with what to watch at each step; take it from `vibe/WORKFLOW.md` if present, otherwise write a five-step one from the cards.

## 3. Build the page

1. Read [template.html](template.html) from this skill's directory. Do not rewrite its layout or styles; the cat, the chapters, the search box, the picker and the progress ticks are already in it.
2. Replace the single line `/*ASKCAT_DATA*/` with `window.ASKCAT = <your JSON>;`. Valid JSON, no trailing commas, strings escaped.
3. Write the result to `askcat.html` in the current directory, or to the path the argument names. One file, no external assets, no network requests.
4. Open it for the user if the host can run a command (`open`, `xdg-open`, `start`); otherwise give the path and say to double-click it.
5. If the argument named a skill, append `#skill-<name>` to the path you give back so the page opens on that card, and answer in chat with that card's one-liner and example in two or three sentences.

Reply briefly: where the file is, how many skills are on it, and that ticks (the "I've tried this" boxes) are saved in the browser, so the page doubles as a checklist. Offer to regenerate after they install or update skills; the page has no memory of its own beyond those ticks.

## Rules

- Read before you write. A card for a skill whose file you didn't open in this session is a card you may not write.
- Don't run, install, or configure anything. If the user asks "so which one should I run now", answer from the picker and stop; `vibe` exists for the routing.
- Don't add skills that aren't installed, and don't hide ones that are. If you find a skill you can't explain from its file, put it on the page with its description and a note saying the file didn't say more.
- The cat is a guide, not a mascot for its own sake. Every bubble carries information; if a bubble could be deleted without losing anything, delete it.
- No em-dashes in the page copy.
