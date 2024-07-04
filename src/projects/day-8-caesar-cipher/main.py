from typing import List
from art import logo

alphabet: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text: str, shift_num: int, cipher_direction: str) -> str:
    end_text = ""
    if cipher_direction == "decode":
        shift_num *= -1

    for letter in start_text:
        if not letter.isalpha():
            end_text += letter
            continue
        new_index: int = alphabet.index(letter) + shift_num
        end_text += alphabet[new_index]

    return end_text


print(logo)

while True:
    direction: str = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ['encode', 'decode']:
        print("Please type 'encode' or 'decode'.\n")
        direction: str = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text: str = input("Type your message:\n").lower()
    shift: int = int(input("Type the shift number:\n")) % 26

    print(f"The {direction}d message is \"{caesar(text, shift, direction)}\"")

    go_again: str = input("Would you like to go again? (yes/no): ")
    while go_again.lower() not in ['yes', 'no']:
        print("Please type 'yes' or 'no'.\n")
        go_again: str = input("Type 'yes' to keep ciphering or 'no' to quit.\n: ")

    if go_again.lower() == "no":
        break
