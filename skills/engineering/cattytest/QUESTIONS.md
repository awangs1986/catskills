# Question bank

Branches of the design tree `cattytest` walks, with the questions that belong to each and the shape of a recommended answer. Ask the frontier only: a branch's questions open once the branch before it has answers. Skip any question the repo already answers; the bank is what to ask the user, not a checklist to recite.

Every question carries a recommended answer in the `grilling` format. The recommendation comes from what was read in the repo; when nothing was read that bears on it, say so in the recommendation rather than inventing one.

## 1. Stakes

Opens after scope. Orders every later branch.

- **Loud failures**: "If one thing in this scope broke tonight, which one would you hear about first? Second? Third?" ➡️ Propose from the entry points: the one users hit most, the one that touches money or someone else's data, the one that writes something irreversible.
- **The last embarrassment**: "What was the last bug here that a test should have caught?" ➡️ Look in git log and the tracker for a fix commit; propose it. It becomes a claim.
- **Done enough**: "What has to be true for you to merge or ship this scope without a knot in your stomach?" ➡️ For a feature: its acceptance criteria hold and one wrong path per criterion is covered. For a project: the Loud three have end-to-end claims, everything else waits.
- **What no test will ever prove** (whole project only): "Which parts are you happy to keep checking by hand?" ➡️ Visual polish, third-party dashboards, anything a screenshot judges better than an assertion. Goes in Out of scope.

## 2. Claims

Opens after Stakes. Draft first, then ask.

- **Correction, not authorship**: present the drafted claims (from criteria, user stories, the code's branches, the embarrassment bug). "Read these as business rules. Which sentence is wrong, and which rule is missing?" ➡️ Recommend the list as drafted, with the two you are least sure of marked.
- **The unsure rule**: for any claim where the user hesitates: "Is the rule wrong, or do you not know what the rule is?" ➡️ Not knowing is a spec gap: flag **rule unconfirmed**, point at `refocus` if the answer should be on disk, keep going.
- **Duplicate wording**: two claims that differ only in phrasing: "Same rule, or two?" ➡️ Same, unless a different actor or a different seam is involved.

## 3. Seams

Opens once the claims are stable.

- **Where it crosses**: per claim (batched by entry point): "This rule is observable at `<seam>`. Test it there, or somewhere closer to the user?" ➡️ The public boundary nearest the rule: an exported function for pure logic, the route or command for anything with an actor, the UI only for the Loud three.
- **No clean seam**: "This rule lives across `<files>`; there's no one place to observe it without reaching inside. Test it at `<nearest seam>` and accept a wider test, or park it and note a Tidy candidate?" ➡️ Nearest seam now, Tidy candidate written down; never a test of internals.
- **Confirm the set**: "These are the seams the plan will test at, and nothing else. Agreed?" ➡️ The list. `tdd` will refuse an unconfirmed seam later, so settle it here.

## 4. Oracle and level

Opens per claim once its seam is set.

- **How do you know**: "When this is right, what exactly do you see? A specific value, a specific row, a screenshot you'd judge?" ➡️ A literal from the spec or a worked example the user can state now. If the only answer is "whatever the code returns", the claim is **oracle missing**.
- **Level**: "Unit at the function, integration through the seam with real dependencies, or end-to-end through the running app?" ➡️ Integration at the seam by default; unit when the oracle is a worked example and the logic is pure; end-to-end for the Loud three only, and only if `verify` isn't already covering them per ticket.
- **Who judges**: for screenshot-shaped oracles: "Is this a test, or a `verify` step a human looks at?" ➡️ `verify` step, listed in Out of scope with that reason.

## 5. Doubles

Opens per claim once its level is set. Only for claims whose path touches the outside world (read from the code; don't ask whether it does).

- **Real or fake**: "This path touches `<db / network / clock / fs / env / randomness>`. Real, faked at the boundary, or skipped for this claim?" ➡️ Real for a local database or filesystem in a temp dir; fake at the boundary for network and time (a fixed clock, a recorded response); skipped only when a different claim covers that touch.
- **Never the thing itself**: if the user suggests mocking the module under test: "That's the code the claim is about; a mock there makes the test pass whatever the code does. Fake its dependency instead?" ➡️ Yes; `tdd`'s mocking.md has the shapes.
- **Shared fixtures**: "Is there a fixture or factory already used for `<entity>`, and is it one you trust?" ➡️ Reuse if trusted; a fixture that hides the interesting value is rewritten in the test.

## 6. Data

Opens with Oracle; often the same round.

- **A real example**: "Give me one realistic input for this claim, and the exact output you'd expect. Not a shape, the values." ➡️ Propose one from the spec or a seed file; the user confirms or corrects.
- **Independent source**: "Where does that expected value come from, other than running the code?" ➡️ The spec, a hand calculation, a known-good record, a regulator's example. If none exists, **oracle missing**.
- **Boundaries in the data**: "Is there a value where the rule flips? Zero, the maximum, yesterday versus today, the same name in a different case?" ➡️ Propose from the comparisons in the code; each one is a Wrong-path candidate.

## 7. Wrong paths

Opens per claim once its data is set.

- **The usual five**: "For this rule: empty input, the boundary value, doing it twice, a record that belongs to someone else, two at once. Which of these matter here?" ➡️ One per claim minimum; all five for anything that touches another user's data or money.
- **The failure the user wants**: "When this goes wrong, what should the user see: an error they can act on, a silent no-op, or a refusal?" ➡️ Whatever the spec says; if the spec is silent, that's a **rule unconfirmed** for the ticket.

## 8. Existing tests

Opens once claims exist to compare against. Present the sort, don't ask the user to make it.

- **The sort**: "I read the `<n>` existing tests. Keep `<list>` (they claim something on the list). Rewrite `<list>` (they run the right code but claim nothing, or claim the wrong thing). Delete `<list>` (tautological, or test a rule nobody has). Objections?" ➡️ The sort as proposed, one line of evidence per rewrite and delete.
- **The orphan**: for a test that claims a rule not on the list: "This test claims `<sentence>`. Is that a rule we forgot, or a test nobody asked for?" ➡️ Usually a forgotten rule; add the claim.

## 9. Budget

Opens last.

- **Before the next merge**: "How many of these red tests before this merges? Five is a plan; twenty is a backlog." ➡️ Five for a feature; the Loud three plus their wrong paths for a project's first pass.
- **Order**: "Of the first `<n>`, which goes first?" ➡️ The claim from Stakes with the cheapest oracle; a first test that goes red in five minutes keeps the plan alive.
- **Out**: "Say out loud what's out of scope, so it isn't silently assumed in." ➡️ Everything not in the first `<n>` and not in a later ticket, listed with the sentence that put it out.
