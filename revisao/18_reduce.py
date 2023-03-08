"""
https://realpython.com/python-reduce-function/ 
"""
from functools import reduce


lista = [0, 6, 3, 7, 1, 9, 5, 6, 1, 2, 4]


def reduce_func(acc, curr_item):
    curr_str = str(curr_item)
    if len(acc) == 2:
        return acc + curr_str + "."
    if len(acc) == 6:
        return acc + curr_str + "."
    if len(acc) == 10:
        return acc + curr_str + "-"
    return acc + curr_str


str_lista = reduce(reduce_func, lista, "")

print(str_lista)