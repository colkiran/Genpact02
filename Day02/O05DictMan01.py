
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('age', 30), ('runs', 85), ('oppn', 'NZL')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='rahul', age=32, runs=70, oppn='WI')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
d5 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"d5 :{d5}")

print(d5['c'])

print("-" * 40)
veg = {'carrot': '500 gms', 'beans': '250 gms', 'okra': '500 gms', 'green peas': '250 gms'}
print(f"veg :{veg}")

print(f"orka :{veg['okra']}")
del veg['green peas']

veg['drum_stick'] = None                                    # None is same as NULL
print(f"veg :{veg}")

print("-" * 40)
veg['drum_stick'] = 5                                       # set a new value
veg['greens'] = ['coriander', 'curry leaves', 'spinach']    # adding a new key value
veg['beans'] = '500 gms'                                    # modifying

print(f"veg :{veg}")

print("-" * 40)
print(veg.get('cabbage'))               # returns the value if the key exists else returns none

print("-" * 40)
print(dir(veg))
