from fpdf import FPDF
import pandas
from pathlib import Path
import glob

filepaths = glob.glob("Text/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")
for filename in filepaths:
    file = Path(filename).stem
    header = file.split("/")[0]
    print(header)
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=10, txt=header.title(), ln=4)
    pdf.set_font(family="Times", size=14)
    with open(filename, "r") as content:
        pdf.multi_cell(w=200, h=5, txt=content.read())


pdf.output("Text/animals.pdf")