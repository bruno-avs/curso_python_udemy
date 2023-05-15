import threading
import time

"""
Resolvendo o problema de condições de corrida com a classe lock.

Class Lock
    - A classe lock permite basicamente impedir que ocorra simultaneidade em
    trechos do código.
    - O objeto lock funciona como um corredor, com portas, em que só uma thread
    pode passar por vez.
    - O método acquire() é utilizado para ceder um bloqueio a uma thread,
    bloqueando o acesso as outras threads até que o método release seja
    executado, em outras palavras, ele da acesso a uma thread ao corredor
    permitindo que ela execute o código enquanto as outras threads aguardam.
    - O método release() permite liberar um bloqueio da thread que o possui
    dando acesso ao código a outra thread que esta em espera. 
"""
database = 0

lock = threading.Lock()


def add_value_in_database(value: int) -> None:
    # estou simulando de um amaneira bem simples um post em uma base de dados
    print("conectando ao banco de dados....")

    time.sleep(0.3)

    lock.acquire()

    global database
    local_database = database

    print("conectado.")
    print(f"adicionando o valor {value} no banco de dados...")

    time.sleep(0.5)

    local_database += value
    database = local_database

    print("valor adicionado com sucesso.")
    print("desconectando do banco de dados...")

    lock.release()

    time.sleep(0.3)

    print("desconectado.")


T1 = threading.Thread(target=add_value_in_database, args=[3])
T2 = threading.Thread(target=add_value_in_database, args=[9])
T3 = threading.Thread(target=add_value_in_database, args=[5])

T1.start()
T2.start()
T3.start()

T1.join()
T2.join()
T3.join()

print(f"database value: {database}")
