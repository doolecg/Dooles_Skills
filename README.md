<div align="center">

# Dooles Skills

**One repo for my Claude Code skills, my global rules and my OpenCode worker agents.**

![Skills](https://img.shields.io/badge/skills-353-blue)
![Plugins](https://img.shields.io/badge/plugins-17-brightgreen)
![Claude Code](https://img.shields.io/badge/Claude%20Code-marketplace-orange)
![OpenCode](https://img.shields.io/badge/OpenCode-compatible-purple)

</div>

Install the skills on any PC in one go. Browse, update or turn them off from Claude Code's `/plugin` screen like any other plugin. My mods (the Main Menu, the bottom bar and the rest) are in a separate repo: [dooles-tools](https://github.com/doolecg/dooles-tools).

## How it fits together

```
                      Dooles_Skills (this repo)
                                |
        +-----------------------+------------------------+
        |                       |                        |
   plugins/*/skills         rules/rules.md          opencode/agent/*.md
        |                       |       \                |
 ~/.claude/skills        ~/.claude/CLAUDE.md   opencode.jsonc      ~/.config/opencode/agent
 (plugin install)        (via dooles-rules     (`instructions`)    (directory junction)
        |                 junction)                 |                   |
        v                       v                   v                   v
   Claude Code  <---------------+------------->  OpenCode  <------------+
        ^                                           |
        +------- OpenCode also reads ~/.claude/skills
```

## Quick start

**One click (Windows):** clone this repo and double-click `install.cmd`. It adds the marketplace and installs every plugin. To pick some: `.\install.ps1 blockdesigner,minecraft-modding`.

**Inside Claude Code:**

```
/plugin marketplace add doolecg/Dooles_Skills
/plugin install core@dooles-skills
```

**From a terminal:**

```
claude plugin marketplace add doolecg/Dooles_Skills
claude plugin install <name>@dooles-skills
```

Useful after that:

- `/plugin` lists the marketplace. Install, enable, disable, uninstall and update from there.
- `claude plugin list` shows what is installed. `claude plugin details <name>@dooles-skills` shows a plugin's skills and their token cost.
- `claude plugin marketplace update dooles-skills` pulls the latest. Turn on auto-update in `/plugin` under Marketplaces to do it at startup.

Plugin skills are namespaced, for example `/blockdesigner:blockdesigner-release`.

## Plugins

| Plugin | Skills | Highlights | Source |
|---|---|---|---|
| `core` | 6 | `team-work`, `ui-change`, `repo-release`, `plain-writing`, `minecraft-test-setup`, `desktop-app-baseline` | mine |
| `blockdesigner` | 3 | `blockdesigner-release`, `blockdesigner-plugin-release`, `blockdesigner-plugin-new` | mine |
| `agent-viewer` | 1 | `release` | mine (only copy) |
| `voxel-icons` | 1 | `voxel-icons` | mine |
| `design` | 2 | `ui-critique`, `ui-foundations` | mine, adapted from [designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT) |
| `minecraft-modding` | 3 | `fabric-modding`, `neoforge-modding`, `minecraft-26-1-migration` | [siredvin/minecraft-modding-skills](https://github.com/siredvin/minecraft-modding-skills) (MIT), pinned |
| `minecraft-multiloader` | 1 | `minecraft-multiloader` | [jahrome907/minecraft-agent-skills](https://github.com/jahrome907/minecraft-agent-skills) (MIT), pinned |
| `minecraft-mod-dev` | 1 | `minecraft-mod-dev` | mcpmarket (copy) |
| `google-workspace` | 100 | `gws-gmail`, `gws-calendar`, `gws-drive`, `google-sheets-builder` | mine and collected |
| `ai-and-agents` | 39 | `browser-app-automation`, `computer-use`, `dspy`, `hindsight-integration` | mine and collected |
| `seo-content` | 37 | `seo-keyword-research`, `content-gen-outline`, `company-enrichment` | mine and collected |
| `dev-practices` | 35 | `api-and-interface-design`, `debugging-and-error-recovery`, `ci-cd-and-automation` | mine and collected |
| `project-lessons` | 35 | `to-build-the-github-release-body`, `after-publishing-a-release-find-the` | mine and collected |
| `ux-design` | 30 | `accessibility`, `ux-heuristics-review`, `journey-mapping`, `dieter-rams-principles` | mine and collected |
| `web-and-cloud` | 30 | `cron-patterns`, `vps-fastapi-deployment`, `nextjs-development-patterns` | mine and collected |
| `media-and-docs` | 15 | `docx`, `pdf`, `xlsx`, `ocr-and-documents` | mine and collected |
| `games` | 14 | `minecraft-bedrock-server`, `minecraft-modpack-server`, `check-the-core-keeper-mod-in-game` | mine and collected |

Third-party plugins are not copied here. `marketplace.json` points at their original repos, pinned to a commit.

Anthropic's built-in skills and the ones synced to my claude.ai account are not here. They already follow the account.

The BlockDesigner skills call their scripts by path in the BlockDesigner checkout (`F:/PROGRAMMING/REPOS/BlockDesigner/.claude/skills/...`). Use them on a PC that has that checkout.

## The rules file

`rules/rules.md` holds my global rules for both tools: how I want mod test setups done, releases and commits, subagent model choice, and how I like replies written.

- Claude Code imports it from `~/.claude/CLAUDE.md` with `@~/.claude/dooles-rules/rules.md`. `dooles-rules` is a directory junction to `rules/`.
- OpenCode loads it through `instructions` in `~/.config/opencode/opencode.jsonc`.

Edit it here and both tools pick it up.

## OpenCode worker agents

`opencode/agent/` holds three subagents. `~/.config/opencode/agent` is a directory junction to it. They follow the "smallest model that fits" rule in `rules/rules.md`.

| Agent | Tier | Model | Use it for |
|---|---|---|---|
| `worker-small` | Small | `anthropic/claude-haiku-4-5` | Lookups, reading files, renames, builds and tests, simple edits, screenshots |
| `worker-medium` | Medium | `anthropic/claude-sonnet-5-5` | A feature across a few files, a normal bug fix, a UI change |
| `worker-hard` | Hard | `anthropic/claude-opus-5-5` | Architecture, big refactors, tricky debugging, security work (only with my say-so) |

Skills work in both tools, because OpenCode reads `~/.claude/skills`. The `team-work` skill describes how to hand out jobs to these workers.

## Keeping it in sync

My own skills are edited where they are used, next to their projects. Many are git-ignored there, so this repo is also their backup.

```
python sync.py --dry-run     # show what changed
python sync.py               # copy it in
python sync.py --upstream    # also move third-party plugins to their repos' latest commit
claude plugin validate .
git add -A && git commit -m "Sync skills" && git push
```

- The themed plugins are listed in `themes.json`. `sync.py` copies each named skill in and prints any source skill that is not in a plugin yet.
- To add a skill of my own, add its folder to `SOURCES` in `sync.py`, or its name to a plugin in `themes.json`. For a new plugin, also add an entry to `.claude-plugin/marketplace.json`. Then run the sync.
- Skills in `core`, `design` and `voxel-icons` are edited in this repo. `~/.claude/skills/<name>` links to their folders, so `sync.py` does not copy them (they are listed in `REPO_OWNED`).
