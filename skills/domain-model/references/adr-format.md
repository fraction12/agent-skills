# ADR Format

ADRs live in `docs/adr/` unless the repo has context-local ADRs. Use sequential numbering: `0001-slug.md`, `0002-slug.md`, etc.

Create the `docs/adr/` directory lazily — only when the first ADR is genuinely needed.

## Template

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

That is enough for many ADRs. The value is recording that a decision was made and why, not filling out ceremony.

## Optional sections

Only include these when they add genuine value:

- **Status** frontmatter: `proposed | accepted | deprecated | superseded by ADR-NNNN`
- **Considered Options** — only when rejected alternatives are worth remembering
- **Consequences** — only when non-obvious downstream effects matter

## When to offer an ADR

All three must be true:

1. **Hard to reverse** — the cost of changing later is meaningful.
2. **Surprising without context** — a future reader will wonder why it was done this way.
3. **Real tradeoff** — there were genuine alternatives and a specific reason for the choice.

Skip ADRs for obvious, easy-to-reverse, or temporary decisions.

## What qualifies

- Architectural shape: monorepo, event sourcing, projection model, context split.
- Integration patterns between contexts: events vs sync HTTP, ownership by ID only.
- Technology choices with meaningful lock-in: database, message bus, auth provider, deployment target.
- Boundary and scope decisions: which context owns which data.
- Deliberate deviations from obvious paths: manual SQL over ORM, REST over GraphQL, etc.
- Constraints not visible in code: compliance, latency, partner contract, budget, operational constraints.
- Non-obvious rejected alternatives that future agents would otherwise propose again.
