import random
import sys

a = 0
while a == 0:

    level = input("Level: ")
    try:
        number = random.randint(1, int(level))
        a = a + 1
    except ValueError:
        a = 0

while True:

    guess = input("Guess: ")
    if int(guess) == number:
        print("Just right!")
        sys.exit()

    if int(guess) < number:
        print("Too small!")

    if int(guess) > number:
        print("Too large!")
