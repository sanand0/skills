# Laptop skill audit — 10 November 2026

After a minimality review, retained only direct navigation/command corrections in [SKILL.md](SKILL.md). Broader additions from the first revision were undone and moved to the remaining-work list below. The highest remaining priorities are restoring reliable Graphene → Plutonium sync, making Plutonium's live Google access usable, and refreshing stale LocalMCP2 tool metadata. The remaining items below need an operational change, a policy choice, or more evidence; they are not claims that every related workflow is broken.

## Scope and evidence

- Audited the existing skill line by line, including its uncommitted LocalMCP2-first routing changes. Preserved that preference and the unrelated `prompts.md`.
- Read `~/code/scripts/` entrypoints, `services/sync-plutonium.sh`, `daily-activities`, `agentlog.py`, `context.py`, `mcpserver.py`, `dev.sh`, setup guides, and relevant recent commits. Important changes: `121f2fc` (20 October, full Documents copy), `8be31f8` (2 November, agent/private-file copies), `6ca6ffd` (3 November, agent prompts command), `da2f4b7` (6 November, Fish sync abbreviation), `8dc5fed` (9 November, skill consolidation), and `73d2169` / `5de5a2b` (10 November, fixes and tool retirements).
- Verified SSH to Plutonium, its native home/junctions, shell/version, available CLIs, copied data, Git heads/status, and Desktop Commander configuration. Both Desktop Commander devices were online. LocalMCP2 successfully inspected the current skill through its own file tool.
- Examined actual Desktop Commander `~/.claude-server-commander/tool-history.jsonl` on both machines, plus selected failures. This is the usage history of the running `@wonderwhy-er/desktop-commander` installation, not an inference from npm download logs. Device connection logs are separately under `~/.desktop-commander-device/remote-<weekday>.log`.
- Streamed LocalMCP2 `~/.local/share/sanand-scripts/mcpserver/events.jsonl` for 15 October–9 November, inclusive. Used tool-call records for totals and separate Bash records for exit status; did not double-count their duplicate Bash records. Also checked startup logs, sync run logs, and context query logs. No raw private conversation/tool outputs were added to this repository.

| Retained usage examined | Calls | Observation |
| --- | ---: | --- |
| LocalMCP2, 15 October–9 November UTC | 6,393 | 4,580 Bash calls; 630 `read_file`, 251 `read_files`, 245 `search`, 364 `edit_block`, 118 `list_directory`, 99 `file_info`, 105 downloads, 1 upload |
| Desktop Commander on graphene, 26 October–10 November UTC | 1,613 | 827 process starts, 381 output reads; actual examples of PowerShell sent to Bash |
| Desktop Commander on Plutonium, 31 October–9 November UTC | 1,846 | 838 process starts, 287 output reads; actual examples of Bash sent to PowerShell |

LocalMCP2's Bash status records contain 4,202 successes, 339 failures, 33 timeouts and 6 errors. These are command outcomes, not a measure of tool reliability: some were intentional probes or failed external commands. Text matches in logged output can quote source code/errors and are not reliable failure counts. Desktop Commander sometimes replaces output over 4,096 bytes with an omission marker, so its retained history cannot prove every final outcome.

## Minimal corrections retained in the skill

Compared with the user's pre-audit file, this revision adds 83 words (576 → 659), down from roughly 1,100 words in the first revision. The original description, routing preference, context-freshness advice, browser/transcription workflow and source-labeling instructions are preserved.

| Retained correction | Why it is needed |
| --- | --- |
| Explicit DC device and Bash/PowerShell choice | Both devices can be online; actual logs show commands sent to the wrong shell in both directions. One sentence is enough. |
| Native Windows paths without a blanket Cygwin prohibition | Windows programs cannot open Cygwin `/home/...` paths, but the rsync setup deliberately uses Cygwin. |
| Documents replication, copied agent history and sync run-log location | The original per-machine claim was incorrect and hid Graphene's history on Plutonium. The successful-apply check prevents assuming the hourly timer means fresh data. |
| Check `context.sqlite`, not just its parent directory | A directory alone does not establish that the queryable index exists. |
| Conditional gws authentication and the exact default work-config path | Plutonium's default account has no saved credentials; logs also show a guessed, incorrect work-config directory. Existing account-before-write guidance is sufficient. |
| Maintained builder/query README | The archive README names nonexistent builders and the wrong LinkedIn posts filename. Route to the maintained script index rather than copy schemas into the skill. |
| Runnable, bounded agent-history listing and replica roots | The old backend-only command displays help; native Plutonium roots omit `C:\graphene` history. |

