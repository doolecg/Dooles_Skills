# README preset (every repo)

Used whenever a README is asked for or rewritten, in any repo. The layout follows the Graphify project's README (https://github.com/Graphify-Labs/graphify): what it is, a 30-second start, what you get, then the detail. The words are ours; the plain-writing rules in CLAUDE.md section 11 apply.

Order. Drop a section that has nothing real to say; never fill one with filler.

1. **Title and one sentence.** What it turns into what, for whom. No tagline, no badges row unless there are real CI or release badges.
2. **Picture.** One real screenshot or output image, with a one-line caption saying what it shows. Skip it for libraries with no visual output.
3. **Get started in about 30 seconds.** One line of requirements (versions, OS), then at most three commands or steps, then "that's it" and what the user now has. If the tool writes files, show them as a short tree with a few words each.
4. **What it does.** A two-column table: Capability | What you get. Five to eight rows, each a real, checkable thing.
5. **Common commands.** One code block, each line commented. The ones people use daily, not the full reference.
6. **Install.** Every supported method, the recommended one first. Project-scoped or portable options if they exist. Platform notes in one line each.
7. **Using it with other tools.** Only if the project plugs into editors, AI assistants or CI: what to run once, what it writes, how to remove it.
8. **Configuration.** The config file name, a short example with comments, and the one gotcha people hit first.
9. **Privacy.** What stays on the computer and what leaves it, per feature. Say "nothing leaves your machine" only when that is true.
10. **Docs.** A short link list: quickstart, reference, how it works, troubleshooting.
11. **Contributing.** Where to start, how to run the tests, what a good contribution is.
12. **Credits.** Required when the project is modelled on another one: name the originals, say what is borrowed (ideas, never code or text unless the licence allows it).
13. **Licence.** One line, then the "Disclaimer" section from `~/.claude/dooles-rules/disclaimer-template.md`.

House rules for this preset

- Sentence-case headings, no numbering, no emoji.
- Commands the reader can paste. Never a placeholder that cannot run.
- Every claim in the table is something the project does today. Planned work goes in a "Not built yet" line, or not at all.
- Keep it to what a person reads in two minutes before deciding to install. Detail goes in `docs/`.
- Do not create a README unprompted (CLAUDE.md section 5). This is the layout when one is asked for.
