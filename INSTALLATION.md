# Installation

I clone to `~/code/skills`:

If `~/.agents/skills` already exists as a real directory, inspect and move it aside first. `ln -sfn` would otherwise create a **nested** `skills` symlink inside it instead of replacing it. Keep any third-party skills you still use separately.

```sh
gh repo clone sanand0/skills ~/code/skills
cd ~/code/skills && just install-hooks  # regenerate README on every commit
mkdir -p ~/.agents ~/.claude ~/.codex ~/.copilot
# Update skills paths
ln -sfn ~/code/skills ~/.agents/skills  # Codex, Pi, Copilot, OpenCode
ln -sfn ~/code/skills ~/.claude/skills  # Claude Code
# Replace `AGENTS.md` - global coding-agent rules.
ln -sfn ~/code/skills/AGENTS.md ~/.codex/AGENTS.md
ln -sfn ~/code/skills/AGENTS.md ~/.copilot/copilot-instructions.md
# Tell Claude to use AGENTS.md
printf "@$HOME/code/skills/AGENTS.md\n@AGENTS.md\n" >> ~/.claude/CLAUDE.md
# Tell OpenCode to use AGENTS.md
jq --arg file "$HOME/code/skills/AGENTS.md" '.instructions = [$file, "AGENTS.md"]'  ~/.config/opencode/opencode.jsonc | sponge ~/.config/opencode/opencode.jsonc
```

### Claude online

Add `sanand0/skills` under **Customize → Plugins → Add marketplace**, enable automatic sync, and install the `anand-skills` plugin.
The `.claude-plugin/` manifests make every skill available without manually maintaining a plugin list.

### ChatGPT online

In Custom Instructions, keep a short list of high-priority skill names and triggers.
Fetch the full skill on demand from `https://github.com/sanand0/skills/blob/main/{name}/SKILL.md` using the GitHub connector (or web); inspect the repository for additional skills when useful. Changes to skill bodies require no Custom Instructions update.
