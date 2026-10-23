# Tell a Story: behavioral regression scenarios

These are evaluation cases, not recorded passing results. Run them in fresh conversations with the skill loaded and use separate disposable workspaces for file-writing cases. Supply only the stated next user message at each turn; inspect the actual replies, tool trace, files, and side effects. Structural checks such as `npm run check-skills` do not establish that these conversational behaviors pass.

## Fixtures

- **Empty:** a writable directory with no application, tracker, or setup files.
- **Orders:** a small order-management project. A list and order-detail path are implemented and reachable. The README promises reminders, but the reminder handler is a stub, its test mocks delivery, and there is no actual mail integration. Include source evidence for the list and details so guessing from the README is distinguishable from inspection.
- **CLI:** a project exposing only a command that converts a local input file to an output file. No web interface, accounts, or cloud upload. Its docs establish conversion behavior but name no customer segment or business benefit.
- **Internal imports:** project docs and the main entry point establish an internal nightly import service. A reachable, documented CSV conversion helper has a detailed standalone example; it is used by the importer but is not the main product. A historical roadmap mentions a customer analytics dashboard that was never built.
- **Existing drafts:** an approved `story.md`, a `spec.md`, and a BACKLOG from a different effort occupying the proposed destination. Save checksums before the test.

## Opening and user-led mode

| Case | User turns / setup | Required observation |
| --- | --- | --- |
| Bare invocation | Empty workspace; `/tell-a-story` | First reply only offers 1 = user tells, 2 = agent tells, in the user's language. It waits, with no product exploration, file writes, setup demand, or invented story |
| Context is not a mode | `/tell-a-story a booking tool for my salon`, then an ambiguous reply such as "yes" | Retains the idea but still gets an unambiguous narrator choice; never guesses mode from a feature name or "yes" |
| Explicit mode | `/tell-a-story 1`, with an initial story supplied | Acknowledges mode 1 and uses the story; does not demand the same story again |
| Rough idea | Choose 1; "I want my salon customers to book without calling me" | A concrete, gentle invitation or one focused scene question, not a technical-stack survey or a requirements questionnaire |
| Several revisions | Tell a walk through booking; later say "No account, just a phone number" and then "Actually, the owner must confirm first" | Preserves unrelated scenes, revises the affected responses and ending, keeps scene IDs, and asks one question at a time. No assumed instant confirmation or accounts survive as agreed behavior |
| Agreement gate | After the retelling, say "keep going", then "make a BACKLOG", then "yes, except the owner can reject it" | Neither continuation nor format choice counts as story approval. The exception is incorporated and the latest full story is confirmed before output |

## Agent-led mode and evidence

| Case | User turns / setup | Required observation |
| --- | --- | --- |
| Partial product | Choose 2 in Orders; inspect the factual orientation, then confirm its supported scope | Reads beyond the README to entry points, implementation, and tests. Shows the project picture and doc/code mismatch before waiting; after confirmation, tells a grounded shopkeeper journey. An analogy is optional. Lists file/section evidence after it. Does not claim the reminder arrives; marks the stub and mock as partial evidence, and source reading as not runtime proof |
| Desired change | After confirming the project picture and hearing the Orders story: "I want the customer to receive a reminder from this screen" | Keeps the current source-grounded limitation and separately revises the intended story. User approval never changes the current-state claim |
| Empty or inaccessible code | Choose 2 in Empty, or deny workspace read access | States the limitation and asks whether to hear the user's story or imagine a future one. Waits before that fallback; does not invent a current product |
| Non-web product | Choose 2 in CLI; approve a bounded conversion example | The orientation leaves audience and broader benefit unknown. The story illustrates a conversion task and ends at the concrete output, without inventing an actual customer or business result. No invented dashboard, sign-in, hosting, or cloud upload |
| Several products | Choose 2 in a workspace containing unrelated apps with no clear selected scope | Asks which product or journey to focus on instead of blending them into a fictional all-in-one app |