## Remaining work, prioritized

### P1 — 1. Unrelated private-code symlinks can stop all personal-data replication

🟢 DONE 11 Nov 2026. Commit 32751e6: sync-plutonium.sh skip environments, etc.

**Confirmed.** In `~/.cache/sanand-scripts/sync-plutonium/run.log`, the 10 November apply run completed at **10:16:02 +08:00**. The 11:38 run skipped on network policy. The **12:06:56** run failed before transferring any group because `code/exam/.private/face-expressions/.venv-pyfeat/lib64` is a directory symlink. The validator accepts only symlinks to files within their source root, so this normal generated virtual-environment link aborts Documents and agent-history refresh too.

**Review:** exclude generated environments consistently from validation and transfer, and consider making independent transfer groups fail independently while retaining an overall failed status. Decide whether generated environments belong in the private-code backup at all. Verify with a small fixture containing this directory symlink before running the real service; then confirm a complete apply run. Do not remove the validator or treat “timer active” as success.

Source: [sync-plutonium.sh](../../scripts/services/sync-plutonium.sh), source validation and `run_sync` ordering; [service guide](../../scripts/services/README.md). The service may fail again until the source or exclusion policy changes.

### P1 — 2. Plutonium's live Google fallback is unauthenticated

🟢 DONE 11 Nov 2026. Commit cd7c40a: setup/windows.md gws config

**Confirmed for the default work account.** A fresh Desktop Commander PowerShell process returned `gws auth status` with `auth_method: none`, `storage: none`, no encrypted/plain credentials and no token cache. A `client_secret.json` exists, which is not a signed-in account. Retained Plutonium calls on 6/9 November returned Google 401 “No credentials provided”. Other account folders exist, but their live authentication was not verified in this audit.

**Review:** decide which accounts must work independently on Plutonium; authenticate each there and run a small read from every required service. Verify service identity, not just configured scopes. Graphene credentials/keyring state are not made portable by copying Documents. The skill now describes authentication as conditional instead of promising live access.

### P1 — 3. Advertised LocalMCP2 paths still reference retired skill locations

🟢 DONE 11 Nov 2026. Restarted.

**Confirmed mismatch; cause not fully isolated.** This session's LocalMCP2 Bash tool description advertises `~/code/scripts/agents/*/SKILL.md` and `~/code/blog/pages/skills/*/SKILL.md`. Current `mcpserver.py::MOUNTED_PATHS` uses `~/code/skills/*/SKILL.md`; the old locations were consolidated on 9 November. The latest recorded server startup was **9 November 04:55:28 UTC**. A live `file_info` call successfully reached the new laptop skill, so stale advertising does not establish that the actual mount is missing.

**Review:** restart through the normal `mcpserver` wrapper if its running code is old, refresh LocalMCP2 tool discovery in ChatGPT, and check the advertised paths plus a real read in a new conversation. Distinguish old process code from cached plugin schemas before changing mount configuration. See [setup/localmcp.md](../../scripts/setup/localmcp.md). No server or connector restart was performed during this audit.

### P2 — 4. Filtered agent-history listing parses the full archive

🟡 #MEDIUM

**Confirmed code path and observed cost.** `agentlog.py::_can_stream_ls` disables streaming for date/cwd filters. `CodexBackend.list_sessions` reads every candidate JSONL before applying its final limit. On Plutonium, an offline Python 3.12 invocation of `codex ls --root C:/graphene/.codex --since 2026-11-08 --limit 1` returned a valid copied session, but the combined context-status/list process took **62.52 seconds**. This is a combined runtime, not an isolated agentlog benchmark. A prior default-interpreter invocation exceeded a 60-second SSH observation window, so interpreter/dependency startup may also contribute.

**Review:** benchmark a dated sample, then add safe candidate pruning or a summary index without dropping sessions updated outside their creation-date directory. Preserve sorting by actual session timestamps. The skill uses the cheaper unfiltered example; the detailed filter warning remains here rather than in the skill. Source: [agentlog.py](../../scripts/agentlog.py).

### P2 — 5. Plutonium has no r2 copy

🟢 DONE. Commit 6bb5d53: sync-plutonium.sh: sync r2

**Confirmed absence at the intended locations.** `C:\r2` and `$HOME/r2` were missing. The sync service does not include r2. The setup guide's intended layout is not proof that its copy/link steps were completed.

**Review:** choose the travel/offline subset of `files`, `media`, and `private` worth maintaining, or explicitly accept that these sources require graphene. Decide cadence/storage before copying. Do not create a junction to a nonexistent target and call it repaired.

