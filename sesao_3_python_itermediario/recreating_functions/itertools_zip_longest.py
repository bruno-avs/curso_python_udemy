
def my_zip_longest(*__iters: list | tuple, fill_value: object = None):
    size_of_largest_iterable = max([len(iter) for iter in __iters])

    for key in range(size_of_largest_iterable):
        pairing: tuple = ()
        for iter in __iters:
            if key >= len(iter):
                pairing += (fill_value,)
                continue
            pairing += (iter[key],)

        yield pairing


list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3]

for pairing in my_zip_longest(list_1, list_2, list_3):
    print(pairing)
