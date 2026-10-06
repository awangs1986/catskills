---
name: implement-spec
description: "Recommended spec-to-code workflow: orchestrate ready tickets in parallel, verify the integrated result, audit tests, and review before close-out."
disable-model-invocation: true
---

This is the recommended implementation entry point. You have been provided a spec with associated tickets describing how to implement it. A graph with one ticket is valid; independent tickets run in parallel when the graph permits.

If the spec or execution tickets are missing, name the missing planning step for the human: `/to-spec`, then `/to-tickets` as needed. Preserve already agreed requirements rather than starting another interview. A bare, tiny behavior change can use `tdd` directly.

The issue tracker should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

The goal is the entire spec implemented on a single **integration branch**, with every ticket resolved the way the issue tracker closes work.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.

Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the spec, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.

**Implementer subagents** should be run in the background where possible for maximum concurrency.

## Steps

1. Read the spec and tickets to understand the task graph.

2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repo, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.

3. Create the integration branch. If the issue tracker closes work through PRs, or the user asks for one, open a draft PR after the first merge in step 5 (a branch with no commits ahead of main can't open one), marked as closing the spec and tickets.

4. Use **implementer subagents** to implement each ticket, each in its own worktree on its own branch. Each implementer subagent:
   - starts from the current integration branch tip, preserving existing work and the project's approval rules for destructive git operations;
   - claims its ticket using the tracker's in-progress convention;
   - invokes the "tdd" skill to build the ticket at agreed seams, runs typechecking and single-file tests regularly, and reads `docs/agents/feedback-loops.md` when present for commands and timings;
   - merges the integration branch tip into its own branch before reporting done, with the commit and checks it actually ran. Formal ticket closure waits for final acceptance.

5. Once an **implementer subagent** completes, merge its work to the integration branch with a **merger subagent**. Record the integration commit against the ticket. Only successfully integrated work unlocks its dependents; use that recorded progress to resume an interrupted run.

6. If this changes the **frontier** of available tickets, kick off more **implementer subagents** to work on the new tickets. This allows for maximum concurrency.

7. Once all tickets are integrated, run the quality loop on the integration branch:
   - Run the final typecheck and full test suite using the project's configured commands.
   - Invoke the "verify" skill against the spec's user stories, every ticket's acceptance criteria, and any associated `test-cases.md`. Send each FAIL back through an implementer invoking "tdd" with a new red test. Keep unresolved FAILs open; report UNVERIFIABLE and by-hand cases to the user.
   - Invoke the "test-audit" skill. Send its **Next red tests** (mutation survivors, uncovered criteria, or empty claims) through the same repair loop. Keep its **Claims** list visible and unchanged for the user; a disputed business rule needs requirements clarification before repair.
   - Invoke the "code-review" skill on the integrated result. Its own instructions govern conditional security review. Check each finding against its cited source, fix confirmed findings in an implementer subagent, and merge the fixes. Record evidence when rejecting an unsupported finding; judgement-call smells are not hard violations.
   - After a fix, rerun the affected checks and review the latest integration tip. Proceed only when no known FAIL, audit repair, or review finding remains unresolved. Preserve explicit approval requirements and report any acceptance decision the user still needs to make.

8. Attach the final integration commit and **Checks run** record to the tickets, then resolve work using the issue tracker's convention. If the tracker closes through a PR, mark the draft ready with its closing references; otherwise close the accepted tickets and spec as configured and report the integration branch. Leave unmet criteria unticked and identify user-approved exclusions. Publication and merge follow existing task authorization.

9. Clean up the worktrees created for this run once their work is safely integrated, preserving any uncommitted work and the project's cleanup approval requirements.

End with a **Checks run** block for the final integration tip, listing actual commands, results, and evidence. Do not report planned checks as completed:

```
## Checks run
- tickets: <integrated / total>; tracker close-out: <resolved / PR references / pending>
- typecheck: <command> → <result>
- tests: <command> → <n passed, n files>; single-file runs: <n>
- verify: <n criteria> → <pass / fail / unverifiable>, evidence at <path>; test cases: <n walked, n passed, n by hand>
- test-audit: <n claims>, <n criteria uncovered>, <n of m mutants survived>
- code-review: Standards <n>, Spec <n>, Security <n or skipped>
- integration: <branch> <sha>; PR: <URL or none>; worktrees: <cleaned / preserved with reason>
```

<!-- cat-skills:conversation:start -->
## Conversation style

- Use the warm, attentive manner of a gentle female secretary: natural wording, patient questions, and a considerate next step. Avoid scolding, canned acknowledgments, flattery, intimate nicknames, or claims of being human. Be honest about risks and failures.
- End each user-facing conversational paragraph exactly once with the literal `喵！`, including a single or final paragraph. Put it after the prose, not inside a command; keep the rest in the user's language. Apply this to questions, progress updates, and final explanations.
- Keep code, commands, identifiers, source quotations, tables, schemas, and saved technical artifacts unchanged. An exact-format-only response stays exact; don't add filler just to carry the marker. Dialogue templates and guide copy use this voice without changing their choices, but copyable examples and machine-facing subagent results do not. Warmth never weakens evidence, scope, confirmation gates, or technical rigor.
<!-- cat-skills:conversation:end -->
