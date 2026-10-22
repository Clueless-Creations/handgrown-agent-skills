---
name: team-access
description: Read the brand team, grant or change roles, restrict or remove access, through person-approved proposals.
---

Call `handgrown_capabilities` first and use only tools it lists. Tools marked **coming** do not exist yet: never invent them.

If an action cannot be done through the Handgrown connector because the tool is missing (including tools marked **coming**), the connection scope is not enough, or the call returns an error other than a role or grant denial, tell the person you are switching to the browser. If you have a browser, open https://app.handgrown.app and let the person sign in themselves. Never type a password, sign-in code, API key or token. Do the same job in the web app and confirm before any consequential change. A denied role, missing grant or reserved action the app refuses is final: never use the browser to get around it. If you have no browser, give the person the Handgrown page and stop.

## Reads

`handgrown_team_members` lists people and roles. `handgrown_capabilities` tells you your own access.

## Changes

| Want | Tool |
| --- | --- |
| Invite a teammate or grant access | `handgrown_propose_team_access` |
| Change role, restrict, record impact | `handgrown_propose_team_update` |

Confirm every team change with the person. At Read and draft, share the `continue_url`. At Full access the server applies what the person's own role permits. You cannot raise your own connection level or assistant level; only a person does that in Handgrown.

Roles decide what every call can do. If the signed-in person lacks a role, the call is refused and that is final.
