#!/usr/bin/env python3
"""Create a self-contained HTML diagram skeleton with embedded CSS."""

from __future__ import annotations

import argparse
from datetime import date
from html import escape
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="Output .html path")
    parser.add_argument("--title", default="Diagram")
    parser.add_argument("--kicker", default="HTML Diagram")
    parser.add_argument("--subtitle", default="A portable single-file diagram artifact.")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    css_path = script_dir.parent / "assets" / "diagram.css"
    css = css_path.read_text(encoding="utf-8")

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    title = escape(args.title)
    kicker = escape(args.kicker)
    subtitle = escape(args.subtitle)
    generated = date.today().isoformat()

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
{css}
  </style>
</head>
<body>
  <main class="diagram-page">
    <header class="diagram-header">
      <div class="diagram-kicker">{kicker}</div>
      <h1 class="diagram-title">{title}</h1>
      <p class="diagram-subtitle">{subtitle}</p>
    </header>

    <section class="diagram-canvas" aria-label="{title}">
      <div class="diagram-grid diagram-columns">
        <article class="node">
          <h2 class="node-title">First node</h2>
          <p class="node-text">Replace this with one clear concept, actor, step, or system.</p>
          <div class="node-meta">
            <span class="badge blue">example</span>
          </div>
        </article>
      </div>
      <footer class="legend">
        <span class="legend-item"><span class="legend-swatch"></span> Generated {generated}</span>
      </footer>
    </section>
  </main>
</body>
</html>
"""

    output.write_text(html, encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
