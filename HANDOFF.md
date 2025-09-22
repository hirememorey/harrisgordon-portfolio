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
- Section order is Hero (Thesis) → Proof (Case Studies) → Operating System (AI-Native Development Methodology & Proof).
- Layout updated with title, meta description, viewport, Inter font, and base body classes.
- Reading measure applied to main container; global vertical rhythm utility (`section-y`) and base prose leading in place.
- `Hero` includes updated copy with new positioning and track record with links to each case study; CTA "Explore the Proof" jumps to `#proof`.
- `Proof` section leads with three case studies: The Crisis Manager, The Turnaround Operator, and The Venture Builder.
- `Operating System` section showcases AI-native development methodology with core pillars AND demonstrates it through YesAnd Music as proof.
- `CaseStudy` component uses enhanced Interactive Proof model: always-visible Title, Playbook, and Quantified Outcome; collapsible Situation, Intervention, and Key Results.
- **ENHANCED CONTENT HIERARCHY**: Playbook is now first (always visible), followed by Quantified Outcome, maintaining scannable-first user experience.
- **UNIFIED COMPONENT ARCHITECTURE**: All case studies use the single `CaseStudy` component for consistency and maintainability.

### Recent decisions
- **Content Strategy Update**: Implemented new copy with enhanced positioning while preserving the Interactive Proof model for optimal user experience.
- **Enhanced Content Hierarchy**: Restructured CaseStudy component to show Playbook first, then Quantified Outcome, maintaining scannable-first approach.
- **Updated Hero Positioning**: New headline emphasizes "founder-level operator" with clear value proposition and updated track record.
- **Case Study Restructuring**: All three case studies updated with new content structure: The Crisis Manager, The Turnaround Operator, and The Venture Builder.
- **Operating System Split**: Separated methodology explanation from YesAnd Music proof point for clearer narrative flow.
- **Preserved Interactive Proof Model**: Maintained the sophisticated "scannable first, details on demand" user experience that makes the site effective for busy executives.
- **Content Compression Strategy**: Extracted key phrases for always-visible sections while preserving full detail in collapsible sections.

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

**CaseStudy props:**
- `title: string` - Case study title
- `playbook: string[]` - Always visible, first section (repeatable methodology)
- `quantifiedOutcome: string` - Always visible, second section (measurable result)
- `situation: string` - Collapsible (context and challenge)
- `intervention: string[]` - Collapsible (detailed steps taken)
- `keyResults: string[]` - Collapsible (specific outcomes achieved)
- `role?: string`, `timeframe?: string`, `domain?: string` - Optional metadata badges
- `githubUrl?: string` - Optional GitHub link

**Content Hierarchy:**
- Always Visible: Title → Playbook → Quantified Outcome
- Collapsible: Situation → Intervention → Key Results

### Known considerations
- Keep JS minimal. `CaseStudy` uses native details/summary and no client JS.
- Maintain semantic HTML and accessible focus/ring states.
- Alignment system: single axis for body copy (left-aligned). Exceptions: hero headline can be centered; Operating System heading is centered on small screens only and left-aligned from `md` up. All multi-line text remains left-aligned at all sizes.

### Fold acceptance criteria
- Targets: 1280×800 and 1440×900
- Without scrolling: name, thesis, CTA + Email/LinkedIn, and the one‑sentence results snapshot are visible.
- Proof section should be visible to demonstrate business results immediately.

If you need more detail or open questions, see ROADMAP.md and CASE_STUDIES_TODO.md.


