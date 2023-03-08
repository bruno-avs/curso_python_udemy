from typing import Iterable


def join(string: str, __iterable: Iterable[str]) -> str:
    if not isinstance(string, str):
        raise TypeError()

    if not isinstance(__iterable, Iterable):
        raise TypeError()

    assembled: str = string
    for value in __iterable:
        assembled += value
    return assembled
