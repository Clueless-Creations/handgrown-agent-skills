---
name: launch-hold
description: Hold accepted invitations as 'Approved, waiting for launch', review the eligible release cohort and propose an Admin's launch release when these tools are listed.
---

Call `handgrown_capabilities` first and use only tools it lists. Tools marked **coming** do not exist yet: never invent them.

If an action cannot be done through the Handgrown connector because the tool is missing (including tools marked **coming**), the connection scope is not enough, or the call returns an error other than a role or grant denial, tell the person you are switching to the browser. If you have a browser, open https://app.handgrown.app and let the person sign in themselves. Never type a password, sign-in code, API key or token. Do the same job in the web app and confirm before any consequential change. A denied role, missing grant or reserved action the app refuses is final: never use the browser to get around it. If you have no browser, give the person the Handgrown page and stop.

## Tools, when listed

Availability comes from this workspace's live discovery. Missing tools do not prove access is On or Off. Read the current policy in the supported console flow before accepting if the person requires no invitation email.

| Tool | Purpose |
| --- | --- |
| `handgrown_member_access_get` | Read Member app access (default On), current policy version and held count. |
| `handgrown_member_access_set` | Propose the Admin's exact On/Off change. On alone keeps existing holds. |
| `handgrown_held_applicants` | Page through held invitations and their release eligibility. |
| `handgrown_held_release` | Preview first with `dry_run: true`; propose the exact eligible cohort, selected template and counts with `dry_run: false`. |

## Hold and release

- While access is **Off**, accepting records the decision/admission and holds the Member invitation with no invitation email queued. The applicant sees "Approved, waiting for launch". Current held accepts still count toward city targets; they are not joined members.
- Existing memberships keep their own truth. Turning On alone does not release held invitations. A held invitation's original expiry is historical; eligible release issues a fresh 14-day link from release.
- Follow all held-list cursors. Preview the cohort, ready/blocked counts and offered message templates. Show these to the person and obtain an explicit yes to the exact release and queued email. Blocked rows remain held; do not promise that every held person will receive a new link.
- Propose with the current policy version, basis digest, chosen template and expected release/blocked counts from that preview. A material change needs a new preview and confirmation. If nothing is eligible, report the blocked work rather than inventing a release.
- Use an open general task and a stable `request_id`; inspect the live schema, including any ID required for preview. A proposal is a different intended request from its preview. Keep the exact proposal ID/arguments for retries and reconcile the approval/history first after an unknown result.
- An Admin's human decision is required for policy changes and bulk release even at Full. Full never turns a release proposal into an automatic launch. At Read, use the supported console review. These controls do not grant another role or bypass a missing permission.
- Release queues eligible invitations at the server's controlled pace. Queued is not sent, delivered or joined. Read the resulting policy, held list and invitation/admission history before claiming the requested change.

Save for later sends no invitation, but it is a different review decision. Never silently substitute it for acceptance. Do not use a new invitation or a reissue to evade the held cohort's release checks.
