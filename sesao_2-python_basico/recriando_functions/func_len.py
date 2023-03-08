from typing import Iterable
# from functools import reduce

# esta é uma representação minha sobre a lógica da função len


def my_len(__obj: Iterable, /) -> int:
    if not isinstance(__obj, Iterable):
        raise TypeError(
            f"object of type '{type(__obj).__name__}' has no len()")
    # Eu percebi que com reduce o código fica menor, mas optei por uma
    # forma mais python de código.
    # return reduce(lambda acc, _: acc + 1, __obj, 0)

    length: int = 0
    for _ in __obj:
        length += 1
    return length


print(my_len("my name"))
