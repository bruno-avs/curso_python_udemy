from pathlib import Path

path_to_test = Path(
    "D:\\User",
    "Documentos",
    "python",
    "curso_python_udemy",
    "sesao_5_python_modulos",
    "007_pathlib",
)

print("=" * 79)
path_without_segments = Path()
# se você não informar nenhum segmento na instância da classe ela ira
# representar o caminho relativo
print(f"Path() -> {path_without_segments}")

print("=" * 79)

print("Métodos e propriedades herdados")

print("_" * 79)

whole_path = Path("sesao_5_python_modulos", "007_pathlib")
print(f"\twhole_path -> {whole_path}")

parts = whole_path.parts
# retorna uma tupla com os segmentos do caminho separados

print(f"\twhole_path.parts -> {parts}")

print("_" * 79)

drive = path_to_test.drive
# retorna uma string que representa a letra ou nome da unidade, se houver
print(f"\tpath -> {path_to_test}")
print(f"\tpath.drive -> {drive}")

print("_" * 79)

root = path_to_test.root
# retorna uma string que representa a raiz (local ou global), se houver
print(f"\tpath -> {path_to_test}")
print(f"\tpath.root -> {root}")

print("_" * 79)

parents = path_to_test.parents
# retorna uma sequência imutável que fornece acesso aos ancestrais lógicos do
# caminho
print(f"\tpath -> {path_to_test}")
print(f"\tpath.parent[0] -> {parents[0]}")
print(f"\tpath.parent[1] -> {parents[1]}")

print("_" * 79)

parent = path_to_test.parent
# retorna um path referente a pasta pai (acima) da pasta atual
print(f"\tpath -> {path_to_test}")
print(f"\tpath.parent -> {parent}")

print("_" * 79)

final_segment = path_to_test.name
# retorna o segmento final de um caminho
print(f"\tpath -> {path_to_test}")
print(f"\tpath.name -> {final_segment}")

print("_" * 79)
path_file = path_to_test.joinpath("file.txt")
suffix = path_file.suffix
# retorna a extensão do arquivo, se houver

print(f"\tpath_file -> {path_file}")
print(f"\tpath_file.suffix -> {suffix}")

print("_" * 79)

# retorna o componente final do caminho, sem seu sufixo
stem_dir = path_to_test.stem

print(f"\tpath_to_test -> {path_to_test}")
print(f"\tpath_to_test.stem -> {stem_dir}")
print()

stem_file = path_file.stem

print(f"\tpath_file -> {path_file}")
print(f"\tpath_file.stem -> {stem_file}")

print("_" * 79)

is_absolute = path_to_test.is_absolute()
# retorna True se o caminho for absoluto, False caso contrario.
print(f"\tpath -> {path_to_test}")
print(f"\tpath.is_absolute() -> {is_absolute}")

print("_" * 79)

is_relative_to = path_to_test.is_relative_to(path_file)
# retorna True se o caminho for relativo (semelhantes) ao caminho passado no
# argumento

print(f"\tpath -> {path_to_test}")
print(f"\tother_path -> {path_file}")
print(f"\tpath.is_relative_to(other_path) -> {is_relative_to}")

print("_" * 79)

concatenated_path = path_to_test.joinpath("new_folder", "file.json")
# permite concatenar outros segmentos ao caminho, igual a função os.path.join()

print(f"\tpath -> {path_to_test}")
print(f'\tpath.joinpath("new_folder", "file.json") -> {concatenated_path}')

print("_" * 79)

path_with_new_name = path_file.with_name("new_file.rar")
# retorna um novo caminho com o "name" (ultimo segmento) alterado

print(f"\tpath_file -> {path_file}")
print(f'\tpath_file.with_name("new_file.rar") -> {path_with_new_name}')

print("_" * 79)

path_with_new_stem = path_file.with_stem("new_file")
# retorna um novo caminho com o "stem" (ultimo segmento, se for arquivo retorna
# sem a extensão) alterado

print(f"\tpath_file -> {path_file}")
print(f'\tpath_file.with_stem("new_file") -> {path_with_new_stem}')

print("_" * 79)

path_with_new_suffix = path_file.with_suffix(".py")
# retorna um novo caminho com a extensão alterada

print(f"\tpath_file -> {path_file}")
print(f'\tpath_file.with_suffix("py") -> {path_with_new_suffix}')

print("=" * 79)

print("Métodos e propriedades de Path")

print("_" * 79)

cwd = Path().cwd()
# retorna um novo caminho que representa o diretório atual

print(f"\tPath().cwd() -> {cwd}")

print("_" * 79)

home = Path().home()
# retorna um novo caminho que representa o diretório do usuário

print(f"\tPath().home() -> {home}")

print("_" * 79)

path_stat = path_to_test.stat()
# Retorna um objeto os.stat_result contendo informações sobre este caminho,
# como os.stat().
print(f"\tpath.stat() -> {path_stat}")

