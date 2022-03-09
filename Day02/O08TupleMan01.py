
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3
print(f"t5 :{t5}")
print(type(t5))

print("-" * 40)
t = tuple(range(1, 6))
print(f"t :{t}")
print(f"t[0] :{t[0]}")
print(f"t[-1] :{t[-1]}")

print("-" * 40)
l = list(t)
print(f"l :{l}")
print(type(l))
l.extend([6, 7, 8, 9])
print(f"l :{l}")
t = tuple(l)
print(f"t :{t}")

# print(f"t[1] :{t[1]}")
# t[1] = 'two'
# print("-" * 40)
# print(dir(t))
print("count".center(40, "-"))
t1 = (1, 2, 3, 1, 2, 1, 1, 3, 1, 1, 2, 1, 4, 3)
print(f"1 :{t1.count(1)}")

print("index".center(40, "-"))
print(f"t1 :{t1}")
print(t1.index(3))
print(t1.index(3, 4))
print(t1.index(3, 8))
