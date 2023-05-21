# Aqui criaremos um PDF encriptado (com uma senha)

from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path


ABS_PATH = Path(__file__).parent
PDF_PATH = ABS_PATH / "R20230512.pdf"
PATH_TO_ENCRYPTED_PDF = ABS_PATH / "cryptography" / "encrypted-pdf.pdf"

reader = PdfReader(stream=PDF_PATH)
writer = PdfWriter()

# Copiamos todas as paginas do objeto PDF de leitura para o objeto PDF de
# escrita
for page in reader.pages:
    writer.add_page(page)

# Adicionamos a senha
writer.encrypt("my-password-123")

# Criamos o novo PDF
with open(PATH_TO_ENCRYPTED_PDF, "wb") as file:
    writer.write(file)