print("_" * 79)

print(f"\tpath.stat().st_mode -> {path_stat.st_mode}")

path_to_test.chmod(mode=0o444)
# Altera o modo de arquivo e as permissões, como os.chmod()
print(f"\tpath.chmod(mode=33277) \n\t>>> {path_to_test.stat().st_mode}")

print("_" * 79)

exist = path_to_test.exists()
# retorna se o caminho aponta para um arquivo ou diretório existente
print(f"\tpath.exists() -> {exist}")

print("_" * 79)

files = path_to_test.glob("**\*.py")
# Retorna todos os arquivos que corresponderem ao patter
print("\tpath_to_test.glob('**\*.py')")

for key, file in enumerate(files):
    print(f"\t\tfile {key} -> {file.name}")

print("_" * 79)

is_dir = path_to_test.is_dir()
# retorna true se o caminho apontar para um diretório existente
print(f"\tpath_to_test.is_dir() -> {is_dir}")

print("_" * 79)

is_file = path_file.is_file()
# retorna true se o caminho apontar para um arquivo existente
print(f"\tpath_file.is_file() -> {is_file}")

print("_" * 79)

is_symlink = path_file.is_symlink()
# retorna true se o caminho apontar para um arquivo existente
print(f"\tpath_file.is_symlink() -> {is_symlink}")

print("_" * 79)

files_or_dirs = path_to_test.iterdir()
# retorna um iterador, se o caminho apontar para um diretório, com cada
# iteração sendo um arquivo ou subpasta
print("\tpath.iterdir()")

for key, file_or_dir in enumerate(files_or_dirs):
    print(f"\t\tfile {key} -> {file_or_dir.name}")

print("_" * 79)

new_folder = path_to_test / "new_test_folder"
new_folder.mkdir(exist_ok=True)
# este método permite criar pastas no sistema

print("\tnew_folder.mkdir(exist_ok=True)")
print(f"\t>>> {new_folder}")

print("_" * 79)

new_file = new_folder.joinpath("file_test.txt")

print("\twith new_file.open('w+', encoding='UTF-8') as file:")
print('\t\tfile.write("Arquivo criado com sucesso")')

with new_file.open("w+", encoding="UTF-8") as file:
    file.write("Arquivo criado com sucesso")

print(f"\t{new_file}")

print("_" * 79)

bytes = new_file.read_bytes()
# Retorna o conteúdo binário do arquivo apontado como um objeto bytes
print(f"\tnew_file.read_bytes() -> {bytes}")

print("_" * 79)

content = new_file.read_text()
# Retorna o conteúdo binário do arquivo apontado como um objeto bytes
print(f"\tnew_file.read_text() -> {content}")

print("_" * 79)

target = path_to_test / "renamed_file.txt"
# target_path = new_file.rename(target)
# permite renomear um arquivo, mudando ou não ele de lugar

print("\tnew_file.rename() -> target_path")

print("_" * 79)

target_replace = new_file
# old_target = path_file.replace(target_replace)
# permite renomear um arquivo, mudando ou não ele de lugar

print("\tpath_file.rename() -> old_target")

print("_" * 79)

relative_path = Path()
print("\trelative_path = Path()")

absolute_path = relative_path.absolute()
print(f"\trelative_path.absolute() -> {absolute_path}")
# permite torna um caminho absoluto, retornado um novo objeto de caminho

print("_" * 79)

rglob = path_to_test.rglob("*.py")
# É o mesmo que chamar Path.glob() com “**/” adicionado na frente do pattern
# relativo fornecido

print('\tpath.rglob("*.py")')

for file in rglob:
    print(f"\t\t{file.name}")

print("_" * 79)

# path_to_test.rmdir()
print("\tpath_to_test.rmdir()")
# remove este diretório. O diretório deve estar vazio.

print("_" * 79)


samefile = path_to_test.samefile(path_to_test)
# Retorna tTrue se este path apontar para o mesmo arquivo em other_path,
# que pode ser um objeto PATH ou uma String
print(f"\tpath_to_test.samefile(path_to_test) -> {samefile}")

print("_" * 79)

created_file = path_to_test / "temp_file.txt"
print('\tcreated_file = path_to_test / "temp_file.txt"')

created_file.touch(exist_ok=True)
# Cria um arquivo neste caminho especifico. Se o arquivo já existir, a função
# será bem-sucedida se exist_ok for verdadeiro
print("\tcreated_file.touch(exist_ok=True)")

print("_" * 79)

print('\tcreated_file = path_to_test / "temp_file.txt"')

created_file.unlink(missing_ok=True)
# Remove um arquivo neste caminho especifico. Se missing_ok for verdadeiro,
# exceções de FileNotFoundError serão ignoradas
print("\tcreated_file.unlink(missing_ok=True)")

print("_" * 79)
