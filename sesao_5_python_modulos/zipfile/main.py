from zipfile import ZipFile
import os

abs_path = os.path.abspath(".")
zip_file_name = "my_zip.zip"
path_files = os.path.join(abs_path, "files")
path_zip = os.path.join(abs_path, zip_file_name)

files_folder = os.listdir(path_files)
# gravando os arquivos no zip
with ZipFile(path_zip, "w") as zipfile:
    for file in files_folder:
        path_to_file = os.path.join(path_files, file)
        zipfile.write(path_zip, file)

# lendo os arquivos no zip
with ZipFile(path_zip, "r") as zipfile:
    if zipfile.testzip() is None:
        for z_info in zipfile.infolist():
            print(z_info)
    
