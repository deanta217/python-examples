import sys, rich
from rich import print as rprint
print("Welcome!\nThis script will convert binary to decimal!")
while True:
    binary = input("Enter your binary string.\n")
    if not binary.isdigit():
        print("Enter a number.\n")
        continue
    decimal = int(binary, 2)
    #converts input to decimal. 2 represents the base.
    print("Your decimal is {}".format(decimal))
    while True:
        rprint("[yellow]If this is running through the launcher, this doesn't work. I am currently looking for a fix.")
        convertmore = input("Would you like to convert another binary string? (Y/N)\n")
        if convertmore.upper() == "Y":
            break
        elif convertmore.upper() == "N":
           print("Goodbye.")
           quit()
           #ends program
        else:
           print("Enter Y or N.\n")