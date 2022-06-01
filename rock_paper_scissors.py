import random


choice_list = ['Rock', 'Paper', 'Scissors']

def rps():
    player1 = input('Make a choice. rock, paper or scissors? ')
    comp_choice = random.choice(choice_list)

    if comp_choice.lower() == 'rock':
        if player1.lower()=='paper': print(f'You win. {player1} beats {comp_choice}')
        elif player1.lower() == 'scissors': print(f'You lose. {comp_choice} beats {player1}')
    elif comp_choice.lower() == 'paper':
        if player1.lower()=='scissors': print(f'You win. {player1} beats {comp_choice}')
        elif player1.lower() == 'rock': print(f'You lose. {comp_choice} beats {player1}')
    elif comp_choice.lower() == 'scissors':
        if player1.lower()=='rock': print(f'You win. {player1} beats {comp_choice}')
        elif player1.lower() == 'paper': print(f'You lose. {comp_choice} beats {player1}')
    else:
        print("Tie. Try again")
        rps()


rps()
