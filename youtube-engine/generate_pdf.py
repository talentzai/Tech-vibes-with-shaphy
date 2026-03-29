import sys
import re
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib import colors

def md_to_reportlab(text):
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    return text

def md_to_pdf(input_path, output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=22*mm,
        rightMargin=22*mm,
        topMargin=24*mm,
        bottomMargin=24*mm,
        title="Tech Vibes Research Note"
    )

    H1 = ParagraphStyle("H1",
        fontSize=20, fontName="Helvetica-Bold",
        textColor=colors.HexColor("#111111"),
        spaceAfter=10, leading=26)

    H2 = ParagraphStyle("H2",
        fontSize=13, fontName="Helvetica-Bold",
        textColor=colors.HexColor("#222222"),
        spaceBefore=14, spaceAfter=5, leading=18)

    H3 = ParagraphStyle("H3",
        fontSize=11, fontName="Helvetica-Bold",
        textColor=colors.HexColor("#333333"),
        spaceBefore=10, spaceAfter=4, leading=16)

    META = ParagraphStyle("META",
        fontSize=9, fontName="Helvetica",
        textColor=colors.HexColor("#666666"),
        spaceAfter=6, leading=14)

    BODY = ParagraphStyle("BODY",
        fontSize=10, fontName="Helvetica",
        textColor=colors.HexColor("#1a1a1a"),
        spaceAfter=8, leading=16)

    BULLET = ParagraphStyle("BULLET",
        fontSize=10, fontName="Helvetica",
        textColor=colors.HexColor("#1a1a1a"),
        leftIndent=14, spaceAfter=5, leading=15,
        bulletIndent=4)

    FOOTER = ParagraphStyle("FOOTER",
        fontSize=8, fontName="Helvetica",
        textColor=colors.HexColor("#999999"),
        spaceAfter=0, leading=12)

    story = []

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip()

        if not line.strip():
            story.append(Spacer(1, 5))
            continue

        if line.startswith("# "):
            story.append(Paragraph(md_to_reportlab(line[2:].strip()), H1))
            story.append(HRFlowable(width="100%", thickness=1,
                color=colors.HexColor("#dddddd"), spaceAfter=8))

        elif line.startswith("## "):
            story.append(Paragraph(md_to_reportlab(line[3:].strip()), H2))

        elif line.startswith("### "):
            story.append(Paragraph(md_to_reportlab(line[4:].strip()), H3))

        elif line.startswith("- ") or line.startswith("* "):
            story.append(Paragraph(
                f"• &nbsp; {md_to_reportlab(line[2:].strip())}", BULLET))

        elif line.startswith("**") and "|" in line:
            story.append(Paragraph(md_to_reportlab(line.strip()), META))

        elif line.startswith("---"):
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=0.5,
                color=colors.HexColor("#cccccc"), spaceAfter=6))

        else:
            story.append(Paragraph(md_to_reportlab(line.strip()), BODY))

    story.append(Spacer(1, 16))
    story.append(HRFlowable(width="100%", thickness=0.5,
        color=colors.HexColor("#eeeeee"), spaceAfter=6))
    story.append(Paragraph(
        f"Tech Vibes Research Engine — Generated {datetime.now().strftime('%Y-%m-%d')}",
        FOOTER))

    doc.build(story)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_pdf.py <input.md> <output.pdf>")
        sys.exit(1)
    md_to_pdf(sys.argv[1], sys.argv[2])
