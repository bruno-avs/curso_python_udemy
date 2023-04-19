from src.database_managers import PhysicalPersonDatabaseManager
from src.cpf import generate_cpf, cpf_is_valid, Regions
from src.new_exceptions import CPFNotRegisteredError
from src.brazil_states import BrazilStates
from src.persons import Person
from typing import Any


class PhysicalPerson:
    def __init__(self, person: Person, cpf: str) -> None:
        self._person = person
        self._cpf = cpf
        self._registered_material_goods: list = []
        self._debts: list = []

    @property
    def person(self):
        return self._person

    @property
    def cpf(self):
        return self._cpf

    @property
    def registered_material_goods(self):
        return self._registered_material_goods

    @property
    def debts(self):
        return self._debts


class PhysicalPersonRegistrar:
    def __init__(self) -> None:
        self._database = PhysicalPersonDatabaseManager()

    def cpf_is_registered(self, cpf: str) -> bool:
        if not cpf_is_valid(cpf):
            return False

        if self._database.cpf_is_registered_in_database(cpf):
            return True
        return False

    def register_new_person(
            self, person: Person, state: BrazilStates) -> str:
        generated_cpf: str = ""

        for region in Regions:
            curr_region = region
            if region.name == state.name:
                generated_cpf = generate_cpf(curr_region)

        self._database.post_physical_person(
            PhysicalPerson(person, generated_cpf))

        return generated_cpf

    def register_debt(self, cpf: str, debt: Any) -> None:
        if not cpf_is_valid(cpf):
            raise ValueError(f"O CPF {cpf} não é um CPF valido.")

        if self._database.cpf_is_registered_in_database(cpf):
            raise CPFNotRegisteredError(
                f"O CPF {cpf} não esta registrado no banco de dados."
            )

        self._database.post_debt(cpf, debt)

    def register_material_goods(self, cpf: str, material_good: Any) -> None:
        if not cpf_is_valid(cpf):
            raise ValueError(f"O CPF {cpf} não é um CPF valido.")

        if self._database.cpf_is_registered_in_database(cpf):
            raise CPFNotRegisteredError(
                f"O CPF {cpf} não esta registrado no banco de dados."
            )

        self._database.post_material_good(cpf, material_good)
