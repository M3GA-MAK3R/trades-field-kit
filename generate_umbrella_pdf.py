#!/usr/bin/env python3
"""
Handy Helper Umbrella — 8-Panel Field Reference PDF
Generates a printable field reference guide organized like umbrella flaps.
"""

import urllib.request
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Design palette (Nexus)
BG = HexColor("#F7F6F2")
SURFACE = HexColor("#F9F8F5")
BORDER = HexColor("#D4D1CA")
TEXT = HexColor("#28251D")
TEXT_MUTED = HexColor("#7A7974")
PRIMARY = HexColor("#01696F")
WARNING = HexColor("#964219")
SUCCESS = HexColor("#437A22")
ACCENT = HexColor("#DA7101")

# Panel header colors — alternate between primary and accent shades
PANEL_COLORS = [
    HexColor("#01696F"),  # Safety — teal
    HexColor("#1B474D"),  # Refrigeration — dark teal
    HexColor("#DA7101"),  # Superheat — orange
    HexColor("#A84B2F"),  # Thermostat — terra
    HexColor("#7A39BB"),  # Contactor — purple
    HexColor("#006494"),  # Heat pump — blue
    HexColor("#437A22"),  # Electrical — green
    HexColor("#944454"),  # Troubleshooting — mauve
]

# Download fonts
FONT_DIR = Path("/tmp/fonts")
FONT_DIR.mkdir(exist_ok=True)

fonts = {
    "Inter": ("Inter", "https://github.com/google/fonts/raw/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf"),
    "DMSans-Bold": ("DMSans-Bold", "https://github.com/google/fonts/raw/main/ofl/dmsans/DMSans%5Bopsz%2Cwght%5D.ttf"),
}

for name, (font_name, url) in fonts.items():
    path = FONT_DIR / f"{name}.ttf"
    if not path.exists():
        try:
            urllib.request.urlretrieve(url, str(path))
        except Exception:
            pass
    if path.exists():
        pdfmetrics.registerFont(TTFont(font_name, str(path)))

# Use downloaded fonts if available, otherwise Helvetica
BODY_FONT = "Inter" if "Inter" in pdfmetrics.getRegisteredFontNames() else "Helvetica"
BOLD_FONT = "DMSans-Bold" if "DMSans-Bold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"
MONO_FONT = "Courier"

# Styles
panel_title = ParagraphStyle(
    "PanelTitle", fontName=BOLD_FONT, fontSize=13, leading=16,
    textColor=HexColor("#FFFFFF"), alignment=TA_LEFT, spaceAfter=0,
)
panel_subtitle = ParagraphStyle(
    "PanelSubtitle", fontName=BODY_FONT, fontSize=8, leading=10,
    textColor=HexColor("#E0DFD9"), alignment=TA_LEFT, spaceAfter=0,
)
body = ParagraphStyle(
    "Body", fontName=BODY_FONT, fontSize=8.5, leading=11,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=4,
)
body_small = ParagraphStyle(
    "BodySmall", fontName=BODY_FONT, fontSize=7.5, leading=9.5,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=3,
)
heading = ParagraphStyle(
    "Heading", fontName=BOLD_FONT, fontSize=9, leading=11,
    textColor=PRIMARY, alignment=TA_LEFT, spaceAfter=2, spaceBefore=4,
)
code_style = ParagraphStyle(
    "Code", fontName=MONO_FONT, fontSize=7, leading=8.5,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=2,
    leftIndent=8,
)
warning_style = ParagraphStyle(
    "Warning", fontName=BOLD_FONT, fontSize=8, leading=10,
    textColor=WARNING, alignment=TA_LEFT, spaceAfter=3,
)
footnote = ParagraphStyle(
    "Footnote", fontName=BODY_FONT, fontSize=6.5, leading=8,
    textColor=TEXT_MUTED, alignment=TA_LEFT, spaceAfter=1,
)

PAGE_W, PAGE_H = letter

def make_panel_header(number, title, subtitle, color):
    """Create a colored header bar for a panel."""
    num_text = f"  {number}  "
    title_text = f"<font name='{BOLD_FONT}' size='13' color='#FFFFFF'>{num_text}  {title}</font>"
    sub_text = f"<font name='{BODY_FONT}' size='8' color='#E0DFD9'>{subtitle}</font>"
    
    header_table = Table(
        [[Paragraph(title_text, panel_title)],
         [Paragraph(sub_text, panel_subtitle)]],
        colWidths=[PAGE_W - 1.4 * inch],
    )
    header_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    return header_table

