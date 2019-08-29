from abc import ABCMeta
from abc import abstractmethod


class Product(metaclass=ABCMeta):

    @abstractmethod
    def use(self):
        pass


class Factory(metaclass=ABCMeta):

    def create(self, owner):
        product = self.createProduct(owner)
        self.registerProduct(product)
        return product

    @abstractmethod
    def createProduct(self, owner):
        pass

    @abstractmethod
    def registerProduct(self, product):
        pass
