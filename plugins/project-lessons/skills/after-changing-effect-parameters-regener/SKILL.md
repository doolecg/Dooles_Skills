---
name: after-changing-effect-parameters-regener
description: After changing effect parameters, regenerate the effects doc with `UPDATE_DOCS=1 cargo test -p effectcraft-effects --lib effects_doc_is_current`. Then run that test again without the variable to confi
---

# after-changing-effect-parameters-regener

Drafted from a working procedure.

1. After changing effect parameters, regenerate the effects doc with `UPDATE_DOCS=1 cargo test -p effectcraft-effects --lib effects_doc_is_current`. Then run that test again without the variable to confirm it passes.
