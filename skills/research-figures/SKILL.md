---
name: research-figures
description: Create research-paper-grade figures and charts from benchmark, experiment, CSV/JSON, or paper-context data. Use when the user asks for publication-quality plots, ML-systems paper figures, multi-panel charts, Matplotlib/Seaborn figures, academic plotting, paper-style graphs, figure panels, camera-ready chart exports, or asks to match a provided research-paper chart style.
---

# Research Figures

Create paper figures, not dashboards. Optimize for compact ML/AI systems paper style: multi-panel grids, shared legends, precise axes, small subplot titles, light gridlines, direct data labels only when they do not clutter, and vector outputs.

This skill is adapted from the public `academic-plotting` workflow idea: numerical figures use Matplotlib/Seaborn, diagram figures use a separate diagram workflow, and every figure must be reproducible from data.

## Workflow

1. Define the figure claim in one sentence: what should the reader learn?
2. Inspect the data source and create a compact computed-data table before plotting.
3. Choose the figure type from the data shape:
   - time/step/length axis: line plot
   - methods x benchmarks: grouped bars or multi-panel bars
   - many methods, one metric: horizontal bar
   - matrix: heatmap
   - distributions: violin/box/ECDF
   - multiple models/settings: small multiples with shared axes
4. Read `references/paper-style-guide.md` when matching ML-paper style, making multi-panel figures, or when prior output had overlap.
5. Use Matplotlib's object-oriented API. Avoid stateful one-off plotting unless making a quick scratch plot.
6. Export `svg`, `pdf`, and `png` from the same script.
7. Render a PNG/contact sheet and visually inspect it before final. Check every title, legend, tick, annotation, and panel label.

## Hard Rules

- Never put title, subtitle, legend, or annotations where they can overlap plotted data.
- Reserve physical layout regions: header area, legend area, plot grid, caption/notes area.
- Prefer a shared legend above or below the full panel grid, not repeated legends inside each subplot.
- Use small subplot titles, not large dashboard titles.
- Use consistent y-axis ranges for comparable panels unless a broken/free scale is explicitly justified.
- Use colorblind-safe colors and distinguish lines with style/marker when print readability matters.
- Mark projections, synthetic data, and targets visually differently from measured data.
- Do not use cards, giant KPI panels, decorative backgrounds, gradients, or presentation-dashboard styling for paper figures.
- Do not manually alter plotted values in SVG/PDF after generation.

## Figure QA Checklist

Before finalizing, verify:

- [ ] The figure claim is visible from the chart without reading a long explanation.
- [ ] Legend and title have no overlap with each other or the axes.
- [ ] No tick label collides with another tick, axis label, or panel.
- [ ] Every annotation is inside its reserved area or clearly attached to its data.
- [ ] Axis units are explicit.
- [ ] Fonts are readable at paper scale.
- [ ] PDF/SVG vector outputs exist for LaTeX/paper use.
- [ ] PNG preview was rendered and visually inspected.

## Reusable Resources

- `references/paper-style-guide.md`: ML-paper visual rules, layout patterns, and style tokens.
- `scripts/paper_figure_template.py`: minimal Matplotlib template for multi-panel paper figures with shared legend and no-overlap layout.

When creating repo-specific chart pipelines, copy the structure from the template but keep data loading in the repo script so figures remain reproducible from raw artifacts.
