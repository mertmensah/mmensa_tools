from __future__ import annotations

from html import escape
from pathlib import Path
from typing import Sequence

from .types import DeckSection, DeckSlide, DeckTheme


def _render_section(section: DeckSection) -> str:
    bullets = "".join(f"<li>{escape(item)}</li>" for item in section.bullets)
    body = f"<p>{escape(section.body)}</p>" if section.body else ""
    bullet_block = f"<ul>{bullets}</ul>" if bullets else ""
    return (
        '<section class="deck-section">'
        f"<h3>{escape(section.heading)}</h3>"
        f"{body}"
        f"{bullet_block}"
        "</section>"
    )


def _render_slide(slide: DeckSlide, index: int, total: int) -> str:
    eyebrow = f'<p class="eyebrow">{escape(slide.eyebrow)}</p>' if slide.eyebrow else ""
    subtitle = f'<p class="subtitle">{escape(slide.subtitle)}</p>' if slide.subtitle else ""
    bullets = "".join(f"<li>{escape(item)}</li>" for item in slide.bullets)
    bullet_block = f'<ul class="bullets">{bullets}</ul>' if bullets else ""
    sections = "".join(_render_section(section) for section in slide.sections)
    notes = f'<p class="notes">{escape(slide.notes)}</p>' if slide.notes else ""
    kicker = f'<p class="kicker">{escape(slide.kicker)}</p>' if slide.kicker else ""
    return (
        f'<article class="slide" data-slide-index="{index}">'
        '<div class="slide-panel">'
        f"{eyebrow}"
        f"<h2>{escape(slide.title)}</h2>"
        f"{subtitle}"
        f"{bullet_block}"
        f'<div class="sections">{sections}</div>'
        f"{notes}"
        f"{kicker}"
        f'<div class="slide-progress">{index + 1} / {total}</div>'
        "</div>"
        "</article>"
    )


