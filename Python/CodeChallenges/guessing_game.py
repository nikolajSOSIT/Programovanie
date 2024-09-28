import random

def guessing_game():
    number = random.randint(1, 100)
    guess = 0
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Just right!")
    
guessing_game()

