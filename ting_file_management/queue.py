from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()
        self._length = 0

    def __len__(self):
        return self._length

    def enqueue(self, value):
        self._data.append(value)
        self._length += 1

    def dequeue(self):
        if len(self._data) == 0:
            return None
        self._length -= 1
        return self._data.pop(0)

    # teste PR 2
    def search(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
