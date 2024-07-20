import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+' "."]

length = int(input("Enter a password length from 15 to 100: "))
while length < 15 or length > 100:
    print("That length is invalid")
    length = int(input("Enter a password length from 15 to 100: "))
password = ""
chars = [letters, numbers, symbols]

for i in range(length):
    password += random.choice(random.choice(chars))

print(f"Your password is: {password}")