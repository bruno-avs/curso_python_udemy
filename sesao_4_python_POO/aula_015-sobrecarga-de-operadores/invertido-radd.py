from typing import Union, NewType

number = NewType('number', Union[int, float])


class Cilindro:
    def __init__(self, x: number, y: number, comp: number):
        self.x = x
        self.y = y
        self.comp = comp

    def __add__(self, other):
        print('__add__')
        val_X: number = self.x + other
        val_y: number = self.y + other
        val_comp: number = self.comp + other
        return Cilindro(val_X, val_y, val_comp)

    def __radd__(self, other):
        print('__add__')
        val_X: number = other + self.x
        val_y: number = other + self.y
        val_comp: number = other + self.comp
        return Cilindro(val_X, val_y, val_comp)


cilindro_1 = Cilindro(57, 49, 300)
cilindro_2 = Cilindro(30, 45, 800)

cilindro_3 = 20 + cilindro_1
cilindro_4 = cilindro_2 + 90

print(cilindro_3.x)
print(cilindro_4.x)