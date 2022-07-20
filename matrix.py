from numpy import *
arr1 = array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 3]

])
arr2 = arr1.flatten()
arr3 = arr2.reshape(3, 4)
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr2)
print(arr3)
m = matrix('1 2 3; 0 6 5')
print(m)