---
name: demo-requests
description: Read and act on demo requests and their ops alerts. Decisions and alternates are coming.
---

Call `handgrown_capabilities` first and use only tools it lists. Tools marked **coming** do not exist yet: never invent them.

If an action cannot be done through the Handgrown connector because the tool is missing (including tools marked **coming**), the connection scope is not enough, or the call returns an error other than a role or grant denial, tell the person you are switching to the browser. If you have a browser, open https://app.handgrown.app and let the person sign in themselves. Never type a password, sign-in code, API key or token. Do the same job in the web app and confirm before any consequential change. A denied role, missing grant or reserved action the app refuses is final: never use the browser to get around it. If you have no browser, give the person the Handgrown page and stop.

## Reads (live)

- `handgrown_demo_review_notifications` and `handgrown_demo_request_ops_alerts` for incoming requests and alerts.
- `handgrown_demo_review_preferences` / `handgrown_demo_review_preferences_set` for who gets notified.

## Coming

Listing requests, decide, withdraw, propose alternates and demo-adjustment decisions have no connector tool yet. Use the browser fallback and confirm each decision with the person first.

To turn an approved request into an event, follow `handgrown-brand-operations` and `event-management` (`handgrown_propose_event_drafts`).
