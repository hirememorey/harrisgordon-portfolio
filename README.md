## Harris Gordon — Portfolio (Astro + Tailwind)

Minimal, fast, and accessible portfolio site built with Astro v5 and Tailwind CSS v4.

### Getting started

```bash
npm install
npm run dev
```

Local dev runs at `http://localhost:4321`.

### Key files
- `src/layouts/Layout.astro` — layout shell, meta, Inter font
- `src/styles/global.css` — Tailwind v4 entry and small utilities
- `src/pages/index.astro` — single-page composition
- `src/components/CaseStudy.astro` — disclosure component using native `<details>/<summary>`

### What’s implemented
- Hero, Operating System, and three populated Case Studies
- Native disclosure for playbooks (no client JS)

### Next steps
- Typography/spacing polish (see `ROADMAP.md`)
- SEO/OG/Twitter meta + canonical URL in `Layout.astro`
- Choose deployment target (Vercel/Netlify/Cloudflare) and enable preview deploys

### Scripts
- `npm run dev` — start dev server
- `npm run build` — build to `dist/`
- `npm run preview` — preview production build
