# escrevendo metadados em um arquivo PDF
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

ABS_PATH = Path(__file__).parent

ORIGINAL_PDF_PATH = ABS_PATH / "R20230512.pdf"
PATH_TO_CHANGED_PDF = ABS_PATH / "meta-pdf.pdf"

# Criado um objeto PDF leitura e um objeto PDF escrita.
# O objeto PDF de escrita será usado para gravar os novos metadados

reader = PdfReader(stream=ORIGINAL_PDF_PATH)
writer = PdfWriter()

# Copiando as paginas do objeto PDF de leitura para o objeto de escrita
for page in reader.pages:
    writer.add_page(page)

# adicionado os metadados
writer.add_metadata({"/Author": "Bruno", "/Producer": "Company"})

# criando o novo arquivo
with open(PATH_TO_CHANGED_PDF, "wb") as file:
    writer.write(file)

reader_2 = PdfReader(stream=PATH_TO_CHANGED_PDF)

meta = reader_2.metadata

print(meta.author)
print(meta.producer)
