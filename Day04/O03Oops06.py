
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, name, age):           # factory
        return cls(f"Mr. {name}", f"{age} years")


ply1 = Player('Sachin', 38)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Dhoni", 29)
ply2.get_details()
