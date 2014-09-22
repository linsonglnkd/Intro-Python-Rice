# mini project: Rock-paper-scissors-lizard-Spock
#   0 — rock
#   1 — Spock
#   2 — paper
#   3 — lizard
#   4 — scissors

import random

def name_to_number(name) :
    if name.lower() == 'rock' :
        return 0
    elif name.lower() == 'spock' :
        return 1
    elif name.lower() == 'paper' :
        return 2
    elif name.lower() == 'lizard' :
        return 3
    elif name.lower() == 'scissors' :
        return 4
    else :
        print 'Errors in input: not in (rock, spock, paper, lizard, scissors)'
        return -1

def number_to_name(number) :
    if number == 0 :
        return 'rock'
    elif number == 1 :
        return 'spock'
    elif number == 2 :
        return 'paper'
    elif number == 3 :
        return 'lizard'
    elif number == 4 :
        return 'scissors'
    else :
        print 'Error in number!'
        return 'Error in number!'

def rpsls(player_choice) :
    print
    print 'Player chooses %s' % player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(5)
    comp_name = number_to_name(comp_number)
    print 'Computer chooses %s' % comp_name
    compare = (player_number - comp_number) % 5
    if compare in (1,2) :
        print 'Player wins!'
    elif compare in (3,4) :
        print 'Computer wins!'
    else :
        print 'Player and computer tie!'
   
for i in range(10) :
    rpsls('lizard')
