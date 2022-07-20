file = open("god.jpeg", 'rb')
file1 = open("MyPic.jpeg", 'wb')
for i in file:
    file1.write(i)