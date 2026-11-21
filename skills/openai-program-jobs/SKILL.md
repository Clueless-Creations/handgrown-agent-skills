---
name: openai-program-jobs
description: Run a Handgrown catch-up in ChatGPT, set up three scheduled program jobs, or monitor supported Handgrown events with a dot.
---

# Handgrown in ChatGPT and dots

Start with `handgrown_capabilities` on the brand's selected connection. Verify the workspace and signed-in person's access. Read `handgrown_guide` and its Program jobs topic. For a source sync, read Synced context too. Keep cursors, source permissions and delivery audiences separate by workspace. A person can say **“Catch up Handgrown”** in a chat to run the first prompt once.

## ChatGPT Scheduled

For recurring work the person requested, ask ChatGPT to save these three tasks in the brand's time zone. Use the person's chosen times. The examples leave half an hour between the sync and the morning brief. Include the full prompt in each task; a task in a Project cannot read that Project's uploaded files. Select the authorized Handgrown app and the sources the job requires. Update an equivalent existing task in place.

| Task | Example time | Task prompt |
| --- | --- | --- |
| Catch up Handgrown | Daily at 08:30 | “Check my Handgrown workspace and Program jobs guide. Read changes since the last successful cursor and the current open queue and handoffs. Link what needs a decision. On the first run, take a baseline and show what is open.” |
| Sync Handgrown sources | Daily at 08:00 | “Check my Handgrown workspace and Synced context guide. Read only the email or calendar sources I enabled for sync. Save permitted matches, report the covered window and counts for each source, and keep the previous successful cursor if coverage is incomplete.” |
| Weekly Handgrown takeaways | Monday at 09:00 | “Read last week’s Handgrown events, reports and handoffs in the brand’s reporting time zone. Give the dates, counts, missing reports and takeaways with record links. Report privately here.” |

Read back the enabled trigger and next run in Scheduled. Check a watched run and the next unattended result for the correct workspace and source access. If a task lacks its app, permissions, available task slot or scheduler, run its prompt on request and tell the person which recurring task is missing. [ChatGPT scheduled tasks](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)

## Dot monitoring

Use the installed Handgrown plugin and the brand connection in a Work task. Ask the dot which Handgrown event types the connector advertises, then request monitoring for handoff creation or change, new applications and answered stops. Subscribe only to types that the connector actually lists and the person authorized. Verify the subscription and its scope on this connection. Keep unsupported event types pending and explain which updates will come through catch-up. Report event capability only after an actual subscription succeeds. [OpenAI MCP Events](https://developers.openai.com/plugins/build/mcp-events)

An event is a reason to reread the record. Deduplicate its identity and version, inspect the current handoff or application and check whether a person has already answered. Keep private background research read-only. Do authorized writes in an assigned task, reuse its operation ID on retry and verify its receipt. When the agent needs a decision, record the stop on the same handoff and give the person its link. Retain one daily catch-up for delayed or missed delivery. A first baseline or an unavailable event stream also requires checking the current queue and open handoffs. [Dot tasks and memory](https://learn.chatgpt.com/docs/dots/tasks-and-memory)

## Record the result

When discovery lists the host-profile, schedule registration and run-report tools, use the installed plugin manifest version. Report the actual host as `chatgpt` or `openai_dots`. Record a daily source schedule only for an enabled source sync with a confirmed host schedule. Read back its cadence, next run and connection. The catch-up and weekly summaries remain host tasks. For each attempted source record the actual trigger, window, counts and outcome. A completed check with zero matches is a success. An unreadable source stays partial or failed. Reuse its request ID on retry. If Handgrown does not return the receipt, say which part still needs verification.
