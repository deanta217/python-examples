#setup#
import os, rich, playsound, time
from rich import print as rprint
#functions#
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#start menu#
rprint("[blue]Welcome!\nThis alarm is writen entirely in python!")
rprint("[yellow]Enter any character when you're ready to start!")
input()
#empty input so it waits until a character is inputted.
clear_screen()
#alarm config#
while True:
    while True:
        hours = input("How many hours?\n")
        if not hours.isdigit():
            clear_screen()
            rprint("[yellow]You must enter a digit!")
            continue
        else:
            break
    clear_screen()
    while True:
        minutes = input("How many minutes\n")
        if not minutes.isdigit():
            clear_screen()
            rprint("[yellow]You must enter a digit!")
            continue
        else:
            break
    clear_screen()
    while True:
        seconds = input("How many seconds?\n")
        if not seconds.isdigit():
            clear_screen()
            rprint("[yellow]You must enter a digit!")
            continue
        else:
            break
    if int(hours) + int(minutes) + int(seconds) == 0:
        rprint("[yellow]A timer must be at minimum 1 second.")
        continue
    else:
        print("Timer is >= 1 second! Good")
        break
clear_screen
hour_int = int(hours)
minute_int = int(minutes)
second_int = int(seconds)
while True:
    print(str(hour_int) + ":" + str(minute_int) + ":" + str(second_int))
    time.sleep(1)
    second_int=second_int-1
    if second_int == -1:
        second_int = 59
        minute_int = minute_int-1
        if minute_int == -1:
            minute_int = 59
            hour_int = hour_int-1
            if hour_int == -1:
                hour_int = 0
                minute_int = 0
                second_int = 0
                break
    clear_screen()
clear_screen()
print("Timer Done")
playsound.playsound("/Users/deant/repos/python-examples/InteractiveScripts/timer/timer.mp3")
clear_screen()
while True:
    time.sleep(0.5)
    print("Timer Done")
    time.sleep(0.5)
    clear_screen()