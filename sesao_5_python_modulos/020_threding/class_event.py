# os objetos events permitem implementar o mecanismo mais simples de
# comunicação entre threads. fornecendo uma maneira fácil de compartilhar uma
# variável booliana que pode atuar como um gatilho ativando threads em espera.

import threading
import time
import random


def task(event: threading.Event):
    event.wait(30)
    curr_thread = threading.current_thread()

    time.sleep(random.random())

    print(f"{curr_thread.name}")


event = threading.Event()

task1 = threading.Thread(target=task, args=(event,))
task2 = threading.Thread(target=task, args=(event,))
task3 = threading.Thread(target=task, args=(event,))
task4 = threading.Thread(target=task, args=(event,))

task1.start()
task2.start()
task3.start()
task4.start()

time.sleep(2)
event.set()

task1.join()
task2.join()
task3.join()
task4.join()

print("terminou")