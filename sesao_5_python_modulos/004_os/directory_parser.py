import os

path = r"D:\User\Documentos\python\curso_python_udemy\sesao_5_python_modulos\004_os"
"""
ele lista tudo oque esta no diretório do caminho especificado,
mostrando algumas informações a mais
"""


def format_size(file_in_bytes):
    base = 1024
    kb = base
    mb = base**2
    gb = base**3
    tb = base**4

    format_abbr: str = ""

    if file_in_bytes < kb:
        format_abbr = "B"
    elif file_in_bytes < mb:
        file_in_bytes /= kb
        format_abbr = "KB"
    elif file_in_bytes < gb:
        file_in_bytes /= mb
        format_abbr = "MB"
    elif file_in_bytes < tb:
        file_in_bytes /= gb
        format_abbr = "GB"

    rounded_size = round(file_in_bytes, 2)
    return f"{rounded_size}{format_abbr}".replace(".", ",")


for root, dirs, files in os.walk(path):
    numb_files = 0
    for file in files:
        try:
            numb_files += 1
            name, exten = os.path.splitext(file)
            full_path = os.path.join(root, file)
            size_in_bytes = os.path.getsize(full_path)
            size = format_size(int(size_in_bytes))

            print(f"Full path: {full_path}")
            print(f"File name: {name}")
            print(f"Extension: {exten}")
            print(f"Size in bytes: {size_in_bytes}")
            print(f"Size: {size}")
            print()
        except PermissionError:
            print("File not permission")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error:{e}")

    print(f"{numb_files} file(s) found.")
