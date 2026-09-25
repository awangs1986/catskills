---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

**Claim the ticket first.** On a local tracker set its `Status:` line to `in-progress`; on GitHub or GitLab, assign yourself and comment that work has started. This is what lets a later session (or `/vibe`) see what was in flight. Skip only when there is no ticket (a spec alone, or a conversation).

Use /tdd where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end. If `docs/agents/feedback-loops.md` exists, it names the commands and how long each takes; use those.

Once the suite is green, invoke the "verify" skill to run the built thing against the ticket's acceptance criteria. Each FAIL it reports goes back into the /tdd loop as a new red test. Do not proceed with a FAIL open; UNVERIFIABLE rows go to the user.

Then invoke the "test-audit" skill. Its **Next red tests** (mutation survivors, uncovered criteria, tests that claim nothing) go back into the /tdd loop before review. Leave its **Claims** list in the transcript untouched: the user reads it as business rules, and a wrong claim there is the finding that matters most.

Then use /code-review to review the work.

Commit your work to the current branch.

**Close the ticket.** On a local tracker set `Status:` to `done` and append, under `## Comments`, the commit sha and the Checks run block below; on GitHub or GitLab, post the same as a comment and close the issue (or leave it open with a `done` label if the repo's conventions want a human to close). Tick the acceptance criteria you met; leave unticked any the user accepted as out of scope, and say so. Never touch the parent spec issue; `to-tickets` owns that.

End with a **Checks run** block so the user can see what was actually checked, not just that it passed:

```
## Checks run
- typecheck: <command> → <result>
- tests: <command> → <n passed, n files>; single-file runs: <n>
- verify: <n criteria> → <pass / fail / unverifiable>, evidence at <path>
- test-audit: <n claims>, <n criteria uncovered>, <n of m mutants survived>
- code-review: Standards <n>, Spec <n>, Security <n or skipped>
- commit: <sha> <subject>
```