### P2 — 6. A fresh context index still has source gaps

🟢 DONE. Requested Claude export.

**Confirmed.** Both machines reported build `2026-11-09T23:21:56.114496+00:00`, Drive missing, and Claude stale with latest content **27 September**. ChatGPT's latest indexed content was **4 November**. Fresh mail/chat/calendar/transcript rows do not repair these gaps. `context.py` does not index browser history or coding-agent logs either; its `SourceConfig` and builders enumerate a narrower source set.

**Review:** decide whether Claude exports need refreshing and whether any offline Drive cache is actually wanted. Drive's absence is consistent with the current skill's live-gws route; it is not automatically a defect requiring a new backup system. Use dedicated browsing/agent tools for sources outside context coverage. Direct-source fallbacks can be chosen for the task without adding a generic search checklist to the skill.

### P2 — 7. Data archive documentation contains dead names

🟢 DONE

**Confirmed.** `~/Documents/data/README.md` refers to removed/misnamed builders and `linkedin-posts.json`; the actual posts are JSONL. `~/code/scripts/README.md` correctly names `backupwhatsapp.py` and `browsing_history.py`. The data README also calls browsing storage Edge history without explaining that current builders can include recoverable Shortcuts records.

**Review:** update the archive README in its own data workspace, including current builders, actual formats and schemas. First establish the current LinkedIn export producer; do not invent a replacement for the missing `backup_linkedin.py`. The skill no longer relies on this README for maintained script names.

### P2 — 8. Replication has overwrite semantics, no deletion convergence or version recovery

🟢 #DROP for now. I will handle deletes later.

**Confirmed behavior; policy decision.** `rsync -rlt --copy-links` uses neither `--update` nor destination backup/versioning, and there is intentionally no `--delete`. Changed Windows files can be overwritten, while Graphene-deleted files persist on Windows. Old and renamed data can therefore coexist; a complete successful run does not prove identical inventories. The header's “update-no-delete” wording does not mean “preserve newer destination files”.

**Review:** keep this as an archive/replica if intentional. If Windows edits to copied Documents must survive, define ownership/conflict handling first. If deleted-source visibility or historical recovery matters, choose a manifest/versioned backup strategy rather than blindly adding `--delete` or `--update`. The skill retains only “updates, no deletions”; the fuller overwrite/conflict-policy discussion stays here.

### P2 — 9. Plutonium scripts are behind Graphene, with local work present

🟢 #DROP for now. Each may have separate working code.

**Confirmed snapshot.** Graphene scripts HEAD was `5de5a2b` (10 November); Plutonium was `8dc5fed` (9 November) and had untracked `preferences.py`. Both skills checkouts were at `10a6792` before this audit's uncommitted changes. Private-file replication does not advance these Git checkouts; it can also supply ignored files alongside an older checkout.

**Review:** integrate the scripts updates on Plutonium while preserving its local work, and separately propagate this reviewed skill change through the usual Git workflow. Do not blanket-reset, auto-stash or assume all of `C:\code` is synchronized. The original branch/status and push/fetch guidance is unchanged; operational integration remains separate.

### P3 — 10. Setup notes contain historical observations that should stay dated

🟢 #DROP

**Mixed: one now corroborated, one no longer reproduced.** [setup/windows.md](../../scripts/setup/windows.md) says Desktop Commander's reboot connectivity was unverified. Plutonium's last boot was 6 November, its `DesktopCommanderRemote` task last started shortly afterward, its task result was `267009` (running), and live DC access worked today. This corroborates access after that boot, but does not isolate the scheduled task as the sole cause or test another reboot.

The same guide says DC processes inherit `XDG_DATA_HOME=/home/Anand/.local/share`. A fresh DC process today had **no** `XDG_DATA_HOME`, so that workaround should not become an unconditional skill instruction. `pwsh` was not found in SSH command discovery; PowerShell 7 syntax should not be assumed.

**Review:** update dated setup evidence, and test startup causality/recovery in a planned reboot window if required. Keep runtime quirks in the setup guide, not a growing list of permanent laptop-skill prohibitions.

### P3 — 11. Tool logs are expensive and incomplete audit sources

🟢 DONE. Commit 83e37e8: mcpserver events.jsonl is rotated monthly

**Confirmed.** LocalMCP2 `events.jsonl` was about **603 MiB**, with Bash requests/results also represented by tool-call records and readable Markdown copies. Desktop Commander retained windows differed by machine and capped some outputs at 4,096 bytes. Logs show both substantial file-tool use and many legitimate shell tasks; the larger Bash count alone is not evidence that calls should be mechanically converted.

