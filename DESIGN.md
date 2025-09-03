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

#### Components (utility-first)
- Section wrapper: `w-full py-12 md:py-16 lg:py-20`
- Section header group: `space-y-2`
- Card/surface (if needed): `rounded-lg border border-neutral-200 p-6 md:p-8 bg-white/80`
- Disclosure/accordion buttons: focus-visible outlines, `data-[state=open]:...` where applicable

#### Accessibility
- Maintain sufficient color contrast (WCAG AA+).
- Use semantic HTML: `header`, `main`, `section`, `footer`.
- Ensure focus states are visible and keyboard nav works.

#### Assets
- Favicon at `/public/favicon.svg`.
- Avoid heavy images; prefer text-first content.


