from typing import Iterator


def my_count(start: int = 0, step: int = 1) -> Iterator:
    c: int = start
    while True:
        c += step
        yield c


for c in my_count():
    print(c)
    if c == 10:
        break
