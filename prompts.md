# Prompts

## Codex skills setup, 25 Nov 2026

<!--
cd ~/code/skills
codex --model gpt-6.2-sol --config model_reasoning_effort=medium
-->

When I run codex in any directory, I think it picks up skills from this directory - `~/code/skills/` - under the [anand-skills] group.
Is that right? How does it do it - I mean what config enables that? Or is it something done via ChatGPT.com?

---

My ChatGPT Plus account (open on the browser, CDP localhost:9222, use devtools skill, prefer background operations than bringing into focus) allows plugins to be uploaded via https://chatgpt.com/plugins.
But I can't find a way to keep a live GitHub repo as a plugin. Is there one? If so, add https://github.com/sanand0/skills/.
Else, if only upload is supported, create a `just zip` option that bundles what's required and lets me upload it. Upload it and test it.

<!-- codex resume 01a21040-78de-75e1-9929-4f1a129b54ab -->

## Improve anand-laptop, 10 Nov 2026

<!--
cd ~/code/skills
codex --model gpt-6.1-sol --config model_reasoning_effort=high
-->

What corrections / improvements does anand-laptop/SKILL.md need? Find everything that’s broken, inconsistent, inefficient, or no longer needed.
`ssh plutonium` can help check on Plutonium.
See ~/code/scripts/ - especially services/sync-plutonium.sh, but also others - and recent commits, actual usage logs of mcpserver and `npx @wonderwhy-er/desktop-commander`.
Fix what you’re sure about and list the rest for me to review, prioritized, in anand-laptops/improvements.md, dated today.

---

Do you REALLY need every change you fixed in SKILL.md? If not, undo, and move to "Remaining work, prioritized". Is what's remaining the MINIMAL change that would achieve the intended results? If not, minimize the change.

<!-- codex resume 01a1c3b1-839c-78f1-bee2-244147919619 -->
