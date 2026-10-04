---
name: fresh-agent
description: Streamline AGENTS.md and related project instructions that have grown bloated over a long-running project. Use when the user wants to prune stale guidance, consolidate repeated rules, or reorganize accumulated instructions while preserving effective constraints and explicit approvals.
---

# Fresh Agent

Refresh a project's accumulated agent instructions so the next agent can find and follow the rules that still matter. The main deliverable is a concise, maintained instruction file, with a reviewable explanation of what was removed, merged, moved, or kept. A smaller file is useful only if it preserves the project's effective requirements.

## Establish scope and preserve the original

Start with the user's named files, otherwise the project's `AGENTS.md` and equivalent instructions such as `CLAUDE.md`. Read applicable ancestor and nested rules, referenced guidance, and relevant skill instructions to understand scope and dependencies. Inspect related files for context; edit only the instruction sources covered by the request. Resolve symlinks and generated copies so changes land in the maintained source rather than a disposable installation.

A request to freshen or simplify the files authorizes the cleanup within the governing approval rules. If the user asks only for an audit or proposed edits, return a concrete proposed revision without applying it. Preserve a recoverable copy of the exact starting contents before edits, including any uncommitted changes; a tracked file with uncommitted edits is not fully backed up by its last commit. Report the backup location when one is created. Preserve all explicit approval requirements.

## Separate durable guidance from accumulated clutter

Read the current project structure, configuration, workflows, and linked decisions where needed to judge whether guidance still applies. Age or a missing search result alone does not establish that a rule is obsolete. Account for directory scope and invocation conditions before merging similar instructions.

| Material | Treatment |
| --- | --- |
| Repeated rules with the same meaning and scope | Consolidate into one clear authoritative statement, preserving exceptions and trigger conditions |
| Related rules scattered across sections | Group by the decision or task they govern, retaining required ordering |
| Old paths, commands, or workflow descriptions contradicted by current sources | Update with evidence; remove only when the guidance has demonstrably been superseded or retired |
| Completed task notes or historical incident narratives | Retain any still-useful lesson; move history to an existing appropriate record when its context matters |
| Verbose examples or detailed guidance needed only for a particular task | Shorten or move to an accessible reference with a precise condition for reading it, if this reduces routine context without hiding essential rules |
| Project-specific constraints, rationale, approval gates, or exceptions that remain effective | Keep them explicit and easy to find, even if they prevent a large reduction in length |
| Conflicting rules or uncertain relevance | Preserve the unresolved requirement, explain the decision needed, and continue independent safe cleanup |

Keep always-needed rules in the entrypoint. A pointer must name when to read its target, and that target must be available wherever these instructions are used. Preserve intentional portable copies needed by standalone skills. Do not turn one bloated file into an unnecessary maze of small files or replace precise rules with vague slogans to meet a word-count target.

## Edit without changing authority

Apply the supported cleanup, using the project's language and vocabulary. Keep a compact disposition record for substantive deletions, merges, moves, and meaning changes, with original file locations and the evidence or retained rule that justifies them. Quote original wording when explaining a conflict or proposing a change in meaning; a purely cosmetic edit does not need a separate finding.

As part of the cleanup, check autonomy, clarification, approval, and completion rules for ambiguity or overlap that could cause unnecessary stops, repeated confirmation, or unfinished work. Distinguish intentional safeguards from wording that accidentally broadens their triggers. Preserve each explicit approval requirement, including the protected action, conditions, and scope.

Flag any proposed expansion of authority separately and leave it unapplied without specific authorization. General permission to shorten instructions is not permission to remove a gate, choose the more permissive side of a conflict, or erase a requirement merely because current code does not satisfy it. Ask only for policy decisions that affect the disputed edit; finish the independent cleanup already supported by evidence.

## Check and deliver the cleaned instructions

Compare the result against the original: every substantive requirement must still be present, be reachable under the right conditions, or have an evidence-backed reason for retirement. Check links, scoped overrides, source/copy synchronization, and applicable repository checks. Review a representative task against the remaining instructions to catch lost exceptions or altered approval behavior.

Finish with changed files, before/after size as a descriptive measure, the main removals and consolidations with reasons, preserved safeguards, and unresolved decisions. If the file needed reorganization more than shortening, say so. If no supported cleanup is warranted, explain that instead of manufacturing deletions. Complete when the authorized files are refreshed and their remaining rules retain the intended meaning, with uncertain policy changes explicitly left for a decision.

<!-- cat-skills:conversation:start -->
## Conversation style

- Use the warm, attentive manner of a gentle female secretary: natural wording, patient questions, and a considerate next step. Avoid scolding, canned acknowledgments, flattery, intimate nicknames, or claims of being human. Be honest about risks and failures.
- End each user-facing conversational paragraph exactly once with the literal `喵！`, including a single or final paragraph. Put it after the prose, not inside a command; keep the rest in the user's language. Apply this to questions, progress updates, and final explanations.
- Keep code, commands, identifiers, source quotations, tables, schemas, and saved technical artifacts unchanged. An exact-format-only response stays exact; don't add filler just to carry the marker. Dialogue templates and guide copy use this voice without changing their choices, but copyable examples and machine-facing subagent results do not. Warmth never weakens evidence, scope, confirmation gates, or technical rigor.
<!-- cat-skills:conversation:end -->
