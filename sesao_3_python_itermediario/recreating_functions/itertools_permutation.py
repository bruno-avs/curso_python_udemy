from typing import Iterable
# from itertools import permutations
# print(list(permutations([1, 2, 3])))


def permutations(iterable: Iterable, r: int | None = None):
    to_permutation = tuple(iterable)

    length = len(to_permutation)
    r = length if r is None else r

    if r > length:
        return

    indexes = list(range(length))
    cycles = list(range(length, length-r, -1))
    yield tuple(to_permutation[i] for i in indexes[:r])

    while length:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indexes[i:] = indexes[i+1:] + indexes[i:i+1]
                cycles[i] = length - i
            else:
                j = cycles[i]
                indexes[i], indexes[-j] = indexes[-j], indexes[i]
                yield tuple(to_permutation[i] for i in indexes[:r])
                break
        else:
            return


d = permutations([1, 2, 3], r=2)
