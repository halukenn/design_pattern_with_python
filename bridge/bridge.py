from abc import ABCMeta
from abc import abstractmethod


class DisplayImpl(metaclass=ABCMeta):

    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass


class SringDisplayImpl(DisplayImpl):

    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def raw_open(self):
        self.print_line()

    def raw_print(self):
        print('|', self.string, '|')

    def raw_close(self):
        self.print_line()

    def print_line(self):
        print('+ ', end='')
        for _i in range(self.width):
            print('-', end='')
        print(' +')


class Display:

    def __init__(self, display_impl):
        self.display_impl = display_impl

    def open(self):
        self.display_impl.raw_open()

    def print(self):
        self.display_impl.raw_print()

    def close(self):
        self.display_impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):

    def __init__(self, display_impl):
        super().__init__(display_impl)

    def multi_display(self, times):
        self.open()
        for _i in range(times):
            self.print()
        self.close()
