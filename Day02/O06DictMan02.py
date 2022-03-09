
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
'pop', 'popitem', 'setdefault', 'update', 'values'
"""

print("keys".center(40, "-"))
player = {'name': 'sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus', 'venue': 'Perth'}
print(f"player :{player}")

# keys
key = player.keys()
print(f"key :{key}")
for k in key:
    print(k, end=" ")
print()

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus', 'venue': 'Perth'}
print(f"player :{player}")
vl = player.values()
print(f"values :{vl}")

print("fromkeys".center(40, "-"))
veg = ['carrot', 'beans', 'okra', 'cabbage', 'tomato', 'potato']
print(f"veg :{veg}")
print(type(veg))

vegdct = dict.fromkeys(veg)                 # add none as value
print(f"vegdct :{vegdct}")

print("-" * 40)
vegdct = dict.fromkeys(veg, "200 gms")
print(f"vegdct :{vegdct}")

print("setdefault".center(40, "-"))
# to add new key values into the dictionary
player = {'name': 'sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus', 'venue': 'Perth'}
print(f"player :{player}")
player.setdefault("age", 32)
player.setdefault("date", "04/10/2003")

print(f"player :{player}")

