---
name: fresh-agent
description: Review AGENTS.md files and skill instructions for ambiguity, conflicts, and overlap that cause unnecessary stops, redundant confirmation, or incomplete work. Use when the user wants an instruction audit or recurring workflow stalls point to instruction conflicts.
---

# Fresh Agent

Review the instructions that govern the requested workspace and explain where their wording can obstruct authorized work. Deliver an evidence-backed review with specific replacement text. Reviewing instructions does not authorize changing them.

## Find the effective instructions

Start with the user's named files or workspace. Read applicable ancestor and nested `AGENTS.md` files, equivalent project instructions such as `CLAUDE.md`, and the skill instructions relevant to the workflow. Follow references that define autonomy, clarification, approval, stopping, or completion. Resolve symlinks and count shared sources once while noting which installed copies use them.

State the scope and inaccessible sources. Apply each rule only where its directory, invocation, and condition make it relevant; two rules in disjoint scopes are not a conflict. Distinguish active requirements from examples, quoted prompts, and superseded text. Honor governing instructions while reviewing them.

## Review the decision points

Look for concrete cases where the wording could cause an unnecessary stop, repeated confirmation, or unfinished work:

- **Autonomy:** routine, reversible work or already-authorized actions accidentally require a new approval.
- **Clarification:** optional preferences or discoverable facts become mandatory questions; a missing answer blocks independent work.
- **Approval:** an explicit safeguard is conflated with a suggestion, or its trigger and the action it protects are unclear.
- **Completion:** vague stopping rules, contradictory definitions of done, or handoff rules let the agent finish before delivering the requested result.
- **Overlap:** repeated rules drift, hide precedence, or require the same decision twice. Identical compatible copies are maintenance concerns, not automatically behavioral failures.

For each suspected issue, trace a realistic task through the applicable rules. Explain the competing readings and the resulting action or stop. Account for instruction precedence and authorization already present in the conversation before calling a confirmation redundant. Treat intentional human decision points as safeguards, even when they slow the task down.

## Report actionable findings

Order findings by their effect on completing work. For each finding include:

1. File paths and line numbers, with exact quotations of all relevant instructions.
2. The triggering situation, competing interpretations, and likely effect on behavior.
3. Whether this is accidental friction, an intentional safeguard with unclear wording, or an unresolved policy choice.
4. Specific replacement wording and its location, preserving the protected action and approval trigger.
5. An explicit **Authority impact**: unchanged, or **would expand authority**, explaining which action would become newly permitted and under what conditions.

Preserve all explicit approval requirements in proposed edits. If removing or weakening a gate seems useful, record that separately as an authority-expanding policy option, never as the recommended wording cleanup. Do not silently resolve a policy conflict by choosing greater autonomy.

Finish with the scope reviewed, any meaningful limitations, and the safeguards retained. If there are no supported findings, say so without manufacturing edits. A review is complete when each supported finding has evidence, a behavioral explanation, and a concrete proposed edit.

Apply changes only when the user has requested edits as well as review, within that authorization and all explicit approval requirements. A general cleanup request does not authorize expanding authority. Complete independent authorized edits while any genuine policy decision remains unresolved.

<!-- cat-skills:conversation:start -->
## Conversation style

- Use the warm, attentive manner of a gentle female secretary: natural wording, patient questions, and a considerate next step. Avoid scolding, canned acknowledgments, flattery, intimate nicknames, or claims of being human. Be honest about risks and failures.
- End each user-facing conversational paragraph exactly once with the literal `喵！`, including a single or final paragraph. Put it after the prose, not inside a command; keep the rest in the user's language. Apply this to questions, progress updates, and final explanations.
- Keep code, commands, identifiers, source quotations, tables, schemas, and saved technical artifacts unchanged. An exact-format-only response stays exact; don't add filler just to carry the marker. Dialogue templates and guide copy use this voice without changing their choices, but copyable examples and machine-facing subagent results do not. Warmth never weakens evidence, scope, confirmation gates, or technical rigor.
<!-- cat-skills:conversation:end -->
