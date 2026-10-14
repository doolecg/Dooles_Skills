---
name: to-run-the-dev-effectcraft-while
description: To run the dev EffectCraft while another agent builds, copy effectcraft.exe and element-setup.exe from the build target folder into a separate run folder (F:\PROGRAMMING\ec-run-dev), then start it the
---

# to-run-the-dev-effectcraft-while

Drafted from a working procedure.

1. To run the dev EffectCraft while another agent builds, copy effectcraft.exe and element-setup.exe from the build target folder into a separate run folder (F:\PROGRAMMING\ec-run-dev), then start it there with --control 9877. Set EC_LINK_EXPORT and ELEMENT_SETUP_EXE to point at that copy. This stops the running app from locking the build files.
