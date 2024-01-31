import os
import sys
import random
import time
from termcolor import colored
from logo import logo_text

def clear():
    os.system("clear")


def rules():
    print(colored("Objective: ",'cyan'))
    print("Guess the secret number correctly within a limited number of attempts.\n")

    print(colored("Setup: ",'cyan'))
    print("Select Difficulty Level: The range for each level is 1-50. The number of attempts varies by difficulty:")
    print("• Easy: 10 attempts.")
    print("• Medium: 5 attempts.")
    print("• Hard: 3 attempts.\n")

    print(colored("Game Play: ",'cyan'))
    print("1. Start the Game: After selecting the difficulty level, the game will generate a random number within the range of 1-50.")
    print("2. Enter Your Guess: Input your guess for the number and submit it.")
    print("3. Feedback: After each guess, the game will inform you if your guess is too high, too low, or correct.\n")

    print(colored("Rules: ",'cyan'))
    print("1. Each guess must be a number within the range of 1-50.")
    print("2. You will receive feedback after each guess to help guide your next guess.")
    print("3. The number of guesses is limited based on the difficulty level chosen at the start of the game.\n")

    print(colored("Winning: ",'cyan'))
    print("• You win the game by guessing the correct number within the allowed number of attempts for your chosen difficulty level.\n")

    print(colored("Losing: ",'cyan'))
    print("• If you fail to guess the number within the allotted attempts, the game ends and the correct number is revealed.\n")


def confirmation(conf_type: str):
    
    confirmation_msg = ["\nProceed with the game? (",
                    "\n\nAre you ready? ("]
    
    if conf_type == 'start':
        print(colored(confirmation_msg[0],'yellow'),end='')

    elif conf_type == 'ready':
        print(colored(confirmation_msg[1],'yellow'),end='')

    else:
        print(colored("Invalid Confirmation Input!!", 'red'))
        quit()

    print(colored("Y",'green'),end='')
    print(colored("/",'yellow'),end='')
    print(colored("N",'red'),end='')
    print(colored(") ",'yellow'),end='')

    if conf_type == 'start':
        confirmation_start=input()

        if confirmation_start.lower() != 'y':
            print()
            quit()
    else:
        confirmation_ready=input()

        if confirmation_ready.lower() != 'y':
            print()
            quit()


def choose_difficulty():

    print(colored("Difficulty levels: ",'yellow'))
    print(colored("• Easy",'green'))
    print(colored("• Medium",'red'))
    print(colored("• Hard\n",'magenta'))

    print(colored("Press ",'yellow'),end='')
    print("(",end='')
    print(colored("E",'green'),end='')
    print(")",end='')
    print(colored("asy, ",'yellow'),end='')
    print("(",end='')
    print(colored("M",'red'),end='')
    print(")",end='')
    print(colored("edium or ",'yellow'),end='')
    print("(",end='')
    print(colored("H",'magenta'),end='')
    print(")",end='')
    print(colored("ard for choosing difficulty level: ",'yellow'),end='')

    level = input()

    if level.upper() == 'E': 
        print(colored("\nYou chose ", 'yellow'),end='')
        print(colored("'Easy' ",'green'),end='')
        print(colored("level. So you'll have ",'yellow'),end='')
        print(colored("'10 chances'",'green'),end='')
        print(colored(" to guess the number.",'yellow'),end='')
        total_chances=10

    elif level.upper() == 'M': 
        print(colored("\nYou chose ", 'yellow'),end='')
        print(colored("'Medium' ",'red'),end='')
        print(colored("level. So you'll have ",'yellow'),end='')
        print(colored("'5 chances'",'red'),end='')
        print(colored(" to guess the number.",'yellow'),end='')
        total_chances=5

    elif level.upper() == 'H':
        print(colored("\nYou chose ", 'yellow'),end='')
        print(colored("'Hard' ",'magenta'),end='')
        print(colored("level. So you'll have ",'yellow'),end='')
        print(colored("'3 chances'",'magenta'),end='')
        print(colored(" to guess the number.",'yellow'),end='')
        total_chances=3

    else:
        print(colored("\nInvalid Input. Please try again!\n", 'red'))
        quit()
    
    return total_chances


def number_guesser(total_chances:int, guessed: bool, guess_count: int):

    random_num = random.randint(1,int(top_range))
    guess_prompts = [
        "Let's start! Your guess? ",
        "Not quite, try again: ",
        "Missed! Another go: ",
        "Oops, guess once more: ",
        "Still not right, guess again: ",
        "Halfway there! Your next guess? ",
        "Close but not yet, try again: ",
        "Only a few tries left, guess: ",
        "Almost there, think carefully: ",
        "Last chance! Your guess? "
    ]

    for i in range(total_chances):

        user_guess = input(colored("\n"+guess_prompts[i],'yellow'))
        guess_count+=1

        if not user_guess.isdigit():
            print(colored("\nPlease enter a valid number!!",'red'))
            continue

        user_guess=int(user_guess)
        
        if user_guess == random_num:
            print(colored("• Correct! You did it!",'green'))
            guessed=True
            break

        elif user_guess > random_num:
            print(colored("• You are above the number!",'cyan'))
            print(colored(f"• Guesses left: {total_chances-i-1}",'magenta'))

        else:
            print(colored("• You are below the number!", 'cyan'))
            print(colored(f"• Guesses left: {total_chances-i-1}",'magenta'))

    if guessed:
        print(colored("\nYou guessed the number in",'yellow'),end=' ')
        print(colored(str(guess_count),'blue'),end=' ')
        print(colored("tries!\n",'yellow'))
        time.sleep(4)
    else:
        print(colored("\nAllowed Chances Exceeded!!\nThe number was",'yellow'),end=' ')
        print(colored("'"+str(random_num)+"'", 'blue'),end='')
        print(colored(".",'yellow'))
        time.sleep(2)

def animate_message(message, color, total_dots=3, duration=1):
    for i in range(total_dots + 1):
        colored_message = colored(text=message + "." * i, color=color)
        sys.stdout.write("\r" + colored_message)
        sys.stdout.flush()
        time.sleep(duration / total_dots)
    print()

def game_over():
    clear()
    logo_text("Game", "Over!", "RED", "RED")

    animate_message("Quitting", color="red", total_dots=3, duration=2)



if __name__ == "__main__":
    total_chances=0
    hasGuessed=False
    guess_count=0
    top_range = 50

    clear()
    logo_text("Number", "Guesser")
    rules()
    confirmation('start')    

    clear()
    logo_text("Number", "Guesser")
    total_chances = choose_difficulty()
    confirmation('ready')

    clear()
    logo_text("Number", "Guesser")
    number_guesser(total_chances, hasGuessed, guess_count)
    game_over()