from typing import Callable, Iterable


def filter(__function: Callable, __iterable: Iterable):
    if not callable(__function):
        raise TypeError(
            "O primeiro parâmetro deve ser uma "
            "função que retorne um boolean.")
    if not isinstance(__iterable, Iterable):
        raise TypeError("O segundo parâmetro deve ser um iterável.")

    for value in __iterable:
        the_value_is_true = __function(value)
        if the_value_is_true:
            yield value


my_list = [1, 7, 2, 0, 1, 29, 77]

print(list(filter(lambda v: v > 2, my_list)))
