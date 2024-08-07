#THE HANGMAN

import random

def hanged_man(counter = 0):
    hangman_diagram = [
        "   ___",
        "  |   |",
        "  |",
        "  |",
        "  |",
        "  |",
        "__|__"
    ]

    if counter == 1:
        hangman_diagram[2] = "  |   O"
    elif counter == 2:
        hangman_diagram[2] = "  |   O"
        hangman_diagram[3] = "  |   |"
    elif counter == 3:
        hangman_diagram[2] = "  |   O"
        hangman_diagram[3] = "  |  /|"
    elif counter == 4:
        hangman_diagram[2] = "  |   O"
        hangman_diagram[3] = "  |  /|\\"
    elif counter == 5:
        hangman_diagram[2] = "  |   O"
        hangman_diagram[3] = "  |  /|\\"
        hangman_diagram[4] = "  |  /"
    elif counter == 6:
        hangman_diagram[2] = "  |   O"
        hangman_diagram[3] = "  |  /|\\"
        hangman_diagram[4] = "  |  / \\"

    for line in hangman_diagram:
        print(line)

counter = 0

print("THE HANGMAN.\nBELOW YOU HAVE BEEN GIVEN A WORD TO GUESS.\nGUESS THE WORD LETTER BY LETTER.\nYOU WILL BE GIVEN 6 LIVES. IF YOU GUESS WRONG FOR 6 TIMES, THE MAN WILL BE HANGED!\n  GOODLUCK!!!")
hanged_man()

with open('words.txt', 'r') as file:
    diction = file.read().splitlines()
selected = random.choice(diction)
dashes = ['_'] * len(selected)
print("\n\nWORD:", end = ' ')
print(" ".join(dashes))

while True:
    print("\n\n")
    guess = input("Guess a letter: ")
    if guess in selected:
        print("Correct!!")
        positions = [pos for pos, char in enumerate(selected) if char == guess]
        for position in positions:
            dashes[position] = guess
        print("\n")
        print("WORD:", end = ' ')
        print(" ".join(dashes))
    else:
        print("\n\nOH NO!! Try again.\n")
        print("WORD:", end = ' ')
        print(" ".join(dashes))
        counter += 1
        print()
        hanged_man(counter)
        if counter == 6:
            print("Game over.\nThe word was", selected)
            break

    if '_' not in dashes:
        print(f"Congratulations!\nThe word was {selected}.")
        break