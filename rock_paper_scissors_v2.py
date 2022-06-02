import random

choices = ['R', 'P', 'S']
choice_dict = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

def rps():
    user_input = input("Pick a choice, [R, P or S]: ")
    user_input = user_input.upper()
    if user_input not in choices:
        print("Try again")

    cpu_pick = random.choice(choices)
    print(f"Player ({choice_dict[user_input]}) : CPU ({choice_dict[cpu_pick]})")

    if user_input == cpu_pick:
        print("Tie. Try again")
        return repr(rps())
    elif user_input == "R":
        if cpu_pick == 'S': 
            return ("Player wins")
        else:
            return ("CPU wins")
    elif user_input == "S":
        if cpu_pick == "P":
            return ("Player wins")
        else:
            return ("CPU wins")
    elif user_input == "P":
        if cpu_pick == "R":
            return ("Player wins")
        else:
            return ("CPU wins")

print(repr(rps()))