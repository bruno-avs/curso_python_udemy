"""
considerando duas listas de inteiros ou folats, some os valores entre as listas
e retorne os valores somados em uma nova lista.

se uma lista for maior que a outra< a soma só vai considerar o tamanho da menor.
"""
from itertools import zip_longest

numbers_A = [1, 3, 6, 10, 2, 2.5, 2.9, 11]
numbers_B = [7, 2, 4, 17, 5.6, 4.9]

new_list = zip(numbers_A, numbers_B)
print(new_list)
list_sum = [v1 + v2 for v1, v2 in new_list]
print(list_sum)
print()

# a mesma forma só que mais simplificada

list_sum = [v1 + v2 for v1, v2 in zip(numbers_A, numbers_B)]
print(list_sum)  # o mesmo resultado, só que agora usando apenas uma linha de código
print('#' * 80)

# com zip_longest
sum_list = [v1 + v2 for v1, v2 in zip_longest(numbers_A, numbers_B, fillvalue=0)]

print(sum_list)


