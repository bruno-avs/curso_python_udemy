from typing import Any
import pickle
import os


class PhysicalPersonDatabaseManager:
    def __init__(self) -> None:
        self._database_address = os.path.join(
            os.getcwd(),
            "sesao_4_python_POO",
            "refatoracao-desadio_001-conta-bancaria",
            "src",
            "database",
            "database.json",
        )

        if not os.path.isfile(self._database_address):
            self._create_database()

    def _create_database(self):
        base_for_the_database = {
            "physical_persons": [],
        }
        with open(self._database_address, "wb") as file:
            pickle.dump(base_for_the_database, file)

    def cpf_is_registered_in_database(self, cpf: str) -> bool:
        record = self.get_physical_person(cpf)
        if record is None:
            return False
        return True

    def get(self):
        with open(self._database_address, "rb") as file:
            data = pickle.load(file)
            return data

    def get_physical_person(self, cpf: str) -> Any:
        data = self.get()
        for physical_person in data["physical_persons"]:
            if physical_person.cpf == cpf:
                return physical_person
        return None

    def __post(self, data: Any):
        with open(self._database_address, "wb") as file:
            pickle.dump(data, file)

    def post_physical_person(self, physical_person: Any) -> None:
        data = self.get()
        data["physical_persons"].append(physical_person)

        self.__post(data)

    def post_debt(self, cpf: str, debt: Any) -> None:
        data = self.get()

        for physical_person in data["physical_persons"]:
            if physical_person.cpf == cpf:
                physical_person.debts.append(debt)

        self.__post(data)

    def post_material_good(self, cpf: str, material_good: Any) -> None:
        data = self.get()

        for physical_person in data["physical_persons"]:
            if physical_person.cpf == cpf:
                physical_person.registered_material_goods.append(material_good)

        self.__post(data)

    def delete(self, cpf: str) -> None:
        data = self.get()
        for physical_person in data["physical_persons"]:
            if physical_person.cpf == cpf:
                data["physical_persons"].remove(physical_person)

        self.__post(data)


class BankDataManager:
    def __init__(
        self,
        database_address: str,
        bank_name: str,
        bank_id: int,
    ) -> None:
        self._database_address = database_address
        self.bank_name = bank_name
        self.bank_id = bank_id

        if not os.path.isfile(database_address):
            self._create_database()

    def _create_database(self) -> None:
        base_for_the_database = {
            "bank_id": self.bank_id,
            "bank_name": self.bank_name,
            "accounts": [],
        }
        with open(self._database_address, "wb") as file:
            pickle.dump(base_for_the_database, file)

    def get_data(self) -> Any:
        with open(self._database_address, "rb") as file:
            return pickle.load(file)

    def get_accounts(self) -> list[Any]:
        data = self.get_data()
        return data["accounts"]

    def get_account(self, account_number: str) -> Any:
        accounts = self.get_accounts()

        for account in accounts:
            if account.account_number == account_number:
                return account

        return None

    def _post_data(self, data: Any) -> None:
        with open(self._database_address, "wb") as file:
            pickle.dump(data, file)

    def post_account(self, account: Any) -> None:
        data = self.get_data()
        data["accounts"].append(account)
        self._post_data(data)
