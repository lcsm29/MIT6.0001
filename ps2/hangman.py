# Problem Set 2, hangman.py
# Name: lcsm29
# Collaborators: None
# Time spent: unknown
# ver 0.13.210528 - decluttered (mostly non-main functions)

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """ Returns a list of valid words. Words are strings of lowercase letters
    Depending on the size of the word list, this function may take a while
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """ wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """ secret_word: string, the word the user is guessing
        assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far
        assumes that all letters are lowercase
    Returns: boolean, True if all the letters of secret_word
        are in letters_guessed; False otherwise
    """
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    """ secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    Returns: string, comprised of letters, underscores (_), and spaces
        that represents which letters in secret_word have been guessed so far
    """
    sw, lg = secret_word, letters_guessed
    return ''.join(['_' if c not in lg else c for c in sw])


def get_available_letters(letters_guessed):
    """ letters_guessed: list (of letters), which letters have been
        guessed so far
    Returns: string (of letters), comprised of letters that represents
        which letters have not yet been guessed.
    """
    lo, g = string.ascii_lowercase, letters_guessed
    return lo if g == '' else ''.join([c for c in lo if c not in g])


def hangman(secret_word):
    """ secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.
    Follows the other limitations detailed in the problem write-up.
    """
    letters_guessed = ''
    g_remaining, w_remaining = 6, 3
    user_input = ''

    def input_validator(user_input):
        nonlocal letters_guessed
        if len(user_input) == 1 and user_input.encode().isalpha():
            if user_input.isupper():
                user_input = user_input.lower()
            if user_input not in letters_guessed:
                letters_guessed += user_input
            return True
        else:
            return False

    def invalid_char_penalty():
        nonlocal g_remaining, w_remaining
        if w_remaining > 0:
            w_remaining -= 1
            penalty = "You have " + str(w_remaining) + " warnings left:"
        else:
            g_remaining -= 1
            penalty = "You have no warnings left so you lose one guess:"
        return penalty

    def wrong_guess_penalty():
        nonlocal g_remaining
        if user_input.lower() in ('a', 'e', 'i', 'o', 'u'):
            g_remaining -= 2
        else:
            g_remaining -= 1

    # print welcome message
    print(
        f"Welcome to the game Hangman!\n"
        f"I am thinking of a word that is {len(secret_word)} letters long\n"
        f"You have {w_remaining} warnings left.")
    while g_remaining >= 1:
        # before proceeding into the loop, check if the word has been guessed
        if is_word_guessed(secret_word, letters_guessed) == True:
            print(
                f"----------\n"
                f"Congratulations, you won!\n"
                f"Your total score for this game is:  {len(set(secret_word)) * g_remaining}"
            )
            return
        # printing required statements and take user_input
        print(
            f"----------\n"
            f"You have {g_remaining} guesses left\n"
            f"Available Letters: {get_available_letters(letters_guessed)}"
        )
        user_input = input("Please guess a letter: ")
        # if user entered nothing, give him a free pass and loop again.
        if user_input == '':
            continue
        # if it's already been guessed, issue a penalty notice and jump to next iteration
        if user_input.lower() in letters_guessed:
            print(
                f"Oops! You've already guessed that letter. "
                f"{invalid_char_penalty()} {get_guessed_word(secret_word, letters_guessed)}"
            )
            continue
        # if it's invalid (non-English alphabet, blank, or len > 1), give user a warning/penalty
        if input_validator(user_input) == False:
            print(
                f"Oops! That is not a valid letter. "
                f"{invalid_char_penalty()} {get_guessed_word(secret_word, letters_guessed)}"
            )
        # if user_input is valid, check if it's correct and print accordingly
        if input_validator(user_input) == True:
            if user_input.lower() not in secret_word:
                wrong_guess_penalty()
                print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            elif user_input.lower() in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
    # if g_remaining ran out, print end of game
    print(
        f"-----------\n"
        f"Sorry, you ran out of guesses. The word was {secret_word}."
    )

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)
# -----------------------------------


def match_with_gaps(my_word, other_word):
    """ my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    Returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    if len(my_word) == len(other_word):
        for i, char in enumerate(my_word):
            if char != '_' and char != other_word[i]:
                break
            if i + 1 == len(my_word):
                return True
    return False


def show_possible_matches(my_word):
    """ my_word: string with _ characters, current guess of secret word
    Returns: nothing, but should print out every word in wordlist that
        matches my_word. Keep in mind that in hangman when a letter is
        guessed, all the positions at which that letter occurs in
        the secret word are revealed. Therefore, the hidden letter(_) cannot
        be one of the letters in the word that has already been revealed.
    """
    possible_matches = [w for w in wordlist if match_with_gaps(my_word, w)]
    if len(possible_matches) == 0:
        print("No matches found")
    else:
        print(f"Possible matches are: {' '.join(possible_matches)}")


def hangman_with_hints(secret_word):
    """ secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many letters
      the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    letters_guessed = ''
    g_remaining, w_remaining = 6, 3
    user_input = ''

    def input_validator(user_input):
        nonlocal letters_guessed
        if len(user_input) == 1 and user_input.encode().isalpha():
            if user_input.isupper():
                user_input = user_input.lower()
            if user_input not in letters_guessed:
                letters_guessed += user_input
            return True
        else:
            return False

    def invalid_char_penalty():
        nonlocal g_remaining, w_remaining
        if w_remaining > 0:
            w_remaining -= 1
            penalty = "You have " + str(w_remaining) + " warnings left:"
        else:
            g_remaining -= 1
            penalty = "You have no warnings left so you lose one guess:"
        return penalty

    def wrong_guess_penalty():
        nonlocal g_remaining
        if user_input.lower() in ('a', 'e', 'i', 'o', 'u'):
            g_remaining -= 2
        else:
            g_remaining -= 1

    # print welcome message
    print(
        f"Welcome to the game Hangman!\n"
        f"I am thinking of a word that is {len(secret_word)} letters long\n"
        f"You have {w_remaining} warnings left."
    )
    while g_remaining >= 1:
        # before proceeding into the loop, check if the word has been guessed
        if is_word_guessed(secret_word, letters_guessed) == True:
            print(
                f"----------\n"
                f"Congratulations, you won!\n"
                f"Your total score for this game is: {len(set(secret_word)) * g_remaining}"
            )
            return
        # printing required statements and take user_input
        print(
            f"----------\n"
            f"You have {g_remaining} guesses left\n"
            f"Available Letters: {get_available_letters(letters_guessed)}"
        )
        user_input = input("Please guess a letter: ")
        # if user entered *, call show_possible_matches
        if user_input == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue
        # if user entered nothing, give him a free pass and loop again.
        if user_input == '':
            continue
        # if it's already been guessed, issue a penalty notice and jump to next iteration
        if user_input.lower() in letters_guessed:
            print(
                f"Oops! You've already guessed that letter. "
                f"{invalid_char_penalty()} {get_guessed_word(secret_word, letters_guessed)}"
            )
            continue
        # if it's invalid (non-English alphabet, blank, or len > 1), give user a warning/penalty
        if input_validator(user_input) == False:
            print(
                f"Oops! That is not a valid letter. "
                f"{invalid_char_penalty()} {get_guessed_word(secret_word, letters_guessed)}"
            )
        # if user_input is valid, check if it's correct and print accordingly
        if input_validator(user_input) == True:
            if user_input.lower() not in secret_word:
                wrong_guess_penalty()
                print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            elif user_input.lower() in secret_word:
                print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
    # if g_remaining ran out, print end of game
    print(
        f"-----------\n"
        f"Sorry, you ran out of guesses. The word was {secret_word}."
    )


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
