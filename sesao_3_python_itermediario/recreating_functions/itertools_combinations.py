# from itertools import combinations
from typing import Iterable


def my_combinations(iterable: Iterable, r: int = 2):
    to_combine = tuple(iterable)

    length_combine = len(to_combine)

    if r > length_combine:
        return

    indexes = list(range(r))
    yield tuple(to_combine[i] for i in indexes)
    while True:
        for i in reversed(range(r)):
            if indexes[i] != i + length_combine - r:
                break
        else:
            return
        indexes[i] += 1

        for i2 in range(i + 1, r):
            indexes[i2] = indexes[i2 - 1] + 1
        yield tuple(to_combine[i] for i in indexes)


print(list(my_combinations([1, 2, 3], r=3)))
