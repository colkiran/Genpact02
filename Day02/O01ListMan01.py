
l1 = list()
print(f"l1 :{l1}")
print(f"l1 :{type(l1)}")

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.9, 9.2, 10+3j, 11+1j, True, False]
print(f"l2 :{l2}")

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")

print("-" * 40)
l = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.9, 9.2, 10+3j, 11+1j, True, False]
print(f"l[2] : {l[2]}")
print(f"l[9] :{l[9]}")
print(type(l[9]))

for i  in l:
    print(i, end=" ")
print()

l[2] = 3000
print(f"l :{l}")
# l[13] = "new_element"
# print(f"l :{l}")

print("-" * 40)
values = list(range(10, 51, 10))
print(f"values :{values}")
# unpack list
a, b, c, d, e = values
print(a, b, c, d, e, sep=", ")

values = list(range(10, 101, 10))
print(f"values :{values}")
a, b, *c = values
print(a, b, c)

print("-" * 40)
a, *b, c = values
print(a, b, c)

print("-" * 40)
*a, b, c = values
print(a, b, c)

print("-" * 40)
l1 = [1, 2, 3, 4]
l2 = [11, 22, 33, 44, 55]

l3 = [l1, l2]
print(f"l3 :{l3}")
print(len(l3))

print("-" * 40)
l4 = [*l1, *l2]             # unpacking the list and then assining the values to the list
print(f"l4 :{l4}")
print(len(l4))

print("-" * 40)
print(dir(l))
