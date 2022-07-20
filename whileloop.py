"""week with days and hours and minutes and seconds"""
i = 1
while i <= 7:
    if i==1:
        print("Sunday")
    elif i==2:
        print("Monday")
    elif i==3:
        print("Tuesday")
    elif i == 4:
        print("Wednesday")
    elif i == 5:
        print("Thursday")
    elif i==6:
        print("Friday")
    else:
        print("Saturday")
    j = 0
    while j < 24:
        print(j,"o'clock")
        k=1
        while k<60:
            print(k,"minute",end=" ")
            l=1
            while l<=60:
                print(l,"seconds")
                l = l+1
            k=k+1
        j = j+1
    i = i + 1
    print()
