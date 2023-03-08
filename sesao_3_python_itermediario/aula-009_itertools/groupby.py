from itertools import groupby
# agrupando valores com grupby
alunos = [
    {'name': 'bruno', 'nota': 'A'},
    {'name': 'joão', 'nota': 'B'},
    {'name': 'gustavo', 'nota': 'D'},
    {'name': 'algusto', 'nota': 'C'},
    {'name': 'pedro', 'nota': 'A'},
    {'name': 'guilherme', 'nota': 'B'},
    {'name': 'inacío', 'nota': 'A'},
    {'name': 'cleber', 'nota': 'D'},
    {'name': 'brenner', 'nota': 'C'},
]

order = lambda v: v['nota']
alunos.sort(key=order)
print(alunos)

alunos_grups = groupby(alunos, order)
for nota, grups in alunos_grups:
    print(f'Alunos que tiraram {nota}')
    for aluno in grups:
        aluno['name'] = aluno['name'].title()
        print(f"\t{aluno}")
