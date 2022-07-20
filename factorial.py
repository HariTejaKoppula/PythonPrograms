"""Factorial"""
def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f
x = 5

result = fact(x)
print(result)



"""Factorial Using Recursion"""
def fac(n):

    if n == 0:
        return 1
    return n * fac(n-1)
res = fac(5)
print(res)