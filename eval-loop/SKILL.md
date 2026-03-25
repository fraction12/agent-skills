---
name: eval-loop
description: "Set up and manage Karpathy-style eval/improve loops on any project. Autonomous cron cycles that evaluate product quality, identify the worst issue, fix it with TDD, and ship or revert. Use when: (1) starting an eval loop on a project, (2) adding issues/features to an existing loop, (3) checking loop status/progress, (4) killing/pausing a loop, (5) adjusting loop settings, (6) user says 'eval loop', 'Karpathy loop', 'improvement loop', 'start the eval', 'auto-improve', 'how is the loop doing', 'add this to the loop', or '/eval-loop'. NOT for: one-off bug fixes (just fix them), agent-loop ticket work (use agent-loop skill), or manual code review."
---

# Eval Loop

Autonomous product improvement via eval → fix → ship cycles.

## Concept

Three files form the contract between the cron agent and the project:

```
eval/
  program.md        # Constitution — identity, methodology, rules (agent reads, never modifies)
  scenarios.yaml    # Scenario bank — what "good" looks like (agent reads, never modifies)
  experiments.md    # Log — cycle results, shipped commits, failed attempts (agent appends only)
```

A cron runs every N minutes, reads all three, executes one cycle, and ships or reverts.

## Commands

### Start a loop: `"Start an eval loop on <project>"`

1. **Check for existing loop**: `openclaw cron ls | grep -i "<project>"`. If found, offer to reconfigure instead of duplicating.
2. Inspect the project — detect language, build/test commands, entry points, binary path.
3. Ask Sir 2-3 targeted questions:
   - "What does 'good' look like? CLI output? Web UI? API responses? Visual polish?"
   - "What are the 3-5 things that bug you most right now?"
   - "How aggressive? Every 15m, 30m, hourly?"
