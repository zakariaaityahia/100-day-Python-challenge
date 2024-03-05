height = input("enter you height in metre :")
weight = input("enter you weight in kg :")

height_input = float(height)
weight_input = int(weight)

bmi = weight_input / height_input ** 2

bmi_int = int(bmi)
print(bmi_int) 