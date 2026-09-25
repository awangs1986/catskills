---
"cat-skills": minor
---

Add the `setup-feedback-loops` skill (engineering bucket, user-invoked). Audits a repo for the checks the other skills spend (typecheck, lint, test runner with a single-file variant, formatter in check mode, smoke test, readable dev-server logs, a headless browser for web apps, a pre-commit guardrail), treats present-but-silent as worse than missing, proposes the gaps in one table, wires the stack's conventional defaults, proves every loop goes red on a deliberate fault, and writes commands and timings to `docs/agents/feedback-loops.md`, which `implement`, `tdd`, `diagnosing-bugs` and `verify` now read. Ships a template for that file.
