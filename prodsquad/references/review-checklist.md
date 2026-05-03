# Review Checklist

Use this for `/prodsquad:review` or when auditing a draft spec/change before implementation.

## Review Goal

Be critical and gap-focused. Do not rubber-stamp. The review should answer: can a competent coding agent build this without guessing, and would a product/design/engineering reviewer understand the decision?

## Product Review

Check:

- [ ] Problem is specific, not a vague desire
- [ ] User/job is clear
- [ ] Goals are explicit
- [ ] Non-goals are explicit
- [ ] Chosen approach is justified
- [ ] Decision rationale is captured
- [ ] Alternatives/tradeoffs are captured
- [ ] Success metrics or signals exist
- [ ] Rollout/MVP boundary is clear

## Research Review

Check:

- [ ] Relevant external research was done or intentionally skipped with reason
- [ ] Current facts were verified with web search/fetch when needed
- [ ] Sources are cited when web research was used
- [ ] Competitor/adjacent patterns are synthesized into product implications
- [ ] The spec avoids stale, unsupported, or overconfident claims

## UX Review

Check user-facing work for:

- [ ] Primary user flow
- [ ] Secondary flows
- [ ] Empty state
- [ ] Loading state
- [ ] Error state
- [ ] Success state
- [ ] Disabled/permission state
- [ ] Mobile/responsive considerations where relevant
- [ ] Accessibility considerations
- [ ] Copy/labels for confusing moments

## Engineering Review

Check:

- [ ] Existing codebase fit was inspected
- [ ] Recommended abstraction is named
- [ ] Data/API/system impact is explicit
- [ ] Dependencies are justified
- [ ] Migration/backfill needs are stated or ruled out
- [ ] Security/privacy/performance risks are considered
- [ ] Rejected approaches are captured
- [ ] Open engineering questions are visible

## Requirements Review

Check:

- [ ] Requirements are testable
- [ ] Acceptance criteria are specific
- [ ] Edge cases are covered
- [ ] Tasks are actionable
- [ ] Validation/test commands are listed
- [ ] The spec does not require implementation guessing

## OpenSpec Review

If using OpenSpec, check:

- [ ] `proposal.md` explains why and scope
- [ ] `design.md` captures UX/architecture/tradeoffs
- [ ] spec deltas use SHALL language where appropriate
- [ ] scenarios use WHEN/THEN style where appropriate
- [ ] `tasks.md` is executable and verifiable
- [ ] `openspec validate <change-id>` passes or blocker is documented

## Review Output Template

```markdown
## ProdSquad Review

**Verdict:** ready / needs revision / blocked

### Highest-risk gaps
1.
2.
3.

### Product gaps
-

### UX gaps
-

### Engineering gaps
-

### Requirements/test gaps
-

### Missing decision-grilling questions
-

### Recommended fixes before build
1.
2.
3.
```
