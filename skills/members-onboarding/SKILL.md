---
name: members-onboarding
description: Configure and track member onboarding after acceptance: training, kit, cities and kickoffs.
---

Call `handgrown_capabilities` first and use only tools it lists. Tools marked **coming** do not exist yet: never invent them.

If an action cannot be done through the Handgrown connector because the tool is missing (including tools marked **coming**), the connection scope is not enough, or the call returns an error other than a role or grant denial, tell the person you are switching to the browser. If you have a browser, open https://app.handgrown.app and let the person sign in themselves. Never type a password, sign-in code, API key or token. Do the same job in the web app and confirm before any consequential change. A denied role, missing grant or reserved action the app refuses is final: never use the browser to get around it. If you have no browser, give the person the Handgrown page and stop.

## Tools (live)

| Want | Tool |
| --- | --- |
| Read onboarding status | `handgrown_member_onboarding` |
| Configure steps | `handgrown_member_onboarding_configure` |
| Record or report kit | `handgrown_member_onboarding_record_kit`, `handgrown_member_onboarding_report_kit` |
| Acknowledge a step | `handgrown_member_onboarding_acknowledge` |
| Kickoffs | `handgrown_member_kickoff_create`, `_get`, `_correct`, `_cancel`, `_record_attendance`, `_report`, `_link` |
| Live roster | `handgrown_active_ambassadors` |

These take effect under the person's edit access. Confirm creates, cancels and corrections first.

## Application admission and invitation history

When listed, `handgrown_application_admission` reads one current accepted application's canonical admission/progress; `handgrown_member_invitations` reads its filtered invitation history. Use the `applicant-lifecycle` skill for paging, issue/revocation approvals and retries. Acceptance, waiting for launch, email delivery and current membership remain separate facts; a held link can coexist with an existing membership.

## Coming

Kit-code completion for an application and brand↔member message threads. Invitation replacement is available only when discovery lists `handgrown_member_invitation_reissue`; follow `applicant-lifecycle`.

A member is not event-ready until onboarding and any agreements are complete. Report each step separately.
