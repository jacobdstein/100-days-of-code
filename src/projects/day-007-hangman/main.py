import random
from hangman_words import word_lists
from hangman_art import stages, logo

end_of_game: bool = False
lives: int = 6

# Avoid confusion by "clearing" the console so user sees only one hangman picture
def clear():
    print("\n" * 10)


print(logo + "\n")

# Prompt user to choose difficulty
difficulty: str = input("Choose your difficulty. Type \"easy\", \"medium\", \"hard\", or \"phrases\": ").lower()
while difficulty not in word_lists:
    print("That is not a valid difficulty option.")
    difficulty = input("Choose your difficulty. Type \"easy\", \"medium\", \"hard\", or \"phrases\": ").lower()

# Select a random word from the difficulty list
word: str = random.choice(word_lists[difficulty])
word_len: int = len(word)

# If the selected mode is phrases, show non letter characters so that user does not have to guess them
display: list[str] = ["_" if char.isalpha() else char for char in word] if difficulty == "phrases" else ["_"] * word_len
guesses = set()

clear()
while not end_of_game:
    print(stages[lives])
    print(" ".join(display))
    guess = input("\nGuess a letter: ").lower()
    while len(guess) != 1 or not guess.isalpha() or guess in guesses:
        print(f"\nYou already guessed \"{guess}\"" if guess in guesses else "\nThat is not a valid guess.")
        guess = input("\nGuess another letter: ").lower()

    guesses.add(guess)
    if guess in word.lower():
        for i in range(word_len):
            if word[i].lower() == guess:
                display[i] = word[i]
        clear()
    else:
        clear()
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
