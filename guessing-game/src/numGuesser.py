# Guessing Game with 3 choices to guess the correct number.

import random
print("Welcome to guessing game")
print("In this game you have 3 chances to guess the number correctly.")
play = input("Would you like to play the game? ")

if play.lower() not in ['yes', 'y', '1']:
    quit()

# Generated Random Number within the range
genNum = random.randint(1, 10)
chance = 1

while True:
    chance += 1
    guessNum = int(input("Enter the guess number : "))
    if guessNum == genNum:
        print("Your guess is correct! Congrats!")
        break
    if chance == 4:
        print("Sorry. Better luck next time.")
        break
    else:
        print("Wrong! Guess again")