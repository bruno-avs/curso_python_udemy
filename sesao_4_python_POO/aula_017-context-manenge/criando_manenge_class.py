class ContextManange:
    def __init__(self, name_file, mode):
        self.file = open(name_file, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.file.close()
            print('Arquivo fechado com sucesso')
        except AttributeError:
            print('Arquivo não pode ser fechado')

            return True



with ContextManange('obs.txt', 'w+') as file:
    file.write('Ola')
