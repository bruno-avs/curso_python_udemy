class Pessoa:
    def __init__(self, name: str, last_name: str, old: int) -> None:
        self.name = name
        self.last_name = last_name
        self.full_name = f'{self.name} {self.last_name}'.title()
        self.old = old

    def falar(self) -> None:
        print(f'{self.full_name} está falando da classe pessoa......')


class Estudante(Pessoa):
    def estudar(self) -> None:
        print(f'{self.full_name} está estudando.....')

    def parar_estudar(self) -> None:
        print(f'{self.full_name} parou de estudar.....')

    def falar(self) -> None:
        print(f'{self.full_name} está falando da classe estudante......')


class Cliente(Pessoa):
    def comprar(self) -> None:
        print(f'{self.full_name} está comprando.....')

    def parar_comprar(self) -> None:
        print(f'{self.full_name} parou de comprar.....')

    def falar(self) -> None:
        print(f'{self.full_name} está falando da classe cliente......')

class ClienteVIP(Cliente):
    def __init__(self, name: str, last_name: str, old: int) -> None:
        Pessoa.__init__(self, name, last_name, old)
        self.credit = 'R$ 100.00'
