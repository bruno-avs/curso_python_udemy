"""
Um método statico é como uma função normal, portanto ela não  tem acesso a instância( self )
e nem a classe ( cls )

Ela pode ser chamada atraves da instância e da classe
"""


class Mouse:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def diga(texto):
        print(texto)


mouse = Mouse('Ryzer')
print(mouse.name)
print('=================')
mouse.diga('bom mause')
print('=================')
Mouse.diga('legal mouse')


