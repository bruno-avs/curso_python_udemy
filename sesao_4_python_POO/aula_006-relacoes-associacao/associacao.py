from ferramentas import Martelo, Serrote


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self._ferramenta = None

    def get_ferramenta(self):
        # print('executando => get func')
        return self._ferramenta

    def set_ferramenta(self, ferramenta):
        # print('executando => set func')
        self._ferramenta = ferramenta

    def del_ferramenta(self):
        # print('executando => del func')
        del self._ferramenta

    ferramenta = property(get_ferramenta, set_ferramenta, del_ferramenta)


pessoa = Pessoa('Bruno', '20')

pessoa.ferramenta = Martelo('cabo de madeira')
pessoa.ferramenta.usar()
pessoa.ferramenta = Serrote('Serrote azul')
pessoa.ferramenta.usar()

