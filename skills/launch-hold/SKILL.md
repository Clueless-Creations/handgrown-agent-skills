---
name: launch-hold
description: Hold accepted applicants as 'Approved, waiting for launch' and release them all at once when the brand launches. Planned capability: tools are coming.
---

Call `handgrown_capabilities` first and use only tools it lists. Tools marked **coming** do not exist yet: never invent them.

If an action cannot be done through the Handgrown connector because the tool is missing (including tools marked **coming**), the connection scope is not enough, or the call returns an error other than a role or grant denial, tell the person you are switching to the browser. If you have a browser, open https://app.handgrown.app and let the person sign in themselves. Never type a password, sign-in code, API key or token. Do the same job in the web app and confirm before any consequential change. A denied role, missing grant or reserved action the app refuses is final: never use the browser to get around it. If you have no browser, give the person the Handgrown page and stop.

## Status: coming

The launch hold is planned and not yet live. Do not call any tool on this page until `handgrown_capabilities` lists it.

Planned tools (**coming**):

| Tool | Purpose |
| --- | --- |
| `handgrown_member_access_get` | Read the brand's member app access switch (on/off) and the held count. |
| `handgrown_member_access_set` | Turn the switch on or off. Person-approved; brand admin only. |
| `handgrown_held_applicants` | List accepted applicants whose invitation is held. |
| `handgrown_held_release` | Release every held invitation (with `dry_run` count first), choose the welcome message, and turn access on. |

## How it will work

- While access is **off**, accepting records the decision and admission, but the invitation is **held**: no email is sent. The applicant sees "Approved, waiting for launch". Held accepts still count toward city targets.
- Release moves every held invitation to pending and sends the welcome email. The 14-day link starts at release.
- Before release: run the dry run, tell the person the exact count and message, and get an explicit yes. Release is a bulk email send.

## Until it ships

Accept sends the Member invitation immediately. If the person wants to approve people without notifying them yet, use **Save for later** (`handgrown_application_decision` with `save_for_later`), which sends nothing, and tell them that is the interim hold.
