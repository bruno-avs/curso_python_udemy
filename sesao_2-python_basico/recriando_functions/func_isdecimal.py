
# O ideal era eu construir 3 funções a isdecimal, isnumeric e isdigit, mas
# essa 3 funções tem praticamente o memo papel

def my_isdecimal(__str: str, /) -> bool:
    try:
        int(__str)
        return True
    except ValueError:
        return False

# minha versão mais completa, podendo checar inteiros e floats


def is_number(__str: str, /) -> bool:
    try:
        int(__str)
        return True
    except ValueError:
        try:
            float(__str)
            return True
        except ValueError:
            return False
