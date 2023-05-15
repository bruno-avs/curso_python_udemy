# A classe Thread nos permite criar objetos que representam threads
from threading import Thread
import threading
from time import sleep
from random import random


# existem duas maneiras de criar objetos Thread:


#   1 - Passando um objeto que pode ser chamado para a classe.
def calculate_the_value(v1: float, v2: float) -> float:
    current_thread = threading.current_thread()
    print(f"{current_thread.name} esta executando a função.")

    sleep(0.5)

    print(f"\tident => {current_thread.ident}")
    print(f"\tnative id => {current_thread.native_id}")

    sleep(0.3)

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


#   2 - Herdando a classe Thread e substituindo o método run().
class MyThread(Thread):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        time = random()
        for i in range(10):
            sleep(time)
            print(i, threading.current_thread().name)


T3 = MyThread()
T3.start()


T3.join()

print("threads executados")
