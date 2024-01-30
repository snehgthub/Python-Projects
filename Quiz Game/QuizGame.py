import os
from art import tprint

pathToFile=os.path.dirname(__file__)
correct=0
iter=0

tprint("Welcome   to   Computer   Quiz!")
user_choice=input("Do you want to play? ")

if user_choice.lower() != "yes":
    quit()
else:
    print("Okay! Let's play :)\n")

try:
    with open(pathToFile+"/QuizQuestions.txt",'r') as questFile, open(pathToFile+"/QuizAnswers.txt",'r') as ansFile:

        questions = questFile.read().split('\n')
        answers = ansFile.read().split('\n')
        
        for question in questions:
            print(f"Question {iter}:", end=" ")
            userAnswer = input(question)
           
            if userAnswer.lower() == answers[iter]:
                print("Correct!\n")
                correct+=1
            else:
                print("Incorrect!\n")

            iter+=1
            
except:
    print("\nSomething Went Wrong!")

print("Your Score is",str(correct)+"/4")
print("Your got",str((correct/4)*100)+"%")