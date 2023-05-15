# A classe Time permite executar uma thread depois de um determinado período
# de tempo. Esta classe é uma subclasse de Thread

import time
import threading
import random


def task():
    curr_tread_name = threading.current_thread().name
    time.sleep(random.random())
    print(f"{curr_tread_name}: executou a função 'task()'.")


T1 = threading.Timer(interval=5, function=task)
T2 = threading.Timer(interval=5, function=task)

T1.start()
T2.start()

print("Esperando o times terminar.")

T1.join()
T2.join()

print("timer terminou.")
