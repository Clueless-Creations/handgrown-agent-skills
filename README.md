# Handgrown agent skills

Run your brand's Handgrown work from any connected AI assistant (Claude, ChatGPT, Grok Bot, Muse, Cursor, Codex and others): demo and sampling requests, events, recruiting and applicant review. These skills and instructions work the same way on every host.

Your history and knowledge live in Handgrown, not in any one assistant. Switch assistants or use several, and none of them starts from zero.

## The short version

Paste this into your assistant:

> Use https://github.com/Clueless-Creations/handgrown-agent-skills to set me up with Handgrown. Walk me through each step and wait for me where I need to click something.

Your assistant can't add connectors or sign in for you, so it will walk you through the steps below. Each person on your team does this with their own assistant and their own Handgrown account.

## Before you start

- You have a Handgrown account and can sign in to your brand's workspace.
- Your assistant supports remote MCP connectors. On a team or enterprise plan, an owner may need to allow custom connectors and skills first.

## 1. Add the Handgrown connector

Every host uses the same remote connector. No API key is needed.

```
https://app.handgrown.app/mcp
```

If Handgrown shows a different address under **Settings → Assistants**, use that one. If your assistant asks, choose automatic registration and leave client ID, secret and headers empty.

- **Claude:** **Customize → Connectors → Add custom connector**, name it **Handgrown**, paste the address.
- **ChatGPT:** add it as a custom connector/app where your plan allows it.
- **Claude Code:** clone this repo; the included `.mcp.json` adds the connector.
- **Cursor, Codex, VS Code, Gemini CLI and other MCP hosts:** add a remote (streamable HTTP) MCP server named `handgrown` with the address above.

## 2. Sign in and choose an access level

1. Click **Connect**. Handgrown's sign-in page opens.
2. Sign in and choose your brand's workspace.
3. Choose an access level:
   - **Read and draft** (the default): your assistant prepares proposals and you approve them in Handgrown.
   - **Full access** (shown only when your workspace offers it): your assistant can also apply the changes your brand role already allows, as you. It still confirms with you before anything consequential.
4. Approve the connection. Never paste passwords, codes or tokens into the chat.

## 3. Add the instructions and skills

Start with [`AGENTS.md`](AGENTS.md): entities, states, permissions and routing for any agent.

1. Paste [`PROJECT_INSTRUCTIONS.md`](PROJECT_INSTRUCTIONS.md) into your assistant's project or custom instructions (for example a private Claude Project or a ChatGPT project).
2. Add the skills. Each folder in [`skills/`](skills) is one skill. Start with `handgrown-brand-operations` and `event-management`; add the rest as you need them.
   - **Claude:** zip a folder and upload it under **Customize → Skills → Add skill → Upload skill**, then turn it on.
   - **Claude Code:** copy the `skills/` folders into `~/.claude/skills/`.
   - **Other hosts:** load the `SKILL.md` files the way your host supports skills or rules, or paste the relevant one into the conversation.

## 4. Try a first request

In a new conversation with Handgrown turned on, try these in order:

1. "Use Handgrown capabilities. Tell me which brand workspace I'm connected to and what access I have. Read only."
2. "Read our Handgrown work snapshot. Show what's open, what's waiting for approval, and the next useful step, with links."
3. "Prepare a demo request draft for one of our stores. Don't send, submit or book anything."

More to try: "Store this ambassador agreement PDF, list the versions we have, pin this version on the application form, and show me who accepted it."

If the brand shown in step 1 isn't yours, stop and disconnect the connector.

## How approvals work

Your assistant reads the request, checks it against your stores and calendar, and prepares a proposal (for example a new event, an offer to an ambassador, or a reply).

- **Read and draft:** each proposal comes back with an approval link. Approve or reject it in Handgrown; your assistant never approves on your behalf.
- **Full access:** after you confirm, Handgrown applies the change in the same call, as you, within your role and your workspace's limits. Holds, money movement, store submissions and anything your role can't do still stay with a person in Handgrown.

## When the connector can't do it

If a job can't be done through the connector (a missing tool, not enough access, or an error other than a role or permission denial), your assistant tells you it is switching to the browser. If it has one, it opens https://app.handgrown.app, you sign in yourself, and it does the same job in the web app, confirming with you before anything consequential. It never types your password and never uses the browser to get around something your role isn't allowed to do. Without a browser, it gives you the Handgrown page to finish yourself.

## What's in this repo

| Path | What it is |
| --- | --- |
| `PROJECT_INSTRUCTIONS.md` | Instructions to paste into your assistant's project or custom instructions |
| `skills/handgrown-brand-operations` | Main skill: demos, screening, hiring and events |
| `skills/event-management` | Create, change, offer and cancel events |
| `skills/event-materials` | Event prep materials |
| `skills/coverage-follow-up` | Fill uncovered events |
| `skills/applicant-review` | Screen applicants against your criteria |
| `skills/applicant-lifecycle` | Applicant states, admission and invitations |
| `skills/launch-hold` | Hold accepted invitations until launch; use only tools listed by the connected workspace |
| `skills/applicant-emails` | Automatic email copy and selected current contacts for the brand's own mail workflow; sender/tests need separate qualification |
| `skills/members-onboarding` | Training, kit and kickoffs |
| `skills/team-access` | Team roles and access |
| `skills/demo-requests` | Demo requests |
| `skills/agreements` | Application and program agreements |
| `skills/recruiting-launch`, `skills/recruiting-adoption` | Set up and run recruiting |
| `skills/change-check`, `skills/program-review` | Daily and weekly checks |
| `skills/task-continuity`, `skills/safe-retries`, `skills/shared-context`, `skills/handgrown-records` | Shared helpers |
| `.mcp.json` | Connector config for Claude Code |

## If something goes wrong

| What you see | What to do |
| --- | --- |
| No option to add a connector or upload a skill | Ask your organization owner to enable it. |
| Asked for a client ID or secret | Choose automatic registration. Don't paste a token. |
| Sign-in loop or no tools | Reconnect, sign in to the same Handgrown account, and check the workspace. |
| Wrong workspace | Stop and disconnect. Don't continue with that workspace's records. |
| Only read tools | Reconnect with Read and draft (or Full access) if your role allows it. |
| Full access isn't offered | Your workspace admin hasn't turned it on for your role; use Read and draft. |
| Rate limit (429) | Wait the time shown, then try again. |

## License

MIT
