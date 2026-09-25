---
"mattpocock-skills": minor
---

Add the `verify` skill (engineering bucket, model-invoked). Boots the built thing and walks each acceptance criterion and user story as the actor would (headless browser, curl, the CLI, a direct trigger), tries one obvious wrong path per criterion, and reports PASS / FAIL / UNVERIFIABLE with a file of evidence per row. Observes, never fixes. `implement` now calls it after the suite is green and before `code-review`, and takes each FAIL back into the `tdd` loop.
