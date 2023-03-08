from conta import Conta
from cartao import Cartao


class ContaCorrente(Conta):
    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            print('Valor informado é invalido!!')

            return

        if valor > self.saldo:
            print('Saldo insuficiente')
            return

        self._saldo -= valor

    def register_card(self, limite):
        funcao = 'Débito e Crédito'

        cartao = Cartao(
            self.nome,
            self.sobrenome,
            self.agg,
            self.numero_conta,
            limite,
            funcao
        )
