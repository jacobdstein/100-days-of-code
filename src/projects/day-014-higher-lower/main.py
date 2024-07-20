from random import choice
from game_data import data
from art import logo


def dict_to_string(dictionary):
    return f"{dictionary['name']}, a {dictionary['description']}, from {dictionary['country']}"


def has_more_followers(one, two):
    return 'a' if one['follower_count'] > two['follower_count'] else 'b'


player_score: int = 0
person1, person2 = choice(data), choice(data)

while True:
    print(f'\033[2J')  # Clear screen
    print(logo)
    print(f"\nCompare A: {dict_to_string(person1)}")
    print(f"Against B: {dict_to_string(person2)}")
    more_famous = has_more_followers(person1, person2)
    guess = input("Who has more followers? Guess A or B: ").lower()
    if guess != more_famous:
        print(f"\nYour guess is incorrect.")
        print(f"Final score: {player_score}")
        break
    if guess == 'b':
        person1 = person2
    player_score += 1
    print(f"\nThat is correct! Your score is {player_score}")
    person2 = choice(data)
