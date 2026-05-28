# HTML Diagram Primitives

Use these primitives before inventing new structure.

## Page

- `.diagram-page`: outer width and page padding
- `.diagram-header`: title block
- `.diagram-canvas`: bordered diagram surface
- `.diagram-grid`: inner layout grid

## Nodes

Use `.node` for every meaningful concept, actor, system, state, or step.

Recommended node shape:

```html
<article class="node">
  <h2 class="node-title">Intake Router</h2>
  <p class="node-text">Classifies work by risk, tools, and model need.</p>
  <div class="node-meta">
    <span class="badge blue">classification</span>
    <span class="badge amber">cost control</span>
  </div>
</article>
```

## Lanes

Use lanes when ownership, phase, time, or execution layer matters.

```html
<section class="diagram-grid diagram-lanes">
  <div class="lane-label">User</div>
  <div class="lane-track">
    <article class="node">...</article>
  </div>
</section>
```

## Clusters

Use `.cluster` to group related nodes without making nested cards look heavy.

Good cluster labels:

- Human layer
- Agent layer
- Data plane
- Risk controls
- External systems

## Badges

Use badges only for compact state or category metadata.

Color meanings by default:

- `blue`: routing, information, coordination
- `green`: completed, approved, safe, durable
- `amber`: review, cost, caution, manual handoff
- `red`: blocked, risky, destructive, external side effect
- `purple`: model, intelligence, synthesis

Include a legend if colors carry meaning.

## Connectors

Prefer CSS grid and reading order first. Add inline SVG connectors only when relationships are not obvious.

Use:

- Solid line for primary flow
- Dashed line for optional, fallback, or async flow
- Arrowheads for direction
- Labels only when the relationship is not obvious from node text

Do not draw spaghetti. If more than 8 connectors are needed, split the diagram into sections.

## Callouts

Use `.callout` for the insight, invariant, or warning the diagram exists to explain.

Keep callouts short. They should not become prose dumps.

## Density Rules

- One idea per node
- 3-7 nodes per section where possible
- Use lanes or clusters instead of huge freeform canvases
- Keep labels short enough to scan
- Avoid decorative-only elements
