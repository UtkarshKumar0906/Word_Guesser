import random

# Get the player's name
name = input("What is your name? ")
print("Hello " + name)

# List of words for the game
words = ['apple', 'banana', 'elephant', 'computer', 'happiness', 'rainbow', 'guitar', 'mountain', 'adventure', 'pineapple', 'butterfly', 'happiness', 'universe', 'chocolate', 'waterfall', 'symphony', 'library', 'galaxy', 'wizard', 'treasure', 'harmonica']

# Select a random word from the list
word = random.choice(words)
print("Guess the word by guessing a character. If you get 10 guesses wrong, you are out!")

# Initialize variables
guesses = ''
turns = 10

while turns > 0:
    # Variable to track if the player guessed incorrectly
    failed = 0

    # Check each character in the word
    for char in word:
        if char in guesses:
            print(char, end=" ")  # Print the character if guessed correctly
        else:
            print('_', end=" ")  # Print underscore for unguessed characters
            failed += 1

    # Check if all characters have been guessed
    if failed == 0:
        print("\nYou win")
        print("The Word is " + word)
        break

    # Get the player's guess
    guess = input("\nGuess a character: ")

    # Add the guess to the list of guesses
    guesses += guess

    # Check if the guess is incorrect
    if guess not in word:
        turns -= 1
        print("Wrong guess")
        print("You have " + str(turns) + " remaining")
        
        # Check if the player has no more turns
        if turns == 0:
            print("You lose")
