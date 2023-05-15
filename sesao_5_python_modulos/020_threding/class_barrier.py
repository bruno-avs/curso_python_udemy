# A classe Barrier permite criar objetos que funcionam como uma barreira,
# significa que só liberam a passagem se um número especificado de threads
# estiver esperando nela.

import time
import threading
import random


def flare_gun():
    # Esta é a função que sera passada para a classe Barrier, ela sera
    # executada por uma das threads logo apos a barreira ser liberada
    print("Todas as threads chegaram, carreira liberada.")


def task(barrier: threading.Barrier):
    curr_tread = threading.current_thread()
    time.sleep(random.random())
    print(f"{curr_tread.name} chegou na barreira.")

    barrier.wait(10)

    time.sleep(random.random())
    print(f"{curr_tread.name} passou pela barreira.")


barrier = threading.Barrier(parties=4, action=flare_gun)

T1 = threading.Timer(interval=1, function=task, args=(barrier,))
T2 = threading.Timer(interval=2, function=task, args=(barrier,))
T3 = threading.Timer(interval=3, function=task, args=(barrier,))
T4 = threading.Timer(interval=4, function=task, args=(barrier,))


T1.start()
T2.start()
T3.start()
T4.start()

T1.join()
T2.join()
T3.join()
T4.join()
