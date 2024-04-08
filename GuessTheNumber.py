import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('guess the number!', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])










print("Welcome to the number guess game!")
print("Enter your name.")
name = input()
print("Hello", name)
print("I have chosen a number between 1 and 20.")
print("Can you guess it?")
print("You have 3 tries.")

import random

def play_game():

    number = random.randint(1, 20)
    for i in range(3):
        print("Enter your guess.")
        guess = int(input())
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break

    if guess == number:
        print("Congratulations! You guessed the number in", i+1, "tries.")
    else:
        print("Sorry. The number I chose was", number)
    print("The game is over.")
    play_again()

def play_again():
    print("Play again?")
    print("Enter yes or no.")
    answer = input().lower()  
    if answer == "YES" or answer == "y":
        play_game()  
    else:
        print("Goodbye!")

play_game()  
