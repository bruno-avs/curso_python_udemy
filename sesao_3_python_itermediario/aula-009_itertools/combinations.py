from itertools import combinations, combinations_with_replacement
combinacoes = [1, 3, 4]
# este método retorna retorna, em forma de iterador, todas as combinações ( em grupos,
# tamanho definido no segundo argumento ) possíveis em um iterável
# considerando um elemento como unico pela sua posição e não pelo seu valor
conb_possiveis = combinations(combinacoes, 2)

combinacoes.append(3)
comb_possiveis_2 = combinations(combinacoes, 3)

for comb in conb_possiveis:
    print(comb, next(comb_possiveis_2), sep=' #### ')

# este outro método abaixo faz o mesmo que o de cima a única diferença é que
# os elementos individuais podem se repetir
combs = [1, 2, 3]

all_combs = combinations_with_replacement(combs, 2)

print([v for v in all_combs])
