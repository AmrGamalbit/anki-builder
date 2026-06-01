from fastapi import APIRouter
from models.requests import AppearanceOptions
import textwrap
import re

router = APIRouter()

OVERRIDE_DELIMITER = "\n/* === USER OVERRIDES === */\n"


def format_value(k, v):
    if k == "padding" or k == "font_size":
        return f"{v}px"
    return v


def parse_card_css(css):
    match = re.search(r"\.card\s*\{([^}]+)\}", css)
    if not match:
        return {}
    props = match.group(1).strip().split("\n")
    return {
        k.strip().replace("-", "_"): v.split("px")[0].strip()
        for line in props
        if ":" in line
        for k, v in [line.strip().rstrip(";").split(":", 1)]
    }


def write_card_overrides(overrides: dict):
    with open("config/card.css") as f:
        content = f.read()
    base = content.split(OVERRIDE_DELIMITER)[0]
    is_night_mode = overrides.pop("night_mode", False)
    night_css = ""
    if is_night_mode:
        night_css = textwrap.dedent("""
        .card.night_mode {
          background-color: #1e1e1e;
          color: #e8e8e8;
        }
        """)
    props = "\n  ".join(
        f"{k.replace('_', '-')}: {format_value(k, v)};" for k, v in overrides.items()
    )
    highlight_css = f"color: {overrides['accent_color']};"
    with open("config/card.css", "w") as f:
        f.write(
            base
            + OVERRIDE_DELIMITER
            + ".card {\n"
            + props
            + "\n}"
            + night_css
            + ".highlight {\n"
            + highlight_css
            + "\n}"
        )


def get_card_overrides():
    with open("config/card.css") as f:
        content = f.read()
    return parse_card_css(content)


@router.get("/styles")
def get_styles():
    return get_card_overrides()


@router.post("/styles")
def update_styles(data: AppearanceOptions):
    write_card_overrides(data.model_dump())
    return "Updated"
