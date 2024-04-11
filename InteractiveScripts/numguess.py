import rich, sys, os, playsound, random
from rich import print as rprint
def intro():
    rprint("[red]Number Guesser!")
    rprint("[blue]Guess the number I'm thinking of between 1 and 100!\nYou get 10 guesses!")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
answer = random.randint(1,100)
attempts = 0
clear_screen()
intro()
print(answer)
while True:
    guess = input()
    if not guess.isdigit:
        clear_screen()
        rprint("[yellow]Enter a number!")
        continue
    if int(guess) == answer:
        clear_screen()
        attempts = attempts+1
        rprint("[green]Good Job! You guessed the number {}!\n".format(answer),"[green]It took you {} attempts!".format(attempts))
        sys.exit()
    else:
        clear_screen()
        if int(guess) > answer and int(attempts) <= 9:
            rprint("[red]Smaller")
            attempts = attempts+1
        elif int(guess) < answer and int(attempts) <= 9:
            rprint("[red]Bigger.")
            attempts = attempts+1
        else:
            rprint("[red]You ran out of guesses. The correct answer is {}.".format(answer))
            sys.exit()
    rprint("[yellow]You have used {} guesses.".format(attempts))
        
