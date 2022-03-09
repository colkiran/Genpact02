
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 40)

s2 = {2, 3, 4.5, 5.2, 6.8, 'seven', 'eight', 'nine', True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = set(range(1, 10))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
s1 = {1, 2, 3}
s1.add(1)
s1.add(2)
s1.add(4)
s1.add(3)
print(f"s1 :{s1}")

s1.update([1, 3, 4])
s1.update([2, 4, 5])
s1.update([6, 7, 8])
print(f"s1 :{s1}")

print("-" * 40)
s1.remove(5)
print(f"s1 :{s1}")

s1.discard(2)
print(f"s1 :{s1}")
s1.discard(9)       # number is not there then no error message

res = s1.pop()
print(f"res :{res}")
print(f"s1 :{s1}")
