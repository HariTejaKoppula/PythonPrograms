import sys
print(sys.setrecursionlimit(2135))

print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i += 1
    print("Hello" , i)
    greet()
greet()