# <Project name>

<What it is in two or three sentences: what kind of thing, what it is like and not like, the long-term target. Say if it is a long-term project built in milestones.>

## Team
- **<Owner>:** <what they do>. <How much code they read. How to explain changes to them: plain English, small steps, exact clicks in which tool.>
- **Claude:** <what Claude owns, e.g. all programming>.

## Stack
<Engine/framework and version, language, tooling Claude should use to build, test and read logs, source control (Git LFS if there are binaries), where art or assets come from.>

## Pillars (every feature must serve at least one)
1. **<Pillar>.** <One line.>
2. **<Pillar>.** <One line.>

## Architecture rules
- <Settled rule.> <Date if it was a decision: "(decided YYYY-MM-DD)".>

## The Bible (read first)
`docs/bible.html` is THE reference: what the project is, <Owner>'s settled decisions, the milestone order (trunk before branches: a crude skeleton of the whole thing, then depth passes), how a milestone runs, and where every idea goes. Claude runs project management from it. New ideas are placed with its section 6 rules into its idea map, never slipped into the milestone in progress. Update its map, idea map and change log whenever a milestone starts, finishes or changes.

## Status
<One line: what phase is done.> Full map: `docs/bible.html` section 4.

| Milestone | State | Guide |
| --- | --- | --- |
| 1 "<name>" (<scope in a few words>) | <Planned / In progress: approved YYYY-MM-DD / Done YYYY-MM-DD> | `docs/milestone-1-guide.html` |

Older guides: <list>. The why behind decisions: `docs/design.md`. What the systems are and how they connect: `docs/systems.md`.

**Not built yet** (each has a home in the bible): <list>.

## Conventions (settled; follow these)
- **<Area>:** <rule>. <Date if decided.>

## Working style
- One small step at a time. After each step, tell <Owner> how to test it, with exact clicks or commands.
- <Commit cadence for this repo, e.g. "Commit after each working step with a clear message (standing permission for this repo)." Leave out to use the global rule.>
- Test steps go in the relevant `docs/milestone-N-guide.html`.
- Comment the why, not the what; prefer readable over clever.
- Keep these docs current and short: update `docs/bible.html`, this file's status and `docs/systems.md` when a milestone or system changes. Guides record how to test; design.md records why.
- <Owner's time budget, e.g. "under 3 hours a week: concepts come in one bundle at a milestone's start, one review checklist (30 to 60 minutes) at its end. Don't wait on reviews; fixes from them jump the queue.">
- In skeleton milestones, crude is fine: no polish, tune at the end.
