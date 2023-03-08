from itertools import permutations

# retorna todas as combinações possiveis em um iteravel,
# usando permutação ( troca de possição )

list = ["p", "I", "A", "A"]
all_combs = permutations(list, 2)
print([v for v in all_combs])


# formula para calcular uma permutação simples
def permutation_simple(n):
    if n == 0:
        return 1
    else:
        return n * permutation_simple(n - 1)


permit_simp = permutation_simple(4)
print(permit_simp)


# formula de caucular permutação complexa

def complex_permutations(list):
    values_check = []
    repets = []
    for n in list:
        if list.count(n) != 1:
            if n not in values_check:
                repets.append(list.count(n))
                values_check.append(n)

    def fatorial(v):
        if v == 0:
            return 1
        else:
            return v * fatorial(v - 1)

    len_list = len(list)
    fator_list = fatorial(len_list)

    mult_repets = 1
    for v in repets:
        mult_repets *= fatorial(v)

    return fator_list / mult_repets

result = complex_permutations([1, 2, 2, 2, 1, 3, 4])
print(result)
