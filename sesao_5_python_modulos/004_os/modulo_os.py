import os
import getpass


print("=" * 79)  # Atributos

print("Atributos do modulo")

print("-" * 79)

mapping_environ = os.environ
# retorna um objeto de mapeamento com varias informações sobre o sistema
# operacional
print("\tos.environ")
# print(f"{mapping_environ}")

print("-" * 79)

os_name = os.name
# ele retorna um string do nome da plataforma que esta rodando o código
print(f"\tos.name -> {os_name}")


print("=" * 79)  # métodos

print("Métodos do modulo")

print("-" * 79)

login_name = os.getlogin()
# retorna o nome de usuário logado no terminal de controle de processo
print(f"\tos.getlogin() -> {login_name}")
print(f"\tgetpass.getuser() -> {getpass.getuser()}")  # esta função também faz
# o mesmo

print("-" * 79)

terminal_size = os.get_terminal_size()
# retorna uma tupla com o tamanho do terminal
print(f"\tos.get_terminal_size() -> {terminal_size}")

print("-" * 79)

cwd = os.getcwd()
# retorna uma string representando o diretório de trabalho atual
print(f"\tos.getcwd() -> {cwd}")

print("-" * 79)

ABS_PATH = os.path.join(os.getcwd(), "sesao_5_python_modulos", "004_os")

stat_result = os.stat(os.path.join(ABS_PATH, "directory_parser.py"))
# este método permite obter varias informações do arquivo passado
print(f"\tos.stat(path) -> {stat_result}")

print("-" * 79)

files_in_dir = os.listdir()
# lista todos os arquivos do diretório especificado
print(f"\tos.listdir('.') -> {files_in_dir}")

print("-" * 79)

os.mkdir(os.path.join(ABS_PATH, "created_dir"))
# cria uma pasta, se a pasta ja existir um erro sera levantado
print("\tos.mkdir(os.path.join(ABS_PATH, 'created_dir'))")

print("-" * 79)

os.rmdir(os.path.join(ABS_PATH, "created_dir"))
# exclui uma pasta especificada
print("\tos.rmdir(os.path.join(ABS_PATH, 'created_dir'))")

print("-" * 79)

# os.system("cls")
# permite executar comandos no sistema operacional
# no window para limpar o terminal é cls, nos outros sistemas é clear
print("\tos.system('cls')")

print("-" * 79)

# os.makedirs(os.path.join(ABS_PATH, "new_folder-mekedirs"))
# esta função permite criar um diretório inteiro com todas as pasta, ou criar
# apenas as pastas que faltam
print("\tos.makedirs(os.path.join(ABS_PATH, 'new_folder-mekedirs'))")

print("-" * 79)

src = os.path.join(ABS_PATH, "file_texte.txt")
dst = os.path.join(ABS_PATH, "file_texte_renamed.txt")

# os.rename(src, dst)
# renomeia um arquivo podendo mudar o local do arquivo também
print("\tos.rename(src, dst)")

print("-" * 79)

start_path = os.path.join(ABS_PATH, "references.txt")
# os.startfile(start_path)
# este método nos permite iniciar (abrir) um arquivo, assim como quando você
# clica 2 vezes em um PDF.
print("\tos.startfile(start_path)")

print("-" * 79)

# este método é parecido com o listdir, a diferença é que este atua de forma
# recursiva navegando por tudo dentro do diretório especificado 
for root, dirs, files in os.walk(ABS_PATH):
    print(root)
    print(dirs)
    print(files)

print("=" * 79)