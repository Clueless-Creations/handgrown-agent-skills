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
5. For accepted applicants, report admission, invitation, delivery and current membership separately (below). Report joining only from a current membership/progress read.

Summarize by state: New, Saved, Accepted (and where each is in admission), Denied, Withdrawn. Keep answers short and private.

## State changes

| Want | Tool | Notes |
| --- | --- | --- |
| Accept, deny, save for later | `handgrown_application_decision` | Confirm each with the person. Accept is a person's decision; at Read and draft you get a `continue_url`. See `applicant-review`. |
| Bulk decisions ("approve these three") | One `handgrown_application_decision` per application, each with its own `request_id` | List the names and outcome first and get one clear yes for the list. Report each result separately. |
| Saved back to New | `handgrown_application_return_to_review` | Only the latest Saved application. |
| Internal note | `handgrown_application_internal_note_add` | Plain text, no links. |
| Hold accepted people until launch | `launch-hold`, when its tools are listed | Confirm Member app access is Off before accepting. Saved is a different decision; never substitute it for an accepted hold without the person's choice. |

## Admission and invitations

- Admission steps (training, kit, kickoff): `handgrown_member_onboarding`, kickoffs via `handgrown_member_kickoff_get` / `handgrown_member_kickoff_report`.
- Per-application admission and progress: `handgrown_application_admission`, when listed. Use the current accepted application's ID; inspect invitation, training, kit, kickoff and membership as separate facts.
- Invitation history: `handgrown_member_invitations`, when listed. Includes held, pending, redeemed, revoked and expired links, actual delivery state, versions and expiry. Use application/applicant filters from authorized reads; keep them unchanged while following `next_after`. The older console manager list is actionable-only, so an empty page there does not prove no history exists. A null address is unavailable or erased; never reconstruct it.
- New Member issue: `handgrown_member_invitation_issue`, when listed. Confirm the exact person-supplied lowercase email and consequence, then use an open general task and stable `request_id`. On queues an invitation; Off holds it without invitation mail. This is a new invite, not reissue.
- Revoke: `handgrown_member_invitation_revoke`, when listed. Confirm the selected link/recipient and use its current ID/version and an open task. The exact review shows recipient, waiting/pending state and expiry. It stops the link, keeps existing membership and queues no email. Changed, expired, redeemed, revoked, Admin or unavailable links are refused; read current state before another proposal.
- Read uses the person's supported console action. Draft waits for exact human approval; Full applies after confirmation only within current role and the access class. Reconcile the approval and history after an uncertain reply, then reuse the identical `request_id` and arguments if retrying. A new ID is a new proposal.
- Reissue: `handgrown_member_invitation_reissue`, when listed. Confirm the selected pending, expired or revoked Member link, current version, exact recipient and consequence. Use an open task and stable `request_id`; the required lowercase email must match the original manual recipient or the current verified applicant email for an application-linked invitation. Never reconstruct an erased address. A current Admin decides; Full also requires the current access class. Replacement atomically stops a pending old link, preserves the original acceptor and history, and starts a fresh 7-day standard link when On. Off holds it with no invitation mail. A currently held link must use cohort-bound launch release, including after On. Changed policy, recipient, admission or authority needs a fresh read and confirmation. Reject remains available for stale proposals. Do not imitate replacement with separate revoke and issue calls.
- Joined members: `handgrown_active_ambassadors`.

Held means “Approved, waiting for launch.” Its original expiry is historical; eligible release starts a new 14-day clock. Queued, sent, delivered and joined are different facts. An existing active membership can coexist with a held invitation.
