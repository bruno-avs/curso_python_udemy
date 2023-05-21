from PyPDF2 import PdfReader
from pathlib import Path

PDF_PATH = Path(__file__).parent / "R20230512.pdf"
reader = PdfReader(stream=PDF_PATH)

metadata = reader.metadata

print(metadata.author)
print(metadata.creation_date)
print(metadata.creator)
print(metadata.modification_date)
print(metadata.producer)
print(metadata.subject)
print(metadata.title)