**Review:** choose retention/rotation for MCP events and a compact per-call outcome index if repeat audits are useful. Keep full diagnostic data only as long as needed, and preserve pointers to detailed records. For DC, include later output reads when judging success; a start record with a PID or truncated output is not a final result. Avoid copying operational log-management instructions into this navigation skill.

### P3 — 12. Optional skill expansions removed from the first revision

🔴 #DROP

These are review candidates, not required work. They may be useful for a particular task, but do not justify permanent instructions in this short navigation skill. Prefer the existing tool descriptions/setup guides unless a repeated failure proves a concise addition is needed.

| Undone or reduced addition | Where it belongs / review decision |
| --- | --- |
| Narrower description, a new local-shell-first branch, and a Plutonium-own-state routing exception | Restored the original description and the user's existing LocalMCP2-first routing. Consider changing invocation/routing only if that behavior is wanted; the audit did not establish a need to redesign it. |
| Mandatory `list_devices`/`deviceId` sequence, PID polling and mount-retry instructions | Retained only explicit device/shell choice. Tool descriptions already explain discovery, process sessions, polling and access failures. |
| Container-isolation warning and extra access-guide dependency | [setup/localmcp.md](../../scripts/setup/localmcp.md) already documents the default Docker socket and host mounts. Relevant when configuring access, not for every file lookup. |
| SSH routing, `cmd.exe` default and UTF-16LE encoded-command recipe | Verified during this audit, but optional setup/remote-shell guidance. Add to [setup/windows.md](../../scripts/setup/windows.md) if SSH use recurs; it need not be another default route in this skill. |
| Windows home/junction inventory and Cygwin transport details | Keep the layout in the Windows setup guide. The skill needs only compatible path syntax. |
| Private-code/env sync inventory, unmetered policy, overwrite details, `:` → `%3A` names and Copilot SQLite backup mechanics | Keep implementation detail in [sync-plutonium.sh](../../scripts/services/sync-plutonium.sh) / its service guide. The skill retains the Documents/history destinations, no-delete summary and freshness-log pointer. If a Windows lookup misses a colon-containing name, try the service's `%3A` spelling. Review overwrite policy under item 8. |
| Generic zero-hit/direct-source checklist and longer snapshot/live explanations | Original index-hit, source-date and inference guidance already covers the essential distinction. Specific coverage gaps remain in item 6. |
| Full account-directory table, Bash/PowerShell selector examples, process persistence and extra identity checks | Original secondary-account selector plus the corrected default work path are enough. Put syntax/auth troubleshooting in `~/Dropbox/notes/gws-cli.md`; item 2 covers the actual missing credentials. |
| Archive filename/schema warnings and hard-coded LinkedIn JSONL filename | Fix the archive documentation under item 7; use the maintained script index in the skill. |
| Agent `prompts`/`md`, ISO-date rules, archived-session inventory and filtered-scan caveats | Discover subcommands via `--help`; item 4 records the actual performance issue. The skill only needs a working bounded listing and copied-history root. |
| Expanded browser/localhost guidance, “Fish” wording and rewritten answer/source labels | Restored the existing browser, transcription and answering sections. No demonstrated defect requires expanding these instructions. |

## Verification and limits

- Skill frontmatter/scaffold validator and `git diff --check` passed after minimization. Compared the final skill against a reconstruction of the user's pre-audit file, including their existing routing edit; only the seven corrections above remain.
- Executed `context.py status` on graphene and Plutonium and read a copied Graphene Codex session through `agentlog.py` on Plutonium. Checked CLI help/source for added subcommands/options and archive roots.
- The new unfiltered agent-history example, sampled with `--limit 1` on graphene, completed in **0.20 seconds**. This is a sample on a different machine, not a controlled speedup comparison with the filtered Plutonium run. All report links resolved locally, and listed missing archive builders were checked for actual absence.
- Verified the new paths through local inspection, SSH and a real LocalMCP2 file call; checked DC device discovery and a real explicitly selected PowerShell process through completion.
- Existing recording/transcription inputs and workflow definitions were inspected; no paid transcription was run. Did not log in accounts, transfer user data, modify services, refresh/restart connectors, reboot, commit, or change Plutonium's checkouts. The initial default-interpreter SSH status/list command timed out; the later offline Python 3.12 DC check completed, so that timeout is not presented as a data-access failure.
- Retained logs are samples/windows, not a complete history of every machine interaction. Findings above distinguish observed failures, source-proven behavior, and choices that remain for review.
