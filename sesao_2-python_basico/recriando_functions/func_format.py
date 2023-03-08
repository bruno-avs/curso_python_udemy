# tentei recriar a função format

class MySTR:
    def __init__(self, obj) -> None:
        self.my_str = obj

    def my_format(self, *args, **kwargs) -> str:
        old_str: str = self.my_str
        new_str: str = old_str

        no_index: bool = False
        with_index: bool = False
        current_index: int = 0

        need_to_format: bool = True
        while need_to_format:

            start = new_str.find("{")
            end = new_str.find("}")

            if start == -1 or end == -1:
                break

            key_value = new_str[start + 1: end].strip()

            to_replace = new_str[start: end + 1]
            substitute: str = ""

            if no_index and with_index:
                raise ValueError(
                    "cannot switch from manual field specification to "
                    "automatic field numbering")

            if not key_value and not to_replace == "{0}":

                no_index = True
                if not args:
                    raise IndexError(
                        f"Replacement index {key_value} out of range for "
                        f"positional args tuple")

                substitute = args[current_index]
                new_str = new_str.replace(to_replace, substitute)

                current_index += 1
            elif key_value.isnumeric() or key_value == "":
                with_index = True
                index_value = int(key_value)

                if not args:
                    raise IndexError(
                        f"Replacement index {index_value} out of range for "
                        f"positional args tuple")

                try:
                    substitute = args[index_value]
                except IndexError:
                    raise IndexError(
                        f"Replacement index {index_value} out of range "
                        f"for positional args tuple")

                new_str = new_str.replace(to_replace, substitute)
            elif isinstance(key_value, str):
                if not kwargs:
                    raise KeyError(key_value)

                has_the_key = kwargs.get(key_value, False)

                if not has_the_key:
                    raise KeyError(key_value)

                substitute = has_the_key

                new_str = new_str.replace(to_replace, substitute)
        return new_str


my_str = MySTR("Meu nome é {g} bruno {h} ola {i}")

print(my_str.my_format(h="2", i="3", g="9"))
