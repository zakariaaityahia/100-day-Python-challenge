weight = int(input("Enter you're weight : "))
height = float(input("enter you're height :"))

bmi = (weight / (height * height))
bmi_r = round(bmi, 2)

if bmi_r < 18:
    print("you are underweight")
elif bmi_r >= 18.5 and bmi_r < 25 :
    print("you have normal weight")
elif bmi_r >= 25 and bmi_r < 30:
    print("you are slightly overweight")
elif bmi_r >= 30 and bmi_r < 35: 
    print("you are obese")
else:
    print("you are clinically obese")
    
    
