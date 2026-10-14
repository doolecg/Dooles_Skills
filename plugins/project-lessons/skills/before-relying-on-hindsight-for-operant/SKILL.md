---
name: before-relying-on-hindsight-for-operant
description: Before relying on Hindsight for Operant, call hindsight_sync_status and hindsight_diagnose. If synced is false, most knowledge pages are still empty, so answer code questions with codegraph_explore in
---

# before-relying-on-hindsight-for-operant

Drafted from a working procedure.

1. Before relying on Hindsight for Operant, call hindsight_sync_status and hindsight_diagnose. If synced is false, most knowledge pages are still empty, so answer code questions with codegraph_explore instead.

## Learned correction

- Search Hindsight on every Operant task even when hindsight_sync_status reports synced false. That flag only means the knowledge pages are incomplete, and the user rejected skipping Hindsight in favour of CodeGraph alone.

## Learned correction

- The before-relying-on-hindsight-for-operant skill says to skip Hindsight and use codegraph_explore when synced is false. The user rejected that, so search Hindsight anyway with small queries and use CodeGraph alongside it.

## Learned correction

- The before-relying-on-hindsight-for-operant skill tells you to skip Hindsight and use codegraph_explore when synced is false. The user rejected that. Keep searching Hindsight with small queries even when synced is false, and use CodeGraph alongside it.

## Learned correction

- Search Hindsight on every Operant task even when hindsight_sync_status reports synced false, and use CodeGraph alongside it. The skill's advice to skip Hindsight in that case is wrong, because the user rejected it.

## Learned correction

- Search Hindsight on every Operant task, with small queries, even when hindsight_sync_status reports synced false, and use CodeGraph alongside it. The user rejected the skill's advice to skip Hindsight and rely on CodeGraph alone in that case.

## Learned correction

- Search Hindsight with small queries on every Operant task, even when hindsight_sync_status reports synced false, and use CodeGraph alongside it. The user rejected the skill's advice to skip Hindsight and rely on CodeGraph alone in that case.
