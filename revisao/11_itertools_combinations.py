from itertools import combinations
"""
https://www.geeksforgeeks.org/python-itertools-combinations-function/
https://inventwithpython.com/blog/2021/07/03/combinations-and-permutations-in-python-with-itertools/
https://docs.python.org/3/library/itertools.html
"""
item_1 = ["A", "B", "C"]
# O método combinations permite nos dar todas as combinações entre os valores
# em um iterável
# os elementos são considerados únicos não pelo seu valor e sim pelo seu index
comb_1 = combinations(item_1, 1)
comb_2 = combinations(item_1, 2)
comb_3 = combinations(item_1, 3)

comb_1_list = list(comb_1)
comb_2_list = list(comb_2)
comb_3_list = list(comb_3)

comb_1_list.extend(comb_2_list)
comb_1_list.extend(comb_3_list)

print(comb_1_list)  # todas as combinações realmente possiveis
