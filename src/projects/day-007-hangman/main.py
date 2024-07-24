import random
from hangman_words import word_lists
from hangman_art import stages, logo

end_of_game: bool = False
lives: int = 6

# Prompt user to choose difficulty
difficulty: str = input("Choose your difficulty. Type \"easy\", \"medium\", \"hard\", or \"phrases\": ").lower()
while difficulty not in word_lists:
    print("That is not a valid difficulty option.")
    difficulty = input("Choose your difficulty. Type \"easy\", \"medium\", \"hard\", or \"phrases\": ").lower()

# Select a random word from the difficulty list
word: str = random.choice(word_lists[difficulty])
word_len: int = len(word)

# Show non letter characters so that user does not have to guess them
display: list[str] = ["_" if char.isalpha() else char for char in word]
guesses = set()


def clear_screen():
    print("\033[H\033[J", end="")  # Clear the screen
    print(logo + "\n")


def guess_letter():
    guess_input = input("\nGuess a letter or type 'guess' to guess the word: ").lower()
    if len(guess_input) > 1:
        while guess_input != "guess":
            print("\nThat is not a valid guess.")
            guess_input = input("\nGuess a letter or type 'guess' to guess the word: ").lower()
        guess_input = input("What is your guess? ").lower().strip()
        return guess_input
    else:
        while len(guess_input) != 1 or not guess_input.isalpha() or guess_input in guesses:
            print(f"\nYou already guessed \"{guess_input}\"" if guess_input in guesses else "\nThat is not a valid guess.")
            guess_input = input("\nGuess a letter or type 'guess' to guess the word: ").lower()

    return guess_input


clear_screen()
while not end_of_game:
    print(f"Previous Guesses: {', '.join(guesses)}" if len(guesses) > 0 else "")
    print(stages[lives])
    print(" ".join(display))
    guess = guess_letter()
    if len(guess) != 1:
        end_of_game = True
        print(f"\nThe word was '{word}'")
        if guess == word.lower().strip():
            print(f"You guessed the word! You win!")
        else:
            print(f"You guessed incorrectly. You lose.")
    else:
        guesses.add(guess)

        if guess in word.lower():
            for i in range(word_len):
                if word[i].lower() == guess:
                    display[i] = word[i]
            clear_screen()
        else:
            clear_screen()
            lives -= 1
            print(f"\n\"{guess.upper()}\" is not in the word.")
            if lives == 0:
                end_of_game = True
                print(stages[0])
                print(f"\nThe word was \"{word}\". You lose.")
                break
            print(f"You have {lives} lives left.")

    if "_" not in display:
        end_of_game = True
        print(f"\nThe word was \"{word}\". You win!")