def make_panel(num, title, subtitle, content_flows, color, sources=None):
    """Create a complete panel with header and content."""
    elements = []
    elements.append(make_panel_header(num, title, subtitle, color))
    elements.append(Spacer(1, 4))
    for flow in content_flows:
        elements.append(flow)
    elements.append(Spacer(1, 2))
    if sources:
        for s in sources:
            elements.append(Paragraph(s, footnote))
    
    # Wrap in a bordered table for the "flap" look
    inner = Table([[e] for e in elements], colWidths=[PAGE_W - 1.4 * inch])
    inner.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return inner

# --- Panel 1: Safety First ---
panel1 = [
    Paragraph("Lockout/Tagout (LOTO)", heading),
    Paragraph("1. <b>Notify</b> anyone affected", body_small),
    Paragraph("2. <b>Shut down</b> by normal means", body_small),
    Paragraph("3. <b>Isolate</b> — disconnect/break energy source", body_small),
    Paragraph("4. <b>Lock out</b> — apply individual lock + tag", body_small),
    Paragraph("5. <b>Verify de-energized</b> — test meter on known source first, then circuit", body_small),
    Paragraph("6. <b>Release</b> — only the person who applied the lock removes it", body_small),
    Spacer(1, 3),
    Paragraph("Wet-Work Precautions", heading),
    Paragraph("<b>Never</b> pressure wash energized electrical components. Cover motors, contactors, control boards. Keep water away from disconnects/panels. Allow equipment to dry before re-energizing. Use GFCI-protected power.", body_small),
    Spacer(1, 3),
    Paragraph("PPE Checklist", heading),
    Paragraph("Safety glasses/face shield | Electrical-rated gloves (Class 0) | Hearing protection | EH-rated boots | Long sleeves for brazing", body_small),
]

sources1 = [
    '<a href="https://www.osha.gov/control-hazardous-energy">OSHA Lockout/Tagout (29 CFR 1910.147)</a>',
]

# --- Panel 2: Refrigeration Cycle ---
panel2 = [
    Paragraph("The 4 Stages", heading),
    Paragraph("1. <b>Compressor</b> — raises pressure & temperature of vapor", body_small),
    Paragraph("2. <b>Condenser</b> — rejects heat, vapor becomes liquid", body_small),
    Paragraph("3. <b>Metering Device</b> — drops pressure, liquid becomes mixed phase", body_small),
    Paragraph("4. <b>Evaporator</b> — absorbs heat, refrigerant becomes vapor", body_small),
    Spacer(1, 3),
    Paragraph("    COMPRESSOR", code_style),
    Paragraph("    ▲       ▼", code_style),
    Paragraph(" Low-P    High-P", code_style),
    Paragraph(" vapor    vapor", code_style),
    Paragraph("    ▲       ▼", code_style),
    Paragraph(" EVAP    CONDENSER", code_style),
    Paragraph("    ▲       ▼", code_style),
    Paragraph("    ←─ METERING DEVICE ─→", code_style),
    Spacer(1, 3),
    Paragraph("Pressure Zones (R410A approx)", heading),
    Paragraph("<b>High side:</b> 350-450 PSIG, 100-120°F saturated", body_small),
    Paragraph("<b>Low side:</b> 100-140 PSIG, 40-55°F saturated", body_small),
    Spacer(1, 2),
    Paragraph("Metering Devices: TXV (best efficiency) | Fixed piston (charge-sensitive) | Cap tube (small systems) | EEV (electronic, variable)", body_small),
]

sources2 = [
    '<a href="https://hvacrschool.com/">HVAC School — Refrigeration Cycle</a>',
    '<a href="https://hvac.anthonyscoolschool.com/">Anthony\'s Cool School HVAC Training</a>',
]

