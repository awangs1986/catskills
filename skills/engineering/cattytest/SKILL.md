---
name: cattytest
description: "Grill the user about how to test a half-built project or feature: which behaviours must never break, at which seams, judged by what, with which parts real and which faked. Produces a test plan of numbered business-rule claims and the first red tests, in order, ready for tdd. Use when the user says \"I don't know how to test this\", \"where do I even start with tests\", or has code with no tests worth the name."
disable-model-invocation: true
argument-hint: "A feature, ticket, module, or nothing to be asked what to plan for"
---

# Cattytest

The user has code and no idea how to test it. Not "no tests": no *plan*. `tdd` knows what a good test is, but it assumes someone can already say which seams to test and what the rules are. This skill is the interview that produces that: a grilling session whose only output is a **test plan**, a numbered list of business-rule claims with a seam, a level and an oracle each, and the first red tests in order.

It is `grilling` pointed at one question: *what would have to be true for you to trust this code?* Invoke the "grilling" skill for the discipline (rounds, a frontier, a recommended answer on every question, facts are yours to find and decisions are theirs). This file is what to read first, what to ask, and what to write down.

You plan; you don't write tests here. Every line of the plan is a red test for `tdd`.

## 0. Scope, one question

Before anything else, one question, two options, wait:

> **Q1 - Scope**: plan tests for (a) the current feature or ticket, or (b) the whole project?
> ➡️ Recommend (a) if there is an in-flight ticket or a spec in `.scratch/` or the tracker; the plan attaches to it. Recommend (b) if there is no ticket, the user said "the project", or no test in the repo has ever gone red for a reason. (b) takes more rounds and ends with priorities, not just a list.

If the argument already names one (a ticket id, "the whole thing", a module), take it and say so instead of asking.

## 1. Read first, silently

Facts are your job. Before the first real round, look, and only mention what changes a question:

- `docs/agents/feedback-loops.md`: is there a test command, a single-file command, a duration? **None wired** doesn't stop the interview; it makes `/setup-feedback-loops` the first line of the plan and means no test can be run to confirm anything you find.
- `docs/agents/issue-tracker.md` for where the plan will live, and the ticket or spec in scope: its acceptance criteria and user stories are candidate claims before the user says a word.
- `CONTEXT.md`: claims are written in its words. Absent is fine; use the user's.
- **The existing tests**, all of them in scope: how many, what they touch, which are the `test-audit` kinds (claims nothing, tautological, name and assertion disagree, mocks the thing under test). Don't run a mutation probe; a read is enough to sort them into keep / rewrite / delete candidates for the user to confirm.
- **The code's boundaries**: entry points (routes, commands, UI actions, exported functions callers use), and every place it touches the outside world (database, network, filesystem, clock, randomness, environment, another process). These are the seams and the doubles questions; propose them, don't ask the user to enumerate their own code.
- A `test-plan.md` already in scope: this is a revisit. Load it, and the rounds start from its **Open** section.

## 2. The interview

Work the design tree in rounds, each question numbered with a recommended answer drawn from what you read. The branches, roughly in dependency order (a later branch waits on the earlier one's answers), with the question bank in [QUESTIONS.md](QUESTIONS.md):

1. **Stakes**: the behaviours whose breaking the user would hear about, the last bug that embarrassed them, what "done enough" means for this scope. This orders everything else.
2. **Claims**: each behaviour as one sentence a domain expert would say, true of the product when the test is green. Draft them from the criteria and the code; the user corrects the sentence, not the code. A claim the user is unsure is *right* is flagged, not dropped: it's a spec question (`refocus` or the ticket's comments) and it stays in the plan marked **rule unconfirmed**.
3. **Seams**: for each claim, the public boundary the behaviour crosses. Propose the seam from the entry points you found; the user picks or names a better one. `tdd`'s rule applies here in advance: no test is later written at a seam the user didn't confirm. If a claim has no seam (the behaviour is smeared across five files), say so; that's a Tidy finding, and the claim gets tested at the nearest seam that exists, or parked.
4. **Oracle and level**: how anyone knows the answer is right (a known-good literal, a worked example from the spec, a screenshot a human judges, a second implementation), and therefore which level the test lives at. Recommend integration at the seam by default, unit only for pure logic with a worked example, end-to-end only for the two or three claims the user named under Stakes.
5. **Doubles**: for each outside-world touch on the claim's path, real or faked, and if faked, how (`tdd`'s [mocking.md](../tdd/mocking.md) is the reference). Recommend real for anything cheap and deterministic, a fake at the boundary for network and time, never a mock of the thing under test.
6. **Data**: what a realistic input is and where the expected values come from. An expected value the user can't source independently of the code is a tautology waiting to happen; ask again or mark the claim **oracle missing**.
7. **Wrong paths**: for each claim, the empty case, the boundary, the second call, the record that belongs to someone else, the concurrent one. Ask which matter; recommend one wrong path per claim, more for the Stakes three.
8. **Existing tests**: your keep / rewrite / delete sort, confirmed row by row. A deleted test is written down with why, so `code-review` doesn't ask.
9. **Budget**: how many red tests before the next merge, and what is explicitly out. A plan the user can't finish is a plan they'll abandon; the first five have to be five.

