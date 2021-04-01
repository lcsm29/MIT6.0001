# Problem Set 2, hangman.py
# Name: 
# Collaborators: none
# Time spent:
'''
Note - VS Code on Windows will try to run it like this by default.
full_path_to_python_location\python.exe full_path_to_this_file\hangman.py
However, this command results in this error.
FileNotFoundError: [Errno 2] No such file or directory: 'words.txt'
You could go to the hangman.py folder in terminal and run it like this. 
full_path_to_python_location\python.exe hangman.py
'''
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
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
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
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

import string
letters_guessed = ''


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed=True
    for sw_counter in range(len(secret_word)):
        for lg_counter in range(len(letters_guessed)):
            if secret_word[sw_counter] == letters_guessed[lg_counter]:
                break
            elif lg_counter+1 == len(letters_guessed) and secret_word[sw_counter] != letters_guessed[lg_counter]:
                guessed=False
    return guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter_location = ''
    for lg_counter in range(len(letters_guessed)):
        for sw_counter in range(len(secret_word)):
            if letters_guessed[lg_counter] == secret_word[sw_counter]:
                letter_location += str(secret_word[sw_counter])+"_"+str(sw_counter+1)
    print(letter_location)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ''
    for alphabet in range(26):
        for lg_counter in range(len(letters_guessed)):
            if string.ascii_lowercase[alphabet] == letters_guessed[lg_counter]:
                break
            elif lg_counter+1 == len(letters_guessed) and string.ascii_lowercase[alphabet] != letters_guessed[lg_counter]:
                available_letters += string.ascii_lowercase[alphabet]
    return available_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
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
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    global letters_guessed
    print(f"Let's start the game of hangman.\nYou have 6 guesses to identify the secret word, which has {len(secret_word)}-letters.\n")
    for remaining_guesses in range(6):
        print(f"Round {remaining_guesses + 1}. You have {6 - remaining_guesses} guess(es) remaining.")
        while 1:
            user_input = input("Enter your guess: ")
            if len(user_input) == 1 and user_input.encode().isalpha() == True:
                letters_guessed += user_input
                print(f"List of correctly guessed word so far (if it's empty, it means you got none)\n{get_guessed_word(secret_word,letters_guessed)}")
                break
            elif len(user_input) != 1:
                print("You've either entered nothing or too many letters. Please enter one letter.")
            elif user_input.encode().isalpha()==False:
                print("You've entered non English alphabet. Please enter English alphabet.")
        if is_word_guessed(secret_word, letters_guessed) == True:
            print(f"You've successfully beat the game.")
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)
# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
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
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    secret_word = 'test'
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)



'''
You will implement a function called hangman that will allow the user to play hangman
against the computer. The computer picks the word, and the player tries to guess
letters in the word.

Here is the general behavior we want to implement. Don’t be intimidated! This is just
a description; we will break this down into steps and provide further
functional specs later on in the pset so keep reading!

1. The computer must select a word at random from the list of available words
that was provided in words.txt
Note that words.txt contains words in all lowercase letters.  
2. The user is given a certain number of guesses at the beginning.  
3. The game is interactive; the user inputs their guess and the computer either:
a. reveals the letter if it exists in the secret word
b. penalize the user and updates the number of guesses remaining
4. The game ends when either the user guesses the secret word, or the user runs
out of guesses.  
'''