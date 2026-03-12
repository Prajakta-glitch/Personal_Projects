import random

print("Number Guessing Game")
print("Type 'exit' anytime you want to quit.")

number=random.randint(1,100)
while True:
    guess=input("Guess a number between 1 to 100: ")
    if guess.lower()=="exit":
        print("Thanks for playing")
        break
    guess=int(guess)
    if guess<number:
        print("Too low! Try again.")
    elif guess>number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number.")
        number=random.randint(1,100)