"""
você pode usar variaveis no meio de strings na função print ultilizando o f strings
"""
nome = "Bruno"
sobrenome = "alves"
idade = 20
peso = 70.1
altura = 1.75
imc = peso / altura ** altura

print(f"{nome} {sobrenome}, tem {idade}, seu imc é de {imc:.2f}")
# :.2f, permite formatar um número com duas casas decimais

# Outra forma de ultilizar varíaveis dentro de strings na função print
# é usando a função format no final da string
print("{} {}, tem {}, seu imc é de {:.2f}".format(nome, sobrenome, idade, imc))
# cada chaves é referente a posição da varíavel dentro do format

print("{0} {2}, tem {3}, seu imc é de {3:.2f}".format(nome, sobrenome, idade, imc))
# você pode ultilizar o index referente a posição das varíaveis no format
# para mudar a orden de exibissão

print("{n} {s}, tem {i}, seu imc é de {im:.2f}".format(n=nome, s=sobrenome, i=idade, im=imc))
# você tmabem pode renomear as variaveis, podendo mudar a ordem de exibição


