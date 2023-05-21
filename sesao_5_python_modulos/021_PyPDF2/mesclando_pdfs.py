from PyPDF2 import PdfWriter
from pathlib import Path

ABS_PATH = Path(__file__).parent
PDF_1_PATH = ABS_PATH / "R20230512.pdf"
PDF_2_PATH = ABS_PATH / "meta-pdf.pdf"
NEW_MERGED_PDF_PATH = ABS_PATH / "merged_pdfs" / "new_merged_pdf.pdf"

merger = PdfWriter()


merger.append(fileobj=PDF_1_PATH)
merger.append(fileobj=PDF_2_PATH)

merger.write(NEW_MERGED_PDF_PATH)
merger.close()
