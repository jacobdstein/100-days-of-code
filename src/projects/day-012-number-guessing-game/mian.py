from random import randint

random_num = randint(1, 100)

print("I am thinking of a number from 1 to 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
num_guesses = 5 if difficulty == 'hard' else 10
print(f"You have {num_guesses} guesses left to guess the number.\n")

for i in range(num_guesses, 0, -1):
    guess = int(input("Guess a number: "))
    if guess == random_num:
        print("Congrats! You guessed the number in " + str(num_guesses - i) + " guesses!")
        break
    elif guess > random_num:
        print("Too high!")
    else:
        print("Too low!")
    print(f"You have {i - 1} guesses left.")