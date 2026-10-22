---
name: applicant-lifecycle
description: Answer questions about a brand's applicants end to end (counts, who is where, decisions, admission, invitations, members) and route to the right action.
---

Call `handgrown_capabilities` first and use only tools it lists. Tools marked **coming** do not exist yet: never invent them.

If an action cannot be done through the Handgrown connector because the tool is missing (including tools marked **coming**), the connection scope is not enough, or the call returns an error other than a role or grant denial, tell the person you are switching to the browser. If you have a browser, open https://app.handgrown.app and let the person sign in themselves. Never type a password, sign-in code, API key or token. Do the same job in the web app and confirm before any consequential change. A denied role, missing grant or reserved action the app refuses is final: never use the browser to get around it. If you have no browser, give the person the Handgrown page and stop.

## "Tell me about our applicants"

1. `handgrown_recruiting_overview` or `handgrown_recruiting_status` for each city: target, waiting, accepted, remaining.
2. `handgrown_application_review_counts` for New plus Saved, per city.
3. `handgrown_application_review_workspace` with `review_state` `new`, `saved` or `decided`. Follow every page. Say how many you read against the count.
4. Open individual applications with `handgrown_application_review_inspect` only when the person asks about specific people or wants recommendations (then follow `applicant-review`).
5. For accepted applicants, report admission and invitation separately (below). Never say someone joined unless their invitation is redeemed.

Summarize by state: New, Saved, Accepted (and where each is in admission), Denied, Withdrawn. Keep answers short and private.

## State changes

| Want | Tool | Notes |
| --- | --- | --- |
| Accept, deny, save for later | `handgrown_application_decision` | Confirm each with the person. Accept is a person's decision; at Read and draft you get a `continue_url`. See `applicant-review`. |
| Bulk decisions ("approve these three") | One `handgrown_application_decision` per application, each with its own `request_id` | List the names and outcome first and get one clear yes for the list. Report each result separately. |
| Saved back to New | `handgrown_application_return_to_review` | Only the latest Saved application. |
| Internal note | `handgrown_application_internal_note_add` | Plain text, no links. |
| Hold accepted people until launch | **coming** (`launch-hold`) | Until it ships, use Save for later: it sends nothing. |

## Admission and invitations

- Admission steps (training, kit, kickoff): `handgrown_member_onboarding`, kickoffs via `handgrown_member_kickoff_get` / `handgrown_member_kickoff_report`.
- Per-application admission and progress read: **coming** (`handgrown_application_admission`).
- Invitation list and status (pending, redeemed, revoked, expired): **coming** (`handgrown_member_invitations`).
- Issue, revoke or re-send an invitation: **coming** (`handgrown_member_invitation_issue`, `handgrown_member_invitation_revoke`). Use the browser fallback today, and confirm with the person first because issuing sends an email.
- Joined members: `handgrown_active_ambassadors`.
