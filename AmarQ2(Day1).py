user=int(input("enter num"))
if user%4==0:
    if user%100==0:
        if user%400==0:
            print(user,"is leap year")
        else:
            print(user,"is not leap year")
    else:
        print(user,"is not leap year")
else:
    print(user,"is not leap year")