lista_de_lista_de_ints = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 3, 3, 5, 7, 8, 10, 9],
    [10, 2, 3, 4, 4, 1, 2, 1, 4, 2],
    [1, 2, 5, 7, 1, 2, 3, 4, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
    [1, 2, 3, 3, 3, 5, 7, 8, 10, 9],
    [10, 2, 3, 4, 4, 1, 2, 1, 4, 2],
    [1, 2, 5, 7, 1, 2, 2, 3, 4, 10],
    [1, 2, 3, 1, 1, 2, 5, 6, 2, 10],
    [10, 2, 3, 4, 4, 1, 2, 1, 4, 2],
]


def find_the_duplicate(list_numb):
    numbs_iterated = []
    duplicate_numb = -1
    for numb in list_numb:
        if numb not in numbs_iterated:
            numbs_iterated.append(numb)
            continue
        duplicate_numb = numb
    return duplicate_numb

print(find_the_duplicate(lista_de_lista_de_ints[4]))
