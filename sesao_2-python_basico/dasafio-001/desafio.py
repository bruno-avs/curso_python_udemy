# dasafio
current_year = 2022
nome = "Bruno "
sobrenome = "alves dos santos"
nome_completo = nome + sobrenome
idade = 20
peso = 70.1
altura = 1.75

imc = peso / altura ** 2
ano_nacimento = current_year - idade

print(f"{nome_completo} tem {idade} anos.")
print(f"Nacido em {ano_nacimento}.")
print(f"Seu peso é de {peso} kg, sua altura {altura:.2f} cm, seu imc é de {imc:.2f}.")