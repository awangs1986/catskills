---
"mattpocock-skills": minor
---

Add the `vibe` skill (engineering bucket, user-invoked). A dispatcher for one developer working alone: it puts the user on one of four lanes (Build, Fix, Review, Tidy), sizes Build work as S / M / L with three ordered questions, and hands back a route card naming the exact next command, the steps after it, and the context rule between them. It routes and stops; it may fire a model-invoked first step (`tdd`, `diagnosing-bugs`, `code-review`) only on an explicit "go". The skill ships with `WORKFLOW.md`, the human-facing map it reads from: the curated sixteen-skill kit, the skills deliberately left out with the moment to bring each back, per-lane walkthroughs, five context rules, what accumulates in the repo, two worked sessions, and a cheatsheet. `ask-matt` now points solo users at it and takes them back when other people enter the picture.
