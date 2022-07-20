"""Python program to interchange first and last elements in a list
Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""

def SwapFL(n):
    size = len(n)

    temp = n[0]
    n[0] = n[size-1]
    n[size-1] = temp
    print(n)

n = [12, 35, 9, 56, 24]
SwapFL(n)

def Swapping(n):
    s=len(n)
    n[0],n[-1] = n[-1],n[0]
    print(n)
n= [1, 2, 3, 4, 5]
Swapping(n)

"""Perfect Number"""
def isPerfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n/i
        i += 1
        return (True if sum == n else False)
n = 2
isPerfect(n)
for n in range(10000):
    if isPerfect(n):
        print(n)
