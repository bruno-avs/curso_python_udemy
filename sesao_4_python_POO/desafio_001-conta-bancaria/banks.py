from all_class.accounts import SavingsAccount, CurrentAccount
from all_class.persons import Client
from random import randint



class Bank:
    def __init__(self, bank_name: str, agency: int) -> None:
        self._bank_name = bank_name
        self._agg = agency
        self._acc_type = None
        self.__accounts = []

    @staticmethod
    def generate_acc_number() -> int:
        numb_acc = str(randint(100000, 999999))
        return int("000" + numb_acc)

    def acc_already_exists(self, cpf: str) -> bool:
        for client in self.__accounts:

            if self._acc_type == "current":

                exist_curr = cpf == client.CPF \
                             and client.current_account.acc_type \
                             == self._acc_type

                if exist_curr:
                    return True

            elif self._acc_type == "savings":

                exist_savings = cpf == client.CPF \
                                and client.current_account.acc_type \
                                == self._acc_type

                if exist_savings:
                    return True
            return False

    def create_current_account(
            self,
            name: str,
            last_name: str,
            old: int,
            cpf: str
    ) -> None:
        self._acc_type = "current"
        exists = self.acc_already_exists(cpf)

        if exists:
            print('Opa!! parece que você já possue uma conta em nosso banco.')
            return

        client = Client(name, last_name, old, cpf)

        acc_number = self.generate_acc_number()

        client.current_account = CurrentAccount(
            agency=self._agg,
            acc_number=acc_number,
            acc_type=self._acc_type,
            balance=0
        )
        self.__accounts.append(client)

    def create_savings_account(
            self,
            name: str,
            last_name: str,
            old: int,
            cpf: str

    ):
        self._acc_type = "savings"

        exists = self.acc_already_exists(cpf)

        if exists:
            print('Opa!! parece que você já possue uma conta em nosso banco.')
            return

        client = Client(name, last_name, old, cpf)

        acc_number = self.generate_acc_number()
        client.savings_account = SavingsAccount(
            agency=self._agg,
            acc_number=acc_number,
            acc_type=self._acc_type,
            balance=0
        )
        self.__accounts.append(client)

    def __repr__(self):
        return f"Class name: {__class__.__name__}\n" \
               f"\tbank name: {self._bank_name}\n" \
               f"\tAgency: {self._agg}\n" \
               f"\tAll account: {self.__accounts}\n" \
               f"-------------------------------"
