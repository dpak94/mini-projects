# A Basic Geography Quiz Program

# Importing time module
import time

print("Hello and welcome to Geography Quiz")
play = input("Would you like to play the quiz? ").lower()


if play not in ['yes', 'y', '1']:
    quit()

score = 0

print("Alright, here's the first question :")

# Q&A Section
answer = input("Name the capital of Australia? ")
if answer.lower() == "canberra":
    score += 1
    print("Correct! Next question :")
else:
    print("Wrong! Next question :")

time.sleep(2)

answer = input("On which continent is River Nile located? ")
if answer.lower() == "africa":
    print("Correct! Next question :")
    score += 1
else:
    print("Wrong! Next question :")

time.sleep(2)

answer = input("Name the most populous country in the world ? ")
if answer.lower() == "india":
    print("Correct!")
    score += 1
else:
    print("Wrong! ")

time.sleep(2)

# Final Score printout
print("Your total score is :", score)
if score < 3:
    print("Better luck next time.")
else:
    print("Well Played!")