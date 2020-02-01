import string
from words import choose_word
from images import IMAGES
def ifValid(user_input):
    if len(user_input) != 1:
        return False
    if not user_input.isalpha():
        return False
    return True
def get_hint(secret_word, letters_guessed):
    import random
    letters_not_guessed = []
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index += 1
    return random.choice(letters_not_guessed)
def is_word_guessed(secret_word, letters_guessed):
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True
    return False
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    return letters_left
def hangman(secret_word):
    print "Welcome to the game, Hangman! \n"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long. \n"
    jk=int(input('''Enter the difficulty level in numbers :
                1.Easy
                2.Medium
                3.Hard \n '''))
    if jk==1:
        remaining_lives=8
    elif jk==2:
        remaining_lives=6
    elif jk==3:
        remaining_lives=4
    else:
        print'''invalid input let's start in easy level \n'''
        remaining_lives=8
    letters_guessed = []
    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        print "Available letters:   " + available_letters
        guess = raw_input("\n Please guess a letter:   ")
        letter = guess.lower()
        if (not ifValid(letter)):
            print "\n invalid input"
            continue
        else:
            # print IMAGES[8-remaining_lives]

            if letter in secret_word:
                letters_guessed.append(letter)
                print "\n Good guess: " + get_guessed_word(secret_word, letters_guessed)
                print "\n"
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print " \n * * Congratulations, you won! * * "
                    print "\n"
                    break
            else:
                print "\n Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
                print "\n Remaining Lives : \n", remaining_lives
                print IMAGES[8-remaining_lives]
                letters_guessed.append(letter)
                remaining_lives -= 1
    else:
        print "\n Sorry, you ran out of guesses. The word was: " + str(secret_word) + "."
secret_word = choose_word()
hangman(secret_word)