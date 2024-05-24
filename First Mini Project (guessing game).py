import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q) :")
    if (userChoice == "Q"):
        break
    
    userChoice = int(userChoice)
    if (userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif (userChoice > target):
        print("your number is too big.\nTRY AGAIN")
    else:
        print("your number is too small.\nTRY AGAIN")

print("-----GAME OVER----")