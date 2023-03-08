class MyType:
    def __init__(self):
        self.__items = []
        self.__cur_index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError
        if key >= len(self.__items):
            self.__items.append(value)
        else:
            self.__items[key] = value

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if key >= len(self.__items):
            raise IndexError

        return self.__items[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        del self.__items[key]

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cur_index < len(self.__items):
            item = self.__items[self.__cur_index]
            self.__cur_index += 1
            return item
        else:
            raise StopIteration

    def __str__(self):
        return f"{__class__.__name__}{self.__items}"


my_type = MyType()

my_type.add(12)
my_type.add(12)
my_type.add(12)


for v in my_type:
    print(v)
