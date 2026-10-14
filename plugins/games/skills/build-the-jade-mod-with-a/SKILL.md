---
name: build-the-jade-mod-with-a
description: Build the Jade mod with a temporary editor script at sdk/Assets/TempBuild/Editor/TempBuild.cs run through Unity batch mode. A successful build prints '[TempBuild] result=True'. Check the log for 'erro
---

# build-the-jade-mod-with-a

Drafted from a working procedure.

1. Build the Jade mod with a temporary editor script at sdk/Assets/TempBuild/Editor/TempBuild.cs run through Unity batch mode. A successful build prints '[TempBuild] result=True'. Check the log for 'error CS' to find real compile errors. Remove the temporary script once the build is done.

## Learned correction

- The TempBuild editor script needs its own TempBuild.asmdef in sdk/Assets/TempBuild/Editor that references ModSDK.Editor and includes only the Editor platform; remove it together with the script after the build. A full reimport after clearing sdk/Library is slow, so run the batch build in the background with a long timeout.

## Learned correction

- The temporary TempBuild editor script built here used a TempBuild.asmdef referencing ModSDK.Editor, limited to the Editor platform, next to the script. Run TempBuild.Run through -executeMethod, and delete the whole TempBuild folder afterwards.
