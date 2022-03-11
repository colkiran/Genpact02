
class Animal:
    def eat(self):
        print("Animals eat....")

class Bird(Animal):
    def fly(self):
        print("birds fly....")

class Chicken(Bird):
    pass

chick = Chicken()
chick.eat()
chick.fly()
