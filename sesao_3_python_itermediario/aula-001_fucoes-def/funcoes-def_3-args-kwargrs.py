lista = [1, 2, 3, 4, 5, 6]
print(*lista)  # desempacotando uma lista inteira


def function(*args, **kwargs):
    print(args, kwargs)
    print(kwargs.get('nome', 'ola'))


function(1, 2, 3, 4, nome='bruno', sobrenome='alves')
