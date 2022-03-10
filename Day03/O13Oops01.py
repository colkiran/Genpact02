
"""
__main__    => double underscore  => dunder_main

"""

class Player:               # pascal casing

    def get_runs(self):
        print("runs scored.....")
        print(self.__class__)


sachin = Player()
print(type(sachin))

print("-" * 40)
sachin.get_runs()

print("-" * 40)
print(sachin.__class__)

print("-" * 40)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
