## What it does

`fresh-agent` reviews project and skill instructions for wording that can make an agent stop unnecessarily, request the same confirmation twice, or leave authorized work incomplete. Every finding quotes the instructions, locates them, explains the behavioral consequence, and proposes exact replacement wording.

Explicit approval requirements remain intact. A possible expansion of authority is identified separately as a policy decision, rather than slipped into a wording cleanup.

<!-- cat-skills:conversation-doc:start -->
Conversation follows the [shared style](../../.agents/conversation-style.md): warm, gentle, and natural, with `喵！` at prose paragraph boundaries. Commands and technical artifacts stay exact.
<!-- cat-skills:conversation-doc:end -->

## When to reach for it

Type `/fresh-agent`, or the agent reaches for it automatically when an instruction audit fits the task.

- Use it when overlapping autonomy, clarification, approval, or completion rules keep interrupting routine work.
- Use [fresh-spec](./fresh-spec.md) when the stale document describes software behavior.
- Use [writing-for-agents](../productivity/writing-for-agents.md) when you need general guidance for authoring instructions.

## Evidence before edits

The review follows each rule's scope and trigger before judging it. A real approval boundary stays a boundary; repeated compatible wording may only need a maintenance note. The output gives you a concrete situation and a proposed edit you can assess, including its effect on authority.

## Common questions

**Will it remove approvals to make the agent faster?**

No. The proposed cleanup preserves explicit approvals. Any alternative that would grant more authority is flagged separately for a policy decision.

**Does invoking it change my instruction files?**

The default deliverable is a review. If you also request edits, it applies authorized changes while preserving the approval requirements; general cleanup permission does not grant wider authority.

## It's working if

- You can find every quoted rule at the reported file location.
- Each finding describes a recognizable unnecessary stop or incomplete outcome.
- The replacement text preserves the original safeguard, and any authority expansion is plainly flagged.

## Where it fits

A standalone maintenance tool for instructions. [writing-for-agents](../productivity/writing-for-agents.md) helps write the resulting wording; [fresh-spec](./fresh-spec.md) maintains software descriptions. [ask-matt](./ask-matt.md) maps the wider workflow.
