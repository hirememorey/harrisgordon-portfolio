### Design Guidelines

#### Philosophy
- Less is more. Prioritize clarity, whitespace, and hierarchy.
- Use a light background, dark neutral text, and minimal accent.
- Typography carries the brand. Keep it crisp and readable.

#### Color
- Background: `#ffffff`
- Text: neutral-900 (Tailwind)
- Muted text: neutral-600/700
- Borders/accents: neutral-200/300

If an accent is needed later, choose one muted color and use very sparingly.

#### Typography
- Set by Tailwind defaults; we keep it simple.
- Section titles: `text-3xl md:text-4xl font-semibold tracking-tight`
- Subheads: `text-xl md:text-2xl font-medium`
- Body: `text-base md:text-lg leading-relaxed`
- Links: underlined, neutral-900, subtle hover decoration

#### Spacing & Layout
- Global container: `max-w-5xl mx-auto container-px`
- Vertical rhythm: `py-12 md:py-16 lg:py-20` per major section
- Intra-section spacing: `space-y-4 md:space-y-6`
- Hero and Operating System may be one step denser to satisfy fold acceptance (see below)

#### Components (utility-first)
- Section wrapper: `w-full py-16 md:py-20 lg:py-24`
- Section header group: `space-y-2`
- Card/surface (if needed): `rounded-lg border border-neutral-200 p-6 md:p-8 bg-white/80 shadow-sm`
- Disclosure/accordion buttons: focus-visible outlines; use native `<details>/<summary>` with `group-open` for toggled text

#### Alignment
- Default: left-align all multi-line content within the reading measure.
- Exceptions: the hero headline may be centered; the Operating System section heading may be centered on small screens only. From `md` and up, headings and all body/list content are left-aligned.
- Prefer typographic scale, spacing, and subtle surfaces to convey emphasis rather than introducing multiple alignment systems.

#### Above‑the‑fold acceptance
- Targets: 1280×800 and 1440×900
- Without scrolling, show: name, thesis, primary CTA + Email/LinkedIn, a one‑sentence results snapshot, and the full Operating System block.
- Snapshot clauses are links to specific case studies.

#### Accessibility
- Maintain sufficient color contrast (WCAG AA+).
- Use semantic HTML: `header`, `main`, `section`, `footer`.
- Ensure focus states are visible and keyboard nav works.

#### Assets
- Favicon at `/public/favicon.svg`.
- Avoid heavy images; prefer text-first content.



#### Snapshot label
- In the hero snapshot sentence, prepend a short inline label: `Case studies:`.
- Keep it in the same paragraph as the three links. Do not introduce a new line or badge.
- Style: body size, neutral-700, small right margin.

#### Hero ↔ Operating System spacing
- Hero section uses slightly reduced bottom padding; Operating System uses slightly reduced top padding to tighten the gap while preserving the fold on 1280×800 and 1440×900.
- Verify the fold after any copy changes; prefer adjusting only these paddings rather than global rhythm.

#### Copy & punctuation
- Avoid em/en dashes in visible site copy. Prefer short, clear sentences and minimal commas.
- Examples:
  - Use `0-1`, not `0–1`.
  - Use `go to market`, not `Go-to-Market`.
  - Replace long em-dash clauses with short sentences or simple prepositions.
