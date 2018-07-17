import random

die = [1,2,3,4,5,6]
r = input("Would you like to roll a die? Y/N: ");
#Main body to roll die
def roll():
    try:
        if (r == "Y" or r == "y"):
            print(random.choice(die))

        elif (r=="N" or r=="n"):
            print("Goodbye")
            exit()
    except:
        exit()
    again()
#Second body to try again
def again():
    try:
        rollagain = input("Would you like to roll again? Y/N: ")
        if (rollagain == "Y" or rollagain =="y"):
            roll()

        elif (rollagain == "N" or rollagain=="n"):
            print("Goodbye")
            exit()

    except:
        exit()
roll()
