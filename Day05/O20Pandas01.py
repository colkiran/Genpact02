
import pandas as pd

a = [1, 2, 3, 4, 5]

parr = pd.Series(a)
print(f"parr :{parr}")

parr = pd.Series(a, index=['a', 'b', 'c', 'd', 'e'])
print(parr)

print("-" * 40)
temp = {'blr': 36, 'che': 40, 'hyd': 42, 'del': 28, 'mum':32}
parr1 = pd.Series(temp)
print(f"parr1 :{parr1}")

print("-" * 40)

runs = {
    'sachin': [45, 82, 135, 0, 105],
    'rahul': [18, 97, 65, 30, 70],
    'sehwag': [85, 10, 25, 40, 139]
}

parr2 = pd.DataFrame(runs)
print(parr2)

