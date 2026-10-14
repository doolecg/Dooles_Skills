---
name: to-calibrate-per-image-openai-cost-divid
description: To calibrate per-image OpenAI cost, divide the dashboard spend for an order by its number of image attempts. In the thumbnail-poc test, $1.04 over 9 edit attempts gave about $0.12 per attempt, so use 
---

# to-calibrate-per-image-openai-cost-divid

Drafted from a working procedure.

1. To calibrate per-image OpenAI cost, divide the dashboard spend for an order by its number of image attempts. In the thumbnail-poc test, $1.04 over 9 edit attempts gave about $0.12 per attempt, so use the usage tokens the API returns rather than a fixed constant.
