---
"mattpocock-skills": minor
---

Add the `test-audit` skill (engineering bucket, model-invoked). Audits the tests behind a change for whether they protect the business logic or only pass: translates each test into a one-sentence claim in `CONTEXT.md` vocabulary for the domain expert to judge (flagging name/assertion mismatches, tests that claim nothing, and tautological assertions), maps claims to acceptance criteria and user stories in both directions with untested wrong paths listed, and runs a targeted mutation probe (ten to fifteen mutants at business-rule sites, one at a time, tree verified clean between each) to find rules no test kills. Audits, never fixes; survivors and uncovered rows return to `tdd` as named red tests. `implement` now calls it after `verify` and before `code-review`, and ends with a **Checks run** ledger listing what was actually checked.
