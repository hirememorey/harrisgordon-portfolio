### Development

This project is an Astro v5 + Tailwind CSS v4 site for Harris Gordon's portfolio.

#### Prerequisites
- Node.js 20+ (LTS recommended)
- npm 10+

#### Install
```bash
npm install
```

#### Run locally
```bash
npm run dev
```
Then open the local URL printed by Astro.

#### Build and preview
```bash
npm run build
npm run preview
```

#### Project structure (key files)
- `astro.config.mjs`: Astro config. Tailwind v4 is integrated via `@tailwindcss/vite`.
- `src/styles/global.css`: Imports Tailwind and defines minimal base styles and small utilities (`section-y`, `measure`).
- `src/layouts/Layout.astro`: Imports the global stylesheet and provides a clean, centered content shell with a reading measure.
- `src/pages/index.astro`: The single page. Section order is Hero → Operating System → Proof.

#### Styling
- Tailwind v4 style entry: `@import "tailwindcss";` in `src/styles/global.css`.
- No `tailwind.config.js` is needed for the base; use defaults unless customization is required.

#### Commands
- `npm run dev`: Start dev server
- `npm run build`: Production build to `dist/`
- `npm run preview`: Serve the built site locally

#### Telemetry
Astro collects anonymous telemetry. To opt out:
```bash
npx astro telemetry disable
```

#### Troubleshooting
- npm EACCES errors on macOS (cache permissions):
  - Quick fix (per-command cache):
    ```bash
    npm_config_cache="$HOME/.cache/npm-tmp" npm install
    npm_config_cache="$HOME/.cache/npm-tmp" npx astro add tailwind --yes
    ```
  - Permanent fix:
    ```bash
    sudo chown -R $(id -u):$(id -g) "$HOME/.npm"
    ```
- "Cannot find module 'astro/config'":
  - Ensure dependencies are installed: `npm install`
  - Then rerun the requested command.

#### What to edit next
Work in `src/pages/index.astro`. The base layout and global styles are ready; use the global `section-y` rhythm and reading `measure`. Case studies use a bifurcated layout: always-visible Results + Playbook with the narrative (Situation + Intervention) behind a native `<details>/<summary>`—with explicit “Read full story/Hide full story” labels. Optional metadata badges render if provided.

Hero guidance:
- One-sentence thesis in first person.
- One-sentence results snapshot with 2–3 clauses. Each clause links to a case study anchor (`#cs-crisis`, `#cs-turnaround`, `#cs-venture`).
- CTA `View My Playbooks` links to `#proof`; Email and LinkedIn inline.

Fold validation:
- Targets: 1280×800 and 1440×900.
- Without scrolling: name, thesis, CTA + Email/LinkedIn, snapshot, and full Operating System block are visible.


