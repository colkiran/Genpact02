
import numpy as np

arr = np.array(40)
print(f"array :{arr}\ndimension :{arr.ndim}")

print("-" * 40)
arr1 = np.array([1, 2, 3, 4, 5])
print(f"array :{arr1}\ndimension :{arr1.ndim}")

print("-" * 40)
arr2 = np.array([[1, 3, 5], [2, 4, 6]])
print(f"array :{arr2}\ndimension :{arr2.ndim}")

print("-" * 40)
arr3 = np.array([[[1,2,3],[4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])
print(f"array :{arr3}\ndimension :{arr3.ndim}")

print("-" * 40)
arr4 = np.array([1, 2, 3, 4, 5], ndmin=5)
print(f"array :{arr4}\ndimension :{arr4.ndim}")