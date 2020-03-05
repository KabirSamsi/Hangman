import os
import random
file = open('words.txt', 'r')
words = []
for line in file.read().split('\n'):
    if len(line) >= 5:
        words.append(line.strip())

#Takes guessing word and clears screen to hide it
print("WELCOME TO HANGMAN")
word = random.choice(words)

#Game variables
correct_guessed_letters = []
wrong_guessed_letters =  []
guessed_word = ""
guesses_left = ['hat', 'head', 'torso', 'first arm', 'second arm', 'first leg', 'second leg']
letters = 'abcdefghijklmnopqrstuvwxyz'
welcome = "Guessed word so far: "

#Creates welcome message with some parameters
print("WELCOME TO HANGMAN\n")
for letter in word:
    if letter in letters:
        welcome += "-"
    elif letter not in letters:
        welcome += letter
print(welcome)

#Loop to take guess and evaluate it
while len(guesses_left) > 0:
    print("Correct letters: {}".format(', '.join(correct_guessed_letters)))
    print("Incorrect letters: {}".format(', '.join(wrong_guessed_letters)))
    print("Guesses left: {}".format(len(guesses_left)))
    guess = input("Guess a letter: ")

    #While guess has already been gueessed
    while guess in correct_guessed_letters or guess in wrong_guessed_letters:
        guess = input("You already guessed this letter, try again: ")
    #While guess is not valid
    while len(guess) != 1 or guess not in letters:
        guess = input("Guesses must be letters and must be one character long, try again: ")
    while guess in correct_guessed_letters or guess in wrong_guessed_letters:
        guess = input("You already guessed this letter, try again: ")

    #Evaluates if guess is correct or not
    if guess in word:
        print("Nice job! '{}' is in the word.\n".format(guess))
        correct_guessed_letters.append(guess)
    else:
        print("Too bad! '{}' is not in the word. You lost your {}\n".format(guess, guesses_left[0]))
        wrong_guessed_letters.append(guess)
        guesses_left.pop(0)
    guessed_word = ""

    #Updates the guessed word variable and prints it out
    for letter in word:
        if letter in correct_guessed_letters or letter not in letters:
            guessed_word += letter
        elif letter not in correct_guessed_letters and letter in letters:
            guessed_word += "-"
    print("Guessed word so far: {}".format(guessed_word))

    #Win condition
    if guessed_word == word:
        print("NICE JOB! YOU WON THE GAME WITH {} GUESSES REMAINING!!!!!!!".format(len(guesses_left)))
        break

#Lose condition
if len(guesses_left) == 0:
    print("Sorry, you lost. The word was '{}'. Better luck next time.".format(word))
