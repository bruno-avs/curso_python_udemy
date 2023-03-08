"""
Polimorfismo é um principio que permite que classes que são derivadas de uma mesma superclass
tenham métodos com mesmo nome e assinatura mas com comportamentos diferentes.
"""
from abc import ABC, abstractmethod


class ABCClass(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def printar(self, valor):
        pass


class ChildABC(ABCClass):
    def printar(self, valor):
        print(valor)


childABS = ChildABC()

childABS.printar('ola')
