---
name: effectcraft-is-built-and-run-from
description: EffectCraft is built and run from F:\PROGRAMMING\ec-build-elementcraft. Stop only the PID you started, then run `cargo build --bin effectcraft`. Launch target\debug\effectcraft.exe with `--control 987
---

# effectcraft-is-built-and-run-from

Drafted from a working procedure.

1. EffectCraft is built and run from F:\PROGRAMMING\ec-build-elementcraft. Stop only the PID you started, then run `cargo build --bin effectcraft`. Launch target\debug\effectcraft.exe with `--control 9877`, and set ELEMENT_SETUP_EXE to target\debug\element-setup.exe. Confirm the port is listening with Get-NetTCPConnection on the new PID. The build took about 35 seconds.
