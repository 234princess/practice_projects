import random


def guessing_game() :
    computer_choice = random.randint(1,100)
    #print(computer_choice)
    while True:
        user_choice = int(input("Guess my number! Hint: It's between 1 and 100\n"))
        
        if user_choice < 1 or user_choice > 100:
            print("This number is out of the provided range, try again.")
        elif user_choice> computer_choice:
            print("Too high, try again")
        elif user_choice < computer_choice:
            print("Too low, try again")
        else:
            print("Just right, You win")
            break
    
guessing_game()