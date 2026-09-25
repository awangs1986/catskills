---
"cat-skills": minor
---

The plugin is now `cat-skills`, in this repo's own marketplace `awangs1986` (`/plugin marketplace add awangs1986/popcodeskills`, then `/plugin install cat-skills@awangs1986`); it no longer shares a name with the upstream `mattpocock-skills` listing. `package.json`, `plugin.json`, `marketplace.json`, the changeset config and every pending changeset carry the new name. Docs pages now link to each other and into the repo with repo-relative paths instead of `aihero.dev/skills-<name>` URLs, which only exist for upstream's skills; `check-skills` fails on a docs link that does not resolve.
