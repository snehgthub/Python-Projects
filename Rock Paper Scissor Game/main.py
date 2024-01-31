import random
from art import tprint

tprint("Rock    Paper    Scissor")

options = ['rock', 'paper', 'scissor']
user_win=0
computer_win=0

while True:
    user_input=input("\nType rock/paper/scissor or 'Q' to quit: ").lower()
    
    if user_input == 'q':
        break

    if user_input in options:
        random_num = random.randint(0,2)
        print("Computer chose", options[random_num])

        if user_input == options[random_num]:
            print("No result!")
        
        elif user_input == 'rock' and options[random_num] == 'scissor':
            print("You won!")
            user_win+=1
        
        elif user_input == 'paper' and options[random_num] == 'rock':
            print("You won!")
            user_win+=1
        
        elif user_input == 'scissor' and options[random_num] == 'paper':
            print("You won!")
            user_win+=1
        
        else:
            print("You lost!")
            computer_win+=1
            continue

print("\nUser won the game", user_win, "times.")
print("Computer won the game", computer_win, "times.")