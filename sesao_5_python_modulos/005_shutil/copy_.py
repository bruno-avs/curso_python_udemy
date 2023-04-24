import shutil
import os
# esta função basicamente copia um arquivo, mais não preserva 
# alguns metadados

src_folder = "pasta_text_1"
dest_folder = "pasta_text_2"

src_file = "file_text_1.txt"
dest_file = "file_text_1_copy.txt"

src_path = os.path.join(src_folder, src_file)
dest_path = os.path.join(dest_folder, dest_file)

path_to_copy = shutil.copy(src_path, dest_path)