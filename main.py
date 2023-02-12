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
    pdf.cell(w=0, h=10, txt=header.title())


pdf.output("Text/animals.pdf")