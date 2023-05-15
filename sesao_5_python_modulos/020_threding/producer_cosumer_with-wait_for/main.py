from buffer import Buffer
from flow_manager import FlowManager
from flow_manager import ProducerFlowManager
from producer import Producer
from consumer import Consumer
import threading

# Produtor e consumidor usando só o método wait_for de Condition

buffer = Buffer(max_buffer_size=2)
condition = threading.Condition()

flow_manager = FlowManager(buffer)

producer = Producer(buffer, condition, flow_manager)

producer_flow_manager = ProducerFlowManager(buffer, producer)

consumer = Consumer(buffer, condition, producer_flow_manager)

producer.start()
consumer.start()

producer.join()
consumer.join()

print()
print("operação concluída.")
print()
