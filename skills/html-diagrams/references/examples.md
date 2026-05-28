# HTML Diagram Examples

Use these patterns as starting points.

## System Map

Best for architecture, agent stacks, platform maps, or data flow.

Structure:

- Header explains the system boundary
- Columns for actors, orchestration, storage, and external services
- Clusters for subsystems
- Connectors for the 3-5 most important relationships only

## Workflow

Best for repeatable processes.

Structure:

- Horizontal sequence on desktop
- Vertical flow on mobile
- Each node is a step with owner, input, and output
- Badges indicate automatic, human review, or external action

## Swimlane

Best when multiple roles or execution layers interact.

Structure:

- Lanes for user, agent, worker, system, external service
- Tracks contain steps in rough time order
- Dashed connectors for async handoff or fallback

## Timeline

Best for roadmaps, histories, launch plans, or incident narratives.

Structure:

- Time buckets as lanes or columns
- Nodes include date/time, event, consequence
- Callout captures the pattern or lesson

## Comparison Map

Best for strategy, vendor choice, model choice, or tradeoff explanation.

Structure:

- Columns for options
- Rows for criteria
- Badges for strengths, risks, and unknowns
- Callout gives the recommended choice and why

## Minimal Single-File Skeleton

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Diagram Title</title>
  <style>
    /* Embed assets/diagram.css here. */
  </style>
</head>
<body>
  <main class="diagram-page">
    <header class="diagram-header">
      <div class="diagram-kicker">System Map</div>
      <h1 class="diagram-title">Diagram Title</h1>
      <p class="diagram-subtitle">One sentence describing the boundary and purpose.</p>
    </header>

    <section class="diagram-canvas" aria-label="Diagram Title">
      <div class="diagram-grid diagram-columns">
        <article class="node">
          <h2 class="node-title">Node title</h2>
          <p class="node-text">Node description.</p>
          <div class="node-meta">
            <span class="badge blue">type</span>
          </div>
        </article>
      </div>
      <footer class="legend">
        <span class="legend-item"><span class="legend-swatch"></span> Legend item</span>
      </footer>
    </section>
  </main>
</body>
</html>
```
