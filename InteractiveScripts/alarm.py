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
        hours = int(input("How many hours?\n"))
        if hours > 0:
            break
        else:
            clear_screen()
            rprint("[yellow]You cannot have negative hours!")
            continue
    clear_screen()
    while True:
        minutes = int(input("How many minutess\n"))
        if minutes > 0:
            break
        else:
            clear_screen()
            rprint("[yellow]You cannot have negative minutes!")
            continue
    clear_screen()
    while True:
        seconds = int(input("How many seconds?"))
        if seconds > 0:
            break
        else:
            clear_screen()
            rprint("[yellow]You cannot have negative seconds!")
            continue        
    if hours + minutes + seconds == 0:
        rprint("[yellow]A timer must be at minimum 1 second.")

playsound.playsound("/Users/deant/repos/python-examples/InteractiveScripts/alarm/alarm.mp3")