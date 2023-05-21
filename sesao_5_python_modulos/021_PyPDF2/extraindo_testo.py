# extraindo testo de arquivos PDF

from PyPDF2 import PdfReader
from pathlib import Path

# O PDF escolhido é o relatório focus do banco central
PDF_PATH = Path(__file__).parent / "R20230512.pdf"

# transformando o arquivo em um objeto de leitura
reader = PdfReader(stream=PDF_PATH)

# Pegando a primeira pagina
page = reader.pages[0]

# Extraindo o testo da pagina
text = page.extract_text()

print(text)

