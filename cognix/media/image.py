import json
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont


def get_font(size, bold=False):
    """Safely loads cross-platform system fonts with fallbacks."""
    font_names = [
        "Arial Bold.ttf" if bold else "Arial.ttf",
        "arialbd.ttf" if bold else "arial.ttf",
        "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf",
    ]
    font_dirs = [
        "/System/Library/Fonts/Supplemental/",
        "/Library/Fonts/",
        "C:\\Windows\\Fonts\\",
        "/usr/share/fonts/truetype/dejavu/",
        "/usr/share/fonts/truetype/msttcorefonts/",
    ]

    for directory in font_dirs:
        for name in font_names:
            path = os.path.join(directory, name)
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def render_header(draw, el, theme):
    x = el.get("x", 80)
    y = el.get("y", 80)
    title = el.get("title", "")
    subtitle = el.get("subtitle", "")

    draw.text(
        (x, y),
        title,
        font=get_font(42, bold=True),
        fill=theme.get("text", "#FFFFFF"),
    )
    if subtitle:
        draw.text(
            (x, y + 55),
            subtitle,
            font=get_font(18),
            fill=theme.get("muted", "#A4B0BE"),
        )


def render_stat_grid(draw, el, theme, canvas_width):
    x = el.get("x", 80)
    y = el.get("y", 200)
    columns = el.get("columns", 3)
    items = el.get("items", [])

    col_width = (canvas_width - (x * 2) - ((columns - 1) * 20)) // columns
    card_height = 130

    for i, item in enumerate(items):
        col_idx = i % columns
        row_idx = i // columns

        cx = x + col_idx * (col_width + 20)
        cy = y + row_idx * (card_height + 20)

        # Draw Card Background
        draw.rounded_rectangle(
            (cx, cy, cx + col_width, cy + card_height),
            radius=14,
            fill=theme.get("card_bg", "#1E1E2F"),
            outline=theme.get("primary", "#6C5CE7"),
            width=2,
        )

        # Text content
        draw.text(
            (cx + 24, cy + 20),
            item.get("label", "").upper(),
            font=get_font(13, bold=True),
            fill=theme.get("muted", "#A4B0BE"),
        )
        draw.text(
            (cx + 24, cy + 48),
            item.get("value", ""),
            font=get_font(32, bold=True),
            fill=theme.get("text", "#FFFFFF"),
        )

        change = item.get("change")
        if change:
            draw.text(
                (cx + 24, cy + 92),
                change,
                font=get_font(14, bold=True),
                fill=theme.get("secondary", "#00CEC9"),
            )


def render_card_list(draw, el, theme, canvas_width):
    x = el.get("x", 80)
    y = el.get("y", 400)
    width = el.get("width", canvas_width - (x * 2))
    items = el.get("items", [])

    current_y = y
    for item in items:
        draw.rounded_rectangle(
            (x, current_y, x + width, current_y + 85),
            radius=12,
            fill=theme.get("card_bg", "#1E1E2F"),
        )
        draw.text(
            (x + 24, current_y + 18),
            item.get("title", ""),
            font=get_font(18, bold=True),
            fill=theme.get("text", "#FFFFFF"),
        )

        desc = textwrap.fill(item.get("description", ""), width=85)
        draw.multiline_text(
            (x + 24, current_y + 46),
            desc,
            font=get_font(14),
            fill=theme.get("muted", "#A4B0BE"),
        )

        current_y += 100