# --- Panel 3: Superheat & Subcooling ---
panel3 = [
    Paragraph("Superheat = Suction Line Temp − Sat. Suction Temp", body),
    Paragraph("Measures evaporator performance", body_small),
    Spacer(1, 2),
    Table([
        ["Superheat", "Likely Cause"],
        ["High (>15-20°F)", "Undercharge, restriction, low airflow"],
        ["Low (<5-10°F)", "Overcharge, overfeeding, high airflow"],
        ["Normal (8-14°F)", "System OK (TXV: 10-14, fixed: 8-12)"],
    ], colWidths=[100, 200]),
    Spacer(1, 4),
    Paragraph("Subcooling = Sat. Liquid Temp − Liquid Line Temp", body),
    Paragraph("Measures condenser performance", body_small),
    Spacer(1, 2),
    Table([
        ["Subcooling", "Likely Cause"],
        ["High (>15-20°F)", "Overcharge, liquid line restriction"],
        ["Low (<5-10°F)", "Undercharge, condenser airflow issue"],
        ["Normal (8-12°F)", "System OK"],
    ], colWidths=[100, 200]),
    Spacer(1, 3),
    Paragraph("Steps: Measure line temps | Read gauges | PT chart for sat temps | Calculate | Compare to mfr specs", body_small),
]

sources3 = [
    '<a href="https://hvacrschool.com/">HVAC School — Superheat & Subcooling</a>',
    '<a href="https://hvac.anthonyscoolschool.com/">Anthony\'s Cool School</a>',
]

# --- Panel 4: Thermostat Low-Voltage Wiring ---
panel4 = [
    Paragraph("Terminal Reference", heading),
    Table([
        ["Term", "Color", "Function"],
        ["R/RH/RC", "Red", "24V power (heat/cool)"],
        ["C", "Blue", "Common return"],
        ["Y/Y1", "Yellow", "Cooling → contactor"],
        ["G", "Green", "Fan / blower"],
        ["W/W1", "White", "Heating"],
        ["O", "Orange", "Rev. valve — cool (most)"],
        ["B", "Dk Blue", "Rev. valve — heat (Ruud/Rheem)"],
        ["W2", "White", "Aux / 2nd-stage heat"],
    ], colWidths=[45, 50, 205]),
    Spacer(1, 3),
    Paragraph("Common Failures", heading),
    Paragraph("<b>No 24V at stat:</b> Check transformer, fuse, float switch", body_small),
    Paragraph("<b>Stat blank:</b> Check R-C for 24V, C wire connection", body_small),
    Paragraph("<b>Fan won\'t stop:</b> G wire shorted, relay stuck", body_small),
    Paragraph("<b>No cooling:</b> Y not reaching contactor, float/pressure switch", body_small),
    Paragraph("<b>Rev. valve wrong:</b> Check O/B — energize-in-cool vs heat", body_small),
    Spacer(1, 2),
    Paragraph("Float switch: Breaking R kills stat + defrost board. Breaking Y kills cooling only.", body_small),
]

sources4 = [
    '<a href="https://www.hvacrschool.com/videos/understanding-low-voltage-wiring-for-ac-heat-pumps-3d/">HVAC School — Low Voltage Wiring</a>',
]

# --- Panel 5: Contactor & Capacitor ---
panel5 = [
    Paragraph("Contactor", heading),
    Paragraph("<b>Coil:</b> 24V from stat Y → safety switches → contactor coil", body_small),
    Paragraph("<b>Contacts:</b> 240V through contacts to compressor + condenser fan", body_small),
    Paragraph("<b>Test:</b> Click sound, 24V across coil, ~0V across closed contacts", body_small),
    Spacer(1, 2),
    Paragraph("Capacitor Terminals", heading),
    Table([
        ["Terminal", "Connects To"],
        ["C (Common)", "Run winding + power"],
        ["HERM", "Compressor"],
        ["FAN", "Condenser fan motor"],
    ], colWidths=[80, 220]),
    Spacer(1, 3),
    Paragraph("WARNING: Capacitors hold charge even when power is off!", warning_style),
    Paragraph("Discharge with 20k-ohm resistor across terminals. Wait 30s, short again. Never use a screwdriver.", body_small),
    Spacer(1, 2),
    Paragraph("Testing", heading),
    Paragraph("<b>Visual:</b> Bulging/leaking = replace | <b>MFD:</b> ±10% of rating | <b>Ground:</b> Terminal to case = OL (infinite)", body_small),
]

