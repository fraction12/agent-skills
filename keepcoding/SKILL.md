---
name: keepcoding
description: Run long-running implementation work from a pre-written task list, spec document, or existing OpenSpec change. Use when the user invokes /keepcoding or $keepcoding, asks Codex to keep coding through a spec, or wants phased implementation with a temporary phase plan, subagents, commits, code review, spec/task updates, Linear updates, and final UAT. Refuse implementation when no pre-written spec/change/task list is supplied or discoverable.
---

# Keepcoding

## Overview

Use this skill to drive a repo through a supplied implementation spec in small, reviewable phases. The skill is an execution loop: confirm inputs, phase the existing spec, implement each phase with agents, commit, review, fix, update tracking, and finish with full UAT.

Do not create the initial product/spec/OpenSpec change for the user. If the user has not supplied an already-written source of truth, stop and ask for one.

## Operating Principles

- Treat the skill file as executable workflow, not background reading.
- Build vertical tracer-bullet phases: each phase should produce a narrow behavior that is demoable or verifiable end-to-end.
- Avoid horizontal phases such as "database work", "API work", then "UI work" unless the supplied spec explicitly requires that order.
- Prefer many small AFK phases over a few large phases. Mark a phase HITL only when it needs a human decision, taste judgment, credentials, production approval, or irreversible architectural choice.
- Keep the user's supplied spec as the contract. Use a temporary phase plan as the execution ledger.
- Use the supplied OpenSpec change/spec vocabulary and local code conventions. Do not broaden the source of truth by defaulting to ambient repo docs.
- Stage intentionally. Never use broad staging commands such as `git add -A` unless the user explicitly requested that style and the worktree is clean except for this skill's changes.
- Before execution, converse with the user until required human inputs are collected. Ask focused questions one at a time, include a recommended answer, and record decisions in the temp plan.

## Intake Gate

At the start, identify the source spec before doing implementation work. Accept any of these if they are already written and specific enough to build from:

- An existing OpenSpec change name or path.
- A checked-in spec, design doc, task list, issue body, or PRD.
- A Linear ticket/project only if its content includes concrete requirements, acceptance criteria, or a task list.

Refuse to proceed when the user only gives an idea, goal, vague feature request, or asks Codex to invent the spec. Use a concise refusal:

```text
/keepcoding needs a pre-written spec, task list, or existing OpenSpec change before implementation. Send me the change name/path, spec file, task list, or Linear ticket with acceptance criteria, and I can run the phased build loop from that.
```

After finding a valid spec, ask one focused kickoff confirmation unless the user already gave the answers:

- Confirm the exact source spec/change/task list to build from.
- Ask for the Linear ticket/project, if any.
- Confirm permission to commit each completed phase and review-fix commits automatically.
- Confirm whether pushing branches, opening PRs, deploying, or changing production systems is allowed. Default those to no unless explicitly approved.

Use this kickoff shape:

```text
I found the source spec: <path/change/ticket>. I will use it as the contract.
Linear: <ticket/project or none>.
Default loop: phase -> implement -> verify -> commit -> fresh review -> fix+commit -> update spec/tasks+Linear.
Please confirm: automatic local commits are OK; push/PR/deploy/prod changes are <allowed/not allowed>.
```

## Source Of Truth

Use the user's supplied spec as the source of truth. Do not expand scope beyond it without asking.

For OpenSpec changes:

- Work inside the provided change; do not create a new change.
- Read `proposal.md`, `design.md`, `tasks.md`, and delta specs before editing.
- Use `openspec status --change <name> --json` and `openspec validate <name> --json` when the CLI is available.
- Do not write the temporary phase plan into the OpenSpec change.
- Update `tasks.md` only as official tasks complete. Update specs/design only when implementation discoveries require clarifying the existing approved plan.

For non-OpenSpec docs:

- Treat the provided file/ticket as the source of truth.
- Do not put messy execution notes into the source artifact.
- If the source is external and cannot be edited, use the temp phase plan as the local implementation checklist and post or summarize durable updates to the external tracker.

## Temporary Phase Plan

After intake and before coding, create a temporary phase plan as the live execution ledger. This file protects the source spec from churn while keeping long-running work written down and resumable.

