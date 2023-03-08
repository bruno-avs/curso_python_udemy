from itertools import combinations_with_replacement
"""
https://www.geeksforgeeks.org/python-itertools-combinations-function/
https://inventwithpython.com/blog/2021/07/03/combinations-and-permutations-in-python-with-itertools/
https://docs.python.org/3/library/itertools.html
"""
# este método é idêntico a combinations a única diferença é que os elementos
# considerados únicos por index podem se repetir

item_1 = ["A", "B", "C"]
combi = combinations_with_replacement(item_1, 2)

print(list(combi))
