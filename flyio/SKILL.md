---
name: flyio
description: Manage Fly.io apps using the flyctl CLI — deploy, scale, monitor, manage secrets, SSH, volumes, and networking. Use when the user asks about deploying to Fly, checking Fly app status, viewing Fly logs, managing Fly secrets/env vars, scaling Fly machines, SSH into Fly machines, managing Fly volumes, or any Fly.io infrastructure task. Triggers on mentions of Fly.io, fly deploy, fly status, fly logs, fly secrets, fly scale, or flyctl.
---

# Fly.io CLI

## Prerequisites
- `fly` CLI installed and authenticated (`fly auth login`)
- App config lives in `fly.toml` at repo root

## Quick Reference

For full CLI commands and `fly.toml` config format, read `references/cli-reference.md`.

## Key Workflows

### Deploy
```bash
fly deploy              # Build + deploy from current directory
fly status              # Verify deployment health
fly logs --no-tail      # Check recent logs for errors
```

### Secrets Management
Secrets become ENV vars at runtime. Setting/unsetting triggers a redeploy unless `--stage` is used.
```bash
fly secrets set KEY=VALUE           # Set + redeploy
fly secrets set KEY=VALUE --stage   # Stage only
fly secrets deploy                  # Deploy all staged secrets
fly secrets import < .env           # Bulk import
fly secrets list                    # List names (never shows values)
```

### Debugging a Failed Deploy
1. `fly status` — check machine state and health checks
2. `fly logs` — stream logs for errors
3. `fly releases` — check recent release history
4. `fly ssh console -C "command"` — run diagnostics on the machine

### Scaling
```bash
fly scale show                      # Current size/count
fly scale count 1                   # Single machine (avoid split-brain)
fly scale vm shared-cpu-1x          # Change VM size
fly scale memory 1024               # Set memory in MB
```

## Gotchas
- `fly secrets set` triggers an immediate redeploy. Use `--stage` + `fly secrets deploy` to batch changes.
- `auto_stop_machines = "suspend"` means machines sleep when idle — first request after sleep has cold-start latency.
- Volumes are region-locked. A machine can only mount a volume in the same region.
- `fly deploy` builds remotely by default. Use `--local-only` to build on your machine.
- Health check path in `fly.toml` must return 200 or the deploy will fail/roll back.
