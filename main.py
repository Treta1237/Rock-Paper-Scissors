import random

player = input("What is your choice? 'r' for rock, 'p' for paper and 's' for scissors ")
player = player.lower()

computer = random.choice(['r', 'p', 's'])

if computer == player:
    r = "rock"
    p = "paper"
    s = "scissors"
    print("You have both chosen " + player + ". It's a tie")

elif computer == 'r' and player == 'p':
    print("You have chosen paper and the computer has chosen rock. You win!")

elif computer == 'r' and player == 's':
    print("You have chosen scissors and the computer has chosen rock. You lose!")

elif computer == 'p' and player == 'r':
    print("You have chosen rock and the computer has chosen paper. You lose!")

elif computer == 'p' and player == 's':
    print("You have chosen scissors and the computer has chosen paper. You win!")

elif computer == 's' and player == 'p':
    print("You have chosen paper and the computer has chosen scissors. You lose!")

elif computer == 's' and player == 'r':
    print("You have chosen rock and the computer has chosen paper. You win!")

else:
    print("I brought the paper and the scissors, seems you brought the rocks in your head.")