from collections.abc import Iterable
from typing import Any, Iterator
from itertools import count


class MyList(Iterable):
    def __init__(self, *data: Any) -> None:
        zipped = zip(count(), data)
        self._data = dict(zipped)
        self._next_index = 0

    def append(self, *values: Any):
        last_index = len(self._data) + 1

        for value in values:
            self._data.update({last_index: value})
            last_index += 1

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self._next_index >= len(self._data):
            self._next_index = 0
            raise StopIteration()

        next_value = self._data[self._next_index]
        self._next_index += 1
        return next_value

    def __len__(self) -> int:
        return self._data.popitem()[0]

    def __getitem__(self, index) -> Any:
        return self._data[index]

    def __setitem__(self, index, value) -> None:
        self._data[index] = value

    def __repr__(self) -> str:
        (*values,) = self._data.values()
        return f"{values}"


if __name__ == "__main__":
    my_list = MyList(1, 2, 3, "name")
    print(my_list)
