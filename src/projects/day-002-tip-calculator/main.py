print("Welcome to the the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percent would you like to tip? (Ex. 10) "))
numPeople = int(input("How many people to split the bill? "))
total = bill * (100 + tip) / 100
perPerson = round(total / numPeople, 2)
print(f"\nEach person should pay: ${perPerson:.2f}")

