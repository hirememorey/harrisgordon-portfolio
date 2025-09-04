### Next Steps: Implement the Page Sections

All work happens in `src/pages/index.astro`. Keep sections semantic and minimal.

#### 1) Hero
- Purpose: Name, thesis, call-to-action.
- Structure:
  - `section#hero`
  - Heading with name and brief thesis line
  - One primary CTA (e.g., "Read the Playbooks")
- Suggested Tailwind:
  - Wrapper: `w-full py-16 md:py-20 lg:py-24`
  - Heading: `text-4xl md:text-5xl font-semibold tracking-tight`
  - Sub: `mt-4 text-xl md:text-2xl text-neutral-700`
  - CTA: `mt-8 inline-flex items-center rounded-md border border-neutral-300 px-4 py-2 hover:bg-neutral-50`

#### 2) Operating System
- Purpose: Work philosophy explained concisely.
- Structure:
  - `section#operating-system`
  - Short intro + bullets or numbered list
- Suggested Tailwind:
  - Title: `text-2xl md:text-3xl font-semibold`
  - Content: `mt-4 space-y-3 text-neutral-800`

#### 3) Proof (Case Studies)
- Purpose: Three case studies where Key Results and the Repeatable Playbook are always visible; the narrative (Situation + Intervention) is opt-in via native `<details>/<summary>`.
- Structure:
  - `section#proof`
  - For each case: a `<details>` wrapper with a styled `<summary>` acting as the toggle label
  - Panel contains Situation, Intervention (ordered), Playbook (ordered)
- Suggested Tailwind:
  - Card: `rounded-lg border border-neutral-200 bg-white/80 shadow-sm`
  - Key Results list: `leading-relaxed`
  - Playbook list: `leading-relaxed rounded-md border border-neutral-200 bg-neutral-50 p-3 md:p-4`
  - Summary (toggle): `w-full inline-flex items-center rounded-md border border-neutral-300 px-3 py-1.5 md:text-base hover:bg-neutral-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-neutral-300`; Use `group`/`group-open` to swap label text
  - Panel: `mt-6 space-y-6 text-neutral-800`

#### 4) Core Competencies & Footer
- Purpose: Enumerate strengths; close with contact.
- Structure:
  - `section#competencies`
  - Simple list of competencies in 2 columns on md+ screens
  - Footer with email and minimal links
- Suggested Tailwind:
  - Grid: `mt-6 grid grid-cols-1 md:grid-cols-2 gap-4`
  - Footer: `mt-16 border-t border-neutral-200 pt-6 text-sm text-neutral-700`

#### Content status
- Case studies populated in `src/pages/index.astro` with full `oneLiner`, `keyResults`, `situation`, `intervention`, and `playbook` content.

Example skeleton to paste into `src/pages/index.astro` (adjust copy later):

```astro
---
import Layout from "../layouts/Layout.astro";
---

<Layout>
  <section id="hero" class="w-full py-16 md:py-20 lg:py-24">
    <h1 class="text-4xl md:text-5xl font-semibold tracking-tight">Harris Gordon</h1>
    <p class="mt-4 text-xl md:text-2xl text-neutral-700">Turnaround Operator & Venture Builder. Playbooks that ship outcomes.</p>
    <a href="#proof" class="mt-8 inline-flex items-center rounded-md border border-neutral-300 px-4 py-2 hover:bg-neutral-50">Read the Playbooks</a>
  </section>

  <section id="operating-system" class="w-full py-12 md:py-16 lg:py-20">
    <h2 class="text-2xl md:text-3xl font-semibold">Operating System</h2>
    <div class="mt-4 space-y-3 text-neutral-800">
      <p>How I diagnose, prioritize, and execute in complex environments.</p>
      <ul class="list-disc pl-5 space-y-2">
        <li>Assess reality fast: data, constraints, incentives.</li>
        <li>Define the hill: single measurable target.</li>
        <li>Sequence moves: smallest steps to compounding impact.</li>
      </ul>
    </div>
  </section>

  <section id="proof" class="w-full py-12 md:py-16 lg:py-20">
    <h2 class="text-2xl md:text-3xl font-semibold">Proof</h2>
    <div class="mt-6 divide-y divide-neutral-200 rounded-lg border border-neutral-200">
      <details class="group">
        <summary class="w-full cursor-pointer list-none px-4 py-3 hover:bg-neutral-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-neutral-300">
          <span class="font-medium">Case Study A</span>
          <span class="ml-2 text-neutral-600">— outcome summary</span>
        </summary>
        <div class="px-4 pb-4 text-neutral-800">
          <p>Key problem, actions, and measurable result.</p>
        </div>
      </details>
      <details>
        <summary class="w-full cursor-pointer list-none px-4 py-3 hover:bg-neutral-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-neutral-300">Case Study B</summary>
        <div class="px-4 pb-4 text-neutral-800">Details…</div>
      </details>
      <details>
        <summary class="w-full cursor-pointer list-none px-4 py-3 hover:bg-neutral-50 focus:outline-none focus-visible:ring-2 focus-visible:ring-neutral-300">Case Study C</summary>
        <div class="px-4 pb-4 text-neutral-800">Details…</div>
      </details>
    </div>
  </section>

  <section id="competencies" class="w-full py-12 md:py-16 lg:py-20">
    <h2 class="text-2xl md:text-3xl font-semibold">Core Competencies</h2>
    <div class="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
      <ul class="space-y-2">
        <li>Operational diagnostics</li>
        <li>Go-to-market turnarounds</li>
      </ul>
      <ul class="space-y-2">
        <li>Founder coaching</li>
        <li>Systems design</li>
      </ul>
    </div>

    <footer class="mt-16 border-top border-neutral-200 pt-6 text-sm text-neutral-700">
      <p>Contact: <a href="mailto:harris@harrisgordon.com">harris@harrisgordon.com</a></p>
    </footer>
  </section>

  <!-- End sections -->
</Layout>
```

#### Fold validation checklist
- Viewports: 1280×800 and 1440×900
- Above the fold: name, thesis, primary CTA + Email/LinkedIn, one‑sentence results snapshot, and full Operating System block
- Snapshot clauses link to `#cs-crisis`, `#cs-turnaround`, `#cs-venture` and jump with headings visible (`scroll-mt-24`)

#### Review checklist
- Sections are semantic and vertically spaced consistently
- Typography scale matches `DESIGN.md`
- Minimal visual noise; generous whitespace
- Keyboard and screen-reader friendly disclosures