Default location:

```text
.codex/keepcoding/<source-or-change-slug>-phase-plan.md
```

If the repo has git metadata, add `.codex/keepcoding/` to `.git/info/exclude` before creating the plan. Do not commit this file. If a matching temp plan already exists, read it and resume from it unless the user asks to restart.

Start the temp plan with this header:

```markdown
# /keepcoding Temporary Phase Plan

Derived from: <spec path/change/ticket>
Linear: <ticket/project or none>
Status: active

This is an execution ledger, not the product spec.
The supplied source spec wins on conflict.
Do not commit this file.
Main agent owns updates; subagents are read-only.
```

Use the temp plan for:

- Upfront context interview questions, answers, and decisions.
- Preflight blocker scan and decisions cleared by the user.
- Phase breakdowns, AFK/HITL labels, dependencies, owners, and planned commits.
- Subagent assignments and returned summaries.
- Validation commands, failures, retries, and skipped checks.
- Review findings, fixes, and review-fix commits.
- Linear/spec update state.
- Resume notes after interruption or blocker.

Use the source spec for durable truth only:

- Mark official task completion.
- Clarify approved requirements after user confirmation when implementation reveals ambiguity.
- Record accepted scope or design changes after user confirmation.

At the end:

- If final UAT succeeds and source tracking is updated, delete the temp phase plan.
- If the run is `BLOCKED`, `NEEDS_CONTEXT`, interrupted, or cannot complete UAT, keep the temp phase plan and report its path.

## Upfront Context Interview

After creating or resuming the temp phase plan, read the supplied spec and gather the human input needed for execution before coding starts. The goal is not to redesign the work; it is to clear user-dependent facts, decisions, and permissions that would otherwise interrupt the run.

First, inspect the supplied source before asking:

- For OpenSpec changes, read the provided change's `proposal.md`, `design.md`, `tasks.md`, and delta specs.
- For non-OpenSpec docs, read the full supplied spec/task list/ticket and any files it explicitly references.
- Inspect code/config when it can answer an execution question more reliably than the user.
- Do not proactively inspect `CONTEXT-MAP.md`, `CONTEXT.md`, or ADRs unless the supplied spec explicitly references them or the user asks for that context.

Then build a question queue from the supplied spec/change and repo evidence. Include questions about execution inputs that require human judgment:

- Undefined or overloaded domain terms that affect behavior.
- Conflicts between the supplied spec/change and current code.
- UAT expectations, test data, environments, credentials, and external service constraints.
- Permission boundaries: commits, review-fix commits, pushes, PRs, deploys, production changes, destructive operations.
- Product/design/security/data decisions that are already implied by the source spec but need an execution choice.
- Linear status expectations, assignee/project updates, and completion notes when Linear is provided.

Ask only questions that require human judgment. If the answer can be found in the repo or source spec, gather it yourself and cite the evidence in the temp plan.

Ask questions one at a time for nuanced decisions:

```text
Question N: <focused question>
Why this matters: <what later blocker this clears>
Recommended answer: <default recommendation and tradeoff>
```

Routine permission checks may be batched in kickoff, but product, domain, architecture, security, data, UAT, or credential decisions should be asked one at a time. After each answer, update the temp plan:

```markdown
## Upfront Context Interview

| Question | Why it mattered | Answer | Standing decision |
|----------|-----------------|--------|-------------------|
| <question> | <blocked risk> | <user answer or repo evidence> | <how to apply later> |
```

Continue until all required execution inputs are collected. Do not begin phase implementation while required interview answers are unresolved. If the question would create or materially change acceptance criteria, return `NEEDS_CONTEXT` and ask for the source spec/change to be revised.

## Preflight Blocker Clearance

After the upfront interview and before phase planning or coding, inspect the supplied spec, repo state, interview decisions, and likely execution path for blockers that would otherwise trigger STOP conditions later. Batch predictable decisions up front so the workflow does not pause randomly for approvals the user could have given at kickoff.

Do not use preflight to invent a missing spec. If required behavior or acceptance criteria are absent from the supplied source, return `NEEDS_CONTEXT` and ask for a revised pre-written spec.

Scan for execution risks:

