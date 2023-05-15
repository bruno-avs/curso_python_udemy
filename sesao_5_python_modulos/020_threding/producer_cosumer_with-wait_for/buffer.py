from typing import Any


class Buffer:
    # esta classe representa um buffer, é basicamente uma lista que possui
    # métodos para setar, pegar, verificar se esta cheia ou vazia.
    def __init__(self, max_buffer_size) -> None:
        self.max_buffer_size = max_buffer_size
        self._buffer: list = []

    def set_value(self, value: Any) -> None:
        if len(self._buffer) >= self.max_buffer_size:
            raise BufferError(
                "Operação não pode ser executada: O buffer esta cheio.")

        self._buffer.append(value)

    def get_value(self) -> Any:
        if len(self._buffer) == 0:
            raise BufferError(
                "Operação não pode ser executada: O buffer esta vazio.")
        return self._buffer.pop()

    def get_full_buffer(self) -> list:
        return self._buffer
