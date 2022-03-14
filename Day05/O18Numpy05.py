
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"arr :{arr}")
print(f'arr.shape :{arr.shape}')

print("-" * 40)
arr1 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(f"arr1 :{arr1}")
print(f"arr1.shape :{arr1.shape}")