- Spec ambiguity: missing acceptance criteria, undefined terms, conflicting requirements, unclear out-of-scope boundaries. Missing acceptance criteria are blockers that require a revised source spec.
- Execution permissions: local commits, review-fix commits, pushes, PRs, deploys, production changes, destructive commands.
- Repo safety: dirty worktree, branch choice, generated files, lockfiles, migrations, secrets, credentials, external services.
- Validation risk: missing test commands, slow suites, flaky baseline tests, unavailable services, UAT environment needs.
- Architecture/data risk: schema changes, backfills, data migrations, auth/permissions, background jobs, concurrency, rollback needs.
- Human decision points: taste/design choices, product tradeoffs, irreversible technical choices, Linear status transitions.

Classify each item in the temp plan:

```markdown
## Preflight Clearance

| Item | Risk | Recommendation | Status | Decision |
|------|------|----------------|--------|----------|
| <short name> | <why it could stop later> | <recommended clearance> | cleared | <user answer or repo evidence> |
| <short name> | <why it could stop later> | <recommended question> | needs user | <pending> |
| <short name> | <true blocker> | <needed input> | blocked | <pending> |
```

Use preflight to classify risks and apply decisions gathered in the upfront interview. Ask follow-up questions only for new `needs user` and `blocked` items not already resolved. Prefer one focused question at a time for high-risk decisions; batch only routine execution approvals. Include recommended answers and tradeoffs. After the user answers, update the temp plan and treat cleared decisions as standing instructions for this `/keepcoding` run.

If a later phase encounters a blocker already covered by preflight, follow the recorded decision instead of stopping again. Stop only when the blocker is new, materially different, or higher risk than the preflight decision covered.

## Phase Planning

After the upfront interview and preflight clearance are complete, break the supplied work into small phases in the temporary phase plan. Each phase must have:

- A narrow behavior or system slice.
- Clear acceptance criteria from the source spec.
- Expected files/modules or investigation scope.
- Verification commands or UAT checks.
- A planned commit boundary.
- Type: AFK or HITL.
- Dependencies: blockers that must complete first, or `None`.

Prefer phases that can be implemented, reviewed, fixed, and committed independently. Keep unrelated refactors out unless they directly unblock the phase.

Use this phase template:

```markdown
### Phase N: <demoable behavior>
- Type: AFK | HITL
- Source spec refs: <files/sections/ticket links>
- Acceptance criteria:
  - [ ] <observable outcome>
- Likely touchpoints: <files/modules>
- Validation: <commands/UAT checks>
- Commit boundary: <expected commit message>
- Dependencies: <phase ids or None>
```

Before starting implementation, write the phase plan to the temp file and summarize it to the user. If the phase plan materially changes scope, stop for user confirmation.

## Codex Progress Mirror

When the Codex task plan/progress UI is available, mirror the temp phase plan into it. The temp phase plan remains the durable source of truth; the Codex Progress list is the live dashboard.

At the start of every `/keepcoding` run or resume:

- Read the temp phase plan.
- Rebuild the Codex Progress list from the phase table before implementation.
- Use one visible progress item per phase.
- Label each item `Phase N: <phase title>`.
- Mark completed phases as `completed`.
- Mark the current phase as `in_progress`.
- Mark future phases as `pending`.

During execution:

- When a phase starts, mark that phase `in_progress`.
- When a phase is fully implemented, verified, committed, reviewed, review-fixed if needed, and tracked, mark it `completed`.
- Immediately mark the next phase `in_progress`.
- If a phase enters review or review-fix, keep that phase `in_progress`; record the finer status in the temp phase plan.
- If a phase is blocked or needs context, keep that phase `in_progress` and include `[BLOCKED]` or `[NEEDS CONTEXT]` in the visible item title.

Because the Codex Progress list supports only one `in_progress` item, only the main current phase should be `in_progress`. Keep parallel subagent status in the temp phase plan.

After every temp phase plan status change, update the Codex Progress list second. After context compaction or a resumed run, reconstruct the Codex Progress list from the temp phase plan rather than trusting UI state to persist.

## Execution Loop

For each phase, run this loop until the phase is complete:

