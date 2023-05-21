# Aqui irei extrair todas as imagens do PDF

from PyPDF2 import PdfReader
from pathlib import Path


ABS_PATH = Path(__file__).parent
PDF_PATH = ABS_PATH / "R20230512.pdf"


reader = PdfReader(stream=PDF_PATH)
count = 0
# faço um for em todas as paginas
for page in reader.pages:
    # faço outro em todas as imagens
    for image in page.images:
        PATH_TO_IMG = ABS_PATH / "extracted_imgs" / (str(count) + image.name)

        # crio uma arquivo de imagem usando o atributo name e data
        with open(PATH_TO_IMG, "wb") as file:
            file.write(image.data)

        count += 1
