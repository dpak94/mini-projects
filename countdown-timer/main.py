import time

CLEAR = "\033[2J" # Clears terminal
CLEAR_AND_RETURN = "\033[H" # Clears terminal after every new line is executed

my_time = int(input("Enter the time in seconds: "))

print(CLEAR)
for x in reversed(range(1, my_time + 1)):
    print(CLEAR_AND_RETURN)
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)

print("Time's up!")