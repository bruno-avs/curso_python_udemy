from abc import ABC, abstractmethod
from typing import NewType, Union

monetary = NewType("monetary", Union[int, float])


class Account(ABC):
    def __init__(
            self,
            agency: int,
            acc_number: int,
            acc_type: str,
            balance: monetary
    ) -> None:

        self.__agency = agency
        self.__acc_number = acc_number
        self.__acc_type = acc_type
        self.balance = balance

    def deposit(self, value: monetary) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f'the amount cannot be deposited -> {value}')

        self._balance += value

    @abstractmethod
    def withdraw(self, value: monetary) -> None:
        pass

    @property
    def agency(self):
        return self.__agency

    @property
    def acc_number(self):
        return self.__acc_number

    @property
    def acc_type(self):
        return self.__acc_type

    @property
    def balance(self) -> monetary:
        return self._balance

    @balance.setter
    def balance(self, value: monetary) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f'value cannot be set -> {value}')

        self._balance = value


class CurrentAccount(Account):
    def __init__(
            self,
            agency: int,
            acc_number: int,
            acc_type: str,
            balance: monetary
    ) -> None:
        Account.__init__(self, agency, acc_number, acc_type, balance)
        self.__max_limit = 2000
        self.__curr_limit = 0
        self.__credit = 0

    def increase_limit(self, value: monetary) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"this type of value is not accepted -> {value}")

        if (self.__curr_limit + value) > 2000:
            print(
                f'Não é possivel mais almentar o limite.\n'
                f'Limite maximo: R$ {self.__max_limit}.\n'
                f'Limite atual: R$ {self.__curr_limit}.'
            )
            return

        self.__curr_limit += value

    def increase_credit(self, value: monetary) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"this type of value is not accepted -> {value}")

        if self._balance < 0:
            print(
                'Almento de crédito recusado.\n'
                'Seu saldo está negativado!!.'
            )
            return
        self.__credit += value

    def withdraw(self, value: monetary) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"this type of value is not accepted -> {value}")

        if self._balance < -self.__curr_limit:
            print('Limite maximo de saque atingido!!!!.')
            return

        self._balance -= value

    @property
    def max_limit(self):
        return self.__max_limit

    @property
    def curr_limit(self):
        return self.__curr_limit

    @property
    def credit(self):
        return self.__credit


class SavingsAccount(Account):
    def withdraw(self, value: monetary) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"this type of value is not accepted -> {value}")

        self._balance -= value
