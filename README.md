# Handgrown for Claude

Run your brand's Handgrown work from Claude: demo and sampling requests, events, recruiting and applicant review. Claude prepares drafts and proposals. You still approve anything consequential in Handgrown.

## The short version

Paste this into Claude:

> Use https://github.com/Clueless-Creations/handgrown-claude-skills to set me up with Handgrown. Walk me through each step and wait for me where I need to click something.

Claude can't add connectors or sign in for you, so it will walk you through the steps below. Each person on your team does this with their own Claude and their own Handgrown account.

## Before you start

- You have a Handgrown account and can sign in to your brand's workspace.
- On a Claude Team or Enterprise plan, an owner has allowed custom connectors and custom skills (**Organization settings → Connectors** and **Skills**).

## 1. Add the Handgrown connector

1. In Claude, open **Customize → Connectors → Add custom connector**.
2. Name it **Handgrown**. For the address, use the one shown in Handgrown under **Settings → Assistants**. If there isn't one, use:

   ```
   https://app.handgrown.app/mcp
   ```

3. If Claude asks, choose **Register automatically**. Leave client ID, secret and headers empty.

## 2. Sign in with your Handgrown account

1. Click **Connect**. Handgrown's sign-in page opens.
2. Sign in, choose your brand's workspace, and pick **Read and draft**.
3. Approve the connection. Never paste passwords, codes or tokens into the chat.

## 3. Add the project instructions and skills

1. Create a private Claude Project for your brand.
2. Paste the contents of [`PROJECT_INSTRUCTIONS.md`](PROJECT_INSTRUCTIONS.md) into the Project's instructions.
3. Add the skills. Each folder in [`skills/`](skills) is one skill. Zip a folder (for example `skills/handgrown-brand-operations`) and upload it under **Customize → Skills → Add skill → Upload skill**, then turn it on. Start with `handgrown-brand-operations` and `event-management`; add the rest as you need them.

   Using Claude Code instead? Clone this repo and copy the `skills/` folders into `~/.claude/skills/`. The included `.mcp.json` adds the connector.

## 4. Try a first request

In a new conversation in the Project, with Handgrown turned on, try these in order:

1. "Use Handgrown capabilities. Tell me which brand workspace I'm connected to and what access I have. Read only."
2. "Read our Handgrown work snapshot. Show what's open, what's waiting for approval, and the next useful step, with links."
3. "Prepare a demo request draft for one of our stores. Don't send, submit or book anything."

If the brand shown in step 1 isn't yours, stop and disconnect the connector.

## How approvals work

When a demo or event request comes in, ask Claude to review it. Claude reads the request, checks it against your stores and calendar, and prepares a proposal (for example a new event, an offer to an ambassador, or a reply). Each proposal comes back with an approval link. Open the link and approve or reject it in Handgrown. Claude can then check the result and tell you what happened. Claude never approves on your behalf.

## What's in this repo

| Path | What it is |
| --- | --- |
| `PROJECT_INSTRUCTIONS.md` | Instructions to paste into your Claude Project |
| `skills/handgrown-brand-operations` | Main skill: demos, screening, hiring and events |
| `skills/event-management` | Create, change, offer and cancel events |
| `skills/event-materials` | Event prep materials |
| `skills/coverage-follow-up` | Fill uncovered events |
| `skills/applicant-review` | Screen applicants against your criteria |
| `skills/recruiting-launch`, `skills/recruiting-adoption` | Set up and run recruiting |
| `skills/change-check`, `skills/program-review` | Daily and weekly checks |
| `skills/task-continuity`, `skills/safe-retries`, `skills/shared-context`, `skills/handgrown-records` | Shared helpers |
| `.mcp.json` | Connector config for Claude Code |

## If something goes wrong

| What you see | What to do |
| --- | --- |
| No option to add a connector or upload a skill | Ask your Claude organization owner to enable it. |
| Asked for a client ID or secret | Choose Register automatically. Don't paste a token. |
| Sign-in loop or no tools | Reconnect, sign in to the same Handgrown account, and check the workspace. |
| Wrong workspace | Stop and disconnect. Don't continue with that workspace's records. |
| Only read tools | Reconnect with Read and draft if your role allows it. |
| Rate limit (429) | Wait the time shown, then try again. |

## License

MIT
