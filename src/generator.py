from PIL import Image, ImageDraw, ImageFont
from student_logic import PLACEHOLDERS, FONTS, place_text, draw_background


# -------------------------------
# WIDTH LIMITS
# -------------------------------
DEFAULT_WIDTHS = {
    "recipient_name": 900,
    "certificate_title": 1000,
    "event_name": 800,
    "body_line": 1000
}


# -------------------------------
# FONT LOADER
# -------------------------------
def load_font(font_family, size):
    paths = {
        "serif": "assets/fonts/DejaVuSerif.ttf",
        "sans": "assets/fonts/DejaVuSans.ttf"
    }
    return ImageFont.truetype(paths.get(font_family, paths["serif"]), size)


# -------------------------------
# AUTO FONT FIT
# -------------------------------
def get_fitting_font(draw, text, font, max_width):
    size = font.size

    while size > 10:
        f = font.font_variant(size=size)
        bbox = draw.textbbox((0, 0), text, font=f)
        if bbox[2] - bbox[0] <= max_width:
            return f
        size -= 2

    return font


# -------------------------------
# APPLY STYLE
# -------------------------------
def apply_style(key, base_font, base_color, style):
    if not style or key not in style:
        return base_font, base_color

    s = style[key]

    font = base_font

    if "font_family" in s or "font_size" in s:
        font = load_font(
            s.get("font_family", "serif"),
            s.get("font_size", base_font.size)
        )

    color = s.get("color", base_color)

    return font, color


# -------------------------------
# BACKGROUND HANDLER
# -------------------------------
def create_background(image_path):

    # ORIGINAL TEMPLATE (code-based)
    if image_path == "classic":
        img = Image.new("RGB", (1500, 990), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw_background(draw)
        return img

    # IMAGE TEMPLATE
    else:
        return Image.open(image_path).convert("RGB")


# -------------------------------
# MAIN GENERATOR
# -------------------------------
def generate_certificate(data, image_path, output_path, style=None, layout=None):

    img = create_background(image_path)
    draw = ImageDraw.Draw(img)

    for key, (x, y, anchor, font_key, color) in PLACEHOLDERS.items():

        text = data.get(key)
        if not text:
            continue

        base_font = FONTS[font_key]

        # apply style
        font, color = apply_style(key, base_font, color, style)

        # layout adjustment
        if layout and key in layout:
            x = layout[key].get("x", x)
            y = layout[key].get("y", y)

        max_width = DEFAULT_WIDTHS.get(key, 800)
        font = get_fitting_font(draw, text, font, max_width)

        place_text(draw, x, y, text, font, color, anchor)

    img.save(output_path)
    print(f"✅ Certificate generated → {output_path}")
    
TEMPLATE_CONFIGS = {
    "1": {
        "description": "Template 1: Minimalist Layout",
        "image_path": "templates/template.png",
        "layout": {},
        "style": {}
    },
    "2": {
        "description": "Template 2: Ornate Layout",
        "image_path": "templates/template2.png",
        "layout": {},
        "style": {}
    },
    "3": {
        "description": "Template 3: Corporate Layout (Custom positioning)",
        "image_path": "templates/template3.png",
        "layout": {
            "recipient_name": {"y": 350},
            "certificate_title": {"y": 180}
        },
        "style": {
            "certificate_title": {
                "font_family": "serif",
                "font_size": 65,
                "color": (80, 80, 80)
            },
            "recipient_name": {
                "font_family": "serif",
                "font_size": 95,
                "color": (150, 110, 40)
            }
        }
    }
}

if __name__ == "__main__":
    
    data = {
        # HEADER
        "organization_name": "ABC University",
        "organization_tagline": "Excellence in Education",

        # TITLE SECTION
        "certificate_title": "Certificate of Excellence",
        "subtitle": "This certificate is proudly presented to",

        # MAIN NAME
        "recipient_name": "Krithi Meda",

        # BODY
        "body_line": "for outstanding performance in",
        "event_name": "AI Workshop 2026",
        "organized_by": "organized by ABC University",

        # DETAILS (BOTTOM SECTION)
        "date_label": "Date",
        "date_value": "May 2026",

        "venue_label": "Venue",
        "venue_value": "Hyderabad",

        "cert_id_label": "Certificate No.",
        "cert_id_value": "CERT123",

        # SIGNATURES
        "dignitary_1_name": "Dr. Rao",
        "dignitary_1_title": "Director",

        "dignitary_2_name": "Prof. Sharma",
        "dignitary_2_title": "Dean",

        "dignitary_3_name": "Ms. Iyer",
        "dignitary_3_title": "Coordinator",

        # FOOTER
        "footer_text": "abc@university.com · www.abcuniversity.com"
    }

    image_path = "template3.png"

    style = {
        "certificate_title": {
            "font_family": "serif",
            "font_size": 65,
            "color": (80, 80, 80)
        },

        "recipient_name": {
            "font_family": "serif",
            "font_size": 95,
            "color": (150, 110, 40)
        }
    }

    layout = {
        "recipient_name": {"y": 350},
        "certificate_title": {"y": 180}
    }

    generate_certificate(
        data,
        "classic",
        "output/certificate.png",
        style,
        layout
    )
