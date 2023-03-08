# iteraveis são strings, listas, tuplas, dicionarios

lista = [1, 2, 3, 4, 5, 5, 6]
print(lista)
print(hasattr(lista, '__iter__')) # esta função verifica se um objeto tem na sua herança determinado método
print(hasattr(lista,'__next__'))

lista = iter(lista)  # tranforma um iteravel em um iterador
print(lista)
print(hasattr(lista,'__next__'))
print(hasattr(lista, '__iter__'))
print(next(lista))  # para acessar um valor de um iterador é necessario
                    # usaro método next que retorna o proximo valor em um iterador
