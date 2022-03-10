
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric-difference B :", A ^ B)
print("B symmetric-difference A :", B.symmetric_difference(A))

# frozen-set -> are immutable
a = frozenset([1, 2, 3, 4, 5])
print(f"a :{a}")
print(type(a))


