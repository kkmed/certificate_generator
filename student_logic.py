"""
certificate_template.py  —  Kriti's responsibility
====================================================
Fixed version matching the reference template image (1599x1131).
Canvas: 1500x990
"""

from PIL import Image, ImageDraw, ImageFont
import math, os

# ──────────────────────────────────────────────
#  CANVAS
# ──────────────────────────────────────────────
W, H = 1500, 990

# ──────────────────────────────────────────────
#  COLOUR PALETTE
# ──────────────────────────────────────────────
NAVY       = (15,  30,  80)
GOLD       = (184, 148,  66)
GOLD_LIGHT = (212, 175,  98)
CREAM      = (250, 246, 230)
DARK_TEXT  = (18,  30,  80)
MID_TEXT   = (90,  90,  90)
WHITE      = (255, 255, 255)

# ──────────────────────────────────────────────
#  FONTS
# ──────────────────────────────────────────────
FONT_DIR = "fonts"

def load_font(size, bold=False, italic=False):
    filemap = {
        (True,  True):  "DejaVuSerif-BoldItalic.ttf",
        (True,  False): "DejaVuSerif-Bold.ttf",
        (False, True):  "DejaVuSerif-Italic.ttf",
        (False, False): "DejaVuSerif.ttf",
    }
    path = os.path.join(FONT_DIR, filemap[(bold, italic)])
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    print("Loading:", path, "Exists:", os.path.exists(path))
    return ImageFont.load_default()

# ──────────────────────────────────────────────
#  FONT SIZES  — calibrated to match reference image
#
#  Reference image: 1599×1131, our canvas: 1500×990
#  Scale ≈ 0.938 horizontally, 0.876 vertically
#
#  Element                   Ref px  →  Canvas pt
#  ──────────────────────────────────────────────
#  Header org name bold        ~30   →   28
#  Tagline                     ~18   →   16
#  CERTIFICATE TITLE           ~72   →   68   (was 52 — too small)
#  Subtitle italic             ~28   →   26   (was 20 — too small)
#  RECIPIENT NAME             ~130   →   108  (was 72 — far too small)
#  Body italic                 ~26   →   24   (was 18 — too small)
#  Event name bold italic      ~32   →   30   (was 26 — slightly small)
#  Organized by                ~24   →   22   (was 16)
#  Table label bold            ~22   →   20   (was 14 — too small)
#  Table value                 ~22   →   20   (was 16)
#  Sig name bold               ~22   →   20   (was 16)
#  Sig title                   ~18   →   16   (was 13)
#  Footer                      ~18   →   16   (was 13)
# ──────────────────────────────────────────────

FONTS = {
    "org_name":    load_font(28,  bold=True),
    "tagline":     load_font(16),
    "cert_title":  load_font(68,  bold=True),
    "subtitle":    load_font(26,  italic=True),
    "recipient":   load_font(108, bold=True),
    "body":        load_font(24,  italic=True),
    "event_name":  load_font(30,  bold=True, italic=True),
    "org_small":   load_font(22),
    "table_label": load_font(20,  bold=True),
    "table_value": load_font(20),
    "sig_name":    load_font(20,  bold=True),
    "sig_title":   load_font(16),
    "footer":      load_font(16),
}

# ──────────────────────────────────────────────
#  LAYOUT CONSTANTS
# ──────────────────────────────────────────────
HEADER_H = 160
FOOTER_H = 46

# ──────────────────────────────────────────────
#  PLACEHOLDER COORDINATES
#  (x, y, anchor, font_key, color)
#
#  Spacing rationale (matches reference top-to-bottom):
#    HEADER_H (160) → bottom of navy band
#    +30  → cert title             y=190
#    +100 → gold rule              y=290  (drawn in background)
#    +115 → subtitle               y=305
#    +55  → recipient name         y=360
#    +170 → body text rule         y=530  (recipient name is 108px tall ≈ 160px with padding)
#    +30  → body_line              y=560  (after rule at ~530)
#    +40  → event_name             y=600
#    +36  → organized_by           y=636
#    +30  → info-table rule        y=666  (drawn in background)
#    +20  → date/venue/cert labels y=686
#    +30  → date/venue/cert values y=716
#    +30  → sig rule               y=746  (drawn in background)
#    +110 → sig names              y=840
#    +28  → sig titles             y=868
# ──────────────────────────────────────────────

