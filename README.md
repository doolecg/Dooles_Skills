# dooles-skills

My Claude Code skills as a plugin marketplace: install them on any PC in one go, and browse, update or turn them off from Claude Code's `/plugin` screen like any other plugin. My mods (the sidebar, bottom bar and the rest) live in [dooles-tools](https://github.com/doolecg/dooles-tools).

## Install
**One click:** clone or download this repo and double-click `install.cmd`. It adds the marketplace and installs every plugin. To pick some: `.\install.ps1 blockdesigner,minecraft-modding`.

**From inside Claude Code:**
```
/plugin marketplace add doolecg/Dooles_Skills
/plugin install minecraft-modding@dooles-skills
```
**From a terminal:** `claude plugin marketplace add doolecg/Dooles_Skills`, then `claude plugin install <name>@dooles-skills`.

The repo is private, so git on that PC has to be signed in to GitHub (Git Credential Manager handles it the first time).

## Check and manage them
- `/plugin` in Claude Code lists the marketplace and its plugins. From there you can install, enable, disable, uninstall and update them.
- `claude plugin list` shows what's installed. `claude plugin details <name>@dooles-skills` shows a plugin's skills and how many tokens they cost.
- `claude plugin marketplace update dooles-skills` pulls the latest from this repo. Turn on auto-update for the marketplace in `/plugin` › Marketplaces to have it happen at startup.

Plugin skills are namespaced, like `/blockdesigner:blockdesigner-release`.

## What's in it
| Plugin | Skills | Source |
|---|---|---|
| `blockdesigner` | `blockdesigner-release`, `blockdesigner-plugin-release`, `blockdesigner-plugin-new` | mine |
| `agent-viewer` | `release` (Claude Agent Viewer) | mine; the only copy (its checkout is gone) |
| `operant` | `operant`, `release`, `learn-real-test` | mine |
| `voxel-icons` | `voxel-icons` | mine |
| `core` | `team-work`, `ui-change`, `minecraft-test-setup`, `desktop-app-baseline`, `repo-release`, `plain-writing` | mine |
| `design` | `ui-critique`, `ui-foundations` | mine, adapted from [designer-skills](https://github.com/Owl-Listener/designer-skills) (MIT) |
| `minecraft-modding` | `fabric-modding`, `neoforge-modding`, `minecraft-26-1-migration` | [siredvin/minecraft-modding-skills](https://github.com/siredvin/minecraft-modding-skills) (MIT), pinned to a commit |
| `minecraft-multiloader` | `minecraft-multiloader` | [jahrome907/minecraft-agent-skills](https://github.com/jahrome907/minecraft-agent-skills) (MIT), pinned to a commit |
| `minecraft-mod-dev` | `minecraft-mod-dev` | mcpmarket (copy) |
| `ux-design` | 30 skills, e.g. `accessibility`, `ai-chat-data-apps`, `ai-governors`, `ai-identifiers` | mine and collected |
| `project-lessons` | 49 skills, e.g. `after-an-operant-release-delete-all`, `after-changing-effect-parameters-regener`, `after-operant-changes-run-npm-run`, `after-publishing-a-release-find-the` | mine and collected |
| `dev-practices` | 35 skills, e.g. `api-and-interface-design`, `brainstorming`, `browser-testing-with-devtools`, `ci-cd-and-automation` | mine and collected |
| `ai-and-agents` | 39 skills, e.g. `background-delegation-reliability`, `browser-app-automation`, `computer-use`, `debugging-hermes-tui-commands` | mine and collected |
| `media-and-docs` | 15 skills, e.g. `baoyu-comic`, `creative-ideation`, `document-cross-referencing`, `docx` | mine and collected |
| `seo-content` | 37 skills, e.g. `builtwith-enrichment`, `citation-sourcing`, `company-enrichment`, `content-gen-meta` | mine and collected |
| `web-and-cloud` | 30 skills, e.g. `contributor-pr-review`, `cron-patterns`, `cron-recovery`, `cross-platform-npm-scripts` | mine and collected |
| `google-workspace` | 100 skills, e.g. `gmail-bulk-operations`, `google-sheets-builder`, `google-sheets-operations`, `google-workspace` | mine and collected |
| `games` | 14 skills, e.g. `build-the-jade-mod-with-a`, `check-the-core-keeper-mod-in-game`, `for-core-keeper-qol-idea-lists`, `minecraft-bedrock-server` | mine and collected |

Anthropic's built-in skills (pdf, docx, xlsx, ...) and the ones synced to my claude.ai account aren't here: they already follow the account.

The BlockDesigner skills call their scripts by their path in the BlockDesigner checkout (`F:/PROGRAMMING/REPOS/BlockDesigner/.claude/skills/...`), so they're meant for a PC with that checkout.

## Keeping it up to date
My own skills are edited where they're used, next to their projects (often git-ignored there, so this repo is also their backup). To bring the changes here:
```
python sync.py --dry-run     # what changed
python sync.py               # copy it in
python sync.py --upstream    # also move the third-party plugins to their repos' latest commit
claude plugin validate .
git add -A && git commit -m "Sync skills" && git push
```
The themed plugins (everything else in `~/.claude/skills` and `~/.agents/skills`) are listed in `themes.json`; `sync.py` copies each named skill in and prints any source skill that isn't in a plugin yet, so new ones get noticed. To add a skill of my own, add its folder to `SOURCES` in `sync.py`, or its name to a plugin in `themes.json` (and a plugin entry in `.claude-plugin/marketplace.json` if it's a new plugin), then run the sync.
