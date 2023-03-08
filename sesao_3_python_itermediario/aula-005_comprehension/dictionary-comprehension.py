lista = [
    ['chave-0', 'valor'],
    ['chave-1', 'valor'],
    ['chave-2', 'valor']
]
new_dick = {k: v + k for k, v in lista}
new_set = {k + " " + v for k, v in lista}
print(new_set)
print(new_dick)

