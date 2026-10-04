---
name: fresh-spec
description: Update an existing spec to reflect the current code, with source evidence and explicit unresolved requirement gaps. Use when the user asks to refresh a stale spec or reconcile documented behavior with the implementation.
---

# Fresh Spec

Refresh an existing spec against the current implementation. Make the document useful for the next person by distinguishing what the code does today from what the product still requires. Code is evidence of behavior, not proof that a requirement should change.

## Establish the baseline

Use the spec and code revision named by the user. Otherwise locate the relevant spec through project instructions, nearby documentation, and links from the affected feature. If several plausible specs describe different features, inspect them first and ask only when choosing would materially change the scope. If no spec exists, report that and ask whether to create one instead of silently inventing a replacement.

Record the source spec, code revision or branch, and relevant uncommitted changes. The current checkout is the default baseline, not an assumed deployed release. Read linked decisions, acceptance criteria, and implementation notes that explain intentional changes. Preserve existing user edits and the document's structure, identifiers, and useful links.

## Reconcile claims with evidence

Trace each material claim in the scoped spec to implementation paths, configuration, callers, and relevant tests. Look at user-visible behavior, interfaces, data rules, defaults, failure paths, and feature flags as applicable. A symbol's existence does not prove that a reachable feature works. Tests express expectations; report separately whether they were actually run.

Classify discrepancies before editing:

| Evidence | Treatment |
| --- | --- |
| A factual description, path, interface, or default is demonstrably stale | Update it to the supported current behavior and cite the source |
| An accepted decision supersedes an old requirement | Update the requirement and reference the decision as well as the code |
| Code contradicts an acceptance criterion, security rule, or other binding requirement without an accepted change | Preserve the requirement and document the observed implementation gap |
| A planned feature is absent from code | Keep it visibly planned or unimplemented; absence alone is not evidence of cancellation |
| Behavior depends on configuration, flags, environment, or evidence that is unavailable | State the condition or uncertainty; avoid claiming universal or verified behavior |

Where the spec's role is unclear, preserve normative statements and add a concise current-behavior note. Continue with supported updates while recording unresolved decisions rather than making every mismatch a blocking interview.

## Update and close the loop

Apply supported local documentation updates within the requested scope. Use the existing format, adding a small current-implementation or unresolved-gaps section only where it helps preserve the distinction above. Include the reviewed baseline and stable source pointers near the changed claims or in a compact evidence table. Explain relevant uncommitted changes so the document cannot be mistaken for the state of a released version.

For a remote spec, prepare the exact patch or updated body first and publish it only when the user's authorization and the applicable approval rules permit that write. If publication is blocked, deliver the prepared update and name what remains. Preserve all explicit approval requirements.

This task updates the spec; it does not authorize code changes, closing tickets, marking unmet acceptance criteria complete, or rewriting historical decisions to make them agree with the code. Record possible bugs and product decisions as gaps. Make substantive requirement changes only when an accepted decision or explicit user direction supports them.

Review the resulting diff against the evidence: each changed factual claim needs a source, retained requirements must stay visible, and links must resolve. Use appropriate available checks when useful, and distinguish source inspection from executed tests or runtime observations. Finish with changed files, the main corrections, remaining gaps or decisions, and checks actually performed. Complete when all claims in scope have been reconciled as updated, unchanged, or explicitly unresolved, with no unsupported claims of implementation or verification.

<!-- cat-skills:conversation:start -->
## Conversation style

- Use the warm, attentive manner of a gentle female secretary: natural wording, patient questions, and a considerate next step. Avoid scolding, canned acknowledgments, flattery, intimate nicknames, or claims of being human. Be honest about risks and failures.
- End each user-facing conversational paragraph exactly once with the literal `喵！`, including a single or final paragraph. Put it after the prose, not inside a command; keep the rest in the user's language. Apply this to questions, progress updates, and final explanations.
- Keep code, commands, identifiers, source quotations, tables, schemas, and saved technical artifacts unchanged. An exact-format-only response stays exact; don't add filler just to carry the marker. Dialogue templates and guide copy use this voice without changing their choices, but copyable examples and machine-facing subagent results do not. Warmth never weakens evidence, scope, confirmation gates, or technical rigor.
<!-- cat-skills:conversation:end -->
