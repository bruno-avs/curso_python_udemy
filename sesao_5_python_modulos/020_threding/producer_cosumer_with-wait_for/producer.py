import threading
import random
from flow_manager import FlowManager
from buffer import Buffer
import time


class Producer(threading.Thread):
    # esta classe é o produtor, ela que ira gerar os dados e adicionar-los no
    # buffer
    def __init__(
        self,
        buffer: Buffer,
        condition: threading.Condition,
        flow_manager: FlowManager,
    ) -> None:
        self.__buffer = buffer
        self.condition = condition
        self.flow_manager = flow_manager
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
            print(
                f"{class_name}: {amount_data_to_be_generated} foram gerados."
            )

            print(f"{class_name}: iniciando adição de dados no buffer....")
            time.sleep(0.5)

            for _ in range(amount_data_to_be_generated):
                generated_data = random.randint(1, 99)

                wait_result = condition.wait_for(
                    predicate=self.flow_manager.buffer_is_not_full, timeout=0.1
                )
                if wait_result:
                    time.sleep(0.5)

                    self.__buffer.set_value(generated_data)
                    print(set_value_msg.format(class_name, generated_data))

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
