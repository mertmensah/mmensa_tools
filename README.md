# mertmensah

[Open the live reference site](https://mertmensah.github.io/mmensa_tools/)

A personal style reference toolkit for work artifacts.

This package gives you two things:

- A consistent presentation-quality plotting style for `matplotlib`, `pandas`, `numpy`, and `seaborn`
- A simple HTML slide-deck generator for browser-viewable presentations with click and keyboard navigation

## Install

```bash
pip install -e .
```

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

## Examples

See `examples/` for a plot demo and slide-deck demo.

## Reference Site

A GitHub Pages frontend for browsing chart and slide-deck reference patterns lives under `docs/` and is published at https://mertmensah.github.io/mmensa_tools/.
