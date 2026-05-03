# Engineering Fit

Use this after the product direction and UX are shaped. The goal is to update the spec with implementation reality and grill any engineering decision that needs human judgment.

## Local Codebase Inspection

Inspect relevant:

- modules/components/routes/services
- data models/schema/migrations
- API boundaries
- auth/permissions
- state management
- validation patterns
- tests/fixtures/factories
- error handling conventions
- logging/analytics patterns
- background jobs/queues
- deployment/runtime constraints
- existing abstractions to reuse

## External Technical Research

Do not guess from model memory when versions, APIs, security guidance, or framework behavior could have changed. Use live docs whenever available.


Use web search/fetch/browser tools to check current docs for:

- framework/library APIs
- API provider behavior
- security recommendations
- performance constraints
- accessibility rules
- migration/version behavior
- known issues

## Engineering Grilling Rule

Inspect code/docs first. Grill only the decisions that require judgment: abstraction choice, migration tolerance, dependency appetite, performance/security tradeoffs, and test confidence. Ask one question at a time and provide a recommended answer.

## Questions to Answer

- What is the simplest correct implementation path?
- What abstraction fits the existing system?
- What should not be generalized yet?
- What data shape/API contract is needed?
- What migration or backfill is needed?
- What dependencies are required, if any?
- What risks exist around security, privacy, performance, accessibility, or reliability?
- What tests prove this works?
- What should be instrumented?

## Engineering Fit Brief Template

```markdown
## Engineering Fit Brief

**Relevant existing code:**
**Recommended implementation approach:**
**Key abstractions:**
**Data/API changes:**
**Dependencies:**
**Migration/backfill:**
**Testing strategy:**
**Risks:**
**Rejected approaches:**
**Decision rationale:**
**Open engineering questions:**
```

## Spec Update Checklist

Update the spec with:

- implementation notes
- data/API/system design
- migration/backfill if needed
- test plan
- risks/mitigations
- rejected approaches
- open engineering questions

## Engineering Anti-Patterns

Avoid:

- adding dependencies without justification
- inventing new abstractions when existing ones fit
- over-generalizing v1
- missing tests
- skipping auth/privacy/performance implications
- treating architecture guesses as facts
