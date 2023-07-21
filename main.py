from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    #  Set the Header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)  # border=1 {if we want to have a border}
    for y in range(20, 260, 10):
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(255)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(267)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
        for y in range(20, 264, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
