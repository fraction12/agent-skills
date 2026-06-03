#!/usr/bin/env python3
"""Template for compact ML-paper-style multi-panel Matplotlib figures."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


PALETTE = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "red": "#D55E00",
    "purple": "#CC79A7",
    "gray": "#666666",
}


def configure_matplotlib() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8,
            "axes.titlesize": 9,
            "axes.labelsize": 8,
            "legend.fontsize": 8,
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
        }
    )


def save_all(fig: plt.Figure, output_stem: Path) -> None:
    output_stem.parent.mkdir(parents=True, exist_ok=True)
    for suffix in ("svg", "pdf", "png"):
        fig.savefig(output_stem.with_suffix(f".{suffix}"), bbox_inches="tight", pad_inches=0.02)


def demo(output_stem: Path) -> None:
    configure_matplotlib()

    x = np.linspace(0, 120, 121)
    models = ["Model-A", "Model-B", "Model-C", "Model-D"]
    methods = [
        ("Dense Attention", PALETTE["blue"], "-"),
        ("Window Attention", PALETTE["orange"], "-"),
        ("StreamingLLM", PALETTE["red"], "-"),
    ]

    fig, axes = plt.subplots(
        1,
        4,
        figsize=(10.8, 2.35),
        sharex=True,
        sharey=True,
        constrained_layout=False,
    )
    fig.subplots_adjust(left=0.06, right=0.995, bottom=0.24, top=0.78, wspace=0.2)

    handles = []
    for idx, (ax, model) in enumerate(zip(axes, models)):
        ax.set_title(model, pad=2)
        for method_idx, (method, color, linestyle) in enumerate(methods):
            y = 0.82 - 0.1 * method_idx + 0.04 * np.sin((x + idx * 9) / (8 + method_idx))
            if method == "Window Attention":
                y = np.where(x > 5, 0.0, y)
            if method == "Dense Attention":
                y = np.where(x > 18 + idx * 5, np.nan, y)
            line = ax.plot(x, y, label=method, color=color, linestyle=linestyle, linewidth=1.4)[0]
            if idx == 0:
                handles.append(line)

        for xpos, label in [(18, "KV Cache Size"), (35, "Pre-training Length")]:
            ax.axvline(xpos, color="#333333", linestyle="--", linewidth=0.8)
            ax.text(xpos + 1.5, 0.98, label, rotation=90, va="top", ha="left", fontsize=7)

        ax.set_xlim(0, 120)
        ax.set_ylim(0, 1.0)
        ax.set_xticks([0, 30, 60, 90, 120])
        ax.set_xticklabels(["0K", "30K", "60K", "90K", "120K"])
        if idx == 0:
            ax.set_ylabel("Accuracy")
        ax.set_xlabel("Input Length")

    fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.985))
    save_all(fig, output_stem)


def main() -> int:
    demo(Path("figures/paper-style-demo"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
