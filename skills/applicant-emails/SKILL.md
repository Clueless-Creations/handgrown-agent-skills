---
name: applicant-emails
description: Draft and, only with the person's explicit confirmation, send emails to applicants (one or a filtered group) from templates. Planned capability: tools are coming.
---

Call `handgrown_capabilities` first and use only tools it lists. Tools marked **coming** do not exist yet: never invent them.

If an action cannot be done through the Handgrown connector because the tool is missing (including tools marked **coming**), the connection scope is not enough, or the call returns an error other than a role or grant denial, tell the person you are switching to the browser. If you have a browser, open https://app.handgrown.app and let the person sign in themselves. Never type a password, sign-in code, API key or token. Do the same job in the web app and confirm before any consequential change. A denied role, missing grant or reserved action the app refuses is final: never use the browser to get around it. If you have no browser, give the person the Handgrown page and stop.

## Status: coming

Planned tools (**coming**): `handgrown_applicant_email_templates`, `handgrown_applicant_email_draft`, a confirmed send that Handgrown queues and rechecks, and `handgrown_applicant_email_history`.

## What exists today

Handgrown sends only system emails to applicants: the application received receipt and the Member invitation on accept. Deny and save for later send nothing. There is no connector tool to email applicants yet.

## Until it ships

If the person asks you to "email the applicants we saved":

1. List them with `handgrown_application_review_workspace` (`review_state: saved`).
2. Draft the message in the chat and show the recipient count. Do not paste personal data into other apps.
3. If the person's own email tool is connected and they explicitly choose to send from it in this session, confirm recipients and text, then send there. Otherwise give them the draft and stop.
4. Never imply Handgrown sent it.

## When it ships

Always draft first, show the exact recipients (or count plus list for a group) and the final text, and get a clear yes before queuing. Bulk sends are rate-limited; a queued email is not sent until its status says so.
