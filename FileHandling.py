file = open("MyData", 'r')
print(file.read())

file1 = open("abc", 'w')
file1.write("Something is fishy")

file1 = open("abc", 'a')
file1.write("Something")
