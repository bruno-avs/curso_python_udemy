from threading import Thread
import threading
from time import sleep
from random import random


def calculate_the_value(v1: float, v2: float) -> float:
    time_1 = random()

    # retorna a thread em execução atual
    current_thread = threading.current_thread()
    print(f"{current_thread.name} esta executando a função.")

    sleep(time_1)

    ident = threading.get_ident()  # retorna o identificador
    native_id = threading.get_native_id()  # retorna o id native atribuído pelo
    # sistema

    print(f"\tident => {ident}")
    print(f"\tnative id => {native_id}")

    time_2 = random()

    sleep(time_2)

    print("Calculando.....")
    print(f"{v1} + {v2}")

    sleep(1)

    total = v1 + v2

    print("Valores calculados com sucesso.")
    print(f"Resultado {total}")
    return total


T1 = Thread(target=calculate_the_value, args=(3, 4))
T2 = Thread(target=calculate_the_value, args=(6, 9))

T2.start()
T1.start()

# retorna o número de threads em execução
print(f"running threads => {threading.active_count()}")
print()
# retorna uma lista de thread objetos que estão em execução no momento
print(f"list of currently running threads => {threading.enumerate()}")

# retorna o thread objeto da main thread
print()
print(f"main thread object => {threading.main_thread()}")
