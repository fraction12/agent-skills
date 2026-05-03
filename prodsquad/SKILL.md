---
name: prodsquad
description: Run a grilled product squad process for feature ideas, bugs, UX improvements, experiments, or vague product requests. Use when the user wants to turn an idea or bug into a deeply understood, researched, UX-shaped, engineering-informed spec using the workspace's native spec system, especially OpenSpec when present.
---

# ProdSquad

ProdSquad turns feature ideas and bugs into build-ready specs by grilling the user through product discovery, research, UX shaping, engineering fit, and native spec artifact creation.

It is not “write a spec immediately.” It is the product-thinking layer before and around the spec: relentless clarification first, then researched decisions, then native artifacts.

```text
classify → uncover intent → research options → choose direction
→ shape product → draft spec → design UX → research engineering fit
→ final native spec
```

## Core Rules

1. **Grill before specifying.** Interview the user relentlessly about what they actually want before accepting the proposed solution.
2. **Ask one question at a time.** Do not dump a questionnaire. Walk the decision tree branch by branch and wait for feedback before continuing.
3. **Provide a recommended answer with every question.** Make it easy for the user to say “yes,” correct you, or expose a hidden assumption.
4. **If repo/docs/web can answer it, inspect first.** Do not ask the user to explain facts already available in the codebase, docs, product pages, API docs, or web.
5. **Do not jump straight to implementation.** Discovery and decision clarity come first.
6. **Do not produce the final spec until product, UX, and engineering fit have all been considered and grilled.**
7. **Use the workspace's native spec system.** Detect OpenSpec or other conventions before inventing a format.
8. **Research before recommending.** Use web search, web fetch, browser, docs, and codebase research whenever available and relevant. For current products, competitors, APIs, libraries, pricing, policies, standards, laws, market facts, UX patterns, or implementation approaches, live research is mandatory unless the user explicitly says not to browse.
9. **Keep the user in the loop at phase gates.** Present options and tradeoffs, grill the unresolved decisions, then let the user choose direction before locking the spec.
10. **Make the final output buildable and explainable.** A competent coding agent should be able to implement without guessing, and the human should understand why each decision was made.

## When to Use

Use this skill when the user says or implies:

- “I have a feature idea…”
- “Can we build X?”
- “Users should be able to…”
- “This bug needs a proper spec.”
- “Turn this into an OpenSpec change/spec.”
- “Research this feature before we build it.”
- “What should the UX be?”
- “I need a PRD/spec/product process for this.”

Do **not** use for trivial one-line fixes unless the user asks for product/spec work.



## Grilled Discovery Discipline

ProdSquad uses the Grill Me pattern as its operating style, not as an optional mode. The first serious phase is an intent grill, and every later checkpoint grills the decisions that remain unresolved.

### How to grill

- Interview the user relentlessly until there is shared understanding.
- Ask one question at a time.
- Walk down each branch of the product/design/engineering decision tree, resolving dependencies between decisions one by one.
- For every question, provide your recommended answer.
- Wait for the user's feedback before moving to the next question when the answer requires human judgment.
- If a question can be answered by exploring the codebase, docs, existing specs, or web, do that instead of asking.
- If the user's answer creates a new ambiguity, follow that branch before continuing.
- Keep the conversation moving: ask sharp questions, not bureaucratic forms.

### Where grilling happens

- **Intent discovery:** heavy grilling. Find the real user, job, pain, desired outcome, assumptions, constraints, and success definition.
- **Research/options:** grill why an option is attractive, what tradeoff is acceptable, and what pattern should be copied or avoided.
- **Product shaping:** grill MVP boundaries, non-goals, roles, permissions, edge cases, and rollout.
- **UX/design:** grill states, flows, labels, failure modes, accessibility, and what the user must understand at each step.
- **Engineering fit:** grill implementation assumptions, data/API shape, migrations, dependencies, risks, and tests.
- **Spec review:** grill whether each requirement is testable and whether every major decision has rationale.

### What the grilling should produce

By the time the final spec is written, the conversation and artifact should preserve:

- the real problem behind the request
- decisions made
- rationale for each major decision
- rejected alternatives
- tradeoffs accepted
- unresolved questions
- repo/docs/web facts discovered instead of asking the user

## Web and Research Tool Policy

ProdSquad should be web-capable by default. Product and engineering decisions go stale quickly; do not rely on model memory when live research could materially improve the answer.

Use available web capabilities whenever possible and relevant:

- **Web search** for discovery, competitors, current products, examples, market/user language, libraries, APIs, standards, changelogs, issues, pricing, policies, and recent implementation patterns.
- **Web fetch/extract** for primary sources found via search: official docs, product pages, help centers, API references, changelogs, standards, research papers, and reputable engineering/design writing.
- **Browser tools** when pages are interactive, screenshots/visual inspection matter, docs require navigation, or UX/product patterns need direct inspection.
- **Repo/codebase tools** for local truth: architecture, conventions, tests, existing abstractions, and native spec systems.

### Mandatory live research triggers

