from src.government import PhysicalPersonRegistrar
from src.banks import Bank
from src.brazil_states import BrazilStates
from src.persons import Person


person = Person("Bruno", "Alves", 21)

physical_person_registrar = PhysicalPersonRegistrar()

physical_person_registrar.register_new_person(person, BrazilStates.MT)

bank = Bank("Sicred", "0821", 12)

