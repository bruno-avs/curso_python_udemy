import threading
from flow_manager import ProducerFlowManager
from buffer import Buffer
import time


class Consumer(threading.Thread):
    def __init__(
        self,
        buffer: Buffer,
        condition: threading.Condition,
        producer_flow_manager: ProducerFlowManager,
    ) -> None:
        self.__buffer = buffer
        self.condition = condition
        self.producer_flow_manager = producer_flow_manager
        super().__init__()

    def run(self) -> None:
        condition = self.condition

        condition.acquire()

        class_name = self.__class__.__name__
        get_value_msg = "{0}: Valor {1} foi retirado do buffer."

        print(f"{class_name}: Iniciando o consumo dos dados...")

        while True:
            time.sleep(0.5)
            if self.producer_flow_manager.producer_is_alive():
                wait_result = condition.wait_for(
                    self.producer_flow_manager.buffer_is_not_empty, timeout=0.1
                )
                time.sleep(0.5)

                if wait_result:
                    value = self.__buffer.get_value()
                    print(get_value_msg.format(class_name, value))
                    continue
                else:
                    print(
                        f"{class_name}: Novos dados não foram produzidos, "
                        f"cancelando consumo de dados..."
                    )
                    condition.release()
                    break
            else:
                if self.producer_flow_manager.buffer_is_not_empty():
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
