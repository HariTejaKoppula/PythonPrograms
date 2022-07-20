

a = 5
b = 2

try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter the Number"))
    print(k)
except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number By Zero",e)
except ValueError as e:
    print("Invalid Input", e)
except Exception as e:
    print("Something Went Wrong",e)
finally:
    print("Resource Closed")