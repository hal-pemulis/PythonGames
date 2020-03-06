import random

selections = ["r", "p", "s"]

play_again = 0
user_pick = ""
comp_pick = ""

while play_again < 5:

    user_pick = input("Rock, paper, or scissors?   ")
    comp_pick = random.choice(selections)

    if user_pick == "r" and comp_pick == "p":
        print("The computer picked Paper. You lose!")
    elif user_pick == "r" and comp_pick == "s":
        print("The computer pickeds scissors. You win!")
    elif user_pick == "p" and comp_pick == "s":
        print("The computer picked scissors. You lose!")
    elif user_pick == "p" and comp_pick == "r":
        print("The computer picked Rock. You win!")
    elif user_pick == "s" and comp_pick == "r":
        print("The computer picked Rock. You lose!")
    elif user_pick == "s" and comp_pick == "p":
        print("The computer picked Paper. You win!")
    elif user_pick == comp_pick:
        print(f"You both selected {user_pick}. It's a tie!")
    else:
        print("Please make a valid selection.")

    play_again += 1
    user_pick = ""
    comp_pick = ""

else:
    break
