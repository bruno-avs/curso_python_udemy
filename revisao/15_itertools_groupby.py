from itertools import groupby
"""
https://www.geeksforgeeks.org/itertools-groupby-in-python/
https://docs.python.org/3/library/itertools.html#itertools.groupby
"""
# groupby permite basicamente reunir valores em grupos

alunos = [
    {"name": "bruno", "nota": 10},
    {"name": "marcos", "nota": 10},
    {"name": "José", "nota": 8},
    {"name": "letícia", "nota": 9.5},
    {"name": "vitória", "nota": 8},
    {"name": "lucas", "nota": 6},
    {"name": "enzo", "nota": 7.5},
]
# para que a função funcione corretamente é necessário ordenar os valores

alunos.sort(key=lambda aluno: aluno["nota"], reverse=True)

order_groups = groupby(alunos, lambda aluno: aluno["nota"])

for group in order_groups:
    nota, alunos = group
    print(nota, list(alunos))
