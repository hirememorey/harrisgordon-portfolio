## Developer Handoff

This doc brings you up to speed fast and tells you exactly what to do next.

### Project snapshot
- Stack: Astro v5 + Tailwind CSS v4 (via `@tailwindcss/vite`)
- Node: 20+, npm: 10+
- Global CSS: `src/styles/global.css`
- Layout shell: `src/layouts/Layout.astro` (imports Inter font, base meta)
- Page: `src/pages/index.astro`
- Components: `Hero.astro`, `BaseCaseStudy.astro`, `CaseStudy.astro`

### Current state
- Section order is Hero (Thesis) → Proof (Business Case Studies) → Operating System (AI-Native Development Methodology & Proof).
- Layout updated with title, meta description, viewport, Inter font, and base body classes.
- Reading measure applied to main container; global vertical rhythm utility (`section-y`) and base prose leading in place.
- `Hero` includes a one‑sentence results snapshot with links to each case study; CTA "Explore the Proof" jumps to `#proof`.
- `Proof` section leads with three business case studies demonstrating Turnaround Operator & Venture Builder capabilities.
- `Operating System` section showcases AI-native development methodology with three core pillars AND demonstrates it in action through YesAnd Music as unified proof.
- `BaseCaseStudy` is a shared base component containing common structure (header, playbook section, collapsible details) and GitHub link functionality.
- `CaseStudy` extends BaseCaseStudy for all case studies: always-visible Title, Quantified Outcome, and Playbook, with Key Results in the collapsible section. Supports optional GitHub links.
- **UNIFIED COMPONENT ARCHITECTURE**: All case studies now use the single `CaseStudy` component for consistency and maintainability.

### Recent decisions
- **Unified section architecture**: Merged Operating System and Deep Dive sections into a single, cohesive section that presents methodology and immediately proves it with YesAnd Music.
- **Simplified component architecture**: Eliminated `PlaybooksSection.astro` component and unified all case studies under the single `CaseStudy.astro` component for consistency and maintainability.
- The hero snapshot sentence begins with a small inline label: `Case studies:`. It remains in the same paragraph as the three links to preserve the fold.
- **Updated Hero CTA** from "View My Playbooks" to "Explore the Proof" to better reflect the new narrative flow.
- **Enhanced narrative flow**: Operating System section now seamlessly flows from methodology explanation to concrete proof through YesAnd Music, creating a unified user experience.
- **Evolved CaseStudy component to "Interactive Proof"**: Replaced `oneLiner` with `quantifiedOutcome` prop for immediate impact. Collapsed view now shows Title + Quantified Outcome + Playbook. Expanded view contains Situation + Intervention + Key Results for complete narrative proof.
- **Implemented shared base component architecture**: Created `BaseCaseStudy.astro` to eliminate code duplication. All case studies now use the unified `CaseStudy.astro` component with optional GitHub links and consistent styling.

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

### Component data shapes (for quick reference)

**BaseCaseStudy props:**
- `title: string`, `situation: string`, `intervention: string[]`, `playbook: string[]`
- `role?: string`, `timeframe?: string`, `domain?: string`, `githubUrl?: string`

**CaseStudy props (extends BaseCaseStudy):**
- `quantifiedOutcome: string`, `keyResults: string[]` (Key Results in collapsible section)
- All case studies now use the unified `CaseStudy` component

### Known considerations
- Keep JS minimal. `CaseStudy` uses native details/summary and no client JS.
- Maintain semantic HTML and accessible focus/ring states.
- Alignment system: single axis for body copy (left-aligned). Exceptions: hero headline can be centered; Operating System heading is centered on small screens only and left-aligned from `md` up. All multi-line text remains left-aligned at all sizes.

### Fold acceptance criteria
- Targets: 1280×800 and 1440×900
- Without scrolling: name, thesis, CTA + Email/LinkedIn, and the one‑sentence results snapshot are visible.
- Proof section should be visible to demonstrate business results immediately.

If you need more detail or open questions, see ROADMAP.md and CASE_STUDIES_TODO.md.


