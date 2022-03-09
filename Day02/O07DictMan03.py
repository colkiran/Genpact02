
print("pop".center(40, "-"))
player = {'name': 'sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus', 'venue': 'Perth'}
print(f"player :{player}")

res = player.pop('age')
print(f"res :{res}")
print(f"player :{player}")

#res = player.pop('age')
# print(f"res :{res}")

print("popitem".center(40, "-"))
player = {'name': 'sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus', 'venue': 'Perth'}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")

print("items".center(40, "-"))

emp = {
    'emp1':{'name': 'Jack', 'age': 29, 'desig': 'PM', 'dept': 'HR', 'salary': 45000},
    'emp2':{'name': 'Jill', 'age': 30, 'desig': 'MGR', 'dept': 'Finance', 'salary': 85000},
    'emp3':{'name': 'Janet', 'age': 35, 'desig': 'TL', 'dept': 'IT', 'salary': 135000}
}

print(f"emp :{emp}")
print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print("-" * 40)
print(f"emp1 :{emp['emp2']}")
print("-" * 40)
print(f"emp1 :{emp['emp3']}")

print("-" * 40)
# items = keys + values function
for ky, info in emp.items():
    print(ky)
    print("------")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'name': 'Jack', 'age': 29, 'desig': 'PM', 'dept': 'HR'}
emp2 = {'name': 'Jill', 'age': 30, 'desig': 'MGR', 'salary': 85000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 40)
emp1.update(emp2)
print(f"emp1 :{emp1}")

# copy
player1 = {'name': 'sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus'}
print(f"Before player1 :{player1}")
player2 = player1           # shallow copy
print(f"Before player2 :{player2}")

player2['venue'] = 'Gabba'
print(f"After player2 :{player2}")
print(f"After player1 :{player1}")


player1 = {'name': 'sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus'}
print(f"Before player1 :{player1}")
# player2 = player1           # shallow copy
player2 = player1.copy()      # deep copy
print(f"Before player2 :{player2}")

player2['venue'] = 'Gabba'
print(f"After player2 :{player2}")
print(f"After player1 :{player1}")


player1 = {'name': 'sachin', 'age': 36, 'runs': {'aus':125, 'eng': 89, 'sri': 35, 'wi': 57}}
print(f"Before player1 :{player1}")
# player2 = player1           # shallow copy
player2 = player1.copy()      # deep copy
print(f"Before player2 :{player2}")

player2['runs']['pak'] = 140
print(f"After player2 :{player2}")
print(f"After player1 :{player1}")


player1 = {'name': 'sachin', 'age': 36, 'runs': {'aus':125, 'eng': 89, 'sri': 35, 'wi': 57}}
print(f"Before player1 :{player1}")
from copy import deepcopy
# player2 = player1           # shallow copy
player2 = deepcopy(player1)      # deep copy
print(f"Before player2 :{player2}")

player2['runs']['pak'] = 140
print(f"After player2 :{player2}")
print(f"After player1 :{player1}")

