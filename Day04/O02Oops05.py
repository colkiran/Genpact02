
class Player:
    team = "India"                  # class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Virat", 34)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rohit", 33)
ply2.get_details()

print("-" * 40)
print("Player :", Player.team)
print("pyl1 :", ply1.team)
print("ply2 :", ply2.team)

print("-" * 40)
Player.team = "RCB"
print("Player :", Player.team)
print("pyl1 :", ply1.team)
print("ply2 :", ply2.team)

print("-" * 40)
ply2.team = "MI"
print("ply2 :", ply2.team)

print("-" * 40)
print("Player :", Player.team)
print("pyl1 :", ply1.team)

print("-" * 40)
print(ply2.__dict__)

print("-" * 40)
print(Player.__dict__)