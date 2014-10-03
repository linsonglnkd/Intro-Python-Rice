# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game(game_range):
    # initialize global variables used in your code here
    global secret_number
    global guess
    global num_attempt
    global current_range
    print
    secret_number = random.randrange(game_range)
    current_range = game_range
    if game_range == 100 :
        num_attempt = 7
    else :
        num_attempt = 10
    print '----- new game: range ' + str(game_range) + ' -----'
    print 'number of attempts left: ' + str(num_attempt)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game(100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game(1000)
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(guess)
    global num_attempt
    print
    print "Guess was " + str(guess)
    win_flag = False
    if secret_number > guess :
        print 'Higher!'
    elif secret_number < guess :
        print 'Lower!'
    else :
        print 'Correct!'
        win_flag = True
    if win_flag :
        new_game(current_range)
    else :
        num_attempt -= 1
        print 'number of attempts left: ' + str(num_attempt)
        if num_attempt == 0 :
            print 'You lose.'
            new_game(current_range)

    
# create frame
frame = simplegui.create_frame('Guess number:', 100, 300)

# register event handlers for control elements and start frame
inp = frame.add_input("Input", input_guess, 100)
button_1 = frame.add_button("Range: 0 - 100",	range100)
button_2 = frame.add_button("Range: 0 - 1000",	range1000)


# call new_game 
new_game(100)


# always remember to check your completed program against the grading rubric
