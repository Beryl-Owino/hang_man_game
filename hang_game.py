import random

def choosen_word():
    """_summary_: Generate a random word from the list for user to guess.

    Returns:
        str: it return a random number from the list.
    """
    playing_words = ['cat', 'cow', 'dog', 'top']
    pick_word = random.choice(playing_words)
    return pick_word



def display_word(word, guessed_letters):
    """
    Display the word with underscores for unguessed letters.
    
    Parameters:
    - word (str): The word to be guessed.
    - guessed_letters (list): List of letters guessed by the player.
    
    Returns:
    str: The word with the first letter revealed and underscores for unguessed letters.
    """
    displayed_word = ""
    for i, letter in enumerate(word):
        if letter in guessed_letters or i == 0:  # Reveal the first letter
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def guess():
    """Capture user guesses."""
    user_guess = input("Please enter a single letter: ").lower()

    # Validate that the input is a single letter
    if len(user_guess) == 1 and user_guess.isalpha():
        return user_guess
    else:
        print("Invalid input. Please enter a single letter.")
        # Retry the guess
        return guess()
    

def hangman():
    chosen_word = choosen_word()
    word_length = len(chosen_word)
    max_attempts = 3
    attempts = 0
    guessed_letters = set()
    revealed_word = chosen_word[0] + " _" * (word_length - 2)

    print("Welcome to Hangman!")

    while True:
        displayed = display_word(revealed_word, guessed_letters)
        print(f"Word to Guess: {displayed}")

        # Check if the player has guessed the entire word
        if set(guessed_letters) == set(chosen_word):
            print("Congratulations! You guessed the word.")
            break

        # Get a word guess from the player
        user_word_guess = input("Please enter your word guess: ").lower()

        # Check if the guessed word is correct
        if user_word_guess == chosen_word:
            print(f"Congratulations! '{user_word_guess}' is the correct word.")
            break
        else:
            print(f"Sorry, '{user_word_guess}' is not the correct word. Try again.")
            attempts += 1

        # Check if the player has used all attempts
        if attempts == max_attempts:
            print("Out of attempts. You didn't guess the word.")
            print(f"The word was: {chosen_word}")
            break


hangman()
