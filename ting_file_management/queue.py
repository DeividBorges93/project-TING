from collections.abc import Iterator


class Queue(Iterator):
    def __init__(self):
        self.__data = []
        self.index = 0

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def is_empty(self):
        return self.__data == []

    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def search(self, index):
        if index < 0 or index > len(self.__data):
            raise IndexError('Invalid index')
        return self.__data[index]

    def __next__(self):
        try:
            valor = self.__data[self.index]
            self.index += 1
            return valor
        except IndexError:
            raise StopIteration
