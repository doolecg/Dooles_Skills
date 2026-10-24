# Disclaimer template

Used by CLAUDE.md section 9 and readme-preset.md item 13. Written for UK law (England and Wales). Not legal advice; get a solicitor to check before selling anything.

## What the law lets you do (keep in mind when wording)

- The warranty and liability clauses in MIT (the capitals paragraph) and Apache 2.0 (sections 7 and 8) are the legal disclaimer. The README section points at them and makes them easy to see; it does not add new legal force. Never write wording that contradicts the licence.
- You can never exclude liability for death or personal injury caused by your negligence (Unfair Contract Terms Act 1977 s2(1); Consumer Rights Act 2015 s65 for consumers), or for fraud. Wording that claims to do this is void and makes the rest look unreasonable, so always keep "to the extent permitted by law".
- Free software given away on its own falls outside the Consumer Rights Act 2015 digital content rules (s33 covers content supplied for a price, or free with paid goods or services). If you ever charge, those statutory rights (satisfactory quality, fit for purpose, as described, and s46 repair or compensation for damage to the buyer's device or other content) cannot be excluded for consumers (s47). Paid products then need their own terms, not just MIT.
- EU users: the new Product Liability Directive (EU) 2024/2853 counts software as a product from 9 December 2026, and the Cyber Resilience Act adds security duties from 2026–2027. Both exempt free and open-source software made or supplied outside a commercial activity. Taking money (sales, paid support, ads in the app) can make it commercial.
- A repo with no LICENSE file is "all rights reserved": nobody may legally use, copy or change it, and there is no warranty disclaimer for them to agree to. Pick a licence before publishing.
- Third-party names: say you are not affiliated, and follow that company's brand rules.

## README section (paste under Licence)

```markdown
## Disclaimer

This software is provided "as is", without warranty of any kind, as set out in the [LICENSE](LICENSE). To the extent permitted by law, the authors are not liable for any loss or damage from using it, including lost data, lost work or damage to files or projects. Nothing here limits liability that cannot be limited by law, such as for death or personal injury caused by negligence.

Back up your work before using it. You use it at your own risk.
```

## README section for repos with no licence (all rights reserved)

Licence rule for repos with no LICENSE file: use the manifest's licence field if there is one. If the project is a fork, or built from an MIT (or other licensed) project, use that upstream licence and keep its copyright notice. Otherwise it is all rights reserved: add a LICENSE file containing the first paragraph below, and use this README block.

```markdown
## Disclaimer

Copyright (c) <year> doole. All rights reserved. No licence is granted to copy, change or share this code unless the author says so in writing.

This software is provided "as is", without warranty of any kind. To the extent permitted by law, the author is not liable for any loss or damage from using it, including lost data, lost work or damage to files or projects. Nothing here limits liability that cannot be limited by law, such as for death or personal injury caused by negligence.

Back up your work before using it. You use it at your own risk.
```

## In-app notice (About or Settings page)

> Provided "as is", without warranty, under the <MIT / Apache 2.0> licence. To the extent permitted by law, the authors are not liable for any loss or damage from using it. Back up your work.

Before a risky action (deleting or overwriting files, editing another program's data, bulk changes), show a confirm dialog that says what will change and that it cannot be undone.

## Extra lines by project type (add to the README Disclaimer section)

- Minecraft mods and tools: `NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.` (required by the Minecraft Usage Guidelines). No charging for the mod itself.
- Hytale mods: `Not affiliated with or endorsed by Hypixel Studios.` Follow Hytale's modding terms.
- Other game mods (Core Keeper and so on): `Not affiliated with or endorsed by <studio>. <Game> is a trademark of its owner.` Back up save files before installing.
- Blender add-ons: `Not affiliated with or endorsed by the Blender Foundation.` Add-ons that use Blender's Python API are generally treated as needing a GPL-compatible licence (GPL-2.0-or-later or GPL-3.0); check before publishing under MIT or Apache.
- Tools using Claude or other AI: `Not affiliated with or endorsed by Anthropic.` AI output can be wrong; check it before relying on it. Say what data is sent to the AI service.
- Scrapers and downloaders: `You are responsible for following the terms of service of any site you use this with, and for copyright in anything you download. Use it only for content you have the right to access.`
- Anything that collects or sends personal data: say what, where it goes and why (UK GDPR). If nothing leaves the user's machine, say so.
