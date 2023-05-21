from PyPDF2 import PdfReader, PdfWriter, PageObject
from pathlib import Path
import re

PDF_PATH = Path(__file__).parent / "R20230512.pdf"

reader = PdfReader(stream=PDF_PATH, strict=True)
writer = PdfWriter()

annotation = {"/Main": "Minha anotação."}

for page in reader.pages:
    p = writer.clean_page(page)
    writer.add_page(p)

writer.add_annotation(0, annotation)
my_page = PageObject()

writer.add_filtered_articles(
    re.compile(r"[a-z]{20}"), my_page, reader)
print(writer.get_page(0))
with open("PDF-annotation.pdf", "wb") as fd:
    writer.write(fd)
