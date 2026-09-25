---
"mattpocock-skills": minor
---

Add the `security-review` skill (engineering bucket, model-invoked). A short pass over a diff, one hop into the queries its routes call, for the five failures that account for most incidents in solo-built apps: secrets in source or the client bundle, routes without authentication or per-record authorisation, input trusted at a boundary, data access bypassing RLS or parameterisation, unaudited dependencies. Three severities (`block`, `fix-before-ship`, `note`), under 400 words, with a "checked and clean" line. `code-review` now spawns it as a conditional third sub-agent when the diff touches a route, auth, a query, env, or a dependency manifest, reports it under `## Security`, and states a `block` first.
