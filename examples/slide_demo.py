from pathlib import Path

from mertmensah import DeckSection, DeckSlide, DeckTheme, write_slide_deck

OUTPUT_DIR = Path(__file__).resolve().parent


def main() -> None:
    slides = [
        DeckSlide(
            eyebrow="Quarterly Review",
            title="Commercial Performance",
            subtitle="A concise browser-viewable deck generated from Python.",
            bullets=[
                "Revenue and operating margin both improved.",
                "The strongest region was West.",
                "Next focus is client retention and expansion.",
            ],
            kicker="Recommendation: keep this structure for internal briefings.",
        ),
        DeckSlide(
            eyebrow="Key Takeaways",
            title="What Matters Most",
            sections=[
                DeckSection(
                    heading="Growth",
                    body="Pipeline quality and conversion improved in the second half.",
                    bullets=["Revenue up 18%", "Margin up 3.4 pts"],
                ),
                DeckSection(
                    heading="Actions",
                    bullets=["Prioritize enterprise renewals", "Expand high-performing playbooks"],
                ),
            ],
            notes="Use left/right arrow keys to navigate.",
        ),
    ]

    write_slide_deck(
        slides,
        output_path=OUTPUT_DIR / "quarterly_review.html",
        title="Quarterly Review",
        theme=DeckTheme(title="Quarterly Review", subtitle="Mert Mensah reference deck"),
    )


if __name__ == "__main__":
    main()
