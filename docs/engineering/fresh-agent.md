## What it does

`fresh-agent` tidies `AGENTS.md` and related project instructions after months of additions have made them long, repetitive, or hard to navigate. It removes demonstrably obsolete guidance, consolidates duplicate rules, and groups scattered instructions so the next agent can find what matters.

The default result of a cleanup request is edited files and an explanation of the changes. Effective project constraints and explicit approval requirements survive the cleanup; shorter wording is not permission to change authority.

<!-- cat-skills:conversation-doc:start -->
Conversation follows the [shared style](../../.agents/conversation-style.md): warm, gentle, and natural, with `喵！` at prose paragraph boundaries. Commands and technical artifacts stay exact.
<!-- cat-skills:conversation-doc:end -->

## When to reach for it

Type `/fresh-agent`, or the agent reaches for it automatically when a requested instruction cleanup fits the task.

- Use it when a long-running project's `AGENTS.md` has accumulated repeated rules, old task notes, stale paths, and scattered exceptions.
- Use [fresh-spec](./fresh-spec.md) when the stale document describes software behavior.
- Use [writing-for-agents](../productivity/writing-for-agents.md) for general guidance on authoring instructions.

## Prerequisites

Readable project instructions and enough current project evidence to judge which rules still apply. Editing also needs a writable destination and a recoverable copy of the starting contents, including local changes.

## Prune with reasons

The cleanup distinguishes durable rules from accumulated clutter. Duplicate rules can be merged, but instructions with different scopes or exceptions need to retain those distinctions. Old guidance is retired only with evidence; uncertain rules stay visible for a decision. Detailed references can move out of the entrypoint only when agents can still find them at the right time.

## Common questions

**Does it actually simplify the file, or just produce an audit?**

A cleanup request produces the revised files, a before/after size comparison, and a summary of removals, merges, and moves. Ask for review only if you want proposed edits without applying them.

**Will it delete useful rules just to make the file shorter?**

No. There is no reduction quota. Project constraints, meaningful exceptions, and approval gates remain. A rule is not obsolete merely because it is old or the current implementation violates it. Unresolved conflicts are identified instead of silently choosing greater authority.

## It's working if

- You can find a rule in one appropriate place instead of piecing it together from several sections.
- Removed guidance has a concrete reason, and uncertain rules have not silently disappeared.
- The completion report shows what changed, how much the files changed in size, and which safeguards remain.
- The instructions are easier to follow without losing the conditions that made them useful.

## Where it fits

Periodic maintenance for a project's accumulated instructions. [writing-for-agents](../productivity/writing-for-agents.md) supplies the authoring discipline; [fresh-spec](./fresh-spec.md) refreshes software descriptions. [ask-matt](./ask-matt.md) maps the wider workflow.
