## What it does

`vibe` is a dispatcher for one developer working alone. You tell it what you are trying to do (or nothing, and it asks), and it hands back a **route card**: which of four lanes you are on (Build, Fix, Review, Tidy), how big the work is, the exact next command to type, the two or three steps after that, and what to do with your [context](https://www.aihero.dev/ai-coding-dictionary/context) between them.

It routes and stops. It does not grill, write a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), or start coding; where a lane's first step is a model-invoked skill (`tdd`, `diagnosing-bugs`, `code-review`) it offers to fire that one on a "go", and otherwise you type what the card names.

It is a curated subset, not the full map. The kit is twenty-four skills chosen for solo work; `wayfinder`, `triage`, `to-questionnaire` and the rest are named as deliberately out, each with the moment to bring it back. The full map stays [ask-matt](https://aihero.dev/skills-ask-matt).

## When to reach for it

You invoke this by typing `/vibe`; the agent won't reach for it on its own.

| Your situation | What the card gives back |
| --- | --- |
| An idea, and you don't want to think about process | Build lane, sized S, M or L: just say it, grill then implement, or grill → spec → tickets → implement per ticket |
| Something broke, flaky, or slow | Fix lane, split on whether you already know the cause: `tdd` straight in, or the gated `diagnosing-bugs` loop |
| A branch you want checked | `/code-review main`, and what to do with each axis of findings |
| The codebase feels harder to change than it should | `/improve-codebase-architecture`, and how the idea it produces goes back onto Build |
| You've asked for the same change three times and it's still wrong | Not a fifth attempt. Discard, clear, write one input / expected / actual example; whether you can write it picks the lane |
| The session drifted, is about to move, or died on you | One of the three seam moves: [refocus](https://aihero.dev/skills-refocus) to stay, [handoff](https://aihero.dev/skills-handoff) to leave on purpose, [takeover](https://aihero.dev/skills-takeover) in the new window when the old one is gone |
| A grill question only running code can settle | The prototype detour: `/handoff` the question, [prototype](https://aihero.dev/skills-prototype) in a fresh session, the decision comes back to the grill |
| A team, stakeholders, or a greenfield product too foggy for one head | Not this. It says so in a line and points at [ask-matt](https://aihero.dev/skills-ask-matt) |

## Prerequisites

The repo must have been through [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills). The dispatcher checks for `docs/agents/issue-tracker.md` first and, if it is missing, that is the only thing the card says. Local markdown is the solo default; GitHub works the same way with issues in place of files.

## Lanes and size

The word to think with is **lane**. You are always in exactly one, and each has one decision inside it:

| Lane | The one decision | Why it matters |
| --- | --- | --- |
| **Build** | Size: S, M or L | Size decides how much ceremony you pay. S is a sentence; M is a grill and an implement in one window; L is grill, spec, tickets, and a fresh window per ticket |
| **Fix** | Do you know the cause? | Yes goes straight to a failing test. No goes to a loop that refuses to theorise until one command goes red on the bug |
| **Review** | None | Two axes, Standards and Spec, never merged into one score |
| **Tidy** | Which candidate | The survey produces an idea; the idea goes back onto Build |

The sizing question is asked in order and the first yes wins: can you write it as one sentence with no open questions (S); does it fit one sitting but you have questions first (M); neither (L). Most solo work is S or M, and the card recommends against L until you have caught yourself re-explaining a decision in a second session.

## Common questions

**How is this different from `ask-matt`?**

`ask-matt` is the map of everything, written as prose so it can carry the branches. `vibe` is a fixed subset with the branches pre-decided for one person working alone, and it hands back a fill-in-the-blanks card rather than a paragraph. If your situation involves other people (incoming bug reports, a stakeholder, a colleague picking up the work) you have left the subset, and it says so.

**Can I skip it and just type the skills?**

Yes, and after a week you will. The card exists for the first few sessions, and for the moments where you have a bug and can't tell whether it is a `tdd` bug or a `diagnosing-bugs` bug. The cheatsheet at the bottom of the skill's `WORKFLOW.md` is the same information as a table, and [the poster](https://github.com/awangs1986/popcodeskills/blob/main/docs/engineering/vibe-workflow-poster.png) is the same information as one picture.

**It offered to start `tdd` for me. Is that safe?**

It only fires model-invoked skills, and only after you say go. Every user-invoked step (`grill-with-docs`, `to-spec`, `to-tickets`, `implement`, `improve-codebase-architecture`, `refocus`, `handoff`, `takeover`) stays yours to type; no skill in this repo can fire those for you.

## It's working if

- The card names one next command and stops, instead of starting the work.
- Sizing lands on S or M most of the time, and you can say why the occasional L earned its spec.
- After an L build you notice you are no longer re-explaining decisions between sessions: they are in `CONTEXT.md`, an ADR, or the spec.
- A hard bug's fix commit names the hypothesis that turned out right, because the Fix lane went through the loop rather than around it.

## Where it fits

A **run-first dispatcher**: the thing you type when you don't yet know which chain step you're at. It hands off to the main chain ([grill-with-docs](https://aihero.dev/skills-grill-with-docs) → [to-spec](https://aihero.dev/skills-to-spec) → [to-tickets](https://aihero.dev/skills-to-tickets) → [implement](https://aihero.dev/skills-implement) → [code-review](https://aihero.dev/skills-code-review)) at whichever step the size calls for, to [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) for a hard bug, and to [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) for upkeep. [ask-matt](https://aihero.dev/skills-ask-matt) remains the router over the whole set, because it covers the situations this one deliberately leaves out.
