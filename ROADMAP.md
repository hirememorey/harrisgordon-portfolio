## Roadmap (Prioritized)

### P0 — Content & polish
- [x] Populate all `CaseStudy` props in `index.astro` (Situation, Intervention, Playbook, Key Results)
- [x] Refactor `CaseStudy` to bifurcated layout (Results + Playbook visible; narrative behind toggle)
- [x] Establish global rhythm/utilities: `section-y` and `measure` (~72ch)
- [x] Apply rhythm to `Hero`, `OperatingSystem`, and `#proof` sections
- [x] Normalize CaseStudy lists: `space-y-2` + `leading-relaxed`
- [x] Make disclosure labels explicit/stateful (“Read full story”/“Hide full story”)
- [x] Optional metadata badges (Role/Timeframe/Domain) rendered only if provided

### P1 — SEO & metadata
- [ ] Add Open Graph/Twitter meta in `Layout.astro` (title, description, type, image)
- [ ] Add canonical URL and `theme-color`
- [ ] Consider structured data for Person/Organization (optional)

### P2 — Deployment & analytics
- [ ] Choose host (Vercel/Netlify/Cloudflare). Add project and connect repo
- [ ] Add preview deploys on PRs
- [ ] Optional: lightweight analytics (Plausible/Umami)

### P3 — Content evolution
- [ ] Replace placeholders with final copy
- [ ] Consider Astro Content Collections for case studies if they grow
- [ ] Add footer section (simple, low-chrome). If 3 columns:
  - Wrapper: `grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8`

### Style changes implemented
- Operating System section: added `scroll-mt-24`; increased vertical padding
- Proof section heading: `text-3xl md:text-4xl font-semibold leading-tight`
- CaseStudy card: `shadow-sm`; lists `leading-relaxed` with consistent spacing; explicit disclosure labels; Playbook emphasized; optional badges
- Alignment normalized: left-aligned body across sections; OS heading centered only on small screens; headings and body left-aligned from `md+`.


