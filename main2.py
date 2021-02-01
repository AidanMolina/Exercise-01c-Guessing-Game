#!/usr/bin/env python3
import sys
import random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

number = random.randrange(1,11)
guess = input("Guess a number from 1 to 10: ")

try:
    guess = int(guess) 
except ValueError:
    print("That's not a number")
    exit()

if guess == number: 
    print("Great job! You got it!")   
elif guess != number: 
    print("Sorry, better luck next time.") 
    print("The number was " + str(number))

