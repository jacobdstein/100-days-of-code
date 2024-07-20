height = float(input("Enter your height in meters (e.g. 1.78): "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height * height)

if bmi < 18.5:
    print(f"\nYour BMI is {bmi:.2f}, you are underweight")
elif bmi < 25:
    print(f"\nYour BMI is {bmi:.2f}, you have a normal weight")
elif bmi < 30:
    print(f"\nYour BMI is {bmi:.2f}, you are overweight")
elif bmi < 35:
    print(f"\nYour BMI is {bmi:.2f}, you are obese")
else:
    print(f"\nYour BMI is {bmi:.2f}, you are clinically obese")