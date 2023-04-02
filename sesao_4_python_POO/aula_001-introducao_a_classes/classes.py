class Telephone:
    switched_on = False

    def __init__(
            self, brand, model, RAM
    ):
        self.brand = brand
        self.model = model
        self.RAM = RAM

    def turn_on(self):
        print(f'Ligando {self.model}....')

        if not self.switched_on:
            self.switched_on = True
        else:
            print(f'O aparelho {self.model} já está ligado.')

        print(f'O {self.model} está ligado.')

    def turn_off(self):
        print(f'Desligando {self.model}....')

        if self.switched_on:
            self.switched_on = False


Telephone('apple', 'iphone 11', '8gb')
