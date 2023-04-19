from abc import ABC, abstractmethod
from src.new_exceptions import BankOperationError
from src.government import PhysicalPerson


class Account(ABC):
    def __init__(
        self,
        personal_data: PhysicalPerson,
        agency: str,
        account_number: str,
        email: str,
        password: str

    ) -> None:
        self.agency = agency
        self.account_number = account_number
        self._personal_data = personal_data
        self.__email = email
        self.__password = password

        self.__saldo = 0

    @property
    def saldo(self):
        return self.__saldo

    def _authenticate(self, email: str, password: str) -> None:
        if not email == self.__email:
            raise ValueError("incorrect email.")
        if not password == self.__password:
            raise ValueError("incorrect Password.")

    def see_balance(self) -> None:
        print(f"Your balance is {self.saldo}.")

    @abstractmethod
    def to_withdraw(self, value: int, email: str, password: str) -> None:
        pass

    @abstractmethod
    def to_deposit(self, value: int, email: str, password: str) -> None:
        pass


class CurrentAccount(Account):
    def __init__(
        self,
        personal_data: PhysicalPerson,
        agency: str,
        account_number: str,
        email: str,
        password: str
    ) -> None:
        super().__init__(
            personal_data, agency, account_number, email, password)
        self.__limit = -500
        self.__credit = 1000

    @property
    def limit(self):
        return self.__limit

    @property
    def credit(self):
        return self.__credit

    def get_loan(self, value: int, email: str, password: str) -> None:
        if value < self.__credit:
            raise BankOperationError(
                "Credit withdrawal value cannot be less than 0.")
        if value > self.__credit:
            raise BankOperationError(
                "The credit withdrawal amount cannot be greater than the "
                "credit offered")

        self._authenticate(email, password)
        self.__credit - value

    def to_withdraw(self, value: int, email: str, password: str) -> None:
        if value <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self._authenticate(email, password)

        saldo = self.__saldo - value

        if saldo < self.__limit:
            raise BankOperationError(
                "operation denied, the negative "
                "balance limit has been reached.")

        self.__saldo = saldo

    def to_deposit(self, value: int, email: str, password: str) -> None:
        if value <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        self._authenticate(email, password)

        self.__saldo += value


class SavingsAccount(Account):
    def to_withdraw(self, value: int, email: str, password: str) -> None:
        if value < self.__saldo:
            raise BankOperationError(
                "The withdrawal amount cannot be less than 0.")
        if value > self.__saldo:
            raise BankOperationError(
                "the withdrawal amount cannot be greater "
                "than the account balance.")

        self._authenticate(email, password)

        self.__saldo -= value

    def to_deposit(self, value: int, email: str, password: str) -> None:
        if value < 0:
            raise ValueError(
                "The amount to be deposited must be greater than 0.")

        self._authenticate(email, password)
        self.__saldo += value
