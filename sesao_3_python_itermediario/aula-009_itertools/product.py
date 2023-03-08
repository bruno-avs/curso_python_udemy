from itertools import product
lista = [1,2]
lista_1 = [1,2]
lista_2 = [1,2]

produto_cartesiano = product(lista, lista_1, lista_2, repeat=2)
for v in produto_cartesiano:
    print(v)