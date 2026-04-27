# mertmensah

[Open the live reference site](https://mertmensah.github.io/mmensa_tools/)

A Python package for two repeatable outputs:

- presentation-style charts built with `matplotlib`, `pandas`, `numpy`, and `seaborn`
- browser-viewable HTML slide decks generated from Python data structures

## For AI Agents

Use this package when you need to add polished charts or standalone HTML decks to an existing Python repo.

The public import surface is:

```python
from mertmensah import (
    MertTheme,
    apply_mert_theme,
    get_palette,
    make_figure,
    lineplot,
    barplot,
    heatmap,
    style_axes,
    add_source_note,
    DeckSlide,
    DeckSection,
    DeckTheme,
    build_slide_deck,
    write_slide_deck,
)
```

Choose the integration path by output type:

1. Need a styled chart image in a local project: call `apply_mert_theme()` once, generate a plot with `lineplot`, `barplot`, or `heatmap`, then save with `ax.figure.savefig(...)`.
2. Need a standalone HTML presentation: create `DeckSlide` and optional `DeckSection` objects, then call `write_slide_deck(...)` to produce an `.html` file.
3. Need lower-level control: call `make_figure(...)` and use `style_axes(...)` and `add_source_note(...)` with raw matplotlib code.

Output behavior:

- Chart helpers return a `matplotlib.axes.Axes`
- `build_slide_deck(...)` returns the full HTML as a string
- `write_slide_deck(...)` writes an HTML file and returns the output path
- The package does not start servers, write config files, or modify host application code on its own

## Install

Use one of these install modes:

```bash
# local editable install while developing in this repo
pip install -e .
```

```bash
# install into another repo directly from GitHub
pip install git+https://github.com/mertmensah/mmensa_tools.git
```

Python requirement: `>=3.10`

Core dependencies installed with the package:

- `matplotlib>=3.8`
- `numpy>=1.26,<2.3`
- `pandas>=2.2`
- `seaborn>=0.13`

## Quick Start

```python
from mertmensah import apply_mert_theme, lineplot, DeckSlide, write_slide_deck
import pandas as pd

apply_mert_theme()

df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar"],
    "revenue": [120, 140, 180],
})

ax = lineplot(df, x="month", y="revenue", title="Revenue Growth")
ax.figure.savefig("revenue.png", dpi=160, bbox_inches="tight")

slides = [
    DeckSlide(
        title="Revenue Growth",
        eyebrow="Q1 Review",
        bullets=[
            "Revenue increased each month.",
            "March closed 50% above January.",
        ],
    )
]
write_slide_deck(slides, output_path="deck.html", title="Quarterly Review")
```

## Fast Integration Recipes

### 1. Add a styled chart to an existing project

```python
from pathlib import Path

import pandas as pd
from mertmensah import apply_mert_theme, lineplot, add_source_note

apply_mert_theme()

df = pd.DataFrame(
    {
        "month": ["Jan", "Feb", "Mar", "Apr"],
        "revenue": [120, 140, 180, 205],
    }
)

ax = lineplot(
    df,
    x="month",
    y="revenue",
    title="Revenue Trend",
    subtitle="Monthly commercial momentum",
)
add_source_note(ax, "Source: internal planning model")

output_dir = Path("artifacts")
output_dir.mkdir(exist_ok=True)
ax.figure.savefig(output_dir / "revenue_trend.png", dpi=160, bbox_inches="tight")
```

### 2. Use raw matplotlib with the package theme

```python
import matplotlib.pyplot as plt
import pandas as pd
from mertmensah import apply_mert_theme, style_axes, add_source_note

apply_mert_theme()

data = pd.Series([18, 21, 24, 29], index=["Q1", "Q2", "Q3", "Q4"])

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data.index, data.values, marker="o", linewidth=2.5, color="#2f6fb1")
style_axes(ax, title="Quarterly Volume", subtitle="Custom matplotlib example")
add_source_note(ax, "Source: internal operations")
```

### 3. Generate an HTML deck and place it in a host repo

```python
from pathlib import Path

from mertmensah import DeckSection, DeckSlide, write_slide_deck

slides = [
    DeckSlide(
        eyebrow="Quarterly Review",
        title="Commercial Performance",
        subtitle="A concise browser-viewable deck.",
        bullets=[
            "Revenue and margin improved.",
            "West region led growth.",
        ],
        sections=[
            DeckSection(
                heading="Implication",
                bullets=["Prioritize renewals", "Scale proven playbooks"],
            )
        ],
    )
]

output_path = Path("reports") / "quarterly_review.html"
output_path.parent.mkdir(parents=True, exist_ok=True)
write_slide_deck(slides, output_path=output_path, title="Quarterly Review")
```

## Implementation Rules

If you are an agent adding this package to another repo, follow this sequence:

1. Install the package into the target environment.
2. Import only from `mertmensah`, not internal module paths, unless you are intentionally modifying this package itself.
3. Decide whether your target output is a chart image or an HTML deck.
4. Write generated files into the host repo’s own output folder such as `artifacts/`, `reports/`, or `docs/`.
5. If the host app needs to serve the output, wire the generated file into that app separately. This package only creates the asset.

## Public API Summary

### Theme and figure helpers

- `MertTheme`: dataclass for palette, fonts, rcParams, and visual defaults
- `apply_mert_theme(theme=None)`: applies the global matplotlib theme and returns the resolved theme
- `get_palette(theme=None)`: returns the active palette as a list of hex colors
- `make_figure(...)`: returns `matplotlib.pyplot.subplots(...)` with the package theme applied

### Chart helpers

- `lineplot(data, x=..., y=..., ...)`: seaborn line chart with package styling
- `barplot(data, x=..., y=..., ...)`: seaborn bar chart with package styling
- `heatmap(data, ...)`: seaborn heatmap with package styling
- `style_axes(ax, ...)`: apply title, subtitle, and percent-formatting polish to an axis
- `add_source_note(ax, note)`: place a source note below the chart

### Slide helpers

- `DeckSlide`: slide dataclass with title, eyebrow, subtitle, bullets, sections, notes, and kicker
- `DeckSection`: section dataclass with heading, optional body, and bullets
- `DeckTheme`: deck theme dataclass for fonts and colors
- `build_slide_deck(slides, title=..., theme=None)`: returns complete HTML
- `write_slide_deck(slides, output_path=..., title=..., theme=None)`: writes HTML to disk

## Design Direction

The default theme matches the visual preferences established in recent Mert projects:

- Light blue-white atmosphere
- Aptos-first typography
- Strong bold hierarchy for titles and callouts
- Clean analytical surfaces with presentation-ready spacing

## Modules

- `mertmensah.theme`: palette, rcParams, style helpers
- `mertmensah.plots`: chart helpers and annotation utilities
- `mertmensah.slides`: standalone HTML slide deck generation
- `mertmensah.types`: shared typed data structures

## Repository Layout

- `src/mertmensah/`: package source
- `examples/`: runnable demo scripts
- `tests/`: smoke coverage
- `docs/`: static gallery for browsing styles and snippets

## Examples

See `examples/` for a plot demo and slide-deck demo.

## Reference Site

A GitHub Pages frontend for browsing chart and slide-deck reference patterns lives under `docs/` and is published at https://mertmensah.github.io/mmensa_tools/.
