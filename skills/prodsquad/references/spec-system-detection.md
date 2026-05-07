# Spec System Detection

Use this before writing files.

## Look For

```text
openspec/
.open-spec/
specs/
docs/specs/
docs/requirements/
requirements/
product/
prd/
rfcs/
adr/
.storybook/
.spec-ui/
```

Also inspect:

- README.md
- AGENTS.md
- CLAUDE.md
- CODEX.md
- CONTRIBUTING.md
- existing change/spec folders
- package/framework files
- tests and fixture conventions

## Decision Rules

- If `openspec/` exists, prefer OpenSpec artifacts.
- If another explicit spec/RFC/PRD convention exists, follow it.
- If Storybook/component-state docs are the obvious local convention, produce state/component specs.
- If `.spec-ui/` or prototype packages exist and the work is UX/prototype-heavy, consider Spec UI output.
- If no system exists, use `final-spec-template.md` and ask before writing new files unless the user clearly requested file output.

## Do Not

- initialize a new spec system without permission
- create OpenSpec just because you prefer it
- ignore existing repo conventions
- put specs in random locations
