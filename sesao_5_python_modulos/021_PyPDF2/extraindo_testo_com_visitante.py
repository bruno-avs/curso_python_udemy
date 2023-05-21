# usando uma função visitante para controlar qual parte extrair do PDF.
# elas são chamadas para cada operador ou para cada fragmento de testo.

from PyPDF2 import PdfReader
from pathlib import Path

# No código abaixo estou extraindo apenas o body do PDF, ignorando o cabeçalho
# e o rodapé.

PDF_PATH = Path(__file__).parent / "R20230512.pdf"

reader = PdfReader(stream=PDF_PATH)
page = reader.pages[0]

parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)


page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)
