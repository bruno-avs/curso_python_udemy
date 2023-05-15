# A classe semaphore permite implementar um delimitador de simultaneidade,
# funcionando como um objeto lock com a diferença de que mais de um objeto
# poderá receber o bloqueio de uma só vez. Este recurso é geralmente usado
# quando se quer limitar a quantidade de acessos a um recurso limitado.


import random
import threading
import time


traffic_limit: int = 2
executions: int = 0


def road(semaphore: threading.Semaphore, lock: threading.Lock) -> None:
    curr_tread = threading.current_thread()

    time.sleep(random.random())
    print(f"{curr_tread.name}: esperando no semáforo.")

    semaphore.acquire()

    print(f"{curr_tread.name}: passou pelo semáforo.")

    global executions

    lock.acquire()

    local_executions = executions
    local_executions += 1

    time.sleep(random.random())

    if local_executions >= traffic_limit:
        raise

    executions = 0

    lock.release()

    speed = random.randint(10, 99)
    print(f"{curr_tread.name}: velocidade {speed}/km.")

    semaphore.release()


semaphore = threading.Semaphore(2)
lock = threading.Lock()

T1 = threading.Thread(target=road, args=(semaphore, lock))
T2 = threading.Thread(target=road, args=(semaphore, lock))
T3 = threading.Thread(target=road, args=(semaphore, lock))
T4 = threading.Thread(target=road, args=(semaphore, lock))
T5 = threading.Thread(target=road, args=(semaphore, lock))

T1.start()
T2.start()
T3.start()
T4.start()
T5.start()

T1.join()
T2.join()
T3.join()
T4.join()
T5.join()
