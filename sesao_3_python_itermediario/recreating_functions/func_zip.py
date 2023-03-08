
def my_zip(*__iters: list | tuple):
    size_of_smallest_iter = min([len(iterable) for iterable in __iters])

    for key in range(size_of_smallest_iter):
        pairing: tuple = ()
        for iter in __iters:
            pairing += (iter[key],)
        yield pairing


zips = my_zip([1, 2, 3], [1, 2, 3], [1, 2])

for zip in zips:
    print(zip)