Rules of the interview, beyond `grilling`'s:

- **Never ask what the code answers.** Whether a function is pure, whether a route checks auth, whether tests exist: look. Ask about what the code can't tell you: what matters, what's right, what's out.
- **Every claim in the user's language.** If a claim needs a variable name to make sense, rewrite it. Same test as `test-audit`, on purpose: the two lists are the same list at different times.
- **Recommend, don't lecture.** One line of why per recommendation; the reasoning lives in `tdd` and this file, not the transcript.
- **Whole-project scope ends with a ranking**, not a flat list: the Stakes answers order the claims, and the plan says which ten come first and which fifty can wait.

## 3. Write the plan

Where the tracker keeps specs: local markdown → `.scratch/<feature>/test-plan.md` (whole project: `.scratch/test-plan/test-plan.md`); a real tracker → the same file, plus an issue titled `Test plan: <scope>` whose body is the file, linked from the ticket in scope.

```
# Test plan: <scope>

Feedback loop: <the test command and single-file command from feedback-loops.md, or "none wired: run /setup-feedback-loops first">
Stakes: <the two or three behaviours from round 1, one line each>

## Claims
| # | Claim | Seam | Level | Oracle | Doubles | Now |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | A tag a note already has is not added twice | `addTag()` | unit | worked example in spec | none | missing |
| 2 | Two users never see each other's notes | `GET /notes` | integration | fixture: two users, two notes | real db, fake clock | covered by notes.test.ts:40, weak: asserts count only |
| 3 | ... | ... | ... | ... | ... | rule unconfirmed: see Open |

## Wrong paths
<claim # → the wrong paths that matter, one line each>

## Existing tests
Keep: <file:line, why>
Rewrite: <file:line, what it should claim instead>
Delete: <file:line, why>

## First red tests, in order
1. <claim #, seam, the one input and expected output>
2. ...
5. ...

## Out of scope
<what was named and left out, with the sentence that put it out>

## Open
<claims marked rule unconfirmed or oracle missing, and who can answer>
```

Then hand it back in the transcript in one screen: the Stakes lines, the claim count, the first five, the Open list. End with: **"Read the claims as business rules. Is any of them wrong?"** and wait. That sentence is the reason the plan exists.

## 4. After confirmation

Stop, and say what's next:

- **There is a ticket**: append a one-line comment to it pointing at the plan; `/implement` picks the plan up as its agreed seams and drives `tdd` through the first red tests in order.
- **No ticket, or the user says go**: invoke the "tdd" skill on the first red test, passing the claim, the seam, the oracle and the doubles decision verbatim; then the second; each one red before green. Stop after the five and hand back.
- **No feedback loop was wired**: `/setup-feedback-loops` first; nothing in the plan can be confirmed until a test can go red.
- **Any claim in Open**: that's a spec question before it's a test. Point to `refocus` if the answer should already be on disk, or to the ticket's comments if the user has to decide.

When the tests exist, `test-audit` on the same scope reads them back as claims. Its list and this plan's list should match; a claim in the plan with no claim in the audit is a test that didn't get written, and a claim in the audit with no line in the plan is a test nobody asked for.

## Rules

- **Plan, don't write.** A test written during the interview skipped the confirmation of its seam and its rule.
- **Scope first.** One question, then read, then rounds. Never open with a wall of questions about a codebase you haven't looked at.
- **Facts from the repo, decisions from the user.** Propose seams, levels and doubles from what you read; the user chooses.
- **Unconfirmed rules stay visible.** A claim the user isn't sure of goes in the plan flagged, never silently dropped and never silently assumed true.
- **The first five are five.** If the budget round says two, the section says two. The plan is sized to be finished.
