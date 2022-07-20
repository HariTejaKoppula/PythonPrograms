x = int(input("How many candies you want:"))
av = 10
i = 1
while i <= x:
    if i > av:
        print("Out Of Stock", i-1, "left")
        break
    print("Candy", i)
    i += 1
print("Bye")