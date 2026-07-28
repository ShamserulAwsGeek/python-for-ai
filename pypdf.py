from glob import glob
from PyPDF2 import PdfWriter

with PdfWriter() as merger:
    for pdf in glob("pdf/*.pdf"):
        if pdf != "pdf/merged.pdf":
            merger.append(pdf)
    merger.write("pdf/merged.pdf")
