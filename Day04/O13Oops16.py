
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("getter method called....")
        return self.__price

    @price.setter
    def price(self, val):
        print("setter method called.....")
        if val < 0:
            raise ValueError("Price cannot be less "
                             "than zero")
        else:
            self.__price = val

    @price.deleter
    def price(self):
        print("deleter method called.....")
        self.__price = 0

coke = Product(30)
print(coke.price)

coke.price = 35
print(coke.price)

del coke.price
print(coke.price)
