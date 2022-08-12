print("BMI Calculator\n\n")

bmi_mode = -1
height = -1
weight = -1
bmi_result = -1

while True: 
    print("Choose your mode: \n")
    print("1. Metric\n")
    print("2. Imperial\n")
    bmi_mode = int(input())
    if(bmi_mode == 1 or bmi_mode == 2):
        break
    else:
        print("Please enter valid input\n")

while True:
    if(bmi_mode == 1):
        height = float(input("Please enter your height in (Metres    - m)    : "))
        weight = float(input("Please enter your weight in (Kilograms - kg)   : "))

        if(height > 0 and weight > 0):
            bmi_result = weight / (height ** 2)
            break
        else: 
            print("Please enter valid input\n")

    if(bmi_mode == 2): 
        height = float(input("Please enter your height in (Inches - in)  : "))
        weight = float(input("Please enter your weight in (Pound  - lbs) : "))

        if(height > 0 and weight > 0):
            bmi_result = 703 * weight / (height ** 2)
            break
        else: 
            print("Please enter valid input\n")

if(bmi_result > 0): 
    print(f"Your BMI Score is: {bmi_result}")
else: 
    print("Something went wrong...\n")