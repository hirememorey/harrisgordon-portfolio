## Developer Handoff

This doc brings you up to speed fast and tells you exactly what to do next.

### Project snapshot
- Stack: Astro v5 + Tailwind CSS v4 (via `@tailwindcss/vite`)
- Node: 20+, npm: 10+
- Global CSS: `src/styles/global.css`
- Layout shell: `src/layouts/Layout.astro` (imports Inter font, base meta)
- Page: `src/pages/index.astro`
- Components: `Hero.astro`, `OperatingSystem.astro`, `CaseStudy.astro`, `PlaybooksSection.astro`

### Current state
- Section order is Hero → Operating System → Proof → Deep Dive (System Architecture).
- Layout updated with title, meta description, viewport, Inter font, and base body classes.
- Reading measure applied to main container; global vertical rhythm utility (`section-y`) and base prose leading in place.
- `Hero` includes a one‑sentence results snapshot with links to each case study; CTA jumps to `#proof`.
- `OperatingSystem` is intentionally one step denser so the full block appears in the first view on common laptop sizes.
- `CaseStudy` is a bifurcated card: always-visible Key Results and Playbook, with the detailed narrative (Situation + Intervention) behind a native `<details>/<summary>` (no JS). Disclosure copy is explicit ("Read full story/Hide full story"). Optional metadata badges render if provided.
- `PlaybooksSection` is a specialized component for technical case studies with GitHub integration, featuring the same bifurcated layout as CaseStudy but with additional technical implementation details.

### Recent decisions
- The hero snapshot sentence begins with a small inline label: `Case studies:`. It remains in the same paragraph as the three links to preserve the fold.
- Spacing between Hero and Operating System is slightly tightened via Hero bottom padding and Operating System top padding. Check fold at 1280×800 and 1440×900 after copy changes.
- Visible copy avoids em/en dashes and heavy punctuation. Prefer short sentences and simple phrasing. The meta description also avoids em dashes.
- Resolved "Playbook" terminology ambiguity by renaming technical section to "Deep Dive: System Architecture" to distinguish from business case study playbooks.
- Updated technical case study content to focus on personal problem-solving narrative and system architecture outcomes.

### What’s left (high-signal)
1) SEO/OG/Twitter meta and canonical URL in `Layout.astro`; consider `theme-color`.
2) Decide on deployment target (Vercel/Netlify/Cloudflare) and set up a CI deploy; add preview deploys.
3) Optional: lightweight analytics (Plausible/Umami).
4) Create an OG image.

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
- Alignment system: single axis for body copy (left-aligned). Exceptions: hero headline can be centered; Operating System heading is centered on small screens only and left-aligned from `md` up. All multi-line text remains left-aligned at all sizes.

### Fold acceptance criteria
- Targets: 1280×800 and 1440×900
- Without scrolling: name, thesis, CTA + Email/LinkedIn, one‑sentence snapshot, and the full Operating System block are visible.

If you need more detail or open questions, see ROADMAP.md and CASE_STUDIES_TODO.md.


