#IMPORTANT!# Do not replace the URLS in the requests! This will cause it to run code, that it isn't supposed to!
import rich, os, requests
from rich import print as rprint
#imports modules
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    #sees what the current system is, so it can clear screen
def test_connection():
    try:
        requests.get("https://8.8.8.8", timeout=3)
        return True
    except(requests.ConnectionError, requests.Timeout) as e:
        return False
    #this pings 8.8.8.8, and if it can it will return True. See later use at line 28 for more explaination
#intro#
while True:
    rprint("[red]Welcome to my Python Examples!")
    rprint("[blue]By DeanTA217!")
    rprint("[green]Please enter one of the numbers below!")
    rprint("[yellow]Make sure you have an active internet connection!\nThis launcher gets the other scripts from GitHub to run them!")
    #numbers#
    rprint("[purple][1] Age Calculator")
    rprint("[purple][2] Binary To Decimal Converter")
    rprint("[purple][3] Yes Or No Basic Prompt")
    #script running#
    while True:
        script = input("Enter the number of the script you would like to run.\n")
        #asks for script number
        test_connection()
        #runs the funciton definied earlier
        if test_connection:
            #it will run this if True is returned earlier.
            print("[green]Connected!")
        else:
            #if false is returned, this will run.
            print("[yellow]You must be connected to the internet!\nPlease try again later when connected.")
            exit()
        if not script.isdigit():
            rprint("[yellow]Enter a number from the list above.")
            #makes sure it is a number
            continue
            #resets loop
        else:
            if not int(script) <= 3:
                rprint("[yellow]Enter a number from the list above.")
                #makes sure it is a number from the list above
                continue
            else:
                break
                #breaks out of loop
    script_int = int(script)
    #converts variable script into a integer variable named script_int
    clear_screen()
    #runs function from earlier to clear screen
    if script_int == 1:
        response = requests.get("https://raw.githubusercontent.com/deanta217/python-examples/main/InteractiveScripts/age.py")
        exec(response.text)
        #runs a text version of the response above.
    elif script_int == 2:
        response = requests.get("https://raw.githubusercontent.com/deanta217/python-examples/main/InteractiveScripts/binary2decimal.py")
        exec(response.text)
    elif script_int == 3:
        response = requests.get("https://raw.githubusercontent.com/deanta217/python-examples/main/InteractiveScripts/y_or_n.py")
        exec(response.text)
    clear_screen()
    rprint("[red]Welcome to my Python Examples!")
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