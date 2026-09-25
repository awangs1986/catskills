---
"mattpocock-skills": patch
---

Install block rewritten for this fork (clone and link, skills.sh against `awangs1986/popcodeskills`, the repo's own marketplace as the documented plugin route) so `README.md` copies it verbatim again. New `npm run check-skills` (`scripts/check-skills.mjs`) checks the skill invariants in `CLAUDE.md` mechanically: promoted skills present in both READMEs, the bucket README, `plugin.json`, a docs page with the fixed frame, `openai.yaml` agreeing with the frontmatter, `ask-matt` naming every user-invoked skill, no em-dashes, English only outside the translation. `implement` now names the `test-cases.md` sheet `verify` walks and reports it in the Checks run block; `cattytest` no longer duplicates the sheet as a tracker issue; `askcat`, `takeover` and `wait-what` docs pages gain their missing sections; `CLAUDE.md` names the Pi link directory.
