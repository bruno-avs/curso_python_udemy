def gerador():  # para criar uma função geradora basta trocar a palavra chave return pela yield
    for n in range(10):
        yield n

var = gerador()
print(next(var))  # retorna um objeto iteravel (iterador) a cada execução
print(next(var))

iterable = (n for n in range(10))  # exirte uma forma mais
                                   # simplificada de criar um gerador



