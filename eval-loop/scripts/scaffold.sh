#!/usr/bin/env bash
# scaffold.sh — Create eval/ directory structure in a project repo.
# Usage: scaffold.sh <project-repo-path>
#
# Creates:
#   eval/program.md       (template — fill in project-specific sections)
#   eval/scenarios.yaml   (template — add real scenarios)
#   eval/experiments.md   (empty log)

set -euo pipefail

REPO="${1:?Usage: scaffold.sh <project-repo-path>}"

if [ ! -d "$REPO" ]; then
  echo "Error: $REPO is not a directory" >&2
  exit 1
fi

EVAL_DIR="$REPO/eval"

if [ -d "$EVAL_DIR" ]; then
  echo "Error: $EVAL_DIR already exists. Remove it first or edit in place." >&2
  exit 1
fi

mkdir -p "$EVAL_DIR"

# --- program.md ---
cat > "$EVAL_DIR/program.md" << 'PROGRAM'
# <PROJECT> — Eval & Improve Loop

*Karpathy-style: eval → identify worst issue → fix → verify → commit or revert → repeat.*

## Identity
<!-- One line: who the agent is and what the product is. -->
You are Jarvis, running the <PROJECT> eval-and-improve loop.

## The Product
<!-- 2-3 sentences: what it does, stack, quality bar. -->

## How the Loop Works

Each run:

### 1. Eval — Score the product
Run the scenario bank against the real binary/app. Score each scenario.

### 2. Identify — Pick the worst thing
Find the lowest-scoring or most impactful issue. Pick ONE.

### 3. Fix — Implement the change
One fix per cycle. Red-green TDD when practical.

### 4. Verify — Run tests + re-eval
- Full test suite must pass
- Build must succeed
- Re-run the failing scenario to confirm improvement

### 5. Ship or Revert
- Green + improved → commit + push
- Broken → checkout + clean, log the failure

### 6. Report
Log in `eval/experiments.md`: scores, changes, commit hash or revert reason.

## Hard Rules
1. One fix per cycle.
2. Tests must pass. No exceptions.
3. Build must succeed. Revert if not.
4. No force pushes, no history rewrites.
5. Never modify program.md or scenarios.yaml.
6. Clean up test artifacts.
7. Bail out gracefully near timeout.

## Eval Methodology

<!-- Adapt to project type:
### CLI One-Shot
Run `<binary> "<prompt>" --dry-run` and score output.

### TUI Visual (via Peekaboo)
Launch app, interact via peekaboo, capture screenshots, score.

### API
curl/httpie against endpoints, score response correctness.

### Unit Tests
Run test suite — pass/fail gate, not scored.
-->

## Scoring
0-10 per scenario. Overall = average. Target: 9.0+

## Known Issues (starting state)
<!-- List the bugs/issues identified in initial eval. These are the first targets. -->
PROGRAM

# --- scenarios.yaml ---
cat > "$EVAL_DIR/scenarios.yaml" << 'SCENARIOS'
# Eval Scenarios
# Each scenario defines a real use case, method, and scoring criteria.

scenarios:

  # - id: example-scenario
  #   name: "Human-readable description"
  #   method: cli-oneshot | tui | tui-visual | api | unit-test
  #   prompt: "exact input to test"
  #   steps:                      # for multi-step tui-visual
  #     - launch
  #     - type: "input"
  #     - wait: 5
  #     - screenshot
  #   expected:
  #     key: value
  #   cleanup: "path/to/remove"   # optional
  #   weight: 1-3                 # priority (3 = highest)
SCENARIOS

# --- experiments.md ---
cat > "$EVAL_DIR/experiments.md" << 'EXPERIMENTS'
# Eval Experiments Log

Append-only. Each cycle logs: type, scores, fix attempted, result, commit hash or revert reason.
EXPERIMENTS

echo "✓ Scaffolded $EVAL_DIR/"
echo "  program.md       — fill in project-specific sections"
echo "  scenarios.yaml   — add real scenarios"
echo "  experiments.md   — empty, ready for cycles"
