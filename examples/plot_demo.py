from pathlib import Path

import pandas as pd

from mertmensah import add_source_note, apply_mert_theme, barplot

OUTPUT_DIR = Path(__file__).resolve().parent


def main() -> None:
    apply_mert_theme()
    data = pd.DataFrame(
        {
            "team": ["North", "South", "West", "East"],
            "growth": [14, 9, 17, 12],
        }
    )
    ax = barplot(data, x="team", y="growth", title="Regional Growth", subtitle="Year-over-year percentage change")
    add_source_note(ax, "Source: Internal planning data")
    ax.figure.savefig(OUTPUT_DIR / "regional_growth.png", dpi=160, bbox_inches="tight")


if __name__ == "__main__":
    main()
