# Agent Skills

Portable, agent-agnostic skill pack for coding and product-development agents.

Each skill is a self-contained directory with a `SKILL.md` entrypoint. Skills may include references, scripts, or assets, but the canonical contract is deliberately simple so the pack can move between agents.

## Current skills

See `skill-pack.json` for the machine-readable manifest.

## Install

Copy all skills into Codex:

```bash
scripts/install-skills.sh codex
```

Copy all skills into OpenClaw:

```bash
scripts/install-skills.sh openclaw
```

Install into any agent skill directory:

```bash
scripts/install-skills.sh /path/to/agent/skills
```

Use symlinks instead of copies:

```bash
MODE=symlink scripts/install-skills.sh codex
```

## Skill contract

Required:

```text
skill-name/
  SKILL.md
```

Recommended:

```text
skill-name/
  SKILL.md
  references/   # optional docs loaded only when needed
  scripts/      # optional deterministic helper scripts
  assets/       # optional templates/static assets used in outputs
```

Keep skills runner-neutral where possible. Runner-specific metadata files may exist for compatibility, but `SKILL.md` is the source of truth.
