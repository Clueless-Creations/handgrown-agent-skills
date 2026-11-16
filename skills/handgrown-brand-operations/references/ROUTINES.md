# Recurring work and replacements

The canonical brand-agent template defines two routines. Importing project instructions or a skill does not create either schedule. A normal Project chat and a Slack DM do not import Grok Bot routines or its saved cursor.

| Routine | Cadence in the brand's time zone | Work and replacement |
| --- | --- | --- |
| `handgrown-daily-changes` | Every day at 08:00 | Discover access, read changes or the operations queue and review counts, follow pending approvals, optionally reconcile configured products, report actionable changes. A qualified Claude scheduled task can run it; otherwise use an HQ scheduled job or a person running the Project prompt. |
| `handgrown-weekly-recruiting-status` | Monday at 09:00 | Read setup, city needs, counts, overview and open tasks; follow pending approvals and report missing facts. Use a qualified Claude scheduled task, an HQ scheduled job, or a weekly calendar reminder to run the Project prompt. |
| Change-feed polling, if enabled | Optional 15-minute business-hours check | Persist the brand-bound cursor and handled IDs outside chat memory. Honor `poll_after_seconds` and all pages. No built-in Project background poller is installed by this kit. Use an explicitly created and qualified scheduled task or an HQ worker with durable storage. |
| Event-driven follow-up and store portal work | On a real domain change or qualified retailer route | A chat cannot install Handgrown's event subscriptions, provider workers or a portal integration. Use existing Handgrown work/mandate workers, or an HQ job calling the authorized API. Keep the person's handoff where no qualified route exists. |

Claude now supports [scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) on paid plans. New tasks can run remotely with connectors. Team and Enterprise admins control availability. This is an available host feature, not proof that Handgrown authentication, cursor persistence and unattended approvals work in a particular account. Test a watched run and a later unattended run, including expiry or revocation, before enabling it for the team. Do not import a routine that asks Claude to create a nonexistent scheduler.

For an HQ replacement, an engineer must implement and qualify the job. Store scoped credentials in the server's secret store; never use a shared admin token. Persist cursor, recovery time, operation IDs and delivery receipts by brand and actor. Take a baseline first, read every page and deduplicate events. Recheck capabilities each run. Save no cursor on an unreported or throttled page; respect retry times. Reconcile uncertain writes with status reads and the same `request_id`. Keep applicant admission, store sending, legal and money gates. Notify only the agreed audience and stay quiet on unchanged runs. Stop on revocation or workspace mismatch.

The HQ implementation, Messages API example and key testing are outside this task by the owner's revised scope. Until a schedule passes qualification, a person runs these checks from the Project. The source routine text is bundled as a skill reference for that run, not as an installed job.
