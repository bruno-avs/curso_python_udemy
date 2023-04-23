# Este módulo implementa algumas funções úteis em nomes de caminho
import os

print("=" * 79)
ABS_PATH = os.path.join(os.getcwd(), "sesao_5_python_modulos", "004_os")

print("Métodos do modulo")

print("-" * 79)

abs_path = os.path.abspath(".")
# retorna o caminho absoluto até a pasta atual
print(f"\tos.path.abspath('.') -> {abs_path}")

print("-" * 79)

cwd = os.getcwd()
os_path_join = os.path.join(cwd, "sesao_5_python_modulos")
# este método junta dois ou mais caminhos de forma inteligente seguindo o
# modelo de cada sistema operacional
print(f"\tos.path.join(cwd, 'sesao_5_python_modulos') -> {os_path_join}")

print("-" * 79)

print("\tABS_PATH =", ABS_PATH)
base_name = os.path.basename(ABS_PATH)
# este método retorna o nome base de um caminho
print(f"\tos.path.basename(ABS_PATH) -> {base_name}")

print("-" * 79)

path_to_file = os.path.join(ABS_PATH, "references.txt")
print("\tpath_to_file =", path_to_file)

dir_name = os.path.dirname(path_to_file)
# retorna só a parte do diretório de um caminho que leva a um arquivo
print(f"\tos.path.dirname(path_to_file) -> {dir_name}")

print("-" * 79)

is_exists = os.path.exists(ABS_PATH)
# retorna True se o caminho existir, False caso contrario
print(f"\tos.path.exists(ABS_PATH) -> {is_exists}")

print("-" * 79)

is_dir = os.path.isdir(ABS_PATH)
# retorna True se o caminho levar até um diretório, False caso contrario
print(f"\tos.path.isdir(ABS_PATH) -> {is_dir}")

print("-" * 79)

is_file = os.path.isfile(path_to_file)
# retorna True se o caminho especificado leva a um arquivo, False caso 
# contrario
print(f"\tos.path.isfile(ABS_PATH) -> {is_file}")

print("-" * 79)

path_split = os.path.split(path_to_file)
# este método permite separar o caminho do nome do arquivo
print(f"\tos.path.split(path_to_file) -> {path_split}")

print("-" * 79)