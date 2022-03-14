
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"arr :{arr}")
print(f"arr[0] :{arr[0]}")
print(f"arr[4] :{arr[4]}")
print("-" * 40)


arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"arr1 :{arr1}")
print(f"dimension :{arr1.ndim}")
print(f"3 from the array :{arr1[0, 2]}")
print(f"3 from the array :{arr1[1, 3]}")

print("-" * 40)
arr2 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(f"arr2 :{arr2}")
print(f"dimension :{arr2.ndim}")
print(f"arr2[0, 1, 1] :{arr2[0, 1, 1]}")
print(f'arr2[1, 0, 2] :{arr2[1, 0, 2]}')
