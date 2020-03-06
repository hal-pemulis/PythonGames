"""Hangman
Travis Tyler
Feb. 2, 2019"""

# For selection of random word from word bank
import random

# Allows web scraping
import urllib.request


# Assigns URL to variable
word_url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

# Scrapes page of English words
response = urllib.request.urlopen(word_url)

# Sets data from URL as text
long_txt = response.read().decode()

# Creates a list of English words
word_bank = long_txt.splitlines()

# Displays underscores representing unguessed letters
blanks = []

# The random word separated into a list
correct = []

guessed_letters = []


# Title screen
title = """

 _   _      __   _      _    ___      _____       _      _      __   __     _  
| | | |    /  | |  \   | |  /   \     |   |      | \    / |    /  | |  \   | |
| | | |   /   | |   \  | | |  /\_|        |      |  \  /  |   /   | |   \  | |
| |_| |  / /| | | |\ \ | | | | __         |      |   \/   |  / /| | | |\ \ | | 
|  _  | | |_| | | | \ \| | | ||_ |        |      | |\  /| | | |_| | | | \ \| |
| | | | |  _  | | |  \   | | |  ||        |      | | \/ | | |  _  | | |  \   |
| | | | | | | | | |   \  | | |__||        |      | |    | | | | | | | |   \  |
|_| |_| |_| |_| |_|    \_|  \___/    _____|___   |_|    |_| |_| |_| |_|    \_|

"""

# Text depiction of hanged man
dead_man = ["""
   ____
  |    |
       |
       |
       |
       |
_______|__       
""", """
   ____
  |    |
  o    |
       |
       |
       |
_______|__       
""", """
   ____
  |    |
  o    |
  |    |
       |
       |
_______|__       
""", """
   ____
  |    |
  o    |
 /|    |
       |
       |
_______|__       
""", """
   ____
  |    |
  o    |
 /|\   |
       |
       |
_______|__       
""", """
   ____
  |    |
  o    |
 /|\   |
 /     |
       |
_______|__       
""", """
   ____
  |    |
  o    |
 /|\   |
 / \   |
       |
_______|__       
"""]


# Function to select a random word from the word bank
def select_word():
    word = random.choice(word_bank)
    for letter in word:
        correct.append(letter)
        blanks.append('_')


# Function that lets the player make guesses
def player_guess():

    # Sets number of strikes to zero
    strikes = 0

    # Converts the list 'correct' to a string
    word_string = ''.join(correct)

    # Shows the starting game board
    print(dead_man[strikes])

    # Determines whether the player has won or lost (can still make guesses)
    while strikes < 6 and correct != blanks:

        # Loops through the list blanks
        for letter in blanks:

            # Displays word length and which letters are guessed/unguessed
            print(letter, end=' ')

        # Instructs a player to guess a letter and assigns that letter to the variable 'guess'
        guess = input('\nGuess a letter: ')

        # Determines if the user input is in the list 'correct' at all
        if guess in correct and guess not in guessed_letters:

            # Loops through 'correct' and gets the location of the guessed letter within the list
            for letter in range(len(correct)):

                # Uses list location in 'correct' to replace unguessed letter in 'blanks'
                if correct[letter] == guess:
                    blanks[letter] = correct[letter]

            # Lets the player know the guess was correct and displays current game board
            print(dead_man[strikes] + '\nYES!')

            # Adds letter to list
            guessed_letters.append(guess)

        elif guess in blanks:
            print('You have already guessed that letter')

        elif guess in guessed_letters:
            print('You have already guessed that letter')

        # If the guess was wrong
        else:

            # Adds 1 to the current number of strikes if guess incorrect
            strikes += 1

            # Adds letter to list
            guessed_letters.append(guess)

            # Lets the player know guess was wrong and displays current game board
            print(dead_man[strikes] + '\nWRONG')

    # Checks if number of incorrect guesses has reached the max of 6
    if strikes == 6:

        # Displays game over notification and reveals the word
        print('\nRIP, LOSER\nThe word was ' + word_string)

    # Displays win notification and starting game board if there are no blanks remaining and strikes less than 6
    else:
        print(dead_man[0] + 'YOU WIN!\nThe word was ' + word_string)


# Function that determines game/function order
def main():

    # Displays title screen
    print(title)

    # Asks player to play
    input('Press ENTER to play...')

    # Sets 'again' variable to empty string
    again = ''

    # Sets up loop while the player has not entered 'n' at the 'play again' screen
    while again != 'n':

        # Resets 'blank' list
        del blanks[:]

        # Resets 'correct' word list
        del correct[:]

        # Resets guessed letter list
        del guessed_letters[:]

        # Runs function to select random word
        select_word()

        # Runs guess function
        player_guess()

        # Asks user to play again and sets 'again' variable to input
        again = input('Play again? (y/n): ')

        # Sets up loop until input equals 'y' or 'n'
        while again != 'y':

            # Instructs user to input only acceptable characters if not 'y' or 'n'
            print('Please select only "y" or "n"')

            again = input('Play again? (y/n): ')


# Runs main game function
main()
