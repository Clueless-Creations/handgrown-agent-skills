# Catch up Handgrown with Claude


## Run it now

**Catch up Handgrown** in a Claude chat or Project starts one run. Use the Program jobs guide with the selected workspace and the signed-in person's access. Read open handoffs, the changes since the last successful cursor, and the current queue. Give the person the date range, what changed, anything still waiting and links to the records. On a first run, take a baseline and report the open queue. Preserve the prior successful cursor after a partial read. If the connection or source is unavailable, identify the gap.

## Claude Code starter pack

The starter pack includes three prompts. Choose the brand’s time zone and the times the person wants. Run a prompt manually before enabling its cloud schedule. In Claude Code use `/schedule`, or create a scheduled task on the web. Give each task the exact prompt below, the Handgrown connector and only the other sources it needs. Confirm the workspace in the cloud session. Check `/schedule list` for its enabled trigger and next run. Check the first unattended run for the signed-in workspace, source access and a result. [Anthropic scheduled tasks](https://code.claude.com/docs/en/routines)

| Task | Example cadence | Prompt |
| --- | --- | --- |
| Morning catch-up | Daily at 08:30 | “Catch up Handgrown. Follow the Program jobs guide. Report changes and open handoffs with record links. Use the last successful cursor for this workspace.” |
| Daily source sync | Daily at 08:00 | “Sync the email and calendar sources I enabled for this workspace. Follow the Synced context guide. Reconcile against the last successful source window, record the outcome for each enabled source and tell me what needs attention.” |
| Weekly takeaways | Monday at 09:00 | “Give me last week’s Handgrown takeaways. Use the brand’s reporting time zone. Name the dates, demos, reported results, missing reports and open handoffs. Link the records behind each takeaway.” |

Check the account's existing scheduled tasks before creating one. Update an equivalent task in place. Compare with the recruiting routines below to avoid a second daily products sync or a second weekly summary covering the same work.

## Claude Duet

Use the **Handgrown** plugin or the **Handgrown brand operations** skill on the same Claude account. Open Duet and ask it to verify the expected workspace through the Handgrown connector. Ask it to include Morning catch-up in the built-in morning brief and to use Daily source sync when it checks authorized sources. A person can also start either prompt in a message. List a custom schedule only when Duet displays its enabled cadence. When it gives no cadence, report the built-in brief or the manual run as observed. [Anthropic’s Duet guide](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)

For a long product import, start a separate Duet thread for that import. Read the Products guide, keep the catalog source IDs and import receipts in Handgrown, and use those receipts to resume the same batch. When a handoff hits its limit, record its stop against the existing handoff and read the result. Bring its link and the exact decision to Duet’s next check-in. The recipient can answer in Handgrown’s Needs you. Recheck the saved decision before continuing.

## Report what the host actually runs

Read the installed Handgrown package version from the plugin manifest or the Project bundle’s VERSION file. After discovery, use `handgrown_sync_host_profile_set` when available. Report `claude` for Claude chat and Claude Code or `claude_duet` for Duet, that installed package version and the capabilities this connection demonstrated. A periodic check has `always_on: false`. Report events only after an actual subscription. Read back the profile with `handgrown_sync_health`.

Once a **source sync** has a confirmed schedule, use `handgrown_sync_schedule_set` for each enabled source with its source kind, platform, cadence in minutes and next run if known. A daily sync has cadence 1440. Source schedules are keyed by connection and source. Morning catch-up and weekly takeaways stay on the host unless they actually run a source sync; do not overwrite the daily source schedule to register another task. When the source schedule is removed, clear its cadence and next run in Handgrown and verify the receipt.

Report each attempted source through `handgrown_sync_run_report` when available. Use the actual trigger, times, source window, counts and outcome, including a successful zero-match run. Reconcile an uncertain write with its original request ID. If a reporting tool is absent or refuses the operation, say which receipt is missing. A chat response, a saved task and a successful unattended run are distinct results.

## Existing recruiting routines

The canonical brand-agent template defines two routines. Importing project instructions or a skill does not create either schedule. A normal Project chat and a Slack DM do not import Grok Bot routines or its saved cursor.

| Routine | Cadence in the brand's time zone | Work and replacement |
| --- | --- | --- |
| `handgrown-daily-changes` | Every day at 08:00 | Discover access, read changes or the operations queue and review counts, follow pending approvals, optionally reconcile configured products, report actionable changes. A qualified Claude scheduled task can run it; otherwise use an HQ scheduled job or a person running the Project prompt. |
| `handgrown-weekly-recruiting-status` | Monday at 09:00 | Read setup, city needs, counts, overview and open tasks; follow pending approvals and report missing facts. Use a qualified Claude scheduled task, an HQ scheduled job, or a weekly calendar reminder to run the Project prompt. |
| Change-feed polling, if enabled | Optional business-hours check at the host’s supported cadence | Persist the brand-bound cursor and handled IDs outside chat memory. Honor `poll_after_seconds` and all pages. No built-in Project background poller is installed by this kit. Use an explicitly created and qualified scheduled task or an HQ worker with durable storage. |
| Event-driven follow-up and store portal work | On a real domain change or qualified retailer route | A chat cannot install Handgrown's event subscriptions, provider workers or a portal integration. Use existing Handgrown work/mandate workers, or an HQ job calling the authorized API. Keep the person's handoff where no qualified route exists. |

Claude now supports [scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) on paid plans. New tasks can run remotely with connectors. Team and Enterprise admins control availability. This is an available host feature, not proof that Handgrown authentication, cursor persistence and unattended approvals work in a particular account. Test a watched run and a later unattended run, including expiry or revocation, before enabling it for the team. Do not import a routine that asks Claude to create a nonexistent scheduler.

For an HQ replacement, an engineer must implement and qualify the job. Store scoped credentials in the server's secret store; never use a shared admin token. Persist cursor, recovery time, operation IDs and delivery receipts by brand and actor. Take a baseline first, read every page and deduplicate events. Recheck capabilities each run. Save no cursor on an unreported or throttled page; respect retry times. Reconcile uncertain writes with status reads and the same `request_id`. Keep applicant admission, store sending, legal and money gates. Notify only the agreed audience and stay quiet on unchanged runs. Stop on revocation or workspace mismatch.

The HQ implementation, Messages API example and key testing are outside this task by the owner's revised scope. Until a schedule passes qualification, a person runs these checks from the Project. The source routine text is bundled as a skill reference for that run, not as an installed job.
