from __future__ import annotations

from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes

from .theme import MertTheme, apply_mert_theme, get_palette, make_figure


def style_axes(ax: Axes, *, title: str | None = None, subtitle: str | None = None, y_as_percent: bool = False) -> Axes:
    if title:
        ax.set_title(title, loc="left", pad=14, fontsize=17, fontweight="bold")
    if subtitle:
        ax.text(0.0, 1.02, subtitle, transform=ax.transAxes, ha="left", va="bottom", fontsize=10, color="#466786")
    if y_as_percent:
        ax.yaxis.set_major_formatter(lambda value, _pos: f"{value:,.0f}%")
    ax.spines["left"].set_alpha(0.6)
    ax.spines["bottom"].set_alpha(0.6)
    return ax


def add_source_note(ax: Axes, note: str) -> Axes:
    ax.text(1.0, -0.14, note, transform=ax.transAxes, ha="right", va="top", fontsize=9, color="#5f7c98")
    return ax


def lineplot(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    hue: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    marker: str = "o",
    theme: MertTheme | None = None,
    **kwargs: Any,
) -> Axes:
    apply_mert_theme(theme)
    _, ax = make_figure(theme=theme)
    plot_kwargs: dict[str, Any] = {"data": data, "x": x, "y": y, "hue": hue, "marker": marker, "ax": ax, **kwargs}
    if hue:
        plot_kwargs["palette"] = get_palette(theme)
    else:
        plot_kwargs["color"] = get_palette(theme)[0]
    sns.lineplot(**plot_kwargs)
    return style_axes(ax, title=title, subtitle=subtitle)


def barplot(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    hue: str | None = None,
    title: str | None = None,
    subtitle: str | None = None,
    theme: MertTheme | None = None,
    **kwargs: Any,
) -> Axes:
    apply_mert_theme(theme)
    _, ax = make_figure(theme=theme)
    plot_kwargs: dict[str, Any] = {"data": data, "x": x, "y": y, "hue": hue, "ax": ax, **kwargs}
    if hue:
        plot_kwargs["palette"] = get_palette(theme)
    else:
        plot_kwargs["color"] = get_palette(theme)[0]
    sns.barplot(**plot_kwargs)
    return style_axes(ax, title=title, subtitle=subtitle)


def heatmap(
    data: pd.DataFrame,
    *,
    title: str | None = None,
    subtitle: str | None = None,
    annot: bool = True,
    fmt: str = ".1f",
    cmap: str = "Blues",
    theme: MertTheme | None = None,
    **kwargs: Any,
) -> Axes:
    apply_mert_theme(theme)
    _, ax = make_figure(theme=theme)
    sns.heatmap(data, annot=annot, fmt=fmt, cmap=cmap, linewidths=0.5, linecolor="#d8e7f5", cbar=True, ax=ax, **kwargs)
    return style_axes(ax, title=title, subtitle=subtitle)
