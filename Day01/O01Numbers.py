
"""
    in python everything is an object => even a variable is an object
"""

a = 10
b = -10

print(f"a :{a}")            # f - format keyword which allows interpolation
print(type(a))              # type - RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 40)
c = 5.2
d = -5.2
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 40)
e = 2 + 7j
f = 2 - 7j
print(f"e :{e}")
print(type(e))
print(f"f: {f}")
print(type(f))

print("-" * 40)
g = +2e3
h = -2e3
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 40)
x = 30
y = 8.5
print(f"x :{x}")
print(f"y :{y}")
z = x + y
print(f"z :{z}")
print(f"x :{type(x)}")
print(f"y :{type(y)}")
print(f"z :{type(z)}")

print("Conversions".center(40, "-"))
a = -50
print(f"a :{a}")
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")


print("Number System".center(40, "-"))
print(11)       # decimal
print(0b11)     # binary
print(0b101)    # binary
print(0o11)     # octal
print(0o111)    # octal
print(0xe)      # hexa
print(0xa)      # hexa

print("Number System Conversions".center(50, "-"))
a = 100
print(oct(a))
print(hex(a))
print(bin(a))
