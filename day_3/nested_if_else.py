#nested if else statement
print("hello to rollerCoaster play")
height = int(input("enter your height : "))


if height > 120:
    print("you can play the rollerCoaster")
    age = int(input("enter your age :"))
    if age < 12: 
        print("you have to pay 5$.")
    elif age < 18:
        print("you have to pay 8$.")
    else :
        print("you have to pay 12$")
else:
    print("you have not the required height to play rollerCoaster. sorry !!")