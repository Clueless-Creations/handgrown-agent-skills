---
name: agreements
description: Store, pin and check application agreements, and read program agreement text.
---

Call `handgrown_capabilities` first and use only tools it lists. Tools marked **coming** do not exist yet: never invent them.

If an action cannot be done through the Handgrown connector because the tool is missing (including tools marked **coming**), the connection scope is not enough, or the call returns an error other than a role or grant denial, tell the person you are switching to the browser. If you have a browser, open https://app.handgrown.app and let the person sign in themselves. Never type a password, sign-in code, API key or token. Do the same job in the web app and confirm before any consequential change. A denied role, missing grant or reserved action the app refuses is final: never use the browser to get around it. If you have no browser, give the person the Handgrown page and stop.

## Application agreement (shown on the application form)

| Want | Tool |
| --- | --- |
| List stored versions | `handgrown_application_agreement_list` |
| Upload a new PDF or version | `handgrown_application_agreement_put` |
| Pin, replace or clear on the form | `handgrown_propose_recruiting_configuration` with `rules.agreement` |
| Did this applicant accept? | `handgrown_application_review_inspect` → `agreement_acceptance` |

Each brand uploads its own PDF. Nothing is shown to applicants until a version is pinned. Report acceptance as a record (document, version, title, time), never as proof of suitability. Confirm before pinning or replacing.

## Coming

Downloading the stored PDF and a brand-wide list of acceptances.

## Program and member agreements

Read with `handgrown_program_settings`; propose changes with `handgrown_propose_program_settings`. Members accept in their own session; you never accept for them.
