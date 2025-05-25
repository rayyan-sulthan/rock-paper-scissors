import random

def get_choices():
    player_choice = input("Enter your choice (rock,paper,scissors):")
    options = ["rock","paper","scissors"]
    computers_choice = random.choice(options)
    choices ={"player":player_choice, "computer":computers_choice}
    return choices

def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "its a tie"
    
    elif player == "rock":
        if computer ==  "scissors":
            return "rock smashes scissors! YOU WIN"
        else:
            return "paper fold rock! COMPUTER WINS"
        
    elif player == "paper":
        if computer ==  "rock":
            return "paper fold rock! YOU WIN"
        else:
            return "scissors cut paper! COMPUTER WINS"
    
    elif player == "scissors":
        if computer ==  "paper":
            return "scissors cut paper! YOU WIN"
        else:
            return "rock smash scissors! COMPUTER WINS"
        
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
