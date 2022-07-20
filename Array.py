from array import *
# vals = array('i', [5, 9, 8, 4, 2])
# for i in range(5):
#     print(vals[i])
#
#
# vals = array('i', [5, 9, 8, 4, 2])
# newArr = array(vals.typecode, (a*a for a in vals))
#
# for e in newArr:
#     print(e)
#
# i = 0
# while i < len(newArr):
#     print(newArr[i])
#     i += 1



""" Array """
# arr = array('i', [])
# n = int(input("Enter length of array"))
# for i in range(n):
#     x = int(input("Enter next value"))
#     arr.append(x)
# print(arr)
#
# val = int(input("search"))
# k = 0
# for e in arr:
#     if e == val:
#         print(k)
#         break
#     k += 1
# print(arr.index(val))
#


arr = array('i', [])
n = int(input(" range"))
for i in range(n):
    x = int(input("value: "))
    arr.append(x)
print(arr)
val = int(input("search"))
k = 0
for e in arr:
    if e == val:
        print(k)
    k += 1
print(arr.index(val))
