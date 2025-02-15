# Hangman Game in Python
from WordsList import words
import random

hangman_art = {0: ("        ",
                   "        ",
                   "        "),
               1: ("    o    ",
                   "        ",
                   "        "),
               2: ("    o    ",
                   "    |    ",
                   "        "),
               3: ("    o    ",
                   "   /|    ",
                   "        "),
               4: ("    o    ",
                   "   /|\\    ",
                   "        "),
               5: ("    o    ",
                   "   /|\\    ",
                   "   /    "),
               6: ("    o    ",
                   "   /|\\    ",
                   "   / \\   "),}

def display_hangman(wrong_guesses):
    print("***********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

# main function
def Hangman_Game():
    answer = random.choice(words).lower()
    #hint = ["_"] * len(answer)
    hint = ["_" if char.isalpha() else char for char in answer]  
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter, space, or hyphen: ").lower()

        # if the user types an input that is not valid 
        # for example if the user types a whole word "pizza",
        # the program will not accept it and will ask for a letter
        if len(guess) != 1 or not (guess.isalpha() or guess in [" ", "-"]):
            print("Please enter a single letter, space, or hyphen.\n")
            continue

        # validation for, if the user types a letter that is already guessed
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}', try another one.")
            continue
        guessed_letters.add(guess)


        # if a letter is found within the hint, we need to switch that underscore to each letter
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        # Win condition: No more underscores left in hint
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("🎉 Congratulations, you won!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("💀 Game Over, you lost!")
            is_running = False


if __name__ == "__main__":
    Hangman_Game()
