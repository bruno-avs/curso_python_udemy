from pathlib import Path
import zipfile
import os

# Este modulo permite criar, ler e extrair arquivos ZIP

ABS_PATH = Path(__file__).parent

ORIGINAL_FILES_FD_PATH = ABS_PATH / "original_files"
UNZIPPED_FILES_FD_PATH = ABS_PATH / "unzipped_files"

ZIP_FILE_PATH = ABS_PATH / "my_zip.zip"

# Criando um arquivo ZIP
with zipfile.ZipFile(ZIP_FILE_PATH, "w") as zip:
    for root, dirs, files in os.walk(ORIGINAL_FILES_FD_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            zip.write(file_path, file)

# Lendo um arquivo ZIP
with zipfile.ZipFile(ZIP_FILE_PATH, "r") as zip:
    file_info = zip.getinfo("file.csv")
    # retorna um objeto zip_info referente ao arquivo especificado.
    print(file_info)
    print()

    info_list = zip.infolist()
    # retorna um lista com objetos zip_info referentes ao arquivo
    print(info_list)
    print()

    name_list = zip.namelist()
    # retorna uma lista só com os nomes dos arquivos no zip
    print(name_list)
    print()

    zip.printdir()
    # da um print nos arquivos do zip


# extraindo arquivo zip
with zipfile.ZipFile(ZIP_FILE_PATH, "r") as zip:
    # Você pode extrair só um arquivo ou vários.
    for root, dirs, files in os.walk(UNZIPPED_FILES_FD_PATH):
        for file in files:
            path_file = os.path.join(root, file)
            os.unlink(path_file)

    zip.extract(zip.getinfo("file.csv"), UNZIPPED_FILES_FD_PATH)
    # permite extrair só um arquivo
    zip.extractall(UNZIPPED_FILES_FD_PATH)
    # permite extrair todos os arquivos dentro do zip de uma vez
