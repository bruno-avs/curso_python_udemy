name = "bruno alves"
# O método capitalize retorna uma cópia da string com a primeira letra em
# maiúscula
print(f"Inicio = {name}")
print(f"capitalize() -> {name.capitalize()}")
print("-" * 30)

name = "BRUNO Alves"
# Retorna um cópia da string com todas as letras em minusculas, se diferencia
# de lower pois tem mais compatibilidade, sendo assim mais recomendado para
# corresponder valores
print(f"Inicio = {name}")
print(f"casefold() -> {name.casefold()}")
print("-" * 30)

name = "bruno alves"
# retorna uma cópia da string com espaços adicionados a esquerda até o tamanho
# máximo definido, se a string for menor que esse tamanho a string original é
# retornada
width = 20
print(f"Inicio = {name}")
print(f"center({width}) -> {name.center(width)}")
print("-" * 30)

name = "bruno alves"
# Este método verifica se a string termina com os caracteres informados, se sim
# true é retornado do contrario false
# endswith possui dois outros parâmetros start e end, start permite
# especificar o index em que a pesquisa começara, ja o end é aonde a pesquisa
# terminara
print(f"Inicio = {name}")

sub = "es"
start = 0
end = None
match = name.endswith(sub, start, end)
print(f"endswith({sub}) -> {match}")
print("-" * 30)

name = "\tBruno\talves\tdos\tsantos"
# Este método permite trocar todos os caracteres de tabulação por espaços
# É possível definir a quantidade de espaços que serão adicionados
tabsize = 5
print(r"Inicio = \tBruno\talves\tdos\tsantos")
print(f"expandtabs({tabsize}) -> {name.expandtabs(tabsize)}")
print("-" * 30)

string = "bruno123"
# Só retorna true se todos os caracteres forem alfa numéricos, ou seja
# letras e números
print(f"Inicio = {string}")
result = string.isalnum()
print(f"isalnum() -> {result}")
print("-" * 30)

string = "Bruno"
# Só retorna true se todos os caracteres forem alfabéticos
# Ou seja só letras so alfabeto A a Z, a a z
print(f"Inicio = {string}")
result = string.isalpha()
print(f"isalpha() -> {result}")
print("-" * 30)

string = "bruno"
# Retorna true se todas as letras possíveis tiverem em minusculas
print(f"Inicio = {string}")
result = string.islower()
print(f"islower() -> {result}")
print("-" * 30)

string = "BRUNO"
# Retorna true se todas  as letras possíveis tiverem em maiúsculas
print(f"Inicio = {string}")
result = string.isupper()
print(f"isupper() -> {result}")
print("-" * 30)

string = "Bruno Alves"
# só retorna true se a formatação da string tiver em title case
# com todas as primeiras letras em maiúsculas
print(f"Inicio = {string}")
result = string.istitle()
print(f"istitle() -> {result}")
print("-" * 30)

string = "   "
# retorna true se a string for composta apenas de espaços
print(f"Inicio = {string}")
result = string.isspace()
print(f"isspace() -> {result}")
print("-" * 30)

string = "Bruno Alves dos santos"
# Retorna o número de ocorrências da sub string passada como argumento
print(f"Inicio = {string}")
sub = "o"
start = 0
end = None
result = string.count(sub, start, end)
print(f"count({sub}, {start}, {end}) -> {result}")
print("-" * 30)

string = "Bruno Alves dos santos"
# Retorna o menor index, pesquisando sa esquerda para direita, da string
# onde sub é encontrado
print(f"Inicio = {string}")
sub = "A"
start = 0
end = None
result = string.find(sub, start, end)
print(f"find({sub}, {start}, {end}) -> {result}")
print("-" * 30)

string = "Bruno Alves dos santos"
# Retorna o maior index, pesquisando da direita para esquerda, da string
# onde sub é encontrado
print(f"Inicio = {string}")
sub = "o"
start = 0
end = None
result = string.rfind(sub, start, end)
print(f"rfind({sub}, {start}, {end}) -> {result}")
print("-" * 30)
