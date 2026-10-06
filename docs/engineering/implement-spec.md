## What it does

`implement-spec` is the recommended entry for turning a prepared [spec](https://www.aihero.dev/ai-coding-dictionary/spec) and its [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) into working code. An orchestrating [agent](https://www.aihero.dev/ai-coding-dictionary/agent) runs ready tickets in isolated git worktrees, integrates their commits on one branch, and validates the complete result before tracker close-out.

The tickets are a **task graph**. Blocking relationships decide the ready **frontier**, so independent work runs in parallel and newly integrated blockers unlock more work. A graph with one ticket is valid too; you keep one implementation entry as the feature grows.

<!-- cat-skills:conversation-doc:start -->
Conversation follows the [shared style](../../.agents/conversation-style.md): warm, gentle, and natural, with `喵！` at prose paragraph boundaries. Commands and technical artifacts stay exact.
<!-- cat-skills:conversation-doc:end -->

## When to reach for it

You invoke this by typing `/implement-spec`; the agent won't reach for it on its own.

| Your situation | Next step |
| --- | --- |
| A prepared spec and associated tickets, large or small | `/implement-spec <spec reference>` |
| Agreed planning is still only in the conversation | [to-spec](./to-spec.md), then [to-tickets](./to-tickets.md) as needed |
| A tiny, concrete behavior with no planning questions | [tdd](./tdd.md) directly |
| Work was interrupted | Resume from the spec, ticket statuses, and recorded integration commits; preserve completed work |

## Prerequisites

- A settled spec, associated execution tickets, and real blocking relationships. Local product drafts or decision-map tickets need preparation before execution.
- [setup-matt-pocock-skills](./setup-matt-pocock-skills.md) has configured the issue tracker and domain pointers.
- A [harness](https://www.aihero.dev/ai-coding-dictionary/harness) able to run implementer [subagents](https://www.aihero.dev/ai-coding-dictionary/subagent) in isolated worktrees. Parallelism is limited by both the graph and the available workers.
- Project check commands. [setup-feedback-loops](./setup-feedback-loops.md) can wire missing checks; an existing feedback-loop record supplies commands and timings.

## One integration branch, one quality loop

Workers claim tickets, build with [tdd](./tdd.md), run fast checks, and refresh from the integration tip before handing work back. Successfully integrated ticket work advances the graph. Tracker closure waits for final acceptance, so PR-backed tickets do not deadlock the frontier just because they remain open until merge.

After integration, the orchestrator runs typecheck and the full suite, then [verify](./verify.md) against the spec, every ticket's criteria, and any `test-cases.md`; then [test-audit](./test-audit.md); then [code-review](./code-review.md), whose conditional security review also applies. FAILs, mutation survivors, uncovered criteria, and findings return to red-test repairs. Affected checks and review repeat on the latest integration tip before close-out.

Read the audit's **Claims** list. If a business rule is wrong, clarify the requirement before repairing the implementation. Unverifiable and by-hand cases stay visible. The final **Checks run** record lists actual commands, results, evidence, the integration commit, tracker state, and worktree cleanup.

## Common questions

**Does this overlap the old implementation command?**

Both build agreed work. This is now the recommended planned-build route, with task-graph scheduling, isolated worker contexts, and integrated quality checks. The older entry is retained for compatibility with explicit existing calls.

**Do I need several tickets before using it?**

No. One demoable ticket is enough for a small planned feature. Independent tickets run in parallel when there are several; a dependency chain runs in order. Keep the planning proportional to the work.

**Must I open a PR or merge it?**

No. A draft PR is used when the tracker closes through PRs or you request one, after the branch has a first integrated commit. Otherwise the result is the integration branch and configured tracker close-out. Publishing and merging follow the task's existing authorization.

**Two workers touch the same file. What prevents collisions?**

Worktrees isolate edits but do not eliminate merge conflicts. Use blocking edges for dependent work and shared exploration notes for names and interfaces. Resolve conflicts against the agreed spec and preserve existing work.

**A blocker has merged, but its PR-backed ticket is still open.**

The orchestrator computes progress from recorded integration commits as well as the starting graph. Formal tracker closure follows final acceptance, rather than holding all dependents until the PR merges.

## It's working if

- Independent ready tickets use separate worktrees and run concurrently when workers are available.
- Newly integrated blockers unlock dependent tickets without restarting the coordinator.
- The integrated result has verification evidence, readable Claims, and a review of its latest commits.
- No known FAIL, audit repair, or review finding is hidden by a green test summary.
- The checks ledger, integration commit, and tracker close-out agree, with preserved work reported honestly.

## Where it fits

The recommended implementation step of the main chain:

```text
grill-with-docs → to-spec → to-tickets → implement-spec → retro
```

[to-tickets](./to-tickets.md) prepares the graph; [verify](./verify.md), [test-audit](./test-audit.md), and [code-review](./code-review.md) validate the result. [vibe](./vibe.md) recommends the next step for solo work, and [ask-matt](./ask-matt.md) maps the whole collection.
