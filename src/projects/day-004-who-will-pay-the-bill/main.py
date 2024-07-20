import random

names = input("Enter the names (e.g ben jerry steve): ").split()
unlucky = random.choice(names)

print(f"\n{unlucky} is going to buy the meal today!")