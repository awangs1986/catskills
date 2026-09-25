## What it does

`cattytest` is the interview for the moment `tdd` assumes has already happened: someone can say which behaviours matter, at which seams they are observable, and what the right answer looks like. Half-built projects usually can't. The skill asks one scope question (this feature, or the whole project), reads the repo so it never asks what the code already answers, and then grills in rounds along nine branches: stakes, claims, seams, oracle and level, doubles, data, wrong paths, existing tests, budget. Every question carries a recommended answer drawn from the code, the ticket and `CONTEXT.md`; the user corrects sentences rather than enumerating their own codebase.

It ends with a `test-plan.md` next to the spec: numbered **claims** written as business rules in the project's vocabulary, each with a confirmed seam, a level, an oracle and a decision about what is real and what is faked; a keep / rewrite / delete sort of the tests that already exist; and the first red tests in order, sized to be finished before the next merge. It plans and does not write tests. On go it drives `tdd` through the first red tests, one at a time.

## When to reach for it

Type `/cattytest`. It is user-invoked; the agent never starts a test-planning interview on its own.

| Your situation | Reach for |
| --- | --- |
| Code exists, tests don't, and you don't know where to start | **`/cattytest`** |
| Tests exist but you suspect they are decoration | **`/cattytest`**: the existing-tests round sorts them, and the claims round says what they should have said |
| You know the seams and just want the behaviour built test-first | [tdd](https://aihero.dev/skills-tdd); this skill is for when you can't answer its seam question |
| You want to know what the tests you already have actually protect | [test-audit](https://aihero.dev/skills-test-audit); that one reads tests back as claims, this one writes the claims first |
| You want the feature seen working end to end | [verify](https://aihero.dev/skills-verify) |
| No test command runs at all | [setup-feedback-loops](https://aihero.dev/skills-setup-feedback-loops) first; `cattytest` will tell you so and still write the plan |

## Prerequisites

None hard. It reads `docs/agents/feedback-loops.md`, `docs/agents/issue-tracker.md` and `CONTEXT.md` when they exist and works without them, but a plan for a repo with no test command starts with "wire one".

## The plan is the same list twice

The claims in the plan are written to the same standard as `test-audit`'s claims: one sentence a domain expert would say, true of the product when the test is green, no variable names. That is deliberate. `cattytest` writes the list before the tests exist; `test-audit` reads it back after they do. A claim in the plan with no claim in the audit is a test that didn't get written; a claim in the audit with no line in the plan is a test nobody asked for. Both lists end with the same sentence to the user: *read these as business rules, is any of them wrong?*

## Common questions

**Why not just `/grill-me` about testing?**

You can, and it will ask reasonable questions. It won't read your existing tests first, propose seams from your entry points, know that a screenshot-shaped oracle is a `verify` step rather than a test, or refuse to let an expected value come from running the code. The question bank is the skill.

**It flagged a claim as "rule unconfirmed" and moved on. Isn't that a gap?**

It is, and it is a spec gap, not a test gap. The plan keeps it visible under **Open** with who can answer it. Writing a test for a rule nobody has confirmed produces a green test for a rule that may be wrong, which is the failure `test-audit` exists to catch later; better to name it now.

**Whole project scope gave me sixty claims.**

And a ranking. The stakes round decides which ten come first; the budget round decides how many before the next merge. Sixty claims is a true description of a project; the plan is the five you do this week.

## It's working if

- The first round asks only one thing (scope), and the second round already contains seams and claims you didn't type.
- You correct a sentence or two in the claims list, and at least one claim makes you realise you don't actually know the rule.
- The first red test in the plan goes red within a few minutes of `tdd` starting on it.
- `test-audit` on the finished work produces a claims list that matches the plan.

## Where it fits

Upstream of [tdd](https://aihero.dev/skills-tdd) and [implement](https://aihero.dev/skills-implement): it produces the agreed seams and the ordered red tests those two consume. Downstream of [setup-feedback-loops](https://aihero.dev/skills-setup-feedback-loops), which makes the tests runnable. Its counterpart is [test-audit](https://aihero.dev/skills-test-audit), which reads the written tests back as the same list of claims. [vibe](https://aihero.dev/skills-vibe) routes "I don't know how to test this" here; [ask-matt](https://aihero.dev/skills-ask-matt) is the router over the whole set.
