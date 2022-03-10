
def add(x, y):
    return x + y

a = add
res = a(20, 30)
print(f"res :{res}")

print("-" * 40)

r = lambda x, y: x + y
res = r(10, 15)
print(f"res :{res}")

# used with map, filter and reduce
l = list(range(1, 11))
print(f"l :{l}")

map_res = list(map(lambda x: x ** 2, l))
print(f"map_res :{map_res}")

# USD = [35, 45, 10, 250, 3500, 87.5, 120, 2500]
# convert it into INR => www.xe.com
print("-" * 40)
l = list(range(1, 25))
print(f"l :{l}")
flt_res = list(filter(lambda x: x % 3 == 0, l))
print(f"flt_res :{flt_res}")

# reduce from functools
print("-" * 40)
from functools import reduce
l = [10, 3, 5, 2, 7, 8, 9, 12, 4]
print(f"l :{l}")

red_res = reduce(lambda x, y: x + y, l)
print(f"red_res :{red_res}")

red_res = reduce(lambda x, y: x if x > y else y, l)
print(f"red_res :{red_res}")

print("-" * 40)
from calendar import month_name
months = ['dec', 'oct', 'jun', 'jul', 'jan', 'apr', 'feb', 'nov', 'may', 'aug', 'sep', 'mar']
# print(list(month_name))

for m in list(month_name):
    print(m[0:3].lower(), end= " ")
print()


print("-" * 40)
print(f"months :{months}")
str_months = sorted(months, key=list(map(lambda m: m[0:3].lower(), list(month_name))).index)
print(f"str_months :{str_months}")
