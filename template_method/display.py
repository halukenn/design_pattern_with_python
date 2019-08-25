from abc import ABCMeta
from abc import abstractmethod


class AbstractDisplay(metaclass=ABCMeta):

    def display(self):
        self.open()
        self.print()
        self.close()

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass


class CharDisplay(AbstractDisplay):

    def __init__(self, arg):
        self.arg = arg

    def open(self):
        print('<<', end='')

    def print(self):
        print(self.arg, end='')

    def close(self):
        print('>>')


class StringDisplay(AbstractDisplay):

    def __init__(self, arg):
        self.arg = arg
        self.width = len(arg)

    def open(self):
        self.print_line()

    def print(self):
        print('|', self.arg, '|', sep='')

    def close(self):
        self.print_line()

    def print_line(self):
        print('+', end='')
        for _i in range(self.width):
            print('-', end='')
        print('+')
