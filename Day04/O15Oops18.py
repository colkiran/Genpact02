
class Animal:
    def __init__(self):
        print ("Animal Ctor.....")
        self.age = 1

    def eat(self):
        print("Animals eat....")

class Bird(Animal):
    def __init__(self):                 #overrinding Animal class constructor
        super().__init__()              # call the parent class constructor
        self.size = '1k'
        print("Bird Ctor........")

    def fly(self):
        print("Birds fly.....")

cuckoo = Bird()
print(cuckoo.__dict__)
print(cuckoo.age)
print(cuckoo.size)