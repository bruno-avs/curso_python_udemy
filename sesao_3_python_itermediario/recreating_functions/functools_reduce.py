from typing import Callable, Iterable, Any


def reduce(function: Callable, iterable: Iterable, initial: Any = None):
    if not callable(function):
        raise TypeError(
            "O primeiro parâmetro deve ser uma função.")
    if not isinstance(iterable, Iterable):
        raise TypeError("O segundo parâmetro deve ser um iterável.")

    init_value: Any
    it = iter(iterable)

    if initial is None:
        init_value = next(it)
    else:
        init_value = initial

    acc = init_value
    for value in iterable:
        acc = function(acc, value)
    return acc


my_list = [1, 7, 2, 0, 1, 29, 77]


def converter_in_str(acc, value):
    return acc + str(value)


reduced_in_str = reduce(converter_in_str, my_list, "")

print(reduced_in_str)