Use web search/fetch unless the user explicitly says not to browse when the task involves:

- competitor or adjacent-product patterns
- market/category/user research
- current API/library/framework behavior
- legal/policy/compliance/pricing constraints
- security, privacy, accessibility, or performance best practices
- UX examples from existing products
- implementation approaches that depend on versions or recent ecosystem changes
- claims about what a product currently supports

### Source quality

Prefer primary sources first:

1. official docs/product/help/API/changelog pages
2. standards/specifications or research papers
3. reputable engineering/design writing
4. user reviews/forums/social posts only for sentiment and pain points

When using web research, cite sources in research outputs. Do not dump raw links; synthesize what the sources imply for the product decision.

### If tools are unavailable

If web tools are unavailable, say so clearly and mark findings as assumptions or memory-based. Do not present stale memory as verified current fact.

## Slash Commands / Invocation Phrases

These commands are optional runner conventions. If the agent environment supports slash commands, use them directly. If it does not, treat them as natural-language task modes.

| Command | Purpose | Loads |
|---|---|---|
| `/prodsquad:intake <idea-or-bug>` | Classify the request and run the heavy intent grill before research/spec work. | `feature-process.md` or `bug-process.md` |
| `/prodsquad:research` | Research comparable products, UX patterns, docs, APIs, and market/user expectations. | `research-options.md` |
| `/prodsquad:options` | Synthesize 3–4 product approaches from current context and recommend one. | `research-options.md` |
| `/prodsquad:shape` | Turn the chosen option into product scope, non-goals, flows, edge cases, and metrics. | `feature-process.md` |
| `/prodsquad:ux` | Run the UX/design pass: journey, screens, states, interaction model, copy, prototype needs. | `ux-design-pass.md` |
| `/prodsquad:engineering` | Inspect the codebase and external technical docs to produce implementation fit guidance. | `engineering-fit.md` |
| `/prodsquad:spec` | Write or update the final native spec artifacts. | `spec-system-detection.md`, then `openspec-output.md` or `final-spec-template.md` |
| `/prodsquad:review <spec-or-change>` | Audit an existing spec/change for product, UX, engineering, acceptance, and task gaps. | `review-checklist.md`, plus relevant references as needed |

### Command Behavior

- `/prodsquad:intake` should not write final artifacts. It runs the heavy first grill and produces an Intent Brief or Bug Intent Brief.
- `/prodsquad:research` should use live research when current external facts matter and should cite sources.
- `/prodsquad:options` should produce choices, tradeoffs, and a recommendation, then ask the user to choose.
- `/prodsquad:shape` should assume direction is chosen; if not, ask for the missing decision.
- `/prodsquad:ux` should be skipped or kept lightweight for non-user-facing backend changes.
- `/prodsquad:engineering` should inspect the actual repo before making implementation claims.
- `/prodsquad:spec` should detect the native spec system before writing files.
- `/prodsquad:review` should be critical and gap-focused, not polite rubber-stamping.

### Command Aliases

Accept these natural-language equivalents:

- “run ProdSquad intake” → `/prodsquad:intake`
- “research this feature” → `/prodsquad:research`
- “give me options” → `/prodsquad:options`
- “shape this” → `/prodsquad:shape`
- “do the UX pass” → `/prodsquad:ux`
- “do engineering research” → `/prodsquad:engineering`
- “write the spec” → `/prodsquad:spec`
- “review this spec” → `/prodsquad:review`

## Reference Map

Load only what is needed. All references inherit the grilled discovery discipline from this file: ask one question at a time, provide a recommended answer, and inspect repo/docs/web before asking factual questions.

- Feature ideas: `references/feature-process.md`
- Bugs: `references/bug-process.md`
- Product/user/competitor research: `references/research-options.md`
- UX and design shaping: `references/ux-design-pass.md`
- Engineering/codebase fit: `references/engineering-fit.md`
- Detecting repo spec systems: `references/spec-system-detection.md`
- Writing OpenSpec artifacts: `references/openspec-output.md`
- Fallback/final markdown spec template: `references/final-spec-template.md`
- Reviewing an existing spec/change: `references/review-checklist.md`

## Workflow

### Phase 0 — Classify

Classify the request:

1. feature idea
2. bug
3. UX improvement
4. experiment
5. refactor with product impact
6. vague product thought

If unclear, ask one concise classification question.

Then load the appropriate reference:

- feature / UX / experiment / vague thought → `feature-process.md`
- bug → `bug-process.md`

### Phase 1 — Heavy Intent Grill

Find the underlying user job before accepting the requested solution. This is the most intense grilling phase. Interview the user one question at a time until the real user, pain, workflow, desired outcome, constraints, assumptions, and success definition are understood. Provide a recommended answer with each question. Inspect repo/docs/web instead of asking factual questions.

Output an **Intent Brief** or **Bug Intent Brief** that includes decisions, rationale, assumptions, and open questions. If enough context exists, proceed with assumptions and mark them.

### Phase 2 — Research Options

Use `research-options.md` when the product pattern, market, UX convention, competitor behavior, API, library, or technical facts may matter.

