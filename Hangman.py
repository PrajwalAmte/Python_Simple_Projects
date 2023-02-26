# Hangman game
word = "python"
guessed_letters = ()
attempts_left = 6

while attempts_left > 0:
    letter = input("\nGuess a letter: ")

    if letter in word:
        print("Correct!")
        guessed_letters += (letter,)
    else:
        print("Wrong!")
        attempts_left -= 1

    print("Guessed letters: ", guessed_letters)
    print("Attempts left: ", attempts_left)

print("Game over!")