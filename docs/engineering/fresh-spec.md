## What it does

`fresh-spec` updates an existing [spec](https://www.aihero.dev/ai-coding-dictionary/spec) using evidence from the current code. It records the reviewed revision, refreshes stale descriptions, and makes unresolved differences visible.

Current behavior does not automatically supersede intended behavior. Unmet requirements stay visible unless an accepted decision or explicit direction changes them.

<!-- cat-skills:conversation-doc:start -->
Conversation follows the [shared style](../../.agents/conversation-style.md): warm, gentle, and natural, with `喵！` at prose paragraph boundaries. Commands and technical artifacts stay exact.
<!-- cat-skills:conversation-doc:end -->

## When to reach for it

Type `/fresh-spec`, or the agent reaches for it automatically when the task is to refresh an existing spec from implementation evidence.

- Use it after implementation or refactoring has left the spec out of date.
- Use [to-spec](./to-spec.md) to turn an agreed conversation into a new spec.
- Use [refocus](./refocus.md) when ongoing work has drifted from its requirements.
- Use [fresh-agent](./fresh-agent.md) when the stale or conflicting material governs the agent's own behavior.

## Prerequisites

An existing spec and access to the relevant code. A named revision is useful when you need a release snapshot; otherwise the current checkout, including relevant local changes, is the baseline.

## Current behavior and remaining requirements

The updated document distinguishes supported facts, accepted requirement changes, implementation gaps, and uncertainty. A feature flag or a test assertion alone cannot prove that a feature is available to every user. Source references let the next reader check the claims without reconstructing the whole investigation.

## Common questions

**Will a missing feature disappear from the requirements?**

No. Planned behavior remains planned, and an unmet acceptance criterion remains a gap. The skill updates requirements only with a supporting decision or explicit user direction.

**Does it fix the implementation or publish the spec?**

It updates local documentation in scope. Code fixes are separate work. A remote update requires authorization for that write; otherwise the deliverable is a prepared update with the remaining publication step identified.

## It's working if

- The refreshed document identifies which checkout or revision it describes.
- Changed behavioral claims have concrete code or decision references.
- You can distinguish shipped or implemented behavior from pending requirements and uncertain behavior.
- The completion report says which checks ran and which conclusions came only from source inspection.

## Where it fits

A standalone maintenance tool after code evolves. [to-spec](./to-spec.md) creates a spec from agreed intent, while [refocus](./refocus.md) restores that intent during a drifting session. [ask-matt](./ask-matt.md) maps the wider workflow.
