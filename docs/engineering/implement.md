## What it does

This is the compatibility entry for existing implementation calls. For new planned builds, use [implement-spec](./implement-spec.md), the recommended spec-to-code route with parallel ticket scheduling and integrated quality checks.

An explicit old invocation still follows its original current-branch execution procedure. The router preserves the human's choice and arguments.

<!-- cat-skills:conversation-doc:start -->
Conversation follows the [shared style](../../.agents/conversation-style.md): warm, gentle, and natural, with `喵！` at prose paragraph boundaries. Commands and technical artifacts stay exact.
<!-- cat-skills:conversation-doc:end -->

## When to reach for it

This entry is user-invoked. Reach for it when continuing an existing workflow that explicitly names it. New guides and planned builds recommend `/implement-spec` after the spec and associated tickets are prepared.

## Common questions

**Has my existing command disappeared?**

No. It remains available for explicit existing calls. The preferred new workflow is [to-spec](./to-spec.md) → [to-tickets](./to-tickets.md) → [implement-spec](./implement-spec.md).

**Can I pass the same bare ticket path to the recommended command?**

Use the associated spec reference. The recommended command needs that spec and its execution graph, and can handle a graph with just one ticket. A tiny concrete behavior can use [tdd](./tdd.md) directly.

## It's working if

- Existing explicit calls retain their arguments and current execution behavior.
- New planned work is directed to the recommended spec-to-code workflow.
- The handoff retains the spec and ticket context without claiming missing planning artifacts exist.

## Where it fits

A compatibility entry outside the curated daily kit. [implement-spec](./implement-spec.md) is the main implementation step; [vibe](./vibe.md) and [ask-matt](./ask-matt.md) preserve explicit old requests while recommending it for new work.
