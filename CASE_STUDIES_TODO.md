## Case Studies — Content (Archived TODO)

Status: Complete. All case study content is populated in `src/pages/index.astro` and rendered via `src/components/CaseStudy.astro`.

This document is kept as a reference for the data shape only. Make content edits directly in `index.astro` to avoid duplication/drift.

### Data shape (Updated)
- `title: string` - Case study title
- `playbook: string[]` - Always visible, first section (repeatable methodology)
- `quantifiedOutcome: string` - Always visible, second section (measurable result)
- `situation: string` - Collapsible (context and challenge)
- `intervention: string[]` - Collapsible (detailed steps taken)
- `keyResults: string[]` - Collapsible (specific outcomes achieved)
- `role?: string`, `timeframe?: string`, `domain?: string` - Optional metadata badges
- `githubUrl?: string` - Optional GitHub link

### Where to edit
- Content: `src/pages/index.astro` (props on each `CaseStudy` instance)
- Structure & styles: `src/components/CaseStudy.astro`

### Example usage (in `index.astro`)
```astro
<CaseStudy
  title="The Crisis Manager"
  playbook={[
    'Own the failure to de-escalate.',
    'Build a data mirror to replace opinions with facts.',
    'Partner with the customer to build the fix.'
  ]}
  quantifiedOutcome="Saved a $900k ARR account from churning"
  situation="Our largest account was about to churn. A clinical AI was generating false patient data, and our broken release process had destroyed all trust."
  intervention={[
    'Triage: I took immediate ownership on customer calls...',
    'The Mirror: I built a V1 Health Dashboard...',
    'The New Treaty: Armed with data, I led the negotiation...'
  ]}
  keyResults={[
    'Saved a $900k ARR account from churning.',
    'Created a new Enterprise Release Protocol...',
    'Turned a churn risk into our most important design partner...'
  ]}
/>
```


