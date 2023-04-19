from src.database_managers import BankDataManager
from src.government import PhysicalPerson
from src.accounts import CurrentAccount, SavingsAccount, Account
import random
import os
import re


class Bank:
    def __init__(
        self,
        bank_name: str,
        agency: str,
        bank_id: int,
    ) -> None:
        self.bank_name = bank_name
        self.agency = agency
        self.bank_id = bank_id

        self._database_address: str = os.path.join(
            os.getcwd(),
            f"{bank_name}_database.json"
        )
        self._database: BankDataManager | None = None

    def set_database(self, path_to_database_folder: str) -> None:
        if not os.path.isdir(path_to_database_folder):
            raise ValueError(
                "The path to the database folder must be valid and exist.")

        self._database_address = path_to_database_folder

    def _generate_account_number(self):
        numbers = str(random.randint(1000000, 9999999))
        if numbers == numbers[::-1]:
            return self._generate_account_number()

        digit = str(random.randint(0, 9))
        return numbers + "-" + digit

    def _validate_registration_data(
        self,
        personal_data: PhysicalPerson,
        email: str,
        password: str
    ) -> bool:
        if isinstance(personal_data, PhysicalPerson):
            raise TypeError(
                '"personal_data" must be an instance of "PhysicalPerson".')

        email_regex = re.compile(r"[\w]{5,50}@gmail.com")
        email_is_valid = email_regex.search(email)

        if email_is_valid is None:
            raise ValueError("The email entered is not valid")
        if len(password) < 8:
            raise ValueError("the password entered is too weak")

        return True

    def create_physical_person_saving_account(
        self,
        personal_data: PhysicalPerson,
        email: str,
        password: str
    ) -> None:
        self._validate_registration_data(personal_data, email, password)

        account_number = self._generate_account_number()

        new_account = SavingsAccount(
            personal_data, self.agency, account_number, email, password)

        if self._database is None:
            self._database = BankDataManager(
                self._database_address, self.bank_name, self.bank_id)

        self._database.post_account(new_account)

    def create_physical_person_checking_account(
        self,
        personal_data: PhysicalPerson,
        email: str,
        password: str
    ) -> None:
        self._validate_registration_data(personal_data, email, password)

        account_number = self._generate_account_number()

        new_account = CurrentAccount(
            personal_data, self.agency, account_number, email, password)

        if self._database is None:
            self._database = BankDataManager(
                self._database_address, self.bank_name, self.bank_id)

        self._database.post_account(new_account)

    def login_in_account(self, account_number: str) -> Account:
        if self._database is None:
            self._database = BankDataManager(
                self._database_address, self.bank_name, self.bank_id)

        account = self._database.get_account(account_number)

        if account is None:
            print("The specified account was not found.")
        return account
