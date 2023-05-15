"""
O problema do produtor/consumidor é um dos principais problemas quando se
trata de multi processamento. Este problema consiste em um dessincronização
entre um produtor e um consumidor, que neste caso serão um método que simula
a chegada de dados de uma rede, setando esses dados em um buffer, e um 
consumidor que consome os dados do buffer.

Um dos problemas acontece porque o produtor pode acabar gerando dados demais e 
enchendo o buffer, e os dados que vierem posteriormente serão perdidos.
"""
from typing import Any
import threading
import time
import random


class Buffer:
    # esta classe representa um buffer, é basicamente uma lista que possui
    # métodos para setar, pegar, verificar se esta cheia ou vazia.
    def __init__(self, max_buffer_size) -> None:
        self.max_buffer_size = max_buffer_size
        self.__buffer: list = []

    def set_value(self, value: Any) -> None:
        if self.buffer_is_full():
            raise BufferError("Operação não pode ser executada: O buffer esta cheio.")

        self.__buffer.append(value)

    def get_value(self) -> Any:
        if self.buffer_is_empty():
            raise BufferError("Operação não pode ser executada: O buffer esta vazio.")
        return self.__buffer.pop()

    def buffer_is_full(self) -> bool:
        return len(self.__buffer) >= self.max_buffer_size

    def buffer_is_empty(self) -> bool:
        return len(self.__buffer) == 0


class Producer(threading.Thread):
    # esta classe é o produtor, ela que ira gerar os dados e adicionar-los no
    # buffer
    def __init__(self, buffer: Buffer, condition: threading.Condition) -> None:
        self.condition = condition
        self.__buffer = buffer
        super().__init__()

    def run(self) -> None:
        condition = self.condition
        condition.acquire()

        class_name = self.__class__.__name__
        set_value_msg = "{0}: valor {1} adicionado no buffer."

        print()
        print(f"{class_name}: Gerando dados.....")

        while True:
            time.sleep(0.5)
            amount_data_to_be_generated = random.randint(1, 10)
            print(f"{class_name}: {amount_data_to_be_generated} foram gerados.")

            print(f"{class_name}: iniciando adição de dados no buffer....")
            time.sleep(0.5)

            for _ in range(amount_data_to_be_generated):
                generated_data = random.randint(1, 99)
                time.sleep(0.5)
                if not self.__buffer.buffer_is_full():
                    self.__buffer.set_value(generated_data)
                    print(set_value_msg.format(class_name, generated_data))

                    continue

                print(f"{class_name}: buffer cheio.")
                print(f"{class_name}: parando produção....")
                print()

                time.sleep(0.5)
                wait_result = condition.wait(timeout=30)

                if wait_result:
                    print()
                    print(f"{class_name}: Reiniciando produção....")

                    time.sleep(0.5)

                    self.__buffer.set_value(generated_data)
                    print(set_value_msg.format(class_name, generated_data))

                    condition.notify()
                    continue
                else:
                    print(
                        f"{class_name}: Buffer não foi esvaziado, cancelando"
                        f"produção...."
                    )
                    condition.release()
                    return
            break

        condition.release()


class Consumer(threading.Thread):
    def __init__(
        self, buffer: Buffer, condition: threading.Condition, producer: Producer
    ) -> None:
        self.condition = condition
        self.producer = producer
        self.__buffer = buffer
        super().__init__()

    def run(self) -> None:
        condition = self.condition
        condition.acquire()

        class_name = self.__class__.__name__
        get_value_msg = "{0}: Valor {1} foi retirado do buffer."

        print(f"{class_name}: Iniciando o consumo dos dados...")

        while True:
            time.sleep(0.5)

            if not self.producer.is_alive():
                if not self.__buffer.buffer_is_empty():
                    value = self.__buffer.get_value()
                    print(get_value_msg.format(class_name, value))

                    continue
                else:
                    print(
                        f"{class_name}: Todos os dados foram consumidos, "
                        f"encerando consumo de dados..."
                    )
                    condition.release()
                    break
            else:
                if not self.__buffer.buffer_is_empty():
                    value = self.__buffer.get_value()
                    print(f"Consumer: valor {value} foi retirado do buffer.")
                    continue
                else:
                    print(
                        f"{class_name}: Buffer vazio, parando consumo de " f"dados..."
                    )
                    condition.notify()
                    producer_response = condition.wait(timeout=30)

                    if producer_response:
                        print()
                        print(f"{class_name}: Reiniciando consumo de dados...")
                        continue
                    else:
                        print(
                            f"{class_name}: Novos dados não foram produzidos, "
                            f"cancelando consumo de dados..."
                        )
                        break


buffer = Buffer(2)
condition = threading.Condition()

producer = Producer(buffer, condition)
consumer = Consumer(buffer, condition, producer)

producer.start()
consumer.start()

producer.join()
consumer.join()

print()
print("operação concluída.")
print()
