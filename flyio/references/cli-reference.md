# Fly.io CLI Reference

Full docs: https://fly.io/docs/flyctl/

## Core Commands

### Apps
```bash
fly apps list                          # List all apps
fly apps create <name>                 # Create app without deploying
fly apps destroy <name>                # Delete an app (destructive)
fly apps move <name> --org <org>       # Move app between orgs
```

### Deploy
```bash
fly deploy                             # Deploy from current dir (uses fly.toml)
fly deploy --app <name>                # Deploy specific app
fly deploy --image <image>             # Deploy from Docker image
fly deploy --local-only                # Build locally (default is remote)
fly deploy --build-only                # Build but don't deploy
fly deploy --detach                    # Return immediately, don't wait
fly deploy --now                       # Skip confirmation
fly deploy -e KEY=VAL                  # Set env var for this deploy
fly deploy --build-arg KEY=VAL         # Set Docker build arg
fly deploy --strategy rolling          # Deployment strategy: rolling, immediate, canary, bluegreen
fly deploy --max-unavailable 0.33      # Max unavailable during rolling (0-1 = percent)
fly deploy --wait-timeout 120          # Seconds to wait for health checks
```

### Status & Monitoring
```bash
fly status                             # App status, machines, regions
fly status -a <name>                   # Status for specific app
fly status --json                      # JSON output
fly status --watch                     # Live refresh
fly logs                               # Stream logs (continuous)
fly logs --no-tail                     # Fetch buffered logs only
fly logs -a <name>                     # Logs for specific app
fly logs --region <region>             # Filter by region
fly logs --machine <id>                # Filter by machine
fly logs --json                        # JSON output
fly releases                           # List releases
fly releases -a <name>                 # Releases for specific app
```

### Secrets (env vars at runtime)
```bash
fly secrets list                       # List secret names (not values)
fly secrets set KEY=VALUE              # Set secret (triggers redeploy)
fly secrets set K1=V1 K2=V2            # Set multiple
fly secrets set KEY=VALUE --detach     # Set without waiting for deploy
fly secrets set KEY=VALUE --stage      # Stage without redeploying
fly secrets deploy                     # Deploy staged secrets
fly secrets unset KEY                  # Remove secret (triggers redeploy)
fly secrets import < .env              # Import from stdin/file
```

### Scaling
```bash
fly scale show                         # Show current VM size/count
fly scale vm shared-cpu-1x             # Change VM size
fly scale vm performance-1x            # Larger VM
fly scale memory 512                   # Set memory (MB)
fly scale count 2                      # Set machine count
fly scale count 1                      # Scale to single machine
```

### SSH & Remote Access
```bash
fly ssh console                        # SSH into running machine
fly ssh console -a <name>              # SSH into specific app
fly ssh console -C "command"           # Run command and exit
fly ssh sftp get /path/file ./local    # Download file
fly ssh sftp put ./local /path/file    # Upload file (if writable)
```

### Volumes (persistent storage)
```bash
fly volumes list                       # List volumes
fly volumes create <name> --size 1     # Create volume (GB)
fly volumes create <name> -r <region>  # In specific region
fly volumes extend <id> --size 5       # Resize volume
fly volumes destroy <id>               # Delete volume
fly volumes show <id>                  # Volume details
fly volumes snapshots list <id>        # List snapshots
```

### Networking
```bash
fly ips list                           # List allocated IPs
fly ips allocate-v4                    # Allocate shared IPv4
fly ips allocate-v6                    # Allocate IPv6
fly ips release <ip>                   # Release IP
fly certs list                         # List TLS certificates
fly certs add <hostname>               # Add custom domain cert
fly certs show <hostname>              # Cert status/details
```

### Machines (low-level)
```bash
fly machine list                       # List machines
fly machine status <id>                # Machine details
fly machine start <id>                 # Start stopped machine
fly machine stop <id>                  # Stop running machine
fly machine destroy <id>               # Delete machine
fly machine run <image>                # Run a one-off machine
```

### Config
```bash
fly config show                        # Show current fly.toml config
fly config save                        # Save current config to fly.toml
fly config validate                    # Validate fly.toml
```

## Global Options (available on all commands)
```
-a, --app <name>        Target app name
-c, --config <path>     Path to fly.toml
-t, --access-token      API token (for CI/scripts)
    --json              JSON output (where supported)
    --verbose           Verbose output
    --debug             Debug output
```

## fly.toml Key Sections
```toml
app = "my-app"
primary_region = "iad"

[build]
  # dockerfile = "Dockerfile"
  # image = "registry/image:tag"

[env]
  KEY = "value"                 # Non-secret env vars

[http_service]
  internal_port = 8000
  force_https = true
  auto_stop_machines = "suspend"  # stop | suspend | off
  auto_start_machines = true
  min_machines_running = 0

[checks]
  [checks.health]
    type = "http"
    port = 8000
    path = "/api/health"
    interval = "30s"
    timeout = "10s"

[[vm]]
  size = "shared-cpu-1x"
  memory = "512mb"

[[mounts]]
  source = "data"
  destination = "/data"
```
