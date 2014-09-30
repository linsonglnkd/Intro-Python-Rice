# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guess
    secret_number = random.randrange(100)
    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(100)
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randrange(1000)
    pass
    
def input_guess(guess):
    # main game logic goes here	
    guess = int(inp.get_text())
    print guess, secret_number
    print 
    if secret_number > guess :
        print 'Higher!'
    elif secret_number < guess :
        print 'Lower!'
    else :
        print 'Correct!'
    # remove this when you add your code
    pass

    
# create frame
frame = simplegui.create_frame('Guess number:', 100, 300)

# register event handlers for control elements and start frame
inp = frame.add_input("Input", input_guess, 100)
button_1 = frame.add_button("Range: 0 - 100",	range100)
button_2 = frame.add_button("Range: 0 - 1000",	range1000)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
