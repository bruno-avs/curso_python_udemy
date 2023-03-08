class Person:
    def __init__(self, name: str, last_name: str, old: int, cpf: str) -> None:
        self._name = name
        self._last_name = last_name
        self._full_name = f"{name} {last_name}"
        self._old = old
        self._CPF = cpf

    @property
    def name(self) -> str:
        return self._name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def full_name(self):
        return self._full_name

    @property
    def old(self) -> int:
        return self._old

    @property
    def CPF(self):
        return self._CPF


class Client(Person):
    def __init__(self, name: str, last_name: str, old: int, cpf: str) -> None:
        Person.__init__(self, name, last_name, old, cpf)
        self.__current_account = None
        self.__savings_account = None

    @property
    def current_account(self):
        return self.__current_account

    @current_account.setter
    def current_account(self, account: object):
        self.__current_account = account

    @property
    def savings_account(self):
        return self.__savings_account

    @savings_account.setter
    def savings_account(self, account: object):
        self.__savings_account = account