sources5 = [
    '<a href="https://hvacrschool.com/">HVAC School — Contactor & Capacitor Testing</a>',
]

# --- Panel 6: Heat Pump & Defrost ---
panel6 = [
    Paragraph("Heating Mode Sequence", heading),
    Paragraph("1. Stat calls heat (W/Y energizes)", body_small),
    Paragraph("2. Reversing valve positions for heating (de-energized on most brands)", body_small),
    Paragraph("3. Compressor starts — outdoor coil = evaporator (absorbs heat)", body_small),
    Paragraph("4. Indoor coil = condenser (rejects heat)", body_small),
    Paragraph("5. Supplemental heat (W2) engages if needed", body_small),
    Spacer(1, 2),
    Paragraph("Defrost Cycle", heading),
    Paragraph("Triggers when ice builds on outdoor coil (typically <40°F outdoor). Defrost board reverses to cooling mode, outdoor fan stops, heat strips energize. Duration: 5-15 min.", body_small),
    Spacer(1, 2),
    Table([
        ["Problem", "Check"],
        ["Never defrosts", "Defrost sensor/board, reversing valve"],
        ["Defrosts too often", "Sensor location/accuracy"],
        ["Won\'t exit defrost", "Sensor stuck, board relay"],
        ["Ice on coil", "Low charge, low airflow, defrost fail"],
    ], colWidths=[110, 190]),
    Spacer(1, 2),
    Paragraph("Rev. valve: Most brands energize O in cooling. Ruud/Rheem energize B in heating.", body_small),
]

sources6 = [
    '<a href="https://hvacrschool.com/">HVAC School — Heat Pump Defrost</a>',
    '<a href="https://hvac.anthonyscoolschool.com/">Anthony\'s Cool School</a>',
]

# --- Panel 7: Electrical Pocket Formulas ---
panel7 = [
    Paragraph("Ohm's Law", heading),
    Paragraph("<b>V = I × R</b>    <b>I = V ÷ R</b>    <b>R = V ÷ I</b>", body),
    Spacer(1, 1),
    Paragraph("Power (Single Phase)", heading),
    Paragraph("<b>P = V × I</b>    <b>P = I² × R</b>    <b>P = V² ÷ R</b>", body),
    Spacer(1, 1),
    Paragraph("Three-Phase Power", heading),
    Paragraph("<b>P = V × I × 1.732 × PF</b> (PF typically 0.8-0.95)", body_small),
    Spacer(1, 1),
    Paragraph("Voltage Drop (Copper)", heading),
    Paragraph("<b>VD = 2 × 12.9 × I × D ÷ CM</b>", body),
    Paragraph("K=12.9 (copper) | I=amps | D=one-way feet | CM=circular mils", body_small),
    Spacer(1, 1),
    Table([
        ["AWG", "Ampacity (60°C)", "CM"],
        ["14", "15A", "4,107"],
        ["12", "20A", "6,530"],
        ["10", "30A", "10,380"],
        ["8", "40A", "16,510"],
        ["6", "55A", "26,240"],
    ], colWidths=[60, 120, 110]),
    Spacer(1, 2),
    Paragraph("Motor FLA estimate: 240V 1-phase ≈ HP × 4.5 | 3-phase ≈ HP × 2.5", body_small),
    Paragraph("Always verify against NEC Article 310 and local code.", body_small),
]

sources7 = [
    '<a href="https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=70">NFPA 70 — National Electrical Code</a>',
]

# --- Panel 8: Troubleshooting Flow ---
panel8 = [
    Paragraph("No Cooling", heading),
    Paragraph("Stat on COOL, below room temp?", body_small),
    Paragraph("├ No → Check stat, batteries, display", body_small),
    Paragraph("└ Yes → Outdoor unit running?", body_small),
    Paragraph("   ├ No → Breaker → disconnect → contactor → cap → compressor", body_small),
    Paragraph("   └ Yes → Check suction/head pressure", body_small),
    Paragraph("      ├ Low suction, low head → Low charge / leak", body_small),
    Paragraph("      ├ High suction, high head → Restricted airflow / overcharge", body_small),
    Paragraph("      ├ Low suction, high head → Restriction (filter drier, TXV)", body_small),
    Paragraph("      └ High suction, low head → Bad compressor valves", body_small),
    Spacer(1, 2),
    Paragraph("Short Cycling", heading),
    Paragraph("Check: stat location (drafts), filter, coil freeze-up, low charge, oversized equip, pressure switch", body_small),
    Spacer(1, 2),
    Paragraph("Pressure Washing PM", heading),
    Paragraph("Cover electricals | ≤1500 PSI for condenser coils | Top-down spray | Acid cleaner for condenser, alkaline for evaporator | Rinse thoroughly | Dry before re-energizing | Straighten fins with comb", body_small),
]

