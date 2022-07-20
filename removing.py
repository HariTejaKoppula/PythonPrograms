input_str = "It is a long established fact that reader will be distracted by readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and webpage editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many websites still in their infancy."
inp = "is"
lst=[]
x= input_str.split()
lst.append(x)
print(lst)
for i in range(len(lst)):
    if i == inp:
        lst.pop(i)
    print(lst)

