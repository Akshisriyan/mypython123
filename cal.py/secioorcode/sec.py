import random

options = ["rock", "paper", "scissor"]

computer = random.choice(options)

def player_input():
    player = input("Choose one among 'Rock', 'Paper, 'Scissor': ")
    player = player.lower()
    return player


player = player_input()
if computer == player:
    print("Wow! That's a tie.")

elif computer == "rock":
    if player == "paper":
        print("You won!")
    else:
        print("You lost!")
elif computer == "paper":
    if player == "scissor":
        print("You won!")
    else:
        print("You lose!")
elif computer == "scissor":
    if player == "rock":
        print("You won!")
    else:
        print("You lose!")
else:
    print("There's some issue.. Please enter your choice again...")
    player_input()

print("Computer chose", computer)