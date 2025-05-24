name = input("Enter Your Name :")
Weight = int(input("Enter your Weight in Pounds : "))
Height = int(input("Enter your Height in Inches : "))

BMI = (Weight * 703 ) / (Height * Height)

if BMI > 0:
    if(BMI < 18.5):
        print("You are underweight")
    elif(BMI > 19 and  BMI <= 24.5):
        print("Your are normal weight")
    elif (BMI > 25 and BMI <= 29.9):
        print("Your are Increased weight")
    elif (BMI > 30 and BMI <= 34.5):
        print("Your are over weight")
    else:
        print("UnValid Your Weight")

print(BMI)