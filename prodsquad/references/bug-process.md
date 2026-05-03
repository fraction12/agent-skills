# Bug Process

Use this when actual behavior differs from expected behavior and the user wants a proper product/spec treatment, not just a quick patch.

## Intake Questions

Ask or infer one question at a time. Provide your recommended answer when useful. Inspect logs/code/docs instead of asking for facts the repo can answer.

- What was expected?
- What actually happened?
- How can it be reproduced?
- Who is affected?
- How severe/frequent is it?
- Is there a workaround?
- Did this start after a recent change?
- Is it a data loss, security, billing, workflow, UX, or trust issue?

## Bug Intent Brief Template

```markdown
## Bug Intent Brief

**Expected:**
**Actual:**
**Impact:**
**Repro:**
**Affected surface/users:**
**Severity:**
**Known workaround:**
**Recent related changes:**
**Root decision/rationale:**
**Open questions:**
```

## Bug Research

Research may include:

- codebase inspection
- logs/errors/screenshots if provided
- framework/library known issues
- recent dependency/version behavior
- support/docs for external APIs involved
- similar product behavior if UX ambiguity is part of the bug

## Bug Spec Sections

For final specs, include:

```markdown
## Expected vs Actual
## Reproduction Steps
## Impact and Severity
## Root Cause Hypotheses
## Fix Requirements
## Regression Tests
## Acceptance Criteria
## Rollout / Monitoring
```

## Severity Guide

- **Critical:** data loss, security/privacy, billing breakage, app unusable, production outage
- **High:** major workflow blocked, many users affected, no workaround
- **Medium:** important workflow degraded, workaround exists
- **Low:** polish, rare edge case, minor confusion

## Bug Anti-Patterns

Avoid:

- patching before expected behavior is clear
- skipping repro/impact
- confusing symptoms with root cause
- missing regression tests
- ignoring monitoring/rollback for risky fixes
