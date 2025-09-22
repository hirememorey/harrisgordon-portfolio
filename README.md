## Harris Gordon | Portfolio (Astro + Tailwind)

Minimal, fast, and accessible portfolio site built with Astro v5 and Tailwind CSS v4.

### Getting started

```bash
npm install
npm run dev
```

Local dev runs at `http://localhost:4321`.

### Key files
- `src/layouts/Layout.astro` — layout shell, meta, Inter font, applies reading measure
- `src/styles/global.css` — Tailwind v4 entry and small utilities (`section-y` rhythm, `measure` ~72ch)
- `src/pages/index.astro` — single-page composition
- `src/components/CaseStudy.astro` — enhanced Interactive Proof case study card: Playbook + Quantified Outcome always visible; narrative via native `<details>/<summary>` (no JS); explicit disclosure labels; optional metadata badges
- `src/components/BaseCaseStudy.astro` — shared base component with common structure and GitHub link functionality

### What's implemented
- Section order: Hero (Thesis) → Proof (Case Studies) → Operating System (AI-Native Development Methodology & Proof)
- Hero includes updated positioning and track record with links to each case study
- Primary CTA "Explore the Proof" jumps to `#proof`; Email/LinkedIn shown inline
- Proof section leads with three case studies: The Crisis Manager, The Turnaround Operator, and The Venture Builder
- Operating System section showcases AI-native development methodology with core pillars AND demonstrates it through YesAnd Music as proof
- Global vertical rhythm (`section-y`) and reading measure applied to improve scan/read
- Enhanced Interactive Proof model: Title, Playbook, and Quantified Outcome always visible; Situation, Intervention, and Key Results collapsible
- Native details/summary for the narrative; explicit disclosure labels; optional Role/Timeframe/Domain badges
- Single alignment axis: body copy left-aligned within the measure; hero headline may be centered; OS heading is centered only on small screens and left-aligned from `md` up.

### Next steps
- SEO/OG/Twitter meta + canonical URL in `Layout.astro`; consider `theme-color`
- Choose deployment target (Vercel/Netlify/Cloudflare) and enable preview deploys
- Optional: lightweight analytics (Plausible/Umami)

### First‑view (fold) acceptance criteria
- Viewport targets: 1280×800 and 1440×900
- Without scrolling you should see: name, thesis, CTA + Email/LinkedIn, and the one‑sentence results snapshot
- Snapshot clauses link to specific case studies (`#cs-crisis`, `#cs-turnaround`, `#cs-venture`)
- Proof section should be visible to demonstrate business results immediately

### Scripts
- `npm run dev` — start dev server
- `npm run build` — build to `dist/`
- `npm run preview` — preview production build
