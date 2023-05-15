# as condições de corrida são um dor maiores problema quando se trata de
# execução em paralelo.
# elas ocorrem quando as threads tem acesso a um recurso compartilhado entre
# elas, e por elas estarem executando ao "mesmo tempo" uma acaba interferindo
# no resultado gerado pela outra.
import threading
import time

# o exemplo abaixo ilustra bem isso:
database = 0


def add_value_in_database(value: int) -> None:
    # estou simulando de um amaneira bem simples um post em uma base de dados
    print("conectando ao banco de dados....")

    time.sleep(0.3)

    global database
    local_database = database

    print("conectado.")
    print(f"adicionando o valor {value} no banco de dados...")

    time.sleep(0.5)

    local_database += value
    database = local_database

    print("valor adicionado com sucesso.")
    print("desconectando do banco de dados...")
    time.sleep(0.3)
    print("desconectado.")


T1 = threading.Thread(target=add_value_in_database, args=[3])
T2 = threading.Thread(target=add_value_in_database, args=[9])
T1.start()
T2.start()

T1.join()

print(f"database value: {database}")

# perceba que o valor final do banco de dados é 3 e não 12, isso significa que
# uma das threads interferiu no resultado final sobrescrevendo o valor gravado
# no banco de dados pela outra thread
