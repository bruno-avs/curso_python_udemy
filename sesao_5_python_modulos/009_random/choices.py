import random

name_list = ["Danielly", "Lucas", "Gustavo", "Fernando", "Marcos", "Bruno"]
# normal, retorna uma lista com um valor aleatório
print(random.choices(name_list))
print()
# usando o parâmetro weights, que permite definir de forma relativa
# a probabilidade de cada item da lista
probability = [1, 1, 1, 1, 1, 1]
print(random.choices(name_list, weights=probability))
print()

# usando o parâmetro cum_weights, que permite indicar a probabilidade acumulada
# de repetição de cada elemento
print(random.choices(name_list, cum_weights=probability))
print()

# usando o parâmetro k que indica a quantidade de valores que serão retornado
# de forma aleatória pela função
print(random.choices(name_list, k=2))
print()
