import random

choices = ["rock", "paper", "scissors"]

comp_choice=  random.choice(choices)
print("welcome to the rock, paper scissors game")

user_choice = input('Please enter your choice(rock/ paper/ scissors):  ').lower()

# displaying what user and comp chose
if (user_choice in choices):
    print("Your choice:", user_choice)
    print("Comp choice", comp_choice)
    
    if user_choice == comp_choice:
        print("its a tie")
    elif(
        (user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "paper" and comp_choice == "rock") or
        (user_choice == "scissors" and comp_choice == "paper")
          ):
        print("Congratulations You win!!!")
    else:
        print("computer wins")
        
else:
    print("Invalid choice, Try again ")
        