def build_slide_deck(slides: Sequence[DeckSlide], *, title: str = "Deck", theme: DeckTheme | None = None) -> str:
    if not slides:
        raise ValueError("At least one slide is required")

    selected = theme or DeckTheme(title=title)
    slide_markup = "".join(_render_slide(slide, index, len(slides)) for index, slide in enumerate(slides))

    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{escape(title)}</title>
  <style>
    :root {{
      --font-display: {selected.font_display};
      --font-body: {selected.font_body};
      --bg-top: {selected.background_top};
      --bg-bottom: {selected.background_bottom};
      --panel: {selected.panel};
      --text: {selected.text};
      --muted: {selected.muted};
      --accent: {selected.accent};
      --accent-soft: {selected.accent_soft};
      --line: {selected.line};
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: var(--font-body);
      color: var(--text);
      background:
        radial-gradient(circle at 10% 12%, #ffffff 0, var(--accent-soft) 28%, transparent 55%),
        linear-gradient(180deg, var(--bg-top), var(--bg-bottom));
      min-height: 100vh;
      overflow: hidden;
    }}
    .deck-shell {{ min-height: 100vh; display: grid; grid-template-rows: auto 1fr auto; }}
    .deck-header, .deck-footer {{ padding: 18px 28px; }}
    .deck-header {{ display: flex; justify-content: space-between; align-items: end; gap: 16px; }}
    .deck-header h1 {{ margin: 0; font-family: var(--font-display); font-size: 1.8rem; font-weight: 800; }}
    .deck-header p {{ margin: 4px 0 0; color: var(--muted); }}
    .deck-stage {{ position: relative; overflow: hidden; }}
    .slides {{ height: 100%; display: flex; transition: transform 260ms ease; }}
    .slide {{ min-width: 100%; padding: 18px 28px 28px; display: grid; place-items: center; }}
    .slide-panel {{
      width: min(1120px, 100%);
      min-height: min(76vh, 760px);
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 28px;
      box-shadow: 0 18px 42px rgba(56, 95, 131, 0.16);
      padding: 32px;
      display: grid;
      gap: 18px;
      align-content: start;
    }}
    .eyebrow {{ margin: 0; color: var(--accent); text-transform: uppercase; letter-spacing: 0.14em; font-size: 0.76rem; font-weight: 800; }}
    h2 {{ margin: 0; font-family: var(--font-display); font-size: clamp(2rem, 4vw, 3.6rem); line-height: 1.05; font-weight: 800; }}
    .subtitle {{ margin: 0; font-size: 1.05rem; color: var(--muted); max-width: 70ch; }}
    .bullets {{ margin: 0; padding-left: 1.2rem; display: grid; gap: 10px; font-size: 1.04rem; }}
    .sections {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; }}
    .deck-section {{ background: #ffffff; border: 1px solid var(--line); border-radius: 18px; padding: 18px; }}
    .deck-section h3 {{ margin: 0 0 8px; font-size: 1.1rem; font-family: var(--font-display); font-weight: 800; }}
    .deck-section p {{ margin: 0 0 10px; color: var(--muted); }}
    .deck-section ul {{ margin: 0; padding-left: 1rem; display: grid; gap: 8px; }}
    .notes, .kicker, .slide-progress {{ margin: 0; color: var(--muted); }}
    .kicker {{ font-weight: 700; color: var(--accent); }}
    .slide-progress {{ margin-top: auto; justify-self: end; font-size: 0.95rem; }}
    .deck-footer {{ display: flex; justify-content: space-between; align-items: center; color: var(--muted); }}
    .nav-hint {{ font-size: 0.95rem; }}
    .nav-buttons {{ display: flex; gap: 8px; }}
    button {{
      border: 1px solid var(--line);
      border-radius: 999px;
      background: white;
      color: var(--text);
      padding: 10px 14px;
      font: inherit;
      font-weight: 700;
      cursor: pointer;
    }}
    button:hover {{ border-color: var(--accent); }}
    @media (max-width: 720px) {{
      .slide-panel {{ padding: 22px; min-height: auto; }}
      .deck-header, .deck-footer, .slide {{ padding-left: 16px; padding-right: 16px; }}
    }}
  </style>
</head>
<body>
  <div class=\"deck-shell\">
    <header class=\"deck-header\">
      <div>
        <h1>{escape(selected.title)}</h1>
        <p>{escape(selected.subtitle or title)}</p>
      </div>
      <div class=\"nav-buttons\">
        <button type=\"button\" id=\"prevBtn\">Previous</button>
        <button type=\"button\" id=\"nextBtn\">Next</button>
      </div>
    </header>
    <main class=\"deck-stage\">
      <div class=\"slides\" id=\"slides\">{slide_markup}</div>
    </main>
    <footer class=\"deck-footer\">
      <span class=\"nav-hint\">Use click, previous/next buttons, or keyboard arrow keys.</span>
      <span id=\"footerIndex\">1 / {len(slides)}</span>
    </footer>
  </div>
  <script>
    const slidesEl = document.getElementById('slides');
    const footerIndexEl = document.getElementById('footerIndex');
    const slideCount = {len(slides)};
    let currentIndex = 0;

    function render() {{
      slidesEl.style.transform = `translateX(${{-currentIndex * 100}}%)`;
      footerIndexEl.textContent = `${{currentIndex + 1}} / ${{slideCount}}`;
    }}

    function nextSlide() {{
      currentIndex = Math.min(currentIndex + 1, slideCount - 1);
      render();
    }}

    function prevSlide() {{
      currentIndex = Math.max(currentIndex - 1, 0);
      render();
    }}

    document.getElementById('nextBtn').addEventListener('click', nextSlide);
    document.getElementById('prevBtn').addEventListener('click', prevSlide);
    document.addEventListener('keydown', (event) => {{
      if (event.key === 'ArrowRight' || event.key === 'PageDown' || event.key === ' ') nextSlide();
      if (event.key === 'ArrowLeft' || event.key === 'PageUp') prevSlide();
    }});
    slidesEl.addEventListener('click', (event) => {{
      const half = window.innerWidth / 2;
      if (event.clientX > half) nextSlide(); else prevSlide();
    }});
    render();
  </script>
</body>
</html>
"""


def write_slide_deck(slides: Sequence[DeckSlide], *, output_path: str | Path, title: str = "Deck", theme: DeckTheme | None = None) -> Path:
    output = Path(output_path)
    output.write_text(build_slide_deck(slides, title=title, theme=theme), encoding="utf-8")
    return output
