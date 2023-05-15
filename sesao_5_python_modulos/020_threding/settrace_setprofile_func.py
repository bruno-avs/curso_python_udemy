import threading
from time import sleep
from random import random

count_1 = 0


def tracking(frame, event, args):
    global count_1
    print("tracking", count_1)

    count_1 += 1
    print(frame)
    # print(event)
    # print(args)


count_2 = 0


def profile(frame, event, args):
    global count_2
    print("profile", count_2)

    count_2 += 1
    # print(frame)
    # print(event)
    # print(args)


def calculate_the_value(v1: float, v2: float) -> float:
    current_thread = threading.current_thread()
    print(f"{current_thread.name} esta executando a função.")

    sleep(random())

    print("Calculando.....")
    print(f"{v1} + {v2}")

    sleep(random())

    total = v1 + v2

    print("Valores calculados com sucesso.")
    print(f"Resultado {total}")
    return total


T1 = threading.Thread(target=calculate_the_value, args=(3, 4))
T2 = threading.Thread(target=calculate_the_value, args=(6, 9))

# permite definir uma função de rastreamento
threading.settrace(tracking)

# permite definir uma função de perfil
threading.setprofile(profile)

T2.start()
T1.start()
