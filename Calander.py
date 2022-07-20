a=1
while a<=12:
    if a==1:
        print(a,"January ",end="")
    elif a==2:
        print(a,"February ",end="")
    elif a==3:
        print(a,"March",end="")
    elif a==4:
        print(a,"April ",end="")
    elif a==5:
        print(a,"May ",end="")
    elif a==6:
        print(a,"June ",end="")
    elif a==7:
        print(a,"July ",end="")
    elif a==8:
        print(a,"August ",end="")
    elif a==9:
        print(a,"September ",end="")
    elif a==10:
        print(a,"October ",end="")
    elif a==11:
        print(a,"November ",end="")
    else:
        print(a,"December ",end="")
    b=1
    while b<=31:
        if a ==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
            print(b,end = " ")
        b = b + 1
    c=1
    while c<=28:
        if a==2:
            print(c,end=" ")
        c = c + 1
    d=1
    while d<=30:
        if a==4 or a==6 or a==9 or a==11:
            print(d,end=" ")
        d = d+1

    a+=1
    print()