def update(x):
    print(id(x))
    a[1] = 8
    print(id(x))
    print("x", x)
a=[10,20,30]
print(id(a))
update(a)
print("a", a)


def person(name,age):
    print(name)
    print(age)
person('teja',25)


def sum(*a):
    b = 0
    for i in a:
        b = b + i
    print(b)
sum(5,7,25,36,75,13,24,15)