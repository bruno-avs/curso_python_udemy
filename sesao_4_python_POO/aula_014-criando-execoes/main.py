"""
Crie exeções quandos nenhuma das exeções existentes em python forem compatives
com o tipo de erro que você queira representar.
"""

class myExeptionError(Exception):
    pass


def Calcular(v1, v2):
    if not isinstance((v1, v2), (float, int)):
        raise myExeptionError('errrrr')
    total = v1 + v2

calcular = Calcular(1,'oo')
