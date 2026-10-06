# Upstream synchronization

- Source: https://github.com/mattpocock/skills
- Original shared baseline: `c55ee46073ed923f86ce59a5eb3b6d895095d1b7` (v1.2.3).
- Current upstream release: v1.3.1.
- Synchronized through: `4588b32ecab9ecc9fc8cc6b6c5e7d675b6004b0d`, inspected 2026-10-06.

The promoted collection contains 27 inherited skills and 12 fork additions, 39 total. Upstream graduates `implement-spec`, `pr`, and `retro` are included. `resolving-merge-conflicts` is archived in `skills/deprecated/` and excluded from installation and the plugin. The new upstream experimental `chief-of-staff` is outside this update's promoted and previously inherited scope.

Inherited instructions and human docs incorporate the upstream changes. Local conversation style, host-neutral skill invocation, language policy, plugin naming, and the fork's single-ticket verification, test-audit, security-review, and Checks run integration remain in force. The fork-only skill implementations are preserved; `vibe` and `askcat` receive discovery and routing updates so they describe the current set.

New projects use `GLOSSARY.md` / `GLOSSARY-MAP.md`. The setup/domain adapter retains configured legacy `CONTEXT.md` sources and explains how older skill references resolve to the current glossary. A project migration is separate from updating this skill collection.

For the next update, compare upstream changes from the synchronized commit above, rather than overwriting the entire fork. Check all graduated/retired routes, docs, invocation metadata, catalogs, plugin entries, and generated posters. Preserve the fork-only implementations and validate their content against the starting snapshot.

## Installation and validation

The canonical installation commands and repository metadata now point to `awangs1986/catskills`. Local Claude Code, Codex, and Pi installations link to this checkout, including `askcat`, `vibe`, and the newly promoted commands. Previous installation entries were backed up before relinking.

- `npm run check-skills`: 39 promoted skills, all invariants hold.
- `npm test`: 39 tests pass, including the Askcat picker routes for `implement-spec`, `pr`, and `retro`.
- `npm run check-plugin-version` and `git diff --check`: pass.
- English and Chinese catalog order and invocation groups agree; all 39 promoted skills resolve to the current checkout in all three local harnesses.
- Both regenerated workflow posters were visually inspected. These checks do not claim a live agent conversation evaluation.
- Claude Code 2.1.291: the marketplace manifest passes strict validation. Plugin validation passes with one warning about root `CLAUDE.md` not loading as installed project context; `claude plugin validate . --strict` fails because it treats that warning as an error. The same warning occurs on the unchanged starting snapshot. Keep `CLAUDE.md` for work in this repository; portable skill-local instructions carry the shipped context.
