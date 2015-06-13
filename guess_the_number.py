# "Guess the number" mini-project
# http://www.codeskulptor.org/#user40_AtDk5AM7AT_41.py
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui as sg
import math
import random

# set number of guesses constants
NUM_GUESS_100 = 7
NUM_GUESS_1000 = 10

# global variables and their default values
secret_number = 0
num_range = 100
num_guess = 7
counter = 0

# helper function to start and restart the game
def new_game():
    """
    initialize the game by generating new 
    random number with the current game setting
    """
    global secret_number, counter
    print "New game! Range is from 0 to", num_range
    print "Number of remaining guesses is", num_guess
    print ""
    counter = 0
    secret_number = random.randrange(num_range) 
    
# define event handlers for control panel
def range100():
    """
    button that changes the range to [0,100) 
    and starts a new game 
    """
    global num_range, num_guess
    num_range = 100
    num_guess = NUM_GUESS_100
    new_game()

def range1000():
    """
    button that changes the range to [0,1000) 
    and starts a new game 
    """
    global num_range, num_guess
    num_range = 1000
    num_guess = NUM_GUESS_1000
    new_game()

def input_guess(guess):
    """
    compare player's guess to the secret number
    and print out the result along with remaining
    number of guesses. if the player guesses correctly
    or the guesses run out, a new game starts.
    """
    global num_guess, counter
    num_guess -= 1
    counter += 1
    guess = int(guess)
    print "Guess was", guess
    print "Number of remaining guesses is", num_guess
    
    if (num_guess == 0) and (guess != secret_number):
        print "You ran out of guesses. " \
                "The number was", secret_number, "\n"
        num_guess += counter
        new_game()
    elif guess < secret_number: 
        print "Higher!\n"
    elif guess > secret_number: 
        print "Lower!\n"
    else: 
        print "Correct!\n"
        num_guess += counter
        new_game()
  
# create frame
frame = sg.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


