# Conversation and routing evaluation scenarios

These are behavioral acceptance scenarios, not a claim that a model has passed them. The automated tests cover packaged rules, route coverage, and Askcat's actual renderer; a human or a multi-turn agent harness must still evaluate the conversational behavior below.

## Portable voice

| Situation | Expected behavior |
| --- | --- |
| Invoke a single copied `SKILL.md` in a project without setup | The local conversation block supplies the gentle voice and paragraph marker without needing this repository's root instructions |
| Invoke a model-reachable skill such as `tdd` or `research` directly | Human-facing explanations use the same voice; internal machine-facing results keep their schema |
| Start a new interview, then answer "I don't know" | Patient explanation and a helpful recommendation; no ridicule, pressure, or invented user decision |
| A test fails or a security check blocks shipping | Calm and explicit about the failure; no softened verdict or unsupported reassurance |
| A reply has one paragraph, several paragraphs, or a prose list | Exactly one `喵！` at each conversational paragraph boundary, including the final paragraph; no standalone marker-only paragraph |
| The user speaks a different language | Surrounding prose follows that language; the literal marker stays unchanged |
| Return an exact JSON object, a command, a quotation, a table, or a SPEC file | The technical output remains exact. No decorative suffix in values, paths, status cells, quoted evidence, or saved artifact prose |
| A wrapper invokes another skill and reports its result | One coherent voice in the parent reply, with no doubled suffixes from nested output |
| Run setup a second time | One updated `Agent skills` section and one conversation sub-block; unrelated project instructions remain intact |

## Vibe boundaries

| Request | Expected route |
| --- | --- |
| Product experience unclear in an empty repo | `tell-a-story` before setup or sizing |
| Explain the installed kit in an empty repo | `askcat`, not a forced first-run setup card |
| Continue from an old export without tracker config | `takeover` with the record; no fresh feature interview |
| The experience is agreed but proof cases are missing | `cattytest` |
| Existing acceptance cases need to be run | `verify` |
| What do these existing tests actually protect? | `test-audit` |
| Which library or how does this API work? | `research`; it is not mistakenly excluded from the kit |
| A greenfield effort has many unresolved decisions across sessions | `wayfinder`; story alignment first only when the destination is unclear |
| User names a specific available command | Read its actual instructions and honor the target rather than matching a broad keyword |
| A user-invoked command is absent from the model's implicit list | Check accessible installation files or a manifest before calling it missing |
| A beta command is mentioned | Verify installation and label it beta; do not silently treat it as shipped |
| A route is chosen | One short, considerate explanation and a clean command card; no unauthorized invocation |
| `/vibe implement this prepared spec .scratch/search/spec.md` with tracker and tickets ready | Build L execution, `/implement-spec .scratch/search/spec.md`, no size or lane interview. The human starts the skill; only its source-defined integration checks are promised |
| The same whole-spec request has no tracker configuration | The specific setup prerequisite is the next step; retain the spec reference for the return to execution, without restarting product alignment |
| The spec exists but its tickets have not been prepared | Name ticket preparation as the missing step; do not claim a ready graph or begin orchestration |
| `/vibe write the PR body for this branch against main` in a repo without setup files | Read `pr` and offer the body-writing route under the existing confirmation gate. No forced setup, no invented evidence, no publication or merge implied |
| `/vibe retro on session export.json` with no tracker or feedback-loop record | Preserve `export.json`, name `/retro export.json`, and stop. No setup detour or environment changes; the human starts the retrospective |
| `/vibe retrospect on this session` with no supplied record | Name `/retro` for the current session rather than requiring an export |
| "Checkout is failing again; fix it" | Fix, even though the failure recurs; no automatic retrospective as the repair step |
| "Fix this recurring checkout failure and tell me how the agent could have prevented it" | Fix first and `/retro` in Then, unless the user explicitly chooses another order |
| User says "go" after a route to `/implement-spec` or `/retro` | Preserve the target's user-only invocation policy and name the exact command for the human |

## Askcat inventory and presentation

- Link one skill into multiple harness directories: one card, one count, one progress identity.
- Provide different versions under project and user paths: select the effective source with evidence, or ask when precedence is unknown.
- Show only a repository checkout: visibly label a catalog, not a verified installation.
- Install a new promoted skill: its inventory entry and card appear together; the old hard-coded count is never reused.
- Install a partial kit: no unavailable picker target or first-run command is invented.
- Include `tell-a-story`: show the calico storyteller, both narrator choices, revisions and confirmation, and the draft-only boundary.
- Open the HTML from disk: it loads without outside assets, and examples remain copyable while narration uses the paragraph marker.
- Deny browser storage: progress works while the page remains open, without claiming persistence after reload.
- Include `implement-spec`, `pr`, and `retro`: each picker result reaches the matching card with its context-bearing prompt. The first and third are user-invoked; `pr` is model- or user-reachable; none is labelled beta.
- Explain `implement-spec`: show the prepared spec, tickets, and tracker prerequisites, newly unblocked work, integration review, and tracker-dependent close-out. Do not promise the per-ticket fork's extra checks automatically.
- Explain `pr` with missing before/after evidence: identify the missing evidence, keep the body-writing boundary visible, and never invent a test run or claim the PR was published.
- Explain `retro` on a supplied record: preserve the record, link ranked candidates to observed session problems, and leave changes for the user's choice. Keep live bug repair distinct.
- Install any subset of the three: only the available cards and picker leaves appear; no absent command enters the first-run sequence.

## Tell a Story: understanding an existing project

These scenarios need a live conversational run; static checks alone cannot establish that the narration feels natural.

| Situation | Expected behavior |
| --- | --- |
| User chooses mode 2 in an unfamiliar repository | Read the source, infer its central supported purpose, and tell continuous prose about a person whose concrete problem changes through using the project; no numbered feature tour or visible scene IDs |
| A long-running project has many unrelated-looking capabilities | Choose a representative journey explaining why someone needs the project, rather than including every module or following the code-reading order |
| Agent adds a character's name to five interchangeable feature descriptions | Rewrite before sending: events must be causally connected, and the ending must change what the person can know, decide, or do |
| Project is a library or background service | Ground the story in a developer's or operator's real problem without inventing a dashboard or unsupported end-user actions |
| Documentation promises a result but the reachable implementation stops short | Let the limit affect the ending, and put source evidence and uncertainty after the story; no invented successful save, payment, or notification |
| User confirms that the story captures what the existing project is for | Treat understanding as a complete result; no mandatory redesign, requirements interview, or artifact selection |
| User asks to convert the story after correcting it | Preserve the explicit latest-story confirmation gate, then keep the prose intact in the saved story and add a separate scene map for requirement references |
