
"""
# self -> like this pointer

self will store the name of the object that called the method

member variable stored in an object -> __dict__

"""

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized.......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    def __del__(self):
        print("-" * 40)
        print(self.name + " deleted.....")


ply1 = Player("Sachin", 38)
ply1.get_details()

ply2 = Player("Rahul", 32)
ply2.get_details()

print("-" * 40)
print(ply1.__dict__)

print("-" * 40)
print(ply2.__dict__)

print("-" * 40)
ply2.runs = 145
print(ply2.__dict__)
print(ply1.__dict__)

print("-" * 40)
del ply1

ply2.get_details()
