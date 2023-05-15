import threading
from time import sleep

# threads daemon são threads que são mortas (sua execução é encerrada) quando a
# man thread termina de executar


# quando a main thread termina de executar ela espera as outras threads não
# demônicas terminarem suas tarefas, quando elas terminam são mescladas na main
# thread e o programa se encerra


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


T1 = threading.Thread(target=calculate_the_value, args=(3, 4), daemon=True)
T2 = threading.Thread(target=calculate_the_value, args=(6, 9), daemon=True)
T2.start()
T1.start()

sleep(0.2)

print("Encerrando o programa.")
