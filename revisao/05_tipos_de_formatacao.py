"""
https://cienciaprogramada.com.br/2022/03/formatacao-strings-python/#Metodo_format
"""
"""
Este estilo de formatação permite predefinir o tamanho da string, que ao
ultrapassar o tamanho prè definido caracteres são adicionados para compor
os espaços
"""
name = "Bruno"
# Adiciona a partir do centro
print(f"Ola, {name:^10}.")
print("-" * 20)

# Adiciona do lado direito
print(f"Ola, {name:<10}.")
print("-" * 20)

# Adiciona do lado esquerdo
print(f"Ola, {name:>10}.")
print("-" * 20)

"""Este estilo permite formatar números int e float"""
print("#" * 20)
valor_pos = 1000
valor_neg = -1000

# O sinal = permite adicionar um espaço ou um caracter entre o sinal e o número
print(f"{valor_pos:=10}")
print(f"{valor_neg:=10}")
print("-" * 20)
# use sempre o sinal de mais para que o número seje exibido como negativo
# ou positivo
print(f"{valor_pos:+}")
print(f"{valor_neg:+}")
print("-" * 20)

# Com o negativo o sinal de mais sera omitido
print(f"{valor_pos:-}")
print(f"{valor_neg:-}")
print("-" * 20)

# Use " " (um espaço) para adicionar astomaticamente quando o número for
# positivo
print(f"{valor_pos: }")
print(f"{valor_neg: }")
print("-" * 20)
# você pode usar uma virgula como o separador de milhar
print(f"{valor_pos:,}")
print(f"{valor_neg:,}")
print("-" * 20)
