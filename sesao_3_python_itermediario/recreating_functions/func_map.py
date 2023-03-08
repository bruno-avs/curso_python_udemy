from typing import Callable, Iterable, Any


def map(func: Callable, iter: Iterable) -> Iterable[Any]:
    if not callable(func):
        raise TypeError(
            "O primeiro parâmetro deve ser uma função.")
    if not isinstance(iter, Iterable):
        raise TypeError("O segundo parâmetro deve ser um iterável.")

    for v in iter:
        yield func(v)


my_list = [1, 2, 3, 4, 5]

print(list(map(func=lambda a: a * 2, iter=my_list)))
