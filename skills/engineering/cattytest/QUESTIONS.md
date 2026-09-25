# Question bank

Branches of the design tree `cattytest` walks, with the questions that belong to each and the shape of a recommended answer. Ask the frontier only: a branch's questions open once the branch before it has answers. Skip any question the repo already answers; the bank is what to ask the user, not a checklist to recite.

Every question carries a recommended answer in the `grilling` format, drawn from what was read in the repo. When nothing read bears on it, say so in the recommendation rather than inventing one.

The one move that runs through every branch: when the answer is a proxy (a status code, a log line, "the function returns", "the test passes"), ask **"and then what would you see?"** until it is something a person can point at.

## 1. The apple

Opens after scope. Everything else hangs off it.

- **What was wanted**: "When you asked for this, what did you want to be true afterwards, in the world, that wasn't true before?" ➡️ Propose from the user stories and the entry points' side effects: the thing written, sent, shown, or moved. One sentence per outcome, no code words.
- **Without the code**: "If you couldn't open the repo or the logs, how would you personally check that it worked?" ➡️ The action a user would take to look: open the file, check the inbox, refresh the page, look at the bank sandbox. That check is the evidence line later.
- **Rank**: "If two of these outcomes were true and one wasn't, which missing one would you hear about first?" ➡️ Money, someone else's data, and anything irreversible come first.
- **The apple already missing** (whole product only): "Has a green build ever shipped something that didn't do what you wanted? What was it?" ➡️ Look in the tracker and git log for reverts and hotfixes; propose it. It becomes case 1.

## 2. Proxies

Opens once the apples are stated. Present, don't ask the user to inventory.

- **The gap**: "Here are the gates that exist in scope and what each proves if green. If all of them are green, can `<apple>` still be missing?" ➡️ Yes, and name how: the right function called with the wrong argument, the right file with the wrong encoding, the right email to the wrong address, the right total in the wrong currency, the right row that the UI never shows. Each way is a case.
- **The criterion that is a proxy**: for any acceptance criterion written in code terms: "This criterion says `<'the endpoint returns the rows'>`. What does the user see when it's satisfied?" ➡️ Rewrite the criterion as an outcome; note the original wording under Open so the ticket gets fixed.
- **False comfort**: "Which of these gates do you currently trust as proof that the feature works?" ➡️ Whatever they name goes in *Gates that don't count as proof*, with the apple it can't see.

## 3. The walk

Opens per apple.

- **From where**: "Where does the person start? Logged in as whom, on which screen or in which directory?" ➡️ Propose the realistic start, not the developer's shortcut: the second user, the existing workspace, the shell a user would actually have.
- **Step by step**: "Say the steps as you would to a friend on the phone. What do they click, type, or run, in order?" ➡️ Draft from the UI or CLI; the user corrects. Every step is one action.
- **The shortcut trap**: if a step is "call the API directly" or "run the script": "Is that what a user does, or what a developer does?" ➡️ The user's route, unless the scope is a developer tool.

## 4. Real data

Opens with the walk.

- **Which one**: "Which user, which record, which numbers? Not a kind of user, a specific one." ➡️ Propose from seeds and fixtures; where they don't exist, the case starts with "create `<data>` first" and Open notes that the seed is missing.
- **The awkward record**: "Is there a record that's more likely to break this: the one with two workspaces, the unpaid one, the name with an accent, the amount over the limit?" ➡️ Use the awkward one for the main case; the plain one is the smoke case.
- **Where the expected value comes from**: "The apple says `<total 1 240,00 EUR>`. Where does that number come from, other than the software?" ➡️ A spreadsheet, a hand calculation, a known-good invoice from before. If nowhere, the case is **evidence unknown** and goes to Open.

## 5. Evidence

Opens once the walk and data are set.

- **The artefact**: "What will you look at to know it worked? Say the thing, not the fact." ➡️ The PDF opened in a PDF reader, the inbox with the message, the page after refresh, the file listing, the sandbox transaction. Screenshot or capture of exactly that.
- **Seen how a user sees it**: if the evidence is a database row or a log: "Would the user see it that way? Where would *they* see it?" ➡️ Through the UI, the file, the inbox, the other system. The row is at best supporting evidence.
- **The negative case's evidence**: for "nothing should happen" cases: "How do you show that nothing happened?" ➡️ The unchanged state captured before and after: the same directory listing, the same inbox count, the same balance.

## 6. The ways a real person breaks it

Opens per apple once its main case exists.

- **The usual six**: "For this outcome: did it twice; came back tomorrow; typed it wrong (comma for a point, trailing space, emoji); the connection dropped halfway; it's someone else's; it's the boundary (last day, zero items, the limit). Which of these would you hear about?" ➡️ Two or three per apple, all six for money and other people's data. The rest go to Out of scope by name.
- **What should happen instead**: "When that goes wrong, what does the user get: a message they can act on, a quiet no-op, a refusal?" ➡️ Whatever the spec says; if the spec is silent, an Open item for the ticket, and the case's apple is written as the user's best guess marked *unconfirmed*.

## 7. Who runs it

Opens once cases have evidence.

- **Can the agent see it**: "Can `verify` observe this evidence from inside the repo's feedback loops (browser, logs, filesystem, a test inbox)?" ➡️ Look at `feedback-loops.md`. Yes → `verify`. No (a real inbox, a third-party dashboard, "does it look right") → by hand.
- **Every merge, forever**: "Would you want this exact case run on every merge, unattended?" ➡️ Only for the two or three cases at the top of the ranking whose evidence a machine can read. Those become automated after they've passed once by `verify` or by hand.
- **Judgement**: "Is passing this a fact or an opinion?" ➡️ Opinion (reads well, looks right, feels fast) is by hand, and stays by hand.

## 8. Order and budget

Opens last.

- **Before merge**: "Which of these have to pass before this merges? Draw the line." ➡️ The main case for every apple, plus the wrong paths for money and other people's data. Everything below the line is listed, not lost.
- **First**: "Which one do you run first?" ➡️ The top-ranked apple's main case; if it fails, nothing below it matters yet.
- **Out loud**: "Say what's out of scope, so it isn't silently assumed in." ➡️ Everything named in rounds 1 and 6 that isn't above the line, with the sentence that put it out.
