import shutil
import os

# o método copyfile copia o conteúdo de um objeto de arquivo e
# cola em outro, não copia metadados
# se o destino ja existir, ele será substituído pelo arquivo de origem, caso
# contrario, um novo arquivo sera criado

src_folder = os.path.abspath('pasta_text_1')
destiny_folder = os.path.abspath('pasta_text_2')

src_file = "file_text_1.txt"
destiny_file = "file_text_2.txt"

src_full_path = os.path.join(src_folder, src_file)
destiny_full_path = os.path.join(destiny_folder, destiny_file)

path_copy_file = shutil.copyfile(src_full_path, destiny_full_path)
# ele retorna uma string que representa o arquivo recém criado
print(path_copy_file)
