from itertools import permutations
"""
https://www.geeksforgeeks.org/python-itertools-permutations/
https://www.hackerrank.com/challenges/itertools-permutations/problem
"""
item_1 = [1, 2]
item_2 = [1, 2, 3]
# permutations retorna um iterador de tuplas contendo todas as combinações
# possíveis usando permutação
# todos os elementos são considerados únicos com base em sua posição e não em
# seu valor ou categoria.
per = permutations(item_2, 2)

print(list(per))
