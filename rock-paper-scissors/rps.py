import random, time


user_wins  = 0
comp_wins = 0
choice_list = ['rock', 'paper', 'scissors']

print("Welcome to the game of Rock Paper Scissors!!!")
print("Would you like to participate?")
play = input().lower()

if play not in ['y', 'yes', '1']:
    quit()

while True:
    user_prompt = input("Rock/Paper/Scissors?").lower()
    if user_prompt == "q":
        break

    if user_prompt not in choice_list:
        print("Enter valid input")
        continue

    compPick = choice_list[random.randint(0, 2)]
    # Rock : 0, Paper : 1, Scissors : 2
    print("Computer chose " + compPick +"!")

    if user_prompt == "rock" and compPick == "scissors":
        print("You win!")
        user_wins += 1
        continue
    elif user_prompt == "paper" and compPick == "rock":
        print("You win!")
        user_wins += 1
        continue 
    elif user_prompt == "scissors" and compPick == "paper":
        print("You win!")
        user_wins += 1
        continue
    else:
        comp_wins += 1
        print("Computer wins!")

if user_wins > comp_wins:
    print("You are the winner!")
else:
    print("Computer is the winner!")
time.sleep(1.5)
print("Adios!")