## Developer Handoff

This doc brings you up to speed fast and tells you exactly what to do next.

### Project snapshot
- Stack: Astro v5 + Tailwind CSS v4 (via `@tailwindcss/vite`)
- Node: 20+, npm: 10+
- Global CSS: `src/styles/global.css`
- Layout shell: `src/layouts/Layout.astro` (imports Inter font, base meta)
- Page: `src/pages/index.astro`
- Components: `Hero.astro`, `CaseStudy.astro`, `PlaybooksSection.astro`

### Current state
- Section order is Hero (Thesis) → Proof (Business Case Studies) → Operating System (AI-Native Development Methodology) → Deep Dive (Proof of the OS).
- Layout updated with title, meta description, viewport, Inter font, and base body classes.
- Reading measure applied to main container; global vertical rhythm utility (`section-y`) and base prose leading in place.
- `Hero` includes a one‑sentence results snapshot with links to each case study; CTA "Explore the Proof" jumps to `#proof`.
- `Proof` section leads with three business case studies demonstrating Turnaround Operator & Venture Builder capabilities.
- `Operating System` section showcases AI-native development methodology with three core pillars: The External Brain, The Red Team Pre-Mortem, and The Post-Mortem Time Machine.
- `Deep Dive` section demonstrates the methodology in action through YesAnd Music as proof of the OS.
- `CaseStudy` is a bifurcated card: always-visible Title, Quantified Outcome, and Playbook, with the detailed narrative (Situation + Intervention + Key Results) behind a native `<details>/<summary>` (no JS). Disclosure copy is explicit ("Read full story/Hide full story"). Optional metadata badges render if provided.
- `PlaybooksSection` is a specialized component for technical case studies with GitHub integration, featuring the same bifurcated layout as CaseStudy but with additional technical implementation details.

### Recent decisions
- **Re-architected information hierarchy** to follow thesis-driven narrative flow: Hero (Thesis) → Proof (Business Case Studies) → Operating System (AI-Native Development Methodology) → Deep Dive (Proof of the OS).
- The hero snapshot sentence begins with a small inline label: `Case studies:`. It remains in the same paragraph as the three links to preserve the fold.
- **Updated Hero CTA** from "View My Playbooks" to "Explore the Proof" to better reflect the new narrative flow.
- **Repositioned Operating System section** to focus on AI-native development methodology with three core pillars: The External Brain, The Red Team Pre-Mortem, and The Post-Mortem Time Machine.
- **Repositioned Deep Dive section** to frame YesAnd Music as proof of the AI-native operating system in action.
- **Enhanced section descriptions** to better connect the narrative and show how each section builds on the previous one.
- Visible copy avoids em/en dashes and heavy punctuation. Prefer short sentences and simple phrasing. The meta description also avoids em dashes.
- Resolved "Playbook" terminology ambiguity by renaming technical section to "Deep Dive: Technical Architecture" to distinguish from business case study playbooks.
- **Evolved CaseStudy component to "Interactive Proof"**: Replaced `oneLiner` with `quantifiedOutcome` prop for immediate impact. Collapsed view now shows Title + Quantified Outcome + Playbook. Expanded view contains Situation + Intervention + Key Results for complete narrative proof.

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
- Props: `title: string`, `quantifiedOutcome: string`, `keyResults: string[]`, `situation: string`, `intervention: string[]`, `playbook: string[]`

### Known considerations
- Keep JS minimal. `CaseStudy` uses native details/summary and no client JS.
- Maintain semantic HTML and accessible focus/ring states.
- Alignment system: single axis for body copy (left-aligned). Exceptions: hero headline can be centered; Operating System heading is centered on small screens only and left-aligned from `md` up. All multi-line text remains left-aligned at all sizes.

### Fold acceptance criteria
- Targets: 1280×800 and 1440×900
- Without scrolling: name, thesis, CTA + Email/LinkedIn, and the one‑sentence results snapshot are visible.
- Proof section should be visible to demonstrate business results immediately.

If you need more detail or open questions, see ROADMAP.md and CASE_STUDIES_TODO.md.


