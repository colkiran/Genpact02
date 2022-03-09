
"""
'append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

"""

# add values into a list
print('append'.center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12])
print(f"l1 :{l1}")
print(f"l1[8][1:3] :{l1[8][1:3]}")

print("extend".center(40, "-"))
l2 = list(range(6, 11))
print(f"l2 :{l2}")
l2.extend([11, 12, 13, 14, 15])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = list(range(1, 11, 2))
print(f"l3 :{l3}")
l3.insert(1, 2)
l3.insert(3, 4)
l3.insert(5, 6)
print(f"l3 :{l3}")

print("-" * 40)
l = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"l :{l}")

l1 = list(range(1, 6))
for i in l1:
    l.insert(i, i)

print(f"l :{l}")

print("-" * 40)

# remove values from a list
print("remove".center(40, "-"))
l1 = [1, 2, 1, 1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1, 4]
print(f"l1 :{l1}")

# count
res = l1.count(1)
print(f"res :{res}")

res = l1.remove(1)              # does not return anything
print(f"res :{res}")
print(f"l1 :{l1}")

print(l1.count(1))
while True:
    try:
        l1.remove(1)
    except ValueError:
        break

print(f"l1 :{l1}")
