# Agent Wrappers

The core skill is portable. Use these environment-specific behaviours only when they match the active agent.

## Native Codex

- Save the `.html` file inside the current repo when the diagram documents repo work.
- Save beside the requested source artifact when the user gives a specific file or folder.
- Use local browser/screenshot tooling when available to verify layout.
- Return the file path and a short description of what the diagram contains.

## OpenClaw

- Prefer project/artifact locations over random Desktop output.
- For durable knowledge, save diagrams under the relevant project folder in Second Brain or the current code repo.
- For chat sharing, return a shareable path or media attachment when available.
- Keep the canonical skill source in the agent-skills repo.
- If the OpenClaw skill loader rejects symlinks that leave its skill directory, install a real copied folder instead.