sources8 = [
    '<a href="https://hvac.anthonyscoolschool.com/">Anthony\'s Cool School HVAC Training</a>',
    '<a href="https://www.osha.gov/control-hazardous-energy">OSHA Safety Standards</a>',
]

# --- Build PDF ---
output_path = "/home/user/workspace/Handy_Helper_Umbrella_Field_Reference.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    title="Handy Helper Umbrella — Field Reference",
    author="Perplexity Computer",
    leftMargin=0.7 * inch,
    rightMargin=0.7 * inch,
    topMargin=0.5 * inch,
    bottomMargin=0.5 * inch,
)

story = []

panels = [
    (1, "Safety First", "LOTO, PPE & Wet-Work Precautions", panel1, PANEL_COLORS[0], sources1),
    (2, "Refrigeration Cycle", "The 4 Stages of the Cycle", panel2, PANEL_COLORS[1], sources2),
    (3, "Superheat & Subcooling", "Charge & Performance Diagnostics", panel3, PANEL_COLORS[2], sources3),
    (4, "Thermostat Wiring", "Low-Voltage Terminal Reference", panel4, PANEL_COLORS[3], sources4),
    (5, "Contactor & Capacitor", "Motor Circuit Testing", panel5, PANEL_COLORS[4], sources5),
    (6, "Heat Pump & Defrost", "Sequence & Troubleshooting", panel6, PANEL_COLORS[5], sources6),
    (7, "Electrical Formulas", "Ohm's Law, Power & Voltage Drop", panel7, PANEL_COLORS[6], sources7),
    (8, "Troubleshooting Flow", "Decision Trees & PM Checklist", panel8, PANEL_COLORS[7], sources8),
]

# Title page header
title_para = Paragraph(
    f"<font name='{BOLD_FONT}' size='20' color='#01696F'>Handy Helper Umbrella</font>",
    ParagraphStyle("Title", alignment=TA_CENTER, fontSize=20, leading=24, spaceAfter=4),
)
subtitle_para = Paragraph(
    f"<font name='{BODY_FONT}' size='10' color='#7A7974'>8-Panel Field Reference for HVAC & Electrical Trades</font>",
    ParagraphStyle("Subtitle", alignment=TA_CENTER, fontSize=10, leading=13, spaceAfter=8),
)

# Build pages: 2 panels per page
for page_idx in range(0, len(panels), 2):
    if page_idx > 0:
        story.append(PageBreak())
    
    # Title on first page
    if page_idx == 0:
        story.append(title_para)
        story.append(subtitle_para)
        story.append(HRFlowable(width="100%", thickness=1, color=BORDER, spaceAfter=6))
    
    # Panel pair
    for i in range(2):
        if page_idx + i < len(panels):
            num, title, subtitle, content, color, sources = panels[page_idx + i]
            story.append(make_panel(num, title, subtitle, content, color, sources))
            if i == 0:
                # Fold line between panels
                story.append(Spacer(1, 4))
                story.append(HRFlowable(
                    width="100%", thickness=0.5, color=BORDER,
                    dash=[3, 3], spaceAfter=4,
                ))

# Footer on each page
def page_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFont(BODY_FONT, 7)
    canvas_obj.setFillColor(TEXT_MUTED)
    canvas_obj.drawString(0.7 * inch, 0.3 * inch,
                          "Handy Helper Umbrella — Field Reference for HVAC & Electrical Trades")
    canvas_obj.drawRightString(PAGE_W - 0.7 * inch, 0.3 * inch,
                                f"Page {doc.page} of 4")
    canvas_obj.drawString(0.7 * inch, 0.2 * inch,
                          "Verify all values against manufacturer specs, NEC, and local code. For educational use only.")
    canvas_obj.restoreState()

doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
print(f"PDF generated: {output_path}")
