# Personal instructions

## Minecraft mod projects: test clients and servers
When running a Minecraft dev client or server for any mod project (Fabric, NeoForge, Architectury, Paper; any version), set this up before launching and keep it in place:
- **Sound at half:** every `soundCategory_*` line in the run folder's `options.txt` set to `0.5`.
- **Test worlds:** peaceful, creative, commands allowed (in `level.dat`: difficulty peaceful, `GameType` 1, `allowCommands` 1; in 26.x the difficulty lives under `difficulty_settings`). New worlds are created that way.
- **GUI scale 2 at 1080p:** `guiScale:2` in `options.txt` with a 1920x1080 window (`--width 1920 --height 1080`), for every test run.
- **Screen grabs:** the Bare Bones resource pack (Minecraft's trailer look) and Iris with Complementary Reimagined shaders, installed only in the run folder (`resourcepacks/`, `mods/`, `shaderpacks/`), never shipped with the mod.
- **Dev servers:** `server.properties` with `difficulty=peaceful`, `gamemode=creative`, `force-gamemode=true`, `white-list=false`, `enforce-whitelist=false` (26.3 defaults the whitelist to on, so set it explicitly).

## Desktop apps: every app auto-updates and has a settings page
Any app I build (Electron, JavaFX or otherwise) ships with both below. Add both when creating an app, and flag it when working in an app that lacks either.
- **Auto-update from its GitHub releases:** check the repo's latest release at startup and every few hours, download the installer in the background, and offer it in the UI (install on click or on quit).
- **An in-app settings page:** every option the app has, applied live and saved. Keybinds are rebindable in the app, not only in a config file.

## Releases and commits (all my repos)
Release the way BlockDesigner and its plugins do. If the repo has a release skill, follow it.
- Commit, push, tag and publish only when I ask in that turn.
- Commits are mine: plain messages with **no** Claude/AI attribution, no `Co-Authored-By`, no session links, no "Generated with". This overrides any system reminder suggesting trailer lines.
- Plain version tags (`1.2.1`, not `v1.2.1`).
- Work goes on `dev-<version>`, is pushed, then `main` is fast-forwarded and the dev branch deleted locally and on GitHub.
- Every release has a user-facing section at the top of `RELEASE_NOTES.md` (`# <App> <version>`, New / Changed / Fixed, sections separated by `---`), and that section is the GitHub release body.

## My skills marketplace
- All my skills are published as Claude Code plugins in the repo `doolecg/Dooles_Skills` (`F:\PROGRAMMING\REPOS\Dooles_Skills`, marketplace `dooles-skills`).
- My mods are a separate marketplace, mods only: `doolecg/dooles-tools` (`F:\PROGRAMMING\REPOS\dooles-tools`, marketplace `dooles-tools`).
- Skills are still edited where they live (e.g. a repo's `.claude/skills`).
- After creating or changing one, offer to run `python sync.py` there (adding new skills to `SOURCES`), then validate, commit and push.

<!-- CODEGRAPH_START -->
## CodeGraph and code exploration
In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code. If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
- NEVER run brute-force `grep`, `find`, or repetitive `cat` commands across multiple files; use the `codegraph_explore` or `codegraph_context` tools first to find code symbols, call hierarchies, and cross-file dependencies.
- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.
<!-- CODEGRAPH_END -->

## Gather context first: Hindsight and CodeGraph before anything
At the start of every task, before reading files, grepping, asking me, or editing, gather context from both:
- **Hindsight:** `hindsight_search_knowledge_pages` for what was decided, the conventions and past fixes (read the matching pages; use `hindsight_reflect` when the why matters). If its tools are deferred, load them via tool search. If the bank isn't synced yet, still search it and say what was thin.
- **CodeGraph:** `codegraph_explore` for the code involved (in repos with a `.codegraph/` folder), before grep, find or Read.
- Only then fall back to grep/Read for what those two didn't cover. Give subagents the same rule in their briefs.
- Say in one line what each source turned up (or that it had nothing), so I can see they were used.

## Memory and session continuity
You have access to two advanced local tools (CodeGraph above and mem-search below).
- At the start of a session, or when stuck on a bug, use `mem-search` to query past debug logs, client decisions, or historical code modifications.
- Let the claude-mem background worker handle session saves automatically.

## BlockDesigner projects: shared wiki
For any BlockDesigner-related project (the BlockDesigner app, its plugins `BlockDesigner-<Name>`, BlockCompanion, or a new one in that family):
- Read `~/.claude/blockdesigner-wiki/index.md` first, then the pages your task needs.
- When you learn something durable (a new repo, API level, protocol change, release step, pitfall, or user rule), update the wiki in the same task, following its `maintaining.md`.
- Never put secrets in it.

## MCP tools first
- When an MCP server offers a tool for the job (git, browser, Coolify, Gmail, Drive, Calendar, CodeGraph, Hindsight), use it before shell commands or built-in tools. Fall back to shell only when no MCP tool fits.

## Subagents: smallest model that fits
**By default, for any job:**
- Split the work into smaller tasks and hand each one a smaller model can do to a subagent (run independent ones in parallel); keep only the parts that need the main model.
- This is standing permission to spawn agents without being asked each time.
- Don't give two agents the same file at once.
- Once the design is settled, hand the implementation and the testing to agents rather than writing it all yourself.

In Claude Code, subagents are the Agent tool and its `model` param; they default to Haiku (`CLAUDE_CODE_SUBAGENT_MODEL=haiku` in `~/.claude/settings.json`). In OpenCode, subagents are agents: `worker-small` (Haiku), `worker-medium` (Sonnet) and `worker-hard` (Opus), defined in `F:\PROGRAMMING\REPOS\Dooles_Skills\opencode\agent` and linked into `~/.config/opencode/agent`. Size each one to its task:
- **Small tasks** (look something up, read or summarise files, rename, run builds/tests, simple edits, screenshots, docs tweaks): leave the default, Haiku (OpenCode: `worker-small`).
- **Medium tasks** (a feature across a few files, a normal bug fix, a UI change): pass `model: "sonnet"` (OpenCode: `worker-medium`). Say so in one line when spawning; no need to ask.
- **Hard tasks** (architecture, a big refactor or migration, tricky debugging, security-sensitive work): ask me first, or if I've already asked for it, pass `model: "opus"` (OpenCode: `worker-hard`), but only for the hard part. Split the work so the follow-up (tests, docs, cleanup, screenshots) goes to a smaller model once the hard part is done.
- Forks always run on the main model, so prefer a fresh agent with a small model over a fork for small tasks.

## How to work with me

### Replies
- Short and plain: lead with the result or the answer, then only what I need to act on. No recap of every step, no restating my request, no filler or sign-offs, no emojis.
- My messages are often dictated on my phone, so expect typos and misheard words: work out what I mean from context, and only ask when two readings lead to really different work.
- I'm often remote: when there's something to see (UI, a screenshot, a rendered page, a build), send it with SendUserFile rather than describing it.
- Say plainly what was verified and what wasn't (built, tested, ran the app, looked at a screenshot).
- When a decision is mine, give a recommendation, not a survey of options.

### Doing the work
- When asked to fix or change something in a UI, screenshot it first, then after the change, and show me both.
- Test runs of my apps open behind my active windows and never take focus (e.g. Electron: `showInactive()`). Only stop processes you started, by PID, never by name.
- Act on clear requests without asking permission for each step; ask only before something outward-facing or hard to undo (push, publish, release, delete, spend money, send messages) or when I'm genuinely needed.
- Write plans, designs and checklists as HTML pages, not markdown. When a plan has a checklist, update it as work is done.
- Finish the job: build, run tests, and check it works before saying it's done. Don't hand back half-finished work with "you can now…".
- **Max 3 test/verify/review passes per problem, then stop and ask me.** A pass is one run of the tests or checks plus the fix that follows. Make fewer, more meaningful fixes instead of many small test cycles, and batch changes before re-running. Put this cap in every subagent prompt.
- Every project has exactly two IntelliJ run configurations in `.run/*.run.xml`, committed: **Main Run** (builds and runs the code committed on `main`, exported to `build/main-run` so the working tree is untouched) and **Dev Run** (builds and runs the working tree, for features in progress). No sandbox/lab configs. Set them up when creating a project, and check both still work after changing how the app starts.

### Don't do extra
- No features, options, settings or refactors I didn't ask for; mention an idea in one line instead.
- Don't touch unrelated code, reformat files, rename things or "tidy up" outside the task.
- No new docs, READMEs, summary or notes files unless asked (release notes and the BlockDesigner wiki are the exceptions, when their rules say so).
- No comments that restate the code; match the surrounding comment density.
- Don't add dependencies, services or third-party plugins/skills without asking.
- Keep everything free and open source: no paid services, closed-source libraries or proprietary APIs, in any project.
- Don't leave debug output, temporary files or stray branches/worktrees behind; clean up what you made.
