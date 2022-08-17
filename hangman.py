import random
from random import randint
import numpy as np
import sys

starter_words = {}

letters_used = {}

lives = 6


#menu

menu_choice = input("Menu\n1. Play Game\n2. How to Play\n 3. Add Your Own Word\n 4. Exit\n")
if menu_choice.isnumeric:
    menu_choice = int(menu_choice)
else:
    print("Enter a valid choice")

if menu_choice == 1:
#play 
    word = randint(starter_words[0], len(starter_words) - 1)
    endCondition = False
    while endCondition == False:
        print_board()
elif menu_choice == 2:
#how to play   
    print("PEE")
elif menu_choice == 3:
#add word to list in file
    print("POO")
elif menu_choice == 4:
#exit
    sys.exit("Thank you! Goodbye!")
else:
#other number/word 
    print("Invalid input! Please enter a valid number!")



    
    #print_board function needs incorrect letter guessed and correct letters guessed, along with answer word
def print_board(correctWord, incorrectLetters, correctLetters):
    example = "cat"
    for x in example:
        spaces += "_ "
    #draw man function here !
    print(spaces)
    letter_guess = input("Enter a letter to guess")

    


def matching_indices(correct_word, guess):
    matching = {}
    for x in len(correct_word):
        matching.update({correct_word[x]: x})
    return matching


