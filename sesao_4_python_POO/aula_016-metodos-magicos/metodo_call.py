class Banco:
    def __init__(self, inicial):
        self.inicial = inicial

    def __call__(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                print(f'O valor {arg} não pode ser adicionado.')
            else:
                self.inicial += arg

banco = Banco(100)

banco(9, 'Ola', 10, 8, None)
print(banco.inicial)