---
name: anand-laptops
description: Locate and use Anand's files, projects, notes, archives and agent history on his laptops - graphene (Linux) and Plutonium (Windows, usually online) - which share one ~/ layout. Use before reading or searching his files via LocalMCP2, Remote Desktop Commander or a local shell.
---

# Machines

- **Use local machine** if already on graphene or Plutonium.
- **Else use LocalMCP2**. Runs on graphene container. `~` = `/home/vscode` = `/home/sanand`. Mounts SOME folders (partly read-only). Missing paths may just be unmounted.
- **Else use Remote Desktop Commander - graphene** (Linux - bash) when LocalMCP2 access is not sufficient and the operation is safe.
- **Else use Remote Desktop Commander - Plutonium** (Windows - PowerShell 5.1) when LocalMCP2 & graphene are offline, e.g. while Anand travels.
  - It has the same `~/...` layout, but its `~/Documents` and `~/r2` may be older.
- Name the sources you couldn't reach. Unreachable is not the same as absent.
- **Paths:**
  - Prefer `"$HOME/..."` over `~` which works on bash AND PowerShell. Desktop Commander's file tools accept `~/...` on both machines.
  - Windows programs can't open Cygwin `/home/...` paths; pass native Windows paths.
- **Sync:**
  - `~/Dropbox` syncs live.
  - `~/code` holds independent git checkouts. Check branch and status; push and fetch.
  - `~/Documents` is copied ~hourly from graphene to `C:\Documents` by `~/code/scripts/services/sync-plutonium.sh` (updates, no deletions).
  - Graphene's agent history is copied to `C:\graphene`; Plutonium's native agent sessions, browser state and `~/r2` remain separate.

# Starting points

- `~/code/skills/README.md`: skill index.
- `~/code/skills/AGENTS.md`: for coding, shell, or filesystem-modification tasks.
- **Unclear or cross-source:** `uv run "$HOME/code/scripts/context.py" search '…'`, if `~/Documents/data/context/context.sqlite` exists.
  - Other subcommands: `entity`, `recent`, `open-loops`, `thread`, `style`, `assets`.
  - Hits are candidates, so deep-read the `~/...` locator.
  - `status` shows each source's latest item. The index can be fresh while a source is weeks old.
- **Code, projects:** `~/code/README.md` (repo index; if absent, list `~/code`), then the repo's `README.md` and `AGENTS.md`.
- **Blog, talks, demos, evals, data stories:**
  - `~/code/blog/description.md` (one line per post)
  - `~/code/talks/README.md`
  - `~/code/llmdemos/config.json`
  - `~/code/datastories/config.json`
  - `~/code/llmevals/README.md`
  - `~/code/til/README.md`
- **Notes, people, meetings, tasks:** `~/Dropbox/notes/`, especially `about/<person>.md`, `transcripts/` (date-named), `weekly-tasks.md` and `daily-*.md`.
- **Mail, chat, calendar, Drive:**
  - Live: `gws`. The default account is s.anand@straive.com (`~/.config/gws`).
  - For root.node@gmail.com or anand@study.iitm.ac.in, set `GOOGLE_WORKSPACE_CLI_CONFIG_DIR` to `~/.config/gws-<account>`.
  - Confirm the account before any write. Setup: `~/Dropbox/notes/gws-cli.md`.
  - History: `~/Documents/data/<account>/` covers mail, chat and calendar. For Drive, use `gws`.
  - Older mail: `~/Documents/Mail/` (its README explains the index).
- **WhatsApp, browsing, LinkedIn:** `~/Documents/data/` for archives; `~/code/scripts/README.md` for current builders/query CLIs.
- **ChatGPT and Claude conversations:** `~/Documents/chatgpt/`, `~/Documents/claude/`.
- **Coding-agent sessions:** `uv run "$HOME/code/scripts/agentlog.py" codex ls --limit 20` (or `claude` / `copilot`), on each machine.
  - On Plutonium, use `codex ls --root C:/graphene/.codex --limit 20` for graphene's copied history (similarly `claude` / `.claude` and `copilot` / `.copilot`).
- **Daily activity:** `~/Documents/activities/`.
- **Large files, media:** `~/r2/{files,media,private}/`.
- **Setup, personal CLIs:** `~/code/scripts/README.md`, `~/code/scripts/setup/{linux,windows}.md`, `~/Dropbox/scripts/`.

# Workflows

- Transcribe meeting recordings on graphene
  - Convert video to speech-quality Opus using the `opus` function in `~/code/scripts/setup.fish`. Save in `~/Documents/calls/` as `YYYY-MM-DD Meeting Title.opus`.
  - Transcribe via `~/code/scripts/call` into `~/Dropbox/notes/transcripts/*.md`. If speaker-labeled captions exist (e.g. embedded subtitles), use `## Meeting transcript context` in `~/code/blog/pages/prompts/fragments.md` to generate speaker context for `call --prompt` - along with attendee names, meeting notes, ...
  - Reuse existing files. Verify completion.
