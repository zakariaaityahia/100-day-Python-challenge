year = int(input("enter a year : "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
         print("Leap year")
        else:
            print("its not a leap year")
    else:
        print("Leap year")
else:
    print("its not a leap year")