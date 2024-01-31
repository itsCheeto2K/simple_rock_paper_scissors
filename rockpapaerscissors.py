import random

print('1: Rock\n2: Paper\n3: Scissors')
player_choice = int(input('Rock, paper or scissors?: '))
computer_choice = random.choice([1, 2, 3])

if player_choice == 1:
    if computer_choice == 2:
        print('Player lose. Computer have Paper!')
    elif computer_choice == 3:
        print('Player win. Computer have Scissors!')
    else:
        print('Draw')
elif player_choice == 2:
    if computer_choice == 3:
        print('Player lose. Computer have Scissors!')
    elif computer_choice == 1:
        print('Player win. Computer have Rock!')
    else:
        print('Draw')
elif player_choice == 3:
    if computer_choice == 1:
        print('Player lose. Computer have Rock!')
    elif computer_choice == 2:
        print('Player win. Computer have Paper!')
    else:
        print('Draw') 
else:
    print('WRONG INPUT, PLEASE ENTER AGAIN!')       