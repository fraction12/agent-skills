# OpenSpec Output

Use this when the workspace has `openspec/`.

## Preferred Artifact Shape

```text
openspec/changes/<change-id>/
  proposal.md
  design.md
  tasks.md
  specs/<domain>/spec.md
```

## Useful Commands

```bash
openspec list
openspec list --specs
openspec show <change-or-spec>
openspec status --change <change-id>
openspec instructions --change <change-id> proposal
openspec instructions --change <change-id> design
openspec instructions --change <change-id> tasks
openspec validate <change-id>
```

Follow the repo's established OpenSpec workflow and naming style.

## Mapping

- `proposal.md` — why, problem, goals, non-goals, chosen approach, impact
- `design.md` — UX, architecture, data/API, alternatives, risks
- `specs/<domain>/spec.md` — requirements and scenarios
- `tasks.md` — implementation checklist and validation steps

## Requirement Style

OpenSpec requirements should be testable and scenario-oriented.

```markdown
### Requirement: User can preview generated prototype output
The system SHALL allow users to preview the generated artifact for a selected spec change.

#### Scenario: Preview succeeds
- **WHEN** a user opens an eligible change
- **AND** a generated artifact exists
- **THEN** the system displays the artifact preview
- **AND** shows the artifact path and generation timestamp
```

## Tasks Style

Tasks should be actionable and verifiable:

```markdown
## Tasks
- [ ] Add parser support for <capability>
- [ ] Add validation coverage for <edge case>
- [ ] Update UI flow for <state>
- [ ] Add regression tests for <behavior>
- [ ] Run <test/build/validation command>
```

## Validation

Before done, run or identify:

```bash
openspec validate <change-id>
```

If validation cannot run, state why.