4. Scaffold `eval/` in the project repo — see [Scaffolding](#scaffolding).
5. Fill in the scaffolded templates with project-specific content (scaffold.sh creates placeholders — Jarvis must edit `program.md` and `scenarios.yaml` with real content before the first run).
6. Create the cron — see [Cron Settings](#cron-settings).
7. Verify the cron was created correctly: `openclaw cron ls` and confirm model/timeout/interval.
8. Force-run the first cycle, report back.

### Add an issue/feature: `"Add this to the loop"` / `"The loop should fix X"`

1. Add a scenario to `eval/scenarios.yaml` with appropriate weight.
2. Append a known-issue entry to `eval/experiments.md` with `Priority: HIGH`.
3. Confirm what was added — next matching cycle type picks it up.

### Check status: `"Status on the loop"` / `"How's the eval loop doing?"`

1. Find the cron: `openclaw cron ls | grep -i "<project>"` — note the job ID.
2. Pull recent runs: `openclaw cron runs --id <jobId> --limit 5`.
3. Read the tail of `eval/experiments.md` for score trends: `tail -80 <repo>/eval/experiments.md`.
4. Summarize: wins shipped, failures/timeouts, score trends, current cycle type, consecutive reverts.
5. If 3+ consecutive reverts, flag it — the loop may need scenario adjustment or manual intervention.

### Pause/Kill: `"Pause the loop"` / `"Kill the eval loop"`

1. Find the cron: `openclaw cron ls | grep -i "<project>"`.
2. `openclaw cron disable <jobId>` (pause) or `openclaw cron rm <jobId>` (kill).
3. Summarize total shipped work from `eval/experiments.md`: count of shipped commits, score progression, notable fixes.

### Adjust: `"Make the loop faster/slower"` / `"Change the loop to every 30m"`

1. Find and edit the cron: `openclaw cron edit <jobId> --every <new-interval>`.
2. Confirm the change.

## Scaffolding

Run `scripts/scaffold.sh <repo-path>` to create the `eval/` directory with template files.

**Important:** The script creates templates with `<!-- placeholder -->` comments. After running it, edit all three files:
- `program.md`: Fill in project identity, product description, eval methodology, known issues.
- `scenarios.yaml`: Replace commented examples with real scenarios seeded from Sir's pain points + code inspection.
- `experiments.md`: Leave as-is (empty log).

### program.md

Generate from project inspection. Required sections:

| Section | Content |
|---------|---------|
| Identity | One line: who the agent is, what the product is |
| The Product | 2-3 sentences: what it does, stack, quality bar |
| How the Loop Works | Standard 6-step cycle (eval → identify → fix → verify → ship/revert → report) |
| Hard Rules | See [Hard Rules](#hard-rules) |
| Eval Methodology | Project-specific — see table below |
| Scoring | 0-10 per scenario, overall = average, target 9.0+ |
| Known Issues | Initial bugs from manual eval — the first targets |

Eval methodology by project type:

| Project type | Eval methods |
|-------------|-------------|
| CLI tool | One-shot dry-run output + TUI screenshots via Peekaboo |
| Web app (backend) | API calls (curl/httpie) + unit tests |
| Web app (frontend) | Peekaboo browser screenshots + lighthouse |
| Library/SDK | Unit tests + example script output |
| Mixed | Alternate cycle types — see [Cycle Type Alternation](#cycle-type-alternation) |

### scenarios.yaml

Seed 8-15 scenarios from Sir's pain points + code inspection.

```yaml
scenarios:
  - id: short-kebab-id
    name: "Human-readable description"
    method: cli-oneshot | tui | tui-visual | api | unit-test
    prompt: "exact input to test"        # for cli/tui methods
    steps:                                # for multi-step tui-visual
      - launch
      - type: "input"
      - wait: 5
      - screenshot
    expected:
      key: value                          # project-specific assertions
    cleanup: "path/to/remove"             # optional artifact cleanup
    weight: 1-3                           # priority (3 = highest)
```

Weight guide:
- **3**: Core UX flows, user-reported issues, blocking bugs
- **2**: Important quality/polish, feature correctness
- **1**: Edge cases, nice-to-haves, minor polish

### experiments.md entry format

Each cycle appends one entry in this format:

```markdown
---

### YYYY-MM-DD HH:MM ET — Cycle: <type> (<fast|slow>)
**Scenario scores:**
- scenario-id-1: <before>→<after> (or "not evaluated: <reason>")
- scenario-id-2: <score>/10
**Average:** X.X → Y.Y
**Worst:** <scenario-id> (<score>)
**Fix:** <one-line description of what was attempted>
**Files:** <list of modified files>
**Result:** Shipped `<commit-hash>` | Reverted — <reason>
**Notes:** <optional observations, regressions caught, ideas for next cycle>
```

## Hard Rules

These go in every `program.md` and are echoed in the cron prompt:

1. One fix per cycle.
2. Tests must pass. No exceptions.
3. Build must succeed. Revert if not.
4. No force pushes, no history rewrites.
5. Never modify `program.md` or `scenarios.yaml`.
6. Clean up test artifacts.
7. Bail out gracefully near timeout — ship what's green, log what's pending.

## Pre-Flight Checks

The cron prompt should include these before starting a cycle:

```
## Pre-Flight
1. `cd <repo> && git status` — must be clean. If dirty, stash or abort.
2. `git pull --ff-only` — sync with remote. If conflicts, abort and log.
3. Verify binary builds: `<build command>`.
```

This prevents cycles from failing due to dirty trees, merge conflicts, or stale state.

## Cron Settings

```bash
openclaw cron add \
  --name "<Project> Eval Loop" \
  --every <interval> \
  --agent main \
  --model anthropic/claude-opus-4-6 \
  --thinking high \
  --session isolated \
  --timeout-seconds 900 \
  --best-effort-deliver \
  --announce \
  --failure-alert --failure-alert-after 2 \
  --message "<prompt>"
```

**Naming convention:** Always `"<Project> Eval Loop"` — this makes grep-based lookup reliable for status/kill.

**Non-negotiable settings:**
- **Model:** Opus + `--thinking high` — eval loops require multi-phase reasoning
- **Timeout:** 900s minimum (15 min). Eval + fix + test + commit reliably takes 8-12 min
- **Session:** Always isolated — each cycle must start fresh
- **Failure alerts after 2** — catches systematic problems early

**Post-creation verification:** Run `openclaw cron ls` and confirm the model field shows the expected value. Model alias resolution has caused silent defaults in the past.

**Interval guide:**
- Every 15m: aggressive, for active development sprints
- Every 30m: steady improvement, good default
- Every 1h: background polish, low-urgency projects
- Every 4-6h: maintenance mode, mature projects

### Prompt Construction

Read `references/prompt-template.md` for the full cron prompt template with all placeholders.

The template uses `<INCLUDE IF ...>` markers to indicate conditional sections — these are instructions to Jarvis during prompt assembly, not literal template syntax. Remove the markers and include/exclude the wrapped section based on project needs.

Key prompt sections:
1. Identity + mission (one line)
2. Setup (repo, binary, data paths, config)
3. Pre-flight checks
4. Instructions: read program → read scenarios → read experiments → run one cycle
5. **Time budget** — explicit phase breakdown (total = timeout minus 2 min margin)
6. **Cycle type alternation** — when both fast and slow eval methods exist
7. **Peekaboo commands** — copy-paste ready, only if TUI/visual eval needed
8. Hard rules echo
9. Report format constraint (under 1500 words)

## Cycle Type Alternation

When a project has both fast evals (CLI, unit tests) and slow evals (TUI screenshots, browser):

- Fast cycle: 4-5 CLI/API scenarios, fix worst backend/logic issue
- Slow cycle: 2-3 visual scenarios with real screenshots, fix worst UX issue
- Check `experiments.md` for last cycle type, do the opposite

This prevents slow eval methods from starving the fix phase or causing timeouts.

For single-method projects, skip alternation entirely.

## Circuit Breaker

If `experiments.md` shows 3+ consecutive reverts:
- The loop is stuck. Something structural is wrong.
- The cron prompt should include: *"If the last 3 entries in experiments.md are all reverts, STOP. Do not attempt a fix. Log a diagnostic entry explaining what pattern you see and what might be wrong. Jarvis will intervene."*
- On status check, flag this to Sir and suggest: scenario adjustment, manual fix of the blocker, or pausing the loop.

## Scenario Evolution

Scenarios should grow over time. Suggest new scenarios when:
- A shipped fix reveals an adjacent untested behavior
- Sir mentions a new pain point in conversation (offer: "Want me to add that to the loop?")
- Average score exceeds 8.5 — the bar may be too low; propose harder scenarios
- A category of work has no coverage (e.g., error handling, edge cases, accessibility)

Only Sir modifies `scenarios.yaml` — propose additions via chat, don't auto-add.

## Git Safety

- Eval loop always works on `main` (or the project's default branch).
- Pre-flight stash/abort prevents dirty-tree corruption.
- Each cycle is atomic: one commit or full revert. No partial states.
- `eval/` directory should be committed to the repo — `experiments.md` is version-controlled institutional memory.
- Add to `.gitignore` if the project generates temp eval artifacts: screenshots, debug logs, etc. The eval files themselves should be tracked.

## Lessons Learned (Baked In)

- **Agents fabricate eval scores.** TUI/visual scores MUST come from real screenshots. Hard rule in every prompt.
- **Spell out automation commands.** Peekaboo/osascript syntax must be copy-paste ready in the prompt.
- **Time budgets prevent timeouts.** The agent doesn't know it's about to be killed. Budget phases explicitly.
- **One fix per cycle.** Multi-fix cycles lead to tangled reverts and ambiguous experiments.md entries.
- **experiments.md is institutional memory.** Without it, the loop repeats failed approaches endlessly.
- **Verify model after cron creation.** Model alias resolution can silently default. Always check.
- **Alternating cycles prevent starvation.** All-in-one cycles cause timeouts on complex projects.
- **Pre-flight prevents cascading failures.** A dirty tree from a crashed prior cycle will break the next one.
