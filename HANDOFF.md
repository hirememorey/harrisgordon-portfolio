## Developer Handoff

This doc brings you up to speed fast and tells you exactly what to do next.

### Project snapshot
- Stack: Astro v5 + Tailwind CSS v4 (via `@tailwindcss/vite`)
- Node: 20+, npm: 10+
- Global CSS: `src/styles/global.css`
- Layout shell: `src/layouts/Layout.astro` (imports Inter font, base meta)
- Page: `src/pages/index.astro`
- Components: `Hero.astro`, `OperatingSystem.astro`, `CaseStudy.astro`

### Current state
- Layout updated with title, meta description, viewport, Inter font, and base body classes.
- Homepage assembled with `Hero`, `OperatingSystem`, and three populated `CaseStudy` entries.
- `CaseStudy` now uses native `<details>/<summary>` for disclosure (no JS). Labels swap via CSS using group-open.

### What’s left (high-signal)
1) Typography and spacing polish (see ROADMAP.md). Ensure consistent vertical rhythm across sections and responsive heading scales.
2) Apply the Tailwind refinements listed in ROADMAP.md (spacing, typography, responsive tweaks).
3) Add basic SEO/OG/Twitter meta and canonical URL in `Layout.astro`; consider `theme-color`.
4) Decide on deployment target (Vercel/Netlify/Cloudflare) and set up a CI deploy.

### How to run
```bash
npm install
npm run dev
```
Open the printed local URL.

### Where to work
- Content and structure: `src/pages/index.astro`
- Section components: `src/components/*.astro`
- Design system utilities: `src/styles/global.css`

### CaseStudy data shape (for quick reference)
- Props: `title: string`, `oneLiner: string`, `keyResults: string[]`, `situation: string`, `intervention: string[]`, `playbook: string[]`

### Known considerations
- Keep JS minimal. `CaseStudy` uses small inline script for toggle.
- Maintain semantic HTML and accessible focus/ring states.

If you need more detail or open questions, see ROADMAP.md and CASE_STUDIES_TODO.md.


