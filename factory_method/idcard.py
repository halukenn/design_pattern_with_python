from framework import Product
from framework import Factory


class IDCard(Product):

    def __init__(self, owner):
        print(owner, 'のカードを作ります。', sep='')
        self.owner = owner

    def use(self):
        print(self.owner, 'のカードを使います。', sep='')

    def getOwner(self):
        return self.owner


class IDCardFactory(Factory):

    def __init__(self):
        self.owners = []

    def createProduct(self, owner):
        return IDCard(owner)

    def registerProduct(self, product):
        self.owners.append(product.getOwner())

    def getOwners(self):
        return self.owners
