# Alarm Clock mini project

from playsound import playsound as ps
import time


# Code to clearing terminal
CLEAR = "\033[2J" # Clears terminal
CLEAR_AND_RETURN = "\033[H" # Clears terminal after every new line is executed


# Alarm Function
def alarm(sec):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < sec:
        time.sleep(1)
        time_elapsed += 1

        time_left = sec - time_elapsed
        minutes_left = time_left // 60
        sec_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d} : {sec_left :02d}")
    ps("ringtone.mp3")

minutes = int(input("How many minutes to wait? : "))
seconds = int(input("How many seconds to wait? : "))
total_seconds = (minutes * 60) + seconds
alarm(total_seconds)
