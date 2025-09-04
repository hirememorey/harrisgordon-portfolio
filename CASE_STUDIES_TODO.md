## Case Studies — Content (Archived TODO)

Status: Complete. All case study content is populated in `src/pages/index.astro` and rendered via `src/components/CaseStudy.astro`.

This document is kept as a reference for the data shape only. Make content edits directly in `index.astro` to avoid duplication/drift.

### Data shape
- `title: string`
- `oneLiner: string`
- `keyResults: string[]`
- `situation: string`
- `intervention: string[]` (ordered steps)
- `playbook: string[]` (ordered, repeatable steps)

### Where to edit
- Content: `src/pages/index.astro` (props on each `CaseStudy` instance)
- Structure & styles: `src/components/CaseStudy.astro`

### Example usage (in `index.astro`)
```astro
<CaseStudy
  title="The Crisis Manager"
  oneLiner="Retaining a $900k enterprise account by transforming a P0 crisis into a new company protocol."
  keyResults={["Result A", "Result B"]}
  situation="One concise paragraph here."
  intervention={["Step 1", "Step 2", "Step 3"]}
  playbook={["Repeatable 1", "Repeatable 2", "Repeatable 3"]}
/>
```


