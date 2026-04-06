import textwrap

BASE = """
hr {
  border: none;
  border-top: 1px solid #ddd;
  margin: 16px 0;
}

b, strong {
  color: #2563eb;
}

code {
  background: #f3f4f6;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: monospace;
  font-size: 0.9em;
}

.night_mode code {
  background: #2d2d2d;
}
"""


def format_value(k, v):
    if k == "padding" or k == "font_size":
        return f"{v}px"
    return v


def build_css(style: dict) -> str:
    is_night_mode = style.pop("night_mode", False)
    night_css = ""
    if is_night_mode:
        night_css = textwrap.dedent("""
        .card.night_mode {
          background-color: #1e1e1e;
          color: #e8e8e8;
        }
        """)
    rules = "\n  ".join(
        f"{k.replace('_', '-')}: {format_value(k, v)};" for k, v in style.items()
    )
    highlight_css = f"color: {style.get('accent_color')};"
    return (
        BASE
        + ".card {\n"
        + rules
        + "\n}"
        + night_css
        + ".highlight {\n"
        + highlight_css
        + "\n}"
    )
