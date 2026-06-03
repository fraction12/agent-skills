# Paper Style Guide

Use this guide for ML systems, inference, benchmarking, and paper-style experiment figures.

## Target Look

The target style is compact and information-dense:

- light gray axes background
- thin, light gridlines
- small panel titles
- shared legend across the top
- line colors with high contrast
- vertical reference lines for thresholds, cache sizes, context windows, or pre-training lengths
- labels placed close to reference lines, often rotated vertically
- no large dashboard header inside the figure canvas
- no decorative cards, shadows, or gradients

The figure should look like it belongs in an ML paper, not a web dashboard.

## Layout Rules

- Build the figure in inches, not pixels.
- Use `GridSpec`, `subplot_mosaic`, or explicit `fig.add_axes` regions for fragile layouts.
- Reserve top space for the shared legend before creating subplots.
- Keep a consistent left margin for y-axis labels across panels.
- Prefer one y-axis label per row, not per panel, when panels share a metric.
- Use `sharex=True` and `sharey=True` when panels compare the same metric.
- Use `fig.legend(...)` for shared legend; avoid repeating legends in every panel.
- Use `bbox_inches="tight"` only after the layout is already correct. Do not rely on it to rescue overlaps.

## Matplotlib Defaults

Use these as a starting point:

```python
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 160,
    "savefig.dpi": 300,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "axes.facecolor": "#EAEAEA",
    "figure.facecolor": "white",
    "axes.grid": True,
    "grid.color": "#CFCFCF",
    "grid.linewidth": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
})
```

Use a colorblind-safe palette:

```python
PALETTE = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "gray": "#666666",
}
```

## Common ML-Paper Patterns

### Multi-Panel Line Figure

Use when comparing methods across models, datasets, sequence lengths, or context sizes.

- one subplot per model/dataset
- shared x/y axes if possible
- one global legend
- per-panel title like `Llama-2-7b-Chat`
- reference lines for cache boundaries or training length
- no numeric labels on every point unless there are very few points

### Small Multiples With Reference Lines

Use `ax.axvline(...)` with a thin dashed line. Place the label near the line and rotate it:

```python
ax.axvline(cache_size, color="#333333", linestyle="--", linewidth=0.9)
ax.text(cache_size + 0.02 * x_range, y_top * 0.98, "KV Cache Size",
        rotation=90, va="top", ha="left", fontsize=8)
```

### Projection Figures

Measured and projected values must be visually distinct:

- solid line: measured
- dashed line: projection
- dotted line: target or hypothesis
- annotate projection method in caption or side note

Never let a projection look like measured data.

## Visual QA Method

After generating figures:

1. Make a PNG preview for every SVG/PDF.
2. Create a contact sheet when there are multiple charts.
3. Inspect title/legend/axis/annotation collisions.
4. If overlap exists, fix the layout code and regenerate. Do not hand-edit the SVG.
5. Only then update docs or final response.

## Output Files

For each final figure, emit:

- `.svg` for web and editable vector
- `.pdf` for LaTeX/paper submission
- `.png` for preview and quick embedding

Use deterministic file names such as `fig-cache-gains.svg`, not `plot-final-new2.svg`.
