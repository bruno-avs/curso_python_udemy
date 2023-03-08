"""
https://www.w3schools.com/python/ref_func_filter.asp
"""
# O método filter executa uma função para cada item de um iterável
# parecido com map, a diferença é que este só filtra os valores

alunos = [
    {"name": "bruno", "nota": 10},
    {"name": "marcos", "nota": 10},
    {"name": "José", "nota": 8},
    {"name": "letícia", "nota": 9.5},
    {"name": "vitória", "nota": 8},
    {"name": "lucas", "nota": 6},
    {"name": "enzo", "nota": 7.5},
]

so_10 = filter(lambda aluno: aluno["nota"] >= 10, alunos)

print(list(so_10))