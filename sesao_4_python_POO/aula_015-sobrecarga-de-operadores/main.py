from typing import Union, NewType

number = NewType('number', Union[int, float])


class Cilindro:
    def __init__(self, x: number, y: number, comp: number):
        self.x = x
        self.y = y
        self.comp = comp

    def __add__(self, other):
        print('__add__')
        val_X: number = self.x + other.x
        val_y: number = self.y + other.y
        val_comp: number = self.comp + other.comp
        return Cilindro(val_X, val_y, val_comp)


cilindro_1 = Cilindro(57, 49, 300)
cilindro_2 = Cilindro(30, 45, 800)

cilindro_3 = cilindro_2 + cilindro_1






