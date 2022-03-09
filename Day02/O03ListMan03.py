
print("pop".center(40, "-"))
l1 = list(range(1,11))
print(f"l1 :{l1}")

print("-" * 40)
res = l1.pop(4)
print(f"res :{res}")
print(f"l1 :{l1}")

print("-" * 40)
res = l1.pop(8)
print(f"res :{res}")
print(f"l1 :{l1}")

print("-" * 40)
res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("index".center(40, "-"))
l2 = [1, 2, 3, 1, 2, 2, 1, 2, 1, 1, 2, 3, 2, 1, 1, 4, 1, 1, 2, 3]
print(f"12 :{l2}")

res = l2.index(3)
print(f"res :{res}")

print("-" * 40)

res = l2.index(3, 4, 12)
print(f"res :{res}")

print("-" * 40)

res = l2.index(3, 13)
print(f"res :{res}")

print("copy".center(40, "-"))
l1 = list(range(1, 6))
print(f"Before l1 :{l1}")
l2 = l1             # shallow copy
print(f"Before l2 :{l2}")

print("-" * 40)
l2.extend([6, 7, 8, 9])
print(f"After l2 :{l2}")
print(f"After l1 :{l1}")

print("-" * 40)
l3 = list(range(6, 11))
print(f"Before l3 :{l3}")
l4 = l3.copy()
print(f"Before l4 :{l4}")

print("-" * 40)
l4.insert(1, 6.5)
l4.insert(3, 7.5)
l4.insert(5, 8.5)
print(f"After l4 :{l4}")
print(f"After l3 :{l3}")

print("-" * 40)
l5 = [11, 12, 13, 14, [1, 2, 3, 4, 5], 15]
print(f"Before l5 :{l5}")
l6 = l5.copy()
print(f"Before l6 :{l6}")

print("-" * 40)
l6[4][0] = 11
l6[4][1] = 22
l6[4][2] = 33
l6[4][3] = 44
l6[4][4] = 55
print(f"After l6 :{l6}")
print(f"After l5 :{l5}")

print("-" * 40)
from copy import deepcopy
l7 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(f"Before l7 :{l7}")
l8 = deepcopy(l7)
print(f"l8 :{l8}")

print("-" * 40)
l8[4][0] = 'one'
l8[4][1] = 'two'
l8[4][2] = 'three'
l8[4][3] = 'four'
l8[4][4] = 'five'

print(f"After l8 :{l8}")
print(f"After l7 :{l7}")