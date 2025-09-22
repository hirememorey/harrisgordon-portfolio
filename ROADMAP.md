## Roadmap (Prioritized)

### P0 — Content & polish
- [x] Populate all `CaseStudy` props in `index.astro` (Situation, Intervention, Playbook, Key Results)
- [x] Refactor `CaseStudy` to bifurcated layout (Results + Playbook visible; narrative behind toggle)
- [x] Establish global rhythm/utilities: `section-y` and `measure` (~72ch)
- [x] Apply rhythm to `Hero`, `OperatingSystem`, and `#proof` sections (Hero/OS may be one step denser)
- [x] Normalize CaseStudy lists: `space-y-2` + `leading-relaxed`
- [x] Make disclosure labels explicit/stateful (“Read full story”/“Hide full story”)
- [x] Optional metadata badges (Role/Timeframe/Domain) rendered only if provided
- [x] Reorder sections to Hero (Thesis) → Proof (Business Case Studies) → Operating System (AI-Native Development Methodology & Proof)
- [x] Add snapshot in Hero with links to case studies
- [x] Merge Operating System and Deep Dive sections into unified narrative flow
- [x] Eliminate PlaybooksSection component and unify all case studies under CaseStudy component
- [x] Update technical case study content with personal narrative approach
- [x] Position YesAnd Music as proof point for operating system methodology
- [x] Update Hero CTA to "Explore the Proof" reflecting new narrative flow
- [x] Enhance section descriptions to better connect the narrative flow
- [x] Evolve CaseStudy component to "Interactive Proof" with quantifiedOutcome prop
- [x] Restructure collapsed view to show Title + Quantified Outcome + Playbook
- [x] Restructure expanded view to show Situation + Intervention + Key Results
- [x] Update case study content with new narrative structure
- [x] Reposition Operating System section to focus on AI-native development methodology
- [x] Implement shared base component architecture with BaseCaseStudy.astro
- [x] Add GitHub link functionality to CaseStudy component
- [x] Eliminate code duplication with unified component architecture

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
- CaseStudy "Interactive Proof": Quantified Outcome displayed prominently in collapsed view; Key Results moved to expanded view; enhanced visual hierarchy for better user flow.
- GitHub links: Consistent styling with external link icon, hover states, and proper accessibility attributes across both component types.


