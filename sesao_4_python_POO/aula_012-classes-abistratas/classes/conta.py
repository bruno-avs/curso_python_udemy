from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, nome: str, sobrenome: str, agg: str, numero_conta: str) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self._agg = agg
        self._numero_conta = numero_conta
        self._saldo = 0.0

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            print('valor invalido!!!!')
            return
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def register_card(self, limite):
        pass

    @property
    def agg(self):
        return self._agg

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor