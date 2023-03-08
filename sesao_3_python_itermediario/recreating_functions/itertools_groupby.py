from itertools import groupby
from typing import Iterable, Callable
alunos = [
    {'name': 'bruno', 'nota': 'A'},
    {'name': 'joão', 'nota': 'B'},
    {'name': 'gustavo', 'nota': 'D'},
    {'name': 'algusto', 'nota': 'C'},
    {'name': 'pedro', 'nota': 'A'},
    {'name': 'guilherme', 'nota': 'B'},
    {'name': 'inacío', 'nota': 'A'},
    {'name': 'cleber', 'nota': 'D'},
    {'name': 'brenner', 'nota': 'C'},
]

alunos.sort(key=lambda s: s["nota"])
lista = sorted([1, 2, 3, 3, 3, 3, 2])

for j in groupby(lista):
    print(j[0], list(j[1]))


def my_groupby(iterable: Iterable, key: None = None):
    def closer(func):
        return func

    grouping_func: Callable = closer(lambda v: v)

    if key is not None:
        grouping_func = closer(key)

    last_grouping_value = None
    for v in iterable:
        grouping_value = grouping_func(v)

        if grouping_value == last_grouping_value:
            continue

        last_grouping_value = grouping_value

        group_values: list = []
        for v2 in iterable:
            group_value = grouping_func(v2)

            if group_value == v:
                group_values.append(v2)

        yield grouping_value, group_values


print()

for i in my_groupby(lista):
    p = dict({i[0]: i[1]})
    print(p)
