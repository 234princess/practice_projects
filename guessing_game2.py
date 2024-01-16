import random


def guessing_game() :
    computer_choice = random.randint(1,100)
    #print(computer_choice)

    tries = 3

    while tries > 0:
        user_choice = int(input("Guess my number! Hint: It's between 1 and 100\n"))
        
        if user_choice < 1 or user_choice > 100:
            print("This number is out of the provided range, try again.")
            tries -= 1
        elif user_choice> computer_choice:
            print("Too high, try again")
            tries -= 1
        elif user_choice < computer_choice:
            print("Too low, try again")
            tries -= 1
        else:
            print("Just right, You win")
            break
    if tries == 0:
        print("Sorry you have run out of try's, you lose!")
    
guessing_game()
