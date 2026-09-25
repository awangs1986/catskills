# The canonical install block

One install story, one wording. `README.md` (and its translation `README.zh-CN.md`), `.changeset/*`, and every page under `docs/` must say **this** and nothing else. Change it here first, then propagate.

This repo is a fork of `mattpocock/skills`. It is **not** listed in Claude Code's official marketplace (that listing is Matt's upstream plugin, without this fork's additions), so every route below points at this repository directly. The plugin is `cat-skills` and the marketplace is `awangs1986` (from `.claude-plugin/plugin.json` and `marketplace.json`); the blocks below say whatever the manifests say, and change with them.

## Any agent: clone and link

The route that works the same in Claude Code, Codex and Pi, and the one `README.md` leads with.

<canonical-block name="clone-and-link">

```bash
git clone https://github.com/awangs1986/popcodeskills.git
cd popcodeskills
scripts/link-skills.sh
```

This symlinks every skill into `~/.claude/skills`, `~/.agents/skills` and `~/.pi/agent/skills`, so a `git pull` keeps all three current.

</canonical-block>

## Codex, and other agents: skills.sh

[skills.sh](https://skills.sh) copies editable skill files into the project. The whole-set form:

<canonical-block name="skills-sh-whole-set">

```bash
npx skills@latest add awangs1986/popcodeskills
```

Pick the skills you want and which agents to install them on. **Make sure `setup-matt-pocock-skills` and `vibe` are among them.** The files land in your project as ordinary files you own; pull updates when you want them with `npx skills update`.

</canonical-block>

…and the single-skill form wherever one skill is named on its own:

<canonical-block name="skills-sh-one-skill">

```bash
npx skills@latest add awangs1986/popcodeskills --skill=<name>
```

```bash
npx skills@latest update <name>
```

</canonical-block>

`skills@latest` is the pinned spelling everywhere. The pages under `docs/` carry no install commands at all: the published site renders them itself (see [writing-docs.md](./writing-docs.md)).

## Claude Code: the plugin, from this repo's own marketplace

`.claude-plugin/marketplace.json` makes the repo a single-plugin marketplace. For this fork that is the documented plugin route, not a fallback:

<canonical-block name="claude-code">

```
/plugin marketplace add awangs1986/popcodeskills
/plugin install cat-skills@awangs1986
```

</canonical-block>

Mention, in one sentence, that `claude plugins install mattpocock-skills` (the official listing) is Matt's upstream set without this fork's additions, and that installing both gives every upstream skill twice.

## The routes are exclusive

The plugin is a managed, read-only bundle. skills.sh and the clone-and-link route write files you own. Installing more than one leaves the user with every skill twice: always say "pick one".
