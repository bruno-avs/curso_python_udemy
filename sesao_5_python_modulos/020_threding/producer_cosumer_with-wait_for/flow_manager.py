from buffer import Buffer


class FlowManager:
    def __init__(
        self,
        buffer: Buffer,
    ) -> None:
        self._buffer = buffer

    def _buffer_len(self) -> int:
        return len(self._buffer.get_full_buffer())

    def buffer_is_full(self) -> bool:
        max_buffer_size = self._buffer.max_buffer_size
        return self._buffer_len() >= max_buffer_size

    def buffer_is_not_full(self) -> bool:
        max_buffer_size = self._buffer.max_buffer_size
        return self._buffer_len() < max_buffer_size

    def buffer_is_empty(self) -> bool:
        return self._buffer_len() == 0

    def buffer_is_not_empty(self) -> bool:
        return self._buffer_len() > 0


class ProducerFlowManager(FlowManager):
    def __init__(
        self,
        buffer,
        producer,
    ) -> None:
        self._producer = producer
        super().__init__(buffer)

    def producer_is_alive(self) -> bool:
        return self._producer.is_alive()
