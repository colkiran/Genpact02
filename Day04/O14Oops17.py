
class Animal:
    def __init__(self):
        print("Animal Ctor.......")
        self.age = 1

    def eat(self):
        print("Animals eat......")


class Bird(Animal):
    def fly(self):
        print("Birds fly....")

class Fish(Animal):
    def swim(self):
        print("Fishes swim......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()
print("-" * 40)
dolphin = Fish()
dolphin.swim()
dolphin.eat()
print("-" * 40)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print("-" * 40)
print(isinstance(cuckoo, Bird))
print(isinstance(cuckoo, Animal))
print(isinstance(cuckoo, object))
print(isinstance(cuckoo, Fish))

print("-" * 40)
print(isinstance(dolphin, Bird))
print(isinstance(dolphin, Animal))
print(isinstance(dolphin, object))
print(isinstance(dolphin, Fish))