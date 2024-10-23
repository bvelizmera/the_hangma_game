from words_and_movies_titles import random_words, famous_movies
from ascii_hangman import HANGMANPICS
import random


def main():
    print("Welcome to the Hangman Game!\nYou will have to guess the name of a famous movie title.")
    title = choose_word(famous_movies)
    guess_letter(title)

# Function to choose random title


def choose_word(words):
    return random.choice(words)

# Function to guess the letters


def guess_letter(word):
    title = word
    # convert everything to lower case
    word = word.lower()
    # Establish initial parameters for the game
    lives = len(HANGMANPICS) - 1
    wrong_guesses = 0
    result = []
    words = []

    # run through every letter of the word to convert it into a list
    for char in word:
        # checks for letters in the title
        if char.isalpha():
            words.append(char)
            result.append("__")
        else:  # This includes spaces and punctuation
            words.append(char)
            result.append(char)

    while True:  # Continue until the game ends
        print(HANGMANPICS[wrong_guesses])  # Display the current hangman state
        # Print current unrevealed letters
        print(" ".join(result) + "\n")
        print(f"Lives remaining: {lives}")

        # Ask user for input
        j = input("Please insert a letter or guess the full title: ").lower()
        # Checks if full guess
        if len(j) > 1:  # Full word guess
            if j == word:
                print(f"Well done! The movie title is: {title}")
                break
            else:
                print("Incorrect full guess!")
                lives -= 1
                wrong_guesses += 1
        # Checks if it's one letter
        elif len(j) == 1 and j.isalpha():  # Single letter guess
            if j in result:
                print("You already guessed that letter.")
            elif j in word:
                for i in range(len(word)):
                    if word[i] == j:
                        result[i] = j
            else:
                print("Incorrect guess!")
                lives -= 1
                wrong_guesses += 1

        # Check for win condition
        if result == words:  # If all letters are revealed
            print("Congratulations! You've guessed the movie title:", title)
            break

        # Check for game over condition
        if lives == 0:  # If lives are less than 0, it's game over
            print(HANGMANPICS[wrong_guesses])
            print("Game Over")
            print(f"The correct answer was: {title}")
            break


main()