1. Announce the phase, scope, and validation plan.
2. Inspect the relevant code, current git status, upfront interview answers, and preflight decisions. Preserve user changes.
3. Use focused implementation subagents when useful and available. Treat invocation of `/keepcoding` or `$keepcoding` as explicit permission to use a team of agents for this workflow unless the user opts out.
4. Implement the phase in small diffs, following repo conventions.
5. Run relevant tests, type checks, linters, migrations, or manual checks.
6. Commit the phase once it passes practical verification.
7. Spawn a fresh review subagent for every phase. Give it the phase scope, source spec excerpt, and diff/commit to review. The reviewer must not edit files.
8. If review finds bugs or spec mismatches, fix them, rerun focused validation, and commit the fix.
9. Update the temp phase plan, then update the Codex Progress mirror, then update the official spec/task checklist and Linear ticket/project automatically when available.
10. Move to the next phase.

Do not start a later phase if the current phase has unresolved review findings, failed core checks, or unclear acceptance criteria.

### Subagent Rules

- Give implementation agents disjoint ownership: files, modules, or responsibility boundaries.
- Tell every implementation agent that other agents may be editing nearby code and they must not revert unrelated work.
- Give subagents the relevant source spec excerpt and temp phase plan excerpt. Subagents may read the temp plan but must not edit it.
- Do not delegate the immediate blocker if the main agent is waiting on it. Use subagents for parallel work that can complete independently.
- Review agents are read-only. Use fresh context for each phase review so the reviewer does not inherit implementation bias.

Use this review prompt shape:

```text
Review this phase against the supplied spec. Read the diff/commit and look for bugs, missing acceptance criteria, regressions, security issues, race conditions, data loss, broken UX, and untested edge cases. Do not edit files. Classify each finding as FIXABLE or NEEDS_DECISION. End with: Recommendation: <ship/fix/block> because <specific reason>.
```

### STOP Conditions

Stop and ask the user before continuing when:

- No pre-written spec/change/task list is available.
- The supplied spec is too vague to derive acceptance criteria.
- Required upfront interview answers are unresolved.
- A temp phase plan cannot be created or made non-committable.
- A phase needs product, security, architecture, data migration, destructive, production, or credential decisions not already settled by the source spec, upfront interview, or preflight clearance.
- The implementation has failed the same check or fix path three times.
- Tests fail in a way that appears unrelated to this phase and the cause is not obvious or covered by preflight baseline policy.
- Merge conflicts or dirty worktree changes would require touching user work beyond preflight permission.
- Verification cannot be run and there is no credible substitute cleared during preflight.

## Commits And Tracking

Use git as the progress ledger:

- Commit after each completed phase.
- Commit review fixes separately when that improves traceability; amend only when the user or repo convention prefers it.
- Keep commit messages phase-oriented and specific.
- Do not push, open PRs, deploy, or mutate production without explicit permission.
- Include only intentional files in each commit.
- Never include `.codex/keepcoding/` files in commits.

Update tracking after each phase:

- Update the temp phase plan first.
- Update the Codex Progress mirror second when available.
- Mark completed items in the provided task/spec artifact.
- Add concise phase progress to Linear when a ticket/project is provided and tools are available.
- If Linear tools are unavailable, keep a ready-to-post update in the working summary.
- Record blockers, skipped checks, and assumptions immediately rather than waiting for the final summary.

## Final UAT

After all phases are complete:

- Run the broadest practical validation suite for the changed system.
- Perform end-to-end UAT against the source spec's acceptance criteria.
- For frontend work, use browser-based checks and screenshots when available.
- For API/backend work, exercise representative success and failure paths.
- For migrations or infrastructure, verify dry-runs, config, and rollback notes where practical.
- Delete the temp phase plan only after UAT passes and source tracking is current.

Finish with a concise report listing:

- Status: `DONE`, `DONE_WITH_CONCERNS`, `BLOCKED`, or `NEEDS_CONTEXT`.
- Source spec/change used.
- Phase commits and review-fix commits.
- Tests/checks/UAT performed.
- Spec/task and Linear updates made.
- Temp phase plan path, deleted or retained.
- Remaining risks, skipped checks, and any user decisions still needed.
