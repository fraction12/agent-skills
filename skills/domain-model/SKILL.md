---
name: domain-model
description: Grilled planning against a repo's domain model. Use when the user wants to stress-test a feature, plan, architecture, data model, or product direction against the project's language, CONTEXT.md, CONTEXT-MAP.md, docs/adr/, and actual code. Sharpens terminology and records domain terms/ADRs when decisions crystallize.
---

# Domain Model

Use this skill to reach shared understanding before planning or building. It behaves like a relentless interview, but grounded in the repository's domain language and decisions.

## Core behaviour

Interview the user relentlessly about every aspect of the plan until you reach shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. For each question, provide your recommended answer.

Ask one question at a time, waiting for feedback before continuing when the answer needs human judgment.

If a question can be answered by exploring the codebase, docs, existing specs, or web, explore first instead of asking the user.

## Domain awareness

Before and during exploration, look for:

- `CONTEXT.md`
- `CONTEXT-MAP.md`
- `docs/adr/`
- context-local `CONTEXT.md` files
- context-local `docs/adr/`
- README / AGENTS / CLAUDE / CODEX instructions
- code paths related to the plan

Use `references/context-format.md` when creating or updating `CONTEXT.md`.
Use `references/adr-format.md` when offering or writing ADRs.

## Single vs multi-context repos

Most repos have a single context:

```text
/
├── CONTEXT.md
├── docs/adr/
└── src/
```

A multi-context repo has a root `CONTEXT-MAP.md` that points to per-context docs:

```text
/
├── CONTEXT-MAP.md
├── docs/adr/                  # system-wide decisions
└── src/
    ├── ordering/
    │   ├── CONTEXT.md
    │   └── docs/adr/          # ordering decisions
    └── billing/
        ├── CONTEXT.md
        └── docs/adr/          # billing decisions
```

If `CONTEXT-MAP.md` exists, read it to locate the relevant context. If only root `CONTEXT.md` exists, treat the repo as single-context. If neither exists, create `CONTEXT.md` lazily only when a real domain term is resolved.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with `CONTEXT.md`, call it out immediately:

> Your glossary defines “Cancellation” as voiding an entire Order, but you seem to mean removing one line item. Which is it?

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term:

> You’re saying “account” — do you mean Customer, Workspace, or User? My recommendation is Workspace because permissions appear to attach there.

### Discuss concrete scenarios

Stress-test domain relationships with concrete examples. Invent edge-case scenarios that force precision around boundaries, lifecycle, ownership, permissions, and state changes.

### Cross-reference with code

When the user states how something works, check the code where possible. If the code contradicts the user, surface it clearly:

> The code cancels entire Orders, but you just said partial cancellation is possible. Which one should become the domain truth?

### Update domain docs inline

When a term is resolved, update `CONTEXT.md` immediately. Do not batch these up. Keep `CONTEXT.md` focused on domain language meaningful to domain experts; do not add generic programming concepts or implementation details.

### Offer ADRs sparingly

Only offer an ADR when all three are true:

1. **Hard to reverse** — changing later has meaningful cost.
2. **Surprising without context** — a future reader would wonder why it was done this way.
3. **Real tradeoff** — there were genuine alternatives and a deliberate choice.

If any is missing, skip the ADR.

## Output

At the end of a grilling session, summarize:

- clarified domain terms
- decisions made
- rationale
- rejected alternatives
- contradictions between user understanding and code/docs
- `CONTEXT.md` updates made or recommended
- ADRs created or offered
- remaining open questions

## Short form

If asked what Domain Model does, say:

> Domain Model grills a plan against the repo’s actual language, code, and architectural decisions so the human and agent share the same mental model before specs or implementation begin.
