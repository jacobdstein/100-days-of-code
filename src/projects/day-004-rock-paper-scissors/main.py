import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors")

images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper, 3 for Scissors: "))- 1

computer_choice = random.randint(0, 2)

print("Player chose: \n" + images[player_choice])
print("Computer chose: \n" + images[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("Invalid input")
elif player_choice == computer_choice:
    print("It's a tie")
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print("You won!")
else:
    print("You lost!")