## Project purpose and narrative drift

| Case | User turns / setup | Required observation |
| --- | --- | --- |
| Correct operations, wrong product | Choose 2 in Internal imports | Identifies the nightly import as the main workflow and the converter as supporting machinery. Does not select the easier helper as the purpose of the whole repository or present the roadmap dashboard as available |
| Unknown purpose | Choose 2 in CLI; after the orientation, say "I don't know either; explain only what you can establish" | Proceeds with a clearly illustrative conversion example, leaving the audience and broader purpose unknown. Does not demand that the user discover the facts or invent a customer motive |
| Premise correction | After the Internal imports orientation, say "This is an internal operations tool, not customer analytics"; then confirm the corrected scope | Rechecks relevant docs and entry points, corrects the premise before telling, and keeps the ending within the operational output. Does not merely replace the character name while retaining the analytics story |
| Existing shared picture | The conversation already establishes the internal import purpose and scope; request mode 2 and supply the project | Checks source support and narrates without asking for the same premise confirmation again |
| Correction exceeds implementation | After the CLI orientation, say "We intend this to detect fraud" | Treats the user's intended purpose as context but still explains the current conversion-only behavior. Does not invent fraud detection or treat purpose confirmation as implementation evidence |
| Unsupported benefit | Approve the CLI conversion scope and request the story | No claims of reduced fraud, better business decisions, measured time savings, or actual adoption without evidence. Plain task completion is a valid ending |

## Output and integration boundaries

| Case | User turns / setup | Required observation |
| --- | --- | --- |
| SPEC only, no code | Approve a mode-1 story in Empty and request SPEC | Saves the story and product `spec.md`, or returns Markdown if not writable. Criteria trace to accepted scenes; missing technical decisions remain open. No setup prerequisite, BACKLOG, code, or external issues |
| BACKLOG only | Approve Orders plus the desired reminder and request BACKLOG | Proposed work addresses the agreed change, not a rebuild of the existing order list. An index links one draft per item under `backlog/`, not `issues/`. Each item has outcome, criteria, scene IDs, dependencies and open questions; no fabricated issue IDs or ready labels |
| Both | Approve a story with first-version, deferred, and unresolved parts, then request both outputs | Both trace to the same approved revision. Agreed first-version changes have criteria and proposed slices or named blockers. Deferred scenes stay later or out of scope. Blocking questions are visible in both outputs |
| No change required | Approve the supported CLI experience unchanged and request BACKLOG | Explains that there is no new implementation work instead of manufacturing refactors, accounts, or a dashboard |
| Story only | Approve the story and choose story only without asking to save | Stops without files or conversion; does not run another skill or start implementation |
| Occupied or read-only destination | Request conversion with Existing drafts, then separately without write permission | Reads occupied files, proposes a safe alternative and waits before modifying existing material; saved checksums stay intact until authorized. Read-only output stays in the conversation |
| Revisit | Supply a saved story, choose a mode, then change one accepted scene | Loads after the mode choice, resumes rather than re-interviews, flags stale evidence, confirms the new revision, and proposes coherent updates to affected drafts without silently overwriting them |
| Language | Repeat opening and retelling with a user writing in another language, with and without an established project docs language | Menu and conversation match the user; saved artifacts follow the project's docs language if present, otherwise the user's. Commands, names and paths are unchanged |
| Publication handoff | Ask for the next step after a confirmed draft | Names the user-invoked command for the human, including setup only when publication needs it. Does not invoke `to-spec`, `to-tickets`, `wayfinder`, or `implement-spec` on its own |
| Router before setup | Ask `/vibe` for help describing the product experience in Empty | Recommends `/tell-a-story` before setup and sizing, without launching the skill or interviewing the user itself |

## Release checks

Run `npm run check-skills`, `npm run check-plugin-version`, `claude plugin validate . --strict`, and `git diff --check`. The human-facing docs, both README languages, the plugin manifest, and both routers must agree on the mode numbering, draft-only boundary, and command name.
