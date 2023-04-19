
class Person:
    def __init__(
        self,
        name: str,
        last_name: str,
        old: int
    ) -> None:
        self.name = name
        self.last_name = last_name
        self.full_name = name + " " + last_name
        self.old = old
