from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


@dataclass(slots=True)
class MertTheme:
    palette: tuple[str, ...] = (
        "#2f6fb1",
        "#68a8df",
        "#93c5eb",
        "#204b73",
        "#5f87a8",
        "#8bbce3",
    )
    font_display: str = "Aptos Display"
    font_body: str = "Aptos"
    text_color: str = "#17314a"
    muted_text: str = "#466786"
    grid_color: str = "#d8e7f5"
    face_color: str = "#ffffff"
    figure_face_color: str = "#f7fbff"
    line_color: str = "#cfe1f2"
    accent_color: str = "#2f6fb1"
    title_weight: str = "bold"
    label_weight: str = "bold"
    context: str = "talk"
    rc_overrides: dict[str, object] = field(default_factory=dict)


def get_palette(theme: MertTheme | None = None) -> list[str]:
    selected = theme or MertTheme()
    return list(selected.palette)


def apply_mert_theme(theme: MertTheme | None = None) -> MertTheme:
    selected = theme or MertTheme()
    plt.rcParams.update(
        {
            "figure.facecolor": selected.figure_face_color,
            "axes.facecolor": selected.face_color,
            "axes.edgecolor": selected.line_color,
            "axes.labelcolor": selected.text_color,
            "axes.titlecolor": selected.text_color,
            "axes.titleweight": selected.title_weight,
            "axes.labelweight": selected.label_weight,
            "axes.grid": True,
            "grid.color": selected.grid_color,
            "grid.linestyle": "-",
            "grid.linewidth": 0.8,
            "font.family": "sans-serif",
            "font.sans-serif": [selected.font_body, "Aptos Display", "Segoe UI", "Arial", "sans-serif"],
            "text.color": selected.text_color,
            "xtick.color": selected.muted_text,
            "ytick.color": selected.muted_text,
            "legend.frameon": False,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.spines.left": True,
            "axes.spines.bottom": True,
        }
    )
    if selected.rc_overrides:
        plt.rcParams.update(selected.rc_overrides)
    return selected


def make_figure(
    *,
    width: float = 10,
    height: float = 6,
    nrows: int = 1,
    ncols: int = 1,
    sharex: bool = False,
    sharey: bool = False,
    theme: MertTheme | None = None,
) -> tuple[Figure, Axes | Iterable[Axes]]:
    apply_mert_theme(theme)
    return plt.subplots(nrows=nrows, ncols=ncols, figsize=(width, height), sharex=sharex, sharey=sharey)
