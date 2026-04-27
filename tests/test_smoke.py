from mertmensah import DeckSlide, build_slide_deck


def test_build_slide_deck_contains_title() -> None:
    html = build_slide_deck([DeckSlide(title="Test Slide")], title="Demo Deck")
    assert "Demo Deck" in html
    assert "Test Slide" in html
