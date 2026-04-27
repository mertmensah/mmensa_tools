from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence


@dataclass(slots=True)
class DeckSection:
    heading: str
    body: str | None = None
    bullets: Sequence[str] = field(default_factory=tuple)


@dataclass(slots=True)
class DeckSlide:
    title: str
    eyebrow: str | None = None
    subtitle: str | None = None
    bullets: Sequence[str] = field(default_factory=tuple)
    sections: Sequence[DeckSection] = field(default_factory=tuple)
    notes: str | None = None
    kicker: str | None = None


@dataclass(slots=True)
class DeckTheme:
    title: str = "Mert Mensah Deck"
    subtitle: str | None = None
    font_display: str = 'Aptos Display, Aptos, "Segoe UI", sans-serif'
    font_body: str = 'Aptos, "Segoe UI", sans-serif'
    background_top: str = "#f7fbff"
    background_bottom: str = "#e8f2ff"
    panel: str = "rgba(255,255,255,0.9)"
    text: str = "#17314a"
    muted: str = "#466786"
    accent: str = "#2f6fb1"
    accent_soft: str = "#d8ecff"
    line: str = "#cfe1f2"
