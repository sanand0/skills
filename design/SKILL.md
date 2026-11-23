---
name: design
description: ALWAYS follow this design guide for any front-end work
---

Design principles:

- Dark mode. Add a toggle. Text should contrast background on both modes in ALL elements / states.
- Responsive. Be mobile-friendly at any device size.
- Accessible. Allow extensive keyboard navigation, e.g. for popups on tables, shortcuts for selections, etc.
- Bookmarkable. Capture state in the URL `#path?key=value`. Sharing the URL reproduces the view, with tabs, filters, slider positions, etc. captured. Prefer replaceState()

Prefer creative, distinctive frontends that surprise and delight, not generic, "on distribution" outputs.
A good way is to copy the design of a niche site highly related to the topic. If you do so, mention the site, reason, and what's copied.

Focus on:

- Typography: beautiful, unique, and interesting fonts, not generic fonts like Arial, Roboto, Inter, system. Opt for distinctive choices that elevate the frontend's aesthetics.
- Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.
- Motion: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.

Use tooltips and popups as informative and engaging aids.

- Use **tooltips** for:
  - Explaining the non-obvious
  - Context for data points on table cells, chart elements, etc. (always)
- Use **popups** for:
  - Quotes / citations with links
  - File links. Render Markdown as HTML (syntax-highlighted), tabular data as sortable tables (with gradient-colored numbers)
  - Rich context on table cells, chart elements, etc. with narratives, cards, tables, charts, or even entire dashboards if required
  - Always allow arrow keys to navigate between popups on adjacent table cells, chart elements, etc.

Use icon libraries. Use SVG favicons e.g.

```html
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg%20xmlns ... %3C%2Fsvg%3E"/>
```

Prefer native platform behavior. Before choosing how to build or fix a tooltip, preview, dialog, or animation, run `npx -y modern-web-guidance@latest search "<behavior>"`. Run `npx -y modern-web-guidance@latest retrieve <id>` for the best match by description. If the CLI is unavailable, use the [online guide index](https://developer.chrome.com/docs/modern-web-guidance/guides).

Example searches: `prevent tooltip viewport clipping`, `preview link on hover`, `light dismiss modal dialog`, `animate same page view transitions`, `scroll entry exit effects`.

Keep essential interactions usable by keyboard and touch on the project's supported browsers. Treat motion as an enhancement and respect reduced-motion preferences. If custom JS handles placement, dismissal, focus, or scroll animation, comment why the native pattern doesn't fit.
