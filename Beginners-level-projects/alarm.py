from playsound import playsound
import time

#ANSI escape codes:
# \033 is the escape character (ESC).
# 2J tells the terminal: clear the entire screen.
# H moves the cursor back to the top-left corner (row 0, column 0).
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed=0
    print(CLEAR)

    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left=seconds-time_elapsed     
        minutes_left=time_left//60 #integer division
        seconds_left= time_left%60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in : {minutes_left:02d} : {seconds_left:02d}")
        
    playsound("alarm.wav")

minutes=int(input("How many minutes to wait : "))
seconds=int(input('How many seconds to wait : '))
total_seconds= minutes*60 + seconds
alarm(total_seconds)