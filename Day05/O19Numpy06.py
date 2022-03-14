import numpy
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(f"arr1 :{arr1}")

for i in arr1:
    print(i, end=" ")
print()

print("-" * 40)

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"arr2 :{arr2}")

print("-" * 40)
for j in arr2:
    for k in j:
        print(k, end=" ")
    print()


