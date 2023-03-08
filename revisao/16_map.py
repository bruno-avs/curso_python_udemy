"""
https://www.w3schools.com/python/ref_func_map.asp
"""
# map basicamente executa uma função para cada item de um iterável

names = ["Bruno", "João", "lucas"]


names_full = map(lambda name: name.upper(), names)

print(list(names_full))

values = [10, 30, 9.50, 12, 32]

values_in_reais = map(lambda value: f"{value} R$", values)

print(list(values_in_reais))
