"""
Fatiamento de strings

indices positivos
[0, 1, 2, 3, 4]

indices negativos
[-1, -2, -3, -4]
"""
string = "python_s2"

splited_str = string[0:6] # [inicio:fim:passo]
ultimo = string[-1]
primeiro = string[0]
passos = string[0::2]

print(splited_str, ultimo, primeiro, passos)