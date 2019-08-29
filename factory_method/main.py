from idcard import IDCardFactory

if __name__ == "__main__":
    factory = IDCardFactory()
    card1 = factory.create('ほりいけ')
    card1.use()