def render_timeline(draw, el, theme, canvas_width):
    x = el.get("x", 80)
    y = el.get("y", 500)
    width = el.get("width", canvas_width - (x * 2))
    items = el.get("items", [])

    line_y = y + 40
    draw.line(
        (x, line_y, x + width, line_y),
        fill=theme.get("muted", "#444"),
        width=4,
    )

    step_w = width // max(1, len(items))
    for i, item in enumerate(items):
        cx = x + (i * step_w) + (step_w // 2)

        # Node circle
        draw.ellipse(
            (cx - 10, line_y - 10, cx + 10, line_y + 10),
            fill=theme.get("primary", "#6C5CE7"),
        )

        # Labels
        draw.text(
            (cx - 30, line_y - 40),
            item.get("date", ""),
            font=get_font(15, bold=True),
            fill=theme.get("secondary", "#00CEC9"),
        )
        draw.text(
            (cx - 40, line_y + 25),
            item.get("title", ""),
            font=get_font(16, bold=True),
            fill=theme.get("text", "#FFFFFF"),
        )

def render_design(json_source, output_path="output_design.png"):
    # Load JSON from file path or dictionary
    if isinstance(json_source, str):
        with open(json_source, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json_source

    # Canvas settings
    canvas_cfg = data.get("canvas", {})
    width = canvas_cfg.get("width", 1200)
    height = canvas_cfg.get("height", 800)
    bg_color = canvas_cfg.get("background", "#13131A")

    # Theme palette
    theme = data.get(
        "theme",
        {
            "primary": "#6C5CE7",
            "secondary": "#00CEC9",
            "text": "#FFFFFF",
            "muted": "#A4B0BE",
            "card_bg": "#1E1E2F",
        },
    )

    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    elements = data.get("elements", [])
    for el in elements:
        el_type = el.get("type")
        if el_type == "header":
            render_header(draw, el, theme)
        elif el_type == "stat_grid":
            render_stat_grid(draw, el, theme, width)
        elif el_type == "card_list":
            render_card_list(draw, el, theme, width)
        elif el_type == "timeline":
            render_timeline(draw, el, theme, width)

    img.save(output_path)

def generate_image(
    width,
    height,
    background,

    primary,
    secondary,
    text,
    muted,
    card_bg,

    header_x,
    header_y,
    title,
    subtitle,

    stat_grid_x,
    stat_grid_y,
    stat_columns,

    stat_1_label,
    stat_1_value,
    stat_1_change,

    stat_2_label,
    stat_2_value,
    stat_2_change,

    stat_3_label,
    stat_3_value,
    stat_3_change,

    card_list_x,
    card_list_y,
    card_list_width,

    card_1_title,
    card_1_description,

    card_2_title,
    card_2_description,

    card_3_title,
    card_3_description,

    timeline_x,
    timeline_y,
    timeline_width,

    timeline_1_date,
    timeline_1_title,

    timeline_2_date,
    timeline_2_title,

    timeline_3_date,
    timeline_3_title,

    timeline_4_date,
    timeline_4_title,
    output_path
):
    image_settings = {
        "canvas": {
            "width": width,
            "height": height,
            "background": background
        },

        "theme": {
            "primary": primary,
            "secondary": secondary,
            "text": text,
            "muted": muted,
            "card_bg": card_bg
        },

        "elements": [
            {
                "type": "header",
                "x": header_x,
                "y": header_y,
                "title": title,
                "subtitle": subtitle
            },

            {
                "type": "stat_grid",
                "x": stat_grid_x,
                "y": stat_grid_y,
                "columns": stat_columns,
                "items": [
                    {
                        "label": stat_1_label,
                        "value": stat_1_value,
                        "change": stat_1_change
                    },
                    {
                        "label": stat_2_label,
                        "value": stat_2_value,
                        "change": stat_2_change
                    },
                    {
                        "label": stat_3_label,
                        "value": stat_3_value,
                        "change": stat_3_change
                    }
                ]
            },

            {
                "type": "card_list",
                "x": card_list_x,
                "y": card_list_y,
                "width": card_list_width,
                "items": [
                    {
                        "title": card_1_title,
                        "description": card_1_description
                    },
                    {
                        "title": card_2_title,
                        "description": card_2_description
                    },
                    {
                        "title": card_3_title,
                        "description": card_3_description
                    }
                ]
            },

            {
                "type": "timeline",
                "x": timeline_x,
                "y": timeline_y,
                "width": timeline_width,
                "items": [
                    {
                        "date": timeline_1_date,
                        "title": timeline_1_title
                    },
                    {
                        "date": timeline_2_date,
                        "title": timeline_2_title
                    },
                    {
                        "date": timeline_3_date,
                        "title": timeline_3_title
                    },
                    {
                        "date": timeline_4_date,
                        "title": timeline_4_title
                    }
                ]
            }
        ]
    }
    render_design(image_settings, output_path=output_path)