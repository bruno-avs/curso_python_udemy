class Person:
    ano = 2022
    def __init__(self, name, idade ):
        self.name = name
        self.last_name = idade

    @classmethod
    def classe_metd(cls, name, ano_naci):
        idade = cls.ano - ano_naci
        return cls(name, idade)



person = Person.classe_metd('bruno', 1986)
print(person)



