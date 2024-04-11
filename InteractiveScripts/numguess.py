import rich, sys, os, playsound, random
from rich import print as rprint
def intro():
    rprint("[red]Number Guesser!")
    rprint("[blue]Guess the number I'm thinking of between 1 and 100!")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
answer = random.randint(1,100)
attempts = 0
intro()
while True:
    guess = input()
    if not guess.isdigit:
        clear_screen()
        rprint("[yellow]Enter a number!")
        continue
    if guess == answer:
        clear_screen()
        rprint("[green]Good Job! You guessed the number {}!\n".format(answer),"[green]It took you {} attempts!".format(attempts))
        sys.exit()
    else:
        clear_screen()
        if str(guess) > answer:
            rprint("[red]Smaller")
            attempts = attempts+1
            continue
        