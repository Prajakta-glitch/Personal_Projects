import random

score=0

while(1):
    options=["rock","paper","scissor"]
    print("Your options:",options)
    user=input("Choose from the given options:").lower()

    computer=random.choice(options)
    print("Computer chose:",computer)

    if user not in options:
        print("Choose from the given options!")
        print("Your score:",score)
    elif((computer=="rock" and user=="paper")or(computer=="paper" and user=="scissor")or(computer=="scissor" and user=="rock")):
        print("You win!")
        score+=1
        print("Your score:",score)
    elif(computer==user):
        print("Draw!")
        print("Your score:",score)
    else:
        print("You Lose!")
        print("Your score:",score)
    
    choice=int(input("Do you want to continue? If yes Press 1 else 0: "))
    if(choice==0):
        break