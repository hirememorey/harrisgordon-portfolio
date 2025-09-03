## Roadmap (Prioritized)

### P0 — Content & polish
- [ ] Populate all `CaseStudy` props in `index.astro` (Situation, Intervention, Playbook, Key Results)
- [ ] Refine spacing rhythm across sections: use `py-16 md:py-20 lg:py-24` consistently
- [ ] Typography hierarchy pass per file:
  - Hero: `h1 leading-tight`, `h2 text-2xl md:text-3xl`, paragraph `text-lg md:text-xl`
  - Operating System: `h2 text-3xl md:text-4xl`, paragraph `text-lg md:text-xl`
  - CaseStudy: titles `text-xl md:text-2xl`, lists `leading-relaxed`
- [ ] Improve button sizing responsiveness (Hero CTA, CaseStudy toggle)

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

### Style changes to implement (diff summary)
- Operating System section: add `scroll-mt-24`; increase vertical padding
- Proof section heading: `text-3xl md:text-4xl font-semibold leading-tight`
- CaseStudy card: add `shadow-sm`; lists `leading-relaxed`; responsive button sizing


