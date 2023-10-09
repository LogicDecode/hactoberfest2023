import random

list = ["snake", "water", "gun"]
print("         Welcome to Game            ")
print("you have 5 chances")
chances = 5
while chances != 0:
    choice=random.choice(list)
    a=input("\nEnter your choice from snake, water or gun: ")
    if (a=="snake" and choice=="water"):
        print("Congratulation You won i had choosed ",choice)
    elif (a=="snake" and choice=="gun"):
        print("You lost i had choosed ", choice)
    elif (a=="gun" and choice=="water"):
        print(" You lost i had choosed ", choice)
    elif (a=="gun" and choice=="snake"):
         print("Congratulation You won i had choosed ",choice)
    elif (a=="water" and choice=="gun"):
         print("Congratulation You won i had choosed ",choice)
    elif (a=="water" and choice=="snake"):
        print("You lost i had choosed ",choice)
    else:
          print("OOPS! it's a tie")
    chances -= 1

