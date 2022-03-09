
"""
sort and sorted
---------------
sort will sort the original list

sorted will return a copy of sorted list

reverse and reversed
--------------------
"""

print("sort".center(40, "-"))
l = [9, 4, 10, 1, 7, 2, 5, 3, 6, 8]
print(f"l :{l}")

res = sorted(l)
print(f"res :{res}")

res1 = sorted(l, reverse=True)
print(f"res1 :{res1}")

print("-" * 40)
l = [9, 'zebra', 4, 'yellow', 10, 'apple', 1, 'xmas', 7, 'blue', 2, 'pink', 5, 'green', 3,
     'orange', 6, 'egg', 'cat', 8, 'union', 19, 1024, 128, 27, 205, 2654]
print(f"l :{l}")
print("sorted list".center(40, "-"))
res = sorted(l, key=ascii)
print(f"res :{res}")

print("-" * 40)

cities = ['vishakapatnam', 'chennai', 'bangalore', 'kanyakumari', 'pune', 'ooty', 'hyderabad',
          'delhi', 'thiruvananthapuram', 'kochi', 'mumbai', 'kolkota']
print(f"cities :{cities}")

print("-" * 40)
res = sorted(cities, key=len)
print(f"res :{res}")

#====================================================================
months = ['dec', 'oct', 'jun', 'jul', 'jan', 'apr', 'feb', 'nov', 'may', 'aug', 'sep', 'mar']

# sort the months according to the calendar

print("reversed".center(40, "-"))
l = [9, 4, 10, 1, 7, 2, 5, 3, 6, 8]
res = list(reversed(l))
print(f"res :{res}")

print("-" * 40)
l.reverse()
print(f"l :{l}")