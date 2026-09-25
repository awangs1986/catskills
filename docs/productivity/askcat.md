## What it does

`askcat` builds **one HTML page** that explains every skill you have installed from this repo, the friendly way. A cartoon cat walks you through the kit chapter by chapter, in the order the skills are used rather than alphabetically: start here, build, fix, review, tidy, what to do when the [session](https://www.aihero.dev/ai-coding-dictionary/session) goes wrong, everything else. Each skill gets a card: what it does in one plain sentence, when to reach for it, what a run looks like, one realistic prompt to type, the cat's one tip (the thing people get wrong), and a one-line tell for a good run and a bad one.

Around the cards: a **"which skill do I need?"** picker (three or four questions, lands on one skill and a prompt), the **first-run** sequence with what to watch at each step, a glossary of the repo's words in plain language, search, and an *I've tried this* tick on every card that is saved in your browser, so the page doubles as a checklist.

It is [teach](https://aihero.dev/skills-teach) narrowed to one topic, with the guide character and the layout fixed. The [agent](https://www.aihero.dev/ai-coding-dictionary/agent)'s whole job is the writing, and the writing has one rule: every sentence comes from a `SKILL.md` it opened in this session. Nothing is described from memory.

## When to reach for it

You invoke this by typing `/askcat`; the agent won't reach for it on its own. The page is written in whatever language you are talking to it in; pass a language, an output path, or a skill name to start the tour on.

| Situation | Reach for |
| --- | --- |
| First week with the kit, and the README is a wall | **`/askcat`** |
| Showing the skills to someone you're onboarding | **`/askcat`**, in their language |
| "Which one do I type right now?" | [vibe](https://aihero.dev/skills-vibe): it routes, this page teaches |
| One message from the agent didn't land | [wait-what](https://aihero.dev/skills-wait-what) |
| Learning a topic that isn't this kit | [teach](https://aihero.dev/skills-teach) |

## Common questions

**It generated a page. Is the content trustworthy?**
As trustworthy as the files it read. The skill forbids describing a skill it didn't open, and a card for a skill whose file says nothing about what a good run looks like says exactly that instead of inventing one. If a card looks wrong, the fix is upstream: the skill's own `SKILL.md` or docs page.

**Why chapters by workflow and not a list?**
Because "what is `to-tickets`" is the wrong first question. The useful one is "I have an idea, what happens next", and the answer is a sequence. The page follows the same lanes as `vibe`'s handbook so the two agree.

**Can it open on one skill?**
Yes: `/askcat tdd` builds the whole page, hands back a link that opens on that card, and answers in chat with that card's one-liner and example.

**Does it know what I've tried?**
Only through the ticks, which live in your browser's local storage for that file. Regenerate the page after installing or updating skills; the ticks survive as long as the skill names do.

**Is the cat necessary?**
It is a guide, not decoration: every bubble carries a fact, and the skill deletes any that doesn't. The character exists because a tour with a voice gets read and a reference table gets skimmed.

## It's working if

- Someone who has never used an agent can read a card and know what to type and what they will see.
- Every card's example is something you would actually type, and every picker leaf lands on a skill that is on the page.
- The page opens from disk with no network, and looks the same in every browser you have.
- Nothing on it describes a skill you don't have, and nothing you have is missing.
- After a week the ticks show which skills you've actually run, and the untried ones are the ones you meant to try.

## Where it fits

The onboarding layer over the whole set. [vibe](https://aihero.dev/skills-vibe) routes you to the next command; [ask-matt](https://aihero.dev/skills-ask-matt) is the full map for someone who already knows the names; this page is for the week before either of those is fast. It reads the same `SKILL.md` files and, when present, `vibe/WORKFLOW.md`, so it never disagrees with them; regenerate it whenever the installed set changes. It is [teach](https://aihero.dev/skills-teach) pointed at the kit itself.
