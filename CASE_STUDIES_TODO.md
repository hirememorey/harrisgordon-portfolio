## Case Studies — Content TODO

Populate the following props for each `CaseStudy` instance in `src/pages/index.astro`.

### Data shape
- `title: string`
- `oneLiner: string`
- `keyResults: string[]`
- `situation: string`
- `intervention: string[]` (ordered steps)
- `playbook: string[]` (ordered, repeatable steps)

### Case Study 1 — The Crisis Manager
- keyResults:
  - Retained a $900k ARR strategic account that was on the brink of churning.
  - Created the V1 of a new Enterprise Release Protocol, a playbook now used to de-risk other high-stakes accounts.
  - Transformed the account from a churn risk into our most important design partner for stability.
- situation: <add a concise paragraph>
- intervention:
  - <step 1>
  - <step 2>
  - <step 3>
- playbook:
  - <repeatable step 1>
  - <repeatable step 2>
  - <repeatable step 3>

### Case Study 2 — The Turnaround Operator
- keyResults:
  - <add 2–4 measurable results>
- situation: <add a concise paragraph>
- intervention:
  - <step 1>
  - <step 2>
  - <step 3>
- playbook:
  - <repeatable step 1>
  - <repeatable step 2>
  - <repeatable step 3>

### Case Study 3 — The Venture Builder
- keyResults:
  - <add 2–4 measurable results>
- situation: <add a concise paragraph>
- intervention:
  - <step 1>
  - <step 2>
  - <step 3>
- playbook:
  - <repeatable step 1>
  - <repeatable step 2>
  - <repeatable step 3>

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


