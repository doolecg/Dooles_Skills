---
name: before-deleting-old-dev-branches-on
description: Before deleting old dev-* branches on origin, confirm each is fully merged with `git rev-list --count origin/main..origin/dev-<version>`, which must print 0. Then delete them with `git push origin --d
---

# before-deleting-old-dev-branches-on

Drafted from a working procedure.

1. Before deleting old dev-* branches on origin, confirm each is fully merged with `git rev-list --count origin/main..origin/dev-<version>`, which must print 0. Then delete them with `git push origin --delete <branches>` and check `git branch -a`.
