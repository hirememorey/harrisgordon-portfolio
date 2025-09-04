## Harris Gordon — Portfolio (Astro + Tailwind)

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
- `src/components/CaseStudy.astro` — bifurcated case study card: Key Results + Playbook always visible; narrative via native `<details>/<summary>` (no JS); explicit disclosure labels; optional metadata badges

### What’s implemented
- Hero, Operating System, and three populated Case Studies
- Global vertical rhythm (`section-y`) and reading measure applied to improve scan/read
- CaseStudy lists normalized for scannability; explicit disclosure labels; optional Role/Timeframe/Domain badges
- Native details/summary for the narrative; Results and Playbook are always visible (no client JS)
- Single alignment axis: body copy left-aligned within the measure; hero headline may be centered; OS heading is centered only on small screens and left-aligned from `md` up.

### Next steps
- SEO/OG/Twitter meta + canonical URL in `Layout.astro`; consider `theme-color`
- Choose deployment target (Vercel/Netlify/Cloudflare) and enable preview deploys
- Optional: lightweight analytics (Plausible/Umami)

### Scripts
- `npm run dev` — start dev server
- `npm run build` — build to `dist/`
- `npm run preview` — preview production build
