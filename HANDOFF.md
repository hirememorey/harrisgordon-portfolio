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
- Reading measure applied to main container; global vertical rhythm utility (`section-y`) and base prose leading in place.
- Homepage assembled with `Hero`, `OperatingSystem`, and three populated `CaseStudy` entries.
- `CaseStudy` is a bifurcated card: always-visible Key Results and Playbook, with the detailed narrative (Situation + Intervention) behind a native `<details>/<summary>` (no JS). Disclosure copy is explicit (“Read full story/Hide full story”). Optional metadata badges render if provided.

### What’s left (high-signal)
1) SEO/OG/Twitter meta and canonical URL in `Layout.astro`; consider `theme-color`.
2) Decide on deployment target (Vercel/Netlify/Cloudflare) and set up a CI deploy; add preview deploys.
3) Optional: lightweight analytics (Plausible/Umami).

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
- Keep JS minimal. `CaseStudy` uses native details/summary and no client JS.
- Maintain semantic HTML and accessible focus/ring states.

If you need more detail or open questions, see ROADMAP.md and CASE_STUDIES_TODO.md.


