#setup#
import os, rich, playsound
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
        seconds = input("How many seconds?")
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
hour_int = int(hour)
playsound.playsound("/Users/deant/repos/python-examples/InteractiveScripts/alarm/alarm.mp3")