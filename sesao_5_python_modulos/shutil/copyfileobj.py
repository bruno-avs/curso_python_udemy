import shutil
import os

# o método copyfileobj copia o conteúdo de um objeto de arquivo e
# cola em outro
src_folder = os.path.abspath('pasta_text_1')
destiny_folder = os.path.abspath('pasta_text_2')

src_file = "file_text_1.txt"
destiny_file = "file_text_2.txt"

src_full_path = os.path.join(src_folder, src_file)
destiny_full_path = os.path.join(destiny_folder, destiny_file)

file_1 = open(src_full_path, "r")
file_2 = open(destiny_full_path, "w")

# você precisa fornecer a função copyfileobj um objeto de arquivo de leitura
# e um objeto de arquivo de escrita

path_copy_file = shutil.copyfileobj(file_1, file_2, 1)

file_1.close()
file_2.close()