PLACEHOLDERS = {
    # ── Header band ─────────────────────────────
    "organization_name":    (W//2,  28,  "center", "org_name",   GOLD_LIGHT),
    "organization_tagline": (W//2,  68,  "center", "tagline",    GOLD),

    # ── Body ─────────────────────────────────────
    "certificate_title":    (W//2,  HEADER_H + 30,  "center", "cert_title",  DARK_TEXT),

    # subtitle sits just below the first gold rule (HEADER_H+110 in background)
    "subtitle":             (W//2,  HEADER_H + 120, "center", "subtitle",    MID_TEXT),

    # Recipient name — large dominant element
    "recipient_name":       (W//2,  HEADER_H + 165, "center", "recipient",   DARK_TEXT),

    # second gold rule at HEADER_H+320; body text starts just after
    "body_line":            (W//2,  HEADER_H + 340, "center", "body",        MID_TEXT),
    "event_name":           (W//2,  HEADER_H + 378, "center", "event_name",  DARK_TEXT),
    "organized_by":         (W//2,  HEADER_H + 418, "center", "org_small",   MID_TEXT),

    # ── Info table  (third gold rule at HEADER_H+460) ──
    # Labels & values: centered within their column thirds
    "date_label":           (W//6,      HEADER_H + 472, "center", "table_label", DARK_TEXT),
    "date_value":           (W//6,      HEADER_H + 502, "center", "table_value", MID_TEXT),

    "venue_label":          (W//2,      HEADER_H + 472, "center", "table_label", DARK_TEXT),
    "venue_value":          (W//2,      HEADER_H + 502, "center", "table_value", MID_TEXT),

    "cert_id_label":        (5*W//6,    HEADER_H + 472, "center", "table_label", DARK_TEXT),
    "cert_id_value":        (5*W//6,    HEADER_H + 502, "center", "table_value", MID_TEXT),

    # ── Signature row ────────────────────────────
    "dignitary_1_name":     (W//6,      HEADER_H + 648, "center", "sig_name",  DARK_TEXT),
    "dignitary_1_title":    (W//6,      HEADER_H + 678, "center", "sig_title", MID_TEXT),

    "dignitary_2_name":     (W//2,      HEADER_H + 648, "center", "sig_name",  DARK_TEXT),
    "dignitary_2_title":    (W//2,      HEADER_H + 678, "center", "sig_title", MID_TEXT),

    "dignitary_3_name":     (5*W//6,    HEADER_H + 648, "center", "sig_name",  DARK_TEXT),
    "dignitary_3_title":    (5*W//6,    HEADER_H + 678, "center", "sig_title", MID_TEXT),

    # ── Footer ──────────────────────────────────
    "footer_text":          (W//2, H - FOOTER_H + 12, "center", "footer", GOLD),
}



# ──────────────────────────────────────────────
#  BACKGROUND DRAWING
# ──────────────────────────────────────────────
def draw_background(draw):
    # cream base
    draw.rectangle([0, 0, W, H], fill=CREAM)

    # outer gold border — thick outer + thin inner line
    for offset, lw in [(6, 4), (16, 1)]:
        draw.rectangle([offset, offset, W-offset, H-offset], outline=GOLD, width=lw)

    # navy header & footer bands
    draw.rectangle([0, 0,          W, HEADER_H], fill=NAVY)
    draw.rectangle([0, H-FOOTER_H, W, H],         fill=NAVY)

    # dotted side decoration (left & right body edges)
    for x in (32, W-32):
        for y in range(HEADER_H+20, H-FOOTER_H-20, 20):
            r = 3
            draw.ellipse([x-r, y-r, x+r, y+r], fill=GOLD)

    # horizontal gold rules with centre diamond
    # Adjusted Y positions to match new spacing
    for ry in [HEADER_H+110, HEADER_H+325, HEADER_H+460, HEADER_H+540]:
        draw.line([(80, ry), (W-80, ry)], fill=GOLD, width=1)
        s = 7
        draw.polygon([(W//2, ry-s),(W//2+s, ry),(W//2, ry+s),(W//2-s, ry)], fill=GOLD)

    # table vertical dividers
    for cx in (W//3, 2*W//3):
        draw.line([(cx, HEADER_H+462), (cx, HEADER_H+530)], fill=GOLD, width=1)

    # signature underlines — FIXED: x1 != x2 so actual lines are drawn
    for cx in (W//6, W//2, 5*W//6):
        draw.line([(cx-100, HEADER_H+640), (cx+100, HEADER_H+640)], fill=GOLD, width=1)

    # corner ornaments (3 concentric circles + centre dot)
    for cx, cy in [(55,55),(W-55,55),(55,H-55),(W-55,H-55)]:
        for r, lw in [(42,2),(30,1.5),(18,1)]:
            draw.ellipse([cx-r,cy-r,cx+r,cy+r], outline=GOLD, width=int(lw))
        draw.ellipse([cx-5,cy-5,cx+5,cy+5], fill=GOLD)

    # compass rose in header centre
    cx, cy, r = W//2, 118, 36
    draw.ellipse([cx-r,cy-r,cx+r,cy+r], outline=GOLD_LIGHT, width=2)
    ir = int(r * 0.55)
    draw.ellipse([cx-ir,cy-ir,cx+ir,cy+ir], fill=NAVY, outline=GOLD_LIGHT, width=1)
    for deg in range(0, 360, 45):
        a = math.radians(deg)
        draw.line(
            [(cx + ir*math.cos(a), cy + ir*math.sin(a)),
             (cx + r *math.cos(a), cy + r *math.sin(a))],
            fill=GOLD_LIGHT, width=1
        )
    draw.ellipse([cx-5,cy-5,cx+5,cy+5], fill=GOLD_LIGHT)

    # official seal — moved UP so it sits between sig row and table,
    # centred vertically in the gap between rule at HEADER_H+540 and sig underline
    scx, scy, sr = W//2, HEADER_H + 592, 38
    draw.ellipse([scx-sr,scy-sr,scx+sr,scy+sr], fill=GOLD, outline=GOLD_LIGHT, width=2)
    draw.ellipse(
        [scx-int(sr*.75),scy-int(sr*.75), scx+int(sr*.75),scy+int(sr*.75)],
        outline=WHITE, width=1
    )
    f_seal = load_font(10, bold=True)
    for dy, word in [(-6, "OFFICIAL"), (5, "SEAL")]:
        bb = draw.textbbox((0,0), word, font=f_seal)
        tw = bb[2]-bb[0]
        draw.text((scx - tw//2, scy+dy), word, font=f_seal, fill=WHITE)


# ──────────────────────────────────────────────
#  TEXT PLACEMENT HELPER
# ──────────────────────────────────────────────
def place_text(draw, x, y, text, font, color, anchor="center"):
    if anchor == "center":
        bb = draw.textbbox((0, 0), text, font=font)
        x = x - (bb[2] - bb[0]) // 2
    draw.text((x, y), text, font=font, fill=color)


# ──────────────────────────────────────────────
#  VISUAL TEST  — dummy labels at every position
# ──────────────────────────────────────────────
DUMMY_VALUES = {
    "organization_name":    "[ORGANIZATION_NAME]",
    "organization_tagline": "[ORGANIZATION_TAGLINE / WEBSITE]",
    "certificate_title":    "[CERTIFICATE_TITLE]",
    "subtitle":             "This certificate is proudly presented to",
    "recipient_name":       "[RECIPIENT_NAME]",
    "body_line":            "for exemplary participation and contribution in",
    "event_name":           "[EVENT_NAME]",
    "organized_by":         "organized by  [ORGANIZATION_NAME]",
    "date_label":           "Date",
    "date_value":           "[EVENT_DATE]",
    "venue_label":          "Venue",
    "venue_value":          "[VENUE / CITY]",
    "cert_id_label":        "Certificate No.",
    "cert_id_value":        "[CERT_ID]",
    "dignitary_1_name":     "[DIGNITARY_1_NAME]",
    "dignitary_1_title":    "[DIGNITARY_1_TITLE]",
    "dignitary_2_name":     "[DIGNITARY_2_NAME]",
    "dignitary_2_title":    "[DIGNITARY_2_TITLE]",
    "dignitary_3_name":     "[DIGNITARY_3_NAME]",
    "dignitary_3_title":    "[DIGNITARY_3_TITLE]",
    "footer_text":          "[ORGANIZATION_NAME]  ·  [ORGANIZATION_EMAIL]  ·  [ORGANIZATION_WEBSITE]",
}


def render_template_test(output="template.png"):
    img  = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(img)

    draw_background(draw)

    for key, (x, y, anchor, font_key, color) in PLACEHOLDERS.items():
        text = DUMMY_VALUES.get(key, f"[{key}]")
        font = FONTS[font_key]
        place_text(draw, x, y, text, font, color, anchor)

    img.save(output, dpi=(150, 150))
    print(f"✅  Fixed template saved → {output}")


if __name__ == "__main__":
    render_template_test()
