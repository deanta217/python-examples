#to run this you must download the entire repository.
import rich, os
from rich import print as rprint
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#intro#
while True:
    rprint("[red]Welcome to my Python Examples!")
    rprint("[blue]By DeanTA217!")
    rprint("[green]Please enter one of the numbers below!")
    #numbers#
    rprint("[purple][1] Age Calculator")
    rprint("[purple][2] Binary To Decimal Converter")
    rprint("[purple][3] Yes Or No Basic Prompt")
    #script running#
    while True:
        script = input("Enter the number of the script you would like to run.\n")
        if not script.isdigit():
            rprint("[yellow]Enter a number from the list above.")
            continue
        else:
            if not int(script) <= 3:
                rprint("[yellow]Enter a number from the list above.")
                continue
            else:
                break
    script_int = int(script)
    clear_screen()
    if script_int == 1:
        exec(open("./InteractiveScripts/age.py").read())
    elif script_int == 2:
        exec(open("./InteractiveScripts/binary2decimal.py").read())
    elif script_int == 3:
        exec(open("./InteractiveScripts/y_or_n.py").read())
    clear_screen()
    keep = input("Would you like to run another script? (Y/N)\n")
    clear_screen()
    while True:
        if keep.upper() == "Y":
            break
        elif keep.upper() == "N":
            quit()
        else:
            print("Answer Y or N")
    continue