from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path


ABS_PATH = Path(__file__).parent
PATH_TO_ENCRYPTED_PDF = ABS_PATH / "cryptography" / "encrypted-pdf.pdf"
PATH_TO_DECRYPTED_PDF = ABS_PATH / "cryptography" / "decrypted-pdf.pdf"

if not PATH_TO_ENCRYPTED_PDF.exists():
    print("não existe arquivo para descriptografar")

reader = PdfReader(stream=PATH_TO_ENCRYPTED_PDF)
writer = PdfWriter()

if reader.is_encrypted:
    reader.decrypt(password="my-password-123")

for page in reader.pages:
    writer.add_page(page)

with open(PATH_TO_DECRYPTED_PDF, "wb") as file:
    writer.write(file)
