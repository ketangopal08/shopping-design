"""
CraftWave — UI/UX Case Study PDF Generator
Generates a bold, magazine-like editorial case study PDF using ReportLab.
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
import os

OUTPUT_PATH = "/Users/ketangopalspectro/ClaudeCode Projects/E-commerce/CraftWave_CaseStudy.pdf"

# ── Palette ──────────────────────────────────────────────────────────────────
C_DARK     = HexColor("#0A0A0A")
C_WHITE    = HexColor("#FFFFFF")
C_PURPLE   = HexColor("#7C5CFF")
C_LGRAY    = HexColor("#F4F4F4")
C_ORANGE   = HexColor("#FF6B35")
C_MUTED    = HexColor("#888888")
C_DGRAY    = HexColor("#1A1A1A")
C_MED      = HexColor("#2D2D2D")
C_GREEN    = HexColor("#4CAF50")
C_RED      = HexColor("#D32F2F")
C_DPURPLE  = HexColor("#5B3FCC")

W, H = A4  # 595.27 x 841.89 pts

# ── Helpers ───────────────────────────────────────────────────────────────────

def fill_bg(c, color):
    c.setFillColor(color)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def rounded_rect(c, x, y, w, h, r=6, fill_color=None, stroke_color=None, lw=1):
    if fill_color:
        c.setFillColor(fill_color)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(lw)
    c.roundRect(x, y, w, h, r, stroke=1 if stroke_color else 0, fill=1 if fill_color else 0)


def pill_badge(c, x, y, text, bg=None, fg=None, font_size=8, padding_x=10, padding_y=4):
    bg  = bg  or C_PURPLE
    fg  = fg  or C_WHITE
    c.setFont("Helvetica-Bold", font_size)
    tw  = c.stringWidth(text, "Helvetica-Bold", font_size)
    bw  = tw + padding_x * 2
    bh  = font_size + padding_y * 2
    rounded_rect(c, x - bw/2, y - bh/2, bw, bh, r=bh/2, fill_color=bg)
    c.setFillColor(fg)
    c.drawCentredString(x, y - font_size/2 + 1, text)


def draw_sparkle(c, x, y, size=20, color=None, alpha=0.15):
    color = color or C_WHITE
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", size)
    c.setFillAlpha(alpha)
    c.drawCentredString(x, y, "\u2726")
    c.setFillAlpha(1)


def body_wrap(c, x, y, text, font, size, color, max_width, line_height=None):
    """Simple word-wrap for body text."""
    lh    = line_height or size * 1.4
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line  = ""
    cy    = y
    for word in words:
        test = (line + " " + word).strip()
        if c.stringWidth(test, font, size) <= max_width:
            line = test
        else:
            c.drawString(x, cy, line)
            cy   -= lh
            line  = word
    if line:
        c.drawString(x, cy, line)
    return cy - lh


def page_footer(c, page_num):
    c.setFont("Helvetica", 7)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W / 2, 18, "CraftWave \u2014 UI/UX Case Study")
    c.drawCentredString(W / 2, 8, str(page_num))


def thick_rule(c, y, color=C_PURPLE, lw=2):
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(40, y, W - 40, y)


def decorative_number(c, num_str, x, y, size=80, color=None, alpha=0.08):
    color = color or C_WHITE
    c.setFont("Helvetica-Bold", size)
    c.setFillColor(color)
    c.setFillAlpha(alpha)
    c.drawString(x, y, num_str)
    c.setFillAlpha(1)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1 — COVER
# ─────────────────────────────────────────────────────────────────────────────

def page_cover(c):
    fill_bg(c, C_DARK)

    # Decorative sparkles — corners
    for sx, sy, sz, sa in [(W-60, H-60, 90, 0.10), (50, 60, 70, 0.07),
                            (W-30, 200, 40, 0.05), (30, H-100, 50, 0.06)]:
        draw_sparkle(c, sx, sy, sz, C_WHITE, sa)
    draw_sparkle(c, W-80, H-80, 55, C_PURPLE, 0.25)
    draw_sparkle(c, 60,   70,   45, C_PURPLE, 0.20)

    # Pill badge
    pill_badge(c, W/2, H - 70, "\u2726  UI/UX Case Study \u00b7 2025  \u2726",
               bg=C_PURPLE, fg=C_WHITE, font_size=9, padding_x=16, padding_y=6)

    # Giant headline
    c.setFont("Helvetica-Bold", 80)
    c.setFillColor(C_WHITE)
    c.drawCentredString(W/2 - 55, H - 160, "Craft")
    c.setFillColor(C_PURPLE)
    c.drawCentredString(W/2 + 65, H - 160, "Wave")

    # Underline accent
    c.setStrokeColor(C_PURPLE)
    c.setLineWidth(3)
    c.line(40, H - 175, W - 40, H - 175)

    # Subtitle
    c.setFont("Helvetica", 16)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W/2, H - 205, "Designed for Daily Life")

    # Small decorative rule
    thick_rule(c, H - 225, C_MED, lw=1)

    # Stat boxes — 4 in a row
    stats = [("8", "Sections"), ("2", "Fonts"), ("11", "Colors"), ("Vanilla", "CSS")]
    box_w = 108
    box_h = 65
    sx0   = (W - 4 * box_w - 3 * 8) / 2
    sy    = H - 330
    for i, (val, label) in enumerate(stats):
        bx = sx0 + i * (box_w + 8)
        rounded_rect(c, bx, sy, box_w, box_h, r=8,
                     fill_color=C_MED, stroke_color=C_PURPLE, lw=1)
        c.setFont("Helvetica-Bold", 22)
        c.setFillColor(C_WHITE)
        c.drawCentredString(bx + box_w/2, sy + box_h - 26, val)
        c.setFont("Helvetica", 8)
        c.setFillColor(C_MUTED)
        c.drawCentredString(bx + box_w/2, sy + 10, label)

    # Tech stack strip
    strip_y = H - 370
    c.setFillColor(C_MED)
    c.rect(0, strip_y - 20, W, 28, stroke=0, fill=1)
    tags = "HTML5  \u00b7  CSS3  \u00b7  JavaScript  \u00b7  Claude AI  \u00b7  Google Fonts"
    c.setFont("Helvetica", 9)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W/2, strip_y - 12, tags)

    # Feature bullets section
    features = [
        "\u2726  Fully responsive across all devices",
        "\u2726  Dark-mode ready design system",
        "\u2726  AI-assisted development workflow",
        "\u2726  Component-based architecture",
        "\u2726  Accessibility-first implementation",
    ]
    fy = H - 420
    for feat in features:
        c.setFont("Helvetica", 10)
        c.setFillColor(C_MUTED)
        c.drawString(60, fy, feat)
        fy -= 18

    # Device mockup illustration — monitor + phone
    # Monitor
    mx, my, mw, mh = 320, H - 540, 190, 120
    rounded_rect(c, mx, my, mw, mh, r=5, stroke_color=C_PURPLE, lw=1.5)
    # Screen inside
    rounded_rect(c, mx+6, my+14, mw-12, mh-22, r=3, fill_color=C_MED)
    # Stand
    c.setStrokeColor(C_PURPLE)
    c.setLineWidth(1.5)
    c.line(mx+mw/2, my, mx+mw/2, my-14)
    c.line(mx+mw/2-22, my-14, mx+mw/2+22, my-14)
    # UI lines in screen
    c.setStrokeColor(C_MUTED)
    c.setLineWidth(0.5)
    for li in range(4):
        lsy = my + 14 + 10 + li * 14
        c.line(mx+12, lsy, mx+mw-12, lsy)

    # Phone
    px, py, pw, ph = 525, H - 530, 55, 98
    rounded_rect(c, px, py, pw, ph, r=8, stroke_color=C_ORANGE, lw=1.5)
    rounded_rect(c, px+4, py+10, pw-8, ph-20, r=4, fill_color=C_MED)
    # Home button
    rounded_rect(c, px+pw/2-7, py+3, 14, 5, r=2, stroke_color=C_MUTED, lw=0.5)

    # Year — subtle big number bottom right
    c.setFont("Helvetica-Bold", 120)
    c.setFillColor(HexColor("#161616"))
    c.setFillAlpha(1)
    c.drawRightString(W - 30, 30, "2025")

    page_footer(c, 1)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 2 — PROJECT OVERVIEW
# ─────────────────────────────────────────────────────────────────────────────

def page_overview(c):
    fill_bg(c, C_LGRAY)

    # Decorative number
    decorative_number(c, "01", 30, H - 100, size=80, color=C_DGRAY, alpha=0.06)

    # Section title
    thick_rule(c, H - 65, C_PURPLE, lw=3)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(C_DARK)
    c.drawString(40, H - 100, "Project Overview")

    # LEFT column — About
    lx = 40
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(C_DARK)
    c.drawString(lx, H - 130, "About CraftWave")
    about_text = (
        "CraftWave is a modern e-commerce platform built "
        "to showcase handcrafted goods. The project focuses "
        "on a clean, editorial aesthetic with smooth UX flows, "
        "accessibility standards, and mobile-first design."
    )
    body_wrap(c, lx, H - 148, about_text, "Helvetica", 9, C_MUTED, 230, 14)

    # Goals checklist
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(C_DARK)
    c.drawString(lx, H - 240, "Project Goals")
    goals = [
        "Build a visually striking storefront",
        "Ensure full mobile responsiveness",
        "Integrate an AI-assisted workflow",
        "Achieve accessibility compliance",
        "Create a scalable design system",
    ]
    gy = H - 260
    for goal in goals:
        c.setFillColor(C_GREEN)
        c.circle(lx + 5, gy + 4, 4, stroke=0, fill=1)
        c.setFont("Helvetica", 9)
        c.setFillColor(C_DARK)
        c.drawString(lx + 16, gy, goal)
        gy -= 16

    # Project details table
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(C_DARK)
    c.drawString(lx, H - 380, "Project Details")
    details = [
        ("Timeline",  "2 Weeks"),
        ("Role",      "Solo Designer & Developer"),
        ("Platform",  "Web (HTML/CSS/JS)"),
        ("AI Tools",  "Claude Code, Claude AI"),
    ]
    dy = H - 400
    for label, val in details:
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(C_PURPLE)
        c.drawString(lx, dy, label.upper())
        c.setFont("Helvetica", 9)
        c.setFillColor(C_DARK)
        c.drawString(lx + 80, dy, val)
        dy -= 16

    # RIGHT column — Key Decision cards
    rx = 295
    cw = 240
    decisions = [
        ("No Framework",
         "Pure HTML/CSS/JS keeps the site lean, "
         "fast, and dependency-free."),
        ("AI-First Workflow",
         "Claude AI accelerated ideation, code "
         "generation, and review cycles."),
        ("Dark/Light Hybrid",
         "Strategic use of dark/light sections "
         "creates visual rhythm and drama."),
    ]
    cy2 = H - 115
    for title, desc in decisions:
        rounded_rect(c, rx, cy2 - 72, cw, 68, r=8, fill_color=C_DARK)
        # Purple top accent line
        c.setFillColor(C_PURPLE)
        c.roundRect(rx, cy2 - 6, cw, 6, 3, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(C_WHITE)
        c.drawString(rx + 12, cy2 - 22, title)
        body_wrap(c, rx + 12, cy2 - 36, desc, "Helvetica", 8, C_MUTED, cw - 24, 12)
        cy2 -= 84

    # Sparkles
    draw_sparkle(c, W - 55, H - 55, 40, C_PURPLE, 0.18)
    draw_sparkle(c, W - 30, 120,    25, C_ORANGE, 0.20)

    # Bottom purple banner
    banner_h = 36
    c.setFillColor(C_PURPLE)
    c.rect(0, 35, W, banner_h, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(C_WHITE)
    c.drawCentredString(W/2, 35 + banner_h/2 - 5, "CraftWave \u2014 E-Commerce Experience")

    page_footer(c, 2)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 3 — DESIGN PROCESS
# ─────────────────────────────────────────────────────────────────────────────

def page_process(c):
    fill_bg(c, C_DARK)

    decorative_number(c, "02", 30, H - 100, size=80, color=C_WHITE, alpha=0.05)

    thick_rule(c, H - 65, C_ORANGE, lw=3)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(C_WHITE)
    c.drawString(40, H - 100, "The Process")
    c.setFont("Helvetica", 10)
    c.setFillColor(C_MUTED)
    c.drawString(40, H - 118, "A structured, iterative design and development workflow")

    steps = [
        ("01", "Discovery & Research",   "FigJam",
         ["Competitive analysis", "User persona mapping", "Content audit"]),
        ("02", "Wireframing",             "Figma",
         ["Lo-fi sketches", "Information architecture", "Flow diagrams"]),
        ("03", "Visual Design",           "Figma + CSS",
         ["Style guide creation", "Component library", "Dark/Light system"]),
        ("04", "Development",             "Claude Code",
         ["HTML structure", "CSS animations", "JS interactions"]),
        ("05", "Testing & Launch",        "Browser DevTools",
         ["Responsiveness checks", "Accessibility audit", "Performance test"]),
    ]

    bar_h  = 82
    bar_y  = H - 155
    bar_w  = W - 80
    bx     = 40

    for i, (num, title, tool, bullets) in enumerate(steps):
        bg = C_MED if i % 2 == 0 else HexColor("#141414")
        rounded_rect(c, bx, bar_y - bar_h, bar_w, bar_h, r=6, fill_color=bg)

        # Number pill
        pill_badge(c, bx + 30, bar_y - 22, num, bg=C_PURPLE, fg=C_WHITE, font_size=9,
                   padding_x=10, padding_y=5)

        # Title
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(C_WHITE)
        c.drawString(bx + 64, bar_y - 18, title)

        # Tool pill
        pill_badge(c, bx + bar_w - 70, bar_y - 22, "\u2726 " + tool,
                   bg=C_DPURPLE, fg=C_WHITE, font_size=8, padding_x=10, padding_y=4)

        # Bullets
        bly = bar_y - 38
        for bullet in bullets:
            c.setFont("Helvetica", 8)
            c.setFillColor(C_MUTED)
            c.drawString(bx + 64, bly, "\u00b7 " + bullet)
            bly -= 13

        # Connector arrow (not after last)
        if i < len(steps) - 1:
            mid_y = bar_y - bar_h
            c.setStrokeColor(C_PURPLE)
            c.setLineWidth(1.5)
            c.line(bx + bar_w/2, mid_y, bx + bar_w/2, mid_y - 4)
            # Arrow head using polygon
            c.setFillColor(C_PURPLE)
            arrow_tip = mid_y - 8
            ax = bx + bar_w/2
            p = c.beginPath()
            p.moveTo(ax, arrow_tip)
            p.lineTo(ax - 5, arrow_tip + 7)
            p.lineTo(ax + 5, arrow_tip + 7)
            p.close()
            c.drawPath(p, stroke=0, fill=1)

        bar_y -= bar_h + 8

    # Sparkles
    draw_sparkle(c, W - 55, H - 55, 45, C_ORANGE, 0.18)
    draw_sparkle(c, 55, 80,          30, C_PURPLE, 0.15)

    page_footer(c, 3)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 4 — COLOR PALETTE
# ─────────────────────────────────────────────────────────────────────────────

def page_colors(c):
    fill_bg(c, C_WHITE)

    decorative_number(c, "03", 30, H - 100, size=80, color=C_LGRAY, alpha=1)

    thick_rule(c, H - 65, C_DARK, lw=3)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(C_DARK)
    c.drawString(40, H - 100, "Color System")
    c.setFont("Helvetica", 10)
    c.setFillColor(C_MUTED)
    c.drawString(40, H - 118, "A deliberate palette built for contrast, mood, and purpose")

    primary_swatches = [
        ("#1A1A1A", "Surface Dark",  "Backgrounds, containers"),
        ("#2D2D2D", "Surface Mid",   "Card backgrounds, dividers"),
        ("#F0F0F0", "Surface Light", "Light-mode backgrounds"),
        ("#888888", "Muted",         "Secondary text, icons"),
        ("#FFFFFF", "Pure White",    "Primary text on dark"),
        ("#D32F2F", "Danger Red",    "Alerts, remove actions"),
    ]

    sw = (W - 80 - 20) / 3
    sh = 100
    sx_start = 40
    sy_start = H - 155

    for i, (hex_c, name, usage) in enumerate(primary_swatches):
        col = i % 3
        row = i // 3
        bx  = sx_start + col * (sw + 10)
        by  = sy_start - row * (sh + 30)

        color = HexColor(hex_c)
        needs_border = hex_c == "#FFFFFF"
        if needs_border:
            rounded_rect(c, bx, by - sh, sw, sh, r=6,
                         fill_color=color, stroke_color=HexColor("#E0E0E0"), lw=1)
        else:
            rounded_rect(c, bx, by - sh, sw, sh, r=6, fill_color=color)

        # Hex label
        text_color = C_WHITE if hex_c in ("#1A1A1A", "#2D2D2D") else C_DARK
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(text_color)
        c.drawString(bx + 8, by - 22, hex_c)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(bx + 8, by - 36, name)

        # Usage below block
        c.setFont("Helvetica", 7.5)
        c.setFillColor(C_MUTED)
        c.drawString(bx + 8, by - sh - 14, usage)

    # Secondary chips row
    secondary = ["#FAFAFA", "#F5F5F5", "#E0E0E0", "#4CAF50", "#444444", "#EEEEEE"]
    chip_w = (W - 80 - 50) / 6
    chip_h = 28
    cy_chips = H - 430
    for i, hex_c in enumerate(secondary):
        cx = 40 + i * (chip_w + 10)
        rounded_rect(c, cx, cy_chips, chip_w, chip_h, r=4,
                     fill_color=HexColor(hex_c),
                     stroke_color=HexColor("#DDDDDD"), lw=0.5)
        c.setFont("Helvetica", 6.5)
        c.setFillColor(C_MUTED)
        c.drawCentredString(cx + chip_w/2, cy_chips - 12, hex_c)

    # Accent showcase
    for ax, ac, alabel in [(40, C_PURPLE, "Primary Accent \u2014 #7C5CFF"),
                            (300, C_ORANGE, "Highlight Accent \u2014 #FF6B35")]:
        aw = 230
        rounded_rect(c, ax, cy_chips - 70, aw, 35, r=6, fill_color=ac)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(C_WHITE)
        c.drawCentredString(ax + aw/2, cy_chips - 48, alabel)

    # Purple banner at bottom
    banner_h = 40
    c.setFillColor(C_PURPLE)
    c.rect(0, 35, W, banner_h, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(C_WHITE)
    c.drawCentredString(W/2, 35 + banner_h/2 - 4,
                        "Every color serves a purpose. No decoration without function.")

    draw_sparkle(c, W - 55, H - 55, 40, C_PURPLE, 0.12)
    page_footer(c, 4)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 5 — TYPOGRAPHY
# ─────────────────────────────────────────────────────────────────────────────

def page_typography(c):
    fill_bg(c, C_DARK)

    decorative_number(c, "04", 30, H - 100, size=80, color=C_WHITE, alpha=0.05)

    thick_rule(c, H - 65, C_PURPLE, lw=3)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(C_WHITE)
    c.drawString(40, H - 100, "Type System")

    # Split layout
    mid = W / 2 - 10

    # LEFT — Inter
    c.setFont("Helvetica-Bold", 58)
    c.setFillColor(C_WHITE)
    c.drawString(40, H - 170, "Inter")

    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(C_PURPLE)
    c.drawString(40, H - 188, "PRIMARY TYPEFACE")

    weights = [("400", "Regular"), ("500", "Medium"),
               ("600", "SemiBold"), ("700", "Bold"), ("800", "ExtraBold")]
    wy = H - 210
    for weight, label in weights:
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(C_PURPLE)
        c.drawString(40, wy, weight)
        c.setFont("Helvetica", 8)
        c.setFillColor(C_MUTED)
        c.drawString(75, wy, label)
        wy -= 13

    # RIGHT — DM Sans
    c.setFont("Helvetica-BoldOblique", 52)
    c.setFillColor(C_PURPLE)
    c.drawString(mid + 10, H - 170, "DM Sans")

    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(C_ORANGE)
    c.drawString(mid + 10, H - 188, "SECONDARY TYPEFACE")

    # Use cases
    uses = ["Body copy & descriptions",
            "UI labels & micro-copy",
            "Navigation items",
            "Form inputs & placeholders"]
    uy = H - 210
    for use in uses:
        c.setFont("Helvetica", 8)
        c.setFillColor(C_MUTED)
        c.drawString(mid + 10, uy, "\u00b7 " + use)
        uy -= 14

    # Divider
    thick_rule(c, H - 295, C_MED, lw=1)

    # Type scale
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(C_MUTED)
    c.drawString(40, H - 315, "TYPE SCALE")

    scale = [
        (24, "Display",  "Hero headlines, large callouts"),
        (20, "H1",       "Page titles"),
        (16, "H2",       "Section headings"),
        (13, "H3",       "Card titles, sub-sections"),
        (11, "Body Lg",  "Featured body copy"),
        (9,  "Body",     "Default paragraph text"),
        (7.5,"Caption",  "Labels, metadata, footnotes"),
    ]

    ty = H - 335
    for size, label, usage in scale:
        c.setFont("Helvetica-Bold", min(size, 20))
        c.setFillColor(C_WHITE)
        c.drawString(40, ty, label)
        c.setFont("Helvetica", 7.5)
        c.setFillColor(C_MUTED)
        c.drawString(120, ty + 1, str(size) + "px \u2014 " + usage)
        ty -= max(size * 1.3, 18)

    # Specimen line
    thick_rule(c, 165, C_MED, lw=1)
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(C_WHITE)
    c.drawCentredString(W/2, 140, "Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj")
    c.setFont("Helvetica", 9)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W/2, 120, "Character specimen \u2014 Inter & DM Sans")

    # Pairing note
    rounded_rect(c, 40, 55, W - 80, 35, r=6, fill_color=C_MED)
    c.setFont("Helvetica", 9)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W/2, 68,
        "Inter for headings + DM Sans for body = clarity without compromise.")

    draw_sparkle(c, W - 55, H - 55, 40, C_PURPLE, 0.15)
    page_footer(c, 5)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 6 — SECTION SHOWCASE
# ─────────────────────────────────────────────────────────────────────────────

def page_sections(c):
    fill_bg(c, C_LGRAY)

    decorative_number(c, "05", 30, H - 100, size=80, color=C_DGRAY, alpha=0.06)

    thick_rule(c, H - 65, C_DARK, lw=3)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(C_DARK)
    c.drawString(40, H - 100, "Section Breakdown")

    sections = [
        (1,  "Navigation",   "Fixed sticky",    C_PURPLE, "Smart sticky nav with logo, links & cart icon"),
        (2,  "Hero",         "Full viewport",   C_ORANGE, "Bold headline + CTA over high-contrast background"),
        (3,  "Products",     "4-col grid",      C_DARK,   "Responsive product cards with hover states"),
        (4,  "About",        "Split layout",    C_PURPLE, "Brand story with editorial image + copy"),
        (5,  "Features",     "3-col icons",     C_ORANGE, "USP highlights with animated icon blocks"),
        (6,  "Newsletter",   "Centered form",   C_DARK,   "Minimal email capture with validation"),
        (7,  "Testimonials", "Card carousel",   C_PURPLE, "Customer quotes in rotating card layout"),
        (8,  "Footer",       "4-col links",     C_ORANGE, "Full footer with sitemap and social links"),
    ]

    card_w   = (W - 80 - 12) / 2
    card_h   = 72
    cx_start = 40
    cy_start = H - 140

    for i, (num, name, layout, border_color, desc) in enumerate(sections):
        col  = i % 2
        row  = i // 2
        bx   = cx_start + col * (card_w + 12)
        by   = cy_start - row * (card_h + 10)

        rounded_rect(c, bx, by - card_h, card_w, card_h, r=6, fill_color=C_WHITE)
        # Left border accent
        c.setFillColor(border_color)
        c.roundRect(bx, by - card_h, 4, card_h, 2, stroke=0, fill=1)

        # Section number badge
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(border_color)
        c.drawString(bx + 14, by - 16, "#%02d" % num)

        # Name
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(C_DARK)
        c.drawString(bx + 14, by - 30, name)

        # Layout pill
        pill_badge(c, bx + card_w - 50, by - 23, layout,
                   bg=border_color, fg=C_WHITE, font_size=7,
                   padding_x=7, padding_y=3)

        # Description
        c.setFont("Helvetica", 7.5)
        c.setFillColor(C_MUTED)
        body_wrap(c, bx + 14, by - 44, desc, "Helvetica", 7.5, C_MUTED, card_w - 28, 12)

    # Wireframe sketch
    wf_y = 165
    wf_x = 40
    wf_w = W - 80
    wf_h = 115

    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(C_MUTED)
    c.drawString(wf_x, wf_y + wf_h + 8, "SITE LAYOUT \u2014 WIREFRAME OVERVIEW")

    rounded_rect(c, wf_x, wf_y, wf_w, wf_h, r=4,
                 fill_color=C_WHITE, stroke_color=HexColor("#DDDDDD"), lw=1)

    # Nav bar
    c.setFillColor(C_DARK)
    c.rect(wf_x + 4, wf_y + wf_h - 18, wf_w - 8, 14, stroke=0, fill=1)
    c.setFont("Helvetica", 6)
    c.setFillColor(C_WHITE)
    c.drawString(wf_x + 10, wf_y + wf_h - 10, "LOGO")
    c.drawRightString(wf_x + wf_w - 10, wf_y + wf_h - 10, "NAV  \u00b7  CART")

    # Hero
    c.setFillColor(C_MED)
    c.rect(wf_x + 4, wf_y + wf_h - 46, wf_w - 8, 24, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(C_MUTED)
    c.drawCentredString(wf_x + wf_w/2, wf_y + wf_h - 37, "HERO  \u2014  Headline \u00b7 CTA")

    # Products grid
    col_w = (wf_w - 8 - 9) / 4
    for gi in range(4):
        gx = wf_x + 4 + gi * (col_w + 3)
        c.setFillColor(HexColor("#EEEEEE"))
        c.roundRect(gx, wf_y + wf_h - 74, col_w, 24, 2, stroke=0, fill=1)

    # Footer strip
    c.setFillColor(C_DARK)
    c.rect(wf_x + 4, wf_y + 4, wf_w - 8, 12, stroke=0, fill=1)
    c.setFont("Helvetica", 5.5)
    c.setFillColor(C_MUTED)
    c.drawCentredString(wf_x + wf_w/2, wf_y + 9, "FOOTER")

    draw_sparkle(c, W - 55, H - 55, 35, C_PURPLE, 0.15)
    page_footer(c, 6)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 7 — AI TOOLS
# ─────────────────────────────────────────────────────────────────────────────

def page_ai(c):
    fill_bg(c, C_PURPLE)

    # Decorative bg circles
    c.setStrokeColor(HexColor("#9B80FF"))
    c.setFillColor(HexColor("#9B80FF"))
    c.setFillAlpha(0.08)
    c.circle(W - 80, H - 80, 120, stroke=0, fill=1)
    c.circle(60, 100, 90, stroke=0, fill=1)
    c.setFillAlpha(1)

    decorative_number(c, "06", 30, H - 100, size=80,
                      color=HexColor("#9B80FF"), alpha=0.25)

    thick_rule(c, H - 65, C_WHITE, lw=3)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(C_WHITE)
    c.drawString(40, H - 100, "Built with Claude AI")
    c.setFont("Helvetica", 10)
    c.setFillColor(HexColor("#C8BAFF"))
    c.drawString(40, H - 118, "AI-powered design and development \u2014 a new creative workflow")

    # 3 feature boxes
    feature_data = [
        ("Claude Code",
         "The AI pair-programmer that wrote, reviewed, and "
         "debugged the entire codebase interactively."),
        ("Claude Skills",
         "Pre-built skill templates for PDF generation, "
         "image processing, and data transformation."),
        ("Superpowers",
         "Instant component ideation, accessibility checks, "
         "responsive layout advice, and instant refactors."),
    ]

    bw = (W - 80 - 24) / 3
    bh = 130
    bx0 = 40
    by  = H - 165

    for i, (title, desc) in enumerate(feature_data):
        bx = bx0 + i * (bw + 12)
        rounded_rect(c, bx, by - bh, bw, bh, r=8, fill_color=C_WHITE)
        # Icon area
        c.setFillColor(C_PURPLE)
        c.roundRect(bx + 12, by - 30, 28, 20, 4, stroke=0, fill=1)
        icons = ["\u2328", "\u25c6", "\u2726"]
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(C_WHITE)
        c.drawCentredString(bx + 26, by - 24, icons[i])

        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(C_DARK)
        c.drawString(bx + 12, by - 46, title)
        body_wrap(c, bx + 12, by - 62, desc, "Helvetica", 8, HexColor("#555555"),
                  bw - 24, 12)

    # Workflow arrows
    thick_rule(c, H - 320, HexColor("#9B80FF"), lw=1)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(C_WHITE)
    c.drawCentredString(W/2, H - 340, "DEVELOPMENT WORKFLOW")

    steps_wf = ["Prompt", "Brainstorm", "Plan", "Build", "Review", "Ship"]
    sw_total = W - 80
    sw_step  = sw_total / len(steps_wf)
    wfy      = H - 390

    for i, step in enumerate(steps_wf):
        sx = 40 + i * sw_step + sw_step / 2
        # Circle
        c.setFillColor(C_WHITE if i < 5 else C_ORANGE)
        c.circle(sx, wfy, 18, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(C_PURPLE if i < 5 else C_WHITE)
        c.drawCentredString(sx, wfy - 3, step)
        # Connecting line
        if i < len(steps_wf) - 1:
            c.setStrokeColor(HexColor("#C8BAFF"))
            c.setLineWidth(1.5)
            c.line(sx + 18, wfy, sx + sw_step - 18, wfy)

    # Skill pills at bottom — dark purple strip
    c.setFillColor(C_DPURPLE)
    c.rect(0, 35, W, 90, stroke=0, fill=1)

    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(HexColor("#C8BAFF"))
    c.drawString(40, 112, "SKILLS USED:")

    skills = ["PDF Generation", "Image Processing", "Code Review",
              "Component Design", "Accessibility", "Responsive Layout",
              "Git Commits", "Documentation"]
    sx_pill = 40
    sy_pill = 92
    for skill in skills:
        sw2 = c.stringWidth(skill, "Helvetica", 8) + 18
        if sx_pill + sw2 > W - 40:
            sx_pill = 40
            sy_pill -= 22
        rounded_rect(c, sx_pill, sy_pill - 9, sw2, 16, r=8, fill_color=HexColor("#9B80FF"))
        c.setFont("Helvetica", 8)
        c.setFillColor(C_WHITE)
        c.drawString(sx_pill + 9, sy_pill - 2, skill)
        sx_pill += sw2 + 8

    page_footer(c, 7)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 8 — KEY FEATURES
# ─────────────────────────────────────────────────────────────────────────────

def page_features(c):
    fill_bg(c, C_DARK)

    decorative_number(c, "07", 30, H - 100, size=80, color=C_WHITE, alpha=0.05)

    thick_rule(c, H - 65, C_ORANGE, lw=3)
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(C_WHITE)
    c.drawString(40, H - 100, "Features & Techniques")

    features = [
        ("*", "Sticky Navigation",
         "position: sticky;\ntop: 0; z-index: 100;",
         "Smart nav that locks at top on scroll with smooth blur backdrop."),
        ("+", "CSS Grid Layout",
         "display: grid;\ngrid-template-columns:\n  repeat(auto-fit,\n  minmax(280px,1fr));",
         "Fully responsive product grid that adapts from 1 to 4 columns."),
        ("~", "Hover Animations",
         "transition: transform\n  0.3s cubic-bezier\n  (0.4, 0, 0.2, 1);",
         "Smooth scale and shadow transitions on all interactive elements."),
        ("#", "Dark Mode System",
         "[data-theme='dark'] {\n  --bg: #0A0A0A;\n  --text: #FFFFFF;\n}",
         "CSS custom properties enable instant theme switching system-wide."),
        ("@", "Form Validation",
         "input:invalid {\n  border-color: #D32F2F;\n  box-shadow: ...\n}",
         "Real-time HTML5 validation with custom styled error states."),
        ("^", "Performance Opt.",
         "img { loading: lazy;\n  decoding: async;\n  width: 100%; }",
         "Lazy-loaded images and optimized assets for fast page loads."),
    ]

    card_w = (W - 80 - 12) / 2
    card_h = 108
    cx0    = 40
    cy0    = H - 155

    for i, (icon, title, code, desc) in enumerate(features):
        col = i % 2
        row = i // 2
        bx  = cx0 + col * (card_w + 12)
        by  = cy0 - row * (card_h + 10)

        rounded_rect(c, bx, by - card_h, card_w, card_h, r=6, fill_color=C_MED)

        # Icon pill
        rounded_rect(c, bx + 8, by - 30, 22, 18, r=4, fill_color=C_PURPLE)
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(C_WHITE)
        c.drawCentredString(bx + 19, by - 24, icon)

        # Title
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(C_WHITE)
        c.drawString(bx + 36, by - 22, title)

        # Code snippet
        code_bg_h = 44
        code_bg_y = by - card_h + 26
        rounded_rect(c, bx + 8, code_bg_y, card_w - 16, code_bg_h, r=4,
                     fill_color=HexColor("#0D0D0D"))
        c.setFont("Courier", 6.5)
        c.setFillColor(C_GREEN)
        code_lines = code.split("\n")
        cly = code_bg_y + code_bg_h - 10
        for cl in code_lines:
            c.drawString(bx + 14, cly, cl)
            cly -= 9

        # Description
        c.setFont("Helvetica", 7.5)
        c.setFillColor(C_MUTED)
        trunc = desc[:60] + ("\u2026" if len(desc) > 60 else "")
        c.drawString(bx + 8, by - 38, trunc)

    # Responsive breakpoints
    thick_rule(c, 175, C_MED, lw=1)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W/2, 160, "RESPONSIVE BREAKPOINTS")

    breakpoints = [
        ("Desktop", "1200px+",  280, 90),
        ("Tablet",  "768-1199px", 200, 72),
        ("Mobile",  "< 768px",   120, 60),
    ]
    total_w = sum(bw2 for _, _, bw2, _ in breakpoints) + 40
    bpx     = (W - total_w) / 2
    bpy     = 50

    for label, size, bw2, bh2 in breakpoints:
        # Device frame
        c.setStrokeColor(C_PURPLE)
        c.setLineWidth(1.5)
        c.roundRect(bpx, bpy, bw2, bh2, 4, stroke=1, fill=0)
        # Screen
        c.setFillColor(C_MED)
        c.roundRect(bpx + 4, bpy + 8, bw2 - 8, bh2 - 16, 2, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 7)
        c.setFillColor(C_WHITE)
        c.drawCentredString(bpx + bw2/2, bpy + bh2/2, label)
        c.setFont("Helvetica", 6.5)
        c.setFillColor(C_MUTED)
        c.drawCentredString(bpx + bw2/2, bpy + bh2/2 - 11, size)
        bpx += bw2 + 20

    draw_sparkle(c, W - 55, H - 55, 40, C_ORANGE, 0.15)
    page_footer(c, 8)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 9 — CLOSING
# ─────────────────────────────────────────────────────────────────────────────

def page_closing(c):
    fill_bg(c, C_DARK)

    decorative_number(c, "08", 30, H - 100, size=80, color=C_WHITE, alpha=0.05)
    draw_sparkle(c, W - 60, H - 60, 50, C_PURPLE, 0.18)
    draw_sparkle(c, 55, 200, 35, C_ORANGE, 0.15)

    thick_rule(c, H - 65, C_PURPLE, lw=3)
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(C_PURPLE)
    c.drawString(40, H - 92, "FINAL THOUGHTS")

    # Big quote
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(C_WHITE)
    c.drawCentredString(W/2, H - 130, "\u201cDesign is not decoration.")
    c.drawCentredString(W/2, H - 157, "It\u2019s communication.\u201d")

    # Quote attr
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W/2, H - 175, "\u2014 Guiding principle behind CraftWave")

    thick_rule(c, H - 193, C_MED, lw=1)

    # What I Learned
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(C_WHITE)
    c.drawString(40, H - 218, "What I Learned")

    learnings = [
        "AI tools dramatically compress ideation-to-implementation cycles",
        "Strong typographic hierarchy does more work than any decoration",
        "Dark/light contrast sections create visual rhythm and reader engagement",
        "Constraint-based design (no frameworks) deepens CSS fluency",
        "Accessibility and aesthetics are complementary, not competing goals",
        "Documenting decisions as you build is as valuable as the build itself",
    ]
    ly = H - 242
    for i, item in enumerate(learnings):
        # Numbered circle
        c.setFillColor(C_PURPLE)
        c.circle(54, ly + 4, 7, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 6.5)
        c.setFillColor(C_WHITE)
        c.drawCentredString(54, ly + 1, str(i + 1))
        c.setFont("Helvetica", 9)
        c.setFillColor(C_MUTED)
        c.drawString(68, ly, item)
        ly -= 17

    # LinkedIn CTA card
    cta_y = H - 480
    rounded_rect(c, 40, cta_y, W - 80, 75, r=10, fill_color=C_PURPLE)
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(C_WHITE)
    c.drawCentredString(W/2, cta_y + 50, "Connect on LinkedIn")
    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#C8BAFF"))
    c.drawCentredString(W/2, cta_y + 32,
                        "Let's talk design, code, and creative problem-solving")
    tags = "#UXDesign   #FrontendDev   #AITools   #PortfolioProject   #CraftWave"
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#9B80FF"))
    c.drawCentredString(W/2, cta_y + 14, tags)

    # Stats row
    stat_y = H - 570
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W/2, stat_y, "PROJECT STATS AT A GLANCE")
    stat_data = [("9", "PDF Pages"), ("8", "Site Sections"),
                 ("100%", "Vanilla CSS"), ("1", "Developer")]
    stat_total_w = 4 * 90 + 3 * 12
    stx = (W - stat_total_w) / 2
    sty = stat_y - 20
    for val, lbl in stat_data:
        rounded_rect(c, stx, sty - 35, 90, 35, r=6, fill_color=C_MED)
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(C_WHITE)
        c.drawCentredString(stx + 45, sty - 16, val)
        c.setFont("Helvetica", 7)
        c.setFillColor(C_MUTED)
        c.drawCentredString(stx + 45, sty - 29, lbl)
        stx += 90 + 12

    # ── MARQUEE STRIP ──
    strip_h = 36
    c.setFillColor(C_ORANGE)
    c.rect(0, 0, W, strip_h + 2, stroke=0, fill=1)

    marquee_text = (
        "Thanks for watching  \u2726   CraftWave Case Study  \u2726   "
        "Thanks for watching  \u2726   CraftWave Case Study  \u2726   "
        "Thanks for watching  \u2726   CraftWave Case Study  \u2726"
    )
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(C_WHITE)
    c.drawCentredString(W/2, 12, marquee_text)

    # Page number above strip
    c.setFont("Helvetica", 7)
    c.setFillColor(C_MUTED)
    c.drawCentredString(W/2, strip_h + 10, "CraftWave \u2014 UI/UX Case Study  \u00b7  9")

    c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def generate():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=A4)
    c.setTitle("CraftWave \u2014 UI/UX Case Study")
    c.setAuthor("CraftWave Design")
    c.setSubject("E-Commerce UI/UX Case Study 2025")

    page_cover(c)
    page_overview(c)
    page_process(c)
    page_colors(c)
    page_typography(c)
    page_sections(c)
    page_ai(c)
    page_features(c)
    page_closing(c)

    c.save()
    size = os.path.getsize(OUTPUT_PATH)
    print("PDF generated: " + OUTPUT_PATH)
    print("Pages  : 9")
    print("Size   : %d bytes (%.1f KB)" % (size, size / 1024))


if __name__ == "__main__":
    generate()
