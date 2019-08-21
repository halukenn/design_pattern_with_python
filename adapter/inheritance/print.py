from abc import ABCMeta
from abc import abstractmethod
from banner import banner


class print(metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self, arg):
        pass

    @abstractmethod
    def print_strong(self, arg):
        pass


class print_banner(print, banner):

    def print_weak(self, arg):
        self.show_with_paren(arg)

    def print_strong(self, arg):
        self.show_with_aster(arg)