Output 3–4 approaches with tradeoffs and a recommendation. Grill the choice: ask why the recommended option is acceptable, what tradeoff is unacceptable, and what should be rejected. Ask the user to choose, combine, or reject options before locking direction.

### Phase 3 — Shape Product Direction

Once direction is chosen, clarify:

- MVP scope
- non-goals
- primary flow
- secondary flows
- permissions/roles
- data involved
- edge cases
- success metrics
- rollout notes

Before outputting the **Product Shape**, grill unresolved decisions one at a time. The Product Shape should include decision rationale and rejected alternatives where relevant.

### Phase 4 — Draft Product Spec

Create a first product spec draft before deep engineering work.

This draft should be product-complete but not implementation-final. Mark implementation assumptions as pending engineering research, and include a Decision Log / Rationale section for major choices already grilled.

### Phase 5 — UX / Design Pass

For user-facing work, load `ux-design-pass.md`.

Work through journey, screens, states, interaction model, copy, accessibility, and whether a wireframe/prototype is needed. Grill each meaningful UX decision before locking it. Update the spec with the selected UX direction and rationale.

### Phase 6 — Engineering Fit

Load `engineering-fit.md`.

Inspect the local codebase and relevant external docs. Determine architecture, data/API impact, abstractions, tests, risks, and rejected approaches. Grill implementation assumptions that require human judgment; inspect code/docs for factual answers.

Update the spec to be implementation-informed, including rejected approaches and engineering rationale.

### Phase 7 — Native Spec Artifact

Before writing files, load `spec-system-detection.md` and detect the workspace convention.

- If OpenSpec exists, use `openspec-output.md`.
- If another spec/RFC/PRD convention exists, follow it.
- If no convention exists, use `final-spec-template.md` and ask before writing new files unless the user clearly requested file output.


## Example Invocations

Use these examples as portable invocation patterns:

```text
/prodsquad:intake Users need saved filters on the analytics dashboard
```
Classify the feature, uncover the real user job, and produce an Intent Brief before researching solutions.

```text
/prodsquad:research We want to add team inbox assignment rules
```
Research comparable products and UX patterns, then return 3–4 implementation/product approaches with tradeoffs.

```text
/prodsquad:spec Create an OpenSpec change for the selected saved-filters approach
```
Detect the workspace spec system, then write/update the native spec artifacts.

```text
/prodsquad:review openspec/changes/add-saved-filters
```
Audit the existing change for product, UX, engineering, acceptance, and task gaps before implementation.

## Phase Gates

Do not skip gates unless the user explicitly asks for a lightweight pass.

1. **Intent grilled** — user/job, pain, desired outcome, assumptions, constraints, success definition, and rationale.
2. **Options researched and grilled** — 3–4 plausible approaches, tradeoffs, recommendation, chosen direction, and rejected alternatives.
3. **Product shape grilled** — scope, non-goals, flow, edge cases, success criteria, and why those boundaries were chosen.
4. **UX direction grilled** — journey, states, interaction model, copy/accessibility implications, and rationale for user-facing work.
5. **Engineering fit grilled** — codebase fit, implementation approach, tests, risks, rejected approaches, and open decisions.
6. **Spec completed** — native artifacts are clear, testable, build-ready, and include enough decision rationale that the human and agent share context.

## Conversation Style

- Stay collaborative and decisive.
- Ask one sharp question at a time when a decision needs human judgment.
- Provide your recommended answer with each question.
- If not blocked, inspect repo/docs/web, proceed, and state assumptions.
- Present options as decisions, not as raw research dumps.
- Keep the user involved at direction-selection moments.
- Do not bury the recommendation.

## Output Modes

### Conversational mode
Use during discovery. Keep replies concise and question-driven.

### Research mode
Use when exploring options. Cite sources when web research is used. Summarize into choices.

### Spec-writing mode
Use when direction is selected. Create/update native spec artifacts.

### Review mode
Use when a spec already exists. Audit for missing goals, non-goals, UX states, edge cases, requirements, acceptance criteria, implementation notes, and tests.

## Completion Checklist

Before calling the work done:

- [ ] Workspace/spec system detected
- [ ] Intent grill completed
- [ ] Research performed or explicitly deemed unnecessary
- [ ] Options presented, grilled, and direction selected
- [ ] Product scope/non-goals grilled and clarified
- [ ] UX/design pass completed and grilled when user-facing
- [ ] Engineering/codebase research completed and assumptions grilled
- [ ] Native spec artifacts created/updated
- [ ] Requirements are testable
- [ ] Tasks are actionable
- [ ] Validation command identified or run
- [ ] Decision rationale and rejected alternatives are captured
- [ ] Open questions are explicit

## Short Form

If asked what ProdSquad does, say:

> ProdSquad turns feature ideas and bugs into build-ready specs by grilling the user until the real goal and decisions are understood, researching product options, shaping the chosen direction, designing the UX, researching engineering fit, and writing the final spec in the workspace's native spec system with decision rationale preserved.
