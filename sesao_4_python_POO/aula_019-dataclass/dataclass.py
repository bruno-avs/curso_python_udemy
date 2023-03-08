from dataclasses import dataclass, field, asdict, astuple


@dataclass(
    init=True, repr=True, eq=True, order=False,
    unsafe_hash=False, frozen=False, match_args=True,
    kw_only=False, slots=False
)
class Person:
    name: str
    last_name: str
    old: str = field(default=0, repr=False)
    full_name: str = field(init=False)

    def __post_init__(self):
        self.full_name = f"{self.name} {self.last_name}"


person = Person("bruno", "alves", "20")


print(person.name)
person_dict = asdict(person)
print(person_dict)
person_tuple = astuple(person)
print(person_tuple)

