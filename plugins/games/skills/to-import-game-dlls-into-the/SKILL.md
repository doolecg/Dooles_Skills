---
name: to-import-game-dlls-into-the
description: To import game DLLs into the Core Keeper SDK, call ImporterWindow.UpdateFromGamePath(ImporterSettings.Instance, gamePath, out added) from a temporary editor script via Unity -batchmode -executeMethod.
---

# to-import-game-dlls-into-the

Drafted from a working procedure.

1. To import game DLLs into the Core Keeper SDK, call ImporterWindow.UpdateFromGamePath(ImporterSettings.Instance, gamePath, out added) from a temporary editor script via Unity -batchmode -executeMethod. Move non-compiling project scripts aside first, or the batch run aborts before the method runs.
