
"""
1. Arithmatic
2. Comparison and relational
3. Logical
4  Bitwise
5. Ternary
"""

print("Arithmatic Operators".center(40, "-"))
print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10 * 3)
print("-" * 40)

print(10 // 3)          # floor division
print(10 % 3)
print(10 ** 3)

print("Augmentor Operator".center(40, "-"))
# =, +=, /=, *=, %=

x = 10
x += 3
print(f"x :{x}")
x //= 3
print(f"x :{x}")


print("Comparison Operator".center(40, "-"))
# ==, >=, <-
print(1 == 1)
print(1 < 2)
print(1 > 2)


print("Logical Operators".center(40, "-"))
# and, or , not
print(1 == 1 and 2 == 2)
print(1 == 1 and 1 > 2)
print(not(1 == 1 and 1 > 2))

print("-" * 40)
print(f"A :{ord('A')}")
print(f"a :{ord('a')}")

print("Bitwise Operators".center(40, "-"))
print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)
print(5 << 2)
print(16 >> 1)
print(5 >> 1)

print(~0)
print(~5)

print("ternary".center(40, "-"))
age = 13
print("eligible" if age >= 18 else "not eligible")
