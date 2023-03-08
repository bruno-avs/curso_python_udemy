from data import products, people
from functools import reduce

soma_de_preco = reduce(lambda ac, p: p['value'] + ac, products, 0)
soma_de_idades = reduce(lambda ac, old: old['old'] + ac, people, 0)
so_named = reduce(lambda ac, n: ac + n['name'], people, 'ola')
print(soma_de_preco)
print(soma_de_idades / len(people))
print(so_named)



