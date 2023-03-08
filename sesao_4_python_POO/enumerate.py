from typing import Iterable


class MyEnumerate:
    def __init__(self, iterable: Iterable, start: int = 0) -> None:
        self.__iterable = iterable
        self.__start = start
        self.__curr_key = 0

    def __iter__(self):
        return self

    def __next__(self):
        iterable = self.__iterable
        curr_key = self.__curr_key
        start = self.__start

        length_iter = len(iterable)

        if curr_key >= length_iter:
            raise StopIteration

        curr_value = (start, iterable[curr_key])
        
        self.__start += 1
        self.__curr_key += 1
        return curr_value


for j in MyEnumerate(["1", "d", "f"]):
    print(j)
